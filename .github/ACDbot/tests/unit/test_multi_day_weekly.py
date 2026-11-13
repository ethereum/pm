#!/usr/bin/env python3
"""
Unit tests for multi-day weekly occurrence rates (e.g. "weekly:tu,we,fr").

A series like the PQ-CL Breakout meets several times in the same week, which the
weekly / bi-weekly / monthly rates can't express. These tests cover the shared
parsing helpers and the three places the day set has to reach: the Zoom
recurrence payload, the Google Calendar RRULE, and the YouTube stream schedule.
"""

import os
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest


def _frozen_datetime(pinned):
    """A datetime subclass whose now() is pinned, to project from a fixed 'today'.

    Everything else (fromisoformat, comparison, arithmetic) is inherited, which is
    all find_expected_missing_calls needs.
    """
    return type("FrozenDatetime", (datetime,), {"now": classmethod(lambda cls, tz=None: pinned)})


# Set up required environment variables before importing the zoom module
os.environ.setdefault("ZOOM_CLIENT_ID", "test_client_id")
os.environ.setdefault("ZOOM_CLIENT_SECRET", "test_client_secret")
os.environ.setdefault("ZOOM_REFRESH_TOKEN", "test_refresh_token")

from modules.datetime_utils import (
    next_weekly_day,
    parse_multi_day_weekly,
    weekly_days_to_byday,
    weekly_days_to_zoom,
)


class TestParseMultiDayWeekly:
    """Tests for parse_multi_day_weekly()."""

    def test_parses_two_letter_days(self):
        assert parse_multi_day_weekly("weekly:tu,we,fr") == [1, 2, 4]

    def test_returns_days_in_week_order(self):
        """Day order in the rate shouldn't matter; the result is week order."""
        assert parse_multi_day_weekly("weekly:fr,tu,we") == [1, 2, 4]

    def test_accepts_longer_day_names_and_whitespace(self):
        assert parse_multi_day_weekly("weekly: Tuesday , weds , Fri ") == [1, 2, 4]

    def test_deduplicates_repeated_days(self):
        assert parse_multi_day_weekly("weekly:tu,tu,we") == [1, 2]

    def test_single_day_is_allowed(self):
        assert parse_multi_day_weekly("weekly:we") == [2]

    @pytest.mark.parametrize("rate", ["weekly", "bi-weekly", "monthly", "other", "none", ""])
    def test_plain_rates_are_not_multi_day(self, rate):
        assert parse_multi_day_weekly(rate) is None

    @pytest.mark.parametrize("rate", [None, 120, ["weekly:tu"]])
    def test_non_strings_are_not_multi_day(self, rate):
        assert parse_multi_day_weekly(rate) is None

    def test_unknown_day_invalidates_whole_rate(self):
        """A typo must not silently yield a partial schedule."""
        assert parse_multi_day_weekly("weekly:tu,xx,fr") is None

    def test_empty_day_list_is_rejected(self):
        assert parse_multi_day_weekly("weekly:") is None


class TestDayRendering:
    """Tests for the BYDAY / Zoom weekly_days renderers."""

    def test_byday_tokens(self):
        assert weekly_days_to_byday([1, 2, 4]) == "TU,WE,FR"

    def test_byday_full_week(self):
        assert weekly_days_to_byday([0, 1, 2, 3, 4, 5, 6]) == "MO,TU,WE,TH,FR,SA,SU"

    def test_zoom_days_use_sunday_as_one(self):
        """Zoom numbers weekdays Sun=1..Sat=7, so Tue/Wed/Fri is 3,4,6."""
        assert weekly_days_to_zoom([1, 2, 4]) == "3,4,6"

    def test_zoom_sunday_wraps_to_one(self):
        assert weekly_days_to_zoom([6]) == "1"

    def test_zoom_saturday_is_seven(self):
        assert weekly_days_to_zoom([5]) == "7"


class TestNextWeeklyDay:
    """Tests for next_weekly_day()."""

    def test_steps_to_next_day_in_set(self):
        tuesday = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert next_weekly_day(tuesday, [1, 2, 4]) == datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)

    def test_wraps_into_the_following_week(self):
        """Friday's next slot is the following Tuesday, four days on."""
        friday = datetime(2026, 11, 20, 14, 0, tzinfo=timezone.utc)
        assert next_weekly_day(friday, [1, 2, 4]) == datetime(2026, 11, 24, 14, 0, tzinfo=timezone.utc)

    def test_preserves_time_of_day(self):
        tuesday = datetime(2026, 11, 17, 9, 30, tzinfo=timezone.utc)
        assert next_weekly_day(tuesday, [1, 2, 4]).time() == tuesday.time()

    def test_single_day_set_advances_a_full_week(self):
        wednesday = datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)
        assert next_weekly_day(wednesday, [2]) == datetime(2026, 11, 25, 14, 0, tzinfo=timezone.utc)

    def test_start_off_pattern_finds_next_scheduled_day(self):
        """A Monday start still lands on the next day in the set."""
        monday = datetime(2026, 11, 16, 14, 0, tzinfo=timezone.utc)
        assert next_weekly_day(monday, [1, 2, 4]) == datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)


class TestGcalRecurrenceRules:
    """Tests for gcal._build_recurrence_rules() / _recurrence_cadence_matches()."""

    @pytest.fixture
    def gcal(self):
        from modules import gcal
        return gcal

    def test_multi_day_weekly_builds_byday_rule(self, gcal):
        start = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert gcal._build_recurrence_rules("weekly:tu,we,fr", start) == [
            "RRULE:FREQ=WEEKLY;BYDAY=TU,WE,FR"
        ]

    def test_plain_rates_are_unchanged(self, gcal):
        start = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert gcal._build_recurrence_rules("weekly", start) == ["RRULE:FREQ=WEEKLY"]
        assert gcal._build_recurrence_rules("bi-weekly", start) == ["RRULE:FREQ=WEEKLY;INTERVAL=2"]

    def test_matching_byday_is_not_a_cadence_change(self, gcal):
        start = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert gcal._recurrence_cadence_matches(
            ["RRULE:FREQ=WEEKLY;BYDAY=TU,WE,FR"], "weekly:tu,we,fr", start
        )

    def test_byday_order_does_not_affect_matching(self, gcal):
        start = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert gcal._recurrence_cadence_matches(
            ["RRULE:FREQ=WEEKLY;BYDAY=FR,TU,WE"], "weekly:tu,we,fr", start
        )

    def test_dropping_a_day_is_a_cadence_change(self, gcal):
        start = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert not gcal._recurrence_cadence_matches(
            ["RRULE:FREQ=WEEKLY;BYDAY=TU,WE"], "weekly:tu,we,fr", start
        )

    def test_plain_weekly_series_must_be_rebased_onto_multi_day(self, gcal):
        start = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert not gcal._recurrence_cadence_matches(
            ["RRULE:FREQ=WEEKLY"], "weekly:tu,we,fr", start
        )

    def test_existing_weekly_series_still_matches_weekly(self, gcal):
        """Regression guard: adding BYDAY to the cadence must not churn plain series."""
        start = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert gcal._recurrence_cadence_matches(["RRULE:FREQ=WEEKLY"], "weekly", start)

    @pytest.mark.parametrize("rate,rule", [
        ("weekly", "RRULE:FREQ=WEEKLY;BYDAY=WE"),
        ("bi-weekly", "RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=WE"),
    ])
    def test_single_day_byday_still_matches_plain_rate(self, gcal, rate, rule):
        """Google writes BYDAY=WE whenever a weekly series is touched in its UI.

        Treating that as a cadence change would cap the series with UNTIL=now and
        rebase every such call onto a brand-new event, losing the event id and any
        attendee RSVPs. A lone BYDAY day means the same thing as no BYDAY at all.
        """
        start = datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)
        assert gcal._recurrence_cadence_matches([rule], rate, start)

    def test_multi_day_series_does_not_match_plain_weekly(self, gcal):
        """The reverse direction is a real cadence change and must still rebase."""
        start = datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)
        assert not gcal._recurrence_cadence_matches(
            ["RRULE:FREQ=WEEKLY;BYDAY=TU,WE,FR"], "weekly", start
        )

    def test_single_day_byday_does_not_match_multi_day_rate(self, gcal):
        start = datetime(2026, 11, 17, 14, 0, tzinfo=timezone.utc)
        assert not gcal._recurrence_cadence_matches(
            ["RRULE:FREQ=WEEKLY;BYDAY=WE"], "weekly:tu,we,fr", start
        )

    def test_interval_mismatch_still_wins_over_byday(self, gcal):
        """A weekly rule can't satisfy a bi-weekly rate however its BYDAY reads."""
        start = datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)
        assert not gcal._recurrence_cadence_matches(
            ["RRULE:FREQ=WEEKLY;BYDAY=WE"], "bi-weekly", start
        )

    def test_monthly_byday_is_still_ignored(self, gcal):
        """A monthly call drifting to a different week of the month is not a cadence change."""
        start = datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)  # 3rd Wednesday
        assert gcal._recurrence_cadence_matches(
            ["RRULE:FREQ=MONTHLY;BYDAY=2WE"], "monthly", start
        )


class TestGcalInstanceAlignment:
    """The is_aligned branch of update_recurring_event for a multi-day series.

    When one instance is missing, an aligned next slot means "create a one-time event
    and leave the series alone". Falling through instead shifts the master event's
    DTSTART onto the target date, which drops that week's earlier siblings -- calls
    that have their own issues and mapping entries.
    """

    @pytest.fixture
    def gcal(self):
        from modules import gcal
        return gcal

    def _is_aligned(self, gcal, rate, target, closest_future):
        """The alignment decision as update_recurring_event makes it.

        TestMultiDayInstanceShift below drives the real function end to end; this
        covers the date arithmetic across more cases than mock setups are worth.
        """
        weekdays = gcal.parse_multi_day_weekly(rate)
        assert weekdays, "expected a multi-day rate"
        return gcal.next_weekly_day(target, weekdays).date() == closest_future

    def test_missing_wednesday_aligns_with_friday(self, gcal):
        """Wed missing, next instance Fri (2 days on) -- aligned, so preserve the series."""
        wednesday = datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)
        assert self._is_aligned(gcal, "weekly:tu,we,fr", wednesday, date(2026, 11, 20))

    def test_missing_friday_aligns_with_the_following_tuesday(self, gcal):
        """Fri missing, next instance the following Tue (4 days on) -- still aligned."""
        friday = datetime(2026, 11, 20, 14, 0, tzinfo=timezone.utc)
        assert self._is_aligned(gcal, "weekly:tu,we,fr", friday, date(2026, 11, 24))

    def test_seven_day_gap_is_not_aligned_for_a_multi_day_series(self, gcal):
        """A plain +7 days would have passed the old weekly check but is wrong here."""
        wednesday = datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)
        assert not self._is_aligned(gcal, "weekly:tu,we,fr", wednesday, date(2026, 11, 25))


class TestZoomRecurrencePayload:
    """Tests for the recurrence block zoom.create_recurring_meeting() sends."""

    def _captured_payload(self, occurrence_rate, start_time="2026-11-17T14:00:00Z"):
        from modules import zoom

        with patch("modules.zoom.get_access_token", return_value="token"), \
             patch("modules.zoom.requests.post") as mock_post:
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = {
                "join_url": "https://zoom.us/j/123",
                "id": 123,
            }
            zoom.create_recurring_meeting(
                topic="PQ-CL Breakout",
                start_time=start_time,
                duration=120,
                occurrence_rate=occurrence_rate,
            )
        return mock_post.call_args.kwargs["json"]

    def test_multi_day_weekly_sets_all_days(self):
        recurrence = self._captured_payload("weekly:tu,we,fr")["recurrence"]
        assert recurrence["type"] == 2
        assert recurrence["repeat_interval"] == 1
        assert recurrence["weekly_days"] == "3,4,6"

    def test_multi_day_weekly_is_a_single_recurring_meeting(self):
        """One meeting, so the series keeps one join URL across all three days."""
        assert self._captured_payload("weekly:tu,we,fr")["type"] == 8

    def test_duration_is_carried_through(self):
        assert self._captured_payload("weekly:tu,we,fr")["duration"] == 120

    def test_plain_weekly_still_uses_the_start_day_only(self):
        recurrence = self._captured_payload("weekly")["recurrence"]
        assert recurrence["weekly_days"] == "3"  # Tuesday
        assert recurrence["repeat_interval"] == 1

    def test_bi_weekly_is_unaffected(self):
        recurrence = self._captured_payload("bi-weekly")["recurrence"]
        assert recurrence["repeat_interval"] == 2
        assert recurrence["weekly_days"] == "3"

    def test_end_times_scales_with_the_number_of_weekdays(self):
        """end_times counts occurrences, so 12 would last only 4 weeks at 3/week."""
        assert self._captured_payload("weekly:tu,we,fr")["recurrence"]["end_times"] == 36

    def test_end_times_stays_within_zooms_cap(self):
        recurrence = self._captured_payload("weekly:mo,tu,we,th,fr,sa,su")["recurrence"]
        assert recurrence["end_times"] == 60

    def test_single_day_rates_keep_the_default_end_times(self):
        assert self._captured_payload("weekly")["recurrence"]["end_times"] == 12

    def test_typo_in_day_list_raises_instead_of_creating_a_meeting(self):
        """A bad day list must not quietly become a plain weekly meeting.

        gcal rejects the same string, so carrying on here would leave a live Zoom
        series with no calendar event behind it.
        """
        from modules import zoom

        with patch("modules.zoom.get_access_token", return_value="token"), \
             patch("modules.zoom.requests.post") as mock_post:
            with pytest.raises(ValueError, match="Unsupported occurrence rate"):
                zoom.create_recurring_meeting(
                    topic="PQ-CL Breakout",
                    start_time="2026-11-17T14:00:00Z",
                    duration=120,
                    occurrence_rate="weekly:tu,xx,fr",
                )
        mock_post.assert_not_called()

    def test_typo_is_not_swallowed_into_a_daily_meeting(self):
        """The recurrence block sits inside a bare `except Exception` whose fallback
        is a DAILY meeting, so the validation has to run before it."""
        from modules import zoom

        with patch("modules.zoom.get_access_token", return_value="token"), \
             patch("modules.zoom.requests.post") as mock_post:
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = {"join_url": "u", "id": 1}
            with pytest.raises(ValueError):
                zoom.create_recurring_meeting(
                    topic="PQ-CL Breakout",
                    start_time="2026-11-17T14:00:00Z",
                    duration=120,
                    occurrence_rate="weekly:nope",
                )
        mock_post.assert_not_called()


class TestYoutubeRecurringStreams:
    """Tests for create_recurring_streams() on a multi-day weekly rate."""

    def test_streams_follow_the_weekday_set(self):
        from modules import youtube_utils

        with patch("modules.youtube_utils.create_youtube_stream") as mock_create_stream:
            mock_create_stream.return_value = {"id": "test_stream_id"}

            result = youtube_utils.create_recurring_streams(
                title="PQ-CL Breakout",
                description="Test Description",
                start_time="2026-11-17T14:00:00Z",  # a Tuesday
                occurrence_rate="weekly:tu,we,fr",
                num_events=4,
            )

        assert len(result) == 4
        scheduled = [call[0][2] for call in mock_create_stream.call_args_list]
        assert scheduled == [
            "2026-11-17T14:00:00.000Z",  # Tue
            "2026-11-18T14:00:00.000Z",  # Wed
            "2026-11-20T14:00:00.000Z",  # Fri
            "2026-11-24T14:00:00.000Z",  # following Tue
        ]


class TestMissingCallProjection:
    """Tests for upcoming_calls.find_expected_missing_calls() on a multi-day series."""

    @pytest.fixture
    def find_missing(self):
        from scripts.upcoming_calls import find_expected_missing_calls
        return find_expected_missing_calls

    def _mapping(self, start_times):
        return {
            "pqcl": {
                "occurrence_rate": "weekly:tu,we,fr",
                "occurrences": [{"start_time": st} for st in start_times],
            }
        }

    def test_reports_each_missing_weekday_slot(self, find_missing, monkeypatch):
        monkeypatch.setattr(
            "scripts.upcoming_calls.get_call_series_config",
            lambda key: {"display_name": "PQ-CL Breakout"},
        )
        now = datetime(2026, 11, 18, 9, 0, tzinfo=timezone.utc)  # Wednesday morning
        monkeypatch.setattr("scripts.upcoming_calls.datetime", _frozen_datetime(now))

        # Only Tuesday happened; Wed and Fri of this week are still missing.
        missing = find_missing(self._mapping(["2026-11-17T14:00:00Z"]), days_ahead=4)

        expected = [m["expected_time"] for m in missing]
        assert expected == [
            datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc),
            datetime(2026, 11, 20, 14, 0, tzinfo=timezone.utc),
        ]

    def test_adjacent_day_does_not_satisfy_a_slot(self, find_missing, monkeypatch):
        """With a 2-day tolerance Tuesday's call would wrongly cover Wednesday's slot."""
        monkeypatch.setattr(
            "scripts.upcoming_calls.get_call_series_config",
            lambda key: {"display_name": "PQ-CL Breakout"},
        )
        now = datetime(2026, 11, 18, 9, 0, tzinfo=timezone.utc)
        monkeypatch.setattr("scripts.upcoming_calls.datetime", _frozen_datetime(now))

        missing = find_missing(self._mapping(["2026-11-17T14:00:00Z"]), days_ahead=1)

        assert [m["expected_time"] for m in missing] == [
            datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc)
        ]

    def test_scheduled_slots_are_not_reported(self, find_missing, monkeypatch):
        monkeypatch.setattr(
            "scripts.upcoming_calls.get_call_series_config",
            lambda key: {"display_name": "PQ-CL Breakout"},
        )
        now = datetime(2026, 11, 18, 9, 0, tzinfo=timezone.utc)
        monkeypatch.setattr("scripts.upcoming_calls.datetime", _frozen_datetime(now))

        mapping = self._mapping([
            "2026-11-17T14:00:00Z",
            "2026-11-18T14:00:00Z",
            "2026-11-20T14:00:00Z",
        ])
        assert find_missing(mapping, days_ahead=4) == []

    def test_weekday_held_at_a_different_hour_still_counts(self, find_missing, monkeypatch):
        """A series needn't hold every weekday at the same UTC time (e.g. an APAC
        Friday slot). Matching on the calendar date avoids a standing false alarm."""
        monkeypatch.setattr(
            "scripts.upcoming_calls.get_call_series_config",
            lambda key: {"display_name": "PQ-CL Breakout"},
        )
        now = datetime(2026, 11, 18, 9, 0, tzinfo=timezone.utc)
        monkeypatch.setattr("scripts.upcoming_calls.datetime", _frozen_datetime(now))

        mapping = self._mapping([
            "2026-11-17T14:00:00Z",
            "2026-11-18T14:00:00Z",
            "2026-11-20T02:00:00Z",  # Friday, 12 hours off the projected 14:00
        ])
        assert find_missing(mapping, days_ahead=4) == []

    def test_long_dormant_series_is_skipped(self, find_missing, monkeypatch):
        """Three quiet weeks reads as retired, not as a backlog of missing calls."""
        monkeypatch.setattr(
            "scripts.upcoming_calls.get_call_series_config",
            lambda key: {"display_name": "PQ-CL Breakout"},
        )
        now = datetime(2026, 12, 22, 9, 0, tzinfo=timezone.utc)
        monkeypatch.setattr("scripts.upcoming_calls.datetime", _frozen_datetime(now))

        assert find_missing(self._mapping(["2026-11-17T14:00:00Z"]), days_ahead=7) == []




class _Call:
    def __init__(self, response):
        self.response = response

    def execute(self):
        return self.response


class _Events:
    """Minimal Calendar events resource for a Tue/Wed/Fri series.

    The Wednesday instance is absent and not cancelled, and the next instance is
    the Friday of the same week -- the exact shape that used to fall through to the
    series shift.
    """

    def __init__(self, rrule="RRULE:FREQ=WEEKLY;BYDAY=TU,WE,FR"):
        self.rrule = rrule
        self.update_calls = []

    def get(self, **kwargs):
        return _Call({
            "id": kwargs["eventId"],
            "summary": "PQ-CL Breakout",
            "recurrence": [self.rrule],
            "start": {"dateTime": "2026-11-17T14:00:00Z", "timeZone": "UTC"},
            "end": {"dateTime": "2026-11-17T16:00:00Z", "timeZone": "UTC"},
        })

    def instances(self, **kwargs):
        if kwargs.get("showDeleted"):
            return _Call({"items": []})
        # Tuesday has already happened; Friday is the next one. No Wednesday.
        return _Call({"items": [
            {
                "id": "series_20261117T140000Z",
                "status": "confirmed",
                "start": {"dateTime": "2026-11-17T14:00:00Z", "timeZone": "UTC"},
            },
            {
                "id": "series_20261120T140000Z",
                "status": "confirmed",
                "start": {"dateTime": "2026-11-20T14:00:00Z", "timeZone": "UTC"},
            },
        ]})

    def update(self, **kwargs):
        self.update_calls.append(kwargs)
        return _Call({**kwargs["body"], "id": kwargs["eventId"],
                      "htmlLink": "https://calendar.google.com/event?eid=x"})


class _Service:
    def __init__(self, events):
        self.events_resource = events

    def events(self):
        return self.events_resource


class TestMultiDayInstanceShift:
    """End-to-end: a missing instance must not shift the master event.

    Patching DTSTART onto the target date drops every instance before it -- for a
    multi-day series that means the same week's earlier calls, which have their own
    issues, Zoom occurrences and mapping entries.
    """

    def _run(self, rate):
        from modules.gcal import update_recurring_event

        events = _Events()
        service = _Service(events)
        with patch("modules.gcal.get_calendar_service", return_value=service), \
             patch("modules.gcal.create_event") as mock_create:
            mock_create.return_value = {"id": "one_time", "htmlLink": "https://cal/one_time"}
            result = update_recurring_event(
                event_id="series",
                summary="PQ-CL Breakout #3",
                start_dt=datetime(2026, 11, 18, 14, 0, tzinfo=timezone.utc),
                duration_minutes=120,
                calendar_id="calendar",
                occurrence_rate=rate,
                description="Meeting: https://zoom.us/j/123",
            )
        return result, events, mock_create

    def test_missing_wednesday_creates_a_one_time_event(self):
        result, _, mock_create = self._run("weekly:tu,we,fr")
        mock_create.assert_called_once()
        assert result["action_detail"] == "one_time_created_series_preserved"

    def test_missing_wednesday_leaves_the_series_untouched(self):
        """The master event must not be patched onto the target date."""
        _, events, _ = self._run("weekly:tu,we,fr")
        assert [c["eventId"] for c in events.update_calls] == []

    def test_series_id_is_returned_not_the_one_time_event_id(self):
        result, _, _ = self._run("weekly:tu,we,fr")
        assert result["id"] == "series"

    def test_cadence_check_does_not_rebase_a_matching_multi_day_series(self):
        """Guards the path into this branch: a BYDAY series matching its rate must
        not be capped and recreated before the instance logic is even reached."""
        _, events, _ = self._run("weekly:tu,we,fr")
        bodies = [c["body"] for c in events.update_calls]
        assert not any("recurrence" in b for b in bodies)


class TestZoomSeriesAnchor:
    """The three weekday issues of a multi-day series share one Zoom series.

    Patching the series start_time to each issue's date in turn would march the
    anchor forward past that week's earlier occurrences, stranding the occurrence
    ids already recorded against their issues.
    """

    def _update(self, occurrence_rate):
        sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
        from scripts.handle_protocol_call import ProtocolCallHandler

        handler = ProtocolCallHandler.__new__(ProtocolCallHandler)
        handler.mapping_manager = SimpleNamespace(get_series_meeting_id=lambda s: "99")
        handler._get_zoom_meeting_title = lambda d: "PQ-CL Breakout #3"
        handler._sync_breakout_meeting_topics = lambda *a, **k: None

        fake_zoom = SimpleNamespace(
            get_meeting=lambda mid: {"timezone": "UTC", "occurrences": []},
            is_recurring_meeting=lambda d: True,
            find_occurrence_for_date=lambda occ, st: None,
            needs_time_update=lambda *a: False,
            extend_recurring_meeting_end_date=lambda *a: None,
            update_meeting_occurrence=lambda *a: {},
            get_meeting_url_with_passcode=lambda mid: None,
            update_meeting=MagicMock(return_value={"join_url": "https://zoom.us/j/99"}),
        )
        # `from modules import zoom` resolves the package attribute, so that is
        # what has to be patched -- sys.modules is consulted only on first import.
        with patch("modules.zoom", fake_zoom):
            handler._update_zoom_meeting({
                "call_series": "pqcl",
                "start_time": "2026-11-18T14:00:00Z",
                "duration": 120,
                "occurrence_rate": occurrence_rate,
            })
        return fake_zoom.update_meeting

    def test_multi_day_series_anchor_is_left_alone(self):
        """start_time is passed as None, so the PATCH omits it entirely."""
        update_meeting = self._update("weekly:tu,we,fr")
        assert update_meeting.call_args[0][2] is None

    def test_multi_day_series_still_syncs_title_and_duration(self):
        update_meeting = self._update("weekly:tu,we,fr")
        args = update_meeting.call_args[0]
        assert args[1] == "PQ-CL Breakout #3"
        assert args[3] == 120

    def test_single_day_series_anchor_still_moves(self):
        """Regression guard: ordinary weekly series keep the existing behaviour."""
        update_meeting = self._update("weekly")
        assert update_meeting.call_args[0][2] == "2026-11-18T14:00:00Z"
