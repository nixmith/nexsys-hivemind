<!--
file: context/assessments/2026-06-12_W0_Research_4_Currency_Delta.md
purpose: W0 (PM-internal) — Research-4 currency delta per the 2026-06-11 research architecture §2. Re-anchors REC-31..40 dispositions against source at core HEAD `7c73c91`; refreshes the DQ escalation list; folds the new-since-R4 contract ground (C8, config substrate, OR-M6-NONCE discipline). The three R14/R15 briefs and the M7/M8 charter cite THIS note instead of re-deriving.
audience: PM, Nick
update-cadence: once (consumed by the briefs + charter)
state-type: assessment
status: COMPLETE 2026-06-12 — source-verified at `7c73c91`; no new RECs minted; zero open DQs
anchors: context/assessments/2026-05-22_Research_4_PM_Assessment.md (v3/v4); context/planning/2026-06-11_M7-blueprint_research-architecture.md §2; context/decisions/2026-06-08_B2_schema_decisions_C8_C9.md
-->

# W0 — Research-4 Currency Delta (re-anchor at `7c73c91`)

**Baseline:** core HEAD `7c73c91` (M6.2). Automation module last touched M4.0b-4a (2026-05-31, the `requires com.homesynapse.value` edge); M5/M6 touched nothing in `core/automation` — the "survived-by-construction" claim in the architecture doc §2 is **empirically confirmed**, not assumed.

## 1. Source verification summary (one glance each, 2026-06-12)

| Claim re-checked | Source at `7c73c91` | Verdict |
|---|---|---|
| TriggerDefinition 9 permits (5 T1 + 4 T2) | `TriggerDefinition.java` Javadoc + permits clause; MODULE_CONTEXT §TriggerDefinition | **HOLDS** |
| ConditionDefinition 7 permits (6 T1 + 1 T2) | `ConditionDefinition.java` | **HOLDS** |
| ActionDefinition 8 permits (5 T1 + 3 T2) | `ActionDefinition.java` | **HOLDS** |
| Selector 6 permits, all Tier 1 | `Selector.java` | **HOLDS** |
| `RunContext` 8 fields, `cascadeDepth` (int) at position 7 | `RunContext.java` canonical ctor — field names verbatim per the v3 addendum | **HOLDS** |
| `ActivateSceneAction` = Tier 2 empty record | `public record ActivateSceneAction() implements ActionDefinition {}` | **HOLDS** (clean DQ-2 rename target) |
| `actorRef` = bare nullable `Ulid` on the envelope | `EventEnvelope.java:112` | **HOLDS** (C8 baseline intact) |
| `DispatchingProjectionAdvancer` in tree | `core/state-store/.../DispatchingProjectionAdvancer.java` (M4.0b-1 `cf1a97e`) | **HOLDS** (DQ-3 target real) |
| Automation `module-info.java` | 4× `requires transitive` (platform/event/device/state) **+ plain `requires com.homesynapse.value` (M4.0b-4a)** | **DELTA** — postdates the v3 JPMS verification; see §4.4 |

## 2. REC re-anchors

### 2.1 REC-31 / 32 / 37 / 38 — trigger block: arithmetic CONFIRMED, dispositions UNCHANGED
Permit arithmetic re-verified at source: promotions (`WebhookTrigger`, `PresenceTrigger`) change no permit count; genuinely new = `CalendarTrigger`, `ReachabilityTrigger`, `ManualTrigger` → **9 → 12**. DQ-1/DQ-5 resolutions (v4) bind the shape: the `PresenceTrigger` **promotion shape** lands in the M7 AMD block; geofence **fields + evaluation** are M8. REC-32 still depends on REC-25 (M4, shipped). No change to ACCEPT dispositions.

### 2.2 REC-33 / 40 — action block: CONFIRMED, UNCHANGED
`confirmation()` root-interface addition and `RepeatAction` permit (+1, → 13 total across the hierarchy after the M7 block) remain clean against the verified 5+3 hierarchy.

### 2.3 REC-34 / 35 — selector block: CONFIRMED, one sharpening
6 verified permits + new `SemanticTagSelector` (+1 → 7). REC-35 `includedCategories` is a **breaking change to existing entity-targeting permits** (compact-constructor + every construction site) — under the post-M6 discipline this is **automatically an AMD-block item, never an instruction-level fold** (architecture doc §4 rule c). Disposition unchanged; routing sharpened.

### 2.4 REC-36 — `RunContext` swap: CONFIRMED, UNCHANGED
The single-field swap `cascadeDepth: int → causalChain: RunCausalChain` (supersedes AMD-04) is exactly as the v3 addendum stated; no intervening change. Breaking canonical-ctor change → AMD block. The `RunCausalChain.depth()` accessor replaces the int for the §3.7.1 governor (default 8, range 1–32 — unchanged in Doc 07).

### 2.5 REC-39 — automation event schema (HIGH): **RE-ANCHORED — four new obligations + one new finding**
The v2 disposition (flat package, String dispatch keys, no `Ulid` payload fields, real type names) predates AMD-52, E70-1, the manifest-pin discipline, and the M6.4 survey lesson. Re-anchored obligations for the M7 AMD block:

1. **Type-residency rule (the E70-1/AMD-52 class — NEW FINDING).** Automation event records live in `com.homesynapse.event` and may reference **only event-resident or below types**. `AutomationId` is fine (platform-api). **`RunId`, `RunStatus`, `PendingStatus` are automation-resident and MUST NOT appear in event payloads** — `event → automation` would complete a JPMS cycle (`automation requires transitive event`). Run/status identifiers in payloads must be **flattened** (bare `Ulid` / `String`, the AMD-70 E70-1 precedent) **or** the types relocated — an explicit AMD-block decision, not a Coder call. Research 4 never surfaced this because AMD-52/E70-1 hadn't happened.
2. **Manifest-pin fan-out.** Every new automation event type rides the full P2 fan-out: `EventTypes` 55→+n, `CORE_PRODUCTION_EVENT_CLASSES` 24→+n, `EventCategoryMapping` 36→+n (pins per the M6.2 closeout; M6.2 changed none), **plus** the consumer/pin survey **including the behavioral publish-count-pin category in producing-module sibling tests** (the M6.4 GF-1 lesson — that category postdates Research 4).
3. **Typed values follow AMD-52.** Any automation event carrying attribute values uses the persistence-side tagged-union codec discipline (no `@JsonTypeInfo`, exhaustive no-`default` switch, `schema_version` discriminator precedent). The original REC-39 "String dispatch keys" call is consistent and stands.
4. **Projection handlers ride DQ-3.** The "5 projection handlers" register on the existing `DispatchingProjectionAdvancer` (same advancer, separate registrations; split only at M8 if unmanageable — Nick's v4 ruling).
5. **C8 stamps (see §4.1).** Run-initiating and command events carry `actorRef = AutomationId` — REC-39's event records must leave that to the envelope (no payload-level actor field; the envelope seam owns it).

Disposition stays **MODIFY + ACCEPT**; the MODIFY content is now the five obligations above.

## 3. DQ escalation refresh — **list is EMPTY**

DQ-1/2/3/5 were all **Nick-resolved 2026-05-30 (v4 addendum)**, and each resolution re-verifies clean at `7c73c91` (table §1: empty `PresenceTrigger`, empty `ActivateSceneAction`, advancer in tree, geofence absent). They are no longer escalations — they are **decided ground the M7 AMD block consumes as locked inputs**: DQ-1 promote `PresenceTrigger`; DQ-2 rename → `InvokeAutomationAction` + promote; DQ-3 same advancer/separate handlers; DQ-5 geofence → M8. **W0 raises zero new DQs.** (FQ-2/4/8/9 + DQ-4 were PM-verified at v3 and re-verified here.)

## 4. New-since-Research-4 contract ground (fold into briefs + charter)

1. **B2 C8 `actorRef` (PROPOSED 2026-06-08, ratification = W25 critical path).** Automations MUST stamp `actorRef = AutomationId` on every command/event they originate; kind recoverable by typed-ID provenance; bare `Ulid` stays. **Direct M7 contract dependency: M7.1 does not issue before C8 is RATIFIED** (charter dependencies row). Enforcement test shape is pre-specified in the decision's freeze-gate.
2. **M6 config pipeline = the automation-definition loading substrate.** Doc 07 §3.3 (`automations.yaml`, slug identity, `automations.ids.yaml` companion) now loads through the shipped AMD-66..71 pipeline: AMD-66 listener classification governs automation hot-reload semantics; AMD-71 layout governs file placement; the M6.2 R-1 fail-closed `write()` posture constrains UI/API mutation of tag-bearing definitions (M10 note). The M7 AMD block must reconcile Doc 07 §3.3 with AMD-66/71 explicitly.
3. **OR-M6-NONCE-style co-design discipline** is the pattern for run-persistence hazards: R14-B RQ4 findings (timers, in-flight runs, REPLAY re-derive-never-re-execute — the AMD-41-class hazard) land as **explicit carry pins in the M7.x rows**, not prose.
4. **Module-info delta.** The automation `module-info.java` at `7c73c91` includes the plain `requires com.homesynapse.value` (M4.0b-4a) — **postdating the v3 "platform/event/device/state only" JPMS verification**. The briefs embed the CURRENT file verbatim (done); any researcher claim keyed to the old 4-edge picture is stale by construction.
5. **`InvokeIntegrationAction`/`ParallelAction`** remain Tier-2 reserved and are NOT in the M7 block (unchanged; recorded so the briefs' guardrails can cite it).

## 5. What the briefs and charter cite

Re-anchored disposition state: **REC-31/32/33/34/35/37/38/40 ACCEPT (unchanged, M7 AMD block; REC-35 explicitly AMD-routed) · REC-36 MODIFY+ACCEPT (unchanged) · REC-39 MODIFY+ACCEPT (re-anchored — §2.5 obligations 1–5 are the MODIFY content)**. Zero open DQs. New M7 entry-gate dependencies beyond Research 4: **C8 RATIFIED**, Doc 07 §3.3 ↔ AMD-66/71 reconciliation, the E70-1 type-residency decision for run identifiers (§2.5.1). High-water remains **REC-140**; W0 mints nothing.
