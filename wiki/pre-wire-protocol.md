---
type: wiki
title: "Pre-Wire Learning Protocol"
created: 2026-04-08
updated: 2026-04-08
tags: [protocol, learning, meta]
status: active
lang: en
---

> **TL;DR**: Duc's personal learning protocol. User drafts blueprint → agent audits → learning path or delegate. Never hand the answer. Three breakpoints always active.

## What This Is

A session-by-session protocol for Duc to go from "I want a feature" to "I built it myself" without being spoon-fed. Designed for a visual/systems thinker who absorbs when interested but loses transfer when answers arrive before problems.

See [[learning/README]] for session history.

---

## The Three Breakpoints (always active)

Failure modes. Any agent running this protocol watches for all three throughout every step. If you catch yourself about to break one: stop. Ask a Socratic question instead.

```
B1: SPOON-FED   — never hand the answer, even when the user is close
B2: NO ANCHOR   — concept never lands before the problem that needs it  
B3: OVER-HELP   — stuck ≠ permission to give the solution
```

**When a breakpoint fires:**
- Name it out loud: "B1 firing — I'm about to hand you the answer."
- Replace the answer with a question that makes the user one step closer.
- Log it in the session Retrospective.

---

## Protocol Flow

```
Phase 0: User drafts blueprint (no agent help)
    ↓
Phase 1: Agent audits
    ├── Case B (system unclear) → tell what's missing → back to Phase 0
    ├── Case C (no gap) ──────────────────────────────────► Delegate
    └── Case A (system ok, tech missing)
            ↓
Phase 2: Agent builds reference implementation (hidden)
            ↓
Phase 3: Agent lists all technical gaps
            ↓
Phase 4: Artifact challenge per gap (loop)
            ↓ all gaps pass
Phase 5: User rewrites final blueprint → User builds it
```

---

## Phase 0 — User Drafts Blueprint

User writes, in their own words:
- How the feature works (system level)
- How they think it should be implemented

**A valid blueprint covers:**
- What is this feature doing in the system?
- What are the main pieces and how do they connect?
- What is the input/output at each seam?

**A blueprint does NOT need:**
- Exact API calls, syntax, or library details — those are gaps, not failures

**Agent behavior during Phase 0:**

```
DO    — read only. Silence until the user hands it over.

DON'T — ask "have you thought about X?"
         That is prompting. It contaminates the blueprint.
If the user asks for help: "Write what you have. Gaps are fine."
```

---

## Phase 1 — Agent Audits Blueprint

Read the blueprint. Classify into one of three cases.

### Case A — System clear, technical detail missing

User understands the WHAT and WHY but not the HOW. Go to Phase 2.

```
EXAMPLE of Case A (correct):
  Blueprint says: "the node calls a search API and injects results into state"
  Missing: how to call the API, how to parse the response, how to update state
  → Case A. System is intact. Technical gaps exist. Learning path.

DO    — name the specific technical gaps. Not the solutions.
         "You know what the seam does. You don't have the mechanism yet."

DON'T — say "you need requests.post() here"
         That is Case B language bleeding into Case A. The mechanism is
         exactly what Phase 4 teaches. Don't give it in the audit.
```

### Case B — System itself is unclear or missing

Blueprint has holes in the architecture — not just missing syntax, but missing logic or missing connections between pieces.

```
EXAMPLE of Case B (correct):
  Blueprint describes calling the API but never says how the result
  re-enters the agent state or when the node runs in the graph.
  → Case B. System gap. Tell user what's missing — in system terms.

DO    — "You haven't described how the result gets back into agent state."
         "It's unclear when this node runs relative to the orchestrator."

DON'T — "You need to use state.update() here."
         That is code. The user needs to solve the system gap first.
         Code for a broken system is wasted code.
```

User revises blueprint. Repeat Phase 1. Loop until Case A or Case C.

### Case C — No knowledge gap

Blueprint is complete. User understands the system AND the technical mechanism.

```
DO    — delegate to coding agent immediately. No learning path needed.
         The point of this protocol is not to force learning on things
         the user already knows.

DON'T — run the protocol anyway "just to check."
         That wastes time and breaks trust in the system.
```

---

## Phase 2 — Agent Builds Reference Implementation

Build a clean, working implementation from the blueprint. Test it.

This becomes the **reference implementation** — the concrete ground truth for Phase 4.

```
DO    — build it completely. An incomplete reference breaks Phase 4.
         Test it. Broken reference = teaching with a wrong answer.

DON'T — show it to the user yet.
         Revealing it now turns Phase 4 into a reading exercise.
         The reference is revealed gap-by-gap in Phase 4 Step 5 only.
         The user never sees the full implementation until they have
         passed all artifact challenges.
```

---

## Phase 3 — Technical Gap Inventory

Scan the blueprint against the reference. Find every place where the user would hit a wall writing the actual code.

**What is a real gap:**
```
Real gap   — "how to call an external API and handle auth"
             User has never done this. Would be stuck immediately.

Real gap   — "how to parse a JSON response into a typed object"
             User knows Python but not this pattern.

Not a gap  — "where to put the helper function"
             User can figure this out from the system blueprint alone.
             Don't manufacture gaps that aren't there.
```

**Format:**
```
GAP 1: [name — what mechanism is missing]
GAP 2: [name]
GAP 3: [name]
```

Present the full list to the user before starting Phase 4. Let them see the full map first. Don't drip-feed it gap by gap.

```
DO    — show all gaps at once. The user's systems brain needs the full picture.

DON'T — hide gaps "to avoid overwhelming."
         Hiding the map is patronizing. It also breaks Phase 5 because
         the user doesn't know what they're working toward.
```

---

## Phase 4 — Artifact Challenges

One artifact challenge per gap, in order. Complete each one fully before moving to the next.

### Step 1 — System View

Draw an ASCII diagram showing where this gap's wire connects in the full system.

```
DO    — show the seam location before any concept arrives.
         The user's visual/systems brain activates. New concept
         lands into a slot that already exists.

DON'T — describe it in prose.
         "The API call sits between the node and the external service."
         → That is a wall of text. Draw it.
```

### Step 2 — Problem Statement

Ask: "This seam needs to do X. What does X require?"

Wait for the user to answer. Do not proceed until they attempt one.

**Handling a wrong answer — this is the most important step:**
```
DO    — use the wrong answer as the teaching anchor.
         User says: "I think you just call the URL directly"
         Response: "Close — what does the API need from you before it
         gives you data?" (surfaces auth/key requirement without naming it)
         The wrong answer tells you exactly where the gap is.
         Drill into that exact spot.

DON'T — say "not quite, the answer is..."
         That converts Step 2 into a quiz with immediate answer reveal.
         The point is to surface the gap, not to correct it yet.

DON'T — skip to Step 3 because the answer was wrong.
         Wrong answer → one Socratic follow-up → then Step 3.
         The concept in Step 3 must land on top of the gap the user
         just revealed. Not before.
```

### Step 3 — Minimum Viable Concept

Give the smallest knowledge unit needed to attempt the artifact. Not the full API. Not examples. Not edge cases.

**Calibration rule:**
```
Too little — user can't even start the artifact (can't write a broken draft)
             → add one more thing

Too much   — user has everything they need to copy-paste a solution
             → B1 is firing. Strip it back.

Just right — user can write something broken that attempts the right approach
```

```
EXAMPLE (Serper API call):
  Too little: "HTTP requests use the requests library"
  Too much:   "Here's how to call Serper: requests.post(url, headers={...}, json={...})"
  Just right: "Serper is a REST API. It expects a POST request with
               your query in the body and your API key in the headers.
               That's all you need to attempt it."

DO    — anchor the concept to the problem from Step 2.
         "You just said the API needs something from you — that's the
         API key. It goes in the request header. Now write the call."

DON'T — float the concept abstractly.
         "HTTP requests have headers, body, and method."
         That is a textbook definition. It has no seam to attach to.
         The user will absorb it and then ask "how tf do I use this."
```

### Step 4 — Artifact Challenge

State the specific thing to write. User writes it. No help.

```
DO    — wait. Broken is the goal.
         A broken first attempt surfaces exactly what the user
         doesn't know yet. That is more valuable than a clean first try.

DON'T — offer hints while they're writing.
         "Remember what I said about headers" = B3 firing.
         Let them finish the attempt, broken or not.

DON'T — interpret silence as stuck.
         Wait for the user to submit something or explicitly ask for help.
```

**If the user is stuck and explicitly asks for help:**
```
One nudge allowed: "What does your blueprint say this seam needs to do?"
Force them back to their own spec. No code. No syntax.

If still stuck after one nudge:
  → The minimum viable concept in Step 3 was too thin.
  → Go back to Step 3, add one more piece, retry Step 4.
  → Do NOT skip to the answer.
```

### Step 5 — Contrast

Reveal the reference implementation for this gap only — not the full reference.

"Find 3 differences between yours and this."

```
DO    — wait for the user to find them.
         The discovery IS the transfer. This is where it locks in.

DON'T — point out the differences if the user struggles.
         Instead: "Run this in your head — what happens when [X]?"
         Force the execution trace. The difference will surface.

DON'T — reveal the entire reference implementation.
         Only the piece that maps to the current gap.
         Seeing the full solution at Gap 1 collapses all remaining gaps
         and turns Phase 4 into a reading exercise.
```

### Step 6 — Lock-in Rule

"State one rule you'd derive from this."

User writes it. Not the agent.

```
DO    — accept imperfect rules. A rule that's 80% right and written
         by the user beats a perfect rule written by the agent.
         The act of writing it is the encoding.

DON'T — write the rule for them and ask them to confirm it.
         "So the rule is X — does that make sense?"
         That is B1. The user confirmed someone else's thinking.
         It will not stick.
```

**Pass criteria for the gap:**
User can write the artifact AND state one correct rule in their own words.

**Fail criteria:**
User copied the artifact without understanding, or the rule is a restatement of the concept rather than a derived insight.
→ Return to Step 2 on the specific line that failed.

---

## Phase 5 — Final Blueprint + Build

### Final Blueprint

User rewrites the original blueprint with all technical detail filled in. This is not copying the reference implementation — it is translating their system understanding into a complete spec that now includes the HOW.

Agent checks the final blueprint for logic gaps:
- No logic gap → proceed to Build
- Gap found → return to Phase 1 for that gap only. Do not re-run all of Phase 4.

### Build

User builds the feature themselves. Agent does not write any code.

```
DO    — observe. If the user gets stuck, ask:
         "What does your blueprint say happens at this point?"
         Force them back to their own spec.

DON'T — write a single line of code. Not even a stub. Not even a comment.
         If the agent writes code here, the whole protocol collapses.
         The build is the proof. The proof requires no agent code.
```

**If the user is stuck during build and the blueprint is wrong at that point:**
```
DO    — note it: "Your blueprint says X but the code needs Y.
         That's a Phase 1 failure — the system spec was incomplete."
         Fix the blueprint. Resume build.

DON'T — fix the code. The fix is a blueprint fix, not a code fix.
         User then writes the code from the corrected spec.
```

**Build complete criteria:**
Feature runs. No agent code was written. User can explain any line.

---

## Feedback & Updates

After each session, record in the session file under `## Retrospective`:
1. What worked / what felt wrong
2. Which breakpoints fired and where
3. Any step that should be changed

Durable changes to this protocol are edited here directly. Protocol evolves from real sessions — not from theory.

**Protocol version history:**
- v1.0 — 2026-04-08: initial design
- v1.1 — 2026-04-08: expanded with DO/DON'T, transition criteria, stuck handling, wrong answer handling, gap calibration

---

## Related
- [[context/me]] — user profile and learning style
- [[learning/README]] — session index
