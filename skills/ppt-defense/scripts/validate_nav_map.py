#!/usr/bin/env python3
"""Validate ppt-defense nav_map.json against dual-nav contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_map(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(nav: dict) -> list[str]:
    errors: list[str] = []
    total = int(nav.get("total_pages") or 0)
    if total < 1:
        errors.append("total_pages must be >= 1")
        return errors

    primary = nav.get("primary") or []
    chapters = nav.get("chapters") or {}
    page_chapter = {str(k): v for k, v in (nav.get("page_chapter") or {}).items()}

    if not primary:
        errors.append("primary must be a non-empty list")

    seen_pages: set[int] = set()
    for item in primary:
        cid = item.get("id")
        first = int(item.get("first_page") or 0)
        if cid not in chapters:
            errors.append(f"primary id {cid!r} missing in chapters")
            continue
        pages = [int(p) for p in chapters[cid].get("pages") or []]
        labels = chapters[cid].get("secondary_labels") or []
        if not pages:
            errors.append(f"chapter {cid!r} has empty pages")
            continue
        if min(pages) != first:
            errors.append(
                f"chapter {cid!r}: first_page={first} != min(pages)={min(pages)}"
            )
        if len(pages) >= 2 and len(labels) != len(pages):
            errors.append(
                f"chapter {cid!r}: secondary_labels length {len(labels)} != pages {len(pages)}"
            )
        if len(pages) < 2 and labels:
            errors.append(f"chapter {cid!r}: secondary_labels must be empty for single-page chapters")
        for p in pages:
            if p in seen_pages:
                errors.append(f"page {p} listed in multiple chapters")
            seen_pages.add(p)

    expected = set(range(1, total + 1))
    if seen_pages != expected:
        errors.append(
            f"chapter pages cover {sorted(seen_pages)} but need 1..{total}"
        )

    mapped = {int(k) for k in page_chapter}
    if mapped != expected:
        errors.append(
            f"page_chapter keys cover {sorted(mapped)} but need 1..{total}"
        )

    for page_s, cid in page_chapter.items():
        page = int(page_s)
        if cid not in chapters:
            errors.append(f"page_chapter[{page}] unknown chapter {cid!r}")
            continue
        if page not in [int(p) for p in chapters[cid].get("pages") or []]:
            errors.append(f"page_chapter[{page}]={cid!r} but page not in chapter.pages")

    return errors


def resolve_map_path(project: Path) -> Path:
    for candidate in (
        project / "nav_map.json",
        project / "sources" / "nav_map.json",
        project / "confirm_ui" / "nav_map.json",
    ):
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        f"nav_map.json not found under {project} (tried root, sources/, confirm_ui/)"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="ppt-master project directory")
    parser.add_argument("--map", type=Path, default=None, help="explicit nav_map.json")
    args = parser.parse_args()
    map_path = args.map or resolve_map_path(args.project.resolve())
    errors = validate(load_map(map_path))
    if errors:
        print(f"[FAIL] {map_path}", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(f"[OK] {map_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
