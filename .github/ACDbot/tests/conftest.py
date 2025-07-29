"""
Pytest configuration and fixtures for ACDBot tests.
"""

import pytest
import json
import os
import tempfile
from unittest.mock import Mock, patch
from pathlib import Path


@pytest.fixture
def sample_mapping():
    """Sample mapping data for testing."""
    return {
        "acde": {
            "call_series": "acde",
            "meeting_id": "88269836469",
            "is_recurring": True,
            "occurrence_rate": "bi-weekly",
            "occurrences": [
                {
                    "occurrence_number": 1,
                    "issue_number": 1462,
                    "discourse_topic_id": 23502,
                    "start_time": "2025-04-24T14:00:00Z",
                    "duration": 90
                },
                {
                    "occurrence_number": 2,
                    "issue_number": 1463,
                    "meeting_id": "86109593250",
                    "discourse_topic_id": 23503,
                    "start_time": "2025-05-08T14:00:00Z",
                    "duration": 90
                }
            ]
        },
        "one-off": {
            "89880194464": {
                "issue_number": 1465,
                "meeting_id": "89880194464",
                "discourse_topic_id": 23010
            },
            "99999999999": {
                "issue_number": 1466,
                "meeting_id": "99999999999",
                "discourse_topic_id": 23011
            }
        }
    }


@pytest.fixture
def sample_legacy_issue_body():
    """Sample legacy issue body for testing."""
    return """
### Call Series
All Core Devs - Execution

### Duration
90 minutes

### UTC Date & Time
April 24, 2025, 14:00 UTC

### Is Recurring
- [x] Yes

### Occurrence Rate
Bi-weekly

### Skip Zoom Creation
- [ ] No

### Skip Google Calendar Creation
- [ ] No

### Need YouTube Streams
- [x] Yes

### Display Zoom Link in Calendar Invite (Optional)
- [x] Yes

### Facilitator Emails (Optional)
test@example.com

### Custom Meeting Link (Optional)
_No response_

### Agenda
Test agenda for the meeting
"""


@pytest.fixture
def mock_env_vars():
    """Mock environment variables for testing."""
    env_vars = {
        "GITHUB_TOKEN": "test_github_token",
        "ZOOM_CLIENT_ID": "test_zoom_client_id",
        "ZOOM_CLIENT_SECRET": "test_zoom_client_secret",
        "ZOOM_ACCOUNT_ID": "test_zoom_account_id",
        "ZOOM_REFRESH_TOKEN": "test_zoom_refresh_token",
        "DISCOURSE_API_KEY": "test_discourse_api_key",
        "DISCOURSE_API_USERNAME": "test_discourse_username",
        "DISCOURSE_BASE_URL": "https://test.ethereum-magicians.org",
        "GOOGLE_CLIENT_ID": "test_google_client_id",
        "GOOGLE_CLIENT_SECRET": "test_google_client_secret",
        "YOUTUBE_REFRESH_TOKEN": "test_youtube_refresh_token",
        "GCAL_SERVICE_ACCOUNT_KEY": "test_gcal_service_account_key",
        "GOOGLE_CALENDAR_ID": "test_calendar_id"
    }
    with patch.dict(os.environ, env_vars):
        yield env_vars


@pytest.fixture
def temp_mapping_file():
    """Create temporary mapping file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('{"test": "data"}')
        temp_file = f.name

    yield temp_file

    # Cleanup
    if os.path.exists(temp_file):
        os.unlink(temp_file)


@pytest.fixture
def mock_github_issue():
    """Mock GitHub issue object."""
    issue = Mock()
    issue.number = 1462
    issue.title = "Test Protocol Call"
    issue.body = """
### Call Series
All Core Devs - Execution

### Duration
90

### Start Time
2025-04-24T14:00:00Z
"""
    issue.html_url = "https://github.com/test/repo/issues/1462"
    issue.create_comment = Mock()
    return issue


@pytest.fixture
def mock_zoom_api_response():
    """Mock Zoom API response."""
    return {
        "id": "123456789",
        "join_url": "https://zoom.us/j/123456789",
        "start_url": "https://zoom.us/s/123456789",
        "topic": "Test Meeting",
        "start_time": "2025-04-24T14:00:00Z",
        "duration": 90
    }


@pytest.fixture
def mock_gcal_api_response():
    """Mock Google Calendar API response."""
    return {
        "id": "cal_event_123",
        "htmlLink": "https://calendar.google.com/event?eid=cal_event_123",
        "summary": "Test Meeting",
        "start": {"dateTime": "2025-04-24T14:00:00Z"},
        "end": {"dateTime": "2025-04-24T15:30:00Z"}
    }


@pytest.fixture
def mock_discourse_api_response():
    """Mock Discourse API response."""
    return {
        "topic_id": 23502,
        "action": "created",
        "topic": {
            "id": 23502,
            "title": "Test Meeting",
            "slug": "test-meeting"
        }
    }


@pytest.fixture
def mock_youtube_api_response():
    """Mock YouTube API response."""
    return {
        "streams": [
            {
                "stream_id": "stream_1",
                "stream_url": "https://youtube.com/live/stream_1",
                "scheduled_time": "2025-04-24T14:00:00Z"
            },
            {
                "stream_id": "stream_2",
                "stream_url": "https://youtube.com/live/stream_2",
                "scheduled_time": "2025-05-08T14:00:00Z"
            }
        ]
    }