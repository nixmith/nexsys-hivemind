<!--
file: context/instructions/2026-06-19_AB-3_lifecycle-reconciliation_coding-instruction.md
purpose: The AB-3 coding instruction — app-bootstrap lifecycle reconciliation. The runnability-unlock substrate: main() wires a coherent, phase-ordered HomeSynapseCore, and it lands the three composition-root wiring items M7.1 deferred. Issues FIRST (before AB-1+AB-2+AB-4, the Seam-1 go-live).
audience: Coder (nexsys-coder, Cowork/Claude Code)
state-type: coding instruction (Phase-3 implementation)
status: ISSUED 2026-06-19 — entry-gate clean (A1–A4 ruled; M7.1 deferred build gate RESOLVED GREEN at beb4bc3; the two AB-3 escalations RULED by Nick this session — see Pinned Decisions). No decision gate, no deferred gate open.
baseline: core beb4bc3 (M7.1 GREEN, ./gradlew check 149 tasks) / docs 32afb3f (Doc 12 + Doc 15 LOCKED; Doc 16 DRAFT) / hivemind 88af41e. Watermark AMD-93 (invariants 163/47). RE-VERIFY at issue via the STOP-on-Mismatch gates.
escalations-ruled: (1) lifecycle API-shape (#4b) = HomeSynapseCore IMPLEMENTS SystemLifecycleManager (implement, do NOT delete the Locked interface). (2) registry-home = core:device-model (production InMemory* impls alongside the interfaces).
-->

# Coding Task: AB-3 — App-Bootstrap Lifecycle Reconciliation (runnability substrate)

**Subsystem:** Lifecycle (`com.homesynapse.lifecycle`) + composition root (`com.homesynapse.app`), touching device-model, configuration, automation.
**Design Doc:** Doc 12 — Startup, Lifecycle & Shutdown (**Locked**); Doc 15 §3.8 (**Locked**, phase-gating reference only); Doc 02 §8.1 (**Locked**, the registry interfaces). Confirm all three are Locked in `PROJECT_SNAPSHOT.md`'s Design Documents table before starting.
**Phase:** 3-Implementation
**Task Brief Reference:** App-Bootstrap Charter §2 (AB-3); 2026-06-18 decision record Addendum (M7.1 composition-root wiring deferral, inbound deps a/b/c); 2026-06-19 M7-forward plan R1.

---

## What This Implements

The core was reviewed (2026-06-15) as **sound where built but not yet runnable — `main()` is a one-line stub**, so the engine never boots, the automation subscriber is never wired, and the lifecycle abstractions sit disjoint. AB-3 is the **runnability substrate**: it reconciles the two lifecycle abstractions into one coherent, phase-ordered composition root, adopts a concrete startup phase model, and **lands the three composition-root wiring items M7.1 deferred** (the `automation_engine` subscriber, the config-load + schema-registration glue, and the lifecycle wiring test). After AB-3, the system **boots and runs the automation engine in phase order under a live health loop + systemd watchdog** — but does NOT yet expose HTTP or activate the at-rest cipher (those are the AB-1 + AB-2 + AB-4 "Seam-1" go-live event, which wire into the phase gates AB-3 establishes).

This is the highest-density latent-defect milestone in the project: several one-way and correctness-critical concerns converge at the instant `main()` wires the system. Read the Watch-Out section in full before writing code.

---

## Pinned Decisions (Nick, 2026-06-19) — implement exactly; these are NOT open questions

- **PD-1 — Lifecycle API shape (charter §7 / escalation #4b): `HomeSynapseCore` IMPLEMENTS `SystemLifecycleManager`.** `main()` constructs `HomeSynapseCore` and holds it **as a `SystemLifecycleManager`**: `SystemLifecycleManager mgr = HomeSynapseCore.create(...); mgr.start();` plus a JVM shutdown hook calling `mgr.shutdown(reason)`. HSC becomes the concrete orchestrator the Doc 12 contract describes — re-homing Doc 12's phase model (the `LifecyclePhase` ladder + `currentPhase()` / `healthSnapshot()` / `subsystemStates()`), the §3.10 health loop, and the §3.9 shutdown sequence into HSC.
  - **⛔ PD-1 GOVERNANCE GUARD (binding):** `SystemLifecycleManager` is a **Doc-12-LOCKED contract** (Doc 12 §2.1 "This Subsystem Owns: the SystemLifecycleManager — the top-level orchestrator…", §8.4 the interface signature; also referenced in Doc 14 + the M3.6 Composition Root Design). **IMPLEMENT the interface; do NOT delete, rename, or otherwise supersede it.** A code-level deletion/replacement of the interface would silently supersede a Locked design contract — that is forbidden. If, during implementation, you conclude the interface genuinely should be retired rather than implemented, **STOP and escalate to the PM** (it is a Doc 12 amendment via the re-open → review → ratify pipeline, the same discipline as AMD-94) — never fold it into AB-3 as a silent delete.
- **PD-2 — Registry home (escalation): the three minimal registry impls live in `core:device-model`,** as production `InMemory*Registry` classes alongside their interfaces (the `InMemoryAutomationIdentityStore` precedent; production impls live in their owning module, as `InProcessEventBus` does in event-bus and the SQLite stores do in persistence). **Mark each impl clearly as the minimal MVP substrate** (start-empty; CRUD + the small query set only; no AMD-44 derivation, no Floor/EntityRole breadth) so they are not mistaken for the future integration-backed registries. The composition root only instantiates them.

---

## Files to Read Before Starting

Read every MODULE_CONTEXT.md **and** every `module-info.java` below before writing any code. MODULE_CONTEXT.md gives the type inventory + cross-module contracts + gotchas; `module-info.java` gives the authoritative JPMS module name + `requires`/`exports` graph (the Research-6 lesson: type names without module names produced fabricated module identifiers).

| File | Why |
|---|---|
| `lifecycle/lifecycle/MODULE_CONTEXT.md` | Target module. HomeSynapseCore (16-step `start()`, platform-thread requirement LTD-19), the projection subscriber wiring pattern (Gotcha 9 / AMD-45), `mode()` reading the bus FSM, the FATAL-subsystem set (Doc 12 §4). |
| `lifecycle/lifecycle/src/main/java/module-info.java` | **Changes in AB-3** (adds `requires`). Embedded verbatim + proposed diff below. JPMS name `com.homesynapse.lifecycle`. |
| `core/automation/MODULE_CONTEXT.md` | The headline gotcha: composition-root wiring of `automation_engine` is BLOCKED on app-bootstrap (this WU). FIX-07: `core:automation → config` banned at EVERY scope; schema-register + load ride the composition root. Three independent subscribers; AB-3 wires only `automation_engine`. C1-interim no-publish. |
| `core/automation/src/main/java/module-info.java` | JPMS name `com.homesynapse.automation`; the FIX-07 comment block records why `requires config` is NOT present. Embedded verbatim below. |
| `core/device-model/MODULE_CONTEXT.md` | The registries are interface-only Stage-1 (this WU adds the InMemory impls per PD-2). `AreaRegistry` is read-only; `Area` keys on display name; `EntityRegistry` must be populated before StateProjection processes device-subject events (the catch-up linkage). |
| `core/device-model/src/main/java/module-info.java` | JPMS name `com.homesynapse.device`; already `exports com.homesynapse.device` (no module-info change needed — the InMemory impls live in the already-exported package). Embedded verbatim below. |
| `config/configuration/MODULE_CONTEXT.md` | `ConfigurationService.load()` is the FIRST subsystem init step; `getCurrentModel().rawMap()` returns `Map<String,Object>`; `SchemaRegistry.registerCoreSchema(String,String)`; the declared `(major,minor)` pair is wired TWICE (registry + service) and must match; `SecretStore.create` / `ScopeKeyManager.create` are the public gateways. |
| `config/configuration/src/main/java/module-info.java` | JPMS name `com.homesynapse.config`; `exports com.homesynapse.config`. The new public factory (this WU) lives in this exported package — no module-info change. Embedded verbatim below. |
| `core/event-bus/MODULE_CONTEXT.md` | `subscribeRuntime(SubscriberInfo, Subscriber)` is the subscribe seam; subscriber starts COLD → REPLAY → TRANSITION → LIVE; **the bus drives `subscriber.setMode()` after each CAS** (composition-root wiring does NOT call setMode). `SubscriptionFilter.all()`. `InProcessEventBus` is the production impl. |
| `core/state-store/MODULE_CONTEXT.md` | `StateProjection` (the catch-up subscriber); `StateStoreLifecycle.start()` returns the **gating future** Doc 12 uses to block dependent subsystems; `ReadinessSource.mode()`; "automations should not fire during replay." The subscribe-after-catch-up lever. |
| `core/automation/src/test/java/com/homesynapse/automation/AutomationTestSupport.java` | `StubEntityRegistry` (line 189), `StubAreaRegistry` (244), `StubDeviceRegistry` (273) — **the behavioral shape to productionize** into the device-model InMemory impls. |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/SystemLifecycleManager.java` | The Locked interface HSC implements (PD-1). Embedded verbatim below. |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | The 16-step `start()` you reconcile into the phase model; current constructors; `stop()`. |
| `homesynapse-core-docs/design/12-*.md` | §3.2–§3.8 (Phases 0–6), §3.5 Step 3.2 (REPLAY/LIVE + subscribe ordering), §3.9 (shutdown), §3.10 (health loop), §8.4/§8.5 (the interface + LifecyclePhase/SubsystemState/SystemHealthSnapshot types). |
| `coder-lessons.md` (2026-06-19 entries) | The FIX-07 superseding lesson (`assertAllowedModuleDependencies` bans a forbidden LAYER edge at any scope; the §authoring exported-API check is necessary-not-sufficient). |

**Minimum read set (floor):** `SystemLifecycleManager.java`, the `start()`/`stop()` regions of `HomeSynapseCore.java`, the three registry interfaces (`EntityRegistry`/`DeviceRegistry`/`AreaRegistry`), `AutomationSchema.java`, `AutomationDefinitionLoader.java`, `AutomationEngineSubscriber.java`, and Doc 12 §3.2–§3.10.

---

## STOP-on-Mismatch Gates

Before writing any code, read each file and confirm it matches. **If any diverges, STOP and report — do not proceed on stale assumptions.** (Baseline `beb4bc3`; the prior session source-verified all of these — re-confirm at the issue HEAD.)

| File | Expected State | What to Check |
|---|---|---|
| `lifecycle/.../SystemLifecycleManager.java` | `public interface` with `void start() throws Exception`, `void shutdown(String reason) throws Exception`, `LifecyclePhase currentPhase()`, `SystemHealthSnapshot healthSnapshot()`, `Map<String,SubsystemState> subsystemStates()`; **NO implementing class repo-wide** (`grep -rl "implements SystemLifecycleManager"` → empty) | Interface intact, unimplemented. This is what HSC will implement (PD-1). |
| `lifecycle/.../HomeSynapseCore.java` | `public final class HomeSynapseCore implements ReadinessSource`; constructors `(Path,HomeSynapseConfig,Clock,HomeId)` + `(…,PayloadCipher)`; **`start()` returns `CompletableFuture<Void>`** (the 16-step bootstrap); `stop()` reverse-order | The signature gap: SLM's `start()` is `void … throws Exception` (synchronous/blocking) vs HSC's `CompletableFuture<Void>`. PD-1 requires reconciling these (see Watch-Out). |
| `core/device-model/.../EntityRegistry.java` | interface, **9 methods**: getEntity, findEntity, listAllEntities, listEntitiesByDevice, createEntity, updateEntity, removeEntity, enableEntity, disableEntity | Method count + signatures unchanged (you implement these). |
| `core/device-model/.../DeviceRegistry.java` | interface, **7 methods**: getDevice, findDevice, listAllDevices, createDevice, updateDevice, removeDevice, findByHardwareIdentifier | Count + signatures unchanged. |
| `core/device-model/.../AreaRegistry.java` | interface, **4 methods**, READ-ONLY (no CRUD): get, getAll, getByFloor, getUnassigned | Count + signatures; confirm read-only (Stage-1, write deferred to AMD-45). |
| `core/automation/.../AutomationSchema.java` | `public static final String SCHEMA_SECTION = "automation";` + `public static final String SCHEMA_JSON = """…""";` | The two constants exist (this is the config-free holder FIX-07 created). |
| `core/automation/.../AutomationEngineSubscriber.java` | **package-private** `final class … implements Subscriber`; ctor `(StandardTriggerEvaluator)`; methods `onEvent`, `setMode`, `onCaughtUp`; **`AutomationConfigBridge` is ABSENT** | Confirm visibility + that no public factory exists yet (you add one — see §Technical Spec). |
| `core/automation/.../AutomationDefinitionLoader.java` | `public final class`; ctor `(AutomationIdentityStore, EntityRegistry, AreaRegistry)`; `public LoadResult load(Map<String,Object> document)` | Confirm the `load(Map)` form + the ctor's registry needs (Entity + Area only). |
| `config/.../ConfigurationService.java` + `ConfigModel.java` + `SchemaRegistry.java` | `ConfigurationService.getCurrentModel()` → `ConfigModel`; `ConfigModel.rawMap()` → `Map<String,Object>`; `SchemaRegistry.registerCoreSchema(String,String)`; **`StandardConfigurationService` + `StandardSchemaRegistry` are package-private with NO public factory** | Confirm there is no existing public way to construct a `ConfigurationService` (you add one — see §Technical Spec). |
| `core/automation/.../Standard{AutomationRegistry,SelectorResolver,TriggerEvaluator,ConditionEvaluator}.java` | `StandardAutomationRegistry()` no-arg; `StandardSelectorResolver(EntityRegistry,AreaRegistry,DeviceRegistry)`; `StandardTriggerEvaluator(StandardAutomationRegistry,SelectorResolver,StateQueryService,EventPublisher,Clock[,int])`; `StandardConditionEvaluator(SelectorResolver,Clock)` | **No constructor references FloorRegistry or CapabilityRegistry.** Confirm — this is the contained-fold guarantee (PD-2). |
| `build.gradle.kts` (root) `moduleGraphAssert.allowed` | `:lifecycle:.* -> :config:.*` PRESENT (line ~56); `:core:.* -> :core:.*` / `-> :platform:platform-api` ONLY (no `:core:.* -> :config:.*`) | Confirms lifecycle→config is allowed; core→config is banned (FIX-07). |

---

## Files to Create or Modify

(The Files table governs: where prose and this table disagree on what is touched, the table wins — flag the conflict as `[INFO]`.)

| Action | File Path | Description |
|---|---|---|
| CREATE | `core/device-model/src/main/java/com/homesynapse/device/InMemoryEntityRegistry.java` | Production minimal `EntityRegistry` impl — Map-backed, start-empty, `ReentrantLock` (LTD-11). MVP-substrate Javadoc (PD-2). |
| CREATE | `core/device-model/src/main/java/com/homesynapse/device/InMemoryDeviceRegistry.java` | Production minimal `DeviceRegistry` impl — same shape. |
| CREATE | `core/device-model/src/main/java/com/homesynapse/device/InMemoryAreaRegistry.java` | Production minimal read-only `AreaRegistry` impl — start-empty Map; `getByFloor` filters on `Area.floorId`, `getUnassigned` filters null floorId. |
| CREATE | `core/device-model/src/test/java/com/homesynapse/device/InMemory{Entity,Device,Area}RegistryTest.java` | Unit tests for each impl (CRUD round-trip + the query set + concurrent-read; Clock not needed if no time used). |
| CREATE | `config/configuration/src/main/java/com/homesynapse/config/ConfigurationServiceFactory.java` (or a `static create(...)` on an existing public type — Coder's call) | **Public assembly entry-point** for `ConfigurationService` (none exists today). Wires the package-private `StandardConfigurationService` with a `StandardSchemaRegistry` using the **same** `(major,minor)` pair, the resolving `SecretStore` (via `SecretStore.create` + `ScopeKeyManager.create`), `System::getenv`, the injected `Clock`/`SystemId`/`EventPublisher`/`configDir Path`. Returns the `SchemaRegistry` too (the composition root needs it to call `registerCoreSchema`). |
| CREATE | `config/configuration/src/test/java/com/homesynapse/config/ConfigurationServiceFactoryTest.java` | Factory builds a loadable service against a temp config dir; `(major,minor)` mismatch is impossible by construction. |
| CREATE | `core/automation/src/main/java/com/homesynapse/automation/AutomationEngineAssembly.java` (name Coder's call) | **Public assembly seam** returning the `automation_engine` `Subscriber` given the evaluator chain (keeps `AutomationEngineSubscriber` package-private). May also expose a convenience that builds the full chain (registry → resolver → evaluators → subscriber) from injected registries + `StateQueryService` + `EventPublisher` + `Clock`. See Watch-Out for the promote-vs-factory note. |
| CREATE | `core/automation/src/test/java/.../AutomationEngineAssemblyTest.java` | The assembly returns a working `Subscriber`; REPLAY/LIVE handling intact. |
| MODIFY | `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | HSC **implements `SystemLifecycleManager`** (PD-1): adopt the `LifecyclePhase` ladder + openHAB startlevels; implement `currentPhase()` / `healthSnapshot()` / `subsystemStates()`; reconcile `start()` (see Watch-Out); map the 16-step bootstrap onto the phase model; wire the §3.10 health loop + systemd watchdog + `SystemdHealthReporter`; add the pre-migration snapshot/rollback hook; assemble `ConfigurationService` + the three registries; **register the automation schema + load definitions + subscribe `automation_engine` after state-store catch-up**; gate HTTP-exposure + cipher-activation phases CLOSED (see Boundary). |
| MODIFY | `lifecycle/lifecycle/src/main/java/module-info.java` | Add `requires` for config/device/automation as needed by the chosen assembly placement (all gate-allowed; all plain/non-transitive — see the two-gate check). |
| MODIFY | `lifecycle/lifecycle/build.gradle.kts` | Add `implementation(project(":core:device-model"))` and `implementation(project(":core:automation"))` to lockstep with the new plain `requires`. **`implementation(project(":config:configuration"))` is ALREADY present** — no change for config. |
| MODIFY | `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` | Replace the one-line stub: construct `HomeSynapseCore` (held as `SystemLifecycleManager`), call `start()`, register the SIGTERM shutdown hook → `shutdown(reason)`. (app already `requires` everything — no module-info/Gradle change.) |
| CREATE | `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/LifecycleWiringTest.java` | **The mandated M7.1 lifecycle wiring test** (deferred dep (c)) — see Test Requirements. |
| MODIFY | `lifecycle/lifecycle/MODULE_CONTEXT.md`, `core/device-model/MODULE_CONTEXT.md`, `core/automation/MODULE_CONTEXT.md`, `config/configuration/MODULE_CONTEXT.md` | Update inventories/contracts/gotchas (HSC-implements-SLM; the InMemory registries; the config factory; the automation assembly seam; the resolved wiring). |

---

## Technical Specification

### 1. Lifecycle reconciliation + the phase model (C9)

**1a. HSC implements `SystemLifecycleManager` (PD-1).** `HomeSynapseCore` adds `implements … SystemLifecycleManager`. `main()` holds it as the interface. Provide a `public static HomeSynapseCore create(...)` (or keep public constructors and have `main()` upcast) such that `SystemLifecycleManager mgr = HomeSynapseCore.create(...); mgr.start();` compiles. Implement all five interface methods against the live phase model. **Do not delete the interface (⛔ PD-1 guard).**

**1b. Adopt openHAB's numbered startlevel ladder as the concrete phase model** (R-δ AX-2), mapped onto Doc 12's Phases 0–6. The authoritative openHAB levels are **00 / 10 / 20 / 30 / 40 / 50 / 70** (seven levels — there is NO 80 or 100):

| openHAB level | meaning | Doc 12 home |
|---|---|---|
| 00 | framework started | Phase 0 BOOTSTRAP (§3.2) |
| 10 | bundles activated | Phase 1 FOUNDATION (config) + Phase 2 DATA_INFRASTRUCTURE (§3.3–3.4) |
| 20 | model entities loaded | Phase 3 Step 3.1 (device/entity registries) |
| 30 | item states restored | Phase 3 Step 3.2 (State Store REPLAY→LIVE) |
| 40 | rules loaded | Phase 3 Step 3.4a (load automation definitions) |
| 50 | rule engine active | Phase 3 Step 3.4b (`automation_engine` subscribed + LIVE) |
| 70 | UI up | Phase 5 EXTERNAL_INTERFACES (**gated CLOSED in AB-3** — AB-1) |

Use the existing `LifecyclePhase` enum (Doc 12 §8.5: BOOTSTRAP…INTEGRATIONS + RUNNING/SHUTTING_DOWN/STOPPED). The openHAB ladder is the **ordering discipline** within/across Doc 12's phases — you need not mint a numeric enum unless it reads cleaner; if you do, keep it private/internal and do not change the Locked `LifecyclePhase` contract. `currentPhase()` returns the current `LifecyclePhase`.

**1c. Phase gates (establish; do not activate the AB-1/AB-4 pieces):**
- **HTTP / network exposure gate (openHAB 70 / Doc 12 Phase 5):** AB-3 must **NOT open an HTTP surface.** The current `start()` opens Javalin unauthenticated (steps 12–14) — that is core-review **C1**, and AB-3 is the moment it would go live. Establish the External-Interfaces phase as a **gated, not-yet-activated** step (do not bind the port, do not register endpoints) — AB-1 wires auth + opens it. (See Boundary + Watch-Out.)
- **Cipher-activation gate:** establish the gate "the payload cipher must be live before any sensitive read/write" (Doc 15 §3.8 adapter is app-hosted; R-δ AX-2). **Do not activate the cipher** — that is AB-4. HSC keeps its existing nullable-`PayloadCipher` injection; AB-3 leaves it null (inert), exactly as today.

**1d. Health loop + watchdog (Doc 12 §3.10).** After the engine reaches RUNNING, run the health loop on a dedicated virtual thread, period = `WatchdogSec / 2` (default 30 s): poll registered `HealthContributor`s → aggregate (three-tier) → `HealthReporter.reportWatchdog()` (`WATCHDOG=1`) → `reportStatus(...)`. The system does NOT self-terminate on UNHEALTHY (systemd's watchdog handles hangs). Use the **injected `Clock`** (never `Instant.now()` — production code IS caught by the arch rule). Wire `HealthReporter` selection: `SystemdHealthReporter` when `$NOTIFY_SOCKET` is set, else `NoOpHealthReporter` (the platform-systemd path). `reportReady()` fires only after the runnable phases complete (Doc 12 C12-08 — but note AB-3 does not open HTTP, so READY semantics for AB-3 = engine-running; AB-1 adds the API-serving precondition).

**1e. Pre-migration snapshot + one-click rollback hook (R-δ AX-2).** Before any schema/chain change, take a snapshot and expose a one-click rollback (HA's auto-backup-before-update strength; Apple's destructive-in-place migration anti-lesson). Doc 12 Phase 1 already backs up config before migration (§1.2); generalize the hook so it is invoked before any schema/chain migration. **This is additive — no destructive forced migration** (anti-requirement). For AB-3 the hook is wired into the lifecycle; the chain-change path itself is later (AB-4 / crypto).

### 2. The minimal production registries (PD-2 — `core:device-model`, contained fold)

Create `InMemoryEntityRegistry` (9 methods), `InMemoryDeviceRegistry` (7), `InMemoryAreaRegistry` (4, read-only). **Map-backed, start-empty, `ReentrantLock` for write serialization (LTD-11 — never `synchronized`).** Productionize the behavioral shape of `AutomationTestSupport.Stub{Entity,Area,Device}Registry`. Each class Javadoc states it is the **minimal MVP substrate** (start-empty; CRUD + the small query set; **no AMD-44 derivation, no Floor/EntityRole breadth**; populated later by M9/M14 integrations).

- `InMemoryAreaRegistry`: read-only (the interface has no create) — start-empty; `get`/`getAll`/`getByFloor(FloorId)` (filter `Area.floorId().equals(floorId)`) / `getUnassigned()` (filter `floorId == null`). It depends only on `AreaId`/`FloorId` (ULID wrappers) + `Area` — **no `FloorRegistry`.**
- **Do NOT implement `FloorRegistry` or `CapabilityRegistry`** — verified: none of `StandardSelectorResolver`/`StandardAutomationRegistry`/`StandardTriggerEvaluator`/`StandardConditionEvaluator`/`AutomationDefinitionLoader` references them. If implementation surfaces a path that provably needs one, STOP and escalate (do not silently fold it).

### 3. Land M7.1's three deferred wiring items (decision-record Addendum a/b/c)

**3a (dep a) — assemble `ConfigurationService` + the three registries into the composition root.** Build the registries (`new InMemory*Registry()`), and obtain a `ConfigurationService` via the new public factory (§Files). `ConfigurationService.load()` is the FIRST subsystem init step (config MODULE_CONTEXT / Doc 12 Phase 1). Note: assembling config pulls in its **`SecretStore`** (for `!secret`/`!env` resolution) via `SecretStore.create` + `ScopeKeyManager.create` — this is the **config-secret** substrate and is **separate from** the at-rest `PayloadCipher` (AB-4); assemble config's SecretStore, but leave the at-rest cipher inert (null), as today.

**3b (dep b) — schema registration + definition load (the glue relocated OUT of `core:automation`).** In the composition root (lifecycle/app — **never `core:automation`**, the banned `core→config` edge):
```
schemaRegistry.registerCoreSchema(AutomationSchema.SCHEMA_SECTION, AutomationSchema.SCHEMA_JSON);
LoadResult result = loader.load(configurationService.getCurrentModel().rawMap());
```
`loader` = `new AutomationDefinitionLoader(identityStore, entityRegistry, areaRegistry)` (`InMemoryAutomationIdentityStore` for `identityStore`). Feed `result.loaded()` into `StandardAutomationRegistry.load(...)`. Honor **SD-9 fail-closed-at-load** (a malformed definition fails closed, surfaced via `LoadResult.failures()` — do not boot a half-loaded ruleset silently; decide the FATAL-vs-log posture per Doc 12 §4's FATAL classification for Automation and flag it `[REVIEW]` if the contract is unclear).

**3c (dep a/b) — subscribe `automation_engine` AFTER state-store catch-up (the converge latent-defect site).** Build the evaluator chain — `StandardAutomationRegistry` → `StandardSelectorResolver(entity, area, device)` → `StandardTriggerEvaluator(registry, resolver, stateQueryService, eventPublisher, clock)` + `StandardConditionEvaluator(resolver, clock)` — wrap the `automation_engine` `Subscriber` via the public assembly seam (§Files), and register it with `eventBus.subscribeRuntime(new SubscriberInfo("automation_engine", SubscriptionFilter.all(), …), subscriber)`. **Contract:** the automation engine must not evaluate automations against state until the **state store is caught up (LIVE)** — automations must not fire on partial state during replay. Realize this via the state-store catch-up lever (`StateStoreLifecycle.start()` gating future and/or `ReadinessSource.mode()` reaching LIVE) — gate the `automation_engine` subscribe (or its evaluation) on state-store catch-up. The subscriber's own REPLAY/LIVE handling (`setMode`/`onCaughtUp`, driven by the bus — you do NOT call `setMode`) plus the evaluator's REPLAY timer-suppression are the belt-and-suspenders; the **ordering gate is yours to wire.** Pin it with the LifecycleWiringTest. **C1-interim:** the evaluator does not publish `automation_triggered` in production (holds to M7.2) — unchanged; do not add a publish here.

**3d (dep c) — the M7.1 lifecycle wiring test.** See Test Requirements.

### Verbatim `module-info.java` (touched modules) + proposed diff

**`lifecycle/lifecycle/src/main/java/module-info.java` — CURRENT (verbatim):**
```java
module com.homesynapse.lifecycle {
    requires transitive com.homesynapse.observability;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.persistence;
    requires transitive com.homesynapse.event.bus;
    requires transitive com.homesynapse.state;
    requires com.homesynapse.integration;
    requires com.homesynapse.api.rest;
    requires io.javalin;
    requires org.eclipse.jetty.util;
    requires org.slf4j;
    exports com.homesynapse.lifecycle;
}
```
**PROPOSED diff** (config/device/automation types appear ONLY inside the composition root internals, never on lifecycle's exported API → all three are **plain (non-transitive)** `requires` ⇔ Gradle `implementation(...)`):
```
+    requires com.homesynapse.config;
+    requires com.homesynapse.device;
+    requires com.homesynapse.automation;
```
> Authoring `requires transitive`↔`api` lockstep check: none of config/device/automation appears on lifecycle's **exported** API surface (they are referenced only inside `HomeSynapseCore`/`Main` composition internals), so each is **plain `requires` ⇔ `implementation(...)`** — NOT `requires transitive`/`api`. A non-transitive embed is correct here. (If the chosen design instead injects the already-assembled pieces from `Main` and HSC never names a config/device/automation type, drop the corresponding `requires` — then HSC holds only an event.bus `Subscriber` + java.base, and lifecycle's graph is unchanged. Pick one and make module-info + build.gradle.kts agree.)

**`core/automation` module-info (verbatim — UNCHANGED; the new public assembly class lives in the already-exported `com.homesynapse.automation`):**
```java
module com.homesynapse.automation {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.state;
    requires com.homesynapse.value;
    requires com.homesynapse.event.bus;
    requires org.slf4j;
    exports com.homesynapse.automation;
}
```
> **Do NOT re-add `requires com.homesynapse.config` here** (the FIX-07 instruction defect — `core:automation → config` is banned at every scope by `assertAllowedModuleDependencies`). The schema-register + load glue rides the composition root (3b).

**`core/device-model` module-info (verbatim — UNCHANGED; InMemory impls live in the already-exported `com.homesynapse.device`):**
```java
module com.homesynapse.device {
    requires transitive com.homesynapse.value;
    requires com.homesynapse.event;
    requires transitive com.homesynapse.platform;
    exports com.homesynapse.device;
}
```

**`config/configuration` module-info (verbatim — UNCHANGED; the new public factory lives in the already-exported `com.homesynapse.config`):**
```java
module com.homesynapse.config {
    requires transitive com.homesynapse.event;
    requires org.snakeyaml.engine.v2;
    requires com.networknt.schema;
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.databind;
    requires org.slf4j;
    exports com.homesynapse.config;
}
```

**`app/homesynapse-app` module-info (verbatim — UNCHANGED; already `requires` everything):**
```java
module com.homesynapse.app {
    requires com.homesynapse.lifecycle;
    requires com.homesynapse.observability;
    requires com.homesynapse.event;
    requires com.homesynapse.device;
    requires com.homesynapse.state;
    requires com.homesynapse.persistence;
    requires com.homesynapse.event.bus;
    requires com.homesynapse.automation;
    requires com.homesynapse.integration;
    requires com.homesynapse.integration.runtime;
    requires com.homesynapse.integration.zigbee;
    requires com.homesynapse.config;
    requires com.homesynapse.api.rest;
    requires com.homesynapse.api.ws;
    requires com.homesynapse.platform;
}
```

### The FIX-07 two-gate module-graph check (do BOTH gates)

1. **Gate A — `assertAllowedModuleDependencies` layer allow-list** (root `build.gradle.kts` `moduleGraphAssert.allowed`). Confirm every new edge is allowed:
   - `:lifecycle:.* -> :config:.*` ✅ (line ~56), `:lifecycle:.* -> :core:.*` ✅ (covers device + automation). So `lifecycle → {config, device, automation}` are **all allowed**.
   - `:core:.* -> :core:.*` / `-> :platform` ONLY → **`core:automation → config` stays banned** (do not re-add it). The InMemory registries (core:device-model) depend only on platform.identity + same-package types + java.base → within `:core:.* -> :platform`/`:core:.*`. ✅
   - `:app:.* -> .*` → Main may reference anything. ✅
2. **Gate B — `requires transitive`↔Gradle `api` lockstep** (the `-Xlint:exports`/`-Werror` trap). For each new `requires` in lifecycle: it is non-transitive (types not on the exported API) ⇒ Gradle `implementation(...)`. `implementation(":config:configuration")` already present; add `implementation(":core:device-model")` + `implementation(":core:automation")`. **Never hand a `requires transitive` for a module whose types are only used internally.**

Run a targeted `./gradlew :lifecycle:lifecycle:compileJava :core:device-model:compileJava :core:automation:compileJava :config:configuration:compileJava` (the `-Werror`/`[exports]`-sensitive touched modules) before handoff if the sandbox can run Gradle — it catches the lockstep + residency class in ~20 s (P5 shift-left). The full `./gradlew check` stays the deferred gate.

---

## P2 Consumer/Pin (Fan-Out) Survey

AB-3 adds production types + new module edges + a new bus subscriber, but mints **no new event type, no enum value, no sealed permit, and no manifest entry** (it wires existing pieces). The fan-out to sweep:

- **Event-type / manifest aggregators:** none changed. The automation event records already ride `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` (folded at M7.1); HSC.start() step 1 already aggregates them. **No manifest edit.** Confirm by grep that no `CORE_PRODUCTION_EVENT_CLASSES` / `EventCategoryMapping.TABLE` count changes (they must not).
- **Subscriber-count / composition-root registration pins:** the **dangerous** site. HSC.start() now registers a SECOND `subscribeRuntime` (`automation_engine`) beyond the projection. Grep the lifecycle + app test suites for any test pinning "N subscribers" / asserting the set of `subscribeRuntime` calls / `eventBus.subscribers()` size, and update. (This is the no-test-pins-it latent class the survey exists to catch.)
- **`module-info` / contract-direction (JPMS):** the new lifecycle edges are downward (lifecycle → config/device/automation) — correct direction, no cycle. The InMemory registries place no new type in a base/shared module (they're in device-model, where the interfaces live). No residency inversion. ✅
- **Count pins on the registries:** none exist yet (interfaces were impl-free). Add the new impl tests; ensure no `getDeclaredMethods().length` shape test on the interfaces breaks (the impls add methods to classes, not the interfaces).
- **`HealthContributor` / health-aggregation registrations:** if wiring the health loop adds contributors, sweep observability/lifecycle tests for health-set pins.
- **Behavioral publish-count pins:** AB-3 adds no publish site on an existing path (C1-interim no-publish holds). Confirm no automation publish is introduced.

---

## Locked Decisions That Apply

- **LTD-11 (No Broker):** `ReentrantLock`, never `synchronized` (VT pinning) — the InMemory registries' write serialization, the health-loop VT, any HSC locking.
- **LTD-19 / DECIDE-M2-05:** `HomeSynapseCore.start()` MUST be invoked from a **platform thread** (Jackson warmup pins VT carriers). `main()` calls `start()` on a platform thread.
- **LTD-04 (ULID):** identifiers are typed ULID wrappers; Crockford Base32 only at boundaries/logs. The registries key on `EntityId`/`DeviceId`/`AreaId`.
- **LTD-13 (systemd/FHS):** the watchdog period derives from `WatchdogSec`; `PlatformPaths` for directory conventions.
- **Doc 12 §4 fatal/non-fatal classification:** Configuration, Persistence, Event Bus, Device Model, State Store, Automation, REST API are FATAL subsystems (failure exits the process); Observability, WebSocket, integrations are non-fatal. AB-3's wiring must honor this (a failed automation-definition load posture per §4 — flag `[REVIEW]` if ambiguous).

## Invariants That Must Hold

- **INV-RF-03 (no external blocking during startup):** integrations connect in `run()` (Phase 6), not init. AB-3 doesn't touch integrations but must not introduce blocking external I/O in the init phases.
- **INV-SE-02 (auth on every external interface):** AB-3 must **not** open an external interface (defers to AB-1) — the way AB-3 honors INV-SE-02 is by NOT exposing HTTP. (No enforcing auth code is added here.)
- **INV-CE-02 (zero-configuration first run):** the system must boot with no hand-written config (start-empty registries + default config). The boot must not require pre-populated entities.
- **The catch-up ordering invariant (cross-module contract, lifecycle + automation + state-store MODULE_CONTEXTs):** automation subscribes/evaluates only after state-store catch-up.

---

## Test Requirements

### `LifecycleWiringTest` (the mandated M7.1 deferred test — dep c)

This is the test that could not be written against the M7.1 stubbed composition root. Test class: `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/LifecycleWiringTest.java`. **Inject `Clock.fixed(...)` (§4c).** Assert (real composition root, in-memory/temp-dir deps):

| Test Method | Scenario | Assertion |
|---|---|---|
| `start_assemblesConfigAndRegistries` | `mgr.start()` on a temp config dir | `ConfigurationService` loaded; the three `InMemory*Registry` instances assembled (start-empty: `listAllEntities().isEmpty()`, etc.) |
| `start_registersAutomationSchemaAndLoadsDefinitions` | config dir with a valid `automation:` section | `registerCoreSchema` called with `SCHEMA_SECTION`/`SCHEMA_JSON`; `loader.load(rawMap())` ran; `StandardAutomationRegistry` populated; `LoadResult.failures()` empty |
| `start_subscribesAutomationEngineAfterStateStoreCaughtUp` | boot to RUNNING | the `automation_engine` subscriber is registered; **it does not evaluate against state before the state store reaches LIVE** (assert ordering via the catch-up future / `ReadinessSource.mode()`; no automation fires on partial replay state) |
| `start_implementsSystemLifecycleManager` | hold HSC as `SystemLifecycleManager` | `mgr.currentPhase()` advances through the ladder to RUNNING; `subsystemStates()` non-empty; `healthSnapshot()` non-null |
| `start_doesNotOpenHttpSurface` | boot to RUNNING | **no HTTP port is bound** (the C1 boundary — `boundHttpPort()` reflects not-exposed / the Javalin server is not started); grep-equivalent assertion that no `app.start(port)` ran |
| `loadFailsClosed_onMalformedDefinition` | config with an invalid automation def | fails closed per SD-9 (surfaced in `LoadResult.failures()`; boot posture per Doc 12 §4) — no half-loaded ruleset silently accepted |
| `shutdown_reverseOrder` | `mgr.shutdown("test")` after start | subsystems torn down in reverse init order; idempotent on second call; `currentPhase() == STOPPED` |

### Registry unit tests
`InMemory{Entity,Device,Area}RegistryTest` — CRUD round-trip (Entity/Device), the query set (`listEntitiesByDevice`, `findByHardwareIdentifier`, `getByFloor`, `getUnassigned`), `IllegalArgumentException` on missing-id getters, start-empty, concurrent-read safety. (No `Clock` unless time is used.)

### Health-loop test
The health loop calls `HealthReporter.reportWatchdog()` each period under an injected `Clock` + a fake/advanceable scheduler (do NOT sleep real time); `NoOpHealthReporter` selected when `$NOTIFY_SOCKET` unset.

---

## What to Watch Out For

- **§4c — Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in the test code of `lifecycle`, `device-model`, `automation`, or `config` — these modules are **non-whitelisted**. **Caveat (corrected 2026-06-13):** the `NO_DIRECT_TIME_ACCESS` ArchUnit rule only scans from `com.homesynapse.app`'s test classpath, so `./gradlew check` will NOT catch a direct-time-access violation in these non-app modules' *test* code — treat Clock-injection as a **self-enforced convention** here. **Production** code in any module IS caught (so the health loop's time use must take the injected `Clock`). Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)`.
- **The `start()` signature reconciliation (PD-1).** `SystemLifecycleManager.start()` is `void … throws Exception` (Doc 12: "synchronously … blocks until initialization completes"); `HomeSynapseCore.start()` currently returns `CompletableFuture<Void>`. Reconcile cleanly: e.g., `SystemLifecycleManager.start()` blocks on the bootstrap future (`.join()` with fatal-exception unwrapping), keeping any async internals under a differently-named private/internal method. Confirm exact current signatures via the STOP gate; if reconciliation forces a public-API change to an existing HSC method consumed elsewhere, grep consumers (rest-api readiness gate, tests) and flag `[REVIEW]`.
- **The subscribe-after-catch-up site is the converge latent-defect.** Do not subscribe `automation_engine` such that it can evaluate against a partially-replayed state. The bus drives `setMode` (you don't); the ordering gate (subscribe/evaluate only after state-store LIVE) is the part you wire. Get the lever right (`StateStoreLifecycle.start()` future / `ReadinessSource.mode()`), and pin it with `start_subscribesAutomationEngineAfterStateStoreCaughtUp`.
- **`AutomationEngineSubscriber` is package-private; `AutomationConfigBridge` does not exist.** The composition root cannot name `AutomationEngineSubscriber`. Prefer adding a **public assembly seam** in `com.homesynapse.automation` that returns the `Subscriber` (keeps event.bus-coupled internals off the exported API) over promoting the class to public. Coder's call — **pushback welcome** if promotion reads cleaner, but justify the API-surface tradeoff.
- **No public `ConfigurationService` factory exists.** `StandardConfigurationService` (12-arg) + `StandardSchemaRegistry` + the `ConfigValidator` impl are package-private. Your new factory lives **inside `com.homesynapse.config`** (same package, exported) and must wire the `(major,minor)` pair **identically** into both the `StandardSchemaRegistry` and the `StandardConfigurationService` (config MODULE_CONTEXT: a mismatch fails every load). It needs `configDir: Path`, `Clock`, `SystemId`, `EventPublisher`, the resolving `SecretStore` (`SecretStore.create(Path, ScopeKeyManager, Clock)` + `ScopeKeyManager.create(Path, Clock)`), and `System::getenv`.
- **Config-secret SecretStore ≠ at-rest PayloadCipher.** Assembling config brings up its `SecretStore`/`ScopeKeyManager` (for `!secret`/`!env` config resolution). That is separate from the at-rest event `PayloadCipher` (AB-4). Do NOT activate the at-rest cipher; leave HSC's nullable cipher null (inert), as at `beb4bc3`.
- **Do not open HTTP / do not bind the port (C1).** AB-3 makes `main()` boot, which today would run `app.start(config.httpPort())` unauthenticated. Gate that phase CLOSED. This is the single most important boundary — AB-3 must not be the moment the unauthenticated surface goes live.
- **Platform-thread start (LTD-19).** Call `start()` from a platform thread in `main()`; the health-loop and timer VTs are fine as virtual threads, but the bootstrap (Jackson warmup) must not run on a VT carrier.
- **Do not touch a ratified contract.** AMD-88..93 untouched; no sealed permit/event type added; `RunContext` stays `int cascadeDepth` (the AMD-91 swap is M7.2). Doc 12/15 Locked — no silent edits (⛔ PD-1).

## Coder Pushback Welcome

If any specification here is impractical, contradicts a MODULE_CONTEXT gotcha, or could be done better at the same contract — raise it (skill §4a format). Specific invitations: the `start()` signature reconciliation shape; promote-vs-factory for `AutomationEngineSubscriber`; the exact catch-up lever; whether the config factory should return a small record `(ConfigurationService, SchemaRegistry)` or two calls. And if you find a wiring path that provably needs `FloorRegistry`/`CapabilityRegistry` — STOP and escalate, do not silently fold device-model breadth.

## Out of Scope / Boundary (what AB-3 does NOT do)

- **No auth, no bind posture** (AB-1 / INV-SE-02 / CC-1) — AB-3 does not open HTTP.
- **No `payloadCipher` activation, no read-contract/`DegradedEvent`** (AB-2 / AB-4) — AB-3 establishes the cipher phase-gate only; the cipher stays inert.
- **No `automation_triggered` production publish** (C1-interim holds to M7.2).
- **No device-model breadth** — AMD-44 Floor/EntityRole, Research-8 REC-23–30; the registries start empty, populate is downstream (M9/M14).
- **No M7.2 work** — `RunManager`/`ActionExecutor`/`CommandDispatchService`/`RunCausalChain` are not built here; AB-3 wires only the M7.1 `automation_engine` (trigger/condition) subscriber.
- **No retirement of the `SystemLifecycleManager` interface** (⛔ PD-1 — that is a Doc 12 amendment; escalate, do not delete).

## Build Discipline

You produce files. You do NOT run the full `./gradlew check` (it stays the deferred gate Nick runs). If the sandbox can run Gradle, run only the targeted `:compileJava` on the four touched modules (the two-gate check, P5 shift-left). Hand back as **fix-applied / NOT gate-verified** until Nick's full `./gradlew check` is GREEN — an LLM pass is not the gate (the M6.3/M7.1 lesson).

**Deferred Build Gate (flag in coder-handoff + the WUCP Phase 1 checklist):** Nick runs, against the commit that lands this diff:
1. `./gradlew :lifecycle:lifecycle:compileJava :core:device-model:compileJava :core:automation:compileJava :config:configuration:compileJava :app:homesynapse-app:compileJava` (the `-Werror`/`[exports]`-sensitive touched modules — catches the lockstep + module-graph + residency class fast),
2. then full `./gradlew check` (touched: lifecycle [first composition-root wiring + the wiring test], device-model [new impls + tests], config [new factory], automation [new assembly seam], app [Main]; incl. ArchUnit `NO_DIRECT_TIME_ACCESS` + `assertAllowedModuleDependencies` + spotless + moduleGraphAssert).

## Work Unit Completion (WUCP Phase 1)

After the compile gate passes or is deferred: update the four MODULE_CONTEXT.md files (HSC-implements-SLM; the InMemory registries; the config factory; the automation assembly seam; the resolved wiring — and flip the automation MODULE_CONTEXT's "composition-root wiring BLOCKED on app-bootstrap" gotcha to RESOLVED), update coder-handoff.md with the Deferred Build Gate flag + next-WU pointer, append any coder-lessons, post a cross-agent note, and append the WUCP Phase 1 checklist to your Completion Report. Flag every `[REVIEW]`/`[INFO]` deviation explicitly.

## Success Criterion

DONE when:
1. All files in "Files to Create or Modify" exist with the specified content; `Main` boots `HomeSynapseCore` (held as `SystemLifecycleManager`) with a SIGTERM shutdown hook.
2. HSC implements `SystemLifecycleManager` (interface preserved — PD-1); `start()` reconciled; `currentPhase()`/`healthSnapshot()`/`subsystemStates()` populated from the phase model; the §3.10 health loop + watchdog + `SystemdHealthReporter` path wired; the pre-migration snapshot/rollback hook in place.
3. The three `InMemory*Registry` impls exist in `core:device-model`, marked MVP-substrate, with tests; no `FloorRegistry`/`CapabilityRegistry` added.
4. The three M7.1 deferred items land: ConfigurationService + registries assembled; `registerCoreSchema` + `loader.load(rawMap())` glue in the composition root (NOT core:automation); `automation_engine` subscribed after state-store catch-up; **`LifecycleWiringTest` GREEN** (all methods).
5. AB-3 opens **no HTTP surface** and activates **no cipher** (the Seam-1 boundary).
6. The two-gate module-graph check passes (Gate A allow-list; Gate B lockstep); no manifest/count-pin regressions (P2 survey).
7. MODULE_CONTEXT.md updates + WUCP Phase 1 checklist complete.
