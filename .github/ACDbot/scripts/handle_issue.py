import os
import sys
import argparse
from modules import discourse, zoom, gcal
from github import Github
import re
from datetime import datetime
import json
import requests
from github import InputGitAuthor

# Import your custom modules

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

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

    # 3. Check for existing topic_id in issue comments
    topic_id = None
    for comment in issue.get_comments():
        if comment.body.startswith("**Discourse Topic ID:**"):
            try:
                topic_id = int(comment.body.split("**Discourse Topic ID:**")[1].strip())
                break
            except ValueError:
                continue

    # 3. Discourse handling
    if topic_id:
        action = "updated"
        discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
        comment_lines.append(f"**Discourse Topic ID:** {topic_id}")
        comment_lines.append(f"- Action: {action.capitalize()}")
        comment_lines.append(f"- URL: {discourse_url}")
    else:
        # Create new topic
        discourse_response = discourse.create_topic(
            title=issue_title,
            body=issue_body,
            category_id=63  
        )
        topic_id = discourse_response.get("topic_id")
        action = "created"
        discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"
        comment_lines.append(f"**Discourse Topic ID:** {topic_id}")
        comment_lines.append(f"- Action: {action.capitalize()}")
        comment_lines.append(f"- URL: {discourse_url}")

    # After loading mapping and getting existing_entry
    existing_entry = mapping.get(str(issue_number))
    existing_zoom_meeting_id = existing_entry.get("meeting_id") if existing_entry else None
    
    # Zoom meeting creation/update
    try:
        start_time, duration = parse_issue_for_time(issue_body)
        meeting_updated = False
        
        if existing_zoom_meeting_id:
            # Check if time/duration changed
            stored_start = existing_entry.get("start_time")
            stored_duration = existing_entry.get("duration")
            
            # Always update if missing stored values (legacy entries)
            if not stored_start or not stored_duration:
                meeting_updated = True
            else:
                meeting_updated = (start_time != stored_start) or (duration != stored_duration)
            
            if meeting_updated:
                zoom_response = zoom.update_meeting(
                    meeting_id=existing_zoom_meeting_id,
                    topic=f"Issue {issue.number}: {issue_title}",
                    start_time=start_time,
                    duration=duration
                )
                comment_lines.append("\n**Zoom Meeting Updated**")
                comment_lines.append(f"- Meeting URL: {zoom_response.get('join_url')}")
                comment_lines.append(f"- Meeting ID: {existing_zoom_meeting_id}")
        else:
            # Create new meeting
            join_url, zoom_id = zoom.create_meeting(
                topic=f"{issue_title}",
                start_time=start_time,
                duration=duration
            )
            comment_lines.append("\n**Zoom Meeting Created**")
            comment_lines.append(f"- Meeting URL: {join_url}")
            comment_lines.append(f"- Meeting ID: {zoom_id}")
            meeting_updated = True
        
        # Update mapping if new or updated
        if meeting_updated:
            mapping[str(issue_number)]["start_time"] = start_time
            mapping[str(issue_number)]["duration"] = duration
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
            
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
        telegram_message = f"New Discourse Topic: {issue_title}\n\n{issue_body}\n{discourse_url}"
        telegram.send_message(telegram_message)
    except Exception as e:
        print(f"Telegram notification failed: {e}")
    
    # 5. Calendar event creation
    try:
        start_time, duration = parse_issue_for_time(issue_body)
        calendar_id = "c_upaofong8mgrmrkegn7ic7hk5s@group.calendar.google.com"
        event_link = gcal.create_event(
            summary=issue.title,
            start_dt=start_time,
            duration_minutes=duration,
            calendar_id=calendar_id,
            description=f"Issue: {issue.html_url}\nZoom: {join_url}"
        )
        print(f"Created calendar event: {event_link}")
    except Exception as e:
        print(f"Error creating calendar event: {e}")

    # 6. Update mapping
    meeting_id = str(zoom_id)
    mapping[meeting_id] = {
        "discourse_topic_id": topic_id,
        "issue_title": issue.title,
        "start_time": start_time,
        "duration": duration,
        "issue_number": issue.number,
        "Youtube_upload_processed": False,
        "transcript_processed": False,
        "upload_attempt_count": 0,
        "transcript_attempt_count": 0
    }
    save_meeting_topic_mapping(mapping)
    commit_mapping_file()
    print(f"Mapping updated: Zoom Meeting ID {zoom_id} -> Discourse Topic ID {topic_id}")
    

    # Remove any null mappings or failed entries
    mapping = {str(k): v for k, v in mapping.items() if v["discourse_topic_id"] is not None}

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