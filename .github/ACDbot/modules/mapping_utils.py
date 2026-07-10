"""
Mapping Utilities

Helper functions for working with the new meeting_topic_mapping.json structure
where keys are call series names instead of Zoom IDs.
"""

import json
import os
from pathlib import Path
from typing import Dict, Iterator, Optional, List, Any, Tuple

MAPPING_FILE_PATH = Path(__file__).resolve().parent.parent / "meeting_topic_mapping.json"


def iter_breakout_meetings(series_data: Optional[Dict]) -> Iterator[Tuple[str, str]]:
    """Yield ``(label, meeting_id)`` for each linked breakout meeting on a series.

    Breakout rooms held in a separate Zoom meeting (e.g. the ACDT "CL" breakout)
    are linked via the ``breakout_meeting_ids`` field on a series entry. Entries
    without a usable Zoom meeting id are skipped: a valid Zoom meeting id is
    numeric, so empty values and not-yet-filled placeholders are ignored.
    """
    breakout_meeting_ids = (series_data or {}).get("breakout_meeting_ids") or {}
    for label, meeting_id in breakout_meeting_ids.items():
        meeting_id_str = str(meeting_id).strip()
        if meeting_id_str.isdigit():
            yield label, meeting_id_str


def get_breakout_youtube_state(occurrence: Dict, breakout_label: str) -> Dict:
    """Return upload state for one breakout without mutating the occurrence."""
    breakout_youtube = occurrence.get("breakout_youtube")
    if not isinstance(breakout_youtube, dict):
        return {}
    state = breakout_youtube.get(breakout_label)
    return state if isinstance(state, dict) else {}


def ensure_breakout_youtube_state(occurrence: Dict, breakout_label: str) -> Dict:
    """Create and return upload state for one breakout label."""
    breakout_youtube = occurrence.setdefault("breakout_youtube", {})
    if not isinstance(breakout_youtube, dict):
        raise ValueError("breakout_youtube must be an object")
    state = breakout_youtube.setdefault(breakout_label, {})
    if not isinstance(state, dict):
        raise ValueError(f"breakout_youtube.{breakout_label} must be an object")
    return state


def load_mapping(mapping_file_path: str | os.PathLike = MAPPING_FILE_PATH) -> Dict:
    """Load the meeting topic mapping from file."""
    if os.path.exists(mapping_file_path):
        with open(mapping_file_path, "r") as f:
            return json.load(f)
    return {}


def save_mapping(mapping: Dict, mapping_file_path: str | os.PathLike = MAPPING_FILE_PATH):
    """Save the meeting topic mapping to file."""
    with open(mapping_file_path, "w") as f:
        json.dump(mapping, f, indent=2)


def find_meeting_by_id(meeting_id: str, mapping: Dict) -> Optional[Dict]:
    """
    Find meeting entry by Zoom meeting ID in new structure.

    Args:
        meeting_id: The Zoom meeting ID to search for
        mapping: The mapping dictionary

    Returns:
        The meeting entry if found, None otherwise
    """
    meeting_id = str(meeting_id)

    for _, series_data in mapping.items():
        if not isinstance(series_data, dict):
            continue
        if series_data.get("meeting_id") == meeting_id:
            return series_data

    return None


def find_meeting_by_issue_number(issue_number: int, mapping: Dict) -> Optional[Dict]:
    """
    Find meeting entry by GitHub issue number in new structure.

    Args:
        issue_number: The GitHub issue number to search for
        mapping: The mapping dictionary

    Returns:
        The meeting entry if found, None otherwise
    """
    for _, series_data in mapping.items():
        for occurrence in series_data.get("occurrences", []):
            if occurrence.get("issue_number") == issue_number:
                return occurrence

    return None


def find_series_by_call_series(call_series: str, mapping: Dict) -> Optional[Dict]:
    """
    Find series entry by call series name.

    Args:
        call_series: The call series name to search for
        mapping: The mapping dictionary

    Returns:
        The series entry if found, None otherwise
    """
    return mapping.get(call_series)


def find_occurrence_by_issue_number(call_series: str, issue_number: int, mapping: Dict) -> Optional[Dict]:
    """
    Find specific occurrence within a call series by issue number.

    Args:
        call_series: The call series name
        issue_number: The GitHub issue number
        mapping: The mapping dictionary

    Returns:
        The occurrence entry if found, None otherwise
    """
    series_data = mapping.get(call_series)
    if not series_data:
        return None

    for occurrence in series_data.get("occurrences", []):
        if occurrence.get("issue_number") == issue_number:
            return occurrence

    return None


def find_occurrence_with_index(call_series: str, issue_number: int, mapping: Dict) -> Tuple[Optional[Dict], int]:
    """
    Find specific occurrence and its index within a call series by issue number.

    Returns a tuple of (occurrence or None, index or -1).
    """
    series_data = mapping.get(call_series)
    if not series_data:
        return None, -1

    occurrences = series_data.get("occurrences", [])
    for idx, occurrence in enumerate(occurrences):
        if occurrence.get("issue_number") == issue_number:
            return occurrence, idx
    return None, -1


def update_meeting_entry(meeting_id: str, updates: Dict, mapping: Dict) -> bool:
    """
    Update meeting entry in new structure.

    Args:
        meeting_id: The Zoom meeting ID to update
        updates: Dictionary of fields to update
        mapping: The mapping dictionary

    Returns:
        True if update was successful, False otherwise
    """
    entry = find_meeting_by_id(meeting_id, mapping)
    if entry:
        entry.update(updates)
        return True
    return False


def update_occurrence_entry(call_series: str, issue_number: int, updates: Dict, mapping: Dict) -> bool:
    """
    Update occurrence entry within a call series.

    Args:
        call_series: The call series name
        issue_number: The GitHub issue number
        updates: Dictionary of fields to update
        mapping: The mapping dictionary

    Returns:
        True if update was successful, False otherwise
    """
    occurrence = find_occurrence_by_issue_number(call_series, issue_number, mapping)
    if occurrence:
        # Safelist of allowed fields that can be updated in mapping
        ALLOWED_UPDATE_FIELDS = {
            "issue_title", "start_time", "duration", "skip_youtube_upload",
            "skip_transcript_processing", "youtube_upload_processed", "transcript_processed",
            "upload_attempt_count", "transcript_attempt_count", "telegram_message_id",
            "youtube_streams_posted_to_discourse", "youtube_streams", "discourse_topic_id",
            "calendar_event_id", "occurrence_number", "youtube_video_id", "breakout_youtube",
            "recording_publication_mode"
        }

        # Filter updates to only include allowed fields
        safe_updates = {k: v for k, v in updates.items() if k in ALLOWED_UPDATE_FIELDS}

        if len(safe_updates) != len(updates):
            rejected_fields = set(updates.keys()) - ALLOWED_UPDATE_FIELDS
            print(f"[WARN] Rejected mapping update for non-allowed fields: {rejected_fields}")

        occurrence.update(safe_updates)
        return True
    return False


def add_occurrence_to_series(call_series: str, occurrence_data: Dict, mapping: Dict) -> bool:
    """
    Add new occurrence to existing series.

    Args:
        call_series: The call series name
        occurrence_data: The occurrence data to add
        mapping: The mapping dictionary

    Returns:
        True if addition was successful, False otherwise
    """
    if call_series not in mapping:
        mapping[call_series] = {
            "call_series": call_series,
            "occurrences": []
        }

    mapping[call_series]["occurrences"].append(occurrence_data)
    return True

def get_effective_meeting_id(call_series: str, issue_number: int, mapping: Dict) -> Optional[str]:
    """
    Get the meeting ID for a specific call series.

    Args:
        call_series: The call series name
        issue_number: The GitHub issue number (unused, kept for API compatibility)
        mapping: The mapping dictionary

    Returns:
        The meeting ID, or None if not found
    """
    series_data = mapping.get(call_series)
    if not series_data:
        return None

    meeting_id = series_data.get("meeting_id")
    if meeting_id:
        return str(meeting_id)

    return None


def find_call_series_by_meeting_id(meeting_id: str, occurrence_issue_number: int, mapping: Dict) -> Optional[str]:
    """
    Find the call series for a given meeting ID.

    Args:
        meeting_id: The Zoom meeting ID to search for
        occurrence_issue_number: The GitHub issue number (unused, kept for API compatibility)
        mapping: The mapping dictionary

    Returns:
        The call series name if found, None otherwise
    """
    meeting_id = str(meeting_id)

    for call_series, series_data in mapping.items():
        if not isinstance(series_data, dict):
            continue

        # Check if this is the series-level meeting ID
        if series_data.get("meeting_id") == meeting_id:
            return call_series

    return None


def validate_mapping_structure(mapping: Dict) -> bool:
    """
    Validate that the mapping follows the expected new structure.

    Args:
        mapping: The mapping dictionary to validate

    Returns:
        True if structure is valid, False otherwise
    """
    try:
        for call_series, series_data in mapping.items():
            if not isinstance(series_data, dict):
                return False

            # All series should have call_series and occurrences
            if "call_series" not in series_data:
                return False
            if "occurrences" not in series_data:
                return False
            if not isinstance(series_data["occurrences"], list):
                return False

            # Validate occurrences
            for occurrence in series_data["occurrences"]:
                if not isinstance(occurrence, dict):
                    return False
                if "issue_number" not in occurrence:
                    return False

        return True
    except Exception:
        return False
