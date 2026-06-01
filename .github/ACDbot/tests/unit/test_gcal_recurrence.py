from modules.gcal import truncate_recurrence_rules


def test_truncate_recurrence_rules_caps_rrules_and_preserves_exdates():
    recurrence = [
        "RRULE:FREQ=WEEKLY;INTERVAL=2;UNTIL=20261231T000000Z",
        "EXDATE:20260610T140000Z",
        "RRULE:COUNT=10;FREQ=MONTHLY;BYDAY=2WE",
    ]

    result = truncate_recurrence_rules(recurrence, "20260601T120000Z")

    assert result == [
        "RRULE:FREQ=WEEKLY;INTERVAL=2;UNTIL=20260601T120000Z",
        "EXDATE:20260610T140000Z",
        "RRULE:FREQ=MONTHLY;BYDAY=2WE;UNTIL=20260601T120000Z",
    ]
    assert recurrence == [
        "RRULE:FREQ=WEEKLY;INTERVAL=2;UNTIL=20261231T000000Z",
        "EXDATE:20260610T140000Z",
        "RRULE:COUNT=10;FREQ=MONTHLY;BYDAY=2WE",
    ]


def test_truncate_recurrence_rules_removes_date_only_until():
    result = truncate_recurrence_rules(
        ["RRULE:FREQ=MONTHLY;UNTIL=20261231;BYDAY=-1TH"],
        "20260601T120000Z",
    )

    assert result == ["RRULE:FREQ=MONTHLY;BYDAY=-1TH;UNTIL=20260601T120000Z"]
