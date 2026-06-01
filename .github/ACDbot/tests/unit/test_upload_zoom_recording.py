"""Tests for Zoom recording selection before YouTube upload."""

import importlib.util
import os
import sys
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
