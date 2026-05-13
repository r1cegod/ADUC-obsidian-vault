---
type: note
title: Raven Codex-Native Pivot
created: '2026-05-02'
updated: '2026-05-02'
tags:
  - project/raven
  - ai
  - architecture
  - workflow
  - context
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/notes/raven-current-context.md
  - duc-os/current.md
  - context/hot.md
---
> **TL;DR**: Raven should stop trying to become a custom all-purpose agent harness and narrow into a source-acquisition and evidence-preparation tool that feeds a Codex-centered operating system.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-context-hub]] and [[projects/raven/README]]
- Node role: leaf
- First parent link: [[projects/raven/notes/raven-context-hub]]
- Growth trigger: split only if the Codex-native operating model, Raven source-tool contract, or Wave Reader product surface each develop independent implementation/evaluation branches.
- Forbidden contents: raw transcripts, full repo implementation logs, speculative feature wishlists, and tool-specific hype copied from external courses.
- Source/evidence boundary: this page stores the strategic pivot and architecture boundary; runnable code, eval traces, and fetched third-party content stay in the repo/source lanes.

## Pivot

Nate's AIOS course exposed the resource-allocation error:

```text
old implicit direction
  -> build Raven as custom agent system
  -> pay API/time cost for agent harness
  -> rebuild orchestration Codex already provides

new direction
  -> Codex is the general agent/operator layer
  -> Duc OS + vault are the memory/control layer
  -> Raven is a narrow hard-source acquisition tool
  -> Wave Reader is built around Codex, not inside Raven
```

This is not a downgrade. It is a scope correction.

## New Boundary

Raven owns:

```text
hard-to-reach source discovery
metadata enrichment
bounded fetch/transcript/source access
candidate filtering
source cards / evidence packets
Tier 2 Wave Reports over source cards
local persistence and audit readouts
```

For the official Tier 2 artifact contract, read [[projects/raven/notes/raven-tier-2-source-packet-contract]].

Raven does not own by default:

```text
general agent orchestration
life operating system behavior
multi-tool executive assistant loops
expensive custom LLM harnesses
full autonomous workflow management
public-facing distribution system
```

Codex owns the general reasoning/operator loop:

```text
Duc asks / writes / decides
  -> Codex reads vault + Raven outputs
  -> Codex synthesizes, drafts, plans, audits, edits
  -> vault stores durable decisions
```

## Product Shape

Wave Reader becomes a Codex-native workflow, not a standalone custom agent platform.

```text
source problem
  -> Raven fetches hard sources
  -> Raven emits source packet/card
  -> Codex reads packet + Duc OS context
  -> Codex produces synthesis / decision / post / build implication
  -> vault stores what should compound
```

The practical build target is therefore:

```text
Raven CLI/API/tool
  -> fetches and prepares sources better than manual search
  -> gives Codex clean evidence to think with
  -> avoids durable raw-content hoarding
```

## Strategic Reason

Duc currently has more access to Codex than to paid API budget and more leverage in distribution than in rebuilding infrastructure.

```text
scarce resources
  -> money for APIs: low
  -> time for custom harness: low
  -> access to Codex: available
  -> vault context: strong
  -> distribution gap: high leverage
```

So the founder move is:

```text
rent the general agent layer
build the missing source-access tool
ship proof and distribution earlier
```

## Implications

Immediate implications:

- Stop expanding Raven as a full agent OS.
- Keep evals only where they protect source quality and evidence reliability.
- Prioritize the first usable source packet over new agent features.
- Treat Raven as a tool Codex can invoke/read, not as the brain.
- Shift more effort toward proof artifacts, distribution, and paid-pain discovery once Raven can produce one useful packet.

## Failure Modes

```text
scope relapse
  -> Raven grows back into custom OS
  -> time/API cost returns

thin-wrapper trap
  -> Raven becomes only a script with no judgment/evidence standard
  -> Codex receives noisy source dumps

distribution avoidance
  -> pivot becomes another private architecture improvement
  -> no proof, no room escape
```

Counter-rule:

```text
Raven exists to make Codex + Duc faster at reading waves.
If a feature does not improve hard-source access or evidence quality, it is suspect.
```

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-context-hub]]
- [[projects/raven/notes/raven-current-context]]
- [[projects/raven/notes/raven-progress-map]]
- [[duc-os/current]]
- [[duc-os/escape-route]]
