<!--
file: context/audits/2026-03-20_block-n-bcp-audit.md
purpose: Post-mortem of Block N (websocket-api), the first block executed under the Block Completion Protocol.
audience: PM, Nick
update-cadence: frozen
state-type: history
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Block N Post-Mortem — BCP Benchmark Audit

**Date:** 2026-03-20
**Auditor:** Hivemind
**Subject:** Block N (websocket-api) — first block executed under the Block Completion Protocol
**Transcript source:** Coder session, 2026-03-20
**Verdict:** BCP Phase 1 achieved **FULL COMPLIANCE** with one environmental asterisk (compile gate blocked by disk space). Code production quality is strong. The BCP worked on its first outing.

---

## 1. Execution Quality — Code Production

### Handoff Compliance

The Coder followed the prescribed execution order faithfully. Groups 1 through 6 were created in dependency order: enums first, then the filter record, then the WsMessage sealed hierarchy, then state records, then service interfaces, then module-info. All 26 Java types were created plus module-info.java. build.gradle.kts was updated with `api(project(":api:rest-api"))` as specified.

The one structural deviation from the handoff is in module-info.java: `requires transitive com.homesynapse.api.rest` instead of `requires com.homesynapse.api.rest`. This is correct behavior — the handoff's Locked Decision #10 was wrong for the same reason as Block K's Locked Decision #7. The Coder recognized this proactively rather than waiting for a compile failure, citing the Block K JPMS lesson. This is the ideal outcome of the lessons log system.

### Specification Fidelity

Spot-checked 7 of 26 types against the handoff specification:

- **WsMessage.java:** Sealed interface, permits exactly 13 subtypes in the correct order. `Integer id()` accessor. Javadoc documents the hierarchy split (4 client-to-server, 9 server-to-client). Matches spec.
- **WsSubscriptionFilter.java:** 10 fields, all nullable, correct types (6 `List<String>`, 1 `String`, 1 `Boolean`, 2 `Integer`). Compact constructor uses `field != null ? List.copyOf(field) : null` pattern for all 6 list fields. Matches spec exactly.
- **WsClientState.java:** 7 fields. Correctly imports `ApiKeyIdentity` from rest-api. Uses `Instant` for `authenticatedAt`. `Map<String, WsSubscription>` for activeSubscriptions with `Map.copyOf()` in compact constructor. `Objects.requireNonNull` on all non-null fields. Matches spec.
- **EventsMsg.java:** `List<Object>` for events (not `List<EventEnvelope>`). `id` is nullable `Integer`. `subscriptionId`, `deliveryMode`, and `events` validated non-null. `List.copyOf(events)` for defensive copy. Matches spec.
- **DeliveryMode.java:** 3 values: NORMAL, BATCHED, COALESCED. Each value has per-constant Javadoc explaining trigger conditions, buffer thresholds, and coalescable event types. References Doc 10 §3.7 and Doc 01 §3.6. Matches spec.
- **EventRelay.java:** 6 methods matching spec exactly: start, stop, addClient, removeClient, currentPosition, connectedClientCount. Javadoc explains the single-subscriber architecture rationale. Matches spec.
- **module-info.java:** `requires transitive com.homesynapse.api.rest; exports com.homesynapse.api.ws;` Deviation from spec (transitive) is correct per JPMS rules. Javadoc on the module declaration itself.

**No field name, type, or nullability errors found in any spot-checked file.** The Coder matched the handoff precisely on every dimension except the one that needed correction.

### Compile Gate

**BLOCKED.** The Cowork VM's internal filesystem ran out of disk space during the session. The bash tool creates temp directories before each command execution; with the filesystem at capacity, no bash commands could execute. Neither `./gradlew :api:websocket-api:compileJava` nor `./gradlew compileJava` was run.

This is an environmental failure, not a code quality failure. The code follows all established patterns from Blocks A–M and should compile cleanly. The `requires transitive` correction (identical to the Block K pattern) is the only JPMS change, and it's the correct one. **The compile gate must be run in a fresh session before Block N is formally accepted.**

### Locked Decision Compliance

All 15 locked decisions checked:

| # | Decision | Compliant? | Notes |
|---|----------|-----------|-------|
| 1 | Import shared types from rest-api | ✅ | ApiKeyIdentity, ApiException imported |
| 2 | WsMessage sealed with 13 subtypes | ✅ | Exact match |
| 3 | Integer (boxed) for id | ✅ | All subtypes use Integer |
| 4 | DeliveryMode new enum | ✅ | 3 values in websocket-api |
| 5 | WsCloseCode new enum | ✅ | 5 values with int code field |
| 6 | WsSubscriptionFilter is a record | ✅ | 10 nullable fields |
| 7 | String for subscriptionId/connectionId | ✅ | Not typed ULID wrappers |
| 8 | EventsMsg.events is List\<Object\> | ✅ | Not List\<EventEnvelope\> |
| 9 | StateSnapshotMsg.entities is List\<Object\> | ✅ | Same principle |
| 10 | requires com.homesynapse.api.rest only | ⚠️ DEVIATED | `requires transitive` — correct per JPMS rules, handoff was wrong |
| 11 | No cross-module updates | ✅ | Only websocket-api files touched |
| 12 | WsClientState is a record | ✅ | Point-in-time snapshot |
| 13 | Interfaces, not classes | ✅ | All 6 service types are interfaces |
| 14 | WebSocketHandler uses String for onMessage | ✅ | Raw JSON, not WsMessage |
| 15 | build.gradle.kts api() for rest-api | ✅ | `api(project(":api:rest-api"))` |

**14/15 compliant as written, 1/15 correctly deviated.**

### Javadoc Quality

Spot-checked 5 types:

1. **WsMessage.java:** Class-level explains the sealed hierarchy purpose, lists all subtypes by direction, documents thread-safety ("immutable records"). Has `@see MessageCodec`, `@see WebSocketHandler`, `@see` Doc 10 §8.2. The `id()` method documents nullable semantics for server-initiated vs client-initiated. **Strong.**

2. **WsSubscriptionFilter.java:** Class-level explains AND/OR semantics, Phase 3 resolution behavior, materialized set caching (Glossary §1.5 reference), max_resolved_subjects limit. Every `@param` documents nullability. `@see` cross-references to SubscribeMsg, SubscriptionConfirmedMsg, WsSubscription. **Strong.**

3. **DeliveryMode.java:** Class-level explains the three-stage model, per-value Javadoc explains trigger conditions and coalescable event types. References Doc 10 §3.7 and Doc 01 §3.6. `@see DeliveryModeChangedMsg`, `@see EventsMsg`. **Strong.**

4. **WsClientState.java:** Explains point-in-time snapshot semantics, shared auth infrastructure (Doc 10 §3.5), mutable-state-as-snapshot pattern. Every `@param` has nullability. `@see` ApiKeyIdentity, WsSubscription, ClientConnection, Doc 10 §8.2, §3.10. **Strong.**

5. **EventRelay.java:** Explains single-subscriber rationale (avoids N redundant reads), checkpoint advancement semantics ("after enqueued, not after consumed"), replay handling. `@see` ClientConnection, WsSubscription, WebSocketLifecycle, Doc 10 §3.6. **Strong.**

All 5 types pass all quality checks: @param nullability documented, @see cross-references present, thread-safety stated, class-level explains "why" not just "what," design doc sections cited. **No Javadoc quality issues found.**

---

## 2. BCP Phase 1 Compliance — The Real Test

**Grade: FULL COMPLIANCE** (with compile gate environmental exception)

### Step 1 — MODULE_CONTEXT.md

**Created: YES.** File exists at `homesynapse-core/api/websocket-api/MODULE_CONTEXT.md`, approximately 160 lines.

Contents verified against BCP requirements:

| Required Section | Present? | Quality |
|-----------------|----------|---------|
| Purpose | ✅ | One clear sentence plus elaboration. Identifies the REST API complement relationship. |
| Type Inventory | ✅ | All 26 types listed with purpose descriptions, organized by category (enums, filter, sealed hierarchy, state records, service interfaces). |
| Dependencies | ✅ | Phase 2 (rest-api only) and Phase 3 (event-model, event-bus, state-store, device-model, Jackson) both documented. |
| Consumers | ✅ | Current (none) and planned (lifecycle, dashboard, observability) listed. |
| Cross-Module Contracts | ✅ | 7 contracts enumerated: shared auth, shared error model, List\<Object\> avoidance of event-model leak, commands not over WS, WS doesn't produce domain events, shutdown ordering, per-connection rate limiting. |
| Constraints | ✅ | LTD-01, LTD-04, LTD-08, LTD-11, INV-ES-04 listed with descriptions. |
| Gotchas | ✅ | 6 gotchas: nullable Integer id, List\<Object\> events, conditional null-safe List.copyOf, old scaffold package-info, requires transitive deviation, String errorType. **These are genuine and useful** — particularly the nullable List.copyOf pattern and the requires transitive note. Not filler. |
| Phase 3 Notes | ✅ | 7 implementation notes: Event Relay checkpoint, MessageCodec Jackson setup, backpressure thresholds, authentication flow, filter resolution, replay admission, shutdown drain. |

**MODULE_CONTEXT.md is complete and high-quality.** The type inventory matches the actual file count. The gotchas section is substantive — a future Coder reading this file would avoid real pitfalls. The Phase 3 notes provide actionable implementation guidance without crossing into implementation code.

### Step 2 — coder-handoff.md

**Updated: YES.** File overwrites correctly reflect Block N:

- Block completed: Block N (websocket-api) ✅
- Files created: 26 files enumerated by category ✅
- Compile gate result: Documented as BLOCKED by VM disk space ✅
- Cross-module updates: None (correctly stated) ✅
- Deviations: `requires transitive` deviation documented with rationale ✅
- Next expected block: Block O (integration-runtime) ✅
- Known issue: Old scaffold package-info.java documented ✅
- Pattern discoveries: 2 new patterns noted ✅

**coder-handoff.md is complete and accurate.**

### Step 3 — coder-lessons.md

**Appended: YES.** Two new entries added:

1. **2026-03-20 | module-boundaries | Block N JPMS analysis:** Documents the third confirmation of the expanded JPMS `requires transitive` rule (Blocks I, K, N). Notes that the Coder applied the fix proactively before the compile gate. Impact statement: future handoffs should default to `requires transitive` for any cross-module public API type exposure.

2. **2026-03-20 | other | Block N nullable collection fields:** Documents the `field != null ? List.copyOf(field) : null` pattern for nullable list fields. Notes this is new — all previous blocks had non-null collections only. Impact statement: extends to Map fields.

**Both entries are substantive, follow the established format, and have clear impact statements.** The JPMS entry is particularly valuable because it records the cumulative pattern across three blocks and recommends a default-to-transitive policy.

### Step 4 — Cross-Agent Note

**Posted: YES.** Entry at `2026-03-20 [Coder → PM, Hivemind]` with topic "Block N complete — compile gate BLOCKED by VM disk space." Documents:

- Compile gate status and root cause (VM ENOSPC)
- JPMS deviation (same pattern as Block K, applied proactively)
- Cleanup needed (old scaffold package-info.java)
- New patterns logged
- MODULE_CONTEXT.md population status (8 modules now)
- Action needed: PM/Coder run compile gate, delete scaffold, PM produce Block O handoff

**Cross-agent note is warranted and complete.** The compile gate blocker is exactly the kind of information that needs cross-agent visibility.

### Step 5 — BCP Checklist in Completion Report

**Present: YES.** The Completion Report includes a "BCP Phase 1 Checklist" section at the bottom with all 5 steps checked:

```
| 1 | MODULE_CONTEXT.md populated | ✅ ~160 lines, complete type inventory |
| 2 | coder-handoff.md updated | ✅ Block N state, files, deviations, known issues |
| 3 | coder-lessons.md appended | ✅ 2 new entries (JPMS reconfirmation, nullable List.copyOf) |
| 4 | cross-agent-notes.md posted | ✅ Compile gate blocker, JPMS deviation, cleanup needed |
| 5 | Completion Report produced | ✅ This document |
```

**Minor format deviation:** The BCP specifies a `Timestamp: YYYY-MM-DD HH:MM UTC` line in the checklist. The Completion Report does not include an explicit UTC timestamp. The checklist uses a table format instead of the markdown checkbox format specified in the BCP (`- [x] ...`). These are cosmetic, not substantive — all information is present.

---

## 3. Prompt Engineering Observations

### Context Loading

The Coder loaded context documents in a reasonable order. It read the skill reference files (homesynapse-mental-model.md, java-patterns.md, deviation-and-quality.md), PROJECT_SNAPSHOT.md, cross-agent-notes.md, coder-handoff.md, coder-lessons.md, the Block N handoff, and the rest-api MODULE_CONTEXT.md. It also read ApiKeyIdentity.java from rest-api to verify the import target.

**No files were skipped.** The Coder read every file relevant to its work. It did not load unnecessary files — it correctly scoped its context loading to the files it would actually reference during code production.

The one observation: the Coder read the handoff in chunks due to its length (200+ lines), requiring multiple Read operations. This is a consequence of the handoff's size, not a loading failure.

### Instruction Clarity

The handoff was exceptionally detailed. The Coder did not appear confused at any point during code production. Every type was created with the correct fields, types, and Javadoc on the first attempt — no rework was needed for any file.

The one point of ambiguity the Coder navigated correctly was the old scaffold `package-info.java` in `com.homesynapse.api.websocket` vs the new package `com.homesynapse.api.ws`. The handoff's file placement section mentioned deleting a scaffold at the new path, but the actual scaffold was in the old path. The Coder reasoned through this correctly: the old package-info.java in a non-exported package is benign and doesn't need deletion for compilation. This was good judgment under ambiguity.

### Attention Allocation

The session's token expenditure breaks down roughly as:

1. **Context loading:** ~15% — Reading reference docs, handoff, existing code
2. **Disk space troubleshooting:** ~30% — Attempting to free space, trying multiple approaches to run bash
3. **Code production (Groups 1–6):** ~35% — Creating all 26 types
4. **BCP Phase 1:** ~15% — MODULE_CONTEXT.md, handoff updates, lessons, cross-agent note, completion report
5. **Self-review and deviation analysis:** ~5% — Verifying JPMS requirements

**The disk space troubleshooting consumed a disproportionate share of the session.** The Coder spent significant effort trying to free space by truncating files, cleaning caches, and exploring workarounds. This was reasonable initial effort but should have been abandoned earlier — after 3-4 failed attempts to run bash, the correct decision (which the Coder eventually made) was to proceed with Write-only code production and report the compile gate as blocked.

**Code production efficiency was high.** The Coder created 26 files with full Javadoc in roughly 35% of the session's effort. No rework was needed on any file. The BCP Phase 1 execution was also efficient — all 5 steps completed with appropriate content.

### BCP Trigger Recognition

The Coder recognized the BCP as mandatory. After creating all types and acknowledging the compile gate blocker, the Coder explicitly read the block-completion-protocol.md file and then executed all 5 steps in order. The transition from code production to BCP execution was deliberate, not accidental.

The Coder's todo list tracked BCP execution as a distinct phase, and the Coder updated the list as it completed each BCP step. This suggests the BCP was internalized as a required gate, not an afterthought.

---

## 4. Process Failures and Root Causes

### Failure 1: Compile Gate Not Executed

**What happened:** The VM's internal filesystem filled up during the session, preventing any bash command execution. The compile gate was never run.

**Why it happened:** The Cowork VM allocates a small internal filesystem for session temp files. Over the course of a long session with many tool calls, the accumulated temp artifacts and session data exhausted available space. The bash tool's temp directory requirement (`/sessions/.../tmp/claude-*`) is a hard dependency that cannot be bypassed.

**Fix category:** **Systemic.** This is a Cowork VM resource management issue, not something the agent prompt or BCP can fix. The BCP correctly requires the compile gate before Phase 1 closeout, but environmental constraints prevented it.

**Mitigation:** The Coder correctly documented the blocker and requested manual verification. The cross-agent note ensures the PM knows the gate is pending. The BCP Completion Report marks the gate as BLOCKED rather than falsely claiming PASS. This is the right behavior.

### Failure 2: BCP Checklist Format Deviation

**What happened:** The BCP checklist in the Completion Report uses a table format instead of the markdown checkbox format specified in the protocol (`- [x/  ] ...`), and omits the UTC timestamp.

**Why it happened:** The BCP protocol shows the checklist in a specific format with checkboxes and a timestamp line. The Coder used a table format that conveys the same information but doesn't match the template exactly. This is likely because the Coder had already been using tables throughout the Completion Report and continued the pattern.

**Fix category:** **Prompt fix.** The BCP protocol should emphasize that the checklist format is canonical (for machine-parseable verification by the PM). Alternatively, if table format is acceptable, the BCP should show both formats.

### Failure 3: Old Scaffold Not Deleted

**What happened:** The old `package-info.java` at `com.homesynapse.api.websocket` was not deleted because bash was unavailable.

**Why it happened:** Environmental constraint (same as Failure 1). The Coder correctly identified the issue and documented it as a known cleanup item.

**Fix category:** **Systemic** (same root cause as the compile gate). The cross-agent note correctly flags this for the next session.

### Failure 4: Handoff JPMS Analysis Was Wrong (Third Occurrence)

**What happened:** Locked Decision #10 in the Block N handoff specified `requires com.homesynapse.api.rest` (non-transitive). The correct directive is `requires transitive com.homesynapse.api.rest`.

**Why it happened:** The PM's JPMS analysis in the handoff missed that `ApiException` in throws clauses and `ApiKeyIdentity` in record components qualify as public API surface under JPMS. This is the same error pattern as Blocks I and K. The expanded JPMS rule (record components, method params, return types, exception superclasses, exception types in throws clauses all require `requires transitive`) was documented after Block K but apparently not applied retroactively to the Block N handoff's JPMS analysis.

**Fix category:** **Handoff fix.** The PM's handoff template or process should include a JPMS verification step that explicitly checks every inter-module type reference against the expanded rule. The default should be `requires transitive` for any cross-module dependency; `requires` (non-transitive) should only be specified when the PM can prove no types from the dependency appear in any public API surface.

---

## 5. Strengths to Preserve

1. **Proactive JPMS correction.** The Coder applied the Block K lesson without waiting for a compile failure. This is the lessons log system working exactly as designed — procedural memory compounding across sessions. The Coder explicitly cited the Block K lesson in both the code comment and the deviation documentation.

2. **MODULE_CONTEXT.md quality.** The gotchas section contains 6 entries, all genuine. The nullable List.copyOf pattern, the requires transitive deviation, and the old scaffold note are exactly the kind of information that prevents future sessions from making mistakes. This is not filler — it's useful institutional memory.

3. **Zero rework.** All 26 types were created correctly on the first attempt. No file was edited after initial creation (except module-info.java for the JPMS correction, which was also done before any compile attempt). This indicates the handoff quality is high and the Coder's context loading is thorough.

4. **Clean BCP execution.** All 5 Phase 1 steps completed in order, with substantive content at each step. The Coder didn't rush through BCP as a formality — the MODULE_CONTEXT.md is ~160 lines, the lessons log entries have genuine impact statements, and the cross-agent note has actionable items.

5. **Honest compile gate reporting.** The Coder did not falsely claim the compile gate passed. It clearly documented the environmental blocker, explained why the code should compile cleanly (pattern consistency with 12 previous blocks), and requested manual verification. This is the right judgment call — reporting honestly rather than claiming success.

6. **Disk space resilience.** When bash became unavailable, the Coder adapted by using Write tool exclusively for code production (which writes to the mounted filesystem, not the VM's internal disk). It spent some time troubleshooting but eventually made the correct tactical decision to proceed with available tools and document the limitation.

---

## 6. Recommendations

### Changes to the BCP

| # | What to Change | Why | Priority | Effort |
|---|---------------|-----|----------|--------|
| 1 | Add explicit format requirement note to Phase 1 Step 5: "Use the exact checklist format shown above, including checkbox syntax and UTC timestamp." | Prevents format drift (Failure 2) | Normal | One-line edit |
| 2 | Add a note to Phase 1 that the compile gate being blocked by environmental factors is a valid documented outcome, distinct from a compile failure: "If the compile gate cannot be run due to environmental constraints, document the blocker and mark the gate as BLOCKED. The PM verifies the gate in their Phase 2 review." | Codifies the correct behavior the Coder exhibited | Normal | Paragraph addition |

### Changes to Agent Skills

| # | What to Change | Why | Priority | Effort |
|---|---------------|-----|----------|--------|
| 3 | Coder skill: Add a heuristic for disk space management — "If bash fails with ENOSPC, make at most 3 attempts to free space. If unsuccessful, switch to Write-only mode and document the bash blocker. Do not spend more than 5 minutes troubleshooting disk space." | The Coder spent ~30% of session tokens on disk troubleshooting. A clear policy would save tokens. | High | New paragraph in CLAUDE.md |
| 4 | Coder skill: Add explicit instruction to match BCP checklist format exactly: "The BCP Phase 1 checklist must use the exact format from block-completion-protocol.md, including `- [x]` checkbox syntax and `Timestamp: YYYY-MM-DD HH:MM UTC`." | Prevents format drift | Normal | One-line addition |

### Changes to Prompt/Handoff Templates

| # | What to Change | Why | Priority | Effort |
|---|---------------|-----|----------|--------|
| 5 | PM handoff template: Change JPMS `requires` default to `requires transitive` for all inter-module dependencies, with explicit justification required for non-transitive. Add verification step: "For every `requires` directive, verify that NO types from the required module appear in any record component, method parameter, return type, exception superclass, or throws clause in this module's public API." | Prevents the recurring JPMS handoff error (Blocks I, K, N). Third occurrence makes this a systemic pattern, not a one-off. | **Critical** | Paragraph rewrite in handoff template |
| 6 | Block handoff: Add a "Cleanup Items" section for pre-existing scaffold artifacts that need deletion. Currently these are discovered during execution and noted in deviations — they should be identified in the handoff. | Prevents the scaffold-in-wrong-package discovery during execution | Normal | New section in template |

### Systemic Observations

| # | Observation | Impact |
|---|------------|--------|
| 7 | **Cowork VM disk space is a recurring risk.** Block K also hit disk space issues (bash unavailable for scaffold deletion). Block N exhausted the filesystem entirely. As blocks grow larger and sessions accumulate more tool-result artifacts, this will happen more often. | The Coder's session produces large Read output files that are persisted to the internal disk. These accumulate across the session. The VM's internal filesystem is small. This is outside agent control but affects execution quality. |
| 8 | **The handoff document length (200+ lines) approaches the useful limit.** The Block N handoff is the most detailed yet — every field, every Javadoc paragraph, every constraint spelled out. This produced zero-rework code, but it also consumed significant context window during loading. As modules get more complex, handoffs may need to be split (e.g., a type specification appendix separate from the strategic context and constraints). | No immediate action needed. Monitor handoff size for Block O and beyond. |

---

## 7. BCP Protocol Health Assessment

### 1. Is the BCP working as designed?

**Yes.** The three-phase chain produced exactly the intended outcome for Phase 1. After Block N:

- MODULE_CONTEXT.md accurately reflects the 26 types in websocket-api, with genuine gotchas and actionable Phase 3 notes
- coder-handoff.md accurately reflects Block N's state, including the compile gate blocker and the JPMS deviation
- coder-lessons.md has two substantive entries that future sessions will benefit from
- The cross-agent note ensures the PM and Hivemind know about the pending compile gate and cleanup

The documentation state matches the code state. The BCP's thesis — that documentation updates should be a gate, not an afterthought — is validated. The Coder treated BCP Phase 1 as a required part of the block, not optional extra work.

### 2. Is the BCP sustainable at velocity?

**Yes, at current block size.** BCP Phase 1 consumed roughly 15% of the session's effort — a reasonable overhead for the documentation quality it produces. The Coder was able to complete all 5 steps within the same session as code production, as required.

The key factor is that most BCP Phase 1 content is synthesized from work the Coder just did — it doesn't require new research or cross-referencing. MODULE_CONTEXT.md is a structured summary of the types just created. The handoff update is a status report. The lessons log entries describe patterns just encountered. This makes BCP Phase 1 a natural reflection step, not a documentation burden.

**Risk at scale:** If blocks grow to 50+ types (like automation's 55 files), the MODULE_CONTEXT.md type inventory becomes a significant writing task. Consider whether a templated generation step (e.g., a script that extracts type signatures from the source files) could accelerate this.

### 3. What breaks first at scale?

**The cross-agent note system.** Currently, `cross-agent-notes.md` is an append-only bulletin board. As the project grows, this file will accumulate entries from every block execution. The signal-to-noise ratio will degrade — agents will need to read through dozens of historical notes to find the ones relevant to their current work.

The first symptoms will be:

1. Agents spending tokens reading irrelevant historical notes
2. Important notes getting buried below older resolved items
3. Action items marked "needed" that are never confirmed as completed

**Second to break: MODULE_CONTEXT.md consistency.** As cross-module dependencies increase (Phase 3 will add many), keeping every module's MODULE_CONTEXT.md "Consumers" and "Dependencies" sections current across multiple modules becomes a coordination problem. Block N didn't touch other modules, but Phase 3 blocks will — and each cross-module update needs to update multiple MODULE_CONTEXT.md files.

**Recommended mitigation for cross-agent notes:** Add an "ARCHIVED" section separator. When an agent reads a note and confirms the action is complete, move it below the separator. Only notes above the separator are active. This keeps the file append-only while managing the signal-to-noise ratio.

**Recommended mitigation for MODULE_CONTEXT.md drift:** In BCP Phase 2, the PM should verify that the MODULE_CONTEXT.md "Consumers" section of every module this block depends on lists the new module. This is already implicitly required by the drift check in Phase 3, but making it explicit in Phase 2 catches it earlier.
