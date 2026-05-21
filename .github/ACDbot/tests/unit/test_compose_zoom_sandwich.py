from datetime import datetime, timezone
from pathlib import Path

from scripts.compose_zoom_sandwich import build_ffmpeg_command, select_occurrence_candidates


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
    assert "trim=start=159.400000:end=318.800000" in command_text
    assert "concat=n=3:v=1:a=1" in command_text
    assert "libx264" in command
    assert "+faststart" in command
