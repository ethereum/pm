#!/usr/bin/env python3
"""
Cancel Google Calendar instances for meetings with no corresponding GitHub issue.

Recurring call series have Google Calendar events that repeat on a schedule.
When no GitHub issue is created for an upcoming meeting, the calendar invite
still appears, confusing participants. This script deletes the specific
Google Calendar instance when no issue exists within 24 hours of the meeting.

Supports --dry-run flag for safe previewing.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Resolve paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ACDBOT_DIR = os.path.dirname(SCRIPT_DIR)

# Add ACDbot dir to path so we can import modules
sys.path.insert(0, ACDBOT_DIR)

from modules.call_series_config import get_call_series_config
from scripts.upcoming_calls import find_expected_missing_calls

CANCELLATION_WINDOW_HOURS = 24
MAPPING_FILE = Path(ACDBOT_DIR) / "meeting_topic_mapping.json"


def load_mapping() -> dict:
    """Load the meeting topic mapping file."""
    try:
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[ERROR] Failed to load mapping file: {e}")
        return {}


def find_cancellable_meetings(mapping):
    """Find meetings that should have their calendar instances cancelled.

    Uses find_expected_missing_calls() to detect recurring series where a
    meeting is expected but no occurrence (GitHub issue) exists, then filters
    to only those within 24 hours of now.

    Returns a list of dicts with keys:
        series_key, display_name, expected_time, occurrence_rate, calendar_event_id
    """
    missing = find_expected_missing_calls(mapping, days_ahead=7)
    now = datetime.now(timezone.utc)
    window = now + timedelta(hours=CANCELLATION_WINDOW_HOURS)

    cancellable = []
    for entry in missing:
        expected_time = entry["expected_time"]
        if expected_time > window:
            continue

        series_key = entry["series_key"]
        series_data = mapping.get(series_key, {})
        calendar_event_id = series_data.get("calendar_event_id")

        cancellable.append({
            "series_key": series_key,
            "display_name": entry["display_name"],
            "expected_time": expected_time,
            "occurrence_rate": entry["occurrence_rate"],
            "calendar_event_id": calendar_event_id,
        })

    return cancellable


def main():
    parser = argparse.ArgumentParser(
        description="Cancel Google Calendar instances for unmapped meetings"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Log what would be cancelled without making API calls",
    )
    args = parser.parse_args()

    calendar_id = os.environ.get("GCAL_ID", "")
    if not calendar_id and not args.dry_run:
        print("[ERROR] GCAL_ID environment variable not set")
        sys.exit(1)

    mapping = load_mapping()
    if not mapping:
        print("[INFO] No meetings found in mapping file")
        return

    cancellable = find_cancellable_meetings(mapping)
    if not cancellable:
        print("[INFO] No meetings to cancel")
        return

    print(f"[INFO] Found {len(cancellable)} meeting(s) to cancel")

    cancelled_count = 0
    skipped_count = 0

    for meeting in cancellable:
        series_key = meeting["series_key"]
        display_name = meeting["display_name"]
        expected_date = meeting["expected_time"].date()
        calendar_event_id = meeting["calendar_event_id"]

        if not calendar_event_id:
            print(f"[WARN] {display_name} ({series_key}): no calendar_event_id, skipping")
            skipped_count += 1
            continue

        if args.dry_run:
            print(
                f"[DRY-RUN] Would cancel {display_name} ({series_key}) "
                f"on {expected_date} (event: {calendar_event_id})"
            )
            cancelled_count += 1
            continue

        try:
            from modules.gcal import delete_calendar_instance

            deleted = delete_calendar_instance(
                event_id=calendar_event_id,
                target_date=expected_date,
                calendar_id=calendar_id,
            )
            if deleted:
                print(f"[INFO] Cancelled {display_name} ({series_key}) on {expected_date}")
                cancelled_count += 1
            else:
                print(
                    f"[WARN] {display_name} ({series_key}): "
                    f"no calendar instance found for {expected_date}"
                )
                skipped_count += 1
        except Exception as e:
            print(f"[ERROR] {display_name} ({series_key}): {e}")
            skipped_count += 1

    label = "Would cancel" if args.dry_run else "Cancelled"
    print(f"[INFO] {label} {cancelled_count} meeting(s), skipped {skipped_count}")


if __name__ == "__main__":
    main()
