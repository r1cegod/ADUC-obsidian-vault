---
type: note
title: Raven Tier 2 Source Packet Contract
created: '2026-05-02'
updated: '2026-05-02'
tags:
  - project/raven
  - workflow
  - docs
  - architecture
  - source-summary
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/sources/transcripts/README.md
  - projects/raven/notes/raven-codex-native-pivot.md
  - context/hot.md
---
> **TL;DR**: Raven Tier 2 should run as a three-node, file-first design: fetch full transcripts into the transcript source lane, summarize each source into run-scoped source cards, then synthesize those cards into one Wave Report.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-context-hub]] and [[projects/raven/sources/transcripts/README]]
- Node role: leaf
- First parent link: [[projects/raven/notes/raven-context-hub]]
- Growth trigger: split only when source-card schema, report schema, eval gates, or storage policy each need independent maintained contracts.
- Forbidden contents: long implementation logs, eval trace dumps, speculative UI/product wishlists, and full transcript text embedded inside compiled source cards or Wave Reports.
- Source/evidence boundary: this page defines the artifact contract; full transcripts live in the transcript source lane as raw evidence, while generated source cards and reports live in the summary source lane or repo packets.

## Official Tier 2 Shape

```text
Tier 1
  -> metadata ranker / trash filter
  -> selects candidates worth deeper read

Tier 2 Round 1
  -> fetch transcript/content for each kept candidate
  -> create one source card per source
  -> include enough evidence for Codex/Duc to judge without rereading everything

Tier 2 Round 2
  -> read the source cards as the evidence set
  -> generate one Wave Report / big synthesis report
  -> compare mechanisms, contradictions, patterns, and build implications
```

The source card is the unit of evidence. The Wave Report is the unit of synthesis.

## Three-Node Implementation Shape

Tier 2 can start as three nodes with no new DB work, as long as every artifact carries stable IDs.

```text
transcript_fetcher
  -> input: Tier 1 kept/maybe candidates
  -> fetch path: youtube-transcript-api for YouTube v1
  -> output: full transcript files under the run-scoped transcript source lane plus a transcript manifest
  -> owns: source_id, run_id, candidate_id, fetch status, transcript availability

summarizer
  -> input: transcript/content plus source metadata
  -> output: one raw source card / summary per source
  -> owns: mechanism extraction, evidence spans, failure modes, build implications

reporter
  -> input: source cards / summaries for a run/topic
  -> output: one Wave Report
  -> owns: cross-source synthesis, contradictions, signal vs noise, next action
```

This is deliberately file-first:

```text
no DB dependency for Tier 2 v1
  -> IDs in frontmatter and filenames
  -> folder structure carries run/day context
  -> Codex can inspect artifacts directly
  -> DB can be added later only if artifact lookup becomes painful
```

## Storage Rule

Raven may store full transcripts as raw source evidence, but compiled cards and reports must not become transcript dumps.

```text
full transcript
  -> durable raw evidence under the transcript source lane
  -> source for summarizer
  -> not copied wholesale into source cards or reports

source card
  -> durable compiled evidence object under the summary source lane
  -> compact enough for Codex to read many at once
  -> preserves provenance and audit hooks

Wave Report
  -> durable synthesis object under the summary source lane
  -> links to source cards and transcript paths
  -> does not inline full transcripts
```

Preferred run folder shape:

```text
projects/raven/sources/transcripts/<YYYY-MM-DD>_<run-id>/yt/
  transcript-manifest.md
  transcript_<source-id>_<slug>.md

projects/raven/sources/summaries/<YYYY-MM-DD>_<run-id>/yt/
  raw/
    source-card_<source-id>_<slug>.md
  wave-report_<topic-slug>_<run-id>.md
```

The transcript lane stores raw source evidence. The summary lane stores the Codex-readable operating artifacts.

## Round 1 File: Source Card

One file per source.

Suggested filename:

```text
projects/raven/sources/summaries/<YYYY-MM-DD>_<run-id>/yt/raw/source-card_<source-id-or-video-id>_<slug>.md
```

Minimum sections:

```text
# <Source Title>

## Source Metadata
- source_id:
- url:
- platform:
- author/channel:
- published_at:
- fetched_at:
- original_query:
- run_id:
- candidate_id:
- tier_1_label:
- tier_1_reason:
- transcript_path:
- transcript_status:

## One-Line Verdict
<keep / maybe / discard after transcript, with one hard reason>

## Compact Summary
<short factual summary of what the source actually says>

## Core Mechanism
<the main causal/workflow mechanism, not the topic label>

## Evidence Blocks
- timestamp/span:
  claim:
  evidence_summary:
  why_it_matters:

## Useful Claims
- claim:
  confidence:
  support:
  build_implication:

## Failure Modes / Warnings
- <what is vague, overclaimed, context-bound, outdated, or not actionable>

## Build Implications
- <what this changes about Raven, Duc OS, distribution, product, or a decision>

## Public Artifact Potential
- angle:
- proof needed:
- risk:

## Final Judgment
- transcript_rank: keep | maybe | discard
- confidence: high | medium | low
- next_action:
```

Hard rule: every source card must make a sharper judgment after transcript reading than Tier 1 could make from metadata.

## Round 2 File: Wave Report

One file per topic/run/report.

Suggested filename:

```text
projects/raven/sources/summaries/<YYYY-MM-DD>_<run-id>/yt/wave-report_<topic-slug>_<run-id-or-date>.md
```

The report should link to the `raw/source-card_*.md` files in its evidence set, not rely on tags alone. Tags classify; wikilinks connect.

Minimum sections:

```text
# Wave Report: <Topic>

## Question
<what wave/problem this report is reading>

## Evidence Set
- source_card:
  verdict:
  why_included:

## Executive Readout
<the answer Codex/Duc can act on immediately>

## Pattern Map
<recurring mechanisms across sources>

## Contradictions / Splits
<where sources disagree or talk past each other>

## Signal vs Noise
<what was actually useful versus discarded packaging>

## Build Implications
<what Duc should build/change/avoid within 7-14 days>

## Distribution Angles
<what can become public proof, post, thread, essay, demo, or room-entry artifact>

## Open Questions
<what Raven should fetch next>

## Next Action
<one concrete next move>
```

Round 2 should cite source cards, not raw transcripts. If it needs raw transcript access again, that means the source card was too weak.

## Eval Standard

Tier 2 is green only if:

```text
source card
  -> captures the real mechanism
  -> preserves provenance
  -> identifies at least one limitation or failure mode
  -> produces a build implication that could change a decision

wave report
  -> synthesizes across cards instead of concatenating summaries
  -> names contradictions and tradeoffs
  -> gives one actionable next move
  -> can be read by Codex without loading raw transcripts
```

## Anti-Traps

```text
summary trap
  -> card says what the video is about
  -> no mechanism, no decision impact

transcript hoard trap
  -> vault stores full third-party text
  -> signal buried under raw content

report mush trap
  -> round two repeats each source one by one
  -> no cross-source judgment

agent-OS relapse
  -> Tier 2 becomes autonomous research platform
  -> Raven expands beyond source/evidence prep
```

Counter-rule:

```text
Round 1 prepares evidence.
Round 2 reads the wave.
Codex/Duc decide what to build or publish.
```

## Related

- [[projects/raven/notes/raven-codex-native-pivot]]
- [[projects/raven/sources/transcripts/README]]
- [[projects/raven/sources/README]]
- [[projects/raven/notes/raven-current-context]]
- [[projects/raven/notes/raven-evaluation-hub]]
