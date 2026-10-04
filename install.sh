#!/usr/bin/env bash
# Install or update writing-skill as a personal Claude Code skill.
# Usage: bash install.sh [target folder]
# Default target: ~/.claude/skills/writing-skill
# Running it again updates the skill to the latest version.
set -euo pipefail

REPO="https://github.com/svx2027/sv-writing.git"
TARGET="${1:-$HOME/.claude/skills/writing-skill}"

if [ -d "$TARGET/.git" ]; then
  echo "Updating $TARGET"
  git -C "$TARGET" pull --ff-only
elif [ -e "$TARGET" ]; then
  echo "$TARGET already exists and is not a git checkout. Move it away, then run this again." >&2
  exit 1
else
  mkdir -p "$(dirname "$TARGET")"
  git clone "$REPO" "$TARGET"
fi

version=$(grep -m1 'version:' "$TARGET/SKILL.md" | tr -dc '0-9.')
echo "writing-skill $version is installed at $TARGET"
echo "In Claude Code, type /writing-skill or just ask for writing help."
