#!/usr/bin/env python3
"""
Fetch recent breakout call issues from ethereum/pm and update the active breakouts table.
"""

import json
import re
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path


def load_call_series_config():
    """Load the call series configuration using regex."""
    config_path = Path('.github/ACDbot/call_series_config.yml')
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse call_series entries: key followed by display_name
    config = {'call_series': {}}
    
    # Find all call series entries
    pattern = r'^\s{2}(\w+):\s*\n\s+display_name:\s*"([^"]+)"'
    matches = re.findall(pattern, content, re.MULTILINE)
    
    for key, display_name in matches:
        config['call_series'][key] = {'display_name': display_name}
    
    return config


def get_breakout_series(config):
    """Extract breakout series from config (exclude core ACD calls and one-off)."""
    core_calls = {'acdc', 'acde', 'acdt', 'one-off'}
    breakouts = {}
    
    for key, value in config.get('call_series', {}).items():
        if key not in core_calls:
            breakouts[value['display_name']] = key
    
    return breakouts


# Trusted facilitators whose series are included even if not in config
TRUSTED_FACILITATORS = {'will-corcoran'}


def fetch_github_issues(repo='ethereum/pm', days=90):
    """Fetch recent issues from GitHub API."""
    since = (datetime.utcnow() - timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    all_issues = []
    page = 1
    
    while True:
        url = f"https://api.github.com/repos/{repo}/issues?state=all&since={since}&per_page=100&page={page}"
        
        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/vnd.github.v3+json')
        req.add_header('User-Agent', 'pm-breakout-tracker')
        
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                issues = json.loads(response.read().decode('utf-8'))
                
                if not issues:
                    break
                    
                all_issues.extend(issues)
                page += 1
                
                # Safety limit
                if page > 10:
                    break
                    
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break
    
    return all_issues


def match_issue_to_series(issue_title, breakout_series):
    """Match an issue title to a breakout series."""
    title_lower = issue_title.lower()
    
    for display_name, key in breakout_series.items():
        # Check for exact display name match
        if display_name.lower() in title_lower:
            return display_name, key
        
        # Check for key-based patterns
        patterns = {
            'peerdas': ['peerdas'],
            'focil': ['focil'],
            'epbs': ['epbs', 'eip-7732', '7732'],
            'bal': ['eip-7928', '7928', 'block-level access'],
            'beam': ['beam call', 'beam chain', 'leanconsensus'],
            'rollcall': ['rollcall', 'roll call'],
            'evmmax': ['evmmax'],
            'resourcepricing': ['resource pricing', 'gas pricing'],
            'ethsimulate': ['eth_simulate', 'eth simulate'],
            'ethproofs': ['ethproofs'],
            'stateless': ['stateless'],
            'portal': ['portal'],
            'l2interop': ['l2 interop', 'l2-interop'],
            'pqinterop': ['pq interop', 'post-quantum interop'],
            'pqtransactionsignatures': ['pq transaction', 'post-quantum transaction', 'post quantum transaction', 'pqts'],
            'trustlessagents': ['trustless agents', 'erc-8004'],
            'allwalletdevs': ['allwalletdevs', 'all wallet devs', 'wallet devs'],
            'rpcstandards': ['rpc standards', 'rpc standard'],
            'trustlesslogindex': ['trustless log', 'log index'],
            'eipeditingofficehour': ['eip editing', 'office hour'],
            'eipip': ['eipip'],
            'glamsterdamrepricings': ['glamsterdam repricings', 'glamsterdam gas repricings'],
            'zkevm': ['l1-zkevm', 'l1 zkevm', 'zkevm'],
            'protocolresearch': ['protocol research'],
        }
        
        if key in patterns:
            for pattern in patterns[key]:
                if pattern in title_lower:
                    return display_name, key
    
    return None, None


def parse_meeting_date(text):
    """Extract meeting date from text (title or body)."""
    # Pattern: Month Day, Year (e.g., "January 21, 2026" or "Jan 21, 2026")
    month_pattern = r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2}),?\s+(\d{4})'
    match = re.search(month_pattern, text, re.IGNORECASE)
    if match:
        month_name, day, year = match.groups()
        months = {
            'jan': '01', 'january': '01', 'feb': '02', 'february': '02',
            'mar': '03', 'march': '03', 'apr': '04', 'april': '04',
            'may': '05', 'jun': '06', 'june': '06', 'jul': '07', 'july': '07',
            'aug': '08', 'august': '08', 'sep': '09', 'september': '09',
            'oct': '10', 'october': '10', 'nov': '11', 'november': '11',
            'dec': '12', 'december': '12'
        }
        month_num = months.get(month_name.lower(), '01')
        return f"{year}-{month_num}-{int(day):02d}"
    
    # Pattern: YYYY-MM-DD or YYYY/MM/DD
    iso_pattern = r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})'
    match = re.search(iso_pattern, text)
    if match:
        year, month, day = match.groups()
        return f"{year}-{int(month):02d}-{int(day):02d}"
    
    return None


def extract_series_name_from_title(title):
    """Extract a series name from issue title for unconfigured series."""
    # Pattern: "Series Name #N, Date" or "Series Name | Date"
    # Try to extract the part before the number/date
    match = re.match(r'^([^#|,]+?)(?:\s*[#|,]|\s+\d)', title)
    if match:
        return match.group(1).strip()
    return title.split(',')[0].split('|')[0].strip()


def get_active_breakouts(issues, breakout_series, days=90):
    """Identify active breakouts and their facilitators from recent issues."""
    active = {}  # key -> {display_name, facilitator, meeting_date, issue_url}
    
    # Calculate cutoff date for "active" (meeting date within past N days)
    cutoff_date = (datetime.utcnow() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    for issue in issues:
        # Skip pull requests
        if 'pull_request' in issue:
            continue
            
        title = issue.get('title', '')
        facilitator = issue.get('user', {}).get('login', 'Unknown')
        
        # Try to match to configured series
        display_name, key = match_issue_to_series(title, breakout_series)
        
        # If not matched but from a trusted facilitator, include anyway
        if not key and facilitator in TRUSTED_FACILITATORS:
            # Check if it looks like a call series (has a number pattern)
            if re.search(r'#\d+|call\s*\d+', title, re.IGNORECASE):
                display_name = extract_series_name_from_title(title)
                key = display_name.lower().replace(' ', '_')
        
        if key:
            # Parse meeting date from title first, then body
            meeting_date = parse_meeting_date(title)
            if not meeting_date:
                # Try parsing from issue body
                body = issue.get('body', '') or ''
                meeting_date = parse_meeting_date(body)
            if not meeting_date:
                # Fall back to created_at if no date found
                meeting_date = issue.get('created_at', '')[:10]
            
            # Only include if meeting date is within the active window
            if meeting_date < cutoff_date:
                continue
            
            issue_url = issue.get('html_url', '')
            
            # Keep the most recent issue for each series (by meeting date)
            if key not in active or meeting_date > active[key]['meeting_date']:
                active[key] = {
                    'display_name': display_name,
                    'facilitator': facilitator,
                    'meeting_date': meeting_date,
                    'issue_url': issue_url,
                }
    
    return active


def generate_table_content(active_breakouts):
    """Generate table rows."""
    lines = []
    
    # Sort by display name
    sorted_breakouts = sorted(active_breakouts.items(), key=lambda x: x[1]['display_name'].lower())
    
    for key, info in sorted_breakouts:
        facilitator_link = f"[@{info['facilitator']}](https://github.com/{info['facilitator']})"
        issue_link = f"[Link]({info['issue_url']})" if info['issue_url'] else "—"
        
        lines.append(
            f"| {info['display_name']} | {facilitator_link} | {info['meeting_date']} | {issue_link} |"
        )
    
    return '\n'.join(lines)


def update_breakouts_file(active_breakouts):
    """Update the markdown file"""
    output_path = Path('Breakout-Room-Meetings/active-breakout-series.md')
    
    if not output_path.exists():
        print(f"ERROR: {output_path} not found")
        return False
    
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate new table content
    new_table = generate_table_content(active_breakouts)
    
    # Update timestamp
    new_timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    content = re.sub(
        r'\*Last updated:.*\*',
        f'*Last updated: {new_timestamp} (updated weekly)*',
        content
    )
    
    # Replace table rows (everything between header row and ## Inactive or end of table)
    # Pattern: table header, separator, then rows until empty line or ## 
    table_pattern = (
        r'(\| Call Series \| Facilitator \| Latest \| Issue \|\n'
        r'\|[-|]+\|\n)'  # Header + separator
        r'(?:\|[^\n]+\|\n)*'  # Existing rows
    )
    
    content = re.sub(
        table_pattern,
        r'\g<1>' + new_table + '\n',
        content
    )
    
    # Check if content actually changed (compare without timestamp)
    with open(output_path, 'r', encoding='utf-8') as f:
        existing = f.read()
    
    existing_no_ts = re.sub(r'\*Last updated:.*\*', '', existing)
    content_no_ts = re.sub(r'\*Last updated:.*\*', '', content)
    
    if existing_no_ts.strip() == content_no_ts.strip():
        print("No changes detected (ignoring timestamp)")
        return False
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {output_path}")
    return True


def main():
    print("Loading call series configuration...")
    config = load_call_series_config()
    breakout_series = get_breakout_series(config)
    print(f"Found {len(breakout_series)} breakout series in config")
    
    print("Fetching recent issues from ethereum/pm...")
    issues = fetch_github_issues()
    print(f"Fetched {len(issues)} issues from the past 90 days")
    
    print("Matching issues to breakout series...")
    active_breakouts = get_active_breakouts(issues, breakout_series)
    print(f"Found {len(active_breakouts)} active breakout series")
    
    print("Updating markdown...")
    
    if update_breakouts_file(active_breakouts):
        print("Done!")
    else:
        print("No updates made")
    
    return 0


if __name__ == '__main__':
    exit(main())
