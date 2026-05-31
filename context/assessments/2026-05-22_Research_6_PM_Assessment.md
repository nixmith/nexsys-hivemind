<!--
file: context/assessments/2026-05-22_Research_6_PM_Assessment.md
purpose: PM assessment of Research 6 (Integration Runtime — Supervisor Patterns for Protocol Adapters) — dispositions, modifications, source-verified fabrications, decision questions for Nick.
audience: PM, Nick
state-type: current
status: v1 (PM-verified against MODULE_CONTEXT.md + module-info.java + source; Nick verification PENDING for NQ-1..6). 2026-05-31: AMD-RENUMBER NOTICE added (AMD-53..63 are stale placeholders — see banner; integration block re-bases to 54+ per P2).
last-verified: 2026-05-22 (content); 2026-05-31 (AMD-renumber annotation)
-->

# Research 6 — PM Assessment (v1)

**Date:** 2026-05-22
**Document:** Research 6: Integration Runtime — Supervisor Patterns for Protocol Adapters
**RECs assessed:** REC-41 through REC-52 (12 total)
**AMDs proposed:** AMD-53 through AMD-63 (11 candidates) — ⚠️ **STALE PLACEHOLDERS — see the AMD-RENUMBER NOTICE banner below before using any of these integers.**
**Researcher:** Claude Project
**Protocol:** 6-step A–F processing per PM research pipeline
**Verification base:** `integration/integration-api/src/main/java/module-info.java` + `MODULE_CONTEXT.md`, `integration/integration-runtime/src/main/java/module-info.java` + `MODULE_CONTEXT.md`, `core/state-store/.../module-info.java`, `config/configuration/.../module-info.java`, `core/persistence/.../MigrationRunner.java`, plus targeted grep across the codebase.

---

> ⚠️ **AMD-NUMBER RENUMBER NOTICE (added 2026-05-31 — stale-on-arrival for Workstream C).**
> Every AMD number in this assessment — AMD-53 … AMD-63, including the AMD-53/54/55/56/57/58/59/60/62/63 dispositions in the table, the NQ rows, and the §"AMD Sequencing" list — is a **non-binding provisional placeholder that was never authored as a file.** Two things have moved since 2026-05-22:
> 1. **AMD-53 is now consumed by the timestamp-model unifier** (`design/amendments/AMD-53_Timestamp_Model_Unifier_Event_Time_Activity_Timestamps.md`, RATIFIED; shipped as M4.0b-5, committed `c99b425`, 2026-05-31). It is **not** REC-41.
> 2. Per the **P2 AMD Renumbering Decision** (`context/decisions/2026-05-29_P2_AMD_Renumbering_Decision.md` — §3 allocation note dated 2026-05-31 + §4/§6 assign-at-milestone rule), the integration block is **assigned contiguously at the Workstream-C briefing from the live watermark**, and its indicative range **re-bases to 54+** (was "≈ 53–62"). The provisional per-REC map in §4 of that decision (REC-41→54, REC-42→55, … shifted up by one) is a **planning aid only — non-binding**.
>
> **Action for the eventual Workstream C session:** do **not** author from any AMD number in this file. Assign the integration block fresh from the live watermark at C-briefing, **after** Research 6 NQ-1..6 are resolved (NQ-1..6 may still *split* an amendment — e.g. REC-41's lifecycle hooks vs config-schema versioning — so the count is not fixed either). The REC **dispositions**, the **NQ-1..6 PM leans**, and the **order** of the §"AMD Sequencing" list remain valid; only the integers are stale. See also `context/planning/2026-05-31_Workstream-C_gate-status.md`.

---

## Headline

**Grade: B+ overall. Strong §1–§6, fabrication pattern shifted from type names (Research 4/8 lesson) to JPMS module names (new Research 6 lesson).**

The brief's verified type inventories worked: all 22 integration-api type names + 4 integration-runtime type names + the 5 existing `IntegrationLifecycleEvent` permits + the 4-value `HealthState` + the 3-value `ExceptionClassification` + the 10-field `IntegrationContext` are used correctly throughout the research. Zero fabrication on existing type names. But the brief did not embed the verbatim `module-info.java` contents, and the researcher hallucinated module names in §7.8 — `com.homesynapse.event.model`, `com.homesynapse.state.store`, `com.homesynapse.configuration`, `com.homesynapse.integration.api`, `com.homesynapse.bootstrap`. Same fabrication mechanism, different layer of the cake. **Lesson encoded in the hivemind this session** (PM SKILL.md Step 3, `coding-instruction-format.md` Files-to-Read, research-agenda.md §2 CONSTRAINTS): verbatim `module-info.java` text must be embedded in every coding instruction and research brief that touches the module.

§1 verdicts are clear and defensible. §2 platform deep dives have specific primary-source quotes with URLs — substantially better than Research 4 §2. §3.1 concept-mapping table is the strongest single artifact. §3.3 over-abstraction analysis self-retracts `ExceptionClassification` granularity (rare and valuable). §5.4 explicitly self-flags two constraint violations — exactly the discipline Research 4 lacked.

---

## Disposition Table

| REC | Title | Disposition | Target | AMD | Risk | v1 notes |
|---|---|---|---|---|---|---|
| REC-41 | Four lifecycle hooks on `IntegrationAdapter` (`onConfigUpdated`, `onOptionsUpdated`, `onReauthRequired`, `migrate`) | **ACCEPT (MODIFY)** | M4 | AMD-53 | MEDIUM | Fix package name (`com.homesynapse.integration`, not `.integration.api`). Resolve `schemaVersion` vs `configSchemaMajor/Minor` (see NQ-2). Split AMD-53 into AMD-53 (hooks + outcomes) + AMD-53b (config schema versioning). |
| REC-42 | `HealthDetail` enum + `IntegrationHealthRecord` mods | **ACCEPT (MODIFY)** | M4 (enum) / M9 (population) | AMD-54 | MEDIUM | Drop `@Nullable String description` field (YAGNI; the `reason` field on lifecycle events already covers human-readable context). 12-value `HealthDetail` enum stands as proposed. Canonical-constructor change on `IntegrationHealthRecord` is breaking but acceptable — record is supervisor-internal, not adapter-facing. |
| REC-43 | Add `AUTH_FAILED` to `ExceptionClassification` | **ACCEPT** | M4 (enum) / M9 (routing) | AMD-55 | LOW | Wording fix: REC-43's text says "Affects `ExceptionClassifier`" — the type is the enum `ExceptionClassification`. No `ExceptionClassifier` service exists; the enum is what's being extended. Exhaustive switches in downstream code (Phase 3 supervisor + automation subscribers) need a default-throw audit. |
| REC-44 | Four new `IntegrationLifecycleEvent` records (dot-namespaced) | **ACCEPT** | M4 | AMD-56 | LOW | Per AMD-33: `IntegrationLifecycleEvent` and ALL permits live in `com.homesynapse.integration`, NOT event-model. §7.7's row "event-model gains 7 sealed cases" is wrong — strike it. The 5 new permits (REC-44's 4 + the `IntegrationReauthCompleted` in §7.3) land in integration-api alongside the existing 5. |
| REC-45 | `CredentialRotator` service on `IntegrationContext` | **ACCEPT (MODIFY)** | M4 | AMD-57 | MEDIUM | PM recommendation per NQ-1: take the aggregator option — one new field `SecurityServices security` bundling the rotator and future security services. Keeps `IntegrationContext` at 11 fields instead of 12. `SecureCredentialBundle` lives in `com.homesynapse.config` (NOT `.configuration`). |
| REC-46 | `softDependencies` + Kahn soft-edge semantics | **ACCEPT** | M4 (field) / M9 (Kahn) | AMD-58 | LOW | Clean. `IntegrationStartupOrderer` is a Phase 3 internal type (correctly identified). Soft-edge semantics (log at INFO, not WARN, when missing) match HA `after_dependencies`. |
| REC-47 | Capability events + `CapabilityPublisher` | **MODIFY — needs design pass** | M4 (events) / M9 (publisher) | AMD-59 | MEDIUM-HIGH | Three issues: (a) `CapabilityId` does NOT exist in `core/device-model` (verified via grep) — use `Class<? extends Capability>` permit class or existing `CapabilityInstance` as identity. (b) §7.7's row "state-store adds capability table" conflicts with Research 8 REC-23/REC-26 — capabilities live on `Entity` (device-model), `EntityState` carries no structural metadata. Strike the new SQLite table. (c) The two new events ARE state-changing — they need `ProjectionEventHandler` registrations in the M4 `DispatchingProjectionAdvancer` (Research 8 REC-28). |
| REC-48 | `BackoffParameters` on `IntegrationDescriptor` | **ACCEPT** | M4 | AMD-60 | LOW | HA's empirical 5/10/20/40/80 schedule is a defensible default. `@Nullable` annotation in `@Nullable BackoffParameters` violates codebase convention (Javadoc-only nullability) — fix during AMD authoring. |
| REC-49 | `RestartIntensity` on `IntegrationDescriptor` | **REJECT** | — | (none) | LOW | **Duplicates existing `HealthParameters.maxRestarts` + `restartWindow` fields** (verified per `integration-api/MODULE_CONTEXT.md` line 67). Use the existing fields. Researcher missed them. The OTP-derived `(intensity=1, period=60s)` *defaults* recommendation is still useful — document it as the recommended override on `HealthParameters.defaults()` for embedded systems, not a new record. |
| REC-50 | `IsolationLevel { IN_JVM, RESERVED_SUBPROCESS }` reservation | **ACCEPT (RENAME)** | M4 | AMD-62 | LOW | Rename field `isolationHint` → `isolationLevel` (matches enum name). Reservation-only, M9 supervisor rejects `RESERVED_SUBPROCESS` with `UnsupportedOperationException`. Cheap insurance against retroactive amendment. |
| REC-51 | Per-descriptor `plannedRestartTimeout` | **ACCEPT** | M4 | AMD-63 | LOW | Clean override of the global 60s. Doc 05 §3.14's 60s remains the fallback. |
| REC-52 | Eight internal supervisor types in `integration-runtime` | **ACCEPT (RENAME ONE)** | M9 | (none — Phase 3) | LOW | Rename `MigrationRunner` → `AdapterMigrationRunner`. **A `final class MigrationRunner` already exists in `core/persistence`** (V001/V002/V003 schema migrator, verified at source line 66). Simple-name collision would surface in any consuming module that requires both. Other seven names (`RestartLedger`, `HealthFsm`, `SupervisorVThreadRegistry`, `PlannedRestartCoordinator`, `ReauthDispatcher`, `ConfigUpdateApplier`, `CapabilityChangeRouter`) are conflict-free. |

**Summary: 8 ACCEPT, 3 MODIFY+ACCEPT, 1 REJECT. 10 AMDs ratified (AMD-53/54/55/56/57/58/59/60/62/63). AMD-61 withdrawn (REC-49 duplicated existing fields).**

---

## §7 Source-Verified Fabrications (PM-verified against module-info.java + source)

| # | Researcher wrote | Verified actual value | Affects |
|---|---|---|---|
| F1 | `com.homesynapse.integration.api` (package and JPMS module) | Both module name and package are `com.homesynapse.integration` (single name; no `.api` suffix). The module is at the `integration/integration-api` *Gradle path* but the JPMS identifier is `com.homesynapse.integration`. | REC-41 (line 222), §7.8 first block (line 622) |
| F2 | `requires transitive com.homesynapse.event.model` | `requires transitive com.homesynapse.event` (no `.model` suffix). | §7.8 both blocks |
| F3 | `requires com.homesynapse.state.store` | `requires transitive com.homesynapse.state` (no `.store` suffix; transitive on integration-api). | §7.8 |
| F4 | `requires com.homesynapse.configuration` | `requires transitive com.homesynapse.config` (no `.uration` suffix). | §7.8, REC-45 cross-module note |
| F5 | `exports com.homesynapse.integration.runtime to com.homesynapse.bootstrap` | No `com.homesynapse.bootstrap` module exists. The composition root is `com.homesynapse.app` (Gradle module `homesynapse-app`). Qualified-export target must be `com.homesynapse.app` if a qualified export is even warranted — Doc 05 says `integration-runtime` exports broadly (REST API + observability consume it), so the qualifier is likely incorrect entirely. | §7.8 second block |
| F6 | `CapabilityId` referenced as the identity type for capability records (REC-47) | No `CapabilityId` type exists in `core/device-model` (verified via grep). Capability identity in HomeSynapse is the sealed `Capability` permit class itself (e.g., `Motion.class`, `Occupancy.class`), wrapped at instance level by `CapabilityInstance` (existing type per Research 4 brief). | REC-47, §7.3 |
| F7 | Proposed `MigrationRunner` in `com.homesynapse.integration.runtime` (REC-52, §7.6) | A `final class MigrationRunner` already exists in `core/persistence` (V001/V002/V003 schema migrator, source confirmed at `MigrationRunner.java:66`). Simple-name collision would force fully-qualified imports in any consuming module. | REC-52 |
| F8 | "Affects `ExceptionClassifier` in `com.homesynapse.integration.runtime`" | The type is `ExceptionClassification` (the enum, source-confirmed at `ExceptionClassification.java:49`). No `ExceptionClassifier` service exists in the inventory. | REC-43 |

All eight are mechanical fixes. F1–F5 are search/replace on module names. F6/F7 need a rename decision (NQ-3 and per-REC). F8 is a wording slip.

---

## Open Questions for Nick (NQ-1 through NQ-6)

| # | Question | PM recommendation |
|---|---|---|
| NQ-1 | **`IntegrationContext` field count** — accept 11 (one field per security service, growing linearly with REC-45/REC-47/future services), or aggregate via a single `SecurityServices security` field? | **Aggregator.** Bundles `CredentialRotator` and future security services. Keeps the record at 11 fields. REC-47's `CapabilityPublisher` can be a separate aggregator (`DiscoveryServices`) or its own field — either is fine, but don't grow `IntegrationContext` field-by-field for every new service. |
| NQ-2 | **`schemaVersion` vs `configSchemaMajor/Minor` reconciliation** — the existing `int schemaVersion` on `IntegrationDescriptor` (source-verified at line 80) conflicts with the researcher's proposed `configSchemaMajor` + `configSchemaMinor` pair for REC-41's `migrate(...)`. | **Keep both, rename existing.** Rename the existing field to `descriptorSchemaVersion` (it's about the descriptor's forward-compatibility contract). Add `configSchemaMajor` + `configSchemaMinor` for the *config* schema version, which is what `migrate(...)` operates on. Two distinct concerns; do the rename in the same AMD-53 to make the distinction explicit. |
| NQ-3 | **REC-47 capability identity** — `CapabilityId` doesn't exist. Use sealed `Capability` permit class (`Class<? extends Capability>`), `CapabilityInstance`, or invent `CapabilityId`? | **Use the sealed `Capability` permit class as the type identity + existing `CapabilityInstance` as the instance identity.** `CapabilityAdded(integration, device, capability, instance, ts)` where `capability: Class<? extends Capability>` and `instance: CapabilityInstance`. Inventing a new `CapabilityId` adds a typed wrapper that nothing else in the system uses. |
| NQ-4 | **REC-47 storage model** — the researcher's §7.7 proposes a new `capability` SQLite table in state-store. This conflicts with Research 8 REC-23/REC-26: capabilities live on `Entity` (device-model), `EntityState` carries no structural metadata. | **No new SQLite table.** Capability events update `Entity.capabilities` via projection (the standard pattern from Research 8 REC-28's `DispatchingProjectionAdvancer`). The `CapabilityAdded` / `CapabilityRemoved` events are state-changing (entity-registry projection), not state-store projection. |
| NQ-5 | **REC-49 conflict with existing `HealthParameters.maxRestarts` + `restartWindow`** — researcher proposed a new `RestartIntensity` record but the equivalent fields already exist. | **Reject REC-49.** Use existing fields. Document the OTP-derived `(maxRestarts=1, restartWindow=60s)` as the recommended embedded-system override on `HealthParameters.defaults()`. AMD-61 withdrawn. |
| NQ-6 | **Default restart intensity for radio-based adapters** — OTP's embedded guidance (1/60s) may be too strict for Zigbee/Matter bridges that legitimately glitch a few times per minute during radio init. | **Keep 1/60s as the global default; rely on per-descriptor override (existing `HealthParameters.defaults()` mechanism).** Empirical spike candidate before M9 — measure actual Zigbee/Matter restart frequency on a Pi 5 during normal operation. |

---

## §1–§6 Strengths (kept for the record)

- **§1 Verdict 2 is the right framing.** Adding lifecycle hooks before M4 freeze is the single highest-impact finding. The retroactive-amendment-tax argument is correct and well-defended.
- **§2.1 OTP** quote is canonical Erlang doc text; the "dodos" pathological case (intensity=5/period=1, ten transient children) is a real edge case worth knowing.
- **§2.3 HA** verifies the 8-value `ConfigEntryState` enum with `(value, recoverable)` tuples and the backoff math `2 ** min(self._tries, 4) * 5` → 5/10/20/40/80/80... — arithmetic-checkable, correct.
- **§3.1 concept-mapping table** is production-quality, 13 rows, all five platforms compared on each row.
- **§3.3 over-abstraction analysis** self-retracts `ExceptionClassification` granularity — exactly the discipline Research 4 lacked.
- **§3.4 competitive assessment** is honest about uncalibrated weights ("weights are not empirically calibrated").
- **§5.4 self-flagged constraint violations** is the Research 4-lesson-learned applied: researcher explicitly tells PM "you must decide" rather than silently breaking the inventory.

---

## §1–§6 Weaknesses

- **§7.7 ownership rows are wrong about modules.** Sealed `IntegrationLifecycleEvent` and all permits live in `integration-api`, not event-model — that is the entire AMD-33 rationale. Strike the "event-model gains 7 sealed cases" row.
- **§7.7 double-counts.** The "supervisor-module (M9) — wires ReauthDispatcher, ConfigUpdateApplier, MigrationRunner — ~400 LOC" row double-counts the same code listed in §7.6 (8 internal types in integration-runtime, ~1400 LOC). There is no separate supervisor-module; integration-runtime IS the supervisor module.
- **§7.6 type-name collision** with `core/persistence/MigrationRunner.java` (F7).
- **`@Nullable` annotations** in §7.4 violate the codebase convention (no nullability annotations; Javadoc `{@code null} if…` patterns only — confirmed in integration-api MODULE_CONTEXT Gotchas).

---

## M7-Style Implementation Order

Sequencing for the M4 and M9 work below, ranked to minimize rework:

**M4 (Phase 2 amendments before any new code lands):**
1. **AMD-53 + AMD-53b** (REC-41 lifecycle hooks + schema-version split, NQ-2) — interface change first; everything else depends on the hook shapes.
2. **AMD-55** (REC-43 `AUTH_FAILED`) — enum change touches REC-41's `onReauthRequired` routing.
3. **AMD-54** (REC-42 `HealthDetail`) — record change to `IntegrationHealthRecord`.
4. **AMD-56** (REC-44 four lifecycle events + REC-47 two capability events, addressed per NQ-3/4) — sealed hierarchy expansion.
5. **AMD-57** (REC-45 `SecurityServices` aggregator per NQ-1) — `IntegrationContext` field add.
6. **AMD-58** (REC-46 `softDependencies`), **AMD-60** (REC-48 `BackoffParameters`), **AMD-62** (REC-50 `isolationLevel`), **AMD-63** (REC-51 `plannedRestartTimeout`) — descriptor field additions, mutually independent.

**M9 (Phase 3 supervisor implementation):**
- REC-52 internal types (`RestartLedger`, `HealthFsm`, `SupervisorVThreadRegistry`, `PlannedRestartCoordinator`, `ReauthDispatcher`, `ConfigUpdateApplier`, `AdapterMigrationRunner`, `CapabilityChangeRouter`).
- Kahn's algorithm soft-edge semantics (REC-46 behavior).

---

## Key Insights Internalized

1. **JPMS module names are as fabrication-prone as type names** — and the brief must embed verbatim `module-info.java` text to prevent it. Lesson encoded today in three places: `project-manager/SKILL.md` Step 3, `project-manager/references/coding-instruction-format.md` Files-to-Read, and `context/planning/research-agenda.md` §2 CONSTRAINTS.
2. **The brief's verified type inventories worked** — zero existing-type-name fabrication across 22 + 4 types. The pattern is correct; it just needs the second layer (module identifiers) added.
3. **Researcher's self-flagged constraint violations (§5.4) saved a v2 round.** Tell future researchers: when in doubt, surface the contradiction in a §5.x section rather than silently breaking the inventory.
4. **REC-49 missed an existing field** — the verified type inventory listed `HealthParameters` with its 11 fields including `maxRestarts` and `restartWindow`, but the researcher didn't cross-reference. Reading the inventory is not enough; the researcher must verify whether each proposed field already exists by name match.
5. **Cross-research consistency check** caught REC-47's storage proposal (NQ-4) — capabilities on `Entity`, not a new SQLite table, per Research 8 REC-23/REC-26. The PM's job is to enforce coherence across the research arc; the researcher does not have the full memory of prior decisions.

---

**Assessment completed:** 2026-05-22 by PM (Cowork session).
**Status:** v1 — PM-verified against MODULE_CONTEXT.md + module-info.java + source. Nick verification PENDING for NQ-1 through NQ-6 (strategic / scope calls only — no source-verification items remain open).
**Next step:** Nick decides NQ-1..6; Research 6 v2 finalizes; AMD-53..60 + AMD-62/63 proceed to ratification.
