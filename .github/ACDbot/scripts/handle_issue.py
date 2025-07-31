# DEPRECATED: This script is being replaced by handle_protocol_call.py
import os
import sys
import argparse
from modules import discourse, zoom, gcal, email_utils, tg, rss_utils
# Import the custom exception again
from modules.discourse import DiscourseDuplicateTitleError
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
            # Add error handling for invalid JSON
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"::error::Failed to decode JSON from {MAPPING_FILE}. Returning empty mapping.")
                return {}
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
    - "Facilitator email: email5"
    Returns a list of email addresses.
    """
    pattern_list = r"(?im)^Facilitator emails:\s*(.+)"
    pattern_markdown = r"(?im)^-\s*Facilitator email:\s*\[([^]]+)\]\(mailto:[^)]+\)"
    # Combined pattern for plain text email, dash optional
    pattern_plain_combined = r"(?im)^(?:-\s*)?Facilitator email:\s*([^@\s]+@[^@\s\n]+)"
    print(f"[DEBUG] Extracting facilitator emails from issue body")

    facilitator_emails = []

    # Try matching the comma-separated list format first
    match_list = re.search(pattern_list, issue_body)
    if match_list:
        emails_str = match_list.group(1)
        found_emails = [email.strip() for email in emails_str.split(',') if email.strip()]
        facilitator_emails.extend(found_emails)
    else:
        # If list format not found, try the single email formats
        # Try markdown link first (as it's more specific with the dash)
        match_markdown = re.search(pattern_markdown, issue_body)
        if match_markdown:
            facilitator_emails.append(match_markdown.group(1).strip())
        else:
            # Then try the combined plain text pattern (dash optional)
            match_plain_combined = re.search(pattern_plain_combined, issue_body)
            if match_plain_combined:
                facilitator_emails.append(match_plain_combined.group(1).strip())
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
    display_pattern = r"display zoom link in invite\s*:\s*(true|false)"
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

    # Ensure meeting_id is always defined
    meeting_id = None

    # 1. Connect to GitHub API
    gh = Github(os.environ["GITHUB_TOKEN"])
    repo = gh.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue_title = issue.title
    issue_body = issue.body or "(No issue body provided.)"

    # Initialize potentially missing variables
    start_time = None
    duration = None

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

    # 2. Check for existing topic_id and previous details by searching mapping correctly
    topic_id = None
    previous_zoom_id = None
    previous_join_url = None
    found_meeting_id_for_issue = None
    existing_occurrence_data = None
    is_first_run_for_issue = True # Flag to track if this is the first time processing THIS issue

    print(f"[DEBUG] Searching mapping for existing data related to issue #{issue_number}")
    # Iterate through top-level meeting entries
    for m_id, entry_data in mapping.items():
        # Check if issue number is directly under this meeting ID (for non-recurring/older format)
        if entry_data.get("issue_number") == issue_number:
            found_meeting_id_for_issue = m_id
            existing_occurrence_data = entry_data # Treat top-level as the occurrence data
            print(f"[DEBUG] Found issue #{issue_number} directly under meeting_id {m_id}.")
            break # Found it

        # If not found directly, check inside occurrences list if it exists
        elif "occurrences" in entry_data and isinstance(entry_data["occurrences"], list):
            for occurrence in entry_data["occurrences"]:
                if isinstance(occurrence, dict) and occurrence.get("issue_number") == issue_number:
                    found_meeting_id_for_issue = m_id # The meeting ID this occurrence belongs to
                    existing_occurrence_data = occurrence
                    print(f"[DEBUG] Found issue #{issue_number} within occurrences of meeting_id {m_id}.")
                    break # Found the occurrence
            if found_meeting_id_for_issue: # Break outer loop if found in inner loop
                break

    # Now use the found data (if any) to set initial topic_id and previous Zoom details
    if found_meeting_id_for_issue and existing_occurrence_data:
        print(f"[DEBUG] Processing data found for issue #{issue_number} under meeting_id {found_meeting_id_for_issue}")
        is_first_run_for_issue = False # Found existing data for this issue, so not the first run
        # Get potential topic ID from the occurrence data itself
        potential_topic_id = existing_occurrence_data.get("discourse_topic_id")
        if potential_topic_id and not str(potential_topic_id).startswith("placeholder"):
            topic_id = potential_topic_id
            print(f"[DEBUG] Found valid existing topic_id {topic_id} in mapping for issue {issue_number}.")
        else:
            print(f"[DEBUG] Found mapping entry for issue {issue_number}, but discourse_topic_id is missing or placeholder: {potential_topic_id}")

        # Get previous Zoom details from the TOP-LEVEL meeting entry associated with this issue
        # Only store the meeting ID, not the link (as per updated requirements)
        series_data = mapping.get(found_meeting_id_for_issue, {}) # Get the main dict for the meeting_id
        previous_zoom_id = series_data.get("meeting_id") # which is the key itself
        print(f"[DEBUG] Found previous Zoom meeting ID associated with issue #{issue_number} (meeting_id {found_meeting_id_for_issue}): ID={previous_zoom_id}")
    else:
        print(f"[DEBUG] No previous mapping entry found containing issue #{issue_number}. Assuming new meeting context.")

    issue_link = f"[GitHub Issue]({issue.html_url})"
    updated_body = f"{issue_body}\n\n{issue_link}"

    # Initialize discourse_url to ensure it has a value
    discourse_url = None
    action = None # Initialize action
    # 3. Discourse handling
    # First, check if we already have a valid topic_id from the mapping search above
    if topic_id: # We already established this is a valid, non-placeholder ID from mapping
        print(f"[DEBUG] Updating existing Discourse topic {topic_id} based on mapping.")
        try:
            update_response = discourse.update_topic(
                topic_id=topic_id,
                title=issue_title,
                body=updated_body,
                category_id=63
            )
            action = "updated"
            discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
            comment_lines.append(f"**Discourse Topic ID:** {topic_id}")
            comment_lines.append(f"- Action: {action.capitalize()}")
            comment_lines.append(f"- URL: {discourse_url}")
        except DiscourseDuplicateTitleError as e:
            print(f"[ERROR] Failed to update topic {topic_id} title due to duplicate: {e}")
            comment_lines.append("\n**⚠️ Discourse Topic Error**")
            comment_lines.append(f"- Failed to update topic {topic_id}: Title '{e.title}' already exists.")
            # Keep the existing valid topic_id and URL, but mark action as failed update
            action = "update_failed_duplicate_title"
            discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
        except Exception as e:
            print(f"[ERROR] Failed to update existing Discourse topic {topic_id}: {str(e)}")
            comment_lines.append("\n**⚠️ Discourse Topic Error**")
            comment_lines.append(f"- Failed to update existing topic {topic_id}: {str(e)}")
            # Keep existing topic_id but mark action as failed for comment
            action = "update_failed"
            discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}" # Keep original URL for comment if possible

    else:
        # No valid topic_id found in mapping for this issue, attempt to create
        print(f"[DEBUG] No valid topic_id found in mapping for issue #{issue_number}. Attempting to create Discourse topic: '{issue_title}'")
        try:
            discourse_response = discourse.create_topic(
                title=issue_title,
                body=updated_body,
                category_id=63
            )
            topic_id = discourse_response.get("topic_id")
            action = discourse_response.get("action", "failed") # Should be 'created'

            if not topic_id:
                # This case might be less likely now with specific exceptions, but keep as safeguard
                raise ValueError(f"Discourse module failed to return a valid topic ID for title '{issue_title}'")

            discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
            comment_lines.append(f"**Discourse Topic ID:** {topic_id}")
            comment_lines.append(f"- Action: {action.capitalize()}")
            comment_lines.append(f"- URL: {discourse_url}")
            print(f"[DEBUG] Discourse topic {action}: ID {topic_id}, title '{issue_title}'")

        except DiscourseDuplicateTitleError as e:
            print(f"[INFO] Discourse topic creation failed: Title '{e.title}' already exists. Searching mapping for existing topic.")
            comment_lines.append("\n**Discourse Topic:** Title already exists.")
            found_existing_in_mapping = False
            # Try to find the topic_id from the mapping based on call_series for recurring meetings
            if is_recurring and call_series:
                print(f"[DEBUG] Searching mapping for call series: '{call_series}'")
                # Find entries matching the call series with a valid topic ID, sort by issue number desc
                series_entries = sorted(
                    [entry for entry in mapping.values()
                     if entry.get("call_series") == call_series and
                        entry.get("discourse_topic_id") and # Check top-level first (older format?)
                        not str(entry.get("discourse_topic_id")).startswith("placeholder")],
                    key=lambda e: e.get("issue_number", 0), # May not have issue_number at top level
                    reverse=True
                )
                # If not found at top level, check occurrences within matching series entries
                if not series_entries:
                    potential_series_matches = [
                        (m_id, entry) for m_id, entry in mapping.items()
                        if entry.get("call_series") == call_series and "occurrences" in entry
                    ]
                    for m_id, entry in potential_series_matches:
                         # Sort occurrences by issue number within the series
                         sorted_occurrences = sorted(
                             [occ for occ in entry.get("occurrences", [])
                              if isinstance(occ, dict) and occ.get("discourse_topic_id") and
                                 not str(occ.get("discourse_topic_id")).startswith("placeholder")],
                             key=lambda o: o.get("issue_number", 0),
                             reverse=True
                         )
                         if sorted_occurrences:
                             # Found the most recent valid topic ID within this series' occurrences
                             topic_id = sorted_occurrences[0]["discourse_topic_id"]
                             series_entries = [entry] # Use the parent entry for logging context below
                             print(f"[DEBUG] Found existing topic ID {topic_id} in occurrences for series '{call_series}'")
                             break # Found it in this series, stop searching others

                if series_entries: # If found either at top-level or in occurrences
                    if not topic_id: # If found at top-level
                         topic_id = series_entries[0]["discourse_topic_id"]
                         print(f"[DEBUG] Found existing topic ID {topic_id} at top-level for series '{call_series}'")

                    found_existing_in_mapping = True
                    action = "found_duplicate_series"
                    discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
                    # Log the issue number where the ID was found if possible
                    found_in_issue_num = series_entries[0].get('issue_number', 'N/A')
                    if sorted_occurrences: # If found in occurrences, get issue from there
                         found_in_issue_num = sorted_occurrences[0].get('issue_number', 'N/A')
                    print(f"[DEBUG] Using existing topic ID {topic_id} for series '{call_series}' (found via issue #{found_in_issue_num}).")
                    comment_lines.append(f"- Using existing Topic ID found in mapping: {topic_id}")
                    comment_lines.append(f"- URL: {discourse_url}")
                else:
                    print(f"[DEBUG] No existing valid topic ID found in mapping for series '{call_series}'.")

            # If not found via series (or not recurring), handle as failure to find existing
            if not found_existing_in_mapping:
                print(f"[ERROR] Duplicate title '{e.title}', but could not find existing topic ID in mapping.")
                comment_lines.append("- ⚠️ Could not find existing topic ID in mapping for this duplicate title.")
                topic_id = f"placeholder-duplicate-{issue.number}"
                discourse_url = "https://ethereum-magicians.org (Duplicate title, ID not found)"
                action = "failed_duplicate_title"

        except Exception as e:
            # Catch other errors during creation (e.g., network, other API errors)
            print(f"[ERROR] Exception during Discourse create handling: {str(e)}")
            comment_lines.append("\n**⚠️ Discourse Topic Error**")
            comment_lines.append(f"- Failed to create Discourse topic: {str(e)}")
            topic_id = f"placeholder-error-{issue.number}"
            discourse_url = "https://ethereum-magicians.org (API error occurred)"
            action = "failed"

    # Add existing YouTube stream links (only if action indicates success/found and streams exist)
    # Refine condition to check action status properly
    # Make sure topic_id is valid before using it
    if action in ["created", "updated", "found_duplicate_series"] and topic_id and not str(topic_id).startswith("placeholder") and existing_youtube_streams:
        print(f"[DEBUG] Adding existing YouTube streams to Discourse topic {topic_id}")
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
            # Prepare the body content to append
            youtube_links_body = f"\n\n**Existing YouTube Stream Links:**\n" + "\n".join(stream_links)
            # Get the current content of the first post to append to it
            posts = discourse.get_posts_in_topic(topic_id)
            if posts:
                 first_post_raw = posts[0].get("raw")
                 # Check if links are already there to avoid duplicates
                 if youtube_links_body not in first_post_raw:
                     updated_discourse_body = first_post_raw + youtube_links_body
                     discourse.update_topic(
                         topic_id=topic_id,
                         body=updated_discourse_body # Update the body with appended links
                     )
                     print(f"[DEBUG] Successfully appended YouTube links to topic {topic_id}")
                 else:
                     print(f"[DEBUG] YouTube links already present in topic {topic_id}, skipping append.")
            else:
                  print(f"[WARN] Could not get posts for topic {topic_id} to append YouTube links.")
        except Exception as e:
            print(f"[ERROR] Failed to add existing YouTube streams to Discourse topic {topic_id}: {str(e)}")
            comment_lines.append(f"- ⚠️ Failed to add existing YouTube streams to Discourse topic {topic_id}")

    # Determine the base title for recurring events
    event_base_title = issue_title # Default to issue title
    if is_recurring and call_series:
        # Use call_series in proper Title Case (not all uppercase)
        event_base_title = ' '.join(word.capitalize() for word in call_series.strip().split())
        print(f"[DEBUG] Using call series '{event_base_title}' (Title Case) as base title for recurring Zoom/GCal/YouTube events.")

    # Zoom meeting creation/update
    zoom_id = None
    join_url = None
    meeting_updated = False # Flag to track if mapping needs update due to new/updated Zoom/GCal info
    reusing_series_meeting = False
    zoom_response = None # Store response for potential later use
    original_meeting_id_for_reuse = None # Store the original ID if reusing a series
    zoom_action = "skipped" # Track what happened with Zoom: skipped, created, updated, reused, failed

    try:
        # 1. Parse time and duration first
        start_time, duration = parse_issue_for_time(issue_body)

        # 2. Check if we should skip Zoom API calls entirely
        if skip_zoom_creation:
            print("[DEBUG] Skipping Zoom meeting creation/update based on issue input or existing series.")
            if existing_series_entry_for_zoom:
                # Reuse existing meeting ID from the series
                zoom_id = existing_series_entry_for_zoom["meeting_id"]
                # Don't set join_url yet - will be fetched directly via API call in the main fetch section
                join_url = None
                print(f"[DEBUG] Reusing meeting ID {zoom_id} from series. Will fetch current join URL via API.")
                original_meeting_id_for_reuse = zoom_id # Store the ID we are reusing
                reusing_series_meeting = True
                zoom_action = "reused_series"
                print(f"[DEBUG] Reusing existing Zoom meeting {zoom_id} for call series '{call_series}'")
            else:
                # Skipped via issue input, need placeholder
                print("[DEBUG] Zoom creation skipped via issue input. Using placeholder Zoom ID.")
                zoom_id = f"placeholder-skipped-{issue.number}"
                join_url = "Zoom creation skipped via issue input"
                zoom_action = "skipped_issue"
            # Ensure meeting_id is set when skipping Zoom creation
            meeting_id = zoom_id
        else:
            # Proceed with Zoom creation/update logic (as skip_zoom_creation is False)
            # Check for existing meeting tied to this issue number (using data found earlier)
            print(f"[DEBUG] Proceeding with Zoom creation/update for issue #{issue_number}.")
            # Use the meeting ID and occurrence data found during the initial mapping search
            existing_zoom_id_for_issue = found_meeting_id_for_issue

            if existing_zoom_id_for_issue:
                # Update existing meeting tied to this specific issue number
                # Fetch start/duration from the specific OCCURRENCE data we found earlier
                stored_start = existing_occurrence_data.get("start_time") if existing_occurrence_data else None
                existing_entry_data = mapping.get(existing_zoom_id_for_issue, {})
                stored_start = existing_entry_data.get("start_time") # TODO: This should check OCCURRENCE start time
                stored_duration = existing_entry_data.get("duration") # TODO: This should check OCCURRENCE duration
                zoom_id = existing_zoom_id_for_issue # Use the found ID
                join_url = None # Don't set join_url - will be fetched directly via API in main fetch section
                print(f"[DEBUG] Using existing meeting ID {zoom_id}. Will fetch current join URL via API.")

                if str(zoom_id).startswith("placeholder-"):
                    print(f"[DEBUG] Skipping Zoom update for placeholder ID: {zoom_id}")
                    join_url = join_url or "https://zoom.us (placeholder)"
                    zoom_action = "skipped_placeholder"
                # TODO: Need to compare with the specific occurrence's start/duration if available
                # For simplicity now, assume any update attempt means potential change
                # elif stored_start and stored_duration and (start_time == stored_start) and (duration == stored_duration):
                #     print("[DEBUG] No changes detected in meeting start time or duration. Skipping Zoom update.")
                #     zoom_action = "skipped_no_change"
                else:
                    print(f"[DEBUG] Updating Zoom meeting {zoom_id} based on issue #{issue_number}.")
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
                        zoom_action = "updated"
                        # Update join_url if response has it (it usually doesn't for updates)
                        # Keep the existing join_url unless the update explicitly returns a new one
                        if zoom_response and zoom_response.get('join_url'):
                            join_url = zoom_response.get('join_url')
                    except Exception as e:
                        print(f"[DEBUG] Error updating Zoom meeting {zoom_id}: {str(e)}")
                        comment_lines.append("\n**⚠️ Failed to update Zoom meeting. Please check credentials.**")
                        zoom_action = "failed_update"
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
                    zoom_action = "created"
                except Exception as e:
                    print(f"[DEBUG] Error creating Zoom meeting: {str(e)}")
                    comment_lines.append("\n**⚠️ Failed to create Zoom meeting. Please check credentials.**")
                    zoom_id = f"placeholder-{issue.number}"
                    join_url = "https://zoom.us (API authentication failed)"
                    zoom_action = "failed_create"

    except ValueError as e:
        # Error parsing time/duration
        print(f"[DEBUG] Error parsing time/duration: {str(e)}")
        comment_lines.append(f"\n**⚠️ Error:** {str(e)} Please correct the format in the issue body.")
        zoom_id = f"placeholder-time-error-{issue.number}"
        join_url = "Invalid time/duration in issue"
        zoom_action = "failed_time_parse"
        meeting_id = zoom_id  # Ensure meeting_id is set even on error
    except Exception as e:
        # Catch other unexpected errors during Zoom processing
        print(f"[DEBUG] Unexpected error during Zoom processing: {str(e)}")
        comment_lines.append("\n**⚠️ Unexpected Zoom Processing Error.** Check logs.")
        zoom_id = f"placeholder-error-{issue.number}"
        join_url = "Error during Zoom processing"
        zoom_action = "failed_unexpected"
        meeting_id = zoom_id  # Ensure meeting_id is set even on error

    # --- MODIFIED START: Always fetch Join URL via API ---
    # As per updated requirements, always fetch Zoom join URL from API
    # Never rely on stored URLs in the mapping or previous data

    # First priority: Use zoom_id if available (and not a placeholder)
    if zoom_id and not str(zoom_id).startswith("placeholder-"):
        print(f"[DEBUG] Always fetching current join URL from API for meeting ID: {zoom_id}")
        try:
            meeting_details = zoom.get_meeting(zoom_id)
            if meeting_details and meeting_details.get('join_url'):
                join_url = meeting_details['join_url']
                print(f"[DEBUG] Successfully fetched join_url: {join_url}")

                # Store UUID if available (but not the join_url)
                current_meeting_id = meeting_id if 'meeting_id' in locals() else zoom_id
                if meeting_details.get('uuid') and current_meeting_id:
                    mapping_entry = mapping.get(current_meeting_id, {})
                    # Store UUID in the mapping for this meeting
                    if "uuid" not in mapping_entry or mapping_entry.get("uuid") != meeting_details.get('uuid'):
                        mapping_entry["uuid"] = meeting_details.get('uuid')
                        mapping[current_meeting_id] = mapping_entry
                        mapping_updated = True
                        print(f"[DEBUG] Stored Zoom UUID in mapping: {meeting_details.get('uuid')}")
            else:
                join_url = "Error fetching Zoom link (API returned incomplete data)"
                print(f"[WARN] {join_url}")
        except Exception as e:
            join_url = f"Error fetching Zoom link ({type(e).__name__})"
            print(f"::warning::{join_url}: {str(e)}")

    # Second priority: Use meeting_id as fallback if zoom_id isn't available or failed (and not a placeholder)
    elif meeting_id and not str(meeting_id).startswith("placeholder-"):
        print(f"[DEBUG] Fetching meeting details via API for meeting ID: {meeting_id} to get join_url.")
        try:
            meeting_details = zoom.get_meeting(meeting_id)
            if meeting_details and meeting_details.get('join_url'):
                join_url = meeting_details['join_url']
                print(f"[DEBUG] Successfully fetched join_url: {join_url}")

                # Store UUID if available
                if meeting_details.get('uuid'):
                    # Since we're in the fallback case, we know meeting_id is defined
                    mapping_entry = mapping.get(meeting_id, {})
                    # Store UUID in the mapping for this meeting
                    if "uuid" not in mapping_entry or mapping_entry.get("uuid") != meeting_details.get('uuid'):
                        mapping_entry["uuid"] = meeting_details.get('uuid')
                        mapping[meeting_id] = mapping_entry
                        mapping_updated = True
                        print(f"[DEBUG] Stored Zoom UUID in mapping: {meeting_details.get('uuid')}")
            else:
                join_url = "Error fetching Zoom link (API returned incomplete data)"
                print(f"[WARN] {join_url}")
        except Exception as e:
            join_url = f"Error fetching Zoom link ({type(e).__name__})"
            print(f"::warning::{join_url}: {str(e)}")

    # Last resort: No valid ID available
    else:
        print("[DEBUG] No valid zoom_id or meeting_id available for API call.")
        join_url = "Zoom link not available" # Ensure join_url has a non-None value
    # --- MODIFIED END ---

    # Add Zoom link details to GitHub comment based on the flag
    if zoom_id and not str(zoom_id).startswith("placeholder-"):
        if reusing_series_meeting:
            comment_lines.append(f"\n**Zoom Meeting:** Reusing meeting {zoom_id} for series '{call_series}'.")

        # --- MODIFIED: Use join_url directly, check validity and display flag ---
        is_valid_join_url_for_display = bool(join_url and str(join_url).startswith("https://"))

        if is_valid_join_url_for_display:
             if display_zoom_link_in_invite:
                 comment_lines.append(f"- Zoom Link: {join_url}")
             else:
                 comment_lines.append(f"- *Zoom link hidden (sent to facilitator email)*")
        else: # Handle placeholders or error strings in join_url
             comment_lines.append(f"- *Zoom link not available ({join_url}).*")
        # --- END MODIFICATION ---

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
             should_create_streams = True # Flag to control stream creation

             # Add the check for need_youtube_streams
             if is_recurring and occurrence_rate != "none" and need_youtube_streams:
                 # Check if we are reprocessing and streams already exist for this occurrence
                 if not is_first_run_for_issue and existing_occurrence_data and existing_occurrence_data.get("youtube_streams"):
                     print(f"[DEBUG] Reprocessing issue #{issue_number}. Reusing existing YouTube streams found in occurrence data.")
                     occurrence_youtube_streams = existing_occurrence_data.get("youtube_streams")
                     comment_lines.append("\n**Existing YouTube Stream Links (Reused):**")
                     # Add stream links to comments again for clarity
                     stream_links = []
                     for i, stream in enumerate(occurrence_youtube_streams, 1):
                          stream_date = ""
                          if 'scheduled_time' in stream:
                              try:
                                  from datetime import datetime
                                  scheduled_time = stream['scheduled_time']
                                  if scheduled_time.endswith('Z'): scheduled_time = scheduled_time.replace('Z', '+00:00')
                                  date_obj = datetime.fromisoformat(scheduled_time)
                                  stream_date = f" ({date_obj.strftime('%b %d, %Y')})"
                              except Exception as e: print(f"[DEBUG] Error formatting stream date: {e}")
                          comment_lines.append(f"- Stream {i}{stream_date}: {stream['stream_url']}")
                          stream_links.append(f"- Stream {i}{stream_date}: {stream['stream_url']}")

                     should_create_streams = False # Don't create new ones
                 # TODO: Optional: Consider reusing series-level streams (`existing_youtube_streams`) if no occurrence-specific ones exist?
                 # elif existing_youtube_streams:
                 #     print(f"[DEBUG] No streams found for this specific occurrence, reusing existing series streams for call series: {call_series}")
                 #     occurrence_youtube_streams = existing_youtube_streams
                 #     comment_lines.append("\n**Existing YouTube Stream Links (Series - Reused):**")
                 #     should_create_streams = False
                 else:
                     # Proceed to create streams if needed
                     should_create_streams = True

                 if should_create_streams:
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

        # --- MODIFIED: Use join_url directly for GCal ---
        is_valid_join_url_gcal = bool(join_url and str(join_url).startswith("https://"))

        # Append Zoom link to description only if requested AND available (valid URL)
        if display_zoom_link_in_invite and is_valid_join_url_gcal:
            print("[DEBUG] Adding Zoom link to calendar description.")
            calendar_description += f"\n\nZoom Link: {join_url}"
        else:
            print(f"[DEBUG] Not adding Zoom link to calendar description (flag: {display_zoom_link_in_invite}, valid_url: {is_valid_join_url_gcal}).")
        # --- END MODIFICATION ---

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
                     print(f"[DEBUG] Reusing existing calendar event ID {gcal_event_id_from_series} from series '{call_series}'")
                     print(f"[DEBUG] No changes made to the Google Calendar event series - maintaining consistency")
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
                        print(f"[DEBUG] Updating existing RECURRING calendar event with ID {base_event_id} for {event_base_title}")
                        print(f"[DEBUG] This updates an EXISTING event series in calendar - not creating a new series")
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
                         print(f"[DEBUG] Updating existing ONE-TIME calendar event with ID {base_event_id}")
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
                        # If this is part of an existing recurring series but we're still creating a new event
                        # log a warning since we should be updating an existing event
                        if is_recurring and call_series:
                            print(f"[WARNING] Creating a NEW calendar event for recurring series '{call_series}'")
                            print(f"[WARNING] This may cause duplicate events in calendar - should update existing series instead")

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

        # --- START REFACTOR: Consistent Occurrence Structure ---
        # Ensure 'occurrences' list exists at the top level
        if "occurrences" not in mapping_entry or not isinstance(mapping_entry["occurrences"], list):
            mapping_entry["occurrences"] = []

        # Create data for the current occurrence
        # Initialize with potentially parsed time/duration or None
        parsed_start_time = start_time if 'start_time' in locals() else None
        parsed_duration = duration if 'duration' in locals() else None
        # Determine skip flags based on logic above
        skip_yt_upload = skip_zoom_creation or (need_youtube_streams and is_recurring and occurrence_rate != "none")
        skip_transcript = skip_zoom_creation
        # Get youtube streams created specifically for this occurrence
        current_occurrence_streams = occurrence_youtube_streams if 'occurrence_youtube_streams' in locals() else None

        # Base data for the new/updated occurrence
        occurrence_data = {
            "issue_number": issue.number,
            "issue_title": issue.title,
            "discourse_topic_id": topic_id, # Use the topic_id determined earlier
            "start_time": parsed_start_time,
            "duration": parsed_duration,
            "skip_youtube_upload": skip_yt_upload,
            "skip_transcript_processing": skip_transcript,
            "youtube_upload_processed": False, # Initialize processing flags
            "transcript_processed": False,
            "upload_attempt_count": 0,
            "transcript_attempt_count": 0,
            "telegram_message_id": None, # Placeholder, will be updated if msg sent
            "youtube_streams_posted_to_discourse": False,
            "youtube_streams": [ # Store created streams here
                {
                    "stream_url": stream.get("stream_url"),
                    "scheduled_time": stream.get("scheduled_time")
                }
                for stream in current_occurrence_streams
                if isinstance(stream, dict) and stream.get("stream_url")
            ] if current_occurrence_streams else None
        }

        # Find if an occurrence for this issue number already exists
        existing_occurrence_index = next((i for i, occ in enumerate(mapping_entry["occurrences"]) if occ.get("issue_number") == issue.number), -1)

        if existing_occurrence_index != -1:
            print(f"[DEBUG] Updating existing occurrence at index {existing_occurrence_index} for issue #{issue.number} in mapping.")
            # Preserve existing processing flags and telegram ID when updating
            existing_occurrence = mapping_entry["occurrences"][existing_occurrence_index]
            preserve_flags = {
                "occurrence_number": existing_occurrence.get("occurrence_number"), # Keep original number
                "youtube_upload_processed": existing_occurrence.get("youtube_upload_processed", False),
                "transcript_processed": existing_occurrence.get("transcript_processed", False),
                "upload_attempt_count": existing_occurrence.get("upload_attempt_count", 0),
                "transcript_attempt_count": existing_occurrence.get("transcript_attempt_count", 0),
                "youtube_streams_posted_to_discourse": existing_occurrence.get("youtube_streams_posted_to_discourse", False),
                "telegram_message_id": existing_occurrence.get("telegram_message_id"), # Preserve existing ID
                # Preserve skip flags if they were already true
                "skip_youtube_upload": existing_occurrence.get("skip_youtube_upload", False) or occurrence_data["skip_youtube_upload"],
                "skip_transcript_processing": existing_occurrence.get("skip_transcript_processing", False) or occurrence_data["skip_transcript_processing"],
            }
            # Preserve existing valid discourse_topic_id to prevent overwriting correct mapping
            existing_topic_id = existing_occurrence.get("discourse_topic_id")
            new_topic_id = occurrence_data.get("discourse_topic_id")

            # Case 1: New topic ID is placeholder, existing is valid
            if (
                str(new_topic_id).startswith("placeholder")
                and existing_topic_id
                and not str(existing_topic_id).startswith("placeholder")
            ):
                print(f"[DEBUG] Preserving existing valid discourse_topic_id '{existing_topic_id}' over placeholder.")
                occurrence_data["discourse_topic_id"] = existing_topic_id

            # Case 2: Both are valid but different (prevent overwriting correct mapping)
            elif (
                existing_topic_id
                and not str(existing_topic_id).startswith("placeholder")
                and new_topic_id
                and not str(new_topic_id).startswith("placeholder")
                and existing_topic_id != new_topic_id
            ):
                print(f"[WARNING] Preserving existing valid discourse_topic_id '{existing_topic_id}' over new topic_id '{new_topic_id}' to prevent overwriting correct mapping.")
                print(f"[WARNING] This prevents the bot from overwriting correct topic IDs when re-running on the same issue.")
                occurrence_data["discourse_topic_id"] = existing_topic_id

            # Preserve existing YT streams if new ones weren't generated
            if not occurrence_data["youtube_streams"] and existing_occurrence.get("youtube_streams"):
                 print("[DEBUG] Preserving existing youtube_streams in occurrence.")
                 occurrence_data["youtube_streams"] = existing_occurrence.get("youtube_streams")

            occurrence_data.update(preserve_flags) # Apply preserved flags over defaults
            mapping_entry["occurrences"][existing_occurrence_index] = occurrence_data
        else:
            print(f"[DEBUG] Adding new occurrence for issue #{issue.number} to mapping.")
            # Assign occurrence number based on current count
            occurrence_data["occurrence_number"] = len(mapping_entry["occurrences"]) + 1
            mapping_entry["occurrences"].append(occurrence_data)

        # --- END REFACTOR ---

        # Update series-level info (applies to the meeting_id entry itself)
        series_updated = False
        # Ensure series-level fields are only set if they don't exist or are being explicitly added
        # Meeting ID is the key, so we don't store it inside
        if "is_recurring" not in mapping_entry:
            mapping_entry["is_recurring"] = is_recurring; series_updated = True
        # Update occurrence rate only if not set or 'none'
        if "occurrence_rate" not in mapping_entry or mapping_entry.get("occurrence_rate") == "none":
            mapping_entry["occurrence_rate"] = occurrence_rate if is_recurring else "none"; series_updated = True
        if "call_series" not in mapping_entry and call_series:
            mapping_entry["call_series"] = call_series; series_updated = True
        # No longer storing zoom_link in mapping - links are retrieved via API when needed
        if "zoom_link" in mapping_entry:
            del mapping_entry["zoom_link"]; series_updated = True
            print(f"[DEBUG] Removed zoom_link from mapping entry as per updated requirements")
        if "calendar_event_id" not in mapping_entry and event_id:
            mapping_entry["calendar_event_id"] = event_id; series_updated = True
        # Update calendar_event_id if new one exists and is different
        elif event_id and mapping_entry.get("calendar_event_id") != event_id:
             mapping_entry["calendar_event_id"] = event_id; series_updated = True

        # Deprecated: Do not store youtube_streams or telegram_message_id at the series level anymore
        # if "youtube_streams" in mapping_entry: del mapping_entry["youtube_streams"]
        # if "telegram_message_id" in mapping_entry: del mapping_entry["telegram_message_id"]
        # Deprecated: Do not store issue_number, title, start_time, duration etc. at series level anymore
        # Clean up old top-level fields if they exist
        obsolete_keys = ["issue_number", "issue_title", "discourse_topic_id", "start_time", "duration",
                         "skip_youtube_upload", "skip_transcript_processing",
                         "youtube_upload_processed", "transcript_processed", "upload_attempt_count",
                         "transcript_attempt_count", "telegram_message_id", "youtube_streams",
                         "youtube_streams_posted_to_discourse"]
        for key in obsolete_keys:
            if key in mapping_entry:
                # Check if it might still be needed for a non-recurring meeting WITHOUT occurrences yet
                if not (not mapping_entry.get("is_recurring") and not mapping_entry.get("occurrences")):
                     print(f"[DEBUG] Removing obsolete top-level key: {key}")
                     del mapping_entry[key]
                     series_updated = True # Indicate a change happened

        # Always update the mapping with the potentially modified entry
        # Check if the overall entry (including occurrences) has changed
        original_entry_before_update = mapping.get(meeting_id, {}).copy()

        # Perform a deep comparison if necessary (simple check is usually sufficient here)
        if original_entry_before_update != mapping_entry:
            mapping[meeting_id] = mapping_entry
            mapping_updated = True # Mark that the mapping file needs saving
            print(f"Mapping updated for meeting ID {meeting_id} with occurrence details from issue #{issue.number}.")
            if series_updated:
                print(f"[DEBUG] Series-level information updated or cleaned for {meeting_id}.")
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
        # Send email ONLY if facilitator emails exist, join_url is valid, AND it's the first run for this issue
        emails_sent_count = 0
        emails_failed = []

        # --- MODIFIED: Check join_url status for email ---
        # Determine if we *should* send an email (requires facilitator emails and first run)
        should_attempt_email = bool(facilitator_emails and is_first_run_for_issue)

        # Determine if the link status allows sending useful info
        # We can send even if hidden, just changing the body
        is_valid_join_url_email = bool(join_url and str(join_url).startswith("https://"))
        # We can send an email even if hidden, just need *some* info (zoom_id)
        can_send_email_info = bool(zoom_id and not str(zoom_id).startswith("placeholder-"))

        if not should_attempt_email:
            if not facilitator_emails:
                print(f"[DEBUG] No facilitator emails provided, skipping email notification.")
                comment_lines.append("- Facilitator emails not found in issue, skipping email notification.")
            elif not is_first_run_for_issue:
                 print(f"[DEBUG] Not the first run for issue #{issue.number}. Skipping email notification.")
                 comment_lines.append(f"- Skipping email notification (already processed issue #{issue.number} before).")
        elif not can_send_email_info:
            print(f"[DEBUG] No valid Zoom ID available ('{zoom_id}'), skipping email notification.")
            comment_lines.append(f"- Zoom Meeting ID invalid or missing, skipping email notification.")
        else:
            # Proceed with sending email (First run, emails exist, valid zoom_id)
            print(f"[DEBUG] First run for issue #{issue.number}. Proceeding with email notification (Join URL Status: '{join_url}').")
            email_subject = f"Zoom Meeting Details for {issue_title}"

            # --- MODIFIED: Adjust email body based on join_url validity and display flag ---
            email_body_content = ""
            if is_valid_join_url_email:
                 if display_zoom_link_in_invite:
                     # Valid URL, display allowed
                     email_body_content = f"""
<p><strong>Join URL:</strong> <a href=\"{join_url}\">{join_url}</a></p>
<p><strong>Meeting ID:</strong> {zoom_id}</p>
"""
                 else:
                     # Valid URL, but hidden
                     email_body_content = f"""
<p>The Zoom meeting details for <strong>{issue_title}</strong> have been set up.</p>
<p>As requested, the join link is not being displayed publicly on the calendar/Discourse.</p>
<p><strong>Join URL:</strong> <a href="{join_url}">{join_url}</a></p>
<p><strong>Meeting ID:</strong> {zoom_id}</p>
"""
            else:
                 # join_url is not valid (placeholder/error)
                 email_body_content = f"""
<p>The Zoom meeting (ID: {zoom_id}) for <strong>{issue_title}</strong> has been processed.</p>
<p>However, the join URL could not be retrieved or is invalid ({join_url}). Please check the meeting details in your Zoom account or contact the administrator.</p>
"""
                 print(f"[WARN] Email body content indicates join_url issue: {join_url}")

            # Construct full email body
            email_body = f'''
<h2>Zoom Meeting Details</h2>
<p>For meeting: {issue_title}</p>
{email_body_content}
<p><strong>Links:</strong><br>
<a href="{issue.html_url}">View GitHub Issue</a><br>
<a href="{discourse_url or 'Discourse link not available'}">View Discourse Topic</a></p>

<p>---<br>
This email was sent automatically by the Ethereum Protocol Call Bot because meeting details were created or updated.</p>
'''
            # --- END Email Body Modification ---

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
                            telegram_message_body += f"• <a href='{stream_url}'>Stream </a>"

                # Send the message
                telegram_channel_id = os.environ.get("TELEGRAM_CHAT_ID")
                existing_telegram_message_id = current_occurrence.get("telegram_message_id") # Get existing ID
                telegram_channel_sent = False # Reset flag for this attempt
                new_message_id = None # Store potential new ID

                if telegram_channel_id and tg:
                    try:
                        # --- Revised Logic: Update existing message or create ONLY if none exists ---
                        if existing_telegram_message_id:
                            print(f"[DEBUG] Attempting to update existing Telegram message ID: {existing_telegram_message_id}")
                            update_successful = tg.update_message(existing_telegram_message_id, telegram_message_body)
                            if update_successful:
                                print(f"[DEBUG] Successfully updated Telegram message {existing_telegram_message_id}.")
                                telegram_channel_sent = True  # Updated successfully
                                # Ensure the message ID is preserved in the current occurrence data upon successful update
                                if current_occurrence:
                                    current_occurrence["telegram_message_id"] = existing_telegram_message_id
                                    mapping_updated = True # Mark mapping for update as occurrence data changed
                            else:
                                error_msg = (f"Failed to update Telegram message ID {existing_telegram_message_id}. "
                                             "Message might have been deleted or API call failed.")
                                print(f"[ERROR] {error_msg}")
                                comment_lines.append(f"\n**⚠️ Telegram Update Error:** {error_msg}")
                                # DO NOT fall back to creating a new message – per requirements
                        else:
                            # No existing message ID – send a new one
                            print(f"[DEBUG] No existing Telegram message ID, sending new message for issue #{issue.number}.")
                            new_message_id = tg.send_message(telegram_message_body)
                            if new_message_id:
                                telegram_channel_sent = True
                                current_occurrence["telegram_message_id"] = new_message_id
                                mapping_updated = True
                                print(f"[DEBUG] Stored new telegram_message_id {new_message_id} in occurrence data for issue #{issue.number}.")
                            else:
                                print(f"[ERROR] tg.send_message failed – no message ID returned.")

                        if telegram_channel_sent:
                            comment_lines.append("\n**Telegram Notification**")
                            action_word = "Updated" if existing_telegram_message_id else "Sent"
                            comment_lines.append(f"- {action_word} message for this occurrence to Ethereum Protocol Updates channel")
                        else:
                            comment_lines.append("\n**⚠️ Failed to send or update Telegram message for this occurrence**")
                            print(f"[DEBUG] Failed to send/update Telegram channel message.")

                    except requests.exceptions.HTTPError as http_err:
                        # Log a controlled error message without the full URL/token
                        status_code = http_err.response.status_code if http_err.response else "Unknown"
                        error_reason = http_err.response.reason if http_err.response else "Unknown reason"
                        error_msg = f"Telegram API HTTP Error {status_code} ({error_reason})."
                        print(f"[ERROR] Telegram channel notification failed: {error_msg}")
                        # Add a generic message to the comment, avoiding sensitive details
                        comment_lines.append(f"\n**⚠️ Telegram Channel Notification Failed**: Could not communicate with Telegram API ({status_code}).")
                    except Exception as e:
                        # Catch other potential exceptions (network errors, etc.)
                        error_msg = f"An unexpected error occurred: {type(e).__name__}"
                        print(f"[ERROR] Telegram channel notification failed: {error_msg}")
                        # Add a generic message to the comment
                        comment_lines.append(f"\n**⚠️ Telegram Channel Notification Failed**: {error_msg}")
                else:
                    print("[DEBUG] Telegram channel ID not configured or tg module not available.")

        # --- RSS Notification Adding ---
        # Ensure we have occurrence_issue_number before adding RSS
        # Get occurrence_data again safely before using it
        current_occurrence_for_rss = next((occ for occ in mapping_entry.get("occurrences", []) if occ.get("issue_number") == issue.number), None)
        occurrence_issue_number_rss = current_occurrence_for_rss.get("issue_number") if current_occurrence_for_rss else None

        # CRITICAL: Always update the mapping BEFORE trying RSS (which might fail)
        # This ensures the mapping is stored even if RSS fails
        if mapping_entry and meeting_id:
            # Add the meeting_id to the entry itself to prevent filtering
            mapping_entry["meeting_id"] = meeting_id  # ADD THIS LINE
            mapping[meeting_id] = mapping_entry
            mapping_updated = True  # Mark for saving regardless of RSS outcome
            print(f"[DEBUG] Core mapping for meeting ID {meeting_id} prepared for saving")

        # RSS is NOT critical - completely isolate it
        if occurrence_issue_number_rss:
            try:
                print("[DEBUG] Adding notifications to RSS feed data")
                # RSS operations are now non-critical
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    occurrence_issue_number_rss,
                    "issue_processed",
                    f"GitHub issue #{occurrence_issue_number_rss} processed ({action})",
                    issue.html_url
                )
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    occurrence_issue_number_rss,
                    "discourse_post",
                    f"Discourse topic {action}: {issue_title}",
                    discourse_url
                )
                print("[DEBUG] RSS notifications added successfully")
            except Exception as e:
                print(f"[ERROR] Failed to add RSS notifications: {e}")
                comment_lines.append(f"\n**⚠️ Failed to update RSS data**: {str(e)}")
                # CRITICAL: RSS failure should NOT affect core mapping save
                print("[DEBUG] Continuing despite RSS error - meeting data will still be saved")
        else:
            print(f"[DEBUG] Skipping RSS notification - occurrence issue number missing.")

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
