#!/usr/bin/env python3
"""
Unit tests for .github/scripts/auto-create-pqcl-issue.py.

The script opens real GitHub issues on a schedule with nobody watching, so the
behaviour that matters most is what it does unattended: over a whole week, after
a missed run, when the API fails. Every API call is stubbed here -- nothing in
this file talks to GitHub.

Two properties are load-bearing:

1. NO HUMAN ACTION IS REQUIRED. The next issue is released by the previous CALL
   finishing, never by its ISSUE being closed. Issues here are closed
   automatically by close_stale_meetings.py a full day after the meeting, which
   is slower than this series' own Tue/Wed/Fri cadence -- a close-gated series
   would skip every Wednesday forever. _FakeGitHub therefore reports every issue
   as "open" so that reintroducing a close gate turns these tests red.

2. AT MOST ONE CALL IS EVER PENDING. The three weekdays share one recurring Zoom
   meeting whose topic is a series-level field set from the issue title, so an
   issue opened early would retitle the meeting out from under a call that
   hasn't happened yet.

3. THE RECORD IS READ FROM TITLES, OR NOT AT ALL. Both properties above are
   derived from the list of existing issue titles, so a title the script cannot
   parse has to stop the run rather than be skipped -- skipping it clears the
   gate and restarts the numbering. See TestBrokenRecord.
"""

import importlib.util
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = REPO_ROOT / ".github" / "scripts" / "auto-create-pqcl-issue.py"
CONFIG_PATH = REPO_ROOT / ".github" / "ACDbot" / "call_series_config.yml"

WEEKDAYS = [1, 2, 4]  # Tue, Wed, Fri


def _load_script():
    """Import the hyphenated script file as a module.

    Bytecode writing is suppressed for the duration: .github/scripts/ is not
    covered by a __pycache__ ignore rule, so importing here would otherwise drop
    an untracked .pyc into the working tree on every test run.
    """
    original = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec = importlib.util.spec_from_file_location("auto_create_pqcl", SCRIPT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.dont_write_bytecode = original


@pytest.fixture(scope="module")
def script():
    return _load_script()


def utc(y, m, d, hh=9, mm=0):
    return datetime(y, m, d, hh, mm, tzinfo=timezone.utc)


class _FakeGitHub:
    """Stands in for the GitHub issues API.

    Every issue is reported as state "open", because nobody closes these by hand
    and close_stale_meetings.py is a day behind. If the script ever starts
    gating on state again, the series stops advancing and the timeline tests
    below fail.
    """

    def __init__(self, script, titles=()):
        self.script = script
        self.titles = list(titles)
        self.created = []
        self._next_number = 5000

    def api_call(self, endpoint, method="GET", payload=None):
        if method == "POST":
            self._next_number += 1
            self.created.append(payload["title"])
            self.titles.append(payload["title"])
            return {
                "number": self._next_number,
                "html_url": f"https://github.com/x/y/issues/{self._next_number}",
                "labels": [{"name": lbl} for lbl in payload["labels"]],
            }
        # Match on "&page=", not "page=", because the endpoint also carries
        # "per_page=100" -- whose tail is literally "page=1". Getting this wrong
        # makes every page return page 1, so pagination is never exercised and a
        # fixture of 100+ issues loops forever.
        match = re.search(r"&page=(\d+)", endpoint)
        if not match:
            return []
        page = int(match.group(1))
        start = (page - 1) * 100
        return [{"number": 900 + i, "title": title, "state": "open"}
                for i, title in enumerate(self.titles[start:start + 100], start=start)]

    def run(self, now, **kwargs):
        with patch.object(self.script, "api_call", side_effect=self.api_call):
            return self.script.process(now=now, **kwargs)


class TestConfigAgreement:
    """The script hardcodes what call_series_config.yml declares; pin them together.

    A silent drift here is the nastiest failure available: issues would keep being
    created, just on the wrong days or with a rate the handler no longer accepts.
    """

    @pytest.fixture(scope="class")
    def pqcl_config(self):
        config = yaml.safe_load(CONFIG_PATH.read_text())
        return config["call_series"]["pqcl"]

    def test_display_name_matches(self, script, pqcl_config):
        assert script.DISPLAY_NAME == pqcl_config["display_name"]

    def test_occurrence_rate_matches(self, script, pqcl_config):
        assert script.OCCURRENCE_RATE == pqcl_config["autopilot_defaults"]["occurrence_rate"]

    def test_duration_matches(self, script, pqcl_config):
        """DURATION_MINUTES also decides when a call counts as finished, which is
        what releases the next issue, so it has to be the real meeting length."""
        assert script.DURATION_MINUTES == pqcl_config["autopilot_defaults"]["duration"]
        assert script.DURATION == f"{pqcl_config['autopilot_defaults']['duration']} minutes"

    def test_series_key_exists_in_config(self, script):
        config = yaml.safe_load(CONFIG_PATH.read_text())
        assert script.SERIES_KEY in config["call_series"]

    def test_occurrence_rate_is_a_dropdown_option(self, script):
        """An autopilot-off issue picking a rate the form doesn't offer can't happen,
        but the rate the script writes into the body must still be selectable."""
        form = yaml.safe_load(
            (REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "protocol-call-form.yml").read_text()
        )
        options = next(
            b["attributes"]["options"] for b in form["body"] if b.get("id") == "occurrence-rate"
        )
        assert script.OCCURRENCE_RATE in options

    def test_display_name_is_a_call_series_option(self, script):
        form = yaml.safe_load(
            (REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "protocol-call-form.yml").read_text()
        )
        options = next(
            b["attributes"]["options"] for b in form["body"] if b.get("id") == "call-series"
        )
        assert script.DISPLAY_NAME in options

    def test_cron_hours_can_see_a_settled_call(self, script):
        """The workflow's cron hours have to fall after a call settles, or the
        next issue is never released. Pins the schedule to the constants."""
        workflow = yaml.safe_load(
            (REPO_ROOT / ".github" / "workflows" / "auto-create-pqcl-issues.yml").read_text()
        )
        crons = [c["cron"] for c in workflow[True]["schedule"]]
        hours = {int(h) for c in crons for h in c.split()[1].split(",")}

        settled = script.call_start(date(2026, 11, 17)) \
            + timedelta(minutes=script.DURATION_MINUTES) + script.SETTLE_AFTER_CALL
        assert any(h >= settled.hour for h in hours), (
            f"no cron hour in {sorted(hours)} runs after a call settles at {settled:%H:%M}"
        )


class TestCallSettled:
    """When the Zoom series may be handed over to the next call."""

    CALL = date(2026, 11, 17)  # Tuesday, 14:00-16:00 UTC

    def test_not_settled_before_the_call(self, script):
        assert not script.call_settled(self.CALL, utc(2026, 11, 17, 9))

    def test_not_settled_during_the_call(self, script):
        assert not script.call_settled(self.CALL, utc(2026, 11, 17, 15))

    def test_not_settled_immediately_after(self, script):
        """Margin for a call that ran over, and for its recording to be captured
        under its own title before the Zoom topic moves on."""
        assert not script.call_settled(self.CALL, utc(2026, 11, 17, 16, 30))

    def test_settled_once_the_margin_has_passed(self, script):
        assert script.call_settled(self.CALL, utc(2026, 11, 17, 17, 1))

    def test_settled_long_after(self, script):
        assert script.call_settled(self.CALL, utc(2026, 11, 20))


class TestNextCallDate:
    """Which single date a run targets."""

    def test_picks_the_next_scheduled_weekday(self, script):
        assert script.next_call_date(WEEKDAYS, utc(2026, 11, 14)) == date(2026, 11, 17)

    def test_today_counts_while_the_call_is_still_ahead(self, script):
        """A run the morning of a call must still get it an issue -- that issue
        is what creates the call's Discourse topic and mapping entry, and there
        are eight hours left to do it in."""
        assert script.next_call_date(WEEKDAYS, utc(2026, 11, 18, 6)) == date(2026, 11, 18)

    def test_today_is_dropped_once_the_call_has_started(self, script):
        assert script.next_call_date(WEEKDAYS, utc(2026, 11, 18, 14, 30)) == date(2026, 11, 20)

    def test_today_is_dropped_inside_the_lead_margin(self, script):
        """Half an hour before the call is too late to be worth scheduling."""
        assert script.next_call_date(WEEKDAYS, utc(2026, 11, 18, 13, 30)) == date(2026, 11, 20)

    def test_not_before_pushes_past_a_date_that_has_an_issue(self, script):
        assert script.next_call_date(
            WEEKDAYS, utc(2026, 11, 17, 18), not_before=date(2026, 11, 17)
        ) == date(2026, 11, 18)

    def test_a_stalled_series_resumes_rather_than_backfilling(self, script):
        """After a month-long gap the next call is the next one, not the first of
        the forty that were missed."""
        assert script.next_call_date(
            WEEKDAYS, utc(2026, 11, 14), not_before=date(2026, 10, 1)
        ) == date(2026, 11, 17)

    def test_result_always_lands_on_a_scheduled_weekday(self, script):
        """An off-pattern DTSTART against BYDAY=TU,WE,FR is not something the
        calendar backends agree on, so every issue must land on one."""
        for offset in range(14):
            now = utc(2026, 11, 14) + timedelta(days=offset)
            assert script.next_call_date(WEEKDAYS, now).weekday() in WEEKDAYS


class TestTitleParsing:
    """Titles carry the call date and number, so parsing them is load-bearing."""

    def test_round_trips_a_generated_title(self, script):
        call_date = date(2026, 11, 17)
        title = f"{script.DISPLAY_NAME} #7, {call_date.strftime('%B %-d, %Y')}"
        assert script.parse_title(title) == (7, call_date)

    def test_single_digit_day_without_padding(self, script):
        assert script.parse_title("PQ-CL Breakout #3, November 3, 2026") == (3, date(2026, 11, 3))

    def test_abbreviated_month(self, script):
        assert script.parse_title("PQ-CL Breakout #3, Nov 3, 2026") == (3, date(2026, 11, 3))

    @pytest.mark.parametrize("title", [
        "Post-Quantum (PQ) Interop #49, July 29, 2026",
        "Post Quantum transaction signature (PQTS) Breakout #18",
        "PQ-CL Breakout retrospective",
        "",
    ])
    def test_rejects_other_series_and_malformed_titles(self, script, title):
        """The PostQuantum label is shared with PQ Interop and PQTS."""
        assert script.parse_title(title) is None


class TestUnattendedTimeline:
    """The headline property: left completely alone, the series keeps going."""

    def _crons(self, script, start, days, titles=()):
        """Run the real cron hours over `days`, with nobody touching anything."""
        gh = _FakeGitHub(script, titles)
        for offset in range(days):
            for hour in (7, 19):
                gh.run(start + timedelta(days=offset, hours=hour))
        return gh

    def test_a_fortnight_with_no_human_action(self, script):
        """Every call gets exactly one issue, in order, and Wednesday is never
        skipped -- which is what a close-gated design would do, because these
        issues are not closed until a day after the call."""
        gh = self._crons(script, utc(2026, 11, 14, 0), days=14)
        assert gh.created == [
            "PQ-CL Breakout #1, November 17, 2026",
            "PQ-CL Breakout #2, November 18, 2026",
            "PQ-CL Breakout #3, November 20, 2026",
            "PQ-CL Breakout #4, November 24, 2026",
            "PQ-CL Breakout #5, November 25, 2026",
            "PQ-CL Breakout #6, November 27, 2026",
            "PQ-CL Breakout #7, December 1, 2026",
        ]

    def test_every_issue_arrives_before_its_call(self, script):
        """An issue created after its own call would be useless."""
        gh = _FakeGitHub(script)
        for offset in range(14):
            for hour in (7, 19):
                now = utc(2026, 11, 14, 0) + timedelta(days=offset, hours=hour)
                before = len(gh.created)
                gh.run(now)
                if len(gh.created) > before:
                    created_for = script.parse_title(gh.created[-1])[1]
                    assert script.call_start(created_for) - now >= script.MIN_LEAD

    def test_never_two_pending_calls_at_once(self, script):
        """Checked after every run: at most one call is still to come, so the
        shared Zoom topic always names the call that is about to happen."""
        gh = _FakeGitHub(script)
        for offset in range(14):
            for hour in (7, 19):
                now = utc(2026, 11, 14, 0) + timedelta(days=offset, hours=hour)
                gh.run(now)
                pending = [t for t in gh.titles
                           if not script.call_settled(script.parse_title(t)[1], now)]
                assert len(pending) <= 1, f"{len(pending)} pending at {now}: {pending}"

    def test_a_missed_run_is_recovered_by_the_next(self, script):
        """Only the 07:00 run happens -- an outage, or a skipped GitHub cron."""
        gh = _FakeGitHub(script)
        for offset in range(10):
            gh.run(utc(2026, 11, 14, 7) + timedelta(days=offset))
        assert gh.created[:3] == [
            "PQ-CL Breakout #1, November 17, 2026",
            "PQ-CL Breakout #2, November 18, 2026",
            "PQ-CL Breakout #3, November 20, 2026",
        ]

    def test_a_week_long_outage_resumes_without_backfilling(self, script):
        gh = _FakeGitHub(script, ["PQ-CL Breakout #40, November 3, 2026"])
        gh.run(utc(2026, 11, 14, 19))
        assert gh.created == ["PQ-CL Breakout #41, November 17, 2026"]


class TestPendingGate:
    """Nothing is created while a call is still to come."""

    TUESDAY = "PQ-CL Breakout #1, November 17, 2026"

    def test_a_future_call_blocks(self, script):
        gh = _FakeGitHub(script, [self.TUESDAY])
        assert gh.run(utc(2026, 11, 16, 19)) is None
        assert gh.created == []

    def test_a_call_in_progress_blocks(self, script):
        gh = _FakeGitHub(script, [self.TUESDAY])
        assert gh.run(utc(2026, 11, 17, 15)) is None
        assert gh.created == []

    def test_a_just_finished_call_blocks(self, script):
        """The settle margin protects the recording's title."""
        gh = _FakeGitHub(script, [self.TUESDAY])
        assert gh.run(utc(2026, 11, 17, 16, 30)) is None
        assert gh.created == []

    def test_a_settled_call_releases_the_next(self, script):
        gh = _FakeGitHub(script, [self.TUESDAY])
        gh.run(utc(2026, 11, 17, 19))
        assert gh.created == ["PQ-CL Breakout #2, November 18, 2026"]

    def test_an_issue_filed_far_ahead_blocks_everything(self, script):
        """A hand-filed issue for next Friday is still a pending call."""
        gh = _FakeGitHub(script, ["PQ-CL Breakout #1, November 27, 2026"])
        assert gh.run(utc(2026, 11, 18, 19)) is None
        assert gh.created == []

    def test_a_pending_call_beyond_the_ceiling_fails_the_run(self, script):
        """A wrong year in a title parses fine and then blocks every later call
        for a year, with each run exiting 0. Put a stop to it."""
        gh = _FakeGitHub(script, ["PQ-CL Breakout #1, November 17, 2027"])
        with pytest.raises(RuntimeError, match="ceiling"):
            gh.run(utc(2026, 11, 14, 19))
        assert gh.created == []

    def test_a_normal_gap_is_well_inside_the_ceiling(self, script):
        """Friday -> Tuesday is the widest real gap; it must not trip the guard."""
        gh = _FakeGitHub(script, ["PQ-CL Breakout #1, November 24, 2026"])
        assert gh.run(utc(2026, 11, 20, 19)) is None

    def test_only_one_issue_per_run(self, script):
        gh = _FakeGitHub(script, ["PQ-CL Breakout #40, October 2, 2026"])
        gh.run(utc(2026, 11, 14, 19))
        assert len(gh.created) == 1


class TestBrokenRecord:
    """An issue the script cannot read is one it will duplicate."""

    def test_a_renamed_pending_issue_does_not_become_a_duplicate(self, script):
        """The concrete hazard: someone appends "(cancelled)" to the open issue.
        Silently dropping it would clear the pending gate AND reset numbering,
        opening a second issue for a call that already has one -- retitling the
        shared Zoom meeting before that call happens."""
        gh = _FakeGitHub(script, ["PQ-CL Breakout #5, November 20, 2026 (cancelled)"])
        with pytest.raises(RuntimeError, match="Cannot read the call date"):
            gh.run(utc(2026, 11, 18, 19))
        assert gh.created == []

    def test_an_unparseable_date_stops_the_run(self, script):
        gh = _FakeGitHub(script, ["PQ-CL Breakout #5, Sept 20, 2026"])
        with pytest.raises(RuntimeError, match="Cannot read the call date"):
            gh.run(utc(2026, 11, 14, 19))

    def test_the_error_names_the_offending_issues(self, script):
        gh = _FakeGitHub(script, ["PQ-CL Breakout #5, November 20, 2026 (cancelled)"])
        with pytest.raises(RuntimeError) as exc:
            gh.run(utc(2026, 11, 18, 19))
        assert "(cancelled)" in str(exc.value)

    def test_other_series_titles_are_not_mistaken_for_broken_ones(self, script):
        """Only titles claiming to be this series are held to the format."""
        gh = _FakeGitHub(script, [
            "Post-Quantum (PQ) Interop #49, July 29, 2026",
            "Post Quantum transaction signature (PQTS) Breakout #18",
        ])
        gh.run(utc(2026, 11, 14, 19))
        assert gh.created == ["PQ-CL Breakout #1, November 17, 2026"]

    def test_pagination_reads_every_page(self, script):
        """fetch_existing pages at 100; the record must span all of them or the
        highest call number is wrong and old calls look unfiled."""
        titles = [f"PQ-CL Breakout #{n}, November 3, 2026" for n in range(1, 151)]
        gh = _FakeGitHub(script, titles)
        gh.run(utc(2026, 11, 14, 19))
        assert gh.created == ["PQ-CL Breakout #151, November 17, 2026"]


class TestNumbering:
    def test_continues_from_the_highest_existing(self, script):
        gh = _FakeGitHub(script, ["PQ-CL Breakout #41, November 10, 2026"])
        gh.run(utc(2026, 11, 14, 19))
        assert gh.created == ["PQ-CL Breakout #42, November 17, 2026"]

    def test_other_pq_series_neither_number_nor_block(self, script):
        """The shared PostQuantum label pulls in PQ Interop and PQTS issues."""
        gh = _FakeGitHub(script, [
            "Post-Quantum (PQ) Interop #49, July 29, 2026",
            "Post Quantum transaction signature (PQTS) Breakout #18",
        ])
        gh.run(utc(2026, 11, 14, 19))
        assert gh.created == ["PQ-CL Breakout #1, November 17, 2026"]


class TestFailureModes:
    def test_listing_failure_creates_nothing(self, script):
        """An empty-looking list would read as 'the series hasn't started' and
        mint a duplicate #1, so a transient API error must stop the run."""
        with patch.object(script, "api_call", return_value=None):
            with pytest.raises(RuntimeError, match="refusing to create duplicates"):
                script.process(now=utc(2026, 11, 14, 19))

    def test_missing_labels_raise_rather_than_duplicate(self, script):
        """Without its labels the new issue is invisible to the gate listing, so
        the next run would see a clear series and open another."""
        def fake_api_call(endpoint, method="GET", payload=None):
            if method == "POST":
                return {"number": 1, "html_url": "", "labels": []}
            return []

        with patch.object(script, "api_call", side_effect=fake_api_call):
            with pytest.raises(RuntimeError, match="without label"):
                script.process(now=utc(2026, 11, 14, 19))

    def test_an_issue_that_exists_is_reported_even_when_the_run_fails(self, script):
        """main() writes CREATED to GITHUB_OUTPUT in a finally. An issue that
        exists but never reaches handle_protocol_call.py has no Zoom occurrence,
        calendar instance, Discourse topic or mapping entry, and nothing retries
        it -- so it must be handed to the workflow even on a failed run."""
        def fake_api_call(endpoint, method="GET", payload=None):
            if method == "POST":
                return {"number": 4242, "html_url": "", "labels": []}
            return []

        with patch.object(script, "api_call", side_effect=fake_api_call):
            with pytest.raises(RuntimeError):
                script.process(now=utc(2026, 11, 14, 19))
        assert script.CREATED == [4242]

    def test_created_is_reset_between_runs(self, script):
        """It is per-run state; a stale number would re-handle an old issue."""
        gh = _FakeGitHub(script)
        gh.run(utc(2026, 11, 14, 19))
        assert len(script.CREATED) == 1
        gh.run(utc(2026, 11, 15, 19))          # pending now -> creates nothing
        assert script.CREATED == []

    def test_dry_run_creates_nothing(self, script):
        gh = _FakeGitHub(script)
        assert gh.run(utc(2026, 11, 14, 19), dry_run=True) is None
        assert gh.created == []


class TestStartDate:
    def test_defers_the_series(self, script):
        gh = _FakeGitHub(script)
        gh.run(utc(2026, 11, 14, 19), start_date=date(2026, 11, 19))
        assert gh.created == ["PQ-CL Breakout #1, November 20, 2026"]

    def test_a_past_start_date_changes_nothing(self, script):
        gh = _FakeGitHub(script)
        gh.run(utc(2026, 11, 14, 19), start_date=date(2026, 1, 1))
        assert gh.created == ["PQ-CL Breakout #1, November 17, 2026"]

    def test_does_not_undo_the_duplicate_guard(self, script):
        """A start date earlier than an existing issue must not reopen that call."""
        gh = _FakeGitHub(script, ["PQ-CL Breakout #1, November 17, 2026"])
        gh.run(utc(2026, 11, 17, 19), start_date=date(2026, 1, 1))
        assert gh.created == ["PQ-CL Breakout #2, November 18, 2026"]


class TestIssueBody:
    """The body has to parse back out through ACDbot's form parser."""

    def test_body_round_trips_through_the_form_parser(self, script):
        from modules.form_parser import FormParser

        body = script.build_issue_body(date(2026, 11, 17))
        parser = FormParser()

        assert parser.parse_call_series(body) == script.SERIES_KEY
        assert parser.parse_occurrence_rate(body) == script.OCCURRENCE_RATE
        assert parser.parse_duration(body) == 120

    def test_datetime_is_parseable(self, script):
        from modules.datetime_utils import parse_datetime_string
        from modules.form_parser import FormParser

        body = script.build_issue_body(date(2026, 11, 17))
        parsed = parse_datetime_string(FormParser().parse_date_time(body))
        assert parsed.date() == date(2026, 11, 17)
        assert (parsed.hour, parsed.minute) == (14, 0)

    def test_autopilot_is_enabled(self, script):
        """Autopilot is what applies the 120-minute, Tue/Wed/Fri defaults."""
        from modules.form_parser import FormParser

        body = script.build_issue_body(date(2026, 11, 17))
        assert FormParser().parse_autopilot_mode(body) is True

    def test_agenda_is_the_generic_placeholder(self, script):
        body = script.build_issue_body(date(2026, 11, 17))
        assert "PQ Consensus Layer working session" in body

    def test_body_title_and_call_time_agree(self, script):
        """The title's date and the body's datetime must name the same call."""
        body = script.build_issue_body(date(2026, 11, 17))
        assert f"November 17, 2026, {script.CALL_TIME}" in body
