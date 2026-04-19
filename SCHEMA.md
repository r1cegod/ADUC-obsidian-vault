# SCHEMA.md — Wiki Operations Manual

> **TL;DR**: Canonical operations manual for vault startup, file creation, ingest, sort, query, lint, propagation, and self-healing rules.

> Shared schema for all agents operating on this vault.
> CLAUDE.md and AGENTS.md are thin wrappers that reference this file.

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
| Wiki operation (ingest, sort, lint, query, archive) | stay in `SCHEMA.md`, then open `index.md` only if needed |
| Project workflow / docs / handoff question | `projects/<name>/README.md`, then the relevant hub |
| Exact contract wording / source precision | relevant project note first, then raw source only if still needed |

Default for project work:
- `context/hot.md` only if required by the wrapper
- `briefing.md`
- `context/now.md`
- `projects/<name>/README.md`
- one targeted hub or note
- raw sources only when precision requires it

## File Creation Gate

**Two-phase contract: PRE-write resolve, POST-write register.**
The most common failure mode is writing first and validating second — by then the damage (wrong type, unregistered tags, broken sync) is already in the file and requires a repair pass. Resolve before writing.

### Phase 1 — Pre-Write (before calling the Write tool)

Resolve these three questions against live vault state before writing a single character of frontmatter:

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

C. Project file?
   If this file is a project README or adds a new project:
   → You will need to add it to BOTH briefing.md Active Projects
     AND context/now.md Active Projects in this same session.
   These two lists must always match. The Session Start Protocol
   checks for this mismatch on every session load.
```

### Phase 2 — Post-Write (immediately after Write, before any other action)

```
After every Write to the vault:

1. index.md entry
   File in wiki/, learning/, references/, or projects/?
   → Add entry under the correct section. Bump page count.

2. SCHEMA Directory Map
   File is in a directory not listed in the Directory Map?
   → Add the directory row now.

3. SCHEMA type list
   (Should already be registered from Phase 1 — verify only.)

4. Tag registry
   (Should already be registered from Phase 1 — verify only.)

5. briefing.md Active Projects vs Navigation
   File is a new project README?
   → Add to briefing.md Active Projects AND context/now.md Active Projects.
   → Do NOT add a separate Navigation entry for active projects.
     Active Projects already routes to them. Navigation is for
     utilities (SCHEMA, index, log, context), not active projects.
   File is a global utility hub (protocol, schema, non-project reference)?
   → Add to briefing.md Navigation only.

6. context/now.md
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
type: entity | concept | synthesis | source-summary | project | reference | context | learning-session | hub | protocol | note
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

Every wiki page must have, in order:
1. Frontmatter (YAML)
2. `> **TL;DR**: One-sentence summary.` — mandatory, enables tiered loading
3. Content sections (vary by type — follow the template)
4. `## Related` section at bottom with `[[wikilinks]]` to related pages

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

Primary operation. Triggered when user asks to process source(s).

### Pre-Check — Deduplication

Before creating any wiki page:
1. Search `index.md` for the source path or title
2. `Grep` wiki pages for the source filename
3. If a wiki page already exists for this source:
   - **Same source, no changes**: skip, inform user
   - **Updated source**: update the existing wiki page(s), bump `updated` date, log as `RE-INGEST`
   - **Different source, same topic**: update existing pages with new information, add second source reference

### Step 1 — Read & Analyze Source

- Read the source fully
- Identify: main topic, entities mentioned, concepts introduced, claims made
- Determine content language → sets `lang` field on all generated pages
- If source has images: read text first, then view key images for additional context

**File-type handling:**

| File type | How to process |
|-----------|---------------|
| Markdown (.md) | Read directly, standard ingest |
| PDF (.pdf) | Read with PDF tool, extract text + structure |
| Subtitle/transcript (.vtt, .srt, transcript markdown) | Normalize into markdown under `sources/transcripts/` when useful, then ingest from the normalized transcript |
| Images (.png, .jpg, .svg) | View image, describe content, extract any text |
| Video / YouTube | Capture metadata, create a `references/` page for the URL, extract a local transcript when possible, then ingest from the transcript plus video metadata |
| GitHub repo / issue / PR / gist | Summarize the purpose, architecture, workflows, and caveats. Distinguish repo-level facts from marketing copy or comments |
| Reddit post / comment thread | Capture the main claim, the strongest replies, disagreement pattern, and a reliability caveat. Treat anecdote and consensus separately |
| Code files (.py, .js, .ts, etc.) | Summarize purpose, key functions/classes, architecture patterns. Focus on *what it does and why*, not line-by-line |
| JSON/YAML/config | Extract schema structure, key settings, what it configures |
| Data files (.csv, .xlsx) | Summarize columns, row count, data shape, key patterns |
| Other/binary | Flag as unsupported, ask user how to handle |

### Step 2 — Discuss (optional)

- Summarize key takeaways to user
- Ask if there's anything to emphasize, skip, or connect to existing work
- User can say "just process it" to skip this step

### Step 3 — Create/Update Wiki Pages

**Primary page** (always create one):
- Source summary in the appropriate `wiki/` subfolder
- Sections: TL;DR, Summary (3-5 sentences), Key Points (bullets), Details (organized subsections), Related
- Frontmatter: `type: source-summary`, `source: [[path]]`, all required fields

**Secondary pages** (create or update as needed):
- New entities/concepts introduced → create stubs or full pages
- Existing entities/concepts with new information → update those pages

**Decision guide:**
- Entity/concept mentioned once → include in source summary Key Points, no separate page
- Entity/concept that is a main subject OR appears in 2+ sources → own page
- Entity/concept already has a page → update it, never duplicate

### Step 4 — Cross-Reference

- Add wikilinks between new pages and existing related pages
- Update `## Related` sections on both new and existing pages
- Every new page links to at least 2 existing pages (if available)

### Step 5 — Update Index

- Add entries under the appropriate section in `index.md`
- Format: `- [[wiki/path|Display Name]] — TL;DR one-liner (tags)`
- For sources section: `- YYYY-MM-DD: [[wiki/path|Title]] ← [[sources/path|raw]] (tags)`
- Bump page/source counts in the index header

### Step 6 — Update Context (if relevant)

- Source relates to active project → update `context/now.md` if priorities shifted
- Source reveals user info → update `context/me.md`
- Source affects direction → update `context/goals.md`
- Update `briefing.md` if active projects or focus changed

### Step 7 — Log

```
## [YYYY-MM-DD] INGEST | Source Title
- Source: [[sources/path/file]]
- Created: [[wiki/path/primary-page]] + N stubs
- Updated: [[page1]], [[page2]]
- Tags: #tag1, #tag2
```

### Folder Ingest

When user asks to ingest an entire directory (e.g., "ingest all docs in `sources/docs/`" or "ingest `projects/myapp/sources/`"):

1. **Scan**: list all files in the directory (recursive)
2. **Order**: process files in logical order:
   - README/overview files first (they provide context for everything else)
   - Then by dependency: foundational docs before specialized ones
   - If no clear order: alphabetical
3. **Process each**: run full INGEST Steps 1-7 per file
4. **Cross-reference pass**: after all files processed, check for links between the newly created wiki pages
5. **Synthesis**: if 5+ sources were ingested, create a synthesis page summarizing the batch
6. **Project-level synthesis**: if all files belong to one project, create or update the project README with an overview

### Batch Ingest

When processing multiple unrelated sources at once:
- Process each source through Steps 1-7 individually
- After all: mini-lint pass to check cross-references between newly ingested sources
- If 2+ sources clearly belong to one topic: create or update a human-readable synthesis page so the owner can understand the topic without rereading every raw source
- If 5+ sources: create or update a synthesis page summarizing the batch
- Complete the writeback before sending the response; do not defer the digest or index/log updates to a later "session close"

### Image Ingest

- Agent views the image and creates a wiki page describing what it shows
- If related to existing entity/concept → link the pages
- Diagrams/screenshots with text → extract text into wiki page
- Wiki page includes: `![[images/path/file.png]]` for inline preview

---

## SORT Operation (Pending Folder)

Triggered when user asks to process `pending/` or as part of ingest.

1. Scan `pending/` for files (including subdirectories)
2. Determine destination for each:
   - Markdown article/note → `sources/articles/`
   - PDF/technical doc → `sources/docs/`
   - Video/audio transcript or subtitle export → `sources/transcripts/`
   - Project material → `sources/projects/` or `projects/<name>/sources/` if project exists
   - Image (png, jpg, svg, etc.) → `images/screenshots/`, `images/diagrams/`, or `images/photos/`
   - Reference/link/citation → `references/`
   - Entire subdirectory → keep structure, move to appropriate parent
   - Unknown → `sources/misc/`
3. Move file to destination
4. Ask user if destination is ambiguous
5. Offer to ingest the moved files
6. Log the sort action

User shortcut: "sort and ingest pending" does both in one pass.

---

## QUERY Operation

Triggered when user asks a question against the wiki.

### Step 1 — Search
- Read `index.md` to identify relevant pages
- If the question is project-specific, open `projects/<name>/README.md` before searching deeply
- For project-specific questions, prefer `projects/<name>/notes/` over raw project sources
- Grep wiki pages for key terms if index is insufficient
- Read relevant wiki pages (prefer wiki over raw sources — the wiki is the compiled knowledge)

### Step 2 — Synthesize Answer
- Answer the question using information from wiki pages
- Cite sources with `[[wikilinks]]` inline
- If wiki lacks information: say so explicitly, suggest what sources to add

### Step 3 — Choose Output Format

Match format to the question type:

| Question type | Suggested format |
|---------------|-----------------|
| Factual lookup | Direct answer with citations |
| Comparison | Markdown table |
| Explanation | Structured prose with headers |
| Overview/survey | Bullet summary with links |
| Timeline | Chronological list |

### Step 4 — File Back (optional)

Good answers can become wiki pages — ask the user:
- Analysis or comparison → `wiki/synthesis/` page
- New entity/concept discovered → `wiki/entities/` or `wiki/concepts/` page
- If user says "file it": create the page, update index, log as `QUERY → INGEST`

---

## PROJECT INIT Operation

Triggered when user starts a new project or asks to set one up.

1. **Create structure**:
   ```
   projects/<project-name>/
   ├── README.md        (from tpl-project template)
   ├── sources/         (project-specific raw sources)
   └── notes/           (working notes)
   ```
2. **Fill README.md**: use `tpl-project` template, fill in what's known
   - README must include a clear `Start Here` section
   - README must route by task type when possible (architecture, coding, eval, prompts, sources)
   - README must state the source-of-truth boundary if raw sources come from an external repo
3. **Update index.md**: add entry under `## Projects`
4. **Update briefing.md**: add to Active Projects list
5. **Update context/now.md**: add to Active Projects if it's a current priority
6. **Log**: `## [YYYY-MM-DD] PROJECT INIT | Project Name`

---

## ARCHIVE Operation

Triggered when a page, project, or source is no longer active.

1. Set `status: archived` in frontmatter
2. Set `updated` to today's date
3. In `index.md`: move entry to an `## Archived` section (create if needed)
4. In `briefing.md`: remove from Active Projects if it was listed
5. Do NOT delete the page — archived pages are kept for reference and link integrity
6. Log: `## [YYYY-MM-DD] ARCHIVE | Page/Project Name`

---

## LINT Operation

Health-check the wiki. Run periodically (suggest every ~20 ingests or on request).

### Step 1 — Structural Checks
- **Orphan pages**: zero incoming links → add links from related pages or flag
- **Dead links**: wikilinks to non-existent pages → create stubs or fix the link
- **Index drift**: pages on disk not in `index.md` → add them; stale index entries → remove
- **Filename violations**: uppercase, spaces, too long → flag (don't auto-rename, breaks links)
- **Missing frontmatter**: add required YAML fields
- **Missing TL;DR**: generate and add `> **TL;DR**:` line

### Step 2 — Content Quality
- **Stale stubs**: `status: stub` older than 30 days → flag for expansion or archival
- **Contradictions**: conflicting claims between pages → flag with both pages and the conflict
- **Superseded claims**: newer sources invalidate older wiki pages → update older pages
- **Thin pages**: `status: active` or `mature` with <100 words → expand or downgrade to stub

### Step 3 — Knowledge Gaps
- **Mentioned but missing**: entities/concepts mentioned across pages but lacking their own page → suggest creating them
- **Missing cross-references**: related pages not linked to each other → add links
- **Data gaps**: thin coverage on topics → suggest sources to find (web search, specific docs)
- **Suggested questions**: based on current wiki state, what should be investigated next?

### Step 4 — Tag Health
- **Tag typos/near-duplicates** → standardize to tag registry entries
- **Unused tags** (1 page only) → flag as possible typo
- **Missing tags** → add where clearly applicable

### Step 5 — Pending Check
- Files in `pending/` → flag and offer to sort

### Step 6 — Context Freshness
- `context/now.md` updated more than 7 days ago → flag
- `briefing.md` doesn't match active projects → update it
- `context/goals.md` older than 90 days → suggest review

### Step 7 — Report
Append to the current day file in `sources/log/days/`:
```markdown
## [YYYY-MM-DD] LINT

### Fixed (auto)
- [[page]] — what was fixed

### Fixed (flagged)
- [[page]] — what was fixed + #auto-fixed tag added

### Needs Attention
- issue — suggested action

### Knowledge Gaps
- topic — why it matters + suggested source/action

### Stats
- Total pages: N | Stubs: N | Orphans: N | Dead links: N
```

---

## Conversation-Triggered Context Update

Agents learn facts from two sources: ingested documents and live conversation. INGEST Step 6 covers documents. This rule covers conversation.

**Trigger:** User reveals any of the following in conversation (not from a source doc):
- Personal info (role, background, preferences, constraints)
- Project status change (shipped, blocked, pivoted, deadline moved)
- New priorities or goals

**Action:** Treat it as an implicit INGEST Step 6. Before the main task:
1. Update the relevant `context/` file (`me.md`, `now.md`, or `goals.md`)
2. Log as `## [YYYY-MM-DD] UPDATE | context` in the current day file under `sources/log/days/`
3. Then proceed with the task

**What NOT to update from conversation:** architectural decisions, code behavior, file paths, specific implementation details — verify those in the actual files first.

---

## Self-Healing Protocol

Every agent applies this to vault pages it edits or creates, plus read-only pages only when a visible structural defect or stale routing issue would affect the current task or the next session.
Batch fixes at the end of your task into a single log entry.
**Logging is mandatory for durable work. Evidence-only reads can be summarized in one batch log line instead of producing page-by-page repair work.**

### Evidence-Only Read Exception

If a vault page was read only to gather context or evidence for a repo/eval task, and the page already has the required routing shape or is a raw source/dev-log page, do not run a repair pass just because it was read.

Use this exception when all are true:
- The page was not edited or created in the current task.
- No missing frontmatter/TLDR, broken routing link, stale active-project state, or obvious contradiction would mislead the next agent.
- The task result does not require that page to become the canonical summary.

Allowed write-back under this exception:
- Add one day-log line such as `READ | evidence pages checked; no repair needed`.
- Update `context/hot.md` only as a compact delta when continuity or next action changed.
- Leave derived notes alone unless the stale derived note would misroute the next run.

Do not update `log.md` just because a same-day day-log entry was appended and the existing daily summary still remains accurate.

### Auto-Fix (no approval needed):
- Missing `updated` date → add today's date
- Missing `> TL;DR` line → generate from page content
- Page on disk missing from `index.md` → add entry + bump counts
- Tag typo matching tag registry → standardize
- Broken wikilink where target exists under a slightly different name → fix the link

### Flag + Fix (fix + add `#auto-fixed` tag + log):
- Outdated factual information agent knows is wrong → update
- Missing link between pages that clearly relate → add wikilink
- Stub fillable from information already in context → expand

### Flag Only (log to `sources/log/DATA_HOLES.md`, don't modify):
- Gap requiring a new source to fill
- Contradictions needing user judgment
- Probable duplicates the agent isn't sure about

### Logging Format
At the end of your task, append one block to the current day file in `sources/log/days/`:
```
## [YYYY-MM-DD] AUTO-FIX | <task description>
- **AUTO-FIX** [[page]] — what was fixed
- **FLAG** [[page]] — issue + suggested action
```

After updating the day file, check whether `log.md` needs a navigation sync:
- New day file? → insert a new line at the top of the entries block (newest-first)
- Summary changed? → edit the matching line in `log.md`
- Entry added, summary unchanged? → no `log.md` update needed

Line format: `- YYYY-MM-DD | {Summary} | [entry](./sources/log/days/YYYY-MM-DD.md)`

See `sources/log/HOW_TO_WRITE.md` for full rules.

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
| `index.md` | _(terminal)_ | Routing table — nothing reads index to update itself |
| `log.md` | _(terminal)_ | Navigation index — content lives in day files |
| `briefing.md` | _(terminal)_ | Entry point — nothing reads briefing to update itself |

### Pattern Rules

| File pattern | Must check | Why |
|-------------|-----------|-----|
| `projects/*/README.md` | `briefing.md`, `context/now.md` | Project status changes propagate to Active Projects lists |
| `projects/*/notes/*-hub.md` | `projects/*/README.md` (same project) | Hub routing changes may require README task-router update |
| `sources/log/days/YYYY-MM-DD.md` | `log.md` | Day file write requires navigation line sync in log.md |
| `projects/*/notes/docs-*.md` | `index.md` | Verify index entry exists and parent hub TL;DR is current |
| `wiki/**/*.md` | `index.md` | Verify index entry exists and is current |
| `references/*.md` | `index.md` | Verify index entry exists and is current |

### Adding a New Structural Node

When you add a new project README, hub, or vault-root operational doc:
1. Add an exact-path row to this matrix for the new file
2. Add `feeds_into:` to the new file's frontmatter (if it has frontmatter)
3. Add the inverse relationship — what feeds INTO the new file
4. Update `scripts/check_propagation.py` `EXACT_RULES` dict with the new entry

### Reference Documents
- Full implementation: `vault_propagation.md` (vault root)
- Hook script: `scripts/check_propagation.py`
- Hot cache: `context/hot.md`
