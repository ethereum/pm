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
    # Ensure mapping is saved with indentation for readability
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

def post_zoom_transcript_to_discourse(recording_data: dict, occurrence_details: dict = None):
    # MODIFIED function signature
    """
    Posts the Zoom meeting recording link and summary to Discourse.
    Uses occurrence_details if provided to find the correct Discourse topic ID.
    """
    # Extract meeting ID from the passed-in recording data
    meeting_id = str(recording_data.get("id"))
    if not meeting_id:
        print(f"::error::Meeting ID not found in provided recording_data.")
        return False

    # Load the mapping - still needed for context/fallbacks
    mapping = load_meeting_topic_mapping()
    discourse_topic_id = None
    meeting_topic = recording_data.get("topic", f"Meeting {meeting_id}") # Use topic from recording data as initial default
    entry = mapping.get(meeting_id) # Get the main series entry

    # Find the correct Discourse topic ID & Meeting Topic (Priority: Occurrence -> Entry Fallback)
    if occurrence_details and isinstance(occurrence_details, dict):
        discourse_topic_id = occurrence_details.get("discourse_topic_id")
        # Prefer issue title from occurrence if available
        occurrence_title = occurrence_details.get("issue_title")
        if occurrence_title:
            meeting_topic = occurrence_title
        print(f"[DEBUG] Using occurrence details. Topic ID: {discourse_topic_id}, Title: {meeting_topic}")
    elif entry and isinstance(entry, dict): # Fallback to top-level entry
        discourse_topic_id = entry.get("discourse_topic_id")
        # Use issue title from entry if available and not overridden by occurrence
        entry_title = entry.get("issue_title")
        if entry_title and meeting_topic == recording_data.get("topic", f"Meeting {meeting_id}"): # Only use entry title if not set by occurrence
             meeting_topic = entry_title
        print(f"[DEBUG] Using top-level entry details (fallback). Topic ID: {discourse_topic_id}, Title: {meeting_topic}")
    else:
         print(f"::warning::Mapping entry for meeting ID {meeting_id} not found or invalid. Cannot determine Discourse topic ID.")
         # Don't return False yet, check if discourse_topic_id was somehow set by occurrence_details alone

    if not discourse_topic_id or str(discourse_topic_id).startswith("placeholder"):
        occurrence_issue_num = occurrence_details.get('issue_number', 'N/A') if occurrence_details else 'N/A'
        print(f"::error::No valid Discourse topic ID found for meeting ID {meeting_id} (occurrence: {occurrence_issue_num}). Provided ID: {discourse_topic_id}")
        return False # Indicate failure

    # Check existing posts in Discourse using the determined topic ID and meeting ID
    if discourse.check_if_transcript_posted(discourse_topic_id, meeting_id):
        print(f"Transcript already posted for meeting {meeting_id} in topic {discourse_topic_id}.")
        # Mark as processed in the occurrence if possible
        if occurrence_details and entry and "occurrences" in entry:
            occ_index = -1
            for idx, occ in enumerate(entry["occurrences"]):
                if occ.get("issue_number") == occurrence_details.get("issue_number"):
                    occ_index = idx
                    break
            if occ_index != -1:
                 mapping[meeting_id]["occurrences"][occ_index]["transcript_processed"] = True
                 save_meeting_topic_mapping(mapping) # Save the update
                 print(f"[DEBUG] Marked occurrence {occurrence_details.get('issue_number')} as transcript_processed.")
        return True # Indicate success (already done)

    # --- Start of logic mostly from the user-provided snippet ---

    # Preemptively mark transcript as processed IN THE OCCURRENCE if possible
    # This avoids race conditions if the poll runs again quickly
    marked_processed = False
    if occurrence_details and entry and "occurrences" in entry:
        occ_index = -1
        for idx, occ in enumerate(entry["occurrences"]):
            if occ.get("issue_number") == occurrence_details.get("issue_number"):
                occ_index = idx
                break
        if occ_index != -1:
             # Check if already marked processed before saving again
             if not mapping[meeting_id]["occurrences"][occ_index].get("transcript_processed", False):
                 mapping[meeting_id]["occurrences"][occ_index]["transcript_processed"] = True
                 save_meeting_topic_mapping(mapping) # Save the update
                 marked_processed = True
                 print(f"[DEBUG] Preemptively marked occurrence {occurrence_details.get('issue_number')} as transcript_processed.")
             else:
                 print(f"[DEBUG] Occurrence {occurrence_details.get('issue_number')} already marked as transcript_processed.")

    # Recording data is passed in, no need to fetch recording_data again.
    # meeting_uuid = recording_data.get('uuid', '') # Already have recording_data

    # Check if recording duration is sufficient (using passed-in data)
    recording_duration = recording_data.get('duration', 0)
    if recording_duration < 10:
        print(f"Skipping meeting {meeting_id}: Recording duration ({recording_duration} min) is less than 10 minutes.")
        # If we preemptively marked as processed, revert it
        if marked_processed and occ_index != -1:
            mapping[meeting_id]["occurrences"][occ_index]["transcript_processed"] = False
            save_meeting_topic_mapping(mapping)
            print(f"[DEBUG] Reverted transcript_processed flag for occurrence {occurrence_details.get('issue_number')} due to short duration.")
        return False # Indicate skip due to duration

    # Extract UUID from passed-in data
    meeting_uuid = recording_data.get('uuid', '')
    if not meeting_uuid:
        print(f"::error::Meeting UUID not found in provided recording data for meeting {meeting_id}.")
        # Revert processed flag if needed
        if marked_processed and occ_index != -1:
             mapping[meeting_id]["occurrences"][occ_index]["transcript_processed"] = False
             save_meeting_topic_mapping(mapping)
        return False

    # Get summary using properly encoded UUID
    summary_data = None # Initialize
    try:
        print(f"[DEBUG] Attempting to fetch summary for meeting {meeting_id} using UUID: {meeting_uuid}")
        summary_data = zoom.get_meeting_summary(meeting_uuid=meeting_uuid)
        if summary_data:
             print(f"[DEBUG] Successfully fetched summary data.")
             # print(f"Summary data: {json.dumps(summary_data, indent=2)}") # Optional verbose log
        else:
             print(f"[DEBUG] zoom.get_meeting_summary returned empty data.")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"::warning::Meeting summary not found for {meeting_uuid}. Proceeding without summary. Status: {e.response.status_code}")
            summary_data = None # Ensure it's None
        else:
            print(f"::error::HTTP error fetching summary for {meeting_uuid}: {e}")
            # Revert processed flag if needed
            if marked_processed and occ_index != -1:
                 mapping[meeting_id]["occurrences"][occ_index]["transcript_processed"] = False
                 save_meeting_topic_mapping(mapping)
            return False
    except Exception as e:
        print(f"::error::Error fetching or parsing summary for {meeting_uuid}: {e}")
        # Revert processed flag if needed
        if marked_processed and occ_index != -1:
             mapping[meeting_id]["occurrences"][occ_index]["transcript_processed"] = False
             save_meeting_topic_mapping(mapping)
        return False # Failed to get summary

    # Process summary data (Copied from user snippet)
    summary_overview = ""
    summary_details = ""
    next_steps = ""

    if summary_data:
        summary_overview = summary_data.get("summary", "No summary overview available")
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
        if summary_data.get("next_steps"):
             # Ensure next_steps is a list before iterating
             next_steps_list = summary_data.get("next_steps", [])
             if isinstance(next_steps_list, list) and next_steps_list:
                 steps = [f"- {step}" for step in next_steps_list]
                 next_steps = "### Next Steps:\n" + "\n".join(steps)
    else:
        # Provide a default message if summary couldn't be fetched
        summary_overview = "Meeting summary is not available yet."

    # --- Simplified Logic: Use share_url only, prioritize mapping for passcode --- 
    share_url = recording_data.get('share_url', '')
    print(f"[DEBUG] share_url: {share_url}")

    # Fetch passcode prioritizing mapping
    passcode = None
    if occurrence_details and isinstance(occurrence_details, dict):
        passcode = occurrence_details.get("password")
        if passcode: print(f"[DEBUG] Found passcode in occurrence_details.")

    if not passcode and entry and isinstance(entry, dict):
        passcode = entry.get("password")
        if passcode: print(f"[DEBUG] Found passcode in top-level mapping entry.")

    if not passcode:
        # Fallback to recording data password ONLY if not found in mapping
        passcode = recording_data.get('password') 
        if passcode: print(f"[DEBUG] Found passcode in recording_data.get('password') (fallback).")

    passcode = passcode or '' # Ensure passcode is a string, default to empty if None
    if not passcode:
         print("[DEBUG] No passcode found after checking mapping and recording_data.")

    # Construct the recording access line using ONLY share_url and the fetched passcode
    recording_access_line = ""
    if share_url and passcode:
        recording_access_line = f"- [Join Recording Session]({share_url}) (Passcode: `{passcode}`)"
    elif share_url: # If only share_url is present
        recording_access_line = f"- [Recording Link]({share_url})" # Fallback text if no passcode
    else: # If share_url is also missing
        recording_access_line = "- Recording link not available"
    # --- END Simplified Logic ---

    # Get transcript download URL from recording files
    transcript_url = None
    chat_url = None

    for file in recording_data.get('recording_files', []):
        if file.get('file_type') == 'TRANSCRIPT':
            transcript_url = file.get('download_url')
        elif file.get('file_type') == 'CHAT':
            chat_url = file.get('download_url')

    # Build post content using the format from the user snippet
    # Include passcode only if BOTH share_url AND passcode are present
    post_content = f"""### Meeting Summary:
{summary_overview}

{summary_details}

{next_steps}

### Recording Access:
{recording_access_line}"""

    # Add transcript link if available
    if transcript_url:
        post_content += f"\n- [Download Transcript]({transcript_url})"

    # Add chat file link if available
    if chat_url:
        post_content += f"\n- [Download Chat]({chat_url})"

    # Attempt to post to Discourse
    try:
        discourse.create_post(
            topic_id=discourse_topic_id,
            body=post_content
        )
        print(f"Posted recording links for meeting {meeting_id} to topic {discourse_topic_id}")
        # Ensure transcript_processed is saved if not already done
        if not marked_processed and occurrence_details and entry and "occurrences" in entry:
            occ_index = -1
            for idx, occ in enumerate(entry["occurrences"]):
                if occ.get("issue_number") == occurrence_details.get("issue_number"):
                    occ_index = idx
                    break
            if occ_index != -1:
                if not mapping[meeting_id]["occurrences"][occ_index].get("transcript_processed", False):
                    mapping[meeting_id]["occurrences"][occ_index]["transcript_processed"] = True
                    save_meeting_topic_mapping(mapping)
                    print(f"[DEBUG] Marked occurrence {occurrence_details.get('issue_number')} as transcript_processed after successful post.")
    except Exception as e:
        print(f"::error::Failed to create Discourse post for topic {discourse_topic_id}: {e}")
        # Revert processed flag if needed
        if marked_processed and occurrence_details and entry and "occurrences" in entry:
             occ_index = -1
             for idx, occ in enumerate(entry["occurrences"]):
                 if occ.get("issue_number") == occurrence_details.get("issue_number"):
                     occ_index = idx
                     break
             if occ_index != -1:
                 mapping[meeting_id]["occurrences"][occ_index]["transcript_processed"] = False
                 save_meeting_topic_mapping(mapping)
                 print(f"[DEBUG] Reverted transcript_processed flag for occurrence {occurrence_details.get('issue_number')} due to Discourse post error.")
        return False # Indicate failure

    # Send the same content to Telegram
    try:
        # Use markdownv2 formatting for Telegram if needed, otherwise keep simple
        tg.send_message(post_content) # Consider tg.send_message(tg.escape_markdown(post_content), parse_mode='MarkdownV2') if needed
        print("Message sent to Telegram successfully.")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")
        # Don't return False here, Discourse post was successful

    return True # Indicate success