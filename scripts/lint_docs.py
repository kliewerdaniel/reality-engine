#!/usr/bin/env python3
"""Lint documentation files."""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"

# Patterns that indicate potential issues
PATTERNS = {
    "trailing_whitespace": re.compile(r"\s+$"),
    "empty_lines": re.compile(r"\n\s*\n\s*\n"),
    "lines_longer_than_100": re.compile(r".{101,}\n"),
    "no_trailing_newline": re.compile(r"\n$"),
}

def lint_file(path):
    """Lint a single documentation file."""
    errors = []
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"{path}: Cannot read - {e}"]
    
    lines = content.split("\n")
    
    # Check trailing whitespace
    for i, line in enumerate(lines, 1):
        if line != line.rstrip():
            errors.append(f"{path}:{i}: Trailing whitespace")
    
    # Check for lines longer than 100 characters
    for i, line in enumerate(lines, 1):
        if len(line) > 100:
            errors.append(f"{path}:{i}: Line longer than 100 characters")
    
    # Check file ends with newline
    if content and not content.endswith("\n"):
        errors.append(f"{path}: Missing trailing newline")
    
    return errors

def main():
    errors = []
    md_files = list(DOCS_DIR.rglob("*.md"))
    
    if not md_files:
        md_files = [REPO_ROOT / "README.md"]
    
    for md_file in md_files:
        errors.extend(lint_file(md_file))
    
    if errors:
        print("Documentation lint issues:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("All documentation files pass linting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
