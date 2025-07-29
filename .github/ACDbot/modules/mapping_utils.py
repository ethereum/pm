"""
Mapping Utilities

Helper functions for working with the new meeting_topic_mapping.json structure
where keys are call series names instead of Zoom IDs.
"""

import json
import os
from typing import Dict, Optional, List, Any


def load_mapping(mapping_file_path: str = ".github/ACDbot/meeting_topic_mapping.json") -> Dict:
    """Load the meeting topic mapping from file."""
    if os.path.exists(mapping_file_path):
        with open(mapping_file_path, "r") as f:
            return json.load(f)
    return {}


def save_mapping(mapping: Dict, mapping_file_path: str = ".github/ACDbot/meeting_topic_mapping.json"):
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

    for call_series, series_data in mapping.items():
        if call_series == "one-off":
            # Check one-off entries (meeting_id is the key)
            if meeting_id in series_data:
                return series_data[meeting_id]
        else:
            # For recurring series, check both root level and occurrences
            # Ensure series_data is a dictionary
            if not isinstance(series_data, dict):
                continue

            if series_data.get("meeting_id") == meeting_id:
                return series_data

            # Check occurrences for meeting_id overrides
            for occurrence in series_data.get("occurrences", []):
                if occurrence.get("meeting_id") == meeting_id:
                    return occurrence

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
    for call_series, series_data in mapping.items():
        if call_series == "one-off":
            # Check one-off entries
            for zoom_id, entry_data in series_data.items():
                if entry_data.get("issue_number") == issue_number:
                    return entry_data
        else:
            # Check recurring series occurrences
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
    if not series_data or call_series == "one-off":
        return None

    for occurrence in series_data.get("occurrences", []):
        if occurrence.get("issue_number") == issue_number:
            return occurrence

    return None


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
        occurrence.update(updates)
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
            "is_recurring": True,
            "occurrences": []
        }

    mapping[call_series]["occurrences"].append(occurrence_data)
    return True


# Removed unused functions: get_all_meeting_ids, get_all_occurrences, find_meeting_with_recording
# These functions are not used by any existing scripts and can be added back if needed later


def get_effective_meeting_id(call_series: str, issue_number: int, mapping: Dict) -> Optional[str]:
    """
    Get the effective meeting ID for a specific occurrence.

    This function implements the hybrid approach:
    - If occurrence has its own meeting_id, use that
    - Otherwise, fall back to the root level meeting_id
    - If neither exists, return None

    Args:
        call_series: The call series name
        issue_number: The GitHub issue number
        mapping: The mapping dictionary

    Returns:
        The effective meeting ID, or None if not found
    """
    series_data = mapping.get(call_series)
    if not series_data:
        return None

    if call_series == "one-off":
        # For one-off calls, meeting_id is the key
        for meeting_id, entry_data in series_data.items():
            if entry_data.get("issue_number") == issue_number:
                return str(meeting_id)
        return None

    # For recurring series, find the occurrence
    occurrence = find_occurrence_by_issue_number(call_series, issue_number, mapping)
    if not occurrence:
        return None

    # Check if occurrence has its own meeting_id (override)
    occurrence_meeting_id = occurrence.get("meeting_id")
    if occurrence_meeting_id:
        return str(occurrence_meeting_id)

    # Fall back to root level meeting_id
    root_meeting_id = series_data.get("meeting_id")
    if root_meeting_id:
        return str(root_meeting_id)

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

            if call_series == "one-off":
                # One-off entries should have meeting_id as keys
                for zoom_id, entry_data in series_data.items():
                    if not isinstance(entry_data, dict):
                        return False
                    if "issue_number" not in entry_data:
                        return False
            else:
                # Recurring series should have call_series and occurrences
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