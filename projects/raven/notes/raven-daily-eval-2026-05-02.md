---
type: note
title: Raven Daily Eval 2026-05-02
created: '2026-05-02'
updated: '2026-05-02'
tags:
  - project/raven
  - evaluation
  - daily-eval
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-evaluation-hub.md
  - projects/raven/notes/raven-evaluation-insights.md
---
> **TL;DR**: Latest daily Phase 1 run on 2026-05-02 is run `12`: packet `eval/packets/02-May-2026/15:05:01_raven_full_how-to-grow-a-youtube-channel`, 4 queries, 13 candidates, Tier 1 skipped all 13, and the final-selector packet received 0 non-skip inputs. Per Duc correction, daily eval now stops here and waits for human audit before Phase 2.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-evaluation-hub]]
- Node role: report leaf
- First parent link: [[projects/raven/notes/raven-evaluation-hub]]
- Growth trigger: update only if this daily run receives Duc audit lines, creates focused dataset changes, or changes production-readiness judgment.
- Forbidden contents: raw trace dumps, full candidate JSON, runner code, and third-party content bodies.
- Source/evidence boundary: executable evidence remains in `/home/r1ceg/Raven/eval/packets/`; this note stores the human-readable judgment layer.

## Latest Phase 1 Run

```text
target: how to grow a youtube channel
kind: full graph
status: passed / needs review
run_id: 12
thread: d6e8b412-b1b6-4da4-af1f-44ae65946d8d
packet: eval/packets/02-May-2026/15:05:01_raven_full_how-to-grow-a-youtube-channel
started Vietnam: 15:04:41, 02 May 2026
finished Vietnam: 15:05:01, 02 May 2026
```

## Latest Result

```text
queries: 4
candidates: 13
YouTube filter: 400 raw hits -> 13 candidates, 387 filtered out
Tier 1 labels: skip 13
Final selector packet input count: 0
Console final counts: undecided 13
```

Enricher output:

```text
how to grow a youtube channel
grow a youtube channel fast
youtube channel growth strategy
youtube channel growth tips
key_words: grow, youtube, channel
```

Candidate distribution:

```text
how to grow a youtube channel -> 0 candidates
grow a youtube channel fast -> 7 candidates
youtube channel growth strategy -> 0 candidates
youtube channel growth tips -> 6 candidates
```

## Current Judgment

Do not treat this as a completed two-phase eval. This is the Phase 1 packet for Duc audit.

The packet shows a likely upstream source-discovery issue: broad growth/tips/fast queries produced a small candidate pool, and Tier 1 skipped all candidates. The final-selector markdown says input count `0`, so the high-model final judge did not receive a meaningful survivor set.

## Phase Boundary

```text
Phase 1: complete
Phase 2: blocked until Duc audit lines or explicit approval
```

Earlier run `11` did run focused checks, but that was the wrong automation boundary. The corrected rule is now: daily eval stops after Phase 1 full-graph packet generation, then waits for Duc audit before focused dataset/node eval.

## Packet Naming Change

New packet folders are date-grouped and time-prefixed for scanability:

```text
eval/packets/02-May-2026/15:05:01_raven_full_how-to-grow-a-youtube-channel
```

## Audit Pointers

Primary files for Duc audit:

```text
eval/packets/02-May-2026/15:05:01_raven_full_how-to-grow-a-youtube-channel/04_ranker_tier1.md
eval/packets/02-May-2026/15:05:01_raven_full_how-to-grow-a-youtube-channel/05_ranker_tier1_final.md
```

Fill Duc audit lines in the packet. If a skipped title should have survived, that becomes the approved Phase 2 focused eval input.

## Related

- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-tier-1-ranker-evaluation]]
