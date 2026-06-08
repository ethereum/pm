"""Pure timing helpers for composed Zoom recording sync."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

VTT_CUE_PATTERN = re.compile(
    r"(?P<start>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})\s+-->\s+"
    r"(?P<end>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})"
)
DEFAULT_BUMPER_CLIP_SECONDS = 45.0


@dataclass(frozen=True)
class ZoomTrimWindow:
    start_seconds: float
    end_seconds: float | None


def parse_vtt_timestamp(value: str) -> float:
    parts = value.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + float(seconds)
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    raise ValueError(f"Unsupported VTT timestamp: {value}")


def transcript_cue_times(transcript_text: str) -> list[tuple[float, float]]:
    return [
        (parse_vtt_timestamp(match.group("start")), parse_vtt_timestamp(match.group("end")))
        for match in VTT_CUE_PATTERN.finditer(transcript_text)
    ]


def transcript_speech_window(
    transcript_text: str,
    duration_seconds: float,
    padding_seconds: float = 10,
) -> ZoomTrimWindow | None:
    cue_times = transcript_cue_times(transcript_text)
    if not cue_times:
        return None

    first_start = min(start for start, _ in cue_times)
    last_end = max(end for _, end in cue_times)
    start_seconds = max(0, first_start - padding_seconds)
    end_seconds = min(duration_seconds, last_end + padding_seconds)
    if end_seconds <= start_seconds:
        return None
    return ZoomTrimWindow(start_seconds=start_seconds, end_seconds=end_seconds)


def format_sync_timestamp(seconds: float) -> str:
    whole_seconds = max(0, math.floor(seconds))
    hours = whole_seconds // 3600
    minutes = (whole_seconds % 3600) // 60
    remaining_seconds = whole_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"


def composed_recording_sync_from_transcript(
    transcript_text: str,
    duration_seconds: float = math.inf,
    bumper_clip_seconds: float = DEFAULT_BUMPER_CLIP_SECONDS,
) -> dict[str, str] | None:
    cue_times = transcript_cue_times(transcript_text)
    if not cue_times:
        return None

    trim_window = transcript_speech_window(transcript_text, duration_seconds=duration_seconds)
    if not trim_window:
        return None

    first_start = min(start for start, _ in cue_times)
    transcript_start_seconds = math.floor(first_start)
    video_transcript_delta_seconds = round(bumper_clip_seconds - trim_window.start_seconds)
    return {
        "transcriptStartTime": format_sync_timestamp(transcript_start_seconds),
        "videoStartTime": format_sync_timestamp(transcript_start_seconds + video_transcript_delta_seconds),
    }
