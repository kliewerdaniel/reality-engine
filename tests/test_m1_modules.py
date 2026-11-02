"""Tests for Phase 7 M1 modules."""
from __future__ import annotations

from pathlib import Path

from reality_engine.adapters import DirectoryAdapter, RssAdapter
from reality_engine.cli import main as cli_main
from reality_engine.intelligence import ModelProvider, OllamaProvider
from reality_engine.proposal import ClaimProposer, Proposal, RuleBasedProposer


def test_directory_adapter(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("hello")
    (tmp_path / "sub").mkdir()
    items = DirectoryAdapter(str(tmp_path)).fetch()
    assert len(items) == 2
    assert any(i["content"] == "hello" for i in items)


def test_rss_adapter_fixture(tmp_path: Path) -> None:
    feed = tmp_path / "feed.xml"
    feed.write_text("""<?xml version="1.0"?>
<rss><channel>
<item><title>T</title><link>http://x</link><description>D</description><pubDate>P</pubDate></item>
</channel></rss>""")
    items = RssAdapter("http://feed", str(feed)).fetch()
    assert items[0]["items"][0]["title"] == "T"


def test_rss_adapter_no_fixture() -> None:
    items = RssAdapter("http://feed").fetch()
    assert items[0]["items"] == []


def test_proposal() -> None:
    p = Proposal(foo=1)
    assert p.foo == 1


def test_claim_proposer() -> None:
    assert ClaimProposer().propose("e", []) == []


def test_rule_based_proposer() -> None:
    obs = [{"id": "o1", "observed_value": 5}]
    props = RuleBasedProposer().propose("ent", obs)
    assert len(props) == 1
    assert props[0].entity_id == "ent"


def test_model_provider() -> None:
    assert ModelProvider().generate("p") == ""


def test_ollama_off_by_default() -> None:
    assert OllamaProvider().enabled is False
    assert OllamaProvider().generate("p") == ""
    assert OllamaProvider(enabled=True).generate("p") == ""


def test_cli_init(tmp_path: Path) -> None:
    db = str(tmp_path / "t.db")
    assert cli_main(["--db", db, "init"]) == 0
    assert Path(db).exists()


def test_cli_trace(tmp_path: Path) -> None:
    db = str(tmp_path / "t.db")
    cli_main(["--db", db, "init"])
    assert cli_main(["--db", db, "trace"]) == 0


def test_cli_claims_empty(tmp_path: Path) -> None:
    db = str(tmp_path / "t.db")
    cli_main(["--db", db, "init"])
    assert cli_main(["--db", db, "claims"]) == 0


def test_cli_as_of() -> None:
    assert cli_main(["as-of", "2026-01-01"]) == 0


def test_cli_audit_verify(tmp_path: Path) -> None:
    db = str(tmp_path / "t.db")
    cli_main(["--db", db, "init"])
    assert cli_main(["--db", db, "audit-verify"]) == 0


def test_cli_revise() -> None:
    assert cli_main(["revise", "p1"]) == 0


def test_cli_ingest_dir(tmp_path: Path) -> None:
    d = tmp_path / "d"
    d.mkdir()
    (d / "f.txt").write_text("x")
    db = str(tmp_path / "t.db")
    cli_main(["--db", db, "init"])
    assert cli_main(["--db", db, "ingest", "--path", str(d)]) == 0
