import os
import json
import argparse
from datetime import datetime, timedelta, timezone
import pytz
from modules import zoom, transcript, youtube_utils, rss_utils, discourse
from github import Github, InputGitAuthor

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

def commit_mapping_file():
    commit_message = "Update meeting-topic mapping"
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    token = os.environ["GITHUB_TOKEN"]
    repo_name = os.environ["GITHUB_REPOSITORY"]
    g = Github(token)
    repo = g.get_repo(repo_name)
    author = InputGitAuthor(
        name="GitHub Actions Bot",
        email="actions@github.com"
    )
    file_path = MAPPING_FILE
    with open(file_path, "r") as f:
        file_content = f.read()
    try:
        contents = repo.get_contents(file_path, ref=branch)
        repo.update_file(
            path=contents.path,
            message=commit_message,
            content=file_content,
            sha=contents.sha,
            branch=branch,
            author=author,
        )
        print(f"Updated {file_path} in the repository.")
    except Exception:
        repo.create_file(
            path=file_path,
            message=commit_message,
            content=file_content,
            branch=branch,
            author=author,
        )
        print(f"Created {file_path} in the repository.")

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

def process_meeting(meeting_id, mapping):
    """Process a single meeting's recordings and transcripts"""
    entry = mapping.get(str(meeting_id)) # Ensure meeting_id is string
    if not isinstance(entry, dict):
        print(f"Skipping meeting {meeting_id} - invalid mapping entry")
        return

    # Skip if already processed
    if entry.get("transcript_processed"):
        print(f"Meeting {meeting_id} is already processed")
        return

    # Skip if max attempts reached
    if entry.get("upload_attempt_count", 0) >= 10:
        print(f"Skipping meeting {meeting_id} - max upload attempts reached")
        return
        
    # Skip if max transcript attempts reached
    if entry.get("transcript_attempt_count", 0) >= 10:
        print(f"Skipping meeting {meeting_id} - max transcript attempts reached")
        return
        
    # Skip if meeting hasn't occurred yet
    start_time = entry.get("start_time")
    if start_time:
        try:
            meeting_time = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            now = datetime.now(pytz.UTC)
            
            if meeting_time > now:
                print(f"Skipping meeting {meeting_id} - scheduled for future ({start_time})")
                return
                
            # Also skip if meeting ended less than 30 minutes ago
            duration = entry.get("duration", 60)  # Default to 60 minutes if duration not specified
            meeting_end_time = meeting_time + timedelta(minutes=duration)
            
            if now < meeting_end_time + timedelta(minutes=30):
                print(f"Skipping meeting {meeting_id} - ended less than 30 minutes ago")
                return
                
        except Exception as e:
            print(f"Error parsing meeting time {start_time}: {e}")
            # Continue processing if we can't parse the time

    try:
        # For recurring meetings, we don't need to upload to YouTube
        is_recurring = entry.get("is_recurring", False)
        if is_recurring:
            print(f"Skipping YouTube upload for recurring meeting {meeting_id}")
            # Mark as processed to avoid future attempts
            entry["skip_youtube_upload"] = True
            entry["Youtube_upload_processed"] = True
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
        # Only attempt upload for non-recurring meetings that haven't been processed
        elif not entry.get("Youtube_upload_processed") and not entry.get("skip_youtube_upload", False):
            # Import directly from package path rather than relative path
            import sys
            import os
            script_dir = os.path.dirname(os.path.abspath(__file__))
            sys.path.append(os.path.dirname(script_dir))
            from scripts.upload_zoom_recording import upload_recording
            upload_recording(meeting_id)

        # Process transcript regardless of meeting type
        discourse_topic_id = entry.get("discourse_topic_id")
        if discourse_topic_id:
            transcript.post_zoom_transcript_to_discourse(meeting_id)
            entry["transcript_processed"] = True
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
            
            # Update RSS feed with transcript info
            try:
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    "transcript_posted",
                    "Meeting transcript posted to Discourse",
                    f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{discourse_topic_id}"
                )
                print(f"Updated RSS feed with transcript info for meeting {meeting_id}")
            except Exception as e:
                print(f"Failed to update RSS feed: {e}")

            # Post YouTube stream links if they exist and haven't been posted by this script yet
            if "youtube_streams" in entry and not entry.get("youtube_streams_posted_to_discourse"):
                youtube_streams = entry["youtube_streams"]
                if youtube_streams:
                    print(f"Posting existing YouTube streams to Discourse topic {discourse_topic_id}")
                    stream_links_text = "\n".join([
                        f"- Stream {i+1}: {stream.get('stream_url', 'URL not found')}" 
                        for i, stream in enumerate(youtube_streams)
                    ])
                    discourse_body = f"**Previously Generated YouTube Stream Links:**\n{stream_links_text}"
                    try:
                        discourse.create_post(
                            topic_id=discourse_topic_id,
                            body=discourse_body
                        )
                        entry["youtube_streams_posted_to_discourse"] = True
                        print(f"Successfully posted YouTube streams to Discourse topic {discourse_topic_id}")
                        # Save mapping after successful post
                        save_meeting_topic_mapping(mapping)
                        commit_mapping_file()
                    except Exception as e:
                        print(f"Error posting YouTube streams to Discourse topic {discourse_topic_id}: {e}")

    except Exception as e:
        # Increment attempt counter on failure
        entry["transcript_attempt_count"] = entry.get("transcript_attempt_count", 0) + 1
        print(f"Transcript attempt {entry['transcript_attempt_count']} of 10 failed for meeting {meeting_id}")
        save_meeting_topic_mapping(mapping)
        commit_mapping_file()
        print(f"Error processing meeting {meeting_id}: {e}")

def find_matching_occurrence(occurrences, recording_start_time_str, tolerance_minutes=5):
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
    recording_meeting_id = str(recording.get("id"))
    occurrence_issue_number = occurrence.get("issue_number")
    print(f"Processing transcript for Specific Recording of Meeting ID {recording_meeting_id}, Occurrence Issue #{occurrence_issue_number}")

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
    # ADDED: Check if transcript processing should be skipped based on flag from handle_issue
    should_skip_transcript = occurrence.get("skip_transcript_processing", False)
    
    # Allow forced processing even if attempts > 10 or skip flag is set
    can_attempt_transcript = (not transcript_processed and 
                           (force_process or (not should_skip_transcript and transcript_attempts < 10)) and 
                           discourse_topic_id)
    
    # ADDED: Log reason if skipping due to the new flag
    if should_skip_transcript and not force_process:
        print(f"  -> Skipping transcript posting: External Zoom ID indicated (skip_transcript_processing=True).")

    if can_attempt_transcript:
        attempt_number = transcript_attempts + 1
        print(f"  -> Attempting transcript posting (Attempt {attempt_number})...")
        try:
            # Pass the specific recording data object instead of just the series ID
            transcript_success = transcript.post_zoom_transcript_to_discourse(
                recording_data=recording,
                occurrence_details=occurrence
            )

            if transcript_success:
                mapping[recording_meeting_id]["occurrences"][occurrence_index]["transcript_processed"] = True
                # Reset attempt count on success
                mapping[recording_meeting_id]["occurrences"][occurrence_index]["transcript_attempt_count"] = 0
                mapping_updated = True
                print(f"  -> Transcript posted successfully for occurrence #{occurrence_issue_number} to topic {discourse_topic_id}.")

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
                 if not force_process:
                    mapping[recording_meeting_id]["occurrences"][occurrence_index]["transcript_attempt_count"] = transcript_attempts + 1
                 mapping_updated = True
                 print(f"  -> Transcript posting failed.")

        except Exception as e:
            # Increment attempt counter only if not forced
            if not force_process:
                mapping[recording_meeting_id]["occurrences"][occurrence_index]["transcript_attempt_count"] = transcript_attempts + 1
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
             mapping[recording_meeting_id]["occurrences"][occurrence_index]["youtube_streams_posted_to_discourse"] = True
             mapping_updated = True
             print(f"  -> Successfully posted YouTube streams to Discourse.")
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
    """Fetch recent recordings, match to occurrences, and process transcripts/Discourse posts."""
    print("Fetching recent Zoom recordings...")
    recordings = zoom.get_recordings_list()
    if not recordings:
        print("No recent recordings found on Zoom.")
        return

    print(f"Found {len(recordings)} recordings to check.")
    mapping_updated = False

    for recording in recordings:
        recording_meeting_id = str(recording.get("id"))
        recording_start_time_str = recording.get("start_time")

        if not recording_meeting_id or not recording_start_time_str:
            print(f"[WARN] Skipping recording with missing ID or start_time: {recording.get('topic')}")
            continue

        # Get the series entry from mapping
        series_entry = mapping.get(recording_meeting_id)
        if not isinstance(series_entry, dict) or "occurrences" not in series_entry:
            print(f"[INFO] No mapping entry or occurrences found for meeting ID {recording_meeting_id}. Skipping recording processing.")
            continue

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
            force_process=False # Not forced in regular polling
        )
        if updated:
            mapping_updated = True # Mark that some change occurred in the loop

    # Save and commit mapping if any changes were made during the loop
    if mapping_updated:
        print("Saving updated mapping file...")
        save_meeting_topic_mapping(mapping)
        try:
            commit_mapping_file()
        except Exception as e:
            print(f"::error::Failed to commit mapping file: {e}")
    else:
        print("No mapping changes to commit.")

def main():
    parser = argparse.ArgumentParser(description="Poll Zoom for recordings and post transcripts to Discourse.")
    parser.add_argument("--force_meeting_id", required=False, help="Force processing of a specific Zoom meeting ID")
    parser.add_argument("--force_issue_number", required=False, type=str, help="Force processing for a specific occurrence identified by issue number (requires --force_meeting_id)")
    args = parser.parse_args()

    mapping = load_meeting_topic_mapping()

    # Handle forced processing only if force_meeting_id is provided
    if args.force_meeting_id:
        meeting_id = validate_meeting_id(args.force_meeting_id)
        if not meeting_id:
             print("Invalid force_meeting_id provided")
             return

        print(f"Attempting forced processing for meeting {meeting_id}")
        series_entry = mapping.get(meeting_id)
        if not series_entry or "occurrences" not in series_entry:
            print(f"::error::Meeting ID {meeting_id} not found in mapping or has no occurrences.")
            return

        # Now check force_issue_number
        if args.force_issue_number:
            try:
                # Attempt to convert the string argument to an integer
                occurrence_issue_number = int(args.force_issue_number)
            except ValueError:
                print(f"::error::Invalid integer value provided for --force_issue_number: '{args.force_issue_number}'")
                return
            except TypeError:
                 print(f"::error::--force_issue_number must be provided when --force_meeting_id is used for forced processing.")
                 return
            
            # --- Existing logic to find and process the specific occurrence ---
            print(f"Searching for occurrence with Issue Number: {occurrence_issue_number}")
            # Find the specific occurrence and its index
            target_occurrence = None
            occurrence_index = -1
            for idx, occ in enumerate(series_entry["occurrences"]):
                if occ.get("issue_number") == occurrence_issue_number:
                    target_occurrence = occ
                    occurrence_index = idx
                    break

            if not target_occurrence:
                print(f"::error::Issue number {occurrence_issue_number} not found within occurrences for meeting ID {meeting_id}.")
                return

            print(f"Found occurrence: {target_occurrence.get('issue_title', 'N/A')}")
            occurrence_start_time_str = target_occurrence.get("start_time")
            if not occurrence_start_time_str:
                print(f"::error::Target occurrence {occurrence_issue_number} is missing 'start_time'. Cannot match recording.")
                return

            # Fetch recordings and find the matching one
            print("Fetching Zoom recordings to find match...")
            # Calculate date range for fetching recordings based on occurrence start time
            try:
                target_start_dt = datetime.fromisoformat(occurrence_start_time_str.replace('Z', '+00:00'))
                # Fetch recordings for the specific day of the occurrence
                fetch_date_str = target_start_dt.strftime("%Y-%m-%d") 
                print(f"Fetching recordings specifically for date: {fetch_date_str}")
                # Pass the specific date to get_recordings_list
                recordings = zoom.get_recordings_list(from_date=fetch_date_str, to_date=fetch_date_str)
                # Add logging for fetched recordings
                print(f"[DEBUG] Fetched {len(recordings)} recordings for {fetch_date_str}. Checking for match...")
                if recordings: # Log details only if recordings were found
                    for i, rec in enumerate(recordings):
                        print(f"  [DEBUG] Rec {i+1}: ID={rec.get('id')}, Topic='{rec.get('topic')}', Start='{rec.get('start_time')}'")

            except ValueError:
                # Handle error parsing the occurrence date string itself
                print(f"::error::Invalid start_time format in target occurrence: {occurrence_start_time_str}")
                return
            except Exception as e:
                # Handle errors during the API call
                print(f"::error::Failed to fetch recordings from Zoom: {e}")
                return # Stop if we can't fetch recordings
            
            if not recordings:
                # Use a more specific error message if fetching for the specific date returned nothing
                print(f"::error::No recordings found on Zoom for the date {fetch_date_str} to match against.")
                return

            matching_recording = None
            try:
                # We need the target occurrence start time to find the recording
                target_start_time = datetime.fromisoformat(occurrence_start_time_str.replace('Z', '+00:00'))
                tolerance = timedelta(minutes=15) # Allow larger tolerance for matching

                for recording in recordings:
                    # First check if the recording's meeting ID matches
                    if str(recording.get("id")) != meeting_id:
                        continue
                    # Then check the start time
                    rec_start_str = recording.get("start_time")
                    if not rec_start_str:
                        continue
                    try:
                        rec_start_time = datetime.fromisoformat(rec_start_str.replace('Z', '+00:00'))
                        if abs(rec_start_time - target_start_time) <= tolerance:
                            matching_recording = recording
                            print(f"Found matching Zoom recording: Topic='{recording.get('topic', 'N/A')}', Start='{rec_start_str}'")
                            break # Found the one we need
                    except ValueError:
                        print(f"[WARN] Invalid start_time format in recording: {rec_start_str}")
                        continue

            except ValueError:
                print(f"::error::Invalid start_time format in target occurrence: {occurrence_start_time_str}")
                return

            if not matching_recording:
                print(f"::error::Could not find a matching Zoom recording for Meeting ID {meeting_id}, Occurrence Issue #{occurrence_issue_number} (start time: {occurrence_start_time_str}).")
                print("Check if the recording exists in Zoom and its start time matches the mapping.")
                return

            # Now call the processing function with force=True
            print(f"Forcing processing for Occurrence Issue #{occurrence_issue_number}...")
            mapping_updated = process_single_occurrence(
                recording=matching_recording,
                occurrence=target_occurrence,
                occurrence_index=occurrence_index,
                series_entry=series_entry,
                mapping=mapping,
                force_process=True # Enable force mode
            )

            if mapping_updated:
                print("Saving updated mapping file after forced processing...")
                save_meeting_topic_mapping(mapping)
                try:
                    commit_mapping_file()
                except Exception as e:
                    print(f"::error::Failed to commit mapping file after forced run: {e}")
            else:
                print("No mapping changes resulted from forced processing.")
            # --- End of specific occurrence processing ---

        else:
            # Case: force_meeting_id provided, but force_issue_number is missing/empty
            print("[WARN] Forced processing requires both --force_meeting_id and a valid --force_issue_number.")
        
        # Exit after attempting forced processing (whether successful or not)
        return 

    # --- Regular Polling Logic (only runs if force_meeting_id was NOT provided) ---
    print("Starting regular polling process...")
    process_recordings(mapping)

if __name__ == "__main__":
    main()
