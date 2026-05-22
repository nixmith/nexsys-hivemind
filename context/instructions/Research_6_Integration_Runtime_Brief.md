<!--
file: context/instructions/Research_6_Integration_Runtime_Brief.md
purpose: Self-contained prompt for the Claude Project to produce Research 6 (Integration Runtime Supervisor Patterns).
audience: Nick (paste into Claude Project conversation)
state-type: ephemeral
-->

# RESEARCH BRIEF: Research 6 — Integration Runtime: Supervisor Patterns for Protocol Adapters

You are the PM/architect for HomeSynapse Core, a local-first event-sourced smart home runtime in Java 21 targeting Raspberry Pi 4/5. Your task is to produce a research document following the exact format specified below.

## Mandatory Format

Every research document must follow this structure. Non-negotiable sections are marked **[M]**; optional sections are marked **[O]**.

```
# Research 6: {Title} — {Subtitle}

*Target: HomeSynapse Core M9 (with M4 lifecycle-hook coupling). Date: YYYY-MM-DD.*

## 1. Executive Summary [M]
  - 5-8 bullet points, each a **verdict** with a bold claim and one-sentence defense.
  - Every bullet must take a position. "X is worth investigating" is banned.
    Use "X should be adopted because Y" or "X should be rejected because Y."
  - Flag the single highest-impact finding explicitly.

## 2. Platform / Literature Deep Dives [M]
  - One subsection per platform or prior-art system studied.
  - Each subsection must include:
    (a) How the platform solves the problem under investigation.
    (b) At least one direct quotation from primary source (docs, issue tracker,
        maintainer statement) with URL.
    (c) Known pain points / failure modes from community reports.
    (d) Specific lesson for HomeSynapse (not generic observation).

## 3. Cross-Cutting Analysis [M]
  - Concept Mapping Table: HomeSynapse concept | Platform A | Platform B | ...
  - Gap Analysis: concepts present in 2+ platforms that HomeSynapse lacks,
    ranked by impact.
  - Over-Abstraction Analysis: concepts HomeSynapse has that no one needs,
    with defense or retraction for each.
  - Competitive Assessment: where HomeSynapse is genuinely differentiated,
    with the precise qualifying language that survives scrutiny.

## 4. Amendment Recommendations [M]
  - Ranked by (impact × confidence) / cost.
  - Each REC must include: Gap citation, Lesson source, Change (specific
    record/interface/event shape), Backward compat assessment, Effort estimate.
  - REC-XX format. Numbered globally: Research 4 used REC-31 through REC-40.
    This document starts at REC-41.

## 5. Caveats and Open Questions [M]
  - Source reliability notes.
  - Unresolved tensions between platforms.
  - Questions that require empirical validation (spike/prototype).

## 6. Appendix: Sources [M]
  - URL families grouped by platform.
  - Every factual claim must be traceable to a source listed here.

## 7. HomeSynapse Code-Level Implications [M — required for this research]
  - Specific records, interfaces, sealed hierarchy changes.
  - Event schema additions.
  - MODULE_CONTEXT impact (which modules gain/change types).
  - JPMS module-info impact.
  - Migration considerations (V00x).
```

---

## SCOPE

The Integration Runtime is the supervisory layer that loads, isolates, monitors, and lifecycle-manages every integration adapter inside the HomeSynapse process. It is HomeSynapse's analog of an Erlang/OTP supervisor tree applied to protocol adapters (Zigbee, MQTT, cloud APIs). Doc 05 specifies an OTP-style one-for-one supervisor with a four-state health FSM (HEALTHY → DEGRADED → SUSPENDED → FAILED), asymmetric hysteresis, sliding-window error/timeout/slow-call rates, a weighted health-score formula, exponential restart backoff with intensity limits, and topological startup ordering via Kahn's algorithm. What is missing is empirical validation against production smart-home supervisor implementations and a sharp answer to a specific question: **which IntegrationContext lifecycle hooks does M4 need to expose so that M9's supervisor can implement reauth / reconfigure / options-flow patterns without retroactive AMDs?**

This research is sequenced now (after Research 4 / Research 8 closure) because Research 4 identified that M7 automation needs constrain M4 device-model decisions, and the same logic applies here: M9 supervisor needs constrain M4 IntegrationContext design. Research 2's REC-08 ("Formalize IntegrationContext lifecycle: Reauth, Reconfigure, OptionsFlow analogs") explicitly flagged this coupling. The longer this research is deferred, the more likely M4 will ship an IntegrationContext shape that needs amendment when M9 begins.

### Specific questions to answer

1. **Erlang/OTP supervision in Java.** Doc 05 specifies OTP-style one-for-one supervision. What Java libraries actually exist for OTP-style supervision? (Akka/Pekko typed actors — but HomeSynapse is explicitly NOT actor-based.) How do you implement restart-intensity throttling (max N restarts in T seconds) with virtual threads instead of actors? What's the simplest correct pattern? The supervisor maintains per-integration mutable state (sliding-window deques, restart timestamps, FSM state) — what concurrency primitives does it need? `ConcurrentLinkedDeque` + `ReentrantLock` is the assumed answer (LTD-11 forbids `synchronized`), but validate against real implementations. What's the failure taxonomy granularity? HomeSynapse's `ExceptionClassification(TRANSIENT / PERMANENT / SHUTDOWN_SIGNAL)` — is this the right granularity, or are there subdivisions production systems find load-bearing?

2. **Adapter lifecycle FSM design.** OpenHAB's `ThingStatus` FSM (UNINITIALIZED → INITIALIZING → ONLINE / OFFLINE / UNKNOWN, with REMOVING and REMOVED) is well-documented. HA's `ConfigEntry` lifecycle (NOT_LOADED → SETUP_IN_PROGRESS → LOADED → SETUP_RETRY → SETUP_ERROR → MIGRATION_ERROR → FAILED_UNLOAD). HomeSynapse's `HealthState(HEALTHY, DEGRADED, SUSPENDED, FAILED)` is collapsing OpenHAB's UNINITIALIZED/INITIALIZING into the supervisor's pre-start state and OpenHAB's ThingStatusDetail into a sliding-window health score. Is this collapse the right call, or do operators need to distinguish "still initializing" from "running but unhealthy"? Compare HA's `ConfigEntry.state` against HomeSynapse's `IntegrationHealthRecord.state` — what semantic gaps exist? In particular, where in HomeSynapse's FSM does "config validation failed at startup" land? What about "config validation succeeded but external device unreachable"?

3. **Health aggregation and the weighted score formula.** Doc 05 §4.3 specifies `healthScore = 0.30 × (1 − errorRate) + 0.20 × (1 − timeoutRate) + 0.15 × (1 − slowCallRate) + 0.20 × dataFreshnessScore + 0.15 × resourceComplianceScore`. How does HA aggregate health per-integration? (Answer: no formal aggregation — each integration self-reports a binary loaded/not-loaded plus optional setup_error.) How does OpenHAB aggregate? (ThingStatusInfo with detail enum.) Is HomeSynapse's weighted formula overengineered? What evidence supports the specific weights (0.30 / 0.20 / 0.15 / 0.20 / 0.15)? What about HA's per-entity availability vs HomeSynapse's per-integration health — are these the right levels of granularity? Are there production smart-home supervisors that use a unified score, or does everyone use ad-hoc health signals?

4. **IntegrationContext lifecycle hooks — the M4-coupled question.** Doc 05 §3.8 defines `IntegrationContext` (10 fields, all required at construction). Adapters declare requirements once via `IntegrationDescriptor`, and the supervisor injects a single context at adapter creation. But Home Assistant's `ConfigEntry` flow has *post-setup* lifecycle hooks: `async_reload` (config changed, rebuild), `async_migrate_entry` (schema migration), `async_unload` (clean shutdown), `async_remove` (deletion). HomeSynapse currently has only `IntegrationAdapter.close()` for shutdown — there's no `reload`, no `migrate`, no `reconfigure`. What lifecycle hooks do real-world adapters actually need? Specifically: (a) Reauth flow — token expires, adapter needs to prompt user re-auth without full restart; (b) Reconfigure flow — user edits config, adapter needs to apply changes (rate limits, polling intervals, device list) without losing in-flight commands; (c) Options flow — runtime-tunable parameters distinct from setup config; (d) Migrate flow — adapter version bump requires config schema migration. Which of these does HomeSynapse's `IntegrationContext` need to expose hooks for? Should `IntegrationAdapter` gain methods like `reload(IntegrationContext)`, `migrate(int fromVersion, int toVersion)`, or should these be supervisor-level operations that the adapter signals via events? **Be specific: propose the exact method signatures.**

5. **Dynamic capability discovery post-adoption.** Research 2 §2.3.3 surfaced OpenHAB's pain with dynamic channel creation (openhab-core#4048: channels added at runtime after Thing initialization). When a Zigbee device firmware-updates and gains a new cluster, or a Matter bridge gains a new endpoint, the adapter needs to publish a new `Entity` or extend an existing entity's capabilities. Today's HomeSynapse model has entities and capabilities declared via events (`entity_registered`, `capability_added`?), but does the spec define a "capability_added_post_registration" event? What about capability *removal* (firmware downgrade, hardware swap)? How do HA and OpenHAB handle these? What event schema does HomeSynapse need?

6. **Startup ordering with dependency graphs (Kahn's algorithm in production).** Doc 05 §3.13 specifies Kahn's algorithm with cycle detection (AMD-14). What real dependencies exist between integrations in production smart-home systems? Concrete examples: Zigbee coordinator must start before Zigbee devices (already obvious). Matter bridge must start before bridged devices. What about cross-platform dependencies — a Zigbee group must exist before an automation referencing the group can be enabled (out of scope — that's an automation engine concern). How does HA handle this? (Manifest `after_dependencies` with platform-vs-integration distinction.) How does OpenHAB? Are there real-world dependencies that Kahn's algorithm doesn't model well (e.g., probabilistic dependencies, "integration B is optional if integration A is present")?

7. **Planned restart lifecycle (Doc 05 §3.14) vs ordinary restart.** HomeSynapse distinguishes "planned restart" (supervisor-initiated, e.g., config reload) from "transient failure restart" (TRANSIENT exception → exponential backoff). Planned restarts: suppress `availability_changed` events for owned entities, queue inbound commands, exclude owned devices from orphan detection (AMD-17), 60s timeout. Validate this design against real platforms. Does HA distinguish planned from failure-driven restarts? (Answer: partially — `async_reload` is planned, exception-driven setup_retry is not.) What does OpenHAB do? Is the 60s timeout the right magnitude? Should the supervisor expose this distinction to consumers (REST API, observability), or is it purely internal?

8. **Multi-process isolation as a non-goal.** HA isolates integrations only at the asyncio coroutine level (single process). OpenHAB runs all bindings in one OSGi container. HomeSynapse runs adapters in a single JVM, isolated by JPMS modules + dedicated threads. What real failure modes does this leave unaddressed? Specifically: native memory leaks in JNI (xerial sqlite-jdbc, but also any USB-serial adapter), OOM by one integration killing the whole JVM, blocked carriers from `synchronized` JNI (mitigated by SERIAL → platform thread). Is the JVM-level isolation enough for the Pi 4/5 target, or should HomeSynapse plan for sub-process isolation as a future capability? If yes, what hooks need to exist in the IntegrationContext to allow future out-of-process adapters?

9. **Authentication and credential lifecycle.** Cloud-connected adapters (hypothetical: Hue Bridge, Ecobee, Ring) need OAuth refresh, API key rotation, and certificate updates. HomeSynapse's `ConfigurationService` provides AES-256-GCM encrypted secrets, but there's no formal credential-lifecycle protocol. What does HA do? (Config flow with reauth step.) What does OpenHAB do? (Per-binding credentialed config, no rotation primitive.) Does the IntegrationContext need a `CredentialRotator` service, or is this an adapter-internal concern with the supervisor providing only secret access?

10. **Composite health and observability surface.** Doc 11 §11.3 specifies a composite health indicator. The supervisor exposes `allHealth() → Map<IntegrationId, IntegrationHealthRecord>`. Doc 09 §3.2 / §7 specifies REST endpoints for integration health. What does HA expose? (`/api/states` with availability per entity, plus integration-list endpoint.) What does OpenHAB? (`/rest/things` with status detail.) Validate the granularity choice. Is per-integration the right reporting unit, or do operators need per-entity? What about the relationship to the new M4 `device_reachable_changed` event (Research 8 REC-25)?

### Platforms / prior art to survey

- Erlang/OTP supervisor documentation (canonical reference, especially supervision tree semantics)
- Akka/Pekko typed supervision (Java adaptation — for contrast, since HomeSynapse is NOT actor-based)
- Home Assistant integration lifecycle (`ConfigEntry`, `async_setup_entry`, `async_unload_entry`, `async_migrate_entry`, config flow / options flow / reauth flow)
- OpenHAB binding lifecycle (`ThingHandlerFactory`, `ThingHandler.initialize/dispose`, `ThingStatus`, `ThingStatusDetail`)
- Eclipse Kura container service lifecycle (Karaf / OSGi DS — for constrained-platform comparison)
- Android service lifecycle (for comparison — constrained platform, well-documented FSM)
- Matter 1.4 Bridged Device Basic Information cluster (Reachable attribute, structural reachability)
- Java virtual-thread supervisor patterns (Loom-era literature, JDK 21+ idioms)

---

## CONTEXT YOU NEED

- HomeSynapse Core Knowledge Primer (uploaded to project knowledge — refreshed 2026-05-22, automation/device-model/integration-zigbee package annotations corrected)
- HomeSynapse Current State (uploaded to project knowledge)
- Doc 05 (Integration Runtime) — the governing design document for this research
- Research 2 findings, especially REC-08 (IntegrationContext lifecycle formalization)
- Research 8 findings (Device Model Implementation) — REC-25 introduces `device_reachable_changed`, which is the supervisor's primary signal for "external device is unreachable"
- Research 4 findings (Automation Engine) — establishes the pattern that target-module type inventories must be embedded in research briefs

### Key context from completed upstream research (M4 / M7 implications):

- **Research 8 REC-25 (ACCEPTED for M4.0):** `device_reachable_changed(DeviceId, boolean reachable, Instant at)` — DEVICE-level event, not entity-level. The supervisor produces this when a transport-level signal (Zigbee bridge offline, MQTT broker dropped) makes ALL entities owned by an integration unreachable. The state projection updates `Availability` on child entities via this event. Research 6 must specify which supervisor signals translate to this event vs which translate to per-entity `availability_changed`.

- **Research 8 REC-28 (ACCEPTED for M4.0):** `DispatchingProjectionAdvancer` with constructor-injected handlers (DECIDE-04, NO ServiceLoader). Each new event type the supervisor produces (`integration_started`, `integration_stopped`, `integration_health_changed`, `integration_restarted`, `integration_resource_exceeded`, plus any new ones Research 6 proposes) must have a `ProjectionEventHandler` if it changes state — or be declared observability-only.

- **Research 4 RECs:** Automation triggers can subscribe to integration lifecycle events (e.g., "when Zigbee bridge goes offline, send notification" — an `AvailabilityTrigger` would NOT fire because the supervisor suppresses per-entity availability events during planned restart; a new trigger type listening to `integration_stopped` may be required). Research 6 should consider whether new automation-facing events are needed.

- **OR-M3-17 + OR-M3-18 (open):** `HomeSynapseCore.start()` currently injects `NO_OP_DERIVATION` and `NO_OP_ADVANCER` as placeholders. These close at M4.0 when `DispatchingProjectionAdvancer` ships. Research 6 should consider whether integration-runtime contributes handlers to that advancer (likely yes, for `integration_started`/`integration_stopped`/etc.).

### Key architectural constraints:

- The integration-api module is `integration/integration-api` with package `com.homesynapse.integration` (single flat package, 22 types).
- The integration-runtime module is `integration/integration-runtime` with package `com.homesynapse.integration.runtime` (single flat package, 6 types — scaffold only in Phase 2).
- DECIDE-04: No `ServiceLoader`. Adapters are discovered via explicit `List<IntegrationFactory>` passed to `IntegrationSupervisor.start(...)`.
- LTD-01: `IoType.NETWORK` → virtual thread per adapter; `IoType.SERIAL` → dedicated platform thread (JNI carrier pinning on Pi 4 cores).
- LTD-11: No `synchronized`. Concurrent state uses `ConcurrentLinkedDeque`, `ReentrantLock`, atomic fields. Sliding-window deques and FSM transitions are the main supervisor concurrency surface.
- LTD-17: Adapters use `IntegrationContext` only — no core-internal imports. Build-time (Gradle) and JPMS module-info enforcement.
- AMD-14: Kahn's algorithm with cycle detection for startup ordering. Shutdown in reverse topological order.
- AMD-17: Orphan transition timing — when an integration is removed, its entities' `Availability` must be set to `STALE` immediately, not deferred until AMD-11's 30-second periodic scan. The supervisor is the trigger for this orphan transition.
- AMD-26: All `sqlite-jdbc` operations on platform threads. The supervisor itself does not touch SQLite directly in Phase 2; Phase 3 will publish lifecycle events via `EventPublisher`, which routes writes through the persistence layer's platform-thread executor.
- DEC-M3-09: `Clock` injection for testability — supervisor health-window timestamps, restart-intensity timers, and backoff schedules all take `Clock` via constructor injection. No `Instant.now()` or `System.nanoTime()` (also enforced by `NO_DIRECT_TIME_ACCESS` ArchUnit rule).
- INV-RF-01: Integration isolation — supervisor catches ALL exceptions escaping the adapter boundary.
- INV-RF-03: Startup independence — `IntegrationSupervisor.start()` completes regardless of external device connectivity.
- INV-RF-06: Graceful degradation — four-state health FSM with asymmetric hysteresis is non-negotiable.

---

## CONSTRAINTS

- Take positions. "X is worth investigating" is banned. Use "X should be adopted because Y" or "X should be rejected because Y."
- Cite primary sources (docs, issue trackers, maintainer statements) with URLs.
- Every REC must include effort estimate in lines of code.
- Number RECs globally: Research 4 used REC-31 through REC-40. **This document starts at REC-41.**
- AMD numbering: AMD-01 through AMD-52 are allocated/proposed (AMD-47 withdrawn). New amendments start at **AMD-53**.
- Include §7 (Code-Level Implications) — MANDATORY. Specify exact Java records, interfaces, sealed hierarchy changes, event schema additions, module-info changes.
- For each proposed type change, specify: (a) the exact module, (b) the exact package, (c) public vs package-private visibility, (d) whether it requires an AMD (amendment to a Phase 2 interface).
- **Package name accuracy is critical.** Prior research documents (Research 3, Research 4, Research 8) had systematic package-name and type-name errors that required PM correction. Do NOT invent type names. The verified type inventories for the two target modules appear below — refer to them as the source of truth.

### Verified type inventory — `core/automation/MODULE_CONTEXT.md`-style — for integration-api (`com.homesynapse.integration`)

This is the complete, MODULE_CONTEXT-verified type inventory for `integration/integration-api`. Use these names verbatim. Do NOT add to or modify the list without explicit justification in §7.

**Enums (4):**
- `HealthState` — 4 values: `HEALTHY`, `DEGRADED`, `SUSPENDED`, `FAILED`. Four-state health model (Doc 05 §4.3).
- `IoType` — 2 values: `SERIAL` (platform thread, JNI pinning), `NETWORK` (virtual thread).
- `RequiredService` — 3 values: `HTTP_CLIENT`, `SCHEDULER`, `TELEMETRY_WRITER`. Gates optional service provisioning in `IntegrationContext`.
- `DataPath` — 2 values: `DOMAIN` (event store), `TELEMETRY` (ring buffer).

**Records (9):**
- `IntegrationDescriptor` (8 fields): `integrationType`, `displayName`, `ioType`, `requiredServices`, `dataPaths`, `healthParameters`, `dependsOn`, `schemaVersion`.
- `HealthParameters` (11 fields): `heartbeatTimeout`, `healthWindowSize`, `maxDegradedDuration`, `maxSuspendedDuration`, `maxSuspensionCycles`, `maxRestarts`, `restartWindow`, `probeInitialDelay`, `probeMaxDelay`, `probeCount`, `probeSuccessThreshold`. `defaults()` factory for network polling adapters.
- `IntegrationContext` (10 fields): `integrationId`, `integrationType`, `eventPublisher`, `entityRegistry`, `stateQueryService`, `healthReporter`, `configAccess`, `schedulerService` (nullable), `telemetryWriter` (nullable), `httpClient` (nullable). Optional fields null iff the corresponding `RequiredService` was NOT declared.
- `CommandEnvelope` (6 fields): `entityRef`, `commandName`, `parameters`, `commandEventId`, `correlationId`, `integrationId`. `commandEventId` and `correlationId` are raw `Ulid`, NOT `EventId`.
- `IntegrationStarted` (4 fields): `integrationId`, `integrationType`, `newState`, `reason`. `previousState()` always returns null.
- `IntegrationStopped` (5 fields): `integrationId`, `integrationType`, `previousState`, `newState`, `reason`.
- `IntegrationHealthChanged` (6 fields): `integrationId`, `integrationType`, `previousState`, `newState`, `reason`, `healthScore`.
- `IntegrationRestarted` (6 fields): `integrationId`, `integrationType`, `previousState`, `newState`, `reason`, `restartCount`.
- `IntegrationResourceExceeded` (8 fields): `integrationId`, `integrationType`, `previousState`, `newState`, `reason`, `resourceType`, `currentValue`, `limitValue`. CRITICAL priority.

**Sealed Interface Hierarchy:** `IntegrationLifecycleEvent` (sealed, extends `DomainEvent`) — permits exactly the 5 lifecycle records above (`IntegrationStarted`, `IntegrationStopped`, `IntegrationHealthChanged`, `IntegrationRestarted`, `IntegrationResourceExceeded`). The sealed parent does NOT carry `@EventType`; the 5 concrete subtypes each carry their own `@EventType(EventTypes.INTEGRATION_*)`.

**Service Interfaces (6):**
- `IntegrationFactory` — `descriptor()` → `IntegrationDescriptor` (pure, no I/O), `create(IntegrationContext)` → `IntegrationAdapter`.
- `IntegrationAdapter` extends `AutoCloseable` — `initialize()` (no external I/O per INV-RF-03), `run()` (main loop), `close()` (idempotent cleanup), `commandHandler()` → `CommandHandler` (nullable for read-only adapters).
- `HealthReporter` — `reportHeartbeat()`, `reportKeepalive(Instant)`, `reportError(Throwable)`, `reportHealthTransition(HealthState, String)`.
- `CommandHandler` (`@FunctionalInterface`) — `handle(CommandEnvelope) throws Exception`.
- `SchedulerService` — `schedule(Runnable, Duration)`, `scheduleAtFixedRate(Runnable, Duration, Duration)`, `shutdown()`.
- `ManagedHttpClient` — `send(HttpRequest, BodyHandler)`, `sendAsync(HttpRequest, BodyHandler)`, `close()`.

**Exception (1):** `PermanentIntegrationException` extends `HomeSynapseException`.

**Utility (1):** `IntegrationEvents` (public final, private constructor) — exposes `LIFECYCLE_EVENT_CLASSES` (`public static final List<Class<? extends DomainEvent>>`) listing the 5 lifecycle subtypes. Composition root aggregates this with `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` via `Stream.concat` for the `EventTypeRegistry`.

**Total: 22 public types + module-info.java + package-info.java.** Single flat package.

### Verified type inventory — for integration-runtime (`com.homesynapse.integration.runtime`)

**Enums (1):**
- `ExceptionClassification` — 3 values: `TRANSIENT` (restart with backoff), `PERMANENT` (transition to FAILED), `SHUTDOWN_SIGNAL` (do not restart). Shutdown-aware reclassification: when per-adapter `shuttingDown` flag is set, `SocketException`/`IOException` reclassified from TRANSIENT to SHUTDOWN_SIGNAL.

**Records (2):**
- `SlidingWindow` (3 fields): `size` (int), `count` (int), `rate` (double). Point-in-time snapshot of an error/timeout/slow-call window. Phase 3 backing is `ConcurrentLinkedDeque<Instant>`.
- `IntegrationHealthRecord` (13 fields): `integrationId`, `state` (HealthState), `healthScore` (double 0.0–1.0), `lastHeartbeat`, `lastKeepalive` (nullable), `stateChangedAt`, `consecutiveFailures`, `suspensionCycleCount`, `totalSuspendedTime`, `errorWindow` (SlidingWindow), `timeoutWindow` (SlidingWindow), `slowCallWindow` (SlidingWindow), `plannedRestart` (boolean).

**Service Interface (1):** `IntegrationSupervisor` — 9 methods: `start(List<IntegrationFactory>) → CompletableFuture<Void>` (async), `stop() → void` (sync, blocking), `startIntegration(IntegrationId) → CompletableFuture<Void>`, `stopIntegration(IntegrationId) → CompletableFuture<Void>`, `restartIntegration(IntegrationId) → CompletableFuture<Void>`, `health(IntegrationId) → Optional<IntegrationHealthRecord>`, `allHealth() → Map<IntegrationId, IntegrationHealthRecord>` (unmodifiable snapshot), `isRunning(IntegrationId) → boolean` (HEALTHY or DEGRADED), `registeredIntegrations() → Set<IntegrationId>` (unmodifiable).

**Total: 4 public types + package-info.java + module-info.java = 6 Java files.** Single flat package. Scaffold-only in Phase 2 — no `IntegrationSupervisor` implementation exists yet.

### Verified upstream constraints (do not propose changes to these in Research 6 — they are M4 scope)

- `Entity` (device-model) — 11 fields per Research 8 brief. New fields (`category`, `tags`) land in M4.0 per Research 8 REC-23/REC-26.
- `EntityState` (state-store) — 9 fields per Research 8 brief. Does NOT carry structural metadata.
- `AttributeValue` (device-model) — sealed interface with 5 permits: `BooleanValue`, `IntValue`, `FloatValue`, `StringValue`, `EnumValue`. New permits land in M4.0 per Research 8 REC-24/REC-27.
- `Availability` (state-store) — enum: `AVAILABLE`, `UNAVAILABLE`, `UNKNOWN`. The supervisor's reachability signals translate to this enum on child entities via `device_reachable_changed` (Research 8 REC-25).
- `Capability` (device-model) — sealed interface with 16 permits (15 standard + `CustomCapability`). Standard permits include `Motion`, `Occupancy`, `Contact`.
- `DomainEvent` (event-model) — permanently non-sealed (AMD-33). Use `@EventType` annotation + `EventTypeRegistry` for dispatch, NOT pattern matching on a sealed root.

### Event naming convention

Legacy events use snake_case with underscores: `entity_registered`, `state_reported`, `integration_started`. New events use dot-separated namespacing: `device.reachable_changed`, `automation.run_started`. Both patterns are permanent. When proposing new integration lifecycle events in §7, use whichever style fits the cluster (existing `integration_*` events use underscore; new ones may use either — recommend dot-separated for clarity).

---

## OUTPUT

A single markdown document following the mandatory format above. Do not truncate. Produce the complete document. Target length: ~600–800 lines.

When you reach §7 (Code-Level Implications), structure proposals around these specific surfaces:

1. **`IntegrationContext` field additions or shape changes** — list each field by name + type + nullability + which `RequiredService` gates it. State whether it requires an AMD (yes — `IntegrationContext` is a Phase 2 public record).

2. **`IntegrationAdapter` interface additions** — list each new method by signature, default vs abstract, throws clause. State whether it requires an AMD (yes — interface change).

3. **`IntegrationLifecycleEvent` sealed hierarchy additions** — list each new record by name + fields + `@EventType` constant. State which are state-changing (need `ProjectionEventHandler`) vs observability-only.

4. **`IntegrationDescriptor` field additions** — for declaration-time adapter requirements (e.g., a `lifecycleHooks: Set<LifecycleHook>` field).

5. **`HealthParameters` field additions** — for any new tunable knobs.

6. **New supervisor-internal types** in `com.homesynapse.integration.runtime` (e.g., a `LifecycleHookDispatcher`, a `CredentialRotator`, a `ConfigReloadCoordinator`). State that these need NOT be AMDs because the runtime module is still scaffold-only — adding types to it is normal Phase 3 work.

7. **Cross-module impacts** — does Research 6 require changes to `core/event-model` (new event types), `core/state-store` (new projection handlers), `config/configuration` (new credential APIs)?

8. **JPMS module-info changes** — what `requires` directives need to be added to `integration-runtime` (today: only `requires transitive com.homesynapse.integration`; Phase 3 will add `event-model`, `event-bus`)?

If Research 6 surfaces a question that genuinely requires an empirical spike (e.g., "does Kahn's algorithm with cycle detection handle N = 20 integrations in <50ms on a Pi 4?"), flag it in §5 as a Phase 3 prerequisite spike, not as a Phase 2 blocker.

### Coder Pushback Welcome

If Research 6 uncovers a contradiction between Doc 05 §3.x and the verified MODULE_CONTEXT type inventories above, flag it explicitly in §5. The MODULE_CONTEXT is authoritative for type-level facts (verified 2026-05-22). Doc 05 is authoritative for behavioral contracts. If they diverge, that's a PM action item, not a researcher fabrication.
