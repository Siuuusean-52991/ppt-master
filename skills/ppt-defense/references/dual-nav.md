# Dual-layer navigation (PPT Defense)

## Default policy

**ON by default** for every deck generated through PPT Defense.

- Add dual-nav unless the user explicitly says not to
  (e.g.「不要导航栏」「去掉顶栏」「no navigation」「without nav bar」).
- Do not treat “marketing deck” / “普通 PPT” as an implicit opt-out.
- If nav was on and the user only edits content, keep or refresh nav.

## Goal

Let the speaker answer **interrupt questions** by jumping to the right chapter
and page in one or two clicks—without exiting slideshow or hunting the outline.

## Layout (16:9, 1280×720)

| Region | Bounds (typical) | Height |
|---|---|---|
| Primary + secondary stack | `data-pptx-bounds="0 0 1280 68"` | 68px |
| Primary row | y≈0–35 | dark bar `#0F2747` |
| Divider | y≈36 | `#1B3A5C` |
| Secondary row | y≈40–64 | only if chapter has ≥2 pages |
| Body | below nav; keep titles clear of y=76+ |

Page index chip (optional): top-right `N/TOTAL`, muted `#9EB0C5`.

## Primary bar

- Labels = chapter names (short: ≤6 Chinese chars or one English token).
- Equal-width slots across usable width (leave margin for page chip if used).
- Active chapter: fill accent (e.g. `#2F6FED`), text white / semibold.
- Inactive: bar color, text `#D7E2F0`.
- Each slot wraps `<a href="#slide-N">` where **N = chapter’s first page**.

## Secondary bar

- Render **only** when `len(pages_in_active_chapter) >= 2`.
- Equal-width slots for those pages only.
- Active page: teal `#0D9488`, white text.
- Inactive: `#152A45`, text `#B8C9DC`.
- Each slot → `#slide-N` for that page.

Single-page chapters: draw primary only (taller primary OK) or keep 68px with
empty secondary—prefer **hide secondary** to avoid dead clicks.

## `nav_map.json` shape

```json
{
  "total_pages": 21,
  "primary": [
    {"id": "intro", "label": "介绍", "first_page": 1},
    {"id": "open", "label": "开场", "first_page": 2},
    {"id": "overview", "label": "总览", "first_page": 4}
  ],
  "chapters": {
    "open": {"pages": [2, 3], "secondary_labels": ["结论", "议程"]},
    "overview": {"pages": [4, 5], "secondary_labels": ["地图", "职责"]}
  },
  "page_chapter": {
    "1": "intro",
    "2": "open",
    "3": "open",
    "4": "overview",
    "5": "overview"
  },
  "colors": {
    "bar": "#0F2747",
    "primary_active": "#2F6FED",
    "secondary_active": "#0D9488",
    "secondary_idle": "#152A45",
    "divider": "#1B3A5C"
  }
}
```

Rules:

1. Every page `1..total_pages` appears in exactly one chapter via `page_chapter`.
2. `primary[].first_page` must equal `min(chapters[id].pages)`.
3. `secondary_labels` length must match `pages` when length ≥ 2.
4. Hyperlink targets are **only** `#slide-N` (ppt-master contract).

## SVG snippet pattern

```xml
<g id="nav" data-pptx-bounds="0 0 1280 68">
  <rect x="0" y="0" width="1280" height="68" fill="#0F2747"/>
  <a href="#slide-2">
    <rect .../>
    <text ...>开场</text>
  </a>
  <!-- … -->
  <rect x="0" y="36" width="1280" height="1" fill="#1B3A5C"/>
  <a href="#slide-2">…</a>
  <a href="#slide-3">…</a>
</g>
```

Replace the whole `<g id="nav">…</g>` with `inject_dual_nav.py` rather than
hand-editing per page when the map changes.

## Design do’s / don’ts

- Do keep primary labels stable across the whole deck.
- Do rename secondary labels when chapter structure changes; re-inject.
- Don’t put body CTAs in the nav band.
- Don’t use URL hyperlinks for in-deck jumps.
- Don’t invent chapters that don’t map to real pages.
