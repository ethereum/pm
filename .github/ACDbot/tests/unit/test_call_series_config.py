"""
Unit tests for call_series_config.py module.

Tests the centralized configuration loading functionality.
"""

from modules.call_series_config import (
    get_display_name_to_key_mapping,
    get_youtube_playlist_mapping,
    get_discord_webhook_mapping,
    get_all_call_series_keys,
    get_call_series_config,
    reload_config,
    get_autopilot_defaults,
    has_autopilot_support,
)


class TestCallSeriesConfig:
    """Test cases for call_series_config module."""

    def test_config_file_loads(self):
        """Test that the config file loads without errors."""
        reload_config()  # Force fresh load
        mapping = get_display_name_to_key_mapping()
        assert mapping is not None
        assert len(mapping) > 0

    def test_display_name_to_key_mapping_structure(self):
        """Test that display name mapping has correct structure."""
        mapping = get_display_name_to_key_mapping()

        # All values should be strings (call series keys)
        for display_name, key in mapping.items():
            assert isinstance(display_name, str), f"Display name should be string: {display_name}"
            assert isinstance(key, str), f"Key should be string: {key}"
            assert len(key) > 0, f"Key should not be empty for: {display_name}"

    def test_display_name_mapping_contains_core_series(self):
        """Test that core call series are present in mapping."""
        mapping = get_display_name_to_key_mapping()

        # Core ACD calls must be present
        assert "All Core Devs - Execution" in mapping
        assert "All Core Devs - Consensus" in mapping
        assert "All Core Devs - Testing" in mapping

        # Verify they map to correct keys
        assert mapping["All Core Devs - Execution"] == "acde"
        assert mapping["All Core Devs - Consensus"] == "acdc"
        assert mapping["All Core Devs - Testing"] == "acdt"

    def test_display_name_mapping_contains_one_off(self):
        """Test that one-off call is present in mapping."""
        mapping = get_display_name_to_key_mapping()

        assert "One-time call" in mapping
        assert mapping["One-time call"] == "one-off"

    def test_youtube_playlist_mapping_structure(self):
        """Test that YouTube playlist mapping has correct structure."""
        mapping = get_youtube_playlist_mapping()

        assert mapping is not None
        assert len(mapping) > 0

        # All keys should be strings, values should be strings or None
        for key, playlist_id in mapping.items():
            assert isinstance(key, str), f"Key should be string: {key}"
            assert playlist_id is None or isinstance(playlist_id, str), \
                f"Playlist ID should be string or None for: {key}"

    def test_youtube_playlist_mapping_contains_core_playlists(self):
        """Test that core playlists are present."""
        mapping = get_youtube_playlist_mapping()

        # ACD playlists must be present and valid
        assert "acde" in mapping
        assert "acdc" in mapping
        assert "acdt" in mapping
        assert "allcoredevs" in mapping  # From additional_playlists

        # Verify they have valid playlist IDs
        assert mapping["acde"].startswith("PL")
        assert mapping["acdc"].startswith("PL")
        assert mapping["acdt"].startswith("PL")
        assert mapping["allcoredevs"].startswith("PL")

    def test_youtube_playlist_mapping_allows_none(self):
        """Test that some series can have None playlist (not uploaded to YouTube)."""
        mapping = get_youtube_playlist_mapping()

        # At least some series should have None (managed externally or no YouTube)
        none_playlists = [k for k, v in mapping.items() if v is None]
        assert len(none_playlists) > 0, "Expected some series to have None playlist"

    def test_discord_webhook_mapping_structure(self):
        """Test that Discord webhook mapping has correct structure."""
        mapping = get_discord_webhook_mapping()

        assert mapping is not None

        # All values should be environment variable names (strings)
        for key, env_var in mapping.items():
            assert isinstance(key, str), f"Key should be string: {key}"
            assert isinstance(env_var, str), f"Env var should be string for: {key}"
            assert len(env_var) > 0, f"Env var should not be empty for: {key}"

    def test_discord_webhook_mapping_acd_series(self):
        """Test that ACD series have Discord webhooks configured."""
        mapping = get_discord_webhook_mapping()

        # ACD calls should have webhooks
        assert "acde" in mapping
        assert "acdc" in mapping
        assert "acdt" in mapping

        # They should all use the same webhook env var
        assert mapping["acde"] == "DISCORD_ACD_WEBHOOK"
        assert mapping["acdc"] == "DISCORD_ACD_WEBHOOK"
        assert mapping["acdt"] == "DISCORD_ACD_WEBHOOK"

    def test_get_all_call_series_keys(self):
        """Test getting all call series keys."""
        keys = get_all_call_series_keys()

        assert keys is not None
        assert len(keys) > 0
        assert isinstance(keys, list)

        # Core series should be present
        assert "acde" in keys
        assert "acdc" in keys
        assert "acdt" in keys
        assert "one-off" in keys

    def test_get_call_series_config_existing(self):
        """Test getting config for existing series."""
        config = get_call_series_config("acde")

        assert config is not None
        assert "display_name" in config
        assert config["display_name"] == "All Core Devs - Execution"
        assert "youtube_playlist_id" in config
        assert "discord_webhook_env" in config

    def test_get_call_series_config_nonexistent(self):
        """Test getting config for non-existent series."""
        config = get_call_series_config("nonexistent_series")

        assert config is None

    def test_mappings_are_consistent(self):
        """Test that all mappings are consistent with each other."""
        display_mapping = get_display_name_to_key_mapping()
        all_keys = get_all_call_series_keys()
        youtube_mapping = get_youtube_playlist_mapping()

        # All keys from display mapping should be in all_keys
        for key in display_mapping.values():
            assert key in all_keys, f"Key {key} from display mapping not in all_keys"

        # All keys in all_keys should have a display name
        display_keys = set(display_mapping.values())
        for key in all_keys:
            assert key in display_keys, f"Key {key} has no display name mapping"

        # All call series keys should be in youtube mapping (even if None)
        for key in all_keys:
            assert key in youtube_mapping, f"Key {key} not in youtube mapping"

    def test_display_names_are_unique(self):
        """Test that all display names are unique."""
        mapping = get_display_name_to_key_mapping()

        display_names = list(mapping.keys())
        assert len(display_names) == len(set(display_names)), \
            "Display names should be unique"

    def test_keys_are_unique(self):
        """Test that all call series keys are unique."""
        keys = get_all_call_series_keys()

        assert len(keys) == len(set(keys)), "Call series keys should be unique"

    def test_keys_are_lowercase(self):
        """Test that all call series keys are lowercase (convention)."""
        keys = get_all_call_series_keys()

        for key in keys:
            assert key == key.lower(), f"Key should be lowercase: {key}"


class TestConfigIntegration:
    """Integration tests verifying config works with dependent modules."""

    def test_form_parser_uses_config(self):
        """Test that FormParser correctly uses the config."""
        from modules.form_parser import FormParser

        parser = FormParser()

        # The mapping should come from config
        assert parser.call_series_mapping == get_display_name_to_key_mapping()

    def test_youtube_utils_uses_config(self):
        """Test that youtube_utils correctly uses the config."""
        from modules import youtube_utils

        # The mapping should come from config
        assert youtube_utils.PLAYLIST_MAPPING == get_youtube_playlist_mapping()

    def test_discord_notify_uses_config(self):
        """Test that discord_notify correctly uses the config."""
        from modules import discord_notify

        # The internal mapping should match config
        assert discord_notify._WEBHOOK_ENV_MAPPING == get_discord_webhook_mapping()


class TestAutopilotConfig:
    """Test cases for autopilot configuration."""

    def test_get_autopilot_defaults_for_acde(self):
        """Test that ACDE has autopilot defaults."""
        defaults = get_autopilot_defaults("acde")

        assert defaults is not None
        assert "duration" in defaults
        assert "occurrence_rate" in defaults
        assert "need_youtube_streams" in defaults
        assert "display_zoom_link_in_invite" in defaults
        assert "skip_zoom_creation" in defaults

    def test_get_autopilot_defaults_for_acdc(self):
        """Test that ACDC has correct autopilot defaults."""
        defaults = get_autopilot_defaults("acdc")

        assert defaults is not None
        assert defaults["duration"] == 90
        assert defaults["occurrence_rate"] == "bi-weekly"
        assert defaults["need_youtube_streams"] is True

    def test_get_autopilot_defaults_for_one_off(self):
        """Test that one-off calls have no autopilot defaults."""
        defaults = get_autopilot_defaults("one-off")

        assert defaults is None

    def test_has_autopilot_support(self):
        """Test autopilot support checking."""
        assert has_autopilot_support("acde") is True
        assert has_autopilot_support("acdc") is True
        assert has_autopilot_support("one-off") is False
        assert has_autopilot_support("nonexistent") is False

    def test_autopilot_defaults_structure(self):
        """Test that autopilot defaults have correct structure."""
        defaults = get_autopilot_defaults("acde")

        assert defaults is not None
        assert isinstance(defaults.get("duration"), int)
        assert defaults["duration"] in [30, 60, 90, 120, 180]
        assert defaults["occurrence_rate"] in ["weekly", "bi-weekly", "monthly", "other"]
        assert isinstance(defaults.get("need_youtube_streams"), bool)
        assert isinstance(defaults.get("display_zoom_link_in_invite"), bool)
        assert isinstance(defaults.get("skip_zoom_creation"), bool)

    def test_all_series_with_defaults_have_complete_config(self):
        """Test that all series with autopilot defaults have all required fields."""
        required_fields = [
            "duration",
            "occurrence_rate",
            "need_youtube_streams",
            "display_zoom_link_in_invite",
            "skip_zoom_creation"
        ]

        for key in get_all_call_series_keys():
            defaults = get_autopilot_defaults(key)
            if defaults is not None:
                for field in required_fields:
                    assert field in defaults, f"Series {key} missing field: {field}"
