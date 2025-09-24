import os
import time
import tempfile
import requests
import argparse
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from modules import zoom, transcript, discourse, tg
from modules.youtube_utils import add_video_to_appropriate_playlist
from modules.mapping_utils import (
    load_mapping as load_meeting_topic_mapping,
    save_mapping as save_meeting_topic_mapping,
    find_meeting_by_id,
    find_meeting_by_issue_number,
    find_call_series_by_meeting_id,
    find_occurrence_with_index,
)
from google.auth.transport.requests import Request
import json
import subprocess
from modules.zoom import (
    get_meeting_recording,
    get_access_token,
    get_meeting_summary
)
from google.oauth2 import service_account
from datetime import datetime, timezone, timedelta

# Import RSS utils
try:
    from modules import rss_utils
except ImportError:
    rss_utils = None

# Reuse existing zoom module functions
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube"
]
CLIENT_SECRETS_FILE = "client_secrets.json"

# Add these functions at the top of the file
MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def get_authenticated_service():
    # Initialize credentials from environment variables
    creds = Credentials(
        token=None,
        refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
        client_id=os.environ["GOOGLE_CLIENT_ID"],
        client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
        scopes=SCOPES
    )

    # Token already refreshed at workflow start
    return build("youtube", "v3", credentials=creds)

def video_exists(youtube, meeting_id):
    """Check if video for this meeting ID already exists in mapping"""
    mapping = load_meeting_topic_mapping()
    # Use the new helper function to find the meeting entry
    entry = find_meeting_by_id(str(meeting_id), mapping)
    if not entry:
        return False
    video_id = entry.get("youtube_video_id")
    if video_id is None or str(video_id).lower() in ("none", "null", ""):
        return False
    return True

def find_best_youtube_recording(meeting_id, min_duration_minutes=10):
    """Find the best recording for YouTube upload, checking all instances if needed."""

    # First try direct lookup (for backwards compatibility)
    try:
        recording_info = get_meeting_recording(meeting_id)
        if recording_info and recording_info.get('recording_files'):
            duration = recording_info.get('duration', 0)
            if duration >= min_duration_minutes:
                print(f"[INFO] Found recording via direct lookup: {duration} minutes")
                return recording_info
            else:
                print(f"[WARN] Direct lookup recording too short: {duration} minutes")
    except Exception as e:
        print(f"[WARN] Direct lookup failed: {e}")

    # If direct lookup fails or returns short recording, check all instances
    print(f"[INFO] Checking all meeting instances for meeting {meeting_id}...")
    try:
        instances = zoom.get_past_meeting_instances(meeting_id)
        if not instances:
            print(f"[ERROR] No past meeting instances found for meeting {meeting_id}")
            return None

        print(f"[INFO] Found {len(instances)} past meeting instances")

        valid_recordings = []

        for i, instance in enumerate(instances):
            uuid = instance.get('uuid')
            start_time = instance.get('start_time', 'N/A')

            if not uuid:
                continue

            print(f"[INFO] Checking instance {i+1}: {start_time} (UUID: {uuid})")

            try:
                recording_data = get_meeting_recording(uuid)
                if recording_data and recording_data.get('recording_files'):
                    duration = recording_data.get('duration', 0)
                    recording_files = recording_data.get('recording_files', [])
                    mp4_files = [f for f in recording_files if f.get('file_type') == 'MP4']

                    print(f"[INFO]   Duration: {duration} minutes, MP4 files: {len(mp4_files)}")

                    if duration >= min_duration_minutes and mp4_files:
                        valid_recordings.append({
                            'data': recording_data,
                            'duration': duration,
                            'uuid': uuid,
                            'start_time': start_time
                        })
                        print(f"[INFO]   ✅ Valid recording candidate: {duration} minutes")
                    else:
                        print(f"[INFO]   ⚠️  Skipped: {duration} minutes, {len(mp4_files)} MP4 files")
                else:
                    print(f"[INFO]   ❌ No recording data found")
            except Exception as e:
                print(f"[WARN]   Error checking instance {uuid}: {e}")

        if not valid_recordings:
            print(f"[ERROR] No valid recordings found with duration >= {min_duration_minutes} minutes")
            return None

        # Sort by duration (longest first) and return the best
        valid_recordings.sort(key=lambda x: x['duration'], reverse=True)
        best_recording = valid_recordings[0]

        print(f"[INFO] Selected best recording: {best_recording['duration']} minutes from {best_recording['start_time']}")
        return best_recording['data']

    except Exception as e:
        print(f"[ERROR] Failed to check meeting instances: {e}")
        return None

def download_zoom_recording(meeting_id, min_duration_minutes=10):
    """Download Zoom recording MP4 file to temp location"""
    recording_info = find_best_youtube_recording(meeting_id, min_duration_minutes)

    if not recording_info or 'recording_files' not in recording_info:
        return None

    # Define video quality priority
    video_recording_types_priority = [
        "shared_screen_with_speaker_view",
        "shared_screen_with_gallery_view",
        "speaker_view",
        "gallery_view",
        "shared_screen"
    ]

    best_video_file = None

    # Try each priority level until we find a video
    for preferred_type in video_recording_types_priority:
        for file in recording_info['recording_files']:
            if (file.get('file_type') == 'MP4' and
                file.get('download_url') and
                file.get('recording_type') == preferred_type):
                best_video_file = file
                print(f"[DEBUG] Selected priority video: {preferred_type}")
                break
        if best_video_file:
            break

    # Fallback: If no prioritized video found, use any MP4
    if best_video_file is None:
        for file in recording_info['recording_files']:
            if file.get('file_type') == 'MP4' and file.get('download_url'):
                best_video_file = file
                print(f"[DEBUG] Using fallback video type: {file.get('recording_type', 'unknown')}")
                break

    if best_video_file is None:
        print(f"[ERROR] No MP4 video files with download URLs found for meeting {meeting_id}")
        return None

    download_url = best_video_file['download_url']
    recording_type = best_video_file.get('recording_type', 'unknown')
    file_size = best_video_file.get('file_size', 'unknown')

    print(f"[INFO] Downloading video: type={recording_type}, size={file_size}")

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }

    response = requests.get(download_url, headers=headers, stream=True)
    if response.status_code == 200:
        for chunk in response.iter_content(chunk_size=1024*1024):
            if chunk:
                temp_file.write(chunk)
        temp_file.close()
        print(f"[SUCCESS] Downloaded video to: {temp_file.name}")
        return temp_file.name
    else:
        print(f"[ERROR] Failed to download video: HTTP {response.status_code}")
        temp_file.close()
        os.unlink(temp_file.name)  # Clean up failed download
        return None

def upload_recording(meeting_id, occurrence_issue_number=None, error_collector=None):
    """Uploads Zoom recording to YouTube for a specific occurrence."""

    # Ensure meeting_id is a string
    meeting_id = str(meeting_id)

    youtube = get_authenticated_service()
    mapping = load_meeting_topic_mapping()

    series_entry = find_meeting_by_id(meeting_id, mapping)

    if not series_entry:
        print(f"[ERROR] Meeting ID {meeting_id} not found in mapping.")
        error_msg = f"❌ YouTube upload aborted: Unknown meeting_id {meeting_id} in mapping."
        if error_collector is not None:
            error_collector.append(error_msg)
        else:
            tg.send_message(error_msg)
        return False # Indicate failure

    # Find the specific occurrence
    if occurrence_issue_number is None:
        # Try to find the most recent occurrence if not specified (best effort)
        if series_entry.get("occurrences"):
            matched_occurrence = series_entry["occurrences"][-1] # Assume last is latest
            occurrence_index = len(series_entry["occurrences"]) - 1
            occurrence_issue_number = matched_occurrence.get("issue_number", "[Unknown]")
            print(f"[WARN] occurrence_issue_number not provided, attempting upload for latest occurrence: Issue #{occurrence_issue_number}")
        else:
            print(f"[ERROR] No occurrences found for meeting {meeting_id} and occurrence_issue_number not specified.")
            return False
    else:
        # Resolve call series key from meeting_id, then locate the occurrence within mapping
        call_series_key = find_call_series_by_meeting_id(meeting_id, occurrence_issue_number, mapping)
        if not call_series_key:
            print(f"[ERROR] Could not find call series for meeting {meeting_id}")
            return False
        matched_occurrence, occurrence_index = find_occurrence_with_index(call_series_key, occurrence_issue_number, mapping)

    if matched_occurrence is None:
        print(f"[ERROR] Occurrence with issue number {occurrence_issue_number} not found for meeting ID {meeting_id}.")
        error_msg = f"❌ YouTube upload aborted: Occurrence #{occurrence_issue_number} not found for meeting {meeting_id}."
        if error_collector is not None:
            error_collector.append(error_msg)
        else:
            tg.send_message(error_msg)
        return False # Indicate failure

    # --- Use occurrence-specific data ---
    print(f"Processing YouTube upload for Meeting ID {meeting_id}, Occurrence Issue #{occurrence_issue_number}")

    # Check if this occurrence should skip YouTube upload
    if matched_occurrence.get("skip_youtube_upload", False):
        print(f"  -> Skipping: Occurrence marked as skip_youtube_upload.")
        # Mark as processed anyway so we don't retry?
        # mapping[meeting_id]["occurrences"][occurrence_index]["youtube_upload_processed"] = True # Or leave as is?
        # save_meeting_topic_mapping(mapping) # No commit here, let poll script handle batch commit
        return True # Indicate already processed

    # Check attempt counter within the occurrence
    attempt_count = matched_occurrence.get("upload_attempt_count", 0)
    if attempt_count >= 10:
        print(f"  -> Skipping: Max upload attempts reached for occurrence.")
        return False # Indicate failure

    # Find the series key for this meeting ID
    call_series_key = find_call_series_by_meeting_id(meeting_id, occurrence_issue_number, mapping)
    if not call_series_key:
        print(f"[ERROR] Could not find call series for meeting {meeting_id}")
        return False

    # Increment attempt count immediately
    mapping[call_series_key]["occurrences"][occurrence_index]["upload_attempt_count"] = attempt_count + 1
    save_meeting_topic_mapping(mapping) # Save attempt count increment

    # Only proceed if not already processed
    if matched_occurrence.get("youtube_upload_processed"):
        print(f"  -> Skipping: YouTube upload already processed for occurrence.")
        return True # Indicate already processed

    video_title = matched_occurrence.get("issue_title", f"Meeting {meeting_id} - Issue {occurrence_issue_number}")
    video_description = (
        f"Recording of {video_title}\n\n"
        f"Original Zoom Meeting ID: {meeting_id}"
        f"\nGitHub Issue: https://github.com/{os.environ.get('GITHUB_REPOSITORY', '')}/issues/{occurrence_issue_number}" # Add link to specific issue
    )

    # Check recording duration before downloading
    try:
        recording_info = find_best_youtube_recording(meeting_id, min_duration_minutes=10)
        if not recording_info:
            print(f"[SKIP] No recording found with minimum 10 minutes duration")
            error_msg = f"⏭️ YouTube upload skipped: No recording found for meeting {meeting_id} (issue #{occurrence_issue_number}) with minimum 10 minutes duration."
            if error_collector is not None:
                error_collector.append(error_msg)
            else:
                tg.send_message(error_msg)
            return False # Indicate failure - no suitable recording found
        else:
            recording_duration = recording_info.get('duration', 0)
            print(f"[INFO] Found suitable recording: {recording_duration} minutes")
    except Exception as e:
        print(f"[WARN] Could not check recording duration for meeting {meeting_id}: {e}")
        # Continue with download attempt if we can't check duration

    video_path = download_zoom_recording(meeting_id)
    if not video_path:
        print(f"No MP4 recording available for meeting {meeting_id}")
        error_msg = f"❌ YouTube upload skipped: No MP4 recording available for meeting {meeting_id} (issue #{occurrence_issue_number})."
        if error_collector is not None:
            error_collector.append(error_msg)
        else:
            tg.send_message(error_msg)
        return False # Indicate failure

    try:
        title = video_title
        description = video_description

        request_body = {
            'snippet': {
                'title': title,
                'description': description,
                'categoryId': '28'
            },
            'status': {
                'privacyStatus': 'public',
            }
        }

        media = googleapiclient.http.MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        ).execute()

        # --- Update occurrence flags in mapping ---
        mapping[call_series_key]["occurrences"][occurrence_index]["youtube_video_id"] = response['id']
        mapping[call_series_key]["occurrences"][occurrence_index]["youtube_upload_processed"] = True
        # Reset attempt count on success
        # mapping[call_series_key]["occurrences"][occurrence_index]["upload_attempt_count"] = 0 # Optional reset

        save_meeting_topic_mapping(mapping)

        youtube_link = f"https://youtu.be/{response['id']}"
        print(f"Uploaded YouTube video: {youtube_link}")

        # Add video to appropriate playlist; must be done after upload is successful
        call_series = series_entry.get("call_series")
        if call_series:
            print(f"[DEBUG] Adding video {response['id']} to playlist(s) for call_series: {call_series}")
            playlist_results = add_video_to_appropriate_playlist(response['id'], call_series)
            if playlist_results:
                print(f"[INFO] Successfully added video to {len(playlist_results)} playlist(s) for {call_series}")
            else:
                print(f"[WARN] Failed to add video to any playlist for {call_series}")
        else:
            print(f"[WARN] No call_series found for meeting {meeting_id}, skipping playlist assignment")

        # Post to Discourse (if applicable)
        discourse_topic_id = matched_occurrence.get("discourse_topic_id")
        if discourse_topic_id:
            post_body = f"YouTube recording available: {youtube_link}"

            discourse.create_post(
                topic_id=discourse_topic_id,
                body=post_body # Use the simplified body
            )

        # --- Update RSS feed for this occurrence ---
        if rss_utils:
            try:
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    occurrence_issue_number, # Pass issue number to identify occurrence
                    "youtube_upload",
                    f"Meeting recording uploaded: {video_title}",
                    youtube_link
                )
                print(f"Updated RSS feed with YouTube video for occurrence #{occurrence_issue_number}")
            except Exception as e:
                print(f"Failed to update RSS feed: {e}")

        # Send Telegram notification similar to handle_issue
        try:
            # Find the specific occurrence to get the telegram message ID
            occurrence_telegram_message_id = matched_occurrence.get("telegram_message_id")

            telegram_message = (
                f"✅ YouTube Upload Successful!\n\n"
                f"Title: {video_title}\n"
                f"URL: {youtube_link}"
            )
            # Reply to the original occurrence announcement if possible
            if occurrence_telegram_message_id:
                tg.send_message(telegram_message, reply_to_message_id=occurrence_telegram_message_id)
            else:
                tg.send_message(telegram_message)
            print("Telegram notification sent for YouTube upload.")
        except Exception as e:
            print(f"Error sending Telegram message for YouTube upload: {e}")

        return True # Indicate success
    except HttpError as e:
        print(f"YouTube API error: {e}")
        err_text = getattr(e, 'content', None) or str(e)
        error_msg = f"❌ YouTube upload failed for meeting {meeting_id} (issue #{occurrence_issue_number}).\nError: {err_text}"
        if error_collector is not None:
            error_collector.append(error_msg)
        else:
            tg.send_message(error_msg)
        return False # Indicate failure
    finally:
        os.unlink(video_path)  # Clean up temp file

def main():
    parser = argparse.ArgumentParser(description="Upload Zoom recording to YouTube")
    parser.add_argument("--meeting_id", required=False, help="Zoom meeting ID to process")
    parser.add_argument("--occurrence_issue_number", required=False, type=int, help="Issue number of the specific occurrence to upload (requires --meeting_id)")
    args = parser.parse_args()

    # Handle case where specific occurrence is provided
    if args.meeting_id and args.occurrence_issue_number:
        print(f"Attempting upload for specific occurrence: Meeting ID {args.meeting_id}, Issue #{args.occurrence_issue_number}")
        try:
            upload_recording(args.meeting_id, args.occurrence_issue_number)
        except Exception as e:
            print(f"Failed to process specific occurrence {args.meeting_id} / {args.occurrence_issue_number}: {e}")
        return # Exit after processing specific occurrence

    # Handle case where only meeting_id is provided (legacy or manual run?)
    if args.meeting_id and not args.occurrence_issue_number:
        print(f"[WARN] Only --meeting_id provided. Attempting upload for the LATEST occurrence of {args.meeting_id}.")
        try:
            upload_recording(args.meeting_id) # Will try latest occurrence by default
        except Exception as e:
            print(f"Failed to process latest occurrence for {args.meeting_id}: {e}")
        return

    # Handle case where NO arguments are provided (check mapping)
    if not args.meeting_id and not args.occurrence_issue_number:
        print("No meeting ID provided - checking mapping for unprocessed meetings")
        mapping = load_meeting_topic_mapping()

        # Collect all errors to send as a single aggregated message
        error_messages = []
        success_count = 0
        processed_count = 0

        for _, series_data in mapping.items():
            if "occurrences" in series_data:
                for occurrence in series_data["occurrences"]:
                    occ_issue_num = occurrence.get("issue_number")
                    yt_processed = occurrence.get("youtube_upload_processed", False)
                    yt_skipped = occurrence.get("skip_youtube_upload", False)

                    # Get the effective meeting ID for this occurrence (series-level)
                    effective_meeting_id = str(series_data.get("meeting_id", "")).strip()

                    # Skip if meeting_id isn't a real Zoom ID yet
                    if not effective_meeting_id or effective_meeting_id.lower() in ("pending", "custom") or effective_meeting_id.startswith("placeholder"):
                        continue

                    # Date validation to prevent uploading videos for future meetings
                    meeting_start_time_str = occurrence.get("start_time")
                    if meeting_start_time_str:
                        try:
                            # Parse the meeting start time
                            meeting_start_time = datetime.fromisoformat(meeting_start_time_str.replace('Z', '+00:00'))
                            current_time = datetime.now(timezone.utc)

                            # Only process meetings that ended at least 15 minutes ago to ensure recording is available
                            meeting_duration = occurrence.get("duration", 60)  # Default 60 minutes if not specified
                            meeting_end_time = meeting_start_time + timedelta(minutes=meeting_duration)
                            time_since_meeting_end = current_time - meeting_end_time

                            if current_time < meeting_start_time:
                                print(f"[SKIP] Future meeting: Issue #{occ_issue_num}, starts {meeting_start_time} (in {meeting_start_time - current_time})")
                                continue
                            elif time_since_meeting_end < timedelta(minutes=15):
                                print(f"[SKIP] Recent meeting: Issue #{occ_issue_num}, ended {time_since_meeting_end} ago (waiting for recording to be ready)")
                                continue
                            else:
                                print(f"[INFO] Meeting eligible for upload: Issue #{occ_issue_num}, ended {time_since_meeting_end} ago")
                        except (ValueError, TypeError) as e:
                            print(f"[WARN] Could not parse start_time '{meeting_start_time_str}' for issue #{occ_issue_num}: {e}")
                            # Continue processing if we can't parse the date (don't want to break existing functionality)
                    else:
                        print(f"[WARN] No start_time found for issue #{occ_issue_num}, proceeding without date validation")

                    if not yt_skipped and not yt_processed and occ_issue_num and effective_meeting_id:
                        print(f"\nProcessing occurrence from mapping: Meeting ID {effective_meeting_id}, Issue #{occ_issue_num}")
                        processed_count += 1
                        try:
                            result = upload_recording(effective_meeting_id, occ_issue_num, error_collector=error_messages)
                            if result:
                                success_count += 1
                        except Exception as e:
                            print(f"Failed to process {effective_meeting_id} / {occ_issue_num}: {e}")
                            error_messages.append(f"❌ YouTube upload failed for meeting {effective_meeting_id} (issue #{occ_issue_num}): {str(e)}")

        # Send aggregated message if there were any operations
        if processed_count > 0:
            send_aggregated_telegram_message(error_messages, success_count, processed_count)

def send_aggregated_telegram_message(error_messages, success_count, processed_count):
    """Send a single aggregated Telegram message for batch YouTube upload operations."""
    if not error_messages and success_count == 0:
        return  # Nothing to report

    # Group similar error messages
    error_groups = {}
    for error in error_messages:
        if "Unknown meeting_id" in error and "in mapping" in error:
            key = "unknown_meeting_ids"
            if key not in error_groups:
                error_groups[key] = []
            # Extract meeting ID from the error message
            meeting_id = error.split("meeting_id ")[1].split(" in mapping")[0] if "meeting_id " in error else "Unknown"
            error_groups[key].append(meeting_id)
        elif "No MP4 recording available" in error:
            key = "no_mp4_recordings"
            if key not in error_groups:
                error_groups[key] = []
            # Extract meeting ID and issue number
            if "meeting " in error and "(issue #" in error:
                meeting_part = error.split("meeting ")[1].split(" (issue #")[0]
                issue_part = error.split("(issue #")[1].split(")")[0]
                error_groups[key].append(f"{meeting_part} (issue #{issue_part})")
        elif "YouTube upload failed" in error:
            key = "upload_failures"
            if key not in error_groups:
                error_groups[key] = []
            # Extract meeting ID and issue number
            if "meeting " in error and "(issue #" in error:
                meeting_part = error.split("meeting ")[1].split(" (issue #")[0]
                issue_part = error.split("(issue #")[1].split(")")[0]
                error_groups[key].append(f"{meeting_part} (issue #{issue_part})")
        else:
            # Other errors - keep individual
            key = "other_errors"
            if key not in error_groups:
                error_groups[key] = []
            error_groups[key].append(error)

    # Build the aggregated message
    message_parts = []

    if success_count > 0 or error_messages:
        message_parts.append(f"📺 **YouTube Upload Batch Summary**")
        message_parts.append(f"Processed: {processed_count} | Successful: {success_count} | Failed: {len(error_messages)}")
        message_parts.append("")

    if error_groups:
        if "unknown_meeting_ids" in error_groups:
            count = len(error_groups["unknown_meeting_ids"])
            message_parts.append(f"❌ **Unknown meeting IDs ({count}):**")
            # Show first few, then summarize if many
            if count <= 5:
                for meeting_id in error_groups["unknown_meeting_ids"]:
                    message_parts.append(f"  • {meeting_id}")
            else:
                for meeting_id in error_groups["unknown_meeting_ids"][:3]:
                    message_parts.append(f"  • {meeting_id}")
                message_parts.append(f"  • ... and {count - 3} more")
            message_parts.append("")

        if "no_mp4_recordings" in error_groups:
            count = len(error_groups["no_mp4_recordings"])
            message_parts.append(f"❌ **No MP4 recordings available ({count}):**")
            if count <= 5:
                for meeting_info in error_groups["no_mp4_recordings"]:
                    message_parts.append(f"  • {meeting_info}")
            else:
                for meeting_info in error_groups["no_mp4_recordings"][:3]:
                    message_parts.append(f"  • {meeting_info}")
                message_parts.append(f"  • ... and {count - 3} more")
            message_parts.append("")

        if "upload_failures" in error_groups:
            count = len(error_groups["upload_failures"])
            message_parts.append(f"❌ **Upload failures ({count}):**")
            if count <= 5:
                for meeting_info in error_groups["upload_failures"]:
                    message_parts.append(f"  • {meeting_info}")
            else:
                for meeting_info in error_groups["upload_failures"][:3]:
                    message_parts.append(f"  • {meeting_info}")
                message_parts.append(f"  • ... and {count - 3} more")
            message_parts.append("")

        if "other_errors" in error_groups:
            message_parts.append(f"❌ **Other errors ({len(error_groups['other_errors'])}):**")
            for error in error_groups["other_errors"][:3]:  # Limit to first 3
                message_parts.append(f"  • {error}")
            if len(error_groups["other_errors"]) > 3:
                message_parts.append(f"  • ... and {len(error_groups['other_errors']) - 3} more")

    elif success_count > 0:
        message_parts.append(f"✅ **All {success_count} YouTube uploads completed successfully!**")

    # Send the message if there's content
    if message_parts:
        final_message = "\n".join(message_parts)
        try:
            tg.send_message(final_message)
            print(f"Sent aggregated Telegram message for {processed_count} operations")
        except Exception as e:
            print(f"Failed to send aggregated Telegram message: {e}")

if __name__ == "__main__":
    main()