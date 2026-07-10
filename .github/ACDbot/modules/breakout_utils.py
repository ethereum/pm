"""Shared helpers for breakout meetings linked to a parent call occurrence."""

from __future__ import annotations

from collections.abc import Iterable
import re
from typing import Any


def derive_breakout_topic(parent_topic: str, breakout_label: str) -> str:
    """Insert a breakout label before the date portion of a parent title."""
    suffix = f" - {breakout_label.upper()} Breakout"
    for delimiter in (", ", " | "):
        index = parent_topic.find(delimiter)
        if index != -1:
            return parent_topic[:index] + suffix + parent_topic[index:]
    return parent_topic + suffix


def derive_breakout_youtube_title(
    series_abbrev: str,
    parent_topic: str,
    breakout_label: str,
) -> str:
    """Build the compact breakout YouTube title.

    Example: ``ACDT #84 (CL Breakout), June 22, 2026``. The call number and
    trailing date are taken from the parent topic; the series abbreviation
    comes from the call series key (e.g. ``acdt`` -> ``ACDT``).
    """
    number_match = re.search(r"#\s*0*(\d+)", parent_topic)
    number = f" #{number_match.group(1)}" if number_match else ""

    date = ""
    for delimiter in (", ", " | "):
        index = parent_topic.find(delimiter)
        if index != -1:
            date = parent_topic[index + len(delimiter):]
            break

    title = f"{series_abbrev.upper()}{number} ({breakout_label.upper()} Breakout)"
    if date:
        title += f", {date}"
    return title


def _has_required_file_types(
    recording_data: dict[str, Any],
    required_file_types: set[str],
) -> bool:
    available_types = {
        file_info.get("file_type")
        for file_info in recording_data.get("recording_files", [])
    }
    return required_file_types.issubset(available_types)


def select_breakout_recording(
    zoom_client,
    occurrence: dict[str, Any],
    breakout_meeting_id: str,
    min_duration_minutes: int,
    required_file_types: Iterable[str] = (),
) -> dict[str, Any] | None:
    """Select the breakout recording associated with a parent occurrence.

    The breakout is held in its own dedicated Zoom meeting on the same UTC
    calendar date as the parent call. Multiple recordings on that date are
    treated as restarts of the same session, so the longest is selected.
    """
    occurrence_start = occurrence.get("start_time", "")
    if not occurrence_start:
        return None

    target_date = occurrence_start.split("T")[0]
    required_types = set(required_file_types)

    instances = zoom_client.get_past_meeting_instances(breakout_meeting_id)
    if not instances:
        return None

    candidates: list[dict[str, Any]] = []
    for instance in instances:
        start_time = instance.get("start_time", "")
        if not start_time or not start_time.startswith(target_date):
            continue

        uuid = instance.get("uuid")
        if not uuid:
            continue

        recording_data = zoom_client.get_meeting_recording(uuid)
        if not recording_data or not recording_data.get("recording_files"):
            continue
        if recording_data.get("duration", 0) < min_duration_minutes:
            continue
        if required_types and not _has_required_file_types(recording_data, required_types):
            continue

        candidates.append(recording_data)

    if not candidates:
        return None
    return max(candidates, key=lambda recording: recording.get("duration", 0))
