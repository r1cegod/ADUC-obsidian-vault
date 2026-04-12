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
- Index drift? Glob a project's notes directory and compare against `index.md` → if pages on disk are missing from the index, flag and add before starting the task.

---

## Tiered Loading Quick Reference

Load context in tiers. Stop after each tier — only descend if the task genuinely needs more. **Full rules in `SCHEMA.md → Tiered Loading Protocol`.**

```
Pre     context/hot.md                 ← ALWAYS first. Lists stable routers that
                                          skip repair pass. Update at task end.
Tier 0  briefing.md                    ← ALWAYS. Stop if the task is simple.
Tier 1  context/now.md + SCHEMA.md     ← add for wiki ops or live priorities
Tier 2  projects/<name>/README.md      ← add for any project task
Tier 3  hub notes or leaf notes        ← only the one matching the task domain
Tier 4  raw sources                    ← only when exact wording/precision matters
```

**Hot Cache Rule:** Read `context/hot.md` before any other file. If a structural router (briefing.md, context/now.md, a project README) is listed under "Stable Since Last Session", skip its repair pass. Update `context/hot.md` at the end of every task.

**Stable Router Exception:** `briefing.md`, `context/now.md`, and project READMEs already validated earlier the same session do not need a second repair pass — they were not edited and showed no structural issue on read. A single log note is enough: "stable router pages checked, no repair needed."

**Two-Layer Mirror Rule:** The PathFinder dev-log and the global vault activity log both use the two-layer pattern: an index file (navigation only, one line per day) plus a `days/YYYY-MM-DD.md` file (the real note). Always update the day file first, then sync the index. Never write content directly into the index.

**Propagation Rule:** After every Write or Edit, check `SCHEMA.md → Propagation Sync Matrix` for the file you just touched. Update downstream targets before ending your response. The PostToolUse hook (`scripts/check_propagation.py`) surfaces this automatically.

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

**Write-back rule: complete all vault updates (index entry, log entry, context patch) before ending your response. Do not defer to a later session. The task is not done until the log is written.**

See `SCHEMA.md -> Self-Healing Protocol` for full rules.
