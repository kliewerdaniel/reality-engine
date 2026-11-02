#!/usr/bin/env python3
"""Check documentation links."""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
VALID_EXTENSIONS = {".md", ".pdf", ".txt", ".docx", ".html", ".json", ".yaml", ".yml", ".png", ".jpg", ".jpeg", ".gif", ".svg"}

def check_links():
    """Check all internal links in documentation files."""
    errors = []
    checked = set()
    
    # Find all markdown files
    md_files = list(DOCS_DIR.rglob("*.md"))
    if not md_files:
        md_files = [REPO_ROOT / "README.md"]
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            errors.append(f"{md_file}: Cannot read - {e}")
            continue
        
        # Find links
        link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
        for match in link_pattern.finditer(content):
            text, url = match.group(1), match.group(2)
            
            # Skip external links
            if url.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                continue
            
            # Resolve relative path
            if url.startswith("./"):
                url = url[2:]
            if url.startswith("../"):
                url = url[3:]
            
            # Check if file exists
            target = REPO_ROOT / url
            if not target.exists():
                errors.append(f"{md_file}: Broken link '{url}' -> '{text}'")
    
    return errors

def main():
    errors = check_links()
    if errors:
        print("Broken links found:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("All documentation links are valid.")
        sys.exit(0)

if __name__ == "__main__":
    main()
