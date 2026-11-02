"""Stdlib CLI for Reality Engine."""
from __future__ import annotations

import argparse
import sqlite3
import sys


def _connect(db: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn


def cmd_init(args: argparse.Namespace) -> int:
    from reality_engine.database import Database

    Database(args.db)
    print(f"initialized {args.db}")
    return 0


def cmd_ingest(args: argparse.Namespace) -> int:
    from reality_engine.adapters import DirectoryAdapter, RssAdapter

    if getattr(args, "path", None):
        items = DirectoryAdapter(args.path).fetch()
        print(f"ingested {len(items)} items from {args.path}")
    elif getattr(args, "feed", None):
        items = RssAdapter(args.feed, getattr(args, "fixture", None)).fetch()
        n = sum(len(x.get("items", [])) for x in items)
        print(f"ingested {n} feed items from {args.feed}")
    else:
        print("nothing to ingest")
    return 0


def cmd_claims(args: argparse.Namespace) -> int:
    conn = _connect(args.db)
    rows = conn.execute("SELECT id, subject_id, predicate, object_value FROM claims").fetchall()
    for r in rows:
        print(f"{r['id']} {r['subject_id']} {r['predicate']} {r['object_value']}")
    conn.close()
    return 0


def cmd_trace(args: argparse.Namespace) -> int:
    conn = _connect(args.db)
    claims = conn.execute("SELECT id, document_id FROM claims").fetchall()
    for c in claims:
        doc_id = c["document_id"]
        doc = conn.execute("SELECT id, source_id, content_hash FROM documents WHERE id=?", (doc_id,)).fetchone()
        source = None
        if doc:
            source = conn.execute("SELECT id, name FROM sources WHERE id=?", (doc["source_id"],)).fetchone()
        line = f"claim={c['id']} -> document={doc_id}"
        if doc:
            line += f" (hash={doc['content_hash']})"
        if source:
            line += f" -> source={source['id']} ({source['name']})"
        print(line)
    conn.close()
    return 0


def cmd_as_of(args: argparse.Namespace) -> int:
    print(f"as-of {args.timestamp}")
    return 0


def cmd_audit_verify(args: argparse.Namespace) -> int:
    conn = _connect(args.db)
    try:
        rows = conn.execute("SELECT * FROM audit_log").fetchall()
        print(f"audit entries: {len(rows)}")
    except sqlite3.OperationalError:
        print("no audit_log table")
    conn.close()
    return 0


def cmd_revise(args: argparse.Namespace) -> int:
    print(f"revise {args.proposal}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="reality-engine")
    ap.add_argument("--db", default="reality_engine.db")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_init = sub.add_parser("init")
    p_init.set_defaults(func=cmd_init)
    p_ingest = sub.add_parser("ingest")
    p_ingest.add_argument("--path")
    p_ingest.add_argument("--feed")
    p_ingest.add_argument("--fixture")
    p_ingest.set_defaults(func=cmd_ingest)
    p_claims = sub.add_parser("claims")
    p_claims.set_defaults(func=cmd_claims)
    p_trace = sub.add_parser("trace")
    p_trace.set_defaults(func=cmd_trace)
    p_asof = sub.add_parser("as-of")
    p_asof.add_argument("timestamp")
    p_asof.set_defaults(func=cmd_as_of)
    p_audit = sub.add_parser("audit-verify")
    p_audit.set_defaults(func=cmd_audit_verify)
    p_revise = sub.add_parser("revise")
    p_revise.add_argument("proposal")
    p_revise.set_defaults(func=cmd_revise)
    args = ap.parse_args(argv)
    result = args.func(args)
    return int(result) if result is not None else 0


if __name__ == "__main__":
    sys.exit(main())
