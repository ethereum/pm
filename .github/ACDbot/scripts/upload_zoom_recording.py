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

def download_zoom_recording(meeting_id):
    """Download Zoom recording MP4 file to temp location"""
    try:
        recording_info = get_meeting_recording(meeting_id)
    except Exception as e:
        print(f"Error fetching meeting recording for meeting {meeting_id}: {e}")
        return None

    if not recording_info or 'recording_files' not in recording_info:
        return None

    for file in recording_info['recording_files']:
        if file.get('file_type') == 'MP4' and file.get('download_url'):
            download_url = file['download_url']
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
                return temp_file.name
    return None

def upload_recording(meeting_id, occurrence_issue_number=None):
    """Uploads Zoom recording to YouTube for a specific occurrence."""

    # Ensure meeting_id is a string
    meeting_id = str(meeting_id)

    youtube = get_authenticated_service()
    mapping = load_meeting_topic_mapping()

    series_entry = find_meeting_by_id(meeting_id, mapping)

    if not series_entry:
        print(f"[ERROR] Meeting ID {meeting_id} not found in mapping.")
        tg.send_message(f"❌ YouTube upload aborted: Unknown meeting_id {meeting_id} in mapping.")
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
        tg.send_message(f"❌ YouTube upload aborted: Occurrence #{occurrence_issue_number} not found for meeting {meeting_id}.")
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

    video_path = download_zoom_recording(meeting_id)
    if not video_path:
        print(f"No MP4 recording available for meeting {meeting_id}")
        tg.send_message(f"❌ YouTube upload skipped: No MP4 recording available for meeting {meeting_id} (issue #{occurrence_issue_number}).")
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
        tg.send_message(f"❌ YouTube upload failed for meeting {meeting_id} (issue #{occurrence_issue_number}).\nError: {err_text}")
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

                    if not yt_skipped and not yt_processed and occ_issue_num and effective_meeting_id:
                        print(f"\nProcessing occurrence from mapping: Meeting ID {effective_meeting_id}, Issue #{occ_issue_num}")
                        try:
                            upload_recording(effective_meeting_id, occ_issue_num)
                        except Exception as e:
                            print(f"Failed to process {effective_meeting_id} / {occ_issue_num}: {e}")

if __name__ == "__main__":
    main()