#!/usr/bin/env python3
"""Auto-create the next PQ-CL Breakout issue.

The PQ-CL Breakout meets three times a week (Tue/Wed/Fri), which is too often to
ask a facilitator to open issues by hand. This script opens them instead -- one
at a time, and with no human action required at any point.

WHAT RELEASES THE NEXT ISSUE

  The next call's issue is created only once every call already on record has
  finished (plus SETTLE_AFTER_CALL). Nothing else gates it: not a human, not the
  issue's open/closed state.

  It is tempting to copy auto-create-acd-issue.py and gate on the previous issue
  being CLOSED. That is wrong here. Issues are closed automatically by
  close_stale_meetings.py, 24 hours after the meeting ends -- which is slower
  than this series' own cadence. Tuesday's issue is not closed until Wednesday
  evening, by which time Wednesday's call has already happened, so a close-gated
  series would skip every Wednesday forever. A bi-weekly series never notices
  because its gap is fourteen days.

WHY ONE AT A TIME

  A multi-day series is ONE recurring Zoom meeting, and a Zoom meeting's topic is
  a series-level field -- the three weekdays cannot each carry their own. ACDbot
  sets that topic from the issue title every time it handles an issue. So if
  Tuesday's, Wednesday's and Friday's issues were opened in one batch, the live
  Zoom topic would read "Friday" for all three calls, and each recording -- which
  captures the topic as it stands when the call happens -- would be stamped with
  the wrong call's title.

  Waiting for the previous call to finish before opening the next issue keeps the
  Zoom topic naming the call that is actually about to happen, which is the
  invariant every single-day series gets for free. Note that this is about when
  an issue is CREATED (and so handled), not about how many are open: the previous
  call's issue is still open for another day or so, which is harmless.

Auth:
  GITHUB_TOKEN -- the per-run token provided by GitHub Actions. Issues created
  with it are authored by github-actions[bot] and do NOT emit an issues.opened
  event, so the workflow invokes handle_protocol_call.py directly afterwards
  rather than relying on the event-driven protocol-call-workflow.

  The created issue number is written to $GITHUB_OUTPUT as `created_issues`
  (comma-separated, for symmetry with the ACD workflow) for that follow-up step.

Usage:
  python3 auto-create-pqcl-issue.py                          # create the next issue if due
  python3 auto-create-pqcl-issue.py --dry-run                # print what would be created
  python3 auto-create-pqcl-issue.py --start-date 2027-01-05  # don't schedule anything earlier
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

# Reuse ACDbot's tested weekday parser rather than writing a second one. It is
# pure stdlib, so this works under plain `python3` with no project install.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ACDbot"))
from modules.datetime_utils import parse_multi_day_weekly  # noqa: E402

REPO = os.environ.get("GITHUB_REPOSITORY", "ethereum/pm")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN", "")

# Must match the pqcl entry in .github/ACDbot/call_series_config.yml.
# tests/unit/test_auto_create_pqcl.py asserts they stay in step.
SERIES_KEY = "pqcl"
DISPLAY_NAME = "PQ-CL Breakout"
OCCURRENCE_RATE = "weekly:tu,we,fr"
DURATION_MINUTES = 120
DURATION = f"{DURATION_MINUTES} minutes"

# Shared across the PQ series, so the title regex below does the real narrowing.
LABELS = ["PostQuantum", "protocol-call"]

AGENDA = "- PQ Consensus Layer working session"
CALL_TIME_UTC = time(14, 0)
CALL_TIME = f"{CALL_TIME_UTC:%H:%M} UTC"

# How long after a call's scheduled end we wait before opening the next issue.
# Creating the next issue retitles the shared Zoom meeting, and a Zoom recording
# keeps the topic it was made under, so this is margin for the recording of a
# call that ran over to be captured under its own name.
SETTLE_AFTER_CALL = timedelta(hours=1)

# How close to a call we will still bother opening its issue. The Zoom meeting
# and calendar event already exist (the series is recurring), so a late issue
# still earns its keep -- it is what creates the Discourse topic and the mapping
# entry the asset pipeline needs. But once the call is under way it is too late
# to be useful, and we should move on to the next one.
MIN_LEAD = timedelta(hours=1)

# A pending call further out than this is not a real schedule -- it is a typo in
# an issue title (a wrong year parses fine). Without a ceiling, one such issue
# makes every later run a silent no-op and the series simply stops. The real gap
# never exceeds four days (Fri -> Tue).
MAX_PENDING_LEAD = timedelta(days=14)

# The scan always starts from today, and no weekly pattern has a gap wider than
# a week, so a fortnight is slack. It bounds the loop so a bad weekday set
# raises instead of spinning.
MAX_SEARCH_DAYS = 14

# "PQ-CL Breakout #12, November 17, 2026"
TITLE_RE = re.compile(
    re.escape(DISPLAY_NAME) + r"\s+#(\d+),\s+(\w+\s+\d{1,2},?\s+\d{4})\s*$"
)
DATE_FORMATS = ["%B %d, %Y", "%B %d %Y", "%b %d, %Y", "%b %d %Y"]

# Issue numbers this run has actually created on GitHub. Recorded the instant
# the API confirms them, because the workflow must schedule them even if a later
# step of the same run raises -- an issue that exists but never reaches
# handle_protocol_call.py has no Zoom occurrence, calendar instance, Discourse
# topic or mapping entry, and nothing retries it.
CREATED = []


def api_call(endpoint, method="GET", payload=None):
    """Call the GitHub REST API."""
    url = f"https://api.github.com/repos/{REPO}/{endpoint}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode()
            return json.loads(body) if body.strip() else {}
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()[:200] if e.fp else str(e)
        print(f"  API error ({e.code}): {error_body}")
        return None
    except Exception as e:
        print(f"  API error: {e}")
        return None


def parse_title(title):
    """Return (call_number, date) for a PQ-CL title, or None if it isn't one."""
    match = TITLE_RE.search(title.strip())
    if not match:
        return None
    for fmt in DATE_FORMATS:
        try:
            return int(match.group(1)), datetime.strptime(match.group(2), fmt).date()
        except ValueError:
            continue
    return None


def fetch_existing():
    """Every PQ-CL issue as {number, call_number, date, title}.

    Open and closed issues alike: an issue's state says nothing about whether its
    call has happened (close_stale_meetings.py closes them a day late), so the
    whole record is what matters.

    Two ways this refuses to answer, both because an issue we cannot see is one
    we will duplicate:

      - Returns None if the listing could not be completed. Deliberately
        distinct from an empty result: without a trustworthy view of what
        exists, an empty-looking list reads as "the series has not started yet"
        and mints a duplicate #1.
      - Raises if an issue claims to be this series but its title cannot be
        parsed, rather than dropping it from the record.
    """
    found = []
    unparsed = []
    page = 1
    while True:
        result = api_call(
            f"issues?labels={','.join(LABELS)}&state=all&per_page=100&page={page}"
        )
        if result is None:
            print("  ERROR: could not list existing issues")
            return None
        issues = result if isinstance(result, list) else result.get("items", [])
        if not issues:
            break
        for issue in issues:
            title = issue.get("title", "")
            parsed = parse_title(title)
            if parsed:
                call_number, call_date = parsed
                found.append({
                    "number": issue.get("number"),
                    "call_number": call_number,
                    "date": call_date,
                    "title": title,
                })
            elif title.strip().startswith(DISPLAY_NAME):
                # Looks like one of ours but doesn't parse -- a renamed title
                # ("... (cancelled)"), or a hand-filed one with an odd date.
                # Dropping it silently is the worst option available: the issue
                # would vanish from the record, so a pending call would stop
                # blocking and the numbering would restart, and we would open a
                # second issue for a call that already has one.
                unparsed.append((issue.get("number"), title))
        if len(issues) < 100:
            break
        page += 1

    if unparsed:
        listed = "; ".join(f"#{n} {title!r}" for n, title in unparsed)
        raise RuntimeError(
            f"Cannot read the call date out of {len(unparsed)} {DISPLAY_NAME} "
            f"issue title(s): {listed}. Refusing to continue, because an issue "
            "this script cannot see is one it will duplicate. Restore the title "
            f"format '{DISPLAY_NAME} #N, Month D, YYYY'."
        )
    return found


def call_start(call_date):
    """The UTC start instant of the call on `call_date`."""
    return datetime.combine(call_date, CALL_TIME_UTC, tzinfo=timezone.utc)


def call_settled(call_date, now):
    """Has this call finished long enough ago to hand the Zoom series over?"""
    end = call_start(call_date) + timedelta(minutes=DURATION_MINUTES)
    return now >= end + SETTLE_AFTER_CALL


def next_call_date(weekdays, now, not_before=None):
    """The next scheduled weekday whose call is still at least MIN_LEAD away.

    The scan starts at today rather than at the last issue's date, so a series
    that has been stalled for a month resumes at the next upcoming call instead
    of trying to backfill every one it missed. `not_before` pushes the start of
    the scan past a date that already has an issue.
    """
    day = now.date() - timedelta(days=1)
    if not_before is not None and not_before > day:
        day = not_before

    for _ in range(MAX_SEARCH_DAYS):
        day += timedelta(days=1)
        if day.weekday() in weekdays and call_start(day) - now >= MIN_LEAD:
            return day
    raise RuntimeError(
        f"No schedulable call date within {MAX_SEARCH_DAYS} days of {day}"
    )


def build_issue_body(call_date):
    """Build the issue body matching the protocol-call-form template format."""
    datetime_str = f"{call_date.strftime('%B %-d, %Y')}, {CALL_TIME}"

    return f"""### UTC Date & Time

{datetime_str}

### Agenda

{AGENDA}

### Call Series

{DISPLAY_NAME}

### Autopilot Mode

- [x] Use autopilot (recommended defaults for this call series)


<details>
<summary>🔧 Meeting Configuration</summary>

### Duration

{DURATION}

### Occurrence Rate

{OCCURRENCE_RATE}

### Use Custom Meeting Link (Optional)

- [ ] I will provide my own meeting link

### Display Zoom Link in Calendar Invite (Optional)

- [x] Display Zoom link in invite

### YouTube Livestream Link (Optional)

- [ ] Create YouTube livestream link
</details>"""


def create_issue(call_number, call_date, dry_run=False):
    """Create a GitHub issue for one PQ-CL call."""
    title = f"{DISPLAY_NAME} #{call_number}, {call_date.strftime('%B %-d, %Y')}"
    body = build_issue_body(call_date)

    if dry_run:
        print(f"  [DRY RUN] Would create: {title}")
        print(f"            Labels: {','.join(LABELS)}")
        return None

    result_data = api_call(
        "issues", method="POST", payload={"title": title, "body": body, "labels": LABELS}
    )
    if not (result_data and result_data.get("number")):
        raise RuntimeError(f"Failed to create issue: {title}")

    issue_number = result_data["number"]
    CREATED.append(issue_number)
    print(f"  ✅ Created issue #{issue_number}: {title}")
    print(f"     {result_data.get('html_url', '')}")

    # The gate listing is filtered by these labels, so an issue created without
    # them is invisible to the next run -- which would see no pending call and
    # open another. Raising does NOT prevent that (the issue already exists and
    # still has no labels); what it does is make every such run go red instead
    # of quietly repeating. The number is already in CREATED, so this issue
    # still gets scheduled.
    applied = {lbl.get("name") for lbl in result_data.get("labels", [])}
    missing = [lbl for lbl in LABELS if lbl not in applied]
    if missing:
        raise RuntimeError(
            f"Issue #{issue_number} created without label(s) {missing}. "
            "The token lacks permission to apply labels; the next run would not "
            "see this issue and would create a duplicate."
        )

    return issue_number


def process(now, start_date=None, dry_run=False):
    """Create the next call's issue, if every call on record has finished."""
    CREATED.clear()

    weekdays = parse_multi_day_weekly(OCCURRENCE_RATE)
    if not weekdays:
        raise RuntimeError(f"Unsupported occurrence rate: {OCCURRENCE_RATE!r}")

    existing = fetch_existing()
    if existing is None:
        raise RuntimeError("Could not list existing issues; refusing to create duplicates")

    # Hold off while any call already on record is still to come, or has only
    # just finished. Creating the next issue retitles the shared Zoom meeting,
    # and until this call is done that title still has a job to do.
    pending = [i for i in existing if not call_settled(i["date"], now)]
    if pending:
        soonest = min(pending, key=lambda i: i["date"])
        print(f"  Pending: #{soonest['number']} {soonest['title']}")

        # A pending call blocks everything behind it, so one with an impossible
        # date stops the series for as long as that date is in the future, with
        # every run exiting 0. Put a ceiling on it.
        lead = call_start(soonest["date"]) - now
        if lead > MAX_PENDING_LEAD:
            raise RuntimeError(
                f"Issue #{soonest['number']} is for a call {lead.days} days away "
                f"({soonest['date'].isoformat()}), more than the "
                f"{MAX_PENDING_LEAD.days}-day ceiling. It blocks every later call, "
                "so this is almost certainly a wrong date in the title. No further "
                f"{DISPLAY_NAME} issues will be created until it is corrected."
            )

        print("  That call hasn't finished yet → nothing to do")
        return None

    # Belt and braces. The pending check above already implies every call on
    # record is in the past, but anchoring on them too makes it impossible for a
    # date that has an issue to be chosen again, however the dates were parsed.
    not_before = max((i["date"] for i in existing), default=None)
    if start_date and (not_before is None or start_date - timedelta(days=1) > not_before):
        not_before = start_date - timedelta(days=1)

    call_date = next_call_date(weekdays, now, not_before=not_before)
    call_number = max((i["call_number"] for i in existing), default=0) + 1

    print(f"  Next call: #{call_number} on {call_date.strftime('%B %-d, %Y')}")
    return create_issue(call_number, call_date, dry_run=dry_run)


def main():
    parser = argparse.ArgumentParser(description="Auto-create the next PQ-CL Breakout issue")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be created without creating")
    parser.add_argument("--start-date", type=date.fromisoformat,
                        help="Don't schedule anything before this ISO date (YYYY-MM-DD)")
    args = parser.parse_args()

    print(f"Auto-create {DISPLAY_NAME} issues for {REPO}")
    print(f"Time: {datetime.now(timezone.utc).isoformat()}")
    if args.dry_run:
        print("⚠️  DRY RUN MODE — no issues will be created")

    try:
        process(
            now=datetime.now(timezone.utc),
            start_date=args.start_date,
            dry_run=args.dry_run,
        )
    finally:
        # Hand any new issue number to the workflow so it can run ACDbot's
        # handler on it (no issues.opened event fires for GITHUB_TOKEN). This
        # runs even when process() raised: an issue that exists but is never
        # handled gets no Zoom occurrence, calendar instance, Discourse topic or
        # mapping entry, and nothing retries it.
        output_file = os.environ.get("GITHUB_OUTPUT")
        if output_file:
            with open(output_file, "a") as f:
                f.write(f"created_issues={','.join(str(n) for n in CREATED)}\n")

    print(f"\nDone. Created {len(CREATED)} issue(s).")


if __name__ == "__main__":
    main()
