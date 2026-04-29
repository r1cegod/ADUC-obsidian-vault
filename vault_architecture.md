# Vault Architecture

> **TL;DR**: Architecture reference for the vault's folders, data flow, startup route, write contract, and layer responsibilities; canonical runtime starts at [[duc-os]].

> Optimization reference — read this to understand the full system before restructuring any layer. Canonical runtime starts at [[duc-os]], not the older briefing/context-first route.

---

## 1. Directory Map

```
ADUC_vault/ADUC/
│
├── CLAUDE.md              ← Claude entry point. Thin wrapper -> context/hot.md -> duc-os.md
├── AGENTS.md              ← Codex entry point. Thin wrapper -> context/hot.md -> duc-os.md
├── SCHEMA.md              ← Full operations manual and constitutional law.
├── duc-os.md              ← Root operating layer and meta-router.
├── duc-os/                ← Identity, long arc, current state, KICKSTART, engines, session protocol.
├── briefing.md            ← Active-project dashboard under Duc OS, not the root brain.
├── index.md               ← Content routing table. One entry per page. Tag registry.
├── log.md                 ← Activity log NAVIGATION only. One line per day.
│
├── context/               ← Compatibility redirects + hot cache.
│   ├── hot.md             ← Startup cache before Duc OS.
│   ├── me.md              ← Redirect to duc-os/identity.md
│   ├── now.md             ← Redirect to duc-os/current.md
│   └── goals.md           ← Redirect to duc-os/long-arc.md
│
├── sources/               ← Raw, unprocessed source material
│   ├── articles/          ← Markdown articles
│   ├── docs/              ← PDFs, technical docs
│   ├── transcripts/       ← Audio/video transcripts
│   ├── misc/              ← Unclassified dumps
│   ├── projects/          ← Project sources not yet in a named project workspace
│   └── log/               ← Global vault activity source layer
│       ├── HOW_TO_WRITE.md
│       ├── DATA_HOLES.md  ← Flag-only issues (needs new source, user judgment)
│       └── days/          ← Real log content. One file per day: YYYY-MM-DD.md
│
├── wiki/                  ← Agent-compiled knowledge base
│   ├── concepts/          ← Reusable concepts (usable across projects)
│   ├── entities/          ← People, tools, orgs
│   └── synthesis/         ← Multi-source syntheses, comparison pages
│
├── projects/              ← Project workspaces. Self-contained.
│   ├── pathfinder/        ← Active: LangGraph career guidance chatbot
│   │   ├── README.md      ← Project router. Start here for any PathFinder work.
│   │   ├── notes/         ← Agent-compiled summaries, evaluations, hubs
│   │   └── sources/       ← Project-local raw sources (docs, dev-log, eval reports)
│   │       └── docs/
│   │           ├── evaluation/      ← thinking_eval.md, goals_eval.md, etc.
│   │           ├── DEV_LOG.md       ← Dev log index (navigation only)
│   │           └── dev-log/days/    ← Actual dev log entries (two-layer pattern)
│   │
│   └── ielts-writing/     ← Active: 20-day band 4→7 protocol
│
├── learning/              ← Learning sessions. Pre-Wire protocol.
│   ├── README.md          ← Session index
│   └── sessions/          ← One file per feature attempt
│
├── references/            ← External bookmarks, links, citations (not wiki pages)
├── journal/daily/         ← Human-primary raw capture. YYYY-MM-DD.md format.
├── pending/               ← Drop zone for unsorted files. Agents sort on every session.
├── templates/             ← Obsidian templates. Human-managed.
├── assets/                ← Obsidian auto-attachments. Do not agent-write here.
└── images/                ← Curated source images, screenshots, diagrams.
```

---

## 2. Data Flow — Raw → Compiled

```
User / External Source
        │
        ▼
   pending/           ← drop zone (unsorted)
        │  SORT operation
        ▼
   sources/           ← raw, unprocessed, canonical text
        │  INGEST operation
        ├──────────────────────────────────────────────┐
        ▼                                              ▼
   wiki/              ← reusable compiled knowledge    projects/<name>/notes/
   (concepts, entities,                               (project-specific compiled knowledge)
    synthesis)
        │                                              │
        ▼                                              ▼
   index.md           <- navigation + routing table (pointers only, no content)
        │
        ▼
   briefing.md        <- compact active-project dashboard
        │
        ▼
   duc-os/current.md  <- live priorities, active projects, blockers, and route state
        │
        ▼
   duc-os.md          <- root operating layer chooses the next router
```

Key rule: **content only moves upward into the smallest durable authority**. Index points to wiki/notes. Briefing stays a dashboard. Duc OS owns stance, current route, and long-arc context.
You never put real knowledge into briefing.md, index.md, or log.md — those are navigation only.

---

## 3. Session Protocol — What Agents Do On Start

```
Session starts
      │
      ▼
  Optional wrapper cache: context/hot.md
      │
      ▼
  Read duc-os.md                  <- ALWAYS. Root operating route.
      │
      ├── Need current state? -> read duc-os/current.md and check updated date.
      ├── Need project dashboard? -> read briefing.md.
      ├── Active Projects in briefing == Active Projects in duc-os/current? -> reconcile if not.
      ├── Files in pending/? -> flag + offer to sort.
      ├── User revealed new durable context? -> update owning Duc OS page before task.
      └── Index drift? Glob notes dir, compare to index.md -> add missing entries.
      │
      ▼
  Choose smallest next tier
  ┌───────────────────────────────────────────────────────────────┐
  │ Tier 0  duc-os.md                         ALWAYS              │
  │ Tier 1  duc-os/current.md                 current routing      │
  │         briefing.md                       project dashboard    │
  │         SCHEMA.md                         wiki ops only        │
  │         index.md                          routing needed only  │
  │ Tier 2  projects/<name>/README            project task         │
  │ Tier 3  hub notes / leaf notes            domain-specific      │
  │ Tier 4  raw sources                       precision required   │
  └───────────────────────────────────────────────────────────────┘
  Stop-check between each tier. Descend only if genuinely needed.
```

**Stable Router Exception:** duc-os.md, duc-os/current.md, briefing.md, project READMEs, and project hubs validated earlier the same session do not need a second repair pass. Log "stable router checked, no repair needed."

---

## 4. The Two-Layer Mirror Pattern

Used by: global vault activity log, PathFinder dev-log, PathFinder dev-log repo mirror.

```
Navigation layer (index file)              Content layer (day files)
─────────────────────────────              ──────────────────────────
log.md                          ←──────── sources/log/days/YYYY-MM-DD.md
  - 2026-04-12 | Summary | link              ## [2026-04-12] INGEST | ...
  - 2026-04-11 | Summary | link              ## [2026-04-12] LINT | ...
  (one line per day, newest first)           (full content here, never in index)

projects/pathfinder/sources/docs/DEV_LOG.md ←── ...dev-log/days/YYYY-MM-DD.md
  (same pattern, project-local)
```

**Rules:**
1. Update day file first. Then sync the index.
2. Never write content directly into the index file.
3. Same day changes again → update the existing day file, not a new one.

**PathFinder also mirrors into the repo:**
```
Vault canonical:          D:/ANHDUC/ADUC_vault/ADUC/projects/pathfinder/sources/docs/dev-log/days/
Repo mirror:              D:/ANHDUC/Path_finder/logs/dev/days/
Repo index mirror:        D:/ANHDUC/Path_finder/logs/DEV_LOG.md
```
Every durable dev-log entry must update both locations.

---

## 5. Project Namespace — PathFinder Internal Structure

```
projects/pathfinder/
├── README.md                          ← project router. Task-type routing table.
├── notes/                             ← agent-compiled summaries (40+ files)
│   │
│   ├── HUBs (routing within a domain)
│   │   ├── pathfinder-evaluation-hub.md
│   │   ├── pathfinder-architecture-hub.md
│   │   ├── pathfinder-prompt-hub.md
│   │   ├── pathfinder-workflow-hub.md
│   │   └── pathfinder-docs-ingest.md
│   │
│   ├── LEAF NOTES (domain-specific compiled knowledge)
│   │   ├── docs-current-context.md       ← live sprint state (read early)
│   │   ├── docs-state-architecture.md    ← PathFinderState + Pydantic models
│   │   ├── docs-architecture.md          ← graph topology
│   │   ├── docs-eval-how-to-use.md       ← evaluation workflow
│   │   ├── docs-python-function-check-*.md  (5 buckets)
│   │   ├── docs-*-evaluation.md          ← per-stage audit logs
│   │   └── ... (40+ total)
│   │
│   └── CONTEXT (stable orientation)
│       └── docs-project-context.md
│
└── sources/docs/                      ← raw source documents (canonical wording)
    ├── evaluation/                    ← goals_evaluation.md, thinking_evaluation.md, etc.
    ├── architecture/
    ├── DEV_LOG.md                     ← dev-log navigation index
    └── dev-log/days/                  ← real dev-log content
```

**Reading path for PathFinder task:**
```
duc-os.md -> briefing.md if needed -> projects/pathfinder/README.md -> relevant hub -> leaf note
                                                                               ↓ only if precision needed
                                                                         sources/docs/
```

---

## 6. Agent Write Contract

### File Creation Gate (2-phase)

```
BEFORE calling Write:                   AFTER calling Write:
─────────────────────                   ────────────────────
A. type: → check SCHEMA type list       1. index.md entry → add + bump count
B. tags: → check index.md registry      2. SCHEMA Directory Map → add if new dir
C. New project? -> will need to sync     3. briefing.md Active Projects -> sync if new project
   briefing.md AND duc-os/current.md     4. duc-os/current.md Active Projects -> sync
                                         5. duc-os/current.md Vault Status -> update if context shift
```

Root cause of gate failures: agents write first, validate second.
Pre-write phase eliminates this by forcing resolution before touching Write tool.

### Self-Healing Protocol (runs on every read)

```
Auto-Fix (no approval):                 Flag+Fix (+ #auto-fixed tag):
──────────────────────                  ──────────────────────────────
Missing updated date → add today        Outdated info agent knows is wrong → update
Missing TL;DR → generate from content   Missing link between clearly related pages → add
Page missing from index → add + bump    Stub fillable from current context → expand
Tag typo matching registry → fix
Broken wikilink (target exists) → fix

Flag Only (→ sources/log/DATA_HOLES.md):
─────────────────────────────────────────
Gap needing a new source
Contradictions needing user judgment
Probable duplicates agent isn't sure about
```

**Mandatory log at end of every task:**
Append to `sources/log/days/YYYY-MM-DD.md` → sync `log.md` navigation line.
No exceptions. Even "nothing was fixed" gets logged.

---

## 7. Key Seams + Current Scale

```
Pages (notes): ~140    Sources: ~67    Active projects: 2
PathFinder notes alone: 40+
Index sections close to 30-entry split threshold: monitor
```

**Compile chain for PathFinder knowledge:**
```
repo code / eval runs / frontend runs
        │
        ▼
projects/pathfinder/sources/docs/   ← canonical wording lives here
        │  agent-compiled
        ▼
projects/pathfinder/notes/          ← summaries, key points, audit logs
        │  routing
        ▼
domain hubs -> README.md -> briefing.md dashboard -> duc-os/current.md
```

---

## 8. Optimization Targets

### Structural

| Issue | Current State | Optimization |
|-------|--------------|--------------|
| Index drift | Caught manually each session | No change — the session-start check handles it |
| Index size | ~140 entries, some sections near 30-entry limit | Split by subdomain when any section hits 30 |
| PathFinder notes count | 40+ leaf notes | Evaluation hub exists; architecture + workflow hubs may need auditing for stale entries |
| Two-location log writes | Vault day file + repo day file every time | No shortcut — both are canonical, must stay in sync |
| Source docs vs notes gap | Sources have more detail than notes | Flow-check domains one by one (evaluation ✓, next: architecture) |

### Agent Behavior

| Risk | When It Occurs | Fix Already In Place |
|------|---------------|----------------------|
| Tier skip (agent reads deep before briefing) | Eager parallel tool calls | CLAUDE.md + SCHEMA enforce serial Tier 0 before Tier 1 |
| File Creation without pre-write | Fast write → wrong type/tags | 2-phase gate in CLAUDE.md + SCHEMA |
| Re-healing stable routers | Agent re-validates briefing.md it already read | Stable Router Exception in SCHEMA |
| Missing log entry | Task "done" without write-back | Write-back rule + mandatory log section in CLAUDE.md |
| duc-os/current.md stale | User priorities shift, agent doesn't update | 7-day flag rule in Session Start Protocol |

### Human Maintenance

| File | Risk of Staleness | Trigger to Update |
|------|------------------|-------------------|
| briefing.md Active Projects | Medium - only updated on project init/archive | New project or project ships |
| duc-os/current.md | High - changes week to week | After every sprint update |
| duc-os/long-arc.md | Low - 90-day horizon | Review flag if >90 days old |
| index.md page count | Medium — manual bump required | Every ingest or note creation |
| SCHEMA.md Directory Map | Low — only when new dirs added | New directory creation |

---

## 9. Layer Responsibility Summary

```
duc-os.md        <- What operating route is this session in? (root meta-router)
duc-os/current.md <- What is active now? What's blocked? (live priorities)
briefing.md      <- Which projects are active? (dashboard, NOT deep context)
index.md         <- Where is everything? (routing table, NOT content)
log.md           <- What happened and when? (navigation to day files)
sources/         <- The raw truth (canonical wording, exact content)
notes/           <- The compiled truth (summaries, key points, decisions)
wiki/            <- Reusable knowledge (crosses project boundaries)
hubs             <- Domain routing (navigate within a project layer)
README.md        <- Project routing (entry point for project work)
```

**The rule:** each layer answers one question. When a layer starts doing two jobs, it breaks navigation.

## Duc OS Migration Note

This document is now an architecture reference, not the startup authority. If this file conflicts with [[duc-os]], [[SCHEMA.md]], [[AGENTS.md]], or [[CLAUDE.md]], the Duc OS-first route wins.
