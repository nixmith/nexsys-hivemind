<!--
file: context/audits/2026-06-14_core-review_B_runtime-automation-M7.md
purpose: Review Session B audit — runtime, integration, automation, API, observability & composition (modules 9–22). The runtime/composition health verdict + the M7-readiness call. Feeds the 2026-06-15 converge.
audience: PM (converge session), Nick
state-type: audit (review-specific, one-shot)
status: COMPLETE
review-baseline: core HEAD 1eddd9a (M6 COMPLETE 4-of-4, M6.3 committed); watermark AMD-93; invariants 163/47; projectionVersion 5; 22 Gradle subprojects. Static read-and-reason review — Cowork cannot run Gradle; sandbox git quarantined; host Read tools authoritative.
-->

# Review Session B — Runtime, Integration, Automation & Composition (M7-forward)

**Stance:** static, read-and-reason audit (no Gradle, no sandbox git). Every finding is tagged **[VERIFIED-FROM-SOURCE]** (provable by reading, cited `file:line`) or **[HYPOTHESIS — NEEDS GATE]** (runtime behavior — carries the exact Claude Code check). Surfacing, not fixing.

---

## Freshness preflight

Ran against the framework baseline. All content pins match source: **watermark AMD-93** (invariants §42–§47 present in `Architecture_Invariants_v1.md`), **invariants 163/47**, **projectionVersion 5** (literal `5` at `HomeSynapseCore.java:336`), **22 Gradle subprojects** (`settings.gradle.kts`), **Doc 07 Locked + AMD-25**, **Doc 12 Locked**. The one known staleness — `PROJECT_SNAPSHOT.md` masthead still showing M6.3 uncommitted at `7c73c91`/`824d6ba` — is pre-cleared by the framework and confirmed by the converge baseline (`1eddd9a`). **Not CONFLICTED. Verdict: PASS-for-review** (a read-only review is not forward work; drift is captured as findings below). Environment realities honoured: no sandbox git; host Read tools used throughout.

---

## Executive summary

**Runtime/composition health verdict.** *The runtime that is built is sound; the runtime is not yet a runnable product.* The M3.x spine that actually exists — `HomeSynapseCore`'s 16-step bootstrap wiring persistence → bus → projection → materialized query → embedded HTTP — is coherent, dependency-ordered, defensively shut down, and genuinely exercised by on-device integration tests that prove what they claim (notably crash recovery). The two ArchUnit boundary rules (`QUERY_SERVICE_READ_ONLY`, `REST_ENDPOINTS_NO_EVENT_PUBLISHING`) hold in the endpoint *code*, not merely in the rule. LTD-11 (no `synchronized`) and the production no-direct-time-access discipline are clean across all of modules 9–22. **But** the apex is unbuilt (`main()` is a one-line stub), the live HTTP surface has **no authentication or rate-limiting** wired, and five of the fourteen modules in scope (automation, integration-runtime, integration-zigbee, websocket-api, observability) are **contract-only scaffolding with no implementation** — so their behavioral invariants are presently aspirational and untestable. The composition is sound *where built*; risk concentrates at the unbuilt apex (auth + lifecycle reconciliation) and the large unbuilt behavioral surfaces M7/M9/M11+ will fill.

**The M7-readiness call: M7 is READY to build.** The automation contract surface (53 well-formed types — properly sealed, defensively copied, LTD-04/LTD-11/time-clean) is sound to build *on*; the live dependency surfaces it consumes (`EventEnvelope`, `CommandIdempotency`, `Expectation`, `StateSnapshot`, `Availability`) all exist and are exported; and the three M7 safety pins **hold in source today**: type-residency (AMD-92-INV-01 — no `RunId`/`RunStatus`/`PendingStatus` in event payloads), the C1-interim pin (zero production `automation_triggered` publish sites), and LTD-11. Entry-gate rows 1–2–5 are closed; rows 3 (energy/erasure interviews) and 4 (M5-C Increment 1) govern *issue*, not code-readiness. **Two fix-firsts** should close before M7.2 builds on them (the cascade-governance documentation drift B-M2, and the placeholder automation event records B-M3). The single **HIGH** below is not on the M7 critical path but is the most important thing for Nick to gate before the app-bootstrap milestone.

**No BLOCKING findings.** Nothing in scope breaks a *shipped* contract (nothing ships — `main()` does not run), and the durability path is proven. The HIGH is a latent security gap that becomes live the moment `main()` is wired.

**Top findings (full tables per-module below):**

| ID | sev | type | one-line | disposition |
|---|---|---|---|---|
| **B-H1** | HIGH | security / forward-risk | Composition root starts an unauthenticated, all-interfaces HTTP server; INV-SE-02's enforcing code (`AuthMiddleware`/`RateLimiter`) is unimplemented; nothing gates auth before app-bootstrap exposes it. | needs-Nick-decision + needs-coding-instruction |
| **B-M1** | MEDIUM | forward-risk / composition | Two disjoint lifecycle abstractions: `SystemLifecycleManager` (Doc-12 interface — unimplemented; owns the systemd health loop/watchdog) is not connected to `HomeSynapseCore` (the real composition root); `main()` bridges neither. | needs-coding-instruction + needs-Nick-decision |
| **B-M2** | MEDIUM | drift | Automation cascade governance still documents the **superseded AMD-04** model (`RunContext` Javadoc + MODULE_CONTEXT); AMD-91 replaced it (`cascadeDepth`→`RunCausalChain` + cycle detection). A Coder building M7.2 from the contract would build the wrong model. | needs-doc-fix |
| **B-M3** | MEDIUM | forward-risk / drift (cross-seam) | On-disk automation event records are minimal placeholders below the F5 spec; `AutomationCompletedEvent`'s status string can't express `INTERRUPTED` (the §3.10 zombie-Run case). | needs-coding-instruction (M7 F5) |
| **B-M4** | MEDIUM | test-weakness | Integration behavioral invariants (AMD-56 routing, AMD-62 schedule) are unpinned — tests assert enum shape / a test-local schedule re-impl, not production behavior (because the code doesn't exist). | needs-coding-instruction (M9) |
| **B-M5** | MEDIUM | forward-risk | websocket-api backpressure is undelivered — 25 files of interface/record scaffold; the documented bounded-buffer/`CLIENT_TOO_SLOW` drop policy has no implementation to bound a slow client. | needs-coding-instruction |
| **B-M6** | MEDIUM | forward-risk | Premature/empty production surface: app `runtimeOnly(:web-ui:dashboard)` packages an empty JAR; `spike/wal-validation` still in-tree with committed `.db` blobs (standing `git rm` advisory). | needs-coding-instruction / needs-Nick-decision |
| **B-M7** | MEDIUM | drift / test-gap | `SystemHealth` Javadoc promises "exactly three tiers" but the constructor doesn't validate it; 0 tests in observability leave record validation unpinned. | needs-coding-instruction / needs-doc-fix |

**Corrected candidate finding (calibrated-honesty note):** a sub-agent flagged that a command-bearing `CapabilityAdded` (integration-api, my scope) might degrade on replay because the `Expectation` codec is unshipped/`@Disabled`. **Source refutes this:** AMD-87's `ExpectationSerializer`/`ExpectationDeserializer` are registered in `PersistenceJacksonModule.java:118-119`, and `EventPayloadCodecTest.capabilityAdded_onOff_roundTrips` (`:333-334`) is an **active** (not `@Disabled`) round-trip test. The M9 capability-publish path is codec-ready. Finding dropped.

---

## Per-module sections (9–22)

### 9 — `integration/integration-api` (`com.homesynapse.integration`) — depth: medium

**Model.** The frozen M4.C adapter contract: `module-info` exports the single package and `requires transitive` platform/event/device/state/persistence/config/java.net.http so an adapter declares one `requires`. **40 production types, all contract (records/enums/sealed interfaces/service interfaces)** — descriptor/context/capability surfaces, the 10-permit `IntegrationLifecycleEvent` hierarchy (AMD-58), `CredentialRotator`/`SecurityServices` (AMD-60), `RequiredService` gating. There is no behavior here to break; the invariants it declares are enforced (or not) by the unwritten M9 supervisor.

**Findings.**

| ID | sev | type | file:line | issue | recommendation | disposition | tag |
|---|---|---|---|---|---|---|---|
| B-9a | MEDIUM | test-weakness | `integration-api/.../BackoffParametersTest.java:36-40` | AMD-62 "schedule is a pure function" is asserted against a `delayForAttempt()` re-implemented *inside the test*, not against any production code (`BackoffParameters` is a 3-field record with no schedule method). A supervisor that computes backoff with an off-by-one exponent or wrong cap order would still pass. | When the M9 supervisor lands, move the schedule into production and have the test call it. | needs-coding-instruction (M9) | [VERIFIED-FROM-SOURCE] |
| B-9b | MEDIUM | drift | `integration-api/MODULE_CONTEXT.md:75,88,92` | Inventory tables describe the pre-M4.C shape — "21 Java files", "Records (9)", `IntegrationDescriptor`…`schemaVersion` (8 fields) — while source has 40 types and `IntegrationDescriptor` has **14 components** incl. `descriptorSchemaVersion` (`IntegrationDescriptor.java:119`). Actively misleading for anyone wiring the frozen contract. | Regenerate the inventory tables from source, or delete in favor of the M4.C section. | needs-doc-fix | [VERIFIED-FROM-SOURCE] |

Contract scorecard (all [VERIFIED-FROM-SOURCE]): LTD-11 clean (zero `synchronized`); LTD-04 holds (typed wrappers; `IEEEAddress` correctly a raw `long` protocol identity); LTD-17 structurally clean; AMD-61 disjointness enforced + tested (`IntegrationDescriptor.java:173-179`); AMD-58 10 permits, new ones observability-only; AMD-60 `rotate` atomicity specified in Javadoc only (no impl to verify — the real LTD-15 secret-handling audit must run on the M9 `CredentialRotator` implementation).

Minor observations (1 theme, rolled): `Instant.now()` in test fixtures (`StubIntegrationContext` heartbeat/snapshot paths) bypasses the threaded `Clock` and is invisible to the arch rule — see cross-cutting B-CC3.

### 10 — `integration/integration-runtime` (`com.homesynapse.integration.runtime`) — depth: medium

**Model.** Supervisor *contract* scaffolding: 6 main files, all interface/record/enum. `IntegrationSupervisor` is an **interface with no implementation anywhere in the repo** — failure isolation, backoff, Kahn dependency ordering, AUTH_FAILED routing, and the health FSM are 100% Javadoc, 0% code (M9 territory). The two enums and two records (`ExceptionClassification`, `HealthDetail`, `IntegrationHealthRecord`, `SlidingWindow`) are real and well-guarded.

**Findings.**

| ID | sev | type | file:line | issue | recommendation | disposition | tag |
|---|---|---|---|---|---|---|---|
| B-10a | MEDIUM | test-weakness | `integration-runtime/.../ExceptionClassificationTest.java` | AMD-56-INV-01 (AUTH_FAILED never routes to transient backoff) — the *reason the enum value exists* — is untested; the strongest assertion is `AUTH_FAILED.ordinal()==3`. A mutant routing AUTH_FAILED to transient-retry passes every test. (Root cause: routing code is unwritten — see B-CC2.) | Add a supervisor classification test at M9. | needs-coding-instruction (M9) | [VERIFIED-FROM-SOURCE] |
| B-10b | LOW→rolled | drift | `integration-runtime/MODULE_CONTEXT.md:48,52,69` | Inventory tables self-contradict the changelog (say 1 enum / 3 values / 13 fields; actual 2 / 4 / 14 incl. `HealthDetail`). | Regenerate or delete tables. | needs-doc-fix | [VERIFIED-FROM-SOURCE] |

### 11 — `integration/integration-zigbee` (`com.homesynapse.integration.zigbee`) — depth: light–medium

**Model.** The M14 adapter. `module-info` `requires transitive com.homesynapse.integration` only (LTD-17 structurally clean). **38 main files — every one an interface, enum, or record; zero concrete classes** (`grep "public class"` empty; no TODO/`UnsupportedOperationException` markers). The entire protocol stack (ZNP/EZSP transport, interview pipeline, cluster handlers, Tuya/Xiaomi codecs, availability tracker) is pure type scaffolding. **Real-hardware exposure: none** — nothing opens a serial port, decodes a byte, or talks to a coordinator. This is well-formed *type design*, not stubs and not working code. Wired-but-dormant: `app` declares `implementation(:integration-zigbee)` + `requires` it, but `Main` references nothing Zigbee.

**Findings.** No correctness findings (no behavior to audit). Records that exist are correct: `ZnpFrame`/`ZclFrame` double-defensive-copy `byte[]`; `DeviceProfile` conditional `copyOf` avoids `copyOf(null)`; `IEEEAddress` hex codec is boundary-only. **0 tests for 38 files** is consistent with scaffold status; the LTD-11/concurrency/hardware audit must be redone once the M14 transport classes land. Minor (rolled): MODULE_CONTEXT says "39 Java files" vs actual 38.

### 12 — `core/automation` (`com.homesynapse.automation`) — depth: **DEEP** (the M7 target)

**Model.** The TCA (Trigger-Condition-Action) engine, **Phase-2 interface-only**: 53 public types + `package-info` = 54 files, **0 tests, 0 implementation**. Verified inventory (re-derived from source, matches the corrected MODULE_CONTEXT): 5 enums + 1 ULID wrapper (`RunId`) + 4 sealed roots + 30 permits (6 selectors / 9 triggers / 7 conditions / 8 actions) + 4 data records + 9 service interfaces. `module-info` `requires transitive` platform/event/device/state + `requires value`; **no `requires config`/`event.bus`** (FIX-07 holds — both re-added in M7). The entire implementation (trigger evaluation, run manager, cascade governance, command dispatch, the 3 subscribers) is M7 work.

This is the headline. The defining question — *is M7 ready to build?* — resolves to **yes**, on three legs, each VERIFIED in source:

- **The contract surface is sound to build on.** Sealing is total (`Selector` permits 6, `TriggerDefinition` permits 9 — verified); collections defensively copied (`RunContext.java:78-79` `List.copyOf`/`Map.copyOf`; `CommandAction.java:51`); identifiers typed (`RunId` wraps `Ulid`, LTD-04); compact constructors validate non-null. Zero `synchronized`, zero direct-time-access, zero publish sites in the whole module.
- **The live surfaces it consumes exist and are exported.** `state-store` exports `StateSnapshot` + `Availability`; `device-model` has `Expectation`; `event-model` has `EventEnvelope` + `EventId` + `CommandIdempotency`. Every `requires transitive` edge resolves to a real type.
- **The M7 safety pins hold today.** Type-residency (AMD-92-INV-01): the two existing automation event records carry only flattened scalars — `AutomationTriggeredEvent(String,String)`, `AutomationCompletedEvent(String,String,long)` — no `RunId`/`RunStatus`/`PendingStatus`. The C1-interim pin (no production `automation_triggered` publish before M7.2): **zero** production publish sites; the sole non-test reference to the event types outside event-model is a category-lookup-table entry (`EventCategoryMapping.java`), not a publish — so AMD-92-INV-02 is satisfied vacuously.

The gap is exactly what M7 exists to do: **the ratified AMD-88..93 contract deltas are not yet in code** (all verified ABSENT: `RunCausalChain`, `SemanticTagSelector`, `includedRoles`, `triggerId`, `ConfirmationPolicy`, the new Calendar/Reachability/Manual/Repeat/InvokeAutomation permits). Two of those deltas are breaking (F2 selector `includedRoles`+`SemanticTagSelector`; F4 `RunContext.cascadeDepth:int`→`causalChain:RunCausalChain`) and are M7.1's first construction step + a construction-site sweep. That is the definition of M7, not a defect — but it interacts with two documentation hazards (B-M2, B-M3) that should close first.

**Findings.**

| ID | sev | type | file:line | issue | recommendation | disposition | tag |
|---|---|---|---|---|---|---|---|
| B-12a (=B-M2) | MEDIUM | drift | `RunContext.java:30-36` + `automation/MODULE_CONTEXT.md:200,316` | Cascade governance is documented as the **superseded AMD-04** model — `cascadeDepth` (int), `max_cascade_depth` 8/1–32, `cascade_depth_exceeded`. AMD-91 superseded AMD-04 (F4: `cascadeDepth`→`RunCausalChain`; same-automation cycle detection with a *distinct* diagnostic). A Coder implementing M7.2 cascade governance from the contract/MODULE_CONTEXT (not the charter) builds the depth-only model and misses cycle detection + `RunCausalChain`. | Update the `RunContext` Javadoc + MODULE_CONTEXT to cite AMD-91 and flag the F4 reshape as M7.2 work; the MODULE_CONTEXT is "current" w.r.t. the frozen code but silent on the ratified AMD-88..93 deltas. | needs-doc-fix (before M7.2) | [VERIFIED-FROM-SOURCE] |
| B-12b (=B-M3) | MEDIUM | forward-risk / drift (cross-seam) | `AutomationTriggeredEvent.java:16-19`; `AutomationCompletedEvent.java:31-35`; cf. `RunStatus.java:66-78` | The on-disk automation event records are minimal placeholders below the F5 spec: `AutomationTriggeredEvent` carries only `triggerType`/`triggerDetail` (none of F5's `matched_triggers`/`resolved_targets`/`definition_hash`); `AutomationCompletedEvent`'s status string {`success`,`failure`,`aborted`} cannot express `RunStatus.INTERRUPTED` (the §3.10 zombie-Run finalization terminal) or `CONDITION_NOT_MET`. A consumer relying on `automation_completed` today gets a 3-value status. | M7's F5 slice must widen these (field-additions per AMD-88-INV-01) before any production publish; record the INTERRUPTED/CONDITION_NOT_MET status vocabulary. Cross-seam: the records live in `event-model` (Session A). | needs-coding-instruction (M7 F5) + converge seam | [VERIFIED-FROM-SOURCE] |

Minor observations (rolled): the AMD-88-INV-02 `triggerId` requirement (stable trigger identity on user-facing surfaces) has no field yet on any `TriggerDefinition` permit — an F1 addition, expected.

### 13 — `api/rest-api` (`com.homesynapse.api.rest`) — depth: medium

**Model.** Stateless HTTP translation layer (Javalin). 38 main + 8 test. The M3.6e runtime surface is **real and wired into the live server**: `ReadinessFilter`, `RestFilters`, and 5 `Handler` impls (entity list/get/state + DLQ/projection admin). The historical Phase-2 vocabulary — `AuthMiddleware`, `RateLimiter`, `ProblemDetailMapper`, `RestApiServer`, `ETagProvider`, `PaginationCodec` — are **interfaces with zero implementations**.

**ArchUnit boundary verification (the framework asked for code, not rule).** Both rules are defined in `app/.../HomeSynapseArchRules.java` and wired as live `@ArchTest`s, and **hold in the endpoint source**: `QUERY_SERVICE_READ_ONLY` (`:262-268`) — zero `com.homesynapse.persistence` references in rest-api; every state access is read-only (`queryService.getState`/`getSnapshot`). `REST_ENDPOINTS_NO_EVENT_PUBLISHING` (`:290-296`) — no `EventPublisher` import or publish/append/write call in any endpoint; the only bus touch is `DlqStatusEndpoint` calling `bus.subscribers()` (read-only); belt-and-suspenders, rest-api's `module-info` doesn't even `requires com.homesynapse.event`. [VERIFIED-FROM-SOURCE]

**Findings.** The HIGH no-auth finding's *root cause* is in lifecycle (B-H1); rest-api's own endpoint code is correct. Input validation is solid and [VERIFIED]: `Ulid.parse`→400 on bad id (`GetEntityEndpoint.java:104-110`); `limit` clamped to [1,100] (`ListEntitiesEndpoint.java:165-179`); `sort` whitelisted; RFC 9457 problem bodies centralized; 503 readiness gate fail-closed (`ReadinessFilter.java:113-124`). The 8 tests are genuinely behavioral (mutation-resistant — e.g. `ReadinessFilterTest.readsModeOnEveryCall` kills a cached-mode mutant), with an honest disclosed gap: they drive a fake query service + recording context, so the adapter-wiring and missing-auth paths are not exercised end-to-end (that's the lifecycle ITs). LTD-11/LTD-15/LTD-04/time-access all clean. Minor (rolled): MODULE_CONTEXT `SubscriberSnapshot` field-count drift (closed in M3.7; doc stale).

### 14 — `api/websocket-api` (`com.homesynapse.api.ws`) — depth: light–medium

**Model.** 25 main files, **0 tests — 100% scaffold.** All files are record/enum/sealed-interface/service-interface; **no concrete class, no implementation logic.** `module-info` exports the flat package, `requires transitive com.homesynapse.api.rest` only — no event-bus, no Jackson, confirming nothing is implemented.

**Findings.**

| ID | sev | type | file:line | issue | recommendation | disposition | tag |
|---|---|---|---|---|---|---|---|
| B-14a (=B-M5) | MEDIUM | forward-risk | `ClientConnection.java` (Javadoc); whole module | Backpressure to slow clients is **undelivered**. The contract exists only as prose ("send buffer exceeds `hard_ceiling_kb` default 128 KB → close with `CLIENT_TOO_SLOW`"), but `ClientConnection` is an interface with no implementing class and no queue/buffer field anywhere in the module. The question "does a slow WS client threaten heap/the bus?" is unanswerable from code because the bound does not exist yet. | Treat WS backpressure as NOT DELIVERED. When implemented, the bounded-buffer + drop policy must ship with slow-consumer tests. Note: M7's `RunManager` live-trace streaming (a planned WS consumer) depends on this. | needs-coding-instruction | [VERIFIED-FROM-SOURCE] |

Minor (rolled): MODULE_CONTEXT header names the old package `…api.websocket` vs source `…api.ws`.

### 15 — `observability/observability` (`com.homesynapse.observability`) — depth: medium

**Model.** The diagnostic backbone, **pure scaffold**: 6 service interfaces (`HealthAggregator`, `HealthContributor`, `TraceQueryService`, `MetricsRegistry`, `MetricsStreamBridge`, `LogLevelController`) + ~12 validated records/enums; `requires transitive com.homesynapse.event`. **No implementation class; the only executable logic is record compact-constructor validation. 0 tests.**

Two framework questions answered from source: **(a) `IntegrityService` (the "M12 seam") does not exist anywhere in the repo** — `grep` returns nothing, not even a placeholder or comment. **(b) MDC has zero usage repo-wide** — so the R-ε "MDC on virtual threads" hazard has no current code surface (it becomes live when observability is built in M11/M12; see research avenues).

**Findings.**

| ID | sev | type | file:line | issue | recommendation | disposition | tag |
|---|---|---|---|---|---|---|---|
| B-15a (=B-M7) | MEDIUM | drift / test-gap | `SystemHealth.java:70-100` | Javadoc states `tiers` is "a non-empty map with exactly three entries," but the compact constructor only null-checks + `Map.copyOf` — a `SystemHealth` with 0 or 2 tiers constructs cleanly, violating the documented invariant the REST/UI health surface will rely on. 0 tests leave this and ~11 other records' validation unpinned. | Add `tiers.size()==3`/key-completeness validation (or soften the Javadoc) + record-validation tests. | needs-coding-instruction / needs-doc-fix | [VERIFIED-FROM-SOURCE] |

### 16 — `lifecycle/lifecycle` (`com.homesynapse.lifecycle`) — depth: **DEEP** (the composition root)

**Model.** Process-level orchestration. 12 main + 3 test. `HomeSynapseCore` (626 lines) is the real M3.6 composition root — single owner of persistence, bus, projection, scheduler, rate-limit, health-check, query-service, and the embedded Javalin server, constructed in a fixed 16-step sequence on `start()` and torn down in reverse on `stop()`. `module-info` notably does **not** `requires com.homesynapse.automation` — the automation engine is not wired (expected, M7).

The bootstrap is sound where built: dependency-ordered (persistence→bus→projection→query→HTTP, `:241-435`); the event-type manifest aggregation (`:245-250`) feeds the registry; shutdown is correct and crash-safe — `stop()` (reverse order + WAL flush) and `abandon()` (crash-sim, no durability) are mutually excluded via the `abandoned`/`started` flags (`:477,538`), matching the proven `CrashRecoveryIT`. LTD-11 clean (no real `synchronized` on any code path; the lone textual hit is a Javadoc word). The M6.3 cipher seam is correctly wired: `HomeSynapseCore` holds `payloadCipher` and forwards it into `PersistenceFactory.start(..., payloadCipher)` (`:256-258`) — but it is **dormant** (nothing in production constructs `HomeSynapseCore`; see B-H1/B-M1).

**Findings.**

| ID | sev | type | file:line | issue | recommendation | disposition | tag |
|---|---|---|---|---|---|---|---|
| **B-H1** | **HIGH** | security / forward-risk | `HomeSynapseCore.java:408-435` (+ `:424-432`); `RestFilters` (no auth method); `AuthMiddleware`/`RateLimiter` (zero impls) | The composition root creates the Javalin app, installs **only** `RestFilters.installReadinessGate` as a `before` filter (`:412`), registers entity + admin endpoints, and calls `app.start(config.httpPort())` (`:434`, default 7070, no `.host()` restriction). **No authentication, no rate-limiting.** The `/internal/*` DLQ + projection endpoints are deliberately *outside* even the readiness gate (`:424-432`). INV-SE-02 ("authentication mandatory on every external interface; no local-trust exception") has no enforcing implementation. Not live today only because `main()` is a stub — it becomes a live unauthenticated surface the moment app-bootstrap wires `main()`. | Gate the app-bootstrap milestone on an `AuthMiddleware` `before("/api/*")` + `RateLimiter`; decide bind-address posture (loopback-by-default vs all-interfaces). Confirm whether auth-before-network-exposure is a tracked milestone — it currently is not. | needs-Nick-decision + needs-coding-instruction | [VERIFIED-FROM-SOURCE] (server wiring); the "all-interfaces" exposure is Javalin's documented default host when none is set — **[HYPOTHESIS — NEEDS GATE]** confirm with `grep -rn "\.host(" lifecycle api` (expect none) + a bound-socket check that `:7070` answers on a non-loopback address. |
| **B-M1** | MEDIUM | forward-risk / composition | `SystemLifecycleManager.java:30` (interface, no impl); `HomeSynapseCore.java` (concrete, test-only construction); `Main.java:27-29` (stub) | Two parallel, **disjoint** lifecycle abstractions. `SystemLifecycleManager` — the Doc-12 orchestrator the `module-info` names as the `main()` entry point, owning the 6 init phases, the runtime **health loop** (Doc 12 §3.10) and the **systemd watchdog/shutdown-hook** — is an *unimplemented interface that never references* `HomeSynapseCore`, the real composition root. `HomeSynapseCore` is constructed only in tests. So the systemd liveness protocol (platform-systemd's real `SystemdHealthReporter`) has no path to the running system, and the documented startup model and the actual wiring are unreconciled. This is the framework's "a missed manifest/wiring no test pins" hazard, concretely. | The app-bootstrap milestone must reconcile: either `main()` constructs `HomeSynapseCore` directly (and the 6-phase/health-loop model is retired or re-homed), or `SystemLifecycleManager` is implemented to wrap `HomeSynapseCore`. Decide explicitly; pin the health-loop/watchdog wiring with a test. | needs-coding-instruction + needs-Nick-decision | [VERIFIED-FROM-SOURCE] |

Forward-readiness note for M7 (not a defect): `HomeSynapseCore.start()` has **no automation steps**. M7.1 must add the automation registry + the **three subscribers** (`automation_engine`, `command_dispatch_service`, `pending_command_ledger`), fold the automation event manifest into the step-1 aggregation (`:245-250` — the AMD-92-INV-02 forcing point), and order automation's subscribe after the state store is caught up. The step-1 manifest aggregation and the subscriber wiring are precisely the latent-defect-prone sites; pin them with the consumer/pin survey. Readiness semantics (`mode()`, `:608-632`) currently key on the projection subscriber only and may need to account for automation subscribers.

### 17 — `app/homesynapse-app` (`com.homesynapse.app`) — depth: medium

**Model.** Assembly apex + process entry point. 3 main + 3 test; `requires` 15 subsystem modules; no `exports`. **`main()` is a 1-line stub** (`Main.java:27-29`: `System.out.println("HomeSynapse Core not yet implemented")`) — no runtime construction, no shutdown hook, no socket. The real code is the package-private `payloadCipher(...)` factory (`:63-81`) — a genuine adapter constructing `ScopeKeyManager.create(...)` and delegating `encrypt` to the M6.3 counter-nonce `encryptPayload` (`:70`) and `decrypt` to `keyManager.decrypt` (`:78`); round-trip + scope-isolation + monotonic-nonce tested (`PayloadCipherBridgeTest`). `ExitCode` is a complete real enum.

**Findings.** Reserved-vs-wired is honestly marked: WIRED = the cipher adapter (real, tested) + `ExitCode`; UN-BUILT = `main()` runtime construction (the app-bootstrap milestone — `:50-54` Javadoc states `main()` does not yet construct the runtime). The substantive finding is the composition-root reconciliation (B-M1) and the no-auth gate (B-H1), both of which converge on this unbuilt `main()`. No module-local defects. Minor (rolled): the `NO_DIRECT_TIME_ACCESS` `platform..` whitelist covers a `UlidFactory.generate()` convenience the Javadoc itself flags for Phase-3 removal.

### 18 — `platform/platform-systemd` (`com.homesynapse.platform.systemd`) — depth: light

**Model.** Deployment-tier impls of `PlatformPaths` + `HealthReporter`. 5 main + 4 test. `LinuxSystemPaths`/`LocalPaths` are fully real and tested. `SystemdHealthReporter` is real sd_notify *protocol* logic (once-only READY, ReentrantLock serialization, send-and-forget) behind a `NotifyTransport` seam; the production `UnixDatagramTransport` **fails at construction** with a clear `IllegalStateException` pointing to M13 on JDK 21 (OR-M13-SDNOTIFY) — an honest deferral, not a silent no-op.

**Findings.**

| ID | sev | type | file:line | issue | recommendation | disposition | tag |
|---|---|---|---|---|---|---|---|
| B-18a | MEDIUM | test-gap | `SystemdHealthReporter.java:154-167` | The production 1-arg ctor path (`UnixDatagramTransport` → reframed `IllegalStateException`) has zero test coverage; all 11 tests inject the seam. No test asserts the real ctor throws the M13-deferral exception on JDK 21, nor exercises the `@`→NUL abstract-socket mapping (`:182-184`). | Add a test asserting `new SystemdHealthReporter("/run/x.sock")` throws `IllegalStateException` (M13) on this JDK; unit-test the NUL mapping. | needs-coding-instruction | [VERIFIED-FROM-SOURCE] |

Minor (rolled): `clearDirectoryContents` is byte-identical duplicated across `LinuxSystemPaths`/`LocalPaths` (DRY; both correct + tested).

### 19 — `testing/test-support` — depth: light–medium

**Model.** Real, high-quality test infrastructure: 13 main + 1 test, no `module-info` (consumed via `testImplementation`). The load-bearing doubles — `TestClock` (controllable `Clock`), `SynchronousEventBus` (inline dispatch mirroring the production pull/notify split), `TestSubscriber` (pull→filter→checkpoint with failure injection), `EventCollector` (lock-free, LTD-11) — faithfully mirror production contracts.

**Findings.** No findings. The "CountingPayloadCipher-style fidelity" question resolves well: there is no cipher double *in test-support*; the canonical one lives in `core/persistence` (Session A) — `CountingPayloadCipher` is **faithful, not an identity no-op**: real AES-256-GCM (`Cipher.ENCRYPT/DECRYPT_MODE`, `"AES/GCM/NoPadding"`), distinct DEK per (scope,version), counter nonces flushed to disk *before* return (models OR-M6-NONCE no-reuse-across-restart). A decrypt-mismatch regression would throw, not silently pass. Minor (rolled): `TestSubscriber` re-collects in-page events on retry after an injected failure — faithful at-least-once semantics, noted as a subtlety.

### 20 — `testing/integration-tests` — depth: medium

**Model.** The on-device ITs: 0 main, 12 test files; `-PpiProfile`-gated (excluded from default `check`, `build.gradle.kts:22`). All exercise the genuine production stack (file-backed SQLite+WAL + `InProcessEventBus` + `StateProjection` + real Jetty/HTTP).

**Do the ITs earn their keep? Yes — the headline risk (a crash-recovery IT that passes when recovery is broken) is absent.** [all VERIFIED-FROM-SOURCE]
- `CrashRecoveryIT` — real kill: `abandonForCrashSimulation()` makes harness `close()` early-return and **never** call `lifecycle.stop()` (no WAL checkpoint, no executor shutdown — a faithful `kill -9`); recovery asserted on a fresh harness against the same DB with **state equality** — `hasSize(5000)` + a per-`globalPosition` `[1,5000]` delivery loop. A lost-events regression fails it.
- `CrashRecoveryHttpIT` — the AMD-45 `replay-from-zero` case (frozen clock + 5 events so no checkpoint can fire) is the strongest mutation test in the suite; asserts 5 entities over real HTTP post-restart.
- `HeapBudgetIT` (≤256 MB real bound under `-Xmx256m`), `BurstLoadIT` (ingest <5 s, all 500 delivered, DLQ/crash zero, checkpoint converges), `Pi4SustainedLoadIT` (lag ≤50, WAL ≤6 MB LTD-03, heap ≤200 MB), `Pi4D1SpikeIT` (`finalLag` drains to exactly zero) — all assert genuine invariants.

**Findings.** Two minor (rolled to LOW): `EndpointE2eIT` DLQ test asserts only the empty-DLQ *shape* (self-documented deferral — a populated `oldestParkedAt` path is unexercised); `InFlightRequestShutdownIT` asserts only "not a hang" (`instanceof RuntimeException` catch-all — deliberately loose pending `RestApiLifecycle.stop(drainSeconds)`). Both are honestly disclosed Phase-3 gaps, not false proofs. Direct-time-access: 10 hits (all intentional — WAL `ingest_time` microsecond monotonicity needs real wall-clock; `System.nanoTime()` poll deadlines) — see B-CC3.

### 21 — `web-ui/dashboard` — depth: light

**Model / verdict.** Confirmed empty scaffold: only `MODULE_CONTEXT.md` + a 3-line `build.gradle.kts` (`base` plugin, no deps); `src/` recurses to an empty `main/resources/static`. **No source, no assets.** Sole premature surface is the `app` `runtimeOnly` wiring → see B-M6.

### 22 — `spike/wal-validation` — depth: light

**Model / verdict.** Confirmed throwaway spike: 11 main files, no `module-info`, no MODULE_CONTEXT; the only repo reference is `settings.gradle.kts:74` under a "not part of production build" banner. **No production/app/lifecycle module depends on it** (`grep` for `spike.wal`/`com.homesynapse.spike` outside `spike/` is empty). Still in-tree against the standing `git rm` advisory, **with committed binary `.db` run artifacts + `kill-driver.sh`** → see B-M6. Uses `Instant.now()` directly (acceptable in a throwaway; moot once removed).

---

## Cross-cutting findings

- **B-CC1 (=B-H1+B-M1) — The runtime apex is unbuilt and unauthenticated.** The real composition root (`HomeSynapseCore`) is constructed only in tests; `main()` is a stub; the Doc-12 `SystemLifecycleManager` (health loop + systemd watchdog) is an unimplemented interface disjoint from it; and the HTTP surface it stands up has no auth/rate-limit and binds the default host. The app-bootstrap milestone is where all of this converges — and it is where INV-SE-02 must be satisfied. **This is the single most important thing to gate.** Sites: modules 16, 17, 13.
- **B-CC2 — Five modules are contract-only scaffolding; their behavioral invariants are aspirational.** automation (M7), integration-runtime + integration-zigbee (M9/M14), websocket-api, observability have rich type contracts and **no implementation** (and mostly **0 tests**). Consequence: a static review can verify their *contracts* but not their *behavior*; the LTD-11-in-the-supervisor / backpressure / AMD-56/61/62 routing / cascade-safety audits are deferred until the code lands. This is the honest health framing, not a defect — but it is why the per-module concurrency/crypto verdicts below are "contract correct, behavior unverifiable." Re-audit each as it is implemented.
- **B-CC3 — Test-side direct-time-access is invisible to the gate (LOW).** `NO_DIRECT_TIME_ACCESS` only scans `com.homesynapse.app`'s test classpath (corrected 2026-06-13), so non-app test/fixture code can leak wall-clock undetected. Confirmed sites: `integration-api` fixtures (`StubIntegrationContext` heartbeat/snapshot `Instant.now()`), `integration-tests` (10 hits, mostly intentional pacing/WAL-monotonicity), `spike` (moot). All test-side; none is a production violation. Mitigation option: an ArchUnit variant that scans IT/fixture modules with an allowlist for the legitimate pacing uses.
- **B-CC4 — MODULE_CONTEXT drift is systemic (mostly LOW; one MEDIUM).** integration-api, integration-runtime, automation, rest-api, websocket-api, zigbee all carry inventory/field/package drift vs source. The only materially-misleading one is automation's superseded-AMD-04 cascade model (B-M2 / MEDIUM) because it would mislead an M7.2 implementer; the rest are count/name nits. Theme: the M4.C/M5/M6 contract growth outran several MODULE_CONTEXT inventory tables.

---

## Coverage ledger (modules 9–22)

| # | Module | Depth | Findings (excl. rolled LOW/INFO) | Notes |
|---|---|---|---|---|
| 9 | integration-api | medium | B-9a (MED), B-9b (MED) | 14/40 types read line-by-line (security/descriptor/context/capability/lifecycle core) + all key tests; remainder by file-kind census |
| 10 | integration-runtime | medium | B-10a (MED) | all 6 main files read |
| 11 | integration-zigbee | light–medium | — (clean type design; 0 impl) | 5/38 key records read; remainder census-verified as interface/record/enum |
| 12 | **automation** | **DEEP** | B-12a/B-M2 (MED), B-12b/B-M3 (MED) | module-info + build + 9 load-bearing types read; AMD-88..93 deltas, type-residency, C1-pin all verified in source |
| 13 | rest-api | medium | (HIGH root-caused to B-H1) | ArchUnit rules verified in code; input-validation + all 8 tests read |
| 14 | websocket-api | light–medium | B-14a/B-M5 (MED) | 5 key types read; module confirmed 100% scaffold |
| 15 | observability | medium | B-15a/B-M7 (MED) | all 18 type files read; IntegrityService + MDC confirmed absent repo-wide |
| 16 | **lifecycle** | **DEEP** | B-H1 (HIGH), B-M1 (MED) | `HomeSynapseCore` (626 lines) + `SystemLifecycleManager` + module-info + build read in full |
| 17 | app | medium | (folds into B-H1/B-M1) | `Main.java` read in full; cipher adapter + stub `main()` verified |
| 18 | platform-systemd | light | B-18a (MED) | all 5 main + 4 test read |
| 19 | test-support | light–medium | — (doubles faithful) | key doubles + `CountingPayloadCipher` (persistence) read |
| 20 | integration-tests | medium | — (2 minor rolled) | all 6 load-bearing ITs read; crash-recovery proof verified |
| 21 | web-ui/dashboard | light | (folds into B-M6) | confirmed empty stub |
| 22 | spike/wal-validation | light | (folds into B-M6) | confirmed no production dependency |

Every module 9–22 earned a model + contract + test-strength pass. No module was skipped. Breadth was gathered by sub-agents and **all load-bearing claims were re-verified against source by the PM** before tagging (one candidate finding — the `CapabilityAdded`/`Expectation`-codec degrade — was refuted on verification and dropped).

---

## Research avenues surfaced (M7-forward first; the converge consolidates)

**M7-forward (highest priority):**
1. **The composition-root automation wiring is the M7 latent-defect surface (reinforces the framework's "missed manifest" hazard).** When M7.1 adds the 3 automation subscribers + the automation event manifest to `HomeSynapseCore.start()` step 1, the AMD-92-INV-02 "full manifest before first publish" pin and the subscriber start-ordering (after state-store catch-up) are exactly the things no unit test pins. *Avenue:* the M7.1 instruction should carry a composition-root manifest-survey + a lifecycle wiring test, not just module-local tests. Route: CORE (instruction-embedded), not a research dispatch.
2. **Trigger-evaluation cost on the Pi-4 floor is still unmeasured (R14-B RQ-storm; merged-disposition REC-157).** automation has no implementation, so the O(1) trigger-index claim (Doc 07 §3.4) and the storm-threshold behavior are untested. *Avenue:* the M7.1 storm benchmark harness (already a charter obligation) is the empirical gate — confirm it lands as an investigation trigger.
3. **The F5 automation event-record expansion vs the placeholder records (B-M3) is a cross-seam design beat.** Widening `AutomationCompletedEvent` to express `INTERRUPTED`/`CONDITION_NOT_MET` while honoring type-residency (flatten, AMD-92-INV-01) and AMD-52 codec discipline is a concrete M7 F5 design question that spans event-model (A) and automation (B). Route: converge seam + M7 F5 instruction.
4. **Cascade governance is changing model (AMD-04→AMD-91) and the docs still describe the old one (B-M2).** *Avenue:* before M7.2, the `RunCausalChain` shape + the deterministic cycle-suppression contract (AMD-91-INV-01: causal-chain-and-config-only, no windowed state) needs a crisp interface spec so the implementer doesn't reach for the windowed Doc 01 §4.5 correlation map. Route: CORE (AMD-correction/interface-spec, not research).

**Runtime/composition (M9+ / app-bootstrap):**
5. **Auth + bind-posture before network exposure (B-H1).** The auth model (`AuthMiddleware`/`RateLimiter` are unbuilt) and the bind-address default need a decision and a milestone gate before app-bootstrap. Route: needs-Nick-decision; likely a small security milestone.
6. **The lifecycle reconciliation (B-M1):** `SystemLifecycleManager` (Doc-12 phases + health loop + systemd watchdog) vs `HomeSynapseCore`. Route: app-bootstrap design.
7. **R-ε (MDC on virtual threads) is currently moot but forward-relevant.** No MDC surface exists yet; when observability (M11/M12) builds structured trace context, the Java-21 MDC-copy-into-child mechanism (B-211 ruling; Scoped Values trajectory-only) must be designed in from the start since VTs don't inherit ThreadLocals across spawns. Mark **refined** (the vector is real but has no code surface today). Route: DOCS design-research at the observability milestone.
8. **WS backpressure design (B-M5)** — the bounded-buffer/`CLIENT_TOO_SLOW` policy is unbuilt; M7's live-trace streaming will be its first real consumer. Route: CORE at the WS milestone.

**Reserved-but-unbuilt register (B-side slice; a consumer must not assume these work):** automation engine (entire implementation — M7); `IntegrationSupervisor` + the Zigbee stack (M9/M14); websocket-api (all behavior); observability (all behavior); `IntegrityService` (M12 tamper-evidence — *does not exist even as a seam*); `SystemLifecycleManager` (unimplemented); `main()` runtime construction (app-bootstrap); sd_notify real transport (M13, fails-closed at construction); `AuthMiddleware`/`RateLimiter` (unbuilt — see B-H1). The crypto reserved set (chain-hash activation, Ed25519, crypto-shred, OR-M6-NONCE restore half, the `identity` scope) is Session A's to catalog.

---

## Commit message (handed to Nick; `!`-free)

```
docs(audit): add Review Session B audit — runtime/automation/composition (modules 9-22)

Static read-and-reason audit feeding the 2026-06-15 converge. Baseline core 1eddd9a
(M6 4-of-4), watermark AMD-93, projectionVersion 5, 22 subprojects. Preflight PASS-for-review.

Health verdict: the M3.x runtime that is built is sound (16-step bootstrap, crash-safe
shutdown, ArchUnit REST boundaries hold in code, ITs genuinely prove recovery); the system
is not yet a runnable product (main() is a stub; HTTP surface has no auth wired; automation/
integration-runtime/zigbee/websocket/observability are contract-only scaffolding).

M7-readiness call: READY. The 53-type automation contract surface is sound to build on, the
live event/device/state surfaces it consumes exist, and the M7 safety pins hold in source
(type-residency AMD-92-INV-01, C1-interim no-publish, LTD-11). Two fix-firsts before M7.2:
the cascade-governance doc drift (AMD-04 vs AMD-91) and the placeholder automation event
records. Entry-gate rows 3 (interviews) + 4 (M5-C) still govern issue.

1 HIGH (no auth on the composition-root HTTP surface; INV-SE-02 enforcing code unimplemented;
gate before app-bootstrap), 7 MEDIUM, no BLOCKING. One candidate finding (CapabilityAdded/
Expectation-codec degrade) refuted on source-verification and dropped.

File: context/audits/2026-06-14_core-review_B_runtime-automation-M7.md
```
