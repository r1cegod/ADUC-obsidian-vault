---
type: note
title: Duc OS Kickstart
created: '2026-04-29'
updated: '2026-05-12'
tags:
  - context
  - plan
  - workflow
status: active
lang: en
feeds_into:
  - duc-os.md
  - context/hot.md
---
> **TL;DR**: KICKSTART is the live top-level to-do list. Read-only repo inspection and essential non-mutating tooling like `rtk` orientation/search/status are allowed for planning; evals, edits, prompt patches, git mutation, and implementation require this page to be LOCKED for that lane.

## Growth Contract
- Parent branch: [[duc-os]]
- Node role: leaf
- First parent link: [[duc-os]]
- Growth trigger: update once per workday or when the active lane changes; split only if multiple days or projects start bloating this page.
- Forbidden contents: raw journaling, long project reports, eval traces, full roadmaps, and implementation logs.
- Source/evidence boundary: this page is today's checklist only; durable project detail belongs under project branches.

## Authority / Lock Rule

KICKSTART is the live top-level to-do list for the session. It decides the current lane, execution boundary, and forbidden lanes.

```text
read-only repo inspection and essential orientation tooling
  -> allowed when it improves planning, audit, or understanding
  -> examples: `rtk` read/search/status wrappers, file listing, file reads, static search
  -> do not mutate files, trigger evals, or run implementation/build/codegen workflows

repo eval, git mutation, prompt patch, code edit, implementation, or side-effectful command
  -> read [[duc-os/kickstart]]
  -> require Plan state: LOCKED for the exact lane
  -> execute only that locked lane
```

If KICKSTART is not LOCKED for the requested lane, agents may still inspect repo code and use essential non-mutating tooling such as `rtk` when useful. They must not patch prompts, run evals, edit files, perform git mutation, run side-effectful commands, or expand implementation.

KICKSTART must stay small enough to scan before every repo session. It is not a project report.

## Today

- Date: 2026-05-12
- Plan state: LOCKED / RAVEN RANKER TIER 2 SOURCE PACKET BUILD
- Main execution lane: start Raven Tier 2 now from the source-packet spine: kept/labeled source -> transcript_fetcher -> card_maker -> wave_reader / Wave Report.
- Repo execution gate: Raven Tier 2 implementation, fixtures, tests, observability, docs, and artifact-shape verification are allowed for this lane. Git mutation, Reddit implementation, DB schema work, broad agent-OS expansion, and unrelated Tier 1 rewrites remain blocked unless explicitly reopened.
- Architecture stance: Duc may freestyle the Tier 2 architecture while building. Agent default is BUILD/AUDIT support: provide raw mechanism blocks on request, audit outputs, name failure modes, and interrupt only for critical mistakes that threaten ownership, artifact integrity, provenance, verification, or the Codex-native Raven boundary.
- Vibe Docing lane: whenever Duc asks "how do I do X," default to a VIBE_DOCING-style raw lego block: operation, pattern, inputs, output, failure modes, and where it fits. Do not solve the whole Raven artifact unless Duc explicitly delegates or the task is a one-time utility.
- First live build target: a small, explicit-input YouTube Tier 2 path with fake-client/local-fixture verification before live transcript fetches.
- Hard stop: do not expand to Reddit, DB v1, UI, or a generalized research agent until one YouTube transcript -> source card -> Wave Report path is auditable.

## Locked-Plan Proposal Loop

When KICKSTART is LOCKED but the best execution path is not yet obvious, agents must propose before patching.

```text
locked plan
  -> restate objective and execution boundary
  -> inspect current project/vault evidence
  -> search GitHub for implementation patterns or repos by default
  -> search Reddit for field failures, edge cases, and practitioner pain by default
  -> propose one narrow route
  -> Duc audits
  -> only then execute the approved seam
```

Proposal default:

```text
agent proposes the way
Duc audits the way
repo mutation waits for audit unless the task is already one-time utility or explicitly delegated
```

The proposal should name the first file/module, input, output, failure modes, and verification path. If it cannot name those, the lane is still architecture discussion, not implementation.

## Checklist

| Item | Mode | Status | Done Signal |
|---|---|---|---|
| Raven Tier 2 execution proposal | PLAN | Done | [[projects/raven/notes/raven-tier-2-execution-proposal]] captures the Daniel Priestley proof, external GitHub/Reddit scan, corrected two-node evidence spine (`transcript_fetcher` + `card_maker`), graph-level `wave_reader`, guardrails, and Duc-owned build boundary |
| KICKSTART locked-plan proposal loop | EXECUTE | Done | Locked plans now require proposal -> Duc audit -> approved seam execution, with GitHub repo scan and Reddit field-insight scan as proposal defaults |
| Raven Tier 2 transcript_fetcher start | EXECUTE | Rolled back | Agent-created Tier 2 package/test/dependency removed at Duc's request; backend tests returned to 8/8; Tier 2 remains design-locked but repo-code-paused |
| Raven DB recreate + pytest install | EXECUTE | Done | Default `src/backend/data/raven.sqlite` recreated cleanly with patched run-local uniqueness and 0 runs; pytest installed and backend tests passed 8/8; live full-graph rerun blocked by YouTube API 403; [[projects/raven/notes/raven-daily-eval-2026-05-03]] updated |
| Root AGENTS minimal rule | EXECUTE | Done | `AGENTS.md` adds only the vault-before-finish rule |
| KICKSTART enforcement | EXECUTE | Done | KICKSTART owns repo execution lock rule inside vault only |
| Raven eval docs | EXECUTE | Done | Raven hub/domain/how-to name the two-phase eval loop and update priority |
| General eval domain | EXECUTE | Done | General reusable two-phase method added without Raven-specific state |
| Vault closeout | EXECUTE | Done | Self-healing readback plus `sources/log/days/2026-05-02.md` and `log.md` updated |
| Raven daily eval | EXECUTE | Done | Phase 1 run `12` generated packet `eval/packets/02-May-2026/15:05:01_raven_full_how-to-grow-a-youtube-channel`; Phase 2 is blocked until Duc audit or explicit approval; [[projects/raven/notes/raven-daily-eval-2026-05-02]] updated |
| Raven packet audit UX | EXECUTE | Done | Readout packet `13-20-49_02-May-2026_raven_run-readout_run-0010` is report-first with YouTube filter counts and Tier 1 preview/reasoning |
| Raven YouTube date filter | EXECUTE | Done | `search.list` now sends `publishedAfter` using the same recency window as post-filtering; focused URL-param unit test passed |
| Raven Tier 2 design lock | EXECUTE | Done | Full three-node file-first design is locked in KICKSTART and project docs: transcript_fetcher -> summarizer -> reporter; transcripts in source/transcripts; source cards and Wave Reports in source/summaries; no DB v1 |

## Tier 1 Locked Direction

Do not remove Tier 1 yet.

```text
Tier 1 should become recall gate / trash filter
  -> never lose candidates the final judge or human audit would keep
  -> reduce final-selector token load only after recall is proven
```

Compare two lanes before patching:

```text
A. high LLM final-only over all candidates
B. cheap Tier 1 gate -> high LLM final over survivors
```

Pass condition: `B` keeps every source `A` or human audit would keep while reducing final input tokens. If it drops a keep-worthy source, demote Tier 1 to deterministic trash filtering or remove it.

## Tier 2 Locked Direction

Tier 2 is now locked as a three-node, file-first source packet design.

```text
kept source
  -> transcript_fetcher
      -> use `youtube-transcript-api` for YouTube v1
      -> write full transcript evidence under `projects/raven/sources/transcripts/<YYYY-MM-DD>_<run-id>/yt/`
  -> summarizer
      -> write per-source cards under `projects/raven/sources/summaries/<YYYY-MM-DD>_<run-id>/yt/raw/`
  -> reporter
      -> write one Wave Report under `projects/raven/sources/summaries/<YYYY-MM-DD>_<run-id>/yt/`
```

No DB work for Tier 2 v1. Stable IDs must live in filenames and frontmatter/top metadata: `run_id`, `candidate_id`, `source_id`, `platform`, `url`, `video_id`, `fetched_at`, `transcript_path`, `transcript_status`, `tier_1_label`, and `tier_2_rank`.

Compiled source cards and Wave Reports should link to transcript paths but not inline full transcripts.

## Related

- [[duc-os]]
- [[duc-os/current]]
- [[duc-os/session-protocol]]
- [[projects/raven/notes/raven-current-context]]
- [[projects/raven/notes/raven-evaluation-hub]]
