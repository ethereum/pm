"""Tests for breakout room asset handling (e.g. the ACDT CL breakout)."""

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


ACDBOT_DIR = Path(__file__).resolve().parents[2]
ASSET_PIPELINE_DIR = ACDBOT_DIR / "scripts" / "asset_pipeline"


def load_pipeline_module(filename: str):
    if str(ASSET_PIPELINE_DIR) not in sys.path:
        sys.path.insert(0, str(ASSET_PIPELINE_DIR))

    module_path = ASSET_PIPELINE_DIR / filename
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FakeZoom:
    """Fake zoom module exposing only what breakout downloads need."""

    def __init__(self, instances: list[dict], recordings: dict[str, dict]):
        self.instances = instances
        self.recordings = recordings

    def get_past_meeting_instances(self, meeting_id):
        return self.instances

    def get_meeting_recording(self, uuid):
        return self.recordings.get(uuid)


def make_recording(
    uuid: str,
    start_time: str,
    duration: int,
    topic: str = "All Core Devs - Testing (ACDT) #86 - CL Breakout",
) -> dict:
    return {
        "uuid": uuid,
        "start_time": start_time,
        "duration": duration,
        "topic": topic,
        "recording_files": [
            {"file_type": "TRANSCRIPT", "download_url": f"https://zoom.example/{uuid}/transcript"},
            {"file_type": "CHAT", "download_url": f"https://zoom.example/{uuid}/chat"},
        ],
    }


def test_download_breakout_assets_selects_same_date_instance(tmp_path, monkeypatch):
    download_zoom_assets = load_pipeline_module("download_zoom_assets.py")

    instances = [
        {"uuid": "wrong-date", "start_time": "2026-07-01T15:00:00Z"},
        {"uuid": "short-restart", "start_time": "2026-07-06T15:00:00Z"},
        {"uuid": "full-breakout", "start_time": "2026-07-06T15:05:00Z"},
    ]
    recordings = {
        "wrong-date": make_recording("wrong-date", "2026-07-01T15:00:00Z", 45),
        "short-restart": make_recording("short-restart", "2026-07-06T15:00:00Z", 3),
        "full-breakout": make_recording("full-breakout", "2026-07-06T15:05:00Z", 40),
    }
    monkeypatch.setattr(download_zoom_assets, "zoom", FakeZoom(instances, recordings))

    downloaded = []

    def fake_download_file(url, token, path):
        downloaded.append(url)
        Path(path).write_text("content", encoding="utf-8")
        return True

    monkeypatch.setattr(download_zoom_assets, "download_file", fake_download_file)

    meeting_dir = tmp_path / "acdt" / "2026-07-06_086"
    meeting_dir.mkdir(parents=True)
    occurrence = {"start_time": "2026-07-06T14:00:00Z"}

    download_zoom_assets.download_breakout_assets(
        occurrence, "cl", "99900001111", meeting_dir, "token", 10
    )

    assert (meeting_dir / "transcript_cl.vtt").exists()
    assert (meeting_dir / "chat_cl.txt").exists()
    # Longest same-date recording wins; other dates are never downloaded
    assert all("full-breakout" in url for url in downloaded)
    assert len(downloaded) == 2


def test_download_breakout_assets_picks_longest_same_date_recording(
    tmp_path, monkeypatch
):
    download_zoom_assets = load_pipeline_module("download_zoom_assets.py")
    instances = [
        {"uuid": "first", "start_time": "2026-07-06T15:00:00Z"},
        {"uuid": "second", "start_time": "2026-07-06T16:00:00Z"},
    ]
    recordings = {
        "first": make_recording("first", "2026-07-06T15:00:00Z", 30),
        "second": make_recording("second", "2026-07-06T16:00:00Z", 40),
    }
    monkeypatch.setattr(download_zoom_assets, "zoom", FakeZoom(instances, recordings))

    downloaded = []

    def fake_download_file(url, token, path):
        downloaded.append(url)
        Path(path).write_text("content", encoding="utf-8")
        return True

    monkeypatch.setattr(download_zoom_assets, "download_file", fake_download_file)

    meeting_dir = tmp_path / "acdt" / "2026-07-06_086"
    meeting_dir.mkdir(parents=True)
    download_zoom_assets.download_breakout_assets(
        {
            "issue_title": "All Core Devs - Testing (ACDT) #86, July 6, 2026",
            "start_time": "2026-07-06T14:00:00Z",
        },
        "cl",
        "99900001111",
        meeting_dir,
        "token",
        10,
    )

    # Multiple same-date recordings are treated as restarts; the longest wins
    assert (meeting_dir / "transcript_cl.vtt").exists()
    assert all("second" in url for url in downloaded)


def test_download_breakout_assets_skips_when_assets_exist(tmp_path, monkeypatch):
    download_zoom_assets = load_pipeline_module("download_zoom_assets.py")

    class ExplodingZoom:
        def get_past_meeting_instances(self, meeting_id):
            pytest.fail("Zoom must not be queried when breakout assets already exist")

    monkeypatch.setattr(download_zoom_assets, "zoom", ExplodingZoom())

    meeting_dir = tmp_path / "acdt" / "2026-07-06_086"
    meeting_dir.mkdir(parents=True)
    (meeting_dir / "transcript_cl.vtt").write_text("WEBVTT\n", encoding="utf-8")
    (meeting_dir / "chat_cl.txt").write_text("hi\n", encoding="utf-8")

    download_zoom_assets.download_breakout_assets(
        {"start_time": "2026-07-06T14:00:00Z"},
        "cl",
        "99900001111",
        meeting_dir,
        "token",
        10,
    )


@pytest.mark.parametrize(
    ("min_duration_minutes", "should_download"),
    [(0, True), (5, False), (10, False)],
)
def test_download_breakout_assets_respects_min_duration(
    tmp_path, monkeypatch, min_duration_minutes, should_download
):
    download_zoom_assets = load_pipeline_module("download_zoom_assets.py")

    # Only a two-minute recording exists on the target date.
    instances = [{"uuid": "short", "start_time": "2026-07-06T15:00:00Z"}]
    recordings = {"short": make_recording("short", "2026-07-06T15:00:00Z", 2)}
    monkeypatch.setattr(download_zoom_assets, "zoom", FakeZoom(instances, recordings))

    def fake_download_file(url, token, path):
        Path(path).write_text("content", encoding="utf-8")
        return True

    monkeypatch.setattr(download_zoom_assets, "download_file", fake_download_file)

    meeting_dir = tmp_path / "acdt" / "2026-07-06_086"
    meeting_dir.mkdir(parents=True)

    download_zoom_assets.download_breakout_assets(
        {"start_time": "2026-07-06T14:00:00Z"},
        "cl",
        "99900001111",
        meeting_dir,
        "token",
        min_duration_minutes,
    )

    assert (meeting_dir / "transcript_cl.vtt").exists() is should_download


def test_download_all_breakout_assets_skips_placeholder_ids(tmp_path, monkeypatch):
    download_zoom_assets = load_pipeline_module("download_zoom_assets.py")

    class ExplodingZoom:
        def get_past_meeting_instances(self, meeting_id):
            pytest.fail("Placeholder breakout meeting ids must be skipped")

    monkeypatch.setattr(download_zoom_assets, "zoom", ExplodingZoom())

    meeting_dir = tmp_path / "acdt" / "2026-07-06_086"
    meeting_dir.mkdir(parents=True)
    series_data = {"breakout_meeting_ids": {"cl": "REPLACE_WITH_CL_ZOOM_MEETING_ID"}}

    download_zoom_assets.download_all_breakout_assets(
        series_data,
        {"start_time": "2026-07-06T14:00:00Z"},
        meeting_dir,
        "token",
        10,
    )


def test_download_all_breakout_assets_noop_without_meeting_dir(monkeypatch):
    download_zoom_assets = load_pipeline_module("download_zoom_assets.py")

    class ExplodingZoom:
        def get_past_meeting_instances(self, meeting_id):
            pytest.fail("No downloads should happen without a meeting directory")

    monkeypatch.setattr(download_zoom_assets, "zoom", ExplodingZoom())

    download_zoom_assets.download_all_breakout_assets(
        {"breakout_meeting_ids": {"cl": "99900001111"}},
        {"start_time": "2026-07-06T14:00:00Z"},
        None,
        "token",
        10,
    )


def test_download_all_breakout_assets_forwards_min_duration(tmp_path, monkeypatch):
    download_zoom_assets = load_pipeline_module("download_zoom_assets.py")
    calls = []

    monkeypatch.setattr(
        download_zoom_assets,
        "download_breakout_assets",
        lambda *args: calls.append(args),
    )

    meeting_dir = tmp_path / "acdt" / "2026-07-06_086"
    meeting_dir.mkdir(parents=True)
    occurrence = {"start_time": "2026-07-06T14:00:00Z"}

    download_zoom_assets.download_all_breakout_assets(
        {"breakout_meeting_ids": {"cl": "99900001111"}},
        occurrence,
        meeting_dir,
        "token",
        10,
    )

    assert calls == [
        (occurrence, "cl", "99900001111", meeting_dir, "token", 10)
    ]


def setup_summary_test(tmp_path, monkeypatch, generate_summary):
    """Common fixtures for generate_summary tests: meeting dir, mapping, fake API."""
    meeting_dir = tmp_path / "acdt" / "2026-07-06_086"
    meeting_dir.mkdir(parents=True)
    (meeting_dir / "transcript.vtt").write_text("WEBVTT\nmain call content\n", encoding="utf-8")
    (meeting_dir / "transcript_cl.vtt").write_text("WEBVTT\ncl breakout content\n", encoding="utf-8")
    (meeting_dir / "chat_cl.txt").write_text("cl chat content\n", encoding="utf-8")

    mapping_path = tmp_path / "meeting_topic_mapping.json"
    mapping_path.write_text(
        json.dumps(
            {
                "acdt": {
                    "occurrences": [
                        {
                            "issue_number": 9999,
                            "issue_title": "All Core Devs - Testing (ACDT) #86 | July 6 2026",
                            "start_time": "2026-07-06T14:00:00Z",
                        }
                    ],
                },
            },
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(generate_summary, "MAPPING_FILE", mapping_path)
    monkeypatch.setattr(generate_summary, "fetch_github_issue_agenda", lambda *a, **k: "agenda")

    captured_prompts = []

    class FakeMessages:
        def create(self, model, max_tokens, messages):
            captured_prompts.append(messages[0]["content"])
            return SimpleNamespace(
                content=[SimpleNamespace(text='```json\n{"meeting": "ACDT #86"}\n```')],
                usage=SimpleNamespace(input_tokens=10, output_tokens=5),
            )

    class FakeAnthropic:
        def __init__(self, *args, **kwargs):
            self.messages = FakeMessages()

    monkeypatch.setattr(generate_summary.anthropic, "Anthropic", FakeAnthropic)

    prompt_file = tmp_path / "prompt.md"
    prompt_file.write_text("Summarize the meeting.", encoding="utf-8")

    return meeting_dir, prompt_file, captured_prompts


def test_generate_summary_creates_separate_breakout_tldr(tmp_path, monkeypatch):
    generate_summary = load_pipeline_module("generate_summary.py")
    meeting_dir, prompt_file, captured_prompts = setup_summary_test(
        tmp_path, monkeypatch, generate_summary
    )

    assert generate_summary.generate_summary(meeting_dir, prompt_file, "acdt")

    # One call for the main transcript, one for the CL breakout
    assert len(captured_prompts) == 2

    main_prompt, breakout_prompt = captured_prompts
    # Main summary must not mix in the CL transcript (its timestamps refer to a
    # different recording)
    assert "main call content" in main_prompt
    assert "cl breakout content" not in main_prompt
    assert "cl chat content" not in main_prompt

    assert "cl breakout content" in breakout_prompt
    assert "cl chat content" in breakout_prompt
    assert "main call content" not in breakout_prompt
    assert "(CL breakout)" in breakout_prompt

    assert json.loads((meeting_dir / "tldr.json").read_text()) == {"meeting": "ACDT #86"}
    assert json.loads((meeting_dir / "tldr_cl.json").read_text()) == {"meeting": "ACDT #86"}


def test_generate_summary_only_generates_missing_breakout_tldr(tmp_path, monkeypatch):
    generate_summary = load_pipeline_module("generate_summary.py")
    meeting_dir, prompt_file, captured_prompts = setup_summary_test(
        tmp_path, monkeypatch, generate_summary
    )
    (meeting_dir / "tldr.json").write_text('{"meeting": "existing"}', encoding="utf-8")

    assert generate_summary.generate_summary(meeting_dir, prompt_file, "acdt")

    # Only the missing breakout tldr is generated; main tldr untouched
    assert len(captured_prompts) == 1
    assert "cl breakout content" in captured_prompts[0]
    assert json.loads((meeting_dir / "tldr.json").read_text()) == {"meeting": "existing"}
    assert (meeting_dir / "tldr_cl.json").exists()


def test_generate_summary_skips_when_all_tldrs_exist(tmp_path, monkeypatch):
    generate_summary = load_pipeline_module("generate_summary.py")
    meeting_dir, prompt_file, captured_prompts = setup_summary_test(
        tmp_path, monkeypatch, generate_summary
    )
    (meeting_dir / "tldr.json").write_text("{}", encoding="utf-8")
    (meeting_dir / "tldr_cl.json").write_text("{}", encoding="utf-8")

    assert generate_summary.generate_summary(meeting_dir, prompt_file, "acdt")
    assert captured_prompts == []


def test_derive_breakout_topic_formats():
    from scripts.handle_protocol_call import derive_breakout_topic

    assert derive_breakout_topic(
        "All Core Devs - Testing (ACDT) #87, July 13, 2026", "cl"
    ) == "All Core Devs - Testing (ACDT) #87 - CL Breakout, July 13, 2026"

    assert derive_breakout_topic(
        "All Core Devs - Testing (ACDT) #85 | June 29 2026", "cl"
    ) == "All Core Devs - Testing (ACDT) #85 - CL Breakout | June 29 2026"

    # No date delimiter: append the suffix
    assert derive_breakout_topic("ACDT #90", "cl") == "ACDT #90 - CL Breakout"


def test_derive_breakout_youtube_title_formats():
    from modules.breakout_utils import derive_breakout_youtube_title

    assert derive_breakout_youtube_title(
        "acdt", "All Core Devs - Testing (ACDT) #84, June 22, 2026", "cl"
    ) == "ACDT #84 (CL Breakout), June 22, 2026"

    # Pipe-delimited date variant
    assert derive_breakout_youtube_title(
        "acdt", "All Core Devs - Testing (ACDT) #36 | May 12 2025", "cl"
    ) == "ACDT #36 (CL Breakout), May 12 2025"

    # No number or date delimiter
    assert derive_breakout_youtube_title("acdt", "ACDT breakout", "cl") == (
        "ACDT (CL Breakout)"
    )


def stub_zoom_module(monkeypatch, update_calls):
    """Install a stub modules.zoom (the real one needs Zoom credentials at import)."""
    import modules as modules_pkg

    stub = SimpleNamespace(
        update_meeting=lambda meeting_id, topic, start_time=None, duration=None: update_calls.append(
            (meeting_id, topic, start_time, duration)
        ),
        get_meeting_url_with_passcode=lambda meeting_id: f"https://zoom.us/j/{meeting_id}?pwd=secret",
    )
    monkeypatch.setitem(sys.modules, "modules.zoom", stub)
    monkeypatch.setattr(modules_pkg, "zoom", stub, raising=False)


def test_sync_breakout_meeting_topics_updates_title(monkeypatch):
    from scripts.handle_protocol_call import ProtocolCallHandler

    update_calls = []
    stub_zoom_module(monkeypatch, update_calls)

    handler = ProtocolCallHandler()
    monkeypatch.setattr(
        handler.mapping_manager,
        "load_mapping",
        lambda: {
            "acdt": {
                "meeting_id": "88479308162",
                "breakout_meeting_ids": {"cl": "89441658268"},
            },
        },
    )

    handler._sync_breakout_meeting_topics(
        "acdt", "All Core Devs - Testing (ACDT) #88, July 20, 2026"
    )

    assert update_calls == [
        (
            "89441658268",
            "All Core Devs - Testing (ACDT) #88 - CL Breakout, July 20, 2026",
            None,
            None,
        )
    ]


def test_sync_breakout_meeting_topics_skips_placeholder_and_missing(monkeypatch):
    from scripts.handle_protocol_call import ProtocolCallHandler

    update_calls = []
    stub_zoom_module(monkeypatch, update_calls)

    handler = ProtocolCallHandler()
    monkeypatch.setattr(
        handler.mapping_manager,
        "load_mapping",
        lambda: {
            "acdt": {"breakout_meeting_ids": {"cl": "REPLACE_WITH_CL_ZOOM_MEETING_ID"}},
            "acde": {"meeting_id": "88269836469"},
        },
    )

    handler._sync_breakout_meeting_topics("acdt", "ACDT #88, July 20, 2026")
    handler._sync_breakout_meeting_topics("acde", "ACDE #240, July 16, 2026")
    handler._sync_breakout_meeting_topics("unknown", "Some Call #1, July 1, 2026")

    assert update_calls == []


def test_resource_comment_includes_breakout_zoom_link(monkeypatch):
    from scripts.handle_protocol_call import ProtocolCallHandler

    stub_zoom_module(monkeypatch, [])
    monkeypatch.setitem(
        sys.modules,
        "modules.gcal",
        SimpleNamespace(render_calendar_comment_line=lambda **kwargs: "📅 **Calendar**: stub"),
    )

    handler = ProtocolCallHandler()
    occurrence = {
        "issue_number": 9999,
        "issue_title": "All Core Devs - Testing (ACDT) #87, July 13, 2026",
        "start_time": "2026-07-13T14:00:00Z",
        "duration": 60,
        "discourse_topic_id": 12345,
    }
    monkeypatch.setattr(
        handler.mapping_manager,
        "find_occurrence",
        lambda issue_number: {"call_series": "acdt", "occurrence": occurrence},
    )
    monkeypatch.setattr(
        handler.mapping_manager,
        "load_mapping",
        lambda: {
            "acdt": {
                "meeting_id": "88479308162",
                "breakout_meeting_ids": {"cl": "89441658268"},
            },
        },
    )

    call_data = {
        "issue_number": 9999,
        "issue_title": occurrence["issue_title"],
        "issue_url": "https://github.com/ethereum/pm/issues/9999",
        "duration": 60,
        "display_zoom_link_in_invite": True,
    }

    comment = handler._generate_comprehensive_resource_comment(call_data)

    assert "✅ **Zoom**: [Join Meeting](https://zoom.us/j/88479308162?pwd=secret)" in comment
    assert (
        "✅ **Zoom (CL Breakout)**: [Join Meeting](https://zoom.us/j/89441658268?pwd=secret)"
        in comment
    )


def test_iter_breakout_meetings_filters_non_numeric_ids():
    from modules.mapping_utils import iter_breakout_meetings

    assert list(iter_breakout_meetings(None)) == []
    assert list(iter_breakout_meetings({})) == []
    assert list(
        iter_breakout_meetings(
            {
                "breakout_meeting_ids": {
                    "cl": "89441658268",
                    "placeholder": "REPLACE_WITH_CL_ZOOM_MEETING_ID",
                    "empty": "",
                    "none": None,
                }
            }
        )
    ) == [("cl", "89441658268")]


def test_manifest_lists_cl_breakout_resources(tmp_path):
    generate_manifest = load_pipeline_module("generate_manifest.py")

    call_dir = tmp_path / "2026-07-06_086"
    call_dir.mkdir(parents=True)
    (call_dir / "transcript.vtt").write_text("WEBVTT\n", encoding="utf-8")
    (call_dir / "transcript_cl.vtt").write_text("WEBVTT\n", encoding="utf-8")
    (call_dir / "chat_cl.txt").write_text("hi\n", encoding="utf-8")
    (call_dir / "tldr.json").write_text("{}", encoding="utf-8")
    (call_dir / "tldr_cl.json").write_text("{}", encoding="utf-8")

    resources = generate_manifest.get_call_resources(call_dir)

    assert resources["transcript_cl"] == "transcript_cl.vtt"
    assert resources["chat_cl"] == "chat_cl.txt"
    assert resources["tldr_cl"] == "tldr_cl.json"
    assert resources["transcript"] == "transcript.vtt"
    assert resources["tldr"] == "tldr.json"


def test_manifest_extracts_breakout_video_urls():
    generate_manifest = load_pipeline_module("generate_manifest.py")

    assert generate_manifest.get_breakout_youtube_video_urls(
        {
            "breakout_youtube": {
                "cl": {
                    "youtube_video_id": "cl-video",
                    "youtube_upload_processed": True,
                },
                "invalid": "not-an-object",
            }
        }
    ) == {"cl": "https://www.youtube.com/watch?v=cl-video"}
