"""
Unit tests for form_parser.py module.
"""

import pytest
from modules.form_parser import FormParser
from .test_data import (
    POORLY_FORMATTED_ISSUE,
    FREE_FORM_TEXT,
    PARTIAL_OLD_FORMAT,
    PARTIAL_NEW_FORMAT,
    MIXED_FORMATS,
    MALFORMED_MARKDOWN,
    FORM_WITH_MARKDOWN_LINKS,
    INVALID_DURATION_FORM,
    INVALID_START_TIME_FORM,
    ONE_OFF_MEETING_FORM,
    MISSING_REQUIRED_FIELDS_FORM,
    BOOLEAN_TEST_FORM_TEMPLATE,
    CALL_SERIES_TEST_FORMS,
    OCCURRENCE_RATE_TEST_FORMS,
    WHITESPACE_FORM,
    EDGE_CASE_FORM
)


class TestFormParser:
    """Test cases for FormParser class."""

    def test_parse_form_data_new_format(self):
        """Test parsing new form format."""
        parser = FormParser()

        # Use a complete form from test_data.py
        form_body = """
### Call Series
All Core Devs - Execution

### Duration
90 minutes

### UTC Date & Time
April 24, 2025, 14:00 UTC

### Is Recurring
- [x] Yes

### Occurrence Rate
Bi-weekly

### Skip Zoom Creation
- [ ] No

### Skip Google Calendar Creation
- [ ] No

### YouTube Livestream Link (Optional)
- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)
- [x] Yes

### Facilitator Emails (Optional)
test@example.com

### Custom Meeting Link (Optional)
_No response_

### Agenda
Test agenda for the meeting
"""

        result = parser.parse_form_data(form_body)

        assert result is not None
        assert result["call_series"] == "acde"
        assert result["duration"] == 90
        assert result["start_time"] == "2025-04-24T14:00:00Z"
        assert result["occurrence_rate"] == "bi-weekly"
        assert result["skip_zoom_creation"] is False
        assert result["skip_gcal_creation"] is False
        assert result["need_youtube_streams"] is True
        assert result["display_zoom_link_in_invite"] is True
        assert result["facilitator_emails"] == ["test@example.com"]
        assert result["agenda"] == "Test agenda for the meeting"

    def test_parse_form_data_legacy_format(self, sample_legacy_issue_body):
        """Test parsing legacy issue format."""
        parser = FormParser()

        result = parser.parse_form_data(sample_legacy_issue_body)

        assert result is not None
        assert result["call_series"] == "acde"
        assert result["duration"] == 90
        assert result["start_time"] == "2025-04-24T14:00:00Z"
        assert result["occurrence_rate"] == "bi-weekly"
        assert result["skip_zoom_creation"] is False
        assert result["skip_gcal_creation"] is False
        assert result["need_youtube_streams"] is False

    def test_parse_form_data_one_off_meeting(self):
        """Test parsing one-off meeting form data."""
        parser = FormParser()

        result = parser.parse_form_data(ONE_OFF_MEETING_FORM)

        assert result is not None
        assert result["call_series"] == "one-off"
        assert result["duration"] == 120
        assert result["start_time"] == "2025-04-26T16:00:00Z"
        assert result["skip_zoom_creation"] is True
        assert result["skip_gcal_creation"] is True
        assert result["need_youtube_streams"] is False
        assert result["display_zoom_link_in_invite"] is False
        assert result["facilitator_emails"] == ['organizer@example.com']

    def test_parse_form_data_missing_required_fields(self):
        """Test parsing form data with missing required fields."""
        parser = FormParser()

        result = parser.parse_form_data(MISSING_REQUIRED_FIELDS_FORM)

        # Should still parse but with defaults for missing fields
        assert result is not None
        assert result["call_series"] == "acde"
        assert result["duration"] == 90
        assert result["start_time"] == "2025-04-24T14:00:00Z"

    def test_parse_form_data_invalid_duration(self):
        """Test parsing form data with invalid duration."""
        parser = FormParser()

        result = parser.parse_form_data(INVALID_DURATION_FORM)

        assert result is not None
        assert result["duration"] == 0  # Invalid duration becomes 0

    def test_parse_form_data_invalid_start_time(self):
        """Test parsing form data with invalid start time."""
        parser = FormParser()

        result = parser.parse_form_data(INVALID_START_TIME_FORM)

        assert result is not None
        assert result["start_time"] == "invalid_time"  # Keep as-is for validation later

    def test_parse_form_data_boolean_fields(self):
        """Test parsing boolean fields correctly."""
        parser = FormParser()

        # Test checkbox format (not string format)
        test_cases = [
            ("- [x] Yes", True),
            ("- [ ] No", False),
            ("- [x] True", True),
            ("- [ ] False", False),
        ]

        for input_value, expected in test_cases:
            form_body = BOOLEAN_TEST_FORM_TEMPLATE.format(
                skip_zoom=input_value
            )
            result = parser.parse_form_data(form_body)
            assert result["skip_zoom_creation"] == expected, f"Failed for input: {input_value}"

    def test_parse_form_data_call_series_mapping(self):
        """Test call series display name to key mapping."""
        parser = FormParser()

        test_cases = [
            ("All Core Devs - Execution", "acde"),
            ("All Core Devs - Consensus", "acdc"),
            ("One-time call", "one-off"),
        ]

        for display_name, expected_key in test_cases:
            if display_name in CALL_SERIES_TEST_FORMS:
                form_body = CALL_SERIES_TEST_FORMS[display_name]
                result = parser.parse_form_data(form_body)
                assert result["call_series"] == expected_key, f"Failed for: {display_name}"

    def test_parse_form_data_occurrence_rate_mapping(self):
        """Test occurrence rate display name to key mapping."""
        parser = FormParser()

        test_cases = [
            ("Weekly", "weekly"),
            ("Bi-weekly", "bi-weekly"),
            ("Monthly", "monthly"),
            ("Quarterly", "quarterly"),
            ("None", "none"),
            ("Other", "other"),
            ("Unknown Rate", "unknown rate"),
        ]

        for display_name, expected_key in test_cases:
            if display_name in OCCURRENCE_RATE_TEST_FORMS:
                form_body = OCCURRENCE_RATE_TEST_FORMS[display_name]
                result = parser.parse_form_data(form_body)
                assert result["occurrence_rate"] == expected_key, f"Failed for: {display_name}"

    def test_parse_form_data_empty_body(self):
        """Test parsing empty form body."""
        parser = FormParser()

        with pytest.raises(ValueError, match="Issue body does not appear to be from either the new form format or old template format"):
            parser.parse_form_data("")

    def test_parse_form_data_none_body(self):
        """Test parsing None form body."""
        parser = FormParser()

        with pytest.raises(TypeError, match="expected string or bytes-like object"):
            parser.parse_form_data(None)

    def test_parse_form_data_unrecognized_format(self):
        """Test parsing issue with unrecognized format."""
        parser = FormParser()

        with pytest.raises(ValueError, match="Issue body does not appear to be from either the new form format or old template format"):
            parser.parse_form_data(POORLY_FORMATTED_ISSUE)

    def test_parse_form_data_free_form_text(self):
        """Test parsing free-form text that doesn't match any format."""
        parser = FormParser()

        with pytest.raises(ValueError, match="Issue body does not appear to be from either the new form format or old template format"):
            parser.parse_form_data(FREE_FORM_TEXT)

    def test_parse_form_data_partial_old_format(self):
        """Test parsing text that has some old format indicators but is incomplete."""
        parser = FormParser()

        result = parser.parse_form_data(PARTIAL_OLD_FORMAT)

        assert result is not None
        assert result["call_series"] == "all core devs - execution"
        assert result["duration"] == 90
        assert result["start_time"] is None
        assert result["occurrence_rate"] == "none"

    def test_parse_form_data_partial_new_format(self):
        """Test parsing text that has some new format indicators but is incomplete."""
        parser = FormParser()

        result = parser.parse_form_data(PARTIAL_NEW_FORMAT)

        assert result is not None
        assert result["call_series"] == "acde"
        assert result["duration"] == 90

    def test_parse_form_data_mixed_formats(self):
        """Test parsing text that mixes old and new format indicators."""
        parser = FormParser()

        # This should parse as old format (first match wins)
        result = parser.parse_form_data(MIXED_FORMATS)

        assert result is not None
        assert result["call_series"] == "all core devs - execution"
        assert result["duration"] == 90
        assert result["start_time"] is None
        # Remove is_recurring check since it's no longer meaningful
        assert result["occurrence_rate"] == "none"

    def test_parse_form_data_malformed_markdown(self):
        """Test parsing malformed markdown."""
        parser = FormParser()

        result = parser.parse_form_data(MALFORMED_MARKDOWN)

        # Should parse successfully and ignore unknown fields
        assert result is not None
        assert result["call_series"] == "acde"
        assert result["duration"] == 90
        assert "extra_field" not in result

    def test_parse_form_data_with_markdown_links(self):
        """Test parsing form data with markdown links in start time."""
        parser = FormParser()

        result = parser.parse_form_data(FORM_WITH_MARKDOWN_LINKS)

        assert result is not None
        assert result["start_time"] == "2025-04-24T14:00:00Z"

    def test_parse_form_data_with_whitespace(self):
        """Test parsing form data with extra whitespace."""
        parser = FormParser()

        result = parser.parse_form_data(WHITESPACE_FORM)

        assert result is not None
        assert result["call_series"] == "acde"
        assert result["duration"] == 90
        assert result["start_time"] == "2025-04-24T14:00:00Z"
        assert result["occurrence_rate"] == "bi-weekly"

    @pytest.mark.form_parser
    def test_form_parser_edge_cases(self):
        """Test various edge cases in form parsing."""
        parser = FormParser()

        # Test with very long values
        result = parser.parse_form_data(EDGE_CASE_FORM)
        assert result is not None
        assert result["duration"] == 0  # Invalid duration becomes 0

        # Test with special characters
        special_form = """
### Call Series
All Core Devs - Execution

### Duration
90

### Start Time
2025-04-24T14:00:00Z

### Agenda
Test agenda with special chars: !@#$%^&*()_+-=[]{}|;':",./<>?
"""

        result = parser.parse_form_data(special_form)
        assert result is not None
        assert "special chars" in result["agenda"]

    def test_parse_date_time_edge_cases(self):
        """Test date/time parsing with edge cases."""
        parser = FormParser()

        # Test ordinal dates (24th April 2025, 14:00 UTC)
        start_time, duration = parser.parse_date_time_with_duration("24th April 2025, 14:00 UTC", 90)
        assert start_time == "2025-04-24T14:00:00Z"
        assert duration == 90

        # Test without comma before year (April 24 2025, 14:00 UTC)
        start_time, duration = parser.parse_date_time_with_duration("April 24 2025, 14:00 UTC", 90)
        assert start_time == "2025-04-24T14:00:00Z"
        assert duration == 90

        # Test standard format (should still work)
        start_time, duration = parser.parse_date_time_with_duration("April 24, 2025, 14:00 UTC", 90)
        assert start_time == "2025-04-24T14:00:00Z"
        assert duration == 90

    def test_placeholder_facilitator_emails(self):
        """Test that invalid facilitator emails are filtered out."""
        parser = FormParser()

        # Test with various invalid emails
        legacy_issue_with_invalid_emails = """
# Meeting title eg. All Core Devs - Execution (ACDE) #206, February 27, 2025

- Date and time in UTC in format `month, day, year, time` with link to savvytime.com or timeanddate.com. E.g. [Jan 16, 2025, 14:00 UTC](https://savvytime.com/converter/utc/jan-16-2025/2pm)

# Agenda

- Agenda point 1
- Agenda point n

Other comments and resources

The zoom link will be sent to the facilitator via email
Facilitator emails: XXXXX, YYYYY, test@example.com, INVALID, admin@test.org

<details> <summary>🤖 config</summary>

- Duration in minutes : 90
- Recurring meeting : true
- Call series : acde
- Occurrence rate : bi-weekly
- Already a Zoom meeting ID : false
- Already on Ethereum Calendar : false
- Need YouTube stream links : true
- display zoom link in invite : false

</details>
"""

        result = parser.parse_form_data(legacy_issue_with_invalid_emails)

        assert result is not None
        # Should only include valid emails: test@example.com, admin@test.org
        assert result["facilitator_emails"] == ["test@example.com", "admin@test.org"]
        assert result["call_series"] == "acde"
        assert result["duration"] == 90

    def test_email_validation_edge_cases(self):
        """Test email validation with various edge cases."""
        parser = FormParser()

        # Test with various email formats
        legacy_issue_with_edge_cases = """
# Meeting title

Facilitator emails: test@example.com, no-at-sign, missing@dot, @missinglocal, local@, .missingtld, valid@test.org, another@domain.co.uk

<details> <summary>🤖 config</summary>
- Duration in minutes : 90
- Call series : acde
</details>
"""

        result = parser.parse_form_data(legacy_issue_with_edge_cases)

        assert result is not None
        # Should only include valid emails: test@example.com, valid@test.org, another@domain.co.uk
        assert result["facilitator_emails"] == ["test@example.com", "valid@test.org", "another@domain.co.uk"]