"""Meeting identity helpers for the asset pipeline."""

from __future__ import annotations

import re


MAX_PUBLIC_CALL_NUMBER = 999

PUBLIC_CALL_NUMBER_PATTERNS = (
    r"#\s*0*(\d+)\b",
    r"\b(?:Meeting|Call)\s+0*(\d+)\b",
    r"\bBreakout(?:\s+Room)?\s+0*(\d+)\b",
)

SERIES_CALL_NUMBER_PATTERNS = (
    r"\b(?:ACDE|ACDC|ACDT|Execution|Consensus|Testing)\s+0*(\d+)\b",
)


def parse_public_call_number(value) -> int | None:
    """Parse and validate a public call number."""
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None

    if 0 <= number <= MAX_PUBLIC_CALL_NUMBER:
        return number
    return None


def extract_public_call_number(text: str | None, include_series_patterns: bool = False) -> int | None:
    """Extract an explicit public call number from human-readable meeting text."""
    if not text:
        return None

    patterns = list(PUBLIC_CALL_NUMBER_PATTERNS)
    if include_series_patterns:
        patterns.extend(SERIES_CALL_NUMBER_PATTERNS)

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue

        number = parse_public_call_number(match.group(1))
        if number is not None:
            return number

    return None


def get_occurrence_call_number(occurrence: dict | None) -> int | None:
    """Return the public call number for a mapped occurrence."""
    if not occurrence:
        return None

    title_number = extract_public_call_number(
        occurrence.get("issue_title", ""),
        include_series_patterns=True,
    )
    if title_number is not None:
        return title_number

    return parse_public_call_number(occurrence.get("occurrence_number"))
