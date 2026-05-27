<!--
file: context/instructions/Research_3_Prompt.md
purpose: Self-contained prompt for Claude Project to produce Research 3.
audience: Claude Project (HomeSynapse Core)
state-type: ephemeral (consumed once, then the research document replaces it)
-->

# RESEARCH BRIEF: Research 3 — Integration Testing Patterns for Event-Sourced HTTP Systems

You are the research arm of the PM/architect team for HomeSynapse Core, a local-first event-sourced smart home runtime in Java 21 (Amazon Corretto, JPMS enforced, targeting Raspberry Pi 4/5 with 4 GB RAM). Your task is to produce a deep, opinionated research document that will directly inform the coding instructions for milestone M3.7 — the end-to-end integration test suite.

---

## Why This Research Matters

M3.7 is the next implementation milestone. It must exercise the **full subsystem graph** for the first time: SQLite event store → InProcessEventBus (replay/transition/live) → StateProjection → MaterializedStateQueryService → Javalin HTTP endpoints → JSON response → assertion.

No existing HomeSynapse test does this. The composition root (`HomeSynapseCore`) is a 16-step bootstrap sequence. E2E tests must:
1. Start the full `HomeSynapseCore` (all 16 steps)
2. Publish events through the `EventStore`
3. Wait for the bus to transition through REPLAY → TRANSITION → LIVE
4. Hit HTTP endpoints with a real HTTP client
5. Assert JSON responses reflect correctly projected state

This is not a "nice to have" — it is the verification that 16 weeks of subsystem implementation actually works end-to-end. The research must produce concrete, actionable patterns that the PM can translate directly into coding instructions.

---

## What You Must Produce

Follow this exact document structure. Non-negotiable sections are marked **[M]**; optional sections are marked **[O]**.

```
# Research 3: Integration Testing Patterns for Event-Sourced HTTP Systems

*Target: HomeSynapse Core M3.7. Date: YYYY-MM-DD.*

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
  - Ranked by (impact x confidence) / cost.
  - Each REC must include: Gap citation, Lesson source, Change (specific
    record/interface/event shape), Backward compat assessment, Effort estimate
    (in approximate lines of code).
  - REC-XX format. Numbered globally across all research documents.
    Research 2 used REC-01 through REC-12. This document starts at REC-13.

## 5. Caveats and Open Questions [M]
  - Source reliability notes.
  - Unresolved tensions between platforms.
  - Questions that require empirical validation (spike/prototype).

## 6. Appendix: Sources [M]
  - URL families grouped by platform.
  - Every factual claim must be traceable to a source listed here.

## 7. HomeSynapse Code-Level Implications [M — mandatory for this research]
  - Specific test classes, base test infrastructure, and helper types to create.
  - Module placement (which Gradle module do test classes live in?).
  - JPMS module-info impact (test module opens/requires).
  - Dependencies to add (Javalin test utils, HTTP client, assertion libraries).
  - Interaction with existing test infrastructure (IntegrationTestHarness,
    contract test suites, BurstLoadIT, CrashRecoveryIT).
```

---

## Specific Questions to Answer

Investigate each of the following. Every question must receive a verdict in your executive summary and detailed treatment in the body.

### Q1. Javalin 6.x Embedded Testing Patterns

Javalin 6.x ships with `JavalinTest`. What is its API? Does it start a real Jetty server on a random port, or does it mock the servlet layer? Can `JavalinTest` coexist with JPMS `module-info.java` (HomeSynapse enforces JPMS across all 20 modules)? What's the alternative if `JavalinTest` doesn't work under JPMS — manual `Javalin.create().start(0)` + `java.net.http.HttpClient`?

Investigate Javalin's own test suite on GitHub to see how they test embedded server scenarios. Look at the `javalin-testtools` module specifically.

The critical constraint: HomeSynapse's REST layer uses a **gateway pattern** (DEC-M3-16). The public API class `RestFilters` accepts `Object`-typed parameters to erase Javalin framework types from the public module surface. `Javalin` itself is an implementation dependency of the `rest-api` module, not an API dependency. This means test code in a separate test module cannot directly import Javalin types unless the module graph is configured to allow it. How do other JPMS-aware projects handle this?

### Q2. Port Binding in Parallel Test Execution

`HomeSynapseCore` currently binds Javalin to port 7070 (hardcoded via `DeploymentProfile`). JUnit 5 runs test classes sequentially by default but methods can be parallelized.

- Does `Javalin.create().start(0)` work (port 0 = OS-assigned ephemeral port)?
- How do you retrieve the assigned port after startup? (`javalin.port()` method?)
- What about `SO_REUSEADDR` and `TIME_WAIT` socket states between sequential test classes that each start/stop a Javalin server?
- Is there a risk of port exhaustion on CI with many test classes?
- What patterns do Javalin, Spring Boot (`@SpringBootTest(webEnvironment = RANDOM_PORT)`), and Micronaut use?

### Q3. Mode Transition Timing in Tests (CRITICAL)

This is likely the hardest testing problem. The InProcessEventBus transitions through three modes: `REPLAY → TRANSITION → LIVE`. Entity query endpoints are gated by `ReadinessFilter`, which returns HTTP 503 until the bus reports LIVE. The mode transition happens asynchronously after the bus finishes replaying all stored events.

E2E tests must:
1. Start `HomeSynapseCore` (which starts the bus in REPLAY mode)
2. Wait for LIVE mode
3. Only then hit query endpoints

What is the correct synchronization pattern?

Options to evaluate:
- **Polling with timeout:** Loop on `bus.subscribers().get(0).mode() == LIVE` with Thread.sleep. Simple but fragile — what polling interval? What timeout?
- **CountDownLatch injected into ReadinessSource:** A test-only hook that signals LIVE. Clean but requires modifying production code (or adding a test extension point).
- **HTTP polling:** Hit a health endpoint repeatedly until 200. Realistic but slow.
- **Event-based notification:** Subscribe to a `bus_mode_changed` event. Cleanest but may not exist yet.

What do Axon Framework, EventStoreDB clients, and Marten do for integration test synchronization when waiting for projections to catch up? This is the canonical "projection lag" problem in event sourcing — how is it solved in test contexts specifically?

### Q4. Crash Recovery at the HTTP Level

`CrashRecoveryIT` already exists in the `testing:integration-tests` module. It tests event-level crash recovery: publish 5,000 events → abandon at ≥3,000 → restart → verify exactly-once delivery from checkpoint.

M3.7 should extend this to HTTP-level crash recovery:
1. Start `HomeSynapseCore`
2. Publish events, wait LIVE, verify HTTP responses
3. Simulate crash (hard shutdown — no graceful close)
4. Restart `HomeSynapseCore` on a fresh port
5. Wait LIVE (bus replays from checkpoint)
6. Hit HTTP endpoints → assert state is complete and identical to pre-crash

What edge cases matter?
- In-flight HTTP requests during shutdown — does Javalin handle this gracefully? What does Jetty do with open connections when `stop()` is called?
- SQLite WAL recovery after unclean shutdown — is this already handled by the SQLite driver (xerial sqlite-jdbc), or does HomeSynapse need to do something explicit?
- Checkpoint correctness after crash — the `AtomicCheckpointWriter` writes to a separate table. Is this atomic with respect to the event write transaction?

### Q5. Test Data Factories and JSON Assertion Patterns

Entity state returned via HTTP is JSON. HomeSynapse uses Jackson for serialization. The REST endpoints return responses like:

```json
{
  "entityId": "...",
  "deviceId": "...",
  "attributes": { "brightness": { "type": "INTEGER", "value": 75 } },
  "staleAfter": "PT5M",
  "lastUpdated": "2026-05-22T10:30:00Z"
}
```

What is the cleanest pattern for asserting JSON response bodies in Java 21 without pulling in heavy assertion libraries?

Options to evaluate:
- `java.net.http.HttpClient` + Jackson `ObjectMapper.readTree()` + JUnit 5 assertions on `JsonNode` fields
- `java.net.http.HttpClient` + Jackson deserialization into response DTOs + standard assertions
- AssertJ's JSON assertions (`assertThatJson(body).inPath("$.entityId").isEqualTo(...)`) — is the dependency worth it?
- Hamcrest JSON matchers — still maintained? JPMS-compatible?

Also: what test data factory pattern should be used for constructing the domain events that drive state? HomeSynapse events are Java records (e.g., `StateChanged`, `EntityRegistered`). Should there be builder-style factories (`TestEvents.stateChanged().entityId(...).build()`), or is direct record construction sufficient?

### Q6. The NO_OP Problem — What Should Derivation and Advancement Actually Do?

This is the bridge question between M3.7 (testing) and M4 (device model).

`HomeSynapseCore` currently wires two placeholder implementations:
- `NO_OP_DERIVATION` — a `Function<DomainEvent, Stream<DomainEvent>>` that returns `Stream.empty()` (no derived events)
- `NO_OP_ADVANCER` — a `ProjectionAdvancer` that returns `AdvanceResult.skipped()` for every event (no state projection)

For E2E tests to observe meaningful HTTP responses, the `MaterializedStateQueryService` must return actual entity state — which means the `ProjectionAdvancer` must actually process events and update projections.

**Question:** What is the minimum viable `ProjectionAdvancer.advance()` that:
- Handles `entity_registered` → creates an initial `EntityState`
- Handles `state_changed` → updates attributes on the `EntityState`
- Handles `device_registered` → creates device-level entries
- Returns `AdvanceResult.applied(...)` with the updated state

This is NOT the full M4 implementation. It's the minimum logic needed for M3.7 tests to observe real state through HTTP endpoints. What do other event-sourced test suites do — define a "test projection" that's simpler than production, or use the real production projection from the start?

The tension: if we write a test-only advancer, M4 replaces it. If we write the real advancer, we're doing M4 work inside M3.7. What's the right boundary?

---

## Platforms and Prior Art to Survey

For each, investigate their **testing** patterns specifically — not their runtime architecture (that's covered in other research documents).

1. **Javalin** (javalin.io, GitHub: javalin/javalin)
   - `javalin-testtools` module, `JavalinTest` API
   - Their own integration test suite
   - Community patterns for JPMS + Javalin testing

2. **Axon Framework** (axoniq.io, GitHub: AxonFramework/AxonFramework)
   - `axon-test` module (`FixtureConfiguration`, `AggregateTestFixture`)
   - Saga test fixtures
   - Integration testing with embedded event store
   - How they handle projection catch-up in tests

3. **EventStoreDB** (eventstore.com, GitHub: EventStore/EventStoreDB-Client-Java)
   - Java client integration tests
   - Subscription catch-up patterns in test contexts
   - Testcontainers usage (if any)

4. **Marten** (martendb.io, GitHub: JasperFx/marten — C#/.NET but architecturally relevant)
   - `IDocumentSession` test patterns
   - Projection test utilities
   - How they synchronize projection completion in tests

5. **Spring Boot** (for comparison only — HomeSynapse does NOT use Spring)
   - `@SpringBootTest(webEnvironment = RANDOM_PORT)` + `TestRestTemplate`
   - `WebTestClient` for WebFlux
   - How `@DirtiesContext` and context caching work for integration tests
   - What HomeSynapse should learn (or deliberately reject) from Spring's approach

6. **Micronaut** (for constrained-runtime comparison)
   - `@MicronautTest` with embedded server
   - How Micronaut handles test server lifecycle under GraalVM/constrained envs

---

## Context You Already Have (in project knowledge)

You have access to:
- **HomeSynapse Core Knowledge Primer** — the architectural mental model, module map, and type overview. Refer to this for module names, type locations, and cross-module dependencies.
- **HomeSynapse Current State** — the milestone status through M3.6e.2. Note that M3.6 is COMPLETE (composition root fully wired, 16-step bootstrap, Javalin HTTP on port 7070, readiness-gated entity query endpoints, ungated admin endpoints, ArchUnit enforcement).

Key facts you should incorporate:
- 20 Gradle modules, all JPMS-enforced with `module-info.java`
- `testing:integration-tests` module already exists with `IntegrationTestHarness`, `BurstLoadIT`, `HeapBudgetIT`, `CrashRecoveryIT`, `Pi4SustainedLoadIT`
- The composition root `HomeSynapseCore` (in the `app` module) has a 16-step bootstrap
- `ReadinessFilter` returns 503 until `ReadinessSource.isReady()` returns true (which happens when all bus subscribers report LIVE mode)
- REST endpoints use the DEC-M3-16 gateway pattern: `RestFilters` is a public gateway class with `Object`-typed parameters; actual Javalin types are package-private
- Entity query endpoints: `ListEntitiesEndpoint`, `GetEntityEndpoint`, `GetEntityStateEndpoint` — all package-private, registered via `RestFilters.addEntityEndpoints(Object javalinApp, StateQueryService queryService)`
- Admin endpoints: `DlqStatusEndpoint`, `ProjectionStatusEndpoint` — ungated (no readiness check)
- `DeploymentProfile` enum has `httpPort()` returning 7070 for all profiles currently
- Java 21, virtual threads, no Spring, no CDI, no annotation-based DI
- Jackson for JSON serialization (already a dependency)
- JUnit 5 for all tests, no Mockito in production test suites (in-memory implementations and contract tests instead)

---

## Constraints

1. **Take positions.** "X is worth investigating" is banned. Use "X should be adopted because Y" or "X should be rejected because Y."

2. **Cite primary sources** (documentation pages, GitHub issues, maintainer statements, source code files) with URLs. Every factual claim must be traceable.

3. **Every REC must include an effort estimate** in approximate lines of code (production + test).

4. **Number RECs globally.** Research 2 used REC-01 through REC-12. This document starts at **REC-13**.

5. **Section 7 (Code-Level Implications) is MANDATORY for this research.** Specify exact test class names, base classes, helper types, module placement, and `module-info.java` changes.

6. **Address the JPMS constraint head-on.** Every recommendation must be evaluated against JPMS module boundaries. "Just add the dependency" is not sufficient — specify which module's `module-info.java` changes and what `requires`/`opens` directives are needed.

7. **Do not recommend Testcontainers.** HomeSynapse uses an embedded SQLite database via xerial sqlite-jdbc. There is no external database to containerize. The event bus, state projection, and HTTP server all run in-process.

8. **Do not recommend Mockito or any mocking framework.** HomeSynapse uses in-memory implementations (e.g., `InMemoryEventStore`) and contract test suites instead of mocks. This is a deliberate architectural decision (DEC-M3-05).

9. **Do not truncate.** Produce the complete document. Every section fully populated. If the document is long, that's fine — completeness is more valuable than brevity.

---

## OUTPUT

A single markdown document following the mandatory format above. The document should be directly usable by the PM to produce M3.7 coding instructions — meaning every recommendation must be concrete enough to translate into "create this file, in this module, with this content."
