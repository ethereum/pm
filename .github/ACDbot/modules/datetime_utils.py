import re
import calendar
from datetime import datetime
from typing import Optional


def parse_datetime_string(datetime_str: str) -> Optional[datetime]:
    """
    Parse a datetime string in various common formats.

    Args:
        datetime_str: The datetime string to parse

    Returns:
        Parsed datetime object or None if parsing fails
    """
    if not datetime_str:
        return None

    # Try ISO format first (what's stored internally)
    if datetime_str.endswith('Z'):
        try:
            return datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
        except ValueError:
            pass

    # Try standard format: "April 24, 2025, 14:00 UTC"
    try:
        return datetime.strptime(datetime_str, "%B %d, %Y, %H:%M UTC")
    except ValueError:
        pass

    # Try abbreviated month format: "Aug 24, 2025, 14:00 UTC"
    try:
        return datetime.strptime(datetime_str, "%b %d, %Y, %H:%M UTC")
    except ValueError:
        pass

    # Try to handle case insensitivity and comma variations for all month names
    try:
        normalized_str = datetime_str

        # First, handle comma after month: "Sept, 10, 2025" -> "Sept 10, 2025"
        normalized_str = re.sub(r'([A-Za-z]+),\s+(\d+)', r'\1 \2', normalized_str)

        # Handle non-standard month abbreviations (case insensitive)
        month_mappings = {
            'sept': 'Sep',
            'june': 'Jun',
            'july': 'Jul'
        }

        # Check for non-standard abbreviations (case insensitive)
        for non_standard, standard in month_mappings.items():
            # Use case-insensitive replacement
            pattern = re.compile(re.escape(non_standard), re.IGNORECASE)
            if pattern.search(normalized_str):
                normalized_str = pattern.sub(standard, normalized_str)
                break

        # Try parsing with the normalized string (try both comma formats)
        if normalized_str != datetime_str:
            try:
                return datetime.strptime(normalized_str, "%b %d, %Y, %H:%M UTC")
            except ValueError:
                return datetime.strptime(normalized_str, "%b %d %Y, %H:%M UTC")
    except ValueError:
        pass

    # Try standard formats with case-insensitive month names
    try:
        # Handle case insensitivity for all standard month names
        # Try to fix case by capitalizing first letter of each word
        case_normalized = ' '.join(word.capitalize() for word in datetime_str.split())

        # Remove comma after month if present: "April, 24" -> "April 24"
        case_normalized = re.sub(r'([A-Za-z]+),\s+(\d+)', r'\1 \2', case_normalized)

        if case_normalized != datetime_str:
            # Try all the standard formats with case-corrected input
            formats_to_try = [
                "%B %d, %Y, %H:%M UTC",  # Full month with comma
                "%b %d, %Y, %H:%M UTC",  # Abbreviated month with comma
                "%B %d %Y, %H:%M UTC",   # Full month without comma before year
                "%b %d %Y, %H:%M UTC"    # Abbreviated month without comma before year
            ]

            for fmt in formats_to_try:
                try:
                    return datetime.strptime(case_normalized, fmt)
                except ValueError:
                    continue
    except ValueError:
        pass

    # Try format without comma before year: "April 24 2025, 14:00 UTC"
    try:
        return datetime.strptime(datetime_str, "%B %d %Y, %H:%M UTC")
    except ValueError:
        pass

    # Try abbreviated month without comma: "Aug 24 2025, 14:00 UTC"
    try:
        return datetime.strptime(datetime_str, "%b %d %Y, %H:%M UTC")
    except ValueError:
        pass

    # Try with ordinal dates (normalize first)
    try:
        ordinal_pattern = r'(\d+)(st|nd|rd|th)'
        normalized_str = re.sub(ordinal_pattern, r'\1', datetime_str)
        return datetime.strptime(normalized_str, "%d %B %Y, %H:%M UTC")
    except ValueError:
        pass

    return None


def format_hour_for_savvytime(hour: int) -> str:
    """
    Convert 24-hour format to savvytime's AM/PM format.

    Args:
        hour: Hour in 24-hour format (0-23)

    Returns:
        Hour formatted for savvytime URLs (e.g., "2pm", "9am", "12am")
    """
    if hour == 0:
        return "12am"
    elif hour < 12:
        return f"{hour}am"
    elif hour == 12:
        return "12pm"
    else:
        return f"{hour-12}pm"


def generate_savvytime_url(dt: datetime) -> str:
    """
    Generate a savvytime.com converter URL for a given datetime.

    Args:
        dt: datetime object in UTC

    Returns:
        savvytime.com URL string
    """
    month_name = calendar.month_name[dt.month].lower()
    day = dt.day
    year = dt.year
    hour = dt.hour

    time_str = format_hour_for_savvytime(hour)

    # Format: https://savvytime.com/converter/utc/aug-4-2025/2pm
    return f"https://savvytime.com/converter/utc/{month_name[:3]}-{day}-{year}/{time_str}"


def generate_savvytime_link(datetime_str: str) -> str:
    """
    Generate a markdown-formatted savvytime.com link from a datetime string.

    Args:
        datetime_str: The datetime string to convert

    Returns:
        Markdown link with formatted display text and savvytime URL,
        or the original string if parsing fails
    """
    try:
        parsed_dt = parse_datetime_string(datetime_str)

        if not parsed_dt:
            print(f"[DEBUG] Could not parse datetime string for savvytime link: {datetime_str}")
            return datetime_str

        # Generate the savvytime URL
        savvytime_url = generate_savvytime_url(parsed_dt)

        # Create the markdown link with formatted display text
        display_text = parsed_dt.strftime("%B %d, %Y, %H:%M UTC")
        markdown_link = f"[{display_text}]({savvytime_url})"

        print(f"[DEBUG] Generated savvytime link: {markdown_link}")
        return markdown_link

    except Exception as e:
        print(f"[ERROR] Failed to generate savvytime link: {e}")
        return datetime_str


def format_datetime_display(dt: datetime, include_timezone: bool = True) -> str:
    """
    Format a datetime object for display purposes.

    Args:
        dt: datetime object to format
        include_timezone: Whether to include "UTC" suffix

    Returns:
        Formatted datetime string (e.g., "August 04, 2025, 14:00 UTC")
    """
    formatted = dt.strftime("%B %d, %Y, %H:%M")
    if include_timezone:
        formatted += " UTC"
    return formatted


def is_valid_datetime_format(datetime_str: str) -> bool:
    """
    Check if a string is in a valid datetime format that can be parsed.

    Args:
        datetime_str: The datetime string to validate

    Returns:
        True if the string can be parsed as a datetime, False otherwise
    """
    return parse_datetime_string(datetime_str) is not None


def extract_datetime_from_markdown_link(link_text: str) -> Optional[str]:
    """
    Extract the datetime portion from a markdown link.

    Args:
        link_text: Markdown link text like "[Aug 4, 2025, 14:00 UTC](https://...)"

    Returns:
        Extracted datetime string or None if not a valid markdown link
    """
    # Pattern to match [datetime text](url)
    pattern = r'\[([^\]]+)\]\([^)]+\)'
    match = re.match(pattern, link_text)

    if match:
        return match.group(1)

    return None


def parse_iso_datetime(iso_datetime_str: str) -> Optional[datetime]:
    """
    Parse an ISO datetime string (handles both with and without 'Z' suffix).

    Args:
        iso_datetime_str: ISO format datetime string

    Returns:
        Parsed datetime object or None if parsing fails
    """
    try:
        if iso_datetime_str.endswith('Z'):
            return datetime.fromisoformat(iso_datetime_str.replace('Z', '+00:00'))
        else:
            return datetime.fromisoformat(iso_datetime_str)
    except Exception:
        return None


def format_datetime_for_discourse(iso_datetime_str: str, duration_minutes: int) -> str:
    """
    Format datetime for Discourse topic body display.

    Args:
        iso_datetime_str: ISO format datetime string
        duration_minutes: Duration of the meeting in minutes

    Returns:
        Formatted string like "**Meeting Time:** Monday, August 04, 2025 at 14:00 UTC (90 minutes)"
        or fallback format if parsing fails
    """
    try:
        dt = parse_iso_datetime(iso_datetime_str)
        if dt:
            formatted_date = dt.strftime("%A, %B %d, %Y")
            formatted_time = dt.strftime("%H:%M UTC")
            return f"**Meeting Time:** {formatted_date} at {formatted_time} ({duration_minutes} minutes)"
    except Exception as e:
        print(f"[WARN] Failed to format meeting time: {e}")

    # Fallback to raw time info
    return f"**Meeting Time:** {iso_datetime_str} ({duration_minutes} minutes)"


def format_datetime_for_stream_display(iso_datetime_str: str) -> str:
    """
    Format datetime for YouTube stream display.

    Args:
        iso_datetime_str: ISO format datetime string

    Returns:
        Formatted string like " (Aug 04, 2025)" or empty string if parsing fails
    """
    try:
        dt = parse_iso_datetime(iso_datetime_str)
        if dt:
            return f" ({dt.strftime('%b %d, %Y')})"
    except Exception as e:
        print(f"[DEBUG] Error formatting stream date: {e}")

    return ""
