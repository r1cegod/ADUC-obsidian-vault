# PathFinder - Dev Log Archive

> Archived from `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\DEV_LOG.md`.
> Contains entries dated before `2026-04-01`.

---

### 2026-03-14 | Topology, state contract, and `purpose_graph.py`

**Focus:** Establish the first workable graph shape and get `purpose_graph.py` operating against a real typed state contract.

**Key outcomes:**
- mapped the full 8-agent topology and locked the need for bottom-up build order
- connected LangGraph Studio locally on Windows to avoid Docker friction
- redesigned the orchestrator around internal chat-manager behavior and soft handoff boundaries
- introduced strict Pydantic profile models in `state.py` instead of loose dict state
- fixed the `.model_dump()` boundary in `purpose_graph.py` so Pydantic objects could safely cross TypedDict state
- hardened the early `purpose_graph.py` loop against the real schema with `langgraph dev`

**What I learned:**
- LangGraph state is TypedDict-first, not Pydantic-first; every node has to serialize before returning
- official-doc-style teaching transferred better because the gap between the generic example and the repo stayed visible

**Next:** Keep reinforcing `purpose_graph.py` against the strict schema and preserve the bottom-up build sequence.

---

### 2026-03-17 | Token management and reducer semantics

**Focus:** Add message-budget control to `purpose_graph.py` without losing deterministic state behavior.

**Key outcomes:**
- wired token management into `purpose_graph.py` with `check_node`, a conditional route, and a `summarizer_node`
- used `RemoveMessage` to delete the oldest 3/4 of the message log when the limit was hit
- found and fixed a silent state-key mismatch: `check_sum` read `limit_hit` while `check_node` wrote `purpose_limit`
- fixed `purpose or ""` formatting so `None` no longer leaked into prompts as the literal string `"None"`
- confirmed the path live in LangSmith with `input_token: 1341`, `purpose_limit: false`, and correct routing to `confident`

**What I learned:**
- the `add_messages` reducer has two different behaviors: `BaseMessage` appends, while `RemoveMessage(id=...)` deletes by ID
- conditional routers return lookup keys, not booleans; the `path_map` is the real mental model

**Next:** Keep the stage graph lean and carry the same discipline into the later stage graphs.

---

### 2026-03-18 | Orchestrator classification boundary

**Focus:** Audit the input parser and separate LLM classification from Python routing.

**Key outcomes:**
- audited `INPUT_PARSER_PROMPT` against the 16-dimension production prompt doc and patched 6 gaps in `orchestrator.py`
- moved reasoning into the structured schema (`deflection_reasoning`, `tension_reasoning`) after realizing `with_structured_output` cannot emit free text before JSON
- redesigned the stage manager around 4 Python-owned routing cases: normal, rebound, contradict, and forced
- rewrote `StageCheck` so the LLM only classifies and Python owns the route decision
- clarified the Thinking-stage strategy: use quiz priors, then let the agent verify behaviorally rather than trusting self-report

**What I learned:**
- auditability is the real gain from structured reasoning fields; schema order does not force model cognition
- the clean boundary is `LLM tags, Python routes`; pushing both into the model spends tokens and hides bugs

**Next:** Keep hardening the orchestrator prompts while preserving the Python-owned control surface.

---

### 2026-03-20 | Rebound false positives and StageCheck defaults

**Focus:** Remove silent routing regressions in the orchestrator before they spread across more sessions.

**Key outcomes:**
- fixed false-positive rebound routing by changing `has_rebound` from an OR-like rule to `bool(future) and stage.rebound`
- added the forced-stage carveout so explicit backward jumps no longer count as rebounds
- added a precise stage-content map to `INPUT_PARSER_PROMPT` so broad messages stop spraying tags across stages
- added defaults to every `StageCheck` field in `state.py` and introduced `DEFAULT_STAGE` for stale checkpoints
- removed dead `stage_skipped` state and caught a variable-shadowing bug that silently destroyed a list slice

**What I learned:**
- silent `False` states are worse than exceptions because they degrade behavior without announcing the failure
- prompt precision still depends on having the right local context; the orchestrator needed `current_stage` as an anchor even if Python still owned routing

**Next:** Run the master graph end to end and keep watching for state-shape bugs that import tests will not catch.

### Entry 002 Ã¢â‚¬â€ Day 15: 2026-03-29

**Goal:** Lock the path-agent removal and spec the knowledge/data agent taxonomy and data retrieval contract.

**Decision:** Fully deleted `PathProfile` from `state.py` and removed `path` + `path_limit` from `PathFinderState`. Path debate is now Case B2 in `build_compiler_prompt()` Ã¢â‚¬â€ a prompt injection block (`PATH_DEBATE_BLOCK`) triggered by a pure Python check: all 6 profiles `done=True`. Separately, formalized the agent split into **knowledge agents** (thinking, purpose, goals Ã¢â‚¬â€ extract from the student's head, no external data) and **data agents** (job, major, uni Ã¢â‚¬â€ match against real-world datasets). Designed agent-exclusive Pydantic query forms (`JobQuery`, `MajorQuery`, `UniQuery`) where each form's fields map directly to that agent's `*Profile` fields. `JobScoringOutput` combines FieldEntries + `JobQuery | None` + `need_data: bool` into one structured output call, avoiding a second LLM hop.

**Rejected alternative:** RAG (vector store + semantic search) for data agent retrieval. The full VN-focused dataset is ~100 entries across three categories Ã¢â‚¬â€ it fits in a few KB of JSON. Semantic search adds embedding costs, a vector store dependency, and nondeterministic results on short enum-like entries ("startup", "engineer"). Deterministic Python filter functions on JSON files (`filter(jobs, role_category="engineer")`) are faster, cheaper, and produce auditable results. RAG solves a scale problem that doesn't exist here.

**What broke:** `PathProfile` class and `path: PathProfile | None` / `path_limit: bool` removed from state. Any node that referenced these fields (none were wired yet) would now fail import. `ProfileSummary.path` slot also removed. `_compute_stage_status()` in `output.py` no longer includes a "path" entry in its `profile_map`.

**What I learned:** The gate question for "subgraph vs. compiler mode" is: does this stage introduce a **new query form exclusive to its domain**? Data agents are distinguished by having a typed retrieval contract (a Pydantic query form) that knowledge agents never need. The taxonomy isn't just a UX distinction Ã¢â‚¬â€ it's a structural one that changes node topology.

**Next:** Define `jobs.json` schema (~50 VN-relevant entries: role_category, company_stage, vn_salary range, required_skills, related_majors). Build `retrieve_node` as a pure Python filter. Spec `JobScoringOutput` as the dual-purpose scoring output (FieldEntries + retrieval query).

---

### Entry 003 Ã¢â‚¬â€ Day 15: 2026-03-29

**Goal:** Eliminate redundant LLM calls in stage subgraphs without losing response quality.

**Decision:** Removed `chatbot_node` and `summarizer_node` from all 6 stage subgraphs. Replaced with a single **analyst node** that writes a prose analysis to `stage_reasoning.{stage}`. The output compiler reads `stage_reasoning` via `PROFILE_CONTEXT_BLOCK` and generates the student-facing response itself Ã¢â‚¬â€ it is the sole response generator across all stages.

**Rejected alternative:** Keep the chatbot node, add a `stage_draft` state field, have the output compiler adapt the draft. Rejected because it adds a new top-level state field and a new `STAGE_DRAFT_BLOCK` in `output.py` for zero net gain Ã¢â‚¬â€ the output compiler already has `fields_needed` and `stage_status` from `_compute_stage_status()`.

**What broke:** Nothing at runtime Ã¢â‚¬â€ and that was the sign something was wrong. The chatbot nodes had been silently writing to `{stage}_message` queues while the output compiler reads from `messages` (global). Two LLM calls per turn, only one doing visible work. No error, no warning.

**What I learned:** Trace information flow, not just code flow. The bug wasn't in the node logic Ã¢â‚¬â€ it was in the channel. `{stage}_message` is a routing queue for stage agents to read context; it is not a response channel. The output compiler reads `messages` (global). These are two different channels.

**Next:** Build remaining stage agents using the 2-node pattern (scoring + analyst). Wire all into the master orchestrator.

---

### Entry 004 Ã¢â‚¬â€ Day 16: 2026-03-30

**Goal:** Guarantee stage agents retain full domain memory even after the global summarizer compresses the conversation.

**Decision:** Split memory into two permanent layers. (1) The global `SUMMARIZER_PROMPT` is narrowed to track only macro psychology, compliance, and routing events Ã¢â‚¬â€ not stage content. (2) A deterministic **Python Tagger** is added to `input_parser`: it reads `response.stage_related` from the LLM and instantly copies the raw `HumanMessage` to every matching `{stage}_message` queue. Result: `job_message` is an untruncated vault of every message the student sent that touched the job domain. Separately, wired **contradict tagger** into `stage_manager`: when `contradict_target` is set, the current message is additionally tagged to all past-stage queues, and `context_compiler` assembles prompts from `list(dict.fromkeys(stage_related + contradict_target))` (union, order-preserved).

**Rejected alternative:** Let stage agents read global `messages`. Rejected because the summarizer runs at 2000 tokens Ã¢â‚¬â€ within 30 minutes of a real session, stage agents would lose the student's exact early answers. Let the summarizer track stage data Ã¢â‚¬â€ rejected because it requires the summarizer to understand domain-specific fields without hallucinating them.

**What broke:** Nothing at code level. The `context_stages` union exposes that `contradict_target Ã¢Å â€  stage_related` is currently always true Ã¢â‚¬â€ but that's an assumption that could break if `stage_related` filtering logic changes. Making the union explicit is forward-proof.

**What I learned:** The summarizer compresses exactly what stage agents need most. Routing memory (behavioral patterns) degrades gracefully. Domain memory (what the student actually said) cannot degrade. Two channels, two decay profiles, two memory strategies.

**Next:** Wire all 6 stage subgraphs into the master orchestrator.

---

### Entry 005 Ã¢â‚¬â€ Day 17: 2026-03-31

**Goal:** Full end-to-end pipeline wired. One graph from student input to response.

**Decision:** Compiled all 6 stage subgraphs as nodes in the master `StateGraph`. Node names match `current_stage` string values exactly (`"thinking"`, `"purpose"`, `"goals"`, `"job"`, `"major"`, `"university"`) Ã¢â‚¬â€ `route_stage()` returns `current_stage` directly as the routing key, eliminating a mapping step. Stage subgraphs compile without `checkpointer=` Ã¢â‚¬â€ parent `input_orchestrator` holds the `MemorySaver`, LangGraph propagates it down. `route_stage()` short-circuits to `context_compiler` on `escalation_pending` or `bypass_stage`. Edge: every stage node Ã¢â€ â€™ `context_compiler` Ã¢â€ â€™ `output_compiler` Ã¢â€ â€™ `END`.

**What broke:** Three pre-existing silent bugs discovered in `job_graph.py`, `major_graph.py`, `uni_graph.py`:
- `stage.get("current")` Ã¢â€ â€™ always `None` (key is `"current_stage"`). `is_current_stage` was permanently `False` Ã¢â‚¬â€ scoring nodes never knew they were the active stage.
- `stage_reasoning.university` Ã¢â€ â€™ `AttributeError` at runtime. Field is `stage_reasoning.uni`. Would have been invisible until the uni stage was reached.
- Unused `MemorySaver` import in `uni_graph.py`.

Import tests caught syntax errors. They did not catch wrong dict keys. Those only surface by reading the state schema.

**What I learned:** Silent `False` is worse than an exception. `is_current_stage = False` means the scoring node runs in a degraded mode with no error Ã¢â‚¬â€ it processes the message but without current-stage context. The bug would have produced subtly wrong outputs across every session, never throwing.

**Next:** Live end-to-end test run. Then: `retrieve_node` + `jobs.json` for data agent contracts.

---
