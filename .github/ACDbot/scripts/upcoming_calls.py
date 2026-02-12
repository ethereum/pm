#!/usr/bin/env python3
"""
Upcoming Calls Report

Generates a summary of upcoming calls for the next week, including:
- Title
- Host and alternative hosts (from Zoom API, if available)
- Date and time
- YouTube stream details (title, scheduled time, status)
- Warnings for potential issues

Sends the report to a webhook for Protocol Support team review.
"""

import argparse
import json
import os
import re
import requests
import sys
from datetime import datetime, timedelta, timezone

# Resolve paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ACDBOT_DIR = os.path.dirname(SCRIPT_DIR)

# Add ACDbot dir to path so we can import modules
sys.path.insert(0, ACDBOT_DIR)

from modules.call_series_config import get_call_series_config


def email_to_first_name(email):
    """Extract a short display name from an email address.

    'first.last@ethereum.org' -> 'first'
    """
    local = email.split("@")[0]
    return local.split(".")[0]


def format_hosts(zoom_info):
    """Format host + alt hosts into a single compact string, or None."""
    if not zoom_info:
        return None
    host = email_to_first_name(zoom_info["host_email"])
    alt_hosts_raw = zoom_info.get("alternative_hosts", "")
    if alt_hosts_raw:
        alt_names = ", ".join(
            email_to_first_name(e.strip())
            for e in re.split(r"[,;]", alt_hosts_raw)
            if e.strip()
        )
        return f"Host: {host}. Alt hosts: {alt_names}"
    return f"Host: {host}"


def load_mapping():
    """Load the meeting topic mapping file."""
    mapping_path = os.path.join(ACDBOT_DIR, "meeting_topic_mapping.json")
    with open(mapping_path, "r") as f:
        return json.load(f)


def get_zoom_meeting_details(meeting_id):
    """Fetch host and alternative host info from Zoom API.

    Returns dict with host_email and alternative_hosts, or None if unavailable.
    """
    try:
        from modules.zoom import get_meeting

        details = get_meeting(meeting_id)
        return {
            "host_email": details.get("host_email", "N/A"),
            "alternative_hosts": details.get("settings", {}).get(
                "alternative_hosts", ""
            ),
        }
    except Exception as e:
        print(f"  [Warning] Could not fetch Zoom details for meeting {meeting_id}: {e}")
        return None


def extract_video_id(youtube_url):
    """Extract video ID from a YouTube URL."""
    if not youtube_url:
        return None
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", youtube_url)
    return match.group(1) if match else None


def fetch_youtube_details(video_ids):
    """Batch-fetch YouTube video details for a list of video IDs.

    Returns (results, error) tuple:
      - results: dict mapping video_id -> {title, scheduled_start_time, status}
      - error: error message string if auth/API failed, None on success
    """
    if not video_ids:
        return {}, None

    try:
        from modules.youtube_utils import get_youtube_service

        youtube = get_youtube_service()

        results = {}
        # YouTube API allows up to 50 IDs per request
        for i in range(0, len(video_ids), 50):
            batch = video_ids[i : i + 50]
            response = (
                youtube.videos()
                .list(part="snippet,liveStreamingDetails", id=",".join(batch))
                .execute()
            )

            for item in response.get("items", []):
                vid = item["id"]
                snippet = item.get("snippet", {})
                live_details = item.get("liveStreamingDetails", {})

                scheduled_start = live_details.get("scheduledStartTime")
                scheduled_dt = None
                if scheduled_start:
                    try:
                        scheduled_dt = datetime.fromisoformat(
                            scheduled_start.replace("Z", "+00:00")
                        )
                    except (ValueError, TypeError):
                        pass

                results[vid] = {
                    "title": snippet.get("title", "N/A"),
                    "scheduled_start_time": scheduled_dt,
                    "broadcast_status": snippet.get(
                        "liveBroadcastContent", "unknown"
                    ),
                }

        return results, None

    except Exception as e:
        return {}, str(e)


def find_upcoming_calls(mapping, days_ahead=7):
    """Find all occurrences scheduled within the next `days_ahead` days."""
    now = datetime.now(timezone.utc)
    cutoff = now + timedelta(days=days_ahead)

    upcoming = []

    for series_key, series_data in mapping.items():
        if not isinstance(series_data, dict):
            continue

        meeting_id = series_data.get("meeting_id")

        for occurrence in series_data.get("occurrences", []):
            start_time_str = occurrence.get("start_time")
            if not start_time_str:
                continue

            try:
                start_time = datetime.fromisoformat(
                    start_time_str.replace("Z", "+00:00")
                )
            except (ValueError, TypeError):
                continue

            if now <= start_time <= cutoff:
                youtube_streams = occurrence.get("youtube_streams") or []
                youtube_url = (
                    youtube_streams[0].get("stream_url") if youtube_streams else None
                )

                upcoming.append(
                    {
                        "series_key": series_key,
                        "meeting_id": meeting_id,
                        "title": occurrence.get("issue_title", "Untitled"),
                        "start_time": start_time,
                        "youtube_url": youtube_url,
                        "issue_number": occurrence.get("issue_number"),
                        "occurrence_number": occurrence.get("occurrence_number"),
                    }
                )

    upcoming.sort(key=lambda x: x["start_time"])
    return upcoming


def check_warnings(upcoming_calls, youtube_cache, youtube_enabled=True, youtube_error=None):
    """Check for potential issues and return a list of warning strings."""
    warnings = []

    # Surface YouTube credential/API failure as a single top-level warning
    if youtube_error:
        warnings.append(f"YouTube API error (stream details unavailable): {youtube_error}")

    for call in upcoming_calls:
        label = call["title"]
        series_config = get_call_series_config(call["series_key"])

        # Check: call series config says needs YouTube but no stream URL exists
        if series_config:
            autopilot = series_config.get("autopilot_defaults", {})
            if autopilot.get("need_youtube_streams") and not call["youtube_url"]:
                warnings.append(
                    f"{label}: YouTube stream expected (need_youtube_streams=true) but none scheduled"
                )

        # YouTube-specific checks (only when the API actually succeeded)
        video_id = extract_video_id(call.get("youtube_url"))
        if youtube_error:
            # Skip per-video checks when the API itself failed
            continue

        if video_id and video_id in youtube_cache:
            yt = youtube_cache[video_id]

            # Check: YouTube scheduled time vs mapping start time
            if yt["scheduled_start_time"] and call["start_time"]:
                diff = abs(
                    (yt["scheduled_start_time"] - call["start_time"]).total_seconds()
                )
                if diff > 300:  # more than 5 minutes off
                    yt_time = yt["scheduled_start_time"].strftime("%H:%M UTC")
                    call_time = call["start_time"].strftime("%H:%M UTC")
                    warnings.append(
                        f"{label}: YouTube scheduled time ({yt_time}) differs from meeting time ({call_time})"
                    )

            # Check: stream not in "upcoming" status
            status = yt.get("broadcast_status", "unknown")
            if status == "none":
                warnings.append(
                    f"{label}: YouTube stream is not marked as an upcoming broadcast (status: {status})"
                )

        elif youtube_enabled and call["youtube_url"] and video_id and video_id not in youtube_cache:
            warnings.append(
                f"{label}: YouTube video {video_id} not found (deleted or private?)"
            )

    return warnings


def build_markdown(upcoming_calls, zoom_details_cache, youtube_cache, days_ahead=7, youtube_enabled=True, youtube_error=None):
    """Build a Markdown-formatted report string."""
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = []

    if not upcoming_calls:
        lines.append(f"No upcoming calls found in the next {days_ahead} days (as of {now_str}).")
        return "\n".join(lines)

    lines.append(f"#### Upcoming Calls — Next {days_ahead} Days")
    lines.append(f"*Generated: {now_str}*")

    for call in upcoming_calls:
        # Title linked to issue
        title = call["title"]
        if call["issue_number"]:
            issue_url = f"https://github.com/ethereum/pm/issues/{call['issue_number']}"
            title = f"[{title}]({issue_url})"

        # Flag first occurrence of a new call series
        is_new = call.get("occurrence_number") == 1
        new_badge = " :new: **NEW SERIES**" if is_new else ""

        lines.append("")
        lines.append("---")
        lines.append(f"**{title}**{new_badge}")

        # Host line
        zoom_info = zoom_details_cache.get(call["meeting_id"])
        host_str = format_hosts(zoom_info)
        if host_str:
            lines.append(f"- {host_str}")

        lines.append(
            f"- **Date/Time:** {call['start_time'].strftime('%A, %B %d, %Y at %H:%M UTC')}"
        )

        # YouTube stream
        video_id = extract_video_id(call.get("youtube_url"))
        yt = youtube_cache.get(video_id) if video_id else None

        if yt:
            yt_line = f"- **YouTube:** [{yt['title']}]({call['youtube_url']})"
            details = []
            if yt["scheduled_start_time"]:
                details.append(
                    f"Scheduled: {yt['scheduled_start_time'].strftime('%b %d at %H:%M UTC')}"
                )
            details.append(f"Status: {yt['broadcast_status']}")
            yt_line += f" — {' | '.join(details)}"
            lines.append(yt_line)
        elif call["youtube_url"] and youtube_error:
            lines.append(f"- **YouTube:** [{call['youtube_url']}]({call['youtube_url']}) _(API error — see warnings)_")
        elif call["youtube_url"]:
            lines.append(f"- **YouTube:** [{call['youtube_url']}]({call['youtube_url']})")
        else:
            lines.append("- **YouTube:** No stream scheduled")

    # Warnings
    warnings = check_warnings(
        upcoming_calls, youtube_cache,
        youtube_enabled=youtube_enabled, youtube_error=youtube_error,
    )
    if warnings:
        lines.append("")
        lines.append("---")
        lines.append(f"**:warning: Warnings ({len(warnings)})**")
        for w in warnings:
            lines.append(f"- {w}")

    lines.append("")
    lines.append("---")
    lines.append(f"*{len(upcoming_calls)} call(s) in the next {days_ahead} days*")

    return "\n".join(lines)


def send_to_webhook(webhook_url, markdown_text):
    """Send the report to a Mattermost incoming webhook."""
    payload = {
        "username": "ACDbot",
        "text": markdown_text,
    }

    resp = requests.post(
        webhook_url,
        json=payload,
        headers={"Content-Type": "application/json"},
    )

    if resp.status_code == 200 and resp.text == "ok":
        print(f"\nWebhook: sent successfully to {webhook_url}")
    else:
        print(f"\nWebhook: failed ({resp.status_code}): {resp.text}")


def print_report(upcoming_calls, zoom_details_cache, youtube_cache, days_ahead=7, youtube_enabled=True, youtube_error=None):
    """Print a plain-text report to the terminal."""
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    if not upcoming_calls:
        print(
            f"No upcoming calls found in the next {days_ahead} days (as of {now_str})."
        )
        return

    print(f"{'=' * 60}")
    print(f"  UPCOMING CALLS - Next {days_ahead} Days")
    print(f"  Generated: {now_str}")
    print(f"{'=' * 60}")

    for call in upcoming_calls:
        # Flag first occurrence of a new call series
        is_new = call.get("occurrence_number") == 1
        new_badge = "  *** NEW SERIES ***" if is_new else ""

        # Title with issue number inline
        title = call["title"]
        if call["issue_number"]:
            title = f"{title} (#{call['issue_number']})"

        print(f"\n{'-' * 60}")
        print(f"  {title}{new_badge}")

        # Host line
        zoom_info = zoom_details_cache.get(call["meeting_id"])
        host_str = format_hosts(zoom_info)
        if host_str:
            print(f"  {host_str}")

        print(
            f"  Date/Time: {call['start_time'].strftime('%A, %B %d, %Y at %H:%M UTC')}"
        )

        # YouTube stream
        video_id = extract_video_id(call.get("youtube_url"))
        yt = youtube_cache.get(video_id) if video_id else None

        if yt:
            print(f"  YouTube:   {call['youtube_url']}")
            print(f"    Title:     {yt['title']}")
            if yt["scheduled_start_time"]:
                print(
                    f"    Scheduled: {yt['scheduled_start_time'].strftime('%A, %B %d, %Y at %H:%M UTC')}"
                )
            print(f"    Status:    {yt['broadcast_status']}")
        elif call["youtube_url"] and youtube_error:
            print(f"  YouTube:   {call['youtube_url']}")
            print(f"    (YouTube API error - see warnings)")
        elif call["youtube_url"]:
            print(f"  YouTube:   {call['youtube_url']}")
            print(f"    (details not available)")
        else:
            print(f"  YouTube:   No stream scheduled")

    # Warnings section
    warnings = check_warnings(upcoming_calls, youtube_cache, youtube_enabled=youtube_enabled, youtube_error=youtube_error)
    if warnings:
        print(f"\n{'=' * 60}")
        print(f"  WARNINGS ({len(warnings)})")
        print(f"{'=' * 60}")
        for w in warnings:
            print(f"  ! {w}")

    print(f"\n{'=' * 60}")
    print(f"  Total: {len(upcoming_calls)} call(s) in the next {days_ahead} days")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(
        description="Report upcoming calls for the next week"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Number of days to look ahead (default: 7)",
    )
    parser.add_argument(
        "--no-zoom",
        action="store_true",
        help="Skip Zoom API calls for host info",
    )
    parser.add_argument(
        "--no-youtube",
        action="store_true",
        help="Skip YouTube API calls for stream details",
    )
    parser.add_argument(
        "--webhook-url",
        default=os.environ.get("MATTERMOST_BOT_WEBHOOK_URL", ""),
        help="Mattermost webhook URL (or set MATTERMOST_BOT_WEBHOOK_URL env var)",
    )
    args = parser.parse_args()

    mapping = load_mapping()
    upcoming = find_upcoming_calls(mapping, days_ahead=args.days)

    # Fetch Zoom details for each unique meeting ID
    zoom_details_cache = {}
    if not args.no_zoom:
        unique_meeting_ids = set()
        for call in upcoming:
            mid = call.get("meeting_id")
            if mid and mid not in ("custom", "pending"):
                unique_meeting_ids.add(mid)

        for mid in unique_meeting_ids:
            details = get_zoom_meeting_details(mid)
            if details:
                zoom_details_cache[mid] = details

    # Fetch YouTube details for all streams in a single batch
    youtube_cache = {}
    youtube_error = None
    if not args.no_youtube:
        video_ids = []
        for call in upcoming:
            vid = extract_video_id(call.get("youtube_url"))
            if vid:
                video_ids.append(vid)

        if video_ids:
            youtube_cache, youtube_error = fetch_youtube_details(video_ids)

    report_kwargs = dict(
        upcoming_calls=upcoming,
        zoom_details_cache=zoom_details_cache,
        youtube_cache=youtube_cache,
        days_ahead=args.days,
        youtube_enabled=not args.no_youtube,
        youtube_error=youtube_error,
    )

    # Always print to terminal
    print_report(**report_kwargs)

    # Send to webhook if URL is provided
    if args.webhook_url:
        markdown = build_markdown(**report_kwargs)
        send_to_webhook(args.webhook_url, markdown)


if __name__ == "__main__":
    main()
