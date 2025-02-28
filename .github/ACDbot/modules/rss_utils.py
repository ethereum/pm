import os
import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pytz

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
    
    # Get existing item GUIDs to avoid duplicates
    existing_guids = set()
    for item in channel.findall('item'):
        guid = item.find('guid')
        if guid is not None:
            existing_guids.add(guid.text)
    
    # Add new meetings
    for meeting_id, entry in mapping.items():
        if not isinstance(entry, dict):
            continue
            
        # Skip if already in feed
        if f"meeting-{meeting_id}" in existing_guids:
            continue
            
        # Create new item
        item = ET.SubElement(channel, 'item')
        
        # Title
        title_elem = ET.SubElement(item, 'title')
        title_elem.text = entry.get('issue_title', f"Meeting {meeting_id}")
        
        # Link (to Discourse topic)
        link_elem = ET.SubElement(item, 'link')
        discourse_topic_id = entry.get('discourse_topic_id')
        discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{discourse_topic_id}"
        link_elem.text = discourse_url
        
        # Description
        desc_elem = ET.SubElement(item, 'description')
        
        # Build description content
        desc_content = f"<p><strong>Meeting ID:</strong> {meeting_id}</p>"
        
        # Add Zoom link if available
        zoom_link = entry.get('zoom_link')
        if zoom_link:
            desc_content += f"<p><strong>Zoom Link:</strong> <a href='{zoom_link}'>{zoom_link}</a></p>"
        
        # Add start time and duration
        start_time = entry.get('start_time')
        duration = entry.get('duration')
        if start_time:
            try:
                dt = datetime.datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                formatted_time = dt.strftime("%Y-%m-%d %H:%M UTC")
                desc_content += f"<p><strong>Start Time:</strong> {formatted_time}</p>"
            except:
                desc_content += f"<p><strong>Start Time:</strong> {start_time}</p>"
        
        if duration:
            desc_content += f"<p><strong>Duration:</strong> {duration} minutes</p>"
        
        # Add recurring info if applicable
        is_recurring = entry.get('is_recurring')
        if is_recurring:
            occurrence_rate = entry.get('occurrence_rate', 'none')
            desc_content += f"<p><strong>Recurring Meeting:</strong> {occurrence_rate}</p>"
            
            # Add YouTube stream links if available
            youtube_streams = entry.get('youtube_streams', [])
            if youtube_streams:
                desc_content += "<p><strong>YouTube Streams:</strong></p><ul>"
                for i, stream in enumerate(youtube_streams, 1):
                    stream_url = stream.get('stream_url')
                    if stream_url:
                        desc_content += f"<li><a href='{stream_url}'>Stream #{i}</a></li>"
                desc_content += "</ul>"
        
        # Add YouTube video if available
        youtube_video_id = entry.get('youtube_video_id')
        if youtube_video_id:
            youtube_url = f"https://youtu.be/{youtube_video_id}"
            desc_content += f"<p><strong>Recording:</strong> <a href='{youtube_url}'>{youtube_url}</a></p>"
        
        desc_elem.text = desc_content
        
        # Publication date
        pub_date_elem = ET.SubElement(item, 'pubDate')
        if start_time:
            try:
                dt = datetime.datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                pub_date_elem.text = dt.strftime("%a, %d %b %Y %H:%M:%S %z")
            except:
                pub_date_elem.text = now.strftime("%a, %d %b %Y %H:%M:%S %z")
        else:
            pub_date_elem.text = now.strftime("%a, %d %b %Y %H:%M:%S %z")
        
        # GUID
        guid_elem = ET.SubElement(item, 'guid')
        guid_elem.set('isPermaLink', 'false')
        guid_elem.text = f"meeting-{meeting_id}"
    
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