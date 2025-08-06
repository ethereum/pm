"""
Unit tests for mapping_utils.py module.
"""

import pytest
from modules.mapping_utils import (
    find_meeting_by_id,
    get_effective_meeting_id,
    find_meeting_by_issue_number,
    find_call_series_by_meeting_id
)


class TestMappingUtils:
    """Test cases for mapping utility functions."""

    def test_find_meeting_by_id_recurring_series_root(self, sample_mapping):
        """Test finding meeting in recurring series at root level."""
        result = find_meeting_by_id("88269836469", sample_mapping)
        assert result is not None
        assert result["call_series"] == "acde"
        assert result["meeting_id"] == "88269836469"

    def test_find_meeting_by_id_recurring_series_occurrence_override(self, sample_mapping):
        """Test finding meeting in recurring series with occurrence override."""
        result = find_meeting_by_id("86109593250", sample_mapping)
        assert result is not None
        # Should return the occurrence data, not the series data
        assert result["meeting_id"] == "86109593250"
        assert result["issue_number"] == 1463

    def test_find_meeting_by_id_one_off(self, sample_mapping):
        """Test finding one-off meeting."""
        result = find_meeting_by_id("89880194464", sample_mapping)
        assert result is not None
        assert result["meeting_id"] == "89880194464"
        assert result["issue_number"] == 1465

    def test_find_meeting_by_id_one_off_second(self, sample_mapping):
        """Test finding second one-off meeting."""
        result = find_meeting_by_id("99999999999", sample_mapping)
        assert result is not None
        assert result["meeting_id"] == "99999999999"
        assert result["issue_number"] == 1466

    def test_find_meeting_by_id_not_found(self, sample_mapping):
        """Test finding non-existent meeting."""
        result = find_meeting_by_id("nonexistent", sample_mapping)
        assert result is None

    def test_find_meeting_by_id_empty_mapping(self):
        """Test finding meeting in empty mapping."""
        result = find_meeting_by_id("any_id", {})
        assert result is None

    def test_get_effective_meeting_id_root_level(self, sample_mapping):
        """Test getting effective meeting ID from root level."""
        result = get_effective_meeting_id("acde", 1462, sample_mapping)
        assert result == "88269836469"

    def test_get_effective_meeting_id_occurrence_override(self, sample_mapping):
        """Test getting effective meeting ID with occurrence override."""
        result = get_effective_meeting_id("acde", 1463, sample_mapping)
        assert result == "86109593250"

    def test_get_effective_meeting_id_one_off(self, sample_mapping):
        """Test getting effective meeting ID for one-off meeting."""
        result = get_effective_meeting_id("one-off", 1465, sample_mapping)
        assert result == "89880194464"

    def test_get_effective_meeting_id_series_not_found(self, sample_mapping):
        """Test getting effective meeting ID for non-existent series."""
        result = get_effective_meeting_id("nonexistent", 1462, sample_mapping)
        assert result is None

    def test_get_effective_meeting_id_occurrence_not_found(self, sample_mapping):
        """Test getting effective meeting ID for non-existent occurrence."""
        result = get_effective_meeting_id("acde", 9999, sample_mapping)
        assert result is None

    def test_get_effective_meeting_id_no_root_meeting_id(self, sample_mapping):
        """Test getting effective meeting ID when no root meeting_id exists."""
        # Create a modified mapping without root meeting_id
        modified_mapping = sample_mapping.copy()
        del modified_mapping["acde"]["meeting_id"]

        result = get_effective_meeting_id("acde", 1462, modified_mapping)
        assert result is None

    def test_find_meeting_by_issue_number_recurring_series(self, sample_mapping):
        """Test finding meeting by issue number in recurring series."""
        result = find_meeting_by_issue_number(1462, sample_mapping)
        assert result is not None
        # Should return the occurrence data
        assert result["issue_number"] == 1462
        assert result["occurrence_number"] == 1

    def test_find_meeting_by_issue_number_recurring_series_second(self, sample_mapping):
        """Test finding second occurrence in recurring series."""
        result = find_meeting_by_issue_number(1463, sample_mapping)
        assert result is not None
        # Should return the occurrence data
        assert result["issue_number"] == 1463
        assert result["occurrence_number"] == 2
        assert result["meeting_id"] == "86109593250"

    def test_find_meeting_by_issue_number_one_off(self, sample_mapping):
        """Test finding one-off meeting by issue number."""
        result = find_meeting_by_issue_number(1465, sample_mapping)
        assert result is not None
        assert result["meeting_id"] == "89880194464"
        assert result["issue_number"] == 1465

    def test_find_meeting_by_issue_number_not_found(self, sample_mapping):
        """Test finding non-existent issue number."""
        result = find_meeting_by_issue_number(9999, sample_mapping)
        assert result is None

    def test_find_meeting_by_issue_number_empty_mapping(self):
        """Test finding issue number in empty mapping."""
        result = find_meeting_by_issue_number(1462, {})
        assert result is None

    def test_hybrid_meeting_id_logic_complex(self, sample_mapping):
        """Test complex hybrid meeting ID logic scenarios."""
        # Test that we can find meetings at both root and occurrence levels
        root_result = find_meeting_by_id("88269836469", sample_mapping)
        occurrence_result = find_meeting_by_id("86109593250", sample_mapping)

        assert root_result is not None
        assert occurrence_result is not None

        # Root result should be the series data
        assert root_result["call_series"] == "acde"

        # Occurrence result should be the occurrence data
        assert occurrence_result["meeting_id"] == "86109593250"
        assert occurrence_result["issue_number"] == 1463

    def test_edge_cases_malformed_mapping(self):
        """Test edge cases with malformed mapping data."""
        # Test with missing occurrences list
        malformed_mapping = {
            "acde": {
                "call_series": "acde",
                "meeting_id": "123456789"
                # Missing occurrences list
            }
        }

        result = find_meeting_by_id("123456789", malformed_mapping)
        assert result is not None
        assert result["call_series"] == "acde"

    @pytest.mark.mapping
    def test_mapping_structure_validation(self, sample_mapping):
        """Test that mapping structure is properly validated."""
        # Test valid mapping
        assert find_meeting_by_id("88269836469", sample_mapping) is not None

        # Test invalid mapping
        invalid_mapping = {"invalid": "structure"}
        assert find_meeting_by_id("any_id", invalid_mapping) is None

    def test_find_call_series_by_meeting_id_recurring_series_root(self, sample_mapping):
        """Test finding call series for recurring series root meeting ID."""
        result = find_call_series_by_meeting_id("88269836469", 1462, sample_mapping)
        assert result == "acde"

    def test_find_call_series_by_meeting_id_recurring_series_occurrence_override(self, sample_mapping):
        """Test finding call series for recurring series with occurrence override."""
        result = find_call_series_by_meeting_id("86109593250", 1463, sample_mapping)
        assert result == "acde"

    def test_find_call_series_by_meeting_id_one_off(self, sample_mapping):
        """Test finding call series for one-off meeting."""
        result = find_call_series_by_meeting_id("89880194464", 1465, sample_mapping)
        assert result == "one-off"

    def test_find_call_series_by_meeting_id_one_off_second(self, sample_mapping):
        """Test finding call series for second one-off meeting."""
        result = find_call_series_by_meeting_id("99999999999", 1466, sample_mapping)
        assert result == "one-off"

    def test_find_call_series_by_meeting_id_not_found(self, sample_mapping):
        """Test finding call series for non-existent meeting."""
        result = find_call_series_by_meeting_id("nonexistent", 9999, sample_mapping)
        assert result is None

    def test_find_call_series_by_meeting_id_wrong_issue_number(self, sample_mapping):
        """Test finding call series with wrong issue number."""
        result = find_call_series_by_meeting_id("88269836469", 9999, sample_mapping)
        assert result is None

    def test_find_call_series_by_meeting_id_empty_mapping(self):
        """Test finding call series in empty mapping."""
        result = find_call_series_by_meeting_id("any_id", 1462, {})
        assert result is None