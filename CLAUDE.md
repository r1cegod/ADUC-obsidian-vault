# CLAUDE.md - Claude Code Vault Entry Point

> **TL;DR**: Read [[context/hot]] -> [[briefing.md]] -> [[context/now]], then route through [[wiki/operations-hub]], [[vault-keeping]], [[wiki/learning-protocol-hub]], or a project README. Use `SCHEMA.md` only for exact constitutional law.

## Quick Start

Read in order:
0. `context/hot.md`
1. `briefing.md`
2. `context/now.md`
3. then the smallest next router that fits the task

Open `SCHEMA.md` only for exact constitutional rule, schema, or propagation law.

**Session start check (run before every task):**
- Is `context/now.md` `updated` date > 7 days ago? -> Flag it, do not act on stale context.
- Does `briefing.md` Active Projects match `context/now.md` Active Projects? -> If not, reconcile before proceeding.
- Files in `pending/`? -> Flag and offer to sort before starting task.
- Did user reveal new personal info or project status in conversation? -> Update `context/` now, before the task.
- Index drift? Glob a project's notes directory and compare against `index.md` → if pages on disk are missing from the index, flag and add before starting the task.

## Operation Router

- Official operations registry -> [[wiki/operations-hub]]
- Vault maintenance, drift, logging, or workflow audit -> [[vault-keeping]]
- Exact constitutional rule, schema, or propagation law -> [[SCHEMA.md]]
- Project work -> `projects/<name>/README.md`
- Architecture planning -> project README -> architecture hub -> active `.canvas`
- Collaborative drafting -> [[wiki/operations-hub]] -> [[wiki/operations/draft-operation]]
- Technical help / learning ownership -> [[wiki/learning-protocol-hub]]

## Tiered Loading Quick Reference

Load context in tiers. Stop after each tier unless the task genuinely needs more.

```
Pre     context/hot.md                 ← ALWAYS first. Lists stable routers that
                                          skip repair pass. Delta-update only
                                          when continuity changed.
Tier 0  briefing.md                    ← ALWAYS
Tier 1  context/now.md + SCHEMA.md     ← add SCHEMA only for exact law/wiki ops
Tier 2  projects/<name>/README.md      ← add for any project task
Tier 3  hub notes or leaf notes        ← only the one matching the task domain
Tier 4  raw sources                    ← only when exact wording/precision matters
```

Hot cache rule:
- read `context/hot.md` first
- skip repair pass on routers listed stable there
- update `context/hot.md` only when continuity, stable-router status, or next action changed

Two-layer mirror rule:
- update the day file first
- sync the index only for a new day or changed summary

Propagation rule:
- after every Write/Edit, check `SCHEMA.md -> Propagation Sync Matrix`
- the hook surfaces this automatically

## Universal Help / Learning Gate

For technical help, docs, debugging, or implementation guidance:
1. Start from [[wiki/learning-protocol-hub]]
2. Run [[wiki/help-protocol]]
3. Use [[wiki/vibe-docing]] for narrow mechanism gaps
4. Use [[wiki/build-first-learning]] when the skill should compound
5. Escalate to [[wiki/pre-wire-protocol]] for full feature ownership

Ownership rule before implementation help:
- if Duc can name files, seams, steps, failure modes, and verification path, review/delegation may be allowed
- if not, prefer learning flow unless the task is clear ONE_TIME_UTILITY

## Claude Code-Specific Behavior

- Use the `Edit` tool (not bash sed/awk) when modifying markdown files
- Use the `Write` tool when creating new pages from templates
- Use `Glob` and `Grep` to scan wiki pages before creating new ones (avoid duplicates)
- For project routing, prefer the smallest sufficient path after `README.md`; hubs suggest likely entry points but do not impose a fixed reading sequence
- Obsidian `[[wikilinks]]` are the internal link format - always use these, not markdown URLs
- Frontmatter YAML must be valid - no tabs, consistent quoting
- Treat `journal/daily/` as human-primary raw capture. Do not rewrite it into agent voice unless the task explicitly calls for it.
- Put durable synthesis into `wiki/`, `projects/<name>/notes/`, `index.md`, or the vault log layer (`log.md` + `sources/log/`) instead of back-writing it into raw notes.
- For architecture-heavy work, route `README.md -> architecture hub -> active .canvas` before repo code, and finish vault artifacts before closing the response.
- Officially documented operations are living contracts: if use reveals friction, patch the docs the same session when cheap or log the gap that day.
- Treat [[vault-keeping]] as the top-tier maintenance family hub, not as the global registry for all operations.

---

## After Every Task

1. Run self-healing on edited/created pages, or on read-only pages only if a structural defect would affect this task.
2. Log durable work in `sources/log/days/`.
3. Sync `log.md` only for a new day or changed daily summary.
4. Patch `context/` if conversation changed what future sessions should know.
5. Finish all vault writeback before ending the response.

See `SCHEMA.md -> File Creation Gate` and `SCHEMA.md -> Self-Healing Protocol` for full rules.
