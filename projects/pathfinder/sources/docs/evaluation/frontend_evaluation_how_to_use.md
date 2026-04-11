# PathFinder Frontend Evaluation Workflow

Last updated: 2026-04-11

## Purpose

Use this workflow when testing the PathFinder frontend locally, especially when the goal is to inspect every UI state without spending live LLM turns.

This is a dev/eval workflow. It depends on the debug harness added for local runs and must be guarded by `PATHFINDER_DEBUG=1` on the backend.

## Canonical Locations

- Frontend app: `frontend/`
- Backend app: `main.py`
- Debug trace utilities: `backend/debug_trace.py`
- Debug tab: `frontend/src/components/tabs/DebugTab.jsx`
- Debug fixtures: `frontend/src/data/debugFixtures.js`
- Live traces: `eval/threads/<session_id>/traces/live_*.json`
- Live manifest: `eval/threads/<session_id>/live_session.json`
- Frontend evaluation reports: `eval/FRONTEND_EVALUATION_REPORT.md`

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

## Report Template

Write the report to `eval/FRONTEND_EVALUATION_REPORT.md`.

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
- The repo report exists and the vault/repo dev logs are updated.
