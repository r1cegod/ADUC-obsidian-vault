---
type: note
title: Raven BS Detector Ingestion Architecture
created: '2026-04-20'
updated: '2026-04-25'
tags:
  - project/raven
  - architecture
  - evaluation
  - ingest
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-architecture-hub.md
  - projects/raven/notes/raven-prompt-hub.md
  - projects/raven/notes/raven-evaluation-hub.md
  - projects/raven/notes/raven-phase-1-ingest-rating-plan.md
---
> **TL;DR**: Raven should ingest Duc's detector as audit-backed judgment traces first, not as a self-updating prompt. In Phase 1 this starts with Tier 1 title/preview filtering and human audit evidence; deeper bullshit labels can harden later.

## Core Decision

The detector is not a blob of taste to dump into a prompt. It is a judgment system that needs observable traces.

```text
Duc's tacit judgment
  -> explicit audit action
  -> structured disagreement data
  -> detector change proposal
  -> human-approved criterion update
```

## Phase 1 Boundary

Attach the detector after candidate persistence and before any autonomous evolution.

```text
query target
  -> search metadata
  -> save run/query/candidate rows
  -> Raven Tier 1 output
  -> markdown audit file
  -> Duc audit
  -> disagreement summary
  -> proposed prompt / detector delta later
```

This keeps Phase 1 grounded in the SQLite workbench and avoids pretending Raven can self-evolve before it has evidence.

## Tier 1 First, Full Detector Later

Phase 1 detector ingest is not yet full bullshit classification.

```text
Tier 1 now
  = would Duc click this?
  = title + description_or_preview
  = cheap filter

full detector later
  = stronger epistemic judgment
  = richer evidence surface
  = deeper claim-level evaluation
```

That split matters. If the system confuses attraction filtering with truth judgment, it will fake depth.

## Minimum Phase 1 Audit Shape

Each audit should capture the decision and the correction pressure.

```text
Title
Description_or_preview
Raven output
Human audit line
```

From that artifact, Codex can derive dataset rows and prompt-audit evidence.

## Detector Training Inputs

Raven needs these human signals first:

```text
1. Tier 1 label
   skip / maybe / click / must_click

2. attraction and repulsion markers
   positive_pull[] / negative_push[]

3. natural-language correction
   what Raven got wrong or right

4. disagreement pattern summary later
   where the prompt keeps missing Duc's taste
```

Pairwise preference and stronger bullshit labels can come later if Tier 1 stops being the main bottleneck.

## Evolver Guardrail

Phase 1 evolver output should remain human-gated.

```text
audits in
  -> disagreement patterns
  -> missing criteria
  -> proposed prompt / detector candidates
  -> no automatic rewrite approval
```

Forbidden until audit volume exists:

```text
automatic prompt rewrite deployment
automatic rubric rewrite deployment
automatic code rewrite
```

## First Usable Loop

```text
1. Save YouTube/Reddit metadata candidate.
2. Raven gives Tier 1 output.
3. Raven writes one markdown audit file for the eval run.
4. Duc audits candidates in plain language.
5. Codex reads the audit file and updates dataset/prompt evidence.
6. The next Tier 1 version is proposed from the evidence loop.
```

## Versioning Model

Treat the detector like a product asset.

```text
tier_versions
  id
  created_at
  parent_version_id
  prompt_snapshot
  change_summary
  evidence_refs
  approved_by_human
```

The first version can live as a prompt contract plus a small note trail. Do not add a complex rules engine yet.

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
