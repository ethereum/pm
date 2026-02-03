#!/usr/bin/env python3
"""
Shared utilities for the asset pipeline.
"""

from pathlib import Path

# Base paths relative to this module
SCRIPT_DIR = Path(__file__).parent
ARTIFACTS_DIR = SCRIPT_DIR.parent.parent / "artifacts"

# Maximum meeting number for validation (reasonable upper bound)
MAX_MEETING_NUMBER = 999

# Model pricing per million tokens (input, output)
MODEL_PRICING = {
    "claude-opus-4-5-20251101": (15.00, 75.00),
    "claude-sonnet-4-5-20250929": (3.00, 15.00),
    "claude-sonnet-4-20250514": (3.00, 15.00),
    "claude-3-5-sonnet-20241022": (3.00, 15.00),
    "claude-haiku-3-5-20241022": (0.80, 4.00),
}


def find_call_directory(call: str, number: int, raise_on_missing: bool = True) -> Path | None:
    """
    Find the directory for a given call type and number.

    Args:
        call: Call type (e.g., 'acde', 'acdc', 'acdt')
        number: Call number (e.g., 226)
        raise_on_missing: If True, raise FileNotFoundError when not found.
                         If False, return None.

    Returns:
        Path to the call directory, or None if not found and raise_on_missing=False

    Raises:
        FileNotFoundError: If directory not found and raise_on_missing=True
    """
    call_dir = ARTIFACTS_DIR / call
    if not call_dir.exists():
        if raise_on_missing:
            raise FileNotFoundError(f"Call type directory not found: {call_dir}")
        return None

    # Find directory ending with _{number} (check both zero-padded and non-padded)
    padded = str(number).zfill(3)
    for d in call_dir.iterdir():
        if d.is_dir() and (d.name.endswith(f"_{padded}") or d.name.endswith(f"_{number}")):
            return d

    if raise_on_missing:
        raise FileNotFoundError(f"No directory found for {call} #{number}")
    return None


def calculate_cost(model: str, usage: dict) -> float:
    """
    Calculate cost in USD based on model and token usage.

    Args:
        model: Claude model name
        usage: Dict with 'input_tokens' and 'output_tokens' keys

    Returns:
        Cost in USD
    """
    input_price, output_price = MODEL_PRICING.get(model, (0, 0))
    input_cost = (usage["input_tokens"] / 1_000_000) * input_price
    output_cost = (usage["output_tokens"] / 1_000_000) * output_price
    return input_cost + output_cost
