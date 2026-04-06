# SCHEMA.md — Wiki Operations Manual

> Shared schema for all agents operating on this vault.
> CLAUDE.md and AGENTS.md are thin wrappers that reference this file.

---

## Vault Purpose

Personal master vault: second brain + project docs.
Owner reads it; agents read and write it; everything compounds over time.

---

## Tiered Loading Protocol

Load context in tiers. Read the minimum, then decide if you need more.

```
Tier 0: briefing.md        (~200 tokens)  — ALWAYS read first
         ↓ points to
Tier 1: index.md           (~500-1500 tokens) — read to find pages
        context/now.md     (~200 tokens) — read for current priorities
        SCHEMA.md          (this file) — read when doing wiki operations
         ↓ points to
Tier 2: wiki/, projects/   — read only what's relevant to the task
```

**Simple task** (write code, answer a question): read `briefing.md` → stop if enough context.
**Wiki operation** (ingest, query, lint): read `briefing.md` → `SCHEMA.md` → `index.md` → relevant pages.

---

## Directory Map

| Path | Contents | Notes |
|------|----------|-------|
| `briefing.md` | Vault orientation | Always read first. Keep under 500 tokens. |
| `index.md` | Content routing table | Updated after every ingest. |
| `log.md` | Activity + auto-fix log | Append-only. |
| `context/` | User profile + active state | The "brain" layer. |
| `pending/` | Drop zone for unsorted files | Agents sort and ingest. Check on every session. |
| `sources/` | Raw source documents | Global sources. Agents may annotate/organize. |
| `images/` | Image sources (screenshots, diagrams, photos) | Treated as sources — agents read and reference. |
| `references/` | Bookmarks, links, citations | External reference pages live here (not in wiki/). |
| `wiki/` | Agent-generated knowledge pages | Core knowledge base — entities, concepts, synthesis. |
| `projects/` | Project workspaces | Each project is self-contained with its own sources/notes. |
| `journal/daily/` | Daily notes | YYYY-MM-DD.md format. |
| `templates/` | Obsidian templates | User-managed. |
| `assets/` | Obsidian attachments | Auto-managed by Obsidian when pasting/embedding into notes. |

All directories are read/write for agents.

### Disambiguation

- **`images/` vs `assets/`**: `images/` holds curated source images the user or agent explicitly files (screenshots, diagrams, photos). `assets/` is Obsidian's automatic attachment folder — when you paste an image into a note in Obsidian, it lands here. Agents should file images in `images/`; leave `assets/` to Obsidian.
- **`sources/projects/` vs `projects/<name>/sources/`**: `sources/projects/` holds raw materials that don't belong to a specific project workspace yet. `projects/<name>/sources/` holds sources scoped to a specific project. When a project exists in `projects/`, its sources go there. When in doubt, put it in `projects/<name>/sources/`.
- **`references/`**: Holds reference pages (bookmarks, external links, bibliographies) — these are NOT wiki pages. They use the `tpl-reference` template and are indexed under `## References` in `index.md`.

### Project-Local vs Global Wiki Scope

When ingesting project sources, decide where wiki pages go:

| Criterion | Destination |
|-----------|-------------|
| Topic is project-specific (internal design decisions, project-only jargon, task notes) | `projects/<name>/notes/` |
| Topic is reusable knowledge (a tool, a concept, a person, a technique) | `wiki/` (global) |
| Unsure | Default to `wiki/` — knowledge is more valuable when discoverable globally |

Project README pages always live at `projects/<name>/README.md`.

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
type: entity | concept | synthesis | source-summary | project | reference | context
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
| Images (.png, .jpg, .svg) | View image, describe content, extract any text |
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
- If 5+ sources: create or update a synthesis page summarizing the batch

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
Append to `log.md`:
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

## Self-Healing Protocol

Every agent applies this whenever it reads vault pages — even for non-wiki tasks.
Batch fixes at the end of your task into a single log entry.

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

### Flag Only (log to `## Data Holes` in `log.md`, don't modify):
- Gap requiring a new source to fill
- Contradictions needing user judgment
- Probable duplicates the agent isn't sure about

### Logging Format
At the end of your task, append one block to `log.md`:
```
## [YYYY-MM-DD] AUTO-FIX | <task description>
- **AUTO-FIX** [[page]] — what was fixed
- **FLAG** [[page]] — issue + suggested action
```

---

## Scalability Rules

1. **Index splitting**: when any section exceeds 30 entries, split into domain sub-sections (e.g., `## Entities > AI`, `## Entities > Finance`)
2. **Synthesis hubs**: when 5+ pages share a theme, create a synthesis hub page that links to all of them. Index entry points to the hub.
3. **Tag registry**: at the bottom of `index.md`. Check before creating new tags. Add new tags to the registry when first used.
4. **Archival**: `status: stub` pages not updated in 60+ days → set `status: archived`, move to "Archived" section in index
5. **No deep nesting**: never add subdirectories beyond what's defined in this schema. Use tags and links instead.
6. **Index splitting at scale (300+ pages)**: split into `index-entities.md`, `index-concepts.md`, etc. Root `index.md` becomes meta-router.
