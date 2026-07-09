<!--
file: project-manager/references/coding-instruction-format.md
purpose: Canonical format for coding instructions sent from the PM to the Coder.
audience: PM
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-06-07 against commit 8028337
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

[MODULE_CONTEXT.md files, `module-info.java` files, and source files the Coder
MUST read before writing any code. Always include the relevant MODULE_CONTEXT.md
files (cross-module contracts + gotchas) AND the relevant `module-info.java`
files (verbatim JPMS module names + `requires` / `exports` graph). Type names
without module names produced ~6 fabricated JPMS module names in Research 6
(2026-05-22) even when type inventories were correct — both are required.]

| File | Why |
|---|---|
| `[module]/MODULE_CONTEXT.md` | Complete type inventory, cross-module contracts, gotchas for the target module |
| `[module]/src/main/java/module-info.java` | Verbatim JPMS module name and `requires`/`exports` graph — the authoritative source for module identifiers |
| `[dependency]/MODULE_CONTEXT.md` | Cross-module contracts and gotchas for each dependency module |
| `[dependency]/src/main/java/module-info.java` | Verbatim JPMS module name + `requires`/`exports` for each dependency |
| `[specific source file]` | [Reason — existing pattern to match, interface to implement against, etc.] |

**Rule:** Every MODULE_CONTEXT.md AND every `module-info.java` in the dependency
chain should be listed here. The Coder reads MODULE_CONTEXT.md for type
inventories and `module-info.java` for module identifiers BEFORE writing any
code that mentions a module or package name. The Knowledge Primer's module
descriptions are summaries — always cross-check JPMS module names against the
actual `module-info.java`.

**Embedding rule for coding instructions:** When the instruction includes
proposed JPMS changes (new `requires`, new `exports`, new module names), quote
the current `module-info.java` verbatim in the Technical Specification section
and show the proposed diff. Do not paraphrase module names.

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
- **Record component / static-factory name collision (the M7.2a-2 gate-fix STOP-check):**
  a Java `record X(boolean valid, ...)` AUTOMATICALLY defines an accessor method `valid()`,
  so you CANNOT also declare a `static X valid(...)` factory or any other method named
  `valid()` on that record — it is a compile error (the component accessor already owns the
  name). This shipped TWICE past a clean in-session LLM self-review in M7.2a-2
  (`ValidationResult.valid()`; `ModeDecision.admit/restartCancel/enqueue`) and ONLY the real
  `./gradlew check` / `javac` caught it. **STOP-check before handoff: scan EVERY new or
  modified record — for each component name, confirm no static factory, no instance method,
  and no nested helper shares that exact name.** Prefer a distinct factory name
  (`validated()`, `ofAdmit()`) or a canonical constructor. This is inspection-discoverable —
  catch it pre-handoff; do not spend the gate's bounce budget on it.

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

## Cowork Prompt Conventions (standard since M3.1; extended through M5)

These conventions supplement the template above. They emerged in the M3.1 prompt and are now standard for **every** Phase-3 coding instruction; the M4/M5 additions (the consumer/pin survey, the §4c reminder, gated parts, verbatim module-info embeds, the `requires transitive`↔`api` authoring check) are folded in below.

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

**Shift-left self-check (P5).** The full `./gradlew check` stays deferred to Nick's environment, but when the sandbox can run Gradle the Coder should run a single targeted `./gradlew :module:compileJava` on each touched `-Werror`-sensitive module before handoff. It surfaces `[exports]`, redundant-cast, and unused-import failures in ~20s and converts the lockstep class of misses from a Nick round-trip into an in-session fix. Target: GREEN in one round. (Not the full `check` — that stays the deferred gate.)

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

### Consumer/Pin (Fan-Out) Survey (P2 — mandatory)

For any change that touches an enum, a registry, an event-type set, a sealed hierarchy, a category/mapping table, or **any counted-or-pinned set**, the instruction MUST enumerate every dependent before issue — not just the producer. Run a repo-wide grep and list each in Files to Modify with its required delta. The categories to sweep:

- **count pins** — `hasSize(N)`, `isEqualTo(N)`, `getDeclaredMethods().length`, `getRecordComponents().hasSize(N)`;
- **validity regexes / format validators** over the set (e.g. an event-type naming regex);
- **category / mapping / lookup tables** keyed by the set — `EventCategoryMapping.TABLE` is main-source and the easy miss;
- **manifest / "all-X" aggregators** and `Stream.concat(...)` registries;
- **composition-root AND test-harness registrations** — the production composition root (`HomeSynapseCore`) is the dangerous one: a missed manifest there is a latent runtime defect that **no test pins**;
- **exhaustive `switch` statements** over the set (no-`default` ones compile-fail, which is good, but still list them);
- **JPMS / contract-direction (payload-type residency)** — for any **new type placed in a base/shared module** (especially an **event record** in `com.homesynapse.event`), verify **every component/field type lives in that module, a leaf (`com.homesynapse.value`), or `java.base`** — never a higher-layer domain module (`config`/`device`/`state`/`automation`/`integration`). A base-module type that references a higher layer **inverts the JPMS edge → a cycle** (e.g. `config requires transitive event`, so a config type in an event record forces `event → config` — the AMD-52 `event↔device` / AMD-70 E70-1 class). Read the `module-info`; if the edge points the wrong way, flatten to `java.base`/`String` (the all-`String` `ConfigChangedEvent` precedent) or route typed data through a leaf (`com.homesynapse.value`, e.g. `QuantityValue`). A one-line direction check; a hard compile cycle if missed.
- **behavioral publish-count pins** — whenever the WU **adds, removes, or relocates an event publish site on an existing code path**, sweep the producing module's ENTIRE test suite for publisher-interaction assertions (recorded-publisher fields like `rootDrafts`, `hasSize(` on captured drafts, index-`get(0)`-and-cast patterns) — not just the test class the WU is editing. A sibling contract test pinning "N publishes per operation" is a consumer of the publish behavior exactly as a count-pinned manifest test is a consumer of the type set; the Coder's execution-time re-run must include this grep too. *(Added 2026-06-11 after the M6.4 gate bounce: `ConfigLayoutTest.composeAfterMerge` pinned 1-publish-per-load from the M6.1a era; the ratified R1/DP-10 obligation made it 2; the instruction's survey enumeration AND the Coder's re-run both missed it — the Coder had even adapted the primary service test for the same change. One stale pin = one full gate round.)*

Emit the result as a `## P2 Consumer/Pin (Fan-Out) Survey` section in the instruction (see the M5-A instruction for the worked shape). **Why it exists:** M4.C listed the producer (`EventTypes` +7 constants) but not its seven pin/consumer sites — including the `HomeSynapseCore` aggregation, a latent-M9 bug no test caught — costing a two-round gate bounce. This is the control that makes lockstep clusters go GREEN in one round (P5). The **JPMS/contract-direction** bullet was added **2026-06-09 after AMD-70 E70-1**: a config-typed payload in an event record would have been a hard `event→config` cycle, caught only at independent review — the direction check is the PM's pre-issue guard. **Standing directive (Nick, 2026-06-09): PM and Claude Code sessions are always mindful about contracts and JPMS.**

### Arch-Rule Test-Clock Reminder (§4c — include for non-whitelisted target modules)

When the target module is outside `com.homesynapse.{app,platform,test}..`, paste this verbatim into "What to Watch Out For":

> **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code — the `NO_DIRECT_TIME_ACCESS` ArchUnit rule scans non-whitelisted test classes and fails `./gradlew check`. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via constructor/`@BeforeEach`.

No reminder is needed when the target is `com.homesynapse.{app,platform,test}..` (whitelisted).

### Gated Parts & Verbatim module-info Embeds

- **⛔ gate markers.** When an instruction bundles parts that depend on a not-yet-ratified amendment or an upstream gate, mark each gated row/section with **⛔** and state the un-gate condition in the masthead (e.g. "⛔ GATED on the codec amendment's ratification"). Non-gated parts may land first.
- **Verbatim module-info, with a PROPOSED DIFF.** When the instruction proposes JPMS changes (new `requires`/`exports`/module), quote the current `module-info.java` **verbatim** in the Technical Specification and show the proposed diff. Never paraphrase module names (the Research-6 fabrication lesson).
- **`requires transitive` ↔ Gradle `api` authoring check — do this BEFORE embedding a module-info.** For each public type in an **exported** package, check whether its API surface (supertype, return type, parameter, field) names a type from another module. If so, that module must be `requires transitive` in the embed **and** `api(...)` in `build.gradle.kts` (plain `requires` ⇔ `implementation(...)`). A plain `requires` under these conditions trips `-Xlint:exports` → `-Werror` → a hard compile failure. This has recurred three times (M2.9, M3.6e.1, M5-A) — twice the **embedded module-info in the instruction itself** was the defect. Never hand the Coder a non-transitive embed for a module that exports impls of another module's types.

### Instruction Masthead Conventions

Real instructions carry an HTML-comment masthead with `purpose`, `audience`, `status` (`ISSUE-READY` / `⛔ GATED on …` / `COMPLETE`), and `baseline:` (the HEAD the instruction was authored against — re-verify at issue). When an amendment number is **in flight**, use neutral phrasing ("the current amendment watermark", "the codec amendment") rather than pinning a still-PROPOSED number; add an `amd-number-note` only when a renumber is live (per INV-GA-02, identifiers are never reused, so a retired number must not be re-cited as live).

---

## Additions (2026-06-11, from the M6.2 execution feedback — ratified by the M6.2 zero-bounce outcome)

1. **Internal-consumer survey (MANDATORY).** When the WU modifies an internal component (a loader, codec, writer, helper), the instruction must enumerate EVERY consumer of that component (constructor call sites + call paths) and rule the behavior for each — the P2 consumer/pin survey discipline applied to module internals. Origin: M6.2's DP-10 ruled tag resolution for load+reload but was silent on `YamlLoader`'s write-path consumer; resolving there would have written plaintext secrets to disk.
2. **The Files table governs.** Where instruction prose and the Files table disagree on what is touched, the Files table wins; the Coder flags the conflict as `[INFO]` rather than escalating. (Origin: DP-6's "persistence factory … HOLDS it" vs `PersistenceFactory` absent from the table.)
3. **Minimum read set (MANDATORY section).** Every instruction states the must-understand list explicitly — types and, for large files, the named regions (e.g. "`runPipeline`/`writeLocked` regions of `StandardConfigurationService`"). The Coder may read more, but the floor is declared.
4. **External-standard constants embed verbatim.** Any test pinning standard-derived constants (RFC vectors, IEEE bit patterns, protocol magic) gets them embedded in the instruction verbatim with the source citation — never left for the Coder to recall. Standing practice: the Coder re-derives them independently before pinning.
5. **Worked examples for counter/boundary semantics.** Any N-th-occurrence rule ("the 6th mutation prunes bak.1") carries a one-line worked example resolving whether creation counts.
6. **§4c caveat:** do NOT assert `NO_DIRECT_TIME_ACCESS` scans non-app test source sets — it structurally cannot (see open-questions 2026-06-11). The Clock-injection prescription stands as convention; word it as such until the rule-reach OQ resolves.

## Additions (2026-07-03, from the M9.2 gate rounds — pm-lessons 2026-07-03 carries the full detail)

7. **Checked-exception seam map (MANDATORY when a checked exception is mandated).** If the instruction mandates throwing a checked exception type (e.g. `PermanentIntegrationException` from a rejection tier), it must ALSO state WHERE the `throws` declarations land: which methods declare it, and how it crosses any frozen no-throws interface in the call path (the answer is a package-private checked seam + an unchecked cause-chained rethrow on the frozen surface — never force it through). The frozen-interface collision is predictable at authoring time; leaving it to the Coder produced a 3-file compile bounce that LLM review structurally cannot catch (checked-exception FLOW is javac-only). Companion rule for the classifier era: state whether the exception must arrive at its consumer UNWRAPPED (`ExceptionClassifier` is bare-`instanceof` — a wrapped permanent classifies TRANSIENT).
8. **Stub-tripwire arithmetic excludes instruction-anticipated stubs.** When an instruction sets a proportional STOP tripwire on frozen-interface stubbing ("more than ~a third"), the arithmetic must EXCLUDE methods the instruction itself already assigns to later milestones — count only UNANTICIPATED stubs. M9.2's tripwire fired at 3/7 where all 3 were the instruction's own named deferrals; the STOP would have round-tripped "proceed" (ruled ACCEPT retroactively, beat 58).
9. **Module-info pins are validated against every mandated behavior.** Before pinning "exactly N added directives", walk the instruction's OWN requirements for forced edges (structured logging ⇒ `org.slf4j`; first test tree ⇒ test-scope `test-support`; serialization ⇒ Jackson): each mandated behavior with a module dependency belongs in the pinned diff. M9.2's 1-directive pin contradicted its own §Vectors logging mandate and spent a `[REVIEW]` on a self-inflicted inconsistency.

## Additions (2026-07-04, from the M9.3 arc — validated by the zero-defect audit + the adversarial review)

10. **Governance-freeze-first sections.** When a milestone realizes a ratified amendment into frozen source (an AMD-correction "§1"), structure the instruction so the freeze lands FIRST as its own coherent unit — the types + characterization tests from MEASURED values GREEN — before any pipeline section consumes it, with an explicit "§1 completion marker." M9.3 executed this cleanly end-to-end; it keeps governance out of implementation churn (the DP-1 ruling made mechanism) and gives the auditor a crisp freeze boundary to verify byte-exact.
11. **Cross-repo fixture provenance.** When tests consume fixtures captured in a sibling repo (bench event streams), mandate all three: (a) COPY into the module's test resources (core tests cannot read a sibling repo), (b) a provenance header in the copy (source repo @ SHA + path + "the source repo wins on divergence"), (c) the fixture-clock discipline (`setFixed(...)` the TestClock to each frame's capture timestamp before feeding it — fixture wall-clock time must never leak into production paths as `now()`).
12. **Name the anticipated seam-fill in modified stub tests.** When the WU fills a seam a prior milestone's stub-inventory test asserts (M9.3 filling `interview()`, asserted-throwing by the M9.2 "D-M92-6 stubs" test), the instruction lists that test in Files-to-Modify with the exact assertion delta (drop the filled seam's throw-assert; RETAIN the later milestones' stub asserts) — otherwise the edit arrives as an undeclared surprise in the diff.

## Additions (2026-07-04, from the M9.4a arc — pm-lessons 2026-07-04 carries the full detail)

13. **Test-home grounding (MANDATORY for any new-test row in an otherwise-untouched module).** A Files-table location pin is a SOURCE-STATE claim like any signature pin — ground it before pinning it. Before placing a NEW test in a module the WU doesn't otherwise touch, read that module's `build.gradle.kts` for test-task gating (`tasks.test { enabled = ... }`, profile properties, tag filters) and state the finding in the row. M9.4a pinned the hero IT into `testing/integration-tests` ungrounded; that module is `piProfile`-gated OUT of the default `check`, which would have silently excluded THE done-when test from every default gate and from CI (the Coder's grounded deviation to the lifecycle test tree was correct — R1, ruled ACCEPT with the authoring miss owned). **A test that exists but never runs in the gate of record is worse than no test — it reads as coverage.**

## Additions (2026-07-08, from the M9.5-DUR arc — folded at the v25 skills pass)

14. **Surface-export check against the instruction's OWN DPs before pinning module-info zero-change.** The addition-#9 class recurred a 4th time: M9.5-DUR pinned "zero module-info changes" while its own DP placed new PUBLIC types naming another module's payload records on an EXPORTED surface — which forces the `requires transitive` promotion under `-Xlint:exports`/`-Werror` (and the Gradle `api` lockstep). Before pinning ANY module-info expectation, walk the instruction's own settled decisions for exported-surface types and run the requires-transitive↔api check against THEM, not only against existing code. (The Coder's evidence-based pushback resolved it in-session — ruled ACCEPT, authoring miss owned — but the pin should never have shipped self-inconsistent.)
15. **Non-atomic multi-event emission contracts get a crash-window ruling at authoring.** When an instruction mandates a durable multi-publish sequence whose events are only meaningful together (the AMD-99 `device_registered` → `entity_registered`×N contract), the instruction must either rule the partial-failure semantics (what state does a death between publishes leave, and what repairs it) or explicitly queue the named repair as follow-up. The M9.5-DUR half-registration gap was caught by the Coder's in-session adversarial review fleet, not by the instruction — the class is predictable at authoring time. Companion rule: **a Coder-side self-review fleet is LAYER-1 evidence** — its findings enter the hub's layer-2 adjudication like any lane return (labels-are-claims, quotes-are-evidence); it never substitutes for the hub's audit.

