#!/usr/bin/env python3
"""
Unit tests for ProtocolCallHandler

Focuses on testing the resource handlers and utility functions.
"""

import unittest
import unittest.mock
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
            "issue_url": "https://github.com/ethereum/pm/issues/123",
            "call_series": "test-series",
            "start_time": "2024-01-15T10:00:00Z",
            "duration": 60,
            "agenda": "Test agenda",
            "display_zoom_link_in_invite": True,
            "skip_zoom_creation": False,
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

    def test_handle_discourse_resource_existing(self):
        """Test that discourse resource uses existing data when available."""
        # Mock the discourse module to return unchanged status
        with unittest.mock.patch('modules.discourse.create_or_update_topic') as mock_discourse:
            mock_discourse.return_value = {
                "topic_id": "test-discourse-id",
                "action": "unchanged"
            }

            result = self.handler._handle_discourse_resource(self.sample_call_data, self.sample_existing_resources)

            self.assertTrue(result["discourse_created"])
            self.assertEqual(result["discourse_topic_id"], "test-discourse-id")
            self.assertEqual(result["discourse_action"], "unchanged")

            # Verify discourse module was called with existing topic ID
            mock_discourse.assert_called_once_with(
                title=self.sample_call_data["issue_title"],
                body=unittest.mock.ANY,  # body content can vary
                topic_id="test-discourse-id",
                category_id=63
            )

    def test_handle_youtube_resource_existing(self):
        """Test that youtube resource uses existing data when available."""
        # Enable YouTube streams for this test
        call_data = self.sample_call_data.copy()
        call_data["need_youtube_streams"] = True

        result = self.handler._handle_youtube_resource(call_data, self.sample_existing_resources)

        self.assertTrue(result["youtube_streams_created"])
        self.assertEqual(len(result["youtube_streams"]), 1)
        self.assertEqual(len(result["stream_links"]), 1)
        self.assertEqual(result["youtube_action"], "existing")



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

    def test_is_issue_already_cleaned(self):
        """Test that _is_issue_already_cleaned correctly detects cleaned issues."""
        # Test unclean issue body
        unclean_body = """### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

- Agenda item 1
- Agenda item 2

### Call Series

All Core Devs - Execution

### Duration

90 minutes"""

        result = self.handler._is_issue_already_cleaned(unclean_body)
        self.assertFalse(result)

        # Test cleaned issue body
        cleaned_body = """### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

- Agenda item 1
- Agenda item 2

### Call Series

All Core Devs - Execution

<details>
<summary>🔧 Meeting Configuration</summary>

### Duration

90 minutes
</details>"""

        result = self.handler._is_issue_already_cleaned(cleaned_body)
        self.assertTrue(result)

        # Test body with details but not Meeting Configuration
        other_details_body = """### UTC Date & Time

April 24, 2025, 14:00 UTC

<details>
<summary>Other details</summary>
Some other content
</details>"""

        result = self.handler._is_issue_already_cleaned(other_details_body)
        self.assertFalse(result)

    def test_clean_issue_body_preserves_parsing(self):
        """Test that _clean_issue_body preserves all parsing boundaries."""
        original_body = """### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

- Agenda item 1
- Agenda item 2
- Agenda item with multiple lines
  and indentation

### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] I will provide my own meeting link

### Facilitator Emails (Optional)

test@example.com

### Display Zoom Link in Calendar Invite (Optional)

- [x] Display Zoom link in invite"""

        cleaned_body = self.handler._clean_issue_body(original_body)

        # Test that the essential structure is preserved
        self.assertIn("### UTC Date & Time", cleaned_body)
        self.assertIn("April 24, 2025, 14:00 UTC", cleaned_body)
        self.assertIn("### Agenda", cleaned_body)
        self.assertIn("- Agenda item 1", cleaned_body)
        self.assertIn("### Call Series", cleaned_body)
        self.assertIn("All Core Devs - Execution", cleaned_body)

        # Test that config sections are wrapped in details
        self.assertIn("<details>", cleaned_body)
        self.assertIn("🔧 Meeting Configuration", cleaned_body)
        self.assertIn("### Duration", cleaned_body)
        self.assertIn("90 minutes", cleaned_body)
        self.assertIn("### Occurrence Rate", cleaned_body)
        self.assertIn("test@example.com", cleaned_body)
        self.assertIn("</details>", cleaned_body)

        # Test parsing compatibility by ensuring Call Series appears before details
        call_series_pos = cleaned_body.find("### Call Series")
        details_pos = cleaned_body.find("<details>")
        self.assertLess(call_series_pos, details_pos, "Call Series should appear before details for parsing")

        # Test that the agenda boundary is preserved (agenda ends where Call Series starts)
        agenda_pos = cleaned_body.find("### Agenda")
        agenda_content_start = cleaned_body.find("- Agenda item 1")
        self.assertLess(agenda_pos, agenda_content_start)
        self.assertLess(agenda_content_start, call_series_pos)

    def test_clean_issue_body_handles_edge_cases(self):
        """Test that _clean_issue_body handles various edge cases."""
        # Test non-form issue
        non_form_body = "This is not a form issue body"
        result = self.handler._clean_issue_body(non_form_body)
        self.assertEqual(result, non_form_body)

        # Test issue without Call Series section
        no_call_series_body = """### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

- Agenda item 1

### Duration

90 minutes"""

        result = self.handler._clean_issue_body(no_call_series_body)
        self.assertEqual(result, no_call_series_body)

        # Test issue with Call Series but no content after
        minimal_body = """### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

- Agenda item 1

### Call Series

All Core Devs - Execution"""

        result = self.handler._clean_issue_body(minimal_body)
        # Should not add details if there's no config content after Call Series
        self.assertNotIn("<details>", result)

        # Should have added savvytime link since it has Call Series section
        expected_minimal_body = """### UTC Date & Time

[April 24, 2025, 14:00 UTC](https://savvytime.com/converter/utc/apr-24-2025/2pm)

### Agenda

- Agenda item 1

### Call Series

All Core Devs - Execution"""
        self.assertEqual(result, expected_minimal_body)

    def test_clean_issue_body_with_form_parser_compatibility(self):
        """Test that cleaned issue body maintains form parser compatibility."""
        # Import form parser for testing
        from modules.form_parser import FormParser
        parser = FormParser()

        original_body = """### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

- Important agenda item 1
- Critical agenda item 2
- Final agenda item

### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] I will provide my own meeting link

### YouTube Livestream Link (Optional)

- [x] Create YouTube livestream link"""

        # Parse original body
        original_parsed = parser.parse_form_data(original_body)
        self.assertIsNotNone(original_parsed)

        # Clean the body
        cleaned_body = self.handler._clean_issue_body(original_body)

        # Parse cleaned body
        cleaned_parsed = parser.parse_form_data(cleaned_body)
        self.assertIsNotNone(cleaned_parsed)

        # Compare critical parsing results
        self.assertEqual(original_parsed.get("call_series"), cleaned_parsed.get("call_series"))
        self.assertEqual(original_parsed.get("agenda"), cleaned_parsed.get("agenda"))
        self.assertEqual(original_parsed.get("duration"), cleaned_parsed.get("duration"))
        self.assertEqual(original_parsed.get("occurrence_rate"), cleaned_parsed.get("occurrence_rate"))
        self.assertEqual(original_parsed.get("need_youtube_streams"), cleaned_parsed.get("need_youtube_streams"))

    def test_clean_issue_body_error_handling(self):
        """Test that _clean_issue_body handles errors gracefully."""
        # Test with None input
        result = self.handler._clean_issue_body(None)
        self.assertIsNone(result)

        # Test with malformed body that might cause regex issues
        malformed_body = "### UTC Date & Time\n\n[Invalid date\n\n### Agenda\n\nIncomplete"
        result = self.handler._clean_issue_body(malformed_body)
        # Should return original body if cleaning fails
        self.assertEqual(result, malformed_body)