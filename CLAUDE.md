# CLAUDE.md - Claude Code Vault Entry Point

## Quick Start

**Read in order. Do not open any content file before completing Step 1.**

1. Read `briefing.md` - vault orientation. Do this before anything else, including `context/` files.
2. Read `context/now.md` - current priorities. Do this before reading project files.
3. Read `SCHEMA.md` - only if performing a wiki operation (ingest, query, lint, sort).

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

## Claude Code-Specific Behavior

- Use the `Edit` tool (not bash sed/awk) when modifying markdown files
- Use the `Write` tool when creating new pages from templates
- Use `Glob` and `Grep` to scan wiki pages before creating new ones (avoid duplicates)
- For project routing, prefer the smallest sufficient path after `README.md`; hubs suggest likely entry points but do not impose a fixed reading sequence
- Obsidian `[[wikilinks]]` are the internal link format - always use these, not markdown URLs
- Frontmatter YAML must be valid - no tabs, consistent quoting
- Treat `journal/daily/` as human-primary raw capture. Do not rewrite it into agent voice unless the task explicitly calls for it.
- Put durable synthesis into `wiki/`, `projects/<name>/notes/`, `index.md`, or `log.md` instead of back-writing it into raw notes.

## Pending / Drop Zone

- Check `pending/` at the start of each session - if files exist, offer to sort them
- See `SCHEMA.md -> SORT Operation` for the workflow

## After Every Task

**This is mandatory, not optional.** Before ending your response:

1. Self-healing pass on every page you touched or read:
   - Missing `updated` date? Add today's date.
   - Missing `> TL;DR`? Generate one.
   - Obvious missing wikilinks? Add them.
2. Log to `log.md`. Even if nothing was fixed, log what you did. No exceptions.
   - Format: `## [YYYY-MM-DD] ACTION | Subject` - see `SCHEMA.md -> Self-Healing Protocol`
3. If user revealed new context in conversation (personal info, project status, priorities), update `context/me.md`, `context/now.md`, or `context/goals.md` as appropriate - log as `UPDATE | context`.
4. If the response created durable knowledge, changed the wiki structure, or ingested sources, write those updates before sending the response. Do not wait for a special session-end signal.

See `SCHEMA.md -> Self-Healing Protocol` for full rules.
