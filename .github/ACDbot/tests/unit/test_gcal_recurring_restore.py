from datetime import datetime, timezone
from unittest.mock import patch

from modules.gcal import update_recurring_event


class _CalendarCall:
    def __init__(self, response):
        self.response = response

    def execute(self):
        return self.response


class _CalendarEvents:
    def __init__(self):
        self.instance_calls = []
        self.update_calls = []

    def get(self, **kwargs):
        return _CalendarCall({
            "id": kwargs["eventId"],
            "recurrence": ["RRULE:FREQ=WEEKLY;INTERVAL=2"],
        })

    def instances(self, **kwargs):
        self.instance_calls.append(kwargs)
        if kwargs.get("showDeleted"):
            return _CalendarCall({
                "items": [
                    {
                        "id": "series_20260527T140000Z",
                        "status": "cancelled",
                        "recurringEventId": "series",
                        "originalStartTime": {
                            "dateTime": "2026-05-27T14:00:00Z",
                            "timeZone": "UTC",
                        },
                    }
                ]
            })
        return _CalendarCall({
            "items": [
                {
                    "id": "series_20260513T140000Z",
                    "status": "confirmed",
                    "start": {
                        "dateTime": "2026-05-13T14:00:00Z",
                        "timeZone": "UTC",
                    },
                }
            ]
        })

    def update(self, **kwargs):
        self.update_calls.append(kwargs)
        return _CalendarCall({
            **kwargs["body"],
            "id": kwargs["eventId"],
            "recurringEventId": "series",
            "htmlLink": "https://calendar.google.com/event?eid=restored",
        })


class _CalendarService:
    def __init__(self):
        self.events_resource = _CalendarEvents()

    def events(self):
        return self.events_resource


def test_update_recurring_event_restores_cancelled_instance_without_rebasing_series():
    service = _CalendarService()
    start_dt = datetime(2026, 5, 27, 14, 0, tzinfo=timezone.utc)

    with patch("modules.gcal.get_calendar_service", return_value=service):
        result = update_recurring_event(
            event_id="series",
            summary="Glamsterdam Repricings #8",
            start_dt=start_dt,
            duration_minutes=60,
            calendar_id="calendar",
            occurrence_rate="bi-weekly",
            description="Meeting: https://zoom.us/j/123",
        )

    events = service.events_resource
    assert len(events.instance_calls) == 2
    assert "showDeleted" not in events.instance_calls[0]
    assert events.instance_calls[1]["showDeleted"] is True

    assert len(events.update_calls) == 1
    restored_body = events.update_calls[0]["body"]
    assert events.update_calls[0]["eventId"] == "series_20260527T140000Z"
    assert restored_body["status"] == "confirmed"
    assert restored_body["recurringEventId"] == "series"
    assert restored_body["originalStartTime"]["dateTime"] == "2026-05-27T14:00:00Z"
    assert restored_body["start"]["dateTime"] == "2026-05-27T14:00:00+00:00"
    assert restored_body["end"]["dateTime"] == "2026-05-27T15:00:00+00:00"

    assert result == {
        "htmlLink": "https://calendar.google.com/event?eid=restored",
        "id": "series",
        "action_detail": "cancelled_instance_restored",
    }


class _CadenceChangeEvents:
    """Weekly series that started 2026-09-01, with instances on every Tuesday since."""

    def __init__(self):
        self.patch_calls = []
        self.insert_calls = []

    def get(self, **kwargs):
        return _CalendarCall({
            "id": kwargs["eventId"],
            "recurrence": ["RRULE:FREQ=WEEKLY"],
            "start": {"dateTime": "2026-09-01T14:00:00Z", "timeZone": "UTC"},
        })

    def patch(self, **kwargs):
        self.patch_calls.append(kwargs)
        return _CalendarCall({**kwargs["body"], "id": kwargs["eventId"]})

    def insert(self, **kwargs):
        self.insert_calls.append(kwargs)
        return _CalendarCall({
            **kwargs["body"],
            "id": "new_series",
            "htmlLink": "https://calendar.google.com/event?eid=new_series",
        })


class _CadenceChangeService:
    def __init__(self):
        self.events_resource = _CadenceChangeEvents()

    def events(self):
        return self.events_resource


def test_update_recurring_event_switches_cadence_keeping_past_instances():
    service = _CadenceChangeService()
    start_dt = datetime(2026, 9, 22, 14, 0, tzinfo=timezone.utc)
    now = datetime(2026, 9, 10, 12, 0, tzinfo=timezone.utc)

    with patch("modules.gcal.get_calendar_service", return_value=service), \
            patch("modules.gcal._utcnow", return_value=now):
        result = update_recurring_event(
            event_id="series",
            summary="Frame Transaction Breakout",
            start_dt=start_dt,
            duration_minutes=60,
            calendar_id="calendar",
            occurrence_rate="bi-weekly",
            description="Issue: https://github.com/ethereum/pm/issues/2221",
        )

    events = service.events_resource

    # Old weekly series is capped at "now", so Sep 1 and Sep 8 survive but Sep 15 does not.
    assert len(events.patch_calls) == 1
    assert events.patch_calls[0]["eventId"] == "series"
    assert events.patch_calls[0]["body"] == {
        "recurrence": ["RRULE:FREQ=WEEKLY;UNTIL=20260910T120000Z"]
    }

    # A bi-weekly series takes over from the target date.
    assert len(events.insert_calls) == 1
    new_body = events.insert_calls[0]["body"]
    assert new_body["recurrence"] == ["RRULE:FREQ=WEEKLY;INTERVAL=2"]
    assert new_body["start"]["dateTime"] == "2026-09-22T14:00:00+00:00"

    assert result == {
        "htmlLink": "https://calendar.google.com/event?eid=new_series",
        "id": "new_series",
        "action_detail": "cadence_changed_series_split",
    }
