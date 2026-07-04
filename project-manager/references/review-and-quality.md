<!--
file: project-manager/references/review-and-quality.md
purpose: Review checklists for design docs, interface specs, and Coder output before declaring work complete.
audience: PM
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-06-07 against commit 8028337
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

**Correctness over conformance.** When a `[REVIEW]` deviation cites "preserves prior behavior / avoids a regression," weigh it against the spec on **correctness grounds, not literal spec-conformance** — a coder deviation from a *ratified* amendment can be more-correct than the literal spec (the AMD-51 §2.6 string-fallback that avoided a permanent attribute-freeze regression is the model case). When code ships ahead of a needed spec erratum, **log the erratum as an Open Item in pm-handoff** so the ratified doc is reconciled, rather than letting spec and code drift apart silently.

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

**After approving the work unit (0-indexed to match the protocol; Step 0 = preflight):**
0. Freshness preflight PASS
1. Verify Coder WUCP Phase 1 complete
2. Update (or create) the traceability index in `../../homesynapse-core/docs/traceability/` for the module — there is **no separate template**; mirror an existing index (the old `../context/traceability/TEMPLATE.md` was removed in the 2026-04-11 overhaul)
3. Mark the work unit DONE in `../context/planning/phase-3-milestone-backlog.md` (or `phase-2-block-backlog.md` for Phase 2 retroactive corrections) with commit and date
4. Update `../context/handoff/pm-handoff.md` — including the Open Risks section for deferred build gates
5. Append to `../context/lessons/pm-lessons.md` (if new patterns)
6. Update `../context/status/PROJECT_SNAPSHOT.md`
7. Update the current week's plan file
8. Deferred build gate audit — reconcile every deferred `./gradlew check` against Open Risks
9. Drift check across all artifacts
10. Dual skill-location sync check (`diff -rq` of both skill source trees vs `.claude/skills/nexsys-*` mirrors)
11. Inter-agent message sweep — confirm no blocking `[OPEN-QUESTION]`/`[VERIFY-NEEDED]` entries in `../context/open-questions.md`; `[FORESIGHT-NOTE]` entries carried forward
12. Append WUCP Phase 2 checklist to review output

The WUCP Phase 2 checklist format is documented in `work-unit-completion-protocol.md` Step 12. Use it verbatim. (The skill-sync is **Step 10** in this 0-indexed scheme — matching the WUCP body and the freshness preflight.)

**Ticked-artifact closeout (P3).** "Closeout applied" is not assertable until every artifact is ticked — the fixed six (PROJECT_SNAPSHOT incl. its Recent-Session-Log row; pm-handoff; cross-agent-notes; **coder-handoff with the gate flip OPEN→RESOLVED + commit SHA**; milestone-backlog; weekly-plan incl. its Current-state footer) plus the touched MODULE_CONTEXTs and any Doc body-folds the amendment mastheads point to. The freshness preflight's backlog/weekly checks are load-bearing precisely because a hurried closeout under-updates those two. Write the real commit SHA at closeout — retire the placeholder-`sed`.

**Amendment review depth (P4).** Match review ceremony to the amendment track (`constraint-enforcement.md §6`): a shared block review for trivial additive amendments; a full independent DOCS-Project review for anything touching a persisted shape, a behavioral contract, or a new invariant.

**Audit fan-out with embedded expected values (P5-audit, adopted 2026-07-04 — the M9.3 zero-defect audit's method).** For a large return, partition the surfaces across parallel READ-ONLY verification agents and **embed the authoritative expected values in each agent's brief** so the agent COMPARES (MATCH/MISMATCH per item) instead of describing — a describing agent hides drift; a comparing agent surfaces it. **Independently RECOMPUTE derived test values** (fixture-derived edge counts, unit conversions, arithmetic pins) rather than trusting the assertions under review. The hub keeps the single highest-consequence surface for direct read (trust-but-verify on your own fan-out), spot-checks every agent ABSENT/census claim (the M9.3 "only 4 public types" refutation — agent returns get layer-2 audited exactly like lane returns), and treats claimed-but-unsighted closeout artifacts as UNVERIFIED until grep-confirmed at their stated location (the appended-below-separator catch: the artifact existed, but not where the convention puts it). **Two audit-craft rules (added 2026-07-04 — the M9.4a refuted-DEFECT lesson; pm-lessons 2026-07-04 #1):** (1) when embedding expected semantics in an audit-agent brief, QUOTE the instruction's own sentences verbatim for anything subtle (supersession/expiry/ordering rules) — a paraphrased mandate becomes the agent's phantom truth, and a comparator faithfully amplifies wrong expectations into HIGH-confidence false DEFECTs; (2) agent verdict LABELS are CLAIMS and agent QUOTES are EVIDENCE — layer-2 adjudicates every DEFECT/REFUTED verdict against the PRIMARY text (the instruction + the ratified doc), never against the agent's restatement of the mandate; twice in one arc the quoted evidence was sound while the judgment layer was noise.

**Post-green adversarial review (adopted 2026-07-04 — the M9-arc precedent).** At an arc boundary (a subsystem newly complete, before the milestone that WIRES it), a full-`check`+CI-green record still buys an independent adversarial-review lane: read-only, no authorship stake, hunting the classes automated gates structurally cannot catch (logic, concurrency interleavings, protocol-semantics vs the external standard, spec divergence, scalability traps). Findings require a CONCRETE trigger (input sequence / interleaving / byte-level derivation) — otherwise they are NOTES; settled rulings are fenced but evidence-backed refutation is welcome; clean-sweep ABSENT claims are two-grep verified and listed (the absence record matters as much as the findings). The M9-arc lane returned 3 HIGH on a green baseline — deaf-radio, false-CONFIRMED, and unreachable-confirmation classes — each caught at desk price instead of bench price.
