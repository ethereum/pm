#!/usr/bin/env python3
"""
Processing one PQ-CL call must not disturb its already-scheduled siblings.

A multi-day series is the first case where several FUTURE occurrences can exist
at once. The auto-create workflow avoids it by opening an issue only once the
previous call has finished, so in normal operation no un-held call is ever
disturbed -- but the handler can still be run in that state: a facilitator can
file the week ahead by hand, reopen a closed issue, or edit an older one. When
Wednesday's issue is handled then, Tuesday's call has its Zoom occurrence,
calendar instance and Discourse topic already in place and has not yet happened.

Every single-day series avoids this by construction -- call N has always taken
place before call N+1's issue is handled -- so none of it was previously exercised.

These tests seed a mapping with Tuesday already scheduled, run the real handler
for Wednesday, and assert nothing of Tuesday's survives altered.
"""

import json
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from modules.mapping_manager import MappingManager
from scripts.handle_protocol_call import ProtocolCallHandler

TUESDAY = "2026-11-17T14:00:00Z"
WEDNESDAY = "2026-11-18T14:00:00Z"
SERIES_MEETING_ID = "88800011122"
SERIES_EVENT_ID = "pqcl_series_event"
TUESDAY_OCCURRENCE_ID = "1763388000"
WEDNESDAY_OCCURRENCE_ID = "1763474400"


@pytest.fixture
def mapping_file(tmp_path):
    """A mapping where Tuesday's call is scheduled but has not happened yet."""
    path = tmp_path / "meeting_topic_mapping.json"
    path.write_text(json.dumps({
        "pqcl": {
            "call_series": "pqcl",
            "meeting_id": SERIES_MEETING_ID,
            "calendar_event_id": SERIES_EVENT_ID,
            "occurrence_rate": "weekly:tu,we,fr",
            "occurrences": [
                {
                    "occurrence_number": 1,
                    "issue_number": 5001,
                    "issue_title": "PQ-CL Breakout #1, November 17, 2026",
                    "discourse_topic_id": 40001,
                    "start_time": TUESDAY,
                    "duration": 120,
                    "zoom_occurrence_id": TUESDAY_OCCURRENCE_ID,
                }
            ],
        }
    }))
    return path


@pytest.fixture
def wednesday_call_data():
    return {
        "issue_number": 5002,
        "issue_title": "PQ-CL Breakout #2, November 18, 2026",
        "issue_url": "https://github.com/ethereum/pm/issues/5002",
        "call_series": "pqcl",
        "start_time": WEDNESDAY,
        "duration": 120,
        "occurrence_rate": "weekly:tu,we,fr",
        "display_zoom_link_in_invite": True,
    }


@pytest.fixture
def handler(mapping_file):
    h = ProtocolCallHandler.__new__(ProtocolCallHandler)
    h.mapping_manager = MappingManager(mapping_file)
    h.logger = SimpleNamespace(
        debug=lambda *a, **k: None, info=lambda *a, **k: None,
        error=lambda *a, **k: None, warning=lambda *a, **k: None,
    )
    return h


def _fake_zoom():
    """A Zoom series holding all three of the week's occurrences."""
    return SimpleNamespace(
        get_meeting=lambda mid: {
            "timezone": "UTC",
            "type": 8,
            "topic": "PQ-CL Breakout #1, November 17, 2026",
            "occurrences": [
                {"occurrence_id": TUESDAY_OCCURRENCE_ID, "start_time": TUESDAY, "duration": 120},
                {"occurrence_id": WEDNESDAY_OCCURRENCE_ID, "start_time": WEDNESDAY, "duration": 120},
            ],
        },
        is_recurring_meeting=lambda d: True,
        find_occurrence_for_date=lambda occs, st: next(
            (o for o in occs if o["start_time"][:10] == st[:10]), None
        ),
        needs_time_update=lambda *a: False,
        extend_recurring_meeting_end_date=MagicMock(),
        update_meeting_occurrence=MagicMock(return_value={}),
        update_meeting=MagicMock(return_value={"join_url": "https://zoom.us/j/888"}),
        create_recurring_meeting=MagicMock(),
        create_meeting=MagicMock(),
        get_meeting_url_with_passcode=lambda mid: None,
    )


class TestExistingResourceDetection:
    """Wednesday must be recognised as a new occurrence of an existing series."""

    def test_new_occurrence_sees_series_zoom(self, handler, wednesday_call_data):
        existing = handler._check_existing_resources(wednesday_call_data)
        assert existing["has_zoom"] is True

    def test_new_occurrence_sees_series_calendar(self, handler, wednesday_call_data):
        existing = handler._check_existing_resources(wednesday_call_data)
        assert existing["has_calendar"] is True
        assert existing["calendar_event_id"] == SERIES_EVENT_ID

    def test_new_occurrence_has_no_discourse_of_its_own(self, handler, wednesday_call_data):
        """Discourse is per-occurrence, so Wednesday must get its own topic."""
        existing = handler._check_existing_resources(wednesday_call_data)
        assert existing["has_discourse"] is False

    def test_has_zoom_routes_to_the_update_path(self, handler, wednesday_call_data):
        """_create_zoom_meeting has a second, unguarded series start_time patch.

        has_zoom being True is what keeps Wednesday out of it; if this ever flips,
        the anchor guard is bypassed and the sibling protection silently stops.
        """
        existing = handler._check_existing_resources(wednesday_call_data)
        handler._update_zoom_meeting = MagicMock(return_value={})
        handler._create_zoom_meeting = MagicMock(return_value={})

        handler._handle_zoom_resource(wednesday_call_data, existing)

        handler._update_zoom_meeting.assert_called_once()
        handler._create_zoom_meeting.assert_not_called()


class TestTuesdayZoomIsUnharmed:
    """Handling Wednesday must leave Tuesday's Zoom occurrence alone."""

    def _run(self, handler, call_data):
        fake = _fake_zoom()
        existing = handler._check_existing_resources(call_data)
        with patch("modules.zoom", fake, create=True):
            handler._handle_zoom_resource(call_data, existing)
        return fake

    def test_series_anchor_is_not_moved_to_wednesday(self, handler, wednesday_call_data):
        """Moving the anchor forward would drop Tuesday from the occurrence list."""
        fake = self._run(handler, wednesday_call_data)
        assert fake.update_meeting.call_args[0][2] is None

    def test_tuesdays_occurrence_is_never_patched(self, handler, wednesday_call_data):
        fake = self._run(handler, wednesday_call_data)
        patched = [c[0][1] for c in fake.update_meeting_occurrence.call_args_list]
        assert TUESDAY_OCCURRENCE_ID not in patched

    def test_the_series_is_not_recreated(self, handler, wednesday_call_data):
        """A second create would mint a new join URL and orphan Tuesday's."""
        fake = self._run(handler, wednesday_call_data)
        fake.create_recurring_meeting.assert_not_called()
        fake.create_meeting.assert_not_called()

    def test_recurrence_end_is_not_extended_when_the_occurrence_exists(
        self, handler, wednesday_call_data
    ):
        fake = self._run(handler, wednesday_call_data)
        fake.extend_recurring_meeting_end_date.assert_not_called()

    def test_tuesdays_mapping_entry_is_untouched(self, handler, wednesday_call_data, mapping_file):
        before = json.loads(mapping_file.read_text())["pqcl"]["occurrences"][0]
        self._run(handler, wednesday_call_data)
        after = json.loads(mapping_file.read_text())["pqcl"]["occurrences"][0]
        assert before == after


class TestTuesdayCalendarIsUnharmed:
    """Handling Wednesday must update only the Wednesday instance."""

    def _run(self, handler, call_data):
        instances = {
            "items": [
                {"id": "inst_tue", "status": "confirmed",
                 "start": {"dateTime": TUESDAY, "timeZone": "UTC"},
                 "summary": "PQ-CL Breakout",
                 "description": "Issue: https://github.com/ethereum/pm/issues/5001"},
                {"id": "inst_wed", "status": "confirmed",
                 "start": {"dateTime": WEDNESDAY, "timeZone": "UTC"},
                 "summary": "PQ-CL Breakout",
                 "description": "Issue: https://github.com/ethereum/pm/issues/5001"},
            ]
        }
        updated = []

        class _Events:
            def get(self, **kw):
                return SimpleNamespace(execute=lambda: {
                    "id": kw["eventId"],
                    "summary": "PQ-CL Breakout",
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=TU,WE,FR"],
                    "start": {"dateTime": TUESDAY, "timeZone": "UTC"},
                    "end": {"dateTime": "2026-11-17T16:00:00Z", "timeZone": "UTC"},
                })

            def instances(self, **kw):
                return SimpleNamespace(
                    execute=lambda: {"items": []} if kw.get("showDeleted") else instances
                )

            def update(self, **kw):
                updated.append(kw)
                return SimpleNamespace(execute=lambda: {
                    **kw["body"], "id": kw["eventId"],
                    "recurringEventId": SERIES_EVENT_ID,
                    "htmlLink": "https://calendar.google.com/x",
                })

        service = SimpleNamespace(events=lambda: _Events())
        existing = handler._check_existing_resources(call_data)
        with patch("modules.gcal.get_calendar_service", return_value=service), \
             patch("modules.gcal.create_event") as create_event, \
             patch("modules.gcal.create_recurring_event") as create_series, \
             patch.dict("os.environ", {"GCAL_ID": "cal"}):
            handler._last_zoom_url = "https://zoom.us/j/888"
            result = handler._handle_calendar_resource(call_data, existing)
        return result, updated, create_event, create_series

    def test_only_the_wednesday_instance_is_updated(self, handler, wednesday_call_data):
        _, updated, _, _ = self._run(handler, wednesday_call_data)
        assert [u["eventId"] for u in updated] == ["inst_wed"]

    def test_the_master_event_is_not_patched(self, handler, wednesday_call_data):
        """Patching the master would shift DTSTART and drop Tuesday's instance."""
        _, updated, _, _ = self._run(handler, wednesday_call_data)
        assert SERIES_EVENT_ID not in [u["eventId"] for u in updated]

    def test_the_recurrence_rule_is_not_rewritten(self, handler, wednesday_call_data):
        _, updated, _, _ = self._run(handler, wednesday_call_data)
        assert not any("recurrence" in u["body"] for u in updated)

    def test_no_duplicate_series_is_created(self, handler, wednesday_call_data):
        _, _, create_event, create_series = self._run(handler, wednesday_call_data)
        create_series.assert_not_called()
        create_event.assert_not_called()

    def test_wednesday_instance_gets_its_own_issue_link(self, handler, wednesday_call_data):
        """Tuesday's instance keeps pointing at Tuesday's issue."""
        _, updated, _, _ = self._run(handler, wednesday_call_data)
        assert "issues/5002" in updated[0]["body"]["description"]

    def test_the_series_event_id_is_still_returned(self, handler, wednesday_call_data):
        """The mapping must keep pointing at the series, not at an instance."""
        result, _, _, _ = self._run(handler, wednesday_call_data)
        assert result["calendar_event_id"] == SERIES_EVENT_ID


class TestTuesdayDiscourseIsUnharmed:
    """Discourse topics are per-occurrence; Wednesday must create its own."""

    def _run(self, handler, call_data):
        fake = SimpleNamespace(
            create_or_update_topic=MagicMock(
                return_value={"topic_id": 40002, "action": "created"}
            ),
            DiscourseDuplicateTitleError=type(
                "DiscourseDuplicateTitleError", (Exception,), {"title": ""}
            ),
        )
        existing = handler._check_existing_resources(call_data)
        handler._build_discourse_body = lambda d: "body"
        with patch("modules.discourse", fake, create=True):
            result = handler._handle_discourse_resource(call_data, existing)
        return result, fake

    def test_a_new_topic_is_created_for_wednesday(self, handler, wednesday_call_data):
        result, fake = self._run(handler, wednesday_call_data)
        assert fake.create_or_update_topic.call_args.kwargs["topic_id"] is None
        assert result["discourse_topic_id"] == 40002

    def test_tuesdays_topic_is_not_overwritten(self, handler, wednesday_call_data):
        """Passing Tuesday's id would retitle her topic to Wednesday's call."""
        _, fake = self._run(handler, wednesday_call_data)
        assert fake.create_or_update_topic.call_args.kwargs["topic_id"] != 40001


class TestReprocessingTuesdayItself:
    """Re-running Tuesday's own issue (an edit, or a re-run) must be a no-op."""

    @pytest.fixture
    def tuesday_call_data(self):
        return {
            "issue_number": 5001,
            "issue_title": "PQ-CL Breakout #1, November 17, 2026",
            "issue_url": "https://github.com/ethereum/pm/issues/5001",
            "call_series": "pqcl",
            "start_time": TUESDAY,
            "duration": 120,
            "occurrence_rate": "weekly:tu,we,fr",
            "display_zoom_link_in_invite": True,
        }

    def test_existing_discourse_topic_is_reused(self, handler, tuesday_call_data):
        existing = handler._check_existing_resources(tuesday_call_data)
        assert existing["has_discourse"] is True

    def test_no_second_zoom_series_is_created(self, handler, tuesday_call_data):
        fake = _fake_zoom()
        existing = handler._check_existing_resources(tuesday_call_data)
        with patch("modules.zoom", fake, create=True):
            handler._handle_zoom_resource(tuesday_call_data, existing)
        fake.create_recurring_meeting.assert_not_called()
