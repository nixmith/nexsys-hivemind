<!--
file: context/audits/2026-06-06_M3-M4_foundation-readiness-assessment.md
purpose: Forward-looking, artifact-level readiness assessment of the M3→M4 foundation (code + docs) — what the harder modules ahead (M6–M15 + the long-horizon invariants) will NEED from the foundation that isn't there yet, is under-specified, is stubbed/placeholder/dead, or is too thin for the complexity that's coming.
audience: PM, Nick
update-cadence: frozen
state-type: history
status: CURRENT
last-verified: 2026-06-06 against homesynapse-core HEAD 8ef9e9f (M4 COMPLETE; watermark AMD-64; projectionVersion 5) and homesynapse-core-docs HEAD.
-->

# M3→M4 Foundation-Readiness Assessment (forward-looking gap analysis)

**Date:** 2026-06-06
**Author:** PM (Cowork governance session)
**Subject:** The system as **designed and built across M3 → M4** — event distribution, state projection/derivation, persistence, the device + value model, the integration-api freeze, the composition root, and the foundational invariants/contracts — assessed against the question: *when we build the harder modules that come next, what will they need from this foundation that isn't there yet, is under-specified, is stubbed/dead, or is too thin?*
**Method:** Documents-only. Code re-read at HEAD `8ef9e9f`; every load-bearing code claim was source-verified (file:line) this session, not taken from the pre-M4 investigation. Four parallel source-verification passes (forward foundations vs HEAD; the 14 design docs §8 + contracts; all 21 `MODULE_CONTEXT.md`; the 133 invariants + the AMD-01..65 trail), then nine PM spot-checks of the highest-stakes claims. No code touched.
**Scope:** `homesynapse-core` (HEAD `8ef9e9f`) + `homesynapse-core-docs`. Window: M3 (event-bus / projection / composition root) through end of M4 (projection-derivation foundation, device-model breadth incl. Floor/Area/EntityRole, integration-api freeze AMD-54..64). This is **not** the M4 process retrospective (`context/audits/2026-06-05_M4-retrospective.md`) — governance-hygiene debt it already tracks (§7) is cross-referenced here, not re-derived. The value of this document is the **forward lens**.

**Verdict (one paragraph, full text in §7):** The foundation is deep and well-governed *where code has already touched it* — the event/projection/persistence spine, the typed `AttributeValue` pipeline end-to-end, the composition root, and the integration-api freeze are subsystem-grade. It is deep enough to carry the next few Core milestones. But a handful of **load-bearing contracts were frozen or deferred as interface/Javadoc promises**, and the harder modules will try to stand on them: the crypto/secrets/key-management **design is a vacuum** seven docs already lean on (M6); the integration-api freeze locked two thin spots — the **AMD-65 `Expectation` codec** (un-round-trippable, M9+M14 critical path) and the **INV-SE-04 scoped-registry** promise (a security invariant living only in Javadoc); and **identity-by-convention** (`actorRef` as a bare `Ulid`) plus the **string-typed / scalar data spine** are cheap to harden now and expensive to migrate once the immutable event log accrues.

---

## 0. Reading aids — classification and verdict legends

Every finding carries a **classification** and, where relevant, a **state verdict**.

**Classification (the discipline the brief mandates):**

- **(a) Deliberate deferral** — tracked, scoped to a future milestone, fine. Noted and moved past.
- **(b) Genuine miss** — should exist or be specified, doesn't, and nobody is tracking it as such.
- **(c) Thin contract** — *exists* but is under-specified or under-built for the complexity the consuming module will demand. The most valuable and most easily overlooked category.

**State verdict (the investigation's discipline):** **IN CODE** (concrete production type/field) / **SPEC-ONLY** (only in docs) / **FUTURE** (absent).

**Severity:** HIGH (will block or force rework of a near-horizon module) / MEDIUM (will cost real effort or correctness if unaddressed by its consuming milestone) / LOW (hygiene; cheap whenever done).

**Expand call:** **NOW** (foundational AND cheaper-now-than-later — the bar) / **JIT** (just-in-time, at the consuming milestone) / **ACCEPT** (accept-and-track).

**Forward milestone map** (from `context/planning/phase-3-milestone-backlog.md:143-159`): M5 Platform API + test-support · M6 Configuration + secrets/crypto · M7/M8 Automation · M9 Integration Runtime supervisor · M10 REST API · M11 WebSocket API · M12 Observability · M13 Lifecycle (full) · M14 Zigbee · M15 system integration + perf. Long-horizon: multi-user/RBAC, energy events, on-device AI, mesh telemetry, multi-hub/cloud sync, crypto/tamper-evidence. **Dependency note that amplifies everything below: M6 is a dependency of M7, M9, and (transitively) M10 — so a thin M6 fans out further than any other near-horizon milestone.**

---

## 1. What the M3→M4 foundation actually provides (baseline)

A deliberately brief baseline — the snapshot and retrospective cover *what we built*; this section exists only to anchor the forward analysis in what is genuinely solid, so the gaps that follow are read against a real floor, not a strawman.

**Solid and load-bearing (IN CODE, verified at HEAD):**

- **Event spine.** Single-writer `SqliteEventStore` (LTD-03) on one platform thread; gap-tolerant monotonic `global_position`; per-subject sequences; `DegradedEvent` decode fallback so reads never throw; causal context (`correlationId`/`causationId`) propagated and persisted.
- **Event bus.** `InProcessEventBus` pull model (position-carrying notification, subscriber re-reads), per-subscriber virtual thread (INV-SUB-ISO-01), a real COLD→REPLAY→TRANSITION→LIVE FSM, bounded replay window with recoverable overflow, and a live circuit breaker.
- **Projection / derivation (the M4 headline).** `DispatchingProjectionAdvancer` wired (`HomeSynapseCore.java:235`, REC-28, closing OR-M3-18); production `ProductionDerivationRule`; the AMD-45 atomic subscriber+view checkpoint coupling **now wired on the live path** (`HomeSynapseCore.java:288,307`; `atomicCheckpoint=true` so the bus does not double-write) — the pre-M4 "built-but-unwired" finding is resolved.
- **Typed value pipeline, end-to-end.** `AttributeValue` is an 8-variant sealed hierarchy relocated to a `com.homesynapse.value` leaf module (AMD-52 §11), with a typed change-detection comparator (AMD-51), a typed `StateChangedEvent` payload + hand-rolled tagged-union codec (AMD-52), and event-time-deterministic activity timestamps (AMD-53). `projectionVersion` advanced 1→5 with a frozen reconciliation-backfill (AMD-50).
- **Device model breadth.** `Floor` aggregate + minimal `Area` + `EntityRole` 6×3 legality matrix (AMD-44); `Set<HardwareIdentifier>` dedup.
- **Integration-api freeze.** 22→40 types (AMD-54..64): descriptor 8→14, context 10→12, `RequiredService` 3→5, lifecycle permits 5→10, two capability events, `CredentialRotator`, `HealthDetail`. Contract-only; supervisor impl is M9.
- **Composition root + read surface.** `HomeSynapseCore` boots persistence → bus → projection → scheduler → embedded HTTP and serves read/admin endpoints via `MaterializedStateQueryService`; two ArchUnit rules keep REST read-only. The runtime **is launchable** (test-driven), even though `Main.java` is still a stub (see §3, F8).
- **Quality gates that earned their keep.** 9 ArchUnit rules, 10 abstract contract suites, ~1,396 `@Test`, `-Werror`, the freshness preflight, dual-skill mirrors, and AMD-as-truth governance with external DOCS reviews.

That floor is high. Everything below is what the floor does **not** yet carry.

---

## 2. Documentation gaps

Under-specified contracts, missing design depth, and a stale/inconsistent governance trail. Each is mapped to the module that needs the missing detail.

### 2.1 The crypto / key-management design vacuum — seven docs depend on a design that does not exist *(class (b)→(c); HIGH; M6 + crypto horizon)*

INV-PD-07 (crypto-shredding) and at-rest encryption are *referenced* by **seven** design docs — Doc 01 §12 (`01-event-model-and-event-bus.md:1038`), Doc 02 §12, Doc 04 §12 (`04-persistence-layer.md:1044`), Doc 07 §12 (`07-automation-engine.md:973`), Doc 09 §14 (`09-rest-api.md:991`), Doc 10 §12.6 (`10-websocket-api.md:778`), Doc 14 §12.7 (`14-master-architecture-document.md:845`) — each deferring to "the key-management infrastructure established by INV-PD-03/INV-PD-07." **No *numbered design doc* owns that infrastructure.** The only artifact carrying an actual KEK/DEK key hierarchy is a Draft research piece (`research/2026-03-22_Unified_Cryptographic_Architecture_for_HomeSynapse.md`, status Draft) that was **never promoted to a design doc**; Doc 06 owns only a *narrower* single static-key AES-256-GCM secret store (one key in `.secret-key`, §12.1) — not the per-category DEK / crypto-shredding key manager INV-PD-07 requires. So the per-category crypto-shredding key hierarchy is *referenced across seven docs and designed in none of them* (the substantive design exists only as an unpromoted Draft). This is the single highest-leverage documentation gap, and **M6 is the next major milestone**. Threatens: M6, then the tamper-evidence/crypto-shred horizon.

### 2.2 Doc 06 `SecretStore` is stale against the ratified AMD-60 `CredentialRotator` *(class (c) + STALE; HIGH; M6/M9 seam)*

Doc 06 §8.5 (`06-configuration-system.md:637-645`) exposes only `resolve/set/remove/list` over a **flat global key namespace** driven by a `homesynapse secrets` CLI (§3.4:`172`). But AMD-60 (RATIFIED 2026-06-05) froze a `CredentialRotator.rotate(Map<String,String>)` that is **integration-scoped, atomic across entries, and durable-before-return** (Doc 05 §3.8:`306`, §8.2:`738`). Doc 06 has **no awareness of AMD-60** — no `rotate`, no scoping, no atomic multi-key write. The integration-runtime contract now has a rotation method with no home in the configuration system that is supposed to satisfy it. Threatens: M6 (must build the store), M9 (consumes the rotator).

### 2.3 Doc currency lag in Doc 02 — the device-model owner doc is wrong about where its own types live *(class (c) + STALE; MEDIUM; M6/M7/M14)*

Doc 02 §8.2 (`02-device-model-and-capability-system.md:871-875`) still states `AttributeValue` and the `AttributeValueUpcaster` SPI "live in the same package," but M4.0b-4a (`971cfa1`) **moved `AttributeValue` + 8 variants + `AttributeType` to `com.homesynapse.value`** while the upcaster *stayed* in device-model. Doc 03 §4.1 captured the relocation; Doc 02 — the owner — did not. Compounding it, Doc 02 §15 OQ1 (`:1047`) still marks the JSR-385 unit-library choice **[BLOCKING]** and §16 (`:1076`) still lists "JSR 385 units" as the decision, though both were superseded by REC-93 (hand-rolled `String` units, no library). Every M6/M7/M14 consumer that reads Doc 02 to find these types is misdirected. Threatens: M6, M7, M14.

### 2.4 Governance-trail inconsistencies (the brief's explicit list, confirmed/corrected at HEAD)

| Item | Finding at HEAD | Class | Note |
|---|---|---|---|
| **AMD-34 annotation** | The 2026-05-20 gap-closure doc (§5.4) recommended appending a "home_id written-but-not-exposed; deferred to multi-hub" note to AMD-34. **Never added** (`AMD-34_…md` ends at line 86, no annotation). Code state still matches the premise (`SqliteEventStore.java` binds `home_id`; `fromRow` never reads it; no `EventEnvelope.homeId`). | (a) hygiene | LOW. Accept; fold at multi-hub WU. |
| **AMD-37 annotation** | The recommended "activation invariant" (single-writer / partition-local chain construction) annotation was **never added** (`AMD-37_…md` ends at line 92). | (a) hygiene | LOW. |
| **AMD-37 "stale body"** | The pre-M4 investigation's alarm that AMD-37 still describes `setNull(...)` "chain_hash deferred" is **largely a misread.** That `setNull` text appears only in AMD-37's *Problem* (line 14) and *Before* block (line 46); its prescribed resolution (`setBytes(N, ZERO_HASH)`, lines 49-56) **matches shipped code exactly** (`SqliteEventStore.java:116,353`). The real, softer defect: AMD-37 carries no shipped-state stamp. | correction | Honest correction to the prior baseline; not a spec/code divergence. |
| **Mixed event-naming (permanent)** | Confirmed permanent and frozen in **AMD-58-INV-02**: the 5 legacy `integration_*` events stay snake_case (`EventTypes.java:201`), all new events are dot-namespaced (`integration.config.updated` `:218`; `capability.added` `:235`). **Not propagated to Doc 01** (`01-…:471,580` still describe the clean dichotomy), and the event-model `MODULE_CONTEXT` even gives a wrong example (`device.state_changed` — the core event is snake-case `state_changed`). | (a) tracked doc debt + correctness wrinkle | MEDIUM. Already logged in M4 retro §7.2. Consumers M9/M12/M14 must tolerate both; the Doc 01 rule + the MODULE_CONTEXT example fix should land before they do. |
| **Phase-2 traceability stubs** | Per the snapshot's own tracking (`PROJECT_SNAPSHOT.md:145,189`), **12 docs**, not 10, lack a populated traceability index (docs 02-11, 13, 14); only Doc 01 (44 entries) and Doc 12 (2) are populated (the design-doc bodies otherwise terminate at §16). The Phase-3 plan's **DC-2 checkpoint ("at M4 complete," `…Phase3_Master…v2.md:113`) was supposed to fill them and was missed.** | (a) deliberate deferral | MEDIUM. M4 retro §7.5 retargets to per-subsystem population. Until then, forward impact-analysis (which the harder modules lean on) has no index. |
| **PLAN-M4 currency** | The recommended SUPERSEDED marker is **not in v1's own masthead** — `PLAN-M4-CONSOLIDATED.md:7` still self-identifies as live "DRAFT v1." Even v2 ("FINAL-CANDIDATE", last-verified `e73e199`) is itself **stale vs M4 COMPLETE (`8ef9e9f`)** — its §3 tracks only through M4.B-S1, not M4.C. | (a) tracked doc debt | LOW. M4 retro §7.4. Cheap masthead fix. |

### 2.5 Other documentation seams (each (b)/(c), MEDIUM)

- **Doc 01 internal contradiction (`SubscriptionFilter`)** — §3.4 renamed the field to `subjectTypeFilter` (`01-…:189-193`) but the surrounding prose (`:202`) and §8.2 table (`:892`) still say `entity_type_prefix`. M10/M11/M12 build subscriptions on this contract; a renamed-but-not-propagated field is a latent integration defect. *(class (c)/STALE; fix before M11.)*
- **Doc 01 `chain_hash` omission** — §14 (`:1104`) still says hash-chaining "is not implemented… a `log_hash` column *can be added*," and §4.2's schema shows no such column, though AMD-37 already reserved it. *(STALE; crypto horizon.)*
- **Doc 02 ↔ Doc 07 selector seam** — Doc 02 §3.10 (`02-…:433`) says `EntityRole` "drives automation-selector scope" and AMD-44 added `Floor`/`FloorRegistry`, but Doc 07 §3.12 (`07-…:530-538`) — the *owner* of selector vocabulary — has **neither a `floor:` nor an `entity_role:` selector.** Doc 02 promises a behavior Doc 07 does not define. *(class (c)/STALE; M7/M8/M15.)*
- **Historical / time-series state-query ownership** — Doc 03 §8.1 (`03-…:649`) punts filtering to the API layer and §14 (`:882`) leaves "state at time T" as an event-log scan with a *deferred* time-bucket projection; Doc 04 §15 OQ3 doesn't claim it either. **Neither doc owns historical query.** M10/M11 dashboards, M12 observability, and the energy/AI horizons all need indexed/time-series reads. *(class (b) seam miss; assign an owner before M10/M12.)*

---

## 3. Functional gaps

Stubbed / deferred / placeholder / dead code that a future module depends on. State verdicts at HEAD `8ef9e9f`.

| ID | Gap | State @ HEAD (file:line) | Class | Threatens / when | Sev |
|---|---|---|---|---|---|
| **F1** | **`core/automation` is 100% Phase-2 scaffolding** — 9 interface-only services, 5+ empty Tier-2 record stubs (`PresenceTrigger`/`ZoneCondition`/`TimeTrigger`/`SunTrigger`/`WebhookTrigger`/`ActivateSceneAction`/`InvokeIntegrationAction`/`ParallelAction`), **no `src/test`**, plus 16 critical-review impl findings + 10 Tier-2 deferrals (automation `MODULE_CONTEXT:9,146-157,288-341`). | SPEC-ONLY | M7/M8 (the whole engine) — fans out to M10/M11/M12/M13 (consumers: automation `MODULE_CONTEXT:186-191`) | HIGH (sizing) |
| **F2** | **`WithinTolerance.evaluate()` throws** "Implementation deferred to Phase 3" (`WithinTolerance.java:26`) — and the M4.C freeze made `Expectation` (sealed: `ExactMatch`/`WithinTolerance`/`EnumTransition`/`AnyChange`, `Expectation.java:27-28`) part of the persisted `CapabilityInstance`, but **`Expectation` has no codec in `PersistenceJacksonModule`** (only `AttributeValue` is registered, `:95`) → a command-bearing `CapabilityAdded` decodes to `DegradedEvent`. This is **AMD-65** (QUEUED, BLOCKING-for-M9, **no amendment file yet**). | IN CODE (stub) | **M9** (must not publish command-bearing `CapabilityAdded`) **+ M14** (onOff devices are the first command-bearing capabilities); ~late-Jul/Aug | **HIGH** |
| **F3** | **backup/restore unimplemented** — `SqlitePersistenceLifecycle.createBackup()/restoreFromBackup()` throw `UnsupportedOperationException` (`:393,407`), though `PersistenceLifecycle`/`BackupOptions`/`BackupResult` are fully specified. | IN CODE (throws) | M10 (admin-backup endpoints), M13 (pre-upgrade snapshot, LTD-14) | MED |
| **F4** | **Subscriber retry loop is dead code** — `computeBackoff`/`sleepForBackoff`/`MAX_RETRIES` are never invoked; every failure parks `attemptCount=1` (`SubscriberSupervisor.java:84-86,117`). Combined with F10, dead-letters survive only in a 1024-deep in-memory ring. | IN CODE (dead) | M9 (delivery reliability), M12 (DLQ observability), operational durability | MED-HIGH |
| **F5** | **CommandHandler routing chain unimplemented at every hop** — no production `CommandDispatchService`, no `IntegrationSupervisor`, no REST command endpoint consuming `CommandRequest`, and **`DeviceRegistry.getIntegrationForEntity` does not exist** (named only in `CommandDispatchService.java:16` Javadoc). Grep for `implements CommandDispatchService|IntegrationSupervisor|CommandHandler` in `src/main` → zero. | SPEC-ONLY | M7/M8 (action dispatch), M9 (supervisor routing), M10 (command POST) | HIGH |
| **F6** | **Crypto / `SecretStore` greenfield** — `SecretStore` interface, **zero impls**; `chain_hash` bound as a 32-byte `ZERO_HASH` (`SqliteEventStore.java:116,353`); no key manager/store/rotation; crypto-shredding is a category/column boundary only. | SPEC-ONLY / FUTURE | M6 + crypto/tamper-evidence horizon | HIGH |
| **F7** | **INV-SE-04 least-privilege unenforced** — the string `INV-SE-04` appears in **0 code files**; no production scoped `EntityRegistry` (filtering by `integration_id`); the freeze locked the *promise* of scoping in `IntegrationContext`/`CapabilityPublisher`/`CredentialRotator` Javadoc, but the only impls are test stubs. | SPEC-ONLY | **M9** (builds per-adapter scoped contexts against an unenforceable promise) | HIGH |
| **F8** | **`Main.java` shim** — prints "not yet implemented" (`Main.java:20`); does not reference `HomeSynapseCore`. *Honest correction:* the binary entry point is a stub, but the **runtime is launchable** via the `HomeSynapseCore` composition root (test-driven). | IN CODE (stub) | M13 | LOW |
| **F9** | **REST auth unbuilt while live endpoints are exposed** — `AuthMiddleware`/`RateLimiter` interface-only; bcrypt/key-store Phase-3; **INV-SE-02 ("auth mandatory on every request") is currently unmet** on the shipped `/api/v1/entities*` + `/internal/*` endpoints. Idempotency cache is in-memory, lost on restart (rest-api `MODULE_CONTEXT:231-234,315-316`). | SPEC-ONLY | M10 + multi-user/RBAC | MED |
| **F10** | **Persistent DLQ inert + telemetry ring store absent** — bus constructs each DLQ with `PersistentDlqWriter.noop()` (`InProcessEventBus.java:338`); the three-way `writeAtomicCheckpointWithDlqPark()` has **zero production callers**, so dead-letters persist nowhere. The persistence `telemetry/` dir is `.gitkeep`-only; `TelemetryWriter`/`TelemetryQueryService` + the aggregation engine are unbuilt. | IN CODE (inert) / FUTURE | M9 (telemetry routing), M12 (charts + DLQ), durability, energy/mesh horizon | MED |

**Note on F1/F5:** these are correctly deferred to their milestones — the forward value is the *sizing warning* (F1 is a from-scratch engine, not interface-fill-in) and the *small named-but-absent contract* inside F5 (`DeviceRegistry.getIntegrationForEntity`), which is a genuine miss worth fixing cheaply.

---

## 4. Thin-contract risks

Contracts that *exist* but won't carry the weight the consuming module will put on them. These are the brief's five governing questions, answered against HEAD. This is the most important section.

### 4.1 Is the event/payload model rich enough for energy event types and AIoT? — **No, at the event layer.** *(class (c); MEDIUM; energy + AI horizon, M7 triggers)*

The substrate *reserves slots* but the event layer is not first-class for either:

- **Energy:** `EventCategory.ENERGY` (`EventCategory.java:40`), `EntityType.ENERGY_METER` (`EntityType.java:106`), and `EnergyMeter`/`PowerMeter` capabilities exist — but there are **zero energy event types** in `EventTypes.java`; energy rides the generic `telemetry_summary`. INV-EI-01's MVP-scope claim ("the event taxonomy *must include* energy event types and categories") is **materially unmet**, and Doc 14 §14.3's assertion that "INV-EI invariants [are] satisfied by the core's event model" (`14-…:923`) **overstates readiness**.
- **AIoT:** `StateReportedEvent.value`, `CommandIssuedEvent.parameters`, and `StateConfirmedEvent.expectedValue/actualValue` are **serialized-JSON `String`** (event-model `MODULE_CONTEXT:84,234`); typed wrappers are Phase-3. `TelemetryWriter` is **numeric-scalar-only** (`TelemetrySample(…, double value, …)`, Doc 04 §8.3:`763`) — it cannot carry multi-dimensional or structured behavioral telemetry. INV-AI-05 ("MVP *must define* the behavioral data pipeline") is entirely absent. Presence events are Tier-2 with no producer/consumer.

The energy *event family* is cheap to add now; the string→typed payload migration and the scalar-telemetry limitation are real future costs that the "first-class from day one" framing hides.

### 4.2 Is the capability / `AttributeValue` system deep enough for M7 automation + M14 device breadth? — **Partially.** *(class (c) for breadth/validation, (a) for reserved enums; MEDIUM-HIGH; M7/M14/M15)*

Genuinely strong: `AttributeValue` is now typed end-to-end (8 variants, comparator, codec, checkpoint) — excellent for M7 change-detection. But:

- **`EntityType` has only 6 MVP values** (LIGHT/SWITCH/PLUG/SENSOR/BINARY_SENSOR/ENERGY_METER, device-model `MODULE_CONTEXT:265`); THERMOSTAT/LOCK/COVER/CLIMATE/FAN/VALVE/SIREN/MEDIA_PLAYER/CAMERA are **Javadoc-only**. Every non-MVP device class (M14 breadth) requires extending the enum **and its 6×N legality matrix.**
- **Capability standard set is ~16**; lock/thermostat/cover/color/valve/siren/battery_storage/solar_inverter/ev_charger are "reserved, schema-accommodated" only (Doc 02 §3.6:`281`).
- **`SchemaAttributeValidator` is unbuilt** — ARRAY element constraints, QUANTITY unit/min/max, and all min/max/step/validValues/nullable rules are deferred to M15 (device-model `MODULE_CONTEXT:90,305`). The `AttributeSchema` ctor enforces only the AMD-47-INV-04 DEGRADED guard.
- **`WithinTolerance.evaluate()` throws** (F2) — the very confirmation primitive M7 automation relies on.
- **`entity_profile_changed` has no typed Java event record** (taxonomy-only, device-model `MODULE_CONTEXT:308`) — the M7/M8 reclassification path.

The 6-value `EntityType` ceiling and the absent validator are foundational: they are "reserved but empty" contracts a harder module is forced to fill, and the matrix-extension discipline should be settled before M14.

### 4.3 Is the just-frozen integration-api sufficient for the M9 supervisor + the multi-protocol future, or did we freeze something too thin? — **Mostly sufficient; two genuinely thin spots.** *(class (c); HIGH for AMD-65, MEDIUM otherwise; M9 + multi-protocol horizon)*

The hypothesis that the freeze is "too thin" is **mostly not borne out** — descriptor 8→14, context 10→12, `RequiredService` 3→5, the four lifecycle hooks, `CredentialRotator`, and `HealthDetail` (12 values, each mapping 1:1 to a supervisor FSM transition) are a well-shaped M9 surface, and Doc 05 is the best-maintained doc in the corpus (the only one with a populated traceability index, `05-…:1069`). But three real thin spots:

1. **The AMD-65 `Expectation` codec (F2)** — *this* is the "frozen too thin" instance: the freeze locked a `CapabilityInstance` that cannot round-trip through persistence. M9+M14 critical path. HIGH.
2. **`IoType` is binary** (SERIAL/NETWORK, Doc 05 §8.2:`722`) — the enum that "drives thread allocation" is coarse for a multi-protocol future (BLE/Z-Wave/Matter/Thread/MQTT/USB-HID). Append-only, so cheap to extend, but unacknowledged.
3. **`IsolationLevel` reserves a name, not a design** — `{IN_JVM, RESERVED_SUBPROCESS}` with the supervisor *rejecting* `RESERVED_SUBPROCESS` (AMD-63, Doc 05 §8.2:`735`), while §6.8 documents JNI segfaults that take down the whole JVM — exactly the failure mode a flaky multi-protocol native stack will hit. Out-of-process isolation is the eventual answer and it is undesigned.

Plus the cross-cutting **INV-SE-04 scoping (F7)** and the **`CredentialRotator`↔Doc 06 mismatch (§2.2)** both pierce this contract.

### 4.4 Is identity-by-convention (`actorRef` as bare `Ulid`) enough before multi-user? — **No — it is a deliberate seam that needs a model, and the seam itself is unflagged.** *(class (c); MEDIUM; multi-user/RBAC horizon + M10)*

`actorRef` is a bare nullable `Ulid` on `EventEnvelope` (`:112`), polymorphic by convention (PersonId/AutomationId/SystemId "resolved from context"). The typed wrappers exist but `actorRef` is not typed to them; there is no Person/User entity, no role, no RBAC; REST auth is `ApiKeyIdentity` (a *client*, not a person, rest-api `MODULE_CONTEXT:315`); and automations carry **no actor identity** for the commands they issue. The multi-user *feature* is flagged deferred (Doc 14 §2.2:`67`), but the specific **envelope seam — what `actorRef` points at, and how Tier-1 API keys map onto it — is called out nowhere.** And this field is not merely reserved — `actorRef` already **round-trips through persistence** (written `SqliteEventStore.java:330`, hydrated `:672`), so every event already carries it. Because the event log is append-only and immutable, deciding `actorRef` semantics is *much* cheaper now than after a large corpus accrues and a schema migration is required. INV-MU-01 is the audit-trail foundation and it currently rests on an untyped, unmodeled — but live — field.

### 4.5 Is `Area` deep enough now that `Floor` exists? — **Partially — `Area` is still shallow; `Floor` is deeper; registries are unimplemented.** *(class (c) + (a); MEDIUM; M7/M8 selectors, M10 endpoints, spatial horizon)*

`Area = (AreaId id, String name, FloorId floorId, Instant createdAt)` (`Area.java:34-37`) — M4 gave it a name and a floor link (an improvement on the pre-M4 bare ULID), but **no coordinates, no geometry, no sub-area hierarchy**; its Javadoc defers "full area lifecycle to AMD-45." `Floor` is richer — `(FloorId, name, int level, icon, List<String> aliases, createdAt)` (`Floor.java:40-47`). But: `AreaRegistry`/`FloorRegistry` are **interface-only, no production impl** (AreaRegistry write-CRUD deferred to AMD-45), and **`FloorId` is not yet registered in `PersistenceJacksonModule`** (platform-api `MODULE_CONTEXT:128`) so floor persistence/REST is blocked. Presence triggers (`PresenceTrigger`/`ZoneCondition`) remain empty Tier-2 records — no zone model. The `FloorId` Jackson registration is a tiny now-fix; the Area/Floor depth decision should precede M7 selectors and M10 endpoints building on it.

---

## 5. Forward-looking foundation readiness (long-horizon invariants)

State verdicts at HEAD `8ef9e9f`, with an expand-now-vs-later call. (Invariant line numbers: `governance/Architecture_Invariants_v1.md`.)

| Horizon invariant family | What it promises | Verdict @ HEAD | Strongest in-code evidence | Biggest gap (promise vs code) | Expand call |
|---|---|---|---|---|---|
| **Multi-user identity + RBAC** (INV-MU-01..05, L682-724) | per-user context; presence as a core primitive; preference arbitration; household roles enforced across interfaces; graceful identity degradation | **substrate IN-CODE; model SPEC-ONLY** | `actorRef` *round-trips* (written `SqliteEventStore.java:330`, hydrated `:672` — more live than write-only `home_id` below); `PersonId`/`AutomationId`/`SystemId` wrappers (Jackson-registered); `SubjectType.PERSON`; `EventCategory.PRESENCE` | no Person/User entity, no role, no RBAC, no arbitration; `actorRef` is untyped (`Ulid`); REST = API key | **LATER** for the model — but **decide `actorRef` semantics NOW** (cheap; the field already accrues in the immutable log) |
| **Energy as first-class event domain** (INV-EI-01..05, L634-668) | energy event types + energy entity types; OpenADR/grid-interactive; carbon-aware; data sovereignty | **SPEC-ONLY** (slot reserved) | `EventCategory.ENERGY`; `EntityType.ENERGY_METER`; `EnergyMeter`/`PowerMeter` | **zero energy event types**; 1 of 5 named entity types; INV-EI-01 MVP claim unmet; Doc 14 "satisfied" overstated | **LATER** for full; **add the energy event family + correct the Doc 14 claim** opportunistically |
| **On-device AI pipeline** (INV-AI-01..05, L596-616) | local inference (LightGBM/TinyLSTM/ONNX); behavior modeling; explainable/consent-gated; AI never foundation | **FUTURE** (nothing) | none (no module, no dep, no code) | INV-AI-05 "MVP *must define* the behavioral data pipeline" entirely absent | **LATER** — but let INV-AI-05's pipeline definition ride the telemetry/energy data-schema design |
| **Network / mesh telemetry** (INV-MN-01..04, L738-762) | protocol-agnostic normalized telemetry (RSSI/LQI/route/neighbor); mesh health first-class; predictive; battery-aware | **SPEC-ONLY** | `DeviceHealth` (`rssi_dbm`,`lqi`); Zigbee `RouteHealth`/`NeighborTableEntry`; `EventCategory.DEVICE_HEALTH` | no generic `NetworkHealth`/`NetworkTelemetry` type/event; mesh telemetry Zigbee-package-local; nothing emits; INV-MN-01 MVP "Zigbee must emit" unmet | **LATER (M14)** — but **define the generic normalized-telemetry event shape before M14** wires it Zigbee-only |
| **Multi-hub / cloud sync** (INV-LF-05 L137-147, LF-02 L111) | convergent (CRDT-style) delta sync; no central coordinator; cloud enhancement not dependence | **substrate IN-CODE; sync SPEC-ONLY** | per-entity ULID sequences; checkpoint recovery; `home_id` written every INSERT (AMD-34) | `home_id` write-only (never read; no `EventEnvelope.homeId`); no sync protocol/CRDT/coordination | **LATER** (post-MVP) — substrate adequate; accept-and-track |
| **Privacy / crypto / tamper-evidence / crypto-shredding** (INV-PD-03/07/08 L387-445, INV-SE-03/04/05 L572-580) | encrypted storage (user keys); per-scope keys + crypto-shred ≥1 category at MVP; tamper-evident hash chain; least privilege | **FUTURE / interface-only** | `chain_hash` column (inert `ZERO_HASH`); `SecretStore` interface; `EventCategory` shred boundaries; `AuthMiddleware` interface | no encryption-at-rest, no per-scope keys, no crypto-shred, no active chain, no signing; **INV-PD-07 MVP mandate unmet**; INV-SE-04 absent from code | **NOW** (the *design owner doc*) — M6 is next and 7 docs depend on it |

**Pattern across the table:** the architecture has done its constitutional job of *reserving slots* (categories, entity types, typed ID wrappers, schema columns, event vocabulary) so these families can land without redesign — genuinely good forward hygiene. But **three invariants assert MVP-scoped obligations that are currently unmet**: INV-AI-05 (behavioral pipeline), INV-EI-01 (energy event types), INV-PD-07 (crypto-shredding for ≥1 category). Those three are where "the invariant says MVP, the code says not yet."

---

## 6. Prioritized recommendations

Per finding: severity, the module it threatens, and **expand-now / expand-JIT / accept-and-track**. The bar for **expand-now** is *foundational AND cheaper-now-than-later*.

### 6.1 Expand NOW (foundational + cheaper now than later)

| # | Action | Finding | Threatens | Why now |
|---|---|---|---|---|
| 1 | **Author AMD-65 + the `Expectation` persisted codec** (4 permits; `WithinTolerance(double,double)` gets the AMD-52 bit-anchored-float treatment). | F2 / §4.3 | **M9 + M14** | Already in the pre-M9 queue; the `@Disabled` acceptance test exists; the freeze locked an un-round-trippable contract on the critical path. Cheapest possible now. |
| 2 | **Promote the 2026-03-22 crypto Draft into a numbered, owned design doc** — the KEK/DEK hierarchy, per-category DEK, and at-rest encryption that 7 docs point at. Don't redesign from scratch: the Draft research artifact already holds the substance; supersede it into an owned doc and reconcile it with Doc 06. | §2.1 / F6 | **M6** + crypto horizon | M6 is the next major; building `SecretStore` against an unpromoted Draft guarantees rework. |
| 3 | **Reconcile Doc 06 `SecretStore` with the ratified AMD-60 `CredentialRotator`** (add scoped, atomic, durable rotation to the owning doc). | §2.2 | M6 / M9 | A ratified contract with no home in its owner doc; reconcile before M6 implements the store. |
| 4 | **Decide `actorRef` identity semantics** — what it points at; how Tier-1 API keys map onto it. | §4.4 | multi-user horizon + M10 | Immutable event log; specifying now avoids a later schema migration over an accrued corpus. |
| 5 | **Specify the INV-SE-04 integration-scoped `EntityRegistry` mechanism** before M9 builds per-adapter contexts. | F7 / §4.3 | **M9** | A security invariant currently living only as Javadoc; M9 will otherwise build against an unenforceable promise. |
| 6 | **Fix Doc 02 currency** (AttributeValue relocation; JSR-385→REC-93). | §2.3 | M6/M7/M14 | Cheap; the owner doc misdirects every consumer to the wrong package. |

### 6.2 Expand JUST-IN-TIME (at the consuming milestone, but flag the discipline now)

| Action | Finding | At milestone |
|---|---|---|
| `EntityType` enum + 6×N legality matrix extension; build `SchemaAttributeValidator`. | §4.2 | M14 (breadth) / M15 (validator) |
| Implement backup/restore (interface "looks done" but throws). | F3 | M10 / M13 |
| Wire the subscriber retry loop + persistent DLQ (durable dead-lettering). | F4 / F10 | M9 / M12 |
| Build the telemetry ring store + aggregation engine. | F10 | M9 / M12 (+ energy/mesh) |
| Fix Doc 01 `SubscriptionFilter` field-name + `chain_hash` currency. | §2.5 | before M11 |
| Add `floor:` / `entity_role:` selectors (Doc 02↔07 seam). | §2.5 | M7 |
| Assign an owner for historical / time-series state queries. | §2.5 | before M10/M12 |
| Add the energy event-type family + correct the Doc 14 "INV-EI satisfied" claim. | §4.1 / §5 | energy work / opportunistic |
| Define a generic normalized network-telemetry event shape. | §5 (MN) | before M14 |
| Build REST auth + persistent idempotency; note INV-SE-02 currently unmet on live endpoints. | F9 | M10 |
| Register `FloorId` in `PersistenceJacksonModule` (tiny unblock for floor persistence/REST). | §4.5 | M10 (or now — trivial) |

### 6.3 Accept and track (deliberate deferrals, correctly tracked)

`core/automation` scaffolding (F1 — accept; heed the *sizing* warning) · the CommandHandler chain (F5 — accept; fix the small `DeviceRegistry.getIntegrationForEntity` named-but-absent contract) · `Main.java` shim (F8 — accept; runtime is launchable) · the governance-hygiene items already in **M4 retro §7** (mixed event-naming, traceability stubs, PLAN-M4 currency, AMD-34/37 annotations) · multi-hub sync (substrate adequate) · on-device AI (horizon — but let INV-AI-05's pipeline definition ride the telemetry/energy schema design).

### 6.4 The handful that, left thin, will most hurt the harder modules

1. **AMD-65 `Expectation` codec** — frozen-too-thin contract on the M9+M14 critical path.
2. **The crypto/secrets/key-management design vacuum** (§2.1/§2.2/F6) — M6 is next and seven docs lean on a design that does not exist.
3. **INV-SE-04 scoped registry** (F7) — a security invariant frozen as Javadoc, due at M9.
4. **`actorRef` identity semantics** (§4.4) — cheap now, expensive after the immutable log accrues.
5. **The string-typed payload + scalar telemetry + missing energy event types** (§4.1) — the typed-data spine M7 triggers, energy, and AI will all need; *accommodated, not built*, and the "first-class" claims overstate it.

---

## 7. Closing verdict

**Is the M3→M4 foundation deep enough to carry what's coming?** For the next few Core milestones, yes — and that is not a small thing. Where code has actually touched the foundation, it is subsystem-grade: the single-writer event spine, the pull-model bus with a real subscriber FSM, the now-wired atomic checkpoint coupling, the typed `AttributeValue` pipeline end-to-end, the composition root, and a largely well-shaped integration-api freeze. The governance machinery (STOP-gates, AMDs-as-truth, the freshness preflight, dual-skill mirrors, external DOCS reviews) is real and has caught real defects. The architecture has also done its constitutional job of *reserving slots* for the long-horizon invariants so they can land without redesign.

But there are **specific places to reinforce before we build on top of them**, and they cluster, not scatter. The crypto/secrets/key-management story is a genuine design gap — its substance lives only in an unpromoted 2026-03-22 Draft research artifact, no numbered design doc owns it, and **M6 — the very next major milestone — will hit it on day one** while seven design docs already lean on it. The integration-api freeze, though mostly sound, locked two thin spots that will bite at M9 and M14: the **AMD-65 `Expectation` codec** (a contract that cannot round-trip) and the **INV-SE-04 scoped-registry** promise (a security invariant that exists only as Javadoc). And the cheap-now-expensive-later seams — **identity-by-convention (`actorRef` as a bare `Ulid`)** and the **string-typed/scalar data spine** that the energy, AI, and automation horizons all depend on — should be hardened while the immutable event log is still small. None of these are emergencies; the foundation is not shallow. The honest risk is narrower and more actionable than that: **a handful of load-bearing contracts were frozen or deferred as interface and Javadoc promises, and the harder modules will try to stand on them.** The six "expand-now" items in §6.1 are precisely the reinforcements that are foundational *and* cheaper now than after the dependent modules arrive — and AMD-65, the crypto design owner doc, and the INV-SE-04 mechanism are the three that most directly de-risk M6 and M9.

*End of assessment.*
