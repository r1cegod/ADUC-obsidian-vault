---
type: note
title: Raven Tier 2 Execution Proposal
created: '2026-05-05'
updated: '2026-05-05'
tags:
  - project/raven
  - workflow
  - architecture
  - source-summary
  - youtube
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-tier-2-source-packet-contract.md
  - duc-os/kickstart.md
  - projects/raven/notes/raven-current-context.md
---
> **TL;DR**: Tier 2 should now move from contract to executable proposal through a small, auditable YouTube ingest spine: inventory candidates, fetch transcript segments, write file-first evidence, produce source cards, then synthesize one Wave Report. Daniel Priestley proved the workflow manually; Raven should productize that path without turning into a general research OS.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-context-hub]] and [[projects/raven/notes/raven-tier-2-source-packet-contract]]
- Node role: execution proposal leaf
- First parent link: [[projects/raven/notes/raven-context-hub]]
- Growth trigger: split only if transcript acquisition, source-card generation, Wave Report synthesis, or reliability/fallback policy each need independent maintained contracts.
- Forbidden contents: full transcripts, raw eval traces, repo implementation logs, speculative all-source platform plans, and unsupported claims from third-party sources.
- Source/evidence boundary: this page proposes execution; actual transcript/source-card artifacts live under Raven source lanes, while repo code and tests live in `/home/r1ceg/Raven`.

## Why This Is Ready

The Daniel Priestley ingest proved the human workflow:

```text
channel inventory
  -> long-form policy filter
  -> transcript fetch
  -> source card per video
  -> cross-video synthesis
```

Current evidence:

```text
402 uploads inventoried
378 shorts excluded by policy
24 long-form transcript attempts
23 transcripts fetched
23 source cards created
1 general synthesis created
0 Raven DB or repo-code dependency required
```

This means Tier 2 no longer needs an architecture debate. It needs a narrow implementation path that preserves the artifact discipline already proven manually.

## Proposed Execution Spine

Duc correction: Tier 2 should be two evidence-production nodes plus one graph-level synthesis reader.

```text
candidate set / explicit video list
  -> transcript_fetcher
      -> fetch timestamped transcript segments
      -> write transcript_<source-id>_<slug>.md
      -> write transcript-manifest.md
      -> preserve transcript_status and failure_reason
  -> card_maker
      -> read transcript + metadata
      -> write one source-card_<source-id>_<slug>.md
      -> use the Daniel Priestley source-card settings/sections as the card contract
  -> Raven graph: wave_reader
      -> read all cards for a run/topic
      -> preserve Obsidian file connections / wikilinks to cards and transcript paths
      -> write one wave-report_<topic>_<run-id>.md
```

`tier2_input_builder` is not a node. It is adapter glue: either explicit JSON/list input for early development or DB-run candidate selection later.

V1 should start with YouTube only. Reddit belongs later because Reddit ingestion needs different evidence units: thread, comment tree, score/context, deletion risk, and community-quality reading.

## Acquisition Strategy

Recommended V1 stack:

```text
default path: youtube-transcript-api
fallback path: yt-dlp subtitle extraction
last resort: watch skill / Whisper spot review for selected high-value failures
```

Reason:

- `youtube-transcript-api` is the simplest Python API for timestamped caption segments and already fits the current manual path.
- `yt-dlp` has mature subtitle options and should be treated as a fallback, not the first dependency Raven wraps around.
- `watch` is too heavy for mass ingest but excellent for visual evidence, transcript-missing spot checks, and high-value failures.
- Managed transcript APIs are valid later only if local reliability becomes the bottleneck; do not add paid infrastructure before V1 proves artifact value.

## External Scan

GitHub / package signal:

- `jdepoix/youtube-transcript-api`: Python library for retrieving subtitles/transcripts by video ID, including generated subtitles, no API key or headless browser required; supports listing transcripts and preserving segment timing.
- `yt-dlp/yt-dlp`: mature downloader with `--write-subs`, `--write-auto-subs`, `--list-subs`, subtitle language selection, and subtitle output handling.
- `yt-transcript-dl`: small `yt-dlp`-based package showing useful design ideas for Raven: JSON/SRT/VTT output formats, channel/playlist support, incremental sync, metadata, retry logic, and rate limiting.

Reddit field signal:

- Developers report the simple API wrapper is not the hard part; reliability is. Common failures: 429s, blocked VPS/cloud IPs, private/age-restricted/region-locked videos, missing captions, wrong-language captions, and low-quality auto captions.
- Timestamped segments repeatedly show up as unexpectedly valuable, because they let source cards point back to exact video moments.
- Several builders converge on a two-path reliability model: caption extraction first, then audio-to-text or managed APIs only for stubborn high-value failures.

## V1 Guardrails

```text
no DB schema work
no Reddit implementation
no automatic Duc OS adoption
no full transcript copied into cards or reports
no mass Whisper/audio path unless transcript failure blocks a must-click source
```

Artifact rules:

```text
full transcript -> raw transcript lane
source card -> compact evidence object
Wave Report -> cross-source synthesis from cards only
```

Reliability rules:

```text
store transcript_status for every candidate
store failure_reason when fetch fails
preserve segment timestamps
prefer manual captions over generated captions when available
mark generated captions as lower-confidence evidence
rate-limit batch fetches
make reruns idempotent by filename/source_id
```

## Build Ownership Boundary

Duc builds the working Raven code. Agent help in the development domain means:

```text
BUILD mode
  -> Duc writes the production seam
  -> agent audits shape, failure modes, tests, file artifacts, and docs
  -> agent may build observability, fixtures, reports, maintenance docs, and audit harnesses
  -> agent does not take over the core working code unless Duc explicitly delegates a bounded patch
```

This is the default Raven Tier 2 operating mode. It protects ownership while still letting Codex maintain the surrounding observation system.

## First Build Shape

Duc-owned production seams:

```text
src/backend/tier2/transcript_fetcher.py
src/backend/tier2/card_maker.py
src/backend/raven_graph.py  # wave_reader node wiring only when cards exist
```

Agent-owned support seams, unless Duc says otherwise:

```text
src/backend/test/test_transcript_fetcher.py
src/backend/test/test_card_maker.py
src/backend/test/test_wave_reader.py
fixture transcript/card artifacts
artifact-shape audit notes
vault docs and closeout logs
```

Minimum behavior:

```text
transcript_fetcher input: explicit YouTube video metadata or selected candidate records
transcript_fetcher output: transcript files + manifest
card_maker input: transcript files + source metadata
card_maker output: Daniel-Priestley-style source cards
wave_reader input: source-card folder / manifest
wave_reader output: one Obsidian-linked Wave Report
verification: fake transcript client, local fixture transcript, local fixture cards, no live YouTube dependency
```

## Discussion Prompt For Duc

Proposed route:

```text
1. Duc builds transcript_fetcher with injected transcript client and file writer.
2. Agent audits with fake-client tests and artifact-shape checks.
3. Duc builds card_maker using the Daniel Priestley card contract.
4. Agent audits card completeness against required sections and Obsidian links.
5. Duc wires wave_reader into Raven graph after cards exist.
6. Agent builds/maintains the report-readback and vault documentation around it.
```

Current recommendation: explicit JSON/list first, then DB-run candidates later. Explicit input is less magical, easier to audit, and keeps Tier 2 correctness separate from current DB/run state while the first two nodes are forming.

## Related

- [[projects/raven/notes/raven-tier-2-source-packet-contract]]
- [[projects/raven/notes/raven-distribution-system-ingest-structure]]
- [[sources/summary/daniel-priestley-youtube-2026-05-04/README]]
- [[wiki/synthesis/daniel-priestley-distribution-system]]
- [[duc-os/kickstart]]
