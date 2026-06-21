<!--
file: context/handoff/coder-handoff.md
purpose: Coder session continuity — current task, deferred build gate, next WU, recent closeouts.
audience: Coder, PM
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-05-27 against M3.7 closeout working tree — `./gradlew check` GREEN (139 tasks). Pending commit.
-->

# Coder Session Handoff

---

## M7.2a-1 — Run Lifecycle (RunCausalChain, RunContext swap, run-lifecycle event sub-slice, RunManager FSM) — DONE, NOT gate-verified (2026-06-21)

**Coder (Claude Code).** Built M7.2a-1 per `context/instructions/2026-06-21_M7.2a-1_run-lifecycle_coding-instruction.md` (AMD-91 + AMD-92 rows 2/7/8/10/17/18; Doc 07 + Doc 16 Locked). Handed back **fix-clean / NOT gate-verified** — Nick runs `./gradlew check`. All STOP-on-Mismatch gates re-verified at HEAD `9e73d28` (RunContext 8-comp with `int cascadeDepth` at field 7; RunManager 5-method interface with trailing `int`; RunStatus 7 values incl. INTERRUPTED; ActionExecutor `execute(List,RunContext)`; AutomationCompletedEvent 3-comp; EventTypes 62 const / roster 32; EventCategoryMapping TABLE 44; no StandardRunManager/StandardActionExecutor present). Every gate row MATCHED. A 5-dimension in-session adversarial verification (residency/JPMS, count-pins, FSM compile+logic, tests, constraints) returned **ZERO findings** (an LLM pass, NOT the gate).

**What landed (production, 15 files):**
- **event-model:** RESHAPED `AutomationCompletedEvent` 3→7 comp (row 2: `Ulid runId, String finalStatus, long durationMs, int actionCount, int commandCount, String failureReason?, String abortReason?`); MINTED 5 records — `AutomationRunSkippedEvent` (7), `AutomationRunCancelledEvent` (8), `AutomationDisabledEvent` (10, NORMAL), `CascadeDepthExceededEvent` (17), `CascadeLoopDetectedEvent` (18); `EventTypes` +5 constants (under a `// M7.2 run-lifecycle vocabulary (AMD-92)` banner) + 5 roster entries + Javadoc 32→37. **All flattened (AMD-92-INV-01): runId/cancelledRunId/etc = bare Ulid, finalStatus/mode/severity = String, cascadeDepth = int, cycle path = List<AutomationId>.** event-model module-info UNCHANGED.
- **automation:** `RunCausalChain` (+ nested `ChainLink`) — derived `depth()`, `root()`/`extend()`/`containsAutomation()`; `RunContext` field-7 swap `int cascadeDepth` → `RunCausalChain causalChain` (non-null); `RunManager` `initiateRun` last param `int cascadeDepth` → `RunCausalChain parentChain` + NEW `finalizeZombieRuns(List<ZombieRun>)` + nested `ZombieRun` record; `RunConditionGate` (functional seam); `RunManagerConfig` (plain record, no config edge); `StandardRunManager` (the FSM, package-private, `implements RunManager, AutoCloseable`); `RunManagerAssembly` (public seam → RunManager, mirrors AutomationEngineAssembly). automation module-info UNCHANGED.
- **persistence:** `EventCategoryMapping` +5 `[AUTOMATION]` rows (44→49).

**The C1-interim publish hold (SD-3) is CLOSED** (DP-E): `automation_triggered` (row 1) now has its completing partner — `StandardRunManager` publishes it at Run initiation and `automation_completed` at the terminal transition. Publishes carry the triggering event's `CausalContext` (derived/chained), `actorRef = AutomationId` on the envelope (DP-H), null/inherited `eventTime` (DP-G, never `Instant.now()`).

**Pin fan-out swept (P2 survey, all updated + count-reconciled):** EventTypes 62→67 const / 32→37 roster; EventTypeAnnotationTest EXPECTED_EVENT_RECORDS +5 / hasSize(37) / isEqualTo(37L); EventTypesTest hasSize(67); AutomationCompletedEventTest rewritten to 7-comp (hasSize(7) + 7-arg ctors); EventCategoryMapping(Test) 44→49; EventTypeRegistryTest 32→37 / 44→49; JacksonWarmupTest 44→49 / 32→37; TestEventSamples 2 builders → 7-arg; AllEventClasses prose 32→37 / 44→49; AutomationEventSerdeTest +6 round-trips (reshaped completed + 5 new); IntegrationTestHarness cosmetic prose 36→49.

**Tests created:** `RunCausalChainTest` (AMD-91 §5), `StandardRunManagerTest` (14 FSM cases: dedup, C3 comparator, SINGLE/RESTART/QUEUED admission, condition-not-met-no-slot, completed/failed, cascade depth+cycle+determinism, auto-disable, replay-zombie, residency), 5 per-record event tests. All build against fake `ActionExecutor`/`RunConditionGate` + `RecordingEventPublisher` + `Clock.fixed`; deterministic via a package-private `awaitQuiescence(long)` test seam (joins live Run VTs incl. RESTART victims — `Thread.join` is not banned time access).

### DEFERRED — M7.2a-1 build gate (Nick runs against the commit that lands this diff)
1. Targeted (the `-Werror`/`[exports]`/residency-cycle-sensitive touched modules, fast): `./gradlew :core:event-model:compileJava :core:automation:compileJava :core:persistence:compileJava`
2. Full: `./gradlew check` (touched: event-model, automation [+ first run-lifecycle tests], persistence, testing:integration-tests [cosmetic Javadoc only]). Count pins now **67 const / 37 core / 49 all / 49 category rows / AutomationCompletedEvent 7-comp**.
3. **Reason deferred:** sandbox does not run builds (CLAUDE.md — Nick owns the compile gate). **No `./gradlew` was run in-session.**

### `[REVIEW]` flags (decisions worth PM/Nick eyes)
- **DEVIATION from the instruction's admission sequence — condition-before-mode (honored the locked contract):** the instruction's §"Admission sequence" puts mode enforcement at step 5 and the condition gate in the run body (step 6+, on the VT). That ordering means a `CONDITION_NOT_MET` Run transiently occupies a mode slot (released on terminal), which violates the MODULE_CONTEXT cross-module contract *"Condition evaluation occurs at trigger time, before mode enforcement … does NOT consume a concurrency mode slot"* (and Doc 07 §3.6) in the concurrent case. I implemented **conditions-before-mode**: the gate runs synchronously in `initiateRun` (it is a pure decision; `RunConditionGate` is stubbed in 2a-1) BEFORE mode admission, so a `CONDITION_NOT_MET` Run never enters `activeRuns` / never consumes a slot — even concurrently. The VT runs only the RUNNING (action) phase. All 14 FSM tests pass; **zero 2a-2 rework** (the gate call-site is fixed; 2a-2 only implements the gate impl + row-4 publish). The instruction's "Coder Pushback Welcome" explicitly invited this. *Recommend keeping conditions-before-mode; the literal ordering re-introduces the transient-slot contract violation.*
- **`RunManager` interface gained a 6th method + nested record** (`finalizeZombieRuns(List<ZombieRun>)` + `ZombieRun`). The Technical Spec mandates exposing zombie finalization and the composition root only sees `RunManager` via the assembly seam, so the method must be on the interface. (The gate's "5 methods" describes the pre-change baseline, not a cap.) No new file — both live in the already-MODIFIED `RunManager.java`.
- **QUEUED is admission-equivalent to PARALLEL in 2a-1** (drop `queue_full` at `maxConcurrent`; runs start immediately). True sequential single-flight queue-draining is NOT implemented — only the tested DROP contract is. Deferred (flag for a later slice if strict sequential QUEUED is required; no test exercises sequencing in 2a-1).
- **`RunContext.stateSnapshotPosition` = 0L placeholder in 2a-1** — no `StateSnapshot` is captured (that rides the real `RunConditionGate` in 2a-2). The real trigger-time view position wires in 2a-2.
- **`actionCount`/`commandCount` = 0** in every `automation_completed` (the `ActionExecutor.execute` interface returns `void` — no tally channel exists in 2a-1; 2a-2 carries real tallies).
- **`AutomationEventSerdeTest` + `IntegrationTestHarness` touched though NOT in the instruction's Files table** ([INFO] per "the Files table governs"): the P2 survey (items 18, 20) + Test Requirements direct codec coverage + the cosmetic harness fix there. Both are the natural homes (mirror M7.1).

### `[INFO]`
- New live-VT tracking set in `StandardRunManager` (`liveRunThreads`) — used by `close()` (complete shutdown) and the `awaitQuiescence` test seam so a RESTART victim's terminal publish is observed deterministically. Justified as production shutdown infrastructure, not test-only.
- `triggerIdOf(TriggerDefinition)` switch is duplicated from `StandardTriggerEvaluator` (its copy is private) to map `matchedTriggers` indices → trigger IDs for the row-1 payload. A future refactor could extract a shared package-private helper.

### NEXT WU (refuse-to-close pointer)
- **M7.2a-2 — execution dispatch:** `ActionExecutor` impl (`StandardActionExecutor`) + action events (AMD-92 rows 5/6), real condition evaluation behind `RunConditionGate` + `automation_condition_evaluated` (row 4) + `EvaluatedEntityState`, `CommandDispatchService` + `CommandValidator`, `ConflictDetector` + `automation_conflict_detected` (row 9) + `ConflictEntry`, run-trace assembly (§4.2), and the real trigger-time `StateSnapshot` capture (fills `RunContext.stateSnapshotPosition`) + action/command tallies on `automation_completed`. Then the composition-root wiring of the `RunManager`/subscriber path + the zombie-set log reconstruction ride the lifecycle/app module.

---

## AB-1 + AB-2 — Seam-1 go-live (auth + bind · fail-closed read) — DONE, NOT gate-verified (2026-06-20)

**Coder (Claude Code).** Built **AB-1 (REST auth + bind posture)** and **AB-2 (fail-closed read contract)** per `2026-06-19_AB-1-AB-2-AB-4_Seam-1_go-live_coding-instruction.md`. **AB-4 NOT built** (⛔ AMD-94-gated, HELD — see un-gate condition in the instruction). Handed back **fix-applied / NOT gate-verified** — Nick runs `./gradlew check`. All STOP-on-Mismatch gates re-verified at HEAD `2174fcc`; every gate-table row MATCHED.

**⛔ BLOCKING scope finding — AB-1 WebSocket half NOT built (success criterion #3 unmet).** `api/websocket-api` is a **Phase-2 scaffold only** at HEAD: interfaces + records, NO `WebSocketHandler`/`MessageCodec`/`EventRelay`/`WebSocketLifecycle` impl, NO `app.ws("/ws/v1", …)` Javalin wiring, and `api.ws`'s module-info has zero runtime deps (`requires transitive api.rest` only). There is **no WS upgrade handler to harden** — building WS first-message auth (4403/4408) requires building the entire WS Phase-3 runtime + new module edges (io.javalin, jackson, event-bus, state into api.ws), which is a separate WU, not "wiring existing pieces." The shared `OpaqueTokenStore` + `AuthMiddleware` are ready for it to consume. **Escalation: WS first-message auth is a separate WU; AB-1 REST + AB-2 are fully delivered and separable (as the instruction anticipated).**

**What landed:**
- **AB-1 auth (api.rest, zero new module edges / no build.gradle.kts change):** `StandardAuthMiddleware` (opaque Bearer → SHA-256 lookup, 401/403), `StandardRateLimiter` (per-key token bucket, clock-injected, ConcurrentHashMap.compute), `OpaqueTokenStore` (config-resident `api_tokens`, java.base-only persistence, first-run pairing mint → `initial_api_token` artifact + WARN), `ApiKeyClaims` (enterprise scope/site hook — designed, MVP binary). `RestFilters.installAuth(...)` = catch-all `before(*)` (path canonicalization → 401/403/429, throws to halt the pipeline) + RFC 9457 `ApiException` exception handler.
- **AB-1 bind (lifecycle):** `HomeSynapseConfig` gains 5th component `bindHost` (default loopback `127.0.0.1`). `HomeSynapseCore.start()` Phase 5 now calls `bringUpHttpSurface()` → builds auth, `installAuth` FIRST, `app.start(config.bindHost(), config.httpPort())`. `exposeHttpSurface()` = `requireStarted()` + idempotent bring-up.
- **AB-2 (persistence):** `PayloadDecryptionException` (typed, unchecked → propagates unwrapped through `ReadExecutor`); `SqliteEventStore.decryptStoredPayload` fails the whole read-batch closed, classifying NO_CIPHER_WIRED / MALFORMED_DEK_REF / GCM_AUTH_FAILED (CASE-b) / KEY_ABSENT_OR_DESTROYED (CASE-a); degrade seam designed-not-wired (F4-gated); `DegradedEvent` unchanged.

**Consumer/pin fan-out swept + handled (the AB-3 lesson):** Making `start()` bind HTTP-behind-auth broke every existing unauthenticated HTTP E2E test → updated `HomeSynapseE2eHarness` (`authToken()` reads the pairing artifact; `baseUri()` → `127.0.0.1` to match the IPv4 loopback bind), `EndpointE2eIT`, `CrashRecoveryHttpIT` (+ its direct `HomeSynapseConfig` ctor for the new `bindHost`), `InFlightRequestShutdownIT`. Flipped `LifecycleWiringTest.start_doesNotOpenHttpSurface` → `start_opensHttpSurfaceBehindAuth` and `HomeSynapseCoreTest` C1 test → `opensHttpOnlyBehindAuth` + `httpSurfaceBindsLoopbackOnly`. `Main` HTTP-exposure messaging updated (AB-1 consequence; ctor/cipher stay AB-4-HELD).

### DEFERRED — AB-1 + AB-2 build gate (Nick runs against the commit that lands this diff)
1. Targeted (the `-Werror`/`[exports]`-sensitive touched modules): `./gradlew :api:rest-api:compileJava :api:websocket-api:compileJava :core:persistence:compileJava :lifecycle:lifecycle:compileJava :app:homesynapse-app:compileJava`
2. Full: `./gradlew check` (touched: rest-api, persistence, lifecycle, app; **testing:integration-tests compiles in `check` but its tests are Pi-profile-gated** — run `./gradlew :testing:integration-tests:test -PpiProfile=throttled` to exercise the auth'd E2E/crash/in-flight tests).
3. **Reason deferred:** sandbox does not run builds (CLAUDE.md — Nick owns the compile gate). **No `./gradlew` was run in-session.**

### Watch-outs for the gate
- **Javalin 6.7 API surface** used by `installAuth` (`app.before(Handler)` catch-all, `app.exception(...)`, `app.start(String,int)`, `ctx.header(String)` read / `ctx.header(String,String)` set, `ctx.attribute`, `ctx.contentType`) — verified against in-repo precedent + an adversarial review pass, but unbuilt here. If `app.start(String,int)` differs, that is the one likely surprise.
- **A1.5 static check nuance:** the loopback bind is `app.start(config.bindHost(), config.httpPort())`, NOT a `.host(` call — `grep -rn "\.host(" lifecycle api app` will NOT match; the loopback default is proven by `HomeSynapseCoreTest.opensHttpOnlyBehindAuth`/`httpSurfaceBindsLoopbackOnly` instead.

### `[REVIEW]` flags
- `ApiKeyClaims` — NEW public type in api.rest (the enterprise claims hook; MVP enforcement binary).
- `HomeSynapseConfig.bindHost` — record-shape change (5th component; source-incompatible for direct ctor callers — only `CrashRecoveryHttpIT`, updated).
- `Main` HTTP messaging touched (AB-1 consequence on an otherwise-AB-4 file; ctor + cipher untouched).
- AB-2 `KEY_ABSENT_OR_DESTROYED` message: persistence cannot name the concrete key-file path (config-side) — it names scope/version/position + the config-dir scope-key store + required perms (the literal "path + perms" of A2.1 is satisfied generically).

### Gate round 1 (2026-06-20) — 2 compile fixes applied, declarations/imports only
- **`OpaqueTokenStore.java`** — removed an unused `import java.util.Locale;` (adversarial-review-caught pre-handback; Spotless `removeUnusedImports` would have failed `check`).
- **`SqliteEventStoreDecryptFailClosedTest.java`** — `./gradlew check` failed at `:core:persistence:compileTestJava` (3× "unreported exception `SequenceConflictException`" at the `publishRoot` call sites). Added `throws SequenceConflictException` to the `writeOneEncryptedRow` helper + the three reaching `@Test` methods + the import — matching the sibling `AtRestEncryptionWritePathTest`/`SqlitePersistenceLifecycleTest` pattern. **Declarations only — no assertion or fail-closed-logic change.** (Recurring trap: `publishRoot` declares a checked `SequenceConflictException`; coder-lessons 2026-04-10.) Re-run `./gradlew check` pending.

### NEXT WU (refuse-to-close pointer)
- **Primary: AB-4** (cipher activation via the 6-arg HSC ctor + the 1-byte envelope version tag + F3/F13) — **⛔ HELD until AMD-94 is RATIFIED + folded into Doc 15 §3.4/§5/§6 and the on-disk watermark reads AMD-94.** Re-confirm the gate at Step-0.
- **Also queued (newly surfaced): the WebSocket Phase-3 runtime WU** — `api.ws` first-message auth (4403/4408) + handler/codec/relay/lifecycle + Javalin `app.ws` wiring, consuming the shared `OpaqueTokenStore`. This is what AB-1's success criterion #3 needs and is NOT buildable as part of AB-1.

---

