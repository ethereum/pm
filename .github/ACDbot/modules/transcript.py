import os
import json
from modules import zoom, discourse, tg
import requests

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"::error::Failed to decode JSON from {MAPPING_FILE}. Returning empty mapping.")
                return {}
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

def post_zoom_transcript_to_discourse(recording_data: dict, occurrence_details: dict = None):
    """
    Posts the Zoom meeting recording link and summary to Discourse.
    Uses occurrence_details if provided to find the correct Discourse topic ID.
    
    Args:
        recording_data (dict): The specific recording object from Zoom API.
        occurrence_details (dict, optional): Details about the specific meeting occurrence.
    """
    # Extract meeting ID from the passed-in recording data
    meeting_id = str(recording_data.get("id"))
    if not meeting_id:
        print(f"::error::Meeting ID not found in provided recording_data.")
        return False

    # Load the mapping - still needed to find the main mapping entry for context/fallbacks
    mapping = load_meeting_topic_mapping()
    discourse_topic_id = None
    meeting_topic = recording_data.get("topic", f"Meeting {meeting_id}") # Use topic from recording data
    # Find the main mapping entry using the meeting ID
    entry = mapping.get(meeting_id) 

    # This check might be less critical now but kept for safety
    if not entry or not isinstance(entry, dict):
        print(f"::warning::Mapping entry for meeting ID {meeting_id} not found or invalid. Proceeding with occurrence details if available.")
        # Don't return False here, rely on occurrence_details or defaults

    # Find the correct Discourse topic ID (Priority: Occurrence -> Entry Fallback)
    if occurrence_details and isinstance(occurrence_details, dict):
        discourse_topic_id = occurrence_details.get("discourse_topic_id")
        meeting_topic = occurrence_details.get("issue_title", meeting_topic) # Prefer issue title if available
        print(f"[DEBUG] Using occurrence details. Topic ID: {discourse_topic_id}, Title: {meeting_topic}")
    elif entry: # Fallback to top-level entry only if occurrence_details are missing/invalid
        discourse_topic_id = entry.get("discourse_topic_id")
        meeting_topic = entry.get("issue_title", meeting_topic)
        print(f"[DEBUG] Using top-level entry details (fallback). Topic ID: {discourse_topic_id}, Title: {meeting_topic}")
    else:
         print(f"[DEBUG] No valid occurrence details or mapping entry found to determine Discourse topic ID.")

    if not discourse_topic_id or str(discourse_topic_id).startswith("placeholder"):
        occurrence_issue_num = occurrence_details.get('issue_number', 'N/A') if occurrence_details else 'N/A'
        print(f"::error::No valid Discourse topic ID found for meeting ID {meeting_id} (occurrence: {occurrence_issue_num}). Provided ID: {discourse_topic_id}")
        return False # Indicate failure

    # Check existing posts in Discourse using the extracted meeting_id
    if discourse.check_if_transcript_posted(discourse_topic_id, meeting_id):
        print(f"Transcript already posted for meeting {meeting_id} in topic {discourse_topic_id}.")
        return True

    # Recording data is now passed in, no need to fetch it again.
    # recording_data = zoom.get_meeting_recording(meeting_id)
    # if not recording_data: # This check is now redundant
    #     print(f"::error::No recording data found for meeting ID {meeting_id} via Zoom API.")
    #     return False # Failed to get recording data

    # Check if recording duration is sufficient (using passed-in data)
    recording_duration = recording_data.get('duration', 0)
    if recording_duration < 10:
        print(f"Skipping meeting {meeting_id}: Recording duration ({recording_duration} min) is less than 10 minutes.")
        return False # Indicate skip due to duration

    # Extract UUID from passed-in data
    meeting_uuid = recording_data.get('uuid', '')
    if not meeting_uuid:
        # Use a more specific error message
        print(f"::error::Meeting UUID not found in provided recording data for meeting {meeting_id}.")
        return False

    # Get summary using properly encoded UUID
    try:
        print(f"[DEBUG] Attempting to fetch summary for meeting {meeting_id} using UUID: {meeting_uuid}") # Add log
        summary_data = zoom.get_meeting_summary(meeting_uuid=meeting_uuid)
        # Log summary success/failure based on content
        if summary_data:
             print(f"[DEBUG] Successfully fetched summary data for meeting {meeting_id} (UUID: {meeting_uuid}).")
             # print(f"Summary data for meeting {meeting_id}: {json.dumps(summary_data, indent=2)}") # Optional: keep verbose log
        else:
             print(f"[DEBUG] zoom.get_meeting_summary returned empty data for meeting {meeting_id} (UUID: {meeting_uuid}).")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"::warning::Meeting summary not found for {meeting_uuid} (Meeting ID: {meeting_id}). Might still be processing or unavailable. Status: {e.response.status_code}")
            summary_data = None # Set to None explicitly
        else:
            print(f"::error::HTTP error fetching summary for {meeting_uuid} (Meeting ID: {meeting_id}): {e}")
            return False
    except Exception as e:
        print(f"::error::Error fetching or parsing summary for {meeting_uuid} (Meeting ID: {meeting_id}): {e}")
        return False # Failed to get summary

    # Check if summary data is available *after* the fetch attempt
    if not summary_data:
        print(f"Skipping meeting {meeting_id} (UUID: {meeting_uuid}): No summary data found or available yet.")
        return False # Indicate skip due to missing summary

    # Process summary data
    # Initialize variables with defaults
    summary_overview = "No summary overview available" 
    summary_details = ""
    next_steps = ""
    
    # Directly extract data from the validated summary_data object
    summary_overview = summary_data.get("summary", summary_overview) # Use default if key missing
    
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
        # Ensure next_steps is a list before iterating
        next_steps_list = summary_data.get("next_steps", [])
        if isinstance(next_steps_list, list) and next_steps_list:
            steps = [f"- {step}" for step in next_steps_list]
            next_steps = "### Next Steps:\n" + "\n".join(steps)

    # Extract proper share URL and passcode (new format)
    share_url = recording_data.get('share_url', '')
    passcode = recording_data.get('password', '') # Keep getting passcode for potential future use, but don't modify URL
    
    # Use the share_url directly from the API response
    recording_access_line = "- Recording link not available"
    if share_url:
        recording_access_line = f"- [Join Recording Session]({share_url})"
        # Add a debug log to see the raw share_url from the API
        print(f"[DEBUG] Using share_url from Zoom API: {share_url}") 
    else:
        print(f"[WARN] Share URL not found in recording data for meeting {meeting_id}")

    # Get transcript download URL from recording files
    transcript_url = None
    chat_url = None
    
    for file in recording_data.get('recording_files', []):
        if file.get('file_type') == 'TRANSCRIPT':
            transcript_url = file.get('download_url')
        elif file.get('file_type') == 'CHAT':
            chat_url = file.get('download_url')
    
    # Build post content with the potentially modified recording access line
    post_content = f"""### Meeting Summary:
{summary_overview}

{summary_details}

{next_steps}

### Recording Access:
{recording_access_line}""" # Use the constructed line here

    # Add transcript link if available
    if transcript_url:
        post_content += f"\n- [Download Transcript]({transcript_url})"
        
    # Add chat file link if available
    if chat_url:
        post_content += f"\n- [Download Chat]({chat_url})"

    try:
        discourse.create_post(
            topic_id=discourse_topic_id,
            body=post_content
        )
        print(f"Posted recording links for meeting {meeting_id} to topic {discourse_topic_id}")
    except Exception as e:
        print(f"::error::Failed to create Discourse post for topic {discourse_topic_id}: {e}")
        return False

    # Now, send the same content to Telegram
    try:
        tg.send_message(post_content)
        print("Message sent to Telegram successfully.")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")
    
    return True
