#!/usr/bin/env python3
"""
Retire a recurring call series: end its Google Calendar recurrence and mark it
inactive in the mapping.

The calendar recurrence is ended first (UNTIL=now, preserving past events) and
only then is the mapping updated, so the mapping never claims a retirement that
did not take effect. Set the series' "active" field back to true to resume.

Supports --dry-run.
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
        help="Log what would happen without ending the event or writing the mapping",
    )
    args = parser.parse_args()

    series = args.series
    manager = MappingManager()

    if series not in manager.mapping:
        print(f"[ERROR] Call series '{series}' not found in mapping")
        sys.exit(1)

    if not manager.is_series_active(series):
        print(f"[INFO] Call series '{series}' is already retired; nothing to do")
        return

    calendar_event_id = manager.get_series_calendar_event_id(series)

    if args.dry_run:
        print(
            f"[DRY-RUN] Would end calendar event "
            f"{calendar_event_id or '(none)'} and mark '{series}' active=false"
        )
        return

    # End the calendar recurrence first; only record the retirement if it succeeds.
    if calendar_event_id:
        calendar_id = os.environ.get("GCAL_ID")
        if not calendar_id:
            print("[ERROR] GCAL_ID environment variable not set")
            sys.exit(1)

        from modules.gcal import end_recurring_event

        end_recurring_event(event_id=calendar_event_id, calendar_id=calendar_id)
        print(f"[INFO] Ended recurring calendar event {calendar_event_id}")
    else:
        print(f"[INFO] Series '{series}' has no calendar_event_id; skipping calendar update")

    manager.retire_series(series)
    if not manager.save_mapping():
        print("[ERROR] Failed to save mapping after retiring series")
        sys.exit(1)

    print(f"[INFO] Retired call series '{series}' (active=false)")


if __name__ == "__main__":
    main()
