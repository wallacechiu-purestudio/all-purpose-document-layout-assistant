#!/usr/bin/env python3
"""Basic repository checks; does not replace browser visual QA."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "SKILL.md", "AI-STUDIO-INSTRUCTIONS.md",
    "LICENSE", "NOTICE.md", "index.html",
    "references/crap-checklist.md",
    "references/layout-patterns.md",
    "references/agent-install.md",
]
missing = [name for name in required if not (ROOT / name).is_file()]
if missing:
    print("Missing required files:")
    print("\n".join(f"- {name}" for name in missing))
    sys.exit(1)

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
html = (ROOT / "index.html").read_text(encoding="utf-8")
if not skill.startswith("---\n") or "name: all-purpose-document-layout-assistant" not in skill:
    print("SKILL.md front matter check failed")
    sys.exit(1)
if not all(token in skill for token in ("Contrast", "Repetition", "Alignment", "Proximity")):
    print("CRAP principle check failed")
    sys.exit(1)
for href in re.findall(r'href="([^"]+)"', html):
    if href.startswith(("http://", "https://", "#", "mailto:", "javascript:")):
        continue
    target = (ROOT / href.split("#", 1)[0]).resolve()
    if not target.exists():
        print(f"Missing local href target: {href}")
        sys.exit(1)
print("PASS: required files, Skill front matter, CRAP terms, and local links.")
print("NOTE: this script does not test browser rendering, clipboard permissions, or Pages deployment.")
