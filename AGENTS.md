# AGENTS.md - Codex Vault Entry Point

> **TL;DR**: Read [[context/hot]] -> [[briefing.md]] -> [[context/now]], then choose the smallest next router: [[development]], [[wiki/operations-hub]], [[vault-keeping]], or a project README.

Last updated: 2026-04-25

## Quick Start

Read in order:
0. `context/hot.md`
1. `briefing.md`
2. `context/now.md`
3. then the smallest next router that fits the task

Open `SCHEMA.md` only for exact constitutional rule, schema, or propagation law.
Open `projects/<name>/README.md` before project notes or raw sources.

**Session start check (run before every task):**
- Is `context/now.md` `updated` date > 7 days ago? -> Flag it, do not act on stale context.
- Does `briefing.md` Active Projects match `context/now.md` Active Projects? -> If not, reconcile before proceeding.
- Files in `pending/`? -> Flag and offer to sort before starting task.
- Did user reveal new personal info or project status in conversation? -> Update `context/` now, before the task.

## Operation Router
- Official operations registry -> [[wiki/operations-hub]]
- Vault maintenance, drift, logging, workflow audit, or new branch placement -> [[vault-keeping]] -> [[wiki/operations/branch-growth-operation]] when creating durable nodes; new durable entries must keep a Growth Contract
- Exact constitutional rule, schema, or propagation law -> [[SCHEMA.md]]
- Project work -> `projects/<name>/README.md`
- Architecture planning -> project README -> architecture hub -> active `.canvas`
- Collaborative drafting -> [[wiki/operations-hub]] -> [[wiki/operations/draft-operation]]
- Technical help / learning / code delegation -> [[development]] -> [[wiki/operations/detect-operation]]

## Universal Development Gate

For technical help, docs, debugging, implementation guidance, or code delegation:
1. Start from [[development]]
2. Run [[wiki/operations/detect-operation]] first
3. Route to [[wiki/operations/learn-operation]] for learning/help/audit/mechanism gaps
4. Route to [[wiki/operations/delegate-operation]] only when Duc's pattern is clear enough to copy and audit
5. Use the old learning protocol pages as references inside Learn, not as the top router

Ownership rule before implementation help:
- if Duc can name files, seams, steps, failure modes, and verification path, review/delegation may be allowed
- if not, prefer learning flow unless the task is clear ONE_TIME_UTILITY

Default learning modes:
- `AUDIT` for check/clean/debug on active learning artifacts
- `PATCH` only after explicit patch/delegation request or for ONE_TIME_UTILITY
- `STEAL` for reference-only finished code outside the active path
- `ABSORPTION` only when Duc explicitly wants deep study
- `VIBE_DOCING` uses neutral placeholders only

## Codex-Specific Behavior

- Use `rtk` for shell/repo commands where practical. Fall back to raw shell only when `rtk` cannot express the command cleanly or would hide needed output.
- Use Obsidian MCP for vault reads/writes instead of raw filesystem access. Fall back to filesystem reads only when MCP is unavailable or the task explicitly requires raw file inspection.
- Treat `/home/r1ceg/Path_finder_wsl` as the WSL PathFinder working repo.
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
- For every new durable vault entry, include a `## Growth Contract` with parent branch, node role, first parent link, growth trigger, forbidden contents, and expected child/source boundary when relevant.
- For architecture-heavy work, route `README.md -> architecture hub -> active .canvas` before repo code, and complete vault updates before ending the response.
- Officially documented operations are living contracts: if use reveals friction, patch the docs the same session when cheap or log the gap that day.
- Treat [[vault-keeping]] as the top-tier maintenance family hub, not as the global registry for all operations.

## After Every Task

1. Run self-healing on edited/created pages, or on read-only pages only if a structural defect would affect this task.
2. Log durable work in `sources/log/days/`.
3. Sync `log.md` only for a new day or changed daily summary.
4. Patch `context/` if conversation changed what future sessions should know.
5. Finish all vault writeback before ending the response.

See `SCHEMA.md -> Self-Healing Protocol` for full rules and the Stable Router Exception.
