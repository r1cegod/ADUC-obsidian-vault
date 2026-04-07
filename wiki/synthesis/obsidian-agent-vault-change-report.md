---
type: synthesis
title: "Obsidian Agent Vault Change Report"
created: 2026-04-07
updated: 2026-04-07
tags: [obsidian, memory, report, synthesis]
status: active
lang: en
---

> **TL;DR**: This report covers the Obsidian/agent-memory ingest pass, the vault contract changes made around raw vs compiled knowledge, the new template pack, and the remaining gaps after the first implementation.

## Scope
This report covers the work triggered by the Obsidian/Claude Code source cluster and the follow-up requirement that future ingest should produce a human-readable topic digest, not only raw-source summaries.

## Contract Changes
- Added `sources/transcripts/` as a first-class raw lane for video/audio ingest.
- Formalized the human-vs-agent write boundary: human-primary raw notes stay in `journal/daily/` and similar lanes; durable synthesis belongs in `wiki/`, `projects/<name>/notes/`, `index.md`, and `log.md`.
- Formalized daily-note graduation so stable ideas get promoted out of chronology into reusable pages.
- Expanded ingest guidance to cover YouTube, GitHub, and Reddit sources.
- Clarified the writeback trigger: durable vault updates should happen before finishing a substantive response, not only at a special session-end event.
- Added the rule that multi-source topic ingest should create a human-readable digest the owner can read instead of rereading every source.

## Files Created
- Raw transcript sources under `sources/transcripts/` for the four YouTube videos.
- Reference anchors for the four videos plus Karpathy's gist, Cole's repo, and Greg's companion command page.
- Concept pages: `llm-wiki`, `agent-memory-compilation`, `human-agent-write-boundary`, `daily-note-graduation`.
- Source summaries for each ingested YouTube video.
- Topic digest: [[wiki/synthesis/obsidian-agent-vault-architecture]].
- Template pack:
  - `templates/tpl-youtube-reference.md`
  - `templates/tpl-youtube-source.md`
  - `templates/tpl-github-reference.md`
  - `templates/tpl-github-source.md`
  - `templates/tpl-reddit-reference.md`
  - `templates/tpl-reddit-source.md`
  - `templates/tpl-topic-digest.md`
  - `templates/tpl-change-report.md`

## Files Updated
- [[SCHEMA.md]]
- [[AGENTS.md]]
- [[CLAUDE.md]]
- [[README.md]]
- [[context/goals]]
- [[context/now]]
- [[templates/tpl-daily]]
- [[index.md]]
- [[log.md]]

## Ingest Output
- The current Obsidian/agent-memory topic can now be entered through [[wiki/synthesis/obsidian-agent-vault-architecture]].
- Each primary source has its own source-summary page for detail.
- The concepts extracted from the batch now exist as reusable pages instead of being buried inside one long synthesis note.
- The root router in [[index.md]] now exposes both the topic digest and the reusable concepts.

## Remaining Gaps
- GitHub and Reddit ingest rules are now documented, but they still need one real-world batch each to validate the heuristics.
- The response-completion writeback rule is documented, but it should be stress-tested on a few more real ingest passes.
- `README.md` still carries some mojibake in the ASCII tree block from earlier history; the content is correct, but the formatting could be normalized later.

## Related
- [[wiki/synthesis/obsidian-agent-vault-architecture]]
- [[wiki/concepts/llm-wiki]]
- [[SCHEMA.md]]
