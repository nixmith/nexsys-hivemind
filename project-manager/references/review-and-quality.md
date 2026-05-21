<!--
file: project-manager/references/review-and-quality.md
purpose: Review checklists for design docs, interface specs, and Coder output before declaring work complete.
audience: PM
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Review and Quality Protocol

The PM reviews three types of output: design documents (self-review and Nick's review), interface specifications (self-review), and Coder output (code review). Each type has its own checklist. Apply the appropriate checklist BEFORE declaring any work product complete.

---

## 1. Design Document Review (Phase 1)

Use when: You have produced a design document, or you are reviewing one for consistency with the architecture.

### Template Compliance
- [ ] All 13 MANDATORY sections are present and substantive (not placeholder text)
- [ ] All CONDITIONAL sections are either included or explicitly excluded with reasoning
- [ ] Metadata header is complete: document type, status, subsystem, dependencies, dependents, author, date
- [ ] Dependencies cite specific section references, not just document names
- [ ] Dependents field is populated with known downstream documents

### Invariant Coverage
- [ ] Every invariant relevant to this subsystem is identified in the Contracts and Invariants section
- [ ] Each cited invariant has a specific design decision or mechanism that satisfies it
- [ ] Each invariant has a test description that would verify it
- [ ] I independently scanned the invariant index (Architecture Invariants §17) for uncited invariants

### Locked Decision Compliance
- [ ] Every relevant LTD is cited and incorporated
- [ ] No design decision contradicts a locked decision
- [ ] Where a design decision depends on an LTD's specific configuration (e.g., SQLite PRAGMA values), the configuration is referenced, not assumed

### Precision
- [ ] Every behavioral claim is specific enough to write a test against
- [ ] Performance targets are quantitative with units and deployment context
- [ ] Configuration options have types, defaults, and valid ranges
- [ ] Failure modes describe trigger, impact, recovery, and event production
- [ ] Interface definitions include responsibility, primary consumers, and enough detail for Phase 2

### Consistency
- [ ] Terminology matches the Glossary exactly (spot-check at least 10 terms)
- [ ] Event types referenced match the Event Model §4.3 taxonomy
- [ ] Cross-references to other design documents cite specific sections
- [ ] Scope boundaries (owns/does-not-own) are unambiguous and consistent with adjacent subsystems

### Decision Quality
- [ ] Every decision in the Summary of Key Decisions table has a rationale
- [ ] Rationale references a principle, constraint, or evidence — not just preference
- [ ] Alternatives considered are realistic (no strawmen)
- [ ] Tradeoffs are stated explicitly

### Open Questions
- [ ] Every open question is marked BLOCKING or NON-BLOCKING
- [ ] No BLOCKING questions remain (or they are escalated with a resolution plan)
- [ ] NON-BLOCKING questions state what information would resolve them

---

## 2. Interface Specification Review (Phase 2)

Use when: You have produced Java interface specifications, or you are reviewing them before handing off to Phase 3.

### Traceability
- [ ] Every interface maps to a Key Interface in the Locked design document
- [ ] Every type maps to a Key Type in the Locked design document
- [ ] Every behavioral contract in the Javadoc traces to a specific design doc section
- [ ] No interface or type exists that isn't traceable to the design doc (no scope creep)

### Completeness
- [ ] All public interfaces have Javadoc with behavioral contracts
- [ ] All public methods have parameter types, return types, and exception declarations
- [ ] All records have Javadoc on the record and its components
- [ ] All enums have Javadoc on the type and each constant
- [ ] Sealed interfaces have Javadoc explaining the type hierarchy and the exhaustive list of permitted subtypes
- [ ] Package-level README explains the module's responsibility and its relationship to adjacent modules

### Correctness
- [ ] All identifier types use typed ULID wrappers (LTD-04)
- [ ] No `synchronized` blocks — `ReentrantLock` only (LTD-11)
- [ ] Serialization uses Jackson (LTD-08) with custom serializers for ULID types
- [ ] Configuration types use YAML conventions (LTD-09) with JSON Schema
- [ ] Naming matches the Glossary exactly

### Compilability
- [ ] Interfaces compile against Java 21 without preview features
- [ ] No circular dependencies between packages
- [ ] Module boundaries are consistent with the Gradle multi-module structure (LTD-10)
- [ ] Dependencies between modules follow the allowed direction (core ← integration, never core → integration)

### Cross-Subsystem Alignment
- [ ] Interfaces consumed from other subsystems match those subsystems' Phase 2 specifications
- [ ] Event types produced/consumed match the Event Model taxonomy
- [ ] Shared types (EventEnvelope, typed IDs, CausalContext) are imported from the shared module, not redefined

---

## 3. Code Review (Phase 3 — Reviewing Coder Output)

Use when: The Coder has produced code and you need to verify it meets the instruction's requirements.

### Instruction Compliance
- [ ] All files listed in the coding instruction are created/modified
- [ ] All behavioral contracts from the instruction are implemented
- [ ] All test scenarios from the instruction are covered
- [ ] Success criteria from the original task brief are addressed

### Constraint Compliance
- [ ] Every LTD cited in the instruction is followed (check each explicitly)
- [ ] Every INV cited in the instruction is satisfied (trace to specific code)
- [ ] Naming matches the Glossary (spot-check at least 10 identifiers)
- [ ] No new dependencies introduced outside the version catalog
- [ ] Any new dependency has an Apache 2.0-compatible license

### Source Verification (Architecture Benchmark 2026-03-22)
- [ ] Dependency scopes in coding instructions verified against actual `build.gradle.kts`, not handoff documents
- [ ] Implementation-level claims about existing code verified against source files, not MODULE_CONTEXT summaries or design documents
- [ ] Derived events use inherited `eventTime` (from causing event) or null — never `Instant.now()`

### Code Quality
- [ ] Javadoc on all public interfaces and methods
- [ ] No comments that restate the code (comments explain WHY, not WHAT)
- [ ] Error messages use Register C voice (no "we", "sorry", "please")
- [ ] Logging uses SLF4J with structured context (entity_id, event_type, correlation_id)
- [ ] No `synchronized` blocks (use `ReentrantLock`)
- [ ] ULIDs stored as BLOB(16), string conversion only at API boundaries and logs
- [ ] No `System.out.println` or `System.err.println`
- [ ] No `Thread.sleep()` in production code (use scheduled executors or virtual thread sleep)

### Test Quality
- [ ] Tests are written FIRST (verify timestamps if possible, or verify test structure exists independently of implementation)
- [ ] Tests cover: happy path, edge cases, error conditions, boundary values
- [ ] Tests verify behavior, not implementation (a refactor should not break tests)
- [ ] Test names describe scenarios: `methodName_condition_expectedBehavior()`
- [ ] Integration tests use real SQLite (in-memory or temp file), not mocks for persistence
- [ ] Performance tests reference MVP §8 targets explicitly

### Deviation Assessment
When the Coder reports deviations:
- **[INFO] deviations:** Acknowledge and record. No action needed unless the pattern seems problematic.
- **[REVIEW] deviations:** Evaluate against the design doc and constraints. If the deviation improves the implementation without changing the contract, approve it. If it changes the contract, escalate to Nick.
- **[BLOCKING] deviations:** The Coder cannot proceed. Determine if this is:
  - A constraint conflict → read `constraint-enforcement.md` §3 for resolution
  - A design doc gap → escalate to Nick for potential supersession
  - An instruction error → revise the instruction and reissue

---

## 4. Cross-Output Consistency Checks

After any review, verify consistency with adjacent work:

- [ ] New code doesn't break existing tests (run full test suite)
- [ ] New interfaces are consistent with existing interfaces in the same module
- [ ] New event types are registered in the Event Model taxonomy
- [ ] New configuration keys follow existing YAML structure patterns
- [ ] New error types follow existing exception hierarchy
- [ ] Module dependency graph is still valid (run modules-graph-assert)
- [ ] ArchUnit rules still pass (integration modules don't import core internals)

---

## 5. When to Reject vs. When to Iterate

**Reject and start over when:**
- The output fundamentally misunderstands the subsystem's purpose
- The output violates an architecture invariant in a way that can't be patched
- The output introduces a dependency direction violation (core depends on integration)
- The output silently changes a Locked design doc contract

**Iterate when:**
- The output is structurally correct but has quality issues (missing tests, incomplete Javadoc)
- The output has minor constraint violations that can be fixed in place
- The output has [REVIEW] deviations that need evaluation
- The output needs additional edge case coverage

**Approve when:**
- All checklist items pass
- All deviations are [INFO] level or approved [REVIEW] level
- The output is traceable to the design doc and task brief
- Tests pass, including cross-subsystem consistency checks

---

## 6. Work Unit Completion Protocol (WUCP) — PM Obligations

After approving a completed work unit (Phase 2 block or Phase 3 milestone), execute WUCP Phase 2. Read the full protocol at `../context/protocols/work-unit-completion-protocol.md` §Phase 2.

**Before starting your review:** Run the session-start freshness preflight per `freshness-preflight.md`. If the hivemind is stale, the only allowed WUCP Phase 2 activity is the retroactive closeout for the last completed work unit — no forward review work until freshness is restored.

**Then verify the Coder's WUCP Phase 1 checklist** is present and complete at the bottom of the Completion Report. If it's missing or incomplete, return the report to the Coder.

**After approving the work unit (13 steps — see the protocol for full detail):**
1. Freshness preflight PASS
2. Verify Coder WUCP Phase 1 complete
3. Update (or create) the traceability index in `../../homesynapse-core/docs/traceability/` for the module (template at `../context/traceability/TEMPLATE.md`).
4. Mark the work unit DONE in `../context/planning/phase-3-milestone-backlog.md` (or `phase-2-block-backlog.md` for Phase 2 retroactive corrections) with commit and date
5. Update `../context/handoff/pm-handoff.md` — including the Open Risks section for deferred build gates
6. Append to `../context/lessons/pm-lessons.md` (if new patterns)
7. Update `../context/status/PROJECT_SNAPSHOT.md`
8. Update the current week's plan file
9. Deferred build gate audit — reconcile every deferred `./gradlew check` against Open Risks
10. Drift check across all artifacts
11. Dual skill-location sync check (`diff -rq` of both skill source trees vs `.claude/skills/nexsys-*` mirrors)
12. Inter-agent message sweep — confirm no blocking `[OPEN-QUESTION]`/`[VERIFY-NEEDED]` entries in `../context/open-questions.md`; `[FORESIGHT-NOTE]` entries carried forward
13. Append WUCP Phase 2 checklist to review output

The WUCP Phase 2 checklist format is documented in `work-unit-completion-protocol.md` Step 12. Use it verbatim.
