<!--
file: context/planning/2026-06-27_causal-read-API_scope-freeze-and-milestone-breakdown.md
purpose: The v9 hub's strategic scope-freeze + milestone breakdown for the thin causal-read-API — the next Core slot after the M7.4 arc. Right-sizes the read-API per P1 (size visible at scoping), pins the IN/OUT line against the FROZEN v1.1 dashboard read-API contract, and sequences the sub-milestones. The authority the M-RA coding instructions build against.
audience: Nick (scope authority — this operationalizes his delegation "drive the core forward"), the v9 PM hub (authors the M-RA instructions to this), the Coder (builds to it), the Web-UI lane (consumes the same v1.1 contract).
state-type: planning / scope-freeze + milestone breakdown
status: PROPOSED 2026-06-27 (v9 hub) — Nick delegated the read-API scope call; this is that call. Folds into the backlog M-RA rows on co-sign.
baseline: core db8ab5f (the M7.4 arc COMPLETE — the live pipeline produces RunCausalChain + the run-lifecycle/dispatch/confirmation events the read-API projects). docs 75d0345 (Doc 09 REST / Doc 13 Web-UI / Doc 16 RunCausalChain — Locked).
anchors: context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md (the FROZEN v1.1 contract — the binding shapes) · context/decisions/2026-06-20_V1-launch-scope_decision-record.md (the thin slice; "must not balloon into all of M12") · context/planning/2026-06-26_v6-forward-plan_execution-refresh.md (Core sequence: read-API → AB-4 → M9).
-->

# Causal-Read-API — Scope-Freeze + Milestone Breakdown (2026-06-27, v9 hub)

## The strategic call (why this, why now, why split)

The thin causal-read-API is the **next Core slot** and the **gate-2 enabler** ("the hero renders on real data"). With the M7.4 arc COMPLETE, the live pipeline now produces everything the hero reads — the `RunCausalChain`, the run-lifecycle/dispatch events, and the `confirmed|unconfirmed|failed` outcome. So this milestone is **a projection + REST read surface over data that already exists** — *not* a new-machinery build. **The key grounding finding:** the FROZEN v1.1 contract scopes the hard "why-didn't-it-fire" half to be answerable **from existing run records + absence + config** (recent `SKIPPED` runs → CONDITION_NOT_MET; `UNCONFIRMED`/`FAILED` action → ACTED_BUT_UNCONFIRMED; no run in window → NEVER_TRIGGERED; off → DISABLED). The *deep* per-non-match trigger-evaluation recording is **post-V1** (explicitly OUT). **So no evaluation-trace projection is needed** — the entire V1 causal surface reads from the live log.

The contract defines **six reads** (B3's four + B1 + B2). Six reads is over the P1 sizing smell-test (>3 sub-pieces) → **split into three reviewable/gateable sub-milestones**, sequenced by demo-leverage. This makes size visible at scoping (the M7.4-split discipline), keeps each piece a clean compile-and-gate unit, and protects the **scope guard** (the contract must NOT grow into M12).

## IN (V1 — the frozen v1.1 causal read surface, as pure projections over the log; INV-SA-03)

- **The hero "why did it fire?" + "did it confirm?"** — `GET /api/v1/runs` (run list) + `GET /api/v1/runs/{runId}/causal-chain` (the tree: trigger → conditions+observedState → actions+`outcome`(DISPATCHED|CONFIRMED|UNCONFIRMED|FAILED|SKIPPED) → outcome → cascade). Maps 1:1 onto `RunCausalChain`/`ChainLink` + the AMD-92 event rows; the `CONFIRMED|UNCONFIRMED` distinction reads the M7.3/M7.4c ledger correlation.
- **The co-equal "why didn't it fire?"** — `GET /api/v1/automations/{id}/non-firing` (verdict ∈ {CONDITION_NOT_MET, NEVER_TRIGGERED, ACTED_BUT_UNCONFIRMED, DISABLED} + plain-language explanation + triggerSummary), computed **from existing run records / absence / config**.
- **The automation list** — `GET /api/v1/automations` (component-based summaries; supporting surface #1).
- **The event feed** — `GET /api/v1/events` (B1) with **never-silent-blank `origin`** (AUTOMATION/DEVICE/USER/EXTERNAL/UNKNOWN — UNKNOWN is an explicit honest value) + on-demand `GET /api/v1/events/{eventId}`.
- **Consolidated health** — `GET /api/v1/health` (B2) — a thin aggregation of the EXISTING A4 (`/internal/projection`) + A5 (`/internal/dlq`) + lifecycle health.
- Every read carries the frozen cross-cutting contract: `meta:{viewPosition,timestamp}` (the 1–2s poll model), RFC-9457 problem bodies incl. `state-store-replaying`(503), ETag/304, cursor pagination, AB-1 bearer auth.

## OUT (→ full M12 observability, post-launch — the scope guard, binds every sub-milestone)

No general/ad-hoc query language; no arbitrary event-graph traversal; no cross-run analytics; no audit projection; **no per-non-match trigger-evaluation recording** (the deep "why the trigger didn't match" diagnosis); no metrics/o11y dashboards; **no WebSocket push** (D-OPEN-3 firm — REST poll only). No parallel trace store — explanation is a pure projection of the log (INV-SA-03).

## The breakdown (three sub-milestones — proposed M7.5a/b/c; backlog-number is Nick's placement call)

| Sub-milestone | Reads | Why this grouping | Sequence |
|---|---|---|---|
| **M7.5a — the hero causal read** | `GET /runs` + `GET /runs/{id}/causal-chain` | The gate-2 core: the "why did it fire? / did it confirm?" hero on the live `RunCausalChain` + the M7.4 confirmation data. Highest demo-leverage. The read-projection pattern the other two reuse. | **1st (critical path)** |
| **M7.5b — the non-firing half + automation list** | `GET /automations/{id}/non-firing` + `GET /automations` | Completes the differentiator (the co-equal "why didn't it fire?", from existing run records/config) + supporting surface #1. Builds on M7.5a's projection plumbing. | 2nd |
| **M7.5c — the supporting feeds** | `GET /events` (+`/events/{id}`) + `GET /health` | The event feed (never-silent-blank origin) + the health consolidation. Lower demo-leverage (the device/health views already run off the EXISTING A1–A5); sequence with the Web-UI lane's need, partly deferrable. | 3rd (sequence-with-frontend) |

**Each sub-milestone:** a new endpoint set in the REST module (Doc 09) + a read projection/query service over the log (no new write path, no new event types — zero mint, counts hold 71/41/53), with the frozen v1.1 response shapes pinned in a shape test, behind AB-1 auth, returning `state-store-replaying`(503) until LIVE. Reuses the existing read surfaces (`MaterializedStateQueryService`, the A1–A5 endpoint patterns, `RunCausalChain`, the event store reads).

## Cross-lane + sequencing notes

- **The Web-UI lane consumes the SAME frozen v1.1 contract** — it mocks B1/B2/B3 today and swaps to the real endpoints as M7.5a/b/c land. Any deviation from a frozen shape at implementation is a **cross-lane event** (the hub notifies the Web-UI lane; public-API shape is Nick's call). The forthcoming `nexsys-frontend` skill builds the hero UI against these mocks now.
- **Core sequence (unchanged):** M7.5a → M7.5b → (M7.5c with the frontend) → **AB-4** (before M9 — the trust-hygiene hard-order) → **M9** (real Zigbee; the hero then runs on real device `state_reported` + the M9-seam replay-gate extension).
- **The additive `name` field (C8)** sequences with the config/M9 work, not here (the read endpoints tolerate its absence).

## First instruction (the immediate next Core deliverable)

**M7.5a coding instruction** — authored by the v9 hub against the **committed** post-M7.4d HEAD (so it targets the real composition root, not the working tree; the same discipline that held M7.4d authoring until M7.4c committed). It delivers `GET /api/v1/runs` + `GET /api/v1/runs/{runId}/causal-chain` as pure projections over the live log, to the exact frozen v1.1 shapes, with a shape test + the `state-store-replaying`/auth/poll-meta cross-cutting contract. Out of scope: the non-firing read (M7.5b), the feeds (M7.5c), and anything in the M12 OUT list above.
