#!/usr/bin/env python3
"""
Protocol Call Handler

Clean, focused implementation for handling protocol calls using the new form-based workflow.
This is a fresh implementation designed specifically for the new data model.
"""

import sys
import os
import re
import argparse
from typing import Dict, Optional, List, Set

# Add the modules directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))

from modules.form_parser import FormParser
from modules.mapping_manager import MappingManager
from modules.datetime_utils import generate_savvytime_link, format_datetime_for_discourse, format_datetime_for_stream_display


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
                result = self._update_zoom_meeting(call_data)
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
            existing_calendar_id = existing_resources.get("calendar_event_id")

            print(f"[DEBUG] Calendar decision: has_existing={has_existing}, calendar_id={existing_calendar_id}")

            if has_existing and existing_calendar_id:
                print(f"[DEBUG] Updating existing calendar event with ID: {existing_calendar_id}")
                result = self._update_calendar_event(call_data, existing_resources)
            else:
                print(f"[DEBUG] Creating new calendar event (has_existing={has_existing}, existing_id={existing_calendar_id})")
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

            # Import existing discourse module
            from modules import discourse

            title = call_data["issue_title"]
            discourse_body = self._build_discourse_body(call_data)

            # Get existing topic ID if available
            existing_topic_id = None
            if has_existing:
                existing_occurrence = existing_resources["existing_occurrence"]["occurrence"]
                existing_topic_id = existing_occurrence["discourse_topic_id"]

            # Use the unified create_or_update function
            discourse_response = discourse.create_or_update_topic(
                title=title,
                body=discourse_body,
                topic_id=existing_topic_id,
                category_id=63
            )

            topic_id = discourse_response.get("topic_id")
            action = discourse_response.get("action", "failed")

            if not topic_id:
                raise ValueError(f"Discourse module failed to return a valid topic ID")

            discourse_url = f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{topic_id}"

            print(f"[DEBUG] Discourse topic {action}: ID {topic_id}, title '{title}'")
            print(f"[DEBUG] Discourse URL: {discourse_url}")

            result = {
                "discourse_created": True,
                "discourse_topic_id": topic_id,
                "discourse_url": discourse_url,
                "discourse_action": action
            }

            return result

        except discourse.DiscourseDuplicateTitleError as e:
            print(f"[INFO] Discourse topic failed: Title '{e.title}' already exists.")

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
            print(f"[ERROR] Failed to handle Discourse resource: {e}")
            return {
                "discourse_created": False,
                "discourse_topic_id": f"placeholder-error-{call_data['issue_number']}",
                "discourse_url": "https://ethereum-magicians.org (API error occurred)",
                "discourse_action": "failed"
            }

    def _handle_youtube_resource(self, call_data: Dict, existing_resources: Dict) -> Dict:
        """Handle YouTube streams creation/updates."""
        result = {
            "youtube_streams_created": False,
            "youtube_streams": None,
            "stream_links": []
        }

        try:
            # Skip if user opted out of YouTube streams
            if not call_data.get("need_youtube_streams"):
                print(f"[DEBUG] YouTube stream creation skipped (user opted out)")
                return result

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
                print(f"[DEBUG] Set _last_zoom_url: {self._last_zoom_url}")
            else:
                # Try to get an existing working zoom URL from the mapping
                series_meeting_id = self.mapping_manager.get_series_meeting_id(call_data["call_series"])
                if series_meeting_id and series_meeting_id != "custom":
                    try:
                        from modules import zoom
                        enhanced_url = zoom.get_meeting_url_with_passcode(series_meeting_id)
                        if enhanced_url:
                            self._last_zoom_url = enhanced_url
                            print(f"[DEBUG] Using existing enhanced Zoom URL: {enhanced_url}")
                        else:
                            self._last_zoom_url = f"https://zoom.us/j/{series_meeting_id}"
                            print(f"[DEBUG] Using existing basic Zoom URL: {self._last_zoom_url}")
                    except Exception as e:
                        print(f"[DEBUG] Could not get existing Zoom URL: {e}")
                        self._last_zoom_url = None  # Don't set a bad fallback
                else:
                    print(f"[DEBUG] No valid meeting ID available for Zoom URL fallback")
                    self._last_zoom_url = None

            calendar_result = self._handle_calendar_resource(call_data, existing_resources)
            resource_results.update(calendar_result)
            if not call_data.get("skip_gcal_creation") and not calendar_result.get("calendar_created"):
                critical_failures.append("Calendar event creation failed")

            # Log calendar action for debugging
            if calendar_result.get("calendar_created"):
                action = calendar_result.get("calendar_action", "unknown")
                event_id = calendar_result.get("calendar_event_id")
                print(f"[DEBUG] Calendar event {action}: {event_id}")

            discourse_result = self._handle_discourse_resource(call_data, existing_resources)
            resource_results.update(discourse_result)
            if not discourse_result.get("discourse_created"):
                critical_failures.append("Discourse topic creation failed")

            youtube_result = self._handle_youtube_resource(call_data, existing_resources)
            resource_results.update(youtube_result)
            if call_data.get("need_youtube_streams") and not youtube_result.get("youtube_streams_created"):
                critical_failures.append("YouTube streams creation failed")

            # 7. Always update mapping first, then handle resources
            success = self._update_mapping(call_data, issue, is_update)
            if not success:
                print(f"[ERROR] Failed to update mapping for issue #{issue_number}")
                return False

            # Update mapping with any successfully created resources
            self._update_mapping_with_resources(call_data, resource_results)
            if critical_failures:
                print(f"[ERROR] Critical failures occurred: {', '.join(critical_failures)}")
                print(f"[INFO] Saved any successful resource IDs to mapping; failed resources can be retried later")

            # 8. Save mapping
            self.mapping_manager.save_mapping()

            # 9. Send Telegram notification
            self._send_telegram_notification(call_data, issue, resource_results, is_update)

            # 10. Post results to GitHub
            self._post_results(call_data, issue, resource_results, is_update)

            # 11. Clean up issue body for better readability (only on initial creation)
            if not is_update:
                self._clean_issue_body_if_needed(issue)

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

            # For new occurrences, check series-level resources
            if not call_series_entry:
                print(f"[DEBUG] No existing occurrence found for issue #{call_data['issue_number']}, checking series-level resources")

                # Check series-level resources even for new occurrences
                series_meeting_id = self.mapping_manager.get_series_meeting_id(call_data["call_series"])
                has_zoom = bool(series_meeting_id and not str(series_meeting_id).startswith("placeholder"))

                # Check for existing recurring calendar event at series level
                calendar_event_id = self.mapping_manager.get_series_calendar_event_id(call_data["call_series"])
                has_calendar = bool(calendar_event_id)

                print(f"[DEBUG] Series-level resources for {call_data['call_series']}:")
                print(f"  - Zoom: {has_zoom} (ID: {series_meeting_id})")
                print(f"  - Calendar: {has_calendar} (ID: {calendar_event_id})")

                return {
                    "has_zoom": has_zoom,
                    "has_calendar": has_calendar,
                    "has_discourse": False,
                    "has_youtube": False,
                    "calendar_event_id": calendar_event_id
                }

            occurrence = call_series_entry.get("occurrence")
            if not occurrence:
                print(f"[ERROR] No occurrence data found in call_series_entry for issue #{call_data['issue_number']}")
                print(f"[DEBUG] call_series_entry structure: {call_series_entry}")
                return {
                    "has_zoom": False,
                    "has_calendar": False,
                    "has_discourse": False,
                    "has_youtube": False
                }

            # Check for existing resources
            series_meeting_id = self.mapping_manager.get_series_meeting_id(call_data["call_series"])
            has_zoom = bool(series_meeting_id and not str(series_meeting_id).startswith("placeholder"))

            # Calendar event ID is stored at the parent level (call series level)
            call_series = call_series_entry.get("call_series")
            calendar_event_id = self.mapping_manager.get_series_calendar_event_id(call_series) if call_series else None
            has_calendar = bool(calendar_event_id)
            has_discourse = (occurrence.get("discourse_topic_id") and
                           not str(occurrence.get("discourse_topic_id")).startswith("placeholder"))
            # Safely handle youtube_streams which might be None
            youtube_streams = occurrence.get("youtube_streams", [])
            has_youtube = bool(youtube_streams)

            print(f"[DEBUG] Existing resources for issue #{call_data['issue_number']}:")
            print(f"  - Zoom: {has_zoom} (ID: {call_series_entry.get('meeting_id')})")
            print(f"  - Calendar: {has_calendar} (ID: {calendar_event_id})")
            print(f"  - Discourse: {has_discourse} (ID: {occurrence.get('discourse_topic_id')})")
            print(f"  - YouTube: {has_youtube} (streams: {len(youtube_streams) if youtube_streams else 0})")
            print(f"[DEBUG] Full occurrence data: {occurrence}")
            print(f"[DEBUG] Full call_series_entry data: {call_series_entry}")

            return {
                "has_zoom": has_zoom,
                "has_calendar": has_calendar,
                "has_discourse": has_discourse,
                "has_youtube": has_youtube,
                "existing_occurrence": call_series_entry,
                "calendar_event_id": calendar_event_id
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
                # If livestreams are created, skip YouTube recording upload to avoid duplicate content
                update_data["skip_youtube_upload"] = True
                print(f"[DEBUG] Adding YouTube streams: {len(resource_results['youtube_streams'])} streams")
                print(f"[DEBUG] Setting skip_youtube_upload=True (livestream exists, no recording upload needed)")

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
            # skip_youtube_upload logic:
            # - True if no Zoom meeting (skip_zoom_creation=True) OR if YouTube livestreams will be created
            # - Will be updated to True later if YouTube livestreams are actually created
            initial_skip_upload = call_data.get("skip_zoom_creation", False)

            occurrence_data = self.mapping_manager.create_occurrence_data(
                issue_number=call_data["issue_number"],
                issue_title=call_data["issue_title"],
                discourse_topic_id=None,  # Will be set later if Discourse is created
                start_time=call_data["start_time"],
                duration=call_data["duration"],
                skip_youtube_upload=initial_skip_upload,
                skip_transcript_processing=call_data.get("skip_zoom_creation", False)
            )

            if is_update:
                # Update existing occurrence - only update specific fields to preserve existing data
                update_fields = {
                    "issue_title": call_data["issue_title"],
                    "start_time": call_data["start_time"],
                    "duration": call_data["duration"]
                }

                success = self.mapping_manager.update_occurrence(
                    call_data["call_series"],
                    call_data["issue_number"],
                    update_fields  # Only update specific fields, preserve others like telegram_message_id
                )
            else:
                # Add new occurrence
                success = self.mapping_manager.add_occurrence(
                    call_data["call_series"],
                    occurrence_data
                )

            # Handle meeting ID based on user choice
            if success and not is_update:
                if call_data.get("skip_zoom_creation"):
                    # User opted out of Zoom - set to "custom"
                    self.mapping_manager.set_series_custom_meeting(call_data["call_series"])

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
                if is_recurring and occurrence_rate not in ["none", "other"]:
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
                "zoom_url": None  # Don't set a bad fallback URL, let calendar handle it
            }

    def _update_zoom_meeting(self, call_data: Dict) -> Dict:
        """Update existing Zoom meeting."""
        try:
            existing_meeting_id = self.mapping_manager.get_series_meeting_id(call_data["call_series"])
            result = {
                "zoom_created": True,
                "zoom_id": existing_meeting_id,
                "zoom_url": None,  # Will be set below based on API success/failure
                "zoom_action": "updated"
            }

            # Update the meeting if we have changes
            if existing_meeting_id:
                from modules import zoom
                try:
                    update_result = zoom.update_meeting(
                        existing_meeting_id,
                        call_data["issue_title"],
                        call_data["start_time"],
                        call_data["duration"]
                    )
                    # Use the official join_url from API response, or construct fallback
                    result["zoom_url"] = update_result.get("join_url") or f"https://zoom.us/j/{existing_meeting_id}"
                    print(f"[SUCCESS] Updated Zoom meeting {existing_meeting_id}")
                except Exception as zoom_error:
                    # Handle permission/auth errors gracefully for edits
                    error_text = str(zoom_error).lower()

                    # For HTTP errors, also check the response content
                    if hasattr(zoom_error, 'response') and hasattr(zoom_error.response, 'text'):
                        error_text += " " + zoom_error.response.text.lower()

                    if any(phrase in error_text for phrase in ["access token", "permission", "invalid access token", "scopes"]):
                        print(f"[WARN] Zoom update skipped due to insufficient permissions: {zoom_error}")
                        print(f"[INFO] Meeting link remains functional, only title/description won't be updated in Zoom")
                        result["zoom_action"] = "skipped_permissions"
                    else:
                        # Re-raise other errors (API issues, etc.)
                        raise zoom_error

                try:
                    enhanced_url = zoom.get_meeting_url_with_passcode(existing_meeting_id)
                    if enhanced_url:
                        result["zoom_url"] = enhanced_url
                        print(f"[DEBUG] Retrieved enhanced Zoom URL with passcode for calendar")
                    else:
                        result["zoom_url"] = f"https://zoom.us/j/{existing_meeting_id}"
                        print(f"[DEBUG] Using basic Zoom URL (no passcode available)")
                except Exception as e:
                    print(f"[WARN] Could not retrieve enhanced Zoom URL: {e}")
                    result["zoom_url"] = f"https://zoom.us/j/{existing_meeting_id}"
            else:
                # No existing meeting ID - don't set a bad fallback URL
                print(f"[ERROR] No existing meeting ID found for update")
                result["zoom_url"] = None

            return result

        except Exception as e:
            print(f"[ERROR] Failed to update Zoom meeting: {e}")
            # For permission errors, don't fail the whole process
            if any(phrase in str(e).lower() for phrase in ["access token", "permission", "invalid access token", "scopes"]):
                existing_meeting_id = self.mapping_manager.get_series_meeting_id(call_data["call_series"])

                # Try to get enhanced URL with passcode for calendar
                working_zoom_url = f"https://zoom.us/j/{existing_meeting_id}" if existing_meeting_id else None
                if existing_meeting_id:
                    try:
                        from modules import zoom
                        enhanced_url = zoom.get_meeting_url_with_passcode(existing_meeting_id)
                        if enhanced_url:
                            working_zoom_url = enhanced_url
                            print(f"[DEBUG] Retrieved enhanced Zoom URL with passcode (fallback path)")
                        else:
                            print(f"[DEBUG] Using basic Zoom URL (fallback path, no passcode available)")
                    except Exception as url_error:
                        print(f"[WARN] Could not retrieve enhanced Zoom URL (fallback path): {url_error}")

                return {
                    "zoom_created": True,  # Don't fail the edit process
                    "zoom_id": existing_meeting_id,
                    "zoom_url": working_zoom_url,  # Use enhanced meeting link if available
                    "zoom_action": "skipped_permissions"
                }
            else:
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

            # Get calendar ID from environment
            calendar_id = os.getenv("GCAL_ID")

            # Build description with issue link and optional Zoom link
            description_parts = []

            # Add meeting link to description if requested and available
            if call_data.get("display_zoom_link_in_invite") and call_data.get("zoom_url"):
                description_parts.append(f"Meeting: {call_data['zoom_url']}")

            # Add GitHub issue link
            description_parts.append(f"Issue: {call_data['issue_url']}")

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
                    if is_recurring and occurrence_rate not in ["none", "other"]:
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
            if is_recurring and occurrence_rate not in ["none", "other"]:
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
                # Create one-time event (for one-off calls or "other" occurrence rate)
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
            # Get existing series-level Calendar ID (calendar events are only stored at series level)
            existing_calendar_event_id = existing_resources.get("calendar_event_id")

            if not existing_calendar_event_id:
                # Fallback: get series-level calendar event ID from mapping
                if "existing_occurrence" in existing_resources:
                    existing_occurrence = existing_resources["existing_occurrence"]
                    call_series = existing_occurrence["call_series"]
                    existing_calendar_event_id = self.mapping_manager.get_series_calendar_event_id(call_series)

            print(f"[DEBUG] Updating series-level calendar event with ID: {existing_calendar_event_id}")

            # Pass zoom URL to calendar creation if available
            calendar_call_data = call_data.copy()
            if hasattr(self, '_last_zoom_url'):
                calendar_call_data["zoom_url"] = self._last_zoom_url
                print(f"[DEBUG] Passing zoom_url to calendar: {self._last_zoom_url}")
            else:
                print(f"[DEBUG] No _last_zoom_url available for calendar")

            calendar_result = self._create_or_update_calendar_event(calendar_call_data, existing_calendar_event_id)
            return calendar_result

        except Exception as e:
            print(f"[ERROR] Failed to update calendar event: {e}")
            return {
                "calendar_created": False,
                "calendar_event_id": None,
                "calendar_event_url": None
            }

    def _build_discourse_body(self, call_data: Dict) -> str:
        """Build Discourse topic body from call data."""
        agenda = call_data.get("agenda", "")
        start_time = call_data.get("start_time")
        duration = call_data.get("duration")
        issue_url = call_data["issue_url"]

        # Build clean discourse body with only essential information
        discourse_body_parts = []

        # Add agenda if provided
        if agenda:
            discourse_body_parts.append(f"### Agenda\n\n{agenda}")

        # Add meeting time information
        if start_time and duration:
            time_info = format_datetime_for_discourse(start_time, duration)
            discourse_body_parts.append(time_info)

        # Add GitHub issue link
        discourse_body_parts.append(f"\n[GitHub Issue]({issue_url})")

        # Join all parts
        return "\n\n".join(discourse_body_parts)

    def _get_call_series_display_name(self, call_series_key: str) -> str:
        """Get the human-friendly display name for a call series key."""
        display_name_mapping = {
            "acde": "All Core Devs - Execution",
            "acdc": "All Core Devs - Consensus",
            "acdt": "All Core Devs - Testing",
            "allwalletdevs": "All Wallet Devs",
            "bal": "EIP-7928 Breakout Room",
            "beam": "Beam Call",
            "eipeditingofficehour": "EIP Editing Office Hour",
            "eipip": "EIPIP Meeting",
            "epbs": "EIP-7732 Breakout Room",
            "resourcepricing": "EVM Resource Pricing Breakout",
            "ethsimulate": "eth_simulate Implementers",
            "ethproofs": "Ethproofs Community Call",
            "focil": "FOCIL Implementers",
            "l2interop": "L2 Interop Working Group",
            "pqinterop": "PQ Interop",
            "peerdas": "PeerDAS Breakout",
            "portal": "Portal Implementers",
            "protocolresearch": "Protocol Research Call",
            "rpcstandards": "RPC Standards Call",
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
                        stream_date = format_datetime_for_stream_display(stream['scheduled_time'])

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

    def _build_telegram_debug_message(self, call_data: Dict, resource_results: Dict, is_update: bool) -> str:
        """Build admin-focused Telegram message with debug information."""
        action = "🔄 UPDATED" if is_update else "🆕 CREATED"

        message_lines = [
            f"<b>{action}: {call_data['issue_title']}</b>",
            f"<b>Issue:</b> <a href='{call_data['issue_url']}'>#{call_data['issue_number']}</a>",
            f"<b>Series:</b> {call_data.get('call_series', 'unknown')}",
            ""
        ]

        # Resource status with actions
        message_lines.append("<b>📋 Resource Status:</b>")

        # Zoom
        zoom_action = resource_results.get("zoom_action", "unknown")
        zoom_id = resource_results.get("zoom_id")
        if resource_results.get("zoom_created"):
            if zoom_action == "skipped_permissions":
                message_lines.append(f"🔐 <b>Zoom:</b> Permissions skipped (ID: {zoom_id})")
            elif zoom_action == "updated":
                message_lines.append(f"🔄 <b>Zoom:</b> Updated (ID: {zoom_id})")
            elif zoom_action == "created":
                message_lines.append(f"✅ <b>Zoom:</b> Created (ID: {zoom_id})")
            else:
                message_lines.append(f"⏭️ <b>Zoom:</b> Using existing (ID: {zoom_id})")
        else:
            message_lines.append("❌ <b>Zoom:</b> Failed")

        # Calendar
        cal_action = resource_results.get("calendar_action", "unknown")
        cal_id = resource_results.get("calendar_event_id")
        if resource_results.get("calendar_created"):
            message_lines.append(f"✅ <b>Calendar:</b> {cal_action.title()} (ID: {cal_id})")
        else:
            message_lines.append("❌ <b>Calendar:</b> Failed")

        # Discourse
        discourse_action = resource_results.get("discourse_action", "unknown")
        discourse_id = resource_results.get("discourse_topic_id")
        if resource_results.get("discourse_created"):
            if discourse_action == "unchanged":
                message_lines.append(f"⏭️ <b>Discourse:</b> Content unchanged (ID: {discourse_id})")
            elif discourse_action == "updated":
                message_lines.append(f"🔄 <b>Discourse:</b> Updated (ID: {discourse_id})")
            else:
                message_lines.append(f"✅ <b>Discourse:</b> {discourse_action.title()} (ID: {discourse_id})")
        else:
            message_lines.append("❌ <b>Discourse:</b> Failed")

        # YouTube
        youtube_action = resource_results.get("youtube_action", "unknown")
        streams = resource_results.get("youtube_streams", [])
        if resource_results.get("youtube_streams_created"):
            if youtube_action == "existing":
                message_lines.append(f"⏭️ <b>YouTube:</b> Using existing ({len(streams)} streams)")
            else:
                message_lines.append(f"✅ <b>YouTube:</b> Created ({len(streams)} streams)")
        elif call_data.get("need_youtube_streams"):
            message_lines.append("❌ <b>YouTube:</b> Failed")
        else:
            message_lines.append("⏭️ <b>YouTube:</b> Skipped")

        # Add timing info
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M UTC")
        message_lines.extend(["", f"<i>Processed at {timestamp}</i>"])

        return "\n".join(message_lines)

    def _send_telegram_notification(self, call_data: Dict, issue, resource_results: Dict, is_update: bool):
        """Send Telegram notification to the ACDbot notification channel."""
        try:
            # Import telegram module
            from modules import tg
            import requests

            # Build admin-focused debug message
            telegram_message_body = self._build_telegram_debug_message(call_data, resource_results, is_update)

            # Send the message
            telegram_channel_id = os.environ.get("TELEGRAM_CHAT_ID")
            telegram_channel_sent = False

            if telegram_channel_id and tg:
                try:
                    # Always send new Telegram messages (never update existing ones)
                    print(f"[DEBUG] Sending new Telegram message for issue #{call_data['issue_number']}.")
                    new_message_id = tg.send_message(telegram_message_body)
                    if new_message_id:
                        telegram_channel_sent = True
                        print(f"[DEBUG] Successfully sent new Telegram message {new_message_id}.")
                    else:
                        print(f"[ERROR] tg.send_message failed – no message ID returned.")

                    if telegram_channel_sent:
                        print(f"[DEBUG] Telegram notification sent successfully")
                    else:
                        print(f"[DEBUG] Failed to send Telegram channel message.")

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

    def _find_existing_bot_comment(self, issue):
        """Find the bot's existing resource comment on this issue."""
        try:
            # Get bot username from environment or use fallback
            bot_username = os.getenv('GITHUB_BOT_USERNAME', 'github-actions')

            for comment in issue.get_comments():
                # Check if comment is from the bot and contains our signature
                if (comment.user.login.lower() in [bot_username.lower(), 'github-actions[bot]'] and
                    "**Protocol Call Resources" in comment.body):
                    return comment
            return None
        except Exception as e:
            print(f"[ERROR] Failed to find existing bot comment: {e}")
            return None

    def _generate_comprehensive_resource_comment(self, call_data: Dict) -> Optional[str]:
        """Generate comprehensive resource comment with ALL current resources from mapping."""
        try:
            # Find current occurrence in mapping to get ALL resources (like generate_resource_comment.py)
            existing_occurrence = self.mapping_manager.find_occurrence(call_data["issue_number"])
            if not existing_occurrence:
                print(f"[ERROR] Could not find occurrence for issue #{call_data['issue_number']} in mapping")
                return None

            call_series = existing_occurrence["call_series"]
            occurrence = existing_occurrence["occurrence"]

            # Load full mapping to get series-level data
            mapping = self.mapping_manager.load_mapping()
            series_data = mapping.get(call_series, {})

            comment_lines = [
                "⚡ **Protocol Call Resources:**",
                ""
            ]

            # Zoom Meeting with enhanced URL (including passcode if available)
            meeting_id = series_data.get('meeting_id')
            if meeting_id and not str(meeting_id).startswith("placeholder") and meeting_id != "custom":
                from modules import zoom
                enhanced_url = zoom.get_meeting_url_with_passcode(meeting_id)
                if enhanced_url:
                    comment_lines.append(f"✅ **Zoom**: [Join Meeting]({enhanced_url})")
                else:
                    comment_lines.append(f"✅ **Zoom**: [Join Meeting](https://zoom.us/j/{meeting_id})")
            elif meeting_id == "custom":
                comment_lines.append("🔗 **Zoom**: Custom meeting link (see issue description)")
            else:
                comment_lines.append("❌ **Zoom**: No meeting link available")

            # Calendar Event with proper eid encoding
            calendar_event_id = series_data.get('calendar_event_id')
            if calendar_event_id:
                from modules import gcal
                calendar_id = os.getenv("GCAL_ID")
                encoded_eid = gcal.encode_calendar_eid(calendar_event_id, calendar_id)

                if encoded_eid:
                    calendar_link = f"https://www.google.com/calendar/event?eid={encoded_eid}"
                    comment_lines.append(f"✅ **Calendar**: [Add to Calendar]({calendar_link})")
                else:
                    comment_lines.append("❌ **Calendar**: Failed to generate link")
            else:
                comment_lines.append("❌ **Calendar**: No calendar event found")

            # Discourse Topic
            discourse_topic_id = occurrence.get('discourse_topic_id')
            if discourse_topic_id:
                discourse_link = f"https://ethereum-magicians.org/t/{discourse_topic_id}"
                comment_lines.append(f"✅ **Discourse**: [Discussion Topic]({discourse_link})")
            else:
                comment_lines.append("❌ **Discourse**: No forum topic found")

            # YouTube Stream - only show if stream exists
            youtube_streams = occurrence.get('youtube_streams', [])
            if youtube_streams:
                first_stream = youtube_streams[0]
                stream_url = first_stream.get('stream_url')
                if stream_url:
                    comment_lines.append(f"✅ **YouTube Live**: [Watch Live]({stream_url})")

            return "\n".join(comment_lines)

        except Exception as e:
            print(f"[ERROR] Failed to generate comprehensive resource comment: {e}")
            return None

    def _post_results(self, call_data: Dict, issue, resource_results: Dict, is_update: bool):
        """Post results to GitHub issue."""
        try:
            # Generate comprehensive comment with ALL current resources (like generate_resource_comment.py)
            comment_prefix = "⚡ **Protocol Call Resources:**"
            comment_text = self._generate_comprehensive_resource_comment(call_data)

            # Skip posting if comment generation failed
            if not comment_text:
                print(f"[ERROR] Failed to generate comment content, skipping comment for issue #{issue.number}")
                return

            # Check for existing bot comment
            existing_comment = self._find_existing_bot_comment(issue)

            if existing_comment:
                # Only update if the content would actually be different
                if existing_comment.body.strip() != comment_text.strip():
                    existing_comment.edit(comment_text)
                    print(f"[DEBUG] Updated existing comment {existing_comment.id} on issue #{issue.number} (content changed)")
                else:
                    print(f"[DEBUG] Existing comment {existing_comment.id} is already up-to-date, no update needed")
            else:
                # Create new comment
                new_comment = issue.create_comment(comment_text)
                print(f"[DEBUG] Created new comment {new_comment.id} on issue #{issue.number}")

        except Exception as e:
            print(f"[ERROR] Failed to post results: {e}")

    def _is_issue_already_cleaned(self, issue_body: str) -> bool:
        """Check if the issue body has already been cleaned up."""
        return "<details>" in issue_body and "Meeting Configuration" in issue_body

    def _clean_issue_body_if_needed(self, issue):
        """Clean up the issue body for better readability if not already cleaned."""
        try:
            if self._is_issue_already_cleaned(issue.body):
                print(f"[DEBUG] Issue #{issue.number} body already cleaned, skipping cleanup")
                return

            cleaned_body = self._clean_issue_body(issue.body)
            if cleaned_body != issue.body:
                print(f"[DEBUG] Cleaning up issue #{issue.number} body for better readability")
                issue.edit(body=cleaned_body)
                print(f"[DEBUG] Successfully cleaned issue #{issue.number} body")
            else:
                print(f"[DEBUG] No cleanup needed for issue #{issue.number}")

        except Exception as e:
            print(f"[ERROR] Failed to clean issue body for issue #{issue.number}: {e}")

    def _generate_savvytime_link(self, datetime_str: str) -> str:
        """Generate a savvytime.com link from a datetime string."""
        return generate_savvytime_link(datetime_str)

    def _clean_issue_body(self, issue_body: str) -> str:
        """Transform issue body to hide verbose config sections while preserving parsing."""
        try:
            # Handle None input
            if issue_body is None:
                return None

            # Only proceed if this looks like a form issue
            if not self.form_parser.is_form_issue(issue_body):
                print("[DEBUG] Not a form issue, skipping cleanup")
                return issue_body

            # Auto-generate savvytime link for datetime if not already present
            cleaned_body = self._add_savvytime_link_if_needed(issue_body)

            # Find the position after "### Call Series" section
            call_series_pattern = r"(### Call Series\n\n[^\n]+\n)"
            match = re.search(call_series_pattern, cleaned_body)

            if not match:
                # Try without extra newline
                call_series_pattern = r"(### Call Series\n[^\n]+\n)"
                match = re.search(call_series_pattern, cleaned_body)

            if not match:
                print("[DEBUG] Could not find Call Series section, skipping cleanup")
                return cleaned_body

            # Split the issue body into: before call series, call series, after call series
            call_series_end = match.end()
            before_config = cleaned_body[:call_series_end]
            after_config = cleaned_body[call_series_end:]

            # Only wrap the config sections after Call Series in details
            if after_config.strip():
                cleaned_body = (
                    before_config +
                    "\n<details>\n<summary>🔧 Meeting Configuration</summary>\n\n" +
                    after_config.strip() +
                    "\n</details>\n"
                )
            else:
                cleaned_body = before_config

            return cleaned_body

        except Exception as e:
            print(f"[ERROR] Failed to clean issue body: {e}")
            return issue_body

    def _add_savvytime_link_if_needed(self, issue_body: str) -> str:
        """Add savvytime link to datetime field if user didn't provide one."""
        try:
            # Only add savvytime links for proper form issues with Call Series section
            if "### Call Series" not in issue_body:
                print("[DEBUG] No Call Series section found, skipping savvytime link generation")
                return issue_body

            # Check if savvytime.com link is already present
            if "savvytime.com" in issue_body:
                print("[DEBUG] Savvytime link already present, skipping auto-generation")
                return issue_body

            # Find the UTC Date & Time section
            datetime_pattern = r"(### UTC Date & Time\n\n)([^\n]+)"
            match = re.search(datetime_pattern, issue_body)

            if not match:
                print("[DEBUG] Could not find UTC Date & Time section")
                return issue_body

            section_prefix = match.group(1)
            datetime_text = match.group(2)

            # Check if it's already a markdown link format
            if datetime_text.startswith('[') and '](' in datetime_text:
                print("[DEBUG] DateTime already in markdown link format")
                return issue_body

            # Generate savvytime link
            savvytime_link = self._generate_savvytime_link(datetime_text)

            # Only replace if we successfully generated a link (contains markdown format)
            if savvytime_link != datetime_text and '[' in savvytime_link and '](' in savvytime_link:
                updated_body = issue_body.replace(
                    section_prefix + datetime_text,
                    section_prefix + savvytime_link
                )
                print(f"[DEBUG] Added savvytime link to datetime field")
                return updated_body
            else:
                print("[DEBUG] Could not generate valid savvytime link")
                return issue_body

        except Exception as e:
            print(f"[ERROR] Failed to add savvytime link: {e}")
            return issue_body


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