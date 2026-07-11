"""
Call Series Configuration Loader

Loads call series configuration from the centralized YAML config file.
This module provides a single source of truth for all call series data.
"""

import os
import yaml
from typing import Dict, Optional

# Path to the config file (relative to this module)
CONFIG_FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "call_series_config.yml"
)

_config_cache = None


def _load_config() -> dict:
    """Load and cache the configuration file."""
    global _config_cache
    if _config_cache is None:
        with open(CONFIG_FILE_PATH, 'r') as f:
            _config_cache = yaml.safe_load(f)
    return _config_cache


def get_display_name_to_key_mapping() -> Dict[str, str]:
    """
    Get mapping from display names to call series keys.
    Used by form_parser.py to convert dropdown selections to internal keys.

    Returns:
        Dict mapping display name -> call series key
        e.g., {"All Core Devs - Execution": "acde", ...}
    """
    config = _load_config()
    return {
        series_config["display_name"]: series_key
        for series_key, series_config in config.get("call_series", {}).items()
    }


def get_youtube_playlist_mapping() -> Dict[str, Optional[str]]:
    """
    Get mapping from call series keys to YouTube playlist IDs.
    Used by youtube_utils.py for video playlist assignment.

    Returns:
        Dict mapping call series key -> playlist ID (or None)
        e.g., {"acde": "PLJqWcTqh_zKFFK2Q3eK2hgbGijW_jf-Q5", ...}
    """
    config = _load_config()
    mapping = {}

    # Add call series playlists
    for series_key, series_config in config.get("call_series", {}).items():
        playlist_id = series_config.get("youtube_playlist_id")
        if playlist_id is not None or series_key in config.get("call_series", {}):
            mapping[series_key] = playlist_id

    # Add additional playlists (like allcoredevs)
    for key, playlist_id in config.get("additional_playlists", {}).items():
        mapping[key] = playlist_id

    return mapping


def get_discord_webhook_mapping() -> Dict[str, Optional[str]]:
    """
    Get mapping from call series keys to Discord webhook environment variable names.
    Used by discord_notify.py to determine which webhook to use.

    Returns:
        Dict mapping call series key -> env var name (or None)
        e.g., {"acde": "DISCORD_ACD_WEBHOOK", ...}
    """
    config = _load_config()
    return {
        series_key: series_config.get("discord_webhook_env")
        for series_key, series_config in config.get("call_series", {}).items()
        if series_config.get("discord_webhook_env") is not None
    }


def get_all_call_series_keys() -> list:
    """
    Get list of all call series keys.

    Returns:
        List of call series keys, e.g., ["acdc", "acde", "acdt", ...]
    """
    config = _load_config()
    return list(config.get("call_series", {}).keys())


def get_call_series_config(series_key: str) -> Optional[dict]:
    """
    Get full configuration for a specific call series.

    Args:
        series_key: The call series key (e.g., "acde")

    Returns:
        Dict with display_name, youtube_playlist_id, discord_webhook_env
        or None if not found
    """
    config = _load_config()
    return config.get("call_series", {}).get(series_key)


def reload_config():
    """Force reload of configuration (useful for testing)."""
    global _config_cache
    _config_cache = None
    _load_config()


def get_autopilot_defaults(series_key: str) -> Optional[dict]:
    """
    Get autopilot default configuration for a specific call series.

    Args:
        series_key: The call series key (e.g., "acde")

    Returns:
        Dict with autopilot defaults (duration, occurrence_rate, need_youtube_streams, etc.)
        or None if no autopilot defaults are configured for this series
    """
    config = _load_config()
    series_config = config.get("call_series", {}).get(series_key)
    if series_config:
        return series_config.get("autopilot_defaults")
    return None


def has_autopilot_support(series_key: str) -> bool:
    """
    Check if a call series has autopilot defaults configured.

    Args:
        series_key: The call series key (e.g., "acde")

    Returns:
        True if the series has autopilot_defaults configured, False otherwise
    """
    return get_autopilot_defaults(series_key) is not None


def get_default_autopilot_settings() -> dict:
    """
    Get the default autopilot settings used when a call series
    doesn't have specific configuration.

    Returns:
        Dict with default autopilot settings
    """
    config = _load_config()
    return config.get("default_autopilot_settings", {})


def get_one_off_autopilot_settings() -> dict:
    """
    Get the autopilot settings for one-off calls.

    Returns:
        Dict with one-off autopilot settings
    """
    config = _load_config()
    return config.get("one_off_autopilot_settings", {})
