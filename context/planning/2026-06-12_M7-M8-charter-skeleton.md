<!--
file: context/planning/2026-06-12_M7-M8-charter-skeleton.md
purpose: M7/M8 charter SKELETON — the multi-piece automation-window charter per P1 (pieces visible at scoping, not discovered in arrears). Authored at the W0/brief-authoring session; POPULATED at the R14/R15 synthesis (fold order R14-B → R14-A → R15); ACTIVATES only after the M7 entry-gate closes.
audience: PM, Nick, Coder (at activation)
update-cadence: at synthesis (population), then per-piece
state-type: planning
status: SKELETON — authored 2026-06-12 (PM, Cowork). NOT a commitment to issue; the M7 entry-gate (below) governs. Population markers: ⟨R14-A⟩ ⟨R14-B⟩ ⟨R15⟩ ⟨SYNTH⟩.
anchors: context/planning/2026-06-11_M7-blueprint_research-architecture.md (§4 blueprint outputs); context/assessments/2026-06-12_W0_Research_4_Currency_Delta.md (the re-anchored Research-4 ground); context/planning/weeks/2026-W25_jun15-jun21.md (lanes 3–5); homesynapse-core `7c73c91`
-->

# M7/M8 Charter — SKELETON (automation implementation window)

**P1 sizing statement, up front:** automation core does NOT fit in fewer than ~3 first-class pieces. The M6-charter pattern applies: each M7.x below is a first-class backlog row with its own done-when, lane-tracked, one compile-and-commit unit. The smell test (more than ~3 sub-milestones or amendments = split it) is the standing rule; if synthesis grows any piece past it, the piece splits BEFORE issue, not in arrears.

## Entry-gate (M7.1 issues only when ALL rows are green)

| # | Gate | State at authoring (2026-06-12) |
|---|---|---|
| 1 | **M7 entry-gate AMD block RATIFIED** — the AMD-66..71 pattern: Research-4 re-anchored RECs (W0 §5) + R14 M7-OBLIGATION rows → one PROPOSED block → DOCS review → Nick ratifies. Real AMD numbers assign-at-milestone (P2 rule; the Research-4 "AMD-48..52" labels were placeholders) | NOT AUTHORED — drafts after returns ⟨SYNTH⟩ |
| 2 | **B2 C8 `actorRef` RATIFIED** (automations stamp `AutomationId`) — direct M7 contract input | PROPOSED; W25 Lane-5, before the AMD block freezes |
| 3 | **M6 wrap state:** M6.2 committed ✓ (`7c73c91`); **M6.3 issued-or-formally-deferred past M7 start — Nick's call at the W25/W26 boundary** (the architecture doc §6 explicitly does NOT decide M6.3-vs-M7 ordering; this row surfaces it) | OPEN — Lane-2 evidence gates decide |
| 4 | **W25 Lane-4 structural gate:** no new Core coding instruction until M5-C Increment 1 is DONE (P6) | OPEN — Increment 1 not started at authoring |
| 5 | Automation MODULE_CONTEXT current (incl. the 2026-06-12 permit-count correction) + the §4c arch-rule reminder and P2 consumer/pin survey rows pre-built into each M7.x instruction | MODULE_CONTEXT current ✓; survey rows built per-instruction |

## M7 pieces (first-class rows; scope sketches — populated at synthesis)

| Piece | Scope sketch | Done-when (draft) | Population |
|---|---|---|---|
| **M7.1 — Trigger/condition path** | `AutomationRegistry` impl + definition loading through the shipped config substrate (Doc 07 §3.3 ↔ AMD-66/71 reconciliation — W0 §4.2: listener classification for automation reload, AMD-71 placement, fail-closed write posture); `TriggerEvaluator` (trigger index §3.4; AMD-25 `forDuration` timers incl. rebuild-on-REPLAY); `ConditionEvaluator` (AMD-03 single-snapshot); `SelectorResolver` (§3.12). Publishes the run-initiation slice of the M7 event vocabulary | Definitions load/reload through config pipeline with identity stability (§3.3/§4.1); trigger index O(1) verified; `forDuration` timer crash/rebuild tests GREEN ⟨R14-B RQ1 pins⟩; first manifest fan-out lands (pins 55/24/36 → +n) with the survey re-run | ⟨R14-B RQ1/RQ5⟩ ⟨R14-A RQ1/RQ5⟩ |
| **M7.2 — Run/action/dispatch path** | `RunManager` (§3.7 FSM; C2 dedup; C3 ordering; concurrency modes §3.6; cascade governance §3.7.1 on the post-AMD `RunCausalChain` — W0 §2.4); `ActionExecutor` (§3.9 sequential, virtual threads, `UnavailablePolicy`); `CommandDispatchService` (§3.11.1, `CommandValidator`, DIAGNOSTIC events); run-trace data (§4.2) | Run lifecycle + dedup + ordering contract tests GREEN; cascade-depth governor test-pinned (default 8, 1–32); REPLAY re-derive-never-re-execute kill-tests GREEN ⟨R14-B RQ4 crash-window pins⟩; C8 stamping test (`actorRef = AutomationId`) per the ratified C8 | ⟨R14-B RQ2/RQ4⟩ ⟨R14-A RQ5⟩ |
| **M7.3 — Pending Command Ledger** | §3.11.2 FSM (`PendingStatus` 5 states), `Expectation` correlation → `state_confirmed`, deadline/timeout semantics, `CommandIdempotency` + EXPIRED-on-restart, coalescing DISABLED (correctness pin); projection handlers as separate registrations on the existing `DispatchingProjectionAdvancer` (DQ-3, decided) | Ledger FSM + timeout + idempotency contract tests GREEN; restart/EXPIRED kill-tests GREEN ⟨R14-B RQ3/RQ4 pins⟩; ledger events ride the manifest fan-out + survey | ⟨R14-B RQ3⟩ ⟨R14-A RQ3 — differentiator evidence calibrates defaults⟩ |

**Event-vocabulary placement (PM default, synthesis confirms):** the REC-39 automation event records are CONTRACT content — they land with the AMD block (gate row 1), are implemented incrementally by the piece that first publishes each (M7.1 run-initiation slice; M7.2 run-lifecycle/dispatch slice; M7.3 ledger slice), each slice carrying its own manifest fan-out + survey re-run. Alternative (one dedicated event-vocabulary piece first, the M6.1b pattern) is the ⟨SYNTH⟩ fork if the record count lands large.

**Standing M7 carry pins (from W0 — embed in every relevant M7.x instruction):**
1. **Type-residency (W0 §2.5.1):** `RunId`/`RunStatus`/`PendingStatus` MUST NOT appear in event payloads (JPMS cycle); flatten-or-relocate is an AMD-block decision — the instructions inherit whichever the block ratifies.
2. **Manifest fan-out discipline** per event slice (55/24/36 → +n) + the consumer/pin survey INCLUDING behavioral publish-count pins in sibling tests (the M6.4 lesson).
3. **AMD-52 codec discipline** for any typed-value-bearing event (no `@JsonTypeInfo`; tagged-union; exhaustive no-`default`).
4. **C8 stamping** on every automation-originated publish (gate row 2).
5. **§4c Clock-injection reminder** (automation is non-whitelisted) — worded as convention per the 2026-06-11 NO_DIRECT_TIME_ACCESS-reach OQ (do not assert test-source reach).

## M8 pieces (PROVISIONAL — shapes from synthesis; rows named so sizing is visible)

| Piece | Scope sketch | Population |
|---|---|---|
| **M8.1 — Zone/geofence** | DQ-1/DQ-5 (decided): `PresenceTrigger` promotion fields + `ZoneCondition` + evaluation logic + person/location infrastructure | ⟨R14-A RQ1⟩ ⟨R14-B⟩ |
| **M8.2 — Advanced ledger/reliability behaviors** | retry posture, timeout layering, confirmation surfacing — ONLY what the evidence justifies | ⟨R14-B RQ3⟩ ⟨R14-A RQ2/RQ3⟩ |
| **M8.3 — Tier-2 trigger promotions** (`TimeTrigger`/`SunTrigger` scheduler integration) | FUTURE-AMD-dependent (shapes from R14-B RQ1); may fall past M8 | ⟨R14-B RQ1⟩ ⟨SYNTH⟩ |

**M8 ledger-advancer note:** DQ-3 ruled same-advancer-separate-registrations; split into a dedicated advancer at M8 only if handler count becomes unmanageable — re-evaluate at M8 scoping, not before.

## Sequencing + consumers

```
R14/R15 dispatch ──► returns (any order) ──► serialized assessments (B → A → 15)
   ──► merged disposition (REC-31..40 re-anchored + 141..185)
   ──► THIS charter populated + M7 AMD block PROPOSED ──► DOCS review ──► ratify
   ──► entry-gate rows 1–5 green ──► M7.1 instruction (the §4.3 readiness checklist)
Parallel: Lane-2 M6.3 evidence gates (Nick) ──► the W25/W26 M6.3-vs-M7 ordering call (gate row 3)
```

R15 feeds M5-C/strategy ONLY (no rows here cite it for scope — its parking register is checked at synthesis for anything mis-routed).
