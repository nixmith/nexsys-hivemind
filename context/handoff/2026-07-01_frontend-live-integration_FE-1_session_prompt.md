<!--
file: context/handoff/2026-07-01_frontend-live-integration_FE-1_session_prompt.md
purpose: Dispatch brief for the write-isolated FRONTEND lane — FE-1 live-integration: point the go-live-ready dashboard at a locally-running Core (the real M7.5a/b endpoints) per FE1_GO_LIVE.md, and fold the measured E5 rendering semantics so the hero renders honestly on real confirmation timing. M9-INDEPENDENT — runs in parallel with the M9-authoring lane.
audience: the frontend lane (a FRESH Cowork conversation; nexsys-frontend skill); Nick (boots Core locally + runs the gate); the v13 hub (receives the return).
state-type: session prompt (write-isolated worker lane).
status: READY — authored 2026-07-01 by the v13 hub post-governance-pass. Launch AFTER the beat-43 hivemind commit. Requires Nick at the keyboard for the Core boot + token step.
write-isolation: writes ONLY web-ui/dashboard/** + ONE return file context/audits/2026-07-XX_frontend-dev-lane_FE-1-live-integration_return.md. The frozen v1.1 contract is READ-ONLY LAW (contract gaps → escalate in the return, never patch locally). NO .github/workflows edits (frontend.yml is the hub's), NO spine edits, NO commits.
baseline (RE-DERIVE at session start): core 52824e9 (the dashboard + the activated frontend.yml gate; M7.5a/b endpoints in source; AB-1 bearer auth + AB-2 fail-closed reads + AB-4 cipher LIVE) · docs 1509b34 (AMD-97 ratified — the measured confirmation semantics are now contract) · hivemind cea7ae1 · bench 5ceff3b (the measured timing truth).
-->

# Frontend Lane — FE-1 Live-Integration (the dashboard meets the real backend)

You are the **write-isolated frontend lane** running the **nexsys-frontend** skill. The dashboard is go-live-ready (T1.3 audited; `FE1_GO_LIVE.md` is your checklist). Your charge: **make it render the hero on a live Core**, and make the honest states render at **measured** timing.

## 1. Ground (read first)

`web-ui/dashboard/FE1_GO_LIVE.md` (the one-sitting checklist — it is the plan of record; follow it) · `web-ui/dashboard/MODULE_CONTEXT.md` (or the lane's standing context files) · the frozen contract mirror `src/lib/contract.ts` + the v1.1 freeze record `context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md` · the E5 rendering semantics below · `context/process/cowork-environment-model.md` §1/§3 (path duality; each bash call independent).

## 2. The work

1. **FE-1 per FE1_GO_LIVE.md:** Nick boots Core locally (Seam-1 is closed: AB-1 bearer auth live) and supplies the token; flip `VITE_USE_MOCKS` off; run the checklist's smoke sequence against the real `GET /api/v1/runs`, `/runs/{id}/causal-chain`, `/automations`, `/automations/{id}/non-firing`. **`/events` + `/health` do not exist until M7.5c** — verify the dashboard degrades gracefully where the checklist expects them (the scenario engine's transport conditions cover the shapes; the live gap must not break the hero views).
2. **Fold the measured E5 rendering semantics** (now ratified contract — AMD-97, docs 1509b34; the measured truth in `nexsys-bench/corpus/devices/philips-hue-white-a19.md`):
   - **CT confirms slowly and legitimately** (measured 6.7–8.4 s; ratified per-capability timeout 15 s) — the pending→confirmed transition must not time out early or render failure-anxiety UI inside the window; consider a "confirming — this device reports color slowly" affordance keyed on per-capability timeout, never a hardcoded global.
   - **Idempotent commands may never visually confirm** (no-change ⇒ no report) — render the honest state (confirmed-from-cache/readback when the backend says so; never a forever-spinner).
   - **Effect/identify-class commands render honest `UNCONFIRMED` immediately** (never a false CONFIRMED, never a spinner — the moat's honesty is a UI behavior too).
   - **Superseded commands expire** — rapid re-commands must not strand stale pending chips.
   Scenario-engine coverage: extend `scenarios.ts` so each of these four is one click + contract-validated in CI (the T1.2 pattern).
3. **Gate:** `npm run verify` green locally; the pushed `frontend.yml` run green on the lane's commit (Nick commits host-side on the hub's word; the workflow path-filters on `web-ui/dashboard/**`, so your changes WILL trigger it).

## 3. Return contract

ONE return file: checklist outcomes (each FE1_GO_LIVE item pass/fail), the E5 scenario additions, any contract gaps found live (the entity-display-name candidate is already recorded — add evidence, don't fix), screenshots/notes on the hero rendering real data, and the recorded-backlog deltas (mobile-first hero / PWA / virtualization stay backlogged — do NOT build them here). Report to the hub; no commits, no spine edits.
