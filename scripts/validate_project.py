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
    "references/layout-patterns.md", "references/deliverable-checklist.md",
    "references/agent-install.md",
    "references/guizang-feature-guide.md", "references/multimode-workspace.md",
    "references/layouts.md", "references/layouts-swiss.md",
    "references/components.md", "references/themes.md", "references/themes-swiss.md",
    "references/presenter-mode.md", "references/checklist.md",
    "references/swiss-layout-lock.md", "references/swiss-map-component.md",
    "references/image-prompts.md", "references/screenshot-framing.md",
    "assets/template.html", "assets/template-swiss.html", "assets/motion.min.js",
    "assets/multimode-document-studio-template.html",
    "scripts/validate-presenter-mode.mjs",
    "scripts/check-presenter-runtime-sync.mjs",
    "scripts/validate-swiss-deck.mjs",
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
if not all(token in skill for token in ("Contrast", "Repetition", "Alignment", "Proximity", "履歷", "研究報告", "完整原始碼")):
    print("CRAP principle check failed")
    sys.exit(1)
for href in re.findall(r'href="([^"]+)"', html):
    if href.startswith(("http://", "https://", "#", "mailto:", "javascript:")):
        continue
    target = (ROOT / href.split("#", 1)[0]).resolve()
    if not target.exists():
        print(f"Missing local href target: {href}")
        sys.exit(1)
instructions = (ROOT / "AI-STUDIO-INSTRUCTIONS.md").read_text(encoding="utf-8")
checklist = (ROOT / "references/deliverable-checklist.md").read_text(encoding="utf-8")
for label, content in (("AI Studio instructions", instructions), ("deliverable checklist", checklist)):
    for token in ("履歷", "研究報告", "原始碼"):
        if token not in content:
            print(f"{label} missing required feature: {token}")
            sys.exit(1)
if "v2.0.0" not in instructions or "v2.0.0" not in html or "v2.0.0" not in (ROOT / "README.md").read_text(encoding="utf-8") or "version: 2.0.0" not in skill:
    print("Version consistency check failed")
    sys.exit(1)
for template in ("assets/template.html", "assets/template-swiss.html"):
    content = (ROOT / template).read_text(encoding="utf-8")
    if "<!DOCTYPE html>" not in content or "ppt-presenter" not in content or "ppt-overview" not in content:
        print(f"Template feature check failed: {template}")
        sys.exit(1)
guide = (ROOT / "references/guizang-feature-guide.md").read_text(encoding="utf-8")
mode_spec = (ROOT / "references/multimode-workspace.md").read_text(encoding="utf-8")
mode_template = (ROOT / "assets/multimode-document-studio-template.html").read_text(encoding="utf-8")
for token in ("16:9 學術簡報模式", "CRAP 檢核報告", "列印／PDF", "下載單檔 HTML"):
    if token not in mode_spec or token not in instructions or token not in mode_template:
        print(f"Multimode workspace feature missing: {token}")
        sys.exit(1)
for token in ("data-mode-button", "data-mode-view", "window.print()", "Blob(", "aspect-ratio:16/9", "data-template-choice", "data-palette-choice", "function applyTemplate", "function applyPalette", "Swiss Blue", "Ocean Teal", "Workshop 活力"):
    if token not in mode_template:
        print(f"Multimode HTML template missing behaviour: {token}")
        sys.exit(1)
for token in ("template.html", "template-swiss.html", "presenter-mode.md", "layouts-swiss.md"):
    if token not in guide:
        print(f"Guizang feature guide missing reference: {token}")
        sys.exit(1)
print("PASS: required files, Skill front matter, CRAP terms, complete deliverables, Guizang templates and references, multimode workspace features, version consistency, and local links.")
print("NOTE: this script does not test browser rendering, clipboard permissions, or Pages deployment.")
