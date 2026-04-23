---
type: hub
title: "Vault Keeping"
created: 2026-04-12
updated: 2026-04-21
tags: [vault, meta, operations, hub]
status: active
lang: en
feeds_into:
  - briefing.md
  - AGENTS.md
  - CLAUDE.md
  - wiki/operations-hub.md
---

> **TL;DR**: Top-tier maintenance-family hub for keeping the vault reliable: drift control, logging, self-healing, propagation, and maintenance audits.

---

Use `vault-keeping` when the task is about keeping the vault reliable: maintenance, drift, logging, self-healing, propagation, or operation audits.

This is the maintenance-family hub, not the global registry for every official operation.
For all official operations, use [[wiki/operations-hub]].

## Fast Route

| I need to... | Go to |
|-------------|-------|
| Run a vault maintenance audit | [[wiki/operations/lint-operation]] |
| Fix drift in one domain | [[wiki/operations/lint-operation]] |
| Sort unsorted files from pending/ | [[wiki/operations/sort-operation]] |
| Repair or close out vault edits | [[wiki/operations/self-healing-operation]] |
| Add a new vault page correctly | [[wiki/operations/file-creation-gate]] |
| Understand what to update after writing a file | [[vault_propagation]] → How They Interact + Wire 4 |

---

## What Is Vault Keeping

The continuous work that keeps the vault navigable, fresh, and consistent:

```
Drift-free navigation  →  index.md never falls behind page count
Fresh context          →  context/now.md never stale > 7 days
Consistent structure   →  every new file passes File Creation Gate
Propagated updates     →  every Write triggers downstream targets
```

Four categories. Each fires at a different frequency and scope.

## Official Branching Rule

Branching exists to reduce scan cost, not to create decorative hierarchy.

```text
top router
  -> family hub or project README
  -> domain hub if needed
  -> canonical leaf
```

Hard rules:
- Top-level routers point to family hubs, project READMEs, or canonical registries, not flat leaf dumps across mixed domains.
- Family hubs route inside one family only. Cross-family jumps should point back to the correct top router or family hub.
- Project READMEs are the root branch nodes for their projects. They may point directly to one artifact only when the domain is still too small to deserve a hub.
- Create a hub when a branch has 3+ related notes or is clearly going to keep growing.
- Prefer a maximum of two branch hops from a top router before the leaf:
  `briefing -> family hub -> leaf`
  or `briefing -> project README -> hub -> leaf`
- If a router starts mixing multiple families, or dumping too many direct leaves, split it or elevate one level of routing.
- If a hub exists for a domain, top-level routers should prefer the hub over linking many leaves directly.

Branch audit questions:
- Is this page a router, a family hub, a project root, or a leaf?
- Does it point one level down cleanly?
- Is any branch carrying mixed-family links it should not own?
- Is any leaf being exposed too high in the tree?
- Would a new agent know the next branch without scanning sideways?

---

## Scale Ladder

### 1. Micro — Per-Touch
Fires on every Write or Edit. Not optional.

| Rule | Trigger | Source |
|------|---------|--------|
| Self-Healing Pass | After editing/creating a vault file, or when a read-only page shows a task-affecting defect | [[wiki/operations/self-healing-operation]] |
| Two-Layer Mirror Sync | After writing a day log file, only when the index needs a new day or changed summary | [[CLAUDE.md]] → Two-Layer Mirror Rule |
| Propagation Check | After every Write/Edit (automatic via hook) | [[vault_propagation]] → Wire 4 |

**Self-Healing Pass — three checks, always in this order when the pass is triggered:**
1. Missing `updated` date? Add today's date.
2. Missing `> TL;DR`? Generate one from the content.
3. Obvious missing wikilinks (mentioned page names without `[[]]`)? Add them.

Evidence-only reads for repo/eval work do not trigger page-by-page repair. If no structural defect or stale routing affects the task, summarize those reads once in the day log and move on.

**Two-Layer Mirror Sync — which files have mirrors:**
- `sources/log/days/YYYY-MM-DD.md` → sync `log.md` only for a new day or changed daily summary
- `logs/dev/days/YYYY-MM-DD.md` → sync `logs/DEV_LOG.md` + vault canonical `projects/pathfinder/sources/docs/DEV_LOG.md` only for a new day or changed daily summary

**Propagation Check — what the hook prints:**
The PostToolUse hook reads the file you just wrote, looks up the Propagation Sync Matrix, and prints downstream targets. Act on every target before ending the response.

---

### 2. Session — Per-Session
Fires at the start and end of every session.

**At session start (in order, non-negotiable):**

| Step | Check | Source |
|------|-------|--------|
| 0 | Read `context/hot.md` first. Stable routers listed → skip repair pass. | [[wiki/operations/session-start-operation]] |
| 1 | Read `briefing.md` | [[wiki/operations/session-start-operation]] |
| 2 | Read `context/now.md`. Is `updated` date > 7 days? → Flag. | [[wiki/operations/session-start-operation]] |
| 3 | briefing Active Projects ↔ context/now Active Projects must match | [[wiki/operations/session-start-operation]] |
| 4 | Files in `pending/`? → Flag and offer SORT | [[wiki/operations/sort-operation]] |
| 5 | Index drift? Glob a project's notes dir, compare to `index.md`. Add missing. | [[CLAUDE.md]] → Session start check |
| 6 | User revealed new context? → Update `context/` before starting task | [[wiki/operations/context-update-operation]] |

**At session end (run the applicable mandatory checks before ending response):**

| Step | Action | Source |
|------|--------|--------|
| 1 | Write day log entry for durable work | [[wiki/operations/self-healing-operation]] |
| 2 | Sync the log index only for a new day or changed daily summary | [[sources/log/HOW_TO_WRITE.md]] |
| 3 | Delta-update `context/hot.md` only when continuity, stable-router status, or next action changed | [[context/hot]] |
| 4 | Patch `context/` if user revealed new info | [[wiki/operations/context-update-operation]] |

**Vault-first closeout for architecture work:**
```text
canvas change
  -> markdown mirror
  -> router/context patch if routing changed
  -> day log entry
  -> response
```

Do not leave Canvas updates floating without the markdown/routing pass in the same task.

**Operation evolution rule:**
```text
use official operation
  -> audit friction
  -> patch docs now if cheap
  -> log gap now if not cheap
```

---

### 3. Domain — Periodic
Triggered by drift accumulation or scheduled review. Not every session.

| Operation | When To Run | Source |
|-----------|-------------|--------|
| **SORT** | `pending/` has files. Offer at every session start. | [[wiki/operations/sort-operation]] |
| **Flow-Check** | A domain hasn't been swept recently (> 1 week). One domain per session. | [[wiki/operations/lint-operation]] |
| **LINT** | Full vault structural audit. Trigger: > 10 new pages OR > 2 weeks since last pass. | [[wiki/operations/lint-operation]] |

**Flow-Check scope (one domain = all four layers):**
```
notes/    — are hub notes stale? missing TL;DRs?
sources/  — are source docs missing sections?
hub       — does the hub route all notes in the domain?
index.md  — are all notes registered?
```

---

### 4. Structural — Architectural
When vault topology changes: new project, new hub, new operational doc, new structural node.

| Operation | When To Run | Source |
|-----------|-------------|--------|
| **File Creation Gate** | Every new vault file without exception | [[wiki/operations/file-creation-gate]] |
| **New Project** | Starting a new project namespace | [[vault_propagation]] → Maintenance → Adding a New Project |
| **New Structural Node** | Adding a new hub, README, or vault-root operational doc | [[vault_propagation]] → Maintenance → Adding a New Structural Node |
| **Propagation System** | Reference for how downstream targets are computed | [[vault_propagation]] |
| **System Map** | Reference for directory layout, data flow, layer responsibilities | [[vault_architecture]] |

**File Creation Gate — two-phase (never skip Phase 1):**
```
Phase 1 — Pre-Write:
  type:    → check SCHEMA.md type list (add new type first if needed)
  tags:    → check index.md tag registry (add new tags first, then select)
  project? → briefing.md + context/now.md Active Projects must both be updated

Phase 2 — Post-Write:
  Index entry  → wiki/, learning/, references/, projects/ files → add to index.md
  New dir      → add row to SCHEMA.md Directory Map
  New project  → update both briefing.md and context/now.md Active Projects
  Context shift → update context/now.md Vault Status
```

---

## After Use Evolution Check
- Was the maintenance route obvious without scanning `SCHEMA.md`?
- Did this hub point to the right maintenance leaf page?
- Did any maintenance step still depend on memory instead of routing?
- Did the closeout burn unnecessary tokens?
- If friction appeared, patch this hub now or log the named gap today.

---

## Connections

- [[vault_architecture]] — full directory map, data flow, layer responsibilities, optimization targets
- [[vault_propagation]] — four-wire propagation system (sync matrix, feeds_into:, hot cache, PostToolUse)
- [[SCHEMA.md]] — constitutional rules for routing, schema, propagation, and official-operation governance
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]] — official canvas-first architecture workflow and vault-first closeout order
- [[CLAUDE.md]] — Claude Code-specific rules, tiered loading quick reference, hot cache rule
- [[AGENTS.md]] — Codex-specific behavior, session start sequence
- [[context/hot]] — session hot cache, stable router skip list
