---
type: synthesis
title: Evaluation And Production Prompt Domain
created: '2026-04-26'
updated: '2026-04-26'
tags:
  - evaluation
  - prompts
  - workflow
  - docs
  - synthesis
status: active
lang: en
feeds_into:
  - index.md
  - projects/raven/notes/raven-evaluation-hub.md
  - projects/raven/notes/raven-prompt-hub.md
---
> **TL;DR**: General vault knowledge for evaluation and production prompt creation. Project evaluation branches own project-specific reports, datasets, traces, and readiness decisions; this page owns the reusable method for turning behavior into evals, evals into prompt contracts, and prompt contracts into production gates.

## Growth Contract
- Parent branch: [[index.md]] Synthesis
- Node role: synthesis leaf
- First parent link: [[index.md]]
- Growth trigger: promote into a hub only when multiple reusable evaluation leaves exist, such as prompt gates, trace audit methods, dataset design, and production signoff law.
- Forbidden contents: project-specific run reports, raw traces, datasets, runner scripts, and one-off prompt drafts.
- Source/evidence boundary: reusable method lives here; project evidence stays in each project evaluation branch or repo `eval/` workspace.

## Boundary

```text
global evaluation domain
  -> reusable method
  -> prompt production law
  -> eval design patterns
  -> signoff rules

project evaluation branch
  -> project-specific workflow
  -> project-specific reports
  -> production-readiness decisions
  -> links to executable evidence

repo eval/
  -> runner scripts
  -> datasets
  -> traces
  -> temporary reproduction artifacts
```

Do not turn this page into a project log. If the content only matters to one project run, it belongs in that project's evaluation branch.

## Evaluation Core

Evaluation is a compression machine for behavior.

```text
desired behavior
  -> explicit contract
  -> cases that attack the contract
  -> runner or audit surface
  -> trace inspection
  -> prompt/code change
  -> rerun
  -> production claim with scope
```

A green command is not the same as a production claim. The claim must name the seam it proves and the seams it does not prove.

## Production Prompt Loop

```text
prompt intent
  -> input boundary
  -> output contract
  -> failure modes
  -> evaluation cases
  -> trace audit
  -> prompt revision
  -> rerun until stable
  -> project report
  -> durable insight extraction
```

A production prompt is not a nicer instruction. It is a behavioral contract that survives adversarial, boring, incomplete, and edge-case inputs.

## Production Prompt Formula

PathFinder's old prompt knowledge compresses into this formula:

```text
identity
  -> named role, narrow domain, target user, explicit non-roles

scope
  -> in scope / adjacent / out of scope / boundary script

task
  -> the single job this call performs

input contract
  -> allowed inputs, forbidden inputs, trust level of each input

output contract
  -> exact fields, labels, formats, and omission rules

reasoning protocol
  -> only when the task is judgment-heavy; otherwise skip it

grounding rules
  -> what evidence is allowed, what must never be fabricated

examples
  -> current desired behavior, boundary cases, low-confidence cases

evaluation path
  -> dataset, runner, trace audit, human audit, rerun rule

guardrails
  -> injection defense, identity lock, prompt confidentiality
```

A production prompt is layered context engineering, not a clever paragraph.

```text
static base
  -> identity, scope, contracts, guardrails

dynamic context
  -> runtime state, retrieved docs, user/project context

task block
  -> volatile per-call instruction selected by code
```

## Prompt Contract Checklist

Every production prompt should make these explicit:

```text
identity
  -> what role the model is playing

mission/task
  -> what job it is doing now

input boundary
  -> what it may use and what it must ignore

output contract
  -> exact shape, fields, labels, or format

quality bar
  -> what counts as good behavior

failure penalties
  -> what to avoid, reject, or downgrade

scope denial
  -> what the prompt must not solve

grounding
  -> allowed evidence and anti-fabrication rules

examples
  -> standard, boundary, low-confidence, and adversarial cases

evolution path
  -> how eval results change the prompt later
```

If a prompt has no eval path, it is a draft, not production. If a prompt has no explicit scope denial, it will expand until it lies.

## Evaluation Case Design

Use cases that expose the contract, not cases that flatter the prompt.

```text
happy path
  -> proves the intended behavior can happen

boundary case
  -> proves the prompt respects scope

negative case
  -> proves the prompt can reject weak input

confuser case
  -> proves it does not follow shallow keywords

regression case
  -> preserves a bug fix or hard-earned lesson

human-audit case
  -> captures taste or judgment that cannot be reduced yet
```

Small evals are acceptable when the seam is small. The weak move is pretending a small eval proves the full system.

## Trace Audit Law

Every serious eval needs at least one human-readable audit surface.

```text
input
  -> model output
  -> deterministic checks if available
  -> human audit note when judgment matters
  -> failure reason
  -> next change
```

The trace should answer:

```text
what failed?
why did it fail?
is the failure prompt-level, code-level, data-level, or evaluator-level?
what exact change should be tested next?
```

## Production Claim Law

A production-readiness statement must be scoped.

Good shape:

```text
Production ready: yes/no for <specific seam> under <tested input class> using <eval evidence>.
Not proven: <adjacent seams>.
Next risk: <highest remaining unknown>.
```

Bad shape:

```text
production ready
works now
all good
```

## When To Update This Page

Update this page only for reusable lessons:

```text
- a new eval pattern that applies across projects
- a production prompt law that should be reused
- a stable failure mode in prompt/eval work
- a better signoff rule
- a clearer vault-vs-repo boundary
```

Do not update it for one run's score, trace path, or project-specific readiness status.

## Project Handoff

When a project needs evaluation or prompt work:

```text
1. Start in the project README.
2. Open the project evaluation or prompt hub.
3. Use this page for the reusable method.
4. Put project-specific evidence and reports back into the project branch.
5. Extract only reusable lessons back here.
```

## Related

- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]
- [[projects/pathfinder/notes/pathfinder-prompt-hub]]
- [[projects/pathfinder/notes/docs-production-system-prompts]]
- [[vault-keeping]]
