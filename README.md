# PPT Master (fork) + PPT Defense

[English](./README.md) | [中文](./README_CN.md)

> This repository is a **fork** of [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) (MIT).  
> Branch [`feat/ppt-defense`](https://github.com/Siuuusean-52991/ppt-master/tree/feat/ppt-defense) adds the **PPT Defense** overlay skill for oral defense / interview decks.

## What this fork is for

| Layer | Role |
|---|---|
| **ppt-master** (upstream skill) | Generate native editable PPTX from documents / briefs (SVG → quality gate → PPTX) |
| **PPT Defense** (`skills/ppt-defense`) | Dual-layer clickable navigation + defense-style `Q:` / `A:` speaker notes for rapid Q&A jumping |

Use this fork when you need a **答辩 / 面试 / 质询** deck you can hop through under pressure—not a marketing landing page.

## PPT Defense (this branch)

Path: [`skills/ppt-defense/`](./skills/ppt-defense/)

1. Dual-layer nav: primary = chapters → first page of chapter; secondary = pages inside the active chapter (`#slide-N` links).
2. Notes format: `Q:` / `A:` pairs in `notes/` for rebuttal scripts.
3. Helpers: `nav_map.json` validate + inject into SVG.

### Cursor install

```bash
# Upstream runtime (required)
# keep or install skills/ppt-master → ~/.cursor/skills/ppt-master

# Overlay
cp -R skills/ppt-defense ~/.cursor/skills/ppt-defense
# or: ln -s "$PWD/skills/ppt-defense" ~/.cursor/skills/ppt-defense
```

### Project quick path

```bash
# after ppt-master has produced <project>/svg_output/
python3 skills/ppt-defense/scripts/validate_nav_map.py /path/to/project
python3 skills/ppt-defense/scripts/inject_dual_nav.py /path/to/project
# then finalize + export with ppt-master scripts as usual
```

See [`skills/ppt-defense/README.md`](./skills/ppt-defense/README.md) and [`skills/ppt-defense/SKILL.md`](./skills/ppt-defense/SKILL.md).

## Upstream ppt-master

Deck generation, templates, quality gates, and export still follow the upstream skill:

- Skill entry: [`skills/ppt-master/SKILL.md`](./skills/ppt-master/SKILL.md)
- Official upstream: https://github.com/hugohe3/ppt-master

Do **not** remove `LICENSE`, skill attribution metadata, or `attribution_guard` gates.

## Documentation map

| Doc | Purpose |
|---|---|
| [`skills/ppt-defense/`](./skills/ppt-defense/) | Defense overlay (this fork’s focus) |
| [`skills/ppt-master/`](./skills/ppt-master/) | Upstream generation skill |
| [`docs/FORK.md`](./docs/FORK.md) | What this fork keeps / omits vs upstream |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | Upstream contribution notes (PRs to upstream go there) |

## License & attribution

- License: [MIT](./LICENSE) (unchanged from upstream).
- Upstream author / project: [Hugo He / ppt-master](https://github.com/hugohe3/ppt-master).
- This fork’s additive work: PPT Defense skill under `skills/ppt-defense/`.

Sponsor placements, affiliate blocks, and maintainer personal bio sections from the upstream README are **omitted in this fork**. If you need those materials, see the [upstream repository](https://github.com/hugohe3/ppt-master).
