"""
Test data for form parser tests.

Contains various form body examples used in unit tests.
"""

# Poorly formatted issue examples
POORLY_FORMATTED_ISSUE = """
Meeting Info
July 28, 2025, 15:00 UTC
Duration: 60 minutes
Meet link: shared in [#state-tree-migration](https://discord.gg/6ty8Z6Ev) Eth R&D Discord right before the call
[All previous recordings](https://www.youtube.com/playlist?list=PLJqWcTqh_zKG-A9qKJ-7niPaRXHmXnpU9)

Agenda

1. Team updates
2. New testnet
3. Bloatnet updates
"""

FREE_FORM_TEXT = """
This is just some random text
with no structured format
that should not be parsed
"""

# Partial format examples
PARTIAL_OLD_FORMAT = """
Call series: All Core Devs - Execution
Duration: 90 minutes
# Missing other required fields
"""

PARTIAL_NEW_FORMAT = """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

# Missing other required fields
"""

MIXED_FORMATS = """
### Call Series

All Core Devs - Execution

Call series: All Core Devs - Execution
Duration: 90 minutes
"""

# Malformed markdown example
MALFORMED_MARKDOWN = """
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

### Need YouTube Streams

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

_No response_

### Custom Meeting Link (Optional)

_No response_

### Agenda

Test agenda for the meeting

### Extra Field

This should be ignored
"""

# Form with markdown links
FORM_WITH_MARKDOWN_LINKS = """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

[April 24, 2025, 14:00 UTC](https://time.is/2025-04-24T14:00:00Z)

### Is Recurring

- [x] Yes

### Occurrence Rate

Bi-weekly
"""

# Invalid form examples
INVALID_DURATION_FORM = """
### Call Series

All Core Devs - Execution

### Duration

invalid

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

_No response_

### Custom Meeting Link (Optional)

_No response_

### Agenda

Test agenda for the meeting
"""

INVALID_START_TIME_FORM = """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

invalid_time

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

_No response_

### Custom Meeting Link (Optional)

_No response_

### Agenda

Test agenda for the meeting
"""

# One-off meeting example
ONE_OFF_MEETING_FORM = """
### Call Series

One-time call

### Duration

120 minutes

### UTC Date & Time

April 26, 2025, 16:00 UTC

### Occurrence Rate

None

### Use Custom Meeting Link (Optional)

- [x] Yes

### YouTube Livestream Link (Optional)

- [ ] No

### Display Zoom Link in Calendar Invite (Optional)

- [ ] No

### Facilitator Emails (Optional)

organizer@example.com

### Custom Meeting Link (Optional)

_No response_

### Agenda

One-off meeting agenda
"""

MISSING_REQUIRED_FIELDS_FORM = """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC
"""

BOOLEAN_TEST_FORM_TEMPLATE = """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Use Custom Meeting Link (Optional)

{skip_zoom}
"""

CALL_SERIES_TEST_FORMS = {
    "All Core Devs - Execution": """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC
""",
    "All Core Devs - Consensus": """
### Call Series

All Core Devs - Consensus

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC
""",
    "One-time call": """
### Call Series

One-time call

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC
"""
}

OCCURRENCE_RATE_TEST_FORMS = {
    "Weekly": """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Occurrence Rate

Weekly
""",
    "Bi-weekly": """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Occurrence Rate

Bi-weekly
""",
    "Monthly": """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Occurrence Rate

Monthly
""",
    "Quarterly": """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Occurrence Rate

Quarterly
""",
    "None": """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Occurrence Rate

None
""",
    "Other": """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Occurrence Rate

Other
""",
    "Unknown Rate": """
### Call Series

All Core Devs - Execution

### Duration

90 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Occurrence Rate

Unknown Rate
"""
}

WHITESPACE_FORM = """
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
"""

EDGE_CASE_FORM = """
### Call Series

All Core Devs - Execution

### Duration

999999 minutes

### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

""" + "A" * 10000  # Very long agenda

# Agenda extraction test examples
AGENDA_WITH_USER_HEADERS = """
### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

# Meeting Agenda

## Topics to Discuss
- Topic 1
- Topic 2

### Action Items
- Action 1
- Action 2

## Next Steps
- Step 1
- Step 2

### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

test@example.com
"""

AGENDA_WITH_COMPLEX_FORMATTING = """
### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

**Bold text** and *italic text*

- List item 1
  - Sub-item 1
  - Sub-item 2
- List item 2

> Quote block
> More quote

`Code snippet`

### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

test@example.com
"""

AGENDA_EMPTY_CONTENT = """
### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda


### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

test@example.com
"""

AGENDA_WHITESPACE_ONLY = """
### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda



### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

test@example.com
"""

AGENDA_VERY_LONG_CONTENT = """
### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

""" + "A" * 10000 + """

### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

test@example.com
"""

AGENDA_MISSING_CALL_SERIES_BOUNDARY = """
### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

Test agenda content

### Some Other Section

Other content

### Duration

90 minutes

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

test@example.com
"""

AGENDA_WITH_EXTRA_NEWLINES = """### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda
Test agenda content

### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

test@example.com
"""

AGENDA_PRESERVES_FORMATTING = """
### UTC Date & Time

April 24, 2025, 14:00 UTC

### Agenda

   Indented content

   More indented content

### Call Series

All Core Devs - Execution

### Duration

90 minutes

### Occurrence Rate

Bi-weekly

### Use Custom Meeting Link (Optional)

- [ ] No

### YouTube Livestream Link (Optional)

- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)

- [x] Yes

### Facilitator Emails (Optional)

test@example.com
"""