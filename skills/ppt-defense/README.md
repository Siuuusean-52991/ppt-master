# PPT Defense

Overlay skill for **答辩 / 面试 / 质询** PowerPoint decks, built on
[PPT Master](https://github.com/hugohe3/ppt-master) (MIT).

## What it adds

1. **Dual-layer navigation** — chapter bar + in-chapter sub-bar with `#slide-N`
   jumps for rapid Q&A hopping
2. **Defense notes** — speaker notes as `Q:` / `A:` rebuttal pairs
3. Helpers — `nav_map.json` validation + SVG nav injection

## Install (Cursor)

Copy or symlink this directory to:

```text
~/.cursor/skills/ppt-defense
```

Keep upstream PPT Master installed at `~/.cursor/skills/ppt-master` (required).

## Quick use

1. Build the deck with **ppt-master** as usual.
2. Add `nav_map.json` to the project (see `examples/nav_map.example.json`).
3. Inject nav into SVGs:

```bash
python3 skills/ppt-defense/scripts/validate_nav_map.py /path/to/project
python3 skills/ppt-defense/scripts/inject_dual_nav.py /path/to/project
```

4. Write `notes/` with `Q:` / `A:` pairs; export via ppt-master `svg_to_pptx`.

## Attribution

- Base workflow / runtime: © Hugo He — [ppt-master](https://github.com/hugohe3/ppt-master)
- PPT Defense overlay: additive skill on this fork branch `feat/ppt-defense`
