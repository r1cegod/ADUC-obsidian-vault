---
type: hub
title: "Vault Keeping"
created: 2026-04-12
updated: 2026-04-13
tags: [vault, meta, operations, hub]
status: active
lang: en
feeds_into: []
---

> **TL;DR**: Routing hub for all vault maintenance operations ordered by scale — micro (per-touch) through structural (topology changes). Start here when a maintenance task doesn't have an obvious next file.

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

---

## Scale Ladder

### 1. Micro — Per-Touch
Fires on every Write or Edit. Not optional.

| Rule | Trigger | Source |
|------|---------|--------|
| Self-Healing Pass | After editing/creating a vault file, or when a read-only page shows a task-affecting defect | [[SCHEMA.md]] → Self-Healing Protocol |
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
| 0 | Read `context/hot.md` first. Stable routers listed → skip repair pass. | [[context/hot]] |
| 1 | Read `briefing.md` | [[briefing]] |
| 2 | Read `context/now.md`. Is `updated` date > 7 days? → Flag. | [[SCHEMA.md]] → Session Start Protocol |
| 3 | briefing Active Projects ↔ context/now Active Projects must match | [[SCHEMA.md]] → Session Start Protocol |
| 4 | Files in `pending/`? → Flag and offer SORT | [[SCHEMA.md]] → SORT Operation |
| 5 | Index drift? Glob a project's notes dir, compare to `index.md`. Add missing. | [[CLAUDE.md]] → Session start check |
| 6 | User revealed new context? → Update `context/` before starting task | [[SCHEMA.md]] → Conversation-Triggered Context Update |

**At session end (run the applicable mandatory checks before ending response):**

| Step | Action | Source |
|------|--------|--------|
| 1 | Write day log entry for durable work | [[SCHEMA.md]] → Self-Healing Protocol → Logging Format |
| 2 | Sync the log index only for a new day or changed daily summary | [[sources/log/HOW_TO_WRITE.md]] |
| 3 | Delta-update `context/hot.md` only when continuity, stable-router status, or next action changed | [[context/hot]] |
| 4 | Patch `context/` if user revealed new info | [[SCHEMA.md]] → Conversation-Triggered Context Update |

---

### 3. Domain — Periodic
Triggered by drift accumulation or scheduled review. Not every session.

| Operation | When To Run | Source |
|-----------|-------------|--------|
| **SORT** | `pending/` has files. Offer at every session start. | [[SCHEMA.md]] → SORT Operation |
| **Flow-Check** | A domain hasn't been swept recently (> 1 week). One domain per session. | [[SCHEMA.md]] → LINT Operation |
| **LINT** | Full vault structural audit. Trigger: > 10 new pages OR > 2 weeks since last pass. | [[SCHEMA.md]] → LINT Operation |
| **INGEST** | New source material arrives. Always run deduplication pre-check. | [[SCHEMA.md]] → INGEST Operation |

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
| **File Creation Gate** | Every new vault file without exception | [[SCHEMA.md]] → File Creation Gate |
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

## Decision Table

| I need to... | Go to |
|-------------|-------|
| Fix drift in one domain | [[SCHEMA.md]] → LINT Operation → Flow-Check steps |
| Sort unsorted files from pending/ | [[SCHEMA.md]] → SORT Operation |
| Add a new vault page correctly | [[SCHEMA.md]] → File Creation Gate |
| Add a new project | [[vault_propagation]] → Maintenance → Adding a New Project |
| Understand what to update after writing a file | [[vault_propagation]] → How They Interact + Wire 4 |
| Read the full vault system map | [[vault_architecture]] |
| Skip repair on already-verified routers | [[context/hot]] → Stable Since Last Session |
| Check propagation targets manually | `scripts/check_propagation.py` |
| Understand why full BFS is not used | [[vault_propagation]] → Why Not BFS |

---

## Connections

- [[vault_architecture]] — full directory map, data flow, layer responsibilities, optimization targets
- [[vault_propagation]] — four-wire propagation system (sync matrix, feeds_into:, hot cache, PostToolUse)
- [[SCHEMA.md]] — operations manual (ingest, sort, lint, self-healing, session protocol, file creation gate)
- [[CLAUDE.md]] — Claude Code-specific rules, tiered loading quick reference, hot cache rule
- [[AGENTS.md]] — Codex-specific behavior, session start sequence
- [[context/hot]] — session hot cache, stable router skip list
