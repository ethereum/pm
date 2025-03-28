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
    Extracts facilitator contact information from the issue body.
    Returns a tuple of (email, telegram handle).
    """
    email_pattern = r"Facilitator email:\s*([^\n\s]+)"
    telegram_pattern = r"Facilitator telegram:\s*([^\n\s]+)"
    
    print(f"[DEBUG] Extracting facilitator info from issue body")
    
    email_match = re.search(email_pattern, issue_body)
    telegram_match = re.search(telegram_pattern, issue_body)
    
    facilitator_email = email_match.group(1) if email_match else None
    facilitator_telegram = telegram_match.group(1) if telegram_match else None
    
    print(f"[DEBUG] Extracted facilitator email: {facilitator_email}")
    print(f"[DEBUG] Extracted facilitator telegram: {facilitator_telegram}")
    
    return facilitator_email, facilitator_telegram

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
    
    # Extract whether the meeting is already on the Ethereum Calendar
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
        except Exception as e:
            print(f"[DEBUG] Error in Discourse topic handling: {str(e)}")
            comment_lines.append("\n**⚠️ Discourse Topic Error**")
            comment_lines.append(f"- Failed to create/update Discourse topic: {str(e)}")
            # Set a placeholder topic_id to allow the rest of the process to continue
            topic_id = f"placeholder-{issue.number}"
            discourse_url = "https://ethereum-magicians.org (API error occurred)"
            action = "failed"

    # Zoom meeting creation/update
    try:
        start_time, duration = parse_issue_for_time(issue_body)
        meeting_updated = False
        zoom_id = None
        join_url = None
        zoom_response = None

        # Find an existing mapping item by iterating over (meeting_id, entry) pairs.
        existing_item = next(
            ((meeting_id, entry) for meeting_id, entry in mapping.items() if entry.get("issue_number") == issue.number),
            None
        )
        
        try:
            if existing_item:
                existing_zoom_meeting_id, existing_entry = existing_item
                stored_start = existing_entry.get("start_time")
                stored_duration = existing_entry.get("duration")
                
                # Skip update if this is a placeholder ID
                if str(existing_zoom_meeting_id).startswith("placeholder-"):
                    print(f"[DEBUG] Skipping Zoom update for placeholder ID: {existing_zoom_meeting_id}")
                    zoom_id = existing_zoom_meeting_id
                    join_url = existing_entry.get("zoom_link", "https://zoom.us (placeholder)")
                # Check if both start_time and duration are present and have not changed.
                elif stored_start and stored_duration and (start_time == stored_start) and (duration == stored_duration):
                    print("[DEBUG] No changes detected in meeting start time or duration. Skipping update.")
                    zoom_id = existing_zoom_meeting_id
                    join_url = existing_entry.get("zoom_link")
                else:
                    # Either legacy entry with missing stored values or changes detected => update Zoom meeting.
                    try:
                        zoom_response = zoom.update_meeting(
                            meeting_id=existing_zoom_meeting_id,
                            topic=f"{issue_title}",
                            start_time=start_time,
                            duration=duration
                        )
                        comment_lines.append("\n**Zoom Meeting Updated**")
                        print("[DEBUG] Zoom meeting updated.")
                        zoom_id = existing_zoom_meeting_id
                        meeting_updated = True
                    except Exception as e:
                        print(f"[DEBUG] Error updating Zoom meeting: {str(e)}")
                        comment_lines.append("\n**⚠️ Failed to update Zoom meeting. Please check credentials.**")
                        # Continue with the rest of the process using existing zoom_id
                        zoom_id = existing_zoom_meeting_id
                        join_url = existing_entry.get("zoom_link")
            else:
                # No existing meeting found for this issue; create a new Zoom meeting.
                try:
                    if is_recurring and occurrence_rate != "none":
                        join_url, zoom_id = zoom.create_recurring_meeting(
                            topic=f"{issue_title}",
                            start_time=start_time,
                            duration=duration,
                            occurrence_rate=occurrence_rate
                        )
                        comment_lines.append("\n**Recurring Zoom Meeting Created**")
                    else:
                        join_url, zoom_id = zoom.create_meeting(
                            topic=f"{issue_title}",
                            start_time=start_time,
                            duration=duration
                        )
                        comment_lines.append("\n**Zoom Meeting Created**")
                    
                    print("[DEBUG] Zoom meeting created.")
                    meeting_updated = True
                except Exception as e:
                    print(f"[DEBUG] Error creating Zoom meeting: {str(e)}")
                    comment_lines.append("\n**⚠️ Failed to create Zoom meeting. Please check credentials.**")
                    # Create a placeholder meeting_id to still allow mapping entries to be created
                    zoom_id = f"placeholder-{issue.number}"
                    join_url = "https://zoom.us (API authentication failed)"
        except Exception as e:
            print(f"[DEBUG] Error in Zoom meeting processing: {str(e)}")
            comment_lines.append("\n**⚠️ Zoom API error occurred. Please check credentials.**")
            # Create a placeholder ID to continue processing
            zoom_id = f"placeholder-{issue.number}"
            join_url = "https://zoom.us (API error occurred)"

        # Use zoom_id as the meeting_id (which is the mapping key)
        if zoom_id:
            meeting_id = str(zoom_id)
            
            # Get the meeting join URL - needed for notifications
            if zoom_response:
                join_url = zoom_response.get('join_url')
            elif not join_url and not str(zoom_id).startswith("placeholder-"):
                try:
                    # If not a new meeting and no zoom_response, fetch the meeting details
                    meeting_details = zoom.get_meeting(zoom_id)
                    join_url = meeting_details.get('join_url')
                except Exception as e:
                    print(f"[DEBUG] Error fetching Zoom meeting details: {str(e)}")
                    join_url = join_url or "https://zoom.us (API authentication failed)"
                    
            # Create YouTube streams for recurring meetings only
            youtube_streams = None
            # Use only the value from issue body for recurring meeting configuration
            if is_recurring and occurrence_rate != "none":
                try:
                    print(f"[DEBUG] Creating YouTube streams for recurring meeting: {occurrence_rate}")
                    youtube_streams = youtube_utils.create_recurring_streams(
                        title=issue_title,
                        description=f"Recurring meeting: {issue_title}\nGitHub Issue: {issue.html_url}",
                        start_time=start_time,
                        occurrence_rate=occurrence_rate
                    )
                    
                    # Add stream URLs to comment
                    if youtube_streams:
                        comment_lines.append("\n**YouTube Stream Links:**")
                        stream_links = []
                        for i, stream in enumerate(youtube_streams, 1):
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
                                discourse_content = f"{updated_body}\n\n**YouTube Stream Links:**\n" + "\n".join(stream_links)
                                discourse.update_topic(
                                    topic_id=topic_id,
                                    body=discourse_content
                                )
                            except Exception as e:
                                print(f"[DEBUG] Error updating Discourse topic with YouTube streams: {str(e)}")
                        
                        # Set flag to skip YouTube upload for recurring meetings with streams
                        if meeting_id in mapping:
                            mapping[meeting_id]["skip_youtube_upload"] = True
                            mapping[meeting_id]["youtube_streams"] = youtube_streams
                            mapping_updated = True
                except Exception as e:
                    print(f"[DEBUG] Error creating YouTube streams: {str(e)}")
                    comment_lines.append("\n**⚠️ Failed to create YouTube streams. Please check credentials.**")
            else:
                # This is a one-time meeting, we'll upload the recording to YouTube after the meeting
                print(f"[DEBUG] One-time meeting detected, YouTube upload will be handled after the meeting")
                if meeting_id in mapping:
                    mapping[meeting_id]["skip_youtube_upload"] = False
                    mapping_updated = True

            # Calendar handling
            calendar_id = "c_upaofong8mgrmrkegn7ic7hk5s@group.calendar.google.com"
            calendar_description = f"Issue: {issue.html_url}"
            event_link = None
            
            # Check if meeting is already on the Ethereum Calendar
            if already_on_calendar:
                # Will add the comment at the end of this section
                print(f"[DEBUG] Meeting is already on Ethereum Calendar, skipping calendar creation")
            else:
                # Use only the value from issue body for calendar events
                if existing_item:
                    # Update the specific calendar event instance
                    event_id = existing_entry.get("calendar_event_id")
                    if event_id:
                        try:
                            # For recurring events, the stored ID might include the instance suffix
                            # Extract just the base event ID for more reliable operations
                            base_event_id = extract_event_id_from_link(f"?eid={event_id}")
                            print(f"[DEBUG] Updating calendar event {base_event_id}, is_recurring={is_recurring}, occurrence_rate={occurrence_rate}")
                            
                            # Use the appropriate update function based on whether this is a recurring event
                            if is_recurring and occurrence_rate != "none":
                                print(f"[DEBUG] Using update_recurring_event for recurring meeting with occurrence_rate={occurrence_rate}")
                                event_result = gcal.update_recurring_event(
                                    event_id=base_event_id,
                                    summary=issue_title,
                                    start_dt=start_time,
                                    duration_minutes=duration,
                                    calendar_id=calendar_id,
                                    occurrence_rate=occurrence_rate,
                                    description=calendar_description
                                )
                            else:
                                print(f"[DEBUG] Using update_event for standard meeting")
                                event_result = gcal.update_event(
                                    event_id=base_event_id,
                                    summary=issue_title,
                                    start_dt=start_time,
                                    duration_minutes=duration,
                                    calendar_id=calendar_id,
                                    description=calendar_description
                                )
                            
                            event_link = event_result['htmlLink']
                            event_id = event_result['id']
                            print(f"Updated calendar event: {event_link} with ID: {event_id}")
                            # Store the calendar event ID to ensure we update the same event next time
                            if meeting_id in mapping:
                                mapping[meeting_id]["calendar_event_id"] = event_id
                                mapping_updated = True
                        except ValueError as e:
                            print(f"[DEBUG] Event ID {event_id} not found, creating a new calendar event")
                            # Create new event if update fails due to event not found
                            event_result = create_calendar_event(
                                is_recurring=is_recurring,
                                occurrence_rate=occurrence_rate,
                                summary=issue_title,
                                start_dt=start_time,
                                duration_minutes=duration,
                                calendar_id=calendar_id,
                                description=calendar_description
                            )
                            # Extract and store the clean event ID
                            if event_result:
                                event_link = event_result['htmlLink']
                                new_event_id = event_result['id']
                                print(f"[DEBUG] Created new calendar event with ID: {new_event_id}")
                                if meeting_id in mapping:
                                    mapping[meeting_id]["calendar_event_id"] = new_event_id
                                    mapping_updated = True
                        except Exception as e:
                            print(f"[DEBUG] Failed to update calendar event: {str(e)}")
                            # Create new event if update fails for any other reason
                            event_result = create_calendar_event(
                                is_recurring=is_recurring,
                                occurrence_rate=occurrence_rate,
                                summary=issue_title,
                                start_dt=start_time,
                                duration_minutes=duration,
                                calendar_id=calendar_id,
                                description=calendar_description
                            )
                            # Extract and store the clean event ID
                            if event_result:
                                event_link = event_result['htmlLink']
                                new_event_id = event_result['id']
                                print(f"[DEBUG] Created new calendar event with ID: {new_event_id}")
                                if meeting_id in mapping:
                                    mapping[meeting_id]["calendar_event_id"] = new_event_id
                                    mapping_updated = True
                    else:
                        # No event ID stored, create a new one
                        print(f"[DEBUG] No event ID stored, creating a new calendar event")
                        event_result = create_calendar_event(
                            is_recurring=is_recurring,
                            occurrence_rate=occurrence_rate,
                            summary=issue_title,
                            start_dt=start_time,
                            duration_minutes=duration,
                            calendar_id=calendar_id,
                            description=calendar_description
                        )
                        # Extract and store the event ID
                        if event_result:
                            event_link = event_result['htmlLink']
                            new_event_id = event_result['id']
                            if meeting_id in mapping:
                                mapping[meeting_id]["calendar_event_id"] = new_event_id
                                mapping_updated = True
                else:
                    # Create new calendar event
                    print(f"[DEBUG] Creating new calendar event, is_recurring={is_recurring}, occurrence_rate={occurrence_rate}")
                    event_result = create_calendar_event(
                        is_recurring=is_recurring,
                        occurrence_rate=occurrence_rate,
                        summary=issue_title,
                        start_dt=start_time,
                        duration_minutes=duration,
                        calendar_id=calendar_id,
                        description=calendar_description
                    )
                    # Extract and store the clean event ID
                    if event_result:
                        event_link = event_result['htmlLink']
                        new_event_id = event_result['id']
                        if meeting_id in mapping:
                            mapping[meeting_id]["calendar_event_id"] = new_event_id
                            mapping_updated = True

            # Add comment about the calendar event
            if already_on_calendar:
                comment_lines.append("\n**Calendar Event**")
                comment_lines.append("- Meeting already on Ethereum Calendar")
            elif event_result:
                event_link = event_result['htmlLink']
                comment_lines.append("\n**Calendar Event**")
                comment_lines.append(f"- [Google Calendar]({event_link})")

            # Update mapping if this entry is new or if the meeting was updated.
            # (In the mapping, we use the meeting ID as the key.)
            if meeting_updated or (existing_item is None):
                # When updating the mapping, preserve existing values
                if existing_entry:
                    # Create new mapping with existing values
                    updated_mapping = existing_entry.copy()
                    # Update only the fields that changed
                    updated_mapping.update({
                        "discourse_topic_id": topic_id,
                        "issue_title": issue.title,
                        "start_time": start_time,
                        "duration": duration,
                        "issue_number": issue.number,
                        "meeting_id": meeting_id,
                        "zoom_link": join_url,
                        "is_recurring": is_recurring,
                        "occurrence_rate": occurrence_rate if is_recurring else "none"
                    })
                    # Preserve all other fields from existing entry
                    mapping[meeting_id] = updated_mapping
                else:
                    # Create new mapping entry with initial values
                    # Use the values extracted from the issue body
                    mapping[meeting_id] = {
                        "discourse_topic_id": topic_id,
                        "issue_title": issue.title,
                        "start_time": start_time,
                        "duration": duration,
                        "issue_number": issue.number,
                        "meeting_id": meeting_id,
                        "zoom_link": join_url,
                        "is_recurring": is_recurring,
                        "occurrence_rate": occurrence_rate if is_recurring else "none",
                        "Youtube_upload_processed": False,
                        "transcript_processed": False,
                        "upload_attempt_count": 0,
                        "transcript_attempt_count": 0,
                        "skip_youtube_upload": is_recurring and occurrence_rate != "none"  # Skip upload for recurring meetings with streams
                    }
                
                # Add YouTube streams if available
                if youtube_streams:
                    mapping[meeting_id]["youtube_streams"] = youtube_streams
                    
                mapping_updated = True
                
                # Generate RSS feed
                try:
                    rss_file_path = rss_utils.create_or_update_rss_feed(mapping)
                    print(f"Updated RSS feed at {rss_file_path}")
                    comment_lines.append(f"\n**RSS Feed Updated**")
                except Exception as e:
                    print(f"Failed to update RSS feed: {e}")
                
                print(f"Mapping updated: Zoom Meeting ID {zoom_id} -> Discourse Topic ID {topic_id}")
            else:
                print("[DEBUG] No changes detected; mapping remains unchanged.")

            # Extract facilitator information
            facilitator_email, facilitator_telegram = extract_facilitator_info(issue_body)

            # Send notifications regardless of whether the meeting was updated
            # Send email notification
            email_sent = False
            telegram_sent = False
            
            # Only send notifications if we have a valid zoom_id (not a placeholder)
            if not zoom_id or (isinstance(zoom_id, str) and zoom_id.startswith("placeholder-")) or str(zoom_id).startswith("placeholder-"):
                print(f"[DEBUG] Skipping notifications - Zoom meeting creation failed or invalid zoom_id: {zoom_id}")
                comment_lines.append("\n**⚠️ Zoom Meeting Creation Failed**")
                comment_lines.append("- Notifications suppressed due to Zoom meeting creation failure")
                comment_lines.append("- Please check Zoom credentials and try again")
            else:
                if facilitator_email and join_url:
                    try:
                        print(f"[DEBUG] Sending email to facilitator: {facilitator_email}")
                        email_subject = f"{'Updated ' if existing_item else ''}Zoom Details - {issue_title}"
                        
                        # Create clean HTML email body without indentation problems
                        email_body = f"""
<h2>{'Updated ' if existing_item else ''}Zoom Meeting Details</h2>
<p>For meeting: {issue_title}</p>
<p><strong>Join URL:</strong> <a href="{join_url}">{join_url}</a></p>
<p><strong>Meeting ID:</strong> {zoom_id}</p>
<p><strong>Links:</strong><br>
<a href="{issue.html_url}">View GitHub Issue</a><br>
<a href="{discourse_url}">View Discourse Topic</a></p>

<p>---<br>
This email was sent automatically by the Ethereum Protocol Call Bot.</p>
"""
                        # Try to send email and handle success/failure
                        if email_utils.send_email(facilitator_email, email_subject, email_body):
                            email_sent = True
                            comment_lines.append(f"- Zoom details sent to: {facilitator_email}")
                            print(f"[DEBUG] Successfully sent email to: {facilitator_email}")
                        else:
                            # Check if environment variables are set
                            sender_email = os.environ.get("SENDER_EMAIL")
                            smtp_server = os.environ.get("SMTP_SERVER")
                            
                            comment_lines.append(f"- ⚠️ Failed to send email with Zoom details to {facilitator_email}")
                            
                            # Add more specific troubleshooting info to GitHub comment
                            if not sender_email or not smtp_server:
                                comment_lines.append(f"  - *Note*: Email service is not fully configured. Contact the repository administrator.")
                            else:
                                comment_lines.append(f"  - Please check the GitHub Actions logs for more details")
                                
                            print(f"[DEBUG] Failed to send email to: {facilitator_email}")
                    except Exception as e:
                        print(f"[DEBUG] Exception when sending email: {str(e)}")
                        comment_lines.append(f"- ⚠️ Failed to send email with Zoom details to {facilitator_email}")
                        comment_lines.append(f"  - Error: {str(e)}")
                        import traceback
                        print(traceback.format_exc())
                else:
                    if not facilitator_email:
                        print(f"[DEBUG] No facilitator email provided in the issue")
                    if not join_url:
                        print(f"[DEBUG] No join URL available for the meeting")

            # Send Telegram DM if handle is provided
            if facilitator_telegram and join_url:  # Only proceed if we have a join URL
                try:
                    # Remove @ if present in telegram handle
                    telegram_handle = facilitator_telegram.lstrip('@')
                    print(f"[DEBUG] Attempting to send private Telegram message to @{telegram_handle}")
                    
                    # Escape special characters for Telegram markdown
                    safe_title = issue_title.replace("*", "\\*").replace("_", "\\_").replace("`", "\\`").replace("[", "\\[")
                    safe_url = join_url.replace("*", "\\*").replace("_", "\\_").replace("`", "\\`").replace("[", "\\[")
                    safe_issue_url = issue.html_url.replace("*", "\\*").replace("_", "\\_").replace("`", "\\`").replace("[", "\\[")
                    safe_discourse_url = discourse_url.replace("*", "\\*").replace("_", "\\_").replace("`", "\\`").replace("[", "\\[")
                    
                    # Fix the indentation in the message string - remove leading spaces
                    telegram_message = f"""🎯 *Meeting Details*

*Title*: {safe_title}

*Join URL*: {safe_url}
*Meeting ID*: {zoom_id}

*Links*:
• [GitHub Issue]({safe_issue_url})
• [Discourse Topic]({safe_discourse_url})"""

                    # Send private message to facilitator with explicit parse_mode
                    if tg.send_private_message(telegram_handle, telegram_message, parse_mode="MarkdownV2"):
                        telegram_sent = True
                        comment_lines.append(f"- Zoom details sent via Telegram to: @{telegram_handle}")
                        print(f"[DEBUG] Successfully sent Telegram message to @{telegram_handle}")
                    else:
                        # Get bot username for instructions
                        bot_username = "the meeting bot"
                        try:
                            token = os.environ.get("TELEGRAM_BOT_TOKEN")
                            if token:
                                bot_username = tg.bot_username(token) or bot_username
                        except:
                            pass
                            
                        comment_lines.append(f"- ⚠️ Failed to send Telegram message to @{telegram_handle}")
                        comment_lines.append(f"  - *Note*: The facilitator needs to start a conversation with @{bot_username} on Telegram first")
                        print(f"[DEBUG] Failed to send Telegram message to @{telegram_handle}")
                    
                except Exception as e:
                    print(f"[ERROR] Failed to send Telegram message: {e}")
                    comment_lines.append(f"- ⚠️ Failed to send Telegram message to @{facilitator_telegram}: {str(e)}")
                    import traceback
                    print(traceback.format_exc())

            # Send Telegram notification if enabled
            telegram_handle = os.environ.get("TELEGRAM_CHAT_ID")
            if telegram_handle and tg:
                try:
                    telegram_channel_success = False
                    
                    # Format message with HTML tags for better formatting
                    telegram_message = (
                        f"<b>{issue_title}</b>\n\n"
                        f"{issue_body}\n\n"
                        f"<b>Links:</b>\n"
                        f"• <a href='{discourse_url}'>Discourse Topic</a>\n"
                        f"• <a href='{issue.html_url}'>GitHub Issue</a>\n"
                    )
                    
                    if zoom_id and not (isinstance(zoom_id, str) and zoom_id.startswith("placeholder-")) and not str(zoom_id).startswith("placeholder-"):
                        telegram_message += f"\n<b>Zoom Meeting:</b> <a href='{join_url}'>Join Link</a>"
                    
                    # Check for existing Telegram message ID (for updates)
                    print(f"[DEBUG] Checking for existing telegram_message_id in mapping[{meeting_id}]")
                    
                    # Get from mapping or set None if not found
                    message_id = mapping.get(meeting_id, {}).get("telegram_message_id")
                    if message_id:
                        print(f"[DEBUG] Found existing telegram_message_id: {message_id}")
                        try:
                            if tg.update_message(message_id, telegram_message):
                                print(f"Updated Telegram message {message_id}")
                                telegram_channel_success = True
                            else:
                                print(f"[DEBUG] tg.update_message returned False for message_id {message_id}")
                                raise Exception("Failed to update message")
                        except Exception as e:
                            print(f"Failed to update Telegram message: {e}")
                            print(f"[DEBUG] Sending new message instead")
                            # If update fails, send new message
                            message_id = tg.send_message(telegram_message)
                            if message_id:
                                telegram_channel_success = True
                                mapping[meeting_id]["telegram_message_id"] = message_id
                                mapping_updated = True
                    else:
                        # No message ID stored yet
                        print(f"[DEBUG] No existing telegram_message_id found, creating new message")
                        message_id = tg.send_message(telegram_message)
                        if message_id:
                            telegram_channel_success = True
                            mapping[meeting_id]["telegram_message_id"] = message_id
                            mapping_updated = True
                    
                    if telegram_channel_success:
                        comment_lines.append("\n**Telegram Notification**")
                        comment_lines.append("- Sent message to Ethereum Protocol Updates channel")
                    else:
                        comment_lines.append("\n**⚠️ Failed to update Telegram Channel**")
                
                except Exception as e:
                    print(f"Telegram notification failed: {e}")
                    comment_lines.append(f"\n**⚠️ Telegram Channel Notification Failed**: {str(e)}")
                    import traceback
                    print(traceback.format_exc())

            # Add notification to RSS feed
            rss_utils.add_notification_to_meeting(
                meeting_id,
                "issue_created",
                f"GitHub issue #{issue.number} created",
                issue.html_url
            )

            rss_utils.add_notification_to_meeting(
                meeting_id,
                "discourse_post",
                f"Discourse topic updated: {issue_title}",
                discourse_url
            )
            # Add notification to RSS feed
            rss_utils.add_notification_to_meeting(
            meeting_id,
            "summary_posted",
            "Meeting summary posted to Discourse",
            discourse_url
        )

    except ValueError as e:
        print(f"[DEBUG] Meeting update failed: {str(e)}")
    except Exception as e:
        print(f"[DEBUG] Zoom meeting error: {str(e)}")

    # 5. Post consolidated comment
    if comment_lines:
        # Get the current timestamp
        now = dt.now().strftime("%Y-%m-%d %H:%M UTC")
        
        # Update the action line to include timestamp
        for i, line in enumerate(comment_lines):
            if line.startswith("- Action:"):
                comment_lines[i] = f"- Action: {action.capitalize()} at {now}"
        
        # Check for existing comments by the bot
        existing_comment = None
        comments = issue.get_comments()
        for comment in comments:
            # Check if comment is from the bot
            if comment.user.login == "github-actions[bot]":
                existing_comment = comment
                break
        
        # Update existing comment or create new one
        comment_text = "\n".join(comment_lines)
        if existing_comment:
            existing_comment.edit(comment_text)
            print(f"Updated existing comment {existing_comment.id}")
        else:
            issue.create_comment(comment_text)
            print("Created new comment")

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
