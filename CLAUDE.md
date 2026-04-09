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
- Put durable synthesis into `wiki/`, `projects/<name>/notes/`, `index.md`, or the vault log layer (`log.md` + `sources/log/`) instead of back-writing it into raw notes.

## Pending / Drop Zone

- Check `pending/` at the start of each session - if files exist, offer to sort them
- See `SCHEMA.md -> SORT Operation` for the workflow

## File Creation Gate (triggers on every Write to the vault)

**Two-phase contract. Most failures happen because agents write first and validate second — pre-write phase eliminates this.**

### Phase 1 — Pre-Write (resolve BEFORE calling Write tool)

1. **type:** — Check SCHEMA.md type list. Pick existing. Add new type to list FIRST if needed.
2. **tags:** — Check `index.md` tag registry. Select existing tags only. Add new ones to registry FIRST. Avoid over-granular tags (e.g. `task1`, `task2`) — use reusable domain tags.
3. **New project?** — You will need to update BOTH `briefing.md` Active Projects AND `context/now.md` Active Projects in this session. These two lists must always match.

### Phase 2 — Post-Write (run immediately after Write, before any other action)

| Check | Condition | Action |
|-------|-----------|--------|
| Index entry | File is in `wiki/`, `learning/`, `references/`, or `projects/` | Add entry to `index.md` under correct section + bump page count |
| New directory | File is in a directory not listed in SCHEMA.md Directory Map | Add directory row to SCHEMA.md Directory Map |
| Active Projects sync | File is a new project README | Add to `briefing.md` Active Projects AND `context/now.md` Active Projects — both, not one |
| briefing.md Navigation | File is a global utility hub (protocol, schema, non-project reference) | Add to Navigation only — do NOT add active projects here, Active Projects already routes to them |
| Context shift | File changes what agents should know on next session start | Update `context/now.md` Vault Status AND Active Projects if applicable |

See `SCHEMA.md → File Creation Gate` for the full contract with rationale.

---

## After Every Task

**This is mandatory, not optional.** Before ending your response:

1. Self-healing pass on every page you touched or read:
   - Missing `updated` date? Add today's date.
   - Missing `> TL;DR`? Generate one.
   - Obvious missing wikilinks? Add them.
2. Log to the current day file in `sources/log/days/`. Even if nothing was fixed, log what you did. No exceptions.
   - Format: `## [YYYY-MM-DD] ACTION | Subject` - see `SCHEMA.md -> Self-Healing Protocol`
   - Then sync `log.md` directly with the Edit tool — see `sources/log/HOW_TO_WRITE.md -> Syncing log.md`
3. If user revealed new context in conversation (personal info, project status, priorities), update `context/me.md`, `context/now.md`, or `context/goals.md` as appropriate - log as `UPDATE | context`.

See `SCHEMA.md -> Self-Healing Protocol` for full rules.
