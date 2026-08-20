# PPT Master (fork) + PPT Defense

[English](./README.md) | [中文](./README_CN.md)

> Fork of [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) (MIT).  
> Branch [`feat/ppt-defense`](https://github.com/Siuuusean-52991/ppt-master/tree/feat/ppt-defense): **PPT Defense = expansion pack** — install **one** Cursor skill to get full ppt-master **plus** dual-nav / defense notes.

---

## Foolproof start (copy to your Agent)

### Step 1 — Install **only** PPT Defense

```text
Please search GitHub for the skill “PPT Defense”
(repo Siuuusean-52991/ppt-master, branch feat/ppt-defense) and install it
as a SINGLE Cursor skill expansion pack:

Goal layout:
  ~/.cursor/skills/ppt-defense/
    SKILL.md
    ppt-master/     ← nested full upstream engine
    scripts/ …      ← defense helpers

How:
1) Sparse-clone or fetch skills/ppt-defense + skills/ppt-master from that branch
   (or reuse an existing ppt-master copy as --master-src).
2) Run: ./skills/ppt-defense/install.sh -y
3) Confirm ~/.cursor/skills/ppt-defense/ppt-master/scripts/attribution_guard.py passes.
4) Do NOT ask me to install a separate ppt-master skill — it’s already nested.
```

### Step 2 — Generate

Drop materials into chat, then:

```text
Use PPT Defense to build a PPT from my materials.

I only installed PPT Defense — use its nested ppt-master engine.
If this is for an interview/defense: add dual-layer #slide-N navigation and
Q:/A: speaker notes. Export a native editable .pptx.
Don’t invent unverifiable metrics.
```

---

## What “one install” means

| Layer | Location after install | Capabilities |
|---|---|---|
| **ppt-master** (engine) | `~/.cursor/skills/ppt-defense/ppt-master/` | Generate / template / fill / enhance → native PPTX |
| **PPT Defense** (expansion) | `~/.cursor/skills/ppt-defense/` | Dual-layer nav + defense `Q:`/`A:` notes |

Cursor only needs to discover **`ppt-defense`**. See [`skills/ppt-defense/BUNDLE.md`](./skills/ppt-defense/BUNDLE.md).

---

## What you get

### From upstream PPT Master (nested engine)

**Editable is table stakes — the real question is how much of PowerPoint you actually get.** PPT Master targets PowerPoint’s native object model in depth: native shapes and connectors with adjustment handles, data-backed charts and tables on demand, and the full text / picture / fill / effect model — click an element and keep editing it as a real PowerPoint object. Through the template / structured route, it can also produce decks with real slide masters and layouts (`p:sldMaster` / `p:sldLayout`).

It is a **workflow skill** inside an agent-capable AI tool: you say “make a deck from this PDF,” it runs on your machine and exports a natively editable `.pptx`.

Main routes:

| Route | What it does |
|---|---|
| **Generate** | Document / topic → designed SVG pages → native PPTX |
| **Create Template** | Distill reusable brand / style / layout / deck templates |
| **Fill Native PPTX** | Fill an existing `.pptx` while preserving design |
| **Enhance Native PPTX** | Add transitions, animations, narration to a finished deck |

- **Predictable cost** — open source; you only pay for the AI model you use  
- **Data stays local** — aside from model API calls, the pipeline runs on your machine  
- **No platform lock-in** — any agent-capable AI IDE can drive it  

> [!IMPORTANT]
> ### Tool ≠ wishing well
> `harness + model = agent` — the workflow is ours; the **model** sets the ceiling. Prefer a strong long-context model for source-heavy decks. Don’t expect a perfect one-shot.

Upstream deep docs: [Why PPT Master](./docs/why-ppt-master.md) · [Getting Started](./docs/getting-started.md) · [PowerPoint ↔ SVG Mapping](./docs/powerpoint-svg-mapping.md)

### From PPT Defense (expansion)

| Feature | Why it matters |
|---|---|
| **Dual-layer nav** | Chapter + page jumps during Q&A |
| **`nav_map.json`** | Single source of truth for structure |
| **Defense notes** | `Q:` / `A:` rebuttal scripts in Notes pane |
| **`install.sh`** | One-folder Cursor install |

---

## Manual install

```bash
git clone --filter=blob:none --sparse -b feat/ppt-defense \
  https://github.com/Siuuusean-52991/ppt-master.git
cd ppt-master
git sparse-checkout set skills/ppt-defense skills/ppt-master
./skills/ppt-defense/install.sh -y
```

If you already have ppt-master elsewhere:

```bash
./skills/ppt-defense/install.sh -y --master-src /path/to/ppt-master
```

---

## License & attribution

- License: [MIT](./LICENSE)
- Upstream: [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- Expansion: `skills/ppt-defense/`

Sponsor marketing / maintainer personal bio omitted in this fork’s README. Nested `ppt-master/` keeps the files required by `attribution_guard`.
