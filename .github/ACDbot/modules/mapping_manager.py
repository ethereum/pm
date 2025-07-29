"""
Mapping Manager Module

Handles operations on the meeting_topic_mapping.json file for the new data structure.
Provides clean, focused operations for managing call series and occurrences.
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime


class MappingManager:
    """Manages operations on the meeting_topic_mapping.json file."""

    def __init__(self, mapping_file_path: str = ".github/ACDbot/meeting_topic_mapping.json"):
        self.mapping_file_path = mapping_file_path
        self.mapping = self.load_mapping()

    def load_mapping(self) -> Dict:
        """Load the mapping file."""
        try:
            with open(self.mapping_file_path, 'r') as f:
                mapping = json.load(f)
            print(f"[DEBUG] Loaded mapping with {len(mapping)} entries")
            return mapping
        except FileNotFoundError:
            print(f"[WARNING] Mapping file not found at {self.mapping_file_path}, creating new mapping")
            return {}
        except json.JSONDecodeError as e:
            print(f"[ERROR] Failed to parse mapping file: {e}")
            return {}

    def save_mapping(self) -> bool:
        """Save the mapping file."""
        try:
            # Ensure the directory exists (this should be part of the repository)
            directory = os.path.dirname(self.mapping_file_path)
            if not os.path.exists(directory):
                print(f"[ERROR] Directory {directory} does not exist. The mapping file should be part of the repository.")
                return False

            with open(self.mapping_file_path, 'w') as f:
                json.dump(self.mapping, f, indent=2)
            print(f"[DEBUG] Saved mapping to {self.mapping_file_path}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to save mapping: {e}")
            return False

    def get_call_series(self, call_series: str) -> Optional[Dict]:
        """Get a call series entry from the mapping."""
        if call_series == "one-off":
            return self.mapping.get("one-off", {})
        else:
            return self.mapping.get(call_series)

    def create_call_series_entry(self, call_series: str, meeting_id: str, is_recurring: bool,
                                occurrence_rate: str, duration: int) -> Dict:
        """Create a new call series entry."""
        entry = {
            "call_series": call_series,
            "meeting_id": meeting_id,
            "is_recurring": is_recurring,
            "occurrence_rate": occurrence_rate,
            "occurrences": []
        }

        # Add duration if provided
        if duration:
            entry["duration"] = duration

        return entry

    def add_occurrence(self, call_series: str, occurrence_data: Dict) -> bool:
        """Add a new occurrence to a call series."""
        try:
            if call_series == "one-off":
                # Handle one-off calls
                if "one-off" not in self.mapping:
                    self.mapping["one-off"] = {}

                meeting_id = occurrence_data.get("meeting_id")
                if not meeting_id:
                    print("[ERROR] One-off calls require a meeting_id")
                    return False

                self.mapping["one-off"][meeting_id] = occurrence_data
                print(f"[DEBUG] Added one-off occurrence with meeting_id: {meeting_id}")
            else:
                # Handle recurring calls
                if call_series not in self.mapping:
                    # Create new call series entry
                    self.mapping[call_series] = self.create_call_series_entry(
                        call_series=call_series,
                        meeting_id=occurrence_data.get("meeting_id", "placeholder"),
                        is_recurring=occurrence_data.get("is_recurring", True),
                        occurrence_rate=occurrence_data.get("occurrence_rate", "other"),
                        duration=occurrence_data.get("duration")
                    )

                # Add occurrence to the series
                if "occurrences" not in self.mapping[call_series]:
                    self.mapping[call_series]["occurrences"] = []

                # Set occurrence number
                occurrence_number = len(self.mapping[call_series]["occurrences"]) + 1
                occurrence_data["occurrence_number"] = occurrence_number

                self.mapping[call_series]["occurrences"].append(occurrence_data)
                print(f"[DEBUG] Added occurrence #{occurrence_number} to call series: {call_series}")

            return True
        except Exception as e:
            print(f"[ERROR] Failed to add occurrence: {e}")
            return False

    def update_occurrence(self, call_series: str, issue_number: int, update_data: Dict) -> bool:
        """Update an existing occurrence."""
        try:
            if call_series == "one-off":
                # Handle one-off calls
                if "one-off" not in self.mapping:
                    return False

                # Find the one-off entry with matching issue number
                for meeting_id, entry in self.mapping["one-off"].items():
                    if entry.get("issue_number") == issue_number:
                        entry.update(update_data)
                        print(f"[DEBUG] Updated one-off occurrence for issue #{issue_number}")
                        return True

                print(f"[WARNING] One-off occurrence for issue #{issue_number} not found")
                return False
            else:
                # Handle recurring calls
                if call_series not in self.mapping:
                    return False

                # Find the occurrence with matching issue number
                for occurrence in self.mapping[call_series].get("occurrences", []):
                    if occurrence.get("issue_number") == issue_number:
                        occurrence.update(update_data)
                        print(f"[DEBUG] Updated occurrence for issue #{issue_number} in call series: {call_series}")
                        return True

                print(f"[WARNING] Occurrence for issue #{issue_number} not found in call series: {call_series}")
                return False
        except Exception as e:
            print(f"[ERROR] Failed to update occurrence: {e}")
            return False

    def find_occurrence(self, issue_number: int) -> Optional[Dict]:
        """Find an occurrence by issue number across all call series."""
        # Check one-off calls first
        if "one-off" in self.mapping:
            for meeting_id, entry in self.mapping["one-off"].items():
                if isinstance(entry, dict) and entry.get("issue_number") == issue_number:
                    return {"call_series": "one-off", "meeting_id": meeting_id, "occurrence": entry}

        # Check recurring calls
        for call_series, entry in self.mapping.items():
            if call_series == "one-off":
                continue

            # Skip if entry is not a dictionary (e.g., string values from test fixtures)
            if not isinstance(entry, dict):
                continue

            for occurrence in entry.get("occurrences", []):
                if occurrence.get("issue_number") == issue_number:
                    return {"call_series": call_series, "meeting_id": entry.get("meeting_id"), "occurrence": occurrence}

        return None

    def get_series_meeting_id(self, call_series: str) -> Optional[str]:
        """Get the meeting ID for a call series."""
        if call_series == "one-off":
            return None  # One-off calls don't have a series meeting ID

        series_entry = self.mapping.get(call_series)
        if series_entry:
            meeting_id = series_entry.get("meeting_id")
            if meeting_id and not str(meeting_id).startswith("placeholder"):
                return meeting_id

        return None

    def set_series_meeting_id(self, call_series: str, meeting_id: str) -> bool:
        """Set the meeting ID for a call series."""
        if call_series == "one-off":
            print("[WARNING] Cannot set series meeting ID for one-off calls")
            return False

        if call_series not in self.mapping:
            print(f"[WARNING] Call series '{call_series}' not found in mapping")
            return False

        self.mapping[call_series]["meeting_id"] = meeting_id
        print(f"[DEBUG] Set meeting ID '{meeting_id}' for call series: {call_series}")
        return True

    def get_series_calendar_event_id(self, call_series: str) -> Optional[str]:
        """Get the calendar event ID for a call series."""
        if call_series == "one-off":
            return None

        series_entry = self.mapping.get(call_series)
        if series_entry:
            return series_entry.get("calendar_event_id")

        return None

    def set_series_calendar_event_id(self, call_series: str, calendar_event_id: str) -> bool:
        """Set the calendar event ID for a call series."""
        if call_series == "one-off":
            print("[WARNING] Cannot set series calendar event ID for one-off calls")
            return False

        if call_series not in self.mapping:
            print(f"[WARNING] Call series '{call_series}' not found in mapping")
            return False

        self.mapping[call_series]["calendar_event_id"] = calendar_event_id
        print(f"[DEBUG] Set calendar event ID '{calendar_event_id}' for call series: {call_series}")
        return True

    def get_series_uuid(self, call_series: str) -> Optional[str]:
        """Get the UUID for a call series."""
        if call_series == "one-off":
            return None

        series_entry = self.mapping.get(call_series)
        if series_entry:
            return series_entry.get("uuid")

        return None

    def set_series_uuid(self, call_series: str, uuid: str) -> bool:
        """Set the UUID for a call series."""
        if call_series == "one-off":
            print("[WARNING] Cannot set series UUID for one-off calls")
            return False

        if call_series not in self.mapping:
            print(f"[WARNING] Call series '{call_series}' not found in mapping")
            return False

        self.mapping[call_series]["uuid"] = uuid
        print(f"[DEBUG] Set UUID '{uuid}' for call series: {call_series}")
        return True

    def create_occurrence_data(self, issue_number: int, issue_title: str, discourse_topic_id: Optional[int],
                              start_time: str, duration: int, **kwargs) -> Dict:
        """Create occurrence data structure."""
        occurrence_data = {
            "issue_number": issue_number,
            "issue_title": issue_title,
            "start_time": start_time,
            "duration": duration,
            "skip_youtube_upload": kwargs.get("skip_youtube_upload", False),
            "skip_transcript_processing": kwargs.get("skip_transcript_processing", False),
            "youtube_upload_processed": False,
            "transcript_processed": False,
            "upload_attempt_count": 0,
            "transcript_attempt_count": 0,
            "telegram_message_id": None,
            "youtube_streams_posted_to_discourse": False,
            "youtube_streams": kwargs.get("youtube_streams")
        }

        # Add discourse topic ID if provided
        if discourse_topic_id:
            occurrence_data["discourse_topic_id"] = discourse_topic_id

        # Add meeting_id for one-off calls
        if kwargs.get("meeting_id"):
            occurrence_data["meeting_id"] = kwargs["meeting_id"]

        # Add calendar event ID for one-off calls
        if kwargs.get("calendar_event_id"):
            occurrence_data["calendar_event_id"] = kwargs["calendar_event_id"]

        return occurrence_data

    def validate_mapping_structure(self) -> List[str]:
        """Validate the mapping structure and return any issues found."""
        issues = []

        for call_series, entry in self.mapping.items():
            if call_series == "one-off":
                # Validate one-off structure
                if not isinstance(entry, dict):
                    issues.append(f"one-off entry is not a dictionary")
                    continue

                for meeting_id, one_off_entry in entry.items():
                    if not isinstance(one_off_entry, dict):
                        issues.append(f"one-off/{meeting_id} entry is not a dictionary")
                        continue

                    # Check required fields
                    required_fields = ["issue_number", "issue_title", "start_time", "duration"]
                    for field in required_fields:
                        if field not in one_off_entry:
                            issues.append(f"one-off/{meeting_id} missing required field: {field}")
            else:
                # Validate recurring call structure
                if not isinstance(entry, dict):
                    issues.append(f"call series '{call_series}' entry is not a dictionary")
                    continue

                # Check required fields
                required_fields = ["call_series", "is_recurring", "occurrence_rate"]
                for field in required_fields:
                    if field not in entry:
                        issues.append(f"call series '{call_series}' missing required field: {field}")

                # Check occurrences
                if "occurrences" not in entry:
                    issues.append(f"call series '{call_series}' missing occurrences list")
                elif not isinstance(entry["occurrences"], list):
                    issues.append(f"call series '{call_series}' occurrences is not a list")
                else:
                    # Validate each occurrence
                    for i, occurrence in enumerate(entry["occurrences"]):
                        if not isinstance(occurrence, dict):
                            issues.append(f"call series '{call_series}' occurrence {i} is not a dictionary")
                            continue

                        # Check required occurrence fields
                        required_occurrence_fields = ["issue_number", "issue_title", "start_time", "duration"]
                        for field in required_occurrence_fields:
                            if field not in occurrence:
                                issues.append(f"call series '{call_series}' occurrence {i} missing required field: {field}")

        return issues