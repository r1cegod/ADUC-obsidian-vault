---
type: source-summary
title: Current Context
created: '2026-04-06T00:00:00.000Z'
updated: '2026-04-29'
tags:
  - project/pathfinder
  - pathfinder
  - context
  - live
status: active
lang: en
source: '[[projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md]]'
---
> **TL;DR**: PathFinder is reviewable/portfolio-ready unless a concrete blocker appears. Its remaining live context is evaluation hardening, stage/state correctness, token-memory behavior, and explicit vault/repo sync discipline.

## Role

This is the project-local live context leaf for PathFinder.

```text
duc-os/current.md
  -> says PathFinder status and route only

PathFinder Context Hub
  -> routes project-local live and stable context

this note
  -> carries PathFinder-specific live state
```

Do not move PathFinder implementation detail back into root context unless it changes global priorities.

## Current Status

PathFinder should be treated as reviewable/portfolio-ready unless a specific blocker threatens demo or review confidence.

Current posture:

```text
freeze by default
  -> fix critical blockers only
  -> avoid continued feature pushing without a named review/demo risk
```

The next high-leverage build focus has shifted toward Raven and reusable AI-agent infrastructure.

## Active Hardening Lanes

### Goals / Stage State

- Treat Goals as a planning-ready handoff layer in prompts.
- The next replay should exercise the full orchestrator path so routing and counter behavior are tested beyond the stage + compiler wrapper.
- Do not count assistant wording as stage completion; verify from raw `getBackendState()`.
- Goals completion requires `goals.done === true` plus frontend completed-stage/current-stage agreement.
- Incomplete current stages must stay anchored to raw `done` state.

### Frontend / Live Trace

- Frontend trace output regression is documented in `eval/FRONTEND_EVALUATION_REPORT.md` and the vault frontend-evaluation workflow.
- Use the completed frontend fixture report as the UI baseline.
- Reopen frontend testing only for new UI changes, mobile/visual polish, or a named review risk.
- The uncertainty attack and identity-continuation runs are distinct evaluation modes, not generic replay substitutes.

### Stage Transition / Output

- Stage transitions now have a post-stage manager before output.
- If a stage marks itself done, the output prompt should see the newly active stage in the same turn.
- Output lock and stage intro are complementary: stage intro may acknowledge the completed previous-stage handoff, while current-stage lock prevents moving beyond the newly active incomplete stage.
- Purpose now mirrors Goals' handoff-sufficiency pattern; remaining execution realism belongs to Goals, Job, or Major rather than another repeated risk squeeze.

### Replay Decision

Do not pre-choose:

```text
orchestrator replay
vs
broader full-path audit
```

Make that call only after the full eval sweep lands or a named blocker appears.

## Evaluation And Evidence Boundaries

PathFinder evaluation docs, reports, audits, and run retrospectives are vault-canonical under:

```text
projects/pathfinder/sources/docs/evaluation/
```

Repo `eval/` is executable evidence only:

```text
runners
JSONL datasets
trace folders
manifests
scratch messages
screenshots
temporary reproduction artifacts
```

Route evaluation work through:

```text
[[projects/pathfinder/notes/pathfinder-evaluation-hub]]
  -> [[projects/pathfinder/notes/docs-evaluation-domain]]
  -> relevant workflow/report leaf
```

## Token And Memory Lanes

Token optimization is active in both:

```text
main messages lane
sub-orchestrator routing_memory lane
```

Current behavior:

- workers read a capped recent tail
- `routing_memory` keeps its summarizer lane
- summarizer and worker families have separate focus-eval lanes and production gates
- full eval remains the broader hardening gate

## Testing And Mirror Rules

- Python contract/regression tests live under `D:\ANHDUC\Path_finder\backend\test\`.
- New tests should be invoked as `backend.test.<module>` and should not be added at repo root.
- The vault docs are canonical by default.
- Repo documentation mirrors are explicit exceptions, not a general sync rule.
- The maintained dev-log mirror uses `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` plus mirrored daily files under `logs/dev/days/`.
- Maintained mirrors should use explicit sync routines rather than manual-by-default content copying.

## Open Follow-Up

Only reopen PathFinder if one of these becomes relevant:

```text
review/demo blocker
broader University comparison/ranking proof
fresh Goals/Job/Major handoff replay
frontend continuation proof
cheap Python seam coverage worth locking
explicit repo mirror automation
```

Known University lane:

- UEH/FPT/RMIT/UEL comparison behavior remains the named broader evaluation surface.
- Harden this only if needed for review/demo confidence.

## What Does Not Belong In Root Context

```text
PathFinder eval mechanics
stage-specific hardening notes
frontend/live-trace reproduction details
token-memory implementation detail
repo-vault mirror policy detail
Python test-folder rules
```

Duc OS current state should only say PathFinder's status and point here.

## Related

- [[projects/pathfinder/notes/pathfinder-context-hub]]
- [[projects/pathfinder/README]]
- [[projects/pathfinder/notes/docs-project-context]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]
- [[projects/pathfinder/notes/docs-evaluation-domain]]
- [[projects/pathfinder/notes/pathfinder-workflow-hub]]
