#!/usr/bin/env python3
"""
Unit tests for ProtocolCallHandler

Focuses on testing the edit detection and resource update logic.
"""

import unittest
from unittest.mock import Mock, patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))
from handle_protocol_call import ProtocolCallHandler


class TestProtocolCallHandler(unittest.TestCase):
    """Test cases for ProtocolCallHandler edit detection logic."""

    def setUp(self):
        """Set up test fixtures."""
        with patch('handle_protocol_call.MappingManager') as mock_mapping_manager:
            mock_mapping_manager.return_value = Mock()
            self.handler = ProtocolCallHandler()

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
            "need_youtube_streams": False
        }

        self.sample_existing_occurrence = {
            "call_series": "test-series",
            "occurrence": {
                "issue_number": 123,
                "issue_title": "Test Protocol Call",
                "start_time": "2024-01-15T09:00:00Z",  # Different time
                "duration": 30,  # Different duration
                "meeting_id": "test-meeting-id",
                "calendar_event_id": "test-calendar-id",
                "discourse_topic_id": "test-discourse-id"
            }
        }

    def test_should_process_edit_no_changes(self):
        """Test that edits with no critical changes are skipped."""
        no_change_call_data = {
            "issue_number": 123,
            "issue_title": "Test Protocol Call",
            "call_series": "test-series",
            "start_time": "2024-01-15T10:00:00Z",
            "duration": 60,
            "skip_zoom_creation": False,
            "skip_gcal_creation": False,
            "need_youtube_streams": False
        }

        matching_existing = {
            "call_series": "test-series",
            "occurrence": {
                "issue_number": 123,
                "issue_title": "Test Protocol Call",
                "call_series": "test-series",
                "start_time": "2024-01-15T10:00:00Z",
                "duration": 60,
                "meeting_id": "test-meeting-id",
                "calendar_event_id": "test-calendar-id",
                "discourse_topic_id": "test-discourse-id"
            }
        }

        result = self.handler._should_process_edit(
            no_change_call_data,
            matching_existing
        )
        self.assertFalse(result)

    def test_should_process_edit_start_time_changed(self):
        """Test that start time changes trigger processing."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["start_time"] = "2024-01-15T11:00:00Z"

        result = self.handler._should_process_edit(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_process_edit_duration_changed(self):
        """Test that duration changes trigger processing."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["duration"] = 90

        result = self.handler._should_process_edit(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_process_edit_call_series_changed(self):
        """Test that call series changes trigger processing."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["call_series"] = "new-test-series"

        result = self.handler._should_process_edit(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_process_edit_agenda_changed(self):
        """Test that agenda changes trigger processing."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["agenda"] = "Updated test agenda"

        result = self.handler._should_process_edit(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_process_edit_title_changed(self):
        """Test that issue title changes trigger processing."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["issue_title"] = "Updated Test Protocol Call"

        result = self.handler._should_process_edit(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_process_edit_missing_existing_data(self):
        """Test handling of missing existing occurrence data."""
        incomplete_existing = {"call_series": "test-series", "occurrence": {}}

        result = self.handler._should_process_edit(
            self.sample_call_data,
            incomplete_existing
        )
        self.assertTrue(result)

    def test_should_update_calendar_no_changes(self):
        """Test that calendar updates are skipped when no relevant changes."""
        no_change_call_data = {
            "issue_number": 123,
            "issue_title": "Test Protocol Call",
            "call_series": "test-series",
            "start_time": "2024-01-15T10:00:00Z",
            "duration": 60,
            "skip_zoom_creation": False,
            "skip_gcal_creation": False,
            "need_youtube_streams": False
        }

        matching_existing = {
            "call_series": "test-series",
            "occurrence": {
                "issue_number": 123,
                "issue_title": "Test Protocol Call",
                "start_time": "2024-01-15T10:00:00Z",
                "duration": 60,
                "meeting_id": "test-meeting-id",
                "calendar_event_id": "test-calendar-id",
                "discourse_topic_id": "test-discourse-id"
            }
        }

        result = self.handler._should_update_calendar(
            no_change_call_data,
            matching_existing
        )
        self.assertFalse(result)

    def test_should_update_calendar_start_time_changed(self):
        """Test that start time changes trigger calendar updates."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["start_time"] = "2024-01-15T11:00:00Z"

        result = self.handler._should_update_calendar(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_update_calendar_duration_changed(self):
        """Test that duration changes trigger calendar updates."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["duration"] = 90

        result = self.handler._should_update_calendar(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_update_calendar_title_changed(self):
        """Test that issue title changes trigger calendar updates."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["issue_title"] = "Updated Test Protocol Call"

        result = self.handler._should_update_calendar(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_update_calendar_agenda_changed(self):
        """Test that agenda changes trigger calendar updates."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["agenda"] = "Updated test agenda"

        result = self.handler._should_update_calendar(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_update_calendar_zoom_display_changed(self):
        """Test that Zoom link display setting changes trigger calendar updates."""
        modified_call_data = self.sample_call_data.copy()
        modified_call_data["display_zoom_link_in_invite"] = False

        result = self.handler._should_update_calendar(
            modified_call_data,
            self.sample_existing_occurrence
        )
        self.assertTrue(result)

    def test_should_update_calendar_missing_existing_data(self):
        """Test handling of missing existing occurrence data."""
        incomplete_existing = {"call_series": "test-series", "occurrence": {}}

        result = self.handler._should_update_calendar(
            self.sample_call_data,
            incomplete_existing
        )
        self.assertTrue(result)

    def test_resources_changed_all_false(self):
        """Test that resources_changed returns False when no resources were created."""
        resource_results = {
            "zoom_created": False,
            "calendar_created": False,
            "discourse_created": False,
            "youtube_streams_created": False
        }

        result = self.handler._resources_changed(resource_results)
        self.assertFalse(result)

    def test_resources_changed_some_true(self):
        """Test that resources_changed returns True when some resources were created."""
        resource_results = {
            "zoom_created": False,
            "calendar_created": True,
            "discourse_created": False,
            "youtube_streams_created": False
        }

        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_resources_changed_all_true(self):
        """Test that resources_changed returns True when all resources were created."""
        resource_results = {
            "zoom_created": True,
            "calendar_created": True,
            "discourse_created": True,
            "youtube_streams_created": True
        }

        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_resources_changed_missing_keys(self):
        """Test that resources_changed handles missing keys gracefully."""
        resource_results = {
            "zoom_created": True,
            # Missing other keys
        }

        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_edge_cases_string_comparison(self):
        """Test edge cases with string comparisons."""
        call_data_with_empty = self.sample_call_data.copy()
        call_data_with_empty["agenda"] = ""

        existing_with_none = self.sample_existing_occurrence.copy()
        existing_with_none["occurrence"]["agenda"] = None

        result = self.handler._should_process_edit(
            call_data_with_empty,
            existing_with_none
        )
        self.assertTrue(result)  # Empty string != None

    def test_edge_cases_boolean_comparison(self):
        """Test edge cases with boolean comparisons."""
        call_data_false = self.sample_call_data.copy()
        call_data_false["display_zoom_link_in_invite"] = False

        existing_true = self.sample_existing_occurrence.copy()
        existing_true["occurrence"]["display_zoom_link_in_invite"] = True

        result = self.handler._should_update_calendar(
            call_data_false,
            existing_true
        )
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()