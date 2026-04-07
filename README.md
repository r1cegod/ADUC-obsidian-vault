# ADUC Vault

**Owner:** Duc (Anh Duc) — CS student, FPT University, Vietnam  
**Purpose:** Personal knowledge vault and project workspace. Functions as a structured second brain and agent-readable documentation system.

---

## What This Is

This vault is two things at once:

1. **A personal knowledge system** — notes, context, and goals organized for fast recall across sessions.
2. **A project documentation hub** — canonical docs and derived summaries for active engineering projects.

The primary active project is **PathFinder**, a multi-agent AI career counselor for Vietnamese students, built as a portfolio piece for the FPT Software Engineering Scholarship.

---

## Start Here (Scholarship Reviewer)

If you are here to evaluate the work, read in this order:

| Step | File | What It Tells You |
|------|------|--------------------|
| 1 | [briefing.md](briefing.md) | Vault orientation and active project list |
| 2 | [context/me.md](context/me.md) | Who the owner is, background, goals |
| 3 | [context/goals.md](context/goals.md) | Engineering direction and scholarship context |
| 4 | [projects/pathfinder/README.md](projects/pathfinder/README.md) | PathFinder project — start here for the main work |

---

## PathFinder — Main Project

**PathFinder** is a multi-agent career counselor designed to help Vietnamese students navigate university and career decisions. It is the primary portfolio project submitted for the FPT SE Scholarship.

**Stack:** LangGraph · FastAPI · React · Python · Pydantic

**Status as of 2026-04-07:** Scholarship demo shipped 2026-03-30. Now in eval/hardening phase — auditing prompt stage quality and fixing known runtime issues.

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

```
ADUC/
├── README.md               ← you are here
├── briefing.md             ← vault orientation (read first)
├── index.md                ← full content routing table
├── SCHEMA.md               ← wiki operations manual
├── CLAUDE.md               ← agent behavior rules
├── log.md                  ← activity history
│
├── context/
│   ├── me.md               ← owner profile
│   ├── now.md              ← current focus and blockers
│   └── goals.md            ← short and long-term direction
│
├── projects/
│   └── pathfinder/
│       ├── README.md       ← project router (start here for PathFinder)
│       ├── notes/          ← derived summaries and hub pages (26 pages)
│       └── sources/        ← raw mirrored docs from the repo
│
├── wiki/                   ← general knowledge notes
├── references/             ← reference material
├── sources/                ← raw source files
├── templates/              ← page templates
├── journal/                ← time-stamped entries
└── pending/                ← unsorted drop zone
```

---

## Key Documents

| Document | Purpose |
|----------|---------|
| [context/me.md](context/me.md) | Owner background, skills, learning style |
| [context/now.md](context/now.md) | Current week's focus and open blockers |
| [context/goals.md](context/goals.md) | Scholarship goals and engineering direction |
| [index.md](index.md) | Full content routing table with tags |
| [SCHEMA.md](SCHEMA.md) | How the vault is operated (ingest, lint, self-healing) |
| [log.md](log.md) | Chronological activity log |

---

## Design Principles

- **Tiered loading:** agents read briefing → context → project README before opening any source file. This keeps session start-up fast and avoids context waste.
- **Source-of-truth separation:** raw docs live in `sources/`, derived summaries live in `notes/`. Never overwrite sources with opinions.
- **Self-healing:** every page touched in a session gets a health check (TL;DR present, updated date current, obvious wikilinks added).
- **Bilingual:** agent-facing outputs in Vietnamese, all technical docs and code in English.
