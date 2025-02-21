import os
import sys
import argparse
from modules import discourse, zoom, gcal, email_utils, telegram
from github import Github
import re
from datetime import datetime
import json
import requests
from github import InputGitAuthor


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
    
    email_match = re.search(email_pattern, issue_body)
    telegram_match = re.search(telegram_pattern, issue_body)
    
    facilitator_email = email_match.group(1) if email_match else None
    facilitator_telegram = telegram_match.group(1) if telegram_match else None
    
    return facilitator_email, facilitator_telegram

def handle_github_issue(issue_number: int, repo_name: str):
    """
    Fetches the specified GitHub issue, extracts its title and body,
    then creates or updates a Discourse topic using the issue title as the topic title
    and its body as the topic content.

    If the date/time or duration cannot be parsed from the issue body, 
    a comment is posted indicating the format error, and no meeting is created.
    """
    comment_lines = []
    
    # Load existing mapping
    mapping = load_meeting_topic_mapping()

    # 1. Connect to GitHub API
    gh = Github(os.environ["GITHUB_TOKEN"])
    repo = gh.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue_title = issue.title
    issue_body = issue.body or "(No issue body provided.)"

    # 3. Check for existing topic_id using the mapping instead of comments
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
        # Create new topic
        discourse_response = discourse.create_topic(
            title=issue_title,
            body=updated_body,
            category_id=63  
        )
        topic_id = discourse_response.get("topic_id")
        action = "created"
        discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
        comment_lines.append(f"**Discourse Topic ID:** {topic_id}")
        comment_lines.append(f"- Action: {action.capitalize()}")
        comment_lines.append(f"- URL: {discourse_url}")

    # Zoom meeting creation/update
    try:
        start_time, duration = parse_issue_for_time(issue_body)
        meeting_updated = False
        zoom_id = None  # Will hold the existing or new Zoom meeting ID
        join_url = None  # Will hold the join URL for new meetings
        zoom_response = None  # Will hold the zoom response for updated meetings

        # Find an existing mapping item by iterating over (meeting_id, entry) pairs.
        existing_item = next(
            ((meeting_id, entry) for meeting_id, entry in mapping.items() if entry.get("issue_number") == issue.number),
            None
        )
        
        if existing_item:
            existing_zoom_meeting_id, existing_entry = existing_item
            stored_start = existing_entry.get("start_time")
            stored_duration = existing_entry.get("duration")
            
            # Check if both start_time and duration are present and have not changed.
            if stored_start and stored_duration and (start_time == stored_start) and (duration == stored_duration):
                print("[DEBUG] No changes detected in meeting start time or duration. Skipping update.")
                zoom_id = existing_zoom_meeting_id
            else:
                # Either legacy entry with missing stored values or changes detected => update Zoom meeting.
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
        else:
            # No existing meeting found for this issue; create a new Zoom meeting.
            join_url, zoom_id = zoom.create_meeting(
                topic=f"{issue_title}",
                start_time=start_time,
                duration=duration
            )
            comment_lines.append("\n**Zoom Meeting Created**")
            print("[DEBUG] Zoom meeting created.")
            meeting_updated = True

        # Use zoom_id as the meeting_id (which is the mapping key)
        meeting_id = str(zoom_id)

        # Extract facilitator information
        facilitator_email, facilitator_telegram = extract_facilitator_info(issue_body)

        # Send notifications based on whether it's a new meeting or an update
        if meeting_updated:
            comment_lines.append("- Meeting details have been sent to the facilitator")
            
            # Send email notification
            if facilitator_email:
                try:
                    email_subject = f"{'Updated ' if existing_item else ''}Zoom Details - {issue_title}"
                    email_body = f"""
                    <h2>{'Updated ' if existing_item else ''}Zoom Meeting Details</h2>
                    <p>For meeting: {issue_title}</p>
                    <p><strong>Join URL:</strong> {zoom_response.get('join_url') if zoom_response else join_url}</p>
                    <p><strong>Meeting ID:</strong> {zoom_id}</p>
                    <p><a href="{issue.html_url}">View GitHub Issue</a></p>
                    """
                    email_utils.send_email(facilitator_email, email_subject, email_body)
                    comment_lines.append(f"- Zoom details sent to: {facilitator_email}")
                except Exception as e:
                    print(f"Failed to send email: {e}")
                    comment_lines.append("- ⚠️ Failed to send email with Zoom details")

            # Send Telegram DM if handle is provided
            if facilitator_telegram:
                try:
                    # Remove @ if present in telegram handle
                    telegram_handle = facilitator_telegram.lstrip('@')
                    
                    # Format message for Telegram
                    telegram_message = f"""
                    🎯 *Zoom Meeting Details*
                    *Meeting*: {issue_title}

                    *Join URL*: {zoom_response.get('join_url') if zoom_response else join_url}
                    *Meeting ID*: {zoom_id}

                    *GitHub Issue*: {issue.html_url}
                    """
                    # Send private message to facilitator
                    if telegram.send_private_message(telegram_handle, telegram_message):
                        comment_lines.append(f"- Zoom details sent via Telegram to: @{telegram_handle}")
                    else:
                        comment_lines.append("- ⚠️ Failed to send Telegram message with Zoom details")
                except Exception as e:
                    print(f"Failed to send Telegram message: {e}")

        # Update mapping if this entry is new or if the meeting was updated.
        # (In the mapping, we use the meeting ID as the key.)
        if meeting_updated or (existing_item is None):
            mapping[meeting_id] = {
                "discourse_topic_id": topic_id,
                "issue_title": issue.title,
                "start_time": start_time,
                "duration": duration,
                "issue_number": issue.number,
                "meeting_id": meeting_id,  # Store meeting_id in case we later want it in the value.
                "Youtube_upload_processed": False,
                "transcript_processed": False,
                "upload_attempt_count": 0,
                "transcript_attempt_count": 0
            }
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
            print(f"Mapping updated: Zoom Meeting ID {zoom_id} -> Discourse Topic ID {topic_id}")
        else:
            print("[DEBUG] No changes detected; mapping remains unchanged.")

        # Calendar handling using meeting_id
        existing_event_id = mapping[meeting_id].get("calendar_event_id")
        
        if existing_event_id:
            # Update existing event
            event_link = gcal.update_event(
                event_id=existing_event_id,
                summary=issue.title,
                start_dt=start_time,
                duration_minutes=duration,
                calendar_id="c_upaofong8mgrmrkegn7ic7hk5s@group.calendar.google.com",
                description=f"Issue: {issue.html_url}"
            )
            print(f"Updated calendar event: {event_link}")
        else:
            # Create new event
            event_link = gcal.create_event(
                summary=issue.title,
                start_dt=start_time,
                duration_minutes=duration,
                calendar_id="c_upaofong8mgrmrkegn7ic7hk5s@group.calendar.google.com",
                description=f"Issue: {issue.html_url}"
            )
            print(f"Created calendar event: {event_link}")
            # Store new event ID in mapping
            mapping[meeting_id]["calendar_event_id"] = event_link.split('eid=')[-1]
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
            print(f"Mapping updated: Zoom Meeting ID {zoom_id} -> calendar event ID {mapping[meeting_id]['calendar_event_id']}")

    except ValueError as e:
        print(f"[DEBUG] Meeting update failed: {str(e)}")
    except Exception as e:
        print(f"[DEBUG] Zoom meeting error: {str(e)}")

    # 5. Post consolidated comment
    if comment_lines:
        issue.create_comment("\n".join(comment_lines))

    # Add Telegram notification here
    try:
        import modules.telegram as telegram
        discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
        # Format message with HTML tags for better formatting
        telegram_message = (
            f"<b>Discourse Topic</b>: {issue_title}\n\n"
            f"{issue_body}\n\n"
            f"<b>Links</b>:\n"
            f"• <a href='{discourse_url}'>Discourse Topic</a>\n"
            f"• <a href='{issue.html_url}'>GitHub Issue</a>"
        )
        
        # Check if we already have a telegram message ID for this meeting
        if meeting_id in mapping and "telegram_message_id" in mapping[meeting_id]:
            message_id = mapping[meeting_id]["telegram_message_id"]
            if telegram.update_message(message_id, telegram_message):
                print(f"Updated Telegram message {message_id}")
        else:
            # No existing message, send new one
            message_id = telegram.send_message(telegram_message)
            if meeting_id in mapping:
                mapping[meeting_id]["telegram_message_id"] = message_id
                save_meeting_topic_mapping(mapping)
                print(f"Created new Telegram message {message_id}")
                
    except Exception as e:
        print(f"Telegram notification failed: {e}")
        import traceback
        print(traceback.format_exc())

    # Remove any null mappings or failed entries
    mapping = {str(k): v for k, v in mapping.items() if v.get("discourse_topic_id") is not None}

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
        start_dt = datetime.strptime(datetime_str, "%B %d %Y %H:%M")  # Full month name
    except ValueError:
        try:
            start_dt = datetime.strptime(datetime_str, "%b %d %Y %H:%M")  # Abbreviated month name
        except ValueError as e:
            raise ValueError(f"Unable to parse the start time: {e}")

    start_time_utc = start_dt.isoformat() + "Z"

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
            end_dt = datetime.strptime(end_time_str, "%B %d %Y %H:%M")
        except ValueError:
            end_dt = datetime.strptime(end_time_str, "%b %d %Y %H:%M")

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
