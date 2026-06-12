<!--
file: context/instructions/Research_14A_Automation_UX_Failure_Modes_Brief.md
purpose: Dispatchable research brief — Research 14-A: Automation Authoring & Operating UX: Failure Modes (community-evidence / Mom-Test register). Gap-relative to the frozen Phase-2 automation surface (Doc 07 + AMD-25 + the verified sealed hierarchies) and the Research-4 re-anchored disposition state (W0, 2026-06-12).
audience: DOCS Project researcher (primary), PM (assessment), Nick (dispatch)
status: READY TO DISPATCH — authored 2026-06-12 (PM, Cowork) per context/planning/2026-06-11_M7-blueprint_research-architecture.md. Runs SIMULTANEOUSLY with Research 14-B and Research 15 — REC ranges are partitioned; this brief is fully self-contained (never reference a sibling return).
dispatch-target: the DOCS Claude Project (homesynapse-core-docs connector). ALL FIVE RQs are web-evidence-heavy — WEB SEARCH IS REQUIRED. Fallback if web reach proves too shallow mid-run: return what you have marked INCOMPLETE-EVIDENCE per §3.6 — the PM splits evidence-gathering to a generic deep-research run; the disposition pass is NEVER the generic run.
rec-block: REC-141–155 (reserved; high-water at authoring = REC-140, Research 13; siblings hold 156–170 and 171–185 — do not exceed 155)
baseline: homesynapse-core HEAD `7c73c91` (M6.2) · docs watermark AMD-87 · projectionVersion 5 · event pins 55/24/36
-->

# RESEARCH BRIEF: Research 14-A — Automation Authoring & Operating UX: Failure Modes

*Target: the M7/M8 charter priorities + the M7 entry-gate AMD block + M5-C website/docs superiority material. Date: 2026-06-12.*

You are a market-evidence researcher for HomeSynapse Core, a local-first, event-sourced smart home runtime in Java 21. The automation engine's Phase-2 contract surface is **frozen and Locked** (Doc 07 + AMD-25; the sealed hierarchies below are source-verified at `7c73c91`). Your task is NOT design. It is a **community-evidence gap analysis in the Mom-Test register**: catalogue where automation systems actually break real users — authoring, debugging, trusting, and maintaining automations — then map every finding against the contract ground HomeSynapse has **already frozen or decided**, so the PM can see what is covered, what becomes an M7 or M8 obligation, what warrants a future amendment, and what is honest REJECT.

**The disposition table (§4b) is the load-bearing deliverable.** A finding without a disposition row is unusable. A "gap" that is actually covered by frozen machinery you didn't read poisons the pipeline.

---

## 0. Quote-back gate [DO THIS FIRST]

Open your return by quoting back, **verbatim**: (a) the §0.2 `module-info.java` embed; (b) the §0.3.1 inventory-summary line (the bolded counts line); (c) the five rows of the §0.3.3 decided-ground table. If you cannot quote them, STOP and return INCOMPLETE. A return that fails the quote-back is discarded unread past §0.

## 0.1 Authoritative state (do not work from memory)

- homesynapse-core HEAD: **`7c73c91`** (M6.2, 2026-06-11). M6 state: M6.1 ✓ M6.4 ✓ M6.2 ✓; **M6.3 (at-rest encryption) is triple-gated and OUT OF SCOPE for this research.**
- On-disk amendment watermark **AMD-87** · `projectionVersion` **5** · event manifest pins **55 / 24 / 36** (EventTypes / CORE_PRODUCTION_EVENT_CLASSES / EventCategoryMapping).
- The automation module (`core/automation`) is a **Phase-2 contract surface with NO Phase-3 implementation yet** — ~52 public types, 4 sealed hierarchies, 9 service interfaces, all frozen. Implementation is the M7/M8 window this research feeds.
- Research numbering: this is **Research 14-A**, REC range **141–155**. Research 14-B (engineering register) and Research 15 (strategic register) run simultaneously with their own ranges; you must not reference or anticipate them.

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

Key facts you must hold: Tier 1 triggers = `StateChangeTrigger`, `StateTrigger`, `EventTrigger`, `AvailabilityTrigger`, `NumericThresholdTrigger`; Tier 2 reserved (empty records) = `TimeTrigger`, `SunTrigger`, `PresenceTrigger`, `WebhookTrigger`. Tier 1 actions = `CommandAction`, `DelayAction`, `WaitForAction`, `ConditionBranchAction`, `EmitEventAction`; Tier 2 = `ActivateSceneAction`, `InvokeIntegrationAction`, `ParallelAction`. Conditions: `StateCondition`, `NumericCondition`, `TimeCondition`, `AndCondition`, `OrCondition`, `NotCondition` + Tier 2 `ZoneCondition`. Enums: `ConcurrencyMode` (SINGLE/RESTART/QUEUED/PARALLEL), `RunStatus` (7 values incl. `CONDITION_NOT_MET` — does not consume a mode slot — and `INTERRUPTED`), `PendingStatus` (DISPATCHED/ACKNOWLEDGED/CONFIRMED/TIMED_OUT/EXPIRED), `UnavailablePolicy` (SKIP/ERROR/WARN), `MaxExceededSeverity` (SILENT/INFO/WARNING). `forDuration` (AMD-25) exists on 4 of 5 Tier 1 triggers; `EventTrigger` deliberately has none (events don't "sustain").

### 0.3.2 Doc 07 § anchors for THIS register (read these; they are your gap-relative baseline)

From the `homesynapse-core-docs` connector, `design/07-automation-engine.md` (**LOCKED**, AMD-25 integrated) — the UX-facing machinery:

| Anchor | What it already answers |
|---|---|
| §3.3 Automation Registry | definition identity stability (`AutomationId` assigned at first load, preserved across reloads via `automations.ids.yaml`), slug matching, 30-day retention, hot-reload with in-progress-Run preservation (C7) |
| §3.6 Concurrency Modes | SINGLE (default, drop + `MaxExceededSeverity` logging), RESTART, QUEUED/PARALLEL bounded by `maxConcurrent` |
| §3.7 Run Lifecycle (incl. §3.7.1) | EVALUATING → RUNNING → terminal; dedup by (automation_id, triggering_event_id) (C2); priority-then-id execution order (C3); cascadeDepth governance — `max_cascade_depth` default 8, range 1–32, `cascade_depth_exceeded` DIAGNOSTIC |
| §3.9 Action Execution | sequential on a virtual thread; per-command `UnavailablePolicy` |
| §3.10 Replay Behavior | REPLAY re-derives without re-executing side effects; `INTERRUPTED` runs at REPLAY→LIVE |
| §3.11 Command Pipeline (§3.11.1/§3.11.2) | Command Dispatch Service + **Pending Command Ledger** — command_issued → dispatched → acknowledged → confirmed/timed_out, `state_confirmed` events, coalescing DISABLED (correctness-critical) |
| §3.12 Selectors | 6 types; resolved to `Set<EntityId>` at trigger time; compound = intersection |
| §4.1 Definition Schema | `automations.yaml` shape, slug identity, ids companion file |
| §4.2 Run Trace Data Model | the run-trace observability surface ("why didn't it fire?" raw material) |
| §6.1–§6.7 Failure Modes | definition-validation failure, run failure, dispatch routing failure, confirmation timeout, checkpoint expiration, interruption, event storm |
| §9 Configuration / §11 Observability | config keys + metrics surface |

**Minimum read set (the floor — read more if a finding needs it):** Doc 07 §3.3, §3.6, §3.7 (incl. §3.7.1), §3.9–§3.13, §4.1–§4.3, §6.1–§6.7, §9, §11; `design/01-event-model.md` §4.3 (event taxonomy) for any event-adjacent claim. Every RQ finding must state which anchor (or §0.3 register item) it is relative to. "HomeSynapse should add run tracing" is a FAILED finding — §4.2 already defines it — unless it identifies a *specific delta* with evidence.

### 0.3.3 Decided ground beyond Doc 07 (the W0 re-anchor, 2026-06-12 — quote these rows back in §0)

| # | Decided item | Status |
|---|---|---|
| 1 | **DQ resolutions (Nick, 2026-05-30):** promote `PresenceTrigger` (no separate ZoneTrigger); rename `ActivateSceneAction` → `InvokeAutomationAction` + promote (scenes = automations-with-`ManualTrigger`); Pending-Command-Ledger projection handlers ride the existing advancer; zone/geofence evaluation = M8, not M7 | **DECIDED — not open questions** |
| 2 | **M7 trigger additions (Research 4, re-anchored 2026-06-12):** `CalendarTrigger`, `ReachabilityTrigger`, `ManualTrigger` new permits + `WebhookTrigger`/`PresenceTrigger` promotions → 9→12 permits; `RepeatAction` +1; `SemanticTagSelector` +1; trigger `id` field; `ConfirmationPolicy` opt-in | **ACCEPTED, pending the M7 AMD block** |
| 3 | **C8 `actorRef` (PROPOSED 2026-06-08):** automations stamp `actorRef = AutomationId` on every command/event they originate; bare `Ulid` envelope field unchanged; kind recoverable by typed-ID provenance | **PROPOSED — ratification on the W25 critical path** |
| 4 | **Automation definitions load through the shipped M6 config pipeline** (AMD-66 listener classification for reload, AMD-71 layout, fail-closed write posture for tag-bearing docs) | **SHIPPED substrate (M6.1/M6.2/M6.4)** |
| 5 | **The Pending Command Ledger is the reliability differentiator** — intent-confirmation (did the light ACTUALLY turn on?) is first-class, coalescing disabled, `Expectation`-evaluated confirmation | **LOCKED (Doc 07 §3.11.2)** |

---

## 1. Research questions (answer ALL five; community evidence, Mom-Test standard)

### RQ1 — Authoring failure catalog

Where do **Home Assistant automations/scripts (YAML + UI editor), Node-RED flows, SmartThings Routines, Hubitat Rule Machine, and Homey Flows** actually break users at authoring time? Cover at minimum: syntax/indentation/templating failures (HA Jinja2 templates are the canonical class); mental-model failures (trigger vs condition confusion, edge vs level semantics, mode misunderstanding); refactoring churn (renaming an entity breaks N automations silently); the blank-page problem vs the it-grew-into-spaghetti problem; versioning/diffing of automation definitions. For each failure class: what happened (cited), the user-visible blast radius, and the gap-relative verdict against §0.3 (e.g., HomeSynapse's edge-vs-level split is *structural* — `StateChangeTrigger` vs `StateTrigger` are distinct sealed permits, not a YAML mode flag — does the evidence say that distinction prevents the confusion class or merely relocates it?).

### RQ2 — Debuggability: the "why didn't it fire?" problem

The single most valuable RQ. What run-trace/observability do the surveyed platforms offer (HA traces, Hubitat logs, Node-RED debug nodes), what do users *actually use* when an automation misfires, and what do they beg for in forums and issue trackers? Catalogue the diagnostic questions users ask (didn't trigger? trigger fired but condition false? condition true but action failed? fired but device didn't respond?) and which each platform can/cannot answer. Gap-relative baseline: Doc 07 §4.2 run-trace model + §11 observability + the ledger's command-level confirmation. Verdict per finding: does HomeSynapse's frozen surface already capture the data to answer each diagnostic question, and what M7/M8 obligation (a trace detail, an event, a retention rule — within frozen contracts) does the evidence justify?

### RQ3 — Reliability expectations and the confirmation gap

What do users **assume** about command delivery (fire-and-forget vs confirmed), retries, and offline devices — and where does reality betray them? The Pending Command Ledger (§0.3.3 row 5) is our differentiator: **find the evidence that proves the market gap.** Document: cited stories of "the automation ran but the light stayed off"; how each platform handles (or silently drops) unconfirmed commands; what retry/timeout semantics exist anywhere; whether ANY surveyed platform closes the intent-to-observation loop as a first-class feature. Mom-Test: users who installed verification hacks (wait + re-check state, double-fire, watchdog automations) are the strongest signal. Verdict: which ledger behaviors (timeout defaults, `UnavailablePolicy` ergonomics, confirmation surfacing) the evidence makes M7/M8 obligations vs FUTURE.

### RQ4 — Definition migration/versioning churn

Evidence on automation-definition churn across platform upgrades: HA breaking changes to automation YAML schema; SmartThings Groovy→Lua/Routines forced migrations (the canonical trust-destruction case); Hubitat Rule Machine version migrations (rules frozen at legacy RM versions); Node-RED flow-format evolution. What did users *do* (abandon, freeze versions, migrate away)? Gap-relative: AMD-67 `(major,minor)` forward-only idempotent migration machinery exists for config documents and `automations.yaml` loads through that pipeline (§0.3.3 row 4); Doc 07 §3.3 pins identity stability across reloads. Verdict per finding: what definition-schema versioning/migration posture must the M7 AMD block state explicitly?

### RQ5 — Concurrency footguns users actually hit

Which concurrency failures do real users hit (vs the ones engineers imagine)? HA `mode: single/restart/queued/parallel` confusion (cited threads); double-trigger storms; restart-kills-my-delay complaints (long `delay:` killed by restart or re-trigger); queued backlogs firing stale actions at 3am. Map each against `ConcurrencyMode` + `maxConcurrent` + `MaxExceededSeverity` + `RunStatus.CONDITION_NOT_MET`-doesn't-consume-a-slot (§0.3.1) and §3.7 dedup/ordering. Verdict: which mode defaults/ergonomics the evidence supports, which footguns are structurally closed, which need an M7/M8 obligation (e.g., a specific DIAGNOSTIC on drop).

---

## 2. Mandatory document format

```
# Research 14-A: Automation Authoring & Operating UX — Failure Modes
*Target: HomeSynapse M7/M8 charter + M7 AMD block + M5-C. Date: YYYY-MM-DD.*

## 0. Quote-back gate [M — FIRST] — per §0 above.

## 1. Executive Summary [M] — 5–8 verdict bullets; every bullet takes a position with a
     one-sentence defense. "X is worth investigating" is banned. Flag the single
     highest-impact finding AND the single strongest ledger-gap evidence item.

## 2. Platform Deep Dives [M] — one subsection per platform (HA deepest; SmartThings,
     Node-RED, Hubitat, Homey each substantive). Each: (a) how the platform
     solves/fails the RQ families; (b) ≥1 direct quotation from a primary source
     (docs, issue tracker, forum thread, maintainer statement) WITH URL;
     (c) what users DID (Mom-Test); (d) the gap-relative lesson, citing the §0.3
     anchor it is relative to.

## 3. Cross-Cutting Analysis [M]
   - 3.1 Failure-class concept map: class | HA | SmartThings | Node-RED | Hubitat |
         Homey | HomeSynapse (frozen mechanism, cited anchor).
   - 3.2 The debuggability matrix (RQ2): diagnostic question → which platforms answer
         it → does the frozen HomeSynapse surface capture the data (cite §4.2/§11/ledger).
   - 3.3 The ledger-gap dossier (RQ3): the assembled evidence that intent-confirmation
         is an unserved market need — or an honest finding that it isn't.
   - 3.4 Over-engineering check: frozen machinery NO surveyed platform's users
         actually need — defend or flag each (honesty section; REJECT-candidates).

## 4. Findings + Recommendations [M]
   - 4a. REC-numbered findings, REC-141 through at most REC-155, ranked
         (impact × confidence)/cost. Each REC: failure-class citation; evidence
         (≥1 primary source); gap-relative statement; concrete recommendation;
         effort class (S/M/L, prose).
   - 4b. THE DISPOSITION TABLE [M — load-bearing]: EVERY REC maps to EXACTLY ONE of:
           ALREADY-COVERED (cite the specific Doc 07 §N / AMD-NN / §0.3.3 row)
         | M7-OBLIGATION (charter/AMD-block/instruction item — name what it adds
           INSIDE frozen contracts: a test, a default, a trace detail, an event)
         | M8-OBLIGATION (same, M8 scope — zone/geofence, advanced ledger behaviors)
         | FUTURE-AMD (contract delta sketch — do NOT draft it)
         | POST-MVP (UI/cloud/companion lane)
         | REJECT (reasoned — evidence says HomeSynapse should NOT do this).
         No REC in two buckets. No bucket empty by laziness — if genuinely empty, say why.

## 5. Caveats and Open Questions [M] — source reliability; anything needing empirical
     validation; explicit INCOMPLETE-EVIDENCE declaration if web reach was too shallow.

## 6. Appendix: Sources [M] — URL families grouped by platform; every factual claim traceable.

## 7. HomeSynapse Code-Level Implications [LIGHT] — observations ONLY, routed through §4b.
     NO module-info proposals, NO new types, NO contract drafts. Exact §0.2/§0.3.1
     identifiers only.
```

## 3. Evidence standards (non-negotiable)

1. **Primary sources with URLs.** Issue trackers, forum/Reddit threads (dated), changelogs, maintainer statements. A claim without a citation is a vibe.
2. **Mom-Test discipline everywhere.** What users *did* — abandoned, migrated, forked, paid, built workaround hacks — outranks what they say they want. A verification-hack pattern (RQ3) outranks a feature-request thread.
3. **Community claims need 2+ independent reports or a maintainer statement.**
4. **Take positions.** Every section concludes with a verdict. "Worth investigating" is banned.
5. **Gap-relative or it didn't happen.** Every finding cites its §0.3 anchor. Findings that re-propose frozen machinery score ALREADY-COVERED, not recommendations.
6. **No fabricated identifiers.** Type/module names come from §0.2/§0.3.1 verbatim. If you need a HomeSynapse fact not embedded here and not in the connector, request it in §5 — do not reconstruct it. **Web search is required**; if reach is too shallow, declare INCOMPLETE-EVIDENCE in §5 rather than padding.

## 4. Guardrails (violations = the finding is discarded)

1. **Locked ground is the baseline to measure against, never an open question.** The Doc 07 TCA model, the sealed permits, AMD-25 `forDuration` semantics, ledger ownership, coalescing-disabled — "HomeSynapse should adopt a TCA model" is a discarded finding. The §0.3.3 DQ resolutions are DECIDED — do not re-open PresenceTrigger-vs-ZoneTrigger, the `InvokeAutomationAction` rename, or advancer organization.
2. **No M6.3 creep.** At-rest encryption is triple-gated; nothing here touches it.
3. **You cannot change contracts.** Contract-change implications route to FUTURE-AMD dispositions; you never draft amendment text, types, or module-info changes.
4. **REC numbering: 141–155 ONLY** (append-only global register; siblings own 156–185; high-water 140).
5. **Stay in register.** This brief is community evidence/UX. Scheduler-correctness internals, ledger persistence semantics, and event-storm engineering are the SIBLING research's register — if you trip over engineering prior art, note it in §5 as out-of-register, one line, and move on.
6. Produce ONE complete markdown document. Do not truncate.

## 5. What the PM does with the return (so you aim at it)

The PM runs the standard 6-step A–F assessment, source-verified, folding your disposition table into the merged REC-31..40 (re-anchored) + 141..185 pass: ALREADY-COVERED rows → coverage attestation; M7-OBLIGATION rows → M7 charter priorities + AMD-block content + instruction test requirements; M8-OBLIGATION rows → M8 charter rows; FUTURE-AMD rows → Nick's queue; POST-MVP rows → the M10/M11/Doc 13 lane; REJECTs recorded as anti-requirements. Your §3.3 ledger-gap dossier additionally feeds the M5-C website superiority material (the Research-13 INV-CE-01 pattern). A finding that cannot be placed in that machine is a finding you should sharpen or drop.
