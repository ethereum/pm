"""
Mapping Manager Module

Handles operations on the meeting_topic_mapping.json file for the new data structure.
Provides clean, focused operations for managing call series and occurrences.
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime
try:
    from .logging_config import get_logger, should_log_debug
except ImportError:
    # Fallback for when logging_config is not available
    import logging
    def get_logger():
        return logging.getLogger(__name__)
    def should_log_debug():
        return os.getenv('ACDBOT_LOG_LEVEL', 'INFO').upper() == 'DEBUG'


class MappingManager:
    """Manages operations on the meeting_topic_mapping.json file."""

    def __init__(self, mapping_file_path: str = ".github/ACDbot/meeting_topic_mapping.json"):
        self.mapping_file_path = mapping_file_path
        self.logger = get_logger()
        self.mapping = self.load_mapping()

    def load_mapping(self) -> Dict:
        """Load the mapping file."""
        try:
            with open(self.mapping_file_path, 'r') as f:
                mapping = json.load(f)
            self.logger.info(f"Loaded mapping with {len(mapping)} entries")
            return mapping
        except FileNotFoundError:
            self.logger.warning(f"Mapping file not found at {self.mapping_file_path}, creating new mapping")
            return {}
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse mapping file: {e}")
            return {}

    def save_mapping(self) -> bool:
        """Save the mapping file."""
        try:
            # Ensure the directory exists (this should be part of the repository)
            directory = os.path.dirname(self.mapping_file_path)
            if not os.path.exists(directory):
                self.logger.error(f"Directory {directory} does not exist. The mapping file should be part of the repository.")
                return False

            with open(self.mapping_file_path, 'w') as f:
                json.dump(self.mapping, f, indent=2)
            self.logger.debug(f"Saved mapping to {self.mapping_file_path}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to save mapping: {e}")
            return False

    def get_call_series(self, call_series: str) -> Optional[Dict]:
        """Get a call series entry from the mapping."""
        return self.mapping.get(call_series)

    def create_call_series_entry(self, call_series: str, meeting_id: str,
                                occurrence_rate: str, duration: int) -> Dict:
        """Create a new call series entry."""
        entry = {
            "call_series": call_series,
            "meeting_id": meeting_id,
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
            if call_series not in self.mapping:
                # Create new call series entry
                self.mapping[call_series] = self.create_call_series_entry(
                    call_series=call_series,
                    meeting_id="pending",  # Will be updated to real meeting ID or "custom" based on user choice
                    occurrence_rate=occurrence_data.get("occurrence_rate", "other"),
                    duration=occurrence_data.get("duration")
                )
            else:
                # Ensure existing series has a meeting_id field
                if "meeting_id" not in self.mapping[call_series]:
                    self.mapping[call_series]["meeting_id"] = "pending"

            # Add occurrence to the series
            if "occurrences" not in self.mapping[call_series]:
                self.mapping[call_series]["occurrences"] = []

            # Set occurrence number
            occurrence_number = len(self.mapping[call_series]["occurrences"]) + 1
            occurrence_data["occurrence_number"] = occurrence_number

            self.mapping[call_series]["occurrences"].append(occurrence_data)
            self.logger.debug(f"Added occurrence #{occurrence_number} to call series: {call_series}")

            return True
        except Exception as e:
            self.logger.error(f"Failed to add occurrence: {e}")
            return False

    def update_occurrence(self, call_series: str, issue_number: int, update_data: Dict) -> bool:
        """Update an existing occurrence."""
        try:
            if call_series not in self.mapping:
                return False

            # Find the occurrence with matching issue number
            for occurrence in self.mapping[call_series].get("occurrences", []):
                if occurrence.get("issue_number") == issue_number:
                    occurrence.update(update_data)
                    self.logger.debug(f"Updated occurrence for issue #{issue_number} in call series: {call_series}")
                    return True

            self.logger.warning(f"Occurrence for issue #{issue_number} not found in call series: {call_series}")
            return False
        except Exception as e:
            self.logger.error(f"Failed to update occurrence: {e}")
            return False

    def find_occurrence(self, issue_number: int) -> Optional[Dict]:
        """Find an occurrence by issue number across all call series."""
        if should_log_debug():
            self.logger.debug(f"Searching for issue #{issue_number} in mapping")

        # Check all call series
        for call_series, entry in self.mapping.items():
            # Skip if entry is not a dictionary (e.g., string values from test fixtures)
            if not isinstance(entry, dict):
                continue

            occurrences = entry.get("occurrences", [])
            # Removed verbose "Checking call series" logging - this was the main source of noise

            for occurrence in occurrences:
                if occurrence.get("issue_number") == issue_number:
                    if should_log_debug():
                        self.logger.debug(f"Found issue #{issue_number} in call series '{call_series}'")
                    return {"call_series": call_series, "meeting_id": entry.get("meeting_id"), "occurrence": occurrence}

        if should_log_debug():
            self.logger.debug(f"Issue #{issue_number} not found in any call series")
        return None

    def get_series_meeting_id(self, call_series: str) -> Optional[str]:
        """Get the meeting ID for a call series."""
        series_entry = self.mapping.get(call_series)
        if series_entry:
            meeting_id = series_entry.get("meeting_id")
            if meeting_id and not str(meeting_id).startswith("placeholder") and meeting_id not in ["custom", "pending"]:
                return meeting_id

        return None

    def set_series_meeting_id(self, call_series: str, meeting_id: str) -> bool:
        """Set the meeting ID for a call series."""
        if call_series not in self.mapping:
            self.logger.warning(f"Call series '{call_series}' not found in mapping")
            return False

        self.mapping[call_series]["meeting_id"] = str(meeting_id)
        self.logger.debug(f"Set meeting ID '{meeting_id}' for call series: {call_series}")
        return True

    def set_series_custom_meeting(self, call_series: str) -> bool:
        """Set the meeting ID to 'custom' when user opts out of Zoom creation."""
        if call_series not in self.mapping:
            self.logger.warning(f"Call series '{call_series}' not found in mapping")
            return False

        self.mapping[call_series]["meeting_id"] = "custom"
        self.logger.debug(f"Set meeting ID to 'custom' for call series: {call_series} (user opted out of Zoom)")
        return True

    def get_series_calendar_event_id(self, call_series: str) -> Optional[str]:
        """Get the calendar event ID for a call series."""
        series_entry = self.mapping.get(call_series)
        if series_entry:
            return series_entry.get("calendar_event_id")

        return None

    def set_series_calendar_event_id(self, call_series: str, calendar_event_id: str) -> bool:
        """Set the calendar event ID for a call series."""
        if call_series not in self.mapping:
            self.logger.warning(f"Call series '{call_series}' not found in mapping")
            return False

        self.mapping[call_series]["calendar_event_id"] = calendar_event_id
        self.logger.debug(f"Set calendar event ID '{calendar_event_id}' for call series: {call_series}")
        return True

    def get_series_uuid(self, call_series: str) -> Optional[str]:
        """Get the UUID for a call series."""
        series_entry = self.mapping.get(call_series)
        if series_entry:
            return series_entry.get("uuid")

        return None

    def set_series_uuid(self, call_series: str, uuid: str) -> bool:
        """Set the UUID for a call series."""
        if call_series not in self.mapping:
            self.logger.warning(f"Call series '{call_series}' not found in mapping")
            return False

        self.mapping[call_series]["uuid"] = uuid
        self.logger.debug(f"Set UUID '{uuid}' for call series: {call_series}")
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

        return occurrence_data

    def validate_mapping_structure(self) -> List[str]:
        """Validate the mapping structure and return any issues found."""
        issues = []

        for call_series, entry in self.mapping.items():
            # Validate all call series structure uniformly
            if not isinstance(entry, dict):
                issues.append(f"call series '{call_series}' entry is not a dictionary")
                continue

            # Check required fields
            required_fields = ["call_series", "occurrence_rate"]
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