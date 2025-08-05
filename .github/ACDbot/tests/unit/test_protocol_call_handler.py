#!/usr/bin/env python3
"""
Unit tests for ProtocolCallHandler

Focuses on testing the resource handlers and utility functions.
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

        # Sample existing resources data
        self.sample_existing_resources = {
            "has_zoom": True,
            "has_calendar": True,
            "has_discourse": True,
            "has_youtube": True,
            "existing_occurrence": {
                "call_series": "test-series",
                "occurrence": {
                    "issue_number": 123,
                    "issue_title": "Test Protocol Call",
                    "start_time": "2024-01-15T10:00:00Z",
                    "duration": 60,
                    "agenda": "Test agenda",
                    "meeting_id": "test-meeting-id",
                    "discourse_topic_id": "test-discourse-id",
                    "youtube_streams": [{"stream_url": "https://youtube.com/test"}]
                }
            }
        }

    def test_resources_changed_all_false(self):
        """Test that resources_changed returns False when all resources are False."""
        resource_results = {
            "zoom_created": False,
            "calendar_created": False,
            "discourse_created": False,
            "youtube_streams_created": False
        }

        result = self.handler._resources_changed(resource_results)
        self.assertFalse(result)

    def test_resources_changed_some_true(self):
        """Test that resources_changed returns True when some resources are True."""
        resource_results = {
            "zoom_created": True,
            "calendar_created": False,
            "discourse_created": False,
            "youtube_streams_created": False
        }

        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_resources_changed_all_true(self):
        """Test that resources_changed returns True when all resources are True."""
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
            "zoom_created": True
            # Missing other keys
        }

        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_get_call_series_display_name(self):
        """Test that call series display names are returned correctly."""
        # Test known call series
        result = self.handler._get_call_series_display_name("acde")
        self.assertEqual(result, "All Core Devs - Execution")

        # Test unknown call series
        result = self.handler._get_call_series_display_name("unknown")
        self.assertEqual(result, "unknown")

    def test_handle_zoom_resource_skip_creation(self):
        """Test that zoom resource is skipped when user opted out."""
        call_data = self.sample_call_data.copy()
        call_data["skip_zoom_creation"] = True

        result = self.handler._handle_zoom_resource(call_data, self.sample_existing_resources)

        self.assertFalse(result["zoom_created"])
        self.assertIsNone(result["zoom_id"])
        self.assertIsNone(result["zoom_url"])

    def test_handle_calendar_resource_skip_creation(self):
        """Test that calendar resource is skipped when not on Ethereum calendar."""
        call_data = self.sample_call_data.copy()
        call_data["skip_gcal_creation"] = True

        result = self.handler._handle_calendar_resource(call_data, self.sample_existing_resources)

        self.assertFalse(result["calendar_created"])
        self.assertIsNone(result["calendar_event_id"])
        self.assertIsNone(result["calendar_event_url"])

    def test_handle_discourse_resource_existing(self):
        """Test that discourse resource uses existing data when available."""
        result = self.handler._handle_discourse_resource(self.sample_call_data, self.sample_existing_resources)

        self.assertTrue(result["discourse_created"])
        self.assertEqual(result["discourse_topic_id"], "test-discourse-id")
        self.assertEqual(result["discourse_action"], "existing")

    def test_handle_youtube_resource_existing(self):
        """Test that youtube resource uses existing data when available."""
        result = self.handler._handle_youtube_resource(self.sample_call_data, self.sample_existing_resources)

        self.assertTrue(result["youtube_streams_created"])
        self.assertEqual(len(result["youtube_streams"]), 1)
        self.assertEqual(len(result["stream_links"]), 1)
        self.assertEqual(result["youtube_action"], "existing")

    def test_resources_changed_with_action_fields(self):
        """Test that resources_changed correctly handles action fields."""
        # Test with existing resources
        resource_results = {
            "zoom_created": True,
            "zoom_action": "updated",
            "calendar_created": True,
            "calendar_action": "existing",
            "discourse_created": True,
            "discourse_action": "existing",
            "youtube_streams_created": True,
            "youtube_action": "existing"
        }
        result = self.handler._resources_changed(resource_results)
        self.assertFalse(result)

        # Test with newly created resources
        resource_results = {
            "zoom_created": True,
            "zoom_action": "created",
            "calendar_created": True,
            "calendar_action": "created",
            "discourse_created": True,
            "discourse_action": "created",
            "youtube_streams_created": True,
            "youtube_action": "created"
        }
        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

        # Test with mixed existing and new resources
        resource_results = {
            "zoom_created": True,
            "zoom_action": "updated",
            "calendar_created": True,
            "calendar_action": "created",
            "discourse_created": True,
            "discourse_action": "existing",
            "youtube_streams_created": True,
            "youtube_action": "existing"
        }
        result = self.handler._resources_changed(resource_results)
        self.assertTrue(result)

    def test_find_existing_discourse_topic(self):
        """Test that _find_existing_discourse_topic correctly finds existing topic IDs."""
        # Mock the mapping manager to return test data
        with unittest.mock.patch.object(self.handler.mapping_manager, 'load_mapping') as mock_load:
            mock_load.return_value = {
                "acdt": {
                    "call_series": "acdt",
                    "occurrences": [
                        {
                            "issue_number": 1648,
                            "discourse_topic_id": 24956,
                            "issue_title": "All Core Devs - Testing (ACDT) #47 | August 4 2025"
                        },
                        {
                            "issue_number": 1640,
                            "discourse_topic_id": 24800,
                            "issue_title": "All Core Devs - Testing (ACDT) #46 | July 28 2025"
                        }
                    ]
                }
            }

            # Test finding existing topic for acdt series
            result = self.handler._find_existing_discourse_topic("acdt")
            self.assertEqual(result, 24956)  # Should find the most recent one

            # Test finding existing topic for non-existent series
            result = self.handler._find_existing_discourse_topic("nonexistent")
            self.assertIsNone(result)