#!/usr/bin/env python3
"""Generate docs/STATUS.md from docs/status.json and verify claims against pytest junit."""
import argparse, json, os, sys, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS_JSON = ROOT / "docs" / "status.json"
STATUS_MD = ROOT / "docs" / "STATUS.md"

def load_status():
    return json.loads(STATUS_JSON.read_text())

def junit_passed_ids(junit_path):
    if not junit_path or not Path(junit_path).exists():
        return set()
    tree = ET.parse(junit_path)
    passed = set()
    for tc in tree.iter("testcase"):
        if tc.find("failure") is None and tc.find("error") is None and tc.find("skipped") is None:
            passed.add(tc.get("name"))
    return passed

def gen(s):
    lines = ["# Reality Engine — Status (generated; do not edit by hand)", "", "## Findings", ""]
    lines.append("| ID | state | test | commit |")
    lines.append("|---|---|---|---|")
    for fid, info in s["findings"].items():
        lines.append(f"| {fid} | {info['state']} | {info.get('test') or '-'} | {info.get('commit') or '-'} |")
    lines += ["", "## Milestones", ""]
    for m, st in s["milestones"].items():
        lines.append(f"- {m}: {st}")
    STATUS_MD.write_text("\n".join(lines) + "\n")

def check(s, junit):
    passed = junit_passed_ids(junit)
    ok = True
    for fid, info in s["findings"].items():
        if info["state"] == "fixed":
            t = info.get("test")
            if not t or t not in passed:
                print(f"FAIL: {fid} marked fixed but test not in passing junit: {t}")
                ok = False
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--junit", default="reports/junit.xml")
    args = ap.parse_args()
    s = load_status()
    if args.check:
        ok = check(s, ROOT / args.junit if not os.path.isabs(args.junit) else Path(args.junit))
        if not ok:
            sys.exit(1)
        print("gen_status --check: OK")
    else:
        gen(s)
        print("generated docs/STATUS.md")

if __name__ == "__main__":
    main()
