# PPT Master (fork) + PPT Defense

[English](./README.md) | [中文](./README_CN.md)

> Fork of [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) (MIT).  
> Branch [`feat/ppt-defense`](https://github.com/Siuuusean-52991/ppt-master/tree/feat/ppt-defense) adds **PPT Defense** — dual-layer navigation + defense Q&A notes for oral exams / interviews.

---

## Foolproof start (copy to your Agent)

### Step 1 — Install the skill

Paste this to Cursor / Claude Code / Codex / any agent:

```text
Please search GitHub for the skill “PPT Defense” (repo Siuuusean-52991/ppt-master,
branch feat/ppt-defense), then install it for me:

1) Install / sync the upstream ppt-master skill to ~/.cursor/skills/ppt-master
   (from this fork’s skills/ppt-master, or from hugohe3/ppt-master).
2) Install the PPT Defense overlay to ~/.cursor/skills/ppt-defense
   (from skills/ppt-defense on branch feat/ppt-defense).
3) Confirm both folders exist and that ppt-master’s attribution_guard still passes.
```

### Step 2 — Generate a defense deck

Drop your materials into the chat (PDF / DOCX / Markdown / Feishu links / folder), then paste:

```text
Use the PPT Defense skill to make an interview / oral-defense PPT from the materials I just gave you.

Requirements:
- Dual-layer top navigation (chapter bar + in-chapter bar) with #slide-N jumps
- Speaker notes as Q: / A: defense pairs for each page
- Native editable .pptx export via ppt-master
- Do not invent unverifiable metrics; mark honest gaps
```

That’s it. The agent runs ppt-master for generation/export and PPT Defense for nav + notes.

---

## What you get

### From upstream PPT Master (still the engine)

**Editable is table stakes — the real question is how much of PowerPoint you actually get.** PPT Master targets PowerPoint’s native object model in depth: native shapes and connectors with adjustment handles, data-backed charts and tables on demand, and the full text / picture / fill / effect model — click an element and keep editing it as a real PowerPoint object. Through the template / structured route, it can also produce decks with real slide masters and layouts (`p:sldMaster` / `p:sldLayout`).

It is a **workflow skill** inside an agent-capable AI tool: you say “make a deck from this PDF,” it runs on your machine and exports a natively editable `.pptx`. You install Python + an AI agent, then drop in materials — no app coding required.

Main routes (each with an explicit preserve contract):

| Route | What it does |
|---|---|
| **Generate** | Document / topic → designed SVG pages → native PPTX |
| **Create Template** | Distill reusable brand / style / layout / deck templates |
| **Fill Native PPTX** | Fill an existing `.pptx` while preserving design |
| **Enhance Native PPTX** | Add transitions, animations, narration to a finished deck |

Three practical promises from upstream positioning:

- **Predictable cost** — open source; you only pay for the AI model you use
- **Data stays local** — aside from model API calls, the pipeline runs on your machine
- **No platform lock-in** — any agent-capable AI IDE can drive it

> [!IMPORTANT]
> ### Tool ≠ wishing well
> `harness + model = agent` — PPT Master / PPT Defense own the workflow; the **model** sets the ceiling. Prefer a strong long-context model for source-heavy decks. Don’t expect a perfect one-shot; the value is removing most of the tedious work so you can polish a **native** deck.

Deeper upstream docs (unchanged in this fork): [Why PPT Master](./docs/why-ppt-master.md) · [Getting Started](./docs/getting-started.md) · [PowerPoint ↔ SVG Mapping](./docs/powerpoint-svg-mapping.md)

### From PPT Defense (this fork)

| Feature | Why it matters in a defense |
|---|---|
| **Dual-layer nav** | Chapter jump + page jump while answering interruptions |
| **`nav_map.json`** | Single source of truth for chapters / pages / labels |
| **Defense notes** | `Q:` / `A:` rebuttal scripts in the PowerPoint notes pane |
| **Inject / validate scripts** | Refresh nav after page order changes |

Details: [`skills/ppt-defense/`](./skills/ppt-defense/) · policy: [`docs/FORK.md`](./docs/FORK.md)

---

## Manual install (if your Agent needs a path)

```bash
git clone -b feat/ppt-defense https://github.com/Siuuusean-52991/ppt-master.git
cd ppt-master
python3 -m venv .venv && source .venv/bin/activate   # optional but recommended
pip install -r requirements.txt

mkdir -p ~/.cursor/skills
cp -R skills/ppt-master ~/.cursor/skills/ppt-master
cp -R skills/ppt-defense ~/.cursor/skills/ppt-defense

python3 ~/.cursor/skills/ppt-master/scripts/attribution_guard.py
```

Prerequisites: Python 3 + [pandoc](https://pandoc.org/) (see upstream [Windows guide](./docs/windows-installation.md) if needed).

---

## Example Agent prompts (beyond the foolproof pair)

```text
Use PPT Defense. Build a 16:9 defense deck from ./sources/, ~15–20 pages,
chapters: 介绍 / 开场 / 项目 / 方法 / 证据 / 收束. Add dual-nav + Q/A notes.
```

```text
I already have svg_output/. Only refresh dual-nav from nav_map.json using
PPT Defense inject_dual_nav.py, then re-export PPTX (另存, don’t overwrite).
```

---

## License & attribution

- License: [MIT](./LICENSE) (same as upstream)
- Upstream project: [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- This fork’s additive work: `skills/ppt-defense/`

Sponsor blocks and maintainer personal bio from the upstream README are omitted here; see upstream if you need them. Placeholder `SPONSORS.md` files remain only so the official skill attribution gate stays intact.
