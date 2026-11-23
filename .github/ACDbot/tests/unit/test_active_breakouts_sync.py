"""Issue-fetch errors must not rewrite the breakout table."""

import importlib.util
import io
import json
from pathlib import Path
from urllib.error import HTTPError, URLError

import pytest


@pytest.fixture
def tracker():
    source = Path(__file__).resolve().parents[3] / "sync" / "update_active_breakouts.py"
    spec = importlib.util.spec_from_file_location("active_breakouts_sync", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def table(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    config = tmp_path / ".github" / "ACDbot" / "call_series_config.yml"
    config.parent.mkdir(parents=True)
    config.write_text(
        'call_series:\n  focil:\n    display_name: "FOCIL Breakout"\n',
        encoding="utf-8",
    )
    output = tmp_path / "Breakout-Room-Meetings" / "active-breakout-series.md"
    output.parent.mkdir()
    output.write_text(
        "*Last updated: fixture*\n\n"
        "| Call Series | Facilitator | Latest | Issue |\n"
        "|-------------|-------------|--------|-------|\n"
        "| Existing series | facilitator | 2000-01-01 | existing |\n\n"
        "## Inactive Series\n",
        encoding="utf-8",
    )
    return output


def response(issues):
    return io.BytesIO(json.dumps(issues).encode("utf-8"))


def issue(tracker, number):
    date = tracker.datetime.utcnow().strftime("%Y-%m-%d")
    return {
        "title": f"FOCIL Breakout #{number}, {date}",
        "user": {"login": "facilitator"},
        "html_url": f"https://example.invalid/issues/{number}",
    }


@pytest.mark.parametrize("failed_page", [1, 2])
@pytest.mark.parametrize("failure", ["http", "transport"])
def test_fetch_failure_preserves_table(tracker, table, monkeypatch, failed_page, failure):
    before = table.read_bytes()
    calls = []
    error = (
        HTTPError("https://api.github.com/", 403, "rate limit exceeded", {}, None)
        if failure == "http"
        else URLError("fixture connection failure")
    )

    def urlopen(request, timeout):
        calls.append(request.full_url)
        if len(calls) == failed_page:
            raise error
        return response([issue(tracker, 1)])

    monkeypatch.setattr(tracker.urllib.request, "urlopen", urlopen)
    with pytest.raises(type(error)):
        tracker.main()

    assert len(calls) == failed_page
    assert table.read_bytes() == before


def test_successful_pagination_keeps_all_pages(tracker, monkeypatch):
    pages = [[issue(tracker, 1)], [issue(tracker, 2)], []]
    calls = []

    def urlopen(request, timeout):
        calls.append(request.full_url)
        return response(pages[len(calls) - 1])

    monkeypatch.setattr(tracker.urllib.request, "urlopen", urlopen)
    assert tracker.fetch_github_issues() == pages[0] + pages[1]
    assert [url.rsplit("page=", 1)[1] for url in calls] == ["1", "2", "3"]


def test_successful_fetch_updates_table(tracker, table, monkeypatch):
    pages = iter([[issue(tracker, 1)], []])
    monkeypatch.setattr(
        tracker.urllib.request, "urlopen", lambda request, timeout: response(next(pages))
    )

    assert tracker.main() == 0
    assert "Existing series" not in table.read_text(encoding="utf-8")
    assert "FOCIL Breakout" in table.read_text(encoding="utf-8")


def test_successful_empty_fetch_is_not_an_error(tracker, table, monkeypatch):
    monkeypatch.setattr(
        tracker.urllib.request, "urlopen", lambda request, timeout: response([])
    )

    assert tracker.main() == 0
    assert "Existing series" not in table.read_text(encoding="utf-8")
    assert "## Inactive Series" in table.read_text(encoding="utf-8")
