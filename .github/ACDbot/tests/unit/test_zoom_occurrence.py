#!/usr/bin/env python3
"""
Unit tests for Zoom recurring meeting occurrence logic.

Tests the pure/local functions for:
- Determining if a meeting is recurring
- Finding a specific occurrence by target date
- Determining if a time update is needed for an occurrence
- Validating that start times are UTC
"""

import os
import pytest

# Set up required environment variables before importing zoom module
os.environ.setdefault("ZOOM_CLIENT_ID", "test_client_id")
os.environ.setdefault("ZOOM_CLIENT_SECRET", "test_client_secret")
os.environ.setdefault("ZOOM_REFRESH_TOKEN", "test_refresh_token")

from modules.zoom import (
    is_recurring_meeting,
    find_occurrence_for_date,
    needs_time_update,
    ensure_utc,
)


class TestIsRecurringMeeting:
    """Tests for is_recurring_meeting()."""

    def test_type_8_is_recurring(self):
        """Type 8 (recurring with fixed time) should return True."""
        meeting = {"type": 8, "id": "123"}
        assert is_recurring_meeting(meeting) is True

    def test_type_3_is_recurring(self):
        """Type 3 (recurring with no fixed time) should return True."""
        meeting = {"type": 3, "id": "123"}
        assert is_recurring_meeting(meeting) is True

    def test_type_2_is_not_recurring(self):
        """Type 2 (scheduled, non-recurring) should return False."""
        meeting = {"type": 2, "id": "123"}
        assert is_recurring_meeting(meeting) is False

    def test_type_1_is_not_recurring(self):
        """Type 1 (instant) should return False."""
        meeting = {"type": 1, "id": "123"}
        assert is_recurring_meeting(meeting) is False

    def test_missing_type_returns_false(self):
        """Missing type key should return False."""
        meeting = {"id": "123"}
        assert is_recurring_meeting(meeting) is False

    def test_empty_dict_returns_false(self):
        meeting = {}
        assert is_recurring_meeting(meeting) is False


class TestFindOccurrenceForDate:
    """Tests for find_occurrence_for_date()."""

    @pytest.fixture
    def sample_occurrences(self):
        return [
            {
                "occurrence_id": "1741158000000",
                "start_time": "2026-03-03T11:00:00Z",
                "duration": 60,
                "status": "available",
            },
            {
                "occurrence_id": "1742367600000",
                "start_time": "2026-03-17T11:00:00Z",
                "duration": 60,
                "status": "available",
            },
            {
                "occurrence_id": "1743577200000",
                "start_time": "2026-03-31T11:00:00Z",
                "duration": 60,
                "status": "available",
            },
        ]

    def test_finds_exact_date_match(self, sample_occurrences):
        """Should find the occurrence matching the target date."""
        result = find_occurrence_for_date(sample_occurrences, "2026-03-17T11:00:00Z")
        assert result is not None
        assert result["occurrence_id"] == "1742367600000"

    def test_finds_match_when_times_differ(self, sample_occurrences):
        """Should match by date even when the requested time differs from occurrence time."""
        result = find_occurrence_for_date(sample_occurrences, "2026-03-17T14:00:00Z")
        assert result is not None
        assert result["occurrence_id"] == "1742367600000"

    def test_returns_none_when_no_match(self, sample_occurrences):
        """Should return None when no occurrence matches the target date."""
        result = find_occurrence_for_date(sample_occurrences, "2026-03-20T11:00:00Z")
        assert result is None

    def test_empty_occurrences(self):
        """Should return None for empty occurrence list."""
        result = find_occurrence_for_date([], "2026-03-17T11:00:00Z")
        assert result is None

    def test_finds_first_occurrence(self, sample_occurrences):
        result = find_occurrence_for_date(sample_occurrences, "2026-03-03T11:00:00Z")
        assert result is not None
        assert result["occurrence_id"] == "1741158000000"

    def test_finds_last_occurrence(self, sample_occurrences):
        result = find_occurrence_for_date(sample_occurrences, "2026-03-31T11:00:00Z")
        assert result is not None
        assert result["occurrence_id"] == "1743577200000"


class TestNeedsTimeUpdate:
    """Tests for needs_time_update()."""

    def test_same_time_no_update_needed(self):
        """No update needed when times match exactly."""
        occurrence = {"start_time": "2026-03-17T11:00:00Z", "duration": 60}
        assert needs_time_update(occurrence, "2026-03-17T11:00:00Z", 60) is False

    def test_different_time_needs_update(self):
        """Update needed when start times differ."""
        occurrence = {"start_time": "2026-03-17T14:00:00Z", "duration": 60}
        assert needs_time_update(occurrence, "2026-03-17T11:00:00Z", 60) is True

    def test_different_duration_needs_update(self):
        """Update needed when durations differ."""
        occurrence = {"start_time": "2026-03-17T11:00:00Z", "duration": 60}
        assert needs_time_update(occurrence, "2026-03-17T11:00:00Z", 90) is True

    def test_both_differ_needs_update(self):
        """Update needed when both time and duration differ."""
        occurrence = {"start_time": "2026-03-17T14:00:00Z", "duration": 60}
        assert needs_time_update(occurrence, "2026-03-17T11:00:00Z", 90) is True

    def test_equivalent_times_different_format(self):
        """No update needed when times are equivalent but formatted differently."""
        occurrence = {"start_time": "2026-03-17T11:00:00Z", "duration": 60}
        assert needs_time_update(occurrence, "2026-03-17T11:00:00+00:00", 60) is False

    def test_missing_duration_in_occurrence(self):
        """Should handle missing duration in occurrence gracefully."""
        occurrence = {"start_time": "2026-03-17T11:00:00Z"}
        # If occurrence has no duration, any requested duration counts as a change
        assert needs_time_update(occurrence, "2026-03-17T11:00:00Z", 60) is True

    def test_none_duration_means_no_duration_change(self):
        """When requested duration is None, only compare times."""
        occurrence = {"start_time": "2026-03-17T14:00:00Z", "duration": 60}
        assert needs_time_update(occurrence, "2026-03-17T11:00:00Z", None) is True

    def test_none_duration_same_time(self):
        """When requested duration is None and times match, no update needed."""
        occurrence = {"start_time": "2026-03-17T11:00:00Z", "duration": 60}
        assert needs_time_update(occurrence, "2026-03-17T11:00:00Z", None) is False


class TestEnsureUtc:
    """Tests for ensure_utc()."""

    def test_z_suffix_passes(self):
        result = ensure_utc("2026-03-17T11:00:00Z")
        assert result == "2026-03-17T11:00:00Z"

    def test_plus_zero_offset_normalized_to_z(self):
        result = ensure_utc("2026-03-17T11:00:00+00:00")
        assert result == "2026-03-17T11:00:00Z"

    def test_positive_offset_raises(self):
        with pytest.raises(ValueError, match="UTC"):
            ensure_utc("2026-03-17T11:00:00+05:30")

    def test_negative_offset_raises(self):
        with pytest.raises(ValueError, match="UTC"):
            ensure_utc("2026-03-17T11:00:00-04:00")

    def test_naive_datetime_raises(self):
        """A datetime with no timezone info should be rejected."""
        with pytest.raises(ValueError, match="UTC"):
            ensure_utc("2026-03-17T11:00:00")

    def test_midnight_utc(self):
        result = ensure_utc("2026-03-17T00:00:00Z")
        assert result == "2026-03-17T00:00:00Z"

    def test_with_seconds_and_z(self):
        result = ensure_utc("2026-03-17T11:30:45Z")
        assert result == "2026-03-17T11:30:45Z"

    def test_minus_zero_offset_normalized_to_z(self):
        """UTC can also be expressed as -00:00."""
        result = ensure_utc("2026-03-17T11:00:00-00:00")
        assert result == "2026-03-17T11:00:00Z"
