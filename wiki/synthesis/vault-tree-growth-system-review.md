---
type: synthesis
title: Vault Tree Growth System Review
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
  - wiki/operations-hub.md
  - SCHEMA.md
---
> **TL;DR**: The vault does not primarily need more notes; it needs a mandatory tree-growth law. Every durable idea should enter through a router, attach to the smallest correct branch, split into hub/leaf/source layers when it grows, and stay queryable without forcing agents to reload the whole vault.

## Growth Contract
- Parent branch: [[vault-keeping]]
- Node role: synthesis / diagnostic report leaf
- First parent link: [[vault-keeping]]
- Growth trigger: promote findings into operation docs when they become repeatable behavior; split only if a future audit becomes its own named domain.
- Forbidden contents: durable project status, raw chat residue, and step-by-step enforcement that belongs in operation pages.
- Source/evidence boundary: this page summarizes structural evidence from the vault; exact procedures live in [[wiki/operations/branch-growth-operation]] and [[wiki/operations/file-creation-gate]].

## Core Diagnosis

The current vault has many correct rules, but the growth system is not strict enough.

The failure mode is:

```text
more content
  -> more router links
  -> larger startup/request context
  -> agent reads too many pages
  -> agent forgets what mattered
  -> new files attach by habit instead of branch law
```

The vault needs to behave like a tree:

```text
root entry
  -> trunk router
  -> branch hub
  -> smaller branch / leaf
  -> source or evidence
```

The goal is not maximum linking. The goal is minimum sufficient traversal.

## Tree Model

### Node Types

```text
root entry
  = session entry and global orientation

trunk router
  = top-level family or project selector

branch hub
  = routes inside one domain only

leaf note
  = one durable concept, rule, workflow, decision, or report

raw source
  = evidence, transcript, dataset, sample, trace, or canonical external material
```

### Navigation Law

```text
agent wants X
  -> start at root
  -> choose one trunk
  -> choose one branch hub
  -> open one leaf
  -> open raw source only if precision requires it
```

If the agent must open many sibling notes to discover the right note, the branch is under-designed.

## Critical Flaws Found

### 1. Branch Law Exists, But It Is Not Operational Enough

[[vault-keeping]] already contains an Official Branching Rule. The rule is correct, but it mostly audits existing branches. It does not yet force new ideas through a branch-creation operation.

Missing question before a new page:

```text
What branch is this page growing from?
```

The current [[wiki/operations/file-creation-gate]] checks type, tags, and registration. It does not strongly enough require parent branch selection, sibling scan, or hub-vs-leaf decision.

### 2. Project Init Is Too Thin

[[wiki/operations/project-init-operation]] says to create a project directory, README, source lane, notes lane, and registration. It does not define a mandatory project anatomy.

A project should not begin as a README plus random notes. A project should begin with a small expandable skeleton:

```text
projects/<name>/
  README.md          root project router
  notes/             compiled project knowledge
  sources/           raw/evidence lane
```

Then, as soon as a project domain has 3+ related notes or obvious growth pressure:

```text
notes/<project>-architecture-hub.md
notes/<project>-evaluation-hub.md
notes/<project>-workflow-hub.md
notes/<project>-prompt-hub.md
notes/<project>-context-hub.md
```

Not all hubs must exist on day one. But the project README must declare how hubs appear.

### 3. Raven Shows Mid-Transition Branch Debt

Raven is not empty, but its shape is uneven.

Current Raven has:

```text
projects/raven/
  README.md
  notes/
    raven-architecture-hub.md
    raven-evaluation-domain.md
    raven-prompt-hub.md
    many strong leaf notes
```

Missing or weak:

```text
projects/raven/sources/          absent
raven-context-hub                absent
raven-workflow-hub               absent
raven-evaluation-hub             evaluation-domain exists but is typed as note, not hub
README branch contract           overloaded with status, doctrine, route list, current work
mandatory domain buckets         informal, not enforced
```

This is why Raven feels scattered even though good notes exist. Its leaves are stronger than its branch structure.

### 4. Evaluation Knowledge Is Split Correctly In Theory, But Not Fully Branched

The current evaluation rule is good:

```text
repo eval/
  -> executable evidence

vault notes/
  -> reports, audit narratives, production-readiness decisions, durable lessons
```

But the domain should split more explicitly:

```text
evaluation hub
  -> how-to workflow
  -> per-run reports
  -> rolling insights
  -> datasets / executable evidence pointers
  -> prompt evolution route
```

Right now Raven has [[projects/raven/notes/raven-evaluation-domain]], [[projects/raven/notes/raven-eval-how-to-use]], and [[projects/raven/notes/raven-evaluation-insights]]. That is already enough to justify a real evaluation hub shape.

### 5. Index Is Becoming A Global Leaf Dump

[[index.md]] is useful as a registry, but it is not the right tool for branch traversal once the vault grows.

Failure mode:

```text
agent cannot find route locally
  -> opens index
  -> scans too much global content
  -> context cost grows
```

Index should stay a lookup table and registry. Local routers should carry actual navigation.

### 6. Context Files Carry Too Much Project Detail

[[context/now]] contains a lot of active project state. Some of that is necessary, but the more it absorbs project detail, the more every session pays the cost of every active project.

Better law:

```text
context/now
  -> active priorities and next router only

project README / context hub
  -> project-specific live state
```

For Raven, a `raven-context-hub` or `raven-current-context` leaf would reduce pressure on [[context/now]].

### 7. Raw Source / Sample / Evidence Lanes Are Not Uniform Across Projects

PathFinder has a strong source lane. IELTS has `samples/` and `sources/`. Raven currently lacks `sources/`.

This violates the tree model because raw/evidence material has no project-local landing zone.

A project can be early, but it still needs a declared raw lane before ingest begins.

## Positive Patterns To Preserve

### PathFinder

PathFinder is the strongest current branch model:

```text
README
  -> architecture hub
  -> context hub
  -> prompt hub
  -> evaluation hub
  -> workflow hub
  -> leaf notes
  -> sources/docs only when precision requires it
```

This is the model to generalize, not copy mechanically.

### IELTS Writing

IELTS shows a clean content split:

```text
README
  -> task schema notes
  -> samples as separate leaves
  -> source/tool lane
```

This proves the user's point: samples and how-to rules should not be forced into the same file when separate leaves make retrieval cheaper.

### Raven Vault Keeper Architecture

[[projects/raven/notes/raven-vault-keeper-harness-architecture]] already states the right memory law for Raven itself:

```text
raw source
  -> candidate
  -> judged item
  -> promoted memory
  -> canonical synthesis
```

That same promotion ladder should govern the vault's own growth.

## Proposed Growth Law

Every new durable node must answer these questions before creation:

```text
1. What root/trunk does this belong under?
2. What parent branch owns it?
3. Is it a hub, leaf, source, sample, report, or log entry?
4. Does a sibling already cover this job?
5. Will this branch likely grow to 3+ notes?
6. What page should link to it first?
7. What downstream router or index must know it exists?
```

## Proposed Operation: Branch Growth

Create a new official operation leaf:

```text
[[wiki/operations/branch-growth-operation]]
```

Purpose:

```text
Create or place a new durable vault node without corrupting the tree.
```

Route:

```text
vault-keeping
  -> branch-growth-operation
  -> file-creation-gate
  -> self-healing-operation
```

Minimum steps:

```text
1. Identify root/trunk/project.
2. Identify parent branch hub or create one if branch pressure exists.
3. Decide node role: hub, leaf, source, sample, report, log.
4. Check sibling notes for duplication or split pressure.
5. Create/update the node.
6. Link from parent only, not from every high-level router.
7. Register in index if required.
8. Propagate and log.
```

## Proposed Raven Branch Shape

Raven should evolve into:

```text
projects/raven/
  README.md
  notes/
    raven-context-hub.md
    raven-architecture-hub.md
    raven-evaluation-hub.md
    raven-workflow-hub.md
    raven-prompt-hub.md
    raven-current-context.md
    raven-project-context.md
    raven-*-leaf.md
  sources/
    eval/
    references/
    raw/
```

Immediate low-risk patch:

```text
1. Create projects/raven/sources/ with a README or .gitkeep-equivalent note if needed.
2. Promote raven-evaluation-domain into a true evaluation hub or create raven-evaluation-hub that owns it.
3. Create raven-context-hub and raven-current-context so context/now can point to Raven instead of carrying too much Raven detail.
4. Create raven-workflow-hub for ownership/delegation, draft adoption, repo-vault boundary, and dev-log/eval closeout rules.
5. Slim Raven README so it routes first and describes second.
```

## Proposed Vault Keeping v2

[[vault-keeping]] should become the entry for tree health, not just maintenance.

New top-level structure:

```text
vault-keeping
  -> session hygiene
  -> branch growth
  -> file creation gate
  -> propagation
  -> lint / flow-check
  -> self-healing closeout
```

The key addition is branch growth between idea and file creation:

```text
idea appears
  -> branch-growth decision
  -> file-creation gate
  -> propagation/self-healing
```

## Migration Sequence

### Patch 1 - Add Branch Growth Operation

Create [[wiki/operations/branch-growth-operation]] and route it from [[vault-keeping]] and [[wiki/operations-hub]].

### Patch 2 - Strengthen Project Init

Update [[wiki/operations/project-init-operation]] so every new project declares:

```text
README router
notes lane
sources lane
hub emergence rule
raw/source/evidence boundary
```

### Patch 3 - Restructure Raven Branches

Do not rewrite Raven content first. Add the missing branch hubs and move route responsibility upward:

```text
README -> hubs -> leaves
```

### Patch 4 - Context Compression

Move project-specific live detail from [[context/now]] into project current-context leaves where appropriate. Keep [[context/now]] as a pointer layer.

### Patch 5 - Enforce During File Creation

Patch [[wiki/operations/file-creation-gate]] so every new file must name its parent branch before type/tags are selected.

## Strategic Verdict

The vault is already learning, but it is learning like a fast-growing organism with partial skeleton.

The next system upgrade is not more memory. It is bone structure:

```text
branch before leaf
router before content
source before synthesis
hub before sibling explosion
context pointer before context dump
```

That is how the tree grows without choking the agent that has to climb it.
