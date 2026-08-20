# PPT Defense

Overlay skill for **答辩 / 面试 / 质询** PowerPoint decks, built on
[PPT Master](https://github.com/hugohe3/ppt-master) (MIT).

## Foolproof use (copy-paste)

### 1) Ask your Agent to install

```text
Please search GitHub for “PPT Defense” (Siuuusean-52991/ppt-master, branch
feat/ppt-defense) and install ~/.cursor/skills/ppt-master plus
~/.cursor/skills/ppt-defense for me. Confirm attribution_guard passes.
```

### 2) Drop materials, then generate

```text
Use PPT Defense to generate an interview/defense PPT from my materials:
dual-layer #slide-N navigation, Q:/A: speaker notes, native .pptx via ppt-master.
Don’t invent unverifiable numbers.
```

中文版同样文案见仓库根目录 [`README_CN.md`](../../README_CN.md)。

## What it adds

1. **Dual-layer navigation** — chapter bar + in-chapter sub-bar (`#slide-N`)
2. **Defense notes** — `Q:` / `A:` rebuttal pairs in speaker notes
3. Helpers — `nav_map.json` validate + SVG nav injection

## Manual install

```bash
# from this repo (branch feat/ppt-defense)
cp -R skills/ppt-defense ~/.cursor/skills/ppt-defense
# ppt-master must also exist at ~/.cursor/skills/ppt-master
```

```bash
python3 skills/ppt-defense/scripts/validate_nav_map.py /path/to/project
python3 skills/ppt-defense/scripts/inject_dual_nav.py /path/to/project
```

## Attribution

- Base workflow / runtime: © Hugo He — [ppt-master](https://github.com/hugohe3/ppt-master)
- PPT Defense overlay: `skills/ppt-defense/` on branch `feat/ppt-defense`
