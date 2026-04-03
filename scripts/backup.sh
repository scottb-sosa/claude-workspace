#!/bin/bash
# Auto-backup workspace to GitHub
# Run manually or called automatically at session end

WORKSPACE="/Users/scottbradley/Desktop/Claude/claude workspace template (TPAI)"

cd "$WORKSPACE" || exit 1

# Check if there's anything to commit
if git diff --quiet && git diff --cached --quiet; then
    echo "Nothing to backup — workspace is up to date."
    exit 0
fi

git add -A
git commit -m "Auto-backup: $(date '+%Y-%m-%d %H:%M')"
git push origin main

echo "Workspace backed up to GitHub."
