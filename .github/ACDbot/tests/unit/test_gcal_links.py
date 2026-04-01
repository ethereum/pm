#!/usr/bin/env python3
"""Tests for gcal calendar link builder functions."""

import unittest
import sys
import os
from unittest.mock import MagicMock
from urllib.parse import urlparse, parse_qs

# Mock heavy dependencies before importing gcal
sys.modules['google.oauth2'] = MagicMock()
sys.modules['google.oauth2.service_account'] = MagicMock()
sys.modules['googleapiclient'] = MagicMock()
sys.modules['googleapiclient.discovery'] = MagicMock()
sys.modules['pytz'] = MagicMock()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'modules'))

from gcal import build_calendar_view_link, build_calendar_add_link, PROTOCOL_CALENDAR_ID


class TestBuildCalendarViewLink(unittest.TestCase):

    def test_basic(self):
        result = build_calendar_view_link("2026-04-02T14:00:00Z")
        self.assertIsNotNone(result)
        parsed = urlparse(result)
        params = parse_qs(parsed.query)
        self.assertEqual(parsed.netloc, "calendar.google.com")
        self.assertIn("/calendar/embed", parsed.path)
        self.assertEqual(params["src"], [PROTOCOL_CALENDAR_ID])
        self.assertEqual(params["mode"], ["AGENDA"])
        self.assertEqual(params["dates"], ["20260402/20260403"])
        self.assertEqual(params["ctz"], ["UTC"])

    def test_none_start_time(self):
        self.assertIsNone(build_calendar_view_link(None))

    def test_empty_start_time(self):
        self.assertIsNone(build_calendar_view_link(""))

    def test_invalid_start_time(self):
        self.assertIsNone(build_calendar_view_link("not-a-date"))

    def test_custom_calendar_id(self):
        result = build_calendar_view_link("2026-04-02T14:00:00Z", calendar_id="custom@group.calendar.google.com")
        params = parse_qs(urlparse(result).query)
        self.assertEqual(params["src"], ["custom@group.calendar.google.com"])

    def test_minimal_chrome(self):
        result = build_calendar_view_link("2026-04-02T14:00:00Z")
        params = parse_qs(urlparse(result).query)
        self.assertEqual(params["showCalendars"], ["0"])
        self.assertEqual(params["showTabs"], ["0"])
        self.assertEqual(params["showPrint"], ["0"])
        self.assertEqual(params["showNav"], ["0"])


class TestBuildCalendarAddLink(unittest.TestCase):

    def test_basic(self):
        result = build_calendar_add_link("Test Event", "2026-04-02T14:00:00Z", 60)
        self.assertIsNotNone(result)
        parsed = urlparse(result)
        params = parse_qs(parsed.query)
        self.assertEqual(params["action"], ["TEMPLATE"])
        self.assertEqual(params["text"], ["Test Event"])
        self.assertEqual(params["dates"], ["20260402T140000Z/20260402T150000Z"])

    def test_with_description(self):
        result = build_calendar_add_link("Test", "2026-04-02T14:00:00Z", 60, "Some details")
        params = parse_qs(urlparse(result).query)
        self.assertEqual(params["details"], ["Some details"])

    def test_no_description(self):
        result = build_calendar_add_link("Test", "2026-04-02T14:00:00Z", 60)
        params = parse_qs(urlparse(result).query)
        self.assertNotIn("details", params)

    def test_90_minute_duration(self):
        result = build_calendar_add_link("Test", "2026-04-02T14:00:00Z", 90)
        params = parse_qs(urlparse(result).query)
        self.assertEqual(params["dates"], ["20260402T140000Z/20260402T153000Z"])

    def test_none_start_time(self):
        self.assertIsNone(build_calendar_add_link("Test", None, 60))

    def test_empty_start_time(self):
        self.assertIsNone(build_calendar_add_link("Test", "", 60))

    def test_invalid_start_time(self):
        self.assertIsNone(build_calendar_add_link("Test", "garbage", 60))


if __name__ == '__main__':
    unittest.main()
