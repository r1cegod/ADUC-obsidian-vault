---
type: learning-session
title: Raven API + SQLite Ingest Wire - Learning Session
created: '2026-04-16'
updated: '2026-04-20'
tags:
  - learning-session
  - project/raven
  - api
  - sqlite
  - ingest
status: active
lang: en
feeds_into:
  - learning/README.md
  - projects/raven/README.md
---
> **TL;DR**: Learning session for owning Raven's first API + SQLite ingest wire: get Reddit/YouTube access, learn SQLite as the workbench, plan schema, use APIs, then connect metadata search -> persistence -> normalized candidates.

## Protocol Route

- Hub: [[wiki/learning-protocol-hub]]
- Help gate: [[wiki/help-protocol]]
- Feature protocol: [[wiki/pre-wire-protocol]]
- Raven overlay: [[projects/raven/notes/raven-ownership-delegation-protocol]]

## Scope

```text
Reddit/YouTube API access
  -> SQLite crash course
  -> SQLite planning
  -> API usage mechanism
  -> first Raven metadata search + persistence wire
```

## Verified Reference Paths

- YouTube: Data API v3 getting started, `search.list`, `videos.list`, quota usage.
- Reddit: Developer Platform/Data API usage, Data API wiki, live API `/search`, OAuth2 technical guidance, Responsible Builder Policy.

## Blueprint (user-written)

> Write how this feature works and how you think it should be implemented.
> No help from agent at this stage.
> End with `READY FOR AUDIT` when complete.

```text
Task: Make the first half of Raven, the enricher, search, and SQLite database for strictly agent work
What the feature does: enrich user's query -> search on yt and reddit (get title, description, link) -> store them in database
Files/modules involved: Backend, backend/prompt
Inputs: user query in normal english
Outputs: write the search result in database
Failure modes: timeouts, 404, requesting too fast, dumb enricher, not-my-database
Verification: contract, checks
What I do not understand yet: How to write code to kinda check if anything is wrong like all them senior, apis, SQLite

READY FOR AUDIT
```

---

## Audit Result

- [ ] OWNABLE - review/delegation may be allowed
- [x] MECHANISM_GAP - run artifact challenges
- [x] SYSTEM_GAP - revise blueprint first
- [ ] ONE_TIME_UTILITY - agent may execute lightly

**Notes:**
Blueprint has the right product direction but is not implementation-ownable yet. Missing wires: exact backend module ownership, normalized candidate contract, SQLite table boundary, API credential/error boundary, and verification shape. Mechanism gaps: API auth/request handling, SQLite schema/transactions, and senior-style checks/contracts.

Second blueprint exposed the main structural gap: user is mixing platform/source, author/channel/subreddit, candidate row, API raw payload, and SQLite table into one blob. Next challenge should force data-shape ownership before API code.

---

## Technical Gap Inventory

> Ordered by dependency, not convenience. Initial expected gap order, to be audited after the blueprint.

| # | Gap description | Depends on | Status |
|---|-----------------|------------|--------|
| 1 | API credential/access model for YouTube and Reddit | none | pending |
| 2 | SQLite table/query/transaction basics | none | pending |
| 3 | Raven SQLite schema for runs, candidates, and raw metadata pointers | 2 | pending |
| 4 | API request/response normalization into one candidate shape | 1, 3 | pending |
| 5 | End-to-end fake -> real API -> SQLite verification loop | 1, 2, 3, 4 | pending |

---

## Builder-First Learning Method

This session switched away from passive sandbox tracing. Duc builds Raven's database progressively from the smallest real database upward. The agent acts as mentor/reviewer, not builder.

```text
Duc proposes/implements smallest artifact
  -> agent audits
  -> if direction gap: ask a narrower challenge
  -> if knowledge gap: label "I will do this" and provide reference + official docs
  -> Duc repairs/builds next artifact
  -> only then reveal contrast/reference code
```

### Challenge Format

Each artifact challenge must include:

```text
1. Mission
2. Constraints
3. What Duc must build
4. Allowed docs/reference targets
5. What counts as pass/fail
6. Edge cases the agent may handle as "I will do this" if they require unknown mechanism knowledge
7. Contrast reference after Duc attempts
8. Lock-in rule Duc writes in his own words
```

### Mentor Rules

- Do not make Duc trace unexplained agent code as the main teaching path.
- Do not spoonfeed product implementation before Duc attempts the artifact.
- Use reference code only after attempt, or for explicitly labeled knowledge gaps.
- When the blocker is missing knowledge, say: `I will do this reference piece because the missing mechanism is X`.
- When the blocker is direction/architecture, do not give code; narrow the task.
- Prefer real Raven artifacts over toy-only demos once the smallest database concept is understood.

### Vibe Docing Rule

Canonical operation: [[wiki/vibe-docing]].

In this session, vibe docing means official-doc-shaped mechanism help using neutral placeholder values, not Raven's exact challenge answers.

## SQL-From-Zero Build Strategy

The database learning path must treat SQL as a tool for expressing Raven ownership, not as a separate school subject.

```text
see a Raven storage need
  -> build the smallest table that satisfies it
  -> run it against a real `.sqlite` file
  -> inspect actual rows
  -> add exactly one new SQL concept
  -> break it deliberately
  -> write the rule in Duc's words
```

Teaching rules:

- Start from real Raven database artifacts, not generic SQL drills.
- Future Raven database artifacts live under `src/backend/`; no more new scratch-folder learning artifacts for this track.
- Each artifact is one maturity level, not one isolated feature: naive usable DB -> proper shape -> integrity -> backend API -> adapter-ready -> production-ish.
- One new SQLite concept per maturity level: table, insert, select, relationship, constraint, migration, transaction.
- Use [[wiki/vibe-docing]] only when the missing thing is a mechanism operation, with neutral placeholders and no Raven-specific answer.
- Agent audits the artifact after Duc attempts; no silent patching.
- If a concept is senior-level edge handling, label it `I will do this reference piece because...`, show the mechanism, then return ownership to Duc.
- Every pass condition must be executable or inspectable: file exists, row prints, wrong insert fails, selected output matches expected shape.

Database concepts should arrive in this order:

```text
1. Connection + file path
2. CREATE TABLE
3. INSERT + placeholders
4. SELECT + fetch rows
5. Multiple rows and repeated script behavior
6. Foreign key relationship
7. UNIQUE constraint / dedupe
8. NULL vs NOT NULL
9. Transactions / commit / rollback
10. Schema migration only when the shape changes under existing data
```

### Normal vs Adaptive Cases

Normal cases are required database literacy. Build them before API/product pressure because they teach the mechanisms needed to solve future edge cases.

Adaptive cases require another function, adapter, or API to interact with the database. Do not prebuild them. Add them only when a real caller creates pressure.

```text
Normal cases
  -> needed for ownership now
  -> teach core SQLite/data-model mechanisms
  -> build before APIs

Adaptive cases
  -> depend on API/query/rater behavior
  -> add only when real caller needs them
  -> avoid premature schema complexity
```

Normal case list for Raven DB:

```text
- N0: runnable schema initialization
- create/open database file
- create tables idempotently
- insert rows with placeholders
- return inserted ids
- select and return rows
- parent/child relationship with foreign keys
- duplicate protection for platform identity
- basic NULL vs NOT NULL choice
- readable joined output for run -> queries -> candidates

Joined readback status 2026-04-18: passed. `list_joined_candidates(run_id)` now accepts the current run id, returns the current run's joined candidates, and orders by `raven_queries.query_index, raven_candidates.id`. Normal Raven DB cases are complete enough to move into backend module cleanup.
```

Current N0 blockers from `src/backend/db_l0.py` audit on 2026-04-18:

```text
- invalid ZoneInfo key blocks script before SQLite
- multi-table schema should use sqlite3 executescript or separate execute calls
- foreign-key references use old table names instead of current raven_* table names
- raven_queries and raven_candidates need IF NOT EXISTS while the script is rerunnable
- PRAGMA foreign_keys = ON is needed before testing relationship failures
- list_all_runs returns only first row because return is inside the loop
```

N0 status: passed 2026-04-18. Script now uses valid timezone key, `executescript`, actual `raven_*` table references, `IF NOT EXISTS`, and `list_all_runs` returns rows. Next normal case: `create_query` parent-child insertion.

Adaptive case list for Raven DB:

```text
- API timeout/error recording shape
- missing platform fields normalization
- retry attempt tracking
- raw_response size/storage decisions
- schema migrations under existing data
- transaction bundling across multi-step ingest
- rater/audit tables
- conflict resolution when the same candidate appears from different queries
```

Rule: finish normal cases through candidate storage before YouTube/Reddit. Add adaptive cases only when the API adapter or rater actually needs them.

## Narrowed Ladder To Raven Phase 1

```text
DB1: Simplest real SQLite database
  Duc builds a tiny Raven database file with one table and one insert/select.
  Exit: can create a `.sqlite` file, create a table, insert one row, and read it back.
  Status: passed 2026-04-18 with `src/backend/db_l0.py` and `src/backend/raven.sqlite`; script creates `raven_runs`, inserts neutral placeholder row, commits, selects, and prints rows. Re-running creates repeated rows, which becomes the next maturity level.

DB2: Raven run table
  Duc builds `search_runs` only.
  Exit: one target can be stored and selected back.
  Status: partial pass 2026-04-18 with `src/backend/db_l0.py`; `create_run(target)` inserts with real UTC timestamp and prints last inserted id, and `list_all_runs()` selects rows. Remaining maturity corrections before DB3: `create_run` should return the id, and list function should return rows instead of only printing.

DB3: Run -> query relationship
  Duc adds `search_queries` with `run_id`.
  Exit: one run owns YouTube/Reddit query rows.
  Status: passed 2026-04-18 in `src/backend/db_l0.py`; verified run id 23 owns two query rows for YouTube/Reddit. Cleanup later: `create_query` should return id, list query SQL should filter with WHERE instead of Python filtering, and source casing should normalize to lowercase.

DB4: Query -> candidate relationship
  Duc adds `source_candidates`.
  Exit: one query owns one normalized candidate.
  Status: passed 2026-04-18 in `src/backend/db_l0.py`; verified run id 34 owns two query rows and two candidate rows, with candidates pointing to query ids 35 and 36. Fake platform/link values now use run id to avoid accidental UNIQUE collisions during repeated runs.

DB5: Constraints
  Duc adds foreign keys and duplicate protection.
  Exit: fake `query_id` and duplicate `(source, platform_id)` fail.
  Status: passed 2026-04-18 in `src/backend/db_l0.py`; verified normal run/query/candidate insertion passes, fake `query_id` fails with `FOREIGN KEY constraint failed`, and duplicate `(source, platform_id)` fails with `UNIQUE constraint failed: raven_candidates.source, raven_candidates.platform_id`.

YT1: YouTube response shape
  Duc studies one official response and maps it to `source_candidates`.
  Exit: can name `videoId`, `title`, `description`, `channelTitle`, `publishedAt`, and link construction.
  Status: passed 2026-04-19. Active `src/backend/search/youtube_search.py` calls YouTube `search.list`, captures raw response/status, and returns normalized candidate dicts. Verified with repo `.venv` using a neutral live smoke call returning HTTP 200 plus one candidate.

YT2: One real YouTube search into DB
  Duc wires one `search.list` result into the existing DB shape.
  Exit: one real YouTube candidate is stored.
  Status: next. Commit one YouTube result into SQLite: create run/query log, insert candidate rows, then read back joined rows.

RD1: Reddit response shape
  Duc studies one official/listing response and maps it to `source_candidates`.
  Exit: can name post id, title, selftext/preview, permalink/link, subreddit/author, score, created time.
  Status 2026-04-20: STEAL reference artifact created at local repo path `docs/reference/reddit_search_clean.py`. It compiles and fake-listing normalization passes. Live Reddit smoke is blocked by missing local Reddit credentials, so active `src/backend/search/reddit_search.py` is still not production-complete.

RD2: One real Reddit search into DB
  Duc wires one Reddit result into the same DB shape.
  Exit: one real Reddit candidate is stored.

E2E1: One actual Raven search
  Duc runs one target through YouTube + Reddit and stores results.
  Exit: database contains one run, platform query rows, and normalized candidates from both platforms.
```

Rule: Raven Phase 1 implementation starts after DB5. Real API wiring begins platform-by-platform after YT1/RD1 response-shape gates.

Backend module cleanup status 2026-04-18: `src/backend/db.py` compiles, imports safely after removing bad editor-inserted `dbm.sqlite3` import, and supports a minimal callable flow: connect -> create_schema -> create_run -> create_query -> create_candidate -> list_run_candidates. Workspace Python auto-import completions/add-missing-imports were disabled to prevent bogus imports.

YouTube search status 2026-04-19: active `src/backend/search/youtube_search.py` now owns YouTube API call + platform-specific normalization only. It does not commit to SQLite. Verified through `.venv/bin/python`; system Python is not the right interpreter for this repo because dependencies live in `.venv`.

Repo hygiene note 2026-04-19: a root `test/` folder currently exists, but Raven rules require backend tests under backend test folders. Treat root tests as cleanup debt, not accepted structure.

## Artifact Challenges

### Gap 1: SQLite Workbench Data Shape

**System view:**
```text
user target
  -> search_run
  -> enriched search_queries
  -> normalized source_candidates
  -> raw API JSON attached for audit/debugging
```

**Problem statement:** Raven needs to store normalized candidates, not vague API result blobs. The learner must distinguish table, row, column, relationship, and raw metadata.

**User attempt:**
```text
Table: search_runs
Purpose: store a Raven run
One row means: one run
Columns:
- id: number label
- target: query
- created_at: date

Table: search_queries
Purpose: store one query Raven searched
One row means: one query log
Columns:
- id: number label
- run_id: run id
- query: enriched query
- query_index: original query ?

Table: source_candidates
Purpose: store one result
One row means:
Columns:
- id: number label
- run_id: run id
- query_id: query id
- source: reddit or youtube
- platform_id: video id or post id
- title: title
- description: des or reddit preview
- link: url
- author_or_channel: reddit author or yt channel
- published_at: date yt
- source_metric: yt views, reddit comments
- raw_metadata: original result
- created_at: date reddit

Relationships:
runs owns queries owns candidates

Rule I learned: right data base stores normalized candidates with raw result only for debug
```

**Audit:** pass with corrections needed. User now owns the core table nouns. Corrections: `query_index` is the order of the generated query, not original query; `source_metric` should be a comparable loose metric field, not necessarily semantically identical; `created_at` means when Raven stored the row, not Reddit date; `published_at` should work for both YouTube and Reddit when available; one row in `source_candidates` means one normalized candidate.

**Status:** [x] pass [ ] fail

### Gap 2: SQLite Schema Skeleton

**System view:**
```text
search_runs
  -> search_queries
  -> source_candidates
```

**Problem statement:** Convert the owned Raven workbench nouns into pseudo-SQL with primary keys, foreign keys, required fields, and duplicate protection.

**User attempt:**
```sql
CREATE TABLE search_runs (
  id  INTERGER PRIMARY KEY NOT NULL,
  created_at TEXT NOT NULL,

);

CREATE TABLE search_queries (
  id  INTERGER PRIMARY KEY NOT NULL,
  run_id INTERGER FOREIGN KEY NOT NULL,
  created_at TEXT NOT NULL,
  source TEXT NOT NULL,
  raw_metadata TEXT NOT NULL,
  query TEXT NOT NULL,
);

CREATE TABLE source_candidates (
  id  INTERGER PRIMARY KEY NOT NULL,
  run_id INTERGER FOREIGN KEY NOT NULL,
  query_id INTERGER FOREIGN KEY NOT NULL,
  created_at TEXT NOT NULL,
  source TEXT NOT NULL,
  platform_id INTERGER NOT NULL,
  query TEXT FOREIGN KEY NOT NULL,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  link TEXT NOT NULL UNIQUE,
  author_or_channel TEXT NOT NULL,
  published_at TEXT NOT NULL,
  source_metric TEXT NOT NULL,
);
```

**Audit:** fail but structurally useful. User has table separation and key intent, but syntax and responsibility are not ownable yet. Error classes: `INTEGER` typo; trailing commas before `)`; foreign keys need `REFERENCES table(column)`; `search_runs` is missing `target`; `search_queries` should not own source/raw metadata; candidate `platform_id` must be `TEXT`; `query TEXT FOREIGN KEY` is wrong because candidate already points through `query_id`; raw metadata belongs on `source_candidates`; duplicate protection should be `(source, platform_id)` rather than link-only.

**Status:** [ ] pass [x] fail

**User attempt 2:**
```sql
CREATE TABLE search_runs (
  id  INTEGER PRIMARY KEY NOT NULL,
  created_at TEXT NOT NULL,
  target TEXT NOT NULL
);

CREATE TABLE search_queries (
  id  INTEGER PRIMARY KEY NOT NULL,
  run_id INTEGER NOT NULL REFERENCES search_runs(id),
  created_at TEXT NOT NULL,
  raw_metadata TEXT NOT NULL,
  query TEXT NOT NULL,
  query_index INTEGER PRIMARY KEY NOT NULL
);

CREATE TABLE source_candidates (
  id  INTEGER PRIMARY KEY NOT NULL,
  run_id INTEGER NOT NULL REFERENCES search_runs(id),
  query_id INTEGER NOT NULL REFERENCES search_queries(id),
  created_at TEXT NOT NULL,
  source TEXT NOT NULL,
  platform_id TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  link TEXT NOT NULL UNIQUE,
  author_or_channel TEXT NOT NULL,
  published_at TEXT NOT NULL,
  source_metric TEXT NOT NULL,
  UNIQUE(source, platform_id)
);
```

**Audit 2:** closer. `search_runs` passes. Remaining issues: `search_queries` has two primary keys because `query_index` cannot also be primary key; query-level `raw_metadata` is only valid if it means full API response, but then it needs `source` and probably belongs in a separate `api_responses` table; `source_candidates.platform_id UNIQUE` conflicts with `UNIQUE(source, platform_id)` and should not be standalone unique; `link UNIQUE` is optional but weaker than source/platform identity. User correctly pushed back that full raw API response belongs to the query/API-call layer, while candidate raw item metadata would require slicing per item.

**User attempt 3 / objection:**
User proposed keeping `source` on `search_queries` because YouTube and Reddit queries are unique to each other after enrichment, then connecting candidates to platform-specific query rows instead of introducing a separate `api_responses` table.

**Audit 3:** objection accepted with condition. If `search_queries` means one platform-specific search call, `source` and raw response can belong there. The table should then be understood as `search_tasks` or platform-scoped `search_queries`, not abstract query text. Remaining issues: `source_candidates.source TEXT REFERENCES search_queries(source)` is wrong; candidate ownership is already through `query_id`, and `source` is either denormalized for easy uniqueness or omitted. Foreign-keying to `source` is semantically weak and SQLite requires referenced columns to be primary/unique. `raw_metadata` should be renamed mentally to `raw_response`; failed API calls need status/error fields or nullable raw response. `source_candidates.link UNIQUE` is optional; `(source, platform_id)` remains the real identity.

**User attempt 4:**
User fixed `raw_response`, `status_code`, removed the bad `source` foreign key on candidates, and kept `(source, platform_id)` as the dedupe lock.

**Audit 4:** pass for Phase 1 architecture. Caveats: `id INTEGER PRIMARY KEY` already implies non-null in SQLite; `description`, `published_at`, and `source_metric` may be missing from real APIs, so implementation must either normalize missing values or allow nulls. Next gap is fake SQLite insertion contract before real API calls.

**Status:** [x] pass [ ] fail

## Final Blueprint (user rewrites)

Pending.

## Build Log

[ ] Built by user without agent writing product code

Notes:
Pending.

## Debugging Ladder Used

- [ ] expected behavior stated
- [ ] actual behavior stated
- [ ] data path traced
- [ ] failing seam identified
- [ ] error class explained
- [ ] next inspection target chosen

---

## Retrospective

**What worked:**

**What felt wrong:**

**Breakpoints that fired (B1/B2/B3):**

**Rules derived:**

**Protocol changes to consider:**

---

## Related

- [[wiki/learning-protocol-hub]]
- [[wiki/help-protocol]]
- [[wiki/pre-wire-protocol]]
- [[learning/README]]
- [[projects/raven/README]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
