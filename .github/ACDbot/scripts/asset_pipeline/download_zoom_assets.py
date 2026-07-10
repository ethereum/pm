#!/usr/bin/env python3
"""
Download Zoom Assets

This script downloads transcripts, chat logs, meeting summaries, and other assets
for a given Zoom meeting ID or for recent instances of a recurring meeting series.
"""

import argparse
import json
import sys
import traceback
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

import requests
from dotenv import load_dotenv

# Base paths relative to this script
SCRIPT_DIR = Path(__file__).parent
ACDBOT_DIR = SCRIPT_DIR.parent.parent
ARTIFACTS_DIR = ACDBOT_DIR / "artifacts"
MAPPING_FILE_PATH = ACDBOT_DIR / "meeting_topic_mapping.json"

# Load environment variables from the correct location
load_dotenv(ACDBOT_DIR / ".env")

# Add modules to path for standalone execution
sys.path.insert(0, str(ACDBOT_DIR / "modules"))

import zoom
from breakout_utils import select_breakout_recording
from mapping_manager import MappingManager
from mapping_utils import iter_breakout_meetings
from meeting_identity import extract_public_call_number, get_occurrence_call_number

def download_file(url: str, token: str, path: Path) -> bool:
    """Download a file from a URL with authentication."""
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)
            file_size = len(response.content)
            print(f"  ✅ Downloaded {path.name} ({file_size / 1024:.1f} KB)")
            return True
        else:
            print(f"  ❌ Failed to download {path.name}: {response.status_code} {response.text}")
            return False
    except Exception as e:
        print(f"  ❌ Failed to download {path.name}: {e}")
        return False

def extract_meeting_number(topic, _series_name):
    """Extract meeting number from the meeting topic."""
    number = extract_public_call_number(topic, include_series_patterns=True)
    return str(number) if number is not None else None

def find_occurrences_by_date_and_series(date_str, series_name, mapping_manager):
    """Find mapped occurrences for a specific date and series."""
    try:
        mapping = mapping_manager.mapping
        series_data = mapping.get(series_name)

        if not series_data or 'occurrences' not in series_data:
            return []

        occurrences = []
        for occurrence in series_data['occurrences']:
            start_time = occurrence.get('start_time', '')
            if start_time and start_time.startswith(date_str):
                occurrences.append(occurrence)

        return occurrences
    except Exception as e:
        print(f"   ❌ Error finding occurrence: {e}")
        return []


def find_occurrence_by_date_series_and_number(date_str, series_name, mapping_manager, number=None):
    """Find one mapped occurrence by date, series, and optional public call number."""
    occurrences = find_occurrences_by_date_and_series(date_str, series_name, mapping_manager)
    if number is not None:
        try:
            expected_number = int(number)
        except (TypeError, ValueError):
            print(f"   ❌ Invalid call number: {number}")
            return None

        matches = [
            occurrence for occurrence in occurrences
            if get_occurrence_call_number(occurrence) == expected_number
        ]
        if len(matches) == 1:
            return matches[0]
        if not matches:
            print(f"   ❌ No mapped occurrence for {series_name} #{expected_number} on {date_str}")
            return None
        print(f"   ❌ Multiple mapped occurrences for {series_name} #{expected_number} on {date_str}")
        return None

    if len(occurrences) == 1:
        return occurrences[0]
    if len(occurrences) > 1:
        numbers = [get_occurrence_call_number(occurrence) for occurrence in occurrences]
        print(f"   ❌ Ambiguous mapped occurrences for {series_name} on {date_str}: {numbers}")
    return None


def choose_recording(candidates, series_name, expected_number=None):
    """Choose one recording candidate without guessing across ambiguous calls.

    The mapped occurrence is the source of truth for the public call number.
    Zoom recording topics can retain stale recurring-meeting titles, so a
    single date-matched candidate is accepted even when its topic number is old.
    """
    if not candidates:
        return None, None

    if expected_number is not None:
        expected_number = int(expected_number)
        numbered_candidates = []
        unnumbered_candidates = []
        for instance, recording_data in candidates:
            topic_number = extract_meeting_number(recording_data.get('topic', ''), series_name)
            if topic_number is None:
                unnumbered_candidates.append((instance, recording_data))
            elif int(topic_number) == expected_number:
                numbered_candidates.append((instance, recording_data))
        if len(numbered_candidates) == 1:
            return numbered_candidates[0]
        if len(candidates) == 1 and len(unnumbered_candidates) == 1:
            return unnumbered_candidates[0]
        if len(candidates) == 1:
            _, recording_data = candidates[0]
            topic = recording_data.get('topic', '')
            print(
                f"   ⚠️  Recording topic does not match expected {series_name} #{expected_number}; "
                f"using mapped occurrence because it is the only candidate"
            )
            if topic:
                print(f"      Zoom topic: {topic}")
            return candidates[0]

        print(f"   ❌ Ambiguous recordings for {series_name} #{expected_number}; refusing to guess")
        return None, None

    if len(candidates) == 1:
        return candidates[0]

    print(f"   ❌ Ambiguous recordings for {series_name}; refusing to choose by duration alone")
    return None, None


def parse_utc_datetime(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def filter_candidates_by_occurrence_start(candidates, occurrence, tolerance_minutes=30):
    """Keep recordings near the mapped occurrence start time when possible."""
    if not candidates or not occurrence:
        return candidates

    target_start = parse_utc_datetime(occurrence.get("start_time"))
    if not target_start:
        return candidates

    tolerance = timedelta(minutes=tolerance_minutes)
    matching_candidates = []

    for instance, recording_data in candidates:
        start_time = instance.get("start_time") or recording_data.get("start_time")
        candidate_start = parse_utc_datetime(start_time)
        if candidate_start and abs(candidate_start - target_start) <= tolerance:
            matching_candidates.append((instance, recording_data))

    if matching_candidates:
        skipped = len(candidates) - len(matching_candidates)
        if skipped:
            print(
                f"   📍 Filtered out {skipped} same-day recording(s) outside "
                f"{tolerance_minutes} minutes of mapped start time"
            )
        return matching_candidates

    return candidates


def download_assets_for_meeting(
    recording_data: dict,
    series_name: str,
    access_token: str,
    include_summary: bool = False,
    occurrence: dict | None = None
) -> Path | None:
    """Downloads assets from recording data for a single meeting instance.

    Returns the meeting directory the assets were saved to, or None if the
    recording could not be processed.
    """
    if not recording_data or not recording_data.get('recording_files'):
        print("   No recording files found for this meeting instance.")
        return None

    start_time = recording_data.get('start_time')
    if not start_time:
        print("   ❌ Could not determine meeting start time. Cannot create directory.")
        return None

    if occurrence and occurrence.get('start_time'):
        date_part = occurrence['start_time'].split('T')[0]
    else:
        date_part = start_time.split('T')[0]

    topic = recording_data.get('topic', '')
    mapped_number = get_occurrence_call_number(occurrence)
    meeting_number = str(mapped_number) if mapped_number is not None else None
    number_source = "mapping" if meeting_number else None

    if not occurrence and not meeting_number:
        # Manual one-off processing may not have occurrence context; keep topic
        # parsing there, but never use it when a mapped occurrence is known.
        meeting_number = extract_meeting_number(topic, series_name)
        number_source = "topic" if meeting_number else None

    if not occurrence and not meeting_number:
        mapping_manager = MappingManager(str(MAPPING_FILE_PATH))
        mapped_occurrence = find_occurrence_by_date_series_and_number(date_part, series_name, mapping_manager)
        mapped_number = get_occurrence_call_number(mapped_occurrence)
        if mapped_number is not None:
            meeting_number = str(mapped_number)
            number_source = "mapping"

    # Create directory name with meeting number if available
    if meeting_number:
        padded_number = meeting_number.zfill(3)
        dir_name = f"{date_part}_{padded_number}"
        print(f"   📋 Meeting topic: {topic}")
        if number_source == "mapping":
            print(f"   🔢 Using public call number from mapping: {meeting_number}")
        else:
            print(f"   🔢 Extracted meeting number: {meeting_number}")
    else:
        dir_name = date_part
        if topic:
            print(f"   📋 Meeting topic: {topic} (no meeting number found)")

    # Create directory structure
    series_dir = ARTIFACTS_DIR / series_name
    meeting_dir = series_dir / dir_name

    # Check if assets already exist
    asset_map = {
        'TRANSCRIPT': 'transcript.vtt',
        'CC_TRANSCRIPT': 'closed_captions.vtt',  # Closed captions file
        'CHAT': 'chat.txt',
    }

    # Check if summary exists (only relevant if include_summary is True)
    summary_path = meeting_dir / 'summary.json'
    summary_exists = summary_path.exists()

    meeting_dir.mkdir(parents=True, exist_ok=True)

    print(f"   📂 Saving assets to: {meeting_dir}")

    download_count = 0

    # Download regular assets (transcript, chat) if they don't exist
    assets_to_download = []
    for file_info in recording_data.get('recording_files', []):
        file_type = file_info.get('file_type')
        if file_type in asset_map:
            filename = asset_map[file_type]
            filepath = meeting_dir / filename
            if not filepath.exists():
                assets_to_download.append((file_info, filename, filepath))

    for file_info, filename, filepath in assets_to_download:
        download_url = file_info.get('download_url')
        if download_url:
            if download_file(download_url, access_token, filepath):
                download_count += 1

    # Download meeting summary if requested and it doesn't exist
    if include_summary and not summary_exists:
        print(f"   📄 Checking for meeting summary...")
        meeting_uuid = recording_data.get('uuid')
        if meeting_uuid:
            try:
                summary_data = zoom.get_meeting_summary(meeting_uuid)
                if summary_data and summary_data != {}:
                    # Filter out unwanted keys from summary
                    keys_to_omit = {
                        "meeting_host_id", "meeting_host_email", "meeting_uuid",
                        "meeting_id", "summary_title", "summary_content", "summary_doc_url"
                    }
                    filtered_summary = {k: v for k, v in summary_data.items() if k not in keys_to_omit}

                    with open(summary_path, 'w', encoding='utf-8') as f:
                        json.dump(filtered_summary, f, indent=2)
                    print(f"   ✅ Downloaded summary.json")
                    download_count += 1
                else:
                    print(f"   ⚠️  No summary available for this meeting")
            except Exception as e:
                print(f"   ⚠️  Could not fetch summary: {e}")
        else:
            print(f"   ⚠️  No UUID available for summary download")

    if download_count > 0:
        print(f"   ✅ Downloaded {download_count} asset(s) for meeting on {date_part}.")
    else:
        print("   No new assets found to download for this instance.")

    return meeting_dir


def download_breakout_assets(
    occurrence: dict,
    breakout_label: str,
    breakout_meeting_id: str,
    meeting_dir: Path,
    access_token: str,
    min_duration_minutes: int,
) -> None:
    """Download a breakout room's transcript/chat into the parent occurrence dir.

    Breakout rooms held in a separate Zoom meeting (linked via the series-level
    "breakout_meeting_ids" mapping field) are matched to the parent occurrence
    by date and saved with suffixed filenames (e.g. transcript_cl.vtt) so they
    never collide with the parent call's assets.
    """
    occurrence_start = occurrence.get('start_time', '')
    if not occurrence_start:
        print(f"   ⚠️  No occurrence start time; skipping '{breakout_label}' breakout download")
        return

    target_date = occurrence_start.split('T')[0]

    asset_map = {
        'TRANSCRIPT': f'transcript_{breakout_label}.vtt',
        'CHAT': f'chat_{breakout_label}.txt',
    }

    # Skip Zoom API calls entirely if all breakout assets already exist
    if all((meeting_dir / filename).exists() for filename in asset_map.values()):
        print(f"   ⏭️  Breakout '{breakout_label}' assets already exist")
        return

    print(f"   📋 Checking '{breakout_label}' breakout meeting {breakout_meeting_id} for {target_date}...")

    recording_data = select_breakout_recording(
        zoom,
        occurrence,
        breakout_meeting_id,
        min_duration_minutes,
    )
    if not recording_data:
        print(
            f"   ⏭️  No unambiguous '{breakout_label}' breakout recording "
            f">= {min_duration_minutes} min on {target_date}"
        )
        return

    download_count = 0
    for file_info in recording_data.get('recording_files', []):
        filename = asset_map.get(file_info.get('file_type'))
        if not filename:
            continue
        filepath = meeting_dir / filename
        if filepath.exists():
            continue
        download_url = file_info.get('download_url')
        if download_url and download_file(download_url, access_token, filepath):
            download_count += 1

    if download_count > 0:
        print(f"   ✅ Downloaded {download_count} '{breakout_label}' breakout asset(s)")
    else:
        print(f"   No new '{breakout_label}' breakout assets to download")


def download_all_breakout_assets(
    series_data: dict,
    occurrence: dict,
    meeting_dir: Path | None,
    access_token: str,
    min_duration_minutes: int,
) -> None:
    """Download assets for every breakout meeting linked to a series."""
    if not meeting_dir:
        return

    for breakout_label, breakout_meeting_id in iter_breakout_meetings(series_data):
        try:
            download_breakout_assets(
                occurrence,
                breakout_label,
                breakout_meeting_id,
                meeting_dir,
                access_token,
                min_duration_minutes,
            )
        except Exception as e:
            print(f"   ⚠️  Failed to download '{breakout_label}' breakout assets: {e}")


def process_single_meeting(
    meeting_id: str,
    series_name: str,
    access_token: str,
    include_summary: bool = False
) -> None:
    """Process a single meeting by its ID or UUID."""
    print(f"📋 Getting recordings for meeting: {meeting_id}...")
    recording_data = zoom.get_meeting_recording(meeting_id)
    download_assets_for_meeting(recording_data, series_name, access_token, include_summary)


def process_recent_meetings(
    series_name: str,
    recent_count: int,
    access_token: str,
    min_duration_minutes: int = 15,
    include_summary: bool = False,
    requested_number: int | None = None
) -> None:
    """Fetch and process a number of recent meetings for a series using the mapping file."""
    print(f"📋 Looking up meeting ID for series '{series_name}'...")

    # Load the mapping to get the meeting ID(s) for this series
    mapping_manager = MappingManager(str(MAPPING_FILE_PATH))
    primary_meeting_id = mapping_manager.get_series_meeting_id(series_name)

    if not primary_meeting_id:
        print(f"❌ No meeting ID found for series '{series_name}' in the mapping file.")
        print("Available series:")
        for series in mapping_manager.mapping.keys():
            print(f"  - {series}")
        return

    # Get all meeting IDs for this series (primary + historical)
    meeting_ids = [primary_meeting_id]

    # Check for historical meeting IDs
    series_data = mapping_manager.mapping.get(series_name, {})
    historical_ids = series_data.get('historical_meeting_ids', [])
    if historical_ids:
        meeting_ids.extend(historical_ids)
        print(f"📋 Found {len(meeting_ids)} meeting ID(s) for series '{series_name}': {primary_meeting_id} (current) + {len(historical_ids)} historical")
    else:
        print(f"📋 Found meeting ID {primary_meeting_id} for series '{series_name}'")

    # Collect instances from all meeting IDs
    all_past_instances = []
    for i, meeting_id in enumerate(meeting_ids):
        instances = zoom.get_past_meeting_instances(meeting_id)
        if instances:
            all_past_instances.extend(instances)

    if not all_past_instances:
        print(f"No recent meeting instances found for series '{series_name}' across {len(meeting_ids)} meeting ID(s).")
        return

    print(f"📋 Total instances found across all meeting IDs: {len(all_past_instances)}")

    # Group instances by date and find the best recording for each date
    date_groups = defaultdict(list)

    # Group all instances by date
    for instance in all_past_instances:
        start_time = instance.get('start_time', '')
        if start_time:
            # Extract date (YYYY-MM-DD)
            date_part = start_time.split('T')[0]
            date_groups[date_part].append(instance)

    # Process each date to find the best recording
    valid_meetings = []
    dates_processed = 0

    # Sort dates in reverse chronological order (most recent first)
    sorted_dates = sorted(date_groups.keys(), reverse=True)

    for date in sorted_dates:
        if dates_processed >= recent_count:
            break

        occurrence = find_occurrence_by_date_series_and_number(
            date,
            series_name,
            mapping_manager,
            requested_number,
        )
        if not occurrence:
            print(f"\n⏭️  Skipping {date}: no mapped occurrence for series '{series_name}'")
            continue

        instances_for_date = date_groups[date]
        print(f"\n📅 Processing {len(instances_for_date)} instance(s) from {date}:")

        candidates = []

        # Check all instances for this date to find valid recording candidates.
        for instance in instances_for_date:
            uuid = instance.get('uuid')

            if uuid:
                recording_data = zoom.get_meeting_recording(uuid)

                if recording_data:
                    duration = recording_data.get('duration', 0)

                    if duration >= min_duration_minutes:
                        candidates.append((instance, recording_data))

        expected_number = get_occurrence_call_number(occurrence)
        candidates = filter_candidates_by_occurrence_start(candidates, occurrence)
        best_instance, best_recording = choose_recording(candidates, series_name, expected_number)
        if best_recording and best_instance:
            print(f"   🎯 Selected recording for {date}: {best_recording.get('duration', 0)} minutes")
            valid_meetings.append((best_instance, best_recording, occurrence))
            dates_processed += 1
        else:
            print(f"   ❌ No valid recordings found for {date}")

    if not valid_meetings:
        print(f"❌ No meetings found with duration >= {min_duration_minutes} minutes")
        return

    print(f"\n📋 Found {len(valid_meetings)} meeting(s) with sufficient duration to process.")
    for i, (instance, recording_data, occurrence) in enumerate(valid_meetings):
        uuid = instance.get('uuid')
        start_time = instance.get('start_time', 'N/A')
        duration = recording_data.get('duration', 0)
        date_part = start_time.split('T')[0] if start_time != 'N/A' else 'Unknown'
        print(f"\nProcessing meeting {i+1}/{len(valid_meetings)} from {date_part} (UUID: {uuid}, Duration: {duration} min)")
        meeting_dir = download_assets_for_meeting(recording_data, series_name, access_token, include_summary, occurrence)
        download_all_breakout_assets(
            series_data,
            occurrence,
            meeting_dir,
            access_token,
            min_duration_minutes,
        )


def process_meeting_by_date(
    series_name: str,
    target_date: str,
    access_token: str,
    min_duration_minutes: int = 15,
    include_summary: bool = False,
    requested_number: int | None = None
) -> None:
    """Fetch and process a meeting for a specific date using the mapping file."""
    print(f"📋 Looking up meeting ID for series '{series_name}'...")

    # Load the mapping to get the meeting ID(s) for this series
    mapping_manager = MappingManager(str(MAPPING_FILE_PATH))
    primary_meeting_id = mapping_manager.get_series_meeting_id(series_name)

    if not primary_meeting_id:
        print(f"❌ No meeting ID found for series '{series_name}' in the mapping file.")
        print("Available series:")
        for series in mapping_manager.mapping.keys():
            print(f"  - {series}")
        return

    # Get all meeting IDs for this series (primary + historical)
    meeting_ids = [primary_meeting_id]

    # Check for historical meeting IDs
    series_data = mapping_manager.mapping.get(series_name, {})
    historical_ids = series_data.get('historical_meeting_ids', [])
    if historical_ids:
        meeting_ids.extend(historical_ids)
        print(f"📋 Found {len(meeting_ids)} meeting ID(s) for series '{series_name}': {primary_meeting_id} (current) + {len(historical_ids)} historical")
    else:
        print(f"📋 Found meeting ID {primary_meeting_id} for series '{series_name}'")

    print(f"📋 Searching for meeting on {target_date}...")
    occurrence = find_occurrence_by_date_series_and_number(
        target_date,
        series_name,
        mapping_manager,
        requested_number,
    )
    if not occurrence:
        print(f"❌ Could not resolve a single mapped occurrence for series '{series_name}' on {target_date}.")
        print("   Pass --number when multiple calls share the same date, or fix meeting_topic_mapping.json.")
        return

    candidates = []

    # Method 1: Try get_past_meeting_instances for each meeting ID
    print(f"\n🔍 Method 1: Searching via past meeting instances...")
    for i, meeting_id in enumerate(meeting_ids):
        print(f"   Checking meeting ID {meeting_id} ({i+1}/{len(meeting_ids)})...")
        instances = zoom.get_past_meeting_instances(meeting_id)

        if not instances:
            print(f"   No instances found for meeting ID {meeting_id}")
            continue

        print(f"   Found {len(instances)} instances from meeting ID {meeting_id}")

        # Search for the instance matching the target date
        for instance in instances:
            start_time = instance.get('start_time', '')
            if start_time and start_time.startswith(target_date):
                uuid = instance.get('uuid')
                print(f"   ✅ Found instance from {target_date} (UUID: {uuid})")

                # Get recording data
                recording_data = zoom.get_meeting_recording(uuid)
                if recording_data:
                    duration = recording_data.get('duration', 0)
                    print(f"   Duration: {duration} minutes")

                    if duration >= min_duration_minutes:
                        candidates.append((instance, recording_data))
                    else:
                        print(f"   ⏭️  Duration below minimum ({duration} < {min_duration_minutes} min)")
                else:
                    print(f"   ❌ No recording data found")

    _, matching_recording = choose_recording(
        filter_candidates_by_occurrence_start(candidates, occurrence),
        series_name,
        get_occurrence_call_number(occurrence),
    )
    if not matching_recording:
        print(f"\n❌ No meeting found on {target_date} with duration >= {min_duration_minutes} minutes")
        print(f"\n💡 The mapping file has an occurrence on {target_date}:")
        print(f"   Issue: #{occurrence.get('issue_number')}")
        print(f"   Title: {occurrence.get('issue_title')}")
        print("\n   ACDbot only ingests recordings found through the mapped meeting IDs.")
        print("   If this call used a different Zoom meeting, add that meeting ID to")
        print("   historical_meeting_ids or ingest the exact recording UUID manually.")
        return

    # Download assets for the matched meeting
    print(f"\n📋 Processing meeting from {target_date} (Duration: {matching_recording.get('duration', 0)} min)")
    meeting_dir = download_assets_for_meeting(matching_recording, series_name, access_token, include_summary, occurrence)
    download_all_breakout_assets(
        series_data,
        occurrence,
        meeting_dir,
        access_token,
        min_duration_minutes,
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download assets from Zoom meetings.")

    parser.add_argument("--series-name", required=True, help="The name of the call series (e.g., 'acde').")
    parser.add_argument("--min-duration", type=int, default=15, help="Minimum meeting duration in minutes to process (default: 15). Applies to --recent and --date.")
    parser.add_argument("--include-summary", action="store_true", help="Download Zoom's meeting summary (summary.json). Disabled by default.")
    parser.add_argument("--number", type=int, help="Expected public call number for disambiguating same-day occurrences.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--meeting-id", help="A specific meeting instance ID or UUID.")
    group.add_argument("--recent", type=int, nargs='?', const=1, default=None, help="Download for N most recent meetings in a series. Defaults to 1.")
    group.add_argument("--date", help="Download assets for a meeting on a specific date (YYYY-MM-DD format).")

    args = parser.parse_args()

    try:
        access_token = zoom.get_access_token()

        if args.meeting_id:
            process_single_meeting(args.meeting_id, args.series_name, access_token, args.include_summary)
        elif args.recent is not None:
            process_recent_meetings(
                args.series_name,
                args.recent,
                access_token,
                args.min_duration,
                args.include_summary,
                args.number,
            )
        elif args.date:
            process_meeting_by_date(
                args.series_name,
                args.date,
                access_token,
                args.min_duration,
                args.include_summary,
                args.number,
            )

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        traceback.print_exc()
        sys.exit(1)
