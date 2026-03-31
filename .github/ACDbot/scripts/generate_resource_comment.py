#!/usr/bin/env python3
"""
Generate GitHub Comment for Protocol Call Resources

This script reads the current mapping state and generates a formatted GitHub comment
showing all important resources for a specific meeting occurrence.
"""

import sys
import os
import json
import argparse
from datetime import datetime

# Add the modules directory to the path
modules_path = os.path.join('.github', 'ACDbot', 'modules')
sys.path.append(modules_path)

# Try to import zoom module - it's optional for passcode fetching
zoom_available = False
try:
    import zoom
    zoom_available = True
except (ImportError, KeyError) as e:
    print("⚠️  Zoom API unavailable (missing credentials) - passcodes will not be fetched")
    zoom = None

def load_mapping():
    """Load the current mapping data."""
    mapping_path = '.github/ACDbot/meeting_topic_mapping.json'
    try:
        with open(mapping_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Mapping file not found at {mapping_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in mapping file: {e}")
        return None

def find_occurrence_by_issue(mapping, issue_number):
    """Find an occurrence by GitHub issue number."""
    for call_series, data in mapping.items():
        if 'occurrences' in data:
            for occurrence in data['occurrences']:
                if occurrence.get('issue_number') == issue_number:
                    return call_series, occurrence
    return None, None

def format_datetime_friendly(iso_string):
    """Format ISO datetime string in a human-friendly way."""
    try:
        dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
        return dt.strftime('%B %d, %Y at %H:%M UTC')
    except (ValueError, AttributeError):
        return iso_string


def get_zoom_meeting_url(meeting_id):
    """Get Zoom meeting URL with embedded passcode if available."""
    if not meeting_id or meeting_id == "custom":
        return None

    # If zoom module is not available, return basic URL
    if not zoom_available or zoom is None:
        return f"https://zoom.us/j/{meeting_id}"

    try:
        enhanced_url = zoom.get_meeting_url_with_passcode(meeting_id)
        return enhanced_url
    except Exception as e:
        error_details = str(e)
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_json = e.response.json()
                error_code = error_json.get('code', 'unknown')
                error_message = error_json.get('message', 'No message')
                print(f"⚠️  Zoom API Error {error_code}: {error_message}")
                print(f"⚠️  Meeting ID: {meeting_id}, Status: {e.response.status_code}")
            except Exception:
                print(f"⚠️  Zoom API Error {e.response.status_code}: {error_details}")
        else:
            print(f"⚠️  Could not fetch Zoom meeting details: {error_details}")

        return f"https://zoom.us/j/{meeting_id}"


def generate_comment(call_series, occurrence, mapping):
    """Generate the GitHub comment text."""
    issue_number = occurrence.get('issue_number')
    issue_title = occurrence.get('issue_title', 'Unknown Meeting')
    start_time = occurrence.get('start_time')
    duration = occurrence.get('duration', 60)

    # Get series-level meeting ID
    series_data = mapping.get(call_series, {})
    meeting_id = series_data.get('meeting_id')
    issue_url = f"https://github.com/{os.environ.get('GITHUB_REPOSITORY', 'ethereum/pm')}/issues/{issue_number}"

    comment_lines = [
        "🎉 **Protocol Call Resources:**",
        "",
        f"📅 **Meeting**: {issue_title}",
    ]

    if start_time:
        comment_lines.append(f"🕐 **When**: {format_datetime_friendly(start_time)} ({duration} minutes)")

    comment_lines.append("")

    # Check for date parsing errors
    if start_time and not (isinstance(start_time, str) and start_time.endswith('Z')):
        comment_lines.extend([
            "⚠️ **Date Parsing Issue**: The date/time format could not be parsed automatically.",
            f"   Current value: `{start_time}`",
            "   Please edit the issue and use one of these formats:",
            "   • `April 24, 2026, 14:00 UTC`",
            "   • `Apr 24, 2026, 14:00 UTC`",
            "   • `2026-04-24T14:00:00Z`",
            ""
        ])

    # Zoom Meeting
    zoom_url = get_zoom_meeting_url(meeting_id)
    if zoom_url:
        comment_lines.append(f"✅ **Zoom**: [Join Meeting]({zoom_url})")
    elif meeting_id == "custom":
        comment_lines.append("🔗 **Zoom**: Custom meeting link (see issue description)")
    else:
        comment_lines.append("❌ **Zoom**: No meeting link available")

    # Calendar links
    import gcal
    view_link = gcal.build_calendar_view_link(start_time)

    details_parts = [f"Issue: {issue_url}"]
    if zoom_url:
        details_parts.insert(0, f"Meeting: {zoom_url}")
    add_link = gcal.build_calendar_add_link(issue_title, start_time, duration, "\n\n".join(details_parts))

    if view_link and add_link:
        comment_lines.append(f"✅ **Calendar**: [View]({view_link}) | [Add to Calendar]({add_link})")
    elif add_link:
        comment_lines.append(f"✅ **Calendar**: [Add to Calendar]({add_link})")
    elif view_link:
        comment_lines.append(f"✅ **Calendar**: [View]({view_link})")
    else:
        comment_lines.append("❌ **Calendar**: No calendar event found")

    # Discourse Topic
    discourse_topic_id = occurrence.get('discourse_topic_id')
    if discourse_topic_id:
        discourse_link = f"https://ethereum-magicians.org/t/{discourse_topic_id}"
        comment_lines.append(f"✅ **Discourse**: [Discussion Topic]({discourse_link})")
    else:
        comment_lines.append("❌ **Discourse**: No forum topic found")

    # YouTube Stream
    youtube_streams = occurrence.get('youtube_streams', [])
    if youtube_streams:
        first_stream = youtube_streams[0]
        stream_url = first_stream.get('stream_url')
        if stream_url:
            comment_lines.append(f"✅ **YouTube Live**: [Watch Live]({stream_url})")
        else:
            comment_lines.append("❌ **YouTube Live**: No livestream scheduled")
    else:
        comment_lines.append("❌ **YouTube Live**: No livestream scheduled")

    return "\n".join(comment_lines)

def main():
    parser = argparse.ArgumentParser(
        description='Generate GitHub comment for protocol call resources',
        epilog='Note: Zoom passcodes are included automatically when ZOOM_CLIENT_ID and related credentials are available.'
    )
    parser.add_argument('issue_number', type=int, help='GitHub issue number')
    parser.add_argument('--copy', action='store_true', help='Copy to clipboard (macOS only)')

    args = parser.parse_args()

    print(f"🔍 Looking up resources for issue #{args.issue_number}...")

    # Load mapping
    mapping = load_mapping()
    if not mapping:
        return 1

    # Find the occurrence
    call_series, occurrence = find_occurrence_by_issue(mapping, args.issue_number)
    if not occurrence:
        print(f"❌ Error: No occurrence found for issue #{args.issue_number}")
        print(f"💡 Available issues: {[occ.get('issue_number') for series in mapping.values() for occ in series.get('occurrences', [])]}")
        return 1

    print(f"✅ Found occurrence in call series: {call_series}")
    print(f"📋 Meeting: {occurrence.get('issue_title', 'Unknown')}")
    print()

    # Generate comment
    comment = generate_comment(call_series, occurrence, mapping)

    print("=" * 60)
    print("GENERATED GITHUB COMMENT:")
    print("=" * 60)
    print(comment)
    print("=" * 60)

    # Copy to clipboard if requested (macOS)
    if args.copy:
        try:
            import subprocess
            subprocess.run(['pbcopy'], input=comment.encode(), check=True)
            print("📋 Comment copied to clipboard!")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("⚠️  Could not copy to clipboard (pbcopy not available)")

    return 0

if __name__ == "__main__":
    sys.exit(main())
