from datetime import datetime, timezone
from pathlib import Path

from scripts.compose_zoom_sandwich import (
    ZoomTrimWindow,
    build_ffmpeg_command,
    extract_peak_level_db,
    select_occurrence_candidates,
    select_recording_files,
    transcript_speech_window,
)


def test_select_occurrence_candidates_returns_latest_past_occurrences():
    mapping = {
        "acde": {
            "meeting_id": "85451723466",
            "occurrences": [
                {
                    "occurrence_number": 235,
                    "issue_number": 2015,
                    "issue_title": "ACDE #235",
                    "start_time": "2026-04-23T14:00:00Z",
                },
                {
                    "occurrence_number": 236,
                    "issue_number": 2033,
                    "issue_title": "ACDE #236",
                    "start_time": "2026-05-07T14:00:00Z",
                },
                {
                    "occurrence_number": 238,
                    "issue_number": 2050,
                    "issue_title": "ACDE #238",
                    "start_time": "2026-06-04T14:00:00Z",
                },
            ],
        }
    }

    candidates = select_occurrence_candidates(
        mapping,
        "acde",
        now=datetime(2026, 5, 21, tzinfo=timezone.utc),
    )

    assert [candidate.issue_number for candidate in candidates] == [2033, 2015]
    assert candidates[0].meeting_id == "85451723466"
    assert candidates[0].duration_minutes is None


def test_select_occurrence_candidates_can_target_number():
    mapping = {
        "acde": {
            "meeting_id": "85451723466",
            "occurrences": [
                {"occurrence_number": 235, "issue_number": 2015, "start_time": "2026-04-23T14:00:00Z"},
                {"occurrence_number": 236, "issue_number": 2033, "start_time": "2026-05-07T14:00:00Z"},
            ],
        }
    }

    candidates = select_occurrence_candidates(mapping, "acde", number=235)

    assert len(candidates) == 1
    assert candidates[0].issue_number == 2015


def test_build_ffmpeg_command_splits_bumper_and_reencodes():
    command = build_ffmpeg_command(
        Path("ev.mp4"),
        Path("zoom.mp4"),
        Path("out.mp4"),
        bumper_duration=318.8,
    )

    command_text = " ".join(command)

    assert command[:6] == ["ffmpeg", "-y", "-hide_banner", "-i", "ev.mp4", "-i"]
    assert "trim=start=0:end=159.400000" in command_text
    assert "[1:v]trim=start=0.000000" in command_text
    assert "trim=start=159.400000:end=318.800000" in command_text
    assert "concat=n=3:v=1:a=1" in command_text
    assert "libx264" in command
    assert "+faststart" in command


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


def test_select_recording_files_prefers_largest_m4a_for_call_audio():
    selected = select_recording_files(
        {
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_speaker_view",
                    "download_url": "https://example.com/video.mp4",
                    "file_size": 4_400_000,
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
    assert selected.video_file["download_url"] == "https://example.com/video.mp4"
    assert selected.audio_file is not None
    assert selected.audio_file["download_url"] == "https://example.com/audio.m4a"


def test_select_recording_files_prefers_shared_screen_speaker_layout():
    selected = select_recording_files(
        {
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "active_speaker",
                    "download_url": "https://example.com/speaker.mp4",
                    "file_size": 100_000_000,
                },
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_speaker_view",
                    "download_url": "https://example.com/screen-speaker.mp4",
                    "file_size": 10_000,
                },
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_gallery_view",
                    "download_url": "https://example.com/screen-gallery.mp4",
                    "file_size": 9_000,
                },
            ]
        }
    )

    assert selected is not None
    assert selected.video_file["download_url"] == "https://example.com/screen-speaker.mp4"


def test_select_recording_files_accepts_closed_caption_speaker_layout():
    selected = select_recording_files(
        {
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_speaker_view(CC)",
                    "download_url": "https://example.com/screen-speaker-cc.mp4",
                    "file_size": 10_000,
                },
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_gallery_view",
                    "download_url": "https://example.com/screen-gallery.mp4",
                    "file_size": 100_000_000,
                },
            ]
        }
    )

    assert selected is not None
    assert selected.video_file["download_url"] == "https://example.com/screen-speaker-cc.mp4"


def test_select_recording_files_prefers_caption_variant_over_non_caption_layout():
    selected = select_recording_files(
        {
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_speaker_view(CC)",
                    "download_url": "https://example.com/screen-speaker-cc.mp4",
                    "file_size": 100_000_000,
                },
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen_with_speaker_view",
                    "download_url": "https://example.com/screen-speaker.mp4",
                    "file_size": 10_000,
                },
            ]
        }
    )

    assert selected is not None
    assert selected.video_file["download_url"] == "https://example.com/screen-speaker-cc.mp4"


def test_select_recording_files_rejects_non_speaker_composite_layouts():
    selected = select_recording_files(
        {
            "recording_files": [
                {
                    "file_type": "MP4",
                    "recording_type": "speaker_view",
                    "download_url": "https://example.com/speaker.mp4",
                    "file_size": 100_000_000,
                },
                {
                    "file_type": "MP4",
                    "recording_type": "shared_screen",
                    "download_url": "https://example.com/screen.mp4",
                    "file_size": 9_000,
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


def test_extract_peak_level_db_returns_none_for_silence_only():
    output = """
    [Parsed_astats_0] Peak level dB: -inf
    [Parsed_astats_0] Peak level dB: -inf
    """

    assert extract_peak_level_db(output) is None


def test_transcript_speech_window_uses_first_and_last_vtt_cues_with_padding():
    transcript = """WEBVTT

00:00:18.000 --> 00:00:20.000
Speaker: hello

00:15:00.000 --> 00:15:12.500
Speaker: bye
"""

    window = transcript_speech_window(transcript, duration_seconds=1000, padding_seconds=10)

    assert window == ZoomTrimWindow(start_seconds=8, end_seconds=922.5)


def test_transcript_speech_window_clamps_to_recording_duration():
    transcript = """WEBVTT

00:00:05.000 --> 00:00:20.000
Speaker: hello

00:20:00.000 --> 00:20:12.500
Speaker: bye
"""

    window = transcript_speech_window(transcript, duration_seconds=1000, padding_seconds=10)

    assert window == ZoomTrimWindow(start_seconds=0, end_seconds=1000)
