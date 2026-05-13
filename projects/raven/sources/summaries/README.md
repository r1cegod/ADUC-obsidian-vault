---
type: note
title: Raven Source Summaries
created: '2026-05-02'
updated: '2026-05-02'
tags:
  - project/raven
  - source-summary
  - docs
  - workflow
status: active
lang: en
feeds_into:
  - projects/raven/sources/README.md
  - projects/raven/notes/raven-tier-2-source-packet-contract.md
---
> **TL;DR**: Project-local lane for Raven Tier 2 compiled source outputs: per-source cards under run-scoped `raw/` folders and one Wave Report per topic/run.

## Growth Contract
- Parent branch: [[projects/raven/sources/README]]
- Node role: source lane
- First parent link: [[projects/raven/sources/README]]
- Growth trigger: split only when source cards, Wave Reports, human audit packets, or public artifact drafts become large enough to need separate child lanes.
- Forbidden contents: full raw transcripts, executable eval traces, prompt contracts, repo implementation logs, and current project status.
- Source/evidence boundary: this lane stores compiled summaries and reports derived from raw source material; full transcript evidence belongs under [[projects/raven/sources/transcripts/README]].

## Purpose

This lane stores what Codex should actually read after Raven fetches source material.

```text
full transcript evidence
  -> [[projects/raven/sources/transcripts/README]]

per-source summary / source card
  -> this lane, run-scoped raw/ folder

cross-source Wave Report
  -> this lane, same run/topic folder
```

## Run Folder Shape

```text
projects/raven/sources/summaries/<YYYY-MM-DD>_<run-id>/yt/
  raw/
    source-card_<source-id>_<slug>.md
    source-card_<source-id>_<slug>.md
  wave-report_<topic-slug>_<run-id>.md
```

Round 1 writes the `raw/source-card_*.md` files.
Round 2 writes the `wave-report_*.md` file and links to the source cards in its evidence set.

## Required IDs

Every source card and report should carry IDs in frontmatter or top metadata:

```text
run_id
candidate_id
source_id
platform
url
video_id when platform is YouTube
fetched_at
transcript_path
transcript_status
tier_1_label
tier_2_rank
```

## Related

- [[projects/raven/sources/README]]
- [[projects/raven/sources/transcripts/README]]
- [[projects/raven/notes/raven-tier-2-source-packet-contract]]
- [[projects/raven/notes/raven-codex-native-pivot]]
