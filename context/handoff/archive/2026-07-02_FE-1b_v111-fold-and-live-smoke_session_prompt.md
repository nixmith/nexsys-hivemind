<!--
file: context/handoff/2026-07-02_FE-1b_v111-fold-and-live-smoke_session_prompt.md
purpose: Dispatch brief for the FE-1b frontend micro-lane (separate Cowork conversation) — fold the two adjudicated FE-1 drifts client-side (v1.1.1 slug-suffix problem-type matching; drop the A4/A5 bare-body tolerance now that M7.5c-a landed) + re-run the live smoke. Expect the poll cursor + both honest states to light up. Hours-scale.
audience: Frontend lane (nexsys-frontend skill; fresh Cowork conversation; write-isolated); Nick (Core boot + token for the smoke; commits host-side).
state-type: session prompt (lane dispatch).
status: READY — authored 2026-07-02 by the v14 hub at beat 50 (M7.5c-a landed CI-green).
baseline (RE-VERIFY at launch): core **e3d7296** (M7.5c-a: A4/A5 emit the frozen v1.1.1 `{data, meta}` envelope; ci.yml + install-smoke green on the push) · hivemind **8a34a7f**+beat-50 · freeze **v1.1.1**. Write-isolation: `web-ui/dashboard/**` ONLY.
-->

# FE-1b — the v1.1.1 fold + the live smoke (frontend micro-lane)

Load the **nexsys-frontend** skill FIRST, then ground in order: (1) the freeze record `context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md` — read BOTH `[v1.1.1]` blocks fresh (problem-`type` is the URI form; clients key on the slug suffix); (2) your own FE-1 return `context/audits/2026-07-02_frontend-dev-lane_FE-1-live-integration_return.md` (the two adjudicated drifts + the smoke procedure + FE1_GO_LIVE.md); (3) the M7.5c-a delivery note at the top of `context/handoff/cross-agent-notes.md` (the exact shapes A4/A5 now emit); (4) `web-ui/dashboard/CLAUDE.md`. The env-model applies (`context/process/cowork-environment-model.md`): file-tools for all edits; lock-free git reads only (`git --no-optional-locks status --porcelain`, `git log`); NO commits (Nick commits host-side).

## Scope — IN
1. **DRIFT-2 fold:** problem-type handling keys on the **slug suffix** of the URI form (`https://homesynapse.local/problems/<slug>`) per Locked Doc 09 / freeze v1.1.1 — remove or adjust any matching that assumed a bare form; tests updated to the URI fixtures.
2. **DRIFT-1 fold:** A4 `/internal/projection` + A5 `/internal/dlq` are now enveloped (`{data, meta}` — frozen fields + ruled extras; `meta.viewPosition` on every read). **Drop any bare-body tolerance/shim**; the poll cursor reads `meta.viewPosition` uniformly across all endpoints.
3. `npm run verify` green (the lane gate). `frontend.yml` is the CI gate of record on push (path-filtered `web-ui/dashboard/**`).
4. **Live smoke re-run** (needs Nick: Core boot + pairing token per FE1_GO_LIVE.md): expect the dashboard to REFRESH live — the FE-1 finding "views load once and never refresh" is the bug this closes. Verify: poll cursor advancing; BOTH honest states rendering; zero error banners.

## Scope — OUT
Anything outside `web-ui/dashboard/**` · Core/api changes (if a Core shape still mismatches the freeze, that is a cross-lane event — STOP and report to the hub; never patch client-side against a drifted shape) · the website build (separate lane, launches after FE-1b closes) · new features or refactors.

## Return protocol
Lane-return file in `context/audits/` (`2026-07-0X_frontend-dev-lane_FE-1b_return.md`) + a short cross-agent note + a staged commit message in `_scratch/` carrying the env-model §10 pre-commit audit (exact path count stated; runtime state `.homesynapse/`, tokens, `node_modules/`, `dist/` never staged — name the token artifact's disposition explicitly). The v14 hub (separate conversation) audits the return two-layer before fold.

## Done-when
Slug-suffix matching in place (tests prove it) · bare-body tolerance removed · `npm run verify` green · smoke: live refresh + both honest states + zero error banners against core `e3d7296` · return filed with the §10-audited change set + the next-lane pointer (website build).
