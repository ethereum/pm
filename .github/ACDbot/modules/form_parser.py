"""
Form Parser Module

Handles parsing of GitHub Issue Form data for protocol calls.
Provides clean, focused parsing for the new form-based workflow.
"""

import re
from datetime import datetime
from typing import Dict, Optional, List, Tuple


class FormParser:
    """Parses GitHub Issue Form data for protocol calls."""

    def __init__(self):
        # Display name to call series key mapping
        self.call_series_mapping = {
            "All Core Devs - Consensus": "acdc",
            "All Core Devs - Execution": "acde",
            "All Core Devs - Testing": "acdt",
            "All Wallet Devs": "allwalletdevs",
            "Beam Call": "beam",
            "EIP Editing Office Hour": "eipeditingofficehour",
            "EIPIP Meeting": "eipip",
            "EIP-7732 Breakout Room": "epbs",
            "EIP-7928 Breakout Room": "bal",
            "EVM Resource Pricing Breakout": "resourcepricing",
            "eth_simulate": "ethsimulate",
            "Ethproofs Community Call": "ethproofs",
            "FOCIL Breakout": "focil",
            "L2 Interop Working Group": "l2interop",
            "PQ Interop": "pqinterop",
            "PeerDAS Breakout": "peerdas",
            "Portal Implementers": "portal",
            "Protocol Research": "protocolresearch",
            "RPC Standards": "rpcstandards",
            "RollCall": "rollcall",
            "Stateless Implementers": "stateless",
            "One-time call": "one-off"  # This will be transformed to one-off-{issue_number}
        }

        # Duration mapping (display text -> minutes)
        self.duration_mapping = {
            "30 minutes": 30,
            "60 minutes": 60,
            "90 minutes": 90,
            "120 minutes": 120,
            "180 minutes": 180
        }

    def is_old_format_issue(self, issue_body: str) -> bool:
        """Detects if the issue was created using the old markdown template format."""
        old_format_indicators = [
            r"Call series\s*:\s*",
            r"Recurring meeting\s*:\s*",
            r"Occurrence rate\s*:\s*",
            r"Already on Ethereum Calendar\s*:\s*"
        ]

        for pattern in old_format_indicators:
            if re.search(pattern, issue_body, re.IGNORECASE):
                return True
        return False

    def parse_old_format_data(self, issue_body: str) -> Dict:
        """Parse data from the old markdown template format."""
        print("[DEBUG] Parsing old format issue template")

        # Extract call series
        call_series = self._extract_old_call_series(issue_body)

        # Extract occurrence rate
        occurrence_rate = self._extract_old_occurrence_rate(issue_body)

        # Extract date/time
        start_time = self._extract_old_date_time(issue_body)

        # Extract duration
        duration = self._extract_old_duration(issue_body)

        # Extract boolean flags
        skip_zoom_creation = self._extract_old_zoom_opt_out(issue_body)
        skip_gcal_creation = self._extract_old_already_on_calendar(issue_body)
        need_youtube_streams = self._extract_old_youtube_streams(issue_body)
        display_zoom_link_in_invite = self._extract_old_display_zoom_link(issue_body)

        # Extract other fields
        facilitator_emails = self._extract_old_facilitator_emails(issue_body)
        agenda = self._extract_old_agenda(issue_body)

        return {
            "call_series": call_series,
            "occurrence_rate": occurrence_rate,
            "start_time": start_time,
            "duration": duration,
            "skip_zoom_creation": skip_zoom_creation,
            "skip_gcal_creation": skip_gcal_creation,
            "need_youtube_streams": need_youtube_streams,
            "display_zoom_link_in_invite": display_zoom_link_in_invite,
            "facilitator_emails": facilitator_emails,
            "agenda": agenda
        }

    def _extract_old_call_series(self, issue_body: str) -> Optional[str]:
        """Extract call series from old format."""
        pattern = r"Call series\s*:\s*([^\n]+)"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        if match:
            call_series = match.group(1).strip().lower()
            print(f"[DEBUG] Parsed old format call series: {call_series}")
            return call_series
        return None

    def _extract_old_occurrence_rate(self, issue_body: str) -> str:
        """Extract occurrence rate from old format."""
        occurrence_pattern = r"Occurrence rate\s*:\s*(none|weekly|bi-weekly|monthly)"
        occurrence_match = re.search(occurrence_pattern, issue_body, re.IGNORECASE)
        occurrence_rate = occurrence_match.group(1).lower() if occurrence_match else 'none'
        print(f"[DEBUG] Parsed old format occurrence rate: {occurrence_rate}")
        return occurrence_rate

    def _extract_old_date_time(self, issue_body: str) -> Optional[str]:
        """Extract date/time from old format."""
        # Old format pattern: "UTC Date & Time: [April 24, 2025, 14:00 UTC](https://notime.zone/OWHEr5OFto71X)"
        pattern = r"UTC Date & Time\s*:\s*\[([^\]]+)\]"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        if match:
            date_time_text = match.group(1).strip()
            print(f"[DEBUG] Parsed old format date/time: {date_time_text}")

            # Parse the date/time string using the existing method
            try:
                # Format: "April 24, 2025, 14:00 UTC"
                parsed_time = datetime.strptime(date_time_text, "%B %d, %Y, %H:%M UTC")
                start_time = parsed_time.isoformat() + "Z"
                print(f"[DEBUG] Converted to ISO format: {start_time}")
                return start_time
            except Exception as e:
                print(f"[ERROR] Failed to parse old format date/time '{date_time_text}': {e}")
                return None
        return None

    def _extract_old_duration(self, issue_body: str) -> Optional[int]:
        """Extract duration from old format."""
        # Try "Duration in minutes" first, then fallback to just "Duration"
        patterns = [
            r"Duration\s+in\s+minutes\s*:\s*(\d+)",
            r"Duration\s*:\s*(\d+)\s*minutes?"
        ]

        for pattern in patterns:
            match = re.search(pattern, issue_body, re.IGNORECASE)
            if match:
                duration = int(match.group(1))
                print(f"[DEBUG] Parsed old format duration: {duration} minutes")
                return duration
        return None

    def _extract_old_zoom_opt_out(self, issue_body: str) -> bool:
        """Extract zoom opt-out from old format."""
        pattern = r"Already a Zoom meeting ID\s*:\s*(true|false)"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        skip_zoom = match and match.group(1).lower() == 'true'
        print(f"[DEBUG] Parsed old format skip_zoom_creation: {skip_zoom}")
        return skip_zoom

    def _extract_old_already_on_calendar(self, issue_body: str) -> bool:
        """Extract already on calendar from old format."""
        pattern = r"Already on Ethereum Calendar\s*:\s*(true|false)"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        skip_gcal = match and match.group(1).lower() == 'true'
        print(f"[DEBUG] Parsed old format skip_gcal_creation: {skip_gcal}")
        return skip_gcal

    def _extract_old_youtube_streams(self, issue_body: str) -> bool:
        """Extract YouTube streams need from old format."""
        pattern = r"Need YouTube stream links\s*:\s*(true|false)"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        need_youtube = match and match.group(1).lower() == 'true'
        print(f"[DEBUG] Parsed old format need_youtube_streams: {need_youtube}")
        return need_youtube

    def _extract_old_display_zoom_link(self, issue_body: str) -> bool:
        """Extract display zoom link from old format."""
        pattern = r"display zoom link in invite\s*:\s*(true|false)"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        display_link = match and match.group(1).lower() == 'true'
        print(f"[DEBUG] Parsed old format display_zoom_link_in_invite: {display_link}")
        return display_link

    def _extract_old_facilitator_emails(self, issue_body: str) -> List[str]:
        """Extract facilitator emails from old format."""
        pattern = r"Facilitator emails\s*:\s*([^\n]+)"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        if match:
            emails_text = match.group(1).strip()
            emails = [email.strip() for email in emails_text.split(',') if email.strip()]
            valid_emails = []
            for email in emails:
                # Basic email validation: at least one char + @ + at least one char + . + at least one char
                if re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                    valid_emails.append(email)
                else:
                    print(f"[DEBUG] Filtered out invalid email: {email}")

            print(f"[DEBUG] Parsed old format facilitator_emails: {valid_emails}")
            return valid_emails
        return []



    def _extract_old_agenda(self, issue_body: str) -> Optional[str]:
        """Extract agenda from old format."""
        # Look for agenda section
        pattern = r"Agenda\s*:\s*(.*?)(?=\n\s*\n|\n\s*[A-Z]|$)"
        match = re.search(pattern, issue_body, re.IGNORECASE | re.DOTALL)
        if match:
            agenda = match.group(1).strip()
            print(f"[DEBUG] Parsed old format agenda: {len(agenda)} characters")
            return agenda
        return None

    def is_form_issue(self, issue_body: str) -> bool:
        """Detects if the issue was created using the new GitHub Issue Form."""
        form_indicators = [
            r"### Call Series",
            r"### UTC Date & Time",
            r"### Duration",
            r"### Occurrence Rate"
        ]

        for pattern in form_indicators:
            if re.search(pattern, issue_body):
                return True
        return False

    def parse_call_series(self, issue_body: str, issue_number: Optional[int] = None) -> Optional[str]:
        """Extract and convert call series from form dropdown."""
        # Try with extra newline (real GitHub Issue Form format)
        pattern = r"### Call Series\n\n([^\n]+)"
        match = re.search(pattern, issue_body)
        if not match:
            # Try without extra newline (test data format)
            pattern = r"### Call Series\n([^\n]+)"
            match = re.search(pattern, issue_body)

        if match:
            display_name = match.group(1).strip()
            call_series_key = self.call_series_mapping.get(display_name)
            if call_series_key:
                # For one-off calls, generate the unique key with issue number
                if call_series_key == "one-off" and issue_number is not None:
                    call_series_key = f"one-off-{issue_number}"
                    print(f"[DEBUG] Parsed call series: '{display_name}' -> '{call_series_key}' (one-off with issue #{issue_number})")
                else:
                    print(f"[DEBUG] Parsed call series: '{display_name}' -> '{call_series_key}'")
                return call_series_key
            else:
                print(f"[WARNING] Unknown call series display name: '{display_name}'")
        return None

    def parse_duration(self, issue_body: str) -> Optional[int]:
        """Extract duration from form dropdown and convert to minutes."""
        # Try with extra newline (real GitHub Issue Form format)
        pattern = r"### Duration\n\n([^\n]+)"
        match = re.search(pattern, issue_body)
        if not match:
            # Try without extra newline (test data format)
            pattern = r"### Duration\n([^\n]+)"
            match = re.search(pattern, issue_body)

        if match:
            duration_text = match.group(1).strip()
            duration = self.duration_mapping.get(duration_text)
            if duration:
                print(f"[DEBUG] Parsed duration: {duration} minutes")
                return duration
            else:
                print(f"[WARNING] Unknown duration: '{duration_text}'")
                return 0  # Convert invalid durations to 0

        return None

    def parse_occurrence_rate(self, issue_body: str, call_series: Optional[str] = None) -> Optional[str]:
        """Extract occurrence rate from form dropdown."""
        # Try with extra newline (real GitHub Issue Form format)
        pattern = r"### Occurrence Rate\n\n([^\n]+)"
        match = re.search(pattern, issue_body)
        if not match:
            # Try without extra newline (test data format)
            pattern = r"### Occurrence Rate\n([^\n]+)"
            match = re.search(pattern, issue_body)

        if match:
            rate = match.group(1).strip().lower()
            print(f"[DEBUG] Parsed occurrence rate: {rate}")
            return rate

        # For one-off calls, ensure occurrence_rate is set to "one-time"
        if call_series and call_series.startswith("one-off-"):
            print(f"[DEBUG] Setting occurrence_rate to 'one-time' for one-off call: {call_series}")
            return "one-time"

        return None

    def parse_date_time(self, issue_body: str) -> Optional[str]:
        """Extract date/time from form input."""
        # Try with extra newline (real GitHub Issue Form format)
        pattern = r"### UTC Date & Time\n\n([^\n]+)"
        match = re.search(pattern, issue_body)
        if not match:
            # Try without extra newline (test data format)
            pattern = r"### UTC Date & Time\n([^\n]+)"
            match = re.search(pattern, issue_body)

        if match:
            date_time_text = match.group(1).strip()
            print(f"[DEBUG] Parsed date/time: {date_time_text}")
            return date_time_text
        return None

    def parse_checkbox_field(self, issue_body: str, field_name: str) -> bool:
        """Parse checkbox fields from form."""
        # Try with extra newline (real GitHub Issue Form format)
        pattern = rf"### {field_name}\n\n- \[([ x])\]"
        match = re.search(pattern, issue_body)
        if not match:
            # Try without extra newline (test data format)
            pattern = rf"### {field_name}\n- \[([ x])\]"
            match = re.search(pattern, issue_body)

        if match:
            is_checked = match.group(1) == 'x'
            print(f"[DEBUG] Parsed {field_name}: {is_checked}")
            return is_checked
        return False

    def parse_text_field(self, issue_body: str, field_name: str) -> Optional[str]:
        """Parse text input fields from form."""
        # Try with extra newline (real GitHub Issue Form format)
        pattern = rf"### {field_name}\n\n([^\n]+)"
        match = re.search(pattern, issue_body)
        if not match:
            # Try without extra newline (test data format)
            pattern = rf"### {field_name}\n([^\n]+)"
            match = re.search(pattern, issue_body)

        if match:
            value = match.group(1).strip()
            if value and value != "" and value != "_No response_":
                print(f"[DEBUG] Parsed {field_name}: {value}")
                return value
        return None

    def parse_textarea_field(self, issue_body: str, field_name: str) -> Optional[str]:
        """Parse textarea fields from form."""
        # Try with extra newline (real GitHub Issue Form format)
        pattern = rf"### {field_name}\n\n([\s\S]*?)(?=\n### |$)"
        match = re.search(pattern, issue_body)
        if not match:
            # Try without extra newline (test data format)
            pattern = rf"### {field_name}\n([\s\S]*?)(?=\n### |$)"
            match = re.search(pattern, issue_body)

        if match:
            value = match.group(1).strip()
            if value and value != "" and value != "_No response_":
                print(f"[DEBUG] Parsed {field_name}: {value[:50]}...")
                return value
        return None

    def parse_facilitator_emails(self, issue_body: str) -> List[str]:
        """Extract facilitator emails from form input."""
        emails_text = self.parse_text_field(issue_body, "Facilitator Emails \\(Optional\\)")
        if emails_text:
            emails = [email.strip() for email in emails_text.split(',') if email.strip()]
            print(f"[DEBUG] Parsed facilitator emails: {emails}")
            return emails
        return []



    def parse_agenda(self, issue_body: str) -> Optional[str]:
        """Extract agenda from form textarea."""
        # Extract everything between ### Agenda and ### Call Series
        pattern = r"### Agenda\n\n([\s\S]*?)(?=\n### Call Series)"
        match = re.search(pattern, issue_body)
        if not match:
            # Try without extra newline (test data format)
            pattern = r"### Agenda\n([\s\S]*?)(?=\n### Call Series)"
            match = re.search(pattern, issue_body)

        if match:
            agenda = match.group(1).strip()
            if agenda and agenda != "_No response_":
                print(f"[DEBUG] Extracted agenda: {len(agenda)} characters")
                return agenda
        return None

    def parse_zoom_opt_out(self, issue_body: str) -> bool:
        """Parse zoom meeting opt-out checkbox."""
        return self.parse_checkbox_field(issue_body, "Use Custom Meeting Link \\(Optional\\)")

    def parse_youtube_streams(self, issue_body: str) -> bool:
        """Parse YouTube livestream checkbox."""
        return self.parse_checkbox_field(issue_body, "YouTube Livestream Link \\(Optional\\)")

    def parse_display_zoom_link(self, issue_body: str) -> bool:
        """Parse display zoom link checkbox."""
        return self.parse_checkbox_field(issue_body, "Display Zoom Link in Calendar Invite \\(Optional\\)")

    def parse_date_time_with_duration(self, date_time_text: str, duration_minutes: int) -> Tuple[Optional[str], Optional[int]]:
        """Parse date/time string and return start_time and duration."""
        try:
            # First try to extract from markdown link format
            # Format: [April 24, 2025, 14:00 UTC](https://notime.zone/OWHEr5OFto71X)
            match = re.search(r'\[([^\]]+)\]', date_time_text)
            if match:
                date_time_str = match.group(1)
                print(f"[DEBUG] Extracted date/time from markdown link: {date_time_str}")
            else:
                # If no markdown link, try to parse the text directly
                # Format: "April 24, 2025, 14:00 UTC"
                date_time_str = date_time_text.strip()
                print(f"[DEBUG] Using date/time directly from form: {date_time_str}")

            # Strategy 1: Try standard format first
            # Format: "Month Day, Year, HH:MM UTC"
            try:
                parsed_time = datetime.strptime(date_time_str, "%B %d, %Y, %H:%M UTC")
                start_time = parsed_time.isoformat() + "Z"
                print(f"[DEBUG] Parsed with standard format: {start_time}")
                return start_time, duration_minutes
            except ValueError:
                pass

            # Strategy 2: Try with ordinal dates (1st, 2nd, 3rd, etc.)
            # Users might write "24th April 2025, 14:00 UTC"
            try:
                # Remove ordinal suffixes
                ordinal_pattern = r'(\d+)(st|nd|rd|th)'
                normalized_str = re.sub(ordinal_pattern, r'\1', date_time_str)
                # Try day-first format for ordinal dates
                parsed_time = datetime.strptime(normalized_str, "%d %B %Y, %H:%M UTC")
                start_time = parsed_time.isoformat() + "Z"
                print(f"[DEBUG] Parsed with ordinal normalization: {start_time}")
                return start_time, duration_minutes
            except ValueError:
                pass

            # Strategy 3: Try without comma before year
            # Users might write "April 24 2025, 14:00 UTC"
            try:
                parsed_time = datetime.strptime(date_time_str, "%B %d %Y, %H:%M UTC")
                start_time = parsed_time.isoformat() + "Z"
                print(f"[DEBUG] Parsed without comma before year: {start_time}")
                return start_time, duration_minutes
            except ValueError:
                pass

            # Strategy 4: Try abbreviated month names
            # Users might write "Aug 24, 2026, 14:00 UTC"
            try:
                parsed_time = datetime.strptime(date_time_str, "%b %d, %Y, %H:%M UTC")
                start_time = parsed_time.isoformat() + "Z"
                print(f"[DEBUG] Parsed with abbreviated month: {start_time}")
                return start_time, duration_minutes
            except ValueError:
                pass

            # Strategy 5: Try abbreviated month names without comma before year
            # Users might write "Aug 24 2025, 14:00 UTC"
            try:
                parsed_time = datetime.strptime(date_time_str, "%b %d %Y, %H:%M UTC")
                start_time = parsed_time.isoformat() + "Z"
                print(f"[DEBUG] Parsed with abbreviated month (no comma): {start_time}")
                return start_time, duration_minutes
            except ValueError:
                pass

            # If all strategies fail, return the extracted date string as fallback (not the original markdown)
            print(f"[WARN] Could not parse date/time '{date_time_str}', using extracted text as fallback")
            return date_time_str, duration_minutes

        except Exception as e:
            print(f"[ERROR] Error parsing date/time '{date_time_text}': {e}")
            return date_time_text, duration_minutes

    def should_be_on_ethereum_calendar(self, call_series: str) -> bool:
        """Determine if a call series should be on the Ethereum calendar."""
        # One-time calls should NOT already be on the Ethereum calendar
        # All other call series are expected to be on the calendar
        return not (call_series.startswith("one-off-") or call_series == "one-off")

    def parse_form_data(self, issue_body: str, issue_number: Optional[int] = None) -> Dict:
        """Parse all form data and return structured dictionary."""
        # Check if it's the old format first
        if self.is_old_format_issue(issue_body):
            print("[DEBUG] Detected old format issue template")
            return self.parse_old_format_data(issue_body)

        # Check if it's the new format
        if self.is_form_issue(issue_body):
            print("[DEBUG] Detected new format issue template")
            return self._parse_new_format_data(issue_body, issue_number)

        # If neither format is detected
        raise ValueError("Issue body does not appear to be from either the new form format or old template format")

    def _parse_new_format_data(self, issue_body: str, issue_number: Optional[int] = None) -> Dict:
        """Parse new form format data."""
        # Parse basic fields
        call_series = self.parse_call_series(issue_body, issue_number)
        duration = self.parse_duration(issue_body)
        occurrence_rate = self.parse_occurrence_rate(issue_body, call_series)
        date_time_text = self.parse_date_time(issue_body)

        # Parse options
        skip_zoom_creation = self.parse_zoom_opt_out(issue_body)
        need_youtube_streams = self.parse_youtube_streams(issue_body)
        display_zoom_link_in_invite = self.parse_display_zoom_link(issue_body)

        # Parse additional fields
        facilitator_emails = self.parse_facilitator_emails(issue_body)
        agenda = self.parse_agenda(issue_body)

        # Parse date/time with duration
        start_time, parsed_duration = None, None
        if date_time_text and duration:
            start_time, parsed_duration = self.parse_date_time_with_duration(date_time_text, duration)

        # Determine derived fields
        skip_gcal_creation = not self.should_be_on_ethereum_calendar(call_series) if call_series else True

        return {
            "call_series": call_series,
            "duration": parsed_duration or duration,
            "occurrence_rate": occurrence_rate,
            "start_time": start_time,
            "skip_zoom_creation": skip_zoom_creation,
            "skip_gcal_creation": skip_gcal_creation,
            "need_youtube_streams": need_youtube_streams,
            "display_zoom_link_in_invite": display_zoom_link_in_invite,
            "facilitator_emails": facilitator_emails,
            "agenda": agenda,
            "date_time_text": date_time_text
        }