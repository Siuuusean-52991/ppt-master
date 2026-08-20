# Defense speaker notes (PPT Defense)

## Goal

Notes are a **rebuttal script** for oral defense / interview Q&A—not a second
slide essay.

## Format (required)

Per page file under `notes/` (name matches SVG stem), or sections inside
`notes/total.md` then split:

```text
Q: <one concrete challenge about a visible claim or element>
A: <spoken answer; facts only; admit gaps>

Q: <next challenge>
A: <answer>
```

- Blank line between pairs.
- Do **not** prefix with「面试官问」/「答辩人答」—`Q:` / `A:` only.
- Prefer 3–6 pairs per page; cover title + each major block.

## Content rules

1. Challenge **what is on the slide** (numbers, ownership, method names).
2. No unverifiable metrics. If unknown: say so in `A:`.
3. One idea per `A:`; avoid nested bullets inside answers.
4. Align terminology with on-slide glosses when present.
5. After structural edits to a page, refresh that page’s notes the same turn.

## Anti-patterns

- Dumping the whole resume into every page.
- Marketing adjectives without a checkable fact.
- Questions that cannot be answered from project evidence.
- Overwriting `notes/` without keeping a timestamped export of the PPTX.

## Export

Use ppt-master notes embedding (`svg_to_pptx` with notes enabled). Verify in
PowerPoint **Notes** pane, not only in markdown.
