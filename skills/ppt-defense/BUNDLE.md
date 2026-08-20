# Bundle model

PPT Defense is an **expansion pack**: one Cursor skill install unlocks

1. Full upstream **ppt-master** (nested at `ppt-master/`)
2. Defense features (dual-nav + `Q:`/`A:` notes)

## Source layout (git)

```text
skills/ppt-master/     # upstream engine (unchanged attribution bundle)
skills/ppt-defense/    # expansion layer + install.sh
```

## Installed layout (Cursor)

```text
~/.cursor/skills/ppt-defense/
  SKILL.md
  install.sh
  references/
  scripts/
  ppt-master/          # nested copy of skills/ppt-master
```

Do **not** require `~/.cursor/skills/ppt-master` after a successful `install.sh`.

## Install

```bash
# from a checkout of branch feat/ppt-defense
./skills/ppt-defense/install.sh -y
```

Or ask an Agent to search GitHub for **PPT Defense** and run that installer.
