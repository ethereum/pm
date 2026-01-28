#!/usr/bin/env python3
"""
Close GitHub issues for meetings that occurred more than 24 hours ago.

This script reads the meeting_topic_mapping.json file, identifies meetings
that have ended more than 24 hours ago, and closes their corresponding
GitHub issues with an explanatory comment.

If a date cannot be parsed or any error occurs for a specific meeting,
that meeting is skipped (fail-safe behavior).
"""

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from github import Github


STALE_THRESHOLD_HOURS = 24
MAPPING_FILE = Path(__file__).parent.parent / "meeting_topic_mapping.json"


def load_mapping() -> dict:
    """Load the meeting topic mapping file."""
    try:
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[ERROR] Failed to load mapping file: {e}")
        return {}


def parse_start_time(start_time_str: str) -> datetime | None:
    """
    Parse an ISO format datetime string to a timezone-aware datetime.
    Returns None if parsing fails.
    """
    try:
        # Handle ISO format: "2025-04-24T14:00:00Z"
        if start_time_str.endswith("Z"):
            start_time_str = start_time_str[:-1] + "+00:00"
        dt = datetime.fromisoformat(start_time_str)
        # Ensure timezone-aware
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, TypeError) as e:
        print(f"[WARN] Failed to parse start_time '{start_time_str}': {e}")
        return None


def get_meeting_end_time(occurrence: dict) -> datetime | None:
    """
    Calculate the meeting end time from start_time and duration.
    Returns None if calculation fails.
    """
    start_time_str = occurrence.get("start_time")
    if not start_time_str:
        return None

    start_time = parse_start_time(start_time_str)
    if not start_time:
        return None

    # Duration in minutes, default to 60 if not specified
    duration_minutes = occurrence.get("duration", 60)
    try:
        duration_minutes = int(duration_minutes)
    except (ValueError, TypeError):
        duration_minutes = 60

    return start_time + timedelta(minutes=duration_minutes)


def is_meeting_stale(occurrence: dict) -> bool:
    """
    Check if a meeting ended more than STALE_THRESHOLD_HOURS ago.
    Returns False if unable to determine (fail-safe).
    """
    end_time = get_meeting_end_time(occurrence)
    if not end_time:
        return False

    now = datetime.now(timezone.utc)
    threshold = now - timedelta(hours=STALE_THRESHOLD_HOURS)

    return end_time < threshold


def close_issue_with_comment(repo, issue_number: int, meeting_title: str) -> bool:
    """
    Close the specified issue with an explanatory comment.
    Returns True if successful, False otherwise.
    """
    try:
        issue = repo.get_issue(issue_number)

        # Skip if already closed
        if issue.state == "closed":
            print(f"[INFO] Issue #{issue_number} is already closed")
            return False

        # Post comment and close
        comment = (
            f"This meeting occurred more than {STALE_THRESHOLD_HOURS} hours ago. "
            "Closing automatically."
        )
        issue.create_comment(comment)
        issue.edit(state="closed")

        print(f"[INFO] Closed issue #{issue_number}: {meeting_title}")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to close issue #{issue_number}: {e}")
        return False


def main():
    # Get GitHub token and repository
    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        print("[ERROR] GITHUB_TOKEN environment variable not set")
        sys.exit(1)

    repo_name = os.environ.get("GITHUB_REPOSITORY")
    if not repo_name:
        print("[ERROR] GITHUB_REPOSITORY environment variable not set")
        sys.exit(1)

    # Initialize GitHub client
    gh = Github(github_token)
    repo = gh.get_repo(repo_name)

    # Load mapping
    mapping = load_mapping()
    if not mapping:
        print("[INFO] No meetings found in mapping file")
        return

    closed_count = 0

    # Iterate through all call series, checking only recent occurrences
    for call_series, data in mapping.items():
        occurrences = data.get("occurrences", [])

        # Only check the last 3 occurrences per series (older ones are already closed)
        for occurrence in occurrences[-3:]:
            issue_number = occurrence.get("issue_number")
            issue_title = occurrence.get("issue_title", "Unknown")

            if not issue_number:
                continue

            # Check if meeting is stale
            if not is_meeting_stale(occurrence):
                continue

            # Attempt to close the issue
            if close_issue_with_comment(repo, issue_number, issue_title):
                closed_count += 1

    print(f"[INFO] Closed {closed_count} stale meeting issue(s)")


if __name__ == "__main__":
    main()
