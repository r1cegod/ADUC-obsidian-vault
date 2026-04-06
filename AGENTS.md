# AGENTS.md — Codex Vault Entry Point

## Quick Start

1. Read `briefing.md` for vault orientation (always do this first)
2. Read `SCHEMA.md` for wiki operations (ingest, query, lint)
3. Read `context/now.md` for current priorities

---

## This Vault

Personal master vault: second brain + project docs. You read and write everything here. The wiki compounds — every ingest makes it richer, every lint keeps it healthy.

See `SCHEMA.md` for the full operations manual.

---

## Codex-Specific Behavior

- Prefer targeted file edits over full rewrites
- Obsidian `[[wikilinks]]` are the internal link format — always use these, not markdown URLs
- Frontmatter YAML must be valid — consistent quoting, no tabs
- When running shell commands, prefer reading files directly over piping through grep/sed

## Pending / Drop Zone

- Check `pending/` at the start of each session — if files exist, offer to SORT them
- See `SCHEMA.md → SORT Operation` for the workflow

## After Every Task

Before ending your response, do a quick self-healing pass on any pages you touched or read:
- Missing `updated` date? Add today's date.
- Missing `> TL;DR`? Generate one.
- Obvious missing wikilinks? Add them.
- Log any auto-fixes to `log.md`.

See `SCHEMA.md → Self-Healing Protocol` for the full rules.
