#!/usr/bin/env python3
"""
Centralized logging configuration for ACDbot.

This module provides structured logging with appropriate levels and filters
to reduce verbosity while maintaining important information.
"""

import logging
import os
import sys
from typing import Optional

class ACDbotLogger:
    """Custom logger for ACDbot with structured logging levels."""

    _instance: Optional['ACDbotLogger'] = None
    _logger: Optional[logging.Logger] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._logger is None:
            self._setup_logger()

    def _setup_logger(self):
        """Set up the logger with appropriate configuration."""
        self._logger = logging.getLogger('ACDbot')

        # Set level based on environment variable
        log_level = os.getenv('ACDBOT_LOG_LEVEL', 'INFO').upper()
        self._logger.setLevel(getattr(logging, log_level, logging.INFO))

        # Remove existing handlers
        self._logger.handlers.clear()

        # Create console handler with custom formatter
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(self._logger.level)

        # Custom formatter that matches GitHub Actions format
        formatter = ACDbotFormatter()
        handler.setFormatter(formatter)

        self._logger.addHandler(handler)
        self._logger.propagate = False

    def get_logger(self) -> logging.Logger:
        """Get the configured logger instance."""
        return self._logger


class ACDbotFormatter(logging.Formatter):
    """Custom formatter for ACDbot logs."""

    # Color codes for terminal output (GitHub Actions compatible)
    COLORS = {
        'DEBUG': '\033[90m',     # Gray
        'INFO': '\033[0m',        # Default
        'WARNING': '\033[93m',    # Yellow
        'ERROR': '\033[91m',      # Red
        'SUCCESS': '\033[92m',    # Green
        'RESET': '\033[0m'
    }

    def format(self, record):
        # Map Python logging levels to our custom format
        level_mapping = {
            'DEBUG': 'DEBUG',
            'INFO': 'INFO',
            'WARNING': 'WARN',
            'ERROR': 'ERROR',
            'CRITICAL': 'ERROR'
        }

        # Check for SUCCESS level (custom)
        if hasattr(record, 'success') and record.success:
            level = 'SUCCESS'
        else:
            level = level_mapping.get(record.levelname, record.levelname)

        # Use colors if in terminal
        if sys.stdout.isatty() or os.getenv('GITHUB_ACTIONS'):
            color = self.COLORS.get(level, self.COLORS['RESET'])
            reset = self.COLORS['RESET']
            prefix = f"{color}[{level}]{reset}"
        else:
            prefix = f"[{level}]"

        # Format the message
        return f"{prefix} {record.getMessage()}"


def get_logger() -> logging.Logger:
    """Get the configured ACDbot logger instance."""
    return ACDbotLogger().get_logger()


def log_success(message: str):
    """Log a success message with green color."""
    logger = get_logger()
    # Create a custom log record with success flag
    record = logger.makeRecord(
        logger.name,
        logging.INFO,
        "(unknown file)",
        0,
        message,
        (),
        None
    )
    record.success = True
    logger.handle(record)


# Structured logging functions for common operations
def log_resource_status(resource: str, action: str, details: Optional[str] = None):
    """Log resource operation status in a structured way."""
    logger = get_logger()
    base_msg = f"{resource}: {action}"
    if details:
        base_msg += f" - {details}"

    if action.lower() in ['created', 'updated', 'found']:
        log_success(base_msg)
    elif action.lower() in ['failed', 'error']:
        logger.error(base_msg)
    elif action.lower() in ['skipped', 'pending']:
        logger.warning(base_msg)
    else:
        logger.info(base_msg)


def log_api_call(service: str, operation: str, success: bool = True, details: Optional[str] = None):
    """Log API calls in a structured way."""
    logger = get_logger()
    status = "✓" if success else "✗"
    msg = f"{service} API: {operation} {status}"
    if details:
        msg += f" - {details}"

    if success:
        logger.debug(msg)
    else:
        logger.error(msg)


def should_log_debug() -> bool:
    """Check if debug logging is enabled."""
    return os.getenv('ACDBOT_LOG_LEVEL', 'INFO').upper() == 'DEBUG'