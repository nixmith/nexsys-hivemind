<!--
file: project-knowledge/Decisions_Quick_Reference.md
purpose: Token-efficient index of all locked technical decisions (LTD-01..19) and Phase 3 milestone decisions (DEC-M3-01..17). Agents use this for constraint lookup; full text lives in homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md for JIT reading when detail is needed.
audience: All (PM, Coder, Cowork)
update-cadence: per-milestone (LTD changes rare; DEC-M3 grows with milestones)
state-type: reference
status: CURRENT
freshness-tier: COLD
last-verified: 2026-06-13 — **M6 3-of-4 COMPLETE (`7c73c91`); M6 execution rulings + the M7 decided ground (DQ-1/2/3/5) + B2 C8/C9 (PROPOSED) + the AMD-88..93 PM defaults (PROPOSED, bundled review READY) added as new sections.** _Prior:_ 2026-06-07 — **M5-A COMPLETE (`7f44bed`) + M5-B/B1 DONE (Doc 15 Cryptographic Architecture LOCKED; AMD-86 + AMD-87 RATIFIED; watermark AMD-87)**. Added the **M5-window decision block** (D1–D8; D2 crypto MVP scope; Doc 15; AMD-86 INV-PD-07/03 amendment; AMD-87 Expectation codec RATIFIED+IMPLEMENTED → M9 prereq cleared). LTD/DEC-M3/D-NN content unchanged from the 2026-05-27 verification (19 LTDs, 17 DEC-M3s, 12 D-NNs). Prior spine state: `8ef9e9f` (M4 COMPLETE, watermark AMD-64).
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
| D-09 | M3.7 closed OR-M3-17/OR-M3-18 with the interim `MinimalProjectionAdvancer`. **Fulfilled in M4.0b-1** (`cf1a97e`, 2026-05-29): `MinimalProjectionAdvancer` **deleted**, replaced by the production `DispatchingProjectionAdvancer` (REC-28) + `ProductionDerivationRule`, both package-private in state-store. | 2026-05-22 (fulfilled 2026-05-29) |
| D-10 | M3.7 absorbs M3.6f-shaped pre-work (HTTP IT for endpoints + DLQ `oldestParkedAt` field plumbing). No separate M3.6f WU. | 2026-05-22 |
| D-11 | M3.7 proceeds in parallel with M4-amendment-deliberation window (zero technical coupling). Gate removed from pm-handoff. | 2026-05-22 |
| D-12 | M3.7 uses the established M3.6 Claude Code workflow (no protocol changes). Codifies M3.6 cadence as default for all future milestones. | 2026-05-22 |

---

## Device-Model Attribute-Value Expansion (AMD-47, RATIFIED 2026-05-30)

Locked decisions carried by AMD-47 (full contract: `homesynapse-core-docs/design/amendments/AMD-47_AttributeValue_Expansion_and_Upcaster.md`; invariants AMD-47-INV-01..05 in `Architecture_Invariants_v1.md` §20):

| Decision | Detail |
|---|---|
| **`AttributeType.QUANTITY` added (fork resolved)** | 1:1 value↔type mapping preserved — each value variant has its own `AttributeType` classifier so exhaustive `switch(attributeType())` stays total (AMD-51 typed comparator + `AttributeValidator` branch on the unit-dimensional case without down-casting). The FLOAT-reuse alternative was rejected. |
| **Hand-rolled `String` units, no JSR 385 (REC-93)** | `QuantityValue(double value, String unit)` normalizes to canonical unit at construction via a pure, deterministic, table-driven conversion — **no `javax.measure`/units library** (confirmed against `libs.versions.toml`). Supersedes the deferred-JSR-385 plan permanently (AMD-47-INV-03). |
| **`AttributeValueUpcaster` SPI — no ServiceLoader** | Constructor injection, consistent with DECIDE-04 / REC-28. Strict mode (core projections) halts on failed upcast; lenient mode (forensic) yields `DegradedAttributeValue`. |
| **Watermark (at AMD-47 ratification)** | AMD-47's own ratification did not raise the ceiling (47 < 50). The on-disk watermark was later **raised to AMD-51** at AMD-51's ratification. |
| **IMPLEMENTED** | The three records + `AttributeValueUpcaster` SPI + 3 `AttributeType` constants + §5 contract tests shipped in **M4.B3** (`60b4185`, 2026-05-30); the 8-variant `permits` clause is live in source. |

---

## Typed Change-Detection Comparator (AMD-51, RATIFIED + IMPLEMENTED, M4.0b-3 `98f705b`)

Locked decisions carried by AMD-51 (full contract: `homesynapse-core-docs/design/amendments/AMD-51_Typed_AttributeValue_Change_Detection_Comparator.md`; invariants AMD-51-INV-01..05 in `Architecture_Invariants_v1.md` §21):

| Decision | Detail |
|---|---|
| **External comparator in state-store, not a method on `AttributeValue` (AMD-51-INV-04 / DP-A)** | `AttributeValueComparator` interface + pkg-private `StructuralAttributeValueComparator`, reached via the `AttributeValueComparator.structural()` DEC-M3-16 gateway. Carries a `ComparisonPolicy` (epsilon) — kept out of the device-model data layer. |
| **Exhaustive `switch`, no `default` (AMD-51-INV-01 / DP-B)** | Per-variant dispatch over the sealed 8-variant `AttributeValue` with **no `default` arm** — a future 9th permit MUST break compilation. (D-01 is event-type-scoped; an `AttributeValue` exhaustive switch is permitted.) |
| **Pinned total-form epsilon `1e-9` (AMD-51-INV-02 / DP-D)** | `changed ⟺ |a−b| > max(absEps, relEps·max(|a|,|b|))`, defaults `absEps = relEps = 1e-9`, with full IEEE-754 totality (`Inf−Inf` handled before the arithmetic; `−0.0`/`+0.0` canonicalised). Quantity is canonical-magnitude epsilon + canonical-unit dimension check — **no unit work in the comparator** (AMD-47 canonicalises at construction). |
| **Symmetric both-sides reconstruction (AMD-51-INV-05 / DP-H)** | Both operands reconstruct to the schema-declared variant before compare; the materialized prior is always a `StringValue`, so it is reconstructed too. Distinct from the `AttributeValueUpcaster` SPI (left unchanged). Produced typed values are transient. |
| **Schema source = `StandardCapabilities`, immutable injected snapshot (DP-K)** | Production `StandardCapabilities` (device-model **main**) aggregates the standard capability `AttributeSchema`s; `HomeSynapseCore` injects an immutable `Map`-backed `AttributeSchemaResolver` — NOT a live registry read (AMD-50-INV-03 determinism preserved). `TestCapabilityFactory` delegates to it. |
| **String `StateChangedEvent` payload preserved at M4.0b-3 (DP-G / §2.7)** | At AMD-51 the emitted payload stayed String `oldValue`/`newValue`. **This staging was lifted by AMD-52 (M4.0b-4b, `72596cb`): the payload is now typed `AttributeValue` with a tagged-union codec — see the M4-completion block below.** |
| **`projectionVersion` 2→3 (DP-I)** | Bumped at `HomeSynapseCore`; rides AMD-50's reconciliation-backfill unchanged. |
| **§2.6 erratum — missing-schema → `StringValue` string-compare fallback (D-1)** | When no `AttributeSchema` is known for the key, both operands reconstruct as `StringValue` and the comparator does an exact string compare — NOT Degraded/no-emit (which would freeze unschematized attributes). Preserves M4.0b-2 behaviour + the no-arg `production()` gateway. Erratum applied to AMD-51 §2.6 (2026-05-31). |
| **Watermark (was AMD-51 at this block)** | Raised AMD-50 → AMD-51 at AMD-51 ratification; **subsequently raised to AMD-64** through AMD-52/53 and the AMD-54..64 integration block (M4 COMPLETE). |

---

## M4 Completion — Workstream A finish, Device-Model breadth, Integration Freeze (2026-06-05, watermark AMD-64)

Decisions/amendments locked after the AMD-51 block (full contracts in `homesynapse-core-docs/design/amendments/`; invariants in the Invariants quick-ref §22–§34):

| Decision / amendment | Detail |
|---|---|
| **AMD-52 — typed `StateChangedEvent` payload (IMPLEMENTED, M4.0b-4b `72596cb`)** | `oldValue`/`newValue` String→`AttributeValue`; a custom non-reflective `{"t","v"[,"u"]}` tagged-union codec in persistence (no `@JsonTypeInfo`); bit-anchored float identity; per-event `schema_version` 1→2 discriminator with **no row migration**; Path-B legacy reads → `DegradedEvent`; typed `CheckpointSerializer` envelope; `projectionVersion` 3→4. AMD-52-INV-01..07 §22. |
| **AMD-52 §11 erratum — `AttributeValue` relocation (M4.0b-4a `971cfa1`)** | The sealed `AttributeValue` hierarchy (8 variants) + `AttributeType` moved device-model → new **`core/value-model`** leaf (`com.homesynapse.value`) to break the JPMS event↔device cycle the typed payload created. `AttributeSchema`/`AttributeValueUpcaster` stayed in device-model. Behaviour-preserving. |
| **AMD-53 — timestamp-model unifier (IMPLEMENTED, M4.0b-5 `c99b425`)** | All three `EntityState` activity timestamps (`lastChanged`/`lastUpdated`/`lastReported`) sourced from `eventTime ?? ingestTime` in every projection path; `staleAfter`/`stale` are the sole real-time-clock carve-out; `projectionVersion` 4→5. AMD-53-INV-01/02 §23. **Workstream A complete — typed end-to-end + event-time-deterministic.** |
| **AMD-44 — Floor aggregate + EntityRole (IMPLEMENTED, M4.B-S1 `e73e199` / M4.B-S2 `e76b925`)** | `Floor`/`Area` records + `FloorRegistry`/`AreaRegistry` interfaces; `EntityRole` enum (PRIMARY/DIAGNOSTIC/CONFIG) + `EntityType` 6×3 legality matrix; `Entity` 11→12 / `ProposedEntity` 3→4 with construction-time matrix guard; `hardwareIdentifiers` `List`→`Set`. **Workstream B complete.** |
| **AMD-54..64 — integration-api interface freeze (RATIFIED + FROZEN, M4.C `8ef9e9f`)** | integration-api 22→40 types; descriptor 8→14, context 10→12, RequiredService 3→5, lifecycle permits 5→10 + 2 capability events; code-bearing `PermanentIntegrationException`, `SecurityServices`/`CredentialRotator`, `HealthDetail`, capability events/publisher, outcome enums. Contract-only; **supervisor impl = M9.** 29 invariants §24–§34. One DOCS-Project block review caught AMD-56's unimplementable trigger + AMD-55's void-reauth. **Workstream C → M4 complete.** |
| **AMD-65 → reassigned AMD-87 — `Expectation` persisted codec (RATIFIED + IMPLEMENTED, M5-A Part 2 `7f44bed`)** | Interface-keyed tagged-union codec over the 4 permits; `ExactMatch`/`AnyChange` delegate to the existing `AttributeValue` codec, `WithinTolerance` reuses the AMD-52 bit-anchored-float helpers; the lone JPMS change is `persistence requires com.homesynapse.device` (acyclic). Command-bearing `CapabilityAdded` round-trips; the un-`@Disabled` acceptance test is GREEN. **M9 prerequisite CLEARED.** AMD-87-INV-01 §36. |
| **P2 — AMD renumbering (RATIFIED 2026-05-29)** | device 46–49, projection 50–52 fixed (gaps unused at 46/48/49); integration assigned-at-milestone → AMD-54..64 taken contiguously. AMD-65 RETIRED (→reassigned 87). M6 configuration amendments = AMD-66–71 — **authored 2026-06-08, ratified 2026-06-09 (66/67/68/70/71 RATIFIED; 69 DEFERRED Tier-2/OQ-15-3, number reserved); see the M6 block below.** |

**Watermark = AMD-64** at M4 COMPLETE. `projectionVersion` = 5. *(Subsequently raised to AMD-87 in the M5 window — see the next block.)*

---

## M5 Window — the M6 Entry-Gate Window (2026-06-06/07, watermark AMD-87)

The blended, lane-tracked M5 window (decisions **D1–D8**, full text `nexsys-hivemind/context/decisions/2026-06-06_post-M4_M5-window_decisions.md`):

| Decision / amendment | Detail |
|---|---|
| **D1 — M5 posture** | Charter M5 as a blended, multi-lane window (the "M6 entry-gate window"), **sized to Nick's review/ratification gate** (the binding constraint, not agent output), lane-tracked as 4 first-class pieces M5-A…M5-D (P1 — no single label hides the size). |
| **D2 — Crypto MVP scope (load-bearing)** | Build the per-scope key-management **infrastructure** + encryption-scope categories + at-rest encryption **at MVP**; **defer operational crypto-shredding** to its first cloud/institutional consumer (post-MVP). The sensitive-PII categories (identity, person-linked presence) are **envelope-encrypted-on-write under per-scope DEKs from MVP** — encrypt-on-write is now-or-never on the immutable log; the shred *operation* is deferrable. Reconciled via AMD-86 (full DOCS review). |
| **D3 — Non-Core floor** | The M5-C website/docs lane is a protected, **non-preemptable** floor (P6) — Core may not trade it away. |
| **D4 — Energy** | Author the **regret-proof energy event *shape* now**; build energy *features* only on real interview demand (shape-now, features-later). |
| **D5 — Language deliberation** | The GraalVM/GenZGC spikes + energy interviews ride the window as Lane D; the schema decisions are **regret-proof under both the stay-Java and go-Rust futures**, so the window doesn't wait on the LTD-01 language call. |
| **D6 / D7 / D8** | AMD-87 authored in the window (lightweight block-track); verification-foundation quick-scoped (don't rebuild existing test doubles); adopt process rules **P1** (lane-tracking) / **P2** (consumer-pin survey) / **P3** (ticked WUCP closeout) / **P6** (non-Core floor). |
| **Doc 15 — Cryptographic Architecture (LOCKED)** | The 15th design doc. Keyless **SHA-256 hash chain over stored bytes** (INV-PD-08, tamper-evidence independent of encryption + shredding); **application-level per-scope AES-256-GCM at-rest encryption** (NEVER whole-DB/SQLCipher — per-scope is the only mechanism that supports per-category crypto-shred); machine-local root key at MVP (zero-config → **partial** INV-PD-03: at-rest yes, user-owned-keys + media-theft resistance = Tier-2); **Ed25519** package signing. All crypto on the publishing VT before the single-writer INSERT (JDK-intrinsic — no JNI / carrier-pinning). Pi-4 budget: AES-256-GCM ~30–60 µs/event, ≥500 ev/s sustained (no ARM crypto extensions). |
| **AMD-86 — INV-PD-07 narrow + INV-PD-03 posture (RATIFIED 2026-06-07)** | Strikes INV-PD-07's "crypto-shredding operational for ≥1 category at MVP" clause (→ post-MVP, first cloud/institutional consumer); states the INV-PD-03 *partial*-at-MVP at-rest posture. **AMD-86-INV-01 §35:** encrypt-on-write is irreversible, the shred operation is deferrable. **The M5-D erasure interviews carry the §3 re-scope-up trigger** — a launch-window buyer requiring verifiable erasure re-opens AMD-86 (via the formal pipeline) before M6 freezes the write path. |
| **AMD-87 — `Expectation` persisted codec (RATIFIED + IMPLEMENTED, M5-A Part 2 `7f44bed`)** | See the M4-completion block above (reassigned from AMD-65). **M9 prereq cleared.** AMD-87-INV-01 §36. |
| **OR-M6-NONCE [BLOCKING-for-M6-impl]** | The per-scope GCM counter-nonce must be durable + strictly monotonic across crash AND restore, or (key,nonce) reuse breaks AES-GCM. Embed verbatim in the M6 at-rest-encryption WU; co-design with the deferred backup/restore. |

**Watermark = AMD-87.** `projectionVersion` = 5. **Next: M6 (Configuration + secrets/crypto)** — author/ratify **AMD-66–71** + the Doc 06 `SecretStore.setAll(Map)` currency amendment, resolve **OQ-15-2**, then charter M6 as multiple first-class pieces (P1). See `context/planning/weeks/2026-W24_jun08-jun14.md`. *(Done — see the M6 block below.)*

---

## M6 Config Block — AMD-66..71 RATIFIED/DEFERRED (2026-06-09, watermark unchanged AMD-87)

| Decision / amendment | Detail |
|---|---|
| **AMD-66 — `ConfigurationChangeListener` (RATIFIED 2026-06-09)** | Plain non-generic listener (F7-corrected — the REC-55 sealed-generic shape didn't compile); synchronous classification before the reload event publishes; composition-time registration, no `ServiceLoader`; **no-listener fallback = the locked per-property `x-reload` `PROCESS_RESTART` default ([AMD-66-A] review-ENDORSED over REC-55's `INTEGRATION_RESTART`)**. AMD-66-INV-01/02 §37. Impl M6.1; exercised M6.4. |
| **AMD-67 — config-document schema `(major, minor)` (RATIFIED 2026-06-09)** | `ConfigModel` 5→6 components; `ConfigMigrator` 3→5 methods; the AMD-54 idiom on an explicitly **distinct surface** (no code path derives one from the other); minor never migrates, major always. AMD-67-INV-01/02 §38. Impl M6.1. |
| **AMD-68 — `SecretStore.setAll(Map)` (RATIFIED 2026-06-09 — the Doc 06 currency amendment)** | All-or-nothing, durable-before-return multi-key write (write-temp → fsync → atomic-rename → fsync-dir on `secrets.enc`) — the store-layer guarantee beneath AMD-60-INV-03 (the M9 `CredentialRotator` writes through it); REC-57's bundle/`credentialsFor` retired by ratified AMD-60 (review-VERIFIED, no orphaned consumer). AMD-68-INV-01 §39. Impl M6.2. |
| **AMD-69 — passphrase-root KDF (DEFERRED 2026-06-09 — Option (a) confirmed)** | REC-58's Argon2id/BouncyCastle conflicts with Locked Doc 15 on 3 counts (§2.3 post-MVP; §3.5/§7.3 machine-local MVP root; §3.8 zero-MVP-deps + open OQ-15-3). Deferred to Tier-2/OQ-15-3 (BC vs PBKDF2 vs FFM — gated on the GraalVM C15 closed-world evidence); **the number stays reserved**; no invariant. |
| **AMD-70 — config observability events (RATIFIED 2026-06-09)** | `config.validation_completed` + `config.section_reloaded`, observability-only, flat `com.homesynapse.event` (NQ-5/AMD-52 precedent). **E70-1 (the review's load-bearing catch): payloads flattened to event-resident/`java.base` types under the type-residency rule** — config types consumed, never referenced (else `event→config`, the AMD-52 cycle class); now a standing JPMS lesson in the P2 consumer/pin survey. AMD-70-INV-01 §40. Impl M6.1 + M6.4 (survey re-run). |
| **AMD-71 — hybrid config directory layout (RATIFIED 2026-06-09)** | `${config_dir}` layout (root YAML + `integrations/` + `secrets.enc` + regenerable `schemas/` + `signing-key.pub`); one-level `!include`; canonicalization-based fail-closed traversal guard; **[AMD-71-A] ruled: composition-root `Path` injection (= M6.1 DP-3)** — no `config→platform` edge; the zero-new-edge property the E2 bridge depends on is preserved. AMD-71-INV-01/02 §41. Impl M6.1. |

**Watermark UNCHANGED at AMD-87** — all six were reserved-below-watermark slots; ratification fills them, it does not raise the ceiling. _Execution since (2026-06-10/11):_ **M6.1 COMPLETE (whole: `b7bc65c`+`9035110`) · M6.4 COMPLETE (`62a81e6`) · M6.2 COMPLETE (`7c73c91`) — M6.3 stays triple-gated (OQ-15-2 + AMD-86 §3 interview signal + OR-M6-NONCE).** Review return: `nexsys-hivemind/context/audits/2026-06-09_AMD-66-71_DOCS_Review_Return.md`.

## M6 Execution Rulings (2026-06-10/11 — PM-ruled or Nick-ruled at dispatch/review; binding on downstream work)

| Ruling | Detail |
|---|---|
| **Module-info ruling (Nick, 2026-06-10)** | The five **third-party non-transitive `requires`** on `com.homesynapse.config` (snakeyaml-engine/networknt are explicit JPMS modules; Gradle `implementation` scope does NOT exempt JPMS) + 2 Gradle lockstep lines. APPROVED — the AMD-66..71 §7 embeds carry ruling-correction notes |
| **GF-1 (M6.1a)** | Explicit `CoreSchema` on BOTH LoadSettings (engine default = JSON schema where `~` ≠ null; LTD-09) + ArchUnit Rule 5 drops `com.homesynapse.config..` per ratified AMD-71 (AMD-71-INV-01 containment = the compensating control) |
| **GF-1 (M6.4)** | `ConfigLayoutTest.composeAfterMerge` publish-count pin 1→2 per the ratified R1/DP-10 (implementation contract-correct, NOT changed; test updated). **Process yield: the P2 consumer/pin survey gained the behavioral publish-count-pin category** — every WU adding a publish site to an existing path re-runs it |
| **[R4] (M6.4 dispatch)** | reload publishes `config.section_reloaded` ONLY — the value-bearing `ConfigChangedEvent` stays registered-but-unpublished (Locked Doc 06 §12.4; reconciliation = the REC-138 FUTURE-AMD family) |
| **[R5] (M6.4 dispatch)** | `section_reloaded` publish metadata = DIAGNOSTIC / SYSTEM / null-eventTime / publishRoot / system-subject (the `validation_completed` ruling applied) |
| **[R6] (M6.2 dispatch)** | `scope_keys` = config-side `scope_keys.json` per Locked Doc 15 §3.8's ownership sentence (the §4.1 CREATE TABLE placement is structurally unreachable from config under zero-new-edge — Doc-15 currency nit parked) |
| **R-1 (M6.2 review)** | `write()` REJECTS `!secret`/`!env`-bearing documents fail-closed (resolving on write would bake plaintext secrets into the emitted file — INV-SE-03/LTD-15; leakage irreversible, restriction reversible). **NEW FUTURE-AMD queued: tag-preserving YAML emitter (post-MVP)**; M10 design-input note |
| **R-2 / R-3 (M6.2 review)** | `PersistenceFactory` untouched — extending the frozen gateway IS M6.3's wiring step; DP-6 discharged as `Main.payloadCipher` factory + 5-arg `HomeSynapseCore` ctor + bridge round-trip test (live bootstrap rides M13) |

## M7 Entry-Gate — Decided Ground + the PROPOSED Block (2026-05-30 → 2026-06-13)

**Nick-ruled decided ground (2026-05-30, v4 addendum — the AMD block consumes these as locked inputs; do NOT re-open):**

| DQ | Decision |
|---|---|
| **DQ-1** | **Promote `PresenceTrigger` (Tier 2→Tier 1); separate `ZoneTrigger` permit permanently REJECTED.** Promotion-designation registered in M7 (AMD-88 §2.4); geofence fields + evaluation land M8.1 |
| **DQ-2** | **Rename `ActivateSceneAction` → `InvokeAutomationAction` + promote to Tier 1** (scenes = automations-with-`ManualTrigger`; no scene primitive, ever) |
| **DQ-3** | **Pending Command Ledger projection handlers: SAME `DispatchingProjectionAdvancer`, separate handler registrations** (split into a dedicated advancer at M8 only if unmanageable) |
| **DQ-5** | **Zone/geofence scope = M8.** M7 trigger priorities: Webhook + Calendar + Reachability + Manual |

**B2 schema decisions (PROPOSED 2026-06-08 — ride the bundled review):** **C8** `actorRef` stays a bare nullable `Ulid`; four-kind closed set (PERSON/AUTOMATION/SYSTEM/API_CLIENT) recoverable by typed-ID provenance; Tier-1 API keys → API_CLIENT never PERSON; **automations MUST stamp `actorRef = AutomationId`** (the M7 contract input; R14-A Hubitat provenance evidence attached). **C9** energy SHAPE: four `power_measurement` attributes (W/Wh/V/A as `QuantityValue`) + six aggregate fields + ENERGY consent-scope; rides existing event types; breadth staged behind the M5-D interviews. C10 payload-typing posture consciously deferred. File: `nexsys-hivemind/context/decisions/2026-06-08_B2_schema_decisions_C8_C9.md`.

**The PROPOSED M7 block (AMD-88..93, 2026-06-13 — PM defaults stated for review confirmation; NOT yet binding):** F5 type-residency = **FLATTEN** (`RunId`→bare `Ulid`, `RunStatus`→`String` in payloads; relocation rejected — `RunId` is automation-internal by design) · ConfirmationPolicy named default = **BEST_EFFORT** (ledger iff Expectation present; never blocks Run completion; NO engine retry at any value — anti-req REC-162) · `includedRoles` binds the shipped **`EntityRole`** (the REC's `EntityCategory` never existed in source) · AMD-91 supersedes AMD-04 with an element ledger (rate-limiting clause NOT adopted — REC-168 owns that space) · `automations.yaml` migrations forward-only + idempotent + never destructive (anti-req REC-151) · no templating DSL anywhere (anti-req REC-155). Bundled review prompt: `nexsys-hivemind/context/instructions/2026-06-13_AMD-88-93_C8-C9_Bundled_DOCS_Review_Prompt.md`.

---

*19 LTDs + 17 DEC-M3s + 3 build/module hard constraints (DECIDE-04, LD#10, DECIDE-01) + 9 inline sub-decisions + 12 D-NNs verified 2026-05-27; M4 amendment-decision blocks (AMD-47/51/52/53/44/54-64) + the M5-window block (D1–D8, Doc 15, AMD-86/87) + the M6 block (AMD-66..71 + execution rulings) + the M7 decided ground (DQ-1/2/3/5) + B2 C8/C9 (PROPOSED) + the AMD-88..93 PM defaults (PROPOSED) — current to **M6 3-of-4 COMPLETE (`7c73c91`) / AMD-88..93 + C8/C9 in bundled review / watermark AMD-87 on disk** on 2026-06-13. For full rationale, amendment history, implementation notes, and cross-references, read homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md.*
