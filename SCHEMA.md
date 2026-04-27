# SCHEMA.md — Wiki Constitution

> **TL;DR**: Constitutional rules for vault startup, page schema, routing law, propagation, and official-operation governance. Use hubs and operation leaves for execution.

> Shared schema for all agents operating on this vault.
> CLAUDE.md, AGENTS.md, family hubs, and operation leaves reference this file for canonical law.

---

## Vault Purpose

Personal master vault: second brain + project docs.
Owner reads it; agents read and write it; everything compounds over time.

---

## Session Start Protocol

Run this before every task. It is not optional.

This section is the canonical startup rule. Wrapper files like `AGENTS.md` should point here instead of restating a second competing sequence.

Wrapper exception: `context/hot.md` may be read before `briefing.md` when the wrapper requires the hot cache. That read is a startup cache read, not content descent, and it does not create a page-level repair obligation by itself.

```
0. Optional wrapper cache: context/hot.md
1. Read briefing.md                  ← always, except optional hot cache pre-read
2. Read context/now.md               ← always, before any content file
3. Check context/now.md updated date ← if > 7 days ago, flag before proceeding
4. Check briefing.md Active Projects ← must match context/now.md Active Projects
5. Check pending/                    ← if files exist, flag and offer to sort
6. Check if user revealed new info   ← update context/ before starting task
```

**Enforcement:** If you find yourself opening a wiki page, project note, or source file before completing steps 1-2, stop and go back. Skipping the tiered load is the most common failure mode.

**Canonical startup rule:** every task starts `briefing.md -> context/now.md`, with only the optional `context/hot.md` wrapper cache before it. Only after that may the path branch into `SCHEMA.md`, `index.md`, or a project README.

### Canonical Startup Matrix

After optional `context/hot.md` and required `briefing.md -> context/now.md`, choose the smallest next step that fits the task:

| Task type | Next page |
|-----------|-----------|
| Simple repo task or direct question | Stop if Tier 0+1 is already enough |
| Active project repo work | `projects/<name>/README.md` |
| Wiki operation (ingest, sort, lint, query, archive, draft, self-healing) | `wiki/operations-hub`, then the canonical leaf |
| Project workflow / docs / handoff question | `projects/<name>/README.md`, then the relevant hub |
| Exact contract wording / source precision | relevant project note first, then raw source only if still needed |

Default for project work:
- `context/hot.md` only if required by the wrapper
- `briefing.md`
- `context/now.md`
- `projects/<name>/README.md`
- one targeted hub or note
- raw sources only when precision requires it

## Fast Route

Use this when you need the smallest next page instead of scanning the whole manual:

| Need | Next page |
|------|-----------|
| Vault maintenance, drift, logging, or workflow audit | `vault-keeping.md` |
| Decide where a new durable vault node should attach | `vault-keeping.md` -> `wiki/operations/branch-growth-operation` |
| Official operation family or canonical workflow leaf | `wiki/operations-hub` |
| Exact constitutional rule, schema, or propagation law | `SCHEMA.md` |
| Project work | `projects/<name>/README.md` |
| Architecture planning | `projects/<name>/README.md` -> relevant architecture hub -> active `.canvas` |
| Collaborative feature drafting | `wiki/operations-hub` -> `wiki/operations/draft-operation` |
| Technical-help / learning / delegation gate | `development.md` -> `wiki/operations/detect-operation` |

## Official Operation Evolution Law

This is mandatory.

Any operation that is officially documented in the vault is a **living contract**, not a frozen ritual.

```text
officially documented
  -> must be used in real work
  -> must be reviewed after use
  -> must evolve when friction is found
```

Hard rule:

```text
If an official operation is used,
and that use reveals drift, friction, missing routing, repeated confusion,
or wasted tokens,
the operation must be updated in the vault in the same session when cheap.
If the fix is not cheap, log the gap explicitly that same day.
```

Do not treat "officially documented" as permission to fossilize a workflow.

The vault evolves by:
- use
- audit
- patch
- reuse

Operations that do not evolve after use become dead weight and mislead later sessions.

Minimum after-use audit for any official operation:
- Was the next page obvious?
- Was the route too long?
- Did two docs repeat the same thing?
- Did the operation depend on memory instead of routing?
- Did it burn more tokens than needed?
- Should the operation wording, order, or closeout be tightened?

Closeout rule:
- cheap fix -> patch the official docs now
- not-cheap fix -> log a named operation gap in the day file now

## File Creation Gate

**Branch Growth + two-phase contract: choose parent branch first, then PRE-write resolve, POST-write register.**
The most common failure mode is writing first and validating second — by then the damage (wrong type, unregistered tags, broken sync, fake hierarchy) is already in the file and requires a repair pass. Resolve before writing.

### Phase 0 — Branch Growth (before deciding to create the file)

Run [[wiki/operations/branch-growth-operation]] for any durable vault node. Decide:

```text
1. Parent branch
2. Node role: hub, leaf, source, sample, report, log, operation
3. Real-depth reason
4. Expected child types
5. Forbidden contents
6. First parent link
7. Required propagation targets
```

If a proposed hub does not reduce future search cost, create or update a leaf under the nearest valid branch instead.

### Phase 1 — Pre-Write (before calling the Write tool)

Resolve these questions against live vault state before writing a single character of frontmatter:

```
PRE-WRITE CHECKLIST (run before opening Write tool):

A. type:
   Open SCHEMA.md type list. Pick an existing type.
   If none fits → add the new type to the list FIRST, then write.
   Do NOT invent a type and register it later.

B. tags:
   Open index.md tag registry. Select from existing tags only.
   If a genuinely new tag is needed → add it to the registry FIRST.
   Do NOT use tags that aren't in the registry.
   Avoid over-granular tags (e.g. task1, task2) — prefer reusable
   domain tags (ielts, writing, schema).

C. routing:
   Confirm the first parent link from Branch Growth.
   Hub files link from their parent router first.
   Leaf files link from the nearest valid hub or README, not every root router.

D. Growth Contract:
   Plan the `## Growth Contract` before writing.
   Include parent branch, node role, first parent link, growth trigger,
   forbidden contents, and expected child/source boundary when relevant.

E. Project file?
   If this file is a project README or adds a new project:
   → You will need to add it to BOTH briefing.md Active Projects
     AND context/now.md Active Projects in this same session.
   These two lists must always match. The Session Start Protocol
   checks for this mismatch on every session load.
```

### Phase 2 — Post-Write (immediately after Write, before any other action)

```
After every Write to the vault:

1. Growth Contract
   New durable wiki/project/reference/learning page?
   → Confirm `## Growth Contract` exists unless this is raw daily capture or pending material.

2. index.md entry
   File in wiki/, learning/, references/, or projects/?
   → Add entry under the correct section. Bump page count.

3. SCHEMA Directory Map
   File is in a directory not listed in the Directory Map?
   → Add the directory row now.

4. SCHEMA type list
   (Should already be registered from Phase 1 — verify only.)

5. Tag registry
   (Should already be registered from Phase 1 — verify only.)

6. briefing.md Active Projects vs Navigation
   File is a new project README?
   → Add to briefing.md Active Projects AND context/now.md Active Projects.
   → Do NOT add a separate Navigation entry for active projects.
     Active Projects already routes to them. Navigation is for
     utilities (SCHEMA, index, log, context), not active projects.
   File is a global utility hub (protocol, schema, non-project reference)?
   → Add to briefing.md Navigation only.

7. context/now.md
   File changes what agents should know on next session start?
   → Update context/now.md Vault Status now.
   If it's a new project → also update Active Projects section (not just Vault Status).
```

**Why this exists:** "write back durable changes at end of task" relies on the agent remembering — which is the failure mode. A gate that triggers per Write call cannot be forgotten.

**Root cause of gate failures:** agents write first, validate second. By the time the post-write gate runs, the file has wrong types and unregistered tags that require a second edit pass. The pre-write phase eliminates this.

**What is NOT covered by this gate:** edits to existing files. Those are covered by the Self-Healing Protocol below.

---

## Tiered Loading Protocol

Load context in tiers. **Stop after each tier and ask: is this enough to complete the task?** Only descend if you genuinely need more.

```
Tier 0: briefing.md        (~200 tokens)  — ALWAYS read first. Stop here if the task is simple.
         ↓ only if you need more
Tier 1: context/now.md     (~200 tokens)  — read for current priorities
        index.md           (~500-1500 tokens) — read to find specific pages
        SCHEMA.md          (this file) — read only when doing wiki operations
         ↓ only if you need more
Tier 2: wiki/, projects/   — read only the pages relevant to the task
```

**Simple task** (write code, answer a question): read `briefing.md` → stop if enough context.
**Wiki operation** (ingest, query, lint): read `briefing.md` → `SCHEMA.md` → `index.md` → relevant pages.
**Project task** (work on a specific active project): read `briefing.md` → identify project → open `projects/<name>/README.md` → read the relevant pages in `projects/<name>/notes/` → open raw project sources only when precision requires it.

**Anti-pattern to avoid:** opening multiple content files in parallel before completing Tier 0. Parallel reads are efficient but bypass the tiered stop-check. Read briefing.md alone first, then decide.

**Note on agent tool defaults:** Claude Code defaults to parallel tool calls for efficiency. This creates a structural tension with the tiered stop-check. Resolution: parallel reads are acceptable *within* a tier (e.g., reading two Tier 1 files together is fine), but never *across* tiers (Tier 0 must complete before opening Tier 1 files). The stop-check happens between tiers, not between individual reads within a tier.

**Stop-check applies to writes too:** The tiered stop-check is not just a reading rule. Creating vault files is a Tier 2+ action — it should only happen after you have completed at least Tier 0 + Tier 1 load. If you find yourself about to call the Write tool without having read briefing.md and context/now.md in this session, stop and load them first.

---

## Directory Map

| Path | Contents | Notes |
|------|----------|-------|
| `briefing.md` | Vault orientation | Always read first. Keep under 500 tokens. |
| `development.md` | Top-tier development-domain router | Detect -> Learn/Delegate for technical help and code delegation. |
| `index.md` | Content routing table | Updated after every ingest. |
| `log.md` | Activity log navigation | One line per day; real log blocks live under `sources/log/days/`. |
| `context/` | User profile + active state | The "brain" layer. |
| `pending/` | Drop zone for unsorted files | Agents sort and ingest. Check on every session. |
| `sources/` | Raw source documents + vault activity-log source files | Global sources. Use `articles/`, `docs/`, `transcripts/`, `misc/`, `projects/`, and `log/` as the first filing layer. |
| `images/` | Image sources (screenshots, diagrams, photos) | Treated as sources — agents read and reference. |
| `references/` | Bookmarks, links, citations | External reference pages live here (not in wiki/). |
| `wiki/` | Agent-generated knowledge pages | Core knowledge base — entities, concepts, synthesis. |
| `projects/` | Project workspaces | Each project is self-contained with its own sources/notes. |
| `journal/daily/` | Daily notes | YYYY-MM-DD.md format. |
| `learning/` | Learning sessions | One file per feature attempt, following `wiki/pre-wire-protocol`. Index at `learning/README.md`. Session files live in `learning/sessions/`. |
| `templates/` | Obsidian templates | User-managed. |
| `assets/` | Obsidian attachments | Auto-managed by Obsidian when pasting/embedding into notes. |

All directories are read/write for agents.

### Disambiguation

- **`images/` vs `assets/`**: `images/` holds curated source images the user or agent explicitly files (screenshots, diagrams, photos). `assets/` is Obsidian's automatic attachment folder — when you paste an image into a note in Obsidian, it lands here. Agents should file images in `images/`; leave `assets/` to Obsidian.
- **`sources/projects/` vs `projects/<name>/sources/`**: `sources/projects/` holds raw materials that don't belong to a specific project workspace yet. `projects/<name>/sources/` holds sources scoped to a specific project. When a project exists in `projects/`, its sources go there. When in doubt, put it in `projects/<name>/sources/`.
- **`sources/transcripts/`**: use this for local transcript exports of audio/video sources. Keep the transcript as the practical raw text layer, and keep the external URL separately in a `references/` page.
- **`sources/log/`**: this is the source lane for the global vault activity log. `sources/log/days/YYYY-MM-DD.md` holds the real daily activity notes, while `log.md` stays as the navigation index.
- **`references/`**: Holds reference pages (bookmarks, external links, bibliographies) — these are NOT wiki pages. They use the `tpl-reference` template and are indexed under `## References` in `index.md`.

### Project-Local vs Global Wiki Scope

When ingesting project sources, decide where wiki pages go:

| Criterion | Destination |
|-----------|-------------|
| Topic is project-specific (internal design decisions, project-only jargon, task notes) | `projects/<name>/notes/` |
| Topic is reusable knowledge (a tool, a concept, a person, a technique) | `wiki/` (global) |
| Unsure | Default to `wiki/` — knowledge is more valuable when discoverable globally |

### Human vs Agent Write Boundary

Treat the vault as two cooperating layers:

- **Human-primary raw capture**: `journal/daily/`, meeting notes, rough reflections, and any note whose main value is the author's voice or unprocessed thinking
- **Agent-maintained compiled layer**: `wiki/`, `projects/<name>/notes/`, `index.md`, and the `log.md` navigation layer plus `sources/log/`

Default rule:
- Agents should summarize *out of* human-primary notes into compiled pages rather than rewriting the original notes into agent voice.
- If a daily note contains a durable idea, promote it into a concept, synthesis, project note, or task page instead of over-editing the day note.
- Exception: `context/` files and daily notes may still be updated when the task explicitly asks for it or when the conversation-triggered context rule requires it.

### Two-Layer Human Log Pattern

For project-local human logs, mirrored project dev logs, and the global vault activity log, prefer a two-layer structure:

- index file: short navigation only, one line per day
- day files: the real note, one markdown file per day

Rules:

- update the existing day file if the same day changes again
- keep human-written day files short and readable
- do not turn the index into the real log
- this pattern is preferred for project-local logs and the global vault activity log

### Daily Note Graduation

`journal/daily/` is the raw reflection lane, not the final knowledge layer.

Promote a daily-note fragment when it is:
- stable enough to matter beyond one day
- reusable across projects or questions
- a decision, pattern, or workflow that future sessions should find quickly

Good destinations:
- reusable knowledge -> `wiki/concepts/` or `wiki/synthesis/`
- project-specific learning -> `projects/<name>/notes/`
- short-lived planning -> keep it in the daily note or move it to the relevant task system

Project README pages always live at `projects/<name>/README.md`.

### Project Navigation Protocol

For any task tied to a named project or an active project listed in `briefing.md`, agents should use the smallest sufficient route:

1. `briefing.md` — confirm the active project and current vault focus
2. `projects/<name>/README.md` — use this as the project router
3. Choose the smallest next step that fits the task:
   - stable orientation -> `projects/<name>/notes/docs-project-context.md` or equivalent
   - live workstream -> `projects/<name>/notes/docs-current-context.md` or equivalent
   - domain-specific work -> the relevant hub
   - exact contract wording -> the relevant raw source
4. Descend only when the current page is insufficient

Rules:
- Do not jump straight into `projects/<name>/sources/` unless the task is explicitly source-first or wording precision truly matters.
- Project README must act as a task router, not just a status note.
- Hubs are routing aids, not mandatory reading sequences.
- Avoid opening multiple hubs or leaf notes by default. Pick one likely route, then stop-check.
- Project notes are the default working knowledge layer for project-specific tasks.
- If a reusable concept is discovered while working in a project, file it into global `wiki/` and link back from the project notes.

### Project Hub Pattern

When a project grows beyond a handful of notes, add project-local synthesis hubs in `projects/<name>/notes/`.

Recommended hub types:
- `architecture-hub`
- `context-hub`
- `prompt-hub`
- `evaluation-hub`
- `workflow-hub`

Hub rules:
- Each hub routes to the smaller leaf notes inside one domain.
- Project README links to hubs first, not just to individual leaf notes.
- Hubs should present suggested entry points by task, not a mandatory read order.
- Agents should open the relevant hub before reading multiple leaf notes in the same domain, but should stop there if the hub already answers the routing need.
- Hubs are preferred once a project area has 3+ related notes or is expected to keep growing.

### Canvas-First Architecture Work

Use this when the task is architecture-heavy rather than code-local.

Route:

```text
briefing.md
  -> context/now.md
  -> projects/<name>/README.md
  -> relevant architecture hub
  -> active .canvas board
```

Canvas-first applies when the decision changes:
- system shape
- loop boundaries
- storage boundaries
- promotion rules
- routing/ownership
- ingestion structure

Do not force Canvas into:
- one-function logic
- local refactor mechanics
- helper implementation details
- signature-level code planning

Optimization rules:
- One active canvas board per architecture domain. Do not spread one decision across many boards.
- Stable points on the canvas must be mirrored into markdown notes the same session.
- Architecture tasks should finish vault work first: canvas -> note mirror -> router/context update -> day log -> response.
- If a canvas file changes, the relevant architecture hub or project README must still route to that board clearly.

When the architecture task is also collaborative drafting, pair Canvas-first with [[wiki/operations/draft-operation]] instead of creating a second architecture-specific draft loop.

---

## Page Conventions

### Filenames
- Lowercase, hyphens for spaces: `machine-learning.md`, `john-smith.md`
- Always romanized (even for Vietnamese content): `tri-tue-nhan-tao.md`
- No dates in filenames (dates live in frontmatter)
- Max 60 characters

### Frontmatter Standard

Required on every wiki page, project page, and reference page:

```yaml
---
type: entity | concept | synthesis | source-summary | project | reference | context | learning-session | hub | protocol | operation | note
title: "Human-readable title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
status: stub | active | mature | archived
lang: en | vi
---
```

**Type-specific optional fields:**

| Field | Used by | Purpose |
|-------|---------|---------|
| `source: "[[sources/path]]"` | source-summary | Link to raw source |
| `aliases: ["alt name"]` | entity, concept | Alternative names for Obsidian search |
| `priority: low \| medium \| high` | project | Project priority |
| `url: "https://..."` | reference | External URL |

**Daily notes** use a lighter schema (no `title`, `status`, or `updated` — the date IS the identity):

```yaml
---
type: daily
date: YYYY-MM-DD
tags: [journal]
lang: en
---
```

**Status meanings:**
- `stub` — placeholder, minimal content, needs expansion
- `active` — being actively worked on or recently updated
- `mature` — comprehensive, stable
- `archived` — outdated or superseded, kept for reference

### Template Mapping

| Type | Template | Default location |
|------|----------|-----------------|
| `source-summary` | `templates/tpl-source` | `wiki/` subfolder matching topic |
| `entity` | `templates/tpl-entity` | `wiki/entities/` |
| `concept` | `templates/tpl-concept` | `wiki/concepts/` |
| `synthesis` | `templates/tpl-synthesis` | `wiki/synthesis/` |
| `project` | `templates/tpl-project` | `projects/<name>/README.md` |
| `reference` | `templates/tpl-reference` | `references/` |
| `daily` | `templates/tpl-daily` | `journal/daily/` |
| `protocol` | `templates/learning-session` or local protocol page format | `wiki/` or `projects/<name>/notes/` |
| `operation` | local operation page format | `wiki/operations/` |

### Specialized Ingest Templates

Use these when they fit better than the generic templates:

| Use case | Template |
|----------|----------|
| YouTube / video reference page | `templates/tpl-youtube-reference` |
| YouTube / video source summary | `templates/tpl-youtube-source` |
| GitHub repo / issue / PR reference page | `templates/tpl-github-reference` |
| GitHub source summary | `templates/tpl-github-source` |
| Reddit thread reference page | `templates/tpl-reddit-reference` |
| Reddit source summary | `templates/tpl-reddit-source` |
| Multi-source human-readable digest | `templates/tpl-topic-digest` |
| Change / migration report | `templates/tpl-change-report` |

### Page Structure

Every durable wiki/project/reference page created after 2026-04-25 must have, in order:
1. Frontmatter (YAML)
2. `> **TL;DR**: One-sentence summary.` — mandatory, enables tiered loading
3. `## Growth Contract` — parent branch, node role, first parent link, growth trigger, forbidden contents, plus expected child/source boundary when relevant
4. Content sections (vary by type — follow the template)
5. `## Related` section at bottom with `[[wikilinks]]` to related pages

Legacy pages may be upgraded opportunistically when edited, but do not burn a task rewriting the whole vault just for this section.

**Page size targets:**
- Source summaries: 200-500 words
- Entity/concept pages: 100-400 words
- Synthesis pages: up to 1000 words
- Reference pages: 50-200 words

### Wikilinks
- Always use Obsidian `[[wikilinks]]`, never markdown `[text](url)` for internal links
- Use display text when helpful: `[[machine-learning|ML]]`
- Every page should have at least 2 outgoing links
- Link to wiki pages from wiki pages; link to sources only from the `source:` frontmatter field

### Language
- Structural files (SCHEMA.md, CLAUDE.md, AGENTS.md, index.md, log.md, briefing.md): English
- Wiki page content: matches source language (EN or VI)
- Frontmatter keys: always English
- Filenames: always romanized (no Vietnamese diacritics in filenames)

---

## INGEST Operation

Canonical leaf: [[wiki/operations/ingest-operation]]

Constitutional role:
- INGEST turns raw source material into compiled vault knowledge.
- Dedup must be resolved before creating or updating summary pages.
- INGEST is not complete until cross-links, index updates, relevant context patches, and logging are finished.
- Use the leaf page for file-type handling and the full execution sequence.

---

## SORT Operation (Pending Folder)

Canonical leaf: [[wiki/operations/sort-operation]]

Constitutional role:
- SORT is the official lane for moving `pending/` material into the right source or reference location.
- Ambiguous destination means ask, not guess.
- `sort and ingest` is valid, but each operation still owes its own writeback.
- Use the leaf page for destination rules and execution order.

---

## QUERY Operation

Canonical leaf: [[wiki/operations/query-operation]]

Constitutional role:
- QUERY answers against compiled vault knowledge first, not raw sources by default.
- Good query answers can be promoted into durable pages when the user asks to file them.
- Project-specific queries should route through the project README before deep reads.
- Use the leaf page for the full search, synthesis, and file-back sequence.

---

## DRAFT Operation

Canonical leaf: [[wiki/operations/draft-operation]]

Constitutional role:
- DRAFT is the official iterative drafting loop when the artifact is meant to improve through feedback.
- The loop must optimize for reaction, not premature completeness.
- DRAFT keeps one live artifact path and mirrors stable decisions into the vault layer that should remember them.
- Use the leaf page for the drafting sequence.

---

## BRANCH GROWTH Operation

Canonical leaf: [[wiki/operations/branch-growth-operation]]

Constitutional role:
- BRANCH GROWTH runs before File Creation Gate for durable vault nodes.
- It decides parent branch, node role, real-depth reason, expected child types, forbidden contents, first parent link, and propagation targets.
- It requires new durable entries to carry a Growth Contract so the entry is born branch-aware and can grow without becoming a blob.
- New hubs are allowed only when they reduce future search cost or prevent an overloaded parent branch.
- Use the leaf page for the exact branch decision sequence.

---

## PROJECT INIT Operation

Canonical leaf: [[wiki/operations/project-init-operation]]

Constitutional role:
- PROJECT INIT creates a new project workspace with a real router, not just an empty folder.
- Every project starts with a README router, `notes/` compiled-knowledge lane, and `sources/` raw/evidence lane.
- New projects must sync `briefing.md`, `context/now.md`, and `index.md` in the same session.
- README pages are routing hubs, not passive descriptions; deeper hubs emerge from real branch pressure, not template worship.
- Use the leaf page for exact structure and sync steps.

---

## ARCHIVE Operation

Canonical leaf: [[wiki/operations/archive-operation]]

Constitutional role:
- ARCHIVE retires pages without breaking routing or link integrity.
- Archived pages are kept, not deleted, unless the user explicitly wants destructive cleanup.
- Archive changes must update the router layer that still points to the item.
- Use the leaf page for the exact archive sequence.

---

## DEVELOPMENT Operations

Canonical hub: [[development]]
Canonical leaves: [[wiki/operations/detect-operation]], [[wiki/operations/learn-operation]], [[wiki/operations/delegate-operation]]

Constitutional role:
- Development is the top-domain for technical help, ownership learning, and code delegation.
- Detect always runs before Learn or Delegate.
- Learn is the current user-facing manual for help/docs/mechanism/audit/Build-First/Pre-Wire/Vibe Docing behavior.
- Delegate writes code only after ownership/pattern clarity and must not invent new feature surface unless necessary and justified.

---

## LINT Operation

Canonical leaf: [[wiki/operations/lint-operation]]

Constitutional role:
- LINT is the official structural audit lane for drift, routing health, and stale knowledge surfaces.
- LINT may repair cheap structural defects, but it should log gaps that require judgment or new sources.
- Maintenance-family routing should prefer [[vault-keeping]] first when the task is obviously maintenance-scoped.
- Use the leaf page for the audit sequence and report format.

---

## Conversation-Triggered Context Update

Canonical leaf: [[wiki/operations/context-update-operation]]

Constitutional role:
- Conversation can change vault context even when no source document was ingested.
- Personal info, project-state changes, and priority changes must update the right `context/` file before the main task when they matter for future routing.
- Architectural decisions, code behavior, and file paths do not get patched from conversation alone; verify them in the actual files first.
- Use the leaf page for trigger and closeout steps.

---

## Self-Healing Protocol

Canonical leaf: [[wiki/operations/self-healing-operation]]

Constitutional role:
- Self-healing is mandatory after durable vault edits and task-affecting structural defects.
- Evidence-only reads do not trigger repair just because a page was read.
- Logging is mandatory for durable work; `log.md` sync happens only for a new day or changed daily summary.
- Use the leaf page for the execution sequence and closeout checklist.

### Evidence-Only Read Exception

Use this exception when all are true:
- The page was not edited or created in the current task.
- No missing frontmatter/TLDR, broken routing link, stale active-project state, or obvious contradiction would mislead the next agent.
- The task result does not require that page to become the canonical summary.

Allowed write-back:
- one day-log line for evidence reads
- compact `context/hot.md` delta only when continuity changed
- no forced `log.md` sync when the summary line still holds

### Stable Router Exception

These pages are high-frequency routers:
- `briefing.md`
- `context/now.md`
- `projects/<name>/README.md`
- project hub pages

If a stable router page:
- was already validated earlier the same day
- was not edited in the current task
- and showed no structural issue when read

then do not force a page-by-page repair pass again. A single log note like "stable router pages checked, no repair needed" is enough.

---

## Scalability Rules

1. **Index splitting**: when any section exceeds 30 entries, split into domain sub-sections (e.g., `## Entities > AI`, `## Entities > Finance`)
2. **Synthesis hubs**: when 5+ pages share a theme, create a synthesis hub page that links to all of them. Index entry points to the hub.
   - For projects, prefer domain hubs inside `projects/<name>/notes/` before the graph gets visually noisy.
3. **Tag registry**: at the bottom of `index.md`. Check before creating new tags. Add new tags to the registry when first used.
4. **Archival**: `status: stub` pages not updated in 60+ days → set `status: archived`, move to "Archived" section in index
5. **No deep nesting**: never add subdirectories beyond what's defined in this schema. Use tags and links instead.
6. **Index splitting at scale (300+ pages)**: split into `index-entities.md`, `index-concepts.md`, etc. Root `index.md` becomes meta-router.

---

## Propagation Sync Matrix

> Agent lookup table: if you write or edit file X, these downstream targets must also be checked.
> The PostToolUse hook (`scripts/check_propagation.py`) surfaces this automatically after every Write/Edit.
> Update this matrix whenever a new structural node is added to the vault.

### Exact-Path Rules

| File edited | Must check | Why |
|-------------|-----------|-----|
| `briefing.md` | `context/now.md` | Active Projects list must match between both files |
| `context/now.md` | `briefing.md` | Active Projects list must match between both files |
| `context/now.md` | `index.md` | Vault Status changes may require index header update |
| `SCHEMA.md` | `CLAUDE.md`, `AGENTS.md` | Rule changes in SCHEMA must be reflected in both wrapper files |
| `CLAUDE.md` | `AGENTS.md` | Behavioral rule changes must be consistent across agent entry points |
| `AGENTS.md` | `CLAUDE.md` | Behavioral rule changes must be consistent across agent entry points |
| `context/hot.md` | _(terminal)_ | Nothing feeds from the hot cache |
| `development.md` | `briefing.md`, `AGENTS.md`, `CLAUDE.md`, `wiki/operations-hub.md`, `index.md` | Top development-domain routing must stay visible from startup and both agent wrappers |
| `wiki/operations/branch-growth-operation.md` | `vault-keeping.md`, `wiki/operations-hub.md`, `wiki/operations/file-creation-gate.md`, `wiki/operations/project-init-operation.md`, `index.md` | Branch Growth must stay visible from maintenance, operation routing, and creation gates |
| `index.md` | _(terminal)_ | Routing table — nothing reads index to update itself |
| `log.md` | _(terminal)_ | Navigation index — content lives in day files |
| `briefing.md` | _(terminal)_ | Entry point — nothing reads briefing to update itself |

### Pattern Rules

| File pattern | Must check | Why |
|-------------|-----------|-----|
| `projects/*/README.md` | `briefing.md`, `context/now.md` | Project status changes propagate to Active Projects lists |
| `projects/*/notes/*-hub.md` | `projects/*/README.md` (same project) | Hub routing changes may require README task-router update |
| `projects/*/notes/*.canvas` | `projects/*/notes/<project>-architecture-hub.md`, `projects/*/README.md` (same project) | Canvas routing changes must stay explicit and discoverable from the project docs layer |
| `sources/log/days/YYYY-MM-DD.md` | `log.md` | Day file write requires navigation line sync in log.md |
| `projects/*/notes/*.md` | `index.md` | Verify index entry exists and parent hub TL;DR is current |
| `wiki/**/*.md` | `index.md` | Verify index entry exists and is current |
| `references/*.md` | `index.md` | Verify index entry exists and is current |

### Adding a New Structural Node

When you add a new project README, hub, or vault-root operational doc:
1. Run Branch Growth and add the Growth Contract section
2. Add an exact-path row to this matrix for the new file when pattern rules are not enough
3. Add `feeds_into:` to the new file's frontmatter (if it has frontmatter)
4. Add the inverse relationship — what feeds INTO the new file
5. Update `scripts/check_propagation.py` `EXACT_RULES` dict with the new entry when custom downstream targets are required

### Reference Documents
- Full implementation: `vault_propagation.md` (vault root)
- Hook script: `scripts/check_propagation.py`
- Hot cache: `context/hot.md`
