# PPT Defense

**Expansion pack**: one Cursor install = full **ppt-master** (nested) + defense dual-nav / `Q:`/`A:` notes.

## Foolproof (copy-paste)

### 1) Install only PPT Defense

```text
Search GitHub for “PPT Defense” (Siuuusean-52991/ppt-master, branch feat/ppt-defense).
Run skills/ppt-defense/install.sh -y so that ~/.cursor/skills/ppt-defense contains
a nested ppt-master/. Do NOT install a separate ppt-master skill.
```

### 2) Generate

```text
Use PPT Defense (nested ppt-master) to generate a PPT from my materials.
Dual-layer #slide-N nav is ON by default (say “不要导航栏” only if you want it off).
For interview/defense also add Q:/A: notes. Native .pptx.
```

## Layout after install

```text
~/.cursor/skills/ppt-defense/
  SKILL.md
  ppt-master/          # full upstream engine
  scripts/inject_*.py
  references/
```

See [BUNDLE.md](./BUNDLE.md).

## Attribution

- Nested engine: [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) (MIT)
- Expansion: this folder on branch `feat/ppt-defense`
