#!/usr/bin/env python3
"""
Retire a recurring call series.

Stopping a call series means two things must become true together:
  1. Google Calendar stops emitting future events for the series.
  2. The mapping on disk says the series is retired (no stale data implying
     it is still scheduled).

This script does both, in that order: it deletes the recurring Google Calendar
event, then records ``active: false`` and clears ``calendar_event_id`` in the
mapping. The calendar change happens first and is verified, so the mapping is
never updated to claim a retirement that did not take effect.

After retirement the scheduling guard in handle_protocol_call refuses to
recreate a calendar event for the series, so editing or reopening an old issue
cannot silently bring it back. To resume a series later, set its ``active``
field back to true and open an issue as normal.

Supports --dry-run for safe previewing.
"""

import argparse
import os
import sys

# Resolve paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ACDBOT_DIR = os.path.dirname(SCRIPT_DIR)

# scripts/ is not an installed package, so we need the path for cross-script imports
sys.path.insert(0, ACDBOT_DIR)

from modules.mapping_manager import MappingManager


def main():
    parser = argparse.ArgumentParser(description="Retire a recurring call series")
    parser.add_argument(
        "--series",
        required=True,
        help="Call series key to retire (e.g. 'glamsterdamrepricings')",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Log what would happen without deleting the event or writing the mapping",
    )
    args = parser.parse_args()

    series = args.series
    manager = MappingManager()

    entry = manager.get_call_series(series)
    if entry is None:
        print(f"[ERROR] Call series '{series}' not found in mapping")
        sys.exit(1)

    if not manager.is_series_active(series):
        print(f"[INFO] Call series '{series}' is already retired; nothing to do")
        return

    calendar_event_id = manager.get_series_calendar_event_id(series)

    if args.dry_run:
        print(
            f"[DRY-RUN] Would delete calendar event "
            f"{calendar_event_id or '(none)'} and mark '{series}' active=false"
        )
        return

    # Step 1: end the live calendar event first. Only proceed to record the
    # retirement if this succeeds, so the mapping never lies about reality.
    if calendar_event_id:
        calendar_id = os.environ.get("GCAL_ID")
        if not calendar_id:
            print("[ERROR] GCAL_ID environment variable not set")
            sys.exit(1)

        from modules.gcal import delete_recurring_event

        delete_recurring_event(event_id=calendar_event_id, calendar_id=calendar_id)
        print(f"[INFO] Deleted recurring calendar event {calendar_event_id}")
    else:
        print(f"[INFO] Series '{series}' has no calendar_event_id; skipping calendar deletion")

    # Step 2: record reality on disk.
    manager.retire_series(series)
    if not manager.save_mapping():
        print("[ERROR] Failed to save mapping after retiring series")
        sys.exit(1)

    print(f"[INFO] Retired call series '{series}' (active=false, calendar_event_id cleared)")


if __name__ == "__main__":
    main()
