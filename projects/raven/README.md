---
type: project
title: Raven
created: '2026-04-15'
updated: '2026-04-25'
tags:
  - project/raven
  - ai
  - knowledge
  - evaluation
  - distribution
status: incubating
priority: high
lang: en
feeds_into:
  - briefing.md
  - context/now.md
  - context/goals.md
---
> **TL;DR**: Raven is the active Knowledge Signal Engine scaffold: it turns Duc's tacit bullshit detector into source discovery, metadata triage, audit-backed evaluation, vault memory, and eventually public synthesis.

## Growth Contract
- Parent branch: [[briefing]] Active Projects and `projects/`
- Node role: project root router
- First parent link: [[briefing]]
- Growth trigger: create or promote a Raven hub when the README would otherwise route 3+ same-family leaves or when a domain starts forcing cross-note scans.
- Forbidden contents: raw repo traces, executable eval evidence, full implementation logs, and long current-context detail.
- Expected child types: context, architecture, prompt, evaluation, workflow/rules hubs, and source/evidence lanes.

## Start Here

Use the smallest route that fits the task:

| Need | Go to |
|---|---|
| Current live state, next seam, repo status | [[projects/raven/notes/raven-context-hub]] -> [[projects/raven/notes/raven-current-context]] |
| System shape, Canvas, ingestion/promotion architecture | [[projects/raven/notes/raven-architecture-hub]] |
| Prompt contracts, prompt audits, prompt evolution | [[projects/raven/notes/raven-prompt-hub]] |
| Evaluation workflow, reports, readiness, audit insight | [[projects/raven/notes/raven-evaluation-hub]] |
| Ownership, delegation, draft adoption, repo-vault rules | [[projects/raven/notes/raven-workflow-hub]] |
| Raw evidence, references, source/eval pointers | [[projects/raven/sources/README]] |

Do not jump to raw repo/eval/source material unless a compiled Raven note says exact reproduction or wording precision is needed.

## Core Thesis

Raven is not a passive knowledge absorber. It is a judgment engine.

```text
public source
  -> source discovery
  -> metadata triage
  -> bullshit / signal judgment
  -> audit-backed improvement
  -> vault memory
  -> public synthesis later
```

The main asset to formalize is Duc's internal bullshit detector: fast and brain-native, but not yet inspectable, repeatable, or delegable.

## Detector Direction

Reject or penalize sources/claims with:

```text
vague abstractions
no operational mechanism
no cost/risk/time/tradeoff
recycled consensus
emotional certainty without evidence trail
claims that cannot change a build decision
```

Reward sources/claims with:

```text
specific failure modes
concrete workflow details
named tools, constraints, numbers, examples
falsifiable claims
buildable implications within 7-14 days
public artifact potential
```

## Current Project State

Read [[projects/raven/notes/raven-current-context]] for live implementation status.

Current near-term branch:

```text
enriched query
  -> YouTube search.list
  -> videos.list enrichment
  -> SQLite query/API/candidate logging
  -> Tier 1 ranker
  -> audit markdown
  -> human audit
  -> prompt/eval evolution later
```

## Branch Rules

Raven follows the vault branching rule set in [[wiki/synthesis/vault-target-tree-architecture]].

```text
README
  -> domain hub
    -> leaf
      -> source/evidence only when needed
```

Do not create `main-flow`, `search-feature`, `ranking-feature`, or other feature hubs until [[wiki/operations/branch-growth-operation]] proves real child pressure.

## Boundaries

```text
Vault notes
  -> meaning, reports, decisions, prompt/eval insight, project memory

Repo
  -> code, tests, runnable eval evidence, temporary traces

SQLite
  -> operational workbench for runs, queries, candidates, ratings, logs
```

Raven evaluation reports and production-readiness decisions are vault-canonical under [[projects/raven/notes/raven-evaluation-hub]]. Repo `eval/` is executable evidence only.

## Related

- [[projects/raven/notes/raven-context-hub]]
- [[projects/raven/notes/raven-current-context]]
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-workflow-hub]]
- [[projects/raven/sources/README]]
- [[wiki/synthesis/vault-target-tree-architecture]]
- [[context/now]]
- [[context/goals]]
