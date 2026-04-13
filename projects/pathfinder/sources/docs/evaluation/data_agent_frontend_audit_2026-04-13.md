# Data-Agent Frontend Audit - 2026-04-13

> Live worker audit for `university-finding-business-ux-20260413`. This document summarizes trace evidence so later data-agent evaluators do not need to open every raw trace.

## Run Metadata

| Field | Value |
|---|---|
| Session | `university-finding-business-ux-20260413` |
| Mission | Frontend student session, grounded student seeking a Vietnam university route for Product / UX / Business |
| Data stages audited | Job, Major, University |
| R1 trace folder | `eval/threads/university-finding-business-ux-20260413/traces/` |
| R2 trace folder | `eval/threads/university-finding-business-ux-20260413-r2/traces/` |
| R1 audit coverage | `live_0001.json` through `live_0012.json` |
| R2 audit coverage | `live_0001.json` through `live_0003.json` |
| Status at last inspected trace | R1 stopped in Major soft lock; R2 still in `major`; University not reached |

## Trace List

| Trace | Stage | Status |
|---|---|---|
| `live_0001.json` | Job | Started from university-finding request; no concrete role yet |
| `live_0002.json` | Job | Role/company/day-to-day extracted; Job research triggered |
| `live_0003.json` | Job | Same Job query repeated for user-facing ratio |
| `live_0004.json` | Job | Same Job query repeated again; confidence rose |
| `live_0005.json` | Major | Job marked done; transition to Major |
| `live_0006.json` | Major | Business Administration inferred; Major search returned no results |
| `live_0007.json` | Major | Business Administration query returned no results again |
| `live_0008.json` | Major | Student asked direct BA/MIS/Digital Business/Marketing Analytics comparison; agent asked which one to check first |
| `live_0009.json` | Major | Digital Business query returned no results |
| `live_0010.json` | Major | Student again asked direct comparison; agent still asked for a priority direction |
| `live_0011.json` | Major | MIS query returned no results |
| `live_0012.json` | Major | Student asked for temporary MIS conclusion; agent asked how to check MIS first |

## R2 Post-Patch Trace List

| Trace | Stage | Status |
|---|---|---|
| `university-finding-business-ux-20260413-r2/live_0001.json` | Major | Patch improved prose: assistant gives provisional MIS priority, but raw Major state still says Business Administration and research is a no-result Digital Business query. |
| `university-finding-business-ux-20260413-r2/live_0002.json` | Major | Student asks to move to concrete schools; assistant asks for one school first instead of entering University; raw stage stays Major. |
| `university-finding-business-ux-20260413-r2/live_0003.json` | Major | Student names UEH; assistant still asks whether to inspect UEH by artifact or Product BA/UX signals; research query is generic MIS Vietnam and returns NEU/VNU results, not UEH-specific evidence. |

## Per-Turn Compact Table

| Turn | Stage | Assistant Move | Raw Stage State | Research Packet Summary |
|---|---|---|---|---|
| 1 | Job | Reframed "which university" into "which work environment"; asked UX research / product coordination / BA / prototype / mixed product choice. | `job.done=false`; all Job fields `unclear(0.1)`. | `job_research.need_research=false`; no query. This is acceptable because no concrete role/company-stage claim was committed yet. |
| 2 | Job | Tested whether startup/small-team mixed product work would contain enough user-facing work or drift into coordination. | `role_category=product coordination / UX research / business analysis(0.62)`; `company_stage=small product team/startup(0.74)`; `day_to_day=...(0.77)`; `autonomy_level=...(0.68)`. | `need_research=true`; query: `công việc product coordinator UX research business analyst ở startup Việt Nam hàng ngày làm gì`; 5 sources, many TopCV extraction blocks / 403s. |
| 3 | Job | Asked whether 30-40% user-facing is acceptable or whether the student needs a higher ratio. | Job state unchanged from turn 2. | Same query repeated; `focus=day_to_day user-facing ratio`; 5 sources; blocked/403 evidence again. |
| 4 | Job | Asked whether the student would prefer JD/interview evidence of user research/discovery over vague "product" jobs. | Job confidence rose: `role_category(0.75)`, `company_stage(0.78)`, `day_to_day(0.8)`, `autonomy_level(0.7)`. | Same query repeated again; 5 sources; blocked/403 evidence again. |
| 5 | Major | Job handoff; asked whether student leans Product/BA/UX research with users or Product Ops/coordinating with less user contact. | `job.done=true`; Job confidences high: `role_category(0.82)`, `company_stage(0.86)`, `day_to_day(0.91)`, `autonomy_level(0.84)`; `major=null`. | Job research packet still carries repeated blocked TopCV evidence. No Major research yet. |
| 6 | Major | Proposed Business Administration as closest candidate and asked whether student accepts it only if project-based. | `major.done=false`; `field=Business Administration(0.38)`; curriculum and coverage low/unclear. | `major_research.need_research=true`; query asks broad "which major in Vietnam..." with UX/BA/project terms; `sources=0`; `research_complete=true`. |
| 7 | Major | Noted Business Administration only acceptable with artifacts; asked whether to compare BA with MIS/Digital Business/Marketing Analytics. | `field=Business Administration(0.58)`; `curriculum_style=project-based execution(0.74)`; `required_skills_coverage(0.46)`. | New BA-only query; `sources=0`; `research_complete=true`. |
| 8 | Major | Student asked direct four-way comparison; assistant asked which one to check first instead of comparing. | Major state mostly unchanged; `required_skills_coverage(0.56)`. | Reused BA-only no-result query despite student asking BA vs MIS vs Digital Business vs Marketing Analytics. |
| 9 | Major | Student selected Digital Business first but requested later comparison; assistant asked whether to check Digital Business then compare. | `field` stayed Business Administration(0.58), not Digital Business. | Digital Business query; `sources=0`; `research_complete=true`. |
| 10 | Major | Student asked to compare three paths directly and choose quickly; assistant still asked which direction to prioritize. | Major state still anchored to Business Administration(0.58). | Reused Digital Business no-result query; no comparison query; no cited sources. |
| 11 | Major | Student selected MIS; assistant asked whether to inspect artifact or code heaviness first. | Major state still Business Administration(0.58). | MIS artifact query; `sources=0`; `research_complete=true`. |
| 12 | Major | Student asked for a temporary MIS conclusion; assistant asked how to check MIS first instead of concluding. | Major still incomplete; `field=Business Administration(0.58)`; University not reached. | MIS artifact query; `sources=0`; `research_complete=true`. |

## Data-Agent Flaw Ledger

### F1 - Job Over-Calibrated From Weak / Blocked Evidence

- Severity: High
- Taxonomy: `calibration_fail`, `grounding_fail`, `discipline_fail`
- Source:
  - `eval/threads/university-finding-business-ux-20260413/traces/live_0002.json`
  - `eval/threads/university-finding-business-ux-20260413/traces/live_0004.json`
  - `eval/threads/university-finding-business-ux-20260413/traces/live_0005.json`
- Stage: Job
- Evidence fields:
  - `output.job_research.evidence_summary` includes multiple TopCV extraction failures, Cloudflare / 403 / blocked-page text.
  - `output.job_research.cited_sources` length is 5, but the evidence quality is partly blocked snippets.
  - Job confidences rose to `role_category=0.82`, `company_stage=0.86`, `day_to_day=0.91`, `autonomy_level=0.84` by `live_0005.json`.
- Assistant text summary:
  - The assistant used the research as enough to test and then lock the weekly split and job environment.
- Why it fails:
  - The contract says confidence above 0.7 requires surviving a data-based squeeze, not weak snippets or blocked pages.
  - Blocked extraction should lower trust or trigger a better source/query, not support high confidence.

### F2 - Job Repeated The Same Search Query Across Multiple Turns

- Severity: Medium
- Taxonomy: `discipline_fail`
- Source:
  - `live_0002.json` through `live_0005.json`
- Stage: Job
- Evidence fields:
  - `output.job_research.search_query` remains `công việc product coordinator UX research business analyst ở startup Việt Nam hàng ngày làm gì`.
  - Serper quota count increments from 66 to 69.
- Assistant text summary:
  - Turns 3-5 ask narrower user-facing-ratio questions, but the query does not change enough to target a ratio or fresh market fact.
- Why it fails:
  - Repeated search for unchanged claims violates tool discipline.
  - If the same query cannot answer the ratio question, the query should change or the analyst should state that the evidence is insufficient.

### F3 - Major Search Planner Missed The User's Direct Comparison Request

- Severity: High
- Taxonomy: `query_fail`, `probe_fail`
- Source:
  - `live_0008.json`
  - `live_0010.json`
- Stage: Major
- Evidence fields:
  - In `live_0008.json`, user asks to compare Business Administration, MIS, Digital Business, and Marketing Analytics on four criteria.
  - `output.major_research.search_query` remains a BA-only query about Quản trị kinh doanh.
  - In `live_0010.json`, user asks to compare Digital Business, MIS, and Marketing Analytics directly; `search_query` remains a Digital Business-only query.
- Assistant text summary:
  - Instead of doing the requested comparison, the assistant asks which major to inspect first or which direction to prioritize.
- Why it fails:
  - The central contradiction is comparative curriculum fit. A single-major query cannot answer it.
  - The probe pushes process choice instead of the actual educational tradeoff.

### F4 - Major Treats `No results found` As `research_complete=true`

- Severity: High
- Taxonomy: `grounding_fail`, `discipline_fail`
- Source:
  - `live_0006.json`
  - `live_0007.json`
  - `live_0008.json`
  - `live_0009.json`
  - `live_0010.json`
  - `live_0011.json`
  - `live_0012.json`
- Stage: Major
- Evidence fields:
  - `output.major_research.evidence_summary` repeatedly says `Results: - No results found`.
  - `output.major_research.cited_sources` length is 0.
  - `output.major_research.research_complete=true`.
- Assistant text summary:
  - The assistant says the curriculum evidence is not confirmed, but continues asking another narrowing question instead of changing query strategy or exposing the retrieval failure as a blocker.
- Why it fails:
  - A no-result packet should not count as complete research.
  - The data agent needs a fallback query strategy: official program curriculum pages, university names, Vietnamese/English program names, or broader terms.

### F5 - Major Field State Stayed On Business Administration After Student Pivoted To MIS / Digital Business

- Severity: Medium
- Taxonomy: `calibration_fail`, `grounding_fail`
- Source:
  - `live_0009.json`
  - `live_0010.json`
  - `live_0011.json`
  - `live_0012.json`
- Stage: Major
- Evidence fields:
  - `output.major.field.content` remains `Business Administration` with confidence `0.58`.
  - User explicitly asks to inspect Digital Business, then compare with MIS and Marketing Analytics, then starts from MIS.
- Assistant text summary:
  - The assistant acknowledges the pivot in prose but raw state remains anchored to BA.
- Why it fails:
  - The extracted Major hypothesis should either change to a comparative shortlist or lower BA confidence while inspecting alternatives.
  - Keeping BA as the only `field` makes downstream University selection likely to optimize the wrong major.

### F6 - Major Soft-Locked Before University

- Severity: High
- Taxonomy: `probe_fail`, `query_fail`, `discipline_fail`
- Source:
  - `live_0008.json` through `live_0012.json`
- Stage: Major
- Evidence fields:
  - `output.stage.current_stage=major` throughout.
  - `output.major.done=false`.
  - `output.university=null`; `output.uni_research=null`.
  - Repeated no-result Major packets.
- Assistant text summary:
  - Student repeatedly asks for comparison and temporary conclusion; assistant repeatedly asks which thing to check first.
- Why it fails:
  - The student is not uncertain about process. They ask for a decision aid.
  - The agent should either produce a provisional ranking with uncertainty labels or declare research failure and ask for target schools/programs to inspect.

### F7 - R2 Patch Improved Prose But Did Not Update Raw Major State

- Severity: High
- Taxonomy: `calibration_fail`, `grounding_fail`
- Source:
  - `eval/threads/university-finding-business-ux-20260413-r2/traces/live_0001.json`
  - `eval/threads/university-finding-business-ux-20260413-r2/traces/live_0002.json`
  - `eval/threads/university-finding-business-ux-20260413-r2/traces/live_0003.json`
- Stage: Major
- Evidence fields:
  - Assistant text in R2 `live_0001.json` says MIS is the provisional priority.
  - `output.major.field.content` remains `Business Administration` with confidence `0.58` across R2 `live_0001.json` through `live_0003.json`.
  - `output.major.done=false`; `output.university=null`.
- Assistant text summary:
  - The user accepts MIS as temporary priority and asks to move to school verification, but the raw state does not represent MIS as the major hypothesis.
- Why it fails:
  - The patch improved the conversational answer, but the extractor/state layer remains stale.
  - University selection cannot be reliable while downstream state still optimizes for Business Administration.

### F8 - R2 UEH Request Triggered Non-UEH Research

- Severity: High
- Taxonomy: `query_fail`, `grounding_fail`
- Source:
  - `eval/threads/university-finding-business-ux-20260413-r2/traces/live_0003.json`
- Stage: Major / intended University handoff
- Evidence fields:
  - User asks: inspect UEH first and compare later with FPT, RMIT, UEL.
  - `output.major_research.search_query` is `chuong trinh dao tao MIS o Viet Nam du an do an hoc phan`.
  - `output.major_research.cited_sources` are NEU, NEU MIS, VNU IS, and NEU PDF sources; no UEH source appears.
  - `output.stage.stage_related=["uni"]`, but `output.stage.current_stage="major"`.
- Assistant text summary:
  - The assistant says it will check UEH, then asks whether to inspect artifact or Product BA/UX signals first.
- Why it fails:
  - Once the student names UEH, the required search should include UEH or its official program pages.
  - The raw route recognizes University relevance but does not transition or create `uni_research`.

### F9 - R2 Still Treats No-Result Research As Complete

- Severity: Medium
- Taxonomy: `discipline_fail`, `grounding_fail`
- Source:
  - `eval/threads/university-finding-business-ux-20260413-r2/traces/live_0001.json`
  - `eval/threads/university-finding-business-ux-20260413-r2/traces/live_0002.json`
- Stage: Major
- Evidence fields:
  - R2 `live_0001.json`: Digital Business query returns `No results found`, `cited_sources=[]`, `research_complete=true`.
  - R2 `live_0002.json`: MIS query returns `No results found`, `cited_sources=[]`, `research_complete=true`.
- Assistant text summary:
  - The assistant correctly labels the conclusion as provisional, but the research packet still claims completion.
- Why it fails:
  - The state model still cannot distinguish "tool call ended" from "usable research exists."

## Failure Taxonomy Counts

| Taxonomy | Count | Main Source |
|---|---:|---|
| `trigger_fail` | 0 observed | Search did trigger for concrete Job/Major claims. |
| `query_fail` | 3 | Major comparison request handled with single-major/no-result queries; R2 UEH request searched generic MIS instead. |
| `grounding_fail` | 5 | Blocked Job evidence, Major no-result packets, stale Major state, and non-UEH sources influenced dialogue. |
| `crash_fail` | 0 observed | The issue was failure to ground/compare, not a missed contradiction after good evidence. |
| `calibration_fail` | 3 | Job confidence jumped high; Major field stayed BA through pivots and R2 MIS provisional choice. |
| `discipline_fail` | 5 | Repeated Job query; repeated no-result Major query strategy; no fallback; no-result packets still complete in R2. |
| `probe_fail` | 2 | Major asks process-choice probes after student requests comparison/conclusion. |

## Data-Agent Evaluation Takeaways

1. Job passed the trigger seam but failed evidence quality discipline and confidence calibration.
2. Major currently has the highest-severity problem: it can enter a no-result search loop and avoid giving the comparison the student asked for.
3. `research_complete=true` is too weak as currently recorded; it can mean "tool call ended" rather than "usable evidence exists."
4. Future deterministic evals need fixtures for:
   - blocked job-board pages
   - no-result curriculum queries
   - comparative-major requests
   - student asks for a temporary decision after several failed searches
5. R2 improved the assistant's willingness to provide a provisional answer, but did not fix stale extractor state, no-result completion semantics, or school-specific query routing.
6. University could not be audited because neither R1 nor R2 reached `university` by the inspected traces.

## Recommended Eval Cases

| Attack ID | Stage | Scenario | Expected Check |
|---|---|---|---|
| `job_blocked_sources_confidence_cap_01` | Job | Job search returns mostly blocked job-board pages. | `role_category`, `company_stage`, `day_to_day`, `autonomy_level` remain `<=0.7` unless student independently defends the path. |
| `major_comparison_query_01` | Major | Student asks BA vs MIS vs Digital Business vs Marketing Analytics by explicit criteria. | Query must include at least two compared fields or run multiple targeted searches; assistant must not ask which one to check first. |
| `major_no_results_fallback_01` | Major | First curriculum query returns no results. | `research_complete=false` or fallback query triggered; no confidence increase from no-result evidence. |
| `major_decision_after_failed_search_01` | Major | Student asks for a temporary conclusion after no-result searches. | Assistant gives provisional ranking with uncertainty or asks for school/program targets; no repeated process-choice probe. |
| `major_state_updates_after_provisional_choice_01` | Major | Assistant chooses MIS as provisional priority. | Raw `major.field` must become MIS or a structured shortlist; stale Business Administration must not remain primary. |
| `uni_school_named_query_01` | University | Student names UEH and asks for UEH/MIS/Digital Business/Business Analytics fit. | Query must include UEH or official UEH program identifiers; `uni_research` should start or stage should transition to University. |

## Post-Auditor Extension - R3 through R7

This section was appended by the main session after the worker audit completed.

| Run | Trace Coverage | Data-Agent Finding |
|---|---:|---|
| R3 | `eval/threads/university-finding-business-ux-20260413-r3/traces/live_0001.json` | Major synthesis became handoff-sufficient, but `required_skills_coverage=0.78` kept `major.done=false`. |
| R4 | `eval/threads/university-finding-business-ux-20260413-r4/traces/live_0001.json` | Required-skills floor worked, but `curriculum_style=0.79` became the next threshold blocker. |
| R5 | `eval/threads/university-finding-business-ux-20260413-r5/traces/live_0001.json` | Major completed and same-turn advanced to University. |
| R5 | `live_0002`-`live_0003.json` | University over-restricted UEH searches and asked the student to pick evidence/page type after the student had already specified artifact-first evaluation. |
| R6 | `eval/threads/university-finding-business-ux-20260413-r6/traces/live_0001`-`live_0002.json` | University source allowlist/query discipline improved and recovered UEH sources, but synthesis still asked threshold/meta questions instead of ranking. |
| R7 | `eval/threads/university-finding-business-ux-20260413-r7/traces/live_0001.json` | University moved to FPT comparison and found sources, but still asked how many evidence layers should count as stronger than UEH. |

Additional flaws:

- `UNIVERSITY_OFFICIAL_DOMAINS` initially omitted the exact schools under test: UEH, UEL, FPT, RMIT, and USTH.
- University research can still return noisy school-adjacent sources, such as FPT Software/APTECH, when the intended target is FPT University MIS/Digital Business curriculum.
- University profile fields are too coarse for this mission. `target_school`, `prestige_requirement`, and `campus_format` do not preserve the active comparison matrix: artifact strength, internship/network, international exposure, and ROI.
