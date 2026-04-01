# Calendar Link PR Notes

Date: 2026-04-01

## Findings

- The deployed protocol-call automation path is `.github/workflows/protocol-call-workflow.yml` -> `.github/ACDbot/scripts/handle_protocol_call.py`.
- No blocking regression was found in that automated path.
- The PR behavior matches intent:
  - `View` opens agenda view on the event day.
  - `Add to Calendar` creates a personal event from the occurrence data.
- The deployed path correctly respects `display_zoom_link_in_invite`.
- `meeting_topic_mapping.json` changes look safe:
  - changed `start_time` values were normalized to ISO
  - changed `calendar_event_id` values were normalized from pre-encoded `eid` payloads back to raw event IDs

## Verification

Passed locally:

- `uv run python .github/ACDbot/tests/unit/test_gcal_links.py`
- `uv run python .github/ACDbot/tests/unit/test_datetime_utils.py`
- `PYTHONPATH=.github/ACDbot uv run --with pyyaml --with google-auth --with google-api-python-client --with pytz python .github/ACDbot/tests/unit/test_protocol_call_handler.py`

Also checked:

- `.github/ACDbot/meeting_topic_mapping.json` parses cleanly
- current mapping data works with the new calendar comment builder

## Local Script

Script:

- `.github/ACDbot/scripts/generate_resource_comment.py`

What we found:

- It is not used anywhere in checked-in workflows, scripts, or imports.
- It may still be used manually by us, so we should confirm before deleting it.

Current gap:

- It does not perfectly match deployed behavior.
- The deployed path gets `display_zoom_link_in_invite` from issue form data.
- The local script does not parse the issue form, and that flag is not stored in `meeting_topic_mapping.json`.
- As written, the local script always includes `zoom_url` in the add-to-calendar payload when Zoom exists.

## Options

### If we are not using `generate_resource_comment.py`

- Delete it.
- Optionally remove stale comments in `handle_protocol_call.py` that refer to it.

### If we are using it, but exact parity is not required

- Make it read call-series defaults from `call_series_config.yml`.
- This is a small fix, but it still will not match issue-specific overrides exactly.

### If we are using it and want it to stay in sync

- Do not maintain a second implementation.
- Replace it with a dry-run mode in `handle_protocol_call.py`.
- The dry-run path should reuse the deployed logic and print the exact same comment without posting anything.

## Next Step

1. Confirm whether we use `generate_resource_comment.py` manually.
2. If not, delete it.
3. If yes and we want exact parity, make it a dry-run path of `handle_protocol_call.py`.
