---
type: note
title: Raven Evaluation Workflow
created: '2026-04-22'
updated: '2026-04-22'
tags:
  - project/raven
  - evaluation
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-evaluation-domain.md
  - projects/raven/README.md
---
> **TL;DR**: This is the official how-to for Raven evaluation work. Use it to run, audit, write back, and evolve Raven evaluation loops so the domain compounds instead of resetting each run.

## Purpose

Raven evaluation needs one operational workflow doc, not scattered memory.

```text
eval run
  -> audit evidence
  -> human-readable report
  -> insight writeback
  -> next run improves
```

This note owns the workflow.

## Current Use Case

Primary current use case:

```text
Tier 1 ranker evaluation
  -> run filter
  -> generate trace + markdown audit file
  -> Duc audits
  -> Codex reads audit
  -> Codex updates prompt / dataset
  -> rerun
```

## Workflow

1. Define the evaluation target.
2. Run executable evidence from repo `eval/` or the active backend seam.
3. Produce or inspect the human-readable audit markdown artifact.
4. Audit the result before trusting green output.
5. Write/update the evaluation report in the vault.
6. Write/update the rolling insights note with what the run taught the system.
7. Update project routing only if the domain shape changed.
8. Log the work in the daily log.

## Write Boundary

```text
repo eval/
  -> executable evidence only

vault notes/
  -> workflow docs
  -> reports
  -> audit narratives
  -> compounding insights
  -> production-readiness decisions
```

## Required Outputs Per Non-Trivial Eval Cycle

Minimum closeout:

```text
1. one executable evidence trail
2. one human-readable evaluation report or audit artifact
3. one update to [[projects/raven/notes/raven-evaluation-insights]] when the run teaches anything durable
```

## Tier 1 Specific Flow

```text
ranker runs
  -> markdown audit file
  -> Duc audit line(s)
  -> Codex reads audit file
  -> dataset creation/update
  -> prompt audit / upgrade
  -> rerun
```

No separate complexity theater is required if this loop stays disciplined.

## Compounding Rule

Raven evaluation is not complete when the run finishes.
It is complete when the domain learned.

```text
run result
  -> report
  -> insight extraction
  -> next run starts stronger
```

## Related

- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-enricher-evaluation]]
- [[projects/raven/README]]
