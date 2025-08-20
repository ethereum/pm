import os
import json
import argparse
from datetime import datetime, timedelta, timezone
import pytz
from modules import zoom, transcript, youtube_utils, rss_utils, discourse
from modules import tg
from modules.mapping_utils import (
    load_mapping as load_meeting_topic_mapping,
    save_mapping as save_meeting_topic_mapping,
    find_meeting_by_id,
    update_occurrence_entry,
    find_call_series_by_meeting_id
)

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def is_meeting_eligible(meeting_end_time):
    """
    Check if the meeting ended more than 15 minutes ago.
    Ensures both times are timezone-aware (UTC).
    """
    now_utc = datetime.now(timezone.utc)
    if meeting_end_time.tzinfo is None:
        # Assume UTC if timezone is missing (should not happen with Zoom data)
        meeting_end_time = meeting_end_time.replace(tzinfo=timezone.utc)
    return now_utc - meeting_end_time >= timedelta(minutes=15)

def validate_meeting_id(meeting_id):
    return str(meeting_id).strip()

def find_matching_recordings(meeting_id, series_name=None, target_start_time=None, tolerance_minutes=30):
    """Find recordings for transcript processing with filters.

    Args:
        meeting_id: The Zoom meeting ID
        series_name: Optional series name for logging/topic fallback
        target_start_time: Optional datetime to filter recordings by start time
        tolerance_minutes: Tolerance for time matching in minutes

    Returns:
        List of recording dictionaries matching transcript processing criteria
    """
    topic_fallback = f"{series_name.upper()} Meeting" if series_name else "Meeting"

    return zoom.find_recordings_with_filters(
        meeting_id=meeting_id,
        target_start_time=target_start_time,
        min_duration=10,
        require_transcript=True,
        tolerance_minutes=tolerance_minutes,
        topic_fallback=topic_fallback
    )

def find_best_transcript_recording(meeting_id, target_date=None):
    """Find the best recording for transcript processing, checking all past instances.

    This function:
    - gets all past meeting instances for the meeting ID,
    - checks recordings for each instance UUID,
    - filters by target date if provided (strict date matching), and
    - returns the longest recording with transcript files.

    Args:
        meeting_id: The meeting ID (numeric)
        target_date: Optional date string (YYYY-MM-DD) to match exactly

    Returns:
        Best recording data dict, or None if no suitable recording found
    """
    from datetime import datetime

    instances = zoom.get_past_meeting_instances(meeting_id)
    if not instances:
        print(f"No past meeting instances found for meeting {meeting_id}")
        return None

    print(f"Found {len(instances)} past meeting instances for meeting {meeting_id}")

    valid_recordings = []

    for instance in instances:
        instance_uuid = instance.get('uuid')
        start_time = instance.get('start_time')

        if not instance_uuid or not start_time:
            continue

        # Parse the start time to get the date
        try:
            start_dt = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            instance_date = start_dt.strftime('%Y-%m-%d')
        except:
            print(f"Could not parse start time for instance {instance_uuid}: {start_time}")
            continue

        # If target_date is specified, enforce strict date matching
        if target_date and instance_date != target_date:
            print(f"Skipping instance {instance_uuid}: date {instance_date} != target {target_date}")
            continue

        print(f"Checking recordings for instance {instance_uuid} ({instance_date})")

        # Get recordings for this specific instance UUID
        recording_data = zoom.get_meeting_recording(instance_uuid)

        if recording_data and recording_data.get('recording_files'):
            duration = recording_data.get('duration', 0)
            recording_files = recording_data.get('recording_files', [])

            # Check for transcript files (transcript processing requirement)
            transcript_files = [f for f in recording_files if f.get('file_type') == 'TRANSCRIPT']
            has_transcript = len(transcript_files) > 0

            print(f"  Found recording: {duration} min, {len(recording_files)} files, transcript: {has_transcript}")

            # Only consider recordings with meaningful duration and transcript
            if duration > 10 and has_transcript:
                valid_recordings.append({
                    'data': recording_data,
                    'duration': duration,
                    'date': instance_date,
                    'uuid': instance_uuid,
                    'start_time': start_time,
                    'transcript_files': len(transcript_files)
                })
                print(f"  ✅ Valid recording candidate: {duration} min with transcript")
            else:
                print(f"  ⚠️  Skipped: duration {duration} min, transcript: {has_transcript}")
        else:
            print(f"  No recordings found for instance {instance_uuid}")

    if not valid_recordings:
        print(f"No valid recordings found for meeting {meeting_id}" +
              (f" on date {target_date}" if target_date else ""))
        return None

    valid_recordings.sort(key=lambda x: x['duration'], reverse=True)
    best_recording = valid_recordings[0]

    print(f"Selected best recording: {best_recording['duration']} min from {best_recording['date']} "
          f"(UUID: {best_recording['uuid']})")

    return best_recording['data']

def update_transcript_attempt_count(recording_meeting_id, occurrence_issue_number, transcript_attempts, mapping, force_process=False):
    """Update transcript attempt count if not in force mode.

    Args:
        recording_meeting_id: The meeting ID
        occurrence_issue_number: The occurrence issue number
        transcript_attempts: Current attempt count
        mapping: The mapping dictionary
        force_process: Whether this is forced processing (skips increment if True)
    """
    if force_process:
        return

    call_series = find_call_series_by_meeting_id(recording_meeting_id, occurrence_issue_number, mapping)
    if call_series is not None:
        try:
            updates = {"transcript_attempt_count": transcript_attempts + 1}
            update_occurrence_entry(call_series, occurrence_issue_number, updates, mapping)
        except Exception as e:
            print(f"[ERROR] Failed to update attempt count: {e}")
    else:
        print(f"[ERROR] Could not find call series for updating attempt count")

def find_matching_occurrence(occurrences, recording_start_time_str, tolerance_minutes=30):
    """Finds the occurrence matching the recording start time."""
    if not occurrences:
        return None, -1

    try:
        recording_start_time = datetime.fromisoformat(recording_start_time_str.replace('Z', '+00:00'))
    except ValueError:
        print(f"[ERROR] Invalid recording start time format: {recording_start_time_str}")
        return None, -1

    tolerance = timedelta(minutes=tolerance_minutes)

    for index, occurrence in enumerate(occurrences):
        occurrence_start_time_str = occurrence.get("start_time")
        if not occurrence_start_time_str:
            continue
        try:
            occurrence_start_time = datetime.fromisoformat(occurrence_start_time_str.replace('Z', '+00:00'))
            if abs(recording_start_time - occurrence_start_time) <= tolerance:
                print(f"[DEBUG] Matched recording start time {recording_start_time} with occurrence #{occurrence.get('issue_number')} start time {occurrence_start_time}")
                return occurrence, index
        except ValueError:
            print(f"[WARN] Invalid start_time format in occurrence: {occurrence_start_time_str}")
            continue

    print(f"[WARN] No occurrence found matching recording start time {recording_start_time}")
    return None, -1

def process_single_occurrence(recording, occurrence, occurrence_index, series_entry, mapping, force_process=False):
    """Processes transcript and Discourse posts for a single matched recording and occurrence."""
    mapping_updated = False
    recording_meeting_id = str(series_entry.get("meeting_id")) # Should be the same as recording.get("id")
    occurrence_issue_number = occurrence.get("issue_number")
    # Get the UUID of the specific meeting instance from the recording data
    meeting_instance_uuid = recording.get("uuid")
    if not meeting_instance_uuid:
        print(f"[ERROR] Missing UUID in recording data for Meeting ID {recording_meeting_id}, Start Time {recording.get('start_time')}. Cannot process summary.")
        # Decide how to handle: skip this recording? Mark an error?
        # For now, we'll attempt to continue without the summary.
        pass # Allow proceeding, summary fetch will be skipped later

    print(f"Processing transcript for Meeting ID {recording_meeting_id}, Occurrence Issue #{occurrence_issue_number}")

    # Check eligibility (meeting ended > 15 mins ago)
    try:
        rec_end_time = datetime.fromisoformat(recording.get("end_time", recording.get("start_time")).replace('Z', '+00:00'))
        if not is_meeting_eligible(rec_end_time):
            print(f"  -> Skipping: Meeting ended less than 15 minutes ago ({rec_end_time.isoformat()}).")
            return False # No update occurred
    except Exception as e:
         print(f"[WARN] Could not parse recording end time, proceeding cautiously: {e}")

    # --- Transcript Posting Logic ---
    transcript_processed = occurrence.get("transcript_processed", False)
    transcript_attempts = occurrence.get("transcript_attempt_count", 0)
    discourse_topic_id = occurrence.get("discourse_topic_id")
    # Allow forced processing even if attempts > 10
    can_attempt_transcript = not transcript_processed and (force_process or transcript_attempts < 10) and discourse_topic_id

    if can_attempt_transcript:
        attempt_number = transcript_attempts + 1
        print(f"  -> Attempting transcript posting (Attempt {attempt_number})...")
        try:
            # Pass meeting ID and occurrence details for context
            transcript_success = transcript.post_zoom_transcript_to_discourse(
                meeting_id=recording_meeting_id,
                occurrence_details=occurrence,
                meeting_uuid_for_summary=meeting_instance_uuid # Pass the correct UUID
            )

            if transcript_success:
                # Find the correct call series for updating
                call_series = find_call_series_by_meeting_id(recording_meeting_id, occurrence_issue_number, mapping)

                if call_series is not None:
                    try:
                        # Update the mapping with success status using existing utility
                        updates = {
                            "transcript_processed": True,
                            "transcript_attempt_count": 0
                        }
                        if update_occurrence_entry(call_series, occurrence_issue_number, updates, mapping):
                            mapping_updated = True
                            print(f"  -> Transcript posted successfully for occurrence #{occurrence_issue_number} to topic {discourse_topic_id}.")
                        else:
                            print(f"  -> Transcript posted successfully but failed to update mapping.")
                            mapping_updated = True  # Still mark as updated to prevent retries
                    except Exception as e:
                        print(f"[ERROR] Unexpected error updating mapping: {e}")
                        mapping_updated = True
                else:
                    print(f"[ERROR] Could not find call series for meeting {recording_meeting_id}, issue {occurrence_issue_number}")
                    print(f"[ERROR] This indicates a mapping structure issue. Manual intervention may be needed.")
                    mapping_updated = True  # Still mark as updated to prevent retries

                # Update RSS feed with transcript info
                try:
                    rss_utils.add_notification_to_meeting(
                        recording_meeting_id,
                        occurrence_issue_number, # Pass issue number to identify occurrence
                        "transcript_posted",
                        "Meeting transcript posted to Discourse",
                        f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{discourse_topic_id}"
                    )
                    print(f"  -> Updated RSS feed with transcript info.")
                except Exception as e:
                    print(f"[ERROR] Failed to update RSS feed for transcript: {e}")
            else:
                 # Increment attempt counter only if not forced
                 update_transcript_attempt_count(recording_meeting_id, occurrence_issue_number, transcript_attempts, mapping, force_process)
                 mapping_updated = True
                 print(f"  -> Transcript posting failed.")

        except Exception as e:
            # Increment attempt counter only if not forced
            update_transcript_attempt_count(recording_meeting_id, occurrence_issue_number, transcript_attempts, mapping, force_process)
            mapping_updated = True
            print(f"[ERROR] Error posting transcript for occurrence #{occurrence_issue_number}: {e}")
    elif transcript_processed:
         print(f"  -> Transcript already posted.")
    elif transcript_attempts >= 10 and not force_process:
         print(f"  -> Skipping transcript posting: Max attempts reached.")
    elif not discourse_topic_id:
         print(f"  -> Skipping transcript posting: No Discourse topic ID found for occurrence.")


    # --- Post YouTube stream links to Discourse (if needed) ---
    # This logic remains as it posts *existing* links, not uploading videos.
    streams_posted = occurrence.get("youtube_streams_posted_to_discourse", False)
    occurrence_youtube_streams = occurrence.get("youtube_streams")
    can_post_streams = discourse_topic_id and not streams_posted and occurrence_youtube_streams

    if can_post_streams:
         print(f"  -> Posting YouTube stream links to Discourse topic {discourse_topic_id}...")
         stream_links_text = "\\n".join([
             f"- Stream {i+1}: {stream.get('stream_url', 'URL not found')}"
             for i, stream in enumerate(occurrence_youtube_streams)
         ])
         title = "**YouTube Stream Links:**" # Changed title slightly as context might be different
         discourse_body = f"{title}\n{stream_links_text}"
         try:
             discourse.create_post(topic_id=discourse_topic_id, body=discourse_body)

             # Find the correct call series for updating
             call_series = find_call_series_by_meeting_id(recording_meeting_id, occurrence_issue_number, mapping)

             if call_series is not None:
                 try:
                     updates = {"youtube_streams_posted_to_discourse": True}
                     if update_occurrence_entry(call_series, occurrence_issue_number, updates, mapping):
                         mapping_updated = True
                         print(f"  -> Successfully posted YouTube streams to Discourse.")
                     else:
                         print(f"  -> Posted YouTube streams but failed to update mapping.")
                         mapping_updated = True  # Still mark as updated to prevent retries
                 except Exception as e:
                     print(f"[ERROR] Failed to update mapping for YouTube streams: {e}")
                     mapping_updated = True
             else:
                 print(f"[ERROR] Could not find call series for updating YouTube streams status")
                 mapping_updated = True  # Still mark as updated to prevent retries

         except Exception as e:
             print(f"[ERROR] Error posting YouTube streams to Discourse: {e}")
    elif streams_posted:
         print(f"  -> YouTube stream links already posted to Discourse.")
    elif not occurrence_youtube_streams:
         print(f"  -> No YouTube stream links found for this occurrence to post.")
    elif not discourse_topic_id:
         print(f"  -> Cannot post stream links: No Discourse topic ID.")

    return mapping_updated

def process_recordings(mapping):
    """Check each meeting in mapping for recordings, then process transcripts/Discourse posts."""
    print("Checking each meeting in mapping for recordings...")

    all_recordings = []
    mapping_updated = False

    for series_name, series_data in mapping.items():
        meeting_id = series_data.get('meeting_id')

        if not meeting_id or meeting_id.startswith('placeholder'):
            continue

        print(f"🔍 Checking {series_name.upper()} (Meeting ID: {meeting_id})")

        try:
            # Use the new unified recording finder
            series_recordings = find_matching_recordings(meeting_id, series_name)

            if not series_recordings:
                print(f"   ⚪ No valid recordings found (duration >10 min with transcript)")
                continue

            print(f"   🔍 Found {len(series_recordings)} valid recording(s)")

            # Add all recordings from this series to the main list
            all_recordings.extend(series_recordings)

            # Log details for each recording
            for recording in series_recordings:
                # Parse date for logging
                try:
                    start_dt = datetime.fromisoformat(recording['start_time'].replace('Z', '+00:00'))
                    instance_date = start_dt.strftime('%Y-%m-%d')
                except:
                    instance_date = 'Unknown'

                print(f"   ✅ Added recording: {instance_date}, {recording['duration']} min, {len(recording['recording_files'])} files")

        except Exception as e:
            print(f"   ❌ Error checking {series_name}: {e}")
            continue

    if not all_recordings:
        print("No recordings found for any meetings in mapping.")
        return

    print(f"Found {len(all_recordings)} meetings with recordings to check.")

    for recording in all_recordings:
        # --- Check Recording Duration ---
        recording_duration = recording.get('duration', 0)
        if recording_duration < 10:
            print(f"[INFO] Skipping recording (Topic: {recording.get('topic', 'N/A')}, Start: {recording.get('start_time', 'N/A')}) - Duration ({recording_duration} min) is less than 10 minutes.")
            continue

        recording_meeting_id = str(recording.get("id"))
        recording_start_time_str = recording.get("start_time")
        recording_uuid = recording.get("uuid")

        if not recording_meeting_id or not recording_start_time_str or not recording_uuid:
            print(f"[WARN] Skipping recording with missing ID, start_time, or UUID: {recording.get('topic')}")
            continue

        # Get the series entry from mapping using new helper function
        series_entry = find_meeting_by_id(recording_meeting_id, mapping)
        if not series_entry:
            print(f"[INFO] No mapping entry found for meeting ID {recording_meeting_id}. Skipping recording processing.")
            continue

        # All series now use the unified structure with occurrences
        occurrences = series_entry.get("occurrences", [])
        matched_occurrence, occurrence_index = find_matching_occurrence(occurrences, recording_start_time_str)

        if matched_occurrence is None:
            print(f"[INFO] Could not match recording ({recording.get('topic', 'N/A')} at {recording_start_time_str}) to any occurrence for meeting ID {recording_meeting_id}.")
            continue

        # Call the refactored processing function
        updated = process_single_occurrence(
            recording=recording,
            occurrence=matched_occurrence,
            occurrence_index=occurrence_index,
            series_entry=series_entry,
            mapping=mapping,
            force_process=False # Pass the specific instance UUID
        )
        if updated:
            mapping_updated = True # Mark that some change occurred in the loop

    # Save and commit mapping if any changes were made during the loop
    if mapping_updated:
        print("Saving updated mapping file...")
        save_meeting_topic_mapping(mapping)
    else:
        print("No mapping changes to commit.")

def main():
    parser = argparse.ArgumentParser(description="Poll Zoom for recordings and post transcripts to Discourse.")
    parser.add_argument("--force_meeting_id", required=False, help="Force processing of a specific Zoom meeting ID")
    parser.add_argument("--force_issue_number", required=False, type=int, help="Force processing for a specific occurrence identified by issue number (requires --force_meeting_id)")
    args = parser.parse_args()

    def notify_failure(prefix: str, err: Exception):
        try:
            import requests as _req
            status = None
            reason = None
            body = None
            tracking_id = None
            if isinstance(err, _req.HTTPError) and err.response is not None:
                status = err.response.status_code
                reason = err.response.reason
                body = err.response.text[:400] if err.response.text else None
                tracking_id = err.response.headers.get("X-Zm-Trackingid") or err.response.headers.get("X-Tracking-Id")
            details = [
                f"Error: {type(err).__name__}: {str(err)[:300]}",
            ]
            if status is not None:
                details.append(f"\nHTTP: {status} {reason}")
            if tracking_id:
                details.append(f"\nTracking-ID: {tracking_id}")
            if body:
                details.append(f"\nBody: {body}")
            message = (
                f"⚠️ Zoom Transcript Poller failure\n\n{prefix}\n" + "\n".join(details)
            )
            tg.send_message(message)
        except Exception as _e:
            print(f"[WARN] Failed to send Telegram failure message: {_e}")

    try:
        mapping = load_meeting_topic_mapping()

        if args.force_meeting_id:
            meeting_id = validate_meeting_id(args.force_meeting_id)
            if meeting_id:
                print(f"Attempting forced processing for meeting {meeting_id}")
                # Use the new helper function to find the meeting entry
                series_entry = find_meeting_by_id(meeting_id, mapping)
                if not series_entry:
                    print(f"::error::Meeting ID {meeting_id} not found in mapping.")
                    return

                if args.force_issue_number:
                    occurrence_issue_number = args.force_issue_number
                    print(f"Searching for occurrence with Issue Number: {occurrence_issue_number}")

                    # All series now use the unified structure with occurrences
                    target_occurrence = None
                    occurrence_index = -1
                    for idx, occ in enumerate(series_entry["occurrences"]):
                        if occ.get("issue_number") == occurrence_issue_number:
                            target_occurrence = occ
                            occurrence_index = idx
                            break

                    if not target_occurrence:
                        print(f"::error::Issue number {occurrence_issue_number} not found for meeting ID {meeting_id}.")
                        return

                    print(f"Found occurrence: {target_occurrence.get('issue_title', 'N/A')}")
                    occurrence_start_time_str = target_occurrence.get("start_time")
                    if not occurrence_start_time_str:
                        print(f"::error::Target occurrence {occurrence_issue_number} is missing 'start_time'. Cannot match recording.")
                        return

                    # Extract date from occurrence start time for exact matching
                    try:
                        from datetime import datetime
                        occurrence_dt = datetime.fromisoformat(occurrence_start_time_str.replace('Z', '+00:00'))
                        target_date = occurrence_dt.strftime('%Y-%m-%d')
                        print(f"Target date for recording search: {target_date}")
                    except:
                        print("Warning: Could not parse occurrence start time, searching without date filter")
                        target_date = None

                    # Use the same unified recording finder as regular mode
                    print("Fetching Zoom recordings to find exact match...")
                    target_start_time = datetime.fromisoformat(occurrence_start_time_str.replace('Z', '+00:00'))
                    recordings = find_matching_recordings(meeting_id, target_start_time=target_start_time, tolerance_minutes=30)

                    if not recordings:
                        print("::error::No valid recordings found for this occurrence on Zoom.")
                        print(f"Searched for recordings matching occurrence time: {occurrence_start_time_str}")
                        return

                    print(f"Found {len(recordings)} matching recording(s)")

                    # Use the first (and likely only) recording that matched our search
                    if len(recordings) > 1:
                        print(f"Warning: Found {len(recordings)} matching recordings, using the first one")
                        for i, rec in enumerate(recordings):
                            print(f"  Recording {i+1}: {rec['duration']} min, Start: {rec['start_time']}")

                    matching_recording = recordings[0]
                    print(f"Selected recording: Topic='{matching_recording.get('topic', 'N/A')}', Duration={matching_recording.get('duration')} min, UUID='{matching_recording.get('uuid')}'")

                    # Now call the processing function with force=True
                    print(f"Forcing processing for Occurrence Issue #{occurrence_issue_number}...")

                    # All series now use the unified structure with occurrences
                    mapping_updated = process_single_occurrence(
                        recording=matching_recording,
                        occurrence=target_occurrence,
                        occurrence_index=occurrence_index,
                        series_entry=series_entry,
                        mapping=mapping,
                        force_process=True, # Enable force mode
                    )

                    if mapping_updated:
                        print("Saving updated mapping file after forced processing...")
                        save_meeting_topic_mapping(mapping)
                    else:
                        print("No mapping changes resulted from forced processing.")

                else:
                    # Keep the warning for forcing a whole series ID without issue number
                    print("[WARN] Forced processing for an entire series without polling is not supported. Specify --force_issue_number.")
                return # Exit after forced processing attempt
            else:
                print("Invalid force_meeting_id provided")
                return

        # --- Regular Polling Logic ---
        process_recordings(mapping)
    except Exception as e:
        print(f"::error::Zoom transcript poller failed: {e}")
        notify_failure("Credential or API failure during transcript polling.", e)
        # Re-raise to preserve non-zero exit for the workflow
        raise

if __name__ == "__main__":
    main()