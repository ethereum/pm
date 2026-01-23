#!/usr/bin/env python3
"""
Fetch ACD call data from nixorokish/eth-protocol-transcripts and update the README.
"""

import re
import urllib.request
from pathlib import Path


def fetch_readme(url):
    """Fetch README content from a URL."""
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode('utf-8')


def extract_table_from_readme(readme_content):
    """Extract the ACD calls table from the eth-protocol-transcripts README."""
    pattern = r'# ACD calls\s*\n\n(\|[^\n]+\|\n\| ---[^\n]+\|\n(?:\|[^\n]+\|\n)*)'
    match = re.search(pattern, readme_content)
    if match:
        return match.group(1).strip()
    return None


def update_pm_readme(table_content):
    """Update the nixorokish/pm README with the new table."""
    readme_path = Path('README.md')
    
    if not readme_path.exists():
        print("ERROR: README.md not found")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern: Find the existing unified table after the "Previous AllCoreDevs" section
    pattern = (
        r'(## Previous AllCoreDevs Meetings\s*\n\n)'
        r'\|[^\n]+\|\n\| ---[^\n]+\|\n(?:\|[^\n]+\|\n)*'
    )
    
    # Use a function for replacement to avoid regex interpretation of table_content
    def replacer(match):
        return match.group(1) + table_content + '\n'
    
    updated_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    if updated_content == content:
        print("No changes detected")
        return False
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("README.md updated successfully")
    return True


def main():
    print("Fetching README from nixorokish/eth-protocol-transcripts...")
    
    readme_url = "https://raw.githubusercontent.com/nixorokish/eth-protocol-transcripts/main/README.md"
    
    try:
        readme_content = fetch_readme(readme_url)
    except Exception as e:
        print(f"ERROR: Failed to fetch README: {e}")
        return 1
    
    table = extract_table_from_readme(readme_content)
    
    if not table:
        print("ERROR: Could not find ACD calls table in source README")
        return 1
    
    print(f"Found table with {table.count(chr(10))} rows")
    
    if update_pm_readme(table):
        print("Done!")
    else:
        print("No updates made")
    
    return 0


if __name__ == '__main__':
    exit(main())