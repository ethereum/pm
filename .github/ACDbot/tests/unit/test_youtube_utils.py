"""
Unit tests for youtube_utils.py module.

Tests the YouTube integration functionality including:
- Playlist mapping logic
- Recurring stream date calculations
- Error handling
"""

import pytest
from unittest.mock import patch, MagicMock, Mock
from datetime import datetime, timedelta
import calendar
import pytz
import os

# Set up required environment variables for testing
os.environ.setdefault("YOUTUBE_REFRESH_TOKEN", "test_refresh_token")
os.environ.setdefault("GOOGLE_CLIENT_ID", "test_client_id")
os.environ.setdefault("GOOGLE_CLIENT_SECRET", "test_client_secret")

from modules import youtube_utils


class TestYouTubeUtilsModule:
    """Test cases for youtube_utils.py module."""

    def test_add_video_to_appropriate_playlist_specific_series(self):
        """Test adding video to specific playlist based on call series."""
        with patch('modules.youtube_utils.add_video_to_playlist') as mock_add_video:
            mock_add_video.return_value = {"id": "test_item_id"}

            result = youtube_utils.add_video_to_appropriate_playlist("test_video_id", "acde")

            # Should add to both acde and allcoredevs playlists
            expected_calls = [
                (("test_video_id", "PLJqWcTqh_zKFFK2Q3eK2hgbGijW_jf-Q5"),),  # acde
                (("test_video_id", "PLJqWcTqh_zKHU6gjnA6ZcFPU5Pr0xT0io"),)   # allcoredevs
            ]
            assert mock_add_video.call_args_list == expected_calls
            assert len(result) == 2

    def test_add_video_to_appropriate_playlist_acd_series(self):
        """Test adding video to both specific and general ACD playlists."""
        with patch('modules.youtube_utils.add_video_to_playlist') as mock_add_video:
            mock_add_video.return_value = {"id": "test_item_id"}

            result = youtube_utils.add_video_to_appropriate_playlist("test_video_id", "acde")

            # Should add to both acde and allcoredevs playlists
            expected_calls = [
                (("test_video_id", "PLJqWcTqh_zKFFK2Q3eK2hgbGijW_jf-Q5"),),  # acde
                (("test_video_id", "PLJqWcTqh_zKHU6gjnA6ZcFPU5Pr0xT0io"),)   # allcoredevs
            ]
            assert mock_add_video.call_args_list == expected_calls
            assert len(result) == 2

    def test_add_video_to_appropriate_playlist_unknown_series(self):
        """Test adding video for unknown call series."""
        with patch('modules.youtube_utils.add_video_to_playlist') as mock_add_video:
            result = youtube_utils.add_video_to_appropriate_playlist("test_video_id", "unknown_series")

            # Should not add to any playlist
            mock_add_video.assert_not_called()
            assert result is None

    def test_get_youtube_service_missing_env_vars(self):
        """Test YouTube service creation with missing environment variables."""
        with patch.dict('os.environ', {}, clear=True):
            with pytest.raises(ValueError, match="Missing required environment variables"):
                youtube_utils.get_youtube_service()

    def test_create_recurring_streams_weekly(self):
        """Test creating weekly recurring streams."""
        with patch('modules.youtube_utils.create_youtube_stream') as mock_create_stream:
            mock_create_stream.return_value = {"id": "test_stream_id"}

            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time="2025-01-01T10:00:00Z",
                occurrence_rate="weekly",
                num_events=3
            )

            assert len(result) == 3
            assert mock_create_stream.call_count == 3

            # Verify time calculations - check positional arguments
            calls = mock_create_stream.call_args_list
            assert calls[0][0][2] == "2025-01-01T10:00:00.000Z"  # start_time (3rd positional arg)
            assert calls[1][0][2] == "2025-01-08T10:00:00.000Z"  # +7 days
            assert calls[2][0][2] == "2025-01-15T10:00:00.000Z"  # +14 days

    def test_create_recurring_streams_bi_weekly(self):
        """Test creating bi-weekly recurring streams."""
        with patch('modules.youtube_utils.create_youtube_stream') as mock_create_stream:
            mock_create_stream.return_value = {"id": "test_stream_id"}

            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time="2025-01-01T10:00:00Z",
                occurrence_rate="bi-weekly",
                num_events=2
            )

            assert len(result) == 2
            assert mock_create_stream.call_count == 2

            # Verify time calculations - check positional arguments
            calls = mock_create_stream.call_args_list
            assert calls[0][0][2] == "2025-01-01T10:00:00.000Z"  # start_time (3rd positional arg)
            assert calls[1][0][2] == "2025-01-15T10:00:00.000Z"  # +14 days

    def test_create_recurring_streams_monthly(self):
        """Test creating monthly recurring streams."""
        with patch('modules.youtube_utils.create_youtube_stream') as mock_create_stream:
            mock_create_stream.return_value = {"id": "test_stream_id"}

            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time="2025-01-01T10:00:00Z",  # Wednesday
                occurrence_rate="monthly",
                num_events=2
            )

            assert len(result) == 2
            assert mock_create_stream.call_count == 2

            # Verify time calculations (should be same weekday in next month)
            calls = mock_create_stream.call_args_list
            assert calls[0][0][2] == "2025-01-01T10:00:00.000Z"  # start_time (3rd positional arg)
            # Second call should be same weekday in February
            assert calls[1][0][2] == "2025-02-05T10:00:00.000Z"  # First Wednesday of February

    def test_create_recurring_streams_monthly_last_weekday(self):
        """Test creating monthly streams for last weekday of month."""
        with patch('modules.youtube_utils.create_youtube_stream') as mock_create_stream:
            mock_create_stream.return_value = {"id": "test_stream_id"}

            # Use a date that's the last Wednesday of January
            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time="2025-01-29T10:00:00Z",  # Last Wednesday of January
                occurrence_rate="monthly",
                num_events=2
            )

            assert len(result) == 2
            assert mock_create_stream.call_count == 2

            # Verify time calculations
            calls = mock_create_stream.call_args_list
            assert calls[0][0][2] == "2025-01-29T10:00:00.000Z"  # start_time (3rd positional arg)
            # Should be last Wednesday of February
            assert calls[1][0][2] == "2025-02-26T10:00:00.000Z"

    def test_create_recurring_streams_invalid_rate(self):
        """Test creating streams with invalid occurrence rate."""
        with patch('modules.youtube_utils.create_youtube_stream') as mock_create_stream:
            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time="2025-01-01T10:00:00Z",
                occurrence_rate="invalid",
                num_events=2
            )

            # Should create all requested streams even with invalid rate
            assert len(result) == 2
            assert mock_create_stream.call_count == 2

    def test_create_recurring_streams_string_start_time(self):
        """Test creating streams with string start time."""
        with patch('modules.youtube_utils.create_youtube_stream') as mock_create_stream:
            mock_create_stream.return_value = {"id": "test_stream_id"}

            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time="2025-01-01T10:00:00Z",
                occurrence_rate="weekly",
                num_events=2
            )

            assert len(result) == 2
            mock_create_stream.assert_called()

    def test_create_recurring_streams_datetime_start_time(self):
        """Test creating streams with datetime start time."""
        with patch('modules.youtube_utils.create_youtube_stream') as mock_create_stream:
            mock_create_stream.return_value = {"id": "test_stream_id"}

            start_time = datetime(2025, 1, 1, 10, 0, 0, tzinfo=pytz.UTC)

            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time=start_time,
                occurrence_rate="weekly",
                num_events=2
            )

            assert len(result) == 2
            mock_create_stream.assert_called()

    def test_playlist_mapping_completeness(self):
        """Test that all expected playlists are defined."""
        expected_playlists = [
            "allcoredevs", "acde", "acdc", "acdt", "l2interop", "rpcstandards",
            "stateless", "epbs", "maxeb", "focil", "ethsimulate", "ethproofs", "beam",
            "pqinterop", "peerdas", "evmmax", "rollcall", "resourcepricing",
            "portal", "protocolresearch"
        ]

        for playlist in expected_playlists:
            assert playlist in youtube_utils.PLAYLIST_MAPPING
            # Only check for playlist ID format if the playlist has a mapping (not None)
            if youtube_utils.PLAYLIST_MAPPING[playlist] is not None:
                assert youtube_utils.PLAYLIST_MAPPING[playlist].startswith("PL")

    def test_monthly_recurrence_edge_cases(self):
        """Test monthly recurrence calculations for edge cases."""
        with patch('modules.youtube_utils.create_youtube_stream') as mock_create_stream:
            mock_create_stream.return_value = {"id": "test_stream_id"}

            # Test first day of month
            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time="2025-01-01T10:00:00Z",  # First Wednesday
                occurrence_rate="monthly",
                num_events=2
            )

            assert len(result) == 2

            # Test last day of month
            result = youtube_utils.create_recurring_streams(
                title="Test Meeting",
                description="Test Description",
                start_time="2025-01-31T10:00:00Z",  # Last Friday
                occurrence_rate="monthly",
                num_events=2
            )

            assert len(result) == 2