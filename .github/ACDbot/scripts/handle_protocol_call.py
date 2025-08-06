#!/usr/bin/env python3
"""
Protocol Call Handler

Clean, focused implementation for handling protocol calls using the new form-based workflow.
This is a fresh implementation designed specifically for the new data model.
"""

import sys
import os
import argparse
from typing import Dict, Optional, List, Set
from datetime import datetime

# Add the modules directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))

from modules.form_parser import FormParser
from modules.mapping_manager import MappingManager


class ProtocolCallHandler:
    """Main handler for protocol calls using the new form-based workflow."""

    def __init__(self):
        self.form_parser = FormParser()
        self.mapping_manager = MappingManager()

    def _handle_zoom_resource(self, call_data: Dict, existing_resources: Dict) -> Dict:
        """Handle Zoom meeting creation/updates."""
        result = {
            "zoom_created": False,
            "zoom_id": None,
            "zoom_url": None
        }

        try:
            # Skip if user opted out
            if call_data.get("skip_zoom_creation"):
                print(f"[DEBUG] Zoom creation skipped (user opted out)")
                return result

            # Check if we have an existing Zoom meeting
            has_existing = existing_resources.get("has_zoom", False)

            if has_existing:
                print(f"[DEBUG] Updating existing Zoom meeting")
                result = self._update_zoom_meeting(call_data, existing_resources)
            else:
                print(f"[DEBUG] Creating new Zoom meeting")
                result = self._create_zoom_meeting(call_data)

            return result

        except Exception as e:
            print(f"[ERROR] Failed to handle Zoom resource: {e}")
            return result

    def _handle_calendar_resource(self, call_data: Dict, existing_resources: Dict) -> Dict:
        """Handle Google Calendar event creation/updates."""
        result = {
            "calendar_created": False,
            "calendar_event_id": None,
            "calendar_event_url": None
        }

        try:
            # Skip if not on Ethereum calendar
            if call_data.get("skip_gcal_creation"):
                print(f"[DEBUG] Calendar creation skipped (not on Ethereum calendar)")
                return result

            # Check if we have an existing calendar event
            has_existing = existing_resources.get("has_calendar", False)

            if has_existing:
                print(f"[DEBUG] Updating existing calendar event")
                result = self._update_calendar_event(call_data, existing_resources)
            else:
                print(f"[DEBUG] Creating new calendar event")
                result = self._create_calendar_event(call_data)

            return result

        except Exception as e:
            print(f"[ERROR] Failed to handle Calendar resource: {e}")
            return result

    def _handle_discourse_resource(self, call_data: Dict, existing_resources: Dict) -> Dict:
        """Handle Discourse topic creation/updates."""
        result = {
            "discourse_created": False,
            "discourse_topic_id": None,
            "discourse_url": None
        }

        try:
            # Check if we have an existing discourse topic
            has_existing = existing_resources.get("has_discourse", False)

            if has_existing:
                print(f"[DEBUG] Discourse topic already exists, skipping creation")
                # Use existing Discourse data
                existing_occurrence = existing_resources["existing_occurrence"]["occurrence"]
                result = {
                    "discourse_created": True,
                    "discourse_topic_id": existing_occurrence["discourse_topic_id"],
                    "discourse_url": f"https://ethereum-magicians.org/t/{existing_occurrence['discourse_topic_id']}",
                    "discourse_action": "existing"
                }
            else:
                print(f"[DEBUG] Creating new discourse topic")
                result = self._create_discourse_topic(call_data)

            return result

        except Exception as e:
            print(f"[ERROR] Failed to handle Discourse resource: {e}")
            return result

    def _handle_youtube_resource(self, call_data: Dict, existing_resources: Dict) -> Dict:
        """Handle YouTube streams creation/updates."""
        result = {
            "youtube_streams_created": False,
            "youtube_streams": None,
            "stream_links": []
        }

        try:
            # Check if we have existing YouTube streams
            has_existing = existing_resources.get("has_youtube", False)

            if has_existing:
                print(f"[DEBUG] YouTube streams already exist, using existing")
                # Use existing YouTube streams
                existing_occurrence = existing_resources["existing_occurrence"]["occurrence"]
                youtube_streams = existing_occurrence.get("youtube_streams", [])
                if youtube_streams:
                    stream_links = [f"- Stream {i+1}: {stream['stream_url']}"
                                  for i, stream in enumerate(youtube_streams)]
                else:
                    stream_links = []

                result = {
                    "youtube_streams_created": True,
                    "youtube_streams": youtube_streams,
                    "stream_links": stream_links,
                    "youtube_action": "existing"
                }
            else:
                print(f"[DEBUG] Creating new YouTube streams")
                result = self._create_youtube_streams(call_data)

            return result

        except Exception as e:
            print(f"[ERROR] Failed to handle YouTube resource: {e}")
            return result

    def handle_protocol_call(self, issue_number: int, repo_name: str) -> bool:
        """Main entry point for handling a protocol call issue."""
        try:
            print(f"[INFO] Starting protocol call handler for issue #{issue_number}")

            # 1. Get GitHub issue
            issue = self._get_github_issue(issue_number, repo_name)
            if not issue:
                print(f"[ERROR] Failed to get GitHub issue #{issue_number}")
                return False

            # 2. Parse form data
            form_data = self._parse_form_data(issue.body, issue_number)
            if not form_data:
                print(f"[ERROR] Failed to parse form data from issue #{issue_number}")
                return False

            # 3. Validate and transform data
            call_data = self._validate_and_transform(form_data, issue)
            if not call_data:
                print(f"[ERROR] Failed to validate/transform data for issue #{issue_number}")
                return False

            # 4. Check for existing occurrence and resources
            existing_occurrence = self.mapping_manager.find_occurrence(issue_number)
            is_update = existing_occurrence is not None

            # 5. Check existing resources
            existing_resources = self._check_existing_resources(call_data)

            # 6. Handle each resource type individually
            resource_results = {
                "zoom_created": False,
                "zoom_id": None,
                "zoom_url": None,
                "calendar_created": False,
                "calendar_event_id": None,
                "calendar_event_url": None,
                "discourse_created": False,
                "discourse_topic_id": None,
                "discourse_url": None,
                "youtube_streams_created": False,
                "youtube_streams": None,
                "stream_links": []
            }

            # Track if any critical operations failed
            critical_failures = []

            # Handle each resource type
            zoom_result = self._handle_zoom_resource(call_data, existing_resources)
            resource_results.update(zoom_result)
            if not call_data.get("skip_zoom_creation") and not zoom_result.get("zoom_created"):
                critical_failures.append("Zoom meeting creation failed")

            # Store zoom URL for use by other resources
            if zoom_result.get("zoom_url"):
                self._last_zoom_url = zoom_result["zoom_url"]

            calendar_result = self._handle_calendar_resource(call_data, existing_resources)
            resource_results.update(calendar_result)
            if not call_data.get("skip_gcal_creation") and not calendar_result.get("calendar_created"):
                critical_failures.append("Calendar event creation failed")

            discourse_result = self._handle_discourse_resource(call_data, existing_resources)
            resource_results.update(discourse_result)
            if not discourse_result.get("discourse_created"):
                critical_failures.append("Discourse topic creation failed")

            youtube_result = self._handle_youtube_resource(call_data, existing_resources)
            resource_results.update(youtube_result)
            if call_data.get("need_youtube_streams") and not youtube_result.get("youtube_streams_created"):
                critical_failures.append("YouTube streams creation failed")

            # 7. Update mapping only if no critical failures occurred
            if critical_failures:
                print(f"[ERROR] Critical failures occurred: {', '.join(critical_failures)}")
                print(f"[ERROR] Skipping mapping update to maintain consistency")
                # Still proceed with notifications and GitHub posting, but don't update mapping
            else:
                success = self._update_mapping(call_data, issue, is_update)
                if not success:
                    print(f"[ERROR] Failed to update mapping for issue #{issue_number}")
                    return False

                self._update_mapping_with_resources(call_data, resource_results)

            # 8. Send Telegram notification
            self._send_telegram_notification(call_data, issue, resource_results, is_update)

            # 9. Post results to GitHub only if resources were successfully created
            if self._resources_changed(resource_results):
                self._post_results(call_data, issue, resource_results, is_update)
            else:
                print(f"[DEBUG] No resources successfully created, skipping GitHub comment to avoid email spam")

            # 10. Save mapping
            self.mapping_manager.save_mapping()

            print(f"[INFO] Successfully processed protocol call for issue #{issue_number}")
            return True

        except Exception as e:
            print(f"[ERROR] Unexpected error in protocol call handler: {e}")
            return False

    def _get_github_issue(self, issue_number: int, repo_name: str):
        """Get GitHub issue using the existing GitHub integration."""
        try:
            # Import here to avoid circular imports
            from github import Github

            # Get GitHub token from environment
            github_token = os.getenv('GITHUB_TOKEN')
            if not github_token:
                print("[ERROR] GITHUB_TOKEN environment variable not set")
                return None

            # Initialize GitHub client
            g = Github(github_token)
            repo = g.get_repo(repo_name)
            issue = repo.get_issue(issue_number)

            print(f"[DEBUG] Retrieved GitHub issue: {issue.title}")
            return issue

        except Exception as e:
            print(f"[ERROR] Failed to get GitHub issue: {e}")
            return None

    def _parse_form_data(self, issue_body: str, issue_number: int) -> Optional[Dict]:
        """Parse form data from issue body."""
        try:
            print(f"[DEBUG] Raw issue body:\n{issue_body}")
            form_data = self.form_parser.parse_form_data(issue_body, issue_number)
            print(f"[DEBUG] Successfully parsed form data: {form_data}")
            return form_data

        except Exception as e:
            print(f"[ERROR] Failed to parse form data: {e}")
            return None

    def _validate_and_transform(self, form_data: Dict, issue) -> Optional[Dict]:
        """Validate and transform form data into call data."""
        try:
            # Validate required fields
            required_fields = ["call_series", "duration", "start_time"]
            for field in required_fields:
                if not form_data.get(field):
                    print(f"[ERROR] Missing required field: {field}")
                    return None

            # Create call data structure
            call_data = {
                "issue_number": issue.number,
                "issue_title": issue.title,
                "issue_url": issue.html_url,
                "call_series": form_data["call_series"],
                "duration": form_data["duration"],
                "start_time": form_data["start_time"],
                "occurrence_rate": form_data.get("occurrence_rate", "other"),
                "skip_zoom_creation": form_data["skip_zoom_creation"],
                "skip_gcal_creation": form_data["skip_gcal_creation"],
                "need_youtube_streams": form_data["need_youtube_streams"],
                "display_zoom_link_in_invite": form_data["display_zoom_link_in_invite"],
                "facilitator_emails": form_data["facilitator_emails"],
                "agenda": form_data.get("agenda")
            }

            print(f"[DEBUG] Validated and transformed call data: {call_data}")
            return call_data

        except Exception as e:
            print(f"[ERROR] Failed to validate/transform data: {e}")
            return None

    def _check_existing_resources(self, call_data: Dict) -> Dict:
        """Check if resources already exist for this occurrence."""
        try:
            call_series_entry = self.mapping_manager.find_occurrence(call_data["issue_number"])
            if not call_series_entry:
                return {
                    "has_zoom": False,
                    "has_calendar": False,
                    "has_discourse": False,
                    "has_youtube": False
                }

            occurrence = call_series_entry["occurrence"]

            # Check for existing resources
            series_meeting_id = self.mapping_manager.get_series_meeting_id(call_data["call_series"])
            has_zoom = bool(series_meeting_id and not str(series_meeting_id).startswith("placeholder"))

            # Calendar event ID is stored at the parent level (call series level)
            call_series = call_series_entry.get("call_series")
            calendar_event_id = self.mapping_manager.get_series_calendar_event_id(call_series) if call_series else None
            has_calendar = bool(calendar_event_id)
            has_discourse = (occurrence.get("discourse_topic_id") and
                           not str(occurrence.get("discourse_topic_id")).startswith("placeholder"))
            has_youtube = bool(occurrence.get("youtube_streams"))

            print(f"[DEBUG] Existing resources for issue #{call_data['issue_number']}:")
            print(f"  - Zoom: {has_zoom} (ID: {occurrence.get('meeting_id')})")
            print(f"  - Calendar: {has_calendar} (ID: {calendar_event_id})")
            print(f"  - Discourse: {has_discourse} (ID: {occurrence.get('discourse_topic_id')})")
            print(f"  - YouTube: {has_youtube} (streams: {len(occurrence.get('youtube_streams', []))})")
            print(f"[DEBUG] Full occurrence data: {occurrence}")
            print(f"[DEBUG] Full call_series_entry data: {call_series_entry}")

            return {
                "has_zoom": has_zoom,
                "has_calendar": has_calendar,
                "has_discourse": has_discourse,
                "has_youtube": has_youtube,
                "existing_occurrence": call_series_entry
            }

        except Exception as e:
            print(f"[ERROR] Failed to check existing resources: {e}")
            return {
                "has_zoom": False,
                "has_calendar": False,
                "has_discourse": False,
                "has_youtube": False
            }

    def _update_mapping_with_resources(self, call_data: Dict, resource_results: Dict) -> bool:
        """Update the mapping with resource IDs after they're created."""
        try:
            # Get the existing occurrence to update
            existing_occurrence = self.mapping_manager.find_occurrence(call_data["issue_number"])
            if not existing_occurrence:
                print(f"[ERROR] Could not find occurrence for issue #{call_data['issue_number']} to update with resource IDs")
                return False

            call_series = existing_occurrence["call_series"]
            issue_number = call_data["issue_number"]

            # Prepare update data with resource IDs
            update_data = {}

            # Add Zoom meeting ID if created
            if resource_results.get("zoom_created") and resource_results.get("zoom_id"):
                if not str(resource_results["zoom_id"]).startswith("placeholder"):
                    self.mapping_manager.set_series_meeting_id(call_data["call_series"], resource_results["zoom_id"])
                    print(f"[DEBUG] Set series meeting ID: {resource_results['zoom_id']}")

            # Add Calendar event ID if created (stored at call series level)
            if resource_results.get("calendar_created") and resource_results.get("calendar_event_id"):
                # Use the mapping manager's method to set calendar event ID at call series level
                self.mapping_manager.set_series_calendar_event_id(call_series, resource_results["calendar_event_id"])
                print(f"[DEBUG] Added Calendar event ID at call series level: {resource_results['calendar_event_id']}")

            # Add Discourse topic ID if created
            if resource_results.get("discourse_created") and resource_results.get("discourse_topic_id"):
                if not str(resource_results["discourse_topic_id"]).startswith("placeholder"):
                    update_data["discourse_topic_id"] = resource_results["discourse_topic_id"]
                    print(f"[DEBUG] Adding Discourse topic ID: {resource_results['discourse_topic_id']}")

            # Add YouTube streams if created
            if resource_results.get("youtube_streams_created") and resource_results.get("youtube_streams"):
                update_data["youtube_streams"] = resource_results["youtube_streams"]
                print(f"[DEBUG] Adding YouTube streams: {len(resource_results['youtube_streams'])} streams")

            # Update the occurrence with resource IDs
            if update_data:
                success = self.mapping_manager.update_occurrence(
                    call_series,
                    issue_number,
                    update_data
                )
                if success:
                    print(f"[DEBUG] Successfully updated mapping with resource IDs for issue #{issue_number}")
                    return True
                else:
                    print(f"[ERROR] Failed to update mapping with resource IDs for issue #{issue_number}")
                    return False
            else:
                print(f"[DEBUG] No resource IDs to update for issue #{issue_number}")
                return True

        except Exception as e:
            print(f"[ERROR] Failed to update mapping with resource IDs: {e}")
            return False

    def _update_mapping(self, call_data: Dict, issue, is_update: bool) -> bool:
        """Update the mapping with call data."""
        try:
            # Create occurrence data
            occurrence_data = self.mapping_manager.create_occurrence_data(
                issue_number=call_data["issue_number"],
                issue_title=call_data["issue_title"],
                discourse_topic_id=None,  # Will be set later if Discourse is created
                start_time=call_data["start_time"],
                duration=call_data["duration"],
                skip_youtube_upload=call_data["skip_zoom_creation"],
                skip_transcript_processing=call_data["skip_zoom_creation"]
            )

            if is_update:
                # Update existing occurrence
                success = self.mapping_manager.update_occurrence(
                    call_data["call_series"],
                    call_data["issue_number"],
                    occurrence_data
                )
            else:
                # Add new occurrence
                success = self.mapping_manager.add_occurrence(
                    call_data["call_series"],
                    occurrence_data
                )

            if success:
                print(f"[DEBUG] Successfully {'updated' if is_update else 'added'} occurrence in mapping")
                return True
            else:
                print(f"[ERROR] Failed to {'update' if is_update else 'add'} occurrence in mapping")
                return False

        except Exception as e:
            print(f"[ERROR] Failed to update mapping: {e}")
            return False

    def _create_zoom_meeting(self, call_data: Dict) -> Dict:
        """Create or update Zoom meeting."""
        try:
            # Import existing zoom module
            from modules import zoom

            # Extract parameters from call_data
            topic = call_data["issue_title"]
            start_time = call_data["start_time"]
            duration = call_data["duration"]
            occurrence_rate = call_data.get("occurrence_rate", "other")
            call_series = call_data.get("call_series", "unknown")
            is_recurring = not call_series.startswith("one-off-")

            print(f"[DEBUG] Creating/updating Zoom meeting: {topic}")
            print(f"[DEBUG] Start time: {start_time}, Duration: {duration} minutes")
            print(f"[DEBUG] Recurring: {is_recurring}, Rate: {occurrence_rate}")

            # Check if we have an existing meeting ID to reuse
            existing_meeting_id = None
            if is_recurring:
                # For recurring calls, check if we have a series meeting ID
                existing_meeting_id = self.mapping_manager.get_series_meeting_id(call_series)
                if existing_meeting_id:
                    print(f"[DEBUG] Found existing series meeting ID: {existing_meeting_id}")
                else:
                    print(f"[DEBUG] No existing series meeting ID found for {call_series}")

            if existing_meeting_id:
                # Update existing meeting
                print(f"[DEBUG] Updating existing meeting with ID: {existing_meeting_id}")
                update_result = zoom.update_meeting(existing_meeting_id, topic, start_time, duration)
                join_url = update_result.get("join_url", "https://zoom.us (updated meeting)")
                zoom_id = existing_meeting_id
                print(f"[DEBUG] Updated existing Zoom meeting with ID: {zoom_id}")
            else:
                # Create new meeting based on type
                print(f"[DEBUG] Creating new meeting...")
                if is_recurring and occurrence_rate != "none":
                    # Create recurring meeting
                    join_url, zoom_id = zoom.create_recurring_meeting(
                        topic=topic,
                        start_time=start_time,
                        duration=duration,
                        occurrence_rate=occurrence_rate
                    )
                    print(f"[DEBUG] Created recurring Zoom meeting with ID: {zoom_id}")
                else:
                    # Create one-time meeting
                    join_url, zoom_id = zoom.create_meeting(
                        topic=topic,
                        start_time=start_time,
                        duration=duration
                    )
                    print(f"[DEBUG] Created one-time Zoom meeting with ID: {zoom_id}")

            # Always fetch current join URL from API (as per old system)
            if zoom_id and not str(zoom_id).startswith("placeholder-"):
                try:
                    meeting_details = zoom.get_meeting(zoom_id)
                    if meeting_details and meeting_details.get('join_url'):
                        join_url = meeting_details['join_url']
                        print(f"[DEBUG] Successfully fetched join_url: {join_url}")
                    else:
                        join_url = "Error fetching Zoom link (API returned incomplete data)"
                        print(f"[WARN] {join_url}")
                except Exception as e:
                    join_url = f"Error fetching Zoom link ({type(e).__name__})"
                    print(f"[WARN] {join_url}: {str(e)}")

            return {
                "zoom_created": True,
                "zoom_id": zoom_id,
                "zoom_url": join_url,
                "zoom_action": "created"
            }

        except Exception as e:
            print(f"[ERROR] Failed to create Zoom meeting: {e}")
            # Return placeholder values on error (as per old system)
            return {
                "zoom_created": False,
                "zoom_id": f"placeholder-{call_data['issue_number']}",
                "zoom_url": "https://zoom.us (API authentication failed)"
            }

    def _update_zoom_meeting(self, call_data: Dict, existing_resources: Dict) -> Dict:
        """Update existing Zoom meeting."""
        try:
            existing_meeting_id = self.mapping_manager.get_series_meeting_id(call_data["call_series"])
            result = {
                "zoom_created": True,
                "zoom_id": existing_meeting_id,
                "zoom_url": "https://zoom.us (existing meeting)",
                "zoom_action": "updated"
            }

            # Update the meeting if we have changes
            if existing_meeting_id:
                from modules import zoom
                update_result = zoom.update_meeting(
                    existing_meeting_id,
                    call_data["issue_title"],
                    call_data["start_time"],
                    call_data["duration"]
                )
                if update_result.get("join_url"):
                    result["zoom_url"] = update_result["join_url"]

            return result

        except Exception as e:
            print(f"[ERROR] Failed to update Zoom meeting: {e}")
            return {
                "zoom_created": False,
                "zoom_id": None,
                "zoom_url": None
            }

    def _create_calendar_event(self, call_data: Dict) -> Dict:
        """Create new Google Calendar event."""
        try:
            # Pass zoom URL to calendar creation if available
            calendar_call_data = call_data.copy()
            if hasattr(self, '_last_zoom_url'):
                calendar_call_data["zoom_url"] = self._last_zoom_url

            calendar_result = self._create_or_update_calendar_event(calendar_call_data)
            return calendar_result

        except Exception as e:
            print(f"[ERROR] Failed to create calendar event: {e}")
            return {
                "calendar_created": False,
                "calendar_event_id": None,
                "calendar_event_url": None
            }

    def _create_or_update_calendar_event(self, call_data: Dict, existing_event_id: Optional[str] = None) -> Dict:
        """Create or update Google Calendar event."""
        try:
            # Import existing gcal module
            from modules import gcal

            # Extract parameters from call_data
            start_dt = call_data["start_time"]
            duration_minutes = call_data["duration"]
            occurrence_rate = call_data.get("occurrence_rate", "other")
            call_series = call_data.get("call_series", "unknown")
            is_recurring = not call_series.startswith("one-off-")

            # Determine calendar event title
            if call_series.startswith("one-off-"):
                # For one-off calls, use the issue title
                summary = call_data["issue_title"]
            else:
                # For series calls, use the human-friendly call series name
                summary = self._get_call_series_display_name(call_data["call_series"])

            # Get calendar ID from environment (same as old system)
            calendar_id = os.getenv("GOOGLE_CALENDAR_ID", "primary")

            # Build description with links first, then truncated agenda
            description_parts = []

            # Add meeting link to description if requested and available
            if call_data.get("display_zoom_link_in_invite") and call_data.get("zoom_url"):
                description_parts.append(f"Meeting: {call_data['zoom_url']}")

            # Add GitHub issue link
            description_parts.append(f"Issue: {call_data['issue_url']}")

            # Add truncated agenda if provided
            if call_data.get("agenda"):
                agenda_lines = call_data['agenda'].strip().split('\n')
                # Limit to 7 lines (including "Agenda:" header)
                if len(agenda_lines) > 6:
                    truncated_agenda = '\n'.join(agenda_lines[:6])
                    truncated_agenda += '\n\n[Agenda truncated - see GitHub issue for full details]'
                    description_parts.append(f"Agenda:\n{truncated_agenda}")
                else:
                    description_parts.append(f"Agenda:\n{call_data['agenda']}")

            description = "\n\n".join(description_parts)

            print(f"[DEBUG] {'Updating' if existing_event_id else 'Creating'} calendar event: {summary}")
            print(f"[DEBUG] Start time: {start_dt}, Duration: {duration_minutes} minutes")
            print(f"[DEBUG] Recurring: {is_recurring}, Rate: {occurrence_rate}")
            print(f"[DEBUG] Calendar ID: {calendar_id}")
            if existing_event_id:
                print(f"[DEBUG] Existing event ID: {existing_event_id}")

            # Check if we should update an existing event
            if existing_event_id:
                try:
                    if is_recurring and occurrence_rate != "none":
                        # Update recurring event
                        event_result = gcal.update_recurring_event(
                            event_id=existing_event_id,
                            summary=summary,
                            start_dt=start_dt,
                            duration_minutes=duration_minutes,
                            calendar_id=calendar_id,
                            occurrence_rate=occurrence_rate,
                            description=description
                        )
                        print(f"[DEBUG] Updated recurring calendar event with ID: {event_result.get('id')}")
                    else:
                        # Update one-time event
                        event_result = gcal.update_event(
                            event_id=existing_event_id,
                            summary=summary,
                            start_dt=start_dt,
                            duration_minutes=duration_minutes,
                            calendar_id=calendar_id,
                            description=description
                        )
                        print(f"[DEBUG] Updated one-time calendar event with ID: {event_result.get('id')}")

                    return {
                        "calendar_created": True,
                        "calendar_event_id": event_result.get('id'),
                        "calendar_event_url": event_result.get('htmlLink'),
                        "calendar_action": "updated"
                    }

                except ValueError as e:
                    # Event not found, create a new one
                    print(f"[DEBUG] Existing event not found, creating new one: {e}")
                    existing_event_id = None
                except Exception as e:
                    # Other error, create a new one
                    print(f"[DEBUG] Failed to update existing event, creating new one: {e}")
                    existing_event_id = None

            # Create new event (either no existing ID or update failed)
            if is_recurring and occurrence_rate != "none":
                # Create recurring event
                event_result = gcal.create_recurring_event(
                    summary=summary,
                    start_dt=start_dt,
                    duration_minutes=duration_minutes,
                    calendar_id=calendar_id,
                    occurrence_rate=occurrence_rate,
                    description=description
                )
                print(f"[DEBUG] Created recurring calendar event with ID: {event_result.get('id')}")
            else:
                # Create one-time event
                event_result = gcal.create_event(
                    summary=summary,
                    start_dt=start_dt,
                    duration_minutes=duration_minutes,
                    calendar_id=calendar_id,
                    description=description
                )
                print(f"[DEBUG] Created one-time calendar event with ID: {event_result.get('id')}")

            print(f"[DEBUG] Calendar event result: {event_result}")
            return {
                "calendar_created": True,
                "calendar_event_id": event_result.get('id'),
                "calendar_event_url": event_result.get('htmlLink'),
                "calendar_action": "created"
            }

        except Exception as e:
            print(f"[ERROR] Failed to create calendar event: {e}")
            # Return placeholder values on error (as per old system)
            return {
                "calendar_created": False,
                "calendar_event_id": None,
                "calendar_event_url": None
            }

    def _update_calendar_event(self, call_data: Dict, existing_resources: Dict) -> Dict:
        """Update existing Google Calendar event."""
        try:
            # Get existing Calendar ID from mapping (stored at call series level)
            existing_occurrence = existing_resources["existing_occurrence"]
            call_series = existing_occurrence["call_series"]
            existing_calendar_event_id = self.mapping_manager.get_series_calendar_event_id(call_series)

            # Pass zoom URL to calendar creation if available
            calendar_call_data = call_data.copy()
            if hasattr(self, '_last_zoom_url'):
                calendar_call_data["zoom_url"] = self._last_zoom_url

            calendar_result = self._create_or_update_calendar_event(calendar_call_data, existing_calendar_event_id)
            return calendar_result

        except Exception as e:
            print(f"[ERROR] Failed to update calendar event: {e}")
            return {
                "calendar_created": False,
                "calendar_event_id": None,
                "calendar_event_url": None
            }

    def _create_discourse_topic(self, call_data: Dict) -> Dict:
        """Create Discourse topic."""
        try:
            # Import existing discourse module
            from modules import discourse

            # Extract parameters from call_data
            title = call_data["issue_title"]
            agenda = call_data.get("agenda", "")
            start_time = call_data.get("start_time")
            duration = call_data.get("duration")
            issue_url = call_data["issue_url"]

            # Build clean discourse body with only essential information
            discourse_body_parts = []

            # Add agenda if provided
            if agenda:
                discourse_body_parts.append(agenda)

            # Add meeting time information
            if start_time and duration:
                try:
                    from datetime import datetime
                    # Parse the start time
                    if start_time.endswith('Z'):
                        start_time_parsed = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                    else:
                        start_time_parsed = datetime.fromisoformat(start_time)

                    # Format the date and time
                    formatted_date = start_time_parsed.strftime("%A, %B %d, %Y")
                    formatted_time = start_time_parsed.strftime("%H:%M UTC")

                    time_info = f"**Meeting Time:** {formatted_date} at {formatted_time} ({duration} minutes)"
                    discourse_body_parts.append(time_info)
                except Exception as e:
                    print(f"[WARN] Failed to format meeting time: {e}")
                    # Fallback to raw time info
                    time_info = f"**Meeting Time:** {start_time} ({duration} minutes)"
                    discourse_body_parts.append(time_info)

            # Add GitHub issue link
            discourse_body_parts.append(f"\n[GitHub Issue]({issue_url})")

            # Join all parts
            discourse_body = "\n\n".join(discourse_body_parts)

            print(f"[DEBUG] Creating Discourse topic: {title}")
            print(f"[DEBUG] Body length: {len(discourse_body)} characters")

            # Create topic using existing discourse module
            discourse_response = discourse.create_topic(
                title=title,
                body=discourse_body,
                category_id=63  # Same category as old system
            )

            topic_id = discourse_response.get("topic_id")
            action = discourse_response.get("action", "failed")

            if not topic_id:
                raise ValueError(f"Discourse module failed to return a valid topic ID for title '{title}'")

            discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"

            print(f"[DEBUG] Discourse topic {action}: ID {topic_id}, title '{title}'")
            print(f"[DEBUG] Discourse URL: {discourse_url}")

            return {
                "discourse_created": True,
                "discourse_topic_id": topic_id,
                "discourse_url": discourse_url,
                "action": action
            }

        except discourse.DiscourseDuplicateTitleError as e:
            print(f"[INFO] Discourse topic creation failed: Title '{e.title}' already exists.")

            # Try to find existing topic ID in mapping for recurring calls
            if call_data.get("call_series") and not call_data.get("call_series").startswith("one-off-"):
                existing_topic_id = self._find_existing_discourse_topic(call_data["call_series"])
                if existing_topic_id:
                    discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{existing_topic_id}"
                    print(f"[DEBUG] Found existing topic ID {existing_topic_id} for series '{call_data['call_series']}'")

                    return {
                        "discourse_created": True,
                        "discourse_topic_id": existing_topic_id,
                        "discourse_url": discourse_url,
                        "discourse_action": "found_duplicate_series"
                    }

            # If no existing topic found, return error
            return {
                "discourse_created": False,
                "discourse_topic_id": f"placeholder-duplicate-{call_data['issue_number']}",
                "discourse_url": "https://ethereum-magicians.org (Duplicate title, ID not found)",
                "discourse_action": "failed_duplicate_title"
            }

        except Exception as e:
            print(f"[ERROR] Failed to create Discourse topic: {e}")
            return {
                "discourse_created": False,
                "discourse_topic_id": f"placeholder-error-{call_data['issue_number']}",
                "discourse_url": "https://ethereum-magicians.org (API error occurred)",
                "discourse_action": "failed"
            }

    def _get_call_series_display_name(self, call_series_key: str) -> str:
        """Get the human-friendly display name for a call series key."""
        display_name_mapping = {
            "acde": "All Core Devs - Execution",
            "acdc": "All Core Devs - Consensus",
            "acdt": "All Core Devs - Testing",
            "awd": "All Wallet Devs",
            "beam": "Beam Call",
            "eip": "EIP Editing Office Hour",
            "eipip": "EIPIP Meeting",
            "evm": "EVM Resource Pricing Breakout",
            "eth_simulate": "eth_simulate Implementers",
            "ethproofs": "Ethproofs Community Call",
            "focil": "FOCIL Implementers",
            "l2": "L2 Interop Working Group",
            "pq": "PQ Interop",
            "peerdas": "PeerDAS Breakout",
            "portal": "Portal Implementers",
            "research": "Protocol Research Call",
            "rpc": "RPC Standards Call",
            "rollcall": "RollCall",
            "stateless": "Stateless Implementers"
        }

        return display_name_mapping.get(call_series_key, call_series_key)

    def _find_existing_discourse_topic(self, call_series: str) -> Optional[int]:
        """Find existing Discourse topic ID for a call series."""
        try:
            mapping = self.mapping_manager.load_mapping()

            # Find entries matching the call series with a valid topic ID
            series_entries = sorted(
                [entry for entry in mapping.values()
                 if entry.get("call_series") == call_series and
                    entry.get("discourse_topic_id") and
                    not str(entry.get("discourse_topic_id")).startswith("placeholder")],
                key=lambda e: e.get("issue_number", 0),
                reverse=True
            )

            # If not found at top level, check occurrences within matching series entries
            if not series_entries:
                potential_series_matches = [
                    (m_id, entry) for m_id, entry in mapping.items()
                    if entry.get("call_series") == call_series and "occurrences" in entry
                ]

                for m_id, entry in potential_series_matches:
                    # Sort occurrences by issue number within the series
                    sorted_occurrences = sorted(
                        [occ for occ in entry.get("occurrences", [])
                         if isinstance(occ, dict) and occ.get("discourse_topic_id") and
                            not str(occ.get("discourse_topic_id")).startswith("placeholder")],
                        key=lambda o: o.get("issue_number", 0),
                        reverse=True
                    )

                    if sorted_occurrences:
                        # Found the most recent valid topic ID within this series' occurrences
                        topic_id = sorted_occurrences[0]["discourse_topic_id"]
                        print(f"[DEBUG] Found existing topic ID {topic_id} in occurrences for series '{call_series}'")
                        return topic_id

            if series_entries:
                topic_id = series_entries[0]["discourse_topic_id"]
                print(f"[DEBUG] Found existing topic ID {topic_id} at top-level for series '{call_series}'")
                return topic_id

            return None

        except Exception as e:
            print(f"[ERROR] Failed to find existing Discourse topic: {e}")
            return None

    def _create_youtube_streams(self, call_data: Dict) -> Dict:
        """Create YouTube streams."""
        try:
            # Import existing youtube_utils module
            from modules import youtube_utils

            # Extract parameters from call_data
            title = call_data["issue_title"]
            start_time = call_data["start_time"]
            occurrence_rate = call_data.get("occurrence_rate", "other")
            call_series = call_data.get("call_series", "unknown")
            is_recurring = not call_series.startswith("one-off-")
            issue_url = call_data["issue_url"]

            # Build description (same as old system)
            description = f"Recurring meeting: {title}\nGitHub Issue: {issue_url}"

            print(f"[DEBUG] Creating YouTube streams for: {title}")
            print(f"[DEBUG] Start time: {start_time}")
            print(f"[DEBUG] Recurring: {is_recurring}, Rate: {occurrence_rate}")

            # Only create streams for recurring meetings with valid occurrence rates
            if not is_recurring or occurrence_rate == "none":
                print(f"[DEBUG] Skipping YouTube stream creation - not recurring or no occurrence rate")
                return {
                    "youtube_streams_created": False,
                    "youtube_streams": None
                }

            # Create recurring streams using existing youtube_utils module
            youtube_streams = youtube_utils.create_recurring_streams(
                title=title,
                description=description,
                start_time=start_time,
                occurrence_rate=occurrence_rate
            )

            if youtube_streams:
                print(f"[DEBUG] Successfully created {len(youtube_streams)} YouTube streams")

                # Format stream links for display (same as old system)
                stream_links = []
                for i, stream in enumerate(youtube_streams, 1):
                    # Extract date from stream details if available
                    stream_date = ""
                    if 'scheduled_time' in stream:
                        try:
                            from datetime import datetime
                            scheduled_time = stream['scheduled_time']
                            if scheduled_time.endswith('Z'):
                                scheduled_time = scheduled_time.replace('Z', '+00:00')
                            date_obj = datetime.fromisoformat(scheduled_time)
                            stream_date = f" ({date_obj.strftime('%b %d, %Y')})"
                        except Exception as e:
                            print(f"[DEBUG] Error formatting stream date: {e}")

                    stream_links.append(f"- Stream {i}{stream_date}: {stream['stream_url']}")

                return {
                    "youtube_streams_created": True,
                    "youtube_streams": youtube_streams,
                    "stream_links": stream_links,
                    "youtube_action": "created"
                }
            else:
                print(f"[DEBUG] No YouTube streams created")
                return {
                    "youtube_streams_created": False,
                    "youtube_streams": None,
                    "stream_links": []
                }

        except Exception as e:
            print(f"[ERROR] Failed to create YouTube streams: {e}")
            return {
                "youtube_streams_created": False,
                "youtube_streams": None,
                "stream_links": []
            }

    def _send_telegram_notification(self, call_data: Dict, issue, resource_results: Dict, is_update: bool):
        """Send Telegram notification to the Ethereum Protocol Updates channel."""
        try:
            # Import telegram module
            from modules import tg
            import requests

            # For updates, only send Telegram if resources actually changed
            if is_update and not self._resources_changed(resource_results):
                print(f"[DEBUG] No resource changes detected, skipping Telegram notification for issue #{call_data['issue_number']}")
                return

            # Check if any resources were successfully created
            resources_created = self._resources_changed(resource_results)

            # Build the message
            if resources_created:
                # Success case - include all created resources
                telegram_message_body = (
                    f"<b>{call_data['issue_title']}</b>\n\n"
                    f"<b>Links:</b>\n"
                    f"• <a href='{call_data['issue_url']}'>GitHub Issue</a>\n"
                )

                # Add Discourse link if created
                discourse_url = resource_results.get("discourse_url")
                if discourse_url and discourse_url != "https://ethereum-magicians.org (API error occurred)":
                    telegram_message_body += f"• <a href='{discourse_url}'>Discourse Topic</a>\n"

                # Add Google Calendar link if created
                calendar_event_url = resource_results.get("calendar_event_url")
                if calendar_event_url:
                    telegram_message_body += f"• <a href='{calendar_event_url}'>Google Calendar</a>\n"

                # Add YouTube streams if created
                if resource_results.get("youtube_streams_created") and resource_results.get("stream_links"):
                    telegram_message_body += f"\n<b>YouTube Stream Links:</b>\n"
                    for stream_link in resource_results["stream_links"]:
                        # Extract URL from stream link format: "- Stream 1: https://..."
                        if "https://" in stream_link:
                            url = stream_link.split("https://")[1].split(" ")[0]
                            telegram_message_body += f"• <a href='https://{url}'>Stream {stream_link.split('Stream ')[1].split(':')[0]}</a>\n"
            else:
                # Failure case - notify about the failure
                telegram_message_body = (
                    f"<b>⚠️ Resource Creation Failed</b>\n\n"
                    f"<b>{call_data['issue_title']}</b>\n\n"
                    f"<b>Status:</b>\n"
                )

                # Add failure details for each resource
                if not call_data.get("skip_zoom_creation") and not resource_results.get("zoom_created"):
                    telegram_message_body += "• ❌ Zoom meeting creation failed\n"

                if not call_data.get("skip_gcal_creation") and not resource_results.get("calendar_created"):
                    telegram_message_body += "• ❌ Calendar event creation failed\n"

                if not resource_results.get("discourse_created"):
                    telegram_message_body += "• ❌ Discourse topic creation failed\n"

                if call_data.get("need_youtube_streams") and not resource_results.get("youtube_streams_created"):
                    telegram_message_body += "• ❌ YouTube streams creation failed\n"

                telegram_message_body += f"\n<a href='{call_data['issue_url']}'>GitHub Issue</a>"

            # Send the message
            telegram_channel_id = os.environ.get("TELEGRAM_CHAT_ID")
            telegram_channel_sent = False

            if telegram_channel_id and tg:
                try:
                    # For new issues, always send a new message
                    # For updates, try to update existing message if available
                    existing_occurrence = self.mapping_manager.find_occurrence(call_data["issue_number"])
                    existing_telegram_message_id = None

                    if existing_occurrence and is_update:
                        existing_telegram_message_id = existing_occurrence["occurrence"].get("telegram_message_id")

                    if existing_telegram_message_id:
                        print(f"[DEBUG] Attempting to update existing Telegram message ID: {existing_telegram_message_id}")
                        update_successful = tg.update_message(existing_telegram_message_id, telegram_message_body)
                        if update_successful:
                            print(f"[DEBUG] Successfully updated Telegram message {existing_telegram_message_id}.")
                            telegram_channel_sent = True
                            # Preserve the message ID in the occurrence data
                            if existing_occurrence:
                                self.mapping_manager.update_occurrence(
                                    existing_occurrence["call_series"],
                                    call_data["issue_number"],
                                    {"telegram_message_id": existing_telegram_message_id}
                                )
                        else:
                            error_msg = (f"Failed to update Telegram message ID {existing_telegram_message_id}. "
                                         "Message might have been deleted or API call failed.")
                            print(f"[ERROR] {error_msg}")
                    else:
                        # No existing message ID – send a new one
                        print(f"[DEBUG] Sending new Telegram message for issue #{call_data['issue_number']}.")
                        new_message_id = tg.send_message(telegram_message_body)
                        if new_message_id:
                            telegram_channel_sent = True
                            # Store the new message ID in the occurrence data if we have one
                            if existing_occurrence:
                                self.mapping_manager.update_occurrence(
                                    existing_occurrence["call_series"],
                                    call_data["issue_number"],
                                    {"telegram_message_id": new_message_id}
                                )
                                print(f"[DEBUG] Stored new telegram_message_id {new_message_id} in occurrence data for issue #{call_data['issue_number']}.")
                        else:
                            print(f"[ERROR] tg.send_message failed – no message ID returned.")

                    if telegram_channel_sent:
                        print(f"[DEBUG] Telegram notification {'updated' if existing_telegram_message_id else 'sent'} successfully")
                    else:
                        print(f"[DEBUG] Failed to send/update Telegram channel message.")

                except requests.exceptions.HTTPError as http_err:
                    # Log a controlled error message without the full URL/token
                    status_code = http_err.response.status_code if http_err.response else "Unknown"
                    error_reason = http_err.response.reason if http_err.response else "Unknown reason"
                    error_msg = f"Telegram API HTTP Error {status_code} ({error_reason})."
                    print(f"[ERROR] Telegram channel notification failed: {error_msg}")
                except Exception as e:
                    # Catch other potential exceptions (network errors, etc.)
                    error_msg = f"An unexpected error occurred: {type(e).__name__}"
                    print(f"[ERROR] Telegram channel notification failed: {error_msg}")
            else:
                print("[DEBUG] Telegram channel ID not configured or tg module not available.")

        except Exception as e:
            print(f"[ERROR] Failed to send Telegram notification: {e}")

    def _resources_changed(self, resource_results: Dict) -> bool:
        """Check if any resources were actually created/updated."""
        # Check if Zoom was actually created (not just updated)
        zoom_actually_created = (resource_results.get("zoom_created") and
                               resource_results.get("zoom_action") != "updated")

        # Check if Discourse was actually created (not just found existing)
        discourse_actually_created = (resource_results.get("discourse_created") and
                                    resource_results.get("discourse_action") not in ["existing", "found_duplicate_series"])

        # Check if Calendar was actually created (not just found existing or updated)
        calendar_actually_created = (resource_results.get("calendar_created") and
                                   resource_results.get("calendar_action") not in ["existing", "updated"])

        # Check if YouTube streams were actually created (not just found existing)
        youtube_actually_created = (resource_results.get("youtube_streams_created") and
                                  resource_results.get("youtube_action") != "existing")

        return any([
            zoom_actually_created,
            calendar_actually_created,
            discourse_actually_created,
            youtube_actually_created
        ])

    def _post_results(self, call_data: Dict, issue, resource_results: Dict, is_update: bool):
        """Post results to GitHub issue."""
        try:
            # Only post comment on initial creation or if resources actually changed
            if not is_update:
                # Initial creation - always post comment
                should_post = True
                comment_prefix = "🎉 **Protocol Call Resources Created:**"
            else:
                # Edit - only post if resources actually changed
                should_post = self._resources_changed(resource_results)
                comment_prefix = "🔄 **Protocol Call Resources Updated:**"

            if not should_post:
                print(f"[DEBUG] No resource changes detected, skipping comment for issue #{issue.number}")
                return

            # Build comment content
            comment_lines = [comment_prefix, ""]

            # Add resource creation results - only include newly created resources
            if resource_results["zoom_created"]:
                if resource_results.get("zoom_url"):
                    comment_lines.append(f"✅ **Zoom**: [Join Meeting]({resource_results['zoom_url']})")
                else:
                    comment_lines.append("✅ **Zoom**: Meeting created (join URL not available)")
            elif call_data["skip_zoom_creation"]:
                comment_lines.append("⏭️ **Zoom**: Skipped (user opted out)")
            else:
                comment_lines.append("❌ **Zoom**: Failed to create")

            if resource_results["calendar_created"]:
                calendar_action = resource_results.get("calendar_action", "created")
                if calendar_action in ["existing", "updated"]:
                    # Don't include existing or updated resources in the comment
                    pass
                elif resource_results.get("calendar_event_url"):
                    comment_lines.append(f"✅ **Calendar**: [Add to Calendar]({resource_results['calendar_event_url']})")
                else:
                    comment_lines.append("✅ **Calendar**: Event created")
            elif call_data["skip_gcal_creation"]:
                comment_lines.append("⏭️ **Calendar**: Skipped (not on Ethereum calendar)")
            else:
                comment_lines.append("❌ **Calendar**: Failed to create")

            if resource_results["discourse_created"]:
                discourse_action = resource_results.get("discourse_action", "created")
                if discourse_action in ["existing", "found_duplicate_series"]:
                    # Don't include existing resources in the comment
                    pass
                elif resource_results.get("discourse_url"):
                    comment_lines.append(f"✅ **Discourse**: [{discourse_action.capitalize()} Topic]({resource_results['discourse_url']})")
                else:
                    comment_lines.append(f"✅ **Discourse**: {discourse_action.capitalize()}")
            else:
                comment_lines.append("❌ **Discourse**: Failed to create")

            if resource_results["youtube_streams_created"]:
                youtube_action = resource_results.get("youtube_action", "created")
                if youtube_action == "existing":
                    # Don't include existing resources in the comment
                    pass
                else:
                    comment_lines.append("✅ **YouTube**: Streams created")
                    if resource_results.get("stream_links"):
                        for stream_link in resource_results["stream_links"]:
                            comment_lines.append(f"   📺 {stream_link}")
            elif call_data["need_youtube_streams"]:
                comment_lines.append("❌ **YouTube**: Failed to create streams")

            # [DEBUG] Add issue reference for context
            comment_lines.append(f"\n📋 Issue: #{issue.number}")

            comment_text = "\n".join(comment_lines)

            # issue.create_comment(comment_text)
            # print(f"[DEBUG] Posted results comment to issue #{issue.number}")
            # [DEBUG] Send message to Telegram channel
            try:
                from modules import tg
                message_id = tg.send_message(comment_text)
                print(f"[DEBUG] Posted results to Telegram (message ID: {message_id}) for issue #{issue.number}")
            except ImportError:
                print("[ERROR] Telegram module not available")
            except Exception as e:
                print(f"[ERROR] Failed to send Telegram message: {e}")

        except Exception as e:
            print(f"[ERROR] Failed to post results: {e}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Handle protocol call issues")
    parser.add_argument("--issue_number", type=int, required=True, help="GitHub issue number")
    parser.add_argument("--repo", required=True, help="GitHub repository (format: owner/repo)")

    args = parser.parse_args()

    handler = ProtocolCallHandler()
    success = handler.handle_protocol_call(args.issue_number, args.repo)

    if success:
        print(f"[SUCCESS] Protocol call handler completed for issue #{args.issue_number}")
        sys.exit(0)
    else:
        print(f"[FAILURE] Protocol call handler failed for issue #{args.issue_number}")
        sys.exit(1)


if __name__ == "__main__":
    main()