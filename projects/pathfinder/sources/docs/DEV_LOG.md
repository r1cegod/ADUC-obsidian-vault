# PathFinder — Dev Log

*Anh Duc — solo build, self-taught. FPT SE Scholarship portfolio.*

---

**2026-03-14**
- We mapped the full 8-agent topology. Gap was clear early: without bottom-up build order, the wiring becomes a tangled mess.
- Dialed in the coaching engine — forced official-doc-style patterns only. The gap between generic example and the user's codebase IS the skill transfer. He got it immediately.
- Connected LangGraph Studio local server to sidestep Docker headaches on Windows.
- Started `purpose_graph.py`. Hit the `.model_dump()` wall — Pydantic objects crash LangGraph TypedDict state without it. Learning moment: LangGraph state is TypedDict, not Pydantic. Every node must serialize before returning.
- Ran deep research protocols on LangGraph Evals and Bootstrapping.
- Architecture audit: redesigned Orchestrator with internal Chat Manager nodes, defined "Soft Boundaries" for agent handoffs, injected `ThinkingProfile` into graph state.
- Purged messy dict states. Built strict Pydantic models (`PurposeProfile`, `MajorProfile`, etc.) wired into `state.py`. He was ready to move fast here — no coaching needed.
- Fortified `purpose_graph.py` against the rigid schema via `langgraph dev` testing.

---

**2026-03-17**
- We wired token management into `purpose_graph.py` — `check_node` (pure Python tiktoken, 0.03s), conditional edge to `summarizer_node`, `RemoveMessage` to delete oldest 3/4 of message log.
- Learning moment: `add_messages` reducer has dual behavior — `BaseMessage` → append, `RemoveMessage(id=...)` → delete by ID. Survivors stay untouched because you never return them. He didn't know about the delete path until we traced the reducer.
- Caught silent wiring bug: `check_sum` was reading `state["limit_hit"]` but `check_node` set `state["purpose_limit"]` — summarizer permanently bypassed, no error thrown. Classic state key mismatch. Caught by reading the actual node return, not trusting the variable name.
- Fixed `purpose or ""` on all `.format()` calls — `str.format()` calls `str(None)` = literal `"None"` fed to the model. Subtle.
- Confirmed live in LangSmith: `input_token: 1341`, `purpose_limit: false`, routed to `confident` correctly. `check_node` ran in 0.03s.
- He asked why `add_conditional_edges` routing fn returns a string not a bool — because LangGraph uses it as a dict key lookup. Clicked once he saw the `path_map`.
- Upgraded `/coach` skill: doc-style per-concept teaching. Built `/updater` skill: syncs `.gitignore`, `requirements.txt`, `DEV_DIARY.md`.

---

**2026-03-18**
- We audited `INPUT_PARSER_PROMPT` against the 16-dimension production prompt doc. Found 6 gaps: no output JSON schema (router was parsing blind), no reasoning enforcement, no grounding rules for psych inference, no injection defense, no hallucination prevention for `core_tension`/`deflection_type`, no confidentiality block. Added all six to `orchestrator.py`.
- Hit a real conflict: added `<thinking>` block for CoT reasoning, then realized `with_structured_output` uses function-calling — model can't produce raw text before JSON. Fix: baked reasoning into the Pydantic schema itself (`deflection_reasoning`, `tension_reasoning` fields). He challenged the "top-to-bottom forcing" claim — good instinct. Honest answer: model sees full schema at once, benefit is auditability not mechanical sequencing.
- Architecture pivot he drove: split "LLM does everything" → "LLM classifies `stage_related`, Python handles routing." Designed `stage_manager` node with 4 cases: normal, rebound, contradict, forced. All routing is pure integer comparison on `STAGE_ORDER` — zero LLM tokens for routing decisions. Clean separation of semantics (LLM) vs logic (Python).
- Coached `Command` from `langgraph.types` — node returns `Command(update={...}, goto="node_name")`. Trap: never mix static `add_edge` and `Command` from the same node — both fire. He picked it up fast, no wiring needed.
- Rewrote `StageCheck` model: dropped LLM-managed fields, added Python-managed fields (`stage_related`, `rebound`, `contradict`, `forced_stage`, `stage_skipped`). `InputOutputStyle` now only asks LLM for classification, not routing.
- Thinking stage design: 3 ThinkingProfile fields are metacognitive — students can't self-report accurately. His plan: 16 Personalities + Gardner MI tests as priors, thinking agent validates via behavioral inference. Learning moment: he proposed the 3-tier watcher model then immediately optimized it down to "LLM tags, Python routes" — caught the token cost problem before I did.

---

**2026-03-20**
- Caught false-positive rebound: `has_rebound = bool(future)` alone fired on any broad message the LLM tagged multi-stage. Root cause: OR logic where AND was required. Fixed in `orchestrator_graph.py`: `has_rebound = bool(future) and stage.rebound` — index signal + LLM semantic gate must both agree before rebound fires.
- Second false positive: forced backward jumps (`"Let's go back to thinking"`) returned `rebound=True`. Prompt had no forced_stage carveout. Added rule to `orchestrator.py`: forced_stage set (any direction) → rebound=False always.
- Added stage content map to `INPUT_PARSER_PROMPT` — each stage now has a precise field list so LLM stops tagging "purpose" on broad statements like "tôi muốn tự do". Precision rule appended: default to `current_stage` for ambiguous messages.
- User initially resisted adding `<current_stage>` to the orchestrator prompt ("designed to not know current stage"). After LangSmith showed false positives were unfixable without it, reversed: orchestrator needs current stage to anchor the precision rule, not to route.
- `StageCheck` had no field defaults → `ValidationError` on stale checkpoints when `get_stage()` returned `{}`. Fixed in `state.py`: all six fields get defaults in the Pydantic model. Added `DEFAULT_STAGE` dict. Removed `stage_skipped` — no node writes it, dead weight.
- Learning moment: variable shadowing. User reused `stage` for both the `list[str]` slice and the `StageCheck` object in the same scope — the list was silently destroyed. No error, no warning. Named shadowing is silent data loss.

### Entry 002 — Day 15: 2026-03-29

**Goal:** Lock the path-agent removal and spec the knowledge/data agent taxonomy and data retrieval contract.

**Decision:** Fully deleted `PathProfile` from `state.py` and removed `path` + `path_limit` from `PathFinderState`. Path debate is now Case B2 in `build_compiler_prompt()` — a prompt injection block (`PATH_DEBATE_BLOCK`) triggered by a pure Python check: all 6 profiles `done=True`. Separately, formalized the agent split into **knowledge agents** (thinking, purpose, goals — extract from the student's head, no external data) and **data agents** (job, major, uni — match against real-world datasets). Designed agent-exclusive Pydantic query forms (`JobQuery`, `MajorQuery`, `UniQuery`) where each form's fields map directly to that agent's `*Profile` fields. `JobScoringOutput` combines FieldEntries + `JobQuery | None` + `need_data: bool` into one structured output call, avoiding a second LLM hop.

**Rejected alternative:** RAG (vector store + semantic search) for data agent retrieval. The full VN-focused dataset is ~100 entries across three categories — it fits in a few KB of JSON. Semantic search adds embedding costs, a vector store dependency, and nondeterministic results on short enum-like entries ("startup", "engineer"). Deterministic Python filter functions on JSON files (`filter(jobs, role_category="engineer")`) are faster, cheaper, and produce auditable results. RAG solves a scale problem that doesn't exist here.

**What broke:** `PathProfile` class and `path: PathProfile | None` / `path_limit: bool` removed from state. Any node that referenced these fields (none were wired yet) would now fail import. `ProfileSummary.path` slot also removed. `_compute_stage_status()` in `output.py` no longer includes a "path" entry in its `profile_map`.

**What I learned:** The gate question for "subgraph vs. compiler mode" is: does this stage introduce a **new query form exclusive to its domain**? Data agents are distinguished by having a typed retrieval contract (a Pydantic query form) that knowledge agents never need. The taxonomy isn't just a UX distinction — it's a structural one that changes node topology.

**Next:** Define `jobs.json` schema (~50 VN-relevant entries: role_category, company_stage, vn_salary range, required_skills, related_majors). Build `retrieve_node` as a pure Python filter. Spec `JobScoringOutput` as the dual-purpose scoring output (FieldEntries + retrieval query).

---

### Entry 003 — Day 15: 2026-03-29

**Goal:** Eliminate redundant LLM calls in stage subgraphs without losing response quality.

**Decision:** Removed `chatbot_node` and `summarizer_node` from all 6 stage subgraphs. Replaced with a single **analyst node** that writes a prose analysis to `stage_reasoning.{stage}`. The output compiler reads `stage_reasoning` via `PROFILE_CONTEXT_BLOCK` and generates the student-facing response itself — it is the sole response generator across all stages.

**Rejected alternative:** Keep the chatbot node, add a `stage_draft` state field, have the output compiler adapt the draft. Rejected because it adds a new top-level state field and a new `STAGE_DRAFT_BLOCK` in `output.py` for zero net gain — the output compiler already has `fields_needed` and `stage_status` from `_compute_stage_status()`.

**What broke:** Nothing at runtime — and that was the sign something was wrong. The chatbot nodes had been silently writing to `{stage}_message` queues while the output compiler reads from `messages` (global). Two LLM calls per turn, only one doing visible work. No error, no warning.

**What I learned:** Trace information flow, not just code flow. The bug wasn't in the node logic — it was in the channel. `{stage}_message` is a routing queue for stage agents to read context; it is not a response channel. The output compiler reads `messages` (global). These are two different channels.

**Next:** Build remaining stage agents using the 2-node pattern (scoring + analyst). Wire all into the master orchestrator.

---

### Entry 004 — Day 16: 2026-03-30

**Goal:** Guarantee stage agents retain full domain memory even after the global summarizer compresses the conversation.

**Decision:** Split memory into two permanent layers. (1) The global `SUMMARIZER_PROMPT` is narrowed to track only macro psychology, compliance, and routing events — not stage content. (2) A deterministic **Python Tagger** is added to `input_parser`: it reads `response.stage_related` from the LLM and instantly copies the raw `HumanMessage` to every matching `{stage}_message` queue. Result: `job_message` is an untruncated vault of every message the student sent that touched the job domain. Separately, wired **contradict tagger** into `stage_manager`: when `contradict_target` is set, the current message is additionally tagged to all past-stage queues, and `context_compiler` assembles prompts from `list(dict.fromkeys(stage_related + contradict_target))` (union, order-preserved).

**Rejected alternative:** Let stage agents read global `messages`. Rejected because the summarizer runs at 2000 tokens — within 30 minutes of a real session, stage agents would lose the student's exact early answers. Let the summarizer track stage data — rejected because it requires the summarizer to understand domain-specific fields without hallucinating them.

**What broke:** Nothing at code level. The `context_stages` union exposes that `contradict_target ⊆ stage_related` is currently always true — but that's an assumption that could break if `stage_related` filtering logic changes. Making the union explicit is forward-proof.

**What I learned:** The summarizer compresses exactly what stage agents need most. Routing memory (behavioral patterns) degrades gracefully. Domain memory (what the student actually said) cannot degrade. Two channels, two decay profiles, two memory strategies.

**Next:** Wire all 6 stage subgraphs into the master orchestrator.

---

### Entry 005 — Day 17: 2026-03-31

**Goal:** Full end-to-end pipeline wired. One graph from student input to response.

**Decision:** Compiled all 6 stage subgraphs as nodes in the master `StateGraph`. Node names match `current_stage` string values exactly (`"thinking"`, `"purpose"`, `"goals"`, `"job"`, `"major"`, `"university"`) — `route_stage()` returns `current_stage` directly as the routing key, eliminating a mapping step. Stage subgraphs compile without `checkpointer=` — parent `input_orchestrator` holds the `MemorySaver`, LangGraph propagates it down. `route_stage()` short-circuits to `context_compiler` on `escalation_pending` or `bypass_stage`. Edge: every stage node → `context_compiler` → `output_compiler` → `END`.

**What broke:** Three pre-existing silent bugs discovered in `job_graph.py`, `major_graph.py`, `uni_graph.py`:
- `stage.get("current")` → always `None` (key is `"current_stage"`). `is_current_stage` was permanently `False` — scoring nodes never knew they were the active stage.
- `stage_reasoning.university` → `AttributeError` at runtime. Field is `stage_reasoning.uni`. Would have been invisible until the uni stage was reached.
- Unused `MemorySaver` import in `uni_graph.py`.

Import tests caught syntax errors. They did not catch wrong dict keys. Those only surface by reading the state schema.

**What I learned:** Silent `False` is worse than an exception. `is_current_stage = False` means the scoring node runs in a degraded mode with no error — it processes the message but without current-stage context. The bug would have produced subtly wrong outputs across every session, never throwing.

**Next:** Live end-to-end test run. Then: `retrieve_node` + `jobs.json` for data agent contracts.

---

### Entry 006 - 2026-04-02

**Goal:** Make repo instructions point to the actual docs context system and require agents to keep it updated.

**Decision:** Updated `AGENTS.md` so the first stop for repo context is `docs/context/docs/PROJECT_CONTEXT.md`, then `docs/context/docs/CURRENT_CONTEXT.md`, with `docs/context/how to/context_maintenance.md` as the maintenance workflow. Added an explicit "Critical Development Rules" section and made context updates part of done, not optional follow-up.

**What changed:** `AGENTS.md` now points to the canonical docs tree, defines auto-update rules for `CURRENT_CONTEXT.md`, `PROJECT_CONTEXT.md`, and `docs/DEV_LOG.md`, and calls out guardrails like Python-owned control flow, Path as Output Compiler Case B2, and the state contract update rule. `PROJECT_CONTEXT.md` now also links to the context maintenance guide.

**Why it matters:** The repo already had the right context files, but the top-level agent instructions did not force agents to read or maintain them. That gap makes context drift likely after session compaction or multi-step doc changes.

---

### Entry 007 - 2026-04-02

**Goal:** Tighten the live `PathFinderState` contract and stop the output compiler from misreading nested profiles.

**Decision:** Removed dead state fields that no live node reads or writes (`terminate`, per-stage `*_limit`, `input_token`) from `backend/data/state.py` and the canonical architecture docs. Rewrote `_compute_stage_status()` in `backend/data/prompts/output.py` to recurse through nested models and dicts instead of assuming every top-level field is a direct `FieldEntry`. Added `test_output_prompt_contract.py` to lock the helper behavior for `GoalsProfile`, scalar leaves like `UniProfile.is_domestic`, and the dead-field cleanup.

**What broke:** `GoalsProfile` was a wrapper profile (`long` + `short`), but the helper treated those wrappers as leaf fields, so fully-populated goals still showed `not started`. `UniProfile.is_domestic` is a required boolean, but the helper treated every non-`FieldEntry` leaf as missing, so university progress was also undercounted.

**What I learned:** State helpers are part of the contract surface, not convenience glue. A stale helper can poison prompt assembly just as badly as a bad router because the compiler is the only student-facing response node.

---

### Entry 008 - 2026-04-02

**Goal:** Extract the repeated stage-name and state-key mappings into one reusable contract.

**Decision:** Added `backend/data/contracts/stages.py` as the single source of truth for `STAGE_ORDER`, `STAGE_INDEX`, `STAGE_TO_PROFILE_KEY`, `STAGE_TO_REASONING_KEY`, and `STAGE_TO_QUEUE_KEY`. Wired the contract into `backend/orchestrator_graph.py` for queue tagging, stage-order checks, and route validation, and into `backend/data/prompts/output.py` for profile lookup and reasoning synthesis. Added `test_stage_contract.py` to lock completeness and uniqueness of the mapping.

**What broke before:** The same stage knowledge existed in multiple places with slightly different shapes. That made bugs like `university` vs `uni` or `thinking` vs `thinking_style_message` too easy to create because every file was free to invent its own mapping.

**What I learned:** A contract module is not abstraction for its own sake. It is a pressure valve for string drift. When a concept is reused across routing, state access, and prompt assembly, the cheapest safe move is to name it once and import it everywhere.

**Follow-through:** Migrated all six stage graphs to the contract pattern as well, not just the orchestrator and output helper layer. `thinking_graph.py` served as the manual learning pass, then the same `STAGE / PROFILE_KEY / QUEUE_KEY / REASONING_KEY` pattern was applied to `purpose`, `goals`, `job`, `major`, and `uni`. Validation passed via unit tests, graph imports, and a grep sweep for leftover hardcoded graph key lookups.

**Second follow-through:** Removed redundant `MemorySaver` ownership from all stage subgraphs and from `output_graph.py`; only the root orchestrator keeps the checkpointer now. Also fixed a real output tagging bug: `output_compiler` was appending a new AI response to `messages` but tagging `state["messages"][-1]`, which still pointed at the previous turn's human message. The node now tags the newly created `AIMessage` into the union of `stage_related + contradict_target`, and `test_output_graph_contract.py` locks that behavior.

---

### Entry 009 - 2026-04-03

**Goal:** Define a stable evaluation method for the web-enabled data agents (`job`, `major`, `uni`).

**Decision:** Formalized data-agent evaluation as a **retrieval-plus-reasoning** problem, not a normal stage-agent prompt audit. Added `docs/evaluation/data_agent_evaluation.md` as the canonical guide. The evaluation seam now includes six checks: search-trigger correctness, query quality, evidence grounding, consensus-crash quality, confidence calibration, and tool discipline. Also locked the recommended test stack into three layers: deterministic replay suite as primary, adversarial retrieval suite for noisy/frozen evidence, and live-search smoke runs only for drift detection.

**Why this matters:** The current stage audit pattern was built for knowledge agents. Data agents can fail before reasoning quality even matters: they may skip a required search, formulate the wrong VN query, or ignore the returned evidence while still writing plausible prose. Treating them like normal stage agents hides the real failure mode.

**Constraint surfaced:** `eval/run_eval.py` already replays input state and writes traces, but it does not yet inject mocked tool responses. That means the repo can run live-search attack datasets today, but a fully deterministic replay harness still requires a mockable search seam.

**Next:** Use the new guide to build the first dedicated audit doc and attack dataset for one retrieval stage, preferably `job`, then decide whether to extend the eval runner with frozen tool fixtures.

---

### Entry 010 - 2026-04-05

**Goal:** Evaluate and harden the Stage 2 `goals` agent against the existing attack dataset.

**Decision:** Tightened the `goals` extractor and analyst contracts, then re-ran `eval/goals_attack.jsonl` until all three attacks passed. The extractor now has explicit rules for `TITLE IS NOT DEFENSE`, `NUMBERS OR IT IS UNCLEAR`, `GENERIC SOFT-SKILL BAN`, and `HORIZON GAP PENALTY`. The analyst now explicitly treats `gov stability` vs `freelance/founder` as a structural crash and must embed that contradiction directly into the final `PROBE:` anchor.

**What changed:** Added a clean prompt module at `backend/data/prompts/goals_v2.py` and rewired `backend/goals_graph.py` to import it. Recorded the passing trace results in `docs/evaluation/goals_evaluation.md`. The verified eval command was `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals`.

**What broke before:** The old Stage 2 prompt let self-reported `founder`, `freelance`, `full autonomy`, and `soft skills` claims climb far above the intended verification ceiling. It also let the analyst note prior crashes in prose without always weaponizing them in the final `PROBE:` string.

**What I learned:** For the goals stage, horizon mismatch is a calibration signal, not just analyst commentary. If the student names a bold 5-year identity with no 1-year artifact, that missing bridge must suppress extractor confidence and sharpen the analyst handoff at the same time.

**Follow-up:** Consolidated the clean prompt back into `backend/data/prompts/goals.py` and deleted `goals_v2.py`. The next real gap is coverage, not path layout: the current Stage 2 suite still needs more Vietnamese-student edge cases before it can be called production-grade.

**Second follow-up:** Expanded `eval/goals_attack.jsonl` to 8 attacks and re-ran the suite. New cases covered Vietnamese-student-specific realities: Da Lat lifestyle fantasy, parent-pleasing civil-service compliance, debt-driven salary pressure, founder-to-solo contradiction, and safe-path drift. The goals agent passed all 8. This is enough to call Stage 2 strongly hardened at the stage-agent level, but still not enough to call the full production path hardened without orchestrator/output end-to-end evals.

**Third follow-up:** Closed the last Stage 2 contract gap in `backend/goals_graph.py`. The analyst no longer returns a single free-text blob. It now returns `goals_summary`, `probe_field`, and `probe_instruction`, and Python composes the final `PROBE:` line with a deterministic fallback if the model under-specifies it. Re-ran the previously failing last attack in isolation plus a 3-run stability replay; all runs now preserved a trailing `PROBE:` anchor in `stage_reasoning.goals`.

---

### Entry 011 — Day 23: 2026-04-05

**Goal:** Audit and close the remaining demo-critical gaps before the scholarship submission: RIASEC/MI seeding, completedStages coverage, post-escalation behavior, and vague counter parity.

**Decision:** Moved the post-escalation lock entirely to `main.py`'s `chat_stream`. Before calling `astream_events`, the endpoint calls `aget_state(config)` and checks `escalation_pending`. If True, it streams the hardcoded Vietnamese response directly as a token event and returns — zero graph nodes run, zero LLM calls. The `/test/{session_id}` endpoint was fixed to call `aupdate_state(config, {"thinking": merged})` against the LangGraph checkpointer instead of only yielding a client-side SSE event. `vague_turns` gained a direct consecutive escalation cap at >= 4 in `counter_manager`, matching the disengagement and avoidance pattern.

**Rejected alternative:** Two alternatives were tried and discarded. First: a `locked_response_node` inside `orchestrator_graph`. That node returns a direct `AIMessage` without touching `output_compiler`, so no `on_chat_model_stream` events fire — the frontend would show the user's message with no reply. Second: a frontend guard in `App.jsx handleSend` that short-circuits before the API call. That guard works for UX but duplicates the lock logic on the client, creating two sources of truth for what constitutes a locked session.

**What broke:** `/test/{session_id}` had `# noqa: ARG001` on its `session_id` parameter — the tell that it was intentionally unused. The endpoint was streaming a synthetic `{"type": "state"}` SSE event to React `useState` only. The LangGraph `MemorySaver` checkpointer had never received `brain_type` or `riasec_top`, so `thinking_graph`'s scoring node was reading `None` for both fields on every session.

**What I learned:** The token-stream boundary is a coupling point between the graph and the UI. Any response path that bypasses the LLM output node (`output_compiler`) produces no `on_chat_model_stream` events — only `on_chain_end` state updates, which don't populate the chat window. The lock must be placed upstream of `astream_events()`, not inside the graph, to guarantee both zero cost and a visible response.

**Next:** Knowledge gap drilling — five architectural decisions that must be defensible verbally before the scholarship interview: counter decay, reasoning lock, stage queue tagger, 10-turn window vs. direct escalation, and B2 gate conditions.

---

### Entry 012 - 2026-04-05

**Goal:** Reevaluate the Stage 0 `thinking` agent against the newer S4 stage-prompt rules instead of trusting the earlier S3 audit label.

**Decision:** Hardened `backend/data/prompts/thinking.py` with three explicit extractor rules: `PRIOR AGREEMENT IS NOT DEFENSE`, `DETAIL IS NOT DEFENSE`, and the required `Student Claim -> Agent Squeeze -> Student Defense` verification sequence before any conversational field can exceed `0.7`. Also added explicit analyst-side `TENSION EMBEDDING` language so the final `PROBE:` anchor starts with the actual prior-vs-claim conflict instead of a generic "test it" handoff.

**What broke before:** The replay of `eval/thinking_attack_v2.jsonl` exposed a real cap violation. In the "Abstract Intellectual" case, Nova promoted `learning_mode="theoretical"` to `0.74` from a polished self-report that merely matched the quiz priors. That is exactly the failure the S4 verification loop is supposed to block.

**What I learned:** Prior alignment is calibration context, not proof. If a student says something that sounds smart and it happens to match the test, the model gets seduced into calling it "verified" unless the prompt says, in plain language, that alignment is still just a self-report until the student survives a forced trade-off.

**Verification:** Re-ran both Stage 0 attack suites after the patch:
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack_v2.jsonl --graph thinking`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack.jsonl --graph thinking`

**Next:** Either add a longer multi-turn contradiction dataset for Thinking, or move up one layer and test whether the orchestrator/output path preserves the stronger Stage 0 `PROBE:` tension end-to-end.

---

### Entry 014 - 2026-04-05

**Goal:** Reevaluate the Stage 1 `purpose` agent against the same S4 prompt-audit standard now used for Thinking and Goals.

**Decision:** Hardened Stage 1 at both the prompt and graph layer. `backend/purpose_graph.py` no longer trusts the analyst to emit the final probe line consistently. The analyst now returns structured fields (`purpose_summary`, `probe_field`, `probe_tension`, `probe_instruction`), and Python composes the final trailing `PROBE:` line with deterministic fallbacks. The analyst prompt now receives `user_tag` explicitly, and the extractor prompt gained hard rules for stepping-stone destination blocking, calling-vs-FIRE contradiction drops, contradiction priority, and a digital-nomad location-fantasy cap.

**What broke before:** The fresh replay of `eval/purpose_attack.jsonl` exposed two real regressions. First, multiple traces omitted the required `PROBE:` anchor entirely even though the stage_prompt contract requires it every turn. Second, the FIRE case let `work_relationship="calling"` survive the explicit "retire completely at 35" contradiction, which is exactly the deadlock the Stage 1 rules are supposed to crush.

**What I learned:** For Stage 1, a pure prompt-only contract was not enough. The analyst can still reason correctly and then forget the output anchor, so the handoff itself needs a Python safety rail. Also, contradiction text must be first-class structured data (`probe_tension`) rather than something we hope survives inside a free-text summary.

**Verification:** Re-ran `venv\Scripts\python eval/run_eval.py --mode multi --file eval/purpose_attack.jsonl --graph purpose` until all 7 attacks held the intended caps and every trace ended with a contradiction-rich `PROBE:` line. Also re-verified import health with `venv\Scripts\python -c "from backend.purpose_graph import purpose_graph; print('OK')"`.

**Next:** The remaining question is no longer Stage 1 prompt integrity. It is whether the orchestrator/output path preserves the stronger Stage 1 handoff end-to-end in student-facing Vietnamese responses.

---

### Entry 013 - 2026-04-05

**Goal:** Run the first dedicated retrieval-agent audit on Stage 3 `job` using the data-agent evaluation workflow.

**Decision:** Built `eval/job_attack.jsonl` and `docs/evaluation/job_evaluation.md` as the first `job`-specific audit pair, then hardened `backend/data/prompts/job.py` around the failures exposed by the live traces. The extractor no longer asks for a nonexistent `key_quote`, and now enforces `SINGLE-TURN SELF-REPORT CAP`, stronger `DAY-TO-DAY FIRST`, `AUTONOMY DEPENDS ON GRIND`, and `CONTRADICTION DROP` rules. The analyst now has explicit tool-discipline, Vietnam-query, and tension-embedding rules.

**What broke:** The prompt layer improved, but the audit exposed a deeper graph seam: after tool use, `job_agent` still intermittently leaves `stage_reasoning.job` blank. In the latest live suite, search triggers and confidence ceilings mostly behaved, but only 1 of 4 attacks reliably handed a usable `PROBE:` to the output compiler. This is not a prompt-quality failure anymore; it is a post-tool synthesis reliability problem in the current data-agent graph shape.

**What I learned:** Retrieval agents need a more explicit synthesis seam than normal stage agents. Search-trigger logic and extractor caps can be correct while the actual analyst handoff still collapses. For `job`, the next fix should target graph architecture or deterministic fallback behavior after the tool loop, not more prompt wording alone.

**Next:** Add a reliable post-tool synthesis step for `job`, then decide whether the same seam should be generalized across `major` and `uni` before calling any retrieval stage production-ready.

---

### Entry 014 - 2026-04-05

**Goal:** Clean up the retrieval-stage source layer before adding a dedicated research seam.

**Decision:** Repaired the mojibake in `docs/prompt/docs/stage_prompt.md`, added `backend/data/contracts/research_sources.py` as the first reusable domain/source seed contract, and documented source priorities plus Reddit options in `docs/evaluation/research_sources.md`. Also tightened `backend/tools.py` guidance so retrieval queries stay narrow and contradiction-focused rather than collapsing into one giant request.

**What broke before:** The repo had two separate issues mixed together. First, `stage_prompt.md` had real mojibake in source, not just terminal display noise. Second, Serper behaved badly when asked a broad “research request” query that mixed salary, remote, stakeholder load, and company stage into one search. The result quality improved only when the query was decomposed into narrow factual slices and, in some cases, site filters.

**What I learned:** Source strategy is part of the architecture. A future research node should not start from a blank search box. It needs a curated domain list, query decomposition rules, and explicit treatment of Reddit as supplementary evidence. Reddit's current Data API wiki says OAuth is required and warns that some legacy API documentation is out of date, so the safe short-term move is Serper discovery via `site:reddit.com`, not treating Reddit snippets as primary evidence.

**Next:** Use the new source contract in a dedicated `job` research planner / synthesis path, then decide whether the same source-selection logic should be shared across `major` and `uni`.

## Entry 032 - 2026-04-05
**Goal:** Replace the brittle Stage 3 direct search loop with a working research draft and replay the `job` attack suite.

**Decision:** Stage 3 `job` now uses a dedicated planner/researcher/synthesizer seam backed by OpenAI web search. The graph writes a structured `job_research` packet into shared state, then the synthesizer writes the final `stage_reasoning.job` from that packet instead of trying to synthesize inside the same node that calls tools.

**What changed:**
- Added `JobResearch` and `job_research` to shared state.
- Rewrote `backend/job_graph.py` around `confident_node -> job_research_planner -> job_researcher -> job_synthesizer`.
- Rewrote `backend/data/prompts/job.py` so planning, retrieval, and synthesis are separate prompt responsibilities.
- Replayed `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job`.

**Result:** The draft works materially better than the old Serper-style loop. All 4 attacks completed, each produced a populated research packet, and each preserved a non-empty `stage_reasoning.job` with a trailing `PROBE:`. The main remaining weakness is evidence noise, not handoff collapse.

**Residual issues:** OpenAI web search still returns some irrelevant or weak URLs in `cited_sources`, and eval traces emit Pydantic serializer warnings around structured outputs. Those do not block the draft, but they should be cleaned up before copying the pattern into more stages.

**Next:** Add lightweight source pruning or evidence compression, then decide whether to generalize the same planner/researcher/synthesizer architecture into `major` or `uni`.

## Entry 033 - 2026-04-06
**Goal:** Collapse the evaluation workflow into one official pipeline document before more audit work lands.

**Decision:** `eval/HOW_TO_USE.md` is now the single source of truth for the evaluation pipeline. It owns the production-first workflow, the runner usage, the required context docs, the trace-audit loop, and the new rule that meaningful behavior changes must be surfaced to the user for opinion before they are treated as final production direction.

**What changed:**
- Rewrote `eval/HOW_TO_USE.md` from a runner-only note into the full evaluation workflow.
- Removed duplicated workflow steps from `docs/prompt/docs/stage_prompt.md` and replaced them with a pointer.
- Updated `docs/evaluation/stage_evaluation.md` and `docs/evaluation/data_agent_evaluation.md` to treat `eval/HOW_TO_USE.md` as the official process doc.
- Updated `docs/context/docs/PROJECT_CONTEXT.md` and `docs/context/docs/CURRENT_CONTEXT.md` so the new source-of-truth location is discoverable at the start of work.

**Why this matters:** The repo previously split the process across two files: `stage_prompt.md` described the workflow while `eval/HOW_TO_USE.md` only described the CLI. That made it too easy to skip production planning and too easy for future docs to drift.

**New workflow rules locked:**
- evaluation work must start by planning for production behavior before writing datasets
- evaluation logs are created or updated before JSONL authoring
- meaningful student-facing behavior changes must be discussed with the user and their opinion requested before the behavior is treated as final production direction

**Next:** Use the new pipeline on the next real stage audit and tighten it only if a practical gap shows up in execution.

## Entry 034 - 2026-04-06
**Goal:** Tighten the newly centralized evaluation workflow so production signoff happens in explicit rounds instead of an open-ended hardening loop.

**Decision:** The official evaluation pipeline now uses a hard **3-round gate** before a stage can be called production-ready.

**Rules locked:**
- every evaluation plan is capped at 3 rounds total
- each evaluation run may finish exactly 1 stage only
- after each run, the updated evaluation log must be handed to the user
- after each run, a user conversation must happen before the next round starts
- production-ready status requires all 3 rounds to be completed for that stage

**Why this matters:** Without a round cap and a forced handoff point, evaluation work tends to drift into large bundled passes that hide behavior shifts and skip user review between hardening steps.

**What changed:** Updated `eval/HOW_TO_USE.md` to encode the 3-round gate in the workflow, planning rules, close-the-loop step, and completion criteria. Refreshed `docs/context/docs/CURRENT_CONTEXT.md` to reflect the new cadence.

**Next:** Apply the 3-round gate on the next real stage evaluation and keep it unless execution reveals a concrete failure mode in the process itself.

---

### Entry 014 - 2026-04-05

**Goal:** Eliminate the Stage 3 `job` graph failure where analyst reasoning disappeared after tool use, and align its probe handoff with the newer Purpose/Goals pattern before orchestrator/output evaluation.

**Decision:** Split the old single `job_agent` seam into two roles inside `backend/job_graph.py`: a tool-planning node that only decides search calls, and a non-tool `job_synthesizer` node that always produces structured analyst output (`job_summary`, `probe_field`, `probe_tension`, `probe_instruction`). Python now deterministically composes the final `PROBE:` line from those fields, exactly like the newer Stage 1 and Stage 2 flows.

**What broke before:** The retrieval logic and extraction quality were often acceptable, but after tool use the stage could still end with blank `stage_reasoning.job`. That meant the output compiler would receive no actual Socratic handoff even when the search found useful market contradictions.

**What I learned:** Retrieval stages need a harder seam than prompt-only obedience. A tool planner and a synthesis writer are different jobs. When one node tries to do both, the search loop can succeed while the final reasoning silently collapses. The fix was architectural, not rhetorical.

**Verification:** 
- `venv\Scripts\python -c "from backend.job_graph import job_graph; print('OK')"`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job`

**Result:** all 4 Job attacks now preserve non-empty `stage_reasoning.job` with a trailing `PROBE:` line after tool use.

**Next:** Decide whether to run orchestrator/output end-to-end evaluation now that Stages 0-3 have stronger handoff contracts, or continue stage-local hardening on the remaining later stages first.

---

### Entry 015 - 2026-04-05

**Goal:** Close the last Stage 0 calibration leak before orchestrator/output wiring tests.

**Decision:** Kept the new structured analyst handoff in `backend/thinking_graph.py`, but added a deterministic Python verification clamp inside the Thinking scoring node. If `thinking_style_message` contains fewer than 2 human turns, no conversational Thinking field (`learning_mode`, `env_constraint`, `social_battery`, `personality_type`) may exceed `0.6`, and `done` is recomputed after the clamp. Also tightened the extractor prompt with `FORCED-CHOICE CONFESSION IS STILL SELF-REPORT` and `SCENE DETAIL IS NOT ENV CONSTRAINT`.

**What broke before:** The prompt-only hardening was not enough. In the legacy "dark room" replay, a single forced-choice answer still produced absurdly strong extractor outputs like `social_battery="solo" 0.96` and `env_constraint="home" 0.92`, even though the conversation had not yet completed the required claim -> squeeze -> defense loop.

**What I learned:** For Stage 0, the verification threshold is structural, not rhetorical. If high confidence depends on turn count, Python must own that rule inside the scoring node. Prompt wording can guide the model, but it should not be the sole gate for a hard confidence ceiling.

**Verification:**
- `venv\Scripts\python -c "from backend.thinking_graph import thinking_graph; print('OK')"`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack_v2.jsonl --graph thinking`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack.jsonl --graph thinking`

**Result:** both Thinking suites still pass, every trace still ends with a trailing `PROBE:`, and the old single-turn overconfidence leak is gone in the fresh replay.

**Next:** Use the strongest Stage 0-3 attacks for orchestrator/output end-to-end evaluation and inspect whether the student-facing Vietnamese output preserves the stronger stage-local handoffs.

---

### Entry 016 - 2026-04-06

**Goal:** Retire the repo `docs/` folder as the live documentation source and make the PathFinder vault the official documentation home.

**Decision:** The canonical PathFinder docs now live in the Obsidian vault under `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\`. The repo copy at `D:\ANHDUC\Path_finder\docs\` is archive-only. Repo instruction files now point to the vault first, while the project README and hub layer route agents into the correct canonical files.

**What changed:** Updated repo `AGENTS.md`, `CLAUDE.md`, `README.md`, and `eval/HOW_TO_USE.md` to treat the vault as canonical. Added archive notices to the main repo context files and created `docs/ARCHIVE_NOTICE.md`. Updated the vault copies of `PROJECT_CONTEXT.md`, `CURRENT_CONTEXT.md`, `context_maintenance.md`, and the PathFinder README so the canonical side agrees with the new contract.

**What I learned:** A routing layer naturally becomes the documentation home once it accumulates the canonical raw files, strong hubs, and the maintenance habit. At that point keeping repo `docs/` "also canonical" is not redundancy, it is drift risk.

**Next:** Validate the vault-first read path during the next real coding task and only add more synchronization or freezing machinery if the archive still causes confusion.

---

### Entry 016 - 2026-04-06

**Goal:** Align the repo's agent instructions with the new mirrored Obsidian PathFinder workspace so future sessions can use the vault as a low-token routing layer without confusing it for the source of truth.

**Decision:** Updated `AGENTS.md` and the context docs to acknowledge the vault mirror at `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\`, but locked a strict boundary: the vault is for routing and synthesis, while the repo `docs/` tree remains canonical for operational contracts. The reading pattern is now: repo context docs first, optional vault README/domain hub for faster navigation, then back to repo docs for exact contract checks.

**What changed:** Added a dedicated `Vault Routing Layer` section to `AGENTS.md`, added the vault mirror and navigation pattern to `docs/context/docs/PROJECT_CONTEXT.md`, and refreshed `docs/context/docs/CURRENT_CONTEXT.md` so the active workstream and handoff reflect the new repo-vs-vault convention.

**What I learned:** A strong external knowledge layer becomes risky the moment it stops being clearly subordinate to the repo's canonical docs. The useful pattern is not "replace repo docs with vault notes"; it is "use the vault to route faster, then verify against the repo where exact wording matters."

**Next:** Validate the repo-plus-vault read path on the next real coding task and only add more synchronization machinery if router-level maintenance proves insufficient.

---

### Entry 017 - 2026-04-06

**Goal:** Remove duplicated navigation logic from the repo bootstrap files after the docs-to-vault transition.

**Decision:** Simplified repo `AGENTS.md` and `CLAUDE.md` into thin bootstrap files. They now only state that repo `docs/` is archived, point to the vault as canonical, and direct readers into the vault entry docs instead of recreating the vault routing tree inside the repo.

**What changed:** Rewrote both repo bootstrap files so they no longer duplicate the project routing pattern already defined in the vault. Kept only a minimal repo-local note block plus the hard rule that live documentation belongs in the vault.

**What I learned:** Once a canonical navigation system exists, duplicating that routing tree in a secondary bootstrap file recreates the same drift surface under a different name. The clean bootstrap is a redirect, not a second router.

**Next:** Watch whether `README.md` should also be thinned later, or whether it still serves a distinct project-facing purpose.

---

### Entry 018 - 2026-04-07

**Goal:** Lock the `DEV_LOG.md` synchronization rule after moving canonical docs into the vault.

**Decision:** `projects/pathfinder/sources/docs/DEV_LOG.md` remains the canonical dev log, but `D:\ANHDUC\Path_finder\docs (archived)\DEV_LOG.md` is a required mirror. Every new durable decision entry must be appended to both files in the same change.

**What changed:** Updated the canonical project context docs and maintenance rules to name the mirror exception explicitly, corrected stale repo archive paths to `docs (archived)\`, and updated the repo entry files so future sessions see the rule before touching docs.

**What I learned:** "Archive-only" is too broad when one file is still intentionally mirrored. If the exception is not written down, drift is not an accident; it is the default outcome.

**Next:** Keep both dev-log copies aligned on every future durable documentation or architecture decision.

