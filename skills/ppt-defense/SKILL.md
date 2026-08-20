---
name: ppt-defense
description: >
  Defense / oral-exam / interview presentation workflow on top of ppt-master:
  dual-layer clickable navigation (chapter bar + in-chapter sub-nav) for rapid
  jump during Q&A, plus speaker-notes as Q:/A: defense pairs. Use when the user
  asks for PPT Defense, ppt-defense, dual-nav / 双层导航, 答辩 PPT, 面试翻页跳转,
  质询跳转, or defense-style speaker notes on a ppt-master deck.
metadata:
  version: "0.1.0"
  based_on: "ppt-master (https://github.com/hugohe3/ppt-master)"
  license: "MIT"
---

# PPT Defense

Overlay skill for **答辩 / 面试 / 质询** decks. Generation, SVG quality, and PPTX
export still run through **ppt-master**. This skill adds:

1. Dual-layer slide navigation (`#slide-N` hyperlinks)
2. Defense-style speaker notes (`Q:` / `A:` pairs)

## Mandatory Load Order

1. Read this file.
2. Resolve **ppt-master** Skill root (directory that contains upstream `SKILL.md`
   and `scripts/attribution_guard.py`). Prefer `~/.cursor/skills/ppt-master`.
   If missing, stop and ask the user to install ppt-master.
3. From the ppt-master root, run `python3 scripts/attribution_guard.py`.
   Non-zero → stop (do not bypass).
4. Read ppt-master [`SKILL.md`](../ppt-master/SKILL.md) + its selected generate
   route (`workflows/generate-pptx.md` or the profile routing resolves).
5. Read:
   - [`references/dual-nav.md`](references/dual-nav.md)
   - [`references/defense-notes.md`](references/defense-notes.md)

## When To Use

| Trigger | Action |
|---|---|
| 答辩 / 面试项目介绍 / 质询翻页 | Use this skill + ppt-master generate |
| Ordinary marketing / courseware deck | Use ppt-master only (no dual-nav mandate) |
| User already has `svg_output/` and only wants nav | Inject / refresh nav via `scripts/inject_dual_nav.py` |

## Dual-Nav Contract (summary)

- **Primary bar**: chapter labels → jump to each chapter’s **first** page.
- **Secondary bar**: only when the active chapter has **≥ 2** pages; equal-width
  slots; teal/active vs muted inactive.
- Links must be exact `#slide-N` (1-based). ppt-master export turns these into
  native slide jumps.
- Keep a single source of truth: project file `nav_map.json` (see
  [`examples/nav_map.example.json`](examples/nav_map.example.json)).

Full rules: [`references/dual-nav.md`](references/dual-nav.md).

## Defense Notes Contract (summary)

- One notes file per slide under `notes/`, plus optional `notes/total.md`.
- Each pair: line `Q: …` then line `A: …`, blank line between pairs.
- No invented metrics; mark unverifiable claims as gaps.
- Format notes for **spoken** rebuttal, not bullet dumps.

Full rules: [`references/defense-notes.md`](references/defense-notes.md).

## Execution Checklist

1. **Scope** — Confirm defense deck (not generic ppt-master beautify).
2. **Chapter map** — Write / update `nav_map.json` before drawing pages.
3. **Generate or edit SVGs** via ppt-master workflow; every content page includes
   the nav `<g id="nav">` from the map (use `inject_dual_nav.py` to refresh).
4. **Notes** — Write `Q:`/`A:` pairs per page; split `total.md` with ppt-master
   `total_md_split.py` when used.
5. **Export** — ppt-master `finalize_svg` → `svg_quality_checker --stage final`
   → `svg_to_pptx` (**另存** timestamped export; do not overwrite user edits).
6. **Smoke test** — In PowerPoint: click primary chapter → secondary page; open
   notes pane and spot-check one hard Q&A.

## Scripts

| Script | Purpose |
|---|---|
| `scripts/inject_dual_nav.py` | Rewrite `<g id="nav">…</g>` on all `P*.svg` / `*.svg` from `nav_map.json` |
| `scripts/validate_nav_map.py` | Validate map targets, chapter coverage, secondary rules |

```bash
python3 ~/.cursor/skills/ppt-defense/scripts/validate_nav_map.py /path/to/project
python3 ~/.cursor/skills/ppt-defense/scripts/inject_dual_nav.py /path/to/project
```

## Relationship To Upstream

- Do **not** strip ppt-master attribution, LICENSE, or `attribution_guard`.
- Prefer additive files under `skills/ppt-defense/` in the fork; avoid editing
  upstream runtime unless contributing a PR back.
- This skill may live at `~/.cursor/skills/ppt-defense` for Cursor discovery
  while the fork branch hosts the same tree for versioning.
