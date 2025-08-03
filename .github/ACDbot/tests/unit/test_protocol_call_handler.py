#!/usr/bin/env python3
"""
Unit tests for ProtocolCallHandler

Focuses on testing the edit detection and resource update logic.
"""

import unittest
import sys
import os

# Add the scripts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'scripts'))

from handle_protocol_call import ProtocolCallHandler


class TestProtocolCallHandler(unittest.TestCase):

    def setUp(self):
        self.handler = ProtocolCallHandler()

        # Sample call data for testing
        self.sample_call_data = {
            "issue_number": 123,
            "issue_title": "Test Protocol Call",
            "call_series": "test-series",
            "start_time": "2024-01-15T10:00:00Z",
            "duration": 60,
            "agenda": "Test agenda",
            "display_zoom_link_in_invite": True,
            "skip_zoom_creation": False,
            "skip_gcal_creation": False,
            "need_youtube_streams": False,
            "occurrence_rate": "other"
        }

        # Sample existing occurrence data - must match sample_call_data exactly
        self.sample_existing_occurrence = {
            "call_series": "test-series",
            "occurrence": {
                "issue_number": 123,
                "issue_title": "Test Protocol Call",
                "start_time": "2024-01-15T10:00:00Z",
                "duration": 60,
                "agenda": "Test agenda",
                "display_zoom_link_in_invite": True,
                "skip_zoom_creation": False,
                "skip_gcal_creation": False,
                "need_youtube_streams": False,
                "occurrence_rate": "other",
                "meeting_id": "test-meeting-id",
                "calendar_event_id": "test-calendar-id",
                "discourse_topic_id": "test-discourse-id"
            }
        }

    def test_detect_field_changes_no_changes(self):
        """Test that no changes are detected when data is identical."""
        result = self.handler._detect_field_changes(
            self.sample_call_data,
            self.sample_existing_occurrence
        )

        # Check that no resources need updating
        self.assertFalse(result.get("update_zoom", False))
        self.assertFalse(result.get("update_calendar", False))
        self.assertFalse(result.get("update_discourse", False))
        self.assertFalse(result.get("update_youtube", False))

    def test_detect_field_changes_start_time_changed(self):
        """Test that start time changes are detected."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["start_time"] = "2024-01-15T11:00:00Z"

        result = self.handler._detect_field_changes(
            modified_call_data,
            self.sample_existing_occurrence
        )

        # Check that affected resources need updating
        self.assertTrue(result.get("update_zoom", False))
        self.assertTrue(result.get("update_calendar", False))
        self.assertTrue(result.get("update_youtube", False))

    def test_detect_field_changes_duration_changed(self):
        """Test that duration changes are detected."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["duration"] = 90

        result = self.handler._detect_field_changes(
            modified_call_data,
            self.sample_existing_occurrence
        )

        # Check that affected resources need updating
        self.assertTrue(result.get("update_zoom", False))
        self.assertTrue(result.get("update_calendar", False))

    def test_detect_field_changes_call_series_changed(self):
        """Test that call series changes are detected."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["call_series"] = "new-test-series"

        result = self.handler._detect_field_changes(
            modified_call_data,
            self.sample_existing_occurrence
        )

        # Check that affected resources need updating
        self.assertTrue(result.get("update_zoom", False))
        self.assertTrue(result.get("update_calendar", False))
        self.assertTrue(result.get("update_youtube", False))

    def test_detect_field_changes_agenda_changed(self):
        """Test that agenda changes are detected."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["agenda"] = "Updated test agenda"

        result = self.handler._detect_field_changes(
            modified_call_data,
            self.sample_existing_occurrence
        )

        # Check that affected resources need updating
        self.assertTrue(result.get("update_calendar", False))
        self.assertTrue(result.get("update_discourse", False))

    def test_detect_field_changes_title_changed(self):
        """Test that issue title changes are detected."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["issue_title"] = "Updated Test Protocol Call"

        result = self.handler._detect_field_changes(
            modified_call_data,
            self.sample_existing_occurrence
        )

        # Check that affected resources need updating
        self.assertTrue(result.get("update_zoom", False))
        self.assertTrue(result.get("update_calendar", False))
        self.assertTrue(result.get("update_discourse", False))

    def test_detect_field_changes_missing_existing_data(self):
        """Test handling of missing existing occurrence data."""
        incomplete_existing = {"call_series": "test-series", "occurrence": {}}

        result = self.handler._detect_field_changes(
            self.sample_call_data,
            incomplete_existing
        )

        # Should detect changes when existing data is missing
        self.assertTrue(result.get("update_zoom", False))
        self.assertTrue(result.get("update_calendar", False))
        self.assertTrue(result.get("update_discourse", False))
        self.assertTrue(result.get("update_youtube", False))

    def test_detect_field_changes_new_issue(self):
        """Test that new issues trigger resource creation."""
        result = self.handler._detect_field_changes(
            self.sample_call_data,
            None  # No existing occurrence
        )

        # Check that resources need creation
        self.assertTrue(result.get("create_zoom", False))
        self.assertTrue(result.get("create_calendar", False))
        self.assertTrue(result.get("create_discourse", False))
        self.assertFalse(result.get("create_youtube", False))  # Not requested

    def test_detect_field_changes_zoom_opt_out(self):
        """Test that zoom opt-out prevents zoom creation."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["skip_zoom_creation"] = True

        result = self.handler._detect_field_changes(
            modified_call_data,
            None  # New issue
        )

        # Check that zoom creation is skipped
        self.assertFalse(result.get("create_zoom", False))

    def test_detect_field_changes_calendar_opt_out(self):
        """Test that calendar opt-out prevents calendar creation."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["skip_gcal_creation"] = True

        result = self.handler._detect_field_changes(
            modified_call_data,
            None  # New issue
        )

        # Check that calendar creation is skipped
        self.assertFalse(result.get("create_calendar", False))

    def test_detect_field_changes_youtube_requested(self):
        """Test that YouTube streams are created when requested."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["need_youtube_streams"] = True

        result = self.handler._detect_field_changes(
            modified_call_data,
            None  # New issue
        )

        # Check that YouTube creation is requested
        self.assertTrue(result.get("create_youtube", False))

    def test_detect_field_changes_zoom_display_changed(self):
        """Test that zoom display setting changes are detected."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["display_zoom_link_in_invite"] = False

        result = self.handler._detect_field_changes(
            modified_call_data,
            self.sample_existing_occurrence
        )

        # Check that calendar needs updating
        self.assertTrue(result.get("update_calendar", False))

    def test_detect_field_changes_occurrence_rate_changed(self):
        """Test that occurrence rate changes are detected."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["occurrence_rate"] = "weekly"

        result = self.handler._detect_field_changes(
            modified_call_data,
            self.sample_existing_occurrence
        )

        # Check that affected resources need updating
        self.assertTrue(result.get("update_zoom", False))
        self.assertTrue(result.get("update_youtube", False))

    def test_resources_changed_all_false(self):
        """Test resources_changed with all false values."""
        resource_results = {
            "zoom_created": False,
            "calendar_created": False,
            "discourse_created": False,
            "youtube_streams_created": False
        }

        result = self.handler._resources_changed(resource_results)
        self.assertFalse(result)

    def test_resources_changed_some_true(self):
        """Test resources_changed with some true values."""
        resource_results = {
            "zoom_created": True,
            "calendar_created": False,
            "discourse_created": True,
            "youtube_streams_created": False
        }

        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_resources_changed_all_true(self):
        """Test resources_changed with all true values."""
        resource_results = {
            "zoom_created": True,
            "calendar_created": True,
            "discourse_created": True,
            "youtube_streams_created": True
        }

        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_resources_changed_missing_keys(self):
        """Test resources_changed with missing keys."""
        resource_results = {
            "zoom_created": True
            # Missing other keys
        }

        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_edge_cases_string_comparison(self):
        """Test edge cases with string comparisons."""
        call_data_with_empty = self.sample_call_data.copy()
        call_data_with_empty["agenda"] = ""

        existing_with_none = {
            "call_series": "test-series",
            "occurrence": {
                "agenda": None,
                "calendar_event_id": "test-calendar-id",
                "discourse_topic_id": "test-discourse-id",
                "duration": 30,
                "issue_number": 123,
                "issue_title": "Test Protocol Call",
                "start_time": "2024-01-15T10:00:00Z"
            }
        }

        result = self.handler._detect_field_changes(
            call_data_with_empty,
            existing_with_none
        )

        # Should detect change between empty string and None
        self.assertTrue(result.get("update_calendar", False))
        self.assertTrue(result.get("update_discourse", False))

    def test_edge_cases_boolean_comparison(self):
        """Test edge cases with boolean comparisons."""
        call_data_false = self.sample_call_data.copy()
        call_data_false["display_zoom_link_in_invite"] = False

        existing_true = {
            "call_series": "test-series",
            "occurrence": {
                "display_zoom_link_in_invite": True,
                "calendar_event_id": "test-calendar-id",
                "discourse_topic_id": "test-discourse-id",
                "duration": 30,
                "issue_number": 123,
                "issue_title": "Test Protocol Call",
                "start_time": "2024-01-15T10:00:00Z"
            }
        }

        result = self.handler._detect_field_changes(
            call_data_false,
            existing_true
        )

        # Should detect change between True and False
        self.assertTrue(result.get("update_calendar", False))

    def test_detect_field_changes_exception_handling(self):
        """Test that exceptions in field detection result in safe failure."""
        # Create a scenario that will cause a real exception
        # Use an existing occurrence with invalid data structure that will cause an AttributeError
        existing_occurrence_with_invalid = {
            "call_series": "test-series",
            "occurrence": None  # This will cause an AttributeError when trying to call .get()
        }

        # This should trigger the exception handling when trying to access .get() on None
        result = self.handler._detect_field_changes(self.sample_call_data, existing_occurrence_with_invalid)

        # Should return safe defaults with error flag
        self.assertFalse(result.get("create_zoom", True))
        self.assertFalse(result.get("create_calendar", True))
        self.assertFalse(result.get("create_discourse", True))
        self.assertFalse(result.get("create_youtube", True))
        self.assertFalse(result.get("update_zoom", True))
        self.assertFalse(result.get("update_calendar", True))
        self.assertFalse(result.get("update_discourse", True))
        self.assertFalse(result.get("update_youtube", True))
        self.assertIn("error", result)
        self.assertIn("Failed to detect field changes", result["error"])

    def test_resource_handlers_skip_on_error(self):
        """Test that resource handlers skip operations when change detection fails."""
        # Create changes dict with error
        changes_with_error = {
            "error": "Failed to detect field changes: Test error",
            "create_zoom": False,
            "create_calendar": False,
            "create_discourse": False,
            "create_youtube": False,
            "update_zoom": False,
            "update_calendar": False,
            "update_discourse": False,
            "update_youtube": False
        }

        existing_resources = {
            "has_zoom": False,
            "has_calendar": False,
            "has_discourse": False,
            "has_youtube": False
        }

        # Test that all resource handlers skip operations
        zoom_result = self.handler._handle_zoom_resource(self.sample_call_data, existing_resources, changes_with_error)
        self.assertFalse(zoom_result.get("zoom_created", True))

        calendar_result = self.handler._handle_calendar_resource(self.sample_call_data, existing_resources, changes_with_error)
        self.assertFalse(calendar_result.get("calendar_created", True))

        discourse_result = self.handler._handle_discourse_resource(self.sample_call_data, existing_resources, changes_with_error)
        self.assertFalse(discourse_result.get("discourse_created", True))

        youtube_result = self.handler._handle_youtube_resource(self.sample_call_data, existing_resources, changes_with_error)
        self.assertFalse(youtube_result.get("youtube_streams_created", True))


if __name__ == "__main__":
    unittest.main()