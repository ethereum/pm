#!/usr/bin/env python3
"""Auto-create ACDE/ACDC issues for upcoming protocol calls.

Checks if the most recent ACDE (or ACDC) issue is closed, and if so,
creates the next one with the correct call number, date, and body format
that the ACDbot expects.

Runs every Saturday at 09:00 UTC via GitHub Actions.
Can also be triggered manually via workflow_dispatch.

Usage:
  python3 auto-create-acd-issue.py                    # auto mode (check both ACDE and ACDC)
  python3 auto-create-acd-issue.py --dry-run          # print what would be created, don't create
  python3 auto-create-acd-issue.py --type acde        # only check ACDE
  python3 auto-create-acd-issue.py --type acdc        # only check ACDC
"""

import argparse
import json
import os
import re
from datetime import datetime, timedelta, timezone

REPO = os.environ.get("GITHUB_REPOSITORY", "ethereum/pm")
GITHUB_TOKEN = os.environ.get("PAT_TOKEN") or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN", "")

# Anchors: the most recent known calls
# ACDE #246 = Sep 24, 2026 (open), ACDC #187 = Sep 17, 2026 (open)
# These are used only as fallback if the API query fails

# Series configuration
SERIES_CONFIG = {
    "acde": {
        "display_name": "All Core Devs - Execution",
        "short_name": "ACDE",
        "title_prefix": "All Core Devs - Execution (ACDE)",
        "labels": ["ACD", "Execution", "protocol-call"],
        "layer_label": "Execution",
    },
    "acdc": {
        "display_name": "All Core Devs - Consensus",
        "short_name": "ACDC",
        "title_prefix": "All Core Devs - Consensus (ACDC)",
        "labels": ["ACD", "Consensus", "protocol-call"],
        "layer_label": "Consensus",
    },
}

DEFAULT_AGENDA = "- Glamsterdam\n- Hegotá\n- Misc"
DEFAULT_DURATION = "90 minutes"
DEFAULT_OCCURRENCE = "bi-weekly"
CALL_TIME = "14:00 UTC"
CADENCE_DAYS = 14  # bi-weekly


def api_call(endpoint, method="GET", payload=None):
    """Call GitHub REST API via curl."""
    import urllib.request
    url = f"https://api.github.com/repos/{REPO}/{endpoint}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode()
            return json.loads(body) if body.strip() else {}
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()[:200] if e.fp else str(e)
        print(f"  API error ({e.code}): {error_body}")
        return None
    except Exception as e:
        print(f"  API error: {e}")
        return None

def gh_api(endpoint, method="GET", fields=None):
    """Compatibility wrapper — calls api_call."""
    if fields and method == "POST":
        return api_call(endpoint, method=method, payload=fields)
    return api_call(endpoint, method=method)


def get_recent_issues(series_key):
    """Get the most recent issues for a series, sorted by call number."""
    config = SERIES_CONFIG[series_key]
    label = config["layer_label"]

    # Query issues with ACD + layer label, all states
    result = gh_api(f"issues?labels=ACD,{label}&state=all&per_page=10&sort=created&direction=desc")
    if not result:
        print(f"  WARNING: Could not fetch issues for {series_key}")
        return []

    issues = result if isinstance(result, list) else []
    if isinstance(result, dict) and "items" in result:
        issues = result["items"]

    # Parse call numbers from titles
    parsed = []
    for issue in issues:
        title = issue.get("title", "")
        num_match = re.search(r"#(\d+)", title)
        if num_match:
            parsed.append({
                "number": issue.get("number"),
                "call_number": int(num_match.group(1)),
                "title": title,
                "state": issue.get("state"),
                "created_at": issue.get("created_at"),
                "body": issue.get("body", ""),
            })

    # Sort by call number descending
    parsed.sort(key=lambda x: x["call_number"], reverse=True)
    return parsed


def parse_date_from_title(title):
    """Extract the date from a title like 'All Core Devs - Execution (ACDE) #246, September 24, 2026'."""
    # Try various date formats
    patterns = [
        r"#\d+,\s+(\w+\s+\d{1,2},?\s+\d{4})",  # "September 24, 2026" or "September 24 2026"
    ]
    for pattern in patterns:
        match = re.search(pattern, title)
        if match:
            date_str = match.group(1)
            # Parse it
            for fmt in ["%B %d, %Y", "%B %d %Y", "%b %d, %Y", "%b %d %Y"]:
                try:
                    return datetime.strptime(date_str, fmt).date()
                except ValueError:
                    continue
    return None


def parse_date_from_body(body):
    """Extract the date from the issue body's UTC Date & Time section."""
    pattern = r"### UTC Date & Time\n\n([^\n]+)"
    match = re.search(pattern, body)
    if not match:
        return None
    date_text = match.group(1).strip()
    # Remove markdown link if present
    date_text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", date_text)
    for fmt in ["%B %d, %Y, %H:%M UTC", "%B %d %Y, %H:%M UTC", "%b %d, %Y, %H:%M UTC", "%b %d %Y, %H:%M UTC"]:
        try:
            return datetime.strptime(date_text, fmt).date()
        except ValueError:
            continue
    return None


def build_issue_body(call_date, series_key):
    """Build the issue body matching the protocol-call-form template format."""
    config = SERIES_CONFIG[series_key]
    date_str = call_date.strftime("%B %-d, %Y")
    datetime_str = f"{call_date.strftime('%B %-d, %Y')}, {CALL_TIME}"

    body = f"""### UTC Date & Time

{datetime_str}

### Agenda

{DEFAULT_AGENDA}

### Call Series

{config["display_name"]}

### Autopilot Mode

- [x] Use autopilot (recommended defaults for this call series)


<details>
<summary>🔧 Meeting Configuration</summary>

### Duration

{DEFAULT_DURATION}

### Occurrence Rate

{DEFAULT_OCCURRENCE}

### Use Custom Meeting Link (Optional)

- [ ] I will provide my own meeting link

### Display Zoom Link in Calendar Invite (Optional)

- [x] Display Zoom link in invite

### YouTube Livestream Link (Optional)

- [ ] Create YouTube livestream link
</details>"""

    return body


def check_issue_exists(call_number, series_key):
    """Check if an issue already exists for this call number."""
    config = SERIES_CONFIG[series_key]
    expected_title_fragment = f"{config['title_prefix']} #{call_number}"
    result = gh_api(f"issues?labels=ACD,{config['layer_label']}&state=all&per_page=100")
    if not result:
        return False
    issues = result if isinstance(result, list) else []
    if isinstance(result, dict) and "items" in result:
        issues = result["items"]
    for issue in issues:
        if expected_title_fragment in issue.get("title", ""):
            return True
    return False


def create_issue(call_number, call_date, series_key, dry_run=False):
    """Create a GitHub issue for a protocol call."""
    config = SERIES_CONFIG[series_key]
    title = f"{config['title_prefix']} #{call_number}, {call_date.strftime('%B %-d, %Y')}"
    body = build_issue_body(call_date, series_key)
    labels = ",".join(config["labels"])

    if dry_run:
        print(f"  [DRY RUN] Would create:")
        print(f"    Title: {title}")
        print(f"    Labels: {labels}")
        print(f"    Body preview: {body[:100]}...")
        return True

    # Build gh api command manually for proper label array handling
    payload = {"title": title, "body": body, "labels": config["labels"]}
    result_data = api_call("issues", method="POST", payload=payload)

    if result_data and result_data.get("number"):
        print(f"  ✅ Created issue #{result_data['number']}: {title}")
        print(f"     {result_data.get('html_url', '')}")
        return True
    else:
        print(f"  ❌ Failed to create issue")
        return False


def process_series(series_key, dry_run=False):
    """Check if the next issue should be created for a series."""
    config = SERIES_CONFIG[series_key]
    print(f"\n{'='*50}")
    print(f"Checking {config['short_name']} ({config['display_name']})")
    print(f"{'='*50}")

    issues = get_recent_issues(series_key)
    if not issues:
        print(f"  No existing issues found for {series_key}, skipping")
        return

    latest = issues[0]
    call_num = latest["call_number"]
    state = latest["state"]
    print(f"  Latest: #{call_num} ({latest['title'][:60]}...) — {state.upper()}")

    if state == "open":
        print(f"  Latest issue is still open → skip (call hasn't happened yet)")
        return

    # Issue is closed — calculate next call
    next_num = call_num + 1

    # Get the date from the latest issue
    last_date = parse_date_from_title(latest["title"])
    if not last_date:
        last_date = parse_date_from_body(latest.get("body", ""))
    if not last_date:
        print(f"  WARNING: Could not parse date from latest issue, skipping")
        return

    # Next date = last date + 14 days
    next_date = last_date + timedelta(days=CADENCE_DAYS)

    # If next date is in the past, keep adding 14 days until it's a future Thursday
    today = datetime.now(timezone.utc).date()
    while next_date <= today:
        next_date += timedelta(days=CADENCE_DAYS)
        next_num += 1  # Skip missed calls
        print(f"  Date was in past, advancing to #{next_num} on {next_date}")

    # Verify it's a Thursday
    if next_date.weekday() != 3:  # 3 = Thursday
        print(f"  WARNING: Calculated date {next_date} is not a Thursday (weekday={next_date.weekday()})")
        # Find the next Thursday
        days_until_thu = (3 - next_date.weekday()) % 7
        if days_until_thu == 0:
            days_until_thu = 7
        next_date += timedelta(days=days_until_thu)
        print(f"  Adjusted to next Thursday: {next_date}")

    # Check if issue already exists for this number
    if check_issue_exists(next_num, series_key):
        print(f"  Issue #{next_num} already exists → skip")
        return

    # Create the issue
    print(f"  Next call: #{next_num} on {next_date.strftime('%B %-d, %Y')}")
    create_issue(next_num, next_date, series_key, dry_run=dry_run)


def main():
    parser = argparse.ArgumentParser(description="Auto-create ACDE/ACDC issues")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be created without creating")
    parser.add_argument("--type", choices=["acde", "acdc"], help="Only process one series")
    args = parser.parse_args()

    print(f"Auto-create ACD issues for {REPO}")
    print(f"Time: {datetime.now(timezone.utc).isoformat()}")
    if args.dry_run:
        print("⚠️  DRY RUN MODE — no issues will be created")

    series_to_check = [args.type] if args.type else ["acde", "acdc"]

    for series_key in series_to_check:
        process_series(series_key, dry_run=args.dry_run)

    print("\nDone.")


if __name__ == "__main__":
    main()
