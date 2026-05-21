<!--
file: project-manager/references/coding-instruction-format.md
purpose: Canonical format for coding instructions sent from the PM to the Coder.
audience: PM
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Coding Instruction Format — Coder Communication Protocol

This is the canonical format for all coding instructions sent from the PM to the Coder. The Coder should be able to produce correct, constraint-compliant code from this document alone, while retaining freedom on minor implementation details.

The coding instruction is the PM's primary tool for quality control. Everything that matters about the implementation must be stated here — not implied, not assumed, not left for the Coder to discover.

---

## The Template

```markdown
# Coding Task: [Descriptive Title]

**Subsystem:** [Which subsystem this belongs to]
**Design Doc:** [Which locked design doc governs this work, with status confirmation]
**Phase:** [3-Implementation | Spike]
**Task Brief Reference:** [Title of the task brief this derives from]

## What This Implements

[One paragraph connecting this to the design doc and task brief. The Coder needs
to understand what role this code plays in the larger system. This is NOT the
strategic "why" (that's in the task brief) — this is the engineering "why": what
does this subsystem do, and what specific piece of it are we building right now?]

## Files to Read Before Starting

[MODULE_CONTEXT.md files and source files the Coder MUST read before writing any
code. Always include the relevant MODULE_CONTEXT.md files — they contain the
cross-module contracts and gotchas that prevent bugs.]

| File | Why |
|---|---|
| `[module]/MODULE_CONTEXT.md` | Complete type inventory, cross-module contracts, gotchas for the target module |
| `[dependency]/MODULE_CONTEXT.md` | Cross-module contracts and gotchas for each dependency module |
| `[specific source file]` | [Reason — existing pattern to match, interface to implement against, etc.] |

**Rule:** Every MODULE_CONTEXT.md in the dependency chain should be listed here.
The Coder reads these BEFORE reading individual source files to build
understanding of the module landscape.

## Files to Create or Modify

[Explicit file paths within the repo. Be specific about packages and modules.]

| Action | File Path | Description |
|---|---|---|
| CREATE | `homesynapse-core/src/main/java/com/homesynapse/events/EventPublisher.java` | The event publication interface |
| CREATE | `homesynapse-core/src/test/java/com/homesynapse/events/EventPublisherTest.java` | Unit tests for EventPublisher |
| MODIFY | `homesynapse-core/build.gradle.kts` | Add new module dependency |

## Technical Specification

### Classes and Interfaces

[For each class/interface, specify:]

#### `InterfaceName` (interface | class | record | enum | sealed interface)
**Package:** `com.homesynapse.subsystem`
**Responsibility:** [One sentence]
**Extends/Implements:** [Parent types, or "none"]

**Methods:**
```java
/**
 * [Javadoc contract — preconditions, postconditions, thread safety, exceptions]
 */
ReturnType methodName(ParamType param);
```

**Behavioral contracts:**
- [Precondition: what must be true before calling]
- [Postcondition: what is guaranteed after calling]
- [Invariant: what is always true about this type]
- [Thread safety: is this type safe for concurrent access? How?]

### Event Types Produced or Consumed

[Reference the Event Model design doc §4.3 taxonomy]
- Produces: `device.state_changed`, `device.command_issued`
- Consumes: `system.startup_complete`

### Configuration Parameters

[Reference the Configuration System. YAML key, type, default, valid range.]
- `homesynapse.events.subscriber.checkpoint-interval`: integer, default 100, range [1, 10000]

### Error Handling

[For each error condition:]
| Condition | Exception Type | Message Pattern | Recovery |
|---|---|---|---|
| Duplicate sequence | `SequenceConflictException` | "Event sequence conflict: expected %d, received %d for entity %s" | Caller retries with correct sequence |

[Remember: error messages use Register C voice — direct, neutral, no self-reference,
no apology, no celebration.]

## Locked Decisions That Apply

[Cite ONLY the LTDs the Coder will encounter while writing THIS code. Be specific
about what each one constrains. Cross-reference with the Constraints section in
the relevant MODULE_CONTEXT.md files to ensure you haven't missed any.]

- **LTD-04 (ULID):** All identifiers use typed ULID wrappers. Store as BLOB(16) in
  SQLite. Crockford Base32 string conversion ONLY at API boundaries and in log output.
  Use `UlidFactory.monotonic()` for event IDs, `UlidFactory.generate()` for entity IDs.
  `UlidFactory` is in `platform-api` (hand-rolled, VT-safe via ReentrantLock — DECIDE-02).
- **LTD-11 (No Broker):** Event dispatch via virtual thread executors. Use
  `ReentrantLock`, never `synchronized` — virtual threads pin on `synchronized` blocks.

## Invariants That Must Hold

[Cite ONLY the INVs this code participates in. State the test that verifies each.
Cross-reference with the Constraints section in the relevant MODULE_CONTEXT.md files.]

- **INV-ES-04 (Write-Ahead Persistence):** Event must be durable in SQLite before
  ANY subscriber receives it. Test: kill -9 at random points during processing. On
  restart, every persisted event must be delivered to all subscribers.
- **INV-RF-01 (Integration Isolation):** If this code runs in the integration context,
  it must not be able to crash the core event bus. Test: throw RuntimeException from
  within integration code. Core must remain operational.

## Test Requirements

### Unit Tests
[Be specific. Name the test class. Describe each test scenario.]

**Test class:** `EventPublisherTest`

| Test Method | Scenario | Assertion |
|---|---|---|
| `publishRoot_assignsCorrelationIdToSelf` | Publish a root event | `correlation_id == event_id`, `causation_id == null` |
| `publish_inheritsCorrelationFromCause` | Publish a caused event | `correlation_id == cause.correlation_id` |
| `publish_withDuplicateSequence_throwsConflict` | Same entity, same sequence | Throws `SequenceConflictException` |
| `publish_persistsBeforeReturn` | Publish then query | Event visible in store immediately after method returns |

### Integration Tests
[Cross-subsystem behavior to validate]

### Performance Tests
[Reference MVP §8 targets. Specify methodology.]
- Event throughput: sustained >500 events/second for 60 seconds
- Publish latency p99: <10ms (INV hard invariant)

## Code Quality Standards

- **Comments:** Javadoc on all public interfaces and methods. Comments explain WHY,
  not WHAT. No comments that restate the code.
- **Naming:** Every name matches the Glossary. `EventStore`, not `EventRepository`.
  `EntityId`, not `EntityIdentifier`.
- **Error messages:** Register C voice. No "we", no "sorry", no "please".
- **Logging:** SLF4J with structured context. Include entity_id, event_type, and
  correlation_id in every event-related log statement.

## Dependencies and Integration Points

[What other subsystems does this code interact with? What interfaces does it
consume or produce? Reference specific design doc sections AND the relevant
MODULE_CONTEXT.md Cross-Module Contracts sections.]

- Consumes: `EventStore` (Persistence Layer §8.1) for durable writes
- Produces: notifications via `EventBus` to all registered subscribers
- Cross-subsystem: State Store subscribes to all `state_changed` events from this publisher
- MODULE_CONTEXT contracts: [cite specific contracts from MODULE_CONTEXT.md that apply]

## What to Watch Out For

[The subtle pitfalls. Things that look simple but aren't. Things that have bitten
other implementations. This section is where your senior engineer expertise matters most.

IMPORTANT: Derive these from FOUR sources:
1. Your engineering judgment
2. The Gotchas sections in the relevant MODULE_CONTEXT.md files
3. Lessons from previous implementations (coder-lessons.md)
4. The Source Trust Hierarchy (deviation-and-quality.md §6) — ensure any
   dependency scopes or implementation details you cite are verified against
   actual source files, not handoff documents or MODULE_CONTEXT summaries]

- Virtual threads + `synchronized`: If ANY code in the publish path uses a
  `synchronized` block, including third-party library code, the virtual thread will
  pin to its carrier. Use `ReentrantLock` everywhere. Check transitive dependencies.
- ULID monotonicity: `UlidFactory.monotonic()` guarantees ordering within the same
  millisecond, but ONLY within the same JVM instance. Don't assume cross-JVM ordering.
  Note: `ulid-creator` library was removed (DECIDE-02). Use the hand-rolled `UlidFactory`
  in `platform-api`.
- SQLite single-writer: Only one thread can write at a time in WAL mode. The event
  publish path must serialize writes. This is an architectural simplification, not a
  limitation — the single-writer model matches event sourcing perfectly.
- subject_sequence monotonicity: Per-ENTITY, not global. Two different entities can
  have the same sequence number. The unique constraint is (subject_ref, subject_sequence).
- Derived event time: When a subscriber produces a derived event (e.g., State Projection
  producing `state_changed` from `state_reported`), the `eventTime` field must be inherited
  from the causing event (`causingEnvelope.eventTime()`) or set to null. NEVER use
  `Instant.now()` — the publisher handles `ingestTime` as the system timestamp. Using
  `Instant.now()` for `eventTime` conflates processing time with real-world occurrence
  time and breaks `COALESCE(event_time, ingest_time)` time-range queries.

## Coder Pushback Welcome

[Signal to the Coder that technical pushback is expected and valued.]

If you discover during implementation that any specification in this document is
impractical, will cause performance issues, contradicts a MODULE_CONTEXT.md gotcha,
or could be done better while maintaining the same behavioral contract — raise it.
Use the escalation format in your skill doc. Technical insight from the implementation
level improves the architecture.

## Out of Scope

[Things the Coder might be tempted to build but must not.]

- Subscriber implementations (those are separate coding tasks)
- REST API endpoints for event queries (REST API subsystem)
- Event retention/cleanup logic (Persistence Layer subsystem)
- UI event display (Web UI subsystem)

## Work Unit Completion (WUCP Phase 1)

After the compile gate passes (or is explicitly deferred to Nick's
sandbox-external environment), execute WUCP Phase 1 from
`nexsys-hivemind/context/protocols/work-unit-completion-protocol.md`.
The steps are: update MODULE_CONTEXT.md, update coder-handoff.md
(with Deferred Build Gate flag if applicable), append to
coder-lessons.md (if applicable), post cross-agent note (if
applicable), and append the WUCP Phase 1 checklist to this
Completion Report. The work unit is not done until the checklist is
complete. A deferred build gate MUST be explicitly flagged so the PM
can track it under Open Risks.
```

---

## Field-by-Field Guidance

### What This Implements
This paragraph serves two purposes: it orients the Coder in the system architecture, and it provides the context needed to make judgment calls on unspecified details. Write it as if the Coder has never seen this subsystem before (they may be starting a new session).

### Files to Read Before Starting
**NEW — this section replaces the old "Files to Read" concept.** Always list:
1. The target module's MODULE_CONTEXT.md (if it exists)
2. MODULE_CONTEXT.md for every dependency module in the chain
3. Specific source files the Coder needs for pattern matching or interface implementation

The MODULE_CONTEXT.md files give the Coder the big picture before they dive into individual files. A Coder who reads MODULE_CONTEXT.md first will understand cross-module contracts, sealed hierarchy patterns, and gotchas BEFORE writing a line of code.

### Files to Create or Modify
Explicit paths prevent the Coder from inventing package structure. If the module doesn't exist yet, say so and include the Gradle module declaration.

### Technical Specification
This is the PM's primary tool for quality control. The level of detail should be:
- **Interface signatures:** Fully specified. Return types, parameter types, exception types. The Coder should not invent public API shapes.
- **Behavioral contracts:** Precise enough to write a test against. "Events are published" is too vague. "The event is durable in SQLite before the method returns, and subscriber notification begins asynchronously after the method returns" is testable.
- **Implementation details:** Only specify when the choice is constrained by a locked decision or invariant. Otherwise, leave implementation freedom to the Coder. Say "this must use ReentrantLock" (constrained by LTD-11) but don't say "use a HashMap here" unless there's a specific reason.

### What to Watch Out For
This is the highest-value section. Your experience as a senior engineer lives here. Think about:
- Concurrency traps (virtual thread pinning, race conditions, deadlocks)
- Serialization edge cases (null handling, ULID format at boundaries)
- SQLite-specific behavior (WAL checkpoints, BLOB vs TEXT for ULIDs)
- Cross-subsystem assumptions that might be wrong
- Performance cliffs (what happens at 2x expected load?)
- **MODULE_CONTEXT.md gotchas** — read the Gotchas section for every module in the dependency chain and surface the relevant ones here

### Coder Pushback Welcome
**NEW section.** This explicitly signals to the Coder that technical pushback is valued. Without this signal, the Coder may silently implement something they know is suboptimal because the instructions didn't leave room for pushback. Include this in every coding instruction.

### Out of Scope
Prevents scope creep at the implementation level. The Coder will see adjacent work that "should" be done — the Out of Scope section says "I know, and it's a separate task."

---

## Spike Instructions

Spikes use a simplified format:

```markdown
# Spike: [Question Being Answered]

**Question:** [Precise question — not "explore X" but "does X under Y conditions exceed Z?"]
**Success criteria:** [What answer resolves the question]
**Failure criteria:** [What answer means we need a different approach]
**Time box:** [Maximum effort before reporting back]

## Methodology
[How to test this. What code to write. What to measure.]

## Where to Put It
- Code: `spikes/[descriptive-name]/` — NOT in the production source tree
- Findings: Record in [specific design doc] §[section] open questions

## What This Spike Must NOT Become
Production code. If the spike reveals the right approach, a proper coding task
will be issued against the production source tree with tests.
```

---

## Anti-Patterns

**Too vague on contracts:**
> "Implement the EventPublisher interface."

The Coder doesn't know what the method signatures are, what the behavioral contracts are, or what tests to write.

**Too prescriptive on implementation:**
> "Use a ConcurrentHashMap<String, List<Consumer<EventEnvelope>>> for the subscriber registry, iterate with a for-each loop, and catch RuntimeException."

This removes the Coder's legitimate engineering judgment. Specify the contract (what happens when a subscriber is registered), not the data structure.

**Missing the Watch Out section:**
Without it, the Coder will discover the virtual thread pinning issue by debugging a production hang at 3 AM. The PM's job is to front-load this knowledge.

**Forgetting Out of Scope:**
The Coder implements the EventPublisher and also builds the REST endpoint for event queries because "it seemed related." That's a separate task with its own constraints and tests. The Out of Scope section prevents this.

**Not listing MODULE_CONTEXT.md in Files to Read:**
The Coder starts a fresh session, reads only the specific source files listed, misses the cross-module contracts in MODULE_CONTEXT.md, and introduces a bug that compiles but violates a behavioral promise. Always list the MODULE_CONTEXT.md files.

**Shutting down Coder pushback:**
> "Implement exactly as specified, no deviations."

This prevents the Coder from surfacing legitimate technical concerns. The Coder sees implementation-level details you don't. Always include the "Coder Pushback Welcome" section.

---

## M3 Cowork Prompt Enhancements (Post-M3.1)

The M3.1 prompt demonstrated an evolved format that should be used for all subsequent M3 milestones. These additions supplement the template above.

### STOP-on-Mismatch Gates

Each Cowork prompt must include verification gates where the Coder reads a source file and confirms it matches expectations before proceeding. If the file has changed since the prompt was authored, the Coder stops and reports the discrepancy.

```markdown
## STOP-on-Mismatch Gates

Before writing any code, read the following files and verify they match the expected state.
If any file has diverged, STOP and report — do not proceed with stale assumptions.

| File | Expected State | What to Check |
|---|---|---|
| `core/event-bus/.../EventBus.java` | 8 declared methods (4 abstract, 4 default) | Count methods, verify default bodies |
| `core/event-bus/.../EventBusTest.java` | Asserts 8 methods | Shape test matches interface |
| `core/event-bus/.../EventBusContractTest.java` | 44 test methods across 10 tiers | Tier structure intact |
```

For any type the brief asserts is cross-module accessible, include a gate that
verifies the `public` modifier on the class declaration — not just type existence.
"Type exists in module X" is insufficient; "type is public in module X" is the
correct gate. (Lesson: M3.5a G4 — DerivedWriteRateLimit was package-private
despite PLAN claiming public.)

### Settled Decision Points

When a Cowork prompt derives from a deliberation document (like PLAN-M3-CONSOLIDATED-02), the deliberation's decision points are embedded as settled constraints — not open questions for the Coder to resolve.

```markdown
## Settled Decisions (from PLAN-M3-CONSOLIDATED-02 §X.Y deliberation)

These decisions were resolved during M3 design deliberation. They are NOT open questions.
Implement exactly as stated.

- **DP-1 (Exception taxonomy):** Error/IOException/checked → SUSPENDED. RuntimeException → backoff.
- **DP-2 (DLQ scope):** Per-subscriber, in-memory ring, cap 1024. Persistent overflow deferred to M3.5b.
- **DP-3 (SubscriberInfo stability):** 3 fields only. No runtime state on SubscriberInfo.
```

### Forward Pointers as Implementation Specs

When a decision depends on work in a future milestone, state the current-milestone boundary clearly:

```markdown
**Forward pointer (M3.2 scope — do NOT implement now):**
Full 3s/30s/0.2 exponential backoff is M3.2 scope. M3.1 retries immediately.
The supervisor structure must accommodate future backoff without refactoring.
```

### Binary Success Criterion

Every Cowork prompt ends with an unambiguous pass/fail criterion:

```markdown
## Success Criterion

The milestone is DONE when:
1. All files in "Files to Create or Modify" exist with the specified content.
2. `EventBusContractTest` reports 44 test methods (18 original + 16 new active + 10 disabled).
3. `InProcessEventBusTest` passes all Tier 5-8 tests.
4. `InMemoryEventBusTest` continues to pass all Tier 1-4 tests (Tiers 5-10 skipped via assumeTrue).
5. MODULE_CONTEXT.md updated with accurate type count and tier structure.
6. WUCP Phase 1 checklist completed.
```

### Build Discipline (Cowork-specific)

Cowork prompts produce files only — they do NOT run Gradle. State this explicitly:

```markdown
## Build Discipline

You produce files. You do NOT run `./gradlew` or any build command.
Nick will run the build gate after reviewing your output.
Deferred build gate: flag it in coder-handoff.md and WUCP Phase 1 checklist.
```

### MODULE_CONTEXT Update Spec

Every prompt that creates or modifies production types must specify the MODULE_CONTEXT update:

```markdown
## MODULE_CONTEXT.md Update

After all production files are written, update `core/event-bus/MODULE_CONTEXT.md`:
- Header type count: 4 → 14
- Add new types to Complete Type Inventory (specify public vs package-private)
- Add new Gotchas if any non-obvious behavior was introduced
- Update Phase 3 Notes with current milestone status
```

### Interface Evolution Checklist (PM pre-generation)

Before generating any Cowork prompt that extends an interface:

1. **Grep for shape tests** (`*Test.java` asserting `getDeclaredMethods().length`) — include in Files to Modify.
2. **Check for existing implementations** in testFixtures — specify `default` vs abstract.
3. **Check for contract test subclasses** — specify capability hooks if new tiers are needed.
4. **Verify ArchUnit rule citations** against actual `HomeSynapseArchRules.java` source — do not cite fictitious rules.
