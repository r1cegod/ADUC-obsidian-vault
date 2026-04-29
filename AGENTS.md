# AGENTS.md - Codex Vault Entry Point

> **TL;DR**: Read [[context/hot]] -> [[duc-os]], then let Duc OS choose the next router. [[briefing]] is now a dashboard under Duc OS, not the root authority.

Last updated: 2026-04-29

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
Open `projects/<name>/README.md` before project notes or raw sources.

## Session Start Check

Run before every task:

- Is `duc-os/current.md` `updated` date > 7 days ago? -> Flag it, do not act on stale current state.
- Does [[briefing]] Active Projects match [[duc-os/current]] Active Projects? -> If not, reconcile before proceeding.
- Files in `pending/`? -> Flag and offer to sort before starting task.
- Did Duc reveal new personal, strategic, project, or priority context? -> Update the owning Duc OS page before the task when it affects routing or judgment.

## Duc OS Route

[[duc-os]] is the meta-router above the old top routers.

```text
AGENTS.md
  -> Duc OS
      -> briefing dashboard
      -> development gate
      -> vault-keeping maintenance
      -> project README
      -> operation leaf
```

Trigger Duc OS first for:

- KICKSTART
- leverage / life-system design
- founder path / escape velocity / Singapore direction
- social visibility or inbound strategy
- "what should I do today?"
- motivation vs clarification questions
- personality-wrapper or agent-behavior changes

Do not treat these as coaching requests. Treat them as operating-system clarification requests.

## Operation Router

Duc OS decides when to enter these routers:

- Active-project dashboard -> [[briefing]]
- Official operations registry -> [[wiki/operations-hub]]
- Vault maintenance, drift, logging, workflow audit, or new branch placement -> [[vault-keeping]] -> [[wiki/operations/branch-growth-operation]]
- Exact constitutional rule, schema, or propagation law -> [[SCHEMA.md]]
- Project work -> `projects/<name>/README.md`
- Architecture planning -> project README -> architecture hub -> active `.canvas`
- Collaborative drafting -> [[wiki/operations-hub]] -> [[wiki/operations/draft-operation]]
- Technical help / learning / code delegation -> [[development]] -> [[wiki/operations/detect-operation]]

## Universal Development Gate

For technical help, docs, debugging, implementation guidance, or code delegation:

1. Start from [[development]].
2. Run [[wiki/operations/detect-operation]] first.
3. Route to [[wiki/operations/learn-operation]] for learning/help/audit/mechanism gaps.
4. Route to [[wiki/operations/delegate-operation]] only when Duc's pattern is clear enough to copy and audit.
5. Use the old learning protocol pages as references inside Learn, not as the top router.

Ownership rule before implementation help:

- if Duc can name files, seams, steps, failure modes, and verification path, review/delegation may be allowed
- if not, prefer learning flow unless the task is clear ONE_TIME_UTILITY

## Codex-Specific Behavior

- Use `rtk` for shell/repo commands where practical. Fall back to raw shell only when `rtk` cannot express the command cleanly or would hide needed output.
- Use Obsidian MCP for vault reads/writes instead of raw filesystem access. Fall back to filesystem reads only when MCP is unavailable or the task explicitly requires raw file inspection.
- Treat `/home/r1ceg/Path_finder_wsl` as the WSL PathFinder working repo unless a project wrapper says otherwise.
- Prefer targeted file edits over full rewrites.
- Obsidian `[[wikilinks]]` are the internal link format - always use these, not markdown URLs.
- Frontmatter YAML must be valid - consistent quoting, no tabs.
- When running shell commands, prefer reading files directly over piping through grep/sed.
- `log.md` is the activity-log navigation file; the real daily logs live under `sources/log/days/`.
- For project work, navigate `README.md -> notes/ -> sources/` unless the task explicitly requires raw-source-first reading.
- Treat project README pages as routing hubs, not passive project descriptions.
- Treat `journal/daily/` as human-primary raw capture. Do not rewrite it into agent voice unless the task explicitly calls for it.
- Put durable synthesis into `wiki/`, `projects/<name>/notes/`, `duc-os/`, `index.md`, or the vault log layer (`log.md` + `sources/log/`) instead of back-writing it into raw notes.
- For every new durable vault entry, include a `## Growth Contract`.
- For architecture-heavy work, route through Duc OS first, then the project README, architecture hub, and active `.canvas`.
- Officially documented operations are living contracts: if use reveals friction, patch the docs the same session when cheap or log the gap that day.

## After Every Task

1. Run self-healing on edited/created pages, or on read-only pages only if a structural defect would affect this task.
2. Log durable work in `sources/log/days/`.
3. Sync `log.md` only for a new day or changed daily summary.
4. Patch the owning Duc OS page if conversation changed what future sessions should know.
5. Finish all vault writeback before ending the response.

See `SCHEMA.md -> Self-Healing Protocol` for full rules.