<!--
file: context/instructions/2026-06-13_AMD-88-93_C8-C9_Bundled_DOCS_Review_Prompt.md
purpose: Independent DOCS-Project review prompt — ONE dispatch bundling (A) the six-amendment M7 automation block AMD-88..93 and (B) the B2 schema-irreversible decisions C8 (actorRef) + C9 (energy shape) ratification review. Full review discipline — contract freezes + a persisted-log schema decision.
audience: DOCS-Project reviewer (independent), Nick (dispatch + ratify)
state-type: instruction
status: READY TO DISPATCH — authored 2026-06-13 (M7 entry-gate session). Bundling = PM default per the 2026-06-12 sequencing decision; Nick veto-or-default at dispatch — if vetoed, dispatch §B (C8/C9) FIRST, the block second.
-->

# Bundled DOCS-Project Review — M7 Automation Block (AMD-88..93) + B2 C8/C9

You are the independent reviewer (HomeSynapse Core / DOCS Project) for **two coupled work products in one dispatch**: (A) the six-amendment M7 automation block — contract freezes for the M7 implementation window — and (B) the B2 regret-proof schema decisions **C8 `actorRef` semantics + C9 energy event shape** (PROPOSED 2026-06-08, awaiting exactly this independent review). They are bundled because they RESOLVE TOGETHER: AMD-92's stamping language cites C8 as PROPOSED-pending throughout — ratifying the block while C8 floats would freeze event contracts against an unratified attribution convention. Full review discipline (these freeze persisted/behavioral contracts — the constraint-enforcement §6 full-track, not P4).

## Source baseline (re-derive everything; do not trust the amendments' prose)

- **homesynapse-core HEAD `e5ea76f`** (docs-only MODULE_CONTEXT permit-count fix on **substantive `7c73c91`** = M6.2, 2026-06-11). Automation module last substantively touched M4.0b-4a.
- **homesynapse-core-docs `ed5cf91`+** (this block's six files land on top). On-disk amendment watermark **AMD-87**.
- Automation surface at baseline (re-derive from `core/automation/src/main/java/com/homesynapse/automation/` + `MODULE_CONTEXT.md`, 30-permit corrected 2026-06-12): TriggerDefinition 9 permits (5 T1 + 4 T2) · ConditionDefinition 7 (6+1) · ActionDefinition 8 (5+3) · Selector 6 (all T1) · `RunContext` 8 fields w/ `cascadeDepth` int at position 7 · enums incl. `RunStatus` (7) / `PendingStatus` (5) / `UnavailablePolicy` / `MaxExceededSeverity` · `RunId` automation-resident wrapper.
- Event surface at baseline: `EventTypes` **55** constants (incl. `AUTOMATION_TRIGGERED`/`AUTOMATION_COMPLETED`/`AUTOMATION_CAPABILITY_MISMATCH`); `CORE_PRODUCTION_EVENT_CLASSES` **24** records — incl. minimal-shape `AutomationTriggeredEvent(triggerType, triggerDetail)` + `AutomationCompletedEvent(status, failureReason, durationMs)`; `EventCategoryMapping` **36** entries (automation rows: triggered/completed only). `EventEnvelope` 14 fields, `actorRef` bare nullable `Ulid` at `:112`.
- Device surface: `EntityRole { PRIMARY, DIAGNOSTIC, CONFIG }` (AMD-44, M4.B-S2); `Entity.labels: List<String>`; **NO `EntityCategory` type exists**; **NO `SemanticTag` type exists**; **NO `device.reachable_changed` event exists**.
- Config keys (Doc 07 §9, Locked): `automation.max_cascade_depth` (8, 1–32) · `cascade_depth_health_threshold` (3) · `automation.command_pipeline.default_confirmation_timeout_ms` (30000, 5000–120000) · `automation.trigger.max_concurrent_duration_timers` (1000).
- Decided ground the block CONSUMES as locked inputs (do not re-open): DQ-1 promote `PresenceTrigger`/reject `ZoneTrigger` · DQ-2 rename → `InvokeAutomationAction` + promote · DQ-3 same advancer/separate registrations · DQ-5 geofence M8 (Nick, 2026-05-30, v4 addendum); the 2026-06-12 merged disposition (`nexsys-hivemind/context/planning/2026-06-12_M7-blueprint_merged-disposition.md`) is the routing authority.

## §A — The six amendments

| AMD | Title | Source RECs | Watermark note |
|---|---|---|---|
| 88 | TriggerDefinition M7 expansion (3 new permits, Webhook promotion, Presence promotion-designation, `triggerId`) | 31/32/37/38 (R4, v3-verified) | **ABOVE AMD-87** |
| 89 | Selector: `SemanticTagSelector` + `includedRoles` default exclusion (BREAKING + sweep) | 34/35 | above |
| 90 | ActionDefinition: `ConfirmationPolicy` (33⊕143⊕144⊕161 merged) + `RepeatAction` + `InvokeAutomationAction` | 33/37/40 ⊕ 143/144 ⊕ 161 | above |
| 91 | `RunCausalChain` swap + chain-membership cycle detection — **supersedes AMD-04** | 36⊕158 | above |
| 92 | Automation event vocabulary (16 mints, 2 reshapes, 1 record-for-constant; type-residency FLATTEN; fan-out) | 39 (W0 §2.5 ×5) ⊕ 141/147 | above |
| 93 | `automations.yaml` schema posture: (major,minor) + forward-only guarantee + reference validation + §3.3↔AMD-66/71 reconciliation | 150 ⊕ 153a⊕136 | above |

⚠ **Unlike the AMD-66..71 block (reserved below-watermark slots), AMD-88..93 sit ABOVE the AMD-87 watermark — block ratification RAISES the on-disk ceiling 87 → 93.** Verify the nav-index edit reflects this.

### §A load-bearing adversarial items (each demands an explicit ruling)

1. **`[R92-residency]` — THE block keystone.** AMD-92 §2.1 rules FLATTEN over relocate for `RunId`/`RunStatus`/`PendingStatus` (bare `Ulid`/`String` payload components — the E70-1 precedent; relocation rejected because `RunId` is automation-internal by design). Adversarially test: would ANY M7+ consumer need typed run identifiers from payloads badly enough to justify relocation? Confirm `event → automation` is a real cycle at the embedded module-infos (AMD-92 §7) and that every §2.2 payload component is event-resident-or-below.
2. **`[R92-reshape]`** — AMD-92 reshapes two EXISTING registered records (`AutomationTriggeredEvent`/`AutomationCompletedEvent`) outright. Verify the zero-producer/zero-persisted-instance claim at baseline (no production publish site exists; grep). If any persisted instance can exist (test logs do not count), the reshape needs schema-version machinery instead — rule explicitly.
3. **`[R92-1/2/3]`** — the three flagged payload calls: `automation_invoked` (a NEW type NOT in Doc 07's text — the ManualTrigger/InvokeAutomationAction mint; confirm necessity + the Doc 07 §3.7 table addition); nested payload records `EvaluatedEntityState`/`ConflictEntry` (precedent check); `automation_disabled` priority NORMAL-vs-CRITICAL (Doc 07 §3.7 :326 reasons NORMAL; §6.2 :709 says CRITICAL — the Locked doc disagrees with itself; pick the survivor, the loser gets the correction note).
4. **`[R89-1]` — the naming deviation (deliberate, flag-don't-fold).** The merged disposition's label is `includedCategories`; **`EntityCategory` does not exist in source** — the shipped M4 type is `EntityRole`, and AMD-89 binds `Set<EntityRole> includedRoles` (Glossary-over-label). Confirm the rename, or rule the field keeps the REC label with the real type. Also `[R89-2]`: SemanticTagSelector grounds on the SHIPPED `Entity.labels` namespaced-string convention (Research-8 REC-26's SemanticTag migration never shipped) — confirm convention-over-type.
5. **`[R88-1/2]`** — `CalendarTrigger` field set (PM-proposed beyond the disposition's letter); `ReachabilityTrigger` re-grounding (REC-32's `device.reachable_changed` dependency never shipped → binds device-subject `availability_changed`; `debounce` field replaced by AMD-25 `forDuration`). Verify `availability_changed`'s Entity/Device subject claim against Doc 01 §4.3.
6. **`[R90-1/2]`** — the NAMED confirmation default: AMD-90 reads the disposition's "(off; on where `Expectation` is cheap)" as **`BEST_EFFORT`-as-default** (Expectation-criterion semantics) vs the alternative OPTIMISTIC-as-default reading of "opt-in"; rule it. And the `RepeatAction` WHILE/UNTIL stance: AMD-03's single-snapshot rule kept inviolate (state-based WHILE over a static snapshot degenerates → load-time WARNING) vs per-iteration re-snapshot (breaches AMD-03); confirm the AMD-03-inviolate call.
7. **`[R91-1]` + supersession ledger.** Derived `depth()` + `ChainLink(runId, automationId)` vs REC-36's literal `(List<RunId>, int depth)`. Then audit AMD-91 §2.4's element-by-element AMD-04 disposition — especially **rate limiting NOT ADOPTED** (verify Locked Doc 07 truly never folded it; §6.7 + parked REC-168 own the space) and the suppression-authority transfer from the windowed correlation-set to chain membership (INV-TO-02 determinism claim — test it against the REPLAY rules §3.10).
8. **`[R93-1]`** — dangling-reference severity (per-definition FAILURE on the §6.1 path, tombstone-redirects exempted, same-file forward refs resolved post-parse) — confirm failure-over-warning; and the §2.3 reconciliation: automation reload classified HOT under AMD-66, write-path inherits M6.2 R-1 fail-closed (the M10 fence stated).
9. **Manifest/fan-out arithmetic.** Re-derive AMD-92 §2.3's expected pins (55→71; 24→41; 36→+17) from the §2.2 table; confirm the per-slice split matches the charter's placement (M7.1/M7.2 mint, M7.3 mints nothing) and that the P2-survey-at-instruction obligation (incl. the behavioral publish-count-pin category, the M6.4 lesson) is stated in every implementing AMD.
10. **Anti-requirement placement note (do not flag as a miss):** the session brief's "§7" placement for anti-requirements 151/155/162 is realized as §6 (Scope Fences, explicit non-goals) + §7 citations in each relevant AMD — deliberate, per the AMD-70 section pattern.

## §B — B2 C8/C9 ratification review

**File:** `nexsys-hivemind/context/decisions/2026-06-08_B2_schema_decisions_C8_C9.md` (PROPOSED; baseline `6c6dd33` — re-verify its source claims still hold at `7c73c91`: `actorRef` bare nullable `Ulid` at `EventEnvelope:112`, persisted/hydrated `SqliteEventStore:330/:672`; zero energy event types; `EventCategory.ENERGY`/`EntityType.ENERGY_METER` reserved).

Review like AMD-54..64/Doc 15 (schema-irreversibles over the immutable log): re-derive the source state, test each contract-freeze-readiness gate row (round-trips / enforceable / owner-doc), confirm regret-proofness (no already-written bytes change).

- **C8 `actorRef`:** four-kind closed set (PERSON/AUTOMATION/SYSTEM/API_CLIENT), kind-by-typed-ID-provenance (no new field), Tier-1 API keys → API_CLIENT never PERSON, automations MUST stamp `AutomationId`. **New evidence handed to this review (R14-A REC-146, 2026-06-12):** external community validation — Hubitat's *"what turned on my light?"* is the platform's top provenance complaint class; the audit-trail convention C8 freezes is exactly the differentiator surface. Weigh it as ratification support, not as a content change.
- **C8 ⊕ AMD-92 coupling (the bundle's point):** AMD-92 §2.4 stamps via the ENVELOPE seam only (no payload actor fields — REC-39 obligation 5) and is C8-independent by construction (payload shapes survive any C8 adjustment). Verify that independence claim — it is what makes the bundle safe to ratify in one pass.
- **C9 energy shape:** the four `power_measurement` attributes (W/Wh/V/A as AMD-47/52 `QuantityValue`) + six aggregate fields + ENERGY consent-scope category + ride-existing-types (no protocol vocabulary). Verify the Doc 15 §3.4 plaintext-at-MVP vs shred-scope reconciliation is correctly STAGED on OQ-15-2 (list-tuning, not a Doc-15 re-open), and that C9 stays disjoint from the M7 block (AMD-92 §6 fences energy out — confirm no collision).

## Verdict format (return to `nexsys-hivemind/context/audits/2026-06-DD_AMD-88-93_C8-C9_DOCS_Review_Return.md`)

Per amendment AND per decision (C8, C9): `RATIFY-AS-IS` / `RATIFY-WITH-EDITS` (enumerate every edit, cite the source line) / `REJECT` (reason). Plus: a block-level verdict for §A; explicit rulings on items 1–9 and every `[R*]` flag; a C8⊕AMD-92 coupling statement (safe-to-ratify-together: yes/no); the commit you re-derived at. Flag every place an amendment's prose disagrees with source at `7c73c91`/`e5ea76f` or with Locked Doc 07/Doc 01/Doc 15.

## Guardrails

- **Locked Doc 07 / Doc 01 / Doc 15 are inviolate** — the block proposes bounded currency edits (enumerated in each AMD's §9); if any finding requires MORE than those, say so and STOP that amendment (supersession territory, Nick's call).
- The merged disposition's ROUTING is decided ground; field-level shapes are this review's jurisdiction (the `[R*]` flags mark exactly where the PM specified beyond the disposition's letter).
- DQ-1/2/3/5 are Nick-ruled — do not re-open; verify the AMDs honor them.
- No new dependencies, no module-info changes anywhere in the block (the load-bearing zero-JPMS-change claim — verify it).
