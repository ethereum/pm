import os
import json
from modules import zoom, discourse, tg
import requests
import urllib.parse

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            # Handle potential JSON errors
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"::error::Failed to decode JSON from {MAPPING_FILE}. Returning empty mapping.")
                return {}
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2) # Added indent for readability

def post_zoom_transcript_to_discourse(meeting_id: str, occurrence_details: dict = None, meeting_uuid_for_summary: str = None):
    """
    Posts the Zoom meeting recording link and summary to Discourse.
    Uses occurrence_details if provided to find the correct Discourse topic ID.
    Uses meeting_uuid_for_summary if provided to fetch the AI summary.
    """
    # Load the mapping
    mapping = load_meeting_topic_mapping()
    discourse_topic_id = None
    meeting_topic = f"Meeting {meeting_id}" # Default title
    entry = mapping.get(str(meeting_id))

    if not entry or not isinstance(entry, dict):
        print(f"::error::Mapping entry for meeting ID {meeting_id} not found or invalid.")
        # Indicate failure by returning None or raising an error?
        # For now, return False to signal failure to the caller.
        return False

    # Find the correct Discourse topic ID
    if occurrence_details and isinstance(occurrence_details, dict):
        # If occurrence details are provided, use the topic ID from there
        discourse_topic_id = occurrence_details.get("discourse_topic_id")
        meeting_topic = occurrence_details.get("issue_title", meeting_topic)
        print(f"[DEBUG] Using occurrence details. Topic ID: {discourse_topic_id}, Title: {meeting_topic}")
    else:
        # Fallback for non-recurring or older calls (legacy)
        discourse_topic_id = entry.get("discourse_topic_id")
        meeting_topic = entry.get("issue_title", meeting_topic)
        print(f"[DEBUG] Using top-level entry details. Topic ID: {discourse_topic_id}, Title: {meeting_topic}")

    if not discourse_topic_id or str(discourse_topic_id).startswith("placeholder"):
        print(f"::error::No valid Discourse topic ID found for meeting ID {meeting_id} (occurrence: {occurrence_details.get('issue_number', 'N/A') if occurrence_details else 'N/A'}). Provided ID: {discourse_topic_id}")
        return False # Indicate failure

    # Check existing posts in Discourse
    if discourse.check_if_transcript_posted(discourse_topic_id, meeting_id):
        print(f"Transcript already posted for meeting {meeting_id} in topic {discourse_topic_id}.")
        # Return True because the goal (transcript posted) is achieved.
        return True

    # --- NOTE: Preemptive marking of transcript_processed moved to caller (poll_zoom_recordings.py) --- 
    # This avoids marking as processed if this function fails early.
    # entry["transcript_processed"] = True
    # save_meeting_topic_mapping(mapping)

    # Get recording details using the specific meeting instance UUID
    if not meeting_uuid_for_summary:
        print(f"::error::Cannot fetch recording data for meeting {meeting_id}: Specific meeting instance UUID is missing.")
        return False
        
    print(f"[DEBUG] Fetching recording data using UUID: {meeting_uuid_for_summary}")
    recording_data = zoom.get_meeting_recording(meeting_uuid_for_summary)
    if not recording_data:
        print(f"::error::No recording data found for meeting ID {meeting_id} via Zoom API.")
        return False # Failed to get recording data

    # Check if recording duration is sufficient
    recording_duration = recording_data.get('duration', 0) 
    if recording_duration < 10:
        print(f"::warning::Skipping transcript post for meeting {meeting_id} (UUID: {meeting_uuid_for_summary}): Recording duration ({recording_duration} min) is less than 10 minutes.")
        # Return False as the transcript wasn't posted for this (presumably wrong) short recording
        return False 

    # Log the available recording files for debugging
    available_files = recording_data.get('recording_files', [])
    print(f"[DEBUG] Available recording files for meeting {meeting_id} (UUID: {meeting_uuid_for_summary}): {json.dumps(available_files, indent=2)}")

    # Get summary using properly encoded UUID
    # Summary generation might fail if the meeting wasn't eligible or processing hasn't finished.
    summary_data = None
    summary_error_message = None # Variable to store specific error message for summary
    if meeting_uuid_for_summary: # Only attempt if we have the UUID
        try:
            print(f"[DEBUG] Attempting summary fetch with UUID: {meeting_uuid_for_summary}")
            summary_data = zoom.get_meeting_summary(meeting_uuid=meeting_uuid_for_summary)
            print(f"Summary data for meeting {meeting_id}: {json.dumps(summary_data, indent=2)}")
        except requests.exceptions.HTTPError as e:
            # Handle specific errors like 404 Not Found (summary not ready/available)
            if e.response.status_code == 404:
                print(f"::warning::Meeting summary not found for {meeting_uuid_for_summary} (Meeting ID: {meeting_id}). Might still be processing or unavailable. Status: {e.response.status_code}")
                summary_error_message = "Summary not found (404). Might still be processing."
            elif e.response.status_code == 403: # Handle the specific 403 error
                 print(f"::warning::Meeting summary access forbidden for {meeting_uuid_for_summary} (Meeting ID: {meeting_id}). Status: {e.response.status_code} - {e.response.text}")
                 summary_error_message = "Summary access forbidden (403). It might have been deleted."
            else:
                # Re-raise other HTTP errors
                print(f"::error::HTTP error fetching summary for {meeting_uuid_for_summary}: {e}")
                summary_error_message = f"HTTP error {e.response.status_code} fetching summary."
                # Decide if you want to return False here or just proceed without summary
        except Exception as e:
            print(f"::error::Error fetching or parsing summary for {meeting_uuid_for_summary}: {e}")
            summary_error_message = f"General error fetching summary: {e}"
            # Decide if you want to return False here or just proceed without summary
    else:
        summary_error_message = "Could not attempt summary fetch because meeting UUID was not found."

    # Process summary data
    summary_overview = ""
    summary_details = ""
    next_steps = ""
    
    if summary_data:
        # Extract summary overview
        summary_overview = summary_data.get("summary", "No summary overview available")
        
        # Extract detailed summaries in a collapsible section
        if summary_data.get("summary_details"):
            details = []
            for detail in summary_data.get("summary_details", []):
                section_title = detail.get("section_title", "")
                section_summary = detail.get("summary", "")
                if section_title and section_summary:
                    details.append(f"**{section_title}**\n{section_summary}")
                elif section_summary:
                    details.append(section_summary)
            
            if details:
                summary_details = "<details>\n<summary>Click to expand detailed summary</summary>\n\n"
                summary_details += "\n\n".join(details)
                summary_details += "\n</details>"
        
        # Format next steps
        if summary_data.get("next_steps"):
            steps = [f"- {step}" for step in summary_data["next_steps"]]
            next_steps = "### Next Steps:\n" + "\n".join(steps)
    else:
        summary_overview = f"No summary available. {summary_error_message or 'Could not retrieve summary.'}" # Use error message if available
    
    # Extract URLs and passcodes
    share_url = recording_data.get('share_url', '') # For original "Join Recording Session" link
    manual_passcode = recording_data.get('password', '') # For the original link's displayed passcode
    recording_play_passcode = recording_data.get('recording_play_passcode') # For URL splicing

    primary_video_play_url = None # For "Join Recording Session with pwd"
    transcript_download_url = None  # For "Download Transcript" (direct)
    transcript_play_url = None      # For "Download Transcript with pwd"
    chat_download_url = None        # For "Download Chat" (direct)
    chat_play_url = None            # For "Download Chat with pwd"

    video_recording_types_priority = [
        "shared_screen_with_speaker_view",
        "shared_screen_with_gallery_view",
        "speaker_view",
        "gallery_view",
        "shared_screen"
    ]
    primary_video_play_url_type_priority_index = float('inf')

    for file in available_files:
        file_type = file.get('file_type')
        recording_type = file.get('recording_type')

        if file_type == 'MP4' and recording_type in video_recording_types_priority:
            current_priority_index = video_recording_types_priority.index(recording_type)
            if current_priority_index < primary_video_play_url_type_priority_index:
                primary_video_play_url = file.get('play_url')
                primary_video_play_url_type_priority_index = current_priority_index
        
        if file.get('file_type') == 'TRANSCRIPT':
            transcript_download_url = file.get('download_url')
            transcript_play_url = file.get('play_url')
        elif file.get('file_type') == 'CHAT':
            chat_download_url = file.get('download_url')
            chat_play_url = file.get('play_url')

    # Fallback if no prioritized video play_url found, try any MP4
    if primary_video_play_url is None:
        for file in available_files:
            if file.get('file_type') == 'MP4':
                primary_video_play_url = file.get('play_url')
                if primary_video_play_url: # Take the first MP4 play_url found
                    break
    
    # Build post content
    post_content = f"""### Meeting Summary:
{summary_overview}

{summary_details}

{next_steps}

### Recording Access:"""

    # Line 1: Join Recording Session (manual passcode, uses share_url)
    # if share_url:
    #     post_content += f"\n- [Join Recording Session]({share_url})"
    #     if manual_passcode:
    #         post_content += f" (Passcode: `{manual_passcode}`)"
    # else:
    #     post_content += "\n- *Join Recording Session link (via share page) not available.*"
        
    # Line 2: Join Recording Session with pwd (uses primary_video_play_url)
    if primary_video_play_url and recording_play_passcode:
        # Ensure passcode is URL-encoded
        encoded_pwd = urllib.parse.quote_plus(str(recording_play_passcode))
        join_session_direct_play_url = f"{primary_video_play_url}?pwd={encoded_pwd}"
        post_content += f"\n- [Join Recording Session]({join_session_direct_play_url})"
    elif primary_video_play_url: # Play URL exists, but no passcode for URL
        post_content += "\n- *Link for 'Join Recording Session with pwd' (direct play) could not be generated (passcode for URL not found).* "
    else: # No primary video play_url found
        post_content += "\n- *Direct play link for 'Join Recording Session with pwd' not available (video play URL not found).* "

    # Line 3: Download Transcript (direct download)
    # if transcript_download_url:
    #     post_content += f"\n- [Download Transcript]({transcript_download_url})"
    # else:
    #     post_content += "\n- *Direct download link for transcript not found.*"

    # Line 4: Download Transcript with pwd (uses transcript_download_url)
    if transcript_download_url and recording_play_passcode:
        encoded_pwd = urllib.parse.quote_plus(str(recording_play_passcode))
        download_transcript_with_pwd_url = f"{transcript_download_url}?pwd={encoded_pwd}" # Use download_url
        post_content += f"\n- [Download Transcript]({download_transcript_with_pwd_url})"
    elif transcript_download_url: # transcript_download_url exists, but recording_play_passcode is missing
        post_content += "\n- *Link for 'Download Transcript with pwd' could not be generated (passcode for URL splicing not found).* "
    else: # transcript_download_url is missing
        post_content += "\n- *Download URL for transcript (needed for 'with pwd' link) not found.*"
        
    # Line 5: Download Chat (direct download)
    # if chat_download_url:
    #     post_content += f"\n- [Download Chat]({chat_download_url})"
    # else:
    #     post_content += "\n- *Direct download link for chat not found.*"

    # Line 6: Download Chat with pwd (uses chat_download_url)
    if chat_download_url and recording_play_passcode:
        encoded_pwd = urllib.parse.quote_plus(str(recording_play_passcode))
        download_chat_with_pwd_url = f"{chat_download_url}?pwd={encoded_pwd}" # Use download_url
        post_content += f"\n- [Download Chat]({download_chat_with_pwd_url})"
    elif chat_download_url: # chat_download_url exists, but recording_play_passcode is missing
        post_content += "\n- *Link for 'Download Chat with pwd' could not be generated (passcode for URL splicing not found).* "
    else: # chat_download_url is missing
        post_content += "\n- *Download URL for chat (needed for 'with pwd' link) not found.*"

    try:
        discourse.create_post(
            topic_id=discourse_topic_id,
            body=post_content
        )
        print(f"Posted recording links for meeting {meeting_id} to topic {discourse_topic_id}")
    except Exception as e:
        print(f"::error::Failed to create Discourse post for topic {discourse_topic_id}: {e}")
        # Failure to post to Discourse should be considered a failure of this function
        return False

    # Now, send the same content to Telegram
    # Failure here is less critical than Discourse posting, so don't return False
    try:
        tg.send_message(post_content)
        print("Message sent to Telegram successfully.")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

    # If we reached here, the core task (posting to Discourse) was successful.
    return True