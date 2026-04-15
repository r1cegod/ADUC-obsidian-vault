---
type: project
title: Raven
created: '2026-04-15'
updated: '2026-04-15'
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
  - context/now.md
  - context/goals.md
---
> **TL;DR**: Raven is the candidate next scaffold after PathFinder: a Knowledge Signal Engine that formalizes Duc's internal bullshit detector into source scoring, claim extraction, insight filtering, vault memory, and public synthesis.

## Core Thesis

Raven is not a passive knowledge absorber. It is a judgment engine.

```text
public source
   ↓
claim extraction
   ↓
bullshit detection
   ↓
insight scoring
   ↓
vault memory
   ↓
public synthesis
```

The main asset to formalize is Duc's internal bullshit detector: currently fast, intuitive, and brain-native, but not inspectable, repeatable, or delegable to agents.

## Bullshit Detector Problem

Duc can often sense when a source is fake, vague, guru-fluff, derivative, or non-actionable. The problem is that the detector is tacit.

```text
inside brain
   ↓
fast judgment
   ↓
no explicit labels
   ↓
agent cannot reproduce it
```

Raven's first job is to turn that tacit detector into explicit criteria.

## First Detector Axes

Reject or penalize sources/claims with:

- vague abstractions without concrete mechanism
- no lived experience or operational detail
- no cost, pain, risk, time, money, status, or tradeoff
- advice that survives because it sounds good, not because it predicts reality
- recycled consensus with no new angle
- emotional certainty without evidence trail
- claims that cannot change a build decision

Reward sources/claims with:

- specific failure modes
- concrete workflow details
- named tools, constraints, numbers, or examples
- repeated pain across independent sources
- falsifiable claims
- buildable implications within 7-14 days
- public artifact potential

## Product Shape

Minimum useful loop:

```text
source URL
   ↓
extract claims
   ↓
score each claim
   ↓
label bullshit / weak / useful / high-signal
   ↓
write vault note
   ↓
generate public artifact draft
```

## Distribution Angle

Raven should produce publishable artifacts from its own work:

- signal briefs
- failure analyses
- build logs
- pain maps
- "what the internet is wrong about" posts

The distribution proof is not that Duc consumes more content. The proof is that Raven makes Duc's taste visible.

## Related

- [[context/goals]]
- [[context/now]]
