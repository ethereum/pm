#!/usr/bin/env python3
"""
Fetch ACD call data from nixorokish/eth-protocol-transcripts and update the README, append-only.
"""

import re
import urllib.request
from pathlib import Path


def fetch_readme(url):
    """Fetch README content from a URL."""
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode('utf-8')


def extract_table_rows(table_content):
    """Extract individual rows from a markdown table."""
    lines = table_content.strip().split('\n')
    rows = []
    for line in lines:
        # Skip header and separator rows
        if line.startswith('| Date') or line.startswith('| ---'):
            continue
        if line.startswith('|'):
            rows.append(line)
    return rows


def get_row_key(row):
    """Extract a unique key from a row (date + type + number)."""
    # Row format: | Date | Type | № | Issue | ...
    parts = [p.strip() for p in row.split('|')]
    if len(parts) >= 4:
        # parts[0] is empty (before first |), parts[1] is date, parts[2] is type, parts[3] is number
        return (parts[1], parts[2], parts[3])  # (date, type, number)
    return None


def extract_table_from_readme(readme_content, section_header):
    """Extract table from a README section."""
    # Pattern to find table after section header
    pattern = rf'{re.escape(section_header)}\s*\n\n(\|[^\n]+\|\n\| ---[^\n]+\|\n(?:\|[^\n]+\|\n)*)'
    match = re.search(pattern, readme_content)
    if match:
        return match.group(1).strip()
    return None


def update_pm_readme(new_rows_to_add):
    """Add new rows to the pm README table."""
    readme_path = Path('README.md')
    
    if not readme_path.exists():
        print("ERROR: README.md not found")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not new_rows_to_add:
        print("No new rows to add")
        return False
    
    # Pattern: Find the table header and separator, then insert new rows after
    pattern = (
        r'(## Previous AllCoreDevs Meetings\s*\n\n'
        r'\| Date[^\n]+\|\n'
        r'\| ---[^\n]+\|\n)'
    )
    
    # Insert new rows right after the header
    new_rows_text = '\n'.join(new_rows_to_add) + '\n'
    
    def replacer(match):
        return match.group(1) + new_rows_text
    
    updated_content = re.sub(pattern, replacer, content)
    
    if updated_content == content:
        print("No changes detected")
        return False
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("README.md updated successfully")
    return True


def main():
    print("Fetching README from nixorokish/eth-protocol-transcripts...")
    
    source_url = "https://raw.githubusercontent.com/nixorokish/eth-protocol-transcripts/main/README.md"
    
    try:
        source_readme = fetch_readme(source_url)
    except Exception as e:
        print(f"ERROR: Failed to fetch source README: {e}")
        return 1
    
    # Extract table from source
    source_table = extract_table_from_readme(source_readme, "# ACD calls")
    if not source_table:
        print("ERROR: Could not find ACD calls table in source README")
        return 1
    
    source_rows = extract_table_rows(source_table)
    print(f"Found {len(source_rows)} rows in source")
    
    # Read existing pm README
    readme_path = Path('README.md')
    if not readme_path.exists():
        print("ERROR: README.md not found")
        return 1
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        pm_readme = f.read()
    
    # Extract existing table from pm README
    pm_table = extract_table_from_readme(pm_readme, "## Previous AllCoreDevs Meetings")
    if not pm_table:
        print("ERROR: Could not find table in pm README")
        return 1
    
    pm_rows = extract_table_rows(pm_table)
    print(f"Found {len(pm_rows)} existing rows in pm README")
    
    # Find existing row keys
    existing_keys = set()
    for row in pm_rows:
        key = get_row_key(row)
        if key:
            existing_keys.add(key)
    
    # Find new rows (in source but not in pm)
    new_rows = []
    for row in source_rows:
        key = get_row_key(row)
        if key and key not in existing_keys:
            new_rows.append(row)
            print(f"  New row: {key}")
    
    print(f"Found {len(new_rows)} new rows to add")
    
    if new_rows and update_pm_readme(new_rows):
        print("Done!")
    else:
        print("No updates made")
    
    return 0


if __name__ == '__main__':
    exit(main())
