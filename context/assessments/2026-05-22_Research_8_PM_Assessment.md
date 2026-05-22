<!--
file: context/assessments/2026-05-22_Research_8_PM_Assessment.md
purpose: PM assessment of Research 8 (Device Model Implementation) — dispositions, modifications, follow-up questions, Nick-verified corrections.
audience: PM, Nick
state-type: current
status: CURRENT
last-verified: 2026-05-22 (post Nick source-verification)
-->

# Research 8 — PM Assessment (v2 — post Nick source-verification)

**Date:** 2026-05-22
**Document:** Research 8: Device Model Implementation — Sealed Hierarchy Expansion and AttributeValue Extensions
**RECs assessed:** REC-23 through REC-30 (8 total)
**Researcher:** Claude Project
**Protocol:** 6-step A–F processing per PM research pipeline
**v2 update:** Incorporates Nick's source-verified corrections to FQ-1 through FQ-5, plus 5 errors the initial PM assessment missed.

---

## Disposition Table (FINAL — post source-verification)

| REC | Title | Disposition | Milestone | Dependencies | AMD? | Risk | v2 changes |
|---|---|---|---|---|---|---|---|
| REC-23 | EntityCategory on Entity + entity_registered | **ACCEPT** (scope reduced) | M4.0 | None | YES (Entity record only; ~~EntityState~~ withdrawn) | LOW | Category on `Entity` only, NOT `EntityState`. AMD-47 withdrawn. |
| REC-24 | QuantityValue as AttributeValue permit | **ACCEPT** | M4.0 | REC-30 (batch) | YES (AttributeValue.permits) | MEDIUM | Permits clause corrected (5 existing, not 7). |
| REC-25 | device_reachable_changed event (device-level) | **ACCEPT** (interaction clarified) | M4.0 | None | No | LOW-MEDIUM | Handler updates existing `Availability` enum on child `EntityState` records. Must be idempotent with `availability_changed`. §5 spike withdrawn. |
| REC-26 | SemanticTag replaces labels | **MODIFY** + ACCEPT | M4.0 | REC-29 (CRITICAL) | YES (Entity record) | HIGH | Unchanged. |
| REC-27 | ArrayValue with full-replacement | **ACCEPT** | M4.0 | REC-30 (batch) | YES (with REC-24) | LOW-MEDIUM | Unchanged. |
| REC-28 | DispatchingProjectionAdvancer | **MODIFY** + ACCEPT | M4.0 | None | **No** (PM mods eliminate subpackage AMD) | HIGH (architectural) | OR-M3-17 closure mechanism now fully understood — dispatch table eliminates the separate derivation function. |
| REC-29 | AttributeValueUpcaster SPI | **ACCEPT** | M4.0 | None | No | MEDIUM | Unchanged. |
| REC-30 | Batch Capability expansion (**8** permits) | **ACCEPT** (scope reduced) | M4.0 | None | YES (Capability.permits) | MEDIUM | Reduced from 10 to 8 permits. `OccupancySensor` (→ `Occupancy` exists) and `ContactSensor` (→ `Contact` exists) removed as duplicates. ~430 LOC (was ~520). |

---

## Modifications

### REC-28 — Three PM Modifications

| Mod | Change | Rationale |
|---|---|---|
| A | Reject ServiceLoader; use constructor injection | DECIDE-04 (no ServiceLoader). All handlers are in the same module. Composition root assembles the handler list explicitly. |
| B | Eliminate handlers subpackage; handlers are package-private in `com.homesynapse.state` | Preserves one-flat-package invariant. Eliminates the AMD the researcher identified. |
| C | Rename `ChainedProjectionAdvancer` → `DispatchingProjectionAdvancer` | "Dispatching" accurately describes map-lookup semantics; "Chained" implies chain-of-responsibility. |

### REC-26 — One PM Modification

| Mod | Change | Rationale |
|---|---|---|
| Integration test gate | `LabelsToTagsUpcaster` must have a CI-gated integration test deserializing a REAL pre-M4 `EntityRegistered` JSON blob | Highest-risk migration path; synthetic unit tests insufficient. |

### REC-23 — Nick-directed scope reduction

| Mod | Change | Rationale |
|---|---|---|
| Remove EntityState.category | Category lives on `Entity` (device-model) ONLY. EntityState does not carry structural entity metadata. | MODULE_CONTEXT key design decision #6: `StateQueryService` doesn't support filtered/joined queries. Category filtering is the API layer's job, joining `Entity.category` with `EntityState` at query time. |

### REC-25 — Nick-directed interaction clarification

| Mod | Change | Rationale |
|---|---|---|
| Use existing Availability enum | `device_reachable_changed` handler updates `Availability` field on child `EntityState` records using the existing `Availability { AVAILABLE, UNAVAILABLE, UNKNOWN }` enum. No new enum. | State-store already models entity-level availability via `availability_changed` events. `device_reachable_changed` is a new *cause* for the same state transition. Handler must be idempotent with `availability_changed`. |
| Withdraw §5 spike | In-memory ConcurrentHashMap — no SQL join, no latency concern. | FQ-2 resolved: state store is in-memory map, not SQLite-backed query. |

### REC-30 — Nick-directed scope reduction

| Mod | Change | Rationale |
|---|---|---|
| 8 permits, not 10 | Remove `OccupancySensor` and `ContactSensor` from the batch. | `Occupancy` and `Contact` already exist in the current Capability hierarchy. |

---

## §7 Corrections (comprehensive — PM initial + Nick source-verified)

### Package name errors (PM-caught, Research 3 pattern)

| Error | Researcher wrote | Correct value |
|---|---|---|
| state-store package | `com.homesynapse.statestore` | `com.homesynapse.state` |
| rest-api package | `com.homesynapse.rest` | `com.homesynapse.api.rest` |
| state-store module-info module name | `com.homesynapse.statestore` | `com.homesynapse.state` |
| REC-28 handlers subpackage | `com.homesynapse.statestore.handlers` | Eliminated by PM mod B — handlers are package-private in `com.homesynapse.state` |

### Type name errors (Nick source-verified — PM MISSED these)

| Error | Researcher wrote | Correct value |
|---|---|---|
| AttributeValue permits (§7.3) | `BoolValue, IntValue, LongValue, DoubleValue, StringValue, InstantValue, JsonValue` (7 permits) | `BooleanValue, IntValue, FloatValue, StringValue, EnumValue` (5 permits). `LongValue`, `DoubleValue`, `InstantValue`, `JsonValue` are phantom types. `FloatValue` and `EnumValue` were missing. |
| Entity.capabilities type | `Set<Capability>` | `List<CapabilityInstance>` — wraps capability metadata (featureMap, version, namespace, attributes schema, commands, confirmation policy) |
| Capability permit count | "15 + CustomCapability" | 16 permits total (15 standard + CustomCapability). `Occupancy` and `Contact` already exist — researcher's proposed `OccupancySensor` and `ContactSensor` are duplicates. |

### EntityState field list errors (Nick source-verified — PM MISSED these)

| Error | Researcher wrote | Correct value |
|---|---|---|
| EntityState.id | `id` | `entityId` |
| EntityState.lastEventPosition | Listed as a field | **Phantom field** — does not exist |
| EntityState.adapterId | Listed as a field | **Phantom field** — does not exist |
| EntityState.capabilities | Listed as a field | **Phantom field** — capabilities live on `Entity`, not `EntityState` |
| EntityState.availability | Missing | **REAL field** — `Availability { AVAILABLE, UNAVAILABLE, UNKNOWN }` |
| EntityState.stateVersion | Missing | **REAL field** |
| EntityState.lastChanged | Missing | **REAL field** |
| EntityState.lastReported | Missing | **REAL field** |

**Actual EntityState fields (9):** `entityId`, `attributes`, `availability`, `stateVersion`, `lastChanged`, `lastUpdated`, `lastReported`, `staleAfter`, `stale`.

### Entity record field list errors (Nick source-verified)

| Error | Researcher wrote | Correct value |
|---|---|---|
| Entity field count | 8 fields (implied) | 11 fields (verified by `EntityTest.exactlyElevenFields()`) |
| Entity.id | `id` (EntityId) | `entityId` (EntityId) |
| Entity.type | `type` (EntityType) | `entityType` (EntityType) |
| Entity.name | `name` (String) | `displayName` (String) |
| Entity.capabilities | `Set<Capability>` | `List<CapabilityInstance>` |
| Entity.registeredAt | `registeredAt` (Instant) | `createdAt` (Instant) |
| Missing fields | — | `entitySlug` (String), `endpointIndex` (int), `areaId` (AreaId, nullable), `enabled` (boolean) |

**Actual Entity fields (11):** `entityId`, `entitySlug`, `entityType`, `displayName`, `deviceId` (nullable), `endpointIndex`, `areaId` (nullable), `enabled`, `labels` (List\<String\>), `capabilities` (List\<CapabilityInstance\>), `createdAt`.

### Visibility and design boundary errors

| Error | Researcher wrote | Correct value |
|---|---|---|
| `DegradedAttributeValue` visibility | package-private | Must be PUBLIC (PM-caught, Nick-confirmed) |
| EntityCategory on EntityState | Proposed adding `category` to EntityState | **Design boundary violation** (Nick-caught). Category on `Entity` only. StateQueryService doesn't support filtered queries — filtering by category is the API layer's job. |
| Existing Availability enum | Not mentioned | State-store already has `Availability { AVAILABLE, UNAVAILABLE, UNKNOWN }` and processes `availability_changed` events. REC-25 must integrate with this, not introduce parallel concepts. |

### Other errors

| Error | Researcher wrote | Correct value |
|---|---|---|
| REC-23 AMD in §4 | "AMD: none required" | AMD required (§7.7 correctly identifies this; §4 is internally inconsistent) |
| EntityState post-REC-23 field count | "10th field before stale; stale is 11th" | **MOOT** — category does not go on EntityState |
| Switch-site audit (§7.3) | Lists types that don't exist at `76288af` | Forward-looking for M4 planning; not current codebase state |

**Pattern note:** This is the same category of type-name / field-list error seen in Research 3. The Claude Project researcher does not have MODULE_CONTEXT files; these errors are systematic and predictable. The correction pipeline (PM assessment → Nick source-verification) is working but the PM must not trust §7 type/field details without MODULE_CONTEXT cross-reference.

---

## AMD Candidates for M4.0 (FINAL)

| AMD # (proposed) | Scope | Affected Types | Source RECs | Status |
|---|---|---|---|---|
| AMD-44 | `Entity` record signature expansion | `Entity`: add `EntityCategory category`, change `labels: List<String>` → `tags: List<SemanticTag>` | REC-23 + REC-26 | RETAINED |
| AMD-45 | `AttributeValue.permits` expansion | `AttributeValue`: add `QuantityValue`, `ArrayValue`, `DegradedAttributeValue` (public) | REC-24 + REC-27 + REC-29 | RETAINED |
| AMD-46 | `Capability.permits` batch expansion | `Capability`: add **8** new permits (Thermostat, WindowCovering, DoorLock, MediaPlayer, EnergyMeasurement, WaterValve, Fan, AirQuality) | REC-30 | RETAINED (scope reduced from 10 to 8) |
| ~~AMD-47~~ | ~~`EntityState` record field expansion~~ | ~~`EntityState`: add `category`~~ | ~~REC-23~~ | **WITHDRAWN** (design boundary violation — category on Entity only) |

**Total: 3 AMDs.** All ratified at the M4.0 architecture council meeting.

---

## Follow-Up Questions — RESOLVED

All 5 follow-up questions resolved by Nick's source-verified answers. No outstanding questions for the Claude Project.

| FQ | Status | Resolution |
|---|---|---|
| FQ-1 (Entity fields) | RESOLVED | 11 fields confirmed. `labels: List<String>` exists. `capabilities: List<CapabilityInstance>` (not `Set<Capability>`). |
| FQ-2 (Reachability join) | RESOLVED | In-memory ConcurrentHashMap. No SQL join. Denormalize at write time (option a). Spike unnecessary. |
| FQ-3 (DegradedAttributeValue) | RESOLVED | Public in `com.homesynapse.device`. Confirmed. |
| FQ-4 (OccupancySensor/Motion) | RESOLVED | `Occupancy` and `Contact` already exist. Remove duplicates from REC-30. |
| FQ-5 (OR-M3-17 closure) | RESOLVED | Dispatch table eliminates separate derivation function. Handlers write derived state directly. No new events produced — in-memory state updates only. |

---

## OR-M3-17 Closure Analysis (updated)

OR-M3-17 (NO_OP_DERIVATION) stays open through M3.7. Closes at M4.0 when REC-28's `DispatchingProjectionAdvancer` lands. The closure mechanism:

- The `Function.identity()` derivation placeholder in M3.7's `StateProjection.create(...)` covers the case where an inbound event needs to produce derived outbound state.
- With the dispatch table, each handler's `apply()` writes derived state directly to the projection context. No separate derivation function needed.
- Concrete M4 derivation cases:
  - `device_reachable_changed` → updates `Availability` on all child `EntityState` records (using existing `Availability` enum)
  - `entity_registered` with `category` → sets `Entity.category` (no EntityState change)
- Neither case produces a new event — they update in-memory state.
- The dispatch table IS the derivation mechanism. OR-M3-17 closes naturally.

---

## M4.0 Implementation Order (Nick-approved)

1. **REC-28** (DispatchingProjectionAdvancer) — architectural gateway, unblocks all handlers
2. **REC-23** (EntityCategory on Entity only, NOT EntityState) — low risk, no state-store changes
3. **REC-25** (device_reachable_changed + Availability integration) — careful interaction with existing `availability_changed` handler
4. **REC-24 + REC-27** (QuantityValue + ArrayValue) — batched AttributeValue.permits AMD
5. **REC-29** (AttributeValueUpcaster SPI) — prerequisite for REC-26
6. **REC-26** (SemanticTag replaces labels) — highest risk, upcaster-dependent
7. **REC-30** (Capability batch expansion, 8 permits) — last, touches adapter modules

---

## M3.7 Impact

**None.** All 8 RECs are M4.0 scope. M3.7 proceeds as planned with `MinimalProjectionAdvancer` (REC-20). OR-M3-17 stays open through M3.7; closes at M4.0 with REC-28.

---

## Key Insights Internalized (updated post source-verification)

1. **Type-name string identity (LTD-19's EventTypeRegistry) is the load-bearing forward-compatibility mechanism** for sealed hierarchy expansion. `DegradedAttributeValue` parallels `DegradedEvent` at the subtype level.
2. **Full-replacement ArrayValue semantics are non-negotiable** — delta semantics are incompatible with bounded-window advancer.
3. **Device-level reachability is the CAUSE; entity-level Availability is the PROJECTED STATE.** `device_reachable_changed` → handler updates existing `Availability` enum on child `EntityState` records. No new enum needed. These are complementary layers, not alternatives.
4. **The DispatchingProjectionAdvancer is the M4 gateway** — every new event type is a new handler. Constructor-injected (DECIDE-04), package-private handlers in the flat package, `AdvanceResult.skipped()` for unknown types. This also closes OR-M3-17 by making the dispatch table itself the derivation mechanism.
5. **The upcaster SPI (REC-29) enables sealed hierarchy versioning** without breaking stored event deserialization. `DegradedAttributeValue` is the subtype-level fallback.
6. **EntityState does NOT carry structural entity metadata.** Category, capabilities, device grouping live on `Entity` (device-model). `StateQueryService` serves runtime state; the API layer joins structural and runtime data at query time. This is a design boundary that Research 8 and the initial PM assessment both violated.
7. **The state store is an in-memory ConcurrentHashMap, not SQLite-backed queries.** Performance concerns about joins or read latency are non-issues for the projection; the ≤2s bounded-window contract governs the event-store read, not the state-store read.

---

## Research Quality Assessment

**Grade: B+.** Platform deep-dives are excellent (Matter list semantics, JSR 385 rejection, Axon upcasting). Strategic recommendations are correct (full-replacement ArrayValue, device-level reachability, batch hierarchy expansion, type-name string identity). The systematic weakness — fabricated type/field names without MODULE_CONTEXT access — is predictable and correctable via the PM→Nick verification pipeline. The pipeline caught everything.

---

## Next Steps

1. **Research 4 prompt produced** — saved to `context/instructions/Research_4_Automation_Engine_Brief.md`. RECs start at REC-31. Incorporates Research 8 findings.
2. **M3.7 coding instruction** — proceed independently. No Research 8 findings affect M3.7 scope.
3. **M4 planning** — after Research 4 is processed, begin M4 milestone backlog with the 8 accepted/modified RECs from Research 8, in the implementation order above.

---

**Assessment completed:** 2026-05-22 by PM (Cowork session).
**v2 updated:** 2026-05-22 — incorporates Nick's source-verified corrections (FQ answers, 5 PM-missed errors, EntityState/Entity field lists, Availability enum interaction, design boundary enforcement).
