# HomeSynapse V1 — Master Release Plan

**258-Day Execution Roadmap | March 13 – November 25, 2026**

NexSys Technologies | Prepared by the Hivemind | Version 1.0 | 2026-03-13

CONFIDENTIAL — NexSys Internal

---

## Phase 3 Progress Annotation (added 2026-04-11)

**Do not rewrite the 37-week plan below.** It is the original strategic baseline and is preserved as a reference point. The plan's weekly cadence was built around expected velocity. Actual velocity has run substantially ahead on the interface-spec axis and is converging on the plan's schedule for the persistence subsystem implementation.

**Actuals vs plan (through 2026-05-20):**

| Plan | Planned Window | Actual |
|---|---|---|
| P1 Interface Specification (plan Weeks 1–10, Mar 16 – May 24) | 10 weeks | Finished in 7 days (Mar 14–20). ~9 weeks ahead. All 16 subsystem modules interface-specified. |
| Week 11 — SQLite WAL spike | Week of May 25 | SQLite WAL spike validation 2026-04-02 (commit `d48df13`). ~7 weeks ahead. Result: PASSED, WAL mode viable on aarch64. |
| Test-first prep (not an explicit plan item) | — | 2026-03-27 through 2026-04-09: event-model test suite, InMemoryEventStore implementation (27/27 contract tests pass), test fixtures for event-bus/device-model/state-store/integration-api/configuration, EventBusContractTest + InMemoryEventBus, WriteCoordinatorContractTest + InMemoryWriteCoordinator, EntityState/StateSnapshot/Availability/StateQueryService tests, AMD-33 (DomainEvent permanently non-sealed). |
| Week 12 — Event Store (persistence) | Week of Jun 1 | **Landed Apr 10–11** as milestones M2.1 through M2.5: `@EventType` annotation, migration framework + V001 schema, DatabaseExecutor, serialization infrastructure, SqliteEventStore. ~7 weeks ahead of plan. Commits `b2c8b78`, `696ac37`, `d24f628`, `4b20786`, `d6a6065`, `5279e7a`. |
| Weeks 13–14 — Event Bus + persistence wiring | Weeks of Jun 8–15 | **M2.6–M2.9 (persistence wiring) landed 2026-05-01.** M2-bridge (AMD-34–40, V001→25 columns, V002/V003) landed 2026-05-02. D1 WAL spike landed 2026-05-15. M3.1–M3.4b (event bus core, REPLAY→LIVE, backpressure, state projection, integration tests) landed 2026-05-16–19. M3.6a–M3.6b (composition-root prep) landed 2026-05-20. ~476+ production files, ~1,465+ tests, 20 modules. Still ~2–3 weeks ahead. |

**What the plan called "Phase 1 — Interface Specification" is now the FROZEN Phase 2 block backlog in `phase-2-block-backlog.md`.** Internal project phase naming and Master Release Plan phase naming differ — the plan's "P2 Foundation Implementation" corresponds to internal Phase 3 (test-first implementation). The nexsys-hivemind governance uses internal project phase naming (P1 design docs, P2 interface specs, P3 implementation).

**Tracked going forward:** Every M{x}.{y} milestone's actual completion date against the plan's week boundaries. When a subsystem's implementation milestones complete, compare to the plan's originally allocated week and record the delta in the session log. If actual cadence continues ahead of plan, downstream phases (P3–P7) can absorb buffer time or be compressed.

---

## 1. Executive Summary

This document defines the complete execution plan for shipping HomeSynapse v1 within 258 days (March 13 – November 25, 2026). The plan covers five parallel workstreams: Core Runtime, Web UI, Website & Documentation, Distribution & Packaging, and Quality Assurance. Every week has measurable deliverables. Every dependency is mapped. Every workstream converges on a single gate: a user visits homesynapse.com, clicks Install, and a working smart home operating system is running in their home within 30 minutes.

**Current state:** Phase 1 (System Design Documentation) is complete. All 14 design documents are Locked. The homesynapse-core repository has a fully scaffolded 19-module Gradle project with build infrastructure, CI pipeline, and empty module shells. Zero production code exists. Phase 2 (Interface-Level Specification) is ready to begin.

**End state:** A downloadable installer on homesynapse.com that deploys HomeSynapse Core to a Raspberry Pi (or x86 Linux). The installation wizard configures networking, discovers Zigbee devices, and lands the user in an observability dashboard showing real-time device state, event traces, health status, and basic automation controls. The system runs 50+ Zigbee devices stable for 72+ hours with zero event loss.

---

## 2. Plan Structure & Key Dates

The 258 days divide into seven sequential phases. Phases overlap where dependencies allow, but each phase has a hard gate before the next begins. All dates are Mondays (week start).

| # | Phase | Start | End | Weeks | Gate |
|---|-------|-------|-----|-------|------|
| P1 | Interface Specification | Mar 16 | May 24 | 10 | All interfaces compile |
| P2 | Foundation Implementation | May 25 | Jul 19 | 8 | Event bus + persistence pass |
| P3 | Subsystem Implementation | Jul 20 | Sep 13 | 8 | All subsystems pass tests |
| P4 | Integration & Zigbee | Sep 14 | Oct 11 | 4 | 50 devices stable 24h |
| P5 | System Validation | Oct 12 | Oct 25 | 2 | 72h stability, perf targets |
| P6 | Distribution & Website | Oct 26 | Nov 15 | 3 | Install flow works end-to-end |
| P7 | Launch Prep & Buffer | Nov 16 | Nov 25 | 1.5 | Public launch ready |

Cross-cutting workstreams (Website, Documentation, UI) run in parallel from Week 1. Their integration points are called out in each phase.

---

## 3. Workstream Definitions

Five workstreams run throughout the plan. Each has an owner role, a primary output, and explicit integration points with other workstreams.

| # | Workstream | Primary Output | Owner | Integration Points |
|---|------------|---------------|-------|--------------------|
| W1 | Core Runtime | Java 21 event-sourced runtime | PM + Coder | Feeds APIs to W2, specs to W3 |
| W2 | Web UI | Preact SPA dashboard | PM + Coder | Consumes W1 APIs, matches W4 design |
| W3 | Docs & Website | homesynapse.com + docs site | Hivemind + PM | Consumes W1 specs, hosts W5 artifacts |
| W4 | Distribution | Installer + packaging | Coder | Packages W1 + W2, hosted on W3 |
| W5 | QA & Validation | Test suites + stability runs | Coder | Validates all workstreams |

---

## 4. Phase 1: Interface Specification (Weeks 1–10)

Every Java interface, record, enum, sealed interface, and exception type is defined with full Javadoc contracts. No implementation code. The output is a codebase that compiles to empty JARs but defines every public contract.

### 4.1 Interface Spec Production Order

Interfaces follow the same dependency order as design documents. Four waves, each wave's inputs are the previous wave's outputs.

| Wave | Weeks | Subsystems | Modules | Gate |
|------|-------|------------|---------|------|
| 1 | 1–3 | Event Model, Event Bus, Platform API | event-model, event-bus, platform-api | Foundation types compile |
| 2 | 3–5 | Device Model, State Store, Integration API | device-model, state-store, integration-api | All core types compile |
| 3 | 5–8 | Persistence, Configuration, Automation, Integration Runtime | persistence, configuration, automation, integration-runtime | All internal subsystems compile |
| 4 | 8–10 | REST API, WebSocket API, Observability, Lifecycle, Zigbee (types only) | rest-api, websocket-api, observability, lifecycle, integration-zigbee | Full project compiles clean |

### 4.2 Weekly Deliverables — Interface Spec

| Week | Deliverables | Verification |
|------|-------------|-------------|
| 1 | EventId, EventEnvelope, EventType taxonomy, EventCategory enum, all event records. SubscriptionFilter, EventPublisher, EventStore query interface. PlatformPaths, HealthReporter interfaces. | javac -Xlint:all -Werror passes. All types have Javadoc. |
| 2 | EventBus interface, subscriber checkpoint model, backpressure types. Priority tier enums. Module-info.java for event-model and event-bus. | event-model and event-bus modules compile independently. |
| 3 | Device, Entity, Capability, Attribute, Command types. DeviceRegistry, EntityRegistry, CapabilityRegistry interfaces. CommandValidator. StateQueryService, CheckpointStore interfaces. | device-model and state-store modules compile against event-model. |
| 4 | IntegrationDescriptor, IntegrationAdapter, IntegrationContext, IntegrationSupervisor interfaces. Health FSM types. CommandHandler interface. | integration-api compiles against event-model + device-model. |
| 5 | EventStore persistence interface, TelemetryWriter, retention tier types. ConfigurationAccess, ConfigurationProvider, ConfigModel, ConfigIssue types. | persistence and configuration modules compile. |
| 6 | AutomationDefinition, Run lifecycle FSM, PendingCommand, PendingCommandLedger, AutomationRegistry, RunManager, CommandDispatchService, selector vocabulary. | automation module compiles against all core dependencies. |
| 7 | IntegrationRuntime internal types, supervisor implementation contracts, thread architecture types. Zigbee adapter type stubs (coordinator abstraction, ZigbeeFrame, DeviceProfile). | integration-runtime and integration-zigbee compile. |
| 8 | REST API endpoint interfaces, OpenAPI 3.1 spec (first draft). RFC 9457 error types. ETag types. Cursor pagination types. | rest-api module compiles. OpenAPI spec validates. |
| 9 | WebSocket message protocol types (client-to-server + server-to-client). AsyncAPI 3.0 spec. Observability types: HealthContributor, SystemHealth hierarchy, TraceChain/TraceEvent. JFR event types. | websocket-api and observability modules compile. AsyncAPI validates. |
| 10 | Lifecycle: SystemLifecycleManager, phase types, shutdown ordering. Dashboard build.gradle.kts (Vite/Preact scaffold). Full project compilation gate. Traceability docs populated. | All 19 modules compile clean. ./gradlew check passes. Every interface traceable to design doc section. |

### 4.3 Parallel Workstreams During Phase 1

**Website (W3) — Weeks 1–10**

| Week | Website Task | Output |
|------|-------------|--------|
| 1–2 | Docusaurus project scaffold. Apply DAS v1 design system (typography, colors, layout). Landing page redesign from countdown to product positioning. | Live staging site with brand-consistent design. |
| 3–4 | Core content pages: What is HomeSynapse, Architecture Overview, Privacy Promise, Comparison pages (vs Home Assistant, vs Google/Alexa). | 4–6 content pages drafted per DAS writing standards. |
| 5–6 | Documentation scaffold: Getting Started placeholder, API Reference placeholder, Configuration Reference placeholder. CI pipeline for docs (Vale linting, frontmatter validation). | Docs site builds in CI. Placeholder structure in place. |
| 7–8 | Installation guide wireframe. Hardware requirements page. Supported devices page (Zigbee device database begins). FAQ page. | Complete informational site structure. |
| 9–10 | Blog scaffold. Community page (GitHub links, contribution guide placeholder). Newsletter/mailing list signup integration. | homesynapse.com ready for content population. |

---

## 5. Phase 2: Foundation Implementation (Weeks 11–18)

Test-driven implementation of the foundational subsystems. Tests are written first against Phase 1 interfaces, then implementation makes them pass. The foundation layer must be rock-solid before any higher-level subsystem is built.

### 5.1 Implementation Order

| Week | Subsystem | Key Implementation Work | Tests Required |
|------|-----------|------------------------|----------------|
| 11 | SQLite WAL Validation Spike + EventId/ULID | WAL mode validation on aarch64. ULID generation with monotonic guarantee. EventSerializer (Jackson). Basic event types. | WAL spike results documented. ULID uniqueness under concurrency. Serialization round-trip for all event types. |
| 12 | Event Store (Persistence) | SQLite-backed EventStore. Append-only writes with WAL. Per-entity sequence numbers. Global position tracking. Retention tier storage. | Append + query by entity. Sequence ordering. Crash recovery (kill -9 simulation). Retention execution. |
| 13 | Event Bus | In-process pub-sub with priority tiers. Subscriber checkpoint management. Write-ahead persistence (events durable before delivery). At-least-once delivery with subscriber-side tracking. | Publish + subscribe. Priority ordering. Checkpoint save/restore. Delivery after crash recovery. Backpressure behavior. |
| 14 | State Store | In-memory materialized view driven by event bus subscription. EntityState construction from events. Checkpoint-based recovery. StateQueryService implementation. | State projection correctness. Bulk query performance. Checkpoint recovery matches event replay. Concurrent read safety. |
| 15 | Platform API + test-support | PlatformPaths implementations (Linux, development). HealthReporter. test-support module: InMemoryEventStore, SynchronousEventBus, TestFixtures, TestClock, NoRealIoExtension. | Platform detection. Health reporting format. All test fixtures validated independently. |
| 16 | Configuration System | YAML loading pipeline. JSON Schema validation. Secret store (AES-256-GCM). Hot reload with atomic swap. ConfigurationAccess and ConfigurationProvider implementations. | Schema validation pass/fail. Secret encryption round-trip. Hot reload triggers config_changed event. Invalid config rejected gracefully. |
| 17 | Integration tests: Event Bus + Store + State Store end-to-end | Wire Event Bus to Event Store and State Store. Verify the full event lifecycle: publish -> persist -> deliver -> project state. Failure injection (subscriber crash, store timeout). | End-to-end event flow. State consistency after 10,000 events. Recovery from subscriber crash. No event loss under load. |
| 18 | Performance benchmarks + memory profiling | Benchmark event throughput (target: >500/sec sustained). Benchmark state query latency (target: <5ms p99). Memory profiling under 50-entity simulated load. Fix any performance issues. | All budget goals from MVP §8.2 validated. Memory < 512 MB idle. CPU < 5% idle. |

### 5.2 Parallel Workstreams During Phase 2

**Web UI (W2) — Weeks 11–18**

| Week | UI Task | Output |
|------|---------|--------|
| 11–12 | Vite + Preact project setup. Design system implementation (colors, typography, spacing from DAS). Component library: layout shell, sidebar nav, status indicators, cards. | Compiled Preact app with design system. Component storybook/examples. |
| 13–14 | WebSocket client library (typed messages matching AsyncAPI spec). Connection management with reconnection logic. State management architecture (Preact hooks/context). | WebSocket client that connects to mock server. Typed message handling. |
| 15–16 | Event stream view (virtual-scrolled list). Event detail panel (causal chain visualization). Health status dashboard (three-tier composition). | Working event stream and health views against mock data. |
| 17–18 | Device list view. Device detail view (state attributes, event history). REST API client library (typed, matching OpenAPI spec). Bundle size audit (target: <100 KB gzipped). | Feature-complete dashboard against mock APIs. Bundle under budget. |

**Website (W3) — Weeks 11–18**

| Week | Website Task | Output |
|------|-------------|--------|
| 11–13 | API Reference pages auto-generated from OpenAPI + AsyncAPI specs. Configuration Reference from JSON Schemas. Event Type Reference from event model interfaces. | Auto-generated reference docs in CI pipeline. |
| 14–16 | Architecture deep-dive pages. Event Sourcing explained. Integration isolation explained. Write Getting Started guide (placeholder for install steps, real architecture content). | Technical content pages live on staging. |
| 17–18 | Supported Zigbee devices page (initial list from Doc 08 device profiles). Hardware recommendation page with benchmark data from Week 18. | Device compatibility database started. Hardware guide published. |

---

## 6. Phase 3: Subsystem Implementation (Weeks 19–26)

All remaining subsystems are implemented on top of the verified foundation. Each subsystem follows the same test-first discipline: write tests against the interface, then implement until tests pass.

| Week | Subsystem | Key Implementation Work | Tests Required |
|------|-----------|------------------------|----------------|
| 19 | Integration Runtime | IntegrationSupervisor with OTP-style supervision tree. Health state machine (HEALTHY -> DEGRADED -> SUSPENDED -> FAILED). Thread architecture (platform threads for serial I/O, virtual threads for network). Resource monitoring. | Adapter lifecycle (start/stop/crash/restart). Health state transitions. Crash isolation (one adapter crash doesn't affect others). Resource limit enforcement. |
| 20 | Automation Engine (core) | AutomationRegistry, RunManager. Trigger-Condition-Action execution pipeline. Event-driven trigger matching. State-based condition evaluation via StateQueryService. | Trigger matching accuracy. Condition evaluation against state. Run lifecycle state machine. Automation produces correct events. |
| 21 | Automation Engine (advanced) | PendingCommandLedger with command confirmation matching. CommandDispatchService. Cascade governance (depth limits). Four concurrency modes. Selector vocabulary resolution. | Command tracking and confirmation. Cascade depth enforcement. Concurrent automation execution. Entity selector resolution. |
| 22 | REST API | Javalin-based HTTP server. Five endpoint planes: state, command, event history, automation, system. RFC 9457 error responses. ETag consistency. Cursor-based pagination. | All endpoints return correct data. Error format compliance. Pagination correctness. ETag behavior. Auth token validation. |
| 23 | WebSocket API | Event relay via EventBus subscription. Client message protocol. Subscribe/unsubscribe. Resume-from-checkpoint. Four-stage backpressure escalation. Per-client filter evaluation. | Message protocol compliance. Subscription filtering. Resume correctness. Backpressure triggers at correct thresholds. Connection cleanup. |
| 24 | Observability & Debugging | HealthContributor aggregation (three-tier composition). JFR continuous recording with pre-aggregation. Causal chain assembly from EventStore. Trace query interface. | Health aggregation correctness. JFR events recorded. Causal chain assembly from correlation/causation IDs. Flapping prevention. |
| 25 | Startup, Lifecycle & Shutdown | SystemLifecycleManager with seven-phase initialization. Deterministic startup ordering. Graceful shutdown (reverse order). Systemd watchdog protocol. PlatformPaths (systemd implementation). | Startup sequence correctness. Shutdown drains in-flight events. Watchdog heartbeat. Fail-fast on critical failures. Graceful degradation on non-critical. |
| 26 | Full integration testing | Wire all subsystems together in homesynapse-app. End-to-end: startup -> config load -> event bus running -> state store projecting -> APIs serving -> observability reporting. Simulated device events through the full pipeline. | Application starts and serves APIs. Event flow from publish to UI. Health dashboard shows real status. Automation triggers from simulated events. REST + WebSocket APIs return consistent data. |

### 6.2 Parallel Workstreams During Phase 3

**Web UI (W2) — Weeks 19–26**

| Week | UI Task | Output |
|------|---------|--------|
| 19–20 | Connect to real REST API and WebSocket API (from Phase 2 foundation). Replace mock data with live data. Event stream view with real events. | Dashboard shows live data from running core. |
| 21–22 | Automation status view (active automations, run traces). System health dashboard with real HealthContributor data. Navigation and routing finalized. | Full observability dashboard functional. |
| 23–24 | Basic device control (send commands via REST API). Automation enable/disable. Event filtering and search. Responsive layout for tablet/mobile browsers. | Interactive dashboard (not just read-only). |
| 25–26 | Performance optimization: virtual scrolling tuning, WebSocket reconnection, loading states. Accessibility audit. Bundle final audit (<100 KB). Integration testing with full runtime. | Production-ready dashboard. Bundle under budget. Accessible. |

**Distribution (W4) — Weeks 19–26**

| Week | Distribution Task | Output |
|------|-------------------|--------|
| 19–20 | jlink custom runtime image (Corretto 21, aarch64 + x86_64). Systemd service unit file. Installation directory structure (/opt/homesynapse). Data directory layout. | jlink image boots on RPi 5. Systemd starts/stops service. |
| 21–22 | Installation script (shell-based). Network configuration wizard (port selection, bind address). First-run initialization (database creation, default config generation). | Single-command install on clean Raspberry Pi OS. |
| 23–24 | .deb package creation (dpkg-deb). APT repository structure. Uninstall/upgrade scripts. Config file preservation across upgrades. | .deb installs cleanly. apt install homesynapse works from local repo. |
| 25–26 | Installation wizard UI (served by HomeSynapse on first run). Step-by-step: welcome -> network setup -> Zigbee coordinator detection -> device discovery -> dashboard. Rollback on failure. | End-to-end install wizard tested on fresh Pi. |

---

## 7. Phase 4: Integration & Zigbee (Weeks 27–30)

The Zigbee adapter is the first real-world integration and the validation of the entire architecture against physical hardware.

| Week | Focus | Key Work | Verification |
|------|-------|----------|-------------|
| 27 | Zigbee Coordinator | Z-Stack ZNP serial protocol. EZSP serial protocol. Coordinator abstraction layer. Serial I/O on platform threads. Network formation (channel scan, PAN ID). Permit join. | Coordinator connects to physical USB stick. Network forms. Devices can join. |
| 28 | Device Discovery & Pairing | Device interview (node descriptor, simple descriptor, endpoint enumeration). Cluster-to-capability mapping (ZCL standard clusters). Standard device profiles (lights, switches, sensors, plugs). | Devices pair and appear in DeviceRegistry. Capabilities correctly mapped. State events flowing through event bus. |
| 29 | Manufacturer Codecs & Control | Tuya-specific codec. Xiaomi-specific codec. Command dispatch (on/off, dim, color). State reporting (attribute reports, zone status). Mesh topology monitoring. | Tuya and Xiaomi devices work. Commands produce expected physical results. State reports arrive within latency targets. |
| 30 | Stability Testing (24h) | 50-device deployment. Sustained operation test (24 hours). Integration crash/restart test. Coordinator reconnection after USB unplug. Event loss audit. | 50 devices stable 24 hours. Zero event loss. Crash recovery within 30 seconds. All automations firing correctly. |

---

## 8. Phase 5: System Validation (Weeks 31–32)

The acceptance test from MVP §4 Tier 1. This is the go/no-go gate for release.

| Week | Validation Activity | Pass Criteria |
|------|-------------------|---------------|
| 31 | 72-hour stability test. 50+ Zigbee devices. Six layered automations running continuously. Memory monitoring. Event loss audit. Performance metrics collection. | Zero crashes. Zero event loss. Zero memory leaks. All performance targets met (§8 of MVP doc). Automations firing correctly for full duration. |
| 32 | Failure mode testing: kill -9 recovery, integration crash isolation, coordinator disconnect/reconnect, power cycle recovery. Device replacement test (swap a device, automations intact). Event trace verification (every state change explainable). | Kill -9 recovery with zero event loss. Crash isolation demonstrated. Device replacement preserves automations. Event trace complete for all state changes. All hard invariants from MVP §8.1 pass. |

---

## 9. Phase 6: Distribution & Website (Weeks 33–35)

Package everything for public consumption. The website becomes the distribution point.

| Week | Focus | Key Work | Output |
|------|-------|----------|--------|
| 33 | Packaging finalization | Final .deb packages (aarch64 + x86_64). APT repository hosted on GitHub/Cloudflare. Download page on homesynapse.com. SHA256 checksums. GPG signing. | Signed packages downloadable from homesynapse.com. |
| 34 | Installation flow end-to-end | Test: fresh Raspberry Pi OS -> visit homesynapse.com -> copy install command -> run -> wizard opens in browser -> Zigbee discovered -> devices paired -> dashboard live. Fix all friction points. | Complete install flow under 30 minutes. Zero user intervention beyond wizard steps. |
| 35 | Website launch content | Final Getting Started guide with real screenshots. Video walkthrough (optional). Release notes page. Changelog. Update docs CI to auto-publish. SEO basics (meta tags, Open Graph, structured data). | homesynapse.com ready for public traffic. |

---

## 10. Phase 7: Launch Prep & Buffer (Weeks 36–37)

Buffer for overruns, final polish, and launch preparation. If everything is on track, this time is used for:

| Week | Activity | Output |
|------|----------|--------|
| 36 | Bug fixes from validation. Documentation polish. Performance tuning. Community preparation (GitHub issues templates, contribution guidelines, code of conduct). Social media presence setup. | All known issues resolved. Documentation complete. Community infrastructure ready. |
| 37 | Soft launch to selected testers. Monitor for critical issues. Final website review. Launch announcement draft. Press/community outreach preparation. | Tested by external users. Launch announcement ready. Go/no-go decision made. |

---

## 11. Risk Register & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Zigbee hardware compatibility issues (specific devices don't work with chosen coordinator) | High | Coordinator abstraction (Z-Stack + EZSP) provides two independent paths. Manufacturer codecs limited to ZCL standard + Tuya + Xiaomi (covers ~80% of market). Unknown devices fail gracefully. | Week 27–28 is early enough to discover problems. Two coordinator libraries provide fallback. Supported device list published honestly — no false promises. |
| SQLite performance on aarch64 under sustained write load | Medium | WAL validation spike (Week 11) catches this before any production code depends on it. If spike fails, H2 is the pre-designed fallback (LTD-03 explicitly preserves this option). | Spike-first approach. Fallback path documented. Decision by end of Week 11. |
| Preact bundle size exceeds 100 KB budget | Medium | Charting library (uPlot) is 35 KB. Preact core is 4 KB. Budget leaves ~60 KB for application code. Virtual scrolling library is the main risk. Lazy-load non-critical views. | Bundle audits in Weeks 18 and 26. Lazy loading as escape valve. View prioritization (event stream and health are critical; others can lazy-load). |
| Single developer capacity creates bottleneck on critical path | High | Phases are sequenced to avoid context-switching. Each week has a single primary focus. AI-assisted coding (Coder agent) handles implementation. PM agent handles design translation. Hivemind handles strategic decisions. | AI agent architecture multiplies effective capacity. Critical path has no parallelism requirements within a single week. |
| Phase 2 foundation implementation takes longer than 8 weeks | Medium | Phase 2 has 2 weeks of integration testing and performance benchmarking. If core implementation finishes faster, those weeks absorb into Phase 3. If slower, Phase 3 start shifts but Phases 4–7 compress. | Buffer exists in Phase 7 (1.5 weeks). Phases 4–5 can compress from 6 weeks to 5 if needed. Website work is fully parallel. |
| Zigbee device discovery is unreliable or slow | Medium | Device interview protocol is well-documented in ZCL spec. Timeout and retry logic built into adapter design. Manual device addition as fallback in installation wizard. | Week 28 dedicated to discovery. Manual fallback always available. Supported device list sets honest expectations. |

---

## 12. Weekly Goals Quick Reference

Every week has a single primary objective and 2–3 measurable verification criteria. Use this as the weekly standup checklist.

| Wk | Phase | Primary Objective | Done When |
|----|-------|-------------------|-----------|
| 1 | P1 — Interfaces | Event model foundation types | EventEnvelope, EventId, EventType, all event records compile with Javadoc |
| 2 | P1 — Interfaces | Event bus and subscriber model | EventBus, subscriber checkpoint, backpressure types compile |
| 3 | P1 — Interfaces | Device model and state store types | Device/Entity/Capability types + StateQueryService compile |
| 4 | P1 — Interfaces | Integration API types | IntegrationAdapter, IntegrationContext, health FSM types compile |
| 5 | P1 — Interfaces | Persistence and configuration interfaces | EventStore persistence + ConfigurationAccess compile |
| 6 | P1 — Interfaces | Automation engine types | Full automation type system compiles against all dependencies |
| 7 | P1 — Interfaces | Runtime and Zigbee type stubs | Integration runtime + Zigbee adapter types compile |
| 8 | P1 — Interfaces | REST API + OpenAPI spec | REST module compiles. OpenAPI 3.1 spec validates |
| 9 | P1 — Interfaces | WebSocket + Observability types | WS protocol types + health hierarchy + JFR types compile |
| 10 | P1 — Interfaces | Lifecycle + full compilation gate | All 19 modules compile. Traceability docs complete. ./gradlew check passes |
| 11 | P2 — Foundation | SQLite WAL spike + ULID implementation | WAL spike results documented. ULID passes concurrency tests |
| 12 | P2 — Foundation | Event Store implementation | SQLite-backed store passes all persistence tests. Crash recovery verified |
| 13 | P2 — Foundation | Event Bus implementation | Pub-sub works. Write-ahead persistence. At-least-once delivery verified |
| 14 | P2 — Foundation | State Store implementation | Materialized view correct. Checkpoint recovery matches replay |
| 15 | P2 — Foundation | Platform API + test-support | Platform detection works. All test fixtures validated |
| 16 | P2 — Foundation | Configuration System | YAML loading, schema validation, secrets, hot reload all working |
| 17 | P2 — Foundation | End-to-end integration test | Full event lifecycle verified. 10K events with zero loss |
| 18 | P2 — Foundation | Performance benchmarks | All MVP §8.2 budget goals met on target hardware |
| 19 | P3 — Subsystems | Integration Runtime | Supervisor tree works. Crash isolation verified. Health FSM correct |
| 20 | P3 — Subsystems | Automation Engine (core) | Trigger/condition/action pipeline works. Runs produce correct events |
| 21 | P3 — Subsystems | Automation Engine (advanced) | Command ledger, cascade governance, concurrency modes all pass |
| 22 | P3 — Subsystems | REST API | All 5 endpoint planes work. Error format compliant. Pagination correct |
| 23 | P3 — Subsystems | WebSocket API | Subscriptions, resume, backpressure all work. Protocol compliant |
| 24 | P3 — Subsystems | Observability & Debugging | Health aggregation correct. JFR recording. Causal chains assemble |
| 25 | P3 — Subsystems | Startup & Lifecycle | Seven-phase init works. Graceful shutdown drains events. Watchdog OK |
| 26 | P3 — Subsystems | Full system integration | App starts, serves APIs, projects state, fires automations end-to-end |
| 27 | P4 — Zigbee | Coordinator connection | USB coordinator connects. Network forms. Devices can join |
| 28 | P4 — Zigbee | Device discovery & pairing | Devices pair, appear in registry, state events flowing |
| 29 | P4 — Zigbee | Manufacturer codecs & control | Tuya + Xiaomi work. Commands work. State reports within latency |
| 30 | P4 — Zigbee | 24-hour stability test | 50 devices, 24h stable, zero event loss, crash recovery works |
| 31 | P5 — Validation | 72-hour stability run | Zero crashes/leaks/event loss. All perf targets met for 72 hours |
| 32 | P5 — Validation | Failure mode testing | Kill -9, crash isolation, device replacement, event trace all pass |
| 33 | P6 — Distribution | Package and publish | Signed .deb packages downloadable from homesynapse.com |
| 34 | P6 — Distribution | Install flow end-to-end | Fresh Pi to working dashboard in <30 minutes |
| 35 | P6 — Distribution | Launch content | Getting Started guide, release notes, docs site auto-publishing |
| 36 | P7 — Launch | Bug fixes and polish | All known issues resolved. Docs complete. Community infra ready |
| 37 | P7 — Launch | Soft launch and go/no-go | External testers validated. Launch announcement ready |

---

## 13. Critical Dependency Map

These are the hard dependencies that, if violated, cause cascading delays.

| Dependency | Blocks | Consequence of Delay |
|------------|--------|---------------------|
| Event Model interfaces (Week 2) | Every other module | Entire project shifts. Nothing compiles without event types. |
| Device Model interfaces (Week 3) | State Store, Automation, Zigbee, APIs | Cannot define state shape or command model. |
| SQLite WAL spike (Week 11) | All persistence work | If spike fails, must pivot to H2. Adds 1–2 weeks. |
| Event Store implementation (Week 12) | Event Bus, State Store, everything above | Foundation cannot be tested without durable storage. |
| Event Bus implementation (Week 13) | State Store, Automation, APIs, UI | No event delivery means no state projection. |
| REST + WebSocket APIs (Weeks 22–23) | Web UI live data integration | UI stays on mock data. Install wizard cannot function. |
| Integration Runtime (Week 19) | Zigbee Adapter (Week 27) | Cannot run any real integration without supervisor. |
| Zigbee coordinator working (Week 27) | All hardware testing | No physical device testing possible. |
| 72-hour stability pass (Week 31) | Distribution packaging | Cannot ship unstable software. Plan enters buffer. |
| Install flow tested (Week 34) | Public launch | Cannot launch without verified install experience. |

---

## 14. V1 Release Success Criteria

HomeSynapse v1 ships when ALL of the following are true:

| # | Criterion | Verification Method |
|---|-----------|-------------------|
| 1 | homesynapse.com serves a working download page with install instructions | Manual verification: visit site, follow instructions on fresh Pi |
| 2 | Single-command installation on Raspberry Pi OS (64-bit) | Automated: run install script, verify service starts |
| 3 | Installation wizard discovers Zigbee coordinator and pairs devices | Manual: plug in coordinator, run wizard, pair 5+ devices |
| 4 | Web dashboard shows real-time device state, event stream, health status | Manual: verify all three views update in real-time |
| 5 | 50+ Zigbee devices stable for 72 consecutive hours | Automated: stability test with metrics collection |
| 6 | Zero event loss across kill -9 recovery | Automated: kill process, restart, audit event continuity |
| 7 | Integration crash isolation demonstrated (kill Zigbee, Z-Wave keeps running) | Automated: crash injection test (Tier 1 validates with simulated second adapter) |
| 8 | Event trace explains any device state change | Manual: trigger state change, verify full causal chain in UI |
| 9 | All hard invariants from MVP §8.1 pass | Automated: benchmark suite targeting all six hard invariants |
| 10 | Documentation site live with Getting Started, API Reference, Config Reference | Manual: verify all three sections exist and are accurate |

*End of Document*
