# ADUC Vault

> **TL;DR**: Human-facing overview of the ADUC vault; runtime agent routing starts from `context/hot.md -> duc-os.md`, then Duc OS chooses briefing, development, operations, vault-keeping, or project READMEs.

**Owner:** Duc (Anh Duc) - CS student, FPT University, Vietnam  
**Purpose:** Personal knowledge vault and project workspace. Functions as a structured second brain and agent-readable documentation system.

---

## What This Is

This vault is two things at once:

1. **A personal knowledge system** - notes, context, and goals organized for fast recall across sessions.
2. **A project documentation hub** - canonical docs and derived summaries for active engineering projects.

Current active projects include **Raven** as the active next scaffold, **PathFinder** as reviewable portfolio evidence unless a blocker appears, and **IELTS Writing** as a parallel training track.

## Agent Routing

This file is a human-facing overview, not the runtime startup router.

Use the vault branch stack instead:

```text
context/hot.md
  -> duc-os.md
      -> briefing.md dashboard
      -> development.md
      -> wiki/operations-hub.md
      -> vault-keeping.md
      -> project README
      -> branch hub if needed
      -> leaf
```

For technical help or code delegation, Duc OS routes to `development.md`.
For official operations, Duc OS routes to `wiki/operations-hub.md`.
For maintenance-family work or new branch placement, Duc OS routes to `vault-keeping.md`.
For project work, Duc OS uses `briefing.md` only as a dashboard, then routes to the project `README.md`.

---

## Start Here (Scholarship Reviewer)

If you are here to evaluate the work, read in this order:

| Step | File | What It Tells You |
|------|------|-------------------|
| 1 | [duc-os.md](duc-os.md) | Root operating layer, routing, and context authority |
| 2 | [duc-os/identity.md](duc-os/identity.md) | Who the owner is, working profile, communication protocol |
| 3 | [duc-os/long-arc.md](duc-os/long-arc.md) | Engineering direction, founder path, and escape-velocity context |
| 4 | [briefing.md](briefing.md) | Compact active-project dashboard |
| 5 | [projects/raven/README.md](projects/raven/README.md) | Raven project - current active scaffold |
| 6 | [projects/pathfinder/README.md](projects/pathfinder/README.md) | PathFinder project - reviewable portfolio work |

---

## PathFinder - Reviewable Project

**PathFinder** is a multi-agent career counselor designed to help Vietnamese students navigate university and career decisions. It is reviewable portfolio evidence for the FPT SE Scholarship.

**Stack:** LangGraph · FastAPI · React · Python · Pydantic

**Status as of 2026-04-25:** Scholarship demo shipped 2026-03-30. PathFinder is reviewable unless a concrete blocker threatens demo or review confidence.

### PathFinder Navigation

| Area | Entry Point |
|------|-------------|
| Architecture and graph shape | [pathfinder-architecture-hub.md](projects/pathfinder/notes/pathfinder-architecture-hub.md) |
| Live implementation context | [pathfinder-context-hub.md](projects/pathfinder/notes/pathfinder-context-hub.md) |
| Prompt engineering work | [pathfinder-prompt-hub.md](projects/pathfinder/notes/pathfinder-prompt-hub.md) |
| Evaluation pipeline | [pathfinder-evaluation-hub.md](projects/pathfinder/notes/pathfinder-evaluation-hub.md) |
| Workflows and handoff docs | [pathfinder-workflow-hub.md](projects/pathfinder/notes/pathfinder-workflow-hub.md) |
| All ingested docs (index) | [pathfinder-docs-ingest.md](projects/pathfinder/notes/pathfinder-docs-ingest.md) |

---

## Vault Structure

```text
ADUC/
|-- README.md                <- you are here
|-- duc-os.md                <- root operating layer and meta-router
|-- duc-os/                  <- identity, current state, long arc, KICKSTART, engines, protocol
|-- briefing.md              <- active-project dashboard under Duc OS
|-- index.md                 <- full content routing table
|-- SCHEMA.md                <- vault constitution for routing, schema, and propagation law
|-- CLAUDE.md                <- agent behavior rules
|-- AGENTS.md                <- Codex entry rules
|-- log.md                   <- activity history navigation
|
|-- context/
|   |-- hot.md               <- startup cache
|   |-- me.md                <- redirect to duc-os/identity.md
|   |-- now.md               <- redirect to duc-os/current.md
|   `-- goals.md             <- redirect to duc-os/long-arc.md
|
|-- projects/
|   `-- pathfinder/
|       |-- README.md        <- project router (start here for PathFinder)
|       |-- notes/           <- derived summaries and hub pages
|       `-- sources/         <- raw mirrored docs from the repo
|
|-- wiki/                    <- general knowledge notes
|-- references/              <- external links and source anchors
|-- sources/                 <- raw source files + activity-log source files (`articles/`, `docs/`, `transcripts/`, `log/`, ...)
|-- templates/               <- page templates
|-- journal/                 <- time-stamped raw capture (`daily/` is the reflection lane)
`-- pending/                 <- unsorted drop zone
```

---

## Key Documents

| Document | Purpose |
|----------|---------|
| [duc-os.md](duc-os.md) | Root operating layer and meta-router |
| [duc-os/identity.md](duc-os/identity.md) | Owner background, skills, learning style, communication protocol |
| [duc-os/current.md](duc-os/current.md) | Current focus, active projects, and open blockers |
| [duc-os/long-arc.md](duc-os/long-arc.md) | Escape velocity, founder path, distribution, and engineering direction |
| [index.md](index.md) | Full content routing table with tags |
| [development.md](development.md) | Top development router for Detect, Learn, and Delegate |
| [wiki/operations-hub.md](wiki/operations-hub.md) | Global registry for official vault operations |
| [vault-keeping.md](vault-keeping.md) | Maintenance-family hub for drift, logging, branch growth, and self-healing |
| [SCHEMA.md](SCHEMA.md) | Constitutional rules for routing, schema, propagation, and operation governance |
| [log.md](log.md) | Activity log navigation |

---

## Design Principles

- **Tiered loading:** agents read `context/hot -> duc-os -> smallest needed router` before opening any source file. This keeps session startup fast and avoids context waste.
- **Source-of-truth separation:** raw docs live in `sources/`, derived summaries live in `notes/`. Never overwrite sources with opinions.
- **Human vs agent boundary:** daily notes and other raw reflections stay human-primary; durable synthesis belongs in `wiki/`, project notes, `index.md`, and the vault log layer (`log.md` + `sources/log/`).
- **Graduation over rewriting:** recurring daily-note signals should be promoted into durable pages, not folded back into the raw note until the author's voice disappears.
- **Response-completion writeback:** if a response creates durable knowledge, the vault should be updated before that response ends.
- **Self-healing:** every page touched in a session gets a health check (TL;DR present, updated date current, obvious wikilinks added).
- **Bilingual:** agent-facing outputs in Vietnamese, all technical docs and code in English.
