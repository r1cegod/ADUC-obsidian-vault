---
type: synthesis
title: Vault Target Tree Architecture
created: '2026-04-25'
updated: '2026-04-25'
tags:
  - workflow
  - docs
  - meta
  - obsidian
  - architecture
status: active
lang: en
feeds_into:
  - vault-keeping.md
  - vault_architecture.md
---
> **TL;DR**: A healthy vault grows by branching rules, not by a fixed folder template. Keep the root -> trunk -> branch -> leaf -> source model, then let each project grow creatively as long as every branch reduces search cost, preserves source boundaries, and creates real depth instead of decorative hierarchy.

## Growth Contract
- Parent branch: [[vault-keeping]] and [[wiki/operations/branch-growth-operation]]
- Node role: synthesis / reference leaf
- First parent link: [[vault-keeping]]
- Growth trigger: update when the branch law changes; split only when a specific domain needs its own tree-growth reference.
- Forbidden contents: one-time migration logs, rigid project templates, and project-specific status dumps.
- Source/evidence boundary: this page holds target rules and examples; diagnostic evidence stays in [[wiki/synthesis/vault-tree-growth-system-review]].

## Purpose

This page defines the guardrails for healthy vault growth.

It is not a hard structure, operation manual, or migration checklist. It is the rule set for evaluating whether a vault branch is growing with real depth.

Use this when asking:

```text
Where should a new branch attach?
Is this branch real depth or fake hierarchy?
Does this router make the next decision easier?
Is this page a router, hub, leaf, source, or log?
Is the agent being forced to read too much?
```

Diagnosis lives in [[wiki/synthesis/vault-tree-growth-system-review]]. Execution rules live in operation leaves such as [[wiki/operations/branch-growth-operation]] and [[wiki/operations/file-creation-gate]].

## Base Tree Model

The stable model is:

```text
root entry
  -> trunk router
  -> project or family root
  -> branch hub
  -> leaf note
  -> raw source / evidence only when needed
```

This model is not a rigid file tree. It is a navigation law.

```text
agent wants X
  -> choose the smallest root
  -> choose one trunk
  -> choose one branch
  -> open one leaf
  -> open source only if precision requires it
```

The branch is healthy when every hop answers:

```text
What kind of thing am I looking for next?
```

## Node Roles

```text
Root Entry
  Job: orient the session and choose the next trunk.
  Examples: briefing.md, context/hot.md, context/now.md
  Anti-job: storing project-sized detail.

Trunk Router
  Job: choose the right family or project branch.
  Examples: vault-keeping, development, operations-hub, project README
  Anti-job: dumping mixed-domain leaves.

Project Root
  Job: route project work by task type.
  Example: projects/raven/README.md
  Anti-job: becoming the whole project memory.

Branch Hub
  Job: reduce scan cost inside one meaningful domain, feature, flow, or rule cluster.
  Examples: architecture hub, main-flow hub, search-feature hub, evaluation hub
  Anti-job: adding a click without making a decision easier.

Leaf Note
  Job: hold one durable concept, workflow, report, decision, rule set, or contract.
  Anti-job: becoming an undeclared hub by accumulating many child concerns.

Raw Source / Evidence
  Job: preserve canonical evidence, exact material, traces, samples, datasets, screenshots, transcripts.
  Anti-job: serving as the first thing agents read.

Log / Report
  Job: record what happened and what was learned.
  Anti-job: replacing stable workflow, context, or synthesis pages.
```

## Prime Branching Law

Branching exists to create retrieval intelligence.

```text
branch when it reduces future search cost
branch when it captures a real distinction
branch when the branch will keep growing
branch when the parent is becoming overloaded
branch when siblings are different kinds of work
```

Do not branch for aesthetics.

```text
no fake symmetry
no empty hubs
no folder-shaped vibes
no decorative hierarchy
no mandatory branch just because another project has one
```

Creativity is allowed. Sprawl is not.

## Real Depth vs Fake Depth

Real depth:

```text
Raven README
  -> Architecture Hub
    -> Main Flow Hub
      -> Search Feature Hub
        -> YouTube Search Contract
        -> Reddit Search Contract
        -> Candidate Normalization
        -> Search Evaluation
```

Why this is real:

```text
README chooses project domain
Architecture chooses system shape
Main Flow chooses runtime path
Search Feature chooses one feature surface
Leaves hold actual contracts/evidence
```

Fake depth:

```text
Raven README
  -> Architecture
    -> Main Flow
      -> Feature
        -> Notes
```

Why this is fake:

```text
names are generic
hops do not answer a sharper question
agent still has to inspect siblings to know what matters
```

A branch earns its existence only if it makes the next read more obvious.

A new entry is ready to grow only when it carries its own branch DNA:

```text
parent branch
node role
first parent link
growth trigger
forbidden contents
expected child/source boundary when relevant
```

Without that, the entry is just content. With it, the entry is a living node in the tree.

## Branching Questions

Before creating or promoting a branch, answer:

```text
1. What decision does this branch help an agent make?
2. What kind of child nodes will live here?
3. Are those children the same kind of thing or a mixed bucket?
4. Will this branch likely have 3+ children or repeated future updates?
5. Does this branch replace sideways scanning with a clear route?
6. Is this a domain, a feature, a flow, a rule cluster, or an evidence lane?
7. What is the parent branch?
8. What should never be stored here?
```

If answers are vague, do not create the branch yet. Use a leaf or current hub until growth pressure is real.

## Project Growth Rules

Every project needs a project root and space for compiled knowledge and evidence:

```text
projects/<name>/README.md   project root router
projects/<name>/notes/      compiled project knowledge
projects/<name>/sources/    raw source, evidence, samples, datasets, traces
```

Beyond that, the project grows by pressure, not template worship.

Common branch families:

```text
context       stable/current project state
architecture  system shape, boundaries, diagrams, runtime flow
features      feature-specific contracts, flows, decisions, evals
prompts       prompt contracts, audits, evolution rules
evaluation    workflows, reports, insights, evidence pointers
workflow      handoff, repo-vault boundary, operations, closeout rules
sources       raw/evidence lanes
```

These are suggestions, not required slots. A project should grow the branches its work actually needs.

## Cross-Cutting Domain Rule

Not every child belongs under architecture.

Architecture owns system shape. It should not swallow every other concern.

Better:

```text
Project README
  -> architecture
  -> prompts
  -> evaluation
  -> workflow/rules
  -> sources
```

Then features can cross-link into those domains:

```text
Search Feature Hub
  -> search architecture contract
  -> search prompt if one exists
  -> search eval workflow/report
  -> search raw evidence pointers
```

This preserves both views:

```text
by domain: evaluation hub shows all eval work
by feature: search hub shows everything search-related
```

Cross-links are allowed when they help retrieval. They should not turn the vault into a mesh where every page links to everything.

## Feature Branch Rule

Create a feature branch when a feature becomes a stable unit of work with multiple kinds of knowledge.

Good feature branch shape:

```text
<project>-<feature>-hub
  -> feature overview / contract
  -> implementation architecture
  -> prompt contract if relevant
  -> evaluation workflow/report
  -> source/evidence pointers
  -> open questions or draft leaf if needed
```

Do not create a feature hub for a single simple note. Let the leaf live under the nearest domain hub until it grows.

## Rules Branch Rule

Rules can be their own branch when they govern behavior across many leaves.

Examples:

```text
workflow rules
ownership/delegation rules
evaluation closeout rules
repo-vault boundary rules
source promotion rules
```

Rules should not be buried inside architecture unless they only apply to architecture.

A rule branch is healthy when future agents can ask:

```text
What must I obey before touching this project/domain?
```

and find the answer without reading unrelated design notes.

## Evaluation Branch Rule

Evaluation should separate workflow, evidence, reports, and compounding insight.

```text
evaluation branch
  -> boundary/rule leaf
  -> how-to workflow leaf
  -> per-run report leaves
  -> rolling insights leaf
  -> evidence pointers
  -> prompt/domain routes when evaluation changes prompts
```

The vault stores meaning. The repo stores executable evidence.

For Raven, a healthy evaluation branch might become:

```text
raven-evaluation-hub
  -> raven-evaluation-domain
  -> raven-eval-how-to-use
  -> raven-evaluation-insights
  -> raven-enricher-evaluation
  -> raven-tier1-ranker-evaluation
  -> raven-prompt-hub
  -> repo eval/ evidence pointer
```

## Context Compression Rule

Root context files are pointers, not project databases.

```text
context/hot.md
  -> live continuity cache and next likely route

context/now.md
  -> active priorities, blockers, and project pointers

project context branch
  -> project-specific live state and stable project orientation
```

Bad shape:

```text
context/now.md
  -> many paragraphs of Raven implementation detail
  -> many paragraphs of PathFinder implementation detail
  -> every session pays every project cost
```

Healthy shape:

```text
context/now.md
  -> Raven active; next route: Raven current context or architecture hub
  -> PathFinder reviewable; next route only if blocker appears
```

Then project detail lives under the project branch.

## Source And Evidence Rule

Raw evidence should be reachable but not first-loaded.

```text
compiled note
  -> source pointer
  -> raw source only when exact wording, reproduction, or audit requires it
```

IELTS shows the split:

```text
README
  -> task schema notes
  -> sample leaves
  -> source/tool lane
```

Task 1 schema does not need to contain every sample inline. The schema routes to samples. Samples route back to the schema.

Raven should follow the same separation:

```text
ranker workflow
  -> audit report
  -> raw trace / dataset pointer
```

Do not store full third-party content as durable project memory unless the source lane explicitly owns it and the promotion rule justifies it.

## Link Direction Rule

Links should express ownership and retrieval, not decoration.

```text
parent hub links to child branches/leaves
leaf links back to parent hub
feature hub may link across domains when feature retrieval needs it
root routers link to hubs, not to every leaf
sources are linked from compiled notes, not loaded first
```

If every important note is linked from every router, the vault becomes a mesh. A mesh is expensive to search and hard to maintain.

## Raven Branching Example

This is an example, not a commandment:

```text
projects/raven/README
  -> raven-context-hub
  -> raven-architecture-hub
      -> raven-main-flow-hub
          -> raven-search-feature-hub
          -> raven-ranking-feature-hub
          -> raven-vault-promotion-feature-hub
  -> raven-prompt-hub
      -> enricher prompt
      -> tier1 ranker prompt
      -> prompt evolution rules
  -> raven-evaluation-hub
      -> eval how-to
      -> eval reports
      -> evaluation insights
      -> executable evidence pointers
  -> raven-workflow-hub
      -> ownership/delegation
      -> draft operation adoption
      -> repo-vault boundary
      -> closeout rules
```

This is good only if each branch has real children and helps the next agent choose the next page.

If `raven-main-flow-hub` has only one child, keep it as a leaf or a section inside `raven-architecture-hub` until it grows.

## Growth Examples

### New Raven Search Feature

```text
search starts as one architecture leaf
  -> accumulates YouTube, Reddit, normalization, eval, evidence
  -> promote into raven-search-feature-hub
  -> keep architecture, prompt, eval, and evidence leaves separated
  -> cross-link from domain hubs where useful
```

### New Raven Evaluation Report

```text
new eval run happens
  -> write executable evidence in repo eval/
  -> write report leaf in projects/raven/notes/
  -> link report from raven-evaluation-hub
  -> update raven-evaluation-insights only if cross-run learning changed
  -> log the work
```

### New IELTS Task 1 Sample

```text
new sample appears
  -> store as projects/ielts-writing/samples/<sample>.md
  -> link from the relevant Task 1 schema row
  -> do not paste it into the schema note unless it is a minimal excerpt
```

### New Vault Operation

```text
new operation needed
  -> operations-hub or family hub decides ownership
  -> create operation leaf
  -> route from the owning hub
  -> register in index
  -> update wrappers only if startup behavior changes
```

## Anti-Patterns

```text
hard template worship
  -> every project gets the same empty branches

README as status dump
  -> project root becomes too large to route

index as navigation brain
  -> agent scans global registry instead of local branches

context/now as project database
  -> every session loads stale project detail

raw source as first stop
  -> agent re-derives instead of using compiled knowledge

hub as mixed-family bucket
  -> branch no longer tells the agent what kind of thing it is reading

leaf as accidental hub
  -> one note starts routing many sibling concepts without declaring itself a hub

many direct root links to leaves
  -> tree collapses into flat link soup

fake depth
  -> more hops, same ambiguity
```

## Evaluation Questions

Use these questions when reviewing any vault area:

```text
1. What decision does this branch make easier?
2. What is the root route into this area?
3. What is the parent branch?
4. Is this branch a domain, feature, flow, rule cluster, source lane, or report lane?
5. Can an agent find the right leaf without scanning sibling notes?
6. Does each leaf hold one durable job?
7. Is raw evidence separated from compiled knowledge?
8. Is context pointing to the project branch instead of carrying the branch?
9. Does index register the page without becoming the route itself?
10. Is this real depth, or just another layer of names?
```

## Relationship To Other Files

```text
[[wiki/synthesis/vault-tree-growth-system-review]]
  -> diagnosis: what is broken and why

this page
  -> branching rules: what healthy growth looks like

[[wiki/operations/branch-growth-operation]]
  -> procedure: how to create/attach a new node

[[wiki/operations/file-creation-gate]]
  -> validation: type, tags, registration, propagation

[[vault_architecture]]
  -> current system map and existing directory responsibilities
```
