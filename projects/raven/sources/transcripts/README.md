---
type: note
title: Raven Transcript Sources
created: '2026-04-29'
updated: '2026-05-02'
tags:
  - project/raven
  - source-summary
  - youtube
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/sources/README.md
---
> **TL;DR**: Project-local raw evidence lane for Raven Tier 2 full transcripts and transcript manifests, keyed by run/date/platform and feeding the summary source lane.

## Growth Contract
- Parent branch: [[projects/raven/sources/README]]
- Node role: source lane
- First parent link: [[projects/raven/sources/README]]
- Growth trigger: split only when transcript-derived artifacts accumulate separate recurring child types such as source cards, final reports, or human audit packets.
- Forbidden contents: transcript-derived summaries, Wave Reports, unrelated eval traces, prompt contracts, current project status, and architecture decisions.
- Source/evidence boundary: store full transcript text as raw evidence with provenance, fetch status, and source IDs; compiled summaries and Wave Reports belong under [[projects/raven/sources/summaries/README]].

## Purpose

Raven Tier 2 needs source content, and this lane is allowed to store full transcript evidence. The official artifact contract is [[projects/raven/notes/raven-tier-2-source-packet-contract]].

```text
kept YouTube candidate
  -> transcript_fetcher: use youtube-transcript-api for YouTube v1
  -> write transcript-manifest.md plus transcript_<source-id>_<slug>.md files here
  -> summarizer: write one source card per source under [[projects/raven/sources/summaries/README]] run-scoped raw/
  -> reporter: synthesize source cards into one Wave Report under the same summary run folder
  -> Codex reads the source cards/report first, with transcript paths available for audit
```

This lane is the evidence layer between SQLite operational state and compiled Raven project meaning.

## Artifact Shape

Transcript run folders should contain:

```text
projects/raven/sources/transcripts/<YYYY-MM-DD>_<run-id>/yt/
  transcript-manifest.md
  transcript_<source-id>_<slug>.md
```

The manifest should list every requested source, transcript status, source path, and failure reason when unavailable.

Transcript files should carry source metadata before the transcript body:

```text
source_id
run_id
candidate_id
platform
url
video_id
fetched_at
language
transcript_status
source_policy
```

Source cards and Wave Reports belong under [[projects/raven/sources/summaries/README]], not here.

## Deep Research Steal

OpenAI and Anthropic deep-research patterns imply Tier 2 should behave like a bounded research agent, not a storage crawler:

```text
kept source
  -> clarify the output contract
  -> use read-only source access
  -> fetch only needed source content
  -> preserve citation/provenance blocks
  -> extract mechanism / failure / implication
  -> write reusable report/card
  -> expose source trail for audit
```

Implementation implications for Raven:

```text
search and fetch are separate interfaces
source cards store evidence pointers, not raw transcript dumps
tool/source budget is explicit per run
reports must preserve uncertainty and discard reasons
human audit edits become future eval cases
```


## Related

- [[projects/raven/sources/README]]
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-evaluation-hub]]
