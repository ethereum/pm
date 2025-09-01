import unittest
import sys
import os
from datetime import datetime

# Add the modules directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'modules'))

from datetime_utils import (
    parse_datetime_string,
    parse_iso_datetime,
    format_hour_for_savvytime,
    generate_savvytime_url,
    generate_savvytime_link,
    format_datetime_display,
    format_datetime_for_discourse,
    format_datetime_for_stream_display,
    is_valid_datetime_format,
    extract_datetime_from_markdown_link
)


class TestDatetimeUtils(unittest.TestCase):
    """Test cases for datetime utilities."""

    def test_parse_datetime_string_standard_format(self):
        """Test parsing standard datetime format."""
        test_cases = [
            "April 24, 2025, 14:00 UTC",
            "January 1, 2025, 00:00 UTC",
            "December 31, 2024, 23:59 UTC"
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                result = parse_datetime_string(test_case)
                self.assertIsNotNone(result)
                self.assertIsInstance(result, datetime)

    def test_parse_datetime_string_abbreviated_format(self):
        """Test parsing abbreviated month format."""
        test_cases = [
            "Apr 24, 2025, 14:00 UTC",
            "Jan 1, 2025, 00:00 UTC",
            "Dec 31, 2024, 23:59 UTC"
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                result = parse_datetime_string(test_case)
                self.assertIsNotNone(result)
                self.assertIsInstance(result, datetime)

    def test_parse_datetime_string_non_standard_abbreviations(self):
        """Test parsing non-standard month abbreviations like 'Sept', 'June', 'July'."""
        test_cases = [
            ("Sept 10, 2025, 14:00 UTC", datetime(2025, 9, 10, 14, 0)),
            ("June 15, 2025, 09:30 UTC", datetime(2025, 6, 15, 9, 30)),
            ("July 4, 2025, 16:00 UTC", datetime(2025, 7, 4, 16, 0)),
            # Test with different formatting variations
            ("Sept 1 2025, 12:00 UTC", datetime(2025, 9, 1, 12, 0)),
            ("June 30 2024, 23:59 UTC", datetime(2024, 6, 30, 23, 59)),
            ("July 31 2025, 00:00 UTC", datetime(2025, 7, 31, 0, 0))
        ]

        for test_input, expected_dt in test_cases:
            with self.subTest(test_case=test_input):
                result = parse_datetime_string(test_input)
                self.assertIsNotNone(result, f"Failed to parse: {test_input}")
                self.assertIsInstance(result, datetime)
                # Compare the essential datetime components
                self.assertEqual(result.year, expected_dt.year)
                self.assertEqual(result.month, expected_dt.month)
                self.assertEqual(result.day, expected_dt.day)
                self.assertEqual(result.hour, expected_dt.hour)
                self.assertEqual(result.minute, expected_dt.minute)

    def test_parse_datetime_string_comma_after_month(self):
        """Test parsing formats with comma after month: 'Sept, 10, 2025, 14:00 UTC'."""
        test_cases = [
            ("Sept, 10, 2025, 14:00 UTC", datetime(2025, 9, 10, 14, 0)),
            ("June, 15, 2025, 09:30 UTC", datetime(2025, 6, 15, 9, 30)),
            ("July, 4, 2025, 16:00 UTC", datetime(2025, 7, 4, 16, 0)),
            # Test with standard month names too
            ("April, 24, 2025, 14:00 UTC", datetime(2025, 4, 24, 14, 0)),
            ("Aug, 15, 2024, 12:00 UTC", datetime(2024, 8, 15, 12, 0)),
            # Test with no comma before year
            ("Sept, 1 2025, 12:00 UTC", datetime(2025, 9, 1, 12, 0)),
            ("June, 30 2024, 23:59 UTC", datetime(2024, 6, 30, 23, 59)),
            # Test case variations
            ("sept, 10, 2025, 14:00 UTC", datetime(2025, 9, 10, 14, 0)),  # lowercase
            ("JULY, 4, 2025, 16:00 UTC", datetime(2025, 7, 4, 16, 0)),   # uppercase
            ("apr, 10 2025, 12:00 UTC", datetime(2025, 4, 10, 12, 0)),   # lowercase abbrev, no comma before year
        ]

        for test_input, expected_dt in test_cases:
            with self.subTest(test_case=test_input):
                result = parse_datetime_string(test_input)
                self.assertIsNotNone(result, f"Failed to parse: {test_input}")
                self.assertIsInstance(result, datetime)
                # Compare the essential datetime components
                self.assertEqual(result.year, expected_dt.year)
                self.assertEqual(result.month, expected_dt.month)
                self.assertEqual(result.day, expected_dt.day)
                self.assertEqual(result.hour, expected_dt.hour)
                self.assertEqual(result.minute, expected_dt.minute)

    def test_parse_datetime_string_no_comma_before_year(self):
        """Test parsing format without comma before year."""
        test_cases = [
            "April 24 2025, 14:00 UTC",
            "Aug 15 2024, 09:30 UTC"
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                result = parse_datetime_string(test_case)
                self.assertIsNotNone(result)
                self.assertIsInstance(result, datetime)

    def test_parse_datetime_string_ordinal_dates(self):
        """Test parsing ordinal date formats."""
        test_cases = [
            "1st April 2025, 14:00 UTC",
            "22nd December 2024, 16:30 UTC",
            "3rd May 2025, 10:00 UTC"
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                result = parse_datetime_string(test_case)
                self.assertIsNotNone(result)
                self.assertIsInstance(result, datetime)

    def test_parse_datetime_string_iso_format(self):
        """Test parsing ISO format datetime strings."""
        test_cases = [
            "2025-04-24T14:00:00Z",
            "2025-01-01T00:00:00Z",
            "2024-12-31T23:59:59Z"
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                result = parse_datetime_string(test_case)
                self.assertIsNotNone(result)
                self.assertIsInstance(result, datetime)

    def test_parse_datetime_string_invalid_formats(self):
        """Test that invalid formats return None."""
        invalid_cases = [
            "Invalid datetime",
            "2025-13-01T14:00:00Z",  # Invalid month
            "April 32, 2025, 14:00 UTC",  # Invalid day
            "",
            None
        ]

        for test_case in invalid_cases:
            with self.subTest(test_case=test_case):
                result = parse_datetime_string(test_case)
                self.assertIsNone(result)

    def test_parse_datetime_string_edge_cases(self):
        """Test edge cases and boundary conditions."""
        edge_cases = [
            # Test case sensitivity - should now work with case insensitivity
            ("sept 10, 2025, 14:00 UTC", datetime(2025, 9, 10, 14, 0)),  # lowercase - should work
            ("SEPT 10, 2025, 14:00 UTC", datetime(2025, 9, 10, 14, 0)),  # uppercase - should work
            # Test partial matches that might cause issues
            ("September 10, 2025, 14:00 UTC", datetime(2025, 9, 10, 14, 0)),  # Full name should still work
            ("Sep 10, 2025, 14:00 UTC", datetime(2025, 9, 10, 14, 0)),  # Standard abbrev should work
            # Test that only our specific mappings work
            ("Septemberish 10, 2025, 14:00 UTC", None),  # Contains "Sept" but isn't exact match
            # Test valid month names that we don't have special mappings for
            ("Nov 10, 2025, 14:00 UTC", datetime(2025, 11, 10, 14, 0)),  # Standard abbrev should work
            ("March 10, 2025, 14:00 UTC", datetime(2025, 3, 10, 14, 0)),  # Full name should work
            # Test case insensitivity for all standard month names
            ("april 24, 2025, 14:00 UTC", datetime(2025, 4, 24, 14, 0)),  # lowercase full month
            ("AUGUST 15, 2025, 09:30 UTC", datetime(2025, 8, 15, 9, 30)),  # uppercase full month
            ("apr 10, 2025, 12:00 UTC", datetime(2025, 4, 10, 12, 0)),  # lowercase abbrev
            ("DEC 31, 2024, 23:59 UTC", datetime(2024, 12, 31, 23, 59)),  # uppercase abbrev
        ]

        for test_input, expected_result in edge_cases:
            with self.subTest(test_case=test_input):
                result = parse_datetime_string(test_input)
                if expected_result is None:
                    self.assertIsNone(result, f"Expected None but got {result} for: {test_input}")
                else:
                    self.assertIsNotNone(result, f"Expected valid datetime but got None for: {test_input}")
                    self.assertEqual(result.year, expected_result.year)
                    self.assertEqual(result.month, expected_result.month)
                    self.assertEqual(result.day, expected_result.day)
                    self.assertEqual(result.hour, expected_result.hour)
                    self.assertEqual(result.minute, expected_result.minute)

    def test_parse_iso_datetime(self):
        """Test ISO datetime parsing with various formats."""
        test_cases = [
            ("2025-04-24T14:00:00Z", datetime(2025, 4, 24, 14, 0)),
            ("2025-04-24T14:00:00+00:00", datetime(2025, 4, 24, 14, 0)),
            ("2025-01-01T00:00:00Z", datetime(2025, 1, 1, 0, 0))
        ]

        for iso_str, expected_dt in test_cases:
            with self.subTest(iso_str=iso_str):
                result = parse_iso_datetime(iso_str)
                self.assertIsNotNone(result)
                # Compare without timezone info for simplicity
                self.assertEqual(result.replace(tzinfo=None), expected_dt)

    def test_parse_iso_datetime_invalid(self):
        """Test ISO datetime parsing with invalid inputs."""
        invalid_cases = [
            "invalid-datetime",
            "2025-13-01T14:00:00Z",
            "",
            None
        ]

        for test_case in invalid_cases:
            with self.subTest(test_case=test_case):
                result = parse_iso_datetime(test_case)
                self.assertIsNone(result)

    def test_format_hour_for_savvytime(self):
        """Test hour formatting for savvytime URLs."""
        test_cases = [
            (0, "12am"),
            (1, "1am"),
            (11, "11am"),
            (12, "12pm"),
            (13, "1pm"),
            (23, "11pm")
        ]

        for hour, expected in test_cases:
            with self.subTest(hour=hour):
                result = format_hour_for_savvytime(hour)
                self.assertEqual(result, expected)

    def test_generate_savvytime_url(self):
        """Test savvytime URL generation."""
        test_dt = datetime(2025, 8, 4, 14, 0)  # August 4, 2025, 2:00 PM
        expected_url = "https://savvytime.com/converter/utc/aug-4-2025/2pm"

        result = generate_savvytime_url(test_dt)
        self.assertEqual(result, expected_url)

    def test_generate_savvytime_url_edge_cases(self):
        """Test savvytime URL generation with edge cases."""
        test_cases = [
            (datetime(2025, 1, 1, 0, 0), "https://savvytime.com/converter/utc/jan-1-2025/12am"),
            (datetime(2025, 12, 31, 23, 0), "https://savvytime.com/converter/utc/dec-31-2025/11pm"),
            (datetime(2025, 6, 15, 12, 0), "https://savvytime.com/converter/utc/jun-15-2025/12pm")
        ]

        for test_dt, expected_url in test_cases:
            with self.subTest(datetime=test_dt):
                result = generate_savvytime_url(test_dt)
                self.assertEqual(result, expected_url)

    def test_generate_savvytime_link(self):
        """Test complete savvytime link generation."""
        test_datetime = "August 4, 2025, 14:00 UTC"
        result = generate_savvytime_link(test_datetime)

        # Check that it's a proper markdown link
        self.assertTrue(result.startswith('['))
        self.assertTrue('](' in result)
        self.assertTrue('savvytime.com' in result)
        self.assertTrue('aug-4-2025/2pm' in result)

    def test_generate_savvytime_link_invalid_input(self):
        """Test savvytime link generation with invalid input."""
        invalid_input = "not a valid datetime"
        result = generate_savvytime_link(invalid_input)

        # Should return the original string if parsing fails
        self.assertEqual(result, invalid_input)

    def test_format_datetime_display(self):
        """Test datetime display formatting."""
        test_dt = datetime(2025, 8, 4, 14, 0)

        # With timezone
        result_with_tz = format_datetime_display(test_dt, include_timezone=True)
        self.assertEqual(result_with_tz, "August 04, 2025, 14:00 UTC")

        # Without timezone
        result_without_tz = format_datetime_display(test_dt, include_timezone=False)
        self.assertEqual(result_without_tz, "August 04, 2025, 14:00")

    def test_format_datetime_for_discourse(self):
        """Test Discourse datetime formatting."""
        iso_datetime = "2025-08-04T14:00:00Z"
        duration = 90

        result = format_datetime_for_discourse(iso_datetime, duration)

        expected_parts = [
            "**Meeting Time:**",
            "Monday, August 04, 2025",
            "at 14:00 UTC",
            "(90 minutes)"
        ]

        for part in expected_parts:
            self.assertIn(part, result)

    def test_format_datetime_for_discourse_invalid_input(self):
        """Test Discourse formatting with invalid input."""
        invalid_datetime = "invalid-datetime"
        duration = 90

        result = format_datetime_for_discourse(invalid_datetime, duration)

        # Should return fallback format
        expected = "**Meeting Time:** invalid-datetime (90 minutes)"
        self.assertEqual(result, expected)

    def test_format_datetime_for_stream_display(self):
        """Test stream display datetime formatting."""
        iso_datetime = "2025-08-04T14:00:00Z"

        result = format_datetime_for_stream_display(iso_datetime)

        self.assertEqual(result, " (Aug 04, 2025)")

    def test_format_datetime_for_stream_display_invalid_input(self):
        """Test stream display formatting with invalid input."""
        invalid_datetime = "invalid-datetime"

        result = format_datetime_for_stream_display(invalid_datetime)

        # Should return empty string for invalid input
        self.assertEqual(result, "")

    def test_is_valid_datetime_format(self):
        """Test datetime format validation."""
        valid_cases = [
            "August 4, 2025, 14:00 UTC",
            "Apr 15, 2025, 09:30 UTC",
            "2025-08-04T14:00:00Z"
        ]

        invalid_cases = [
            "not a datetime",
            "August 32, 2025, 14:00 UTC",
            "",
            None
        ]

        for valid_case in valid_cases:
            with self.subTest(case=valid_case):
                self.assertTrue(is_valid_datetime_format(valid_case))

        for invalid_case in invalid_cases:
            with self.subTest(case=invalid_case):
                self.assertFalse(is_valid_datetime_format(invalid_case))

    def test_extract_datetime_from_markdown_link(self):
        """Test extraction of datetime from markdown links."""
        test_cases = [
            ("[August 4, 2025, 14:00 UTC](https://savvytime.com/converter/utc/aug-4-2025/2pm)",
             "August 4, 2025, 14:00 UTC"),
            ("[Apr 15, 2025, 09:30 UTC](https://example.com)",
             "Apr 15, 2025, 09:30 UTC")
        ]

        for link_text, expected_datetime in test_cases:
            with self.subTest(link_text=link_text):
                result = extract_datetime_from_markdown_link(link_text)
                self.assertEqual(result, expected_datetime)

    def test_extract_datetime_from_markdown_link_invalid(self):
        """Test extraction with invalid markdown links."""
        invalid_cases = [
            "Not a markdown link",
            "[Incomplete markdown link",
            "](Missing opening bracket",
            ""
        ]

        for invalid_case in invalid_cases:
            with self.subTest(case=invalid_case):
                result = extract_datetime_from_markdown_link(invalid_case)
                self.assertIsNone(result)