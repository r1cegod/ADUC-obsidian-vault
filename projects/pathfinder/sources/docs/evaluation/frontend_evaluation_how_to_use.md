# PathFinder Frontend Evaluation Workflow

> **TL;DR**: Use fixtures first for UI states, then use the optimized live-user workflow for traced product conversations; verify stage completion from raw backend state, not from assistant wording alone.

Last updated: 2026-04-13

## Purpose

Use this workflow when testing the PathFinder frontend locally, especially when the goal is to inspect every UI state without spending live LLM turns.

This is a dev/eval workflow. It depends on the debug harness added for local runs and must be guarded by `PATHFINDER_DEBUG=1` on the backend.

## Canonical Locations

- Evaluation domain index: `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\README.md`
- Frontend evaluation workflow: `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\frontend_evaluation_how_to_use.md`
- Frontend evaluation reports: `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\`
- Frontend app: `frontend/`
- Backend app: `main.py`
- Debug trace utilities: `backend/debug_trace.py`
- Debug tab: `frontend/src/components/tabs/DebugTab.jsx`
- Debug fixtures: `frontend/src/data/debugFixtures.js`
- Live traces: `eval/threads/<session_id>/traces/live_*.json`
- Live manifest: `eval/threads/<session_id>/live_session.json`

Repo `eval/` is for executable assets and raw evidence only. Write reports, audit logs, workflow changes, and run retrospectives in the vault evaluation directory. The only mirrored documentation is the dev log.

## Required Startup

Start the backend in debug mode:

```powershell
$env:PATHFINDER_DEBUG='1'
venv\Scripts\python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Start the frontend dev server:

```powershell
cd frontend
npm run dev
```

Expected local URLs:

- Frontend: `http://localhost:3000`
- Backend health: `http://localhost:8000/health`

## Guardrails

- Fixture testing comes before live chat testing.
- Do not use live model turns to reach UI states that can be reached through fixtures.
- Start tracing only for a deliberate live run.
- Stop tracing before reviewing trace files.
- Treat `eval/threads/<session_id>/traces/live_*.json` as immutable raw evidence.
- Put curated replay rows in the dataset separately; do not hand-edit raw traces.
- Use fresh `session_id`s for reset-style tests because graph message reducers append by design.

## Evaluation Layers

Run these layers in order.

1. Static checks:

```powershell
cd frontend
npm run lint
npm run build
```

2. Browser load check:

```powershell
agent-browser open http://localhost:3000
agent-browser wait --load networkidle
agent-browser eval 'document.body.innerText.trim().length > 0 ? "HAS_CONTENT" : "BLANK"'
agent-browser eval 'document.querySelector(".vite-error-overlay, #webpack-dev-server-client-overlay, [data-nextjs-dialog]") ? "ERROR_OVERLAY" : "OK"'
agent-browser screenshot --annotate
agent-browser snapshot -i
```

3. Debug helper check:

```powershell
agent-browser eval 'window.__PF_DEBUG__ ? "DEBUG_READY" : "NO_DEBUG"'
agent-browser eval 'JSON.stringify(Object.keys(window.__PF_DEBUG__ || {}))'
```

4. Fixture sweep:

Use the Debug tab or the browser console helper:

The Debug tab fixture and forced-stage buttons apply frontend-only state. Use `patchBackendState(...)` explicitly when the backend graph state must also be changed.

```javascript
await window.__PF_DEBUG__.applyFixture("empty", { backend: false })
await window.__PF_DEBUG__.applyFixture("quizSeeded", { backend: false })
await window.__PF_DEBUG__.applyFixture("activeThinking", { backend: false })
await window.__PF_DEBUG__.applyFixture("activePurpose", { backend: false })
await window.__PF_DEBUG__.applyFixture("activeGoals", { backend: false })
await window.__PF_DEBUG__.applyFixture("activeJob", { backend: false })
await window.__PF_DEBUG__.applyFixture("activeMajor", { backend: false })
await window.__PF_DEBUG__.applyFixture("activeUni", { backend: false })
await window.__PF_DEBUG__.applyFixture("allComplete", { backend: false })
await window.__PF_DEBUG__.applyFixture("pathDebateReady", { backend: false })
await window.__PF_DEBUG__.applyFixture("userTagAlerts", { backend: false })
await window.__PF_DEBUG__.applyFixture("escalationLock", { backend: false })
await window.__PF_DEBUG__.applyFixture("longText", { backend: false })
```

After each fixture:

```powershell
agent-browser eval 'document.querySelector(".vite-error-overlay, #webpack-dev-server-client-overlay, [data-nextjs-dialog]") ? "ERROR_OVERLAY" : "OK"'
agent-browser eval 'document.body.scrollWidth <= document.documentElement.clientWidth ? "NO_HORIZONTAL_OVERFLOW" : "HORIZONTAL_OVERFLOW"'
agent-browser screenshot
```

5. Forced-stage sweep:

Use the Debug tab buttons or the browser console helper:

```javascript
for (const stage of ["thinking", "purpose", "goals", "job", "major", "uni"]) {
  await window.__PF_DEBUG__.forceStage(stage, { backend: false })
  await window.__PF_DEBUG__.finishForcedStage(stage, { backend: false })
}
```

Required visual checks:

- Profile tab remains readable.
- ProgressBar shows both facts in forced mode: the real current stage and the forced anchor stage.
- Stage tab focuses the forced anchor stage as the active card.
- Stage completion states move correctly after each forced-stage finish.
- Test tab still renders seeded answers and results.
- Chat tab keeps messages readable.
- Escalation lock blocks input clearly.
- Long text fixture does not overlap or cause horizontal page overflow.

Reliable browser assertions can use these non-visual attributes:

```javascript
Array.from(document.querySelectorAll("[data-progress-stage]")).map((el) => ({
  stage: el.dataset.progressStage,
  state: el.dataset.progressState,
}))

Array.from(document.querySelectorAll("[data-stage-status]")).map((el) => ({
  title: el.innerText.split("\n")[0],
  state: el.dataset.stageStatus,
}))
```

6. Live trace smoke, only when needed:

```javascript
await window.__PF_DEBUG__.startTrace()
// send one intentional chat turn through the UI
await window.__PF_DEBUG__.stopTrace()
```

Then inspect:

```powershell
Get-ChildItem eval\threads\<session_id>\traces
Get-Content eval\threads\<session_id>\live_session.json
```

7. Live user-like frontend run:

Use this when the goal is to behave like a real student, starting with the tests and then chatting until a target stage is actually complete.

Human profile rule:

- Create one coherent student profile before the run.
- Keep answers consistent with that profile.
- Prefer concise but information-dense replies after turn 5 so the run tests stage movement instead of endless small talk.

Optimized interaction rule:

- Define the target boundary before the first live turn: one stage completion, one stage transition, or one named blocker.
- Stop at that boundary. If the next stage exposes new bugs, record them as next-cycle debt instead of patching them inside the same live run.
- A live operation may patch and rerun the same boundary, but it should not harden multiple stages in one pass unless the user explicitly expands the mission.
- Default stop condition after a fix: two runs only, one reproduction run and one verification run. Add extra `-rN` runs only when the first verification exposes a bug in the same boundary.
- When a patch proves the target boundary but reveals the next stage is weak, write the report and stop.
- Batch-click quiz answers with one `agent-browser eval` command instead of manually clicking 150 buttons.
- Use `agent-browser batch --bail` for short sequential UI actions like click, fill, and Enter.
- Use `window.__PF_DEBUG__.newSession()` for every fresh run.
- Use `window.__PF_DEBUG__.startTrace()` before the first test submission.
- Use the UI buttons, not direct backend patching, for the quiz path unless the run is explicitly a fixture-only recovery.
- After each chat turn, inspect only the latest assistant message plus state summary.
- Every 5 turns, check Profile and Stage tabs for overlay, horizontal overflow, and stage-card status.
- If the run is long or data-heavy, spawn one data-auditor worker. Give it write ownership of one vault audit/report file. The auditor summarizes raw trace evidence; the main agent keeps running the frontend session and fixing blockers. Repo files should hold only raw traces, datasets, manifests, or temporary scratch needed for reproduction.
- Stop the active trace before every patch/restart. Restore the last known-good trace into a new `-rN` session after restart so pre-patch and post-patch evidence stay separate.

Budget split:

- `frontend UX run`: real browser, minimal patching, stop at target boundary.
- `prompt/data-agent hardening`: restored trace with `eval/live_session_probe.py`, no browser except final smoke.
- `data auditor`: compact trace evidence and flaw ledger only; no code/prompt edits.

Completion rule:

Do not trust user-facing wording like "Goals is locked" by itself. A stage is complete only when raw/debug state agrees.

For Goals completion, verify:

```javascript
const payload = await window.__PF_DEBUG__.getBackendState()
payload.rawState.goals?.done === true
payload.frontendState.completedStages.includes("goals")
// or currentStage has advanced to job/major/uni with goals done in raw state
```

If the assistant response claims a later stage while raw state is still earlier, record it as a runtime flaw.

8. Uncertainty attack run:

Use this when the target is a normal student who does not have a stable view yet.

Mission:

- Attack with uncertainty.
- Test whether PathFinder can work with sincere indecision without soft-locking, over-drilling, premature stage claims, or false escalation.

Human profile rule:

- The student is cooperative but not self-authored yet.
- The student should not already know their final career/major direction.
- Answers should contain mixed preferences, family pressure, salary concern, fear of choosing wrong, and shallow exposure.
- Do not troll. Do not stonewall. The uncertainty must be normal and realistic.

Success criteria:

- The system separates genuine uncertainty from avoidance or compliance.
- The system extracts usable weak signals without forcing fake certainty.
- The system asks concrete tradeoff questions.
- The system advances when enough direction exists for handoff.
- Raw backend state agrees with any claimed stage completion.

Failure criteria:

- Repeatedly asks the same tradeoff after the student gives reasonable partial answers.
- Treats "I don't know" as bad faith.
- Escalates normal uncertainty.
- Claims later-stage progress while raw state remains earlier.
- Crashes or returns validation errors.

Report location:

- Vault report: `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\uncertainty_attack_report_YYYY-MM-DD.md`
- Register the focused report in `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\README.md`.

Minimum report sections:

- Mission
- Production target
- Human profile
- Run protocol
- Completion verification
- Turn log
- 5-turn checkpoints
- Findings
- Fixes made
- Evidence
- Residual risk

Representative optimized quiz click pattern:

```javascript
const qButtons = Array.from(document.querySelectorAll("button[aria-label]"))
  .filter((button) => / - [1-5]$/.test(button.getAttribute("aria-label") || ""))

// RIASEC buttons are rendered in question order, five buttons per question:
// 5, 4, 3, 2, 1.
const offsetByScore = { 5: 0, 4: 1, 3: 2, 2: 3, 1: 4 }
qButtons[questionIndex * 5 + offsetByScore[score]].click()
```

9. Identity-continuation debug run:

Use this when the target is not a fresh UI journey, but a continuation from a prior real-user trace. This is the right lane for prompt/stage behavior after a long conversation, especially when replaying all previous turns would waste time and tokens.

Mission:

- Restore the previous raw backend state.
- Continue as the same human identity.
- Check only the latest response and compact state flags each turn.
- Stop when the target stage is complete in raw/debug state.

Use the repo helper:

```powershell
python eval\live_session_probe.py restore <new_session_id> --trace eval\threads\<source_session>\traces\live_0051.json --state-key output
python eval\live_session_probe.py trace <new_session_id> start
python eval\live_session_probe.py send <new_session_id> --message-file eval\scratch\next_message.txt
python eval\live_session_probe.py state <new_session_id>
python eval\live_session_probe.py trace <new_session_id> stop
```

Rules:

- Restore from trace `output`, not `frontend_state`, when testing backend graph continuation.
- Use `--message-file` for Vietnamese or other non-ASCII text. Do not embed Vietnamese literals inside a PowerShell here-string piped into Python; it can corrupt accents in saved trace input.
- Inspect compact state each turn. Do not read the full trace unless there is a crash, stage contradiction, or token/context issue.
- Verify target completion from raw/debug state, not assistant wording.
- If `done === true` but `currentStage` has not advanced, send one transition-confirming answer and record the lag. This can happen because stage routing runs before same-turn extraction.

Focused report location:

- Vault report: `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\identity_continuation_<target>_report_YYYY-MM-DD.md`
- Register the focused report in `D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\README.md`.

Representative latest-response-only check:

```javascript
const messages = window.__PF_DEBUG__.getMessages()
const latest = messages.at(-1)
const state = window.__PF_DEBUG__.getAppState()
JSON.stringify({
  latest: latest?.content,
  currentStage: state.currentStage,
  completedStages: state.completedStages,
})
```

Representative 5-turn tab checkpoint:

```javascript
const noOverlay = document.querySelector(
  ".vite-error-overlay, #webpack-dev-server-client-overlay, [data-nextjs-dialog]"
) ? "ERROR_OVERLAY" : "OK"

const noOverflow =
  document.body.scrollWidth <= document.documentElement.clientWidth
    ? "NO_HORIZONTAL_OVERFLOW"
    : "HORIZONTAL_OVERFLOW"

const stageCards = Array.from(document.querySelectorAll("[data-stage-card]"))
  .map((el) => ({
    title: el.innerText.split("\n")[0],
    state: el.dataset.stageStatus,
  }))
```

## Report Template

Write the report in the vault evaluation directory:

```text
D:\ANHDUC\ADUC_vault\ADUC\projects\pathfinder\sources\docs\evaluation\
```

Required sections:

- Run metadata: date, branch if relevant, local URLs, debug mode status.
- Checks run: lint, build, browser load, fixtures, forced stages, trace smoke if used.
- Findings: bugs first, with exact state or fixture that triggered each issue.
- Fixes made: files changed and behavior fixed.
- Evidence: screenshots, trace session IDs, commands, and relevant output summaries.
- Residual risk: states not exercised, browser sizes not covered, live turns not replayed.

## Completion Criteria

The frontend evaluation is done when:

- Static checks pass.
- Browser loads without error overlay.
- `window.__PF_DEBUG__` is available in Vite dev mode.
- Fixture and forced-stage sweeps can be run without console/runtime errors.
- Any concrete bug found during the sweep is fixed or explicitly recorded.
- The vault report exists.
- Repo trace, dataset, or manifest evidence exists when needed for reproduction.
- The vault dev-log day file is updated and only the dev-log day file is mirrored into repo `logs/dev/days/`.
