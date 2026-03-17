"""
Unit tests for cancel_unmapped_meetings.py — find_cancellable_meetings() logic.

Uses mocked clock and synthetic mapping data. No API calls.
"""

import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch


# The function under test
from scripts.cancel_unmapped_meetings import find_cancellable_meetings


def _make_mapping(
    series_key="test-series",
    occurrence_rate="bi-weekly",
    calendar_event_id="cal123",
    latest_start="2025-06-01T14:00:00Z",
    occurrences=None,
):
    """Build a minimal mapping dict for a single recurring series."""
    if occurrences is None:
        occurrences = [
            {
                "occurrence_number": 1,
                "issue_number": 100,
                "issue_title": "Test Call #1",
                "start_time": latest_start,
                "duration": 60,
            }
        ]

    data = {
        series_key: {
            "call_series": series_key,
            "meeting_id": "111111111",
            "occurrence_rate": occurrence_rate,
            "occurrences": occurrences,
        }
    }
    if calendar_event_id is not None:
        data[series_key]["calendar_event_id"] = calendar_event_id
    return data


# Stub config so get_call_series_config returns a truthy value for our test series
_FAKE_CONFIG = {
    "test-series": {"display_name": "Test Series"},
    "other-series": {"display_name": "Other Series"},
}


def _fake_get_config(key):
    return _FAKE_CONFIG.get(key)


class TestFindCancellableMeetings:
    """Tests for find_cancellable_meetings()."""

    @patch(
        "scripts.upcoming_calls.get_call_series_config",
        side_effect=_fake_get_config,
    )
    def test_biweekly_meeting_in_12_hours(self, _mock_config):
        """A bi-weekly series with expected meeting in 12 hours and no issue → cancellable."""
        # Latest occurrence was 14 days ago; next expected is "now"
        latest = datetime(2025, 6, 1, 14, 0, tzinfo=timezone.utc)
        now = latest + timedelta(days=14) - timedelta(hours=12)

        mapping = _make_mapping(
            latest_start=latest.isoformat().replace("+00:00", "Z"),
        )

        with patch("scripts.upcoming_calls.datetime") as mock_uc_dt, \
             patch("scripts.cancel_unmapped_meetings.datetime") as mock_cu_dt:
            mock_uc_dt.now.return_value = now
            mock_uc_dt.fromisoformat = datetime.fromisoformat
            mock_uc_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            mock_cu_dt.now.return_value = now
            mock_cu_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            result = find_cancellable_meetings(mapping)

        assert len(result) == 1
        assert result[0]["series_key"] == "test-series"
        assert result[0]["calendar_event_id"] == "cal123"

    @patch(
        "scripts.upcoming_calls.get_call_series_config",
        side_effect=_fake_get_config,
    )
    def test_meeting_48_hours_away_not_cancellable(self, _mock_config):
        """A meeting expected in 48 hours is outside the 24h window → not cancellable."""
        latest = datetime(2025, 6, 1, 14, 0, tzinfo=timezone.utc)
        # 48 hours before expected → expected is 48h away
        now = latest + timedelta(days=14) - timedelta(hours=48)

        mapping = _make_mapping(
            latest_start=latest.isoformat().replace("+00:00", "Z"),
        )

        with patch("scripts.upcoming_calls.datetime") as mock_uc_dt, \
             patch("scripts.cancel_unmapped_meetings.datetime") as mock_cu_dt:
            mock_uc_dt.now.return_value = now
            mock_uc_dt.fromisoformat = datetime.fromisoformat
            mock_uc_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            mock_cu_dt.now.return_value = now
            mock_cu_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            result = find_cancellable_meetings(mapping)

        assert len(result) == 0

    @patch(
        "scripts.upcoming_calls.get_call_series_config",
        side_effect=_fake_get_config,
    )
    def test_matching_occurrence_exists(self, _mock_config):
        """If a matching occurrence already exists for the expected date → not missing → not cancellable."""
        latest = datetime(2025, 6, 1, 14, 0, tzinfo=timezone.utc)
        next_expected = latest + timedelta(days=14)
        now = next_expected - timedelta(hours=12)

        mapping = _make_mapping(
            latest_start=latest.isoformat().replace("+00:00", "Z"),
            occurrences=[
                {
                    "occurrence_number": 1,
                    "issue_number": 100,
                    "issue_title": "Test Call #1",
                    "start_time": latest.isoformat().replace("+00:00", "Z"),
                    "duration": 60,
                },
                {
                    "occurrence_number": 2,
                    "issue_number": 101,
                    "issue_title": "Test Call #2",
                    "start_time": next_expected.isoformat().replace("+00:00", "Z"),
                    "duration": 60,
                },
            ],
        )

        with patch("scripts.upcoming_calls.datetime") as mock_uc_dt, \
             patch("scripts.cancel_unmapped_meetings.datetime") as mock_cu_dt:
            mock_uc_dt.now.return_value = now
            mock_uc_dt.fromisoformat = datetime.fromisoformat
            mock_uc_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            mock_cu_dt.now.return_value = now
            mock_cu_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            result = find_cancellable_meetings(mapping)

        assert len(result) == 0

    @patch(
        "scripts.upcoming_calls.get_call_series_config",
        side_effect=_fake_get_config,
    )
    def test_one_off_calls_skipped(self, _mock_config):
        """One-off calls are skipped by find_expected_missing_calls()."""
        latest = datetime(2025, 6, 1, 14, 0, tzinfo=timezone.utc)
        now = latest + timedelta(days=14) - timedelta(hours=12)

        mapping = {
            "one-off-999": {
                "call_series": "one-off-999",
                "meeting_id": "222222222",
                "occurrence_rate": "one-time",
                "calendar_event_id": "cal456",
                "occurrences": [
                    {
                        "occurrence_number": 1,
                        "issue_number": 999,
                        "issue_title": "One-off Call",
                        "start_time": latest.isoformat().replace("+00:00", "Z"),
                        "duration": 60,
                    }
                ],
            }
        }

        with patch("scripts.upcoming_calls.datetime") as mock_uc_dt, \
             patch("scripts.cancel_unmapped_meetings.datetime") as mock_cu_dt:
            mock_uc_dt.now.return_value = now
            mock_uc_dt.fromisoformat = datetime.fromisoformat
            mock_uc_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            mock_cu_dt.now.return_value = now
            mock_cu_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            result = find_cancellable_meetings(mapping)

        assert len(result) == 0

    @patch(
        "scripts.upcoming_calls.get_call_series_config",
        side_effect=_fake_get_config,
    )
    def test_retired_series_skipped(self, _mock_config):
        """Series with no meeting in 3+ intervals are treated as retired → skipped."""
        # Latest occurrence was >3 intervals (42+ days for bi-weekly) ago
        latest = datetime(2025, 3, 1, 14, 0, tzinfo=timezone.utc)
        now = datetime(2025, 6, 15, 14, 0, tzinfo=timezone.utc)

        mapping = _make_mapping(
            latest_start=latest.isoformat().replace("+00:00", "Z"),
        )

        with patch("scripts.upcoming_calls.datetime") as mock_uc_dt, \
             patch("scripts.cancel_unmapped_meetings.datetime") as mock_cu_dt:
            mock_uc_dt.now.return_value = now
            mock_uc_dt.fromisoformat = datetime.fromisoformat
            mock_uc_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            mock_cu_dt.now.return_value = now
            mock_cu_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            result = find_cancellable_meetings(mapping)

        assert len(result) == 0

    @patch(
        "scripts.upcoming_calls.get_call_series_config",
        side_effect=_fake_get_config,
    )
    def test_unsupported_rate_skipped(self, _mock_config):
        """Series with unsupported occurrence_rate are skipped."""
        latest = datetime(2025, 6, 1, 14, 0, tzinfo=timezone.utc)
        now = latest + timedelta(days=14) - timedelta(hours=12)

        mapping = _make_mapping(
            occurrence_rate="quarterly",
            latest_start=latest.isoformat().replace("+00:00", "Z"),
        )

        with patch("scripts.upcoming_calls.datetime") as mock_uc_dt, \
             patch("scripts.cancel_unmapped_meetings.datetime") as mock_cu_dt:
            mock_uc_dt.now.return_value = now
            mock_uc_dt.fromisoformat = datetime.fromisoformat
            mock_uc_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            mock_cu_dt.now.return_value = now
            mock_cu_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            result = find_cancellable_meetings(mapping)

        assert len(result) == 0

    @patch(
        "scripts.upcoming_calls.get_call_series_config",
        side_effect=_fake_get_config,
    )
    def test_no_calendar_event_id_still_returned(self, _mock_config):
        """Series with no calendar_event_id still appears in results (script handles gracefully)."""
        latest = datetime(2025, 6, 1, 14, 0, tzinfo=timezone.utc)
        now = latest + timedelta(days=14) - timedelta(hours=12)

        mapping = _make_mapping(
            calendar_event_id=None,
            latest_start=latest.isoformat().replace("+00:00", "Z"),
        )

        with patch("scripts.upcoming_calls.datetime") as mock_uc_dt, \
             patch("scripts.cancel_unmapped_meetings.datetime") as mock_cu_dt:
            mock_uc_dt.now.return_value = now
            mock_uc_dt.fromisoformat = datetime.fromisoformat
            mock_uc_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            mock_cu_dt.now.return_value = now
            mock_cu_dt.side_effect = lambda *a, **kw: datetime(*a, **kw)
            result = find_cancellable_meetings(mapping)

        assert len(result) == 1
        assert result[0]["calendar_event_id"] is None
