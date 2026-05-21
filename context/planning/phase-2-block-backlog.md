# Phase 2 Block Backlog — FROZEN

**FROZEN — Phase 2 Interface Specification complete 2026-03-20.**

This file is the historical record of all Phase 2 blocks (A–S, with T reclassified to Phase 3). Do not edit. Active Phase 3 tracking lives in `phase-3-milestone-backlog.md`.

Ordered list of Phase 2 implementation blocks. Each block was a single compile-and-commit unit. Details live in the handoff prompts (`docs/handoff/`).

**Status key:** DONE | NEXT | PLANNED | FUTURE (all effective statuses at Phase 2 close)

---

## Sprint 1 — Event Model, Event Bus, Platform API (Week 1)

| Block | Scope | Module | Design Doc | Status | Handoff Prompt |
|-------|-------|--------|------------|--------|----------------|
| A | Ulid value type, UlidFactory, 8 typed ID wrappers, SubjectRef | platform-api, event-model | Doc 01 §4.1, Identity Model | DONE | (predates template) |
| B | EventEnvelope, EventId, DomainEvent, DegradedEvent, CausalContext, 7 enums | event-model | Doc 01 §4.1, §3.3, §3.7, §3.9 | DONE | block-b-event-envelope.md |
| D | EventDraft, EventPublisher, EventStore, EventPage, SequenceConflictException | event-model | Doc 01 §8.3, §4.2, §3.4, §6.7 | DONE | block-d-publisher-store.md |
| E | SubscriptionFilter, SubscriberInfo, EventBus, CheckpointStore, module-info | event-bus | Doc 01 §3.4, §3.6, §8.1 | DONE | block-e-event-bus.md |
| F | PlatformPaths, HealthReporter | platform-api | Doc 12 §8.2, §8.3 | DONE | block-f-platform-api.md |
| — | 18 payload records + EventTypes | event-model | Doc 01 §4.3, §4.6 | DONE | (no handoff — direct from doc) |
| — | Javadoc quality pass + traceability doc + full compile gate | all | all | DONE | (no handoff — manual pass) |

## Sprints 2+3 — Device Model through Automation (Week 12b: Mar 16–22)

| Block | Scope | Module | Design Doc | Status | Handoff Prompt |
|-------|-------|--------|------------|--------|----------------|
| G | ~50 types: sealed Capability (14 standard + Custom), sealed AttributeValue, sealed Expectation, Device, Entity, 7 enums, 8 service interfaces | device-model | Doc 02 §3–4, §8 | DONE | block-g-device-model.md |
| H | StateQueryService, StateStoreLifecycle, EntityState, StateSnapshot, Availability, CheckpointRecord | state-store | Doc 03 §3, §8 | DONE | block-h-state-store.md |
| I | IntegrationFactory, IntegrationAdapter, IntegrationContext, CommandHandler, HealthReporter, 19 types | integration-api | Doc 05 §3.8, §4, §8 | DONE | block-i-integration-api.md |
| J | TelemetryWriter, TelemetrySample, TelemetryQueryService, PersistenceLifecycle, MaintenanceService, ~11 types + IntegrationContext update | persistence | Doc 04 §3, §8 | DONE | block-j-persistence.md |
| K | ConfigurationService, ConfigurationAccess, SecretStore, SchemaRegistry, ConfigModel, ~12 types | configuration | Doc 06 §3, §8 | DONE | block-k-configuration.md |
| L | 4 sealed hierarchies (Trigger/Condition/Action/Selector), AutomationRegistry, RunManager, PendingCommandLedger, 55 files | automation | Doc 07 §3–4, §8 + AMD-25 | DONE | block-l-automation.md |
| — | Javadoc quality pass + 6 traceability docs + full compile gate | all | all | PLANNED | (no handoff — manual pass) |

## Sprint 4 — APIs, Integration Runtime, Zigbee (Week 12b–13: Mar 20–22)

| Block | Scope | Module | Design Doc | Status | Handoff Prompt |
|-------|-------|--------|------------|--------|----------------|
| M | REST API infrastructure: ProblemDetail, EndpointHandler, AuthMiddleware, RateLimiter, command lifecycle types, pagination, 28 files | rest-api | Doc 09 §3–4, §8, §12 | DONE | block-m-rest-api.md |
| N | WebSocket session model, WsMessage sealed hierarchy (13 subtypes), backpressure model, subscription filters, 26 files | websocket-api | Doc 10 §3–5, §8 | DONE (2026-03-20) | block-n-websocket-api.md |
| O | IntegrationSupervisor, IntegrationHealthRecord, ExceptionClassification, SlidingWindow, 5 files | integration-runtime | Doc 05 §4–6, §8 | DONE (2026-03-20) | block-o-integration-runtime.md |
| P | ZCL frame model, device profile types, cluster handler interfaces, coordinator abstraction, adapter factory, 40 files | integration-zigbee | Doc 08 §4–6, §8 | DONE (2026-03-20) | block-p-integration-zigbee.md |

## Sprint 5 — Observability, Lifecycle, App Assembly (Week 5)

| Block | Scope | Module | Design Doc | Status | Handoff Prompt |
|-------|-------|--------|------------|--------|----------------|
| Q | HealthAggregator, HealthContributor, TraceQueryService, MetricsRegistry, MetricsStreamBridge, LogLevelController, 20 files | observability | Doc 11 §3–5, §7–8 | DONE (2026-03-20) | block-q-observability.md |
| R | LifecyclePhase, SubsystemStatus, LifecycleEventType, SubsystemState, SystemHealthSnapshot, SystemLifecycleManager — 8 files + cross-module observability fix | lifecycle | Doc 12 §3–6, §8 | DONE (2026-03-20) | block-r-lifecycle.md |
| S | App assembly: module-info.java (15 requires), ExitCode enum (5 values), package-info, build.gradle.kts update — 3 new files + 2 updated | homesynapse-app | Doc 14, Doc 12 | DONE (2026-03-20) | block-s-homesynapse-app.md |

## Reclassified to Phase 3

| Block | Scope | Module | Design Doc | Status | Handoff Prompt |
|-------|-------|--------|------------|--------|----------------|
| T | Cross-cutting test infrastructure: TestClock, TestIntegrationContext, NoRealIoExtension, SynchronousEventBus, GivenWhenThen DSL | test-support | Repo Architecture v2 §7.3–7.4 | Phase 3 step 3.1.3 | — |

---

## Notes

- Block C was absorbed into Block B during execution (CausalContext rewrite was combined with EventEnvelope)
- Handoff prompts are produced just-in-time: the prompt for Block G is written after Block F compiles
- Sprint boundaries are approximate — blocks may shift earlier if velocity continues ahead of plan
- Each block's handoff prompt is the authoritative spec; this backlog is the high-level roadmap only
- **Phase 2 declared complete 2026-03-20.** All 16 subsystem modules with production interfaces are specified, compiled, and documented. Block T reclassified to Phase 3 step 3.1.3 per Repo Architecture v2 §7.4 — test-support types are implementations, not interface specs.
