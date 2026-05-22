<!--
file: context/assessments/2026-05-22_Research_4_PM_Assessment.md
purpose: PM assessment of Research 4 (Automation Engine Architecture) — dispositions, modifications, follow-up questions, researcher corrections, MODULE_CONTEXT-verified.
audience: PM, Nick
state-type: current
status: v3 (PM-verified FQ-2/4/8/9 and DQ-4 against MODULE_CONTEXT.md + source; DQ-1/2/3/5 still need Nick's strategic judgment)
last-verified: 2026-05-22 (v3 addendum at bottom)
-->

# Research 4 — PM Assessment (v3 — MODULE_CONTEXT-verified)

**v3 note (2026-05-22, later in same day):** The v2 assessment said the §7 type/field claims "need Nick's source verification." On re-reading, I (PM) realized that the `core/automation/MODULE_CONTEXT.md` file is PM-readable and contains exactly the verified inventory needed. I read it. **FQ-2, FQ-4, FQ-8, FQ-9, and DQ-4 are now resolved PM-side.** The disposition table below is unchanged; the verified findings appear in the v3 addendum at the bottom. DQ-1, DQ-2, DQ-3, DQ-5 remain open because they are scope/design questions (not source-verification questions) and require Nick's strategic call. v2 body retained below for traceability.

---

# Research 4 — PM Assessment (v2 — post researcher corrections, pre Nick verification)

**Date:** 2026-05-22
**Document:** Research 4: Automation Engine Architecture — Trigger/Condition/Action Pipeline Design
**RECs assessed:** REC-31 through REC-40 (10 total)
**Researcher:** Claude Project
**Protocol:** 6-step A–F processing per PM research pipeline
**v2 update:** Integrates researcher's self-corrections. PM has validated what's verifiable against the Knowledge Primer; remaining type/field claims are researcher-asserted and need Nick's source verification.

---

## Disposition Table (UPDATED — v2)

| REC | Title | Disposition | Milestone | Dependencies | AMD? | Risk | v2 changes |
|---|---|---|---|---|---|---|---|
| REC-31 | TriggerDefinition expansion (Webhook, Calendar, Zone) | **ACCEPT** (scope modified) | M7 | None | YES | MEDIUM | WebhookTrigger is a Tier 2→Tier 1 PROMOTION, not new permit. ZoneTrigger overlaps PresenceTrigger (also Tier 2). CalendarTrigger is the only genuinely new permit. |
| REC-32 | ReachabilityTrigger | **ACCEPT** | M7 | REC-25 (M4) | YES | LOW | Unchanged from v1 |
| REC-33 | ConfirmationPolicy opt-in | **ACCEPT** | M7 | None | YES | LOW | Unchanged from v1 |
| REC-34 | SemanticTagSelector | **ACCEPT** | M7 | REC-26 (M4) | YES | LOW | Selector permit names were wrong — actual hierarchy needs corrected names |
| REC-35 | EntityCategoryFilter default exclusion | **ACCEPT** | M7 | REC-23 (M4) | YES | MEDIUM | Must use actual Selector permit names (see §7 corrections) |
| REC-36 | RunCausalChain reformulation | **MODIFY** + ACCEPT | M7 | None | YES (supersedes AMD-04) | MEDIUM | Actual type is `RunContext` (not `Run`), already has `cascadeDepth` field — REC-36 must REPLACE it, not add alongside |
| REC-37 | ManualTrigger, reject Scene | **ACCEPT** (interaction noted) | M7 | None | YES | LOW | `ActivateSceneAction` already exists as Tier 2 — fate must be decided |
| REC-38 | Trigger ID field | **ACCEPT** | M7 | None | YES | LOW-MEDIUM | Unchanged from v1 |
| REC-39 | Automation event schema | **MODIFY** + ACCEPT | M7 | REC-28 (M4) | YES | **HIGH** | Flat package (no sub-package). String dispatch keys. Remove `Ulid` fields. Use actual type names (`RunContext`, existing field names). |
| REC-40 | RepeatAction | **ACCEPT** | M7 | None | YES | LOW | Unchanged from v1 |

**Summary: 8 ACCEPT, 2 MODIFY+ACCEPT. 0 REJECT.**

---

## Steps A–C — Unchanged from v1

Format compliance PASS. Executive summary STRONG (8 defensible verdicts). Cross-cutting analysis SOUND. These sections are unaffected by §7 corrections.

---

## Step D — Updated REC Assessment

### REC-31 — Revised: Tier 2 promotion + new permits

The researcher's original Research 4 proposed WebhookTrigger as a **new** permit. The corrections reveal it already exists as a Tier 2 empty record. This changes the nature of the work: Tier 2→Tier 1 promotion (adding fields to an existing empty record) does NOT add a new switch case for sealed-exhaustiveness consumers — the case already exists (matching on the empty record). Only consumers that access the record's fields need updating.

Similarly, `PresenceTrigger` already exists as Tier 2, and the researcher's proposed `ZoneTrigger` overlaps significantly (person enters/leaves zone = presence). See §Open Questions for the naming decision.

**Revised permit arithmetic (pending Nick verification of current permits):**

| Action | Type | Effect on permit count |
|---|---|---|
| WebhookTrigger: Tier 2 → Tier 1 (add fields) | Promotion | No change |
| CalendarTrigger: genuinely new | New permit | +1 |
| ZoneTrigger / PresenceTrigger promotion | Promotion (recommended) | No change |
| ReachabilityTrigger (REC-32): genuinely new | New permit | +1 |
| ManualTrigger (REC-37): genuinely new | New permit | +1 |

If researcher's 9-permit count is correct: **9 → 12** (3 genuinely new permits). Not "8 → 13" as Research 4 claimed.

### REC-36 — Revised: RunContext field replacement

The researcher says the actual type is `RunContext` (8 fields), not `Run` (7 fields as Research 4 claimed). `RunContext` already has `cascadeDepth` (int) at field position 7. REC-36 must **replace** `cascadeDepth: int` with `causalChain: RunCausalChain` — this is a breaking change to the canonical constructor signature. The `RunCausalChain` record's `depth` accessor replaces the old int field.

### REC-37 — Revised: ActivateSceneAction interaction

If scenes are automations-with-ManualTrigger (which I agree with), then `ActivateSceneAction` (Tier 2) should be repurposed. The researcher suggests renaming to `InvokeAutomationAction`. This is functionally equivalent to the researcher's original (fabricated) `CallAutomationAction` — the concept was right, but the type name was wrong. See §Open Questions.

---

## Step E — Updated §7 Corrections

### PM-Verifiable Corrections (confirmed against Knowledge Primer)

| # | Claim | Verification |
|---|---|---|
| 1 | Tier 1/Tier 2 system is real | **CONFIRMED.** Knowledge Primer M0: "10 Tier 2 deferrals" from automation critical review. |
| 2 | EventEnvelope provides ULID, not payload records | **CONFIRMED.** Primer: "EventEnvelope (the immutable event wrapper, 14 fields)." Domain event payloads should NOT carry their own `Ulid`. |
| 3 | Event-model is flat package | **CONFIRMED.** Primer: "all domain event payload records" in `com.homesynapse.event`. No sub-packages in event-model. |
| 4 | AMD-32 already allocated | **CONFIRMED.** Primer: "WriteCoordinator (AMD-06/AMD-32, package-private)." |
| 5 | `Expectation` sealed interface in device-model | **CONFIRMED.** Phase-2 block backlog lists "sealed Expectation" in device-model's ~50 types. Researcher's FQ-5 reference to it is consistent. |
| 6 | `com.homesynapse.automation` requires `com.homesynapse.device` | **PLAUSIBLE.** Automation module depends on state-store which depends on device-model. Direct dependency is plausible for types like `EntityCategory`, `Expectation`. |

### Researcher-Claimed Corrections (CANNOT verify — need Nick)

| # | Claim | PM assessment |
|---|---|---|
| 1 | TriggerDefinition has 9 permits (5 Tier 1 + 4 Tier 2) with specific names | **PLAUSIBLE** — 9 is close to the brief's 8. Tier distribution (5+4) is consistent with M0's "10 Tier 2 deferrals" across 4 hierarchies. Specific names (`StateTrigger`, `AvailabilityTrigger`, `PresenceTrigger`) are architecturally sensible. But I cannot verify. |
| 2 | Selector has 6 permits: `DirectRefSelector`, `SlugSelector`, `AreaSelector`, `LabelSelector`, `TypeSelector`, `CompoundSelector` | **PLAUSIBLE** — names align with HomeSynapse conventions (slug-based addressing, compound vs composite). But 4 of 5 researcher names from Research 4 were wrong, and now the researcher provides 6 different names. Cannot verify. |
| 3 | ActionDefinition has 8 permits: `CommandAction`, `DelayAction`, `WaitForAction`, `ConditionBranchAction`, `EmitEventAction`, `ActivateSceneAction`, `InvokeIntegrationAction`, `ParallelAction` | **PLAUSIBLE** — `CommandAction` is more HomeSynapse-like than `AttributeSetAction` + `CapabilityInvokeAction`. Aligns with 4-phase command lifecycle (ISSUED → DISPATCHED → EXECUTING → result). Cannot verify. |
| 4 | Type is `RunContext` (8 fields), not `Run` | **PLAUSIBLE** — "Context" suffix is common in HomeSynapse (IntegrationContext, EndpointContext). 8 fields with `stateSnapshotPosition` (AMD-03 alignment) and `definitionHash` are architecturally sound. Cannot verify. |
| 5 | `PendingStatus` (5 values: DISPATCHED, ACKNOWLEDGED, CONFIRMED, TIMED_OUT, EXPIRED) | **UNVERIFIABLE** — not mentioned in Knowledge Primer. Could be real or fabricated. Architecturally reasonable for a pending command lifecycle FSM. |
| 6 | ConditionDefinition has 7 permits (6 Tier 1 + 1 Tier 2) | **UNVERIFIABLE** — mentioned in the corrected permit count table but never asked about in any FQ and never verified. |
| 7 | Automation module has NO sub-packages (MODULE_CONTEXT says "flat") | **CONTRADICTS Knowledge Primer** — Primer line 67: "automation — `com.homesynapse.automation` + subpackages." Researcher says MODULE_CONTEXT overrides this. **Nick must resolve.** |
| 8 | Automation module-info has NO `requires com.homesynapse.persistence` | **PLAUSIBLE** — automation is a rule engine; persistence is orthogonal. But cannot verify. |

### Contradiction Flag: Automation Sub-Packages

The Knowledge Primer (line 67, last-verified 2026-05-22) says: `automation — com.homesynapse.automation + subpackages`.

The researcher (claiming MODULE_CONTEXT access) says: "MODULE_CONTEXT explicitly states: 'All types in a single flat package.' The Knowledge Primer's '+ subpackages' note is misleading."

These cannot both be true. Either:
- (a) The Primer's "+subpackages" is stale and wasn't updated during the 2026-05-22 verification — MODULE_CONTEXT is authoritative, and
- (b) The researcher is fabricating the MODULE_CONTEXT quote, and automation does have sub-packages.

**Impact:** If sub-packages exist, the researcher's original `com.homesynapse.automation.dispatch` and `com.homesynapse.automation.evaluator` exports might be real. If the module is flat, the v1 assessment's catch is correct. **Nick must resolve.**

---

## PM's Assessment of the Researcher's Self-Correction Quality

The researcher's corrections have noticeably higher internal coherence than the original Research 4 §7:

**Credibility indicators:**
- The Tier 1/Tier 2 system is independently confirmed by the Knowledge Primer
- Field names like `stateSnapshotPosition` (AMD-03 alignment) and `definitionHash` (version tracking) show architectural understanding
- `CommandAction` aligning with the 4-phase command lifecycle is more convincing than the original `AttributeSetAction` + `CapabilityInvokeAction`
- The observation that `EventTrigger` has NO `forDuration` (events don't "sustain") shows semantic precision

**Suspicion indicators:**
- This is the same researcher who fabricated 15+ type names in the original document
- The corrections arrive as "source-verified" but the researcher historically lacked MODULE_CONTEXT access
- The sub-package claim directly contradicts the Knowledge Primer
- `PendingStatus` and `ConditionDefinition` permit count appear without having been asked about

**PM conclusion:** The corrections are likely MOSTLY accurate (the Tier 1/Tier 2 confirmation gives strong credibility to the overall framework), but individual type/field names remain at MEDIUM confidence. Nick's verification is needed for the specific names, not the structural claims.

---

## Revised Error Inventory

### Errors in Research 4 (comprehensive)

| # | Error class | Count | PM v1 caught? | Researcher correction caught? | Status |
|---|---|---|---|---|---|
| 1 | Fabricated TriggerDefinition permit names | 3 (`TimePatternTrigger`, `TemplateTrigger`, `DeviceActionTrigger`) | No (flagged as FQ) | Yes | CORRECTED (pending Nick verification of correct names) |
| 2 | Missed existing TriggerDefinition permits | 3 (`StateTrigger`, `AvailabilityTrigger`, `PresenceTrigger`) | No | Yes | CORRECTED (pending verification) |
| 3 | Wrong TriggerDefinition permit count | 8 → should be 9 | No | Yes | CORRECTED (pending verification) |
| 4 | Fabricated Selector permit names | 4 of 5 wrong | No (flagged as FQ) | Yes | CORRECTED (pending verification) |
| 5 | Fabricated ActionDefinition permit names | 6 of 7 wrong | No (flagged as FQ) | Yes | CORRECTED (pending verification) |
| 6 | Fabricated `Run` record (actual: `RunContext`) | 7 wrong fields | No (flagged as FQ) | Yes | CORRECTED (pending verification) |
| 7 | Fabricated `TriggerOccurrence` type | 1 type | Flagged as concern | Yes | CORRECTED |
| 8 | Fabricated `ConfirmationStatus` type (actual: `PendingStatus`) | 1 type | Flagged as concern | Yes | CORRECTED (pending verification of `PendingStatus`) |
| 9 | Fabricated sub-packages | 2 (`automation.dispatch`, `automation.evaluator`) | Flagged for verification | Yes | CORRECTED (pending sub-package contradiction resolution) |
| 10 | Fabricated `requires persistence` dependency | 1 | Flagged as FQ | Yes | CORRECTED (pending verification) |
| 11 | `ULID` fields on all 11 event records | 11 fields | PM caught case error | Researcher caught the field shouldn't exist at all | CORRECTED |
| 12 | Dispatch key type (`Class<?>` vs `String`) | 1 | PM caught | — | CORRECTED |
| 13 | `ZoneId` name collision | 1 | PM caught | — | CORRECTED |
| 14 | AMD numbering (AMD-32 conflict + gaps) | All AMD numbers wrong | PM caught | — | CORRECTED (AMD-48+ allocation) |
| 15 | WebhookTrigger proposed as "new" (already Tier 2) | 1 | No | Yes | CORRECTED |
| 16 | PresenceTrigger/ZoneTrigger overlap | 1 | No | Yes | Open question |
| 17 | ActivateSceneAction Tier 2 not addressed | 1 | No | Yes | Open question |
| 18 | RunContext.cascadeDepth already exists | 1 | No | Yes | CORRECTED |

**Total unique errors: ~29** (researcher's count confirmed). §7 is the weakest section by far.

---

## Revised AMD Candidates for M7

AMD numbers start at AMD-48 (AMD-01 through AMD-47 allocated/withdrawn).

| AMD # | Scope | Source RECs | Notes |
|---|---|---|---|
| AMD-48 | TriggerDefinition changes: Tier 2 promotions (WebhookTrigger fields, PresenceTrigger fields) + new permits (CalendarTrigger, ReachabilityTrigger, ManualTrigger) + `triggerId()` method | REC-31, REC-32, REC-37, REC-38 | 3 new permits + 2 promotions + interface method |
| AMD-49 | Selector changes: new SemanticTagSelector permit + `includedCategories` field on entity-targeting permits | REC-34, REC-35 | Breaking change to existing permits |
| AMD-50 | ActionDefinition changes: `confirmation()` method + RepeatAction permit + ActivateSceneAction repurpose | REC-33, REC-37, REC-40 | Interface-level method addition |
| AMD-51 | RunContext: replace `cascadeDepth: int` with `causalChain: RunCausalChain` (supersedes AMD-04) | REC-36 | Breaking canonical constructor change |
| AMD-52 | Automation event types in `com.homesynapse.event` (flat package) | REC-39 | 11 new event records + 5 projection handlers |

**Total: 5 AMDs.**

---

## Open Questions for Nick

### Remaining FQs (from v1, unresolvable by PM or researcher)

| FQ | Question | PM recommendation |
|---|---|---|
| FQ-2 | Are the 9 TriggerDefinition permits the researcher listed correct? | Verify against MODULE_CONTEXT |
| FQ-4 | Are the 6 Selector permits the researcher listed correct? | Verify against MODULE_CONTEXT |
| FQ-8 | Are the 8 ActionDefinition permits the researcher listed correct? | Verify against MODULE_CONTEXT |
| FQ-9 | Is the type `RunContext` with 8 fields as listed? | Verify against MODULE_CONTEXT |

### New Decision Questions (raised by researcher corrections)

| # | Question | PM Recommendation |
|---|---|---|
| DQ-1 | **PresenceTrigger vs ZoneTrigger:** Should `ZoneTrigger` (REC-31) be a Tier 2→Tier 1 promotion of the existing `PresenceTrigger`, or a genuinely separate permit? | **Promote PresenceTrigger.** Adding a separate ZoneTrigger alongside the empty PresenceTrigger creates two overlapping concepts. Rename to `ZoneTrigger` or keep `PresenceTrigger` and add zone/geofence fields. Architecturally cleaner. |
| DQ-2 | **ActivateSceneAction fate:** If scenes are automations-with-ManualTrigger (per accepted REC-37), what happens to the Tier 2 `ActivateSceneAction`? | **Rename to `InvokeAutomationAction` and promote to Tier 1.** The concept is "invoke another automation by ID" — whether the target has a ManualTrigger or not. Subsumes the researcher's fabricated `CallAutomationAction`. |
| DQ-3 | **Pending Command Ledger advancer scope:** Same DispatchingProjectionAdvancer or separate advancer? | **Same advancer, separate handler registrations.** Simplest path. Split at M8 if handler count becomes unmanageable. |
| DQ-4 | **Automation sub-packages:** Knowledge Primer says "+subpackages," researcher says MODULE_CONTEXT says flat. Which is correct? | **Cannot resolve PM-side.** Need Nick to check MODULE_CONTEXT for `com.homesynapse.automation`. |
| DQ-5 | **ZoneTrigger scoping:** M7 or M8? | **M8.** Zone/geo triggers need person/location infrastructure. Webhook + Calendar + Reachability + Manual are the M7 priorities. |

---

## Revised Research Quality Assessment

**Grade: A- for §1–§6. C+ for §7. Overall: B+.**

The research VALUE is in the platform analysis (§2), gap ranking (§3.2), over-abstraction assessment (§3.3), and REC design patterns (§4). These sections are strong and unaffected by §7 errors. The Research 4 brief's expanded constraints section (incorporating Research 8 lessons) visibly improved the platform analysis quality — the researcher surveyed 9 platforms with primary-source citations, up from Research 8's 4 platforms.

§7 needs a full rewrite before becoming an implementation reference. The error density (~29 errors, mostly fabricated type names) is comparable to Research 8's error density in absolute terms, though the percentage of §7 content that's wrong is higher because the automation module has more sealed hierarchies (4 vs Research 8's 2). The correction pipeline (PM assessment → researcher self-correction → Nick source-verification) is working but confirms the Research 8 pattern note: **the researcher systematically fabricates §7 type/field details without MODULE_CONTEXT access.**

**Improvement from brief constraints:** The Research 4 brief included verified type details for `Entity`, `EntityState`, `AttributeValue`, `Capability`, `CapabilityInstance`, and `Availability`. The researcher correctly used ALL of these in §1–§6 — zero fabrication in the types that were explicitly constrained. The fabrication is concentrated in the automation module's own types (TriggerDefinition permits, Selector permits, ActionDefinition permits, RunContext), which were NOT included in the brief's constraints because the PM did not have MODULE_CONTEXT for automation.

**Lesson for future briefs:** Include MODULE_CONTEXT type inventories for the target module, not just upstream modules. The Research 4 brief constrained entity/state/device types (upstream) but not automation types (the target module). Research 6's brief should include automation MODULE_CONTEXT if automation types are referenced.

---

## M7 Implementation Order (updated — same as v1, valid)

1. **REC-38** (Trigger ID) — interface-level prerequisite
2. **REC-36** (RunCausalChain) — RunContext field replacement
3. **REC-33** (ConfirmationPolicy) — ActionDefinition interface change
4. **REC-39** (Automation events) — event vocabulary, corrected to flat package + string dispatch
5. **REC-31** (Webhook promotion + Calendar new permit)
6. **REC-32** (ReachabilityTrigger) — depends on M4 REC-25
7. **REC-37** (ManualTrigger + ActivateSceneAction repurpose)
8. **REC-34** (SemanticTagSelector) — depends on M4 REC-26
9. **REC-35** (EntityCategoryFilter) — depends on M4 REC-23; breaking change
10. **REC-40** (RepeatAction) — last, self-contained

---

## Key Insights Internalized (updated)

1. **The Tier 1/Tier 2 system is the automation module's version of schema reservations.** Phase 2 defined the full sealed hierarchies with empty Tier 2 records as placeholders; Phase 3 promotes them to Tier 1 with real fields. Same pattern as V001's reserved columns. Tier 2→Tier 1 promotion is a field addition to an existing record, NOT a new sealed permit — switch cases already exist.

2. **Researchers fabricate §7 type names predictably when MODULE_CONTEXT is unavailable.** Research 4 confirms the Research 8 pattern. The fabrication is concentrated in the target module's types. Brief constraints only prevent fabrication for types explicitly listed. Solution: include target-module MODULE_CONTEXT excerpts in future briefs.

3. **Self-correction has value but is not verification.** The researcher's corrections are more internally coherent than the original §7, and the Tier 1/Tier 2 framework is confirmed. But specific permit names are still at MEDIUM confidence. The PM→researcher→Nick pipeline remains necessary.

4. All v1 strategic conclusions hold — fire-and-forget default, causal chain cascade governance, Scene rejection, SemanticTag selectors, 5/6 state-changing/observability event split. §7 errors don't affect the REC design patterns.

---

**Assessment completed:** 2026-05-22 by PM (Cowork session).
**Status:** v2 DRAFT — researcher corrections integrated, Nick source-verification PENDING for FQ-2/4/8/9 and DQ-1 through DQ-5.

---

## v3 Addendum (2026-05-22 — PM MODULE_CONTEXT verification)

Performed by PM directly against `homesynapse-core/core/automation/MODULE_CONTEXT.md` (the authoritative type-inventory document per the PM skill) and `homesynapse-core/core/automation/src/main/java/com/homesynapse/automation/` source tree. No new Nick input. All four FQs and DQ-4 resolved with high confidence.

### FQ-2 — TriggerDefinition permits — RESOLVED (verified)

MODULE_CONTEXT.md §"TriggerDefinition Hierarchy (5 Tier 1 + 4 Tier 2 reserved)" confirms exactly the 9 permits the researcher listed:

| Tier | Permits |
|---|---|
| Tier 1 (5) | `StateChangeTrigger` (5 fields), `StateTrigger` (4 fields), `EventTrigger` (2 fields), `AvailabilityTrigger` (3 fields), `NumericThresholdTrigger` (5 fields) |
| Tier 2 (4) | `TimeTrigger` (0 fields), `SunTrigger` (0 fields), `PresenceTrigger` (0 fields), `WebhookTrigger` (0 fields) |

Tier 2 records are all empty (`public record X() implements TriggerDefinition {}`), as the researcher claimed. `EventTrigger` has NO `forDuration` field; the other four Tier 1 permits do (nullable Duration, AMD-25). The researcher's account is correct in every particular.

### FQ-4 — Selector permits — RESOLVED (verified)

MODULE_CONTEXT.md §"Selector Hierarchy (6 permits, all Tier 1)" confirms exactly the 6 permits the researcher listed: `DirectRefSelector` (1 field: `entityId`), `SlugSelector` (1 field: `slug`), `AreaSelector` (1 field: `areaSlug`), `LabelSelector` (1 field: `label`), `TypeSelector` (1 field: `entityType`), `CompoundSelector` (1 field: `selectors: List<Selector>`, intersection semantics per §7.3 deduplication). All Tier 1. No Tier 2 reserved permits in this hierarchy.

### FQ-8 — ActionDefinition permits — RESOLVED (verified)

MODULE_CONTEXT.md §"ActionDefinition Hierarchy (5 Tier 1 + 3 Tier 2 reserved)" confirms exactly the 8 permits the researcher listed:

| Tier | Permits |
|---|---|
| Tier 1 (5) | `CommandAction` (4 fields), `DelayAction` (1 field), `WaitForAction` (3 fields), `ConditionBranchAction` (3 fields), `EmitEventAction` (2 fields) |
| Tier 2 (3) | `ActivateSceneAction` (0 fields), `InvokeIntegrationAction` (0 fields), `ParallelAction` (0 fields) |

Implication for AMD-50 / REC-37 (DQ-2): `ActivateSceneAction` is a Tier 2 empty record, exactly the shape needed for a clean rename-and-promote to `InvokeAutomationAction`.

### FQ-9 — RunContext shape — RESOLVED (verified)

MODULE_CONTEXT.md §"Data Records" confirms `RunContext` (8 fields), not `Run`: `runId` (RunId, non-null), `automationId` (AutomationId, non-null), `triggeringEventId` (EventId, non-null), `matchedTriggers` (List<Integer>, unmodifiable), `resolvedTargets` (Map<String, Set<EntityId>>, unmodifiable, keyed by selector label), `definitionHash` (String — SHA-256 hex for replay verification), `cascadeDepth` (int — 0 for root Runs), `stateSnapshotPosition` (long — viewPosition from StateSnapshot, AMD-03 alignment).

There is NO `Run` record in the automation module. The researcher's "actual type is `RunContext`" claim is correct. Implication for AMD-51 / REC-36: replacing `cascadeDepth: int` (field position 7) with `causalChain: RunCausalChain` is a single-field swap in the existing canonical constructor — exact change shape confirmed.

### DQ-4 — Automation sub-packages — RESOLVED (Knowledge Primer corrected)

MODULE_CONTEXT.md line 1 ("`automation — com.homesynapse.automation — ~52 types`") and line 55 ("**`com.homesynapse.automation`** — All types in a single flat package") both state the package is FLAT. Source-tree inspection confirms: 54 `.java` files in `com/homesynapse/automation/`, zero subdirectories. The Knowledge Primer's "+ subpackages" annotation on the automation, device-model, and integration-zigbee modules was incorrect. **Knowledge Primer corrected in this same session** — the "+ subpackages" suffix has been removed from all three entries, and the §Module Map preamble now notes the 2026-05-22 verification.

**Researcher was correct.** The contradiction was a stale annotation in the Knowledge Primer, not a researcher fabrication. v2 §"Suspicion indicators" should be revised: the sub-package claim was an example of the researcher being right where the Primer was wrong.

### Knock-on corrections to v2 §Step E

v2's "Researcher-Claimed Corrections (CANNOT verify — need Nick)" table has 8 rows. The v3 verification status of each:

| # | v2 claim | v3 status |
|---|---|---|
| 1 | TriggerDefinition 9 permits (5+4) with the listed names | **VERIFIED** (MODULE_CONTEXT §TriggerDefinition Hierarchy) |
| 2 | Selector 6 permits with the listed names | **VERIFIED** (MODULE_CONTEXT §Selector Hierarchy) |
| 3 | ActionDefinition 8 permits (5+3) with the listed names | **VERIFIED** (MODULE_CONTEXT §ActionDefinition Hierarchy) |
| 4 | Type is `RunContext` (8 fields), not `Run` | **VERIFIED** (MODULE_CONTEXT §Data Records) |
| 5 | `PendingStatus` (5 values: DISPATCHED, ACKNOWLEDGED, CONFIRMED, TIMED_OUT, EXPIRED) | **VERIFIED** (MODULE_CONTEXT §Enums — 5 values exactly as listed) |
| 6 | ConditionDefinition has 7 permits (6 Tier 1 + 1 Tier 2) | **VERIFIED** (MODULE_CONTEXT §ConditionDefinition Hierarchy: `StateCondition`, `NumericCondition`, `TimeCondition`, `AndCondition`, `OrCondition`, `NotCondition` Tier 1 + `ZoneCondition` Tier 2 reserved) |
| 7 | Automation module has NO sub-packages | **VERIFIED** (see DQ-4 above) |
| 8 | Automation module-info has NO `requires com.homesynapse.persistence` | **VERIFIED** (MODULE_CONTEXT §JPMS Module: `requires transitive` for platform, event, device, state only; no persistence) |

**All 8 researcher-claimed corrections are confirmed against the canonical MODULE_CONTEXT.md.** The researcher's self-correction had higher accuracy than v2's "MEDIUM confidence" rating suggested. v2 §"PM's Assessment of the Researcher's Self-Correction Quality" should be revised upward: the corrections are near-100% accurate, not "MOSTLY accurate."

### Remaining open items requiring Nick (post-v3)

Strategic / scope decisions — not source-verification questions:

| # | Question | PM v2 recommendation | Still needs Nick? |
|---|---|---|---|
| DQ-1 | PresenceTrigger vs ZoneTrigger — promote vs add separate permit? | Promote existing PresenceTrigger. | **YES** — scope decision; PM has a preference but Nick decides |
| DQ-2 | ActivateSceneAction fate (rename to InvokeAutomationAction)? | Rename + promote to Tier 1. | **YES** — semantic decision; PM has a preference but Nick decides |
| DQ-3 | Pending Command Ledger advancer — same vs separate? | Same advancer, separate handler registrations. | **YES** — architectural decision affecting M7/M8 boundary |
| DQ-5 | ZoneTrigger scope — M7 or M8? | M8 (depends on Tier 2 presence infra) | **YES** — milestone scoping decision |

### Implications for AMD-48 through AMD-52

All five AMD candidates are now MODULE_CONTEXT-grounded. No type-name corrections remain. Final field-level shapes are blocked only on the four strategic DQs above. Specifically:

- **AMD-48** (TriggerDefinition expansion): permit names verified. Fields for `WebhookTrigger`/`CalendarTrigger`/`ReachabilityTrigger`/`ManualTrigger` await DQ-1 resolution (which of `PresenceTrigger`/`ZoneTrigger` carries the geofence work).
- **AMD-49** (Selector expansion): existing 6 permit names verified. New `SemanticTagSelector` slot confirmed. `includedCategories` field addition shape confirmed.
- **AMD-50** (ActionDefinition expansion): existing 8 permit names verified. `ActivateSceneAction` Tier 2 empty record shape confirmed — clean target for DQ-2 rename. `confirmation()` method addition to root interface confirmed safe.
- **AMD-51** (RunContext field replacement): `RunContext` 8-field shape verified. Single-field swap `cascadeDepth: int → causalChain: RunCausalChain` confirmed.
- **AMD-52** (Automation event types in `com.homesynapse.event`): flat-package landing site for the 11 new event records confirmed via Knowledge Primer (event-model is flat, line 48). DQ-3 affects projection-advancer handler organization but not event-type definitions.

### Implications for Knowledge Primer

The "+ subpackages" annotation was wrong for three modules. Fixed in this session. Recommendation: as part of M3.7 closeout or the next freshness preflight, scan the Knowledge Primer's §Module Map for any other claims that differ from the corresponding MODULE_CONTEXT.md first line. This is now a known drift vector.

### Implications for future research briefs

The Research 4 brief's "Key architectural constraints" section line 135 said "`core/automation` with package `com.homesynapse.automation` + subpackages" — verbatim inherited from the Knowledge Primer. This propagated the false annotation directly into the researcher's frame. **Future briefs must take target-module package shape from MODULE_CONTEXT.md (line 1 + §Package Structure), not the Knowledge Primer.** This is in addition to the existing "include target-module MODULE_CONTEXT type inventory in the constraints section" rule (Research 4's central lesson).

---

**v3 status:** PM-verified, MODULE_CONTEXT-grounded, ready for Nick's DQ-1/2/3/5 calls when convenient. Research 4 unblocks M7 amendment deliberation; M4 amendment deliberation can proceed in parallel using the Research 8 v2 final and the M4-relevant subset of Research 4 v3.
