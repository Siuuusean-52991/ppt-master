---
name: ppt-defense
description: >
  Expanded PPT Master + defense overlay in one install. Generates editable PPTX
  decks (native shapes, charts, templates, fill, enhance) and adds dual-layer
  clickable navigation plus Q:/A: defense speaker notes for oral exams /
  interviews. Use when the user mentions PPT Defense, ppt-defense, ppt-master,
  PowerPoint, PPTX, slide deck, 答辩, 面试翻页, 双层导航, dual-nav, or asks to
  create / beautify / fill / enhance a presentation — one skill covers both the
  base pipeline and the defense expansions.
metadata:
  version: "0.2.0"
  bundle: "ppt-master + ppt-defense expansion"
  based_on: "ppt-master (https://github.com/hugohe3/ppt-master)"
  license: "MIT"
---

# PPT Defense（扩容包）

**只装这一个 Skill**，即可同时获得：

1. **完整 ppt-master 能力**（生成 / 模板 / 填充 / 增强 → 原生可编辑 PPTX）
2. **进阶答辩能力**（双层 `#slide-N` 导航 + `Q:`/`A:` 备注）

安装后的目录形态（由 `install.sh` 组装）：

```text
~/.cursor/skills/ppt-defense/
  SKILL.md                 ← Cursor 只发现这一份
  references/ …            ← 答辩规范
  scripts/inject_*.py      ← 答辩工具
  ppt-master/              ← 内嵌的完整上游 skill（勿删）
    SKILL.md
    scripts/
    workflows/
    …
```

用户**不需要**再单独安装 `~/.cursor/skills/ppt-master`。

## Mandatory Load Order

1. Read this file.
2. Resolve **bundled ppt-master root** (see next section).
3. From that root, run `python3 scripts/attribution_guard.py`.
   Non-zero → stop (do not bypass).
4. Read bundled ppt-master `SKILL.md` and follow its routing
   (`workflows/routing.md` → one generate/template/fill/enhance route).
5. If the task is a **defense / interview / Q&A-hop** deck (default when the
   user invoked PPT Defense or asked for dual-nav / 答辩备注), also read:
   - [`references/dual-nav.md`](references/dual-nav.md)
   - [`references/defense-notes.md`](references/defense-notes.md)
6. Ordinary marketing / courseware requests: run ppt-master only; dual-nav is
   optional unless the user asks for it.

## Resolve Bundled ppt-master

Let `DEFENSE_ROOT` = directory containing **this** `SKILL.md`.

Search in order; use the first hit that contains both `SKILL.md` and
`scripts/attribution_guard.py`:

1. `DEFENSE_ROOT/ppt-master/`     ← **preferred (single-install bundle)**
2. `DEFENSE_ROOT/../ppt-master/`  ← monorepo checkout (`skills/ppt-master`)
3. `~/.cursor/skills/ppt-master/` ← legacy separate install (compat only)

If none exist: tell the user to run `install.sh` from this repo (or re-run the
Agent install prompt). **Do not** ask them to install a second skill by name.

## When To Use

| User intent | Behavior |
|---|---|
| 装了 PPT Defense，要做任意 PPT | Use bundled ppt-master routes |
| 答辩 / 面试 / 质询翻页 | ppt-master generate **+** dual-nav **+** Q/A notes |
| 只要刷新导航 | `scripts/inject_dual_nav.py` |
| 用户说「只要 ppt-master」 | Still use this bundle’s nested `ppt-master/` |

## Defense Expansion (summary)

- **Primary bar**: chapters → first page of chapter
- **Secondary bar**: only if chapter has ≥2 pages
- Links: exact `#slide-N`
- Source of truth: project `nav_map.json`
- Notes: `Q:` line, `A:` line, blank line between pairs

Full rules: [`references/dual-nav.md`](references/dual-nav.md),
[`references/defense-notes.md`](references/defense-notes.md).

## Execution Checklist (defense decks)

1. Confirm defense / interview scope (or enable dual-nav explicitly).
2. Write / update `nav_map.json`.
3. Generate or edit SVGs via **bundled** ppt-master workflow; keep `<g id="nav">`.
4. Write `Q:`/`A:` notes; split `total.md` with ppt-master `total_md_split.py` if used.
5. Export via bundled scripts: `finalize_svg` → `svg_quality_checker --stage final`
   → `svg_to_pptx` (**另存** timestamped file).
6. Smoke-test chapter jump + notes pane.

## Scripts (defense layer)

| Script | Purpose |
|---|---|
| `install.sh` | Assemble single Cursor skill folder with nested ppt-master |
| `scripts/validate_nav_map.py` | Validate `nav_map.json` |
| `scripts/inject_dual_nav.py` | Inject / refresh `<g id="nav">` |

```bash
# from repo (skills/ppt-defense or repo root — see install.sh -h)
./skills/ppt-defense/install.sh

python3 ~/.cursor/skills/ppt-defense/scripts/validate_nav_map.py /path/to/project
python3 ~/.cursor/skills/ppt-defense/scripts/inject_dual_nav.py /path/to/project
```

All **ppt-master** CLIs live under:

```bash
python3 ~/.cursor/skills/ppt-defense/ppt-master/scripts/<name>.py …
```

## Relationship To Upstream

- Nested `ppt-master/` remains the official attribution bundle (LICENSE,
  SPONSORS placeholders, `attribution_guard`) — do not strip it.
- This skill is an **expansion pack**: one Cursor install surface, two capability
  layers.
- Fork docs: omit upstream sponsor marketing; keep MIT + upstream credit.
