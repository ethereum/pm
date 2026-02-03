#!/usr/bin/env python3
"""
Download Zoom Assets

This script downloads transcripts, chat logs, meeting summaries, and other assets
for a given Zoom meeting ID or for recent instances of a recurring meeting series.
"""

import argparse
import json
import re
import sys
import traceback
from collections import defaultdict
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

# Add modules to path
sys.path.insert(0, str(ACDBOT_DIR / "modules"))

# Import zoom module after path is set
import zoom
from mapping_manager import MappingManager

# Maximum meeting number for validation (reasonable upper bound)
MAX_MEETING_NUMBER = 999

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

def extract_meeting_number(topic, series_name):
    """Extract meeting number from the meeting topic."""
    if not topic:
        return None

    # Common patterns for meeting numbers
    patterns = [
        # Pattern for "ACDE #210", "ACDC #164", etc.
        r'#(\d+)',
        # Pattern for "Meeting 210", "Call 164", etc.
        r'(?:Meeting|Call)\s+(\d+)',
        # Pattern for numbers at the end like "ACDE 210"
        r'\b(\d{2,4})(?:\s*,|\s*$)',
        # Pattern for numbers after series name like "All Core Devs - Execution 210"
        r'(?:ACDE|ACDC|ACDT|Execution|Consensus|Testing)\s+(\d+)',
        # Pattern for ePBS breakout room calls like "EIP-7732 Breakout Room Call #21"
        r'(?:EIP-7732\s+)?Breakout\s+Room\s+(?:call|Call)\s+#?(\d+)',
        # Pattern for BAL breakout calls like "EIP-7928 Breakout #1"
        r'EIP-7928\s+Breakout\s+#(\d+)',
        # Pattern for FOCIL breakout calls like "FOCIL Breakout #10"
        r'FOCIL\s+Breakout\s+#(\d+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, topic, re.IGNORECASE)
        if match:
            number = match.group(1)
            # Validate it looks like a reasonable meeting number (not year, etc.)
            if 1 <= int(number) <= MAX_MEETING_NUMBER:
                return number

    return None

def find_occurrence_by_date_and_series(date_str, series_name, mapping_manager):
    """Find the occurrence data for a specific date and series."""
    try:
        mapping = mapping_manager.mapping
        series_data = mapping.get(series_name)

        if not series_data or 'occurrences' not in series_data:
            return None

        for occurrence in series_data['occurrences']:
            start_time = occurrence.get('start_time', '')
            if start_time and start_time.startswith(date_str):
                return occurrence

        return None
    except Exception as e:
        print(f"   ❌ Error finding occurrence: {e}")
        return None

def get_youtube_video_url(occurrence):
    """Extract YouTube video URL from occurrence data."""
    # Check for uploaded video ID first (preferred)
    if occurrence.get('youtube_video_id'):
        return f"https://www.youtube.com/watch?v={occurrence['youtube_video_id']}"

    # Check for stream URLs in youtube_streams
    youtube_streams = occurrence.get('youtube_streams')
    if youtube_streams and isinstance(youtube_streams, list) and len(youtube_streams) > 0:
        stream_url = youtube_streams[0].get('stream_url')
        if stream_url:
            return stream_url

    return None

def create_config_json(meeting_dir: Path, occurrence: dict | None) -> None:
    """Create config.json file with issue number and YouTube video URL."""
    if not occurrence:
        print("   ⚠️  No occurrence data found - skipping config.json creation")
        return

    issue_number = occurrence.get('issue_number')
    video_url = get_youtube_video_url(occurrence)

    config_data = {
        "issue": issue_number,
        "videoUrl": video_url,
        "sync": {
            "transcriptStartTime": "00:00:00",
            "videoStartTime": "00:00:00"
        }
    }

    config_path = meeting_dir / 'config.json'
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2)
        print(f"  ✅ Created config.json with issue #{issue_number}")
        if video_url:
            print(f"     📺 Video URL: {video_url}")
        else:
            print(f"     📺 Video URL: null (no video found)")
    except Exception as e:
        print(f"  ❌ Failed to create config.json: {e}")

def download_assets_for_meeting(
    recording_data: dict,
    series_name: str,
    access_token: str,
    include_summary: bool = False
) -> None:
    """Downloads assets from recording data for a single meeting instance."""
    if not recording_data or not recording_data.get('recording_files'):
        print("   No recording files found for this meeting instance.")
        return

    start_time = recording_data.get('start_time')
    if not start_time:
        print("   ❌ Could not determine meeting start time. Cannot create directory.")
        return

    date_part = start_time.split('T')[0]

    # Extract meeting number from topic if available
    topic = recording_data.get('topic', '')
    meeting_number = extract_meeting_number(topic, series_name)

    # Create directory name with meeting number if available
    if meeting_number:
        # Zero-pad meeting number to 3 digits
        padded_number = meeting_number.zfill(3)
        dir_name = f"{date_part}_{padded_number}"
        print(f"   📋 Meeting topic: {topic}")
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

    existing_assets = []
    for file_type, filename in asset_map.items():
        filepath = meeting_dir / filename
        if filepath.exists():
            existing_assets.append(filename)

    # Check if summary exists (only relevant if include_summary is True)
    summary_path = meeting_dir / 'summary.json'
    summary_exists = summary_path.exists()
    if summary_exists:
        existing_assets.append('summary.json')

    # Check if config.json exists
    config_path = meeting_dir / 'config.json'
    config_exists = config_path.exists()

    # Determine if all required assets exist
    summary_satisfied = summary_exists if include_summary else True
    if existing_assets and config_exists and summary_satisfied:
        print(f"   ⏭️  Skipping {date_part} - all assets already exist: {', '.join(existing_assets)}, config.json")
        return

    meeting_dir.mkdir(parents=True, exist_ok=True)

    # Find occurrence data for config.json creation
    mapping_manager = MappingManager(str(MAPPING_FILE_PATH))
    occurrence = find_occurrence_by_date_and_series(date_part, series_name, mapping_manager)

    # Create config.json if it doesn't exist
    if not config_exists:
        create_config_json(meeting_dir, occurrence)

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
    min_duration_minutes: int = 10,
    include_summary: bool = False
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
    print(f"📋 Getting meeting instances with minimum duration of {min_duration_minutes} minutes...")

    # Collect instances from all meeting IDs
    all_past_instances = []
    for i, meeting_id in enumerate(meeting_ids):
        print(f"   Getting instances from meeting ID {meeting_id} ({i+1}/{len(meeting_ids)})...")
        instances = zoom.get_past_meeting_instances(meeting_id)
        if instances:
            print(f"   Found {len(instances)} instances from meeting ID {meeting_id}")
            all_past_instances.extend(instances)
        else:
            print(f"   No instances found for meeting ID {meeting_id}")

    if not all_past_instances:
        print(f"No recent meeting instances found for series '{series_name}' across {len(meeting_ids)} meeting ID(s).")
        return

    print(f"📋 Total instances found across all meeting IDs: {len(all_past_instances)}")

    # Group instances by date and find the best recording for each date
    date_groups = defaultdict(list)

    print(f"📋 Grouping instances by date and finding best recordings...")

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

        instances_for_date = date_groups[date]
        print(f"\n📅 Processing {len(instances_for_date)} instance(s) from {date}:")

        best_recording = None
        best_duration = 0
        best_instance = None

        # Check all instances for this date to find the longest valid recording
        for instance in instances_for_date:
            uuid = instance.get('uuid')
            start_time = instance.get('start_time', 'N/A')

            if uuid:
                print(f"   Checking instance from {start_time} (UUID: {uuid})")
                recording_data = zoom.get_meeting_recording(uuid)

                if recording_data:
                    duration = recording_data.get('duration', 0)
                    print(f"   Duration: {duration} minutes")

                    if duration >= min_duration_minutes and duration > best_duration:
                        best_duration = duration
                        best_recording = recording_data
                        best_instance = instance
                        print(f"   ✅ New best recording for {date} ({duration} min)")
                    else:
                        print(f"   ⏭️  Not the best recording for this date ({duration} min)")
                else:
                    print(f"   ❌ No recording data found")

        if best_recording and best_instance:
            print(f"   🎯 Selected best recording for {date}: {best_duration} minutes")
            valid_meetings.append((best_instance, best_recording))
            dates_processed += 1
        else:
            print(f"   ❌ No valid recordings found for {date}")

    if not valid_meetings:
        print(f"❌ No meetings found with duration >= {min_duration_minutes} minutes")
        return

    print(f"\n📋 Found {len(valid_meetings)} meeting(s) with sufficient duration to process.")
    for i, (instance, recording_data) in enumerate(valid_meetings):
        uuid = instance.get('uuid')
        start_time = instance.get('start_time', 'N/A')
        duration = recording_data.get('duration', 0)
        date_part = start_time.split('T')[0] if start_time != 'N/A' else 'Unknown'
        print(f"\nProcessing meeting {i+1}/{len(valid_meetings)} from {date_part} (UUID: {uuid}, Duration: {duration} min)")
        download_assets_for_meeting(recording_data, series_name, access_token, include_summary)


def get_topic_prefixes_for_series(series_name, mapping_manager):
    """Get possible topic prefixes for a series based on mapping data."""
    # Known prefixes for common series
    known_prefixes = {
        'epbs': ['EIP-7732', 'ePBS'],
        'acde': ['All Core Devs - Execution', 'ACDE', 'AllCoreDevs Execution'],
        'acdc': ['All Core Devs - Consensus', 'ACDC', 'AllCoreDevs Consensus'],
        'acdt': ['All Core Devs - Testing', 'ACDT', 'AllCoreDevs Testing'],
        'focil': ['FOCIL'],
        'bal': ['EIP-7928', 'BAL'],
        'peerdas': ['PeerDAS'],
        'rollcall': ['RollCall', 'Rollup Call'],
    }

    prefixes = known_prefixes.get(series_name, [])

    # Also extract prefix from existing occurrence titles in the mapping
    series_data = mapping_manager.mapping.get(series_name, {})
    occurrences = series_data.get('occurrences', [])
    if occurrences:
        # Get unique prefixes from occurrence titles (first few words)
        for occ in occurrences[:3]:  # Check first 3 occurrences
            title = occ.get('issue_title', '')
            if title:
                # Extract prefix up to first number or comma
                prefix_match = re.match(r'^([A-Za-z\-\s]+)', title)
                if prefix_match:
                    prefix = prefix_match.group(1).strip()
                    if prefix and prefix not in prefixes:
                        prefixes.append(prefix)

    return prefixes


def process_meeting_by_date(
    series_name: str,
    target_date: str,
    access_token: str,
    min_duration_minutes: int = 10,
    include_summary: bool = False
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

    # Track the best matching recording found
    matching_recording = None

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
                        if not matching_recording or duration > matching_recording.get('duration', 0):
                            matching_recording = recording_data
                            print(f"   ✅ Best match so far ({duration} min)")
                    else:
                        print(f"   ⏭️  Duration below minimum ({duration} < {min_duration_minutes} min)")
                else:
                    print(f"   ❌ No recording data found")

    # Method 2: Fallback to searching all recordings for the date if not found
    if not matching_recording:
        print(f"\n🔍 Method 2: Searching via recordings list for {target_date}...")
        topic_prefixes = get_topic_prefixes_for_series(series_name, mapping_manager)
        print(f"   Looking for topics starting with: {topic_prefixes}")

        try:
            recordings = zoom.get_recordings_for_date(target_date)
            print(f"   Found {len(recordings)} recordings on {target_date}")
        except Exception as e:
            print(f"   ❌ Error fetching recordings: {e}")
            recordings = []

        for recording in recordings:
            topic = recording.get('topic', '')
            duration = recording.get('duration', 0)
            uuid = recording.get('uuid', '')

            # Check if topic matches any of our prefixes
            matches_prefix = any(topic.startswith(prefix) for prefix in topic_prefixes)

            if matches_prefix:
                print(f"   📋 Found matching topic: '{topic}' ({duration} min)")

                if duration >= min_duration_minutes:
                    if not matching_recording or duration > matching_recording.get('duration', 0):
                        # Get full recording data
                        full_recording = zoom.get_meeting_recording(uuid)
                        if full_recording:
                            matching_recording = full_recording
                            print(f"   ✅ Best match so far ({duration} min)")
                        else:
                            print(f"   ⚠️  Could not fetch full recording data")
                else:
                    print(f"   ⏭️  Duration below minimum ({duration} < {min_duration_minutes} min)")
            else:
                if duration >= min_duration_minutes:
                    print(f"   ⏭️  Skipping non-matching topic: '{topic}' ({duration} min)")

    if not matching_recording:
        print(f"\n❌ No meeting found on {target_date} with duration >= {min_duration_minutes} minutes")

        # Check if the date exists in the mapping
        occurrence = find_occurrence_by_date_and_series(target_date, series_name, mapping_manager)
        if occurrence:
            print(f"\n💡 Note: The mapping file shows a meeting on {target_date}:")
            print(f"   Issue: #{occurrence.get('issue_number')}")
            print(f"   Title: {occurrence.get('issue_title')}")
            print(f"\n   The Zoom API may not have this meeting's recording available.")
            print(f"   This can happen if:")
            print(f"   - The recording has been deleted or archived")
            print(f"   - The meeting was held with a different meeting ID")
            print(f"   - The Zoom API has a retention limit for past instances")
        return

    # Download assets for the matched meeting
    print(f"\n📋 Processing meeting from {target_date} (Duration: {matching_recording.get('duration', 0)} min)")
    download_assets_for_meeting(matching_recording, series_name, access_token, include_summary)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download assets from Zoom meetings.")

    parser.add_argument("--series-name", required=True, help="The name of the call series (e.g., 'acde').")
    parser.add_argument("--min-duration", type=int, default=10, help="Minimum meeting duration in minutes to process (default: 10). Applies to --recent and --date.")
    parser.add_argument("--include-summary", action="store_true", help="Download Zoom's meeting summary (summary.json). Disabled by default.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--meeting-id", help="A specific meeting instance ID or UUID.")
    group.add_argument("--recent", type=int, nargs='?', const=1, default=None, help="Download for N most recent meetings in a series. Defaults to 1.")
    group.add_argument("--date", help="Download assets for a meeting on a specific date (YYYY-MM-DD format).")

    args = parser.parse_args()

    try:
        print("🔐 Getting Zoom access token...")
        access_token = zoom.get_access_token()
        print("✅ Authenticated with Zoom")

        if args.meeting_id:
            process_single_meeting(args.meeting_id, args.series_name, access_token, args.include_summary)
        elif args.recent is not None:
            process_recent_meetings(args.series_name, args.recent, access_token, args.min_duration, args.include_summary)
        elif args.date:
            process_meeting_by_date(args.series_name, args.date, access_token, args.min_duration, args.include_summary)

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        traceback.print_exc()
        sys.exit(1)
