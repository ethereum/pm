"""Tests for Zoom recording selection before YouTube upload."""

import importlib.util
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


ACDBOT_DIR = Path(__file__).resolve().parents[2]


def load_upload_module():
    os.environ.setdefault("YOUTUBE_REFRESH_TOKEN", "test-youtube-refresh-token")
    os.environ.setdefault("GOOGLE_CLIENT_ID", "test-google-client-id")
    os.environ.setdefault("GOOGLE_CLIENT_SECRET", "test-google-client-secret")
    os.environ.setdefault("ZOOM_CLIENT_ID", "test-zoom-client-id")
    os.environ.setdefault("ZOOM_CLIENT_SECRET", "test-zoom-client-secret")
    os.environ.setdefault("ZOOM_REFRESH_TOKEN", "test-zoom-refresh-token")

    acdbot_path = str(ACDBOT_DIR)
    if acdbot_path not in sys.path:
        sys.path.insert(0, acdbot_path)

    module_path = ACDBOT_DIR / "scripts" / "upload_zoom_recording.py"
    spec = importlib.util.spec_from_file_location("upload_zoom_recording", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_occurrence_upload_uses_past_instance_instead_of_direct_lookup(monkeypatch):
    upload_zoom_recording = load_upload_module()
    meeting_id = "82730734123"

    wrong_direct_recording = {
        "uuid": "wrong-direct",
        "start_time": "2026-05-27T14:56:03Z",
        "duration": 16,
        "recording_files": [
            {
                "file_type": "MP4",
                "recording_type": "active_speaker",
                "file_size": 3_141_213,
                "download_url": "https://example.test/wrong.mp4",
            },
        ],
    }
    correct_recording = {
        "uuid": "correct-instance",
        "start_time": "2026-05-27T13:00:14Z",
        "duration": 54,
        "recording_files": [
            {
                "file_type": "MP4",
                "recording_type": "shared_screen_with_speaker_view(CC)",
                "file_size": 150_000_000,
                "download_url": "https://example.test/correct.mp4",
            },
        ],
    }

    monkeypatch.setattr(
        upload_zoom_recording.zoom,
        "get_past_meeting_instances",
        lambda _meeting_id: [
            {"uuid": "correct-instance", "start_time": "2026-05-27T13:00:14Z"},
            {"uuid": "wrong-direct", "start_time": "2026-05-27T14:56:03Z"},
        ],
    )

    def fake_get_meeting_recording(identifier):
        if identifier == meeting_id:
            return wrong_direct_recording
        if identifier == "correct-instance":
            return correct_recording
        if identifier == "wrong-direct":
            return wrong_direct_recording
        raise AssertionError(f"unexpected recording identifier: {identifier}")

    monkeypatch.setattr(upload_zoom_recording, "get_meeting_recording", fake_get_meeting_recording)

    selected = upload_zoom_recording.find_best_youtube_recording(
        meeting_id,
        min_duration_minutes=10,
        target_start_time="2026-05-27T13:00:00Z",
    )

    assert selected["uuid"] == "correct-instance"


def test_recording_type_matches_zoom_cc_suffix():
    upload_zoom_recording = load_upload_module()

    assert upload_zoom_recording.recording_type_matches(
        "shared_screen_with_speaker_view(CC)",
        "shared_screen_with_speaker_view",
    )


def test_prepare_upload_video_uses_raw_zoom_recording_mode(monkeypatch):
    upload_zoom_recording = load_upload_module()
    calls = []

    monkeypatch.setattr(upload_zoom_recording, "get_recording_publication_mode", lambda _series: "raw_zoom_recording")

    def fake_download_zoom_recording(*args, **kwargs):
        calls.append((args, kwargs))
        return "/tmp/raw.mp4"

    monkeypatch.setattr(upload_zoom_recording, "download_zoom_recording", fake_download_zoom_recording)

    result = upload_zoom_recording.prepare_upload_video(
        "acde",
        {"recording_files": []},
        "123",
        min_duration_minutes=10,
        target_start_time="2026-06-01T14:00:00Z",
    )

    assert result == "/tmp/raw.mp4"
    assert calls[0][0][0] == "123"
    assert calls[0][1]["recording_info"] == {"recording_files": []}


def test_prepare_upload_video_uses_composed_zoom_recording_mode(monkeypatch, tmp_path):
    upload_zoom_recording = load_upload_module()

    bumper_path = tmp_path / "bumper.mp4"
    bumper_path.write_bytes(b"bumper")
    composed_path = tmp_path / "composed.mp4"

    monkeypatch.setattr(upload_zoom_recording, "get_recording_publication_mode", lambda _series: "composed_zoom_recording")
    monkeypatch.setattr(upload_zoom_recording, "resolve_bumper_path", lambda: (bumper_path, False))
    monkeypatch.setattr(upload_zoom_recording, "get_access_token", lambda: "zoom-token")

    from scripts import compose_zoom_recording

    def fake_compose_zoom_recording(recording_info, bumper_path, output_path, access_token):
        assert recording_info == {"recording_files": [{"file_type": "MP4"}]}
        assert bumper_path == tmp_path / "bumper.mp4"
        assert access_token == "zoom-token"
        output_path.write_bytes(b"composed")
        return composed_path

    monkeypatch.setattr(compose_zoom_recording, "compose_zoom_recording", fake_compose_zoom_recording)

    result = upload_zoom_recording.prepare_upload_video(
        "acdt",
        {"recording_files": [{"file_type": "MP4"}]},
        "123",
    )

    assert result == str(composed_path)


def test_upload_breakout_recording_persists_state_and_uses_parent_playlists(
    monkeypatch, tmp_path
):
    upload_zoom_recording = load_upload_module()
    mapping = {
        "acdt": {
            "call_series": "acdt",
            "breakout_meeting_ids": {"cl": "89441658268"},
            "occurrences": [
                {
                    "issue_number": 2151,
                    "issue_title": "All Core Devs - Testing (ACDT) #87, July 13, 2026",
                    "start_time": "2026-07-13T14:00:00Z",
                    "duration": 60,
                    "skip_youtube_upload": False,
                    "youtube_video_id": "parent-video",
                    "youtube_upload_processed": True,
                    "discourse_topic_id": 123,
                }
            ],
        }
    }
    saved = []
    request_bodies = []
    playlist_calls = []
    discourse_posts = []

    monkeypatch.setattr(
        upload_zoom_recording,
        "load_meeting_topic_mapping",
        lambda: mapping,
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "save_meeting_topic_mapping",
        lambda value: saved.append(value),
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "select_breakout_recording",
        lambda *args, **kwargs: {
            "uuid": "cl-instance",
            "duration": 40,
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "speaker_view",
                    "download_url": "https://zoom.example/cl.mp4",
                }
            ],
        },
    )

    video_path = tmp_path / "cl.mp4"
    video_path.write_bytes(b"video")
    download_calls = []

    def fake_download(*args, **kwargs):
        download_calls.append((args, kwargs))
        return str(video_path)

    monkeypatch.setattr(upload_zoom_recording, "download_zoom_recording", fake_download)
    monkeypatch.setattr(
        upload_zoom_recording.googleapiclient.http,
        "MediaFileUpload",
        lambda *args, **kwargs: object(),
    )
    monkeypatch.setattr(upload_zoom_recording, "UPLOAD_THUMBNAIL_PATH", str(tmp_path / "missing.png"))
    monkeypatch.setattr(
        upload_zoom_recording,
        "add_video_to_appropriate_playlist",
        lambda video_id, series: playlist_calls.append((video_id, series)) or ["playlist"],
    )
    monkeypatch.setattr(
        upload_zoom_recording.discourse,
        "create_post",
        lambda **kwargs: discourse_posts.append(kwargs),
    )
    monkeypatch.setattr(upload_zoom_recording, "rss_utils", None)
    monkeypatch.setattr(upload_zoom_recording.tg, "send_message", lambda *args, **kwargs: None)
    monkeypatch.setattr(
        upload_zoom_recording.mattermost_notify,
        "send_mattermost_notification",
        lambda *args, **kwargs: None,
    )

    class Videos:
        def insert(self, **kwargs):
            request_bodies.append(kwargs["body"])
            return self

        def execute(self):
            return {"id": "cl-video"}

    class Youtube:
        def videos(self):
            return Videos()

    monkeypatch.setattr(upload_zoom_recording, "get_authenticated_service", Youtube)

    assert upload_zoom_recording.upload_breakout_recording(
        "acdt",
        2151,
        "cl",
        "89441658268",
        min_duration=10,
    ) is True

    occurrence = mapping["acdt"]["occurrences"][0]
    assert occurrence["youtube_video_id"] == "parent-video"
    assert occurrence["breakout_youtube"]["cl"] == {
        "upload_attempt_count": 1,
        "recording_publication_mode": "raw_zoom_recording",
        "playlist_assignment_processed": True,
        "youtube_video_id": "cl-video",
        "youtube_upload_processed": True,
    }
    assert download_calls[0][0][0] == "89441658268"
    assert download_calls[0][1]["recording_info"]["uuid"] == "cl-instance"
    assert request_bodies[0]["snippet"]["title"] == (
        "ACDT #87 (CL Breakout), July 13, 2026"
    )
    assert playlist_calls == [("cl-video", "acdt")]
    assert discourse_posts == [
        {
            "topic_id": 123,
            "body": "CL breakout YouTube recording available: https://youtu.be/cl-video",
        }
    ]
    assert len(saved) == 3


def test_upload_breakout_recording_skips_existing_video(monkeypatch):
    upload_zoom_recording = load_upload_module()
    mapping = {
        "acdt": {
            "occurrences": [
                {
                    "issue_number": 2151,
                    "breakout_youtube": {
                        "cl": {
                            "youtube_video_id": "existing",
                            "youtube_upload_processed": True,
                        }
                    },
                }
            ]
        }
    }
    monkeypatch.setattr(
        upload_zoom_recording,
        "load_meeting_topic_mapping",
        lambda: mapping,
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "select_breakout_recording",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            AssertionError("Zoom must not be queried for an uploaded breakout")
        ),
    )

    assert upload_zoom_recording.upload_breakout_recording(
        "acdt",
        2151,
        "cl",
        "89441658268",
    ) is None


def test_upload_breakout_recording_retries_pending_playlist_assignment(monkeypatch):
    upload_zoom_recording = load_upload_module()
    mapping = {
        "acdt": {
            "occurrences": [
                {
                    "issue_number": 2151,
                    "breakout_youtube": {
                        "cl": {
                            "youtube_video_id": "existing",
                            "youtube_upload_processed": True,
                            "playlist_assignment_processed": False,
                        }
                    },
                }
            ]
        }
    }
    saved = []
    playlist_calls = []
    monkeypatch.setattr(
        upload_zoom_recording,
        "load_meeting_topic_mapping",
        lambda: mapping,
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "save_meeting_topic_mapping",
        lambda value: saved.append(value),
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "assign_breakout_playlists",
        lambda video_id, series: playlist_calls.append((video_id, series)) or True,
    )

    assert upload_zoom_recording.upload_breakout_recording(
        "acdt",
        2151,
        "cl",
        "89441658268",
    ) is True
    assert playlist_calls == [("existing", "acdt")]
    assert mapping["acdt"]["occurrences"][0]["breakout_youtube"]["cl"][
        "playlist_assignment_processed"
    ] is True
    assert len(saved) == 1


def test_assign_breakout_playlists_reports_partial_failure(monkeypatch):
    upload_zoom_recording = load_upload_module()
    monkeypatch.setattr(
        upload_zoom_recording,
        "add_video_to_appropriate_playlist",
        lambda *args: [{"id": "acdt-item"}, None],
    )

    assert not upload_zoom_recording.assign_breakout_playlists(
        "cl-video",
        "acdt",
    )


def test_forced_parent_failure_does_not_block_breakout_upload(monkeypatch):
    upload_zoom_recording = load_upload_module()
    breakout_calls = []

    monkeypatch.setattr(
        upload_zoom_recording,
        "upload_recording",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("parent failed")),
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "load_meeting_topic_mapping",
        lambda: {"acdt": {}},
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "find_call_series_by_meeting_id",
        lambda *args: "acdt",
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "upload_breakouts_for_occurrence",
        lambda *args, **kwargs: breakout_calls.append((args, kwargs)),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "upload_zoom_recording.py",
            "--meeting_id",
            "88479308162",
            "--occurrence_issue_number",
            "2151",
            "--min-duration",
            "10",
        ],
    )

    upload_zoom_recording.main()

    assert breakout_calls == [(("acdt", 2151), {"min_duration": 10})]


def test_get_latest_past_occurrence_ignores_future_meetings():
    upload_zoom_recording = load_upload_module()
    past = {"issue_number": 1, "start_time": "2026-07-06T14:00:00Z"}
    future = {"issue_number": 2, "start_time": "2026-07-20T14:00:00Z"}

    assert upload_zoom_recording.get_latest_past_occurrence(
        [past, future],
        now=datetime(2026, 7, 10, tzinfo=timezone.utc),
    ) is past


def test_recent_past_occurrence_uses_bounded_breakout_retry_window():
    upload_zoom_recording = load_upload_module()
    now = datetime(2026, 7, 20, tzinfo=timezone.utc)

    assert upload_zoom_recording.is_recent_past_occurrence(
        {"start_time": "2026-07-13T14:00:00Z"},
        now=now,
    )
    assert not upload_zoom_recording.is_recent_past_occurrence(
        {"start_time": "2026-06-01T14:00:00Z"},
        now=now,
    )


def test_batch_retries_recent_breakouts_when_parent_uploads_are_processed(monkeypatch):
    upload_zoom_recording = load_upload_module()
    breakout_calls = []
    now = datetime.now(timezone.utc)
    mapping = {
        "acdt": {
            "meeting_id": "88479308162",
            "breakout_meeting_ids": {"cl": "89441658268"},
            "occurrences": [
                {
                    "issue_number": 2150,
                    "start_time": (now - timedelta(days=8)).isoformat(),
                    "duration": 60,
                    "skip_youtube_upload": False,
                    "youtube_upload_processed": True,
                },
                {
                    "issue_number": 2151,
                    "start_time": (now - timedelta(days=1)).isoformat(),
                    "duration": 60,
                    "skip_youtube_upload": False,
                    "youtube_upload_processed": True,
                }
            ],
        }
    }
    monkeypatch.setattr(
        upload_zoom_recording,
        "load_meeting_topic_mapping",
        lambda: mapping,
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "upload_recording",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            AssertionError("Processed parent must not be uploaded again")
        ),
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "upload_breakouts_for_occurrence",
        lambda *args, **kwargs: breakout_calls.append((args, kwargs)) or [None],
    )
    monkeypatch.setattr(
        upload_zoom_recording,
        "send_aggregated_telegram_message",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(sys, "argv", ["upload_zoom_recording.py"])

    upload_zoom_recording.main()

    assert breakout_calls == [
        (
            ("acdt", 2150),
            {"error_collector": [], "min_duration": 15},
        ),
        (
            ("acdt", 2151),
            {"error_collector": [], "min_duration": 15},
        ),
    ]
