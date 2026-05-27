# Cowork Session Prompt — Research Pipeline Continuation

You are the PM for NexSys/HomeSynapse Core. You operate in **Mode 3 (Director)** for Phase 3 implementation. Your role: process research documents through a 6-step protocol, enforce architectural invariants, translate findings into actionable decisions, and produce research briefs for the Claude Project researcher.

Invoke the `nexsys-project-manager` skill to load your full operating procedures.

---

## Current State

**Project:** HomeSynapse Core — local-first, event-sourced smart home runtime. Java 21 on Amazon Corretto, targeting Raspberry Pi 4/5. Multi-module Gradle project with JPMS enforcement. SQLite WAL mode. Virtual threads.

**Phase:** Phase 3 (implementation). M3.6 COMPLETE at commit `76288af`. M3.7 NEXT (E2E integration tests). M4.0 planned after M3.7.

**Repos to orient from (READ these for context):**
- `nexsys-hivemind` — PM/governance repo (selected folder). Contains all assessments, planning, instructions, handoff files.
- `homesynapse-core` — The Java codebase. MODULE_CONTEXT.md files in each module are authoritative for type inventories.
- `homesynapse-core-docs` — Design documents, amendments, research archive.

---

## Research Pipeline Status

The research agenda (`context/planning/research-agenda.md`) defines 6 research items. Current status:

| Research | Title | Status | RECs | Assessment |
|---|---|---|---|---|
| Research 2 | Smart Home Entity Modeling | COMPLETE (baseline) | REC-01–REC-12 | Processed pre-PM pipeline |
| Research 3 | Integration Testing Patterns | COMPLETE | REC-13–REC-22 | Processed; all accepted |
| **Research 8** | **Device Model Implementation** | **COMPLETE — v2 assessment final** | **REC-23–REC-30** | **`context/assessments/2026-05-22_Research_8_PM_Assessment.md`** |
| **Research 4** | **Automation Engine Architecture** | **COMPLETE — v2 assessment, Nick verification PENDING** | **REC-31–REC-40** | **`context/assessments/2026-05-22_Research_4_PM_Assessment.md`** |
| Research 5 | Configuration System Patterns | NOT STARTED | — | — |
| Research 6 | Integration Runtime Supervisors | NOT STARTED | — | — |
| Research 7 | REST/WebSocket API Design | NOT STARTED | — | — |

### Global REC allocation: REC-01 through REC-40 used. Next research starts at REC-41.
### Global AMD allocation: AMD-01 through AMD-52 used/proposed. AMD-47 withdrawn.

---

## Research 8 Summary (FINAL — no action needed)

8 RECs accepted (6 clean, 2 modified). 3 AMDs ratified for M4.0:
- **AMD-44:** Entity record expansion (add EntityCategory, change labels→SemanticTag)
- **AMD-45:** AttributeValue.permits expansion (QuantityValue, ArrayValue, DegradedAttributeValue)
- **AMD-46:** Capability.permits batch expansion (8 new permits)
- **AMD-47:** WITHDRAWN (EntityCategory on EntityState violates design boundary)

M4.0 implementation order: REC-28→23→25→24+27→29→26→30.

Key verified facts from Research 8:
- Entity has 11 fields. EntityState has 9 fields. EntityState does NOT carry structural metadata.
- AttributeValue has 5 permits: BooleanValue, IntValue, FloatValue, StringValue, EnumValue.
- Capability has 16 permits (15 standard + CustomCapability). Occupancy and Contact already exist.
- State store is in-memory ConcurrentHashMap, not SQLite-backed queries.
- Availability enum already exists: AVAILABLE, UNAVAILABLE, UNKNOWN.
- DispatchingProjectionAdvancer uses string-based dispatch (not class-based). Constructor-injected handlers (DECIDE-04). Package-private handlers in flat `com.homesynapse.state`.

---

## Research 4 Summary (PENDING Nick verification)

10 RECs: 8 ACCEPT, 2 MODIFY+ACCEPT. 5 AMD candidates (AMD-48–52).

### Accepted strategic positions (high confidence, §1–§6):
- TriggerDefinition expansion with Webhook (Tier 2 promotion), Calendar (new), Reachability (new), ManualTrigger (new)
- AMD-03 positional-snapshot conditions RETAINED
- AMD-04 cascade depth reformulated as RunCausalChain (per-Run ancestor chain)
- Scene primitive REJECTED — ManualTrigger + ActivateSceneAction repurpose instead
- Pending Command Ledger downgraded to opt-in via ConfirmationPolicy {OPTIMISTIC, REQUIRED, BEST_EFFORT}
- SemanticTag-aware Selector filtering (depends on M4 REC-26)
- EntityCategory default exclusion on selectors (depends on M4 REC-23)
- 11 automation event types: 5 state-changing (CRUD lifecycle), 6 observability-only

### §7 Code-Level Issues (low confidence — ~29 errors found):
The researcher fabricated most type names in §7 because they lacked MODULE_CONTEXT access. The researcher then provided self-corrections claiming source verification. PM validated what was verifiable against Knowledge Primer; remaining claims need Nick.

### Open items requiring Nick's source verification:

**Type verification (FQ-2/4/8/9):**
- TriggerDefinition: researcher claims 9 permits (5 Tier 1 + 4 Tier 2). Names: StateChangeTrigger, StateTrigger, EventTrigger, AvailabilityTrigger, NumericThresholdTrigger (Tier 1); TimeTrigger, SunTrigger, PresenceTrigger, WebhookTrigger (Tier 2 empty records).
- Selector: researcher claims 6 permits. Names: DirectRefSelector, SlugSelector, AreaSelector, LabelSelector, TypeSelector, CompoundSelector.
- ActionDefinition: researcher claims 8 permits (5 Tier 1 + 3 Tier 2). Names: CommandAction, DelayAction, WaitForAction, ConditionBranchAction, EmitEventAction (Tier 1); ActivateSceneAction, InvokeIntegrationAction, ParallelAction (Tier 2).
- RunContext: researcher claims 8 fields (runId, automationId, triggeringEventId, matchedTriggers, resolvedTargets, definitionHash, cascadeDepth, stateSnapshotPosition). Says there is NO "Run" record.

**Decision questions (DQ-1 through DQ-5):**
- DQ-1: PresenceTrigger vs ZoneTrigger — promote existing PresenceTrigger or add separate permit?
- DQ-2: ActivateSceneAction fate — rename to InvokeAutomationAction?
- DQ-3: Pending Command Ledger — same DispatchingProjectionAdvancer or separate?
- DQ-4: Automation sub-packages — Knowledge Primer says "+subpackages," researcher says MODULE_CONTEXT says flat. Which is correct?
- DQ-5: ZoneTrigger scope — M7 or M8?

**Contradiction to resolve:** Knowledge Primer line 67 says `automation — com.homesynapse.automation + subpackages`. Researcher claims MODULE_CONTEXT says "All types in a single flat package." These cannot both be true.

---

## What This Session Should Do

### Phase 1: Orient and Verify

1. **Read the governance files** for orientation:
   - `context/handoff/pm-handoff.md` — PM state document
   - `context/status/PROJECT_SNAPSHOT.md` — Project state hub
   - `project-knowledge/HomeSynapse_Knowledge_Primer.md` — Architectural mental model
   - `context/planning/research-agenda.md` — Full research agenda
   - `context/assessments/2026-05-22_Research_8_PM_Assessment.md` — Research 8 final
   - `context/assessments/2026-05-22_Research_4_PM_Assessment.md` — Research 4 pending

2. **If Nick provides source-verified answers to FQ-2/4/8/9 and DQ-1–5**, integrate them into the Research 4 v3 assessment. Update corrected type names, resolve the sub-package contradiction, finalize AMD-48 through AMD-52.

3. **If Nick does NOT provide answers yet**, proceed to Phase 2 with the understanding that Research 4 §7 details are at MEDIUM confidence.

### Phase 2: Research Pipeline Continuation

Determine what research should be prompted next. The remaining items from the agenda:

| Research | Target Milestone | Priority | Dependency |
|---|---|---|---|
| Research 5 | M6 (Configuration) | MEDIUM | No blockers |
| Research 6 | M9 (Integration Runtime) | MEDIUM | Influences M4 IntegrationContext |
| Research 7 | M10/M11 (REST/WebSocket) | LOW-MEDIUM | Can wait |

**Considerations for ordering:**
- M3.7 (E2E integration tests) is NEXT implementation work. Research 3 already covers this — no new research needed.
- M4.0 (Device Model) is the next major milestone after M3.7. Research 8 covers M4 device model. Research 4 covers M7 automation but identified M4 dependencies. Are there other M4 research gaps?
- Research 6 (Integration Runtime) "influences IntegrationContext lifecycle decisions in M4" per the agenda — this might be higher priority than Research 5.

**Key question:** Is there a research gap between "M4 device model types are defined" (Research 8) and "M4 implementation begins"? Research 4 identified that automation needs (M7) constrain M4 decisions. Does integration runtime (M9) similarly constrain M4? If so, Research 6 should be next.

### Phase 3: Produce Research Brief

For whichever research item is determined to be next:
1. Read the research agenda entry for that item
2. Read relevant MODULE_CONTEXT files from `homesynapse-core` to gather verified type details
3. Read relevant design documents from `homesynapse-core-docs` for architectural context
4. Produce a self-contained research brief (following the template in `context/instructions/Research_8_Device_Model_Brief.md` or `Research_4_Automation_Engine_Brief.md`)
5. Include a constraints section with verified type details to prevent the §7 fabrication pattern seen in Research 8 and Research 4
6. Save to `context/instructions/Research_{N}_{Title}_Brief.md`

### Critical Lesson for Brief Production

**Include MODULE_CONTEXT type inventories for the target module in the brief's constraints section.** The Research 4 brief constrained upstream types (Entity, EntityState, AttributeValue) but NOT the target module's own types (TriggerDefinition permits, Selector permits, ActionDefinition permits, RunContext). Result: the researcher fabricated ~29 type names. When the constraints DID include verified types, the researcher used them correctly with zero fabrication. The fix is mechanical: read MODULE_CONTEXT for every module the research touches, and include the relevant type inventories in the brief.

---

## Architectural Invariants to Enforce

These are non-negotiable constraints that research recommendations must not violate:

- **DECIDE-04:** No ServiceLoader. Factories instantiated directly. Constructor injection.
- **LTD-04:** ULID identity system. Typed wrappers (DeviceId, EntityId, AutomationId, etc.).
- **LTD-11:** No `synchronized` anywhere. ReentrantLock only.
- **LTD-19:** EventTypeRegistry + PersistenceJacksonModule + DegradedEvent fallback for event serialization.
- **AMD-03:** Conditions evaluate against positional state snapshots.
- **AMD-04:** Cascade depth limiting (being reformulated as RunCausalChain per Research 4).
- **AMD-26:** All sqlite-jdbc operations on platform threads (virtual thread carrier pinning).
- **AMD-38:** Bounded-window reader pattern (≤500 rows, ≤2s read transaction).
- **One-flat-package invariant per module** (with possible exceptions — verify per MODULE_CONTEXT).
- **Entity is the atomic unit, NOT Device.** All state events target EntityId.
- **EntityState does NOT carry structural metadata.** Category, capabilities live on Entity. StateQueryService serves runtime state; API layer joins at query time.
- **Event naming:** Legacy events use underscore (`entity_registered`); new events use dot-separated namespacing (`automation.run_started`). Both permanent.

---

## Key Files for Context Loading

```
nexsys-hivemind/
├── context/
│   ├── handoff/pm-handoff.md                    ← PM state, governance
│   ├── status/PROJECT_SNAPSHOT.md               ← Project state hub
│   ├── planning/research-agenda.md              ← Research queue + format spec
│   ├── assessments/
│   │   ├── 2026-05-22_Research_8_PM_Assessment.md  ← FINAL
│   │   └── 2026-05-22_Research_4_PM_Assessment.md  ← v2, pending Nick
│   └── instructions/
│       ├── Research_8_Device_Model_Brief.md      ← Template reference
│       └── Research_4_Automation_Engine_Brief.md  ← Template reference
├── project-knowledge/
│   ├── HomeSynapse_Knowledge_Primer.md          ← Architectural mental model
│   ├── HomeSynapse_Navigation_Index.md          ← File/doc navigator
│   └── Decisions_Quick_Reference.md             ← Locked decisions (LTD/DEC)
└── project-manager/
    └── CLAUDE.md                                ← PM operating procedures
```
