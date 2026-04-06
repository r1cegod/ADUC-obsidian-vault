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
| `pending/` | Drop zone for unsorted files | Agents sort and ingest. |
| `sources/` | Raw source documents | Agents may annotate/organize. |
| `images/` | Image sources | Treated as sources — agents read and reference. |
| `references/` | Bookmarks, links, citations | External reference store. |
| `wiki/` | Agent-generated knowledge pages | Core knowledge base. |
| `projects/` | Project workspaces | Each project is self-contained. |
| `journal/daily/` | Daily notes | YYYY-MM-DD.md format. |
| `templates/` | Obsidian templates | User-managed. |
| `assets/` | Images, attachments | Obsidian attachment folder. |

All directories are read/write for agents.

---

## Page Conventions

### Filenames
- Lowercase, hyphens for spaces: `machine-learning.md`, `john-smith.md`
- Always romanized (even for Vietnamese content): `tri-tue-nhan-tao.md`
- No dates in filenames (dates live in frontmatter)
- Max 60 characters

### Frontmatter (required on every wiki page)

```yaml
---
type: entity | concept | synthesis | source-summary | project | context
title: "Human-readable title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
status: stub | active | mature | archived
lang: en | vi
source: "[[sources/path]]"     # source-summary pages only
aliases: ["alternate name"]    # optional
---
```

**Status meanings:**
- `stub` — placeholder, minimal content, needs expansion
- `active` — being actively worked on or recently updated
- `mature` — comprehensive, stable
- `archived` — outdated or superseded, kept for reference

### Page Structure

Every wiki page must have, in order:
1. Frontmatter (YAML)
2. `> **TL;DR**: One-sentence summary.` — mandatory, enables tiered loading
3. Content sections (vary by type, see templates)
4. `## Related` section at bottom with `[[wikilinks]]` to related pages

**Page size targets:**
- Source summaries: 200-500 words
- Entity/concept pages: 100-400 words
- Synthesis pages: up to 1000 words

### Wikilinks
- Always use Obsidian `[[wikilinks]]`, never markdown `[text](url)` for internal links
- Use display text when helpful: `[[machine-learning|ML]]`
- Every page should have at least 2 outgoing links
- Link to wiki pages from wiki pages; link to sources only from the `source:` frontmatter field

### Language
- Structural files (SCHEMA.md, CLAUDE.md, AGENTS.md, index.md, log.md, briefing.md): English
- Wiki page content: matches source language (EN or VI)
- Frontmatter keys: always English
- Filenames: always romanized (no Vietnamese characters in filenames)

---

## INGEST Operation

Primary operation. Triggered when user asks to process source(s).

### Step 1 — Read & Analyze Source
- Read the source fully
- Identify: main topic, entities mentioned, concepts introduced, claims made
- Determine content language → sets `lang` field on all generated pages
- If source has images: read text first, then view key images for additional context

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
- Format: `- [[path|Display Name]] — TL;DR one-liner (tags)`
- Bump page/source counts in index header

### Step 6 — Update Context (if relevant)
- Source relates to active project → update `context/now.md` if priorities shifted
- Source reveals user info → update `context/me.md`
- Source affects direction → update `context/goals.md`
- `briefing.md` if active projects or focus changed

### Step 7 — Log
```
## [YYYY-MM-DD] INGEST | Source Title
- Source: [[sources/path/file]]
- Created: [[wiki/path/primary-page]] + N stubs
- Updated: [[page1]], [[page2]]
- Tags: #tag1, #tag2
```

### Batch Ingest
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

1. Scan `pending/` for files
2. Determine destination for each:
   - Markdown article/note → `sources/articles/`
   - PDF/technical doc → `sources/docs/`
   - Project material → `sources/projects/` or `projects/<name>/sources/`
   - Image (png, jpg, svg, etc.) → `images/screenshots/`, `images/diagrams/`, or `images/photos/`
   - Reference/link/citation → `references/`
   - Unknown → `sources/misc/`
3. Move file to destination
4. Ask user if destination is ambiguous
5. Offer to ingest the moved files
6. Log the sort action

User shortcut: "sort and ingest pending" does both in one pass.

---

## QUERY Operation

1. Read `index.md` to identify relevant pages
2. Read relevant wiki pages (not raw sources unless wiki is insufficient)
3. Synthesize answer with wikilink citations
4. If wiki lacks information: say so explicitly, suggest what sources to add
5. Optionally file the answer as a synthesis page (ask user first)

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

### Auto-Fix (no approval needed):
- Missing `updated` date → add today's date
- Missing `> TL;DR` line → generate from page content
- Page on disk missing from `index.md` → add entry
- Tag typo matching tag registry → standardize

### Flag + Fix (fix + add `#auto-fixed` tag + log):
- Outdated factual information agent knows is wrong → update
- Missing link between pages that clearly relate → add wikilink
- Stub fillable from information already in context → expand

### Flag Only (log to `## Data Holes` in `log.md`, don't modify):
- Gap requiring a new source to fill
- Contradictions needing user judgment
- Probable duplicates the agent isn't sure about

---

## Scalability Rules

1. **Index splitting**: when any section exceeds 30 entries, split into domain sub-sections (e.g., `## Entities > AI`, `## Entities > Finance`)
2. **Synthesis hubs**: when 5+ pages share a theme, create a synthesis hub page that links to all of them. Index entry points to the hub.
3. **Tag registry**: at the bottom of `index.md`. Check before creating new tags.
4. **Archival**: `status: stub` pages not updated in 60+ days → set `status: archived`, move to "Archived" section in index
5. **No deep nesting**: never add subdirectories beyond what's defined in this schema. Use tags and links instead.
6. **Index splitting at scale (300+ pages)**: split into `index-entities.md`, `index-concepts.md`, etc. Root `index.md` becomes meta-router.
