<!--
file: context/planning/2026-06-12_M7-blueprint_merged-disposition.md
purpose: THE merged disposition pass (research architecture §4) — ONE table spanning REC-31..40 (W0 re-anchored) + REC-141..185 (R14-A/R14-B/R15, PM-assessed), collisions adjudicated. This is the single authority the M7 AMD block, the M7.x instructions, the M8 rows, the M5-C backlog, and the strategy refresh draw from. Supersedes nothing; consolidates the three assessments + W0.
audience: PM (AMD-block drafting), Nick (ratification view), Coder (at instruction time, via instructions)
state-type: planning
status: COMPLETE 2026-06-12 — all four inputs folded in order (W0 → 14-B → 14-A → 15); research high-water now REC-185
anchors: the three 2026-06-12 PM assessments + 2026-06-12_W0_Research_4_Currency_Delta.md; collision rules per 2026-06-11_M7-blueprint_research-architecture.md §4
-->

# M7 Blueprint — Merged Disposition (REC-31..40 + 141..185)

## 1. Collisions adjudicated (the merged-pass actions)

1. **REC-33 ⊕ REC-143 ⊕ REC-144 ⊕ REC-161 → ONE AMD item:** `ConfirmationPolicy` opt-in (REC-33, Research 4) + the named default (off; on where `Expectation` is cheap — REC-144 w/ the frenck double-actuation rationale) + default `confirmation_timeout_ms` config key (REC-143/161) + the Pi-4 round-trip **calibration spike** (REC-161). Evidence-grade rule applied: R14-A community evidence prioritizes; R14-B prior art constrains.
2. **REC-36 ⊕ REC-158 → ONE AMD item:** `cascadeDepth → causalChain: RunCausalChain` (supersedes AMD-04) now CARRIES same-automation-in-chain detection with a **distinct diagnostic event** (vs the depth diagnostic). The new event type rides the manifest fan-out.
3. **REC-153a ⊕ REC-136 (R13 FUTURE-AMD queue):** M7's dangling-reference load validation partially discharges the queued REC-136 reference-integrity family for automation-internal refs; the queue entry is annotated, not closed (config-side refs remain).
4. **REC-182 ← R14-A RQ2 evidence:** re-bucketed FUTURE-PARKING → M5-C-WEBSITE-INPUT (the competitor-pain match exists: HA #117133 trace eviction, Hubitat provenance complaint, Homey timeline-as-debugger + Six-Battlefields B1/B3/B5).
5. **REC-147 → ALREADY-COVERED:** Doc 07 :270 already specifies `automation_run_skipped`/`automation_run_cancelled` DIAGNOSTICs; default INFO frozen. Test-pins carried to M7.2.
6. **REC-173 verdict flip (within bucket):** Apache 2.0 (LOCKED, file 2) is CONFIRMED by the fork-pattern evidence; governance-posture refinement survives.
7. **Anti-requirements register (consolidated):** REC-155 no templating DSL · REC-162 no engine-level retry · REC-151 no destructive forced migration · REC-181 never lead with commodity-encryption claims (positioning). Each with its evidence citation, embedded in M7.x instructions / M5-C copy rules as applicable.

## 2. The merged table

### 2a. M7 AMD block (entry-gate row 1) — **six families** (the AMD-66..71 sizing class; real numbers assign-at-milestone per P2)

| Family | Content | Source RECs |
|---|---|---|
| **F1 Trigger block** | `CalendarTrigger`/`ReachabilityTrigger`/`ManualTrigger` new permits; `WebhookTrigger`+`PresenceTrigger` promotions (DQ-1 shape — geofence fields M8); `triggerId()` | 31, 32, 37, 38 |
| **F2 Selector block** | `SemanticTagSelector` permit; `includedCategories` on entity-targeting permits (breaking — construction-site sweep) | 34, 35 |
| **F3 Action block** | `confirmation()` / `ConfirmationPolicy` + named default + `confirmation_timeout_ms` default key; `RepeatAction`; `ActivateSceneAction`→`InvokeAutomationAction` rename+promotion (DQ-2) | 33⊕143⊕144⊕161, 40, 37 |
| **F4 RunCausalChain** | `cascadeDepth: int` → `causalChain: RunCausalChain` (supersedes AMD-04); same-automation cycle detection + distinct diagnostic | 36⊕158 |
| **F5 Event vocabulary** | The M7 automation event records in `com.homesynapse.event` (flat): the Doc-07 inventory (`automation_triggered` w/ `matched_triggers`/`resolved_targets`/`definition_hash`, `automation_condition_evaluated`, `automation_action_started/completed`, `automation_completed`, `automation_run_skipped`, `automation_run_cancelled`, `trigger_duration_*`, `cascade_depth_exceeded`, + F4's cycle diagnostic) under the **type-residency rule** (W0 §2.5.1: no `RunId`/`RunStatus`/`PendingStatus` in payloads — flatten-or-relocate DECIDED HERE); full manifest fan-out per slice (55/24/36 → +n) + survey incl. publish-count pins; AMD-52 codec discipline for typed values; C8 stamping via envelope only | 39 (W0-re-anchored, 5 obligations), 141-inventory, 147-events |
| **F6 Definition-schema posture** | `automations.yaml` `(major,minor)` schema_version + forward-only idempotent migration guarantee stated (rides AMD-67 substrate; Doc 07 §4.1 :584 already registers it as a Doc 06 §7 secondary doc); dangling-reference load validation (§6.1) | 150, 153a⊕136 |

### 2b. M7.x instruction obligations (NOT AMD content — tests, pins, defaults inside frozen/ratified contracts)

| Piece | Obligations (REC) |
|---|---|
| **M7.1 trigger/condition path** | Monotonic-seam sustain arithmetic + clock-step test (156, NO_DIRECT_TIME_ACCESS-safe seam); DST-spanning `forDuration` test (167); `definitionHash` mid-flight-edit test w/ C7/P5 (165); storm benchmark harness — trigger-eval path, §10 targets as investigation triggers (157); edge-vs-level schema descriptions + WARNING-class misuse validation (148); W2 kill-mid-sustain test |
| **M7.2 run/action/dispatch path** | Trace-detail test-pins — all four §4.2/:270/:379 details (141); `automation_run_skipped`/`run_cancelled` test-pins + never-default-SILENT attestation (147); W4 narrowed barrier pin — LIVE-transition interleaving across the 3 subscribers (159); W5/W7 zombie-Run + hash tests; cycle-detection tests (158/F4) |
| **M7.3 Pending Command Ledger** | W1 kill-between-dispatch-and-ledger-write test per idempotency class (160); transport-ack ≠ CONFIRMED test (163); stale-`state_reported` confirmation test, log-position-anchored (164, mechanism-corrected); W8 EXPIRED-on-restart test; `PendingStatus` trace surfacing test (143); 7-day-DIAGNOSTIC-window failed-run forensics note + in-window assembly test (145) |
| **Cross-piece** | The W1–W8 crash-window vocabulary is the standing carry-pin namespace; anti-requirements 155/162/151 embedded in every relevant instruction |

### 2c. M8 rows

| Row | Content (REC) |
|---|---|
| M8.1 zone/geofence | unchanged (DQ-1/DQ-5 decided ground) |
| M8.2 advanced ledger/reliability | confirmation-driven remediation — re-issue on TIMED_OUT, the `amitfin/retry` `expected_state` pattern (152); storm×cascade coupling observability (169); recovery thundering-herd bound (170 — WATCH: promote to M7 hardening if M7.2 recovery tests show Pi-4 SQLite pressure) |
| M8.3 Tier-2 promotions | misfire/DST posture field-shape input parked (166) |

### 2d. FUTURE-AMD queue additions

REC-166 (Tier-2 `TimeTrigger`/`SunTrigger` misfire+DST shape) · REC-168 (per-automation trigger-eval rate limit) · REC-153b (stable entity-reference indirection) — join the existing queue (REC-136 [annotated per §1.3], REC-138/§12.4, tag-preserving emitter).

### 2e. M5-C website/docs content backlog (the P6 lane — now evidence-rich)

INV-CE-01 split-brain immunity (R13) · no-cloud-account/no-phone-home flagship (171) · ledger-gap dossier — category-of-one confirmation-of-intent (142/R14-A §3.3) · event-sourced explainability w/ R14-A pain citations (182, re-bucketed) · Data-Act/CRA alignment, dated (174) · Apple-contrast (175) · Matter-friction contrast, positioning-register (176) · cloud-shutdown narrative (179) · structural-absence claims: no trace ring buffer (145), no templating DSL (155) · **copy guardrails:** "controls Matter devices locally" never unqualified "Matter" (172); never lead with commodity encryption (181); privacy-first messaging only for prosumer/EU segments (180)

### 2f. Strategy-refresh drafts (PM drafts → Nick vetoes)

172 Matter economics+fence (file 2/Tier-3) · 173+183 governance-credibility note, license re-affirmed (file 2) · 178 OHF-model governance input (file 3) · 180 segment messaging rule (files 1/3) · 184 Grid/Assure = hypothesis, M5-D interviews cited as the test (files 2/3/4) · 185 unsized-segment risk note (files 3/4) · + the PM-observed file-4-vs-file-2 data-monetization-tension reconciliation line (R15 assessment Step F)

### 2g. ALREADY-COVERED attestations (coverage record; no action)

142 (ledger differentiator — Locked §3.11.2) · 146 (C8 provenance — evidence handed to ratification) · 147 (drop DIAGNOSTICs :270 + INFO default) · 149 (validation surfacing §6.1/AMD-71) · 151 (forced-migration anti-req — AMD-67/§3.3) · R14-B §3.2 W5/W8 (zombie finalization §3.10; EXPIRED §3.11.2) · survive-restart/timer-rebuild (§3.10) · coalescing-disabled (§3.11.2)

## 3. Sizing + sequencing read-out (for the charter)

The AMD block lands at **six families** — the AMD-66..71 class exactly; one PROPOSED block → one DOCS review → one ratification. The M7 milestone holds at **three pieces** (P1 smell test passes; F5 event slices distribute per piece, confirming the charter's PM default — no dedicated event-vocabulary piece needed). **Spike candidates before/at M7.3:** deadline calibration (161) · storm threshold (157, M7.1) · recovery-herd measurement (170, M8 unless promoted). Research high-water: **REC-185**.
