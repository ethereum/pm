"""Tests for asset pipeline orchestration target selection."""

import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest


ACDBOT_DIR = Path(__file__).resolve().parents[2]
ASSET_PIPELINE_DIR = ACDBOT_DIR / "scripts" / "asset_pipeline"


def load_run_pipeline_module():
    if str(ASSET_PIPELINE_DIR) not in sys.path:
        sys.path.insert(0, str(ASSET_PIPELINE_DIR))

    module_path = ASSET_PIPELINE_DIR / "run_pipeline.py"
    spec = importlib.util.spec_from_file_location("run_pipeline", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_mapping(path: Path, series: str, occurrences: list[dict]) -> None:
    path.write_text(
        json.dumps(
            {
                series: {
                    "meeting_id": "84600001111",
                    "occurrences": occurrences,
                },
            },
        ),
        encoding="utf-8",
    )


def write_complete_artifacts(call_dir: Path) -> None:
    call_dir.mkdir(parents=True, exist_ok=True)
    (call_dir / "transcript.vtt").write_text("WEBVTT\n", encoding="utf-8")
    (call_dir / "transcript_changelog.tsv").write_text(
        "original\tcorrected\tconfidence\n",
        encoding="utf-8",
    )
    (call_dir / "transcript_corrected.vtt").write_text("WEBVTT\n", encoding="utf-8")
    (call_dir / "tldr.json").write_text("{}", encoding="utf-8")


def test_recent_run_uses_newest_mapped_occurrence_not_existing_artifact(tmp_path, monkeypatch):
    run_pipeline = load_run_pipeline_module()

    mapping_path = tmp_path / "meeting_topic_mapping.json"
    artifacts_dir = tmp_path / "artifacts"
    write_mapping(
        mapping_path,
        "sample",
        [
            {
                "issue_title": "Sample Call #1",
                "start_time": "2026-05-19T15:00:00Z",
                "occurrence_number": 1,
            },
            {
                "issue_title": "Sample Call #2",
                "start_time": "2026-05-20T15:00:00Z",
                "occurrence_number": 2,
            },
        ],
    )
    write_complete_artifacts(artifacts_dir / "sample" / "2026-05-19_001")

    class FixedDateTime(datetime):
        @classmethod
        def now(cls, tz=None):
            return datetime(2026, 5, 20, 16, tzinfo=timezone.utc)

    monkeypatch.setattr(run_pipeline, "MAPPING_FILE", mapping_path)
    monkeypatch.setattr(run_pipeline, "ARTIFACTS_DIR", artifacts_dir)
    monkeypatch.setattr(run_pipeline, "datetime", FixedDateTime)

    commands = []

    def fake_run_step(name, cmd, check=True):
        commands.append(cmd)
        write_complete_artifacts(artifacts_dir / "sample" / "2026-05-20_002")
        return True

    monkeypatch.setattr(run_pipeline, "run_step", fake_run_step)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_pipeline.py",
            "-c",
            "sample",
            "--recent",
            "--max-age-days",
            "3",
            "--auto-approve",
            "--summarize",
        ],
    )

    with pytest.raises(SystemExit) as exit_info:
        run_pipeline.main()

    assert exit_info.value.code == 0
    assert len(commands) == 1
    download_cmd = commands[0]
    assert download_cmd[:2] == [sys.executable, "download_zoom_assets.py"]
    assert download_cmd[download_cmd.index("--series-name") + 1] == "sample"
    assert download_cmd[download_cmd.index("--date") + 1] == "2026-05-20"
    assert download_cmd[download_cmd.index("--number") + 1] == "2"
    assert "2026-05-19" not in download_cmd


def test_number_only_run_fails_when_public_number_is_ambiguous(tmp_path, monkeypatch, capsys):
    run_pipeline = load_run_pipeline_module()

    mapping_path = tmp_path / "meeting_topic_mapping.json"
    artifacts_dir = tmp_path / "artifacts"
    write_mapping(
        mapping_path,
        "sample",
        [
            {
                "issue_title": "Sample Meeting 98, April 21, 2026",
                "start_time": "2026-04-21T14:00:00Z",
                "occurrence_number": 97,
            },
            {
                "issue_title": "Sample Call 98, May 05, 2026",
                "start_time": "2026-05-05T14:00:00Z",
                "occurrence_number": 98,
            },
        ],
    )

    monkeypatch.setattr(run_pipeline, "MAPPING_FILE", mapping_path)
    monkeypatch.setattr(run_pipeline, "ARTIFACTS_DIR", artifacts_dir)
    monkeypatch.setattr(
        run_pipeline,
        "run_step",
        lambda *args, **kwargs: pytest.fail("ambiguous number must fail before running steps"),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_pipeline.py",
            "-c",
            "sample",
            "-n",
            "98",
            "--auto-approve",
        ],
    )

    with pytest.raises(SystemExit) as exit_info:
        run_pipeline.main()

    assert exit_info.value.code == 1
    output = capsys.readouterr().out
    assert "Ambiguous mapped occurrences for sample #98" in output
    assert "2026-04-21" in output
    assert "2026-05-05" in output
