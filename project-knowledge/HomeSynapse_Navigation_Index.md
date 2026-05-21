# HomeSynapse Core — Navigation Index

When working on any module or topic, use this index to find the exact files you need. Paths are relative to the repo root.

---

## Module Documentation Chains

Each module has up to five documentation layers. Read them in this order when working on a module.

### platform-api
- **MODULE_CONTEXT:** `homesynapse-core/platform/platform-api/MODULE_CONTEXT.md`
- **Design doc:** (covered by Doc 14 — Master Architecture)
- **Traceability:** `homesynapse-core/docs/traceability/14-master-architecture.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-f-platform-api.md`
- **Source package:** `platform/platform-api/src/main/java/com/homesynapse/platform/`
- **Amendments:** None directly; identity types referenced by many amendments

### event-model
- **MODULE_CONTEXT:** `homesynapse-core/core/event-model/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/01-event-model-and-event-bus.md`
- **Traceability:** `homesynapse-core/docs/traceability/01-event-model.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-b-event-envelope.md`, `block-d-publisher-store.md`
- **Source package:** `core/event-model/src/main/java/com/homesynapse/event/`
- **Amendments:** AMD-01 (publish durability), AMD-04 (cascade depth in causal chain), AMD-06 (write contention), AMD-18 (causal chain timeout), AMD-19 (retention priority), AMD-28 (write path VT threading), AMD-33 (DomainEvent non-sealed), AMD-35 (persistent idempotency key on EventDraft)

### event-bus
- **MODULE_CONTEXT:** `homesynapse-core/core/event-bus/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/01-event-model-and-event-bus.md` (shared with event-model)
- **Traceability:** `homesynapse-core/docs/traceability/01-event-model.md` (shared)
- **Handoff:** `homesynapse-core/docs/handoff/block-e-event-bus.md`
- **Source package:** `core/event-bus/src/main/java/com/homesynapse/event/bus/`
- **Amendments:** (inherits AMD-01, AMD-06 via event-model), AMD-26 (subscriber VT threading in LTD-11), AMD-42 (subscriber lifecycle and isolation), AMD-43 (backpressure and observability)

### device-model
- **MODULE_CONTEXT:** `homesynapse-core/core/device-model/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/02-device-model-and-capability-system.md`
- **Traceability:** `homesynapse-core/docs/traceability/02-device-model.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-g-device-model.md`
- **Source package:** `core/device-model/src/main/java/com/homesynapse/device/`
- **Amendments:** AMD-17 (device orphan lifecycle), AMD-23 (cross-protocol identity)

### state-store
- **MODULE_CONTEXT:** `homesynapse-core/core/state-store/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/03-state-store-and-state-projection.md`
- **Traceability:** `homesynapse-core/docs/traceability/03-state-store.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-h-state-store.md`
- **Source package:** `core/state-store/src/main/java/com/homesynapse/state/`
- **Amendments:** AMD-01 (publish durability for derived events), AMD-02 (REPLAY→LIVE reconciliation), AMD-03 (consistent multi-entity snapshot), AMD-10 (projection logic versioning), AMD-11 (state TTL for ephemeral sensors), AMD-29 (projection subscriber VT threading), AMD-38 (checkpoint policy — CheckpointPolicy interface), AMD-41 (state projection execution model)

### persistence
- **MODULE_CONTEXT:** `homesynapse-core/core/persistence/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/04-persistence-layer.md`
- **Traceability:** `homesynapse-core/docs/traceability/04-persistence.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-j-persistence.md`
- **Source package:** `core/persistence/src/main/java/com/homesynapse/persistence/`
- **Amendments:** AMD-05 (write endurance budget), AMD-06 (single-writer contention / WriteCoordinator), AMD-21 (WAL checkpoint strategy), AMD-27 (platform thread executor design), AMD-32 (persistence internal types — WriteCoordinator + WritePriority), AMD-34 (home_id schema reservation), AMD-35 (persistent idempotency key), AMD-36 (subscriber DLQ), AMD-37 (chain_hash NOT NULL), AMD-38 (checkpoint policy — WAL checkpoint side), AMD-39 (WITHDRAWN — journal_size_limit unchanged), AMD-40 (retention execution model)

### automation
- **MODULE_CONTEXT:** `homesynapse-core/core/automation/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/07-automation-engine.md`
- **Traceability:** `homesynapse-core/docs/traceability/07-automation.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-l-automation.md`
- **Source package:** `core/automation/src/main/java/com/homesynapse/automation/`
- **Amendments:** AMD-03 (positional snapshot for condition eval), AMD-04 (cascade detection/depth limiting), AMD-25 (temporal duration trigger modifier), AMD-31 (command execution order guarantees)
- **Additional:** `homesynapse-core-docs/design/amendments/AMD-25_Temporal_Duration_Trigger_Modifier.md` (separate file), `homesynapse-core-docs/design/amendments/AMD-31_Command_Execution_Order_Guarantees.md` (separate file), `homesynapse-core-docs/research/AUTOMATION_ENGINE_CRITICAL_REVIEW.md`

### configuration
- **MODULE_CONTEXT:** `homesynapse-core/config/configuration/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/06-configuration-system.md`
- **Traceability:** `homesynapse-core/docs/traceability/06-configuration.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-k-configuration.md`
- **Source package:** `config/configuration/src/main/java/com/homesynapse/config/`
- **Amendments:** AMD-13 (migration framework), AMD-16 (secrets store backup), AMD-20 (YAML parser safety), AMD-24 (reload atomicity)

### integration-api
- **MODULE_CONTEXT:** `homesynapse-core/integration/integration-api/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/05-integration-runtime.md` (shared with integration-runtime)
- **Traceability:** `homesynapse-core/docs/traceability/05-integration-runtime.md` (shared)
- **Handoff:** `homesynapse-core/docs/handoff/block-i-integration-api.md`
- **Source package:** `integration/integration-api/src/main/java/com/homesynapse/integration/`
- **Amendments:** AMD-14 (adapter dependency ordering)

### integration-runtime
- **MODULE_CONTEXT:** `homesynapse-core/integration/integration-runtime/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/05-integration-runtime.md` (shared with integration-api)
- **Traceability:** `homesynapse-core/docs/traceability/05-integration-runtime.md` (shared)
- **Handoff:** `homesynapse-core/docs/handoff/block-o-integration-runtime.md`
- **Source package:** `integration/integration-runtime/src/main/java/com/homesynapse/integration/runtime/`
- **Amendments:** AMD-14 (adapter dependency ordering / Kahn's algorithm)

### integration-zigbee
- **MODULE_CONTEXT:** `homesynapse-core/integration/integration-zigbee/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/08-zigbee-adapter.md`
- **Traceability:** `homesynapse-core/docs/traceability/08-zigbee-adapter.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-p-integration-zigbee.md`
- **Source package:** `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/`
- **Amendments:** AMD-07 (mesh route health monitoring)

### rest-api
- **MODULE_CONTEXT:** `homesynapse-core/api/rest-api/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/09-rest-api.md`
- **Traceability:** `homesynapse-core/docs/traceability/09-rest-api.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-m-rest-api.md`
- **Source package:** `api/rest-api/src/main/java/com/homesynapse/api/rest/`
- **Amendments:** AMD-08 (idempotency keys), AMD-12 (API key permission scoping), AMD-15 (correlation ID in errors)

### websocket-api
- **MODULE_CONTEXT:** `homesynapse-core/api/websocket-api/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/10-websocket-api.md`
- **Traceability:** `homesynapse-core/docs/traceability/10-websocket-api.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-n-websocket-api.md`
- **Source package:** `api/websocket-api/src/main/java/com/homesynapse/api/websocket/`
- **Amendments:** AMD-09 (rate limiting / reconnection), AMD-12 (API key scoping, shared with rest-api)

### observability
- **MODULE_CONTEXT:** `homesynapse-core/observability/observability/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/11-observability-and-debugging.md`
- **Traceability:** `homesynapse-core/docs/traceability/11-observability.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-q-observability.md`
- **Source package:** `observability/observability/src/main/java/com/homesynapse/observability/`
- **Amendments:** AMD-22 (alerting foundation)

### lifecycle
- **MODULE_CONTEXT:** `homesynapse-core/lifecycle/lifecycle/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/12-startup-lifecycle-shutdown.md`
- **Traceability:** `homesynapse-core/docs/traceability/12-lifecycle.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-r-lifecycle.md`
- **Source package:** `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/`
- **Amendments:** None

### homesynapse-app
- **MODULE_CONTEXT:** `homesynapse-core/app/homesynapse-app/MODULE_CONTEXT.md`
- **Design doc:** `homesynapse-core-docs/design/14-master-architecture-document.md`
- **Traceability:** `homesynapse-core/docs/traceability/14-master-architecture.md`
- **Handoff:** `homesynapse-core/docs/handoff/block-s-homesynapse-app.md`
- **Source package:** `app/homesynapse-app/src/main/java/com/homesynapse/app/`
- **Amendments:** None directly

### test-support
- **MODULE_CONTEXT:** `homesynapse-core/testing/test-support/MODULE_CONTEXT.md`
- **Source package:** `testing/test-support/src/main/java/com/homesynapse/test/`
- **No JPMS module-info** — consumed on classpath, not module path
- **Amendments:** None


### integration-tests
- **MODULE_CONTEXT:** `homesynapse-core/testing/integration-tests/MODULE_CONTEXT.md`
- **Source package:** `testing/integration-tests/src/test/java/com/homesynapse/integration/test/`
- **No JPMS module-info** — classpath-only test code, Pi-profile gated (`-PpiProfile=throttled`)
- **Tests:** `BurstLoadIT`, `HeapBudgetIT` (M3.4a), `Pi4SustainedLoadIT`, `Pi4D1SpikeIT`, `CrashRecoveryIT` (M3.4b), `ThrottledWriteCoordinatorTest` (unit)
- **Test harness:** `IntegrationTestHarness` (composes `PersistenceTestHarness` + `InProcessEventBusFactory`)
- **Amendments:** None
---

## Governance Documents

All in `homesynapse-core-docs/governance/`:

| Document | Purpose |
|----------|---------|
| `HomeSynapse_Core_Locked_Decisions.md` | Authoritative register of all implementation technology choices (LTD-01–LTD-19, LD#*, DECIDE-*) |
| `Architecture_Invariants_v1.md` | Constitutional constraints (INV-*). Cannot be violated. |
| `Design_Review_Amendments_v1.md` | All amendments AMD-01 through AMD-24 (inline). AMD-25 through AMD-43 + Tier 2 addendum in separate files. |
| `HomeSynapse_Core_v1_Project_MVP.md` | Project prompt: vision, competitive strategy, target audiences |
| `DAS_Consolidated_Reference_v1.md` | Documentation voice, tone, and writing standards |
| `Critical_Design_Review_Session_Synopsis.md` | Summary of the adversarial design review that produced the amendments |
| `phase-2-transition-guide.md` | Phase 2 entry criteria, JDK pins, license headers, Gradle baseline |
| `HomeSynapse_Core_Refined_Repo_Architecture_v2.md` | Repository structure research and rationale |
| `Doc_12_Cross_Audit_Report.md` | Cross-document consistency audit results |
| `Virtual_Thread_Risk_Audit_Report.md` | Analysis of virtual thread risks and mitigations |
| `DESIGN_DOC_TEMPLATE.md` | Template for new design documents |
| `Pre_Phase3_Context_Audit_Report_v1.md` | Context file integrity audit — 7 findings, all resolved in M0 |

---

## Research Artifacts

In `homesynapse-core-docs/research/`:

| Document | Purpose |
|----------|---------|
| `sqlite-wal-validation-spike-plan.md` | Fully specified spike plan with 5 core criteria + 3 VT criteria. Ready for execution on Pi 5. |
| `2026-03-21_architecture-benchmark-assessment.md` | Independent architecture stress test. 15 findings applied. |
| `AUTOMATION_ENGINE_CRITICAL_REVIEW.md` | Adversarial review of automation engine — 28 issues categorized, AMD-31 produced. 4 already addressed, 16 Phase 3 notes, 10 Tier 2 deferrals. |
| `2026-04-07_How_to_Build_Test_Suite_That_Proves_HomeSynapse_Architecture.md` | Competitive test suite analysis (HA, OpenHAB, Axon patterns). Testing strategy recommendations R-01–R-11. |
| `Device Model Architectures Across Smart Home Platforms.md` | Protocol abstraction research |
| `Language evaluation strategy and evolution.md` | Java/Rust/Go/Kotlin evaluation |
| `Web_UI_Framework_Research_v1.md` | SPA vs SSR analysis, Preact selection rationale |
| `Portability_Architecture_v1.md` | Cross-platform deployment, CI/CD matrix |
| `Repository_Structure_Test_Infrastructure_And_API_Evolution_Research_v1.md` | Monorepo structure, test patterns, API versioning |
| `contract-testing-for-event-sourced-smart-homes.md` | Contract test pattern research for event-sourced architectures |
| `2026-03-22_Unified_Cryptographic_Architecture_for_HomeSynapse.md` | Hash chain, package signing, envelope encryption + crypto-shredding design. Feeds AMD-37 (chain_hash NOT NULL). |
| `homesynapse-core-cloud-scalability-analysis.md` | Cloud-readiness & scalability deep dive. 5 friction points identified, all deferred with awareness. |
| `Research_Internalization_Report_Architecture_Gaps.md` | 7 research findings mapped to governance. 4 VALIDATED, 2 ANNOTATION, 1 TEST BACKLOG. Produced M2-bridge test scenarios. |
| `2026-03-22_Matter_Device_Conformance_Research_Plan.md` | Matter device spec-to-reality gap research plan. Validates INV-CE-04 integration architecture against Matter. |
| `2026-03-12_context-engineering-hivemind-optimization.md` | Hivemind context engineering optimization. Multi-agent coordination patterns. |
| `v003_snapshots_design_note.md` | V003 migration rationale: snapshots table, index redundancy, chain_hash decision, data contribution readiness |
| D1 WAL Pathology Validation Spike (results in AMD-38/39) | Empirical validation: continuous reader → 20.6 MB WAL; bounded reader → 3.97 MB WAL. Source: `homesynapse-core/spike/wal-validation/src/main/java/com/homesynapse/spike/wal/D1WalStarvationTest.java` |

---

## Amendments Quick Reference

### BLOCKING (applied — resolve before interface specs)
| AMD | Title | Affects |
|-----|-------|---------|
| 01 | EventPublisher.publish() Durability Contract | Doc 01, Doc 03 |
| 02 | REPLAY→LIVE Reconciliation Pass | Doc 03 |
| 03 | Atomic Multi-Entity State Snapshot | Doc 03, Doc 07 |
| 04 | Automation Cascade Detection and Depth Limiting | Doc 07, Doc 01 |
| 05 | Consolidated Write Endurance Budget | Doc 04 |
| 06 | Single-Writer Contention / WriteCoordinator | Doc 04, Doc 01 |
| 07 | Zigbee Mesh Route Health Monitoring | Doc 08 |
| 08 | REST API Idempotency Keys | Doc 09 |
| 09 | WebSocket Rate Limiting and Reconnection | Doc 10 |
| 10 | Projection Logic Versioning in Checkpoints | Doc 03 |

### REQUIRED (applied — resolve before implementation)
| AMD | Title | Affects |
|-----|-------|---------|
| 11 | State TTL for Ephemeral Sensors | Doc 03 |
| 12 | API Key Permission Scoping | Doc 09, Doc 10 |
| 13 | Configuration Migration Framework | Doc 06 |
| 14 | Integration Adapter Dependency Ordering (Kahn's) | Doc 05 |
| 15 | Correlation ID in REST API Errors | Doc 09 |
| 16 | Secrets Store Automatic Backup | Doc 06 |
| 17 | Device Orphan Lifecycle on Integration Removal | Doc 02 |

### RECOMMENDED (deferred for opportunistic application)
| AMD | Title | Affects |
|-----|-------|---------|
| 18 | Causal Chain Timeout Extension | Doc 01 |
| 19 | Emergency Retention Priority Refinement | Doc 01 |
| 20 | YAML Parser Safety Configuration | Doc 06 |
| 21 | WAL Checkpoint Strategy Storage Awareness | Doc 04 |
| 22 | Observability Alerting Foundation | Doc 11 |
| 23 | Cross-Protocol Device Identity Resolution | Doc 02 |
| 24 | Configuration Reload Atomicity Clarification | Doc 06 |

### Separate files
| AMD | Title | Location |
|-----|-------|----------|
| 25 | Temporal Duration Trigger Modifier | `homesynapse-core-docs/design/amendments/AMD-25_Temporal_Duration_Trigger_Modifier.md` |
| 26 | sqlite-jdbc VT Carrier Pinning Mitigation | `homesynapse-core-docs/design/amendments/AMD-26_sqlite_jdbc_VT_Carrier_Pinning_Mitigation.md` |
| 27 | Persistence Layer Platform Thread Executor Design | `homesynapse-core-docs/design/amendments/AMD-27_Persistence_Layer_Platform_Thread_Executor.md` |
| 31 | Command Execution Order Guarantees | `homesynapse-core-docs/design/amendments/AMD-31_Command_Execution_Order_Guarantees.md` |
| 32 | Persistence Internal Types (WriteCoordinator + WritePriority) | `homesynapse-core-docs/design/amendments/AMD-32_Persistence_Internal_Types.md` |
| 33 | DomainEvent Permanently Non-Sealed | `homesynapse-core-docs/design/amendments/AMD-33_DomainEvent_Permanently_NonSealed.md` |
| 34 | Home Identity Schema Reservation | `homesynapse-core-docs/design/amendments/AMD-34_Home_Identity_Schema_Reservation.md` |
| 35 | Persistent Idempotency Key | `homesynapse-core-docs/design/amendments/AMD-35_Persistent_Idempotency_Key.md` |
| 36 | Subscriber Dead-Letter Queue | `homesynapse-core-docs/design/amendments/AMD-36_Subscriber_Dead_Letter_Queue.md` |
| 37 | Chain Hash NOT NULL with Zero Default | `homesynapse-core-docs/design/amendments/AMD-37_Chain_Hash_Not_Null_With_Zero_Default.md` |
| 38 | Checkpoint Policy Revision | `homesynapse-core-docs/design/amendments/AMD-38_Checkpoint_Policy_Revision.md` |
| 39 | Journal Size Limit Revision (WITHDRAWN) | `homesynapse-core-docs/design/amendments/AMD-39_Journal_Size_Limit_Revision.md` |
| 40 | Retention Execution Model | `homesynapse-core-docs/design/amendments/AMD-40_Retention_Execution_Model.md` |
| 41 | State Projection Execution Model | `homesynapse-core-docs/design/amendments/AMD-41-state-projection-execution-model.md` |
| 42 | Subscriber Lifecycle and Isolation | `homesynapse-core-docs/design/amendments/AMD-42-subscriber-lifecycle-and-isolation.md` |
| 43 | Backpressure and Observability | `homesynapse-core-docs/design/amendments/AMD-43-backpressure-observability.md` |
| — | M2-Bridge Tier 2 Schema Reservations | `homesynapse-core-docs/design/amendments/AMD-M2Bridge_Tier2_Schema_Reservations.md` |

### CRITICAL (VT Risk Audit — applied 2026-03-21)
| AMD | Title | Affects |
|-----|-------|---------|
| 26 | sqlite-jdbc VT Carrier Pinning Mitigation | LTD-01 (reversal criteria), LTD-03 (executor pattern), LTD-11 (subscriber threading) |
| 27 | Persistence Layer Platform Thread Executor Design | Doc 04 |
| 28 | Event Model Write Path and Performance Targets | Doc 01 |
| 29 | State Store Projection Subscriber Threading | Doc 03 |
| 30 | Jackson ObjectMapper Warm-up | LTD-08 |

AMD-27 through AMD-30 are downstream amendments established by AMD-26. They do not have individual standalone amendment files — their specifications are embedded in AMD-26's downstream dependencies section and in the design doc sections they amend (Doc 04, Doc 01, Doc 03, LTD-08 respectively).

### CONTRACT-LEVEL (M0 — applied 2026-04-04)
| AMD | Title | Affects |
|-----|-------|---------|
| 31 | Command Execution Order Guarantees | Doc 07 §3.9, §3.11.1 |

AMD-31 establishes three ordering invariants for command execution: sequential within a Run, ULID ascending for multi-target actions, log-order dispatch.

### CONTRACT-LEVEL (M1.8 — applied 2026-04-09)
| AMD | Title | Affects |
|-----|-------|---------|
| 32 | Persistence Internal Types (WriteCoordinator + WritePriority) | Doc 04 §8.7 |

AMD-32 formally specifies the package-private WriteCoordinator interface and WritePriority enum for internal write serialization in the persistence module.

### CONTRACT-LEVEL (M2.1 — applied 2026-04-10)
| AMD | Title | Affects |
|-----|-------|---------|
| 33 | DomainEvent Permanently Non-Sealed | Doc 01 §8.2, LTD-19 |

AMD-33 makes DomainEvent permanently non-sealed due to JEP 409 JPMS cross-module sealed permit restrictions. Type discrimination uses @EventType annotation + EventTypeRegistry.

### CONTRACT-LEVEL (M2-bridge — applied 2026-05-02)
| AMD | Title | Affects |
|-----|-------|---------|
| 34 | Home Identity Schema Reservation | Doc 04 §4 |
| 35 | Persistent Idempotency Key | Doc 01 §4.1, Doc 04 §4, AMD-08 |
| 36 | Subscriber Dead-Letter Queue | Doc 01 §3.5, Doc 04 §4 |
| 37 | Chain Hash NOT NULL with Zero Default | Doc 04 §4 |

AMD-34 through AMD-37 are the M2-bridge structural hardening amendments. They expanded V001 from 17 to 25 columns, added V002 (DLQ table), expanded EventDraft from 8 to 9 fields, and established the schema reservation pattern. The Tier 2 Schema Reservations addendum (informational, not contract-level) documents 6 zero-cost reserved columns.

### CONTRACT-LEVEL (M2→M3 bridge — 2026-05-15)
| AMD | Title | Status | Affects |
|-----|-------|--------|---------|
| 38 | Checkpoint Policy Revision | APPLIED | Doc 03 §9 (200 events / 2 s, validated by D1 spike) |
| 39 | Journal Size Limit Revision | WITHDRAWN | LTD-03 (proposed 64 MB raise unnecessary — D1 Run 3 demonstrated bounded reader at 6 MB suffices) |
| 40 | Retention Execution Model | APPLIED | Doc 04 §3.4 (writer executor, interval-based, bounded chunks) |

AMD-38 promotes Doc 03 §9's checkpoint configuration from (5 min, 1000 events, 30 s min) to (2 s max, 200 events, 1 s min). Empirically validated by the D1 WAL Pathology Validation Spike (2026-05-15) — the 2 s `max_interval_seconds` is the load-bearing safety mechanism that forces the State Projection's read transaction to close on a known cadence so wal_checkpoint can advance. The active 30 s PASSIVE checkpoint cycle is retained as defense-in-depth against degraded projections; D1 showed it is redundant under nominal load.

AMD-39 was WITHDRAWN: D1 Run 3 demonstrated the bounded-window reader pattern keeps the WAL at ~4 MB peak under the existing 6 MB ceiling, so the proposed 64 MB raise is unnecessary. LTD-03's journal_size_limit value is unchanged at 6,144,000 bytes. `DeploymentProfile.{STUDIO, HOME, PERFORMANCE}.journalSizeLimitBytes()` all return the uniform 6 MB value.

AMD-40 governs the MaintenanceSubscriber's execution model: all purge work runs on the persistence write executor (AMD-26/27 compliance), interval-based scheduling (6-hour default, not nightly cron), bounded 1,000-row chunks with ≤ 2 s lock-hold per chunk, storage-pressure-triggered runs respect the same chunk discipline.

### TIER-1 (M3 governance — applied 2026-05-16)
| AMD | Title | Status | Affects |
|-----|-------|--------|---------|
| 41 | State Projection Execution Model | APPLIED | Doc 03 §3.2 (two-phase READ/PUBLISH/CHECKPOINT, SelfProducedFilter, projectionVersion reconciliation) |
| 42 | Subscriber Lifecycle and Isolation | APPLIED | Doc 01 §3.4 (5-state FSM, REPLAY→TRANSITION→LIVE, INV-SUB-ISO-01..06 catalog, per-subscriber resources) |
| 43 | Backpressure and Observability | APPLIED | Doc 01 §3.6, Doc 11 (non-blocking publish INV-BUS-02, 7 bus metrics, QueueSaturationHealthCheck, DerivedWriteRateLimit 200/s) |

AMD-41/42/43 are the M3 governance amendments that translate DEC-M3-01 through DEC-M3-12 into design-doc deltas. They add 14 new architectural invariants in 4 categories (BUS, PROJ, WRITER, SUB-ISO) to Architecture_Invariants_v1.md §19. Separate amendment files in `homesynapse-core-docs/design/amendments/`.

---

## Locked Decision Quick Reference

| ID | Title | Key Constraint |
|----|-------|---------------|
| LTD-01–LTD-18 | See Locked Decisions register | Core technology stack |
| LTD-19 | Event Payload Serialization via EventTypeRegistry + PersistenceJacksonModule | Registry-based type resolution, custom AttributeValue serde, pre-warming, DegradedEvent fallback. Extends LTD-08. |

---

## Foundational References

In `homesynapse-core-docs/foundations/`:
- `HomeSynapse_Core_v1_Glossary.md` — Canonical term definitions
- `HomeSynapse_Identity_and_Addressing_Model_v1.md` — Full identity model specification

---

## Source Repo Cross-Cutting Files

In `homesynapse-core/`:
- `CONTEXT.md` — Root project orientation
- `docs/ARCHITECTURE.md` — Architecture overview with dependency diagram
- `docs/TESTING.md` — Test strategy, categories, conventions, and test-support fixtures
- `docs/decisions/0001-adr-adoption.md` — ADR adoption record (+ template)
- `build-logic/` — Gradle convention plugins (4 files: java-conventions, library-conventions, test-fixtures-conventions, application-conventions)
- `specs/` — OpenAPI and AsyncAPI specifications (skeletons)
- `spike/` — Throwaway spike code (never reference as authoritative). Notable: `spike/wal-validation/` includes the D1 WAL Pathology Validation Spike (D1WalStarvationTest.java) whose results drove AMD-38 APPLIED and AMD-39 WITHDRAWN.
- `.github/workflows/ci.yml` — GitHub Actions CI (`./gradlew check` on push/PR)
- `build.gradle.kts` (root) — `modules-graph-assert` dependency direction enforcement rules

---

## Build Commands

```bash
./gradlew check                        # compile + test + Spotless + architecture checks + dependency rules
./gradlew build                        # full build including JARs
./gradlew test                         # unit tests only
./gradlew :core:event-model:test       # single module test
```
