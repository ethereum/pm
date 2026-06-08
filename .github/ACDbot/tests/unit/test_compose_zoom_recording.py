from pathlib import Path
from datetime import datetime, timezone

import pytest

from scripts.compose_zoom_recording import (
    ZoomTrimWindow,
    build_ffmpeg_command,
    composed_recording_sync_from_transcript,
    extract_peak_level_db,
    select_recording_target,
    select_recording_files,
    transcript_speech_window,
)


def test_select_recording_target_returns_latest_recent_past_occurrence():
    mapping = {
        "acdt": {
            "meeting_id": "88479308162",
            "occurrences": [
                {
                    "occurrence_number": 80,
                    "issue_number": 2049,
                    "issue_title": "ACDT #80",
                    "start_time": "2026-05-18T14:00:00Z",
                    "duration": 60,
                },
                {
                    "occurrence_number": 81,
                    "issue_number": 2085,
                    "issue_title": "ACDT #81",
                    "start_time": "2026-06-01T14:00:00Z",
                    "duration": 60,
                },
                {
                    "occurrence_number": 82,
                    "issue_number": 2090,
                    "issue_title": "ACDT #82",
                    "start_time": "2026-06-08T14:00:00Z",
                    "duration": 60,
                },
            ],
        }
    }

    target = select_recording_target(
        mapping,
        "acdt",
        max_age_days=3,
        now=datetime(2026, 6, 1, 16, tzinfo=timezone.utc),
    )

    assert target is not None
    assert target.number == 81
    assert target.issue_number == 2085
    assert target.meeting_id == "88479308162"


def test_select_recording_target_can_force_public_number():
    mapping = {
        "acdt": {
            "meeting_id": "88479308162",
            "occurrences": [
                {
                    "occurrence_number": 80,
                    "issue_number": 2049,
                    "issue_title": "ACDT #80",
                    "start_time": "2026-05-18T14:00:00Z",
                    "duration": 60,
                },
                {
                    "occurrence_number": 81,
                    "issue_number": 2085,
                    "issue_title": "ACDT #81",
                    "start_time": "2026-06-01T14:00:00Z",
                    "duration": 60,
                },
            ],
        }
    }

    target = select_recording_target(mapping, "acdt", number=80)

    assert target is not None
    assert target.number == 80
    assert target.issue_number == 2049


def test_build_ffmpeg_command_uses_first_and_last_45_seconds_of_bumper():
    command = build_ffmpeg_command(
        Path("ev.mp4"),
        Path("zoom.mp4"),
        Path("out.mp4"),
        bumper_duration=318.8,
    )

    command_text = " ".join(command)

    assert command[:6] == ["ffmpeg", "-y", "-hide_banner", "-i", "ev.mp4", "-i"]
    assert "trim=start=0:end=45.000000" in command_text
    assert "[1:v]trim=start=0.000000" in command_text
    assert "trim=start=273.800000:end=318.800000" in command_text
    assert "concat=n=3:v=1:a=1" in command_text
    assert "libx264" in command
    assert "+faststart" in command


def test_build_ffmpeg_command_rejects_short_bumper():
    with pytest.raises(ValueError, match="Bumper must be at least 90 seconds"):
        build_ffmpeg_command(
            Path("ev.mp4"),
            Path("zoom.mp4"),
            Path("out.mp4"),
            bumper_duration=80,
        )


def test_build_ffmpeg_command_uses_separate_zoom_audio_when_available():
    command = build_ffmpeg_command(
        Path("ev.mp4"),
        Path("zoom.mp4"),
        Path("out.mp4"),
        bumper_duration=318.8,
        zoom_audio_path=Path("zoom.m4a"),
    )

    command_text = " ".join(command)

    assert command[:8] == ["ffmpeg", "-y", "-hide_banner", "-i", "ev.mp4", "-i", "zoom.mp4", "-i"]
    assert "zoom.m4a" in command
    assert "[2:a]atrim=start=0.000000,asetpts=PTS-STARTPTS" in command_text


def test_build_ffmpeg_command_trims_zoom_segment_when_requested():
    command = build_ffmpeg_command(
        Path("ev.mp4"),
        Path("zoom.mp4"),
        Path("out.mp4"),
        bumper_duration=318.8,
        zoom_audio_path=Path("zoom.m4a"),
        zoom_trim=ZoomTrimWindow(start_seconds=12.5, end_seconds=130.25),
    )

    command_text = " ".join(command)

    assert "[1:v]trim=start=12.500000:end=130.250000" in command_text
    assert "[2:a]atrim=start=12.500000:end=130.250000" in command_text


def test_select_recording_files_prefers_required_caption_layout_and_largest_audio():
    selected = select_recording_files(
        {
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_speaker_view",
                    "download_url": "https://example.com/screen-speaker.mp4",
                    "file_size": 100_000_000,
                },
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_speaker_view(CC)",
                    "download_url": "https://example.com/screen-speaker-cc.mp4",
                    "file_size": 10_000,
                },
                {
                    "file_type": "M4A",
                    "recording_type": "audio_only",
                    "download_url": "https://example.com/small.m4a",
                    "file_size": 1_000,
                },
                {
                    "file_type": "M4A",
                    "recording_type": "audio_only",
                    "download_url": "https://example.com/audio.m4a",
                    "file_size": 9_000_000,
                },
            ]
        }
    )

    assert selected is not None
    assert selected.video_file["download_url"] == "https://example.com/screen-speaker-cc.mp4"
    assert selected.audio_file is not None
    assert selected.audio_file["download_url"] == "https://example.com/audio.m4a"


def test_select_recording_files_falls_back_to_active_speaker_without_shared_screen():
    selected = select_recording_files(
        {
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "active_speaker",
                    "download_url": "https://example.com/active-speaker.mp4",
                    "file_size": 100_000_000,
                },
                {
                    "file_type": "MP4",
                    "recording_type": "gallery_view",
                    "download_url": "https://example.com/gallery.mp4",
                    "file_size": 9_000,
                },
            ]
        }
    )

    assert selected is not None
    assert selected.video_file["download_url"] == "https://example.com/active-speaker.mp4"


def test_select_recording_files_rejects_unknown_video_layouts():
    selected = select_recording_files(
        {
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "unknown_layout",
                    "download_url": "https://example.com/unknown.mp4",
                    "file_size": 100_000_000,
                },
            ]
        }
    )

    assert selected is None


def test_extract_peak_level_db_returns_loudest_finite_peak():
    output = """
    [Parsed_astats_0] Peak level dB: -inf
    [Parsed_astats_0] Peak level dB: -42.10
    [Parsed_astats_0] Peak level dB: -18.25
    """

    assert extract_peak_level_db(output) == -18.25


def test_transcript_speech_window_uses_first_and_last_vtt_cues_with_padding():
    transcript = """WEBVTT

00:00:18.000 --> 00:00:20.000
Speaker: hello

00:15:00.000 --> 00:15:12.500
Speaker: bye
"""

    window = transcript_speech_window(transcript, duration_seconds=1000, padding_seconds=10)

    assert window == ZoomTrimWindow(start_seconds=8, end_seconds=922.5)


def test_composed_recording_sync_uses_bumper_and_transcript_trim():
    transcript = """WEBVTT

00:00:43.940 --> 00:00:45.659
Speaker: hello
"""

    assert composed_recording_sync_from_transcript(transcript) == {
        "transcriptStartTime": "00:00:43",
        "videoStartTime": "00:00:54",
    }


def test_composed_recording_sync_can_have_video_before_transcript():
    transcript = """WEBVTT

00:04:47.490 --> 00:04:50.980
Speaker: started
"""

    assert composed_recording_sync_from_transcript(transcript) == {
        "transcriptStartTime": "00:04:47",
        "videoStartTime": "00:00:55",
    }
