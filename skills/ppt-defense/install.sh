#!/usr/bin/env bash
# Assemble a single Cursor skill: ppt-defense + nested ppt-master.
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: install.sh [-y] [--dest DIR] [--master-src DIR] [--defense-src DIR]

Installs ONE Cursor skill that includes full ppt-master + PPT Defense:

  ~/.cursor/skills/ppt-defense/
    SKILL.md
    …
    ppt-master/          # nested upstream skill

Options:
  -y               Non-interactive overwrite
  --dest DIR       Default: ~/.cursor/skills/ppt-defense
  --master-src DIR Default: auto (repo skills/ppt-master or ~/.cursor/skills/ppt-master)
  --defense-src DIR Default: directory of this script
EOF
}

DEST="${HOME}/.cursor/skills/ppt-defense"
MASTER_SRC=""
DEFENSE_SRC=""
YES=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) usage; exit 0 ;;
    -y) YES=1; shift ;;
    --dest) DEST="$2"; shift 2 ;;
    --master-src) MASTER_SRC="$2"; shift 2 ;;
    --defense-src) DEFENSE_SRC="$2"; shift 2 ;;
    --repo-root)
      ROOT="$2"
      MASTER_SRC="${ROOT}/skills/ppt-master"
      DEFENSE_SRC="${ROOT}/skills/ppt-defense"
      shift 2
      ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFENSE_SRC="${DEFENSE_SRC:-${SCRIPT_DIR}}"

if [[ -z "${MASTER_SRC}" ]]; then
  if [[ -f "${SCRIPT_DIR}/../ppt-master/SKILL.md" ]]; then
    MASTER_SRC="$(cd "${SCRIPT_DIR}/../ppt-master" && pwd)"
  elif [[ -f "${HOME}/.cursor/skills/ppt-master/SKILL.md" ]]; then
    MASTER_SRC="${HOME}/.cursor/skills/ppt-master"
  else
    echo "[FAIL] Cannot find ppt-master skill source." >&2
    echo "       Clone branch feat/ppt-defense (skills/ppt-master) or keep a copy at" >&2
    echo "       ~/.cursor/skills/ppt-master, then rerun." >&2
    exit 1
  fi
fi

if [[ ! -f "${DEFENSE_SRC}/SKILL.md" ]]; then
  echo "[FAIL] defense src missing SKILL.md: ${DEFENSE_SRC}" >&2
  exit 1
fi
if [[ ! -f "${MASTER_SRC}/scripts/attribution_guard.py" ]]; then
  echo "[FAIL] master src incomplete: ${MASTER_SRC}" >&2
  exit 1
fi

DEST="$(mkdir -p "$(dirname "${DEST}")" && cd "$(dirname "${DEST}")" && pwd)/$(basename "${DEST}")"
MASTER_SRC="$(cd "${MASTER_SRC}" && pwd)"
DEFENSE_SRC="$(cd "${DEFENSE_SRC}" && pwd)"

echo "[PLAN] defense_src=${DEFENSE_SRC}"
echo "[PLAN] master_src=${MASTER_SRC}"
echo "[PLAN] dest=${DEST}"

if [[ -e "${DEST}" && "${YES}" -ne 1 ]]; then
  if [[ -t 0 ]]; then
    read -r -p "Overwrite ${DEST}? [y/N] " ans
    [[ "${ans}" == "y" || "${ans}" == "Y" ]] || exit 1
  else
    echo "[FAIL] Dest exists; pass -y to overwrite." >&2
    exit 1
  fi
fi

STAGE="$(mktemp -d "${TMPDIR:-/tmp}/ppt-defense-install.XXXXXX")"
cleanup() { rm -rf "${STAGE}"; }
trap cleanup EXIT

mkdir -p "${STAGE}/bundle" "${STAGE}/bundle/ppt-master"

# Stage defense overlay without any nested ppt-master
if command -v rsync >/dev/null 2>&1; then
  rsync -a \
    --exclude 'ppt-master/' \
    --exclude '.venv/' \
    --exclude '__pycache__/' \
    "${DEFENSE_SRC}/" "${STAGE}/bundle/"
  rsync -a \
    --exclude '.venv/' \
    --exclude '__pycache__/' \
    --exclude 'projects/' \
    "${MASTER_SRC}/" "${STAGE}/bundle/ppt-master/"
else
  # cp fallback
  (cd "${DEFENSE_SRC}" && tar cf - \
    --exclude='ppt-master' --exclude='.venv' --exclude='__pycache__' .) \
    | (cd "${STAGE}/bundle" && tar xf -)
  (cd "${MASTER_SRC}" && tar cf - \
    --exclude='.venv' --exclude='__pycache__' --exclude='projects' .) \
    | (cd "${STAGE}/bundle/ppt-master" && tar xf -)
fi

rm -rf "${DEST}"
mkdir -p "$(dirname "${DEST}")"
mv "${STAGE}/bundle" "${DEST}"

chmod +x "${DEST}/install.sh" 2>/dev/null || true
chmod +x "${DEST}/scripts/"*.py 2>/dev/null || true

echo "[CHECK] attribution_guard…"
python3 "${DEST}/ppt-master/scripts/attribution_guard.py"

echo "[OK] Single skill installed: ${DEST}"
echo "     Capabilities: ppt-master (nested) + PPT Defense expansion"
echo "     No separate ppt-master Cursor skill required."
