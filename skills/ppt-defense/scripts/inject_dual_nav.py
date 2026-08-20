#!/usr/bin/env python3
"""Inject dual-layer <g id="nav"> into project SVG slides from nav_map.json."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_nav_map import load_map, resolve_map_path, validate  # noqa: E402

NAV_RE = re.compile(r'<g\b[^>]*\bid="nav"[^>]*>.*?</g>', re.DOTALL)
SVG_OPEN_RE = re.compile(r"<svg\b[^>]*>", re.DOTALL)


def _colors(nav: dict) -> dict[str, str]:
    defaults = {
        "bar": "#0F2747",
        "primary_active": "#2F6FED",
        "primary_text": "#D7E2F0",
        "primary_text_active": "#FFFFFF",
        "secondary_active": "#0D9488",
        "secondary_idle": "#152A45",
        "secondary_text": "#B8C9DC",
        "secondary_text_active": "#FFFFFF",
        "divider": "#1B3A5C",
        "page_chip": "#9EB0C5",
    }
    defaults.update(nav.get("colors") or {})
    return defaults


def _font(nav: dict) -> str:
    return nav.get("font_family") or (
        "PingFang SC, Inter, Microsoft YaHei, Arial, sans-serif"
    )


def build_nav_svg(nav: dict, page: int) -> str:
    total = int(nav["total_pages"])
    page_chapter = {str(k): v for k, v in nav["page_chapter"].items()}
    chapters = nav["chapters"]
    primary = nav["primary"]
    c = _colors(nav)
    font = _font(nav)
    active_chapter = page_chapter[str(page)]

    # Primary slots: leave right margin for page chip
    left, right = 24.0, 1180.0
    n = len(primary)
    slot_w = (right - left) / n
    parts: list[str] = [
        '  <g id="nav" data-pptx-bounds="0 0 1280 68">',
        f'    <rect x="0" y="0" width="1280" height="68" fill="{c["bar"]}"/>',
    ]
    for i, item in enumerate(primary):
        x = left + i * slot_w
        cid = item["id"]
        label = item["label"]
        first = int(item["first_page"])
        active = cid == active_chapter
        fill = c["primary_active"] if active else c["bar"]
        text_fill = c["primary_text_active"] if active else c["primary_text"]
        weight = "600" if active else "400"
        cx = x + slot_w / 2
        parts.append(f'    <a href="#slide-{first}">')
        parts.append(
            f'      <rect x="{x:.1f}" y="4" width="{slot_w:.1f}" height="28" fill="{fill}"/>'
        )
        parts.append(
            f'      <text x="{cx:.1f}" y="24" text-anchor="middle" fill="{text_fill}" '
            f'font-family="{font}" font-size="12" font-weight="{weight}">{label}</text>'
        )
        parts.append("    </a>")

    parts.append(
        f'    <text x="1236" y="24" text-anchor="end" fill="{c["page_chip"]}" '
        f'font-family="{font}" font-size="12" font-weight="400">{page}/{total}</text>'
    )
    parts.append(
        f'    <rect x="0" y="36" width="1280" height="1" fill="{c["divider"]}"/>'
    )

    chapter = chapters[active_chapter]
    pages = [int(p) for p in chapter["pages"]]
    labels = list(chapter.get("secondary_labels") or [])
    if len(pages) >= 2:
        sec_left, sec_right = 48.0, 1232.0
        sec_w = (sec_right - sec_left) / len(pages)
        gap = 8.0
        inner_w = sec_w - gap
        for i, (p, label) in enumerate(zip(pages, labels)):
            x = sec_left + i * sec_w + gap / 2
            active = p == page
            fill = c["secondary_active"] if active else c["secondary_idle"]
            text_fill = (
                c["secondary_text_active"] if active else c["secondary_text"]
            )
            weight = "600" if active else "400"
            cx = x + inner_w / 2
            parts.append(f'    <a href="#slide-{p}">')
            parts.append(
                f'      <rect x="{x:.1f}" y="40" width="{inner_w:.1f}" height="24" fill="{fill}"/>'
            )
            parts.append(
                f'      <text x="{cx:.1f}" y="57" text-anchor="middle" fill="{text_fill}" '
                f'font-family="{font}" font-size="12" font-weight="{weight}">{label}</text>'
            )
            parts.append("    </a>")

    parts.append("  </g>")
    return "\n".join(parts) + "\n"


def page_number_from_svg(path: Path) -> int | None:
    stem = path.stem
    m = re.fullmatch(r"P0*([1-9][0-9]*)", stem, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"(\d+)", stem)
    return int(m.group(1)) if m else None


def inject_file(path: Path, nav_svg: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if NAV_RE.search(text):
        new_text = NAV_RE.sub(nav_svg.rstrip() + "\n", text, count=1)
    else:
        m = SVG_OPEN_RE.search(text)
        if not m:
            raise ValueError(f"no <svg> root in {path}")
        insert_at = m.end()
        new_text = text[:insert_at] + "\n" + nav_svg + text[insert_at:]
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def list_svgs(svg_dir: Path) -> list[Path]:
    files = sorted(svg_dir.glob("P*.svg"))
    if not files:
        files = sorted(svg_dir.glob("*.svg"))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="ppt-master project directory")
    parser.add_argument("--map", type=Path, default=None)
    parser.add_argument(
        "--svg-dir",
        type=Path,
        default=None,
        help="defaults to <project>/svg_output",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    project = args.project.resolve()
    map_path = args.map or resolve_map_path(project)
    nav = load_map(map_path)
    errors = validate(nav)
    if errors:
        for err in errors:
            print(f"[FAIL] {err}", file=sys.stderr)
        return 1

    svg_dir = (args.svg_dir or (project / "svg_output")).resolve()
    if not svg_dir.is_dir():
        print(f"[FAIL] missing svg dir: {svg_dir}", file=sys.stderr)
        return 1

    changed = 0
    for path in list_svgs(svg_dir):
        page = page_number_from_svg(path)
        if page is None or page < 1 or page > int(nav["total_pages"]):
            print(f"[SKIP] {path.name}: cannot map to page index")
            continue
        nav_svg = build_nav_svg(nav, page)
        if args.dry_run:
            print(f"[DRY] would update {path.name} (page {page})")
            continue
        if inject_file(path, nav_svg):
            changed += 1
            print(f"[OK] {path.name}")
        else:
            print(f"[SAME] {path.name}")
    print(f"[DONE] updated={changed} map={map_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
