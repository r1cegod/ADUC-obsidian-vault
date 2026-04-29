# CLAUDE.md - Claude Code Vault Entry Point

> **TL;DR**: Read [[context/hot]] -> [[duc-os]], then let Duc OS choose the next router. [[briefing]] is a dashboard under Duc OS, not the root authority.

## Quick Start

Read in order:

0. `context/hot.md` - temporary session cache
1. `duc-os.md` - root operating layer and meta-router
2. then the smallest route selected by Duc OS:
   - [[briefing]] for active-project dashboard
   - [[development]] for technical help, implementation, learning, or delegation
   - [[vault-keeping]] for maintenance, drift, logging, or branch placement
   - project README for named project work
   - official operation leaf for a named workflow

Open `SCHEMA.md` only for exact constitutional rule, schema, propagation, or file-creation law.

## Session Start Check

Run before every task:

- Is `duc-os/current.md` `updated` date > 7 days ago? -> Flag it, do not act on stale current state.
- Does [[briefing]] Active Projects match [[duc-os/current]] Active Projects? -> If not, reconcile before proceeding.
- Files in `pending/`? -> Flag and offer to sort before starting task.
- Did Duc reveal new personal, strategic, project, or priority context? -> Update the owning Duc OS page before the task when it affects routing or judgment.
- Index drift? Check likely touched directories against `index.md`; if pages are missing, flag and add before starting implementation.

## Duc OS Route

[[duc-os]] is the meta-router above the old top routers.

```text
CLAUDE.md
  -> Duc OS
      -> briefing dashboard
      -> development gate
      -> vault-keeping maintenance
      -> project README
      -> operation leaf
```

Trigger Duc OS first for KICKSTART, leverage, founder path, social visibility, "what should I do today?", motivation-vs-clarification, and personality-wrapper changes.

Do not treat these as coaching requests. Treat them as operating-system clarification requests.

## Tiered Loading Quick Reference

Load context in tiers. Stop after each tier unless the task genuinely needs more.

```text
Pre     context/hot.md          temporary session cache
Tier 0  duc-os.md               root operating layer
Tier 1  duc-os/current.md       current state when needed
        briefing.md             dashboard when project/status snapshot is needed
        SCHEMA.md               only for exact law/wiki ops
Tier 2  projects/<name>/README  for project task
Tier 3  hub notes or leaf notes only the one matching the task domain
Tier 4  raw sources             only when exact wording/precision matters
```

## Universal Development Gate

For technical help, docs, debugging, implementation guidance, or code delegation:

1. Start from [[development]].
2. Run [[wiki/operations/detect-operation]] first.
3. Route to [[wiki/operations/learn-operation]] for learning/help/audit/mechanism gaps.
4. Route to [[wiki/operations/delegate-operation]] only when Duc's pattern is clear enough to copy and audit.

## Claude Code-Specific Behavior

- Use the `Edit` tool when modifying markdown files.
- Use the `Write` tool when creating new pages from templates.
- Use `Glob` and `Grep` to scan wiki pages before creating new ones when duplicate risk exists.
- For project routing, prefer the smallest sufficient path after `README.md`; hubs suggest likely entry points but do not impose a fixed reading sequence.
- Obsidian `[[wikilinks]]` are the internal link format - always use these, not markdown URLs.
- Frontmatter YAML must be valid - no tabs, consistent quoting.
- Treat `journal/daily/` as human-primary raw capture. Do not rewrite it into agent voice unless the task explicitly calls for it.
- Put durable synthesis into `wiki/`, `projects/<name>/notes/`, `duc-os/`, `index.md`, or the vault log layer (`log.md` + `sources/log/`).
- For every new durable vault entry, include a `## Growth Contract`.
- For architecture-heavy work, route through Duc OS first, then the project README, architecture hub, and active `.canvas`.
- Officially documented operations are living contracts: if use reveals friction, patch the docs the same session when cheap or log the gap that day.

## After Every Task

1. Run self-healing on edited/created pages, or on read-only pages only if a structural defect would affect this task.
2. Log durable work in `sources/log/days/`.
3. Sync `log.md` only for a new day or changed daily summary.
4. Patch the owning Duc OS page if conversation changed what future sessions should know.
5. Finish all vault writeback before ending the response.

See `SCHEMA.md -> File Creation Gate` and `SCHEMA.md -> Self-Healing Protocol` for full rules.