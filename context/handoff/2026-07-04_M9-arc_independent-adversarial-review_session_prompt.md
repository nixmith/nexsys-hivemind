<!--
file: context/handoff/2026-07-04_M9-arc_independent-adversarial-review_session_prompt.md
purpose: Dispatch brief for an INDEPENDENT adversarial review lane over the M9 arc (M9.1–M9.3 integration code) at core c856eab. Bug-hunt, not style review: logic, concurrency, protocol semantics, spec divergence — the defect classes compilers and green tests do NOT catch.
audience: a fresh Cowork session (read-only; nexsys-coder skill for the mental model + java-patterns; NO code writes); Nick (launches); the PM hub (audits the return two-layer).
state-type: session prompt (lane)
status: READY — authored 2026-07-04 by the v17 hub (beat 4). Launch anytime; write-disjoint from everything (read-only lane, one return file). Runs in PARALLEL with M9.4 authoring.
baseline: core `c856eab` (M9.3 landed, ./gradlew check GREEN 153 + CI green on the push) · docs `01602fa` · bench `5ceff3b`. The code you review has PASSED every automated gate — you hunt what gates structurally cannot catch.
-->

# Session Brief — M9-Arc Independent Adversarial Review (find what green cannot see)

You are an independent senior reviewer with NO authorship stake in this code. Your charge: find bugs, logical/computational errors, concurrency hazards, protocol-semantics divergences, and forward-scalability traps in the M9 integration arc BEFORE M9.4 wires it to the command path and real silicon. A `./gradlew check` + CI green baseline means the cheap defect classes are gone — you are paid for the expensive ones.

## 1. Ground first (read-only)

`context/process/cowork-environment-model.md` (§2 phantom family — NEVER trust VM git output; §4 no index-touching git; host file tools are truth) → `working-with-nick.md` + `decision-rationale-index.md` → the M9.3 instruction (`context/instructions/2026-07-03_M9.3_interview-ingestion-profile-registry_coding-instruction.md`) + `context/pre-verifications/WU-M9.3.md` → pm-handoff v17 beats 1–3 (the rulings) → `integration/integration-zigbee/MODULE_CONTEXT.md` (all gotchas) → Doc 08 §3.3–§3.7/§3.12–§3.14 · Doc 02 §3.8/§3.12 · AMD-96/97 · Doc 05 §3.7 (exception classification). Bench ground truth: `nexsys-bench/corpus/devices/*` + `fixtures/*` + the coordinator file.

## 2. Scope (core `c856eab`)

**Primary:** `integration/integration-zigbee/src/main/**` (all 100 types — M9.2 transport/ASH/EZSP + M9.3 pipeline) + its test tree (test-LOGIC errors are in scope: a test that asserts the wrong thing is a finding). **Secondary (the seams M9.4 will stress):** `core/automation` `StandardPendingCommandLedger` + `StandardActionExecutor` confirmation path · `core/device-model` `Expectation`/`WithinTolerance`/`ConfirmationMode`/`CommandDefinition` · `integration-runtime` supervisor/`ExceptionClassifier`/`CommandRoutingSubscriber` · the `integration-api` frozen surfaces they cross.

**Priority surfaces (ranked — the M9.4-critical list):**
1. **Replay purity adjacency:** anything in the zigbee ingestion/adoption path that could EVER publish or actuate on REPLAY-order delivery (INV-ES-09 — the moat's honesty depends on it; M9.4 registers the first real CommandHandler).
2. **The ledger/expectation evaluation path** end-to-end: coercion (`coerce(...)` in the ledger), `WithinTolerance.evaluate` numeric edges (NaN/Infinity/overflow on `double` compare; `QuantityValue` normalization traps), EXACT_MATCH vs typed values, deadline arithmetic at clock edges.
3. **Concurrency:** `PendingInterviewQueue` / `ReportDeduplicator` / `ZigbeeDeviceCache` (debounce + load/write races) / `StandardAvailabilityTracker` / `StandardDeviceProfileRegistry` lock discipline (LTD-11: ReentrantLock only — also check lock ORDER and what's held across I/O or publishes), `EzspCoordinatorProtocol` single-in-flight + callback-drain interactions.
4. **Protocol semantics vs the standard:** ASH framing/derandomization/CRC + sequence-number edges (mod-8 wrap under retransmit), EZSP frame-format edges (legacy 0x0000 negotiation, v13 vs v14 dialect assumptions), ZDO/ZCL codec field ordering + endianness + signed/unsigned traps (the `int`-everywhere convention's boundary crossings), TSN wrap in dedup, mireds=0 division guard, bitmap8 occupancy parsing.
5. **FSM edge cases:** interview timeout boundaries (exactly-10s/exactly-60s at the clock edge), retry-ladder off-by-ones, sleepy park/resume races (frame arrives DURING expiry evaluation), PARTIAL-vs-COMPLETE classification, rejoin during in-flight interview, dedup-clear vs in-window twins.
6. **Loader/data:** profile JSON edge cases (duplicate criteria, empty strings vs nulls, priority collisions producing nondeterminism the lexicographic key doesn't cover, schemaVersion minor-field absence), cache corruption recovery completeness, path handling on Windows vs Linux.
7. **Forward-scalability traps** (name them even when not bugs today): unbounded maps keyed by IEEE across device churn; O(n·m) match scans at thousands-of-profiles scale (§F index-first honored?); anything that couples the corpus format to core release cadence (§I); anything a Matter/plugin adapter would find un-reusable in the confirmation seam.

## 3. Settled ground (defend-don't-relitigate — but REFUTE with evidence if actually wrong)

The five M9.3 [REVIEW] rulings (queue-scheduled retry · endpointless-ISE · 4-field DeviceDiscoveredEvent + "unknown" sentinel · DeviceRegistry ctor-injection · stub-test update), the §1 freezes (eight fields, sealed MatchCriteria, precedence, namespace), the five [INFO]s (incl. dedup payload-scope), and the two-handler-seam duality — all ruled, pointers in pm-handoff v17 beat-3. Re-arguing preference is out of scope; a ruling REFUTED BY EVIDENCE (a concrete failing scenario) is explicitly welcome — the audit culture rewards it (the dist-gitignore precedent).

## 4. Method (evidence or it does not exist)

Every finding carries: file:line (host paths) · the defect class · a CONCRETE failing scenario (input sequence, interleaving, or byte-level derivation — "this could be a problem" without a trigger is a NOTE, not a finding) · severity (CRITICAL = wrong verdict/data-loss/actuation hazard; HIGH = functional defect on a real path; MEDIUM = edge-case defect; LOW/NOTE = hardening or scalability observation) · the suggested fix DIRECTION (one line, no patches). External-standard claims (ASH/EZSP/ZCL) cite the standard or the reference implementation (bellows/zigpy lineage) — re-derive, never recall. Two-grep rule before any ABSENT claim. NO builds, NO gradle, NO file writes outside your ONE return file, NO VM-git trust (read files via host tools only).

## 5. Deliverable + return protocol

ONE file: `context/audits/2026-07-04_M9-arc_adversarial-review_return.md` — masthead (baseline SHAs, scope actually covered, method) · severity-ranked findings table (claim → evidence → scenario → fix direction) · a NOTES section for scalability observations · an explicit "surfaces swept clean" list (what you checked and found sound — the absence claims matter as much as the findings) · your §10-style write-isolation statement (exactly 1 file). The PM hub audits two-layer (your claims AND your observations); Nick commits host-side. If you find a CRITICAL, say so in your first line.
