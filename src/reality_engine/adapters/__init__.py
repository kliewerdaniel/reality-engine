"""Adapters for ingesting external sources."""
from __future__ import annotations

import glob
import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


class DirectoryAdapter:
    def __init__(self, directory: str) -> None:
        self.directory = directory

    def fetch(self) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for p in sorted(glob.glob(os.path.join(self.directory, "*"))):
            if os.path.isfile(p):
                out.append({"path": p, "content": Path(p).read_text(encoding="utf-8", errors="replace")})
            else:
                out.append({"path": p, "content": ""})
        return out


class RssAdapter:
    def __init__(self, feed_url: str, fixture_path: str | None = None) -> None:
        self.feed_url = feed_url
        self.fixture_path = fixture_path

    def fetch(self) -> list[dict[str, Any]]:
        if self.fixture_path is None:
            return [{"feed": self.feed_url, "items": []}]
        text = Path(self.fixture_path).read_text(encoding="utf-8")
        try:
            root = ET.fromstring(text)
        except ET.ParseError:
            return [{"feed": self.feed_url, "items": []}]
        items: list[dict[str, Any]] = []
        for item in root.iter("item"):
            items.append(
                {
                    "title": (item.findtext("title") or "").strip(),
                    "link": (item.findtext("link") or "").strip(),
                    "description": (item.findtext("description") or "").strip(),
                    "pubDate": (item.findtext("pubDate") or "").strip(),
                }
            )
        return [{"feed": self.feed_url, "items": items}]
