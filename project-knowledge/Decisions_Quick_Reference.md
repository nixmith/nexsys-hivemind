<!--
file: project-knowledge/Decisions_Quick_Reference.md
purpose: Token-efficient index of all locked technical decisions (LTD-01..19) and Phase 3 milestone decisions (DEC-M3-01..17). Agents use this for constraint lookup; full text lives in homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md for JIT reading when detail is needed.
audience: All (PM, Coder, Cowork)
update-cadence: per-milestone (LTD changes rare; DEC-M3 grows with milestones)
state-type: reference
status: CURRENT
freshness-tier: COLD
last-verified: 2026-05-21 against HomeSynapse_Core_Locked_Decisions.md (19 LTDs, 17 DEC-M3s) + system prompt hard constraints + MODULE_CONTEXT codebase grep
full-text-location: homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md
-->

# Locked Decisions — Quick Reference

**19 Locked Technical Decisions (LTD-01 through LTD-19)** — permanent technology and architecture choices.
**17 Phase 3 Milestone Decisions (DEC-M3-01 through DEC-M3-17)** — implementation decisions locked during M3.
**Full text with rationale, amendment history, and cross-references:** homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md

---

## Locked Technical Decisions (LTD)

### Runtime and Language

| ID | Decision | Key Constraints |
|---|---|---|
| LTD-01 | **Java 21 LTS** (Amazon Corretto). G1GC mandated. Virtual threads enabled. -Xmx1536m, -Xss512k on constrained tier. | All modules. Language baseline. |
| LTD-02 | **Pi 5 recommended, Pi 4 validation floor.** NVMe via M.2 HAT is production requirement. | Hardware performance floor for all benchmarks. |

### Persistence and Data

| ID | Decision | Key Constraints |
|---|---|---|
| LTD-03 | **SQLite in WAL mode** for event store, state store, all metadata. All sqlite-jdbc operations through bounded platform thread executor (avoids VT carrier pinning). | Persistence layer. Event store. State store. See AMD-26/27. |
| LTD-04 | **ULID with monotonic generation** for all IDs. BLOB(16) in SQLite. Hand-rolled VT-safe UlidFactory (replaced ulid-creator per DECIDE-02). | platform-api (UlidFactory, Ulid). All identity types. Crockford Base32 at API boundaries. |
| LTD-05 | **Per-entity sequence numbers** for optimistic concurrency + SQLite rowid as global position. Correlation + causation IDs on every event. | Event store schema. Subscriber checkpoints. Projections. |
| LTD-06 | **Write-ahead persistence.** Events persisted to SQLite before delivery. Subscribers at-least-once, must be idempotent. Event store IS the outbox. | Persistence. Event bus. Subscriber system. |
| LTD-07 | **Hand-rolled forward-only SQL migrations.** Flyway-compatible naming. Runner refuses without pre-migration backup (enforced at runtime). | Persistence layer. Upgrade workflow. CI. |

### Serialization and Configuration

| ID | Decision | Key Constraints |
|---|---|---|
| LTD-08 | **Jackson 2.18+** with Blackbird module. Singleton ObjectMapper. Mandatory startup warm-up before VT access. EventSerializer abstraction boundary. | Events, REST, WebSocket, config internal. Pin ≥2.18.2 (record regression). |
| LTD-09 | **YAML 1.2** (SnakeYAML Engine) for user config. JSON Schema validation (networknt). `homesynapse validate-config` CLI. | /etc/homesynapse/. VS Code auto-completion via schema. |
| LTD-19 | **Registry-based event type resolution.** @EventType annotation + EventTypeRegistry. PersistenceJacksonModule for sealed interfaces. DegradedEvent two-stage fallback. No @JsonTypeInfo on domain types. | Event serialization. Event-model module. Integration-api (lifecycle events). Device model (AttributeValue serde). |

### Build and Module System

| ID | Decision | Key Constraints |
|---|---|---|
| LTD-10 | **Gradle + Kotlin DSL.** Version catalogs. Convention plugins in build-logic/. modules-graph-assert for dependency direction. ArchUnit for code-level architecture tests. | Build system. CI. All module boundaries. |
| LTD-17 | **All MVP integrations compiled-in.** No dynamic JAR loading. Integration API boundary enforced at build time (Gradle deps, modules-graph-assert, ArchUnit, JPMS module-info). | integration-api. core-internal. integration-zigbee. |

### Event Bus and Integration

| ID | Decision | Key Constraints |
|---|---|---|
| LTD-11 | **In-process event bus using virtual threads.** No external broker (no Kafka/RabbitMQ/NATS). EventPublisher interface abstracts dispatch. Per-subscriber bounded queues. No `synchronized` — use ReentrantLock only. | core/event-bus. All event consumers. Integration runtime. |
| LTD-12 | **Zigbee only in MVP.** Device model and capability system protocol-agnostic from day one. | integration-zigbee. Device model. Capability system. |

### Deployment and Operations

| ID | Decision | Key Constraints |
|---|---|---|
| LTD-13 | **Self-contained jlink distribution.** systemd service, dedicated homesynapse user. FHS layout: /opt/, /etc/, /var/lib/, /var/log/. ProtectSystem=strict. MemoryMax=2G. | Packaging. Deployment. Security (unprivileged user). |
| LTD-14 | **CLI-driven upgrades.** No auto-updates. Mandatory pre-upgrade snapshot. Dry-run migration against DB copy. Auto-rollback on health check failure. 3 snapshots retained. | Upgrade workflow. Snapshot management. LTD-07 dependency. |
| LTD-15 | **SLF4J 2.x + Logback 1.5.x + logstash-logback-encoder** (structured JSON). JFR continuous recording (6h rolling, 100 MB). Custom JFR events. No Prometheus/OpenTelemetry in MVP. | Logging (all). Observability. JFR Event Streaming for real-time dashboards. |
| LTD-16 | **SemVer 2.0.0.** Major-version URL prefix (/api/v1/). Additive-only within major. ≥1 major version deprecation window. OpenAPI 3.1 for REST. AsyncAPI for WebSocket. oasdiff in CI. | REST/WebSocket/Integration API. Event schema. |

### Web UI

| ID | Decision | Key Constraints |
|---|---|---|
| LTD-18 | **Preact SPA (~4 KB)** for observability dashboard at /dashboard/. uPlot charting. 100 KB gzipped budget. HTMX + JTE reserved for Tier 2+ config UI at /config/. | Web UI. Javalin HTTP server. REST/WebSocket consumption. |

---

## Phase 3 Milestone Decisions (DEC-M3)

### Event Bus and Projection Architecture (DEC-M3-01 through DEC-M3-10)

| ID | Decision | Source |
|---|---|---|
| DEC-M3-01 | **Projection read/write discipline.** Two-phase: READ → PUBLISH → CHECKPOINT. No interleaving. | AMD-41 §3.2.1 |
| DEC-M3-02 | **Self-produced event detection.** SelfProducedFilter (60s TTL, lazy eviction) + stateVersion defence-in-depth. | AMD-41 §3.2.2 |
| DEC-M3-03 | **REPLAY→LIVE transition.** Three-phase: REPLAY (catch-up) → TRANSITION (drain queue) → LIVE. | AMD-42 §3.4.2 |
| DEC-M3-04 (modified) | **State projection checkpoints.** MVP uses ViewCheckpointStore. SqliteSnapshotStore deferred. | AMD-41 §3.2.3 |
| DEC-M3-05 | **Snapshot format.** Jackson JSON with snapshotVersion + projectionVersion headers. V003 table created; impl deferred. | AMD-41 §3.2.3–4 |
| DEC-M3-06 (augmented) | **Subscriber isolation catalog.** INV-SUB-ISO-01..06 — per-subscriber VT, connection, DLQ, mode, queue, filter. | AMD-42 §3.4.4–6 |
| DEC-M3-07 | **Coalescing DEFERRED** past M3. coalesceExempt retained but inert. | AMD-43 §3.6.5 |
| DEC-M3-08 (rejected, replaced) | **Backpressure model.** No publish blocking on queue depth. Natural backpressure from single-writer. Rate limit (200/s) for StateProjection. | AMD-43 §3.6.1 |
| DEC-M3-09 | **Clock injection.** Single Clock per JPMS module. NO_DIRECT_TIME_ACCESS ArchUnit rule. Not an AMD — standalone ArchUnit decision. | ArchUnit rule |
| DEC-M3-10 | **State_changed derivation** lives in StateProjection (core/state-store), NOT in writer. Writer is semantic-free. | AMD-41 (scope) |

### Implementation Order and Build Decisions (DEC-M3-11 through DEC-M3-15)

| ID | Decision | Source |
|---|---|---|
| DEC-M3-11 | **Implementation order.** M3.1 → M3.5a → M3.2 → M3.3 → M3.4 → M3.5b → M3.6 → M3.7. | PLAN-M3 §1.2 |
| DEC-M3-12 (modified) | **Pi 4 support.** Universal defaults at MVP. Platform-aware tuning deferred to M3.4 outcome. | AMD-43 §3.6.6 |
| DEC-M3-13 | **Integration-test module placement.** `testing:integration-tests` module. Created in M3.4a (2026-05-19). | PLAN-M3 §8.2 |
| DEC-M3-14 | **Writer queue depth observation.** Via IntSupplier injection at construction time. Overrides PLAN-M3 §7.2/§7.9. | M3.3 deliberation; Nick-approved 2026-05-17 |
| DEC-M3-15 | **M3.5a STOP gate removal pattern.** Remove gate where gated component is independently testable without StateProjection. Test: can type be exercised with mock subscribers + injected deps? If yes → gate removed. | M3.2 precedent; formalized M3.3 |

### Composition Root Visibility (DEC-M3-16, DEC-M3-17)

| ID | Decision | Source |
|---|---|---|
| DEC-M3-16 | **Composition-root visibility strategy.** InProcessEventBus → promoted public (M3.6b, `df2743a`). SqlitePersistenceLifecycle → requires public factory (ships M3.6d-b). QueueSaturationHealthCheck → promoted public (M3.6d-a, `25bc23b`). | PM decision 2026-05-20 |
| DEC-M3-17 | **HealthSignal + HealthLevel public visibility** (DEC-M3-16 addendum). 3-type promotion chain because constructor's `Consumer<HealthSignal>` leaks both types under -Xlint:exports. Pattern: pre-promotion must check transitive type closure. | Implementation discovery M3.6d-a; ratified 2026-05-20 |

---

## Sub-decisions referenced inline (for completeness)

These are scoped sub-decisions within LTD-19's amendment history. They are not top-level locked decisions but are referenced in code and MODULE_CONTEXTs.

| ID | Context |
|---|---|
| DECIDE-02 | Replaced ulid-creator with hand-rolled UlidFactory (VT-safe). Within LTD-04. |
| DECIDE-M2-01 | Every DomainEvent record carries @EventType with explicit module-level registration. |
| DECIDE-M2-02 | EventTypeRegistry receives explicit class lists; builds immutable bidirectional map. |
| DECIDE-M2-03 | AttributeValue deserialized via custom JsonDeserializer discriminating by JSON token type. |
| DECIDE-M2-04 | Singleton ObjectMapper via PersistenceObjectMapper.create() with specified modules/features. |
| DECIDE-M2-05 | JacksonWarmup pre-builds ObjectReader/ObjectWriter for every registered event type before VT access. |
| DECIDE-M2-06 | Event payloads stored as writeValueAsBytes → SQLite BLOB. No String conversion. |
| DECIDE-M2-07 | DegradedEvent two-stage fallback: unknown type → immediate; known type + deser failure → raw bytes preserved. |
| DECIDE-M2-08 | Jackson pinned ≥2.18.2 (record introspection regressions in 2.18.0/2.18.1). |

---

## Build and Module Conventions (Hard Constraints)

These decisions exist outside the formal LTD register but are actively cited as hard constraints in MODULE_CONTEXTs, module-info.java source, and agent system prompts. Agents reference them by ID during code production.

| ID | Decision | Scope |
|---|---|---|
| DECIDE-04 | **No ServiceLoader.** Direct factory construction. IntegrationSupervisor accepts `List<IntegrationFactory>` at construction; application module assembles list explicitly. Overrides Doc 05 §3.10 for MVP. (2026-03-20, Block O) | integration-runtime, homesynapse-app, all integration modules. Affects composition root wiring (M3.6). |
| LD#10 | **`requires transitive` is the default** for all inter-module `requires` directives. Use non-transitive `requires` ONLY when you can confirm NO types from the required module appear in any record component, method parameter, return type, exception superclass, or throws clause in the module's exported API. Exception: homesynapse-app is the one module where LD#10 default does NOT apply (it is the terminal consumer). | All module-info.java files. Referenced in ≥6 MODULE_CONTEXTs. Most frequently cited constraint when writing module declarations. |
| DECIDE-01 | **SLF4J is always non-transitive.** `requires org.slf4j;` (non-transitive) + `implementation` scope in Gradle, because SLF4J types never appear in exported APIs. Pattern: LTD-15 / DECIDE-01. | lifecycle, persistence, state-store, event-bus module-info.java files. Cited when writing any module-info `requires` block. |

---

## Cross-Module Decisions (D-NN series)

These live in `context/decisions/phase-3-cross-module-decisions.md` and record implementation patterns discovered during Phase 3. They are orthogonal to the DEC-M3-NN ledger.

| ID | Decision | Date |
|---|---|---|
| D-01 | DomainEvent is permanently non-sealed (AMD-33). | 2026-04-10 |
| D-02 | Persistence module uses platform threads, not virtual threads. | 2026-04-10 |
| D-03 | Persistence module internals are package-private. | 2026-04-10 |
| D-04 | Clock must be injected everywhere outside app/platform/test whitelist. | 2026-04-11 |
| D-05 | Every event record and payload-carrying test double carries @EventType. | 2026-04-10 |
| D-06 | V001 schema may be amended pre-launch; no migration file cut for amendments. | 2026-04-10 |
| D-07 | Event categories derived at write time via EventCategoryMapping. | 2026-04-10 |
| D-08 | Visibility promotion requires transitive -Xlint:exports verification (DEC-M3-17). | 2026-05-20 |

---

*19 LTDs + 17 DEC-M3s + 3 build/module hard constraints (DECIDE-04, LD#10, DECIDE-01) + 9 inline sub-decisions + 8 D-NNs verified against source documents, system prompt hard constraints, and MODULE_CONTEXT references 2026-05-21. For full rationale, amendment history, implementation notes, and cross-references, read homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md.*
