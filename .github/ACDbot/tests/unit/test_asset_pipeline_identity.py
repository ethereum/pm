"""Tests for artifact identity in the asset pipeline."""

import importlib.util
import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


ACDBOT_DIR = Path(__file__).resolve().parents[2]
ASSET_PIPELINE_DIR = ACDBOT_DIR / "scripts" / "asset_pipeline"
MODULES_DIR = ACDBOT_DIR / "modules"


def load_asset_pipeline_module(module_name: str):
    os.environ.setdefault("ZOOM_CLIENT_ID", "test-client-id")
    os.environ.setdefault("ZOOM_CLIENT_SECRET", "test-client-secret")
    os.environ.setdefault("ZOOM_REFRESH_TOKEN", "test-refresh-token")

    for path in (str(ASSET_PIPELINE_DIR), str(MODULES_DIR)):
        if path not in sys.path:
            sys.path.insert(0, path)

    module_path = ASSET_PIPELINE_DIR / f"{module_name}.py"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_single_occurrence_mapping(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "sample": {
                    "meeting_id": "83343889436",
                    "occurrences": [
                        {
                            "issue_number": 1001,
                            "issue_title": "Sample Call #1, May 20, 2026",
                            "start_time": "2026-05-20T15:30:00Z",
                            "occurrence_number": 1,
                            "youtube_video_id": "sampleVideoId",
                        },
                    ],
                },
            },
        ),
        encoding="utf-8",
    )


def write_same_day_mapping(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "sample": {
                    "meeting_id": "84600001111",
                    "occurrences": [
                        {
                            "issue_number": 1037,
                            "issue_title": "Sample Call #37 | May 19 2025",
                            "start_time": "2025-05-19T14:00:00Z",
                            "occurrence_number": 5,
                        },
                        {
                            "issue_number": 1038,
                            "issue_title": "Sample Call #38 | May 19 2025",
                            "start_time": "2025-05-19T14:00:00Z",
                            "occurrence_number": 6,
                        },
                    ],
                },
            },
        ),
        encoding="utf-8",
    )


def test_public_call_number_uses_explicit_title_number_before_occurrence_number():
    meeting_identity = load_asset_pipeline_module("meeting_identity")

    assert meeting_identity.get_occurrence_call_number(
        {
            "issue_title": "Sample Meeting 116 | May 21, 2025",
            "occurrence_number": 1,
        }
    ) == 116
    assert meeting_identity.get_occurrence_call_number(
        {
            "issue_title": "Sample Office Hour Meeting 64 (Topic) | July 08, 2025",
            "occurrence_number": 1,
        }
    ) == 64
    assert meeting_identity.get_occurrence_call_number(
        {
            "issue_title": "Sample planning session, May 21, 2025",
            "occurrence_number": 7,
        }
    ) == 7
    assert meeting_identity.extract_public_call_number("Sample planning session, May 21, 2025") is None


def test_forced_target_resolution_returns_exact_occurrence_identity():
    resolve_forced_target = load_asset_pipeline_module("resolve_forced_target")

    target = resolve_forced_target.resolve_forced_target(
        {
            "sample": {
                "meeting_id": "84600001111",
                "occurrences": [
                    {
                        "issue_number": 1483,
                        "issue_title": "Sample Meeting 116 | May 21, 2025",
                        "start_time": "2025-05-21T14:00:00Z",
                        "occurrence_number": 1,
                    },
                ],
            },
        },
        "sample",
        116,
    )

    assert target == {
        "meeting_id": "84600001111",
        "issue_number": 1483,
        "date": "2025-05-21",
        "number": 116,
    }


def test_forced_target_resolution_rejects_duplicate_public_numbers():
    resolve_forced_target = load_asset_pipeline_module("resolve_forced_target")

    with pytest.raises(ValueError, match="Ambiguous mapped occurrences for sample #98"):
        resolve_forced_target.resolve_forced_target(
            {
                "sample": {
                    "meeting_id": "84600001111",
                    "occurrences": [
                        {
                            "issue_number": 1001,
                            "issue_title": "Sample Meeting 98, April 21, 2026",
                            "start_time": "2026-04-21T14:00:00Z",
                            "occurrence_number": 97,
                        },
                        {
                            "issue_number": 1002,
                            "issue_title": "Sample Call 98, May 05, 2026",
                            "start_time": "2026-05-05T14:00:00Z",
                            "occurrence_number": 98,
                        },
                    ],
                },
            },
            "sample",
            98,
        )


def test_date_ingestion_ignores_recordings_outside_mapped_meeting_ids(tmp_path, monkeypatch):
    download_zoom_assets = load_asset_pipeline_module("download_zoom_assets")

    mapping_path = tmp_path / "meeting_topic_mapping.json"
    write_single_occurrence_mapping(mapping_path)
    monkeypatch.setattr(download_zoom_assets, "MAPPING_FILE_PATH", mapping_path)
    monkeypatch.setattr(download_zoom_assets, "ARTIFACTS_DIR", tmp_path / "artifacts")

    monkeypatch.setattr(download_zoom_assets.zoom, "get_past_meeting_instances", lambda meeting_id: [])
    monkeypatch.setattr(
        download_zoom_assets.zoom,
        "get_recordings_for_date",
        lambda date: [
            {
                "uuid": "outside-mapped-meeting",
                "start_time": "2026-05-20T15:30:00Z",
                "duration": 69,
                "topic": "Sample Call #1, May 20, 2026",
                "recording_files": [
                    {"file_type": "CHAT", "download_url": "https://example.test/outside-chat.txt"},
                ],
            },
        ],
    )
    monkeypatch.setattr(
        download_zoom_assets,
        "download_file",
        lambda url, token, path: path.write_text(url, encoding="utf-8") > 0,
    )

    download_zoom_assets.process_meeting_by_date(
        "sample",
        "2026-05-20",
        "test-token",
        min_duration_minutes=10,
    )

    assert not (tmp_path / "artifacts" / "sample").exists()


def test_artifact_directory_uses_mapped_occurrence_number(tmp_path, monkeypatch):
    download_zoom_assets = load_asset_pipeline_module("download_zoom_assets")

    artifacts_dir = tmp_path / "artifacts"
    monkeypatch.setattr(download_zoom_assets, "ARTIFACTS_DIR", artifacts_dir)
    monkeypatch.setattr(
        download_zoom_assets,
        "download_file",
        lambda url, token, path: path.write_text(url, encoding="utf-8") > 0,
    )

    download_zoom_assets.download_assets_for_meeting(
        {
            "uuid": "sample-recording",
            "start_time": "2026-05-20T15:30:00Z",
            "duration": 69,
            "topic": "Different Series Call #40, May 20, 2026",
            "recording_files": [
                {"file_type": "CHAT", "download_url": "https://example.test/chat.txt"},
            ],
        },
        "sample",
        "test-token",
        occurrence={
            "issue_number": 1001,
            "issue_title": "Sample Call #1, May 20, 2026",
            "start_time": "2026-05-20T15:30:00Z",
            "occurrence_number": 1,
        },
    )

    assert sorted(path.name for path in (artifacts_dir / "sample").iterdir()) == ["2026-05-20_001"]
    assert (artifacts_dir / "sample" / "2026-05-20_001" / "chat.txt").exists()
    assert (
        artifacts_dir / "sample" / "2026-05-20_001" / "chat.txt"
    ).read_text(encoding="utf-8") == "https://example.test/chat.txt"


def test_requested_number_selects_matching_same_day_occurrence(tmp_path, monkeypatch):
    download_zoom_assets = load_asset_pipeline_module("download_zoom_assets")

    mapping_path = tmp_path / "meeting_topic_mapping.json"
    artifacts_dir = tmp_path / "artifacts"
    write_same_day_mapping(mapping_path)
    monkeypatch.setattr(download_zoom_assets, "MAPPING_FILE_PATH", mapping_path)
    monkeypatch.setattr(download_zoom_assets, "ARTIFACTS_DIR", artifacts_dir)
    monkeypatch.setattr(
        download_zoom_assets.zoom,
        "get_past_meeting_instances",
        lambda meeting_id: [
            {"uuid": "sample-37-recording", "start_time": "2025-05-19T14:00:00Z"},
            {"uuid": "sample-38-recording", "start_time": "2025-05-19T14:00:00Z"},
        ],
    )
    recordings = {
        "sample-37-recording": {
            "uuid": "sample-37-recording",
            "start_time": "2025-05-19T14:00:00Z",
            "duration": 60,
            "topic": "Sample Call #37 | May 19 2025",
            "recording_files": [
                {"file_type": "CHAT", "download_url": "https://example.test/sample-37-chat.txt"},
            ],
        },
        "sample-38-recording": {
            "uuid": "sample-38-recording",
            "start_time": "2025-05-19T14:00:00Z",
            "duration": 60,
            "topic": "Sample Call #38 | May 19 2025",
            "recording_files": [
                {"file_type": "CHAT", "download_url": "https://example.test/sample-38-chat.txt"},
            ],
        },
    }
    monkeypatch.setattr(
        download_zoom_assets.zoom,
        "get_meeting_recording",
        lambda uuid: recordings[uuid],
    )
    monkeypatch.setattr(
        download_zoom_assets,
        "download_file",
        lambda url, token, path: path.write_text(url, encoding="utf-8") > 0,
    )

    download_zoom_assets.process_meeting_by_date(
        "sample",
        "2025-05-19",
        "test-token",
        min_duration_minutes=10,
        requested_number=38,
    )

    assert (artifacts_dir / "sample" / "2025-05-19_038" / "chat.txt").exists()
    assert (
        artifacts_dir / "sample" / "2025-05-19_038" / "chat.txt"
    ).read_text(encoding="utf-8") == "https://example.test/sample-38-chat.txt"
    assert not (artifacts_dir / "sample" / "2025-05-19_037").exists()


def test_expected_number_rejects_single_recording_with_wrong_topic_number(tmp_path, monkeypatch):
    download_zoom_assets = load_asset_pipeline_module("download_zoom_assets")

    mapping_path = tmp_path / "meeting_topic_mapping.json"
    artifacts_dir = tmp_path / "artifacts"
    write_same_day_mapping(mapping_path)
    monkeypatch.setattr(download_zoom_assets, "MAPPING_FILE_PATH", mapping_path)
    monkeypatch.setattr(download_zoom_assets, "ARTIFACTS_DIR", artifacts_dir)
    monkeypatch.setattr(
        download_zoom_assets.zoom,
        "get_past_meeting_instances",
        lambda meeting_id: [{"uuid": "sample-37-recording", "start_time": "2025-05-19T14:00:00Z"}],
    )
    monkeypatch.setattr(
        download_zoom_assets.zoom,
        "get_meeting_recording",
        lambda uuid: {
            "uuid": uuid,
            "start_time": "2025-05-19T14:00:00Z",
            "duration": 60,
            "topic": "Sample Call #37 | May 19 2025",
            "recording_files": [
                {"file_type": "CHAT", "download_url": "https://example.test/sample-37-chat.txt"},
            ],
        },
    )
    monkeypatch.setattr(
        download_zoom_assets,
        "download_file",
        lambda *args, **kwargs: pytest.fail("wrong-number recording must not be downloaded"),
    )

    download_zoom_assets.process_meeting_by_date(
        "sample",
        "2025-05-19",
        "test-token",
        min_duration_minutes=10,
        requested_number=38,
    )

    assert not (artifacts_dir / "sample").exists()


def test_summary_generation_uses_directory_number_for_same_day_occurrences(tmp_path, monkeypatch):
    generate_summary = load_asset_pipeline_module("generate_summary")

    mapping_path = tmp_path / "meeting_topic_mapping.json"
    write_same_day_mapping(mapping_path)
    monkeypatch.setattr(generate_summary, "MAPPING_FILE", mapping_path)

    meeting_dir = tmp_path / "artifacts" / "sample" / "2025-05-19_038"
    meeting_dir.mkdir(parents=True)
    (meeting_dir / "transcript.vtt").write_text("WEBVTT\n\nSample transcript", encoding="utf-8")
    prompt_path = tmp_path / "summarize.md"
    prompt_path.write_text("Return JSON.", encoding="utf-8")

    fetched_issue_numbers = []
    prompts = []

    def fake_fetch_github_issue_agenda(issue_number):
        fetched_issue_numbers.append(issue_number)
        return f"Agenda for issue {issue_number}"

    class FakeMessages:
        def create(self, model, max_tokens, messages):
            prompts.append(messages[0]["content"])
            return SimpleNamespace(
                usage=SimpleNamespace(input_tokens=1, output_tokens=1),
                content=[SimpleNamespace(text='{"summary": "ok"}')],
            )

    class FakeAnthropic:
        def __init__(self):
            self.messages = FakeMessages()

    monkeypatch.setattr(generate_summary, "fetch_github_issue_agenda", fake_fetch_github_issue_agenda)
    monkeypatch.setattr(generate_summary, "get_example_summary", lambda call_type: "")
    monkeypatch.setattr(generate_summary, "VOCAB_FILE", tmp_path / "missing-vocab.yaml")
    monkeypatch.setattr(generate_summary, "calculate_cost", lambda model, usage: 0)
    monkeypatch.setattr(generate_summary.anthropic, "Anthropic", FakeAnthropic)

    assert generate_summary.generate_summary(
        meeting_dir,
        prompt_path,
        "sample",
        model="test-model",
    )
    assert fetched_issue_numbers == [1038]
    assert "Sample Call #38 | May 19 2025" in prompts[0]
    assert "Sample Call #37 | May 19 2025" not in prompts[0]
    assert json.loads((meeting_dir / "tldr.json").read_text(encoding="utf-8")) == {"summary": "ok"}


def test_manifest_rejects_numbered_artifact_without_mapped_occurrence(tmp_path, monkeypatch):
    generate_manifest = load_asset_pipeline_module("generate_manifest")

    artifacts_dir = tmp_path / "artifacts"
    correct_call = artifacts_dir / "sample" / "2026-05-20_001"
    wrong_call = artifacts_dir / "sample" / "2026-05-20_040"
    correct_call.mkdir(parents=True)
    wrong_call.mkdir(parents=True)
    (correct_call / "chat.txt").write_text("sample chat", encoding="utf-8")
    (wrong_call / "transcript.vtt").write_text("WEBVTT\n\nwrong transcript", encoding="utf-8")

    config_path = tmp_path / "call_series_config.yml"
    config_path.write_text(
        """
call_series:
  sample:
    display_name: "Sample Calls"
    youtube_playlist_id: "PLJqWcTqh_zKSample"
""",
        encoding="utf-8",
    )

    mapping_path = tmp_path / "meeting_topic_mapping.json"
    mapping_path.write_text(
        json.dumps(
            {
                "sample": {
                    "occurrences": [
                        {
                            "issue_number": 1001,
                            "issue_title": "Sample Call #1, May 20, 2026",
                            "start_time": "2026-05-20T15:30:00Z",
                            "occurrence_number": 1,
                            "youtube_video_id": "sampleVideoId",
                        },
                    ],
                },
            },
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(generate_manifest, "ARTIFACTS_DIR", artifacts_dir)
    monkeypatch.setattr(generate_manifest, "CALL_SERIES_CONFIG", config_path)
    monkeypatch.setattr(generate_manifest, "MAPPING_FILE", mapping_path)

    with pytest.raises(
        ValueError,
        match="artifact directory has no mapped occurrence: sample/2026-05-20_040",
    ):
        generate_manifest.generate_manifest()
