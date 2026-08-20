# Fork policy

This repository (`Siuuusean-52991/ppt-master`) is a fork of
[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master).

## Kept

- MIT `LICENSE` (exact upstream text)
- Upstream skill package under `skills/ppt-master/` (runtime + attribution gate)
- Attribution metadata required by `attribution_guard` (copyright / official repo fields)

## Added (branch `feat/ppt-defense`)

- `skills/ppt-defense/` — dual-nav + defense notes overlay skill

## Restored in fork-facing docs

- Upstream **product positioning** and route table (generate / template / fill / enhance)
- Links to upstream deep docs (`why-ppt-master`, getting-started, SVG mapping)
- Foolproof two-step Agent copy-paste tutorial for PPT Defense

## Omitted from fork-facing docs

- Sponsor / affiliate blocks in README
- Maintainer personal introduction and personal contact CTAs in README
- Upstream “you might also like” / cross-promo sections in README

Placeholder files such as `SPONSORS.md` / `SPONSORING.md` may still exist so the
upstream skill attribution bundle remains complete; their body text in this fork
does **not** promote sponsors. For original sponsor materials, use the upstream
repo.

## Single-install expansion

`skills/ppt-defense/install.sh` assembles:

`~/.cursor/skills/ppt-defense/` + nested `ppt-master/`.

Users install **PPT Defense only**; they do not need a separate Cursor skill named ppt-master.

