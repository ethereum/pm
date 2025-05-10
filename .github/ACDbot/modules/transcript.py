import os
import json
from modules import zoom, discourse, tg
import requests

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
    
    # Extract proper share URL and passcode (new format)
    share_url = recording_data.get('share_url', '')
    passcode = recording_data.get('password', '')
    
    # Get transcript download URL from recording files
    transcript_url = None
    chat_url = None
    
    for file in available_files: # Use the stored list
        if file.get('file_type') == 'TRANSCRIPT':
            transcript_url = file.get('download_url')
        elif file.get('file_type') == 'CHAT':
            chat_url = file.get('download_url')
    
    # Build post content with the new format
    post_content = f"""### Meeting Summary:
{summary_overview}

{summary_details}

{next_steps}

### Recording Access:
- [Join Recording Session]({share_url}) (Passcode: `{passcode}`)"""

    # Add transcript link if available
    if transcript_url:
        post_content += f"\n- [Download Transcript]({transcript_url})"
        
    # Add chat file link if available
    if chat_url:
        post_content += f"\n- [Download Chat]({chat_url})"

    # Add notes if transcript or chat are missing
    if not transcript_url:
        post_content += "\n- *Transcript file not found in recording data.*"
    if not chat_url:
        post_content += "\n- *Chat file not found in recording data.*"

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