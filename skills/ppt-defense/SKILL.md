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
  version: "0.2.1"
  bundle: "ppt-master + ppt-defense expansion"
  based_on: "ppt-master (https://github.com/hugohe3/ppt-master)"
  license: "MIT"
  defaults:
    dual_nav: "on"
---

# PPT Defense（扩容包）

**只装这一个 Skill**，即可同时获得：

1. **完整 ppt-master 能力**（生成 / 模板 / 填充 / 增强 → 原生可编辑 PPTX）
2. **进阶答辩能力**（双层 `#slide-N` 导航 + `Q:`/`A:` 备注）

## Default: dual-nav ON

**凡经本 Skill 生成 / 重画的内容页，默认都带双层导航栏。**

| 情况 | 导航栏 |
|---|---|
| 用户说用 PPT Defense / 做 PPT / 生成答辩稿（未提导航） | **必须加** |
| 用户明确说「不要导航栏 / 去掉顶栏 / no nav / without navigation」 | 不加 |
| 用户只改正文、未否定导航 | **保留或补全**导航 |

Opt-out must be **explicit**. Silence = keep nav. Do not ask “要不要导航” unless the user is undecided after seeing a draft.

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
5. **Always** read [`references/dual-nav.md`](references/dual-nav.md) before
   drawing or exporting pages — unless the user explicitly opted out of nav.
6. Read [`references/defense-notes.md`](references/defense-notes.md) when the
   deck is for 答辩 / 面试 / 质询, or when the user asks for Q&A notes.
   (Nav still defaults ON even if notes are skipped.)

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
| 装了 PPT Defense，要做任意 PPT | Bundled ppt-master **+ dual-nav (default)** |
| 答辩 / 面试 / 质询 | 同上 **+** Q/A notes |
| 明确不要导航栏 | Bundled ppt-master only（no `<g id="nav">`） |
| 只要刷新导航 | `scripts/inject_dual_nav.py` |

## Defense Expansion (summary)

- **Primary bar**: chapters → first page of chapter
- **Secondary bar**: only if chapter has ≥2 pages
- Links: exact `#slide-N`
- Source of truth: project `nav_map.json`
- Notes: `Q:` line, `A:` line, blank line between pairs

Full rules: [`references/dual-nav.md`](references/dual-nav.md),
[`references/defense-notes.md`](references/defense-notes.md).

## Execution Checklist

1. Assume **dual-nav ON** unless user opted out in this turn / prior explicit rule.
2. Write / update `nav_map.json` (required when nav is ON).
3. Generate or edit SVGs via **bundled** ppt-master workflow; every content page
   gets `<g id="nav">` (use `inject_dual_nav.py` to refresh).
4. If 答辩/面试/质询 (or user asked): write `Q:`/`A:` notes; split `total.md` with
   ppt-master `total_md_split.py` if used.
5. Export via bundled scripts: `finalize_svg` → `svg_quality_checker --stage final`
   → `svg_to_pptx` (**另存** timestamped file).
6. Smoke-test: click a chapter + a secondary page (skip if nav opted out).

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
