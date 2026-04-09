# AGENTS.md - Codex Vault Entry Point

> **TL;DR**: Start every session with [[briefing.md]], then [[context/now]], then route through [[SCHEMA.md]] and the relevant project README before touching deeper vault or repo content.

Last updated: 2026-04-09

## Quick Start

**Read in order. Do not open any content file before completing Step 1.**

1. Read `briefing.md` - vault orientation. Do this before anything else, including `context/` files.
2. Read `context/now.md` - current priorities. Do this before reading project or wiki files.
3. Use `SCHEMA.md -> Canonical Startup Matrix` to choose the next page only if the next step is not obvious from the task.
4. If the task touches an active or named project, open `projects/<name>/README.md` before reading project notes or raw sources.

**Session start check (run before every task):**
- Is `context/now.md` `updated` date > 7 days ago? -> Flag it, do not act on stale context.
- Does `briefing.md` Active Projects match `context/now.md` Active Projects? -> If not, reconcile before proceeding.
- Files in `pending/`? -> Flag and offer to sort before starting task.
- Did user reveal new personal info or project status in conversation? -> Update `context/` now, before the task.

---

## This Vault

Personal master vault: second brain + project docs. You read and write everything here. The wiki compounds - every ingest makes it richer, every lint keeps it healthy.

See `SCHEMA.md` for the full operations manual.

---

## Codex-Specific Behavior

- Prefer targeted file edits over full rewrites
- Obsidian `[[wikilinks]]` are the internal link format - always use these, not markdown URLs
- Frontmatter YAML must be valid - consistent quoting, no tabs
- When running shell commands, prefer reading files directly over piping through grep/sed
- `log.md` is the activity-log navigation file; the real daily logs live under `sources/log/days/`
- For project work, navigate `README.md -> notes/ -> sources/` unless the task explicitly requires raw-source-first reading
- Treat project README pages as routing hubs, not passive project descriptions
- If a project has domain hubs, use them as suggestion menus to find one likely next page; do not treat them as mandatory syllabi
- Treat `journal/daily/` as human-primary raw capture. Do not rewrite it into agent voice unless the task explicitly calls for it.
- Put durable synthesis into `wiki/`, `projects/<name>/notes/`, `index.md`, or the vault log layer (`log.md` + `sources/log/`) instead of back-writing it into raw notes.

## Pending / Drop Zone

- Check `pending/` at the start of each session - if files exist, offer to SORT them
- See `SCHEMA.md -> SORT Operation` for the workflow

## After Every Task

**This is mandatory, not optional.** Before ending your response:

1. Self-healing pass on every page you touched or read:
   - Missing `updated` date? Add today's date.
   - Missing `> TL;DR`? Generate one.
   - Obvious missing wikilinks? Add them.
2. Log to the current day file in `sources/log/days/`. Even if nothing was fixed, log what you did. No exceptions.
   - Format: `## [YYYY-MM-DD] ACTION | Subject` - see `SCHEMA.md -> Self-Healing Protocol`
   - Then sync `log.md` directly with the Edit tool — see `sources/log/HOW_TO_WRITE.md -> Syncing log.md`
1. If user revealed new context in conversation (personal info, project status, priorities), update `context/me.md`, `context/now.md`, or `context/goals.md` as appropriate - log as `UPDATE | context`.
2. If the response created durable knowledge, changed the wiki structure, or ingested sources, write those updates before sending the response. Do not wait for a special session-end signal.

See `SCHEMA.md -> Self-Healing Protocol` for full rules.

Stable router pages already validated earlier the same day do not need repeated structural repair passes if they were not edited in the current task; follow `SCHEMA.md -> Stable Router Exception`.
