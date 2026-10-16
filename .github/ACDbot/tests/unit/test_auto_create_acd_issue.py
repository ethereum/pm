"""Regression tests for ACD issue lookup failures."""

import importlib.util
import io
import sys
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock

import pytest


@pytest.fixture
def issue_creator():
    script = Path(__file__).resolve().parents[3] / "scripts" / "auto-create-acd-issue.py"
    spec = importlib.util.spec_from_file_location("auto_create_acd_issue", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fail_github_lookup(monkeypatch, issue_creator):
    def unavailable(*_args, **_kwargs):
        raise urllib.error.HTTPError(
            "https://api.github.com/repos/ethereum/pm/issues",
            503,
            "Service Unavailable",
            {},
            io.BytesIO(b"temporary failure"),
        )

    monkeypatch.setattr(issue_creator.urllib.request, "urlopen", unavailable)


@pytest.mark.parametrize("series", ["acde", "acdc"])
def test_recent_issue_lookup_failure_is_not_an_empty_series(monkeypatch, issue_creator, series):
    fail_github_lookup(monkeypatch, issue_creator)

    with pytest.raises(RuntimeError, match="Could not fetch issues"):
        issue_creator.get_recent_issues(series)


def test_recent_issue_lookup_failure_makes_run_fail(monkeypatch, issue_creator):
    fail_github_lookup(monkeypatch, issue_creator)
    monkeypatch.setattr(sys, "argv", ["auto-create-acd-issue.py", "--type", "acde"])
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)

    with pytest.raises(SystemExit) as exc:
        issue_creator.main()

    assert exc.value.code == 1


def test_duplicate_lookup_failure_does_not_create_issue(monkeypatch, issue_creator):
    today = datetime.now(timezone.utc).date()
    last_thursday = today - timedelta(days=(today.weekday() - 3) % 7)
    monkeypatch.setattr(
        issue_creator,
        "get_recent_issues",
        lambda _series: [{
            "call_number": 247,
            "title": f"All Core Devs - Execution (ACDE) #247, {last_thursday:%B %d, %Y}",
            "state": "closed",
            "body": "",
        }],
    )
    fail_github_lookup(monkeypatch, issue_creator)
    create_issue = Mock()
    monkeypatch.setattr(issue_creator, "create_issue", create_issue)

    with pytest.raises(RuntimeError, match="Could not check whether"):
        issue_creator.process_series("acde")

    create_issue.assert_not_called()


def test_duplicate_lookup_failure_on_later_page_is_not_a_miss(monkeypatch, issue_creator):
    pages = []

    def list_issues(endpoint, **_kwargs):
        pages.append(endpoint)
        assert len(pages) <= 2
        if endpoint.endswith("&page=1"):
            return [{"title": "Unrelated meeting"}] * 100
        return None

    monkeypatch.setattr(issue_creator, "api_call", list_issues)

    with pytest.raises(RuntimeError, match="Could not check whether"):
        issue_creator.check_issue_exists(248, "acde")

    assert len(pages) == 2


@pytest.mark.parametrize("response", [{}, {"items": {}}])
def test_malformed_issue_list_is_not_treated_as_empty(monkeypatch, issue_creator, response):
    monkeypatch.setattr(issue_creator, "api_call", lambda *_args, **_kwargs: response)

    with pytest.raises(RuntimeError, match="Could not fetch issues"):
        issue_creator.get_recent_issues("acde")

    with pytest.raises(RuntimeError, match="Could not check whether"):
        issue_creator.check_issue_exists(248, "acde")


def test_empty_lookup_responses_remain_valid(monkeypatch, issue_creator):
    monkeypatch.setattr(issue_creator, "api_call", lambda *_args, **_kwargs: [])

    assert issue_creator.get_recent_issues("acde") == []
    assert issue_creator.check_issue_exists(248, "acde") is False


def test_items_list_response_remains_supported(monkeypatch, issue_creator):
    monkeypatch.setattr(
        issue_creator, "api_call", lambda *_args, **_kwargs: {"items": []}
    )

    assert issue_creator.get_recent_issues("acde") == []
    assert issue_creator.check_issue_exists(248, "acde") is False


def test_existing_issue_is_still_detected(monkeypatch, issue_creator):
    monkeypatch.setattr(
        issue_creator,
        "api_call",
        lambda *_args, **_kwargs: [
            {"title": "All Core Devs - Execution (ACDE) #248, October 22, 2026"}
        ],
    )

    assert issue_creator.check_issue_exists(248, "acde") is True


def test_one_series_failure_preserves_other_created_issue(monkeypatch, issue_creator, tmp_path):
    def process_series(series, dry_run=False):
        if series == "acde":
            raise RuntimeError("GitHub lookup failed")
        return 1234

    output = tmp_path / "github_output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    monkeypatch.setattr(sys, "argv", ["auto-create-acd-issue.py"])
    monkeypatch.setattr(issue_creator, "process_series", process_series)

    with pytest.raises(SystemExit) as exc:
        issue_creator.main()

    assert exc.value.code == 1
    assert output.read_text() == "created_issues=1234\n"
