<!--
file: context/audits/2026-06-05_AMD-54-64_DOCS_Review_Return.md
purpose: DOCS-Project ratification-review return for the Workstream C integration AMD block (AMD-54..64), per the 2026-06-05 review brief.
audience: Nick (ratify), PM
state-type: audit/review return
status: COMPLETE — all gates run; G1 ran against the inline Research 6 return (received complete, §1–§7, terminates "*End of Research 6.*")
baseline: homesynapse-core HEAD `e76b925` (independently confirmed: `git log` head = "e76b925 M4.B-S2: EntityRole enum + EntityType legality matrix + …")
-->

# DOCS-Project Review Return: Workstream C Integration AMD Block (AMD-54 … AMD-64)

**Inline-input status (per the brief's confabulation guard):** the Research 6 return ("Integration Runtime — Supervisor Patterns for Protocol Adapters") was supplied INLINE and is **complete** — §1 Executive Summary through §7 Code-Level Implications, ending "*End of Research 6.*". No section is missing or truncated. All G1/G2 fidelity gates ran against that inline copy only. No gate returns INCOMPLETE.

---

## 1. Per-AMD Verdict Table

| AMD | Verdict | Blocking items | Edits (E#) |
|---|---|---|---|
| **AMD-54** | **RATIFY-AS-IS** | none | none |
| **AMD-55** | **RATIFY-WITH-EDITS** | none | E1 (arithmetic), E2 (reauth outcome signal — Nick call), E3 (failed-apply vocabulary — Nick call) |
| **AMD-56** | **RATIFY-WITH-EDITS** | none | E4 (route-(a) trigger is unimplementable as worded — wording fix required before freeze) |
| **AMD-57** | **RATIFY-WITH-EDITS** | none | E5 (R4 fired: the 12-value list differs from REC-42 in 11 of 12 entries — Nick must arbitrate list vs. AMD-57-INV-02; verbatim REC-42 list supplied in §2.R4) |
| **AMD-58** | **RATIFY-WITH-EDITS** | none | E6 (R5 fired: 2 permit-name + 4 event-string diffs vs. REC-44/§7.3 — recommend keeping PM names, recording deviation in Review Disposition), E7 (migration-failure vocabulary gap) |
| **AMD-59** | **RATIFY-WITH-EDITS** | none | E8 (research's `CapabilityRemovalReason` silently dropped — add or record deliberate drop) |
| **AMD-60** | **RATIFY-WITH-EDITS** | none | E9 (R7: widen to `rotate(Map<String,String>)` — the AMD's own pre-authorized fallback; rationale in §3.R7) |
| **AMD-61** | **RATIFY-AS-IS** | none | none |
| **AMD-62** | **RATIFY-WITH-EDITS** | none | E10 (doc-only: record the dropped `maxConsecutiveBeforeSuspend` field and its NQ-5 rationale) |
| **AMD-63** | **RATIFY-AS-IS** | none | none |
| **AMD-64** | **RATIFY-AS-IS** | none | none |

No AMD is BLOCKING. No constraints-catalogue violation was found anywhere in the block (§6).

---

## 2. G1 — Research-Fidelity Diffs (verbatim, against the inline return)

### R4 (AMD-57) — `HealthDetail` vs. return §REC-42

**Count: CONFIRMED.** REC-42 proposed exactly 12 values; AMD-57 has exactly 12. But the lists are **different taxonomies**, not a transcription drift — only `NONE` matches exactly (and `AUTH_FAILED`≈`AUTH_FAILURE`).

Researcher's verbatim list (return §REC-42):

> Add `HealthDetail` enum (`NONE`, `COMMUNICATION_ERROR`, `CONFIGURATION_ERROR`, `AUTH_FAILED`, `BRIDGE_OFFLINE`, `DUTY_CYCLE_THROTTLED`, `RATE_LIMITED`, `STARTUP_TIMEOUT`, `RESOURCE_LIMIT`, `DEPENDENCY_FAILED`, `MIGRATING`, `DISABLED_BY_USER`). Add `HealthDetail detail` and `@Nullable String description` to `IntegrationHealthRecord`.

AMD-57's PM-reconstructed list: `NONE, HEARTBEAT_TIMEOUT, KEEPALIVE_TIMEOUT, ERROR_RATE_EXCEEDED, TIMEOUT_RATE_EXCEEDED, SLOW_CALL_RATE_EXCEEDED, PROBE_FAILED, RESTART_LIMIT_EXCEEDED, SUSPENSION_LIMIT_EXCEEDED, RESOURCE_QUOTA_EXCEEDED, AUTH_FAILURE, PERMANENT_FAILURE`.

**The diff is not mechanically resolvable.** AMD-57 §2.1 instructs "replace it verbatim if it differs," but verbatim replacement breaks **AMD-57-INV-02** as written ("values map 1:1 to supervisor transition triggers") — REC-42's `DISABLED_BY_USER`, `MIGRATING`, `BRIDGE_OFFLINE`, `DEPENDENCY_FAILED` are operator-cause values (OpenHAB `ThingStatusDetail`-derived, per return §2.4(d): *"add a `HealthDetail` reason enum with at minimum `COMMUNICATION_ERROR`, `CONFIGURATION_ERROR`, `BRIDGE_OFFLINE` (parent integration down), `DUTY_CYCLE_THROTTLED` (Zigbee-specific but reusable), and `AUTH_FAILED`"*), not threshold-transition triggers. The PM list is trigger-oriented (1:1 with the source-verified `HealthParameters` surface). **Nick must arbitrate (E5):** (a) adopt REC-42 verbatim and reword INV-02; (b) keep the PM list, rewrite the §2.1 provenance note so it no longer promises verbatim replacement, and record the deviation in §10 Review Disposition; or (c) union the operator-cause values the PM list lacks. The reviewer leans (b) with selective adoption of `DEPENDENCY_FAILED` and `MIGRATING` (both have AMD-55/61 counterpart flows in this very block); semantics and component placement are unaffected either way, as AMD-57 itself states. Also note: the return's `@Nullable String description` was dropped by documented PM disposition — sound (Javadoc-only nullability rule; narrative lives in lifecycle-event `reason`).

### R5 (AMD-58) — five permits vs. return §REC-44 + §7.3

**`IntegrationReauthCompleted`: CONFIRMED present in the return** — it appears only in §7.3 (REC-44's code block has four records; §7.3 lists five lifecycle rows plus two capability rows). Verbatim §7.3 row:

> | `IntegrationReauthCompleted` | `"integration.reauth_completed"` | id, ts, success | observability only |

Name/string diffs (researcher → AMD-58):

| Return §REC-44/§7.3 (verbatim name, string) | AMD-58 | Diff |
|---|---|---|
| `IntegrationConfigUpdated`, `"integration.config_updated"` | `IntegrationConfigUpdated`, `integration.config.updated` | string leaf `_`→`.` |
| `IntegrationOptionsUpdated`, `"integration.options_updated"` | `IntegrationOptionsUpdated`, `integration.options.updated` | string leaf `_`→`.` |
| `IntegrationReauthRequested`, `"integration.reauth_requested"` | `IntegrationReauthRequired`, `integration.reauth.required` | **name + string** |
| `IntegrationReauthCompleted`, `"integration.reauth_completed"` | `IntegrationReauthCompleted`, `integration.reauth.completed` | string leaf `_`→`.` |
| `IntegrationMigrated`, `"integration.migrated"` | `IntegrationMigrationCompleted`, `integration.migration.completed` | **name + string** |

Per-permit field diffs: the researcher's records carry `id`/`ts` and payload fields, verbatim from §REC-44: `IntegrationConfigUpdated(IntegrationId id, Instant timestamp, int configHashBefore, int configHashAfter, ConfigUpdateOutcome outcome)`; `IntegrationOptionsUpdated(IntegrationId id, Instant timestamp, Set<String> changedKeys)`; `IntegrationReauthRequested(IntegrationId id, Instant timestamp, String reason)`; `IntegrationMigrated(… int fromMajor, int fromMinor, int toMajor, int toMinor, boolean success)`. AMD-58 drops `timestamp` (correct — envelope-owns-time house rule; the existing five permits carry none, source-verified), folds `id`/`reason` into the sealed parent's source-verified 5-accessor contract (correct), drops `configHashBefore/After` and `changedKeys` in favor of `ConfigUpdateOutcome outcome` (thinner audit narrative — acceptable; `reason` covers narrative per INV-HO-04), and replaces `boolean success` with `MigrationOutcome`.

**Recommendation (E6):** keep the PM names. `IntegrationReauthRequired`/`integration.reauth.required` is coherent with the `onReauthRequired()` hook (the return is internally inconsistent here — its §3.1 table names the hook `onReauthRequired` while its event says `reauth_requested`); `IntegrationMigrationCompleted` pairs with `MigrationOutcome`. The fully-dotted strings are the better fit to the project-wide `automation.run.*`/`config.*` direction. Record all five diffs in §10 Review Disposition so the fidelity trail is preserved.

**E7 (field-level gap):** the researcher's `boolean success` admits `false`; `MigrationOutcome { MIGRATED, NOT_REQUIRED }` cannot express a failed migration, and AMD-55 §2.3 routes migrate-failure to FAILED via `PermanentIntegrationException` — so a failed migration emits **no** migration event at all (only a health transition). Either add a `FAILED` value to `MigrationOutcome` (AMD-55's enum) and emit the event on failure, or add one sentence to AMD-58 §2.1 stating that migration failure is deliberately represented by the FAILED lifecycle transition, not by this event. Reviewer leans the one-sentence documentation; Nick's call.

### R2 (AMD-55) — four hook signatures vs. return §REC-41

Researcher's verbatim signatures (return §REC-41):

> ```java
> default ConfigUpdateOutcome onConfigUpdated(
>     IntegrationConfig oldConfig,
>     IntegrationConfig newConfig
> ) throws IntegrationConfigException {
>     return ConfigUpdateOutcome.RESTART_REQUIRED;
> }
>
> default void onOptionsUpdated(IntegrationOptions newOptions) { /* no-op */ }
>
> default ReauthOutcome onReauthRequired(ReauthContext ctx) {
>     return ReauthOutcome.UNSUPPORTED;
> }
>
> default boolean migrate(
>     int fromMajor, int fromMinor,
>     int toMajor, int toMinor,
>     IntegrationConfig oldConfig
> ) {
>     return fromMajor == toMajor;
> }
> ```

The researcher's two outcome enums: `ConfigUpdateOutcome` — three values per return §2.5(d): *"`onConfigUpdated` should return `ConfigUpdateOutcome` (RESTART_REQUIRED / APPLIED_IN_PLACE / REJECTED) so a failed apply triggers supervisor restart with the prior config"* — and `ReauthOutcome` (only `UNSUPPORTED` is named). (Internal research inconsistency for the record: §7.2's table adds `throws IntegrationMigrationException` to `migrate`, absent from the REC-41 code block.)

Diff vs. AMD-55 §2.1/§2.2:

| Aspect | Return | AMD-55 | Assessment |
|---|---|---|---|
| `onConfigUpdated` params | `(IntegrationConfig old, IntegrationConfig new)` | `(ConfigChangeSet changes)` | **Sound — superior.** `IntegrationConfig`/`IntegrationConfigException` do not exist at `e76b925` (verified: zero matches); `ConfigChangeSet(Instant timestamp, List<ConfigChange> changes)` exists, and `ConfigChange(String sectionPath, String key, Object oldValue, Object newValue, ReloadClassification reload)` carries per-key old/new — the return's load-bearing requirement (§2.5(d): *"pass both old and new so adapters can diff and avoid recreating expensive resources"*) is preserved at finer grain. |
| `ConfigUpdateOutcome` values | `RESTART_REQUIRED / APPLIED_IN_PLACE / REJECTED` | `{ APPLIED, RESTART_REQUIRED }` | **E3.** Dropping `REJECTED` loses the researcher's failed-apply → restart-with-prior-config vocabulary, and the AMD also drops the `throws` clause, leaving no specified channel for "I tried to apply and failed." Either add `REJECTED` (supervisor restarts with prior config — frozen semantics, M9 behavior) or document that apply-failures are signaled by thrown exception and classified per AMD-56's taxonomy. The shape freezes now, so this should be settled now. |
| `onOptionsUpdated` | `void`, no-op default, `IntegrationOptions` | `ConfigUpdateOutcome`, `RESTART_REQUIRED` default, `ConfigChangeSet` | Deviation, defensible: `IntegrationOptions` doesn't exist; the conservative default honors AMD-55 §2.4's "defaults never silently claim a capability." Note it costs the research's options-are-in-place presumption until adapters opt in. Accept. |
| `onReauthRequired` | `ReauthOutcome onReauthRequired(ReauthContext ctx)`, default `UNSUPPORTED` | `void onReauthRequired()`, default no-op | **E2 — the one signature diff with real consequence.** With `void`, the supervisor cannot distinguish "adapter initiated async reauth (await `integration.reauth.completed`)" from "default no-op (will never complete)". AMD-56 §2's Javadoc promises *"If the adapter does not implement re-auth (default no-op hook), the supervisor degrades to the standard suspension policy"* — undetectable with a void no-op except by timeout. The researcher's `ReauthOutcome.UNSUPPORTED` exists precisely to make non-implementation observable. Recommend `ReauthOutcome onReauthRequired()` with `{ INITIATED, UNSUPPORTED }`, default `UNSUPPORTED` (dropping `ReauthContext`, which doesn't exist and whose contents the return never specifies, is fine). Alternative: keep `void` and document the M9 timeout-based fallback in AMD-55/56 — but the enum is one file and removes a frozen-surface ambiguity. Nick's call; reviewer recommends the enum. |
| `migrate` params/return | 5 params incl. `toMajor/toMinor/oldConfig`, returns `boolean`, default `fromMajor == toMajor` | `(int fromMajor, int fromMinor)`, returns `MigrationOutcome`, `throws PermanentIntegrationException`, default `NOT_REQUIRED` | **Sound narrowing.** The to-pair is the adapter's own AMD-54 declaration (it knows it); old config arrives via the injected `ConfigurationAccess` (AMD-55 Javadoc says so); `MigrationOutcome` is clearer than the researcher's overloaded boolean; the `throws` aligns failure with `initialize()`'s established taxonomy. Accept. |

**E1 (mechanical):** AMD-55 §4 — "4 → 10 declared members (4 existing + 4 default hooks…)" is arithmetic drift: 4 + 4 = **8** declared methods (the 2 enums are separate files, as the same sentence says). Fix to "4 → 8".

### R3 (AMD-56) — did REC-43 propose a dedicated auth exception type?

**Yes — both the enum value and a dedicated type.** Verbatim from return §REC-43:

> Also add `IntegrationAuthException extends RuntimeException` to `integration-api` as the canonical signal type.

So AMD-56 §2's "the assessment records only the enum addition" understates the return: the researcher proposed the type. The AMD's deferral of the type to M9 is a legitimate PM narrowing — and the researcher's `extends RuntimeException` would in fact contradict the shipped hierarchy (`HomeSynapseException` is source-verified `abstract class … extends Exception`, i.e. checked) — **but the deferral as worded has a defect, E4:** route (a) says AUTH_FAILED maps from *"a `PermanentIntegrationException` whose error code is `integration.auth_failed`"*, and the shipped `PermanentIntegrationException` hard-codes `private static final String ERROR_CODE = "integration.permanent_failure"` with `errorCode()` returning it and **no constructor accepting a code** (source-verified). The only way to produce `integration.auth_failed` from that type is a subclass — which *is* a new exception type, the very thing the AMD says it does not add and defers. The frozen trigger contract therefore references an unimplementable mechanism. Required wording fix (choose one): (i) reword route (a) to "an error-code surface to be provided at M9 — either a code-bearing constructor on `PermanentIntegrationException` or a typed subclass, M9's choice"; or (ii) adopt the researcher's typed exception now as a checked `HomeSynapseException` subclass in integration-api (one small final class; honors the return; kills the ambiguity). Reviewer mildly prefers (ii); (i) is acceptable. Also for the record: the return's enum ordering placed `AUTH_FAILED` third (before `SHUTDOWN_SIGNAL`); AMD-56 appends last with the documented AMD-44 declaration-order rationale — sound deviation, already documented in the AMD. The note that no `ExceptionClassifier` service exists is confirmed (integration-runtime main = `ExceptionClassification, IntegrationHealthRecord, IntegrationSupervisor, SlidingWindow, package-info` only; no production `switch` over the enum exists at `e76b925`).

---

## 3. G2 — PM Narrowings (soundness verification; pre-co-signed)

### R6 (AMD-59 §2.1 payload refinement) — SOUND on all three counts

(a) **Serde argument sound.** A `Class<? extends Capability>` component in a persisted payload requires FQN-string encode + `Class.forName` decode — exactly the reflective typing the AMD-52 discipline excludes (AMD-52-INV-02 is built on explicit type tags and bans `@JsonTypeInfo`; the Jackson-isolation HARD RULE keeps annotations off device-model types). And it is redundant: `CapabilityInstance.capabilityId` (source-verified component 1 of 7) already carries type identity in persisted form. (b) **No research contradiction of entity-targeting.** The return's REC-47 records are device-keyed (`DeviceId device, CapabilityId capability`), but the return itself classifies both events *"state-changing (updates entity registry)"* and never argues for device-scoped identity; NQ-4 projects into `Entity.capabilities`, and `Entity` is source-verified to carry `deviceId` + `endpointIndex` — one device, many entities — so a deterministic projection **requires** `EntityId`. The AMD keeps `deviceId` too (a superset of the research fields). Also note the return's `CapabilityId` type collides with ratified NQ-3 ("no new CapabilityId wrapper"); the AMD's `String capabilityId` is the NQ-3-correct rendering (`CapabilityId` confirmed nonexistent in source). (c) **Replay self-sufficiency (AMD-59-INV-02) holds:** `CapabilityAdded` embeds the complete `CapabilityInstance`; `CapabilityRemoved` carries the removal identity; the §2.5 projection (append-with-same-id-replace / remove-matching) is a deterministic function of the log alone. The dropped `discoveredAt`/`lostAt` payload timestamps are the same envelope-owns-time rule applied in AMD-58 — sound.

**E8:** the return's `CapabilityRemoved` carries `CapabilityRemovalReason reason  // FIRMWARE_DOWNGRADE | DEVICE_REPLACED | TRANSIENT_LOSS | UNREGISTERED` (verbatim). AMD-59 drops the field without remark. It is not load-bearing for the projection, but it is audit/diagnostic vocabulary that is cheap now and a sealed-record amendment later; `TRANSIENT_LOSS` also interacts with orphan-detection semantics. Add the enum + field, or add one sentence recording the deliberate drop. Nick's call; reviewer mildly favors adding it.

One namespace note for the record: the return's strings were `integration.capability_added/_removed`; AMD-59 uses `capability.added/.removed` under a separate `CapabilityEvent` hierarchy. Sound — the lifecycle parent's source-verified 5-accessor contract (`previousState/newState/reason`) is meaningless for capability changes, and a new family gets its own dot namespace per the project direction. Record as a deviation in §10.

### R7 (AMD-60 §2.1 rotate narrowing) — strict trigger NOT met; widen recommended anyway

REC-45 never enumerates `SecureCredentialBundle` fields — there is **no** explicit token+refresh-token field list anywhere in the return. The bundle appears only as an opaque carrier, verbatim:

> ```java
> public interface CredentialRotator {
>     CompletableFuture<Void> rotate(IntegrationId id, SecureCredentialBundle bundle);
>     SecureCredentialBundle current(IntegrationId id);
> }
> ```

So the AMD's conditional ("if the review finds the research's bundle carried load-bearing extra fields … widen") is **not strictly triggered**. However, the bundle's *atomicity* is load-bearing by construction: return §1 Verdict 5 names OAuth adapters (*"OAuth-bearing cloud adapters (Nest, Tado, Netatmo) cannot recover via supervisor restart alone"*), and an OAuth rotation is an access-token + refresh-token **pair**. Single-key `rotate(String, String)` with AMD-60-INV-03's per-call durable-before-return means a crash between two calls persists a torn pair — precisely the inconsistency a bundle prevents. **E9: widen to `void rotate(Map<String,String> secrets)`** (atomic multi-key; single-key callers pass `Map.of(k, v)`); this is the AMD's own pre-authorized fallback, stays inside the `SecretEntry` string vocabulary (no new bundle type — the narrowing's anti-duplication rationale survives intact), and costs nothing. Flagged for Nick per the AMD's own clause. Two further deviations verified sound: dropping `current(...)` (read path belongs to `ConfigurationAccess`; the rotator is a write-only seam — documented in the AMD) and sync-durable vs. the return's `CompletableFuture<Void>` (one-virtual-thread-per-adapter makes blocking correct and simpler). `SecretEntry(String key, String value, Instant createdAt, Instant updatedAt)` source-verified as claimed.

### R1 (AMD-55 §6 options-vs-config deferral) — CONFIRMED, research does not require freezing the partition

The return never defines which keys are "options" vs. "config." Its closest statements: §2.3(a) *"Options flows allow runtime-tunable parameters distinct from setup data"* and gap table #4 *"Options-flow / runtime-tunable parameters … operators must restart to change poll intervals, log levels."* Nothing in REC-41 or §7.2 demands the partition be frozen at M4; only the hook *shape* is M4-blocking (§1 Verdict 2). AMD-55's deferral to M6/M9 matches the research's intent. Gate closed.

---

## 4. G3 — Source-Shape Spot Checks (independent re-derivation at `e76b925`)

All confirmed by direct Read of the source, not from the AMDs:

- `IntegrationDescriptor` = **8 components**, `int schemaVersion` **last**, declared at **line 80** (`IntegrationDescriptor.java:72-81`); defensive-copy pattern at lines 105-107. ✓
- `IntegrationContext` = **10 components** (`integrationId, integrationType, eventPublisher, entityRegistry, stateQueryService, healthReporter, configAccess, schedulerService, telemetryWriter, httpClient`). ✓
- `HealthParameters` = 11 fields; `defaults()` = **(120s, 20, 5m, 1h, 5, 3, 60s, 30s, 5m, 3, 2)** — Javadoc list verified verbatim, incl. `maxRestarts: 3`, `restartWindow: 60 seconds`. ✓
- `IntegrationHealthRecord` = **13 components**, exactly the list AMD-57 §1 recites, incl. `boolean plannedRestart` last. ✓
- `ExceptionClassification` = **3 values**, declaration order `TRANSIENT, PERMANENT, SHUTDOWN_SIGNAL`. ✓
- `IntegrationLifecycleEvent` = sealed, **5 permits**, and the 5-accessor contract exactly as AMD-58 recites: `integrationId(), integrationType(), previousState()` (Javadoc: *"nullable … for IntegrationStarted"*), `newState(), reason()`. ✓
- `IntegrationEvents.LIFECYCLE_EVENT_CLASSES` = **5 entries** (`List.of(IntegrationStarted, IntegrationStopped, IntegrationHealthChanged, IntegrationRestarted, IntegrationResourceExceeded)`). ✓
- `EventTypes` INTEGRATION_* = **5 snake_case constants**; **zero** dot-namespaced strings exist anywhere in `EventTypes` (grep count 0). ✓ `IntegrationEventTypeAnnotationTest` pins `startsWith("integration_")` (line 137) and `EXPECTED_SUBTYPES.hasSize(5)` — AMD-58 §2.2's consequence claim is accurate. ✓
- `CapabilityInstance` = **7 components led by `String capabilityId`**. ✓ `Capability` sealed = **16 permits** (15 standard + `CustomCapability`). ✓
- `Entity` = **12 components incl. `List<CapabilityInstance> capabilities`** (post-B-S2 shape: `entityId, entitySlug, entityType, displayName, deviceId, endpointIndex, areaId, enabled, labels, capabilities, entityRole, createdAt`). ✓
- Both `module-info.java` files match the AMD-54 §7 / AMD-56 §6 embeds **character-for-character** (same seven `requires transitive` lines + single export for integration-api; `requires transitive com.homesynapse.integration` + single export for integration-runtime). ✓
- `IntegrationAdapter` = exactly 4 declared methods with the exact signatures AMD-55 recites (`initialize() throws PermanentIntegrationException; run() throws Exception; close(); CommandHandler commandHandler()`). ✓
- `RequiredService` = 3 values, `TELEMETRY_WRITER` last (append point for `DISCOVERY, SECURITY` as both AMDs state). ✓
- Supporting claims: `ConfigChangeSet(Instant, List<ConfigChange>)` ✓; `SecretEntry(key, value, createdAt, updatedAt)` ✓; persistence `MigrationRunner` collision is real (`core/persistence/.../MigrationRunner.java` exists — AMD-55 §6's `AdapterMigrationRunner` rename is warranted) ✓; config-module `ConfigMigrator`/`MigrationResult` exist (AMD-54 §3 cross-reference warranted) ✓; `StubIntegrationContextTest` = 39 `@Test` methods exactly as AMD-60 claims ✓; none of the new type names collide with existing types (`IntegrationConfig, IntegrationOptions, ReauthContext, IntegrationAuthException, CapabilityId, SecureCredentialBundle, IsolationLevel, BackoffParameters, CredentialRotator, SecurityServices, DiscoveryServices, CapabilityPublisher, HealthDetail` — all zero matches) ✓.

**Zero JPMS changes: CONFIRMED.** Every new type lands in `com.homesynapse.integration` or `com.homesynapse.integration.runtime`, both already exported. Every referenced foreign type rides an existing `requires transitive` edge: `EntityId`/`DeviceId`/`CapabilityInstance`/`Capability` via `com.homesynapse.device`; `IntegrationId` via `com.homesynapse.platform`; `DomainEvent`/`@EventType` via `com.homesynapse.event`; `ConfigChangeSet` via `com.homesynapse.config`; `Duration`/`Map`/`Set` via `java.base`. `EventTypes` gains string constants only. (For the record: the return's §7.8 module-info sketches use module names that do not exist — `com.homesynapse.integration.api`, `com.homesynapse.event.model`, `com.homesynapse.configuration` — and proposed a qualified-export topology change; the AMDs correctly ignored all of it, and the R7 narrowing moots the `configuration`-export proposal entirely.)

---

## 5. G4 — Cross-Block Coherence

- **AMD-55 `migrate(fromMajor, fromMinor)` consumes AMD-54's pair** — explicit both directions (AMD-54 §3 / AMD-55 §2.2 Javadoc). ✓
- **AMD-56 `AUTH_FAILED` → AMD-55 `onReauthRequired`** — Javadoc-bound in AMD-56 §2; **AMD-58 closes the loop** with `integration.reauth.required`/`integration.reauth.completed`, and the strings cross-referenced from AMD-55 §2.2 and AMD-56 §2 match AMD-58's table exactly. ✓ (Subject to E2/E4 — the loop's *mechanics* have the two gaps noted, but the three AMDs are mutually consistent.)
- **`IntegrationContext` 10 → 12**: AMD-60 appends `security` (component 11), AMD-59 appends `discovery` (component 12); both AMDs state the same final layout, both nullable, both `RequiredService`-gated; **`RequiredService` 3 → 5** with identical append order (`DISCOVERY, SECURITY` after `TELEMETRY_WRITER`) in both AMDs; the 10-arg convenience constructor is named in both. ✓ Consistent with the source-verified null-when-not-requested gotcha.
- **Descriptor 8 → 14 composes**: AMD-54 (+2: `configSchemaMajor`, `configSchemaMinor`), AMD-61 (+1 `softDependencies`), AMD-62 (+1 `backoffParameters`), AMD-63 (+1 `isolationLevel`), AMD-64 (+1 `plannedRestartTimeout`) = 14. **The single 8-arg convenience-ctor default story is complete and consistent**: `configSchemaMajor=1, configSchemaMinor=0` (AMD-54), `Set.of()` (AMD-61), `BackoffParameters.defaults()` non-null (AMD-62), `IN_JVM` non-null (AMD-63), `null`→global 60s (AMD-64) — every component has exactly one documented default, no AMD contradicts another. *Block-level nicety (non-blocking):* no single AMD pins the final 14-component declaration order (AMD-54 §2.3 implies append-in-AMD-number-order); recommend the ratification record state it explicitly so the Coder's canonical-ctor order is not inferred.
- **Dot-namespace decision coherent**: new families `integration.*` (AMD-58) and `capability.*` (AMD-59) match the project-wide direction (`automation.run.*`, `config.*`); the legacy snake_case five are stated frozen in AMD-58 §2.2, AMD-58-INV-02, and the §2.3 test-evolution note — everywhere it matters. The annotation-test prefix evolution (`integration_` or `integration.`) is specified and matches the source-verified current pin. ✓

No inter-AMD contradiction found.

---

## 6. G5 — Invariant Quality + Constraints Catalogue

**Invariants (AMD-54-INV-01 … AMD-64-INV-01, 24 total):** all use the amendment-scoped `AMD-NN-INV-NN` form; **no identifier or content collision with §20–§23** (AMD-47/51/52/53 blocks, read in full at `governance/Architecture_Invariants_v1.md:1098-1200`). Registrable as §24+ following the §20 precedent (contract registered at ratification; behavior implemented by a later WU — the same pattern as AMD-47's M4.B3 deferral, so the many "M9 behavioral, contract frozen here" invariants are convention-conformant). Each invariant is testable either by an M4.C shape/guard test the AMD itself enumerates or by a named M9 behavioral test; the sets are non-overlapping (AMD-56-INV-01 reauth-routing vs. AMD-55-INV-02 sequencing vs. AMD-58-INV-03 observability-only are adjacent but disjoint claims). **One reconciliation required:** AMD-57-INV-02's "values map 1:1 to supervisor transition triggers" is true of the PM list and false of the REC-42 list — it must be settled jointly with E5 (whichever list Nick picks, INV-02's wording must match it).

**Constraints catalogue — no violations:** no `ServiceLoader` (AMD-58 §2.3 / AMD-59 §3 use manifest-list registration, DECIDE-04-conformant); no Jackson in domain/api (AMD-59 §3 explicitly invokes annotation-free generic serde with STOP-and-report); no `@Nullable` annotations (AMD-62 and AMD-64 explicitly convert the return's `@Nullable` to Javadoc-only; AMD-57 drops the `@Nullable description` field); no `synchronized` anywhere (block is contract-only); typed-ULID identifiers throughout (`EntityId`/`DeviceId`/`IntegrationId`; `String capabilityId` is the NQ-3-ratified established vocabulary, not a new raw-string ID); LTD-17 enforced by AMD-59-INV-05 and AMD-60-INV-03; `DomainEvent` non-sealed extension (AMD-59's `CapabilityEvent`) is exactly the AMD-33 sanctioned pattern; persisted event-type strings immutable (AMD-58-INV-02); Register C voice present where reason/error text is specified (AMD-56's well-known code, AMD-63's rejection message); supervisor implementation deferred to M9 in every AMD's scope fences. ✓

---

## 7. Decision-Authority Conformance (not re-opened — rendering checked only)

NQ-1 rendered as aggregators (AMD-59 `DiscoveryServices`, AMD-60 `SecurityServices`, AMD-60-INV-01) ✓. NQ-2 rendered exactly (rename + pair, AMD-54) ✓. NQ-3 rendered (permit class + `CapabilityInstance`, no wrapper; AMD-59-INV-03) ✓. NQ-4 rendered (no SQLite table; entity-registry projection; AMD-59-INV-01/§2.5) ✓. NQ-5 rendered (no `RestartIntensity` record; 1/60s documented as embedded override in AMD-62 §2.3) ✓. NQ-6 rendered (global default kept; per-descriptor override; pre-M9 Zigbee spike named) ✓. P2 §8.1 rendered (AMD-54 + AMD-55 as two full integers) ✓. Post-B-S2 freeze base (Entity 12 / ProposedEntity 4 at `e76b925`) — Entity independently verified at 12; the block touches neither. ✓

---

## 8. Block Verdict

**RATIFY-WITH-EDITS.** Nothing blocking; zero constraint violations; zero JPMS drift; every PM source-shape claim survived independent re-derivation. The required edits, in priority order:

1. **E4 (AMD-56)** — fix the unimplementable route-(a) trigger wording (or adopt a typed checked auth exception). Required before freeze: the trigger contract as written cannot be implemented against the shipped `PermanentIntegrationException`.
2. **E5 (AMD-57)** — Nick arbitrates the HealthDetail taxonomy (REC-42 verbatim list supplied above); reconcile AMD-57-INV-02 with the choice.
3. **E2/E3 (AMD-55)** — reauth outcome signal and failed-apply vocabulary; both are frozen-surface shape decisions, settle now.
4. **E9 (AMD-60)** — widen to `rotate(Map<String,String>)` (pre-authorized fallback; atomic OAuth pair rotation).
5. **E6/E7 (AMD-58)**, **E8 (AMD-59)** — record name deviations in Review Disposition; settle migration-failure vocabulary and the dropped `CapabilityRemovalReason`.
6. **E1 (AMD-55)**, **E10 (AMD-62)** — mechanical/doc-only.

Per the brief's confabulation guard: every research claim above is quote-backed from the inline return; every source claim is Read-verified at `e76b925` and is re-derivable by the PM from the cited files/lines.

---

## 9. Addendum — Arbitration Outcomes and Ratification (2026-06-05, post-return)

Nick accepted the return (second-opinion PM concurred with the block verdict) and arbitrated every open item; all edits were folded pre-ratification and the block was **RATIFIED 2026-06-05**:

- **A1 (E5, AMD-57):** PM transition-trigger taxonomy KEPT; research's operator-cause taxonomy declined (OpenHAB self-report vs. HomeSynapse metrics-aggregation — the return's own §1 verdict rationale); may resurface as observability display labels.
- **A2 (E6, AMD-58):** PM permit names KEPT (`IntegrationReauthRequired`, `IntegrationMigrationCompleted`); fidelity diffs recorded in the AMD and §2.R5 above.
- **A3 (E2, AMD-55):** `ReauthOutcome { INITIATED, UNSUPPORTED }` ADOPTED, default `UNSUPPORTED`. Fidelity check: no `FAILED` member exists in the return — none added.
- **A4 (E4, AMD-56):** code-bearing constructor pair ADDED to the existing `PermanentIntegrationException` (append-only); research's `IntegrationAuthException` DECLINED (also wrong base: `RuntimeException` vs. the checked `HomeSynapseException` hierarchy). Frozen as AMD-56-INV-03.
- **A5 (E9, AMD-60):** `rotate(Map<String,String>)` ADOPTED as primary + `default` single-key convenience; AMD-60-INV-03 strengthened to atomic-across-entries.
- **E3 ruling (AMD-55):** `REJECTED` ADDED to `ConfigUpdateOutcome` (outcome-enum channel over exception-typing; defined safe recovery = prior config). Frozen as AMD-55-INV-04.
- **E7 ruling (AMD-58):** FAILED-transition route DOCUMENTED with the deliberate REJECTED-asymmetry principle (rejected apply has a valid fallback state; failed migration has none); `MigrationOutcome` gains no `FAILED`.
- **E8 ruling (AMD-59):** `CapabilityRemovalReason` (FIRMWARE_DOWNGRADE | DEVICE_REPLACED | TRANSIENT_LOSS | UNREGISTERED) RESTORED onto `CapabilityRemoved` + `publishRemoved(...)`; descriptive-only doctrine frozen as AMD-59-INV-06 (Research 12 Aqara transient-loss evidence cited).
- **E1/E10:** applied as mechanical/doc-only edits. **A6:** AMD-54/61/63/64 ratified as-is; R6/R7 co-signs formalized.

Invariant deltas vs. §1's table introduced by the arbitration edits: **+AMD-55-INV-04, +AMD-56-INV-03, +AMD-59-INV-06** (29 invariants registered, §24–§34).

*End of review return.*
