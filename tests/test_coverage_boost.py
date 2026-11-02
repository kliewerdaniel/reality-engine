"""Targeted coverage boost tests."""
from __future__ import annotations

import sqlite3
from pathlib import Path

from reality_engine.cli import (
    cmd_as_of,
    cmd_audit_verify,
    cmd_claims,
    cmd_ingest,
    cmd_init,
    cmd_revise,
    cmd_trace,
)
from reality_engine.core.temporal import (
    bitemporal_key,
    format_iso8601,
    get_observations_in_interval,
    get_observations_since,
    get_relationships_in_interval,
    get_relationships_since,
    parse_iso8601,
    reconstruct_claims_at,
    reconstruct_events_at,
    reconstruct_observations_at,
)


def test_parse_iso() -> None:
    assert parse_iso8601(None) is None
    assert parse_iso8601("") is None
    assert parse_iso8601("None") is None
    assert parse_iso8601("bad") is None
    dt = parse_iso8601("2026-01-01T00:00:00")
    assert dt is not None
    assert format_iso8601(dt) == "2026-01-01T00:00:00"
    assert bitemporal_key("r", "v", "t") == ("r", "v", "t")


def test_cli_ingest_feed(tmp_path: Path) -> None:
    feed = tmp_path / "feed.xml"
    feed.write_text('<?xml version="1.0"?><rss><channel><item><title>T</title><link>http://x</link><description>D</description></item></channel></rss>')
    ns = type("NS", (), {"path": None, "feed": "http://feed", "fixture": str(feed)})()
    assert cmd_ingest(ns) == 0


def test_cli_ingest_nothing() -> None:
    ns = type("NS", (), {"path": None, "feed": None, "fixture": None})()
    assert cmd_ingest(ns) == 0


def test_cli_trace_empty(tmp_path: Path) -> None:
    db = str(tmp_path / "t.db")
    cmd_init(type("NS", (), {"db": db})())
    assert cmd_trace(type("NS", (), {"db": db})()) == 0


def test_cli_claims_empty(tmp_path: Path) -> None:
    db = str(tmp_path / "t.db")
    cmd_init(type("NS", (), {"db": db})())
    assert cmd_claims(type("NS", (), {"db": db})()) == 0


def test_cli_audit_no_table(tmp_path: Path) -> None:
    db = str(tmp_path / "t.db")
    conn = sqlite3.connect(db)
    conn.close()
    assert cmd_audit_verify(type("NS", (), {"db": db})()) == 0


def test_cli_as_of_revise() -> None:
    assert cmd_as_of(type("NS", (), {"timestamp": "2026-01-01"})()) == 0
    assert cmd_revise(type("NS", (), {"proposal": "p1"})()) == 0


def test_temporal_helpers_empty(tmp_path: Path) -> None:
    from reality_engine.database import Database
    db = Database(str(tmp_path / "t.db"))
    conn = db.conn
    assert get_observations_in_interval(conn, "a", "b") == []
    assert get_observations_since(conn, "a") == []
    assert reconstruct_observations_at(conn, None, "2026-01-01") == []
    assert reconstruct_claims_at(conn, None, "2026-01-01") == []
    assert get_relationships_in_interval(conn, "a", "b") == []
    assert get_relationships_since(conn, "a") == []
    assert reconstruct_observations_at(conn, "ent", "2026-01-01") == []
    assert reconstruct_claims_at(conn, "ent", "2026-01-01") == []
    assert reconstruct_events_at(conn, "2026-01-01", "2026-12-31") == []
