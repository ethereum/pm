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
    Returns the email address.
    """
    email_pattern = r"Facilitator email:\s*([^\n\s]+)"
    
    print(f"[DEBUG] Extracting facilitator email from issue body")
    
    email_match = re.search(email_pattern, issue_body)

    
    facilitator_email = email_match.group(1) if email_match else None
    
    print(f"[DEBUG] Extracted facilitator email: {facilitator_email}")
    
    # Return email
    return facilitator_email

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

    # Extract recurring meeting info from issue body - this is the source of truth
    is_recurring, occurrence_rate = extract_recurring_info(issue_body)
    
    # Extract whether YouTube stream links are needed
    need_youtube_streams = extract_need_youtube_streams(issue_body)
    
    # Extract call series
    call_series = extract_call_series(issue_body)

    # Check for existing YouTube streams for this call series
    existing_youtube_streams = check_existing_youtube_streams(call_series, mapping)
    
    # Extract whether the meeting is already on the Ethereum Calendar
    existing_series_event = next((entry for entry in mapping.values() if entry.get("call_series") == call_series), None)
    if existing_series_event:
        already_on_calendar = True
        comment_lines.append("\n**Note:** Meeting already exists for this call series. Skipping event creation.")
    else:
        already_on_calendar = extract_already_on_calendar(issue_body)

    # 2. Check for existing topic_id using the mapping instead of comments
    topic_id = None
    existing_entry = next((entry for entry in mapping.values() if entry.get("issue_number") == issue_number), None)
    if existing_entry:
        topic_id = existing_entry.get("discourse_topic_id")

    issue_link = f"[GitHub Issue]({issue.html_url})"
    updated_body = f"{issue_body}\n\n{issue_link}"

    # 3. Discourse handling
    if topic_id:
        discourse_response = discourse.update_topic(
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
        
        # Add existing YouTube stream links to comments and discourse post if available
        if existing_youtube_streams:
            comment_lines.append("\n**Existing YouTube Stream Links:**")
            stream_links = []
            for i, stream in enumerate(existing_youtube_streams, 1):
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
            if topic_id:
                try:
                    discourse_content = f"{updated_body}\n\n**Existing YouTube Stream Links:**\n" + "\n".join(stream_links)
                    discourse.update_topic(
                        topic_id=topic_id,
                        body=discourse_content
                    )
                except Exception as e:
                    print(f"[DEBUG] Error updating Discourse topic with existing YouTube streams: {str(e)}")
    else:
        # Create a new topic - the updated create_topic function will handle duplicate titles
        try:
            print(f"[DEBUG] Creating new topic: '{issue_title}'")
            discourse_response = discourse.create_topic(
                title=issue_title,
                body=updated_body,
                category_id=63  
            )
            
            topic_id = discourse_response.get("topic_id")
            action = discourse_response.get("action", "created")  # Get action from response or default to "created"
            
            discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
            comment_lines.append(f"**Discourse Topic ID:** {topic_id}")
            comment_lines.append(f"- Action: {action.capitalize()}")
            comment_lines.append(f"- URL: {discourse_url}")
            
            print(f"[DEBUG] Discourse topic {action}: ID {topic_id}, title '{issue_title}'")
            
            # Add existing YouTube stream links to comments and discourse post if available
            if existing_youtube_streams:
                comment_lines.append("\n**Existing YouTube Stream Links:**")
                stream_links = []
                for i, stream in enumerate(existing_youtube_streams, 1):
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
                if topic_id:
                    try:
                        discourse_content = f"{updated_body}\n\n**Existing YouTube Stream Links:**\n" + "\n".join(stream_links)
                        discourse.update_topic(
                            topic_id=topic_id,
                            body=discourse_content
                        )
                    except Exception as e:
                        print(f"[DEBUG] Error updating Discourse topic with existing YouTube streams: {str(e)}")
        except Exception as e:
            print(f"[DEBUG] Error in Discourse topic handling: {str(e)}")
            comment_lines.append("\n**⚠️ Discourse Topic Error**")
            comment_lines.append(f"- Failed to create/update Discourse topic: {str(e)}")
            # Set a placeholder topic_id to allow the rest of the process to continue
            topic_id = f"placeholder-{issue.number}"
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

    try:
        # 1. Parse time and duration first
        start_time, duration = parse_issue_for_time(issue_body)

        # 2. Check if it's a recurring series and if we already have a meeting ID for it
        existing_series_entry = None
        if is_recurring and call_series:
            # Find the most recent entry for this call series
            series_entries = [
                entry for entry in mapping.values() 
                if entry.get("call_series") == call_series and "meeting_id" in entry
            ]
            if series_entries:
                # Sort by issue number descending to get the latest entry
                series_entries.sort(key=lambda e: e.get("issue_number", 0), reverse=True)
                existing_series_entry = series_entries[0]

        if existing_series_entry:
            # Reuse existing meeting ID and link from the series
            zoom_id = existing_series_entry["meeting_id"]
            join_url = existing_series_entry.get("zoom_link", "Link not found in mapping")
            reusing_series_meeting = True
            print(f"[DEBUG] Reusing existing Zoom meeting {zoom_id} for call series '{call_series}'")
            comment_lines.append(f"\n**Zoom Meeting:** Reusing existing meeting for series '{call_series.upper()}' ({zoom_id})")
            comment_lines.append(f"- Join URL: {join_url}")
            # We don't need to call Zoom API, meeting_updated remains False unless GCal/YT changes it
        else:
            # Not reusing, proceed with create/update logic based on issue number
            print(f"[DEBUG] No existing meeting found for series '{call_series}' or not a recurring series call. Checking for meeting tied to issue #{issue_number}.")
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

    # Use zoom_id as the meeting_id (which is the mapping key)
    if zoom_id:
        meeting_id = str(zoom_id) # Ensure it's a string for mapping key

        # Check if YT streams were created/reused
        if reusing_series_meeting and existing_series_entry and "youtube_streams" in existing_series_entry:
             youtube_streams = existing_series_entry["youtube_streams"]
             # We might have already added the comment for existing streams earlier
             # Let the existing logic handle adding YT stream comments if needed
        else:
             # Calculate youtube_streams based on need_youtube_streams and create if necessary
             try:
                print(f"[DEBUG] Creating YouTube streams for recurring meeting: {occurrence_rate}")
                youtube_streams = youtube_utils.create_recurring_streams(
                    title=issue_title, # CHANGE: Use issue_title instead of event_base_title
                    description=f"Recurring meeting: {issue_title}\nGitHub Issue: {issue.html_url}", # CHANGE: Use issue_title in description too
                    start_time=start_time,
                    occurrence_rate=occurrence_rate
                )
                
                # Add stream URLs to comment
                # ... (rest of the block)
             except Exception as e:
                print(f"[DEBUG] Error creating YouTube streams: {str(e)}")
                youtube_streams = None

        # Calendar handling
        calendar_id = "c_upaofong8mgrmrkegn7ic7hk5s@group.calendar.google.com"
        calendar_description = f"Issue: {issue.html_url}"
        event_link = None
        event_result = None # Define event_result

        if reusing_series_meeting:
            print("[DEBUG] Reusing series meeting, skipping Google Calendar API calls.")
            # Optionally try to find the GCal link from the series mapping entry
            if existing_series_entry and existing_series_entry.get("calendar_event_id"):
                 gcal_event_id = existing_series_entry.get("calendar_event_id")
                 # Construct a potential link (may not be perfect)
                 event_link = f"https://calendar.google.com/calendar/event?eid={gcal_event_id}" # Simplified link
                 comment_lines.append("\n**Calendar Event:** Reusing existing event for series.")
                 if event_link:
                     comment_lines.append(f"- [Approximate Google Calendar Link]({event_link})")
            else:
                 comment_lines.append("\n**Calendar Event:** Reusing existing event for series (Link not found in mapping).")
        elif already_on_calendar:
            print(f"[DEBUG] Meeting is already on Ethereum Calendar (or duplicate series), skipping calendar creation")
            comment_lines.append("\n**Calendar Event**")
            comment_lines.append("- Meeting already on Ethereum Calendar or duplicate series.")
        else:
            # Proceed with GCal creation/update logic ONLY if not reusing and not already marked as on calendar
            # ... (insert existing GCal create/update logic here, ensuring it uses meeting_id) ...
            # This logic might set meeting_updated = True
            pass # Placeholder for the existing complex GCal logic block

        # --- Mapping Update Logic --- 
        print(f"[DEBUG] Preparing to update mapping for meeting ID: {meeting_id}")
        
        # Get current mapping for this meeting_id, or initialize if new
        current_mapping_entry = mapping.get(meeting_id, {}).copy()
        
        # Create the updated entry data
        updated_mapping_data = {
                        "discourse_topic_id": topic_id,
                        "issue_title": issue.title,
            "start_time": start_time if 'start_time' in locals() else current_mapping_entry.get("start_time"), # Use parsed time if available
            "duration": duration if 'duration' in locals() else current_mapping_entry.get("duration"), # Use parsed duration if available
                        "issue_number": issue.number,
                        "meeting_id": meeting_id,
            "zoom_link": join_url, # Use the determined join_url
                        "is_recurring": is_recurring,
                        "occurrence_rate": occurrence_rate if is_recurring else "none",
            "call_series": call_series,
            # Preserve or update specific fields
            "Youtube_upload_processed": current_mapping_entry.get("Youtube_upload_processed", False),
            "transcript_processed": current_mapping_entry.get("transcript_processed", False),
            "upload_attempt_count": current_mapping_entry.get("upload_attempt_count", 0),
            "transcript_attempt_count": current_mapping_entry.get("transcript_attempt_count", 0),
            # Determine skip_youtube_upload based on current logic
            "skip_youtube_upload": is_recurring and occurrence_rate != "none" and need_youtube_streams, 
            # Add youtube_streams if they were generated or reused
            "youtube_streams": youtube_streams if 'youtube_streams' in locals() and youtube_streams else current_mapping_entry.get("youtube_streams"),
            # Add calendar event ID if it was determined
            "calendar_event_id": locals().get("event_id") or current_mapping_entry.get("calendar_event_id"),
            # Add telegram message ID if it was determined
            "telegram_message_id": locals().get("message_id") or current_mapping_entry.get("telegram_message_id"),
            # Add the discourse post flag for YT streams if reusing
            "youtube_streams_posted_to_discourse": current_mapping_entry.get("youtube_streams_posted_to_discourse", False)
        }

        # Check if anything actually changed compared to the existing entry
        if current_mapping_entry != updated_mapping_data:
            mapping[meeting_id] = updated_mapping_data
            mapping_updated = True # Mark that the mapping file needs saving
            print(f"Mapping updated for meeting ID {meeting_id} with details from issue #{issue_number}.")
        else:
            print(f"[DEBUG] Mapping entry for {meeting_id} remains unchanged.")

        # --- Notification Logic --- 
        # Extract facilitator information
        facilitator_email = extract_facilitator_info(issue_body)

        # Send notifications regardless of whether the meeting was updated
        # Send email notification
        email_sent = False
        telegram_sent = False # Keep this maybe for channel posts?
        
        # Only send notifications if we have a valid zoom_id
        if not zoom_id or (isinstance(zoom_id, str) and zoom_id.startswith("placeholder-")):
            print("[DEBUG] Skipping notifications due to placeholder zoom_id")
            pass # Add pass for the if block
        else:
            # --- Email sending logic --- 
            if facilitator_email and join_url:
                print("[DEBUG] (Placeholder) Would send email here")
                pass # Add pass for the email sending block
            else:
                print("[DEBUG] (Placeholder) Email conditions not met")
                pass # Add pass for the email else block
            
            # --- REMOVED Telegram DM logic --- 

            # --- Telegram Channel logic --- 
            telegram_handle = os.environ.get("TELEGRAM_CHAT_ID")
            if telegram_handle and tg:
                print("[DEBUG] (Placeholder) Would send Telegram channel message here")
                pass # Add pass for the Telegram channel block
            
            # --- RSS Notification logic --- 
            print("[DEBUG] (Placeholder) Would add RSS notifications here")
            # rss_utils.add_notification_to_meeting(
            #     meeting_id,
            #     # ... (RSS notification calls) ...
            # )
            pass # Add pass for the RSS block
        
    else:
        # zoom_id was not determined (likely due to errors)
        print("[ERROR] zoom_id could not be determined. Skipping downstream processing and mapping update.")
        comment_lines.append("\n**⚠️ Critical Error:** Could not determine Zoom Meeting ID. Processing halted.")

    # --- Final Comment Posting & Mapping Commit --- 
    # ... (rest of the script) ...

    # Remove any null mappings or failed entries
    mapping = {str(k): v for k, v in mapping.items() if v.get("discourse_topic_id") is not None}

    # Update the mapping file if any changes were made
    if mapping_updated:
        save_meeting_topic_mapping(mapping)
        commit_mapping_file()
        print(f"Mapping updated: Zoom Meeting ID {meeting_id} -> Discourse Topic ID {topic_id}")

def parse_issue_for_time(issue_body: str):
    """
    Parses the issue body to extract a start time and duration based on possible formats:
    
    - Date/time line followed by a duration line (with or without "Duration in minutes" preceding it)
    - Accepts both abbreviated and full month names
    """
    
    # -------------------------------------------------------------------------
    # 1. Regex pattern to find the date/time in the issue body
    # -------------------------------------------------------------------------
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

    date_match = date_pattern.search(issue_body)
    if not date_match:
        raise ValueError("Missing or invalid date/time format.")

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
