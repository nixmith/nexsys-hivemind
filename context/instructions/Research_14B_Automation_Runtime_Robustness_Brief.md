<!--
file: context/instructions/Research_14B_Automation_Runtime_Robustness_Brief.md
purpose: Dispatchable research brief — Research 14-B: Automation Engine Runtime: Robustness Prior Art (engineering register). Gap-relative to the frozen Phase-2 automation surface (Doc 07 + AMD-25 + verified sealed hierarchies), the event-sourced replay discipline (AMD-41/AMD-50 class), and the Research-4 re-anchored disposition state (W0, 2026-06-12).
audience: DOCS Project researcher (primary), PM (assessment), Nick (dispatch)
status: READY TO DISPATCH — authored 2026-06-12 (PM, Cowork) per context/planning/2026-06-11_M7-blueprint_research-architecture.md. Runs SIMULTANEOUSLY with Research 14-A and Research 15 — REC ranges are partitioned; this brief is fully self-contained (never reference a sibling return).
dispatch-target: the DOCS Claude Project (homesynapse-core-docs connector). Engineering prior art needs source/docs citations — WEB SEARCH IS REQUIRED. Fallback if web reach proves too shallow mid-run: return what you have marked INCOMPLETE-EVIDENCE per §3.6 — the PM splits evidence-gathering to a generic deep-research run; the disposition pass is NEVER the generic run.
rec-block: REC-156–170 (reserved; high-water at authoring = REC-140, Research 13; siblings hold 141–155 and 171–185 — do not exceed 170)
baseline: homesynapse-core HEAD `7c73c91` (M6.2) · docs watermark AMD-87 · projectionVersion 5 · event pins 55/24/36
-->

# RESEARCH BRIEF: Research 14-B — Automation Engine Runtime: Robustness Prior Art

*Target: the M7 entry-gate AMD block + M7.x/M8.x coding-instruction obligations + the M7/M8 charter. Date: 2026-06-12.*

You are an engineering prior-art researcher for HomeSynapse Core, a local-first, event-sourced smart home runtime in Java 21 on constrained hardware (Raspberry Pi 4 class). The automation engine's Phase-2 contract surface is **frozen and Locked** (Doc 07 + AMD-25; verified at `7c73c91`); implementation is the upcoming M7/M8 window. Your task is NOT design. It is a **robustness prior-art gap analysis in the engineering register**: how do production systems get temporal triggers, cascade containment, intent-confirmation, run persistence, and event-storm behavior RIGHT (or verifiably wrong) — mapped against the machinery HomeSynapse has already frozen, so the PM can extract implementation obligations, test obligations, and AMD-block content.

**The disposition table (§4b) is the load-bearing deliverable.** A finding without a disposition row is unusable. A "gap" that the frozen contracts already close poisons the pipeline.

---

## 0. Quote-back gate [DO THIS FIRST]

Open your return by quoting back, **verbatim**: (a) the §0.2 `module-info.java` embed; (b) the §0.3.1 inventory-summary line (the bolded counts line); (c) the six rows of the §0.3.3 decided-ground table. If you cannot quote them, STOP and return INCOMPLETE. A return that fails the quote-back is discarded unread past §0.

## 0.1 Authoritative state (do not work from memory)

- homesynapse-core HEAD: **`7c73c91`** (M6.2, 2026-06-11). M6 state: M6.1 ✓ M6.4 ✓ M6.2 ✓; **M6.3 (at-rest encryption) is triple-gated and OUT OF SCOPE for this research.**
- On-disk amendment watermark **AMD-87** · `projectionVersion` **5** · event manifest pins **55 / 24 / 36** (EventTypes / CORE_PRODUCTION_EVENT_CLASSES / EventCategoryMapping).
- The automation module (`core/automation`) is a **Phase-2 contract surface with NO Phase-3 implementation yet** — ~52 public types, 4 sealed hierarchies, 9 service interfaces, frozen. The engine subscribes to an **immutable, event-sourced log with deterministic REPLAY** (the platform's foundational property — see §0.3.3 row 4).
- Research numbering: this is **Research 14-B**, REC range **156–170**. Research 14-A (community/UX register) and Research 15 (strategic register) run simultaneously with their own ranges; you must not reference or anticipate them.

## 0.2 Embedded verbatim — `core/automation/src/main/java/module-info.java` at `7c73c91`

(The standing Research-6 rule: module names and edges are authoritative from this embed, not from any summary. §7 of your return is LIGHT — you must NOT propose module-info changes — but any code-adjacent observation must use these exact identifiers.)

```java
/*
 * HomeSynapse Core
 * Copyright (c) 2026 NexSys. All rights reserved.
 */

/**
 * Automation engine module: trigger-condition-action rules, cascade governor,
 * command dispatch, and pending command tracking.
 *
 * <p>This module defines the public API contracts for the HomeSynapse automation
 * subsystem. It exports sealed type hierarchies (triggers, conditions, actions,
 * selectors), data records (automation definitions, run contexts, pending commands),
 * and service interfaces consumed by the REST API, WebSocket API, Observability,
 * and Lifecycle modules.</p>
 */
module com.homesynapse.automation {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.state;

    // M4.0b-4a: PendingCommand's javadoc references com.homesynapse.value
    // .AttributeValue (via {@link Expectation#evaluate}); declared non-transitive
    // (value is not on automation's public API). The type is also reachable
    // transitively through `requires transitive com.homesynapse.device`; the edge
    // is declared explicitly at its use site per the relocation design note.
    requires com.homesynapse.value;

    exports com.homesynapse.automation;
}
```

## 0.3 Embedded — the frozen/decided ground your findings must be gap-relative to

### 0.3.1 Automation type-inventory summary (MODULE_CONTEXT, source-verified at `7c73c91`)

**~53 public types in ONE FLAT package `com.homesynapse.automation`: 5 enums · 1 typed ULID wrapper (`RunId`) · 4 sealed hierarchies with 30 permits (Selector 6, all Tier 1 · TriggerDefinition 9 = 5 Tier 1 + 4 Tier 2 empty-reserved · ConditionDefinition 7 = 6 Tier 1 + 1 Tier 2 · ActionDefinition 8 = 5 Tier 1 + 3 Tier 2) · 4 data records (`AutomationDefinition` 12 fields, `RunContext` 8 fields, `PendingCommand` 8 fields, `DurationTimer` 8 fields) · 9 service interfaces.** *(Permit total re-derived from source 2026-06-12: 6+9+7+8 = 30.)*

Runtime-relevant facts you must hold: `forDuration` (nullable `Duration`, AMD-25) on 4 of 5 Tier 1 triggers; `EventTrigger` deliberately has NO `forDuration`. `DurationTimer` (8 fields incl. `startingEventId`, `expiresAt`, `virtualThread`) is **NOT persisted — rebuilt from events on REPLAY→LIVE**; keyed (automationId, triggerIndex), at most one per key; cancellation via `Thread.interrupt()`. `RunContext` carries `definitionHash` (SHA-256, replay verification), `cascadeDepth` (int, 0 for root), `stateSnapshotPosition` (long — AMD-03: all conditions in a Run evaluate against ONE snapshot captured at trigger time). `PendingCommand` carries `expectation` (sealed `Expectation` from device-model), `deadline` (Instant), `idempotency` (`CommandIdempotency` from event-model), `status` (`PendingStatus`: DISPATCHED/ACKNOWLEDGED/CONFIRMED/TIMED_OUT/EXPIRED — EXPIRED = NOT_IDEMPOTENT on restart). `RunStatus` includes `INTERRUPTED` (produced during REPLAY→LIVE per Doc 07 §3.10) and `CONDITION_NOT_MET` (does not consume a concurrency slot). Concurrency: `ConcurrencyMode` SINGLE/RESTART/QUEUED/PARALLEL with `maxConcurrent` (default 10 QUEUED/PARALLEL, 1 SINGLE/RESTART). Three independent Phase-3 subscribers planned: `automation_engine`, `command_dispatch_service`, `pending_command_ledger` — each with its own virtual thread and checkpoint. Run execution on virtual threads (LTD-01); SQLite access routes through the persistence platform-thread executor (LTD-03); all time access is Clock-injected (the `NO_DIRECT_TIME_ACCESS` discipline); no `synchronized` blocks (LTD-11).

### 0.3.2 Doc 07 § anchors for THIS register (read these; they are your gap-relative baseline)

From the `homesynapse-core-docs` connector, `design/07-automation-engine.md` (**LOCKED**, AMD-25 integrated) — the runtime machinery:

| Anchor | What it already answers |
|---|---|
| §3.2 Event Subscription | subscriber/checkpoint model; the engine is an event-bus subscriber |
| §3.4 Trigger Evaluation | trigger index (O(1) event-type lookup); `for_duration` semantics (AMD-25): timer start, sustain check, cancellation on counter-evidence |
| §3.5 Trigger Deduplication | dedup keys and scope |
| §3.6 Concurrency Modes | SINGLE/RESTART/QUEUED/PARALLEL; `maxConcurrent` bounds; drop semantics + `MaxExceededSeverity` |
| §3.7 Run Lifecycle (incl. §3.7.1) | run FSM; dedup (automation_id, triggering_event_id) (C2); deterministic ordering (C3); **cascade governance: `cascadeDepth`, `max_cascade_depth` default 8 range 1–32, `cascade_depth_exceeded` DIAGNOSTIC** |
| §3.8 Condition Evaluation | single-`StateSnapshot`-at-trigger-time (AMD-03) |
| §3.10 Replay Behavior | **REPLAY re-derives, never re-executes side effects; timers rebuilt; in-flight runs → `INTERRUPTED` at REPLAY→LIVE** |
| §3.11 Command Pipeline (§3.11.1/§3.11.2) | dispatch routing + validation; **Pending Command Ledger: command_issued → dispatched → acknowledged → confirmed/timed_out; `state_confirmed`; coalescing DISABLED (correctness-critical)** |
| §4.3 Pending Command Entry | the ledger data model (deadline, idempotency, expectation) |
| §6.5–§6.7 Failure Modes | checkpoint expiration; virtual-thread interruption during delay; **event-storm overload** |
| §10 Performance Targets | quantitative targets (investigation triggers, not revision triggers) |

**Minimum read set (the floor — read more if a finding needs it):** Doc 07 §3.2, §3.4–§3.8, §3.10, §3.11, §4.2–§4.3, §6.5–§6.7, §10; `design/01-event-model.md` §3 (envelope/ordering) and §4.3 (taxonomy); `design/amendments/AMD-25_*.md` (for_duration) if present in the connector. Every RQ finding must state which anchor (or §0.3 register item) it is relative to. "Automations should survive restart" is a FAILED finding — §3.10 + the timer-rebuild rule already answer it — unless it identifies a *specific delta* with evidence.

### 0.3.3 Decided ground beyond Doc 07 (the W0 re-anchor, 2026-06-12 — quote these rows back in §0)

| # | Decided item | Status |
|---|---|---|
| 1 | **DQ resolutions (Nick, 2026-05-30):** Pending-Command-Ledger projection handlers register on the existing `DispatchingProjectionAdvancer` (separate registrations; split only at M8 if unmanageable); zone/geofence evaluation = M8 | **DECIDED — not open questions** |
| 2 | **REC-36 (re-anchored):** `RunContext.cascadeDepth: int` will be REPLACED by `causalChain: RunCausalChain` in the M7 AMD block (supersedes AMD-04); the `depth()` accessor feeds the §3.7.1 governor unchanged | **ACCEPTED, pending the M7 AMD block** |
| 3 | **REC-39 (re-anchored, HIGH):** the M7 automation event vocabulary lands in `com.homesynapse.event` (flat) under a type-residency rule — **automation-resident types (`RunId`, `RunStatus`, `PendingStatus`) MUST NOT appear in event payloads** (JPMS cycle); flattened identifiers or relocation = an AMD-block decision; every new event type rides the manifest fan-out (55/24/36 + consumer/pin survey) | **ACCEPTED, pending the M7 AMD block** |
| 4 | **The replay hazard class is named:** side-effecting subsystems re-derive state during REPLAY but NEVER re-execute side effects (the AMD-41-class rule; Doc 07 §3.10 applies it to automation). Run-persistence findings must be expressed against this rule | **LOCKED discipline** |
| 5 | **C8 `actorRef` (PROPOSED 2026-06-08):** automations stamp `actorRef = AutomationId` on every command/event they originate; bare `Ulid` envelope field unchanged | **PROPOSED — ratification on the W25 critical path** |
| 6 | **Co-design carry-pin discipline (the OR-M6-NONCE pattern):** crash/restore-correctness hazards (your RQ4 findings) land as EXPLICIT carry pins in milestone rows, co-designed with the features they interact with — your job is to identify the hazards precisely enough to pin | **STANDING process rule** |

---

## 1. Research questions (answer ALL five; engineering register, source/docs citations)

### RQ1 — Temporal-trigger correctness prior art

How do production systems handle: DST transitions (the 2:30am-doesn't-exist / happens-twice classes); clock skew and NTP step corrections; downtime catch-up (missed-while-down: fire-on-boot vs skip vs configurable — cf. cron vs anacron vs systemd timers `Persistent=`; Quartz misfire instructions); monotonic-vs-wall-clock discipline for durations. Survey at minimum: cron/anacron, systemd timers, Quartz (misfire policy taxonomy), HA time triggers (cited bug history), and one event-sourced/workflow system (e.g., Temporal durable timers). Gap-relative baseline: AMD-25 `forDuration` semantics (§3.4), the Clock-injection discipline, `DurationTimer` rebuilt-from-events on REPLAY (§0.3.1) — and the fact that `TimeTrigger`/`SunTrigger` are **Tier-2 empty-reserved** (their field shapes are FUTURE design; your findings inform what those shapes must eventually accommodate, routed FUTURE-AMD). Verdict per finding: which correctness behaviors are M7 obligations for `forDuration` (test obligations especially), which are FUTURE-AMD input for the Tier-2 promotions.

### RQ2 — Cascade/loop containment prior art

How do engines bound runaway automation chains? Survey: HA (no structural loop protection — cite the evidence and the workarounds), Node-RED loop patterns, rule-engine literature (Rete-class infinite loop guards, trigger-depth limits in DB trigger systems — e.g., SQL Server's 32-level nesting cap), workflow engines (max recursion/child-workflow depth). Gap-relative: §3.7.1 `cascadeDepth` + `max_cascade_depth` (default 8, range 1–32) + `cascade_depth_exceeded` DIAGNOSTIC; the REC-36 `RunCausalChain` replacement (§0.3.3 row 2) which makes the full causal chain first-class. Verdict: is depth-bounding alone sufficient per prior art, or does the evidence justify cycle-detection (same-automation-in-chain), rate-based containment, or storm-coupling — and at which disposition (M7 vs M8 vs FUTURE-AMD)?

### RQ3 — Intent-confirmation / command-ledger prior art

Where has the command-ack-confirm pattern been engineered well? Survey: messaging QoS ladders (MQTT QoS 0/1/2 semantics + their failure modes), Zigbee APS acks vs default-response semantics, k8s declarative reconciliation (the desired-state alternative to imperative confirm), industrial/SCADA command-verification practice, and any home-automation system with delivery confirmation. For each: the ack taxonomy (transport-ack vs application-ack vs state-confirmation), timeout/retry semantics, idempotency handling, and the failure modes (duplicate execution, ack-lost-but-executed, confirmation-by-stale-state). Gap-relative: §3.11.2 ledger FSM (`PendingStatus` 5 states), `Expectation`-evaluated state confirmation, `deadline`, `CommandIdempotency` + EXPIRED-on-restart, coalescing DISABLED (§0.3.1). Verdict: which ledger behaviors (timeout layering, retry posture — note the frozen surface has NO retry field — duplicate-confirmation handling, deadline defaults) become M7/M8 obligations vs FUTURE-AMD.

### RQ4 — Run persistence/recovery across restart (the event-sourced interaction)

The hardest RQ; co-design carry pins come from here (§0.3.3 row 6). How do systems persist/recover in-flight work across crash/restart, and what goes WRONG: timers lost or double-fired on recovery; in-flight steps re-executed (the side-effect replay hazard — §0.3.3 row 4 is our rule); recovery ordering races (subsystem acts on half-rebuilt state); checkpoint-vs-side-effect atomicity (the exactly-once lie). Survey: workflow engines with event-sourced recovery (Temporal/Cadence replay + side-effect isolation is the canonical prior art), Akka persistence, BPM engines, and HA's restart behavior for `delay`/`wait` (cited losses). Gap-relative: §3.10 (re-derive-never-re-execute; `INTERRUPTED` runs; timer rebuild from events), `DurationTimer.startingEventId` dedup, `RunContext.definitionHash` (replay verification), `stateSnapshotPosition` (AMD-03), the three-subscriber/three-checkpoint model (§0.3.1), `PendingStatus.EXPIRED` (NOT_IDEMPOTENT on restart). Verdict: enumerate the crash-window hazard list the M7.x instructions must carry as explicit pins (the kill-mid-flight test pattern: crash injected at each window, recovery asserted — name each window precisely), and any genuine contract gap → FUTURE-AMD.

### RQ5 — Event-storm behavior

How do event-driven systems behave under burst load, and which postures work: bounded queues + drop policies, backpressure propagation (Reactive Streams), coalescing/debouncing (and where coalescing is WRONG — our ledger forbids it), load-shedding by priority, pathological feedback (storm → automation → more events). Survey: reactive-streams practice, MQTT broker overload behavior, HA event-storm incidents (cited), stream-processing backpressure (Kafka consumer lag semantics). Gap-relative: §6.7 (event-storm failure mode), QUEUED/PARALLEL `maxConcurrent` bounds, `MaxExceededSeverity` drop logging, coalescing-DISABLED-for-the-ledger (correctness), the trigger index (§3.4), §10 targets. Verdict: which storm behaviors are structurally closed, which need M7/M8 test obligations (storm simulation), which justify FUTURE-AMD (e.g., per-automation rate limits — note `maxConcurrent` bounds runs, not trigger evaluations).

---

## 2. Mandatory document format

```
# Research 14-B: Automation Engine Runtime — Robustness Prior Art
*Target: HomeSynapse M7 AMD block + M7.x/M8.x instructions + M7/M8 charter. Date: YYYY-MM-DD.*

## 0. Quote-back gate [M — FIRST] — per §0 above.

## 1. Executive Summary [M] — 5–8 verdict bullets; every bullet takes a position with a
     one-sentence defense. "X is worth investigating" is banned. Flag the single
     highest-impact finding AND the single nastiest crash-window hazard found.

## 2. Prior-Art Deep Dives [M] — one subsection per system/domain surveyed (the RQ1–RQ5
     coverage above). Each: (a) the mechanism, precisely (semantics, defaults, bounds);
     (b) ≥1 direct quotation from a primary source (docs, source code, issue tracker,
     post-mortem) WITH URL; (c) documented failure modes; (d) the gap-relative lesson,
     citing the §0.3 anchor it is relative to.

## 3. Cross-Cutting Analysis [M]
   - 3.1 Mechanism concept map: concern (temporal | cascade | confirmation | recovery |
         storm) | surveyed systems' answers | HomeSynapse frozen mechanism (cited anchor).
   - 3.2 The crash-window hazard table (RQ4): hazard → prior-art mitigation →
         HomeSynapse mechanism → CLOSED / CLOSED-UNTESTED (→ named test obligation) / OPEN.
   - 3.3 The ledger semantics matrix (RQ3): ack layer → prior art → §3.11.2 mapping.
   - 3.4 Over-engineering check: frozen machinery the prior art says is unnecessary —
         defend or flag each (honesty section; REJECT-candidates).

## 4. Findings + Recommendations [M]
   - 4a. REC-numbered findings, REC-156 through at most REC-170, ranked
         (impact × confidence)/cost. Each REC: the concern class; evidence (≥1 primary
         source); gap-relative statement; concrete recommendation; effort class (S/M/L, prose).
   - 4b. THE DISPOSITION TABLE [M — load-bearing]: EVERY REC maps to EXACTLY ONE of:
           ALREADY-COVERED (cite the specific Doc 07 §N / AMD-NN / §0.3.3 row)
         | M7-OBLIGATION (AMD-block/instruction item INSIDE frozen contracts —
           typically a test obligation, a default, a carry pin)
         | M8-OBLIGATION (same, M8 scope)
         | FUTURE-AMD (contract delta sketch — do NOT draft it; Tier-2 promotion
           field-shape input lands here)
         | POST-MVP (UI/cloud lane)
         | REJECT (reasoned — prior art says HomeSynapse should NOT do this).
         No REC in two buckets. No bucket empty by laziness — if genuinely empty, say why.

## 5. Caveats and Open Questions [M] — source reliability; spike candidates (anything
     needing empirical validation on Pi-4-class hardware); explicit INCOMPLETE-EVIDENCE
     declaration if web reach was too shallow.

## 6. Appendix: Sources [M] — URL families grouped by system; every factual claim traceable.

## 7. HomeSynapse Code-Level Implications [LIGHT] — observations ONLY, routed through §4b.
     NO module-info proposals, NO new types, NO contract drafts. Exact §0.2/§0.3.1
     identifiers only.
```

## 3. Evidence standards (non-negotiable)

1. **Primary sources with URLs.** Official docs, source code, issue trackers, post-mortems, specs (the MQTT/Zigbee specs are primary; a blog summarizing them is secondary). A claim without a citation is a vibe.
2. **Engineering claims need source/docs citations**; failure-mode claims are strongest as documented incidents/post-mortems or maintainer-acknowledged issues.
3. **Precision over breadth.** "Quartz has misfire policies" is useless; the policy taxonomy with semantics and defaults is the finding.
4. **Take positions.** Every section concludes with a verdict. "Worth investigating" is banned.
5. **Gap-relative or it didn't happen.** Every finding cites its §0.3 anchor. Findings that re-propose frozen machinery score ALREADY-COVERED, not recommendations.
6. **No fabricated identifiers.** Type/module names come from §0.2/§0.3.1 verbatim. If you need a HomeSynapse fact not embedded here and not in the connector, request it in §5 — do not reconstruct it. **Web search is required**; if reach is too shallow, declare INCOMPLETE-EVIDENCE in §5 rather than padding. Any external-standard constant you cite (spec timeouts, protocol values) must carry its source citation verbatim.

## 4. Guardrails (violations = the finding is discarded)

1. **Locked ground is the baseline to measure against, never an open question.** The TCA model, sealed permits, AMD-25 semantics, the re-derive-never-re-execute rule, coalescing-disabled, the single-snapshot rule (AMD-03), virtual-thread execution (LTD-01), Clock injection — none of these are open. "Use a different concurrency model" is a discarded finding. The §0.3.3 decided rows are DECIDED — do not re-open them.
2. **No M6.3 creep.** At-rest encryption, nonce machinery, encrypted-scope sets are triple-gated elsewhere; nothing here touches them. (The OR-M6-NONCE *pattern* — crash/restore co-design pins — is cited as process discipline only.)
3. **You cannot change contracts.** Contract-change implications route to FUTURE-AMD dispositions; you never draft amendment text, types, or module-info changes. Tier-2 trigger promotions (`TimeTrigger`, `SunTrigger`) are FUTURE design — your RQ1 findings *inform* their eventual shape via FUTURE-AMD rows.
4. **REC numbering: 156–170 ONLY** (append-only global register; siblings own 141–155 and 171–185; high-water 140).
5. **Stay in register.** This brief is engineering prior art. User complaints, forum archaeology, and UX evidence are the SIBLING research's register — if you trip over strong community evidence, note it in §5 as out-of-register, one line, and move on.
6. Produce ONE complete markdown document. Do not truncate.

## 5. What the PM does with the return (so you aim at it)

The PM runs the standard 6-step A–F assessment, source-verified. **Your return is folded FIRST** (engineering constrains what the engine can promise; the sibling evidence then prioritizes which promises matter). Disposition rows route: ALREADY-COVERED → coverage attestation; M7-OBLIGATION → AMD-block content + M7.x instruction test requirements and carry pins (your §3.2 crash-window table feeds these directly — the OR-M6-NONCE-pattern pins); M8-OBLIGATION → M8 charter rows; FUTURE-AMD → Nick's queue (Tier-2 promotion shapes); POST-MVP → parked; REJECT → anti-requirements with reasoning. A finding that cannot be placed in that machine is a finding you should sharpen or drop.
