import os
import sys
import argparse
from modules import discourse, zoom, gcal, email_utils, tg, rss_utils
from github import Github
import re
from datetime import datetime as dt
import json
import requests
from github import InputGitAuthor

# Add youtube_utils import
from modules import youtube_utils

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

def extract_facilitator_info(issue_body):
    """
    Extracts facilitator email information from the issue body.
    Handles:
    - "Facilitator emails: email1, email2"
    - "- Facilitator email: email3"
    - "- Facilitator email: [email4](mailto:email4)"
    Returns a list of email addresses.
    """
    # Combined pattern to capture both formats
    # Group 1: Comma-separated list from "Facilitator emails: ..."
    # Group 2: Single email from markdown link in "- Facilitator email: [...]..."
    # Group 3: Single plain email from "- Facilitator email: ..."
    email_pattern = r"(?im)^(?:Facilitator emails:\s*(.+)|-\s*Facilitator email:\s*(?:\(\[([^\@\s\]]+@[^\s\)]+)\]\(mailto:[^\)]+\))|([^\@\s]+@[^\s\n]+)))"
    
    print(f"[DEBUG] Extracting facilitator emails from issue body")
    
    facilitator_emails = []
    # Use finditer to handle the different capturing groups based on which pattern matched
    for match in re.finditer(email_pattern, issue_body):
        if match.group(1): # Matched "Facilitator emails: ..."
            emails_str = match.group(1)
            # Split by comma, strip whitespace from each email
            found_emails = [email.strip() for email in emails_str.split(',') if email.strip()]
            facilitator_emails.extend(found_emails)
        elif match.group(2): # Matched "- Facilitator email: [markdown]..."
            facilitator_emails.append(match.group(2).strip())
        elif match.group(3): # Matched "- Facilitator email: plain..."
            facilitator_emails.append(match.group(3).strip())
            
    if facilitator_emails:
        print(f"[DEBUG] Extracted facilitator emails: {facilitator_emails}")
        return facilitator_emails
    else:
        print(f"[DEBUG] No facilitator emails found in the expected format.")
        return [] # Return an empty list if no match

def extract_recurring_info(issue_body):
    """
    Extracts recurring meeting information from the issue body.
    Returns a tuple of (is_recurring, occurrence_rate).
    For one-time calls, these fields might be missing - default to false/none.
    """
    recurring_pattern = r"Recurring meeting\s*:\s*(true|false)"
    occurrence_pattern = r"Occurrence rate\s*:\s*(none|weekly|bi-weekly|monthly)"
    
    recurring_match = re.search(recurring_pattern, issue_body, re.IGNORECASE)
    occurrence_match = re.search(occurrence_pattern, issue_body, re.IGNORECASE)
    
    # Default to false and none if fields are missing (one-time meeting template)
    is_recurring = recurring_match and recurring_match.group(1).lower() == 'true'
    occurrence_rate = occurrence_match.group(1).lower() if occurrence_match else 'none'
    
    return is_recurring, occurrence_rate

def extract_already_on_calendar(issue_body):
    """
    Extracts information about whether a meeting is already on the Ethereum Calendar.
    Returns a boolean indicating if the meeting is already on the calendar.
    """
    calendar_pattern = r"Already on Ethereum Calendar\s*:\s*(true|false)"
    
    calendar_match = re.search(calendar_pattern, issue_body, re.IGNORECASE)
    already_on_calendar = calendar_match and calendar_match.group(1).lower() == 'true'
    
    return already_on_calendar

def extract_call_series(issue_body):
    """
    Extracts and normalizes the 'Call series' field from the issue body.
    """
    call_series_pattern = r"Call series\s*:\s*([^\n]+)"
    match = re.search(call_series_pattern, issue_body, re.IGNORECASE)
    return match.group(1).strip().lower() if match else None

def extract_need_youtube_streams(issue_body):
    """
    Extracts information about whether YouTube stream links are needed.
    Returns a boolean indicating if stream links should be created.
    """
    youtube_pattern = r"Need YouTube stream links\s*:\s*(true|false)"
    
    youtube_match = re.search(youtube_pattern, issue_body, re.IGNORECASE)
    need_youtube_streams = youtube_match and youtube_match.group(1).lower() == 'true'
    
    return need_youtube_streams

def check_existing_youtube_streams(call_series, mapping):
    """
    Check if there are existing YouTube streams for a call series.
    Returns a list of stream links previously created, if any.
    """
    if not call_series:
        return None
        
    # Find all entries with the same call_series
    existing_entries = [entry for entry in mapping.values() 
                      if entry.get("call_series") == call_series 
                      and "youtube_streams" in entry]
    
    # Sort by issue number if available (to get the most recent ones)
    existing_entries.sort(key=lambda e: e.get("issue_number", 0), reverse=True)
    
    # Return the YouTube streams from the most recent entry
    if existing_entries:
        return existing_entries[0].get("youtube_streams")
    
    return None

def extract_already_zoom_meeting(issue_body):
    """
    Extracts information about whether a Zoom meeting ID already exists.
    Returns a boolean indicating if Zoom creation should be skipped.
    """
    zoom_pattern = r"Already a Zoom meeting ID\s*:\s*(true|false)"
    
    zoom_match = re.search(zoom_pattern, issue_body, re.IGNORECASE)
    skip_zoom_creation = zoom_match and zoom_match.group(1).lower() == 'true'
    
    return skip_zoom_creation

def extract_display_zoom_link(issue_body):
    """
    Extracts the boolean flag indicating whether to display the Zoom link in the calendar invite.
    Defaults to False if the line is not found or value is not 'true'.
    """
    display_pattern = r"display zoom link in invite\\s*:\\s*(true|false)"
    match = re.search(display_pattern, issue_body, re.IGNORECASE)
    
    display_link = match and match.group(1).lower() == 'true'
    print(f"[DEBUG] Extracted display_zoom_link_in_invite: {display_link}")
    return display_link

def handle_github_issue(issue_number: int, repo_name: str):
    """
    Fetches the specified GitHub issue, extracts its title and body,
    then creates or updates a Discourse topic using the issue title as the topic title
    and its body as the topic content.

    If the date/time or duration cannot be parsed from the issue body, 
    a comment is posted indicating the format error, and no meeting is created.
    """
    comment_lines = []
    mapping_updated = False
    
    # Load existing mapping
    mapping = load_meeting_topic_mapping()

    # 1. Connect to GitHub API
    gh = Github(os.environ["GITHUB_TOKEN"])
    repo = gh.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue_title = issue.title
    issue_body = issue.body or "(No issue body provided.)"

    # Extract configuration from issue body
    is_recurring, occurrence_rate = extract_recurring_info(issue_body)
    need_youtube_streams = extract_need_youtube_streams(issue_body)
    call_series = extract_call_series(issue_body)
    skip_zoom_creation = extract_already_zoom_meeting(issue_body)
    skip_gcal_creation = extract_already_on_calendar(issue_body)
    display_zoom_link_in_invite = extract_display_zoom_link(issue_body) # Extract the new flag

    # Check for existing YouTube streams for this call series
    existing_youtube_streams = check_existing_youtube_streams(call_series, mapping)
    
    # --- Start Refactor: Separate Zoom and GCal skip logic --- 
    # Extract whether to skip Zoom creation
    skip_zoom_creation = extract_already_zoom_meeting(issue_body)
    # Extract whether to skip Google Calendar creation
    skip_gcal_creation = extract_already_on_calendar(issue_body)

    # Automatic skip logic based on existing series (OVERRIDES issue input)
    existing_series_entry_for_zoom = None # Keep track if we reuse for Zoom
    if is_recurring and call_series:
        # Find the most recent entry for this call series with a meeting_id
        series_entries = [
            entry for entry in mapping.values() 
            if entry.get("call_series") == call_series and "meeting_id" in entry
        ]
        if series_entries:
            series_entries.sort(key=lambda e: e.get("issue_number", 0), reverse=True)
            # Check the most recent entry for this series
            potential_existing_series = series_entries[0]
            existing_series_meeting_id = potential_existing_series.get("meeting_id")
            is_placeholder_id = (str(existing_series_meeting_id) == "null" or 
                                 str(existing_series_meeting_id).startswith("placeholder-"))

            if existing_series_meeting_id and not is_placeholder_id:
                # Found a valid, non-placeholder meeting ID - force reuse
                existing_series_entry_for_zoom = potential_existing_series # Confirm this is the one we reuse
                if not skip_zoom_creation:
                    print(f"[INFO] Overriding 'Already a Zoom meeting ID: false' because a *valid* existing meeting ({existing_series_meeting_id}) for series '{call_series}' was found.")
                skip_zoom_creation = True # Force skip Zoom creation
            elif is_placeholder_id:
                print(f"[INFO] Found existing series '{call_series}' but meeting ID is a placeholder ('{existing_series_meeting_id}'). Will not force reuse based on this placeholder.")
                # Do NOT force skip_zoom_creation or skip_gcal_creation based on a placeholder.
                # Let the script decide based on issue input later.
                # Still set existing_series_entry_for_zoom in case other details (like GCal ID) are valid and reusable
                existing_series_entry_for_zoom = potential_existing_series 
            # Else: No meeting ID found in the most recent entry, do nothing here.
    
    # Add comments based on final skip decisions
    if skip_zoom_creation and not existing_series_entry_for_zoom: # Skipped via issue input, not series reuse
        comment_lines.append("\n**Note:** Zoom meeting creation skipped as requested in issue.")
    if skip_gcal_creation and not existing_series_entry_for_zoom: # Skipped via issue input, not series reuse
        comment_lines.append("\n**Note:** Google Calendar event creation skipped as requested in issue.")
    # Note for series reuse is added within the Zoom processing block later
    # --- End Refactor --- 

    # 2. Check for existing topic_id using the mapping instead of comments
    topic_id = None
    existing_entry = next((entry for entry in mapping.values() if entry.get("issue_number") == issue_number), None)
    if existing_entry:
        topic_id = existing_entry.get("discourse_topic_id")

    issue_link = f"[GitHub Issue]({issue.html_url})"
    updated_body = f"{issue_body}\n\n{issue_link}"

    # Initialize discourse_url to ensure it has a value
    discourse_url = None
    # 3. Discourse handling
    if topic_id:
        print(f"[DEBUG] Creating new topic or finding existing: '{issue_title}'")
        # discourse.create_topic now handles duplicate titles internally
        discourse_response = discourse.create_topic(
            title=issue_title,
            body=updated_body,
            category_id=63  # Example category ID
        )
        
        topic_id = discourse_response.get("topic_id")
        action = discourse_response.get("action", "failed") # Default to failed if action not returned
        
        if topic_id:
            discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
            comment_lines.append(f"**Discourse Topic ID:** {topic_id}")
            comment_lines.append(f"- Action: {action.capitalize()}")
            comment_lines.append(f"- URL: {discourse_url}")
            print(f"[DEBUG] Discourse topic {action}: ID {topic_id}, title '{issue_title}'")
            
            # Add existing YouTube stream links to comments and discourse post if available AND topic exists
            if existing_youtube_streams:
                comment_lines.append("\n**Existing YouTube Stream Links:**")
                stream_links = []
                for i, stream in enumerate(existing_youtube_streams, 1):
                    stream_date = ""
                    if 'scheduled_time' in stream:
                        try:
                            from datetime import datetime
                            scheduled_time = stream['scheduled_time']
                            if scheduled_time.endswith('Z'):
                                scheduled_time = scheduled_time.replace('Z', '+00:00')
                            date_obj = datetime.fromisoformat(scheduled_time)
                            stream_date = f" ({date_obj.strftime('%b %d, %Y')})"
                        except Exception as e:
                            print(f"[DEBUG] Error formatting stream date: {e}")
                    comment_lines.append(f"- Stream {i}{stream_date}: {stream['stream_url']}")
                    stream_links.append(f"- Stream {i}{stream_date}: {stream['stream_url']}")
                
                # Update Discourse post with stream links
                try:
                    discourse_content = f"{updated_body}\n\n**Existing YouTube Stream Links:**\n" + "\n".join(stream_links)
                    discourse.update_topic(
                        topic_id=topic_id,
                        body=discourse_content
                    )
                except Exception as e:
                    print(f"[DEBUG] Error updating Discourse topic {topic_id} with existing YouTube streams: {str(e)}")
                    comment_lines.append(f"- ⚠️ Failed to add existing YouTube streams to Discourse topic {topic_id}")
        else:
            # Handle case where create_topic failed to return a topic_id (even after trying to find existing)
            print(f"[ERROR] Failed to create or find Discourse topic for title: '{issue_title}'")
            comment_lines.append("\n**⚠️ Discourse Topic Error**")
            comment_lines.append(f"- Failed to create/find Discourse topic. Check Discourse module logs.")
            topic_id = f"placeholder-failed-{issue.number}" # Keep a placeholder for downstream logic
            discourse_url = "https://ethereum-magicians.org (API error occurred)"
            action = "failed"

    # Determine the base title for recurring events
    event_base_title = issue_title # Default to issue title
    if is_recurring and call_series:
        # Use call_series, potentially capitalizing it for better presentation
        event_base_title = call_series.strip().upper()
        print(f"[DEBUG] Using call series '{event_base_title}' as base title for recurring Zoom/GCal/YouTube events.")

    # Zoom meeting creation/update
    zoom_id = None
    join_url = None
    meeting_updated = False # Flag to track if mapping needs update due to new/updated Zoom/GCal info
    reusing_series_meeting = False
    zoom_response = None # Store response for potential later use
    original_meeting_id_for_reuse = None # Store the original ID if reusing a series

    try:
        # 1. Parse time and duration first
        start_time, duration = parse_issue_for_time(issue_body)

        # 2. Check if we should skip Zoom API calls entirely
        if skip_zoom_creation:
            print("[DEBUG] Skipping Zoom meeting creation/update based on issue input or existing series.")
            if existing_series_entry_for_zoom:
                # Reuse existing meeting ID and link from the series
                zoom_id = existing_series_entry_for_zoom["meeting_id"]
                join_url = existing_series_entry_for_zoom.get("zoom_link", "Link not found in mapping")
                original_meeting_id_for_reuse = zoom_id # Store the ID we are reusing
                reusing_series_meeting = True
                print(f"[DEBUG] Reusing existing Zoom meeting {zoom_id} for call series '{call_series}'")
            else:
                # Skipped via issue input, need placeholder
                print("[DEBUG] Zoom creation skipped via issue input. Using placeholder Zoom ID.")
                zoom_id = f"placeholder-skipped-{issue.number}"
                join_url = "Zoom creation skipped via issue input"
        else:
            # Proceed with Zoom creation/update logic (as skip_zoom_creation is False)
            # No need to check for series again, just check for existing meeting tied to this issue
            print(f"[DEBUG] Proceeding with Zoom creation/update for issue #{issue_number}.")
            existing_item_for_issue = next(
                ((m_id, entry) for m_id, entry in mapping.items() if entry.get("issue_number") == issue.number),
                None
            )
            
            if existing_item_for_issue:
                # Update existing meeting tied to this specific issue number
                existing_zoom_meeting_id, existing_entry = existing_item_for_issue
                stored_start = existing_entry.get("start_time")
                stored_duration = existing_entry.get("duration")
                zoom_id = existing_zoom_meeting_id # Use the found ID
                join_url = existing_entry.get("zoom_link") # Use existing link initially

                if str(zoom_id).startswith("placeholder-"):
                    print(f"[DEBUG] Skipping Zoom update for placeholder ID: {zoom_id}")
                    join_url = join_url or "https://zoom.us (placeholder)"
                elif stored_start and stored_duration and (start_time == stored_start) and (duration == stored_duration):
                    print("[DEBUG] No changes detected in meeting start time or duration. Skipping Zoom update.")
                else:
                    print(f"[DEBUG] Updating Zoom meeting {zoom_id} based on changes in issue #{issue_number}.")
                    try:
                        zoom_response = zoom.update_meeting(
                            meeting_id=zoom_id,
                            topic=event_base_title, # Use call series or issue title
                            start_time=start_time,
                            duration=duration
                        )
                        comment_lines.append("\n**Zoom Meeting Updated**")
                        print("[DEBUG] Zoom meeting updated.")
                        meeting_updated = True
                        # Update join_url if response has it
                        if zoom_response and zoom_response.get('join_url'):
                            join_url = zoom_response.get('join_url')
                    except Exception as e:
                        print(f"[DEBUG] Error updating Zoom meeting {zoom_id}: {str(e)}")
                        comment_lines.append("\n**⚠️ Failed to update Zoom meeting. Please check credentials.**")
                        # Keep existing zoom_id and join_url
            else:
                # No meeting tied to this issue number, and not reusing a series meeting -> Create new
                print(f"[DEBUG] No existing meeting found for issue #{issue_number}. Creating new Zoom meeting.")
                try:
                    if is_recurring and occurrence_rate != "none":
                        join_url, zoom_id = zoom.create_recurring_meeting(
                            topic=event_base_title, # Use call series or issue title
                            start_time=start_time,
                            duration=duration,
                            occurrence_rate=occurrence_rate
                        )
                        comment_lines.append("\n**Recurring Zoom Meeting Created**")
                    else:
                        join_url, zoom_id = zoom.create_meeting(
                            topic=event_base_title, # Use call series or issue title
                            start_time=start_time,
                            duration=duration
                        )
                        comment_lines.append("\n**Zoom Meeting Created**")
                    
                    print(f"[DEBUG] Zoom meeting created with ID: {zoom_id}")
                    meeting_updated = True
                except Exception as e:
                    print(f"[DEBUG] Error creating Zoom meeting: {str(e)}")
                    comment_lines.append("\n**⚠️ Failed to create Zoom meeting. Please check credentials.**")
                    zoom_id = f"placeholder-{issue.number}"
                    join_url = "https://zoom.us (API authentication failed)"

    except ValueError as e:
        # Error parsing time/duration
        print(f"[DEBUG] Error parsing time/duration: {str(e)}")
        comment_lines.append(f"\n**⚠️ Error:** {str(e)} Please correct the format in the issue body.")
        # Can't proceed with Zoom/GCal/YT without time/duration
        # Post comment and exit handling for this issue? Or let it continue partially?
        # For now, set a placeholder to prevent downstream errors but allow mapping/commenting.
        zoom_id = f"placeholder-time-error-{issue.number}"
        join_url = "Invalid time/duration in issue"
    except Exception as e:
        # Catch other unexpected errors during Zoom processing
        print(f"[DEBUG] Unexpected error during Zoom processing: {str(e)}")
        comment_lines.append("\n**⚠️ Unexpected Zoom Processing Error.** Check logs.")
        zoom_id = f"placeholder-error-{issue.number}"
        join_url = "Error during Zoom processing"

    # Add Zoom link details to GitHub comment based on the flag
    if zoom_id and not str(zoom_id).startswith("placeholder-"):
        if reusing_series_meeting:
            comment_lines.append(f"\n**Zoom Meeting:** Reusing meeting {zoom_id} for series '{call_series}'.")
        # Add the join URL to the comment if the flag is set and link is valid
        if display_zoom_link_in_invite and join_url and not str(join_url).startswith("Zoom creation skipped"):
             comment_lines.append(f"- Zoom Link: {join_url}")
        # Add a note if the link is intentionally hidden
        elif not display_zoom_link_in_invite and join_url and not str(join_url).startswith("Zoom creation skipped"):
             comment_lines.append(f"- *Zoom link hidden from public view (check facilitator email)*")
        # Handle cases where join_url might be invalid even if zoom_id isn't a placeholder
        elif not join_url or str(join_url).startswith("Zoom creation skipped"):
             comment_lines.append(f"- *Zoom link not available or creation skipped.*")

    # Use zoom_id as the meeting_id (which is the mapping key)
    if zoom_id:
        meeting_id = str(zoom_id) # Ensure it's a string for mapping key
        if reusing_series_meeting and original_meeting_id_for_reuse:
            meeting_id = str(original_meeting_id_for_reuse) # CRITICAL: Use the ORIGINAL ID for mapping key
            print(f"[DEBUG] Reusing original meeting ID {meeting_id} for mapping key.")

        # Check if YT streams were created/reused
        if reusing_series_meeting and existing_series_entry_for_zoom and "youtube_streams" in existing_series_entry_for_zoom:
             youtube_streams = existing_series_entry_for_zoom["youtube_streams"]
             # We might have already added the comment for existing streams earlier
             # Let the existing logic handle adding YT stream comments if needed
        else:
             # Calculate youtube_streams based on need_youtube_streams and create if necessary
             # Initialize youtube_streams to None here
             occurrence_youtube_streams = None
             # Add the check for need_youtube_streams
             if is_recurring and occurrence_rate != "none" and need_youtube_streams:
                 # If we already have streams for this call series, reuse them
                 if existing_youtube_streams:
                     print(f"[DEBUG] Reusing existing YouTube streams for call series: {call_series}")
                     occurrence_youtube_streams = existing_youtube_streams
                     comment_lines.append("\n**Using Existing YouTube Stream Links**")
                 else:
                     # Only create new streams if needed
                     try:
                         print(f"[DEBUG] Creating YouTube streams for recurring meeting occurrence: {occurrence_rate}")
                         occurrence_youtube_streams = youtube_utils.create_recurring_streams(
                             title=issue_title, # Use the specific occurrence title
                             description=f"Recurring meeting: {issue_title}\nGitHub Issue: {issue.html_url}",
                             start_time=start_time,
                             occurrence_rate=occurrence_rate # Needs careful handling if only ONE stream is needed
                         )
                         
                         # Add stream URLs to comment
                         if occurrence_youtube_streams:
                             comment_lines.append("\n**YouTube Stream Links:**")
                             stream_links = []
                             for i, stream in enumerate(occurrence_youtube_streams, 1):
                                 # Extract date from stream details if available
                                 stream_date = ""
                                 if 'scheduled_time' in stream:
                                     try:
                                         # Import datetime in this scope
                                         from datetime import datetime
                                         # Parse the scheduled_time string to a datetime object
                                         scheduled_time = stream['scheduled_time']
                                         if scheduled_time.endswith('Z'):
                                             scheduled_time = scheduled_time.replace('Z', '+00:00')
                                         date_obj = datetime.fromisoformat(scheduled_time)
                                         # Format as "Mon DD, YYYY"
                                         stream_date = f" ({date_obj.strftime('%b %d, %Y')})"
                                     except Exception as e:
                                         print(f"[DEBUG] Error formatting stream date: {e}")
                                         # If parsing fails, leave date empty
                                         pass
                                 
                                 # Add date to stream links
                                 comment_lines.append(f"- Stream {i}{stream_date}: {stream['stream_url']}")
                                 stream_links.append(f"- Stream {i}{stream_date}: {stream['stream_url']}")
                             
                             # Update Discourse post with stream links if we have a topic ID
                             if topic_id and not str(topic_id).startswith("placeholder-"):
                                 try:
                                     discourse_content = f"{updated_body}\n\n**YouTube Stream Links:**\n" + "\n".join(stream_links)
                                     discourse.update_topic(
                                         topic_id=topic_id,
                                         body=discourse_content
                                     )
                                 except Exception as e:
                                     print(f"[DEBUG] Error updating Discourse topic with YouTube streams: {str(e)}")
                             
                             # Flag that streams were generated (will be saved in occurrence data later)
                             # mapping_updated = True # Handled later when saving occurrence
                     except Exception as e:
                         print(f"[DEBUG] Error creating YouTube streams: {str(e)}")
                         comment_lines.append("\n**⚠️ Failed to create YouTube streams. Please check credentials.**")
                         # occurrence_youtube_streams remains None if creation fails
             elif is_recurring:
                 # Recurring meeting, but streams not needed
                 print(f"[DEBUG] Recurring meeting detected, but YouTube streams were not requested")
             else:
                 # One-time meeting, upload handled later
                 print(f"[DEBUG] One-time meeting detected, YouTube upload will be handled after the meeting")

        # Calendar handling
        calendar_id = "c_upaofong8mgrmrkegn7ic7hk5s@group.calendar.google.com"
        # Base calendar description
        calendar_description = f"Issue: {issue.html_url}"
        # Append Zoom link to description if requested and available
        if display_zoom_link_in_invite and join_url and not str(join_url).startswith("Zoom creation skipped"):
            print("[DEBUG] Adding Zoom link to calendar description.")
            calendar_description += f"\n\nZoom Link: {join_url}"
        else:
            print("[DEBUG] Not adding Zoom link to calendar description (flag false or link unavailable).")
            
        event_link = None
        event_id = None # Initialize event_id
        event_result = None # Initialize event_result

        # Check ONLY already_on_calendar flag for skipping GCal
        if skip_gcal_creation:
            print("[DEBUG] Skipping Google Calendar event creation/update based on issue input or existing series.")
            if reusing_series_meeting: # Check if we reused Zoom series
                 if existing_series_entry_for_zoom and existing_series_entry_for_zoom.get("calendar_event_id"):
                     gcal_event_id_from_series = existing_series_entry_for_zoom.get("calendar_event_id")
                     # Construct a potential link (may not be perfect)
                     event_link = f"https://calendar.google.com/calendar/event?eid={gcal_event_id_from_series}" # Simplified link
                     comment_lines.append("\n**Calendar Event:** Reusing existing event for series.")
                     if event_link:
                         comment_lines.append(f"- [Approximate Google Calendar Link]({event_link})")
                     # Store the reused event ID for mapping
                     event_id = gcal_event_id_from_series 
                 else:
                     comment_lines.append("\n**Calendar Event:** Reusing existing event for series (Link/ID not found in mapping).")
            # else: GCal skipped via issue input, no comment needed as it was added earlier
        else:
            # Proceed with GCal creation/update logic based on mapping entry for meeting_id
            print(f"[DEBUG] Proceeding with Google Calendar check/update for meeting_id: {meeting_id}")
            # Find GCal event ID associated with this meeting_id in mapping
            gcal_event_id_from_mapping = mapping.get(meeting_id, {}).get("calendar_event_id")
            
            # --- Start of Restored GCal Logic ---
            if gcal_event_id_from_mapping:
                # Found existing event ID, try to update it
                print(f"[DEBUG] Found existing calendar event ID: {gcal_event_id_from_mapping}. Attempting update.")
                try:
                    base_event_id = extract_event_id_from_link(f"?eid={gcal_event_id_from_mapping}")
                    if is_recurring and occurrence_rate != "none":
                        event_result = gcal.update_recurring_event(
                            event_id=base_event_id,
                            summary=event_base_title, # Use call series or issue title
                            start_dt=start_time,
                            duration_minutes=duration,
                            calendar_id=calendar_id,
                            occurrence_rate=occurrence_rate,
                            description=calendar_description
                        )
                    else:
                         event_result = gcal.update_event(
                             event_id=base_event_id,
                             summary=event_base_title, # Use call series or issue title
                             start_dt=start_time,
                             duration_minutes=duration,
                             calendar_id=calendar_id,
                             description=calendar_description
                         )
                    
                    if event_result: # Check if update was successful
                        event_link = event_result.get('htmlLink')
                        event_id = event_result.get('id') # Assign event_id for mapping update
                        print(f"Updated calendar event: {event_link} with ID: {event_id}")
                        meeting_updated = True # Mark mapping for update
                        comment_lines.append("\n**Calendar Event Updated**")
                        if event_link: comment_lines.append(f"- [Google Calendar]({event_link})")
                    else:
                         # Handle case where update function might return None or empty dict on failure
                         print(f"[DEBUG] gcal.update function returned no result for {base_event_id}. Assuming update failed.")
                         gcal_event_id_from_mapping = None # Reset to trigger creation below

                except ValueError as e: # Specific error if event ID not found by gcal functions
                     print(f"[DEBUG] Calendar Event ID {gcal_event_id_from_mapping} not found, creating a new calendar event: {str(e)}")
                     gcal_event_id_from_mapping = None # Reset to trigger creation below
                except Exception as e:
                    print(f"[DEBUG] Failed to update calendar event {gcal_event_id_from_mapping}, creating new one instead: {str(e)}")
                    gcal_event_id_from_mapping = None # Reset to trigger creation below
            
            # Separate block for creation if no ID found OR update failed
            if not gcal_event_id_from_mapping:
                print(f"[DEBUG] No existing calendar event found or update failed. Creating new GCal event.")
                if start_time and duration: # Ensure we have time/duration before creating
                    try:
                        event_result = create_calendar_event(
                            is_recurring=is_recurring,
                            occurrence_rate=occurrence_rate,
                            summary=event_base_title, # Use call series or issue title
                            start_dt=start_time,
                            duration_minutes=duration,
                            calendar_id=calendar_id,
                            description=calendar_description
                        )
                        if event_result:
                            event_link = event_result.get('htmlLink')
                            event_id = event_result.get('id') # Assign event_id for mapping update
                            print(f"[DEBUG] Created new calendar event with ID: {event_id}")
                            meeting_updated = True # Mark mapping for update
                            comment_lines.append("\n**Calendar Event Created**")
                            if event_link: comment_lines.append(f"- [Google Calendar]({event_link})")
                        else:
                            # Handle case where create function might return None or empty dict on failure
                            print(f"::warning::Failed to create Calendar Event - create_calendar_event returned no result.")
                            comment_lines.append("\n**⚠️ Failed to create Calendar Event.** Check logs.")
                    except Exception as e:
                        print(f"::error::Error creating calendar event: {str(e)}")
                        comment_lines.append("\n**⚠️ Failed to create Calendar Event.** Check logs.")
                else:
                    print("[DEBUG] Skipping GCal creation due to missing start_time/duration.")
                    comment_lines.append("\n**Calendar Event:** Skipped creation due to missing time/duration in issue.")
            # --- End of Restored GCal Logic ---

        # --- Mapping Update Logic ---
        print(f"[DEBUG] Preparing to update mapping for meeting ID: {meeting_id}")

        # Get existing entry or initialize
        mapping_entry = mapping.get(meeting_id, {}).copy()

        # Ensure 'occurrences' list exists
        if "occurrences" not in mapping_entry:
            mapping_entry["occurrences"] = []

        # Create data for the current occurrence
        occurrence_data = {
            "occurrence_number": len(mapping_entry["occurrences"]) + 1,
            "issue_number": issue.number,
            "issue_title": issue.title,
            "discourse_topic_id": topic_id,
            "start_time": start_time if 'start_time' in locals() else None,
            "duration": duration if 'duration' in locals() else None,
            # Calculate skip_youtube_upload based on current issue's flags
            "skip_youtube_upload": need_youtube_streams and is_recurring and occurrence_rate != "none",
            # Initialize processing flags for this new occurrence
            "Youtube_upload_processed": False,
            "transcript_processed": False,
            "upload_attempt_count": 0,
            "transcript_attempt_count": 0,
            "telegram_message_id": None, # Placeholder for occurrence-specific message ID
            "youtube_streams_posted_to_discourse": False,
            # Add generated streams to the occurrence data
            "youtube_streams": occurrence_youtube_streams if 'occurrence_youtube_streams' in locals() else None
        }

        # Append the new occurrence data
        # Check if an occurrence with the same issue number already exists to prevent duplicates
        existing_occurrence_index = next((i for i, occ in enumerate(mapping_entry["occurrences"]) if occ.get("issue_number") == issue.number), -1)
        if existing_occurrence_index != -1:
            print(f"[DEBUG] Updating existing occurrence for issue #{issue.number} in mapping.")
            # Preserve existing processing flags if just updating metadata
            existing_flags = {
                "Youtube_upload_processed": mapping_entry["occurrences"][existing_occurrence_index].get("Youtube_upload_processed", False),
                "transcript_processed": mapping_entry["occurrences"][existing_occurrence_index].get("transcript_processed", False),
                "upload_attempt_count": mapping_entry["occurrences"][existing_occurrence_index].get("upload_attempt_count", 0),
                "transcript_attempt_count": mapping_entry["occurrences"][existing_occurrence_index].get("transcript_attempt_count", 0),
                "youtube_streams_posted_to_discourse": mapping_entry["occurrences"][existing_occurrence_index].get("youtube_streams_posted_to_discourse", False)
            }
            occurrence_data.update(existing_flags) # Keep existing flags
            # Update occurrence number just in case list order changed (though unlikely)
            occurrence_data["occurrence_number"] = mapping_entry["occurrences"][existing_occurrence_index].get("occurrence_number", occurrence_data["occurrence_number"])
            mapping_entry["occurrences"][existing_occurrence_index] = occurrence_data
        else:
            print(f"[DEBUG] Adding new occurrence for issue #{issue.number} to mapping.")
            mapping_entry["occurrences"].append(occurrence_data)

        # Update series-level info (only if missing/being set for the first time)
        series_updated = False
        if "meeting_id" not in mapping_entry:
            mapping_entry["meeting_id"] = meeting_id; series_updated = True
        if "is_recurring" not in mapping_entry:
            mapping_entry["is_recurring"] = is_recurring; series_updated = True
        if "occurrence_rate" not in mapping_entry or mapping_entry["occurrence_rate"] == "none":
            mapping_entry["occurrence_rate"] = occurrence_rate if is_recurring else "none"; series_updated = True
        if "call_series" not in mapping_entry and call_series:
            mapping_entry["call_series"] = call_series; series_updated = True
        if "zoom_link" not in mapping_entry and join_url and not str(join_url).startswith("https://zoom.us (API"):
            mapping_entry["zoom_link"] = join_url; series_updated = True
        if "calendar_event_id" not in mapping_entry and event_id:
            mapping_entry["calendar_event_id"] = event_id; series_updated = True
        # Store youtube_streams only if generated AND not already present at series level
        if "youtube_streams" not in mapping_entry and 'youtube_streams' in locals() and occurrence_youtube_streams:
            mapping_entry["youtube_streams"] = occurrence_youtube_streams; series_updated = True
        # Store telegram_message_id only if generated AND not already present at series level
        current_telegram_id = locals().get("message_id")
        if "telegram_message_id" not in mapping_entry and current_telegram_id:
            # Deprecated: telegram_message_id is now per-occurrence
            # mapping_entry["telegram_message_id"] = current_telegram_id; series_updated = True
            pass

        # Always update the mapping with the potentially modified entry (contains new occurrence)
        # Check if the overall entry has changed before marking for saving
        original_entry_before_update = mapping.get(meeting_id, {}).copy()
        if original_entry_before_update != mapping_entry:
            mapping[meeting_id] = mapping_entry
            mapping_updated = True # Mark that the mapping file needs saving
            print(f"Mapping updated for meeting ID {meeting_id} with occurrence details from issue #{issue_number}.")
            if series_updated:
                print(f"[DEBUG] Series-level information updated for {meeting_id}.")
        else:
            print(f"[DEBUG] Mapping entry for {meeting_id} remains unchanged.")

        # --- Notification Logic ---
        print("[DEBUG] Entering Notification Block")
        # Extract facilitator information
        facilitator_emails = extract_facilitator_info(issue_body)
        
        # Initialize flags
        email_sent = False
        telegram_channel_sent = False 

        # --- Email Sending --- 
        # Send email ONLY if we have facilitator emails AND a valid join_url
        emails_sent_count = 0
        emails_failed = []

        if not facilitator_emails:
            print(f"[DEBUG] No facilitator emails provided, skipping email notification.")
            comment_lines.append("- Facilitator emails not found in issue, skipping email notification.")
        elif not join_url or str(join_url).startswith("https://zoom.us (API") or str(join_url).startswith("Zoom creation skipped") or str(join_url).startswith("Invalid time/duration"):
            print(f"[DEBUG] No valid Zoom join URL ({join_url}), skipping email notification.")
            comment_lines.append(f"- Zoom Join URL invalid or missing, skipping email notification.")
        else:
            # Proceed with sending email
            email_subject = f"Zoom Meeting Details for {issue_title}"
            email_body = f"""
<h2>Zoom Meeting Details</h2>
<p>For meeting: {issue_title}</p>
<p><strong>Join URL:</strong> <a href="{join_url}">{join_url}</a></p>
<p><strong>Meeting ID:</strong> {zoom_id}</p>
<p><strong>Links:</strong><br>
<a href="{issue.html_url}">View GitHub Issue</a><br>
<a href="{discourse_url}">View Discourse Topic</a></p>

<p>---<br>
This email was sent automatically by the Ethereum Protocol Call Bot.</p>
"""

            for email in facilitator_emails:
                try:
                    print(f"[DEBUG] Attempting to send Zoom details email to: {email}")
                    if email_utils.send_email(email, email_subject, email_body):
                        emails_sent_count += 1
                        print(f"[DEBUG] Successfully sent email to: {email}")
                    else:
                        emails_failed.append(email)
                        print(f"[DEBUG] Failed to send email to: {email}")
                except Exception as e:
                    emails_failed.append(email)
                    print(f"[DEBUG] Exception sending email to {email}: {str(e)}")
                    comment_lines.append(f"- ⚠️ Exception sending email to {email}: {str(e)}")

            # Update comment based on success/failure
            if emails_sent_count > 0:
                 sent_to_emails = [e for e in facilitator_emails if e not in emails_failed]
                 comment_lines.append(f"- Zoom details sent via email to: {', '.join(sent_to_emails)}")
            if emails_failed:
                sender_email = os.environ.get("SENDER_EMAIL")
                smtp_server = os.environ.get("SMTP_SERVER")
                comment_lines.append(f"- ⚠️ Failed to send email with Zoom details to: {', '.join(emails_failed)}")
                if not sender_email or not smtp_server:
                    comment_lines.append(f"  - *Note*: Email service is not fully configured. Contact the repository administrator.")
                else:
                    comment_lines.append(f"  - Please check the GitHub Actions logs for more details")

        # --- Telegram Channel Posting --- 
        # Send Telegram regardless of Zoom status, as long as basic info is available
        # Ensure discourse_url is valid before proceeding
        if not discourse_url or discourse_url == "https://ethereum-magicians.org (API error occurred)":
             print("[DEBUG] Skipping Telegram notification - Discourse URL not available.")
             comment_lines.append("\n**Telegram Notification**")
             comment_lines.append("- Skipped: Discourse URL not available.")
        else:
            # Proceed with Telegram message generation
            # Find the current occurrence data to get generated streams
            current_occurrence = next((occ for occ in mapping_entry.get("occurrences", []) if occ.get("issue_number") == issue.number), None)
            if not current_occurrence:
                 print(f"[ERROR] Could not find current occurrence for issue {issue.number} to generate Telegram message.")
                 comment_lines.append("\n**⚠️ Failed to send Telegram message: Could not find occurrence data.**")
            else:
                # Build the message
                telegram_message_body = (
                    f"<b>{issue_title}</b>\n\n"
                    f"<b>Links:</b>\n"
                    f"• <a href='{discourse_url}'>Discourse Topic</a>\n"
                    f"• <a href='{issue.html_url}'>GitHub Issue</a>\n"
                )
                if event_link:
                    telegram_message_body += f"• <a href='{event_link}'>Google Calendar</a>\n"

                # Add occurrence-specific YouTube streams if they exist
                occurrence_streams = current_occurrence.get("youtube_streams")
                if occurrence_streams:
                    telegram_message_body += f"\n<b>YouTube Stream Links:</b>\n"
                    for i, stream in enumerate(occurrence_streams):
                        stream_url = stream.get('stream_url')
                        if stream_url:
                            telegram_message_body += f"• <a href='{stream_url}'>Stream {i+1}</a>\n"

                # Send the message
                telegram_channel_id = os.environ.get("TELEGRAM_CHAT_ID")
                if telegram_channel_id and tg:
                    try:
                        print(f"[DEBUG] Sending new Telegram channel message for occurrence (Issue #{issue.number}).")
                        message_id = tg.send_message(telegram_message_body)
                        if message_id:
                            telegram_channel_sent = True
                            # Store the message ID within the *current occurrence* object
                            current_occurrence_index = next((i for i, occ in enumerate(mapping_entry["occurrences"]) if occ.get("issue_number") == issue.number), -1)
                            if current_occurrence_index != -1:
                                mapping_entry["occurrences"][current_occurrence_index]["telegram_message_id"] = message_id
                                mapping_updated = True
                                print(f"[DEBUG] Stored telegram_message_id {message_id} in occurrence data for issue #{issue.number}.")
                            else:
                                print(f"[ERROR] Could not find occurrence for issue #{issue.number} to store telegram_message_id.")
                        
                        if telegram_channel_sent:
                            comment_lines.append("\n**Telegram Notification**")
                            comment_lines.append("- Sent message for this occurrence to Ethereum Protocol Updates channel")
                        else:
                            comment_lines.append("\n**⚠️ Failed to send Telegram message for this occurrence**")
                            print(f"[DEBUG] Failed to send/update Telegram channel message.")

                    except Exception as e:
                        print(f"[ERROR] Telegram channel notification failed: {e}")
                        comment_lines.append(f"\n**⚠️ Telegram Channel Notification Failed**: {str(e)}")
                else:
                    print("[DEBUG] Telegram channel ID not configured or tg module not available.")

        # --- RSS Notification Adding --- 
        # Ensure we have occurrence_issue_number before adding RSS
        occurrence_issue_number_rss = occurrence_data.get("issue_number")
        if occurrence_issue_number_rss:
            try:
                print("[DEBUG] Adding notifications to RSS feed data")
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    occurrence_issue_number_rss, # Pass issue number to identify occurrence
                    "issue_processed",
                    f"GitHub issue #{occurrence_issue_number_rss} processed ({action})",
                    issue.html_url
                )
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    occurrence_issue_number_rss, # Pass issue number to identify occurrence
                    "discourse_post",
                    f"Discourse topic {action}: {issue_title}",
                    discourse_url
                )
                # Add more RSS notifications as needed (e.g., for GCal, Zoom)
                mapping_updated = True # RSS utils likely modifies mapping indirectly
            except Exception as e:
                print(f"[ERROR] Failed to add RSS notifications: {e}")
                comment_lines.append(f"\n**⚠️ Failed to update RSS data**: {str(e)}")
        else:
            print(f"[ERROR] Could not add RSS notification - occurrence issue number missing.")

    # --- End of Notification Block ---
    else:
        # zoom_id was not determined (likely due to errors)
        print("[ERROR] zoom_id could not be determined. Skipping downstream processing and mapping update.")
        comment_lines.append("\n**⚠️ Critical Error:** Could not determine Zoom Meeting ID. Processing halted.")

    # --- Final Comment Posting & Mapping Commit Logic --- 
    print("[DEBUG] Entering Final Comment Posting & Mapping Commit Logic")
    # 1. Post consolidated comment to GitHub Issue
    if comment_lines:
        now = dt.now().strftime("%Y-%m-%d %H:%M UTC")
        # Try to find the existing action line to update timestamp
        action_line_index = -1
        for i, line in enumerate(comment_lines):
            # Match lines like "- Action: Created" or "- Action: Updated"
            if re.match(r"-\s+Action:\s+(Created|Updated|Failed)", line):
                action_line_index = i
                break
        if action_line_index != -1:
            comment_lines[action_line_index] = f"- Action: {action.capitalize()} at {now}"
        else: # Add action line if it wasn't present (e.g., only errors occurred)
            comment_lines.insert(0, f"- Action: Bot processing finished at {now}") # Add at the beginning
            
        comment_text = "\n".join(comment_lines)
        
        # Check for existing comments by the bot to update instead of creating new
        existing_comment = None
        try:
            comments = issue.get_comments()
            for comment in comments:
                if comment.user.login == "github-actions[bot]":
                    existing_comment = comment
                    print(f"[DEBUG] Found existing bot comment ID: {existing_comment.id}")
                    break
        except Exception as e:
            print(f"::warning::Could not fetch existing comments: {e}")
        
        # Update or create comment
        try:
            if existing_comment:
                print(f"[DEBUG] Attempting to update existing comment {existing_comment.id}")
                existing_comment.edit(comment_text)
                print(f"Successfully updated existing comment {existing_comment.id}")
            else:
                print("[DEBUG] Attempting to create new comment")
                new_comment = issue.create_comment(comment_text)
                print(f"Successfully created new comment ID: {new_comment.id}")
        except Exception as e:
            print(f"::error::Failed to create or update GitHub comment: {e}")
            # Don't append to comment_lines here as we can't post it

    # 2. Commit mapping file if it was updated
    # Remove any null mappings or failed entries before saving
    # Filter based on existence of meeting_id and occurrences list having at least one entry with discourse_topic_id
    mapping = {
        str(k): v for k, v in mapping.items()
        if isinstance(v, dict) and v.get("meeting_id") and
        (
            # For non-recurring, check top-level discourse ID
            (not v.get("is_recurring") and v.get("discourse_topic_id")) or
            # For recurring, check if occurrences list exists and has entries
            (v.get("is_recurring") and isinstance(v.get("occurrences"), list) and len(v.get("occurrences")) > 0)
        )
    }

    if mapping_updated:
        print("[DEBUG] Mapping was updated, attempting to save and commit.")
        try:
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
            print(f"Successfully saved and committed mapping file.")
            # Include meeting_id in final print statement if available
            final_meeting_id_str = f" Zoom Meeting ID {meeting_id}" if 'meeting_id' in locals() else ""
            print(f"Mapping final update complete.{final_meeting_id_str} -> Discourse Topic ID {topic_id}")
        except Exception as e:
            print(f"::error::Failed to save or commit mapping file: {e}")
    else:
         print("[DEBUG] No changes detected in mapping, skipping commit.")

def parse_issue_for_time(issue_body: str):
    """
    Parses the issue body to extract a start time and duration based on possible formats:
    
    - Date/time line followed by a duration line (with or without "Duration in minutes" preceding it)
    - Accepts both abbreviated and full month names
    - Handles formats like "Apr 22 (Tues), 2025, 14:00 UTC"
    """
    
    # -------------------------------------------------------------------------
    # 1. Regex pattern to find the date/time in the issue body
    # -------------------------------------------------------------------------
    # Original pattern
    date_pattern = re.compile(
        r"""
        \[?                                        # Optional opening bracket
        (?:(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+)?    # Optional day of the week
        (?P<month>[A-Za-z]{3,9})\s+               # Full or abbreviated month name
        (?P<day>\d{1,2}),?\s+                      # Day of the month, comma optional
        (?P<year>\d{4}),?\s+                       # Year, comma optional
        (?P<hour>\d{1,2}):(?P<minute>\d{2})        # Start time HH:MM
        (?:-(?P<end_hour>\d{1,2}):(?P<end_minute>\d{2}))?  # Optional end time HH:MM
        \s*UTC                                     # UTC timezone
        \]?                                        # Optional closing bracket
        """,
        re.IGNORECASE | re.VERBOSE
    )
    
    # Alternative pattern for PeerDAS format: "Apr 22 (Tues), 2025, 14:00 UTC"
    alt_date_pattern = re.compile(
        r"""
        (?P<month>[A-Za-z]{3,9})\s+                # Month name (abbreviated or full)
        (?P<day>\d{1,2})                           # Day number
        \s*(?:\([A-Za-z]{3,4}\))?,?\s*            # Optional day of week in parentheses, optional comma
        (?P<year>\d{4}),?\s*                      # Year, optional comma
        (?P<hour>\d{1,2}):(?P<minute>\d{2})        # Start time HH:MM
        (?:\s*-\s*(?P<end_hour>\d{1,2}):(?P<end_minute>\d{2}))?  # Optional end time HH:MM
        \s*UTC                                     # UTC timezone
        """,
        re.IGNORECASE | re.VERBOSE
    )

    # Try original pattern first
    date_match = date_pattern.search(issue_body)
    if not date_match:
        # Try alternative pattern
        date_match = alt_date_pattern.search(issue_body)
        
    if not date_match:
        # Try to find any date-like mentions in the issue
        date_samples = re.findall(r'[A-Za-z]+\s+\d{1,2}(?:,?\s*\d{4})(?:,?\s*\d{1,2}:\d{2})?', issue_body)
        time_samples = re.findall(r'\d{1,2}:\d{2}\s*(?:UTC|GMT|EST|PST|[+-]\d{2}:\d{2})?', issue_body)
        error_msg = "Missing or invalid date/time format."
        
        if date_samples or time_samples:
            error_msg += f" Found potential date/time fragments: {', '.join(date_samples[:2])} {', '.join(time_samples[:2])}"
        
        print(f"[DEBUG] Could not match date pattern. Issue body excerpt: '{issue_body[:200].replace(chr(10), ' ')}'")
        raise ValueError(error_msg)

    month = date_match.group('month')
    day = date_match.group('day')
    year = date_match.group('year')
    hour = date_match.group('hour')
    minute = date_match.group('minute')
    end_hour = date_match.group('end_hour')
    end_minute = date_match.group('end_minute')

    # Construct the datetime string
    datetime_str = f"{month} {day} {year} {hour}:{minute}"
    try:
        start_dt = dt.strptime(datetime_str, "%B %d %Y %H:%M")  # Full month name
    except ValueError:
        try:
            start_dt = dt.strptime(datetime_str, "%b %d %Y %H:%M")  # Abbreviated month name
        except ValueError as e:
            raise ValueError(f"Unable to parse the start time: {e}")

    # Convert to UTC ISO format with Z suffix for Zoom API
    start_time_utc = start_dt.isoformat() + "Z"
    
    # For debugging timezone issues
    print(f"[DEBUG] Parsed date: {month} {day}, {year} at {hour}:{minute} UTC")
    print(f"[DEBUG] Formatted as ISO 8601 for API: {start_time_utc}")
    print(f"[DEBUG] Day of week: {start_dt.strftime('%A')}")

    # -------------------------------------------------------------------------
    # 2. Extract duration from issue body using a unified regex
    # -------------------------------------------------------------------------
    duration_match = re.search(
        r"(?i)duration(?:\s*(?:in)?\s*minutes)?[:\s-]*(\d+)\s*(?:minutes|min|m)?\b",
        issue_body
    )
    if not duration_match:
        # Fallback: match a line starting with '-' followed by a number (e.g., '- 15 minutes')
        duration_match = re.search(
            r"(?m)^\s*-\s*(\d+)\s*(?:minutes|min|m)?\b",
            issue_body
        )
    
    if duration_match:
        return start_time_utc, int(duration_match.group(1))

    # -------------------------------------------------------------------------
    # 3. If an end time is provided, compute duration from start and end times.
    # -------------------------------------------------------------------------
    if end_hour and end_minute:
        end_time_str = f"{month} {day} {year} {end_hour}:{end_minute}"
        try:
            end_dt = dt.strptime(end_time_str, "%B %d %Y %H:%M")
        except ValueError:
            end_dt = dt.strptime(end_time_str, "%b %d %Y %H:%M")

        if end_dt <= start_dt:
            raise ValueError("End time must be after start time.")

        duration_minutes = int((end_dt - start_dt).total_seconds() // 60)
        return start_time_utc, duration_minutes

    # No valid duration found
    raise ValueError("Missing or invalid duration format. Provide duration in minutes after the date/time.")

def commit_mapping_file():
    file_path = MAPPING_FILE
    commit_message = "Update meeting-topic mapping"
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    author = InputGitAuthor(
        name="GitHub Actions Bot",
        email="actions@github.com"
    )
    
    # Add repo initialization
    token = os.environ["GITHUB_TOKEN"]
    repo_name = os.environ["GITHUB_REPOSITORY"]
    g = Github(token)
    repo = g.get_repo(repo_name)

    # Read the LOCAL updated file content
    with open(file_path, "r") as f:
        file_content = f.read()

    try:
        # Get the CURRENT file state from repository
        contents = repo.get_contents(file_path, ref=branch)
        
        # Verify we're updating the correct file
        if contents.path != file_path:
            raise ValueError(f"Path mismatch: {contents.path} vs {file_path}")

        # Perform the update
        update_result = repo.update_file(
            path=contents.path,
            message=commit_message,
            content=file_content,
            sha=contents.sha,
            branch=branch,
            author=author,
        )
        print(f"Successfully updated {file_path} in repository. Commit SHA: {update_result['commit'].sha}")
        
    except Exception as e:
        # If file doesn't exist, create it
        if isinstance(e, Exception) and "404" in str(e):
            print(f"Creating new file {file_path} as it doesn't exist in repo")
            repo.create_file(
                path=file_path,
                message=commit_message,
                content=file_content,
                branch=branch,
                author=author,
            )
        else:
            print(f"Failed to commit mapping file: {str(e)}")
            raise

def create_calendar_event(is_recurring, occurrence_rate, **kwargs):
    """Helper function to create the appropriate type of calendar event"""
    print(f"[DEBUG] Creating calendar event: is_recurring={is_recurring}, occurrence_rate={occurrence_rate}")
    
    if is_recurring and occurrence_rate != "none":
        print(f"[DEBUG] Creating recurring calendar event with occurrence_rate={occurrence_rate}")
        return gcal.create_recurring_event(
            occurrence_rate=occurrence_rate,
            **kwargs
        )
    else:
        print(f"[DEBUG] Creating standard (non-recurring) calendar event")
        return gcal.create_event(**kwargs)

def extract_event_id_from_link(event_link):
    """
    Extract the Google Calendar event ID from the event link.
    For recurring events, Google Calendar uses a format like:
    base_event_id_20250326T030000Z
    
    We need to extract just the base event ID for updates to work properly.
    """
    if not event_link:
        return None
        
    try:
        # First try to extract the eid parameter from the URL
        import re
        import urllib.parse
        
        # Parse the URL to extract the eid parameter
        result = re.search(r'[?&]eid=([^&]+)', event_link)
        if result:
            eid = result.group(1)
            # Clean up any URL encoding
            eid = urllib.parse.unquote(eid)
            # Remove any trailing parameters or @ sections
            if ' ' in eid:
                eid = eid.split(' ')[0]
            if '@' in eid:
                eid = eid.split('@')[0]
            
            # For recurring events, Google Calendar adds a date suffix
            # Example: base_id_20250326T030000Z
            # We need just the base event ID for API operations
            base_id_match = re.match(r'([^_]+)(?:_\d{8}T\d{6}Z)?', eid)
            if base_id_match:
                base_id = base_id_match.group(1)
                print(f"[DEBUG] Extracted base event ID: {base_id} from full ID: {eid}")
                return base_id
                
            print(f"[DEBUG] Extracted event ID: {eid}")
            return eid
            
        # Fallback: Just strip anything after a space or @
        if 'eid=' in event_link:
            eid = event_link.split('eid=')[1]
            if ' ' in eid:
                eid = eid.split(' ')[0]
            if '@' in eid:
                eid = eid.split('@')[0]
                
            # For recurring events, extract the base ID
            base_id_match = re.match(r'([^_]+)(?:_\d{8}T\d{6}Z)?', eid)
            if base_id_match:
                base_id = base_id_match.group(1)
                print(f"[DEBUG] Extracted base event ID (fallback): {base_id} from full ID: {eid}")
                return base_id
                
            print(f"[DEBUG] Extracted event ID (fallback): {eid}")
            return eid
    except Exception as e:
        print(f"Error extracting event ID from link: {e}")
        # If we can't parse it, just store the whole link to be safe
        return event_link
        
    return None

def analyze_zoom_occurrences(response_data, start_dt, occurrence_rate):
    """
    Analyzes Zoom meeting occurrences to detect patterns and potential issues
    Args:
        response_data: Zoom API response containing occurrences
        start_dt: Original requested start datetime
        occurrence_rate: weekly, bi-weekly, or monthly
    Returns:
        Dictionary with analysis results
    """
    import calendar
    from datetime import datetime
    
    results = {
        "has_mismatches": False,
        "first_occurrence_mismatch": False,
        "day_pattern_type": None,  # "calendar_day", "weekday", "weekly" or "mixed"
        "specific_dates": []
    }
    
    # Only analyze if we have occurrences
    if 'occurrences' not in response_data or not response_data['occurrences']:
        return results
        
    occurrences = response_data['occurrences']
    
    # Check if the first occurrence matches our intended start date
    if len(occurrences) > 0:
        first_occurrence = occurrences[0]
        first_occurrence_time = first_occurrence.get('start_time')
        if first_occurrence_time:
            first_occurrence_dt = datetime.fromisoformat(first_occurrence_time.replace('Z', '+00:00'))
            
            # Original date might be a string, convert if needed
            if isinstance(start_dt, str):
                if start_dt.endswith('Z'):
                    start_dt = start_dt.replace('Z', '+00:00')
                original_dt = datetime.fromisoformat(start_dt)
            else:
                original_dt = start_dt
                
            # Compare calendar days
            if original_dt.date() != first_occurrence_dt.date():
                results["first_occurrence_mismatch"] = True
                results["has_mismatches"] = True
    
    # Analyze the pattern of occurrences
    if len(occurrences) >= 2:
        # Get dates and weekdays for all occurrences
        dates = []
        days_of_month = []
        weekdays = []
        weekday_positions = []
        
        for occurrence in occurrences:
            occurrence_time = occurrence.get('start_time')
            if occurrence_time:
                occurrence_dt = datetime.fromisoformat(occurrence_time.replace('Z', '+00:00'))
                dates.append(occurrence_dt)
                days_of_month.append(occurrence_dt.day)
                weekdays.append(occurrence_dt.weekday())
                
                # Calculate weekday position (1st, 2nd, 3rd, 4th, or 5th)
                week_number = (occurrence_dt.day - 1) // 7 + 1
                weekday_positions.append(week_number)
                
                # Add to specific dates
                results["specific_dates"].append({
                    "date": occurrence_dt.strftime("%Y-%m-%d"),
                    "weekday": calendar.day_name[occurrence_dt.weekday()],
                    "position": week_number
                })
        
        # Determine what kind of recurrence pattern this is
        
        # Calculate intervals between consecutive dates
        intervals = [(dates[i+1] - dates[i]).days for i in range(len(dates)-1)]
        
        # Check for consistent intervals
        unique_intervals = set(intervals)
        
        # Weekly pattern: all intervals are 7 days
        if unique_intervals == {7}:
            results["day_pattern_type"] = "weekly"
            # Check if this was supposed to be monthly
            if occurrence_rate == "monthly":
                results["has_mismatches"] = True
        
        # Bi-weekly pattern: all intervals are 14 days
        elif unique_intervals == {14}:
            results["day_pattern_type"] = "bi-weekly"
            # Check if this was supposed to be monthly
            if occurrence_rate == "monthly":
                results["has_mismatches"] = True
        
        # Monthly by same day: all days of month are the same
        elif len(set(days_of_month)) == 1:
            results["day_pattern_type"] = "calendar_day" 
        
        # Monthly by same weekday: all weekdays are the same and positions follow a monthly pattern
        elif len(set(weekdays)) == 1:
            # Check for consistent monthly patterns - days should be approximately 28-31 days apart
            monthly_intervals = [interval for interval in intervals if 27 <= interval <= 35]
            if len(monthly_intervals) > 0:
                results["day_pattern_type"] = "weekday"
            else:
                # If weekdays are consistent but not monthly, it might be weekly on same weekday
                results["day_pattern_type"] = "weekly"
                if occurrence_rate == "monthly":
                    results["has_mismatches"] = True
        
        # Mixed or unclear pattern
        else:
            results["day_pattern_type"] = "mixed"
            results["has_mismatches"] = True
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Handle GitHub issue and create/update Discourse topic.")
    parser.add_argument("--issue_number", required=True, type=int, help="GitHub issue number")
    parser.add_argument("--repo", required=True, help="GitHub repository (e.g., 'org/repo')")
    args = parser.parse_args()

    if not args.issue_number or not args.repo:
        print("Empty issue number or repository provided. Exiting without processing.")
        sys.exit(0)

    handle_github_issue(issue_number=args.issue_number, repo_name=args.repo)


if __name__ == "__main__":
    main()
