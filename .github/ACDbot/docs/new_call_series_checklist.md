# Adding a New Call Series

This document describes how to add a new recurring call series to ACDbot.

## Required Changes

Adding a new call series requires updating **3 files**:

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
      occurrence_rate: "bi-weekly"      # Recurrence: weekly, bi-weekly, monthly, or other
      need_youtube_streams: false       # Create YouTube livestreams?
      display_zoom_link_in_invite: true # Show Zoom link in calendar invite?
      external_meeting_link: false      # Use external link instead of creating Zoom meeting?
```

**Autopilot field reference:**
| Field | Values | Description |
|-------|--------|-------------|
| `duration` | `30`, `60`, `90`, `120`, `180` | Meeting length in minutes |
| `occurrence_rate` | `weekly`, `bi-weekly`, `monthly`, `other` | Calendar recurrence pattern |
| `need_youtube_streams` | `true`, `false` | Whether to create YouTube livestreams |
| `display_zoom_link_in_invite` | `true`, `false` | Show Zoom link in calendar event description |
| `external_meeting_link` | `true`, `false` | Skip Zoom creation (use external meeting link) |

**Notes:**
- If `autopilot_defaults` is omitted, system defaults are used (60 min, bi-weekly, no streams)
- One-off calls don't support autopilot (users must specify all options)
- Set `external_meeting_link: true` for calls hosted elsewhere (e.g., StreamETH, Google Meet)

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
| Tests fail after changes | Config structure issue | Run `pytest .github/ACDbot/tests` locally |

## File Reference

| File | Purpose | Manual edit required? |
|------|---------|----------------------|
| `.github/ACDbot/call_series_config.yml` | Central config for all call series (incl. autopilot defaults) | **Yes** |
| `.github/ISSUE_TEMPLATE/protocol-call-form.yml` | Issue template dropdown | **Yes** |
| `.github/labeler.yml` | Auto-labeling regex patterns | **Yes** |
| `.github/ACDbot/meeting_topic_mapping.json` | Runtime meeting data | No (auto-populated) |
| `.github/ACDbot/modules/form_parser.py` | Parses issue forms | No (reads from config) |
| `.github/ACDbot/modules/call_series_config.py` | Loads config and autopilot defaults | No (reads from YAML) |
| `.github/ACDbot/modules/youtube_utils.py` | YouTube integration | No (reads from config) |
| `.github/ACDbot/modules/discord_notify.py` | Discord notifications | No (reads from config) |
