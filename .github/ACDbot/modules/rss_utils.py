import os
import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pytz
import json

RSS_FILE_PATH = ".github/ACDbot/rss/meetings.xml"

def ensure_rss_directory():
    """Ensure the RSS directory exists"""
    os.makedirs(os.path.dirname(RSS_FILE_PATH), exist_ok=True)

def create_or_update_rss_feed(mapping):
    """
    Creates or updates the RSS feed with meeting information
    Args:
        mapping: The meeting-topic mapping dictionary
    """
    ensure_rss_directory()

    # Create RSS feed structure if it doesn't exist
    if not os.path.exists(RSS_FILE_PATH):
        create_new_rss_feed()

    # Load existing RSS feed
    tree = ET.parse(RSS_FILE_PATH)
    root = tree.getroot()
    channel = root.find('channel')

    # Update lastBuildDate
    last_build_date = channel.find('lastBuildDate')
    now = datetime.datetime.now(pytz.UTC)
    last_build_date.text = now.strftime("%a, %d %b %Y %H:%M:%S %z")

    # Remove existing items first to rebuild based on current mapping state
    existing_items = channel.findall('item')
    for item in existing_items:
        channel.remove(item)

    # Add items based on occurrences
    for call_series, series_data in mapping.items():
        if not isinstance(series_data, dict):
            continue

        if call_series == "one-off":
            # One-off meetings: each entry is an occurrence
            for meeting_id, entry in series_data.items():
                if not isinstance(entry, dict):
                    continue

                item = ET.SubElement(channel, 'item')
                issue_number = entry.get('issue_number')

                # Title (from entry)
                title_elem = ET.SubElement(item, 'title')
                title_elem.text = entry.get('issue_title', f"One-off Meeting {meeting_id}")

                # Link (to entry's Discourse topic)
                link_elem = ET.SubElement(item, 'link')
                discourse_topic_id = entry.get('discourse_topic_id')
                if discourse_topic_id:
                    discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{discourse_topic_id}"
                    link_elem.text = discourse_url
                else:
                    link_elem.text = os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org') # Fallback link

                # Description
                desc_elem = ET.SubElement(item, 'description')
                desc_content = f"<p><strong>Meeting ID:</strong> {meeting_id}</p>"
                desc_content += f"<p><strong>Issue:</strong> <a href='https://github.com/{os.environ.get('GITHUB_REPOSITORY', '')}/issues/{issue_number}'>#{issue_number}</a></p>"

                # Add start time and duration from entry
                start_time = entry.get('start_time')
                duration = entry.get('duration')
                if start_time:
                    try:
                        dt_occ = datetime.datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                        formatted_time = dt_occ.strftime("%Y-%m-%d %H:%M UTC")
                        desc_content += f"<p><strong>Start Time:</strong> {formatted_time}</p>"
                    except Exception as e:
                        print(f"[WARN] Error formatting entry start time {start_time}: {e}")
                        desc_content += f"<p><strong>Start Time:</strong> {start_time}</p>"

                if duration:
                    desc_content += f"<p><strong>Duration:</strong> {duration} minutes</p>"

                # Add YouTube stream links (from entry)
                entry_youtube_streams = entry.get('youtube_streams', [])
                if entry_youtube_streams:
                    desc_content += "<p><strong>YouTube Streams:</strong></p><ul>"
                    for i, stream in enumerate(entry_youtube_streams, 1):
                        stream_url = stream.get('stream_url')
                        if stream_url:
                            desc_content += f"<li><a href='{stream_url}'>Stream #{i}</a></li>"
                    desc_content += "</ul>"

                desc_elem.text = desc_content

                # Add pubDate
                pub_date_elem = ET.SubElement(item, 'pubDate')
                if start_time:
                    try:
                        dt_occ = datetime.datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                        pub_date_elem.text = dt_occ.strftime("%a, %d %b %Y %H:%M:%S %z")
                    except Exception as e:
                        print(f"[WARN] Error formatting pubDate for entry {issue_number}: {e}")
                        pub_date_elem.text = datetime.datetime.now(pytz.UTC).strftime("%a, %d %b %Y %H:%M:%S %z")
                else:
                    pub_date_elem.text = datetime.datetime.now(pytz.UTC).strftime("%a, %d %b %Y %H:%M:%S %z")

        else:
            # Recurring series: Create an item for each occurrence
            if "occurrences" in series_data and isinstance(series_data["occurrences"], list):
                for occurrence in series_data["occurrences"]:
                    if not isinstance(occurrence, dict):
                        continue

                    item = ET.SubElement(channel, 'item')
                    issue_number = occurrence.get('issue_number')

                    # Title (from occurrence)
                    title_elem = ET.SubElement(item, 'title')
                    title_elem.text = occurrence.get('issue_title', f"{call_series.upper()} - Occurrence {issue_number}")

                    # Link (to occurrence's Discourse topic)
                    link_elem = ET.SubElement(item, 'link')
                    discourse_topic_id = occurrence.get('discourse_topic_id')
                    if discourse_topic_id:
                        discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{discourse_topic_id}"
                        link_elem.text = discourse_url
                    else:
                        link_elem.text = os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org') # Fallback link

                    # Description
                    desc_elem = ET.SubElement(item, 'description')
                    desc_content = f"<p><strong>Series:</strong> {call_series.upper()}</p>"
                    desc_content += f"<p><strong>Occurrence Issue:</strong> <a href='https://github.com/{os.environ.get('GITHUB_REPOSITORY', '')}/issues/{issue_number}'>#{issue_number}</a></p>"

                    # Add start time and duration from occurrence
                    start_time = occurrence.get('start_time')
                    duration = occurrence.get('duration')
                    if start_time:
                        try:
                            dt_occ = datetime.datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                            formatted_time = dt_occ.strftime("%Y-%m-%d %H:%M UTC")
                            desc_content += f"<p><strong>Start Time:</strong> {formatted_time}</p>"
                        except Exception as e:
                            print(f"[WARN] Error formatting occurrence start time {start_time}: {e}")
                            desc_content += f"<p><strong>Start Time:</strong> {start_time}</p>"

                    if duration:
                        desc_content += f"<p><strong>Duration:</strong> {duration} minutes</p>"

                    # Add series recurring info
                    if series_data.get('is_recurring'):
                        occurrence_rate = series_data.get('occurrence_rate', 'none')
                        desc_content += f"<p><strong>Recurring Series:</strong> {occurrence_rate}</p>"

                    # Add YouTube stream links (from occurrence)
                    occurrence_youtube_streams = occurrence.get('youtube_streams', [])
                    if occurrence_youtube_streams:
                        desc_content += "<p><strong>YouTube Streams (Occurrence):</strong></p><ul>"
                        for i, stream in enumerate(occurrence_youtube_streams, 1):
                            stream_url = stream.get('stream_url')
                            if stream_url:
                                desc_content += f"<li><a href='{stream_url}'>Stream #{i}</a></li>"
                    desc_content += "</ul>"

                # Add occurrence-specific YouTube video if available
                youtube_video_id = occurrence.get('youtube_video_id')
                if youtube_video_id:
                    youtube_url = f"https://youtu.be/{youtube_video_id}"
                    desc_content += f"<p><strong>Recording (This Occurrence):</strong> <a href='{youtube_url}'>{youtube_url}</a></p>"

                # Add occurrence-specific notifications
                notifications = occurrence.get('notifications', [])
                if notifications:
                    desc_content += "<h3>Occurrence Updates:</h3><ul>"
                    # Sort notifications by timestamp if possible
                    try:
                        notifications.sort(key=lambda x: datetime.datetime.fromisoformat(x.get('timestamp')), reverse=True)
                    except:
                        pass # Ignore sorting errors

                    for notification in notifications:
                        timestamp = notification.get('timestamp')
                        n_type = notification.get('type')
                        n_content = notification.get('content')
                        n_url = notification.get('url', '')

                        formatted_time_notif = timestamp
                        try:
                            dt_notif = datetime.datetime.fromisoformat(timestamp)
                            formatted_time_notif = dt_notif.strftime("%Y-%m-%d %H:%M UTC")
                        except:
                            pass

                        if n_url:
                            desc_content += f"<li><strong>{formatted_time_notif} - {n_type}:</strong> <a href='{n_url}'>{n_content}</a></li>"
                        else:
                            desc_content += f"<li><strong>{formatted_time_notif} - {n_type}:</strong> {n_content}</li>"
                    desc_content += "</ul>"

                desc_elem.text = desc_content

                # Publication date (use occurrence start time)
                pub_date_elem = ET.SubElement(item, 'pubDate')
                if start_time:
                    try:
                        dt_pub = datetime.datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                        pub_date_elem.text = dt_pub.strftime("%a, %d %b %Y %H:%M:%S %z")
                    except:
                        pub_date_elem.text = now.strftime("%a, %d %b %Y %H:%M:%S %z")
                else:
                    pub_date_elem.text = now.strftime("%a, %d %b %Y %H:%M:%S %z")

                # GUID (unique per occurrence)
                guid_elem = ET.SubElement(item, 'guid')
                guid_elem.set('isPermaLink', 'false')
                guid_elem.text = f"meeting-{meeting_id}-occurrence-{issue_number}"

    # Write updated RSS feed
    write_rss_feed(tree)

    return RSS_FILE_PATH

def create_new_rss_feed():
    """Creates a new RSS feed file with basic structure"""
    rss = ET.Element('rss')
    rss.set('version', '2.0')

    channel = ET.SubElement(rss, 'channel')

    # Required channel elements
    title = ET.SubElement(channel, 'title')
    title.text = "Ethereum Protocol Meetings"

    link = ET.SubElement(channel, 'link')
    link.text = os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')

    description = ET.SubElement(channel, 'description')
    description.text = "RSS feed for Ethereum Protocol Meetings"

    # Optional channel elements
    language = ET.SubElement(channel, 'language')
    language.text = "en-us"

    now = datetime.datetime.now(pytz.UTC)

    pub_date = ET.SubElement(channel, 'pubDate')
    pub_date.text = now.strftime("%a, %d %b %Y %H:%M:%S %z")

    last_build_date = ET.SubElement(channel, 'lastBuildDate')
    last_build_date.text = now.strftime("%a, %d %b %Y %H:%M:%S %z")

    generator = ET.SubElement(channel, 'generator')
    generator.text = "ACDbot RSS Generator"

    docs = ET.SubElement(channel, 'docs')
    docs.text = "https://www.rssboard.org/rss-specification"

    # Write to file
    tree = ET.ElementTree(rss)
    write_rss_feed(tree)

def write_rss_feed(tree):
    """Writes the RSS feed to file with pretty formatting"""
    rough_string = ET.tostring(tree.getroot(), 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    with open(RSS_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)

def add_meeting_to_rss(meeting_id, entry):
    """
    Adds a single meeting to the RSS feed
    Args:
        meeting_id: The meeting ID
        entry: The meeting entry dictionary
    """
    # Load existing mapping
    from .transcript import load_meeting_topic_mapping
    mapping = load_meeting_topic_mapping()

    # Update mapping with new entry
    mapping[meeting_id] = entry

    # Update RSS feed
    create_or_update_rss_feed(mapping)

# Helper to find occurrence by issue number (copied from upload_zoom_recording.py)
def find_occurrence_by_issue_number(series_entry, issue_number):
    """Helper function to find an occurrence by issue number."""
    if not series_entry or "occurrences" not in series_entry:
        return None, -1
    for index, occ in enumerate(series_entry["occurrences"]):
        # Ensure comparison is between same types if issue_number can be string/int
        if str(occ.get("issue_number")) == str(issue_number):
            return occ, index
    return None, -1

# New function to add notifications to existing meeting entries
def add_notification_to_meeting(meeting_id, occurrence_issue_number, notification_type, content, url=None):
    """
    Adds a notification to a specific meeting occurrence in the mapping.

    Args:
        meeting_id: The meeting ID
        occurrence_issue_number: The issue number identifying the specific occurrence.
        notification_type: Type of notification (issue_created, discourse_post, youtube_upload, summary)
        content: Notification content/description
        url: Optional URL associated with the notification
    """
    # Load existing mapping
    # Use absolute import if running as script, relative if part of package
    try:
        from .transcript import load_meeting_topic_mapping, save_meeting_topic_mapping # Relative import
    except ImportError:
        # Assume running as script, need a way to load/save mapping
        # This might require moving load/save functions out or duplicating them
        print("[WARN] Could not perform relative import for mapping functions in rss_utils.")
        # Fallback: Define simple load/save here if needed, or rely on caller to save
        def load_meeting_topic_mapping(): # Simple fallback
             if os.path.exists(".github/ACDbot/meeting_topic_mapping.json"): # Adjust path if needed
                 with open(".github/ACDbot/meeting_topic_mapping.json", "r") as f:
                     return json.load(f)
             return {}
        def save_meeting_topic_mapping(m): # Simple fallback
             with open(".github/ACDbot/meeting_topic_mapping.json", "w") as f:
                 json.dump(m, f, indent=2)

    mapping = load_meeting_topic_mapping()

    series_entry = mapping.get(str(meeting_id))

    if not series_entry:
        print(f"[ERROR] Meeting series {meeting_id} not found in mapping for RSS notification.")
        return

    # Find the specific occurrence
    matched_occurrence, occurrence_index = find_occurrence_by_issue_number(series_entry, occurrence_issue_number)

    if matched_occurrence is None:
        print(f"[ERROR] Occurrence {occurrence_issue_number} not found in meeting {meeting_id} for RSS notification.")
        return

    # Get or create notifications list for this occurrence
    if "notifications" not in matched_occurrence:
        matched_occurrence["notifications"] = []

    # Create notification entry with timestamp
    notification = {
        "type": notification_type,
        "content": content,
        "timestamp": datetime.datetime.now(pytz.UTC).isoformat(),
    }

    if url:
        notification["url"] = url

    # Add to notifications list within the occurrence
    matched_occurrence["notifications"].append(notification)

    # Update the occurrence in the main mapping structure
    mapping[str(meeting_id)]["occurrences"][occurrence_index] = matched_occurrence

    # Save mapping
    save_meeting_topic_mapping(mapping)

    # Update RSS feed
    create_or_update_rss_feed(mapping)