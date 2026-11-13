# Adding a New Call Series

This document describes how to add a new recurring call series to ACDbot.

## Required Changes

Adding a new call series requires updating **4 files**:

### 1. Call Series Config

**File:** `.github/ACDbot/call_series_config.yml`

Add a new entry under `call_series:`:

```yaml
  yournewcall:
    display_name: "Your New Call"
    youtube_playlist_id: null        # or "PLJqWcTqh_zK..." if you have one
    discord_webhook_env: null        # or "DISCORD_WEBHOOK_ENV_VAR" if needed
    autopilot_defaults:              # Optional - see below
      duration: 60
      occurrence_rate: "bi-weekly"
      need_youtube_streams: false
      display_zoom_link_in_invite: true
      external_meeting_link: false
```

**Field reference:**
| Field | Description |
|-------|-------------|
| `yournewcall` | Internal key (lowercase, no spaces) |
| `display_name` | Shown in issue template dropdown (must match exactly) |
| `youtube_playlist_id` | YouTube playlist ID for uploaded recordings, or `null` |
| `discord_webhook_env` | Environment variable name for Discord notifications, or `null` |
| `autopilot_defaults` | Optional preset values when autopilot mode is enabled (see below) |

### 2. Issue Template Dropdown

**File:** `.github/ISSUE_TEMPLATE/protocol-call-form.yml`

Add the display name to the dropdown options (around line 35):

```yaml
    options:
      - "-- Please select a call series --"
      - All Core Devs - Consensus
      - All Core Devs - Execution
      # ... existing options ...
      - Your New Call              # <-- Add here (alphabetically)
      - One-time call
```

**Important:** The display name must exactly match `display_name` in `call_series_config.yml`.

### 3. Auto-labeling

**File:** `.github/labeler.yml`

Add a regex pattern so issues for this call series are automatically labeled:

```yaml
YourCallLabel:
 - "^(.*[Yy]our [Cc]all [Nn]ame.*)"
```

The pattern should match likely variations of how the call name appears in issue titles. Use case-insensitive character classes (e.g., `[Yy]our`) for flexibility.

### 4. Trusted Contributors

**File:** `.github/workflows/protocol-call-workflow.yml`

Add the facilitator's GitHub username to the `trustedContributors` array (around line 42):

```javascript
const trustedContributors = [
  "poojaranjan", "adietrichs", "carlbeek", // ... existing users
  "newfacilitator"  // <-- Add here
];
```

This allows the facilitator to create call agenda issues that ACDbot will process. Without this, the workflow will skip issues created by unrecognized users.

## What Happens Automatically

When the first issue for the new call series is created:

1. **Form parsing** - ACDbot reads the issue and maps the display name to the internal key
2. **Zoom meeting** - Created automatically (unless user opts out)
3. **Calendar event** - Added to the Ethereum Protocol Events calendar
4. **Discourse topic** - Created for meeting notes/discussion
5. **JSON mapping** - Entry auto-created in `meeting_topic_mapping.json`

You do **not** need to manually edit `meeting_topic_mapping.json`.

## Optional: YouTube Playlist

If you want recordings uploaded to a dedicated YouTube playlist:

1. Create a playlist on the [Ethereum Protocol YouTube channel](https://www.youtube.com/@EthereumProtocol)
2. Copy the playlist ID from the URL (starts with `PL`)
3. Add it to `youtube_playlist_id` in `call_series_config.yml`

If `youtube_playlist_id` is `null`, recordings will still be uploaded but won't be added to a playlist.

## Optional: Discord Notifications

To enable Discord notifications before meetings:

1. Create a webhook in the target Discord channel
2. Add the webhook URL as a GitHub Actions secret
3. Set `discord_webhook_env` to the secret name in `call_series_config.yml`

Currently only ACD calls (acde, acdc, acdt) have Discord notifications configured.

## Recommended: Autopilot Defaults

Autopilot mode allows users to create issues with minimal input - just select the call series and date/time, and all other settings are filled in automatically.

To configure autopilot defaults for your call series, add an `autopilot_defaults` section:

```yaml
  yourcall:
    display_name: "Your Call"
    youtube_playlist_id: null
    discord_webhook_env: null
    autopilot_defaults:
      duration: 60                      # Meeting length in minutes (30, 60, 90, 120, 180)
      occurrence_rate: "bi-weekly"      # Recurrence: weekly, bi-weekly, monthly, weekly:<days>, or other
      need_youtube_streams: false       # Create YouTube livestreams?
      display_zoom_link_in_invite: true # Show Zoom link in calendar invite?
      external_meeting_link: false      # Use external link instead of creating Zoom meeting?
```

**Autopilot field reference:**
| Field | Values | Description |
|-------|--------|-------------|
| `duration` | `30`, `60`, `90`, `120`, `180` | Meeting length in minutes |
| `occurrence_rate` | `weekly`, `bi-weekly`, `monthly`, `weekly:<days>`, `other` | Calendar recurrence pattern (see below) |
| `need_youtube_streams` | `true`, `false` | Whether to create YouTube livestreams |
| `display_zoom_link_in_invite` | `true`, `false` | Show Zoom link in calendar event description |
| `external_meeting_link` | `true`, `false` | Skip Zoom creation (use external meeting link) |

### Calls that meet several times a week

`weekly`, `bi-weekly` and `monthly` all assume one meeting per cycle, on the weekday
of the first occurrence. A series that meets on several weekdays of every week uses a
multi-day weekly rate instead — `weekly:` followed by a comma-separated day list:

```yaml
  pqcl:
    display_name: "PQ-CL Breakout"
    autopilot_defaults:
      duration: 120
      occurrence_rate: "weekly:tu,we,fr"   # every Tue, Wed and Fri
```

Days accept two-letter, three-letter or full names (`tu`, `tue`, `tuesday`) in any
order. An unrecognised day invalidates the whole rate rather than silently dropping
that day, and both backends then raise `Unsupported occurrence rate` — the run fails
instead of quietly creating a plain weekly meeting on the wrong schedule.

This stays a **single** recurring Zoom meeting and a **single** calendar series, so the
join URL is stable across all three days — Zoom expresses the day set as
`recurrence.weekly_days` and Google Calendar as `RRULE:FREQ=WEEKLY;BYDAY=TU,WE,FR`.

**Four things to know when using a multi-day rate:**

1. Any rate you put in the config must also exist as an option in the **Occurrence
   Rate** dropdown in `.github/ISSUE_TEMPLATE/protocol-call-form.yml` (the literal
   string, e.g. `"weekly:tu,we,fr"`). Without it, an issue filed with autopilot *off*
   would fall back to plain `weekly` and rebase the calendar series onto one day.
2. There is no bi-weekly equivalent — `weekly:` always means every week. A series
   meeting on multiple days every *other* week isn't supported yet.
3. The Zoom series anchor is deliberately **not** moved to each issue's date for a
   multi-day series (ordinary series still do move it). The three weekday issues
   share one Zoom series and are usually filed in advance, so marching the anchor
   forward would push it past that week's earlier occurrences and strand the
   occurrence ids already recorded against their issues.
4. **File one issue at a time — don't batch the week.** A Zoom meeting's topic
   is a *series-level* field: the weekdays cannot each carry their own, and
   ACDbot sets it from the issue title every time it handles an issue. Filing the
   week's issues together therefore leaves the live Zoom topic naming whichever
   was handled last, and a recording keeps the topic it was made under, so the
   earlier calls get recordings stamped with a later call's title. Opening each
   issue only after the previous call has finished gives a multi-day series the
   same guarantee a single-day series gets for free: the Zoom topic always names
   the call that is about to happen.

**Notes:**
- If `autopilot_defaults` is omitted, system defaults are used (60 min, bi-weekly, no streams)
- One-off calls don't support autopilot (users must specify all options)
- Set `external_meeting_link: true` for calls hosted elsewhere (e.g., StreamETH, Google Meet)

## Optional: Auto-creating the issues

A facilitator normally opens each call's issue by hand. For a series that meets
often enough to make that a chore, a scheduled workflow can open them instead.
Two exist today:

| Workflow | Series | Schedule | Releases the next issue when |
|---|---|---|---|
| `auto-create-acd-issues.yml` | ACDE, ACDC | Sat 09:00 UTC | the previous **issue** is closed |
| `auto-create-pqcl-issues.yml` | PQ-CL | 07:23 and 19:23 UTC daily | the previous **call** has finished |

Neither asks anything of the facilitator: issues are closed for them by
`close-stale-meetings.yml`, 24 hours after the meeting ends. That job only
inspects `occurrences[-3:]` per series, which is weeks of slack at one call a
fortnight but roughly 2.5 days at three calls a week — so if it is down for a
few days, a PQ-CL issue can slip out of the window and stay open for good.
Nothing breaks when that happens (no part of the schedule depends on closure),
but widening the slice would be cheap if stray open issues start to accumulate.

**Which release condition to copy depends on the cadence, and copying the wrong
one fails silently.** The ACD workflow gates on the previous issue being closed,
which works because its calls are a fortnight apart — far longer than the 24-hour
auto-close. A series meeting Tue/Wed/Fri has gaps of one to three days, so
Tuesday's issue is not auto-closed until Wednesday evening, after Wednesday's
call has already happened. A close-gated PQ-CL series produces Tue, Fri, Tue,
Fri… and **never schedules a Wednesday at all**. Gate on the call having finished
instead, and the facilitator's habits stop mattering entirely.

Six things any such workflow has to get right:

1. **No event fires.** Issues created with `GITHUB_TOKEN` are authored by
   `github-actions[bot]` and emit no `issues.opened`, so `protocol-call-workflow.yml`
   never runs. The workflow must invoke `handle_protocol_call.py` itself. This also
   means the `trustedContributors` gate doesn't apply to auto-created issues.
2. **Release on elapsed time, not on a human or on issue state** — unless the
   cadence is comfortably longer than the 24-hour auto-close. See above.
3. **Never pick a date that already has an issue.** The next call is chosen to be
   later than every call already on record — including one filed ahead of time —
   rather than simply "the next upcoming weekday".
4. **Fail if labels don't apply.** The gate listing is filtered by label, so an
   issue created without them is invisible to the next run — which would see a
   clear series and open another, every run, forever.
5. **Treat an unreadable record as fatal.** These scripts reconstruct what has
   already been filed from issue *titles*. A title that no longer matches the
   expected format must stop the run, not be skipped — skipping it drops the
   issue from the record, which clears the gate and restarts the numbering, and
   the next run opens a second issue for a call that already has one.
6. **Don't collide on the mapping commit.** Several of these workflows commit or
   read `meeting_topic_mapping.json`. Give a new one its own cron hours rather
   than racing an existing job's `git push`.

### What the PQ-CL facilitator actually has to do

Nothing. Each issue appears a day or more before its call, with Zoom, the
calendar event and a Discourse topic already wired up, and is normally closed
for them a day after by `close-stale-meetings.yml` (see the caveat above — a
stray issue occasionally stays open, which costs nothing). Two things are
*optional*:

- **Replace the placeholder agenda.** Issues are created with a generic
  `- PQ Consensus Layer working session`. Editing the issue fires `issues.edited`,
  which does go through `protocol-call-workflow.yml` — so the editor's GitHub
  handle must be in `trustedContributors` for the change to reach Discourse and
  the calendar.
- **Cancel a call** by closing its issue early. That stops nothing else; the next
  issue is still released once that call's slot has passed. Close it — don't
  rename it. The issue title is the only record of which calls have been filed,
  so a title that no longer matches `PQ-CL Breakout #N, Month D, YYYY` makes the
  run fail rather than risk opening a second issue for the same call.

## Verification

After merging your changes:

1. Create a test issue using the new call series
2. Verify the ACDbot workflow completes successfully (check GitHub Actions)
3. Confirm resources were created:
   - Zoom meeting link in issue comment
   - Calendar event on [Ethereum Protocol Events](https://calendar.google.com/calendar/embed?src=c_upaofong8mgrmrkegn7ic7hk5s%40group.calendar.google.com)
   - Discourse topic linked in issue

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| "Unknown call series" in logs | Display name mismatch | Ensure dropdown option exactly matches `display_name` in config |
| Workflow fails to parse issue | Missing config entry | Add entry to `call_series_config.yml` |
| No YouTube playlist assignment | Playlist ID not set | Add `youtube_playlist_id` to config (or leave as `null`) |
| Autopilot uses wrong defaults | Missing `autopilot_defaults` | Add `autopilot_defaults` section to your call series config |
| Autopilot ignored for one-off | One-off calls unsupported | One-off calls require manual configuration (by design) |
| Tests fail after changes | Config structure issue | Run `uv run --project .github/ACDbot pytest .github/ACDbot/tests` locally |
| Workflow doesn't process issue | Facilitator not trusted | Add GitHub username to `trustedContributors` in workflow |

## File Reference

| File | Purpose | Manual edit required? |
|------|---------|----------------------|
| `.github/ACDbot/call_series_config.yml` | Central config for all call series (incl. autopilot defaults) | **Yes** |
| `.github/ISSUE_TEMPLATE/protocol-call-form.yml` | Issue template dropdown | **Yes** |
| `.github/labeler.yml` | Auto-labeling regex patterns | **Yes** |
| `.github/workflows/protocol-call-workflow.yml` | Trusted contributors list | **Yes** |
| `.github/ACDbot/meeting_topic_mapping.json` | Runtime meeting data | No (auto-populated) |
| `.github/ACDbot/modules/form_parser.py` | Parses issue forms | No (reads from config) |
| `.github/ACDbot/modules/call_series_config.py` | Loads config and autopilot defaults | No (reads from YAML) |
| `.github/ACDbot/modules/youtube_utils.py` | YouTube integration | No (reads from config) |
| `.github/ACDbot/modules/discord_notify.py` | Discord notifications | No (reads from config) |
| `.github/workflows/auto-create-*-issues.yml` | Scheduled issue creation | Only if automating a series |
| `.github/scripts/auto-create-*.py` | The creation logic for those workflows | Only if automating a series |
