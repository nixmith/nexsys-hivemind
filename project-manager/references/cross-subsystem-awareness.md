# Cross-Subsystem Awareness Guide

HomeSynapse Core consists of 13 subsystems that interact through defined interfaces. The PM must understand how subsystems connect so that work on one subsystem doesn't inadvertently break or constrain another. This guide maps the critical boundaries.

**Primary reference for cross-module contracts:** Each module's `MODULE_CONTEXT.md` file documents the behavioral contracts, consumers, and gotchas specific to that module. This guide provides the big-picture dependency map; MODULE_CONTEXT.md files provide the precise details. Always read both.

---

## 1. The Dependency Graph

This is the production order from MVP §9.3, with interface direction added.

```
                    ┌──────────────────────┐
                    │  01 Event Model &    │
                    │     Event Bus        │ ◄──── FOUNDATIONAL
                    └────┬─────┬─────┬────┘       Everything depends on this.
                         │     │     │             Get it right.
            ┌────────────┤     │     ├────────────────┐
            │            │     │     │                │
            ▼            ▼     │     ▼                ▼
    ┌──────────┐  ┌──────────┐ │  ┌──────────┐  ┌──────────┐
    │ 02 Device│  │ 05 Integ │ │  │ 06 Config│  │ 10 WS API│
    │ Model    │  │ Runtime  │ │  │ System   │  │          │
    └─┬──┬──┬──┘  └────┬─────┘ │  └─────┬────┘  └──────────┘
      │  │  │          │       │        │
      │  │  └──────┐   │       │        │
      │  │         │   │       │        │
      ▼  │         ▼   ▼       │        │
  ┌──────┴──┐  ┌──────────┐   │    ┌───┴──────┐
  │ 03 State│  │ 08 Zigbee│   │    │ 07 Auto- │
  │ Store   │  │ Adapter  │   │    │ mation   │
  └────┬────┘  └──────────┘   │    └────┬─────┘
       │                      │         │
       ▼                      │         │
  ┌──────────┐                │         │
  │ 04 Persi-│                │         │
  │ stence   │                │         │
  └──────────┘                │         │
                              │         │
            ┌─────────────────┘         │
            ▼                           │
    ┌──────────┐                        │
    │ 09 REST  │◄───────────────────────┘
    │ API      │
    └─────┬────┘
          │
    ┌─────┴────┐
    │ 11 Obser-│◄─── 03 State Store, 10 WS API
    │ vability │
    └─────┬────┘
          │
    ┌─────┴────┐
    │ 13 Web UI│
    └──────────┘

    ┌──────────┐
    │ 12 Life- │◄─── ALL preceding subsystems
    │ cycle    │
    └──────────┘

    ┌──────────┐
    │ 14 Master│◄─── ALL subsystems (synthesis document)
    │ Arch Doc │
    └──────────┘
```

---

## 2. Critical Interface Boundaries

These are the places where subsystems connect. When working on ANY subsystem, check whether you're near a boundary and what contracts govern it.

**For precise contract details, always read the relevant MODULE_CONTEXT.md files.** The summaries below provide orientation; the MODULE_CONTEXT.md Cross-Module Contracts sections provide the authoritative behavioral promises.

### Event Model ↔ Everything (the universal dependency)

Every subsystem produces and/or consumes events through the Event Model. The contracts that matter:

- **Event envelope schema (DD-01 §4.1):** The wire format every subsystem reads and writes. Changing the envelope breaks everything.
- **Event type taxonomy (DD-01 §4.3):** Each subsystem owns a namespace within the taxonomy. New event types must follow the naming rules and be registered.
- **Producer boundaries (DD-01 §3.1):** Strict partitioning of who can produce which event types. Integrations produce device events. Core services produce system events. Automations produce automation events. Violations break auditability.
- **CausalContext propagation (DD-01 §4.1):** Every event in a causal chain must carry correct correlation_id and causation_id. Breaking causality breaks the "why did this happen?" explainability guarantee (INV-ES-06).

**What to watch for:** Any subsystem that publishes events must use the `EventPublisher` interface with compile-time causality enforcement. Any subsystem that consumes events must handle `ProcessingMode` correctly (LIVE vs REPLAY behave differently).

**MODULE_CONTEXT.md reference:** See `core/event-model/MODULE_CONTEXT.md` Cross-Module Contracts for the full list of behavioral promises, including the synchronous publish guarantee and ProcessingMode side-effect rules.

### Event Bus ↔ Subscribers (the delivery contract)

- **Pull-based model:** The EventBus notifies subscribers, subscribers pull from EventStore. This is NOT push-based delivery.
- **CheckpointStore vs ViewCheckpointStore:** Subscriber position checkpoints (subscriberId → globalPosition) vs. state view checkpoints (viewName → position + data blob). Different tables, different interfaces, same database.
- **Coalesce exemptions:** State Projection and Pending Command Ledger must be coalesceExempt. Other subscribers may have DIAGNOSTIC events coalesced.

**MODULE_CONTEXT.md reference:** See `core/event-bus/MODULE_CONTEXT.md` Gotchas for the CheckpointStore confusion warning and coalesceExempt requirements.

### Device Model ↔ Integration Runtime

- **Discovery pipeline (DD-02 §3.12):** Integrations propose devices via `ProposedDevice`. The Device Model validates and adopts them. The handoff protocol is critical — the integration doesn't create devices directly.
- **Capability contracts (DD-02 §3):** Integrations must map protocol-specific data to standard capabilities. The `CapabilityRegistry` defines what capabilities exist. Custom capabilities use namespace isolation.
- **Hardware identifier matching (DD-02 §3.12):** Prevents duplicate devices on re-pairing. The Device Model owns the matching rules; the Integration Runtime executes them within integration scope.

**What to watch for:** An integration adapter must not bypass the discovery pipeline. It must not create entities directly. It must not invent capability types that aren't registered.

**MODULE_CONTEXT.md reference:** See `core/device-model/MODULE_CONTEXT.md` for the complete sealed Capability hierarchy (16 types, not 15), nullable field documentation, and EntityType MVP restrictions.

### Device Model ↔ State Store

- **Entity state shape:** The State Store materializes current state from events. It needs to know what attributes each entity type exposes (from the Device Model's capability definitions).
- **State projections:** When a `state_changed` event arrives, the State Store updates the materialized view. The projection logic must match the Device Model's capability attribute schemas.

**What to watch for:** If the Device Model changes an attribute schema, the State Store's projection must be updated to match. These must stay in sync.

### Event Model ↔ Persistence Layer

- **Write-ahead persistence:** The Event Model defines that events must be durable before subscriber notification. The Persistence Layer implements the actual SQLite WAL commit.
- **Domain event store schema (DD-01 §4.2):** The table structure is defined in the Event Model design doc. The Persistence Layer implements it.
- **Retention tiers (DD-01 §3.3):** Priority-based retention is defined by the Event Model (CRITICAL events retained longest). The Persistence Layer executes retention policy.
- **Telemetry boundary (DD-01 §3.5):** High-frequency telemetry goes to a separate ring store, NOT the domain event store. The Persistence Layer owns the ring store.

**What to watch for:** The Persistence Layer must not change the domain event store schema without updating the Event Model design doc. Retention execution must respect priority ordering.

### Automation Engine ↔ Event Model + Device Model + Configuration

The Automation Engine is the most cross-cutting subsystem after the Event Model:
- **Triggers** are event subscriptions (Event Model §3.4 subscription model)
- **Conditions** evaluate entity state (Device Model capabilities + State Store queries)
- **Actions** produce events (through EventPublisher, respecting producer boundaries)
- **Definitions** are YAML configuration (Configuration System)

**What to watch for:** Automation event production must follow the same causality rules as any other event producer. The Automation Engine must not bypass the EventPublisher to write directly to the event store. Loop detection is the Automation Engine's responsibility, not the Event Model's.

### REST/WebSocket API ↔ Everything

The API layer is the external interface. It must serialize internal types to JSON correctly:
- **ULID rendering:** Internal BLOB(16) → Crockford Base32 string at the API boundary (LTD-04)
- **Event envelope:** Full envelope serialization for event query endpoints
- **Device/Entity state:** Current state serialized with capability-defined attribute types
- **Configuration:** Config exposed through API must match YAML schema

**What to watch for:** The API layer must not expose internal implementation types. It serializes the public types defined in Phase 2. If an internal type changes, the API layer must not break — the Phase 2 interface types are the contract.

### Integration Runtime ↔ Core (the isolation boundary)

This is the most important boundary for reliability (INV-RF-01):
- **Integration API surface:** Integrations receive a composed set of narrow interfaces (`IntegrationContext`). They cannot access core internals.
- **Module boundary enforcement:** `modules-graph-assert` (Gradle) + ArchUnit (code) enforce that integration modules cannot import core-internal packages.
- **Thread isolation:** Each integration runs in its own virtual thread group (or platform thread for serial I/O). A crash or hang in one integration does not affect others.
- **Event production restrictions:** Integrations can only produce the event types permitted by Event Model §3.1.

**What to watch for:** Any coding instruction for an integration adapter must verify that the adapter only uses the `IntegrationContext` interfaces. Any test for an integration must include a crash isolation test (throw RuntimeException in the adapter, verify core continues operating).

---

## 3. The Shared Type Problem

Several types are used across multiple subsystems. These MUST be defined in a shared module, not redefined in each subsystem:

- **Typed ID wrappers:** `EntityId`, `DeviceId`, `EventId`, `AutomationId`, `PersonId`, `HomeId`, `AreaId` — defined in a shared identity module
- **EventEnvelope** and **CausalContext** — defined in the events API module
- **DomainEvent** sealed interface — defined in the events API module
- **Capability** sealed interface — defined in the device model API module
- **AttributeValue** sealed interface — defined in the device model API module

**Rule:** If a type is referenced by more than one subsystem, it belongs in a shared API module. If it's only used internally by one subsystem, it belongs in that subsystem's internal module.

**What to watch for:** The Coder may define a type locally that should be shared. If a type appears in an interface that another subsystem consumes, it must be in the shared module.

**MODULE_CONTEXT.md reference:** Each module's Complete Type Inventory section lists every public type, making it easy to verify whether a type already exists before creating a duplicate.

---

## 4. Cross-Subsystem Checklist

Before finalizing any work product, verify:

- [ ] The work doesn't change any interface consumed by another subsystem (or if it does, the change is intentional and the impact is traced)
- [ ] New event types follow the taxonomy naming rules and are registered
- [ ] New shared types are in the shared module, not defined locally
- [ ] Dependency direction is correct (core ← integration, never core → integration)
- [ ] CausalContext is propagated correctly through any event production chain
- [ ] The boundary between this subsystem and adjacent subsystems matches both subsystems' scope definitions (owns/does-not-own)
- [ ] **MODULE_CONTEXT.md files for affected modules are still accurate** — if this work changes cross-module contracts, update the relevant MODULE_CONTEXT.md files

---

## 5. Working on Subsystems Whose Dependencies Don't Exist Yet

In early Phase 2 and Phase 3, you may need to produce interface specs or coding instructions for a subsystem whose dependency is at Design-Locked but not yet implemented.

**Protocol:**
1. Reference the dependency's Locked design document for interface shapes
2. If the dependency's Phase 2 spec exists, use those exact interface definitions
3. **If the dependency's MODULE_CONTEXT.md is populated, read it** — it's faster and more precise than re-reading the full design doc + source files
4. If the dependency's Phase 2 spec does NOT exist, define the interface you need as a "consumed interface" and note that the dependency's Phase 2 must produce a compatible definition
5. Never mock the interface shape — use the actual interface from the shared API module, even if the implementation behind it doesn't exist yet

This is why the dependency graph matters: ideally, you're implementing subsystems in order, so dependencies are always ahead of dependents.

---

### JPMS Verification Checkpoint (M3.3 lesson)

**Before prescribing cross-module access patterns or making directive-level claims about module availability in a task instruction:**

1. Trace the target module's `module-info.java` chain to determine which modules are transitively available.
2. If the new code uses types from a JDK module (`jdk.jfr`, `java.sql`, `jdk.management`, etc.), verify that module is in the transitive closure. If not, the task instruction MUST prescribe adding `requires <jdk.module>;` to `module-info.java`.
3. Do NOT write "no requires needed" based on the module being a "JDK platform module" — that only means no Maven/Gradle dependency is needed. The JPMS `requires` directive is a separate concern.

**Origin:** M3.3 task instruction stated "Do NOT add `requires jdk.jfr`." This was a PM-originated error (the PM equated "platform module" with "auto-required"). The build failed on the first pass; the Coder corrected it. This checkpoint exists to force verification at the point where the PM makes JPMS claims, rather than relying on reference documents being consulted after the fact.
