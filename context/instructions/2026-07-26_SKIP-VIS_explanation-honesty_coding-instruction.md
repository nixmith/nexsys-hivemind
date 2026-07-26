<!--
file: context/instructions/2026-07-26_SKIP-VIS_explanation-honesty_coding-instruction.md
purpose: Coding instruction for WU-SKIP-VIS — the explanation-honesty set: CORE-P1 (raw-outcome carry; superseded never FAILED; honest-unconfirmed derives UNCONFIRMED), CORE-P2 (completedVerdict silent-skip honesty), and THE RUNS-TRIGGEREDAT FIX (both derivation sites), under the ruled v1.1.2 four-constraint law (Nick ruling 1, 2026-07-22, verbatim in context/decisions/2026-07-22_nick-rulings-1-5_verbatim.md). One instruction, one audit, one deploy (pm-handoff v37 beats 2–3; the fold is GO on Nick's conditional).
audience: Coder (host-side Claude Code lane, homesynapse-core; nexsys-coder skill); PM hub (two-layer audit on return).
status: ISSUE-READY — ⛔ DP-4 ONLY is gated on Nick's one-line Q1b ruling (carried in the dispatch turn; every other part is ruled and unconditional).
baseline: core `4bc1258` (re-verify at dispatch — any drift ⇒ STOP and report; line numbers below were re-enumerated at source against this HEAD on 2026-07-26).
lane-law: core stays SERIALIZED (this is the only core lane); tests BEFORE implementation; the hub's two-layer audit precedes ANY commit; commit messages carry NO attribution trailers (env-model §9).
-->

# Coding Task: WU-SKIP-VIS — Explanation Honesty (raw outcome carry · silent-skip verdict honesty · the triggeredAt fix)

**Subsystem:** Automation (Superior Automation Layer, Doc 16 §3.3 — the log-derived explanation projection) + REST API (the frozen v1.1 dashboard read surface)
**Design Doc:** Doc 16 (Superior Automation Layer) — LOCKED; Doc 07 §3.9 (per-target skip gate) — LOCKED; the FROZEN v1.1 dashboard read-API contract (`nexsys-hivemind/context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md`) as amended by **the v1.1.2 ruling** (Nick ruling 1, 2026-07-22 — additive-only · wire-casing at the endpoint · emitter-leads · version discipline)
**Phase:** 3-Implementation
**Task Brief Reference:** v38 orchestrator charge 3 (SKIP-VIS — the fold GO); pm-handoff v37 beats 2–3 (the RUNS-TRIGGEREDAT adjudication + Nick's conditional); the G1 explainability-lane return §5–§6 (`nexsys-hivemind/context/audits/2026-07-19_explainability-ux-lane_return.md` — CORE-P1/CORE-P2 verbatim); the Rosonway report §4 (`nexsys-hivemind/context/handoff/2026-07-25_rosonway-topology-move_I3b_bench-session-report.md` — the fix DP's ground truth)

## What This Implements

The explanation projection (`StandardExplanationService`, Doc 16 §3.3) is the read-side that answers the product's hero questions — "why did it fire?", "why didn't it?", "did it actually confirm?" — purely from the immutable event log (INV-SA-03). Three honesty defects live in it today, all confirmed at source. **(1)** `deriveOutcome` collapses every non-`acknowledged` `command_result` into `FAILED`, so a deliberately **superseded** command renders as a failure and zigbee's **honest-`unconfirmed`** verdict (an ACK followed by silence — the system explicitly refusing to treat an ACK as proof) renders as `FAILED` instead of `UNCONFIRMED`; the raw ten-value outcome vocabulary never reaches the wire (G1 return GAP-1/CORE-P1). **(2)** `completedVerdict` reports a COMPLETED run that issued **zero device commands** (all device actions skipped per Doc 07 §3.9, or none defined) as the clean-success "last fired and confirmed" — a do-nothing run rendering as confirmed success, the composed-behavior defect class that produced four days of lawful do-nothing runs reading as success in the I3a era (CORE-P2). **(3)** `toSummary` computes `triggeredAt = terminalTime − durationMs` on the assumption that the terminal envelope's `eventTime` is completion time — but under the ruled DP-G inheritance (`StandardRunManager` stamps the run family with the TRIGGERING event's `eventTime`), that `eventTime` IS the trigger instant, so the wire understates `triggeredAt` by exactly the run's duration (Rosonway §4: proven to the microsecond on two runs of differing duration; it creates a duration-wide false-FAIL dead zone in the bench's `new_run_after` instrument). The same wrong arithmetic has a **second site**: `explainNonFiring`'s `evaluatedAt` (found at authoring re-enumeration). This WU fixes all three at the derivation layer, adds the two ruled additive wire keys, and changes **no emitter and no existing wire key** — the emitters are lawful; the read side stops mis-deriving from them.

## Files to Read Before Starting

| File | Why |
|---|---|
| `core/automation/MODULE_CONTEXT.md` | Type inventory, cross-module contracts, Gotchas (read the Gotchas + Phase 3 Notes sections in full) |
| `core/automation/src/main/java/module-info.java` | Verbatim JPMS graph (quoted below — verify unchanged; this WU makes ZERO module-info changes) |
| `api/rest-api/MODULE_CONTEXT.md` | The endpoint layer's contracts + the plain (non-transitive) `requires com.homesynapse.automation` note |
| `api/rest-api/src/main/java/module-info.java` | Verbatim JPMS graph (quoted below — ZERO changes) |
| `core/automation/src/main/java/com/homesynapse/automation/StandardExplanationService.java` | The target file — all three DPs live here |
| `core/automation/src/main/java/com/homesynapse/automation/StandardRunManager.java` | The DP-G emitter half: `eventTime = triggeringEvent.eventTime()` (≈`:210`, comment "inherited or null (DP-G)") and `publishCompleted` (≈`:656–:665`) publishing `run.eventTime` + live-measured `durationMs` — read so the fix's premise is understood, then leave untouched |
| `core/automation/src/main/java/com/homesynapse/automation/RunExplanation.java` | `ActionView` (currently 6 components) + `OutcomeView` — DP-1's record delta |
| `core/automation/src/main/java/com/homesynapse/automation/NonFiringExplanation.java` | The 8-component record + 4-value `NonFiringVerdict` — DP-2's record delta; do NOT grow the verdict enum |
| `core/automation/src/main/java/com/homesynapse/automation/RunSummary.java` | The `triggeredAt` javadoc parenthetical DP-3 corrects |
| `core/event-model/src/main/java/com/homesynapse/event/CommandResultEvent.java` | The live ten-value outcome vocabulary (`:22–:27` region) — DP-1's classification input, embedded below |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/GetRunCausalChainEndpoint.java` | `actionsList` — where `resultOutcome` (and gated `settled`) land |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/GetNonFiringEndpoint.java` | `toWire` — where `noCommandsIssued` lands |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/ListRunsEndpoint.java` | READ-ONLY: `toWire` + `wireStatus` — the runs-list wire must remain byte-identical in shape. (Law (b)'s casing is read at each TARGET endpoint — the new keys' casing reference is the sibling keys in the very maps they join) |
| `core/automation/src/test/java/com/homesynapse/automation/StandardExplanationServiceTest.java` | The seeding idiom (`seedRun`/`publishRoot`/`publishDerived`, `InMemoryEventStore(FIXED_CLOCK)`) the new tests must follow |
| `core/automation/src/test/java/com/homesynapse/automation/NonFiringExplanationServiceTest.java` | Existing non-firing coverage the DP-2/DP-3b tests extend |
| `api/rest-api/src/test/java/com/homesynapse/api/rest/RunEndpointsTest.java` | The causal-chain/runs wire pins (only `:201` updates; the rest are SD-5 regression proof) |
| `api/rest-api/src/test/java/com/homesynapse/api/rest/AutomationEndpointsTest.java` | The non-firing wire pin (`:79–:80`) + the 8-arg `NonFiringExplanation` construction sites — this WU's non-firing test home (G-7b) |
| `nexsys-hivemind/context/decisions/2026-07-22_nick-rulings-1-5_verbatim.md` | Ruling 1 — the four-constraint law governing every wire delta here |
| `nexsys-hivemind/context/handoff/2026-07-25_rosonway-topology-move_I3b_bench-session-report.md` §4–§5 | The field evidence for DP-3 (§4), DP-1's superseded/honest-unconfirmed exhibits (§5.1), the silent-skip context (§5.2), §5.9 (DP-4's motivation) |
| `nexsys-hivemind/context/audits/2026-07-19_explainability-ux-lane_return.md` §5–§6 | CORE-P1/CORE-P2 as the consuming lane stated them (the ruled asks this WU realizes) |

## STOP-on-Mismatch Gates

Before writing any code, read and verify. Any divergence ⇒ STOP and report; do not proceed on stale assumptions.

| # | File | Expected state (verified 2026-07-26 at `4bc1258`) |
|---|---|---|
| G-1 | `StandardExplanationService.java` | 724 lines. `toSummary` declared `:453`; the subtraction `Instant triggeredAt = terminalTime.minusMillis(Math.max(0L, payload.durationMs()));` at `:466`; `explainNonFiring`'s `Instant evaluatedAt = terminalInstant(latest).minusMillis(Math.max(0L, payload.durationMs()));` at `:228–:229`; `completedVerdict` declared `:284`; `deriveOutcome` declared `:616`; `isFailure` at `:656`; private `record Outcome(RunExplanation.ActionOutcome value, String reason)` at `:661` |
| G-2 | `StandardExplanationService.java` `buildTrigger` | `matchedAt = triggered.eventTime() != null ? triggered.eventTime() : triggered.ingestTime()` — NO arithmetic (this is the already-correct sibling DP-3 aligns `toSummary` with) |
| G-3 | `RunExplanation.ActionView` | Exactly 6 components: `type, targetRef, command, paramsJson, outcome, reason` (construction sites: `StandardExplanationService:584`, `:610`, `RunEndpointsTest:278` — and no others repo-wide) |
| G-4 | `NonFiringExplanation` | Exactly 8 components (`automationId, automationName, enabled, verdict, lastRelevantRunId, explanation, triggerSummary, lastEvaluation`); `NonFiringVerdict` exactly 4 values; `LastEvaluationView(Instant at, String conditionsResult)` |
| G-5 | `CommandResultEvent` javadoc | The ten-value outcome vocabulary verbatim as embedded below; note "integration adapters may publish additional protocol-specific strings" |
| G-6 | `GetRunCausalChainEndpoint.actionsList` | 6-entry action map: `type, targetRef, command, params, outcome, reason`; `GetNonFiringEndpoint.toWire` 8-entry data map ending `lastEvaluation` |
| G-7 | `RunEndpointsTest` | 8 `@Test` methods, 331 lines; wire-key pins at `:75, :79, :89, :95, :177, :180, :187, :191, :194, :198, :201, :206, :209, :217, :222` (`containsOnlyKeys`); it instantiates ONLY `ListRunsEndpoint` + `GetRunCausalChainEndpoint` — the non-firing endpoint is NOT tested here |
| G-7b | `AutomationEndpointsTest` | Holds the non-firing coverage: `nonFiring_v11ShapeTest` (≈`:56`) instantiates `GetNonFiringEndpoint` (≈`:64–:65`) and pins the 8-key non-firing wire map at `:79–:80` (`containsOnlyKeys("automationId", "automationName", "enabled", "verdict", "lastRelevantRunId", "explanation", "triggerSummary", "lastEvaluation")`); 9 `containsOnlyKeys` pins total (`:76, :79, :89, :94, :187, :191, :199, :204, :210`); constructs `NonFiringExplanation` at `:57, :102, :150` (8-arg sites DP-2's record delta reaches) |
| G-8 | `StandardExplanationServiceTest` / `NonFiringExplanationServiceTest` | 13 / 11 `@Test` methods (403 / 351 lines) |
| G-9 | `HomeSynapseArchRules.java` | Rules reaching `com.homesynapse.automation..`: NO_REVERSE_DEPENDENCIES (`:143/:150`) + NO_DIRECT_FILESYSTEM_IN_CORE (`:191/:197`); NO_DIRECT_TIME_ACCESS `:98`. This WU adds no clock reads, no filesystem access, no new cross-module access — zero collisions expected (the beat-3 grep, re-confirmed at authoring) |
| G-10 | `StandardActionExecutor.java` | Emission truth for DP-2 (READ-ONLY; the executor is untouched): the only `"skipped"` completion publish (≈`:192`) sits in the `catch (InterruptedException …)` **abort** path — it is NOT the §3.9 skip. The real §3.9 per-target skip is `case SKIP -> continue` (≈`:243–:245`) which emits **nothing** per skipped target, and a command action whose targets were ALL skipped falls through to a `"success"` completion (≈`:199`). A silent-skip run therefore carries NO skip events and NO SKIPPED views — the terminal payload's `commandCount == 0` arithmetic is the ONLY log-visible disclosure, which is exactly why DP-2 detects on the payload |

## Settled Decisions (ruled — implement exactly; these are NOT open questions)

- **SD-1 (the four-constraint law, Nick ruling 1 verbatim-class):** every wire change is **additive-only** (new keys inside existing shapes; if any part turns out to require changing/removing an existing v1.1 field, casing, or nesting — STOP, that half returns to Nick as a contract conversation) · new keys use the **live per-endpoint camelCase**, read at the endpoint · **the emitter leads** (this WU is the producer of record for the skip-visibility data; FE-VERDICT-2 consumes observed payloads) · **version discipline** — the contract stamps **v1.1.2**; the amendment note in the read-API doc is **hub-owned at WUCP Phase 2 (do NOT edit `nexsys-hivemind/` from this lane — write-isolation)**.
- **SD-2 (frozen vocabularies do NOT grow):** `RunExplanation.ActionOutcome` stays exactly `{DISPATCHED, CONFIRMED, UNCONFIRMED, FAILED, SKIPPED}`; `NonFiringVerdict` stays exactly its 4 values; `ListRunsEndpoint.wireStatus` mapping untouched. Distinctions ride the additive keys.
- **SD-3 (emitters untouched):** `StandardRunManager`, `StandardActionExecutor`, every event record, and the pending-command ledger are OUT. The DP-G inheritance is ruled design (the emitter is lawful); the skip completion's null `errorDetail` stays as-is (an emitter-side reason string is a separate, unruled candidate — noted, not built).
- **SD-4 (§5.4 adjudicated — by design, no change):** `actionCount` (9) vs `actions[]` (5) disagreement is the designed disclosure: successful non-command actions (delay/wait/branch/emit) are deliberately omitted from the confirmation-centric `actions[]` (the `buildActions` javadoc states it), while `outcome.actionCount`/`commandCount` disclose the totals. FE renders the distinction from existing fields. Do not surface delay actions.
- **SD-5 (runs-list wire byte-shape frozen):** `ListRunsEndpoint` is not modified; `RunEndpointsTest:79`'s 6-key pin on the runs entry (`runId, automationId, automationName, triggeredAt, status, terminalReason`) must still pass UNCHANGED — it is the wire-shape-unchanged proof for DP-3.
- **SD-6 (EXEC-DETERMINISM adjudicated OUT):** the executor's `Map.copyOf` parameter-serialization salt (minted non-gate at the CMD-API audit) is explicitly NOT in this WU — it is a write-path executor concern in a read-side honesty WU (scope discipline). Re-homed by the hub: the first post-gate automation/executor-touching WU (candidate pairing: CMD-API-ACTOR). Do not touch it.
- **SD-7 (unknown outcome strings classify conservatively):** adapters may publish protocol-specific outcome strings beyond the ten. Any outcome not in the non-failure set `{acknowledged, superseded, unconfirmed}` classifies as failure-class — unknown strings keep today's conservative FAILED semantics. **Stated residue (surfaced to Nick with this WU's dispatch, default = as specified here):** of the four DISPOSITIONS the vocabulary names, `expired_on_restart` and `invalid` remain failure-class under this instruction — CORE-P1's operative (b)/(c) name only `superseded`/`unconfirmed`, and both residues read honestly as failures (a restart-expired confirm window is a lost outcome; `invalid` is a rejection). One line from Nick re-classes either later; `resultOutcome` already carries both distinctly on the wire from this WU on.

## Files to Create or Modify (exactly 12 M, 0 new — the P2-audited census)

| Action | File | Description |
|---|---|---|
| MODIFY | `core/automation/src/main/java/com/homesynapse/automation/StandardExplanationService.java` | DP-1 (`deriveOutcome`/`isFailure` + call sites), DP-2 (`completedVerdict`), DP-3 (`toSummary` + `explainNonFiring` `evaluatedAt`) |
| MODIFY | `core/automation/src/main/java/com/homesynapse/automation/RunExplanation.java` | `ActionView` +`resultOutcome` (nullable String; 7th component; + `settled` 8th iff DP-4 GO) |
| MODIFY | `core/automation/src/main/java/com/homesynapse/automation/NonFiringExplanation.java` | +`noCommandsIssued` (nullable Boolean, 9th component) + javadoc |
| MODIFY | `core/automation/src/main/java/com/homesynapse/automation/RunSummary.java` | Javadoc only: the `triggeredAt` parenthetical re-states the corrected derivation (no component change) |
| MODIFY | `core/automation/src/test/java/com/homesynapse/automation/StandardExplanationServiceTest.java` | DP-1 + DP-3 fixture-paired tests (existing 13 methods remain green) |
| MODIFY | `core/automation/src/test/java/com/homesynapse/automation/NonFiringExplanationServiceTest.java` | DP-2 + DP-3b fixture-paired tests (existing 11 remain green) |
| MODIFY | `core/automation/MODULE_CONTEXT.md` | Inventory deltas (record components), the derivation-contract note, new gotcha (see MODULE_CONTEXT Update) |
| MODIFY | `api/rest-api/src/main/java/com/homesynapse/api/rest/GetRunCausalChainEndpoint.java` | `actionsList` +`resultOutcome` key (+`settled` iff DP-4 GO); javadoc v1.1.2 note |
| MODIFY | `api/rest-api/src/main/java/com/homesynapse/api/rest/GetNonFiringEndpoint.java` | `toWire` +`noCommandsIssued` key; javadoc v1.1.2 note |
| MODIFY | `api/rest-api/src/test/java/com/homesynapse/api/rest/RunEndpointsTest.java` | Wire-pin update (`:201` actions keys ONLY; every other pin in this file — incl. `:79` and `:209` — stays untouched and must pass as-is) + the ActionView construction `:278` + new `causalChain_resultOutcomeOnWire` assertions |
| MODIFY | `api/rest-api/src/test/java/com/homesynapse/api/rest/AutomationEndpointsTest.java` | The non-firing wire-pin update (`:79–:80` gains `noCommandsIssued`) + the three 8-arg `NonFiringExplanation` construction sites (`:57, :102, :150` — untouched if you take the convenience-ctor option) + new `nonFiring_noCommandsIssuedOnWire` assertions |
| MODIFY | `api/rest-api/MODULE_CONTEXT.md` | The v1.1.2 additive-key note on the two endpoints |

Zero `module-info.java` changes (validated against these DPs per format-addition #14: every new component type is `String`/`Boolean` = `java.base`; no new cross-module type appears on any exported surface). Zero `build.gradle.kts` changes. Zero event-model changes. Zero `ListRunsEndpoint`/`ListAutomationsEndpoint` changes (`ListAutomationsEndpoint` consumes `AutomationSummary` + `latestRunByAutomation()`, neither touched — verified at authoring).

## Technical Specification

### Embedded vocabulary (verbatim source citation — `CommandResultEvent` javadoc, `4bc1258`)

> the live vocabulary (M9.4b §4.3 currency): `acknowledged` | `rejected` | `timed_out` | `invalid` | `unsupported` | `handler_error` | `integration_unavailable` | `superseded` | `expired_on_restart` | `unconfirmed`. The last four (including `invalid`) are DISPOSITIONS — terminal reports the pending command ledger's `onCommandResult` guard skips, never terminal-matches; integration adapters may publish additional protocol-specific strings.

### DP-1 — `deriveOutcome` carries the raw outcome; superseded never FAILED; honest-unconfirmed derives UNCONFIRMED (CORE-P1, ruled)

**Record delta.** `RunExplanation.ActionView` gains component 7, `String resultOutcome` — nullable; javadoc: "the raw `command_result.outcome` string associated with this action's command (the ten-value vocabulary plus adapter-specific strings), or `null` when no `command_result` exists in the chain. Additive v1.1.2 field (GAP-1)." Update all three construction sites (G-3). The private `Outcome` record (`:661`) grows to carry it (or an equivalent mechanism — Coder's freedom; the contract below is fixed).

**Derivation contract (replaces the current confirmed→failure→timeout→DISPATCHED cascade; precedence is LAW, mechanism is yours):**

Scan the chain exactly as today (payload-match for `state_confirmed`/`command_confirmation_timed_out`; causation-match for `command_result`; last-in-chain-order wins within each class). Let `lastResult` = the last causation-matched `command_result` of ANY outcome class.

1. `state_confirmed` present → **CONFIRMED**, reason `null`.
2. else last failure-class `command_result` present (failure-class = outcome ∉ {`acknowledged`, `superseded`, `unconfirmed`} — SD-7) → **FAILED**, reason `firstNonBlank(failureReason, outcome)` (today's rule).
3. else last `command_result` with outcome `unconfirmed` present → **UNCONFIRMED**, reason `firstNonBlank(failureReason, outcome)` — the recorded zigbee reason verbatim (e.g. "DefaultResponse SUCCESS +90 ms, then no report, ever"), never the generic timeout text.
4. else `command_confirmation_timed_out` present → **UNCONFIRMED**, reason `"confirmation timed out"` (today's rule).
5. else → **DISPATCHED**, reason `null`. (A `superseded`-only or `acknowledged`-only result lands here — supersession is an intent change, not a failure, per the ruled CORE-P1(b); its distinctness rides `resultOutcome`.)

In every branch, **`resultOutcome` = `lastResult.outcome()` if `lastResult` exists, else `null`** — a pure fact-carry, independent of which branch classified.

**Worked example (the §5.1 exhibit):** `set_color_temp 4550` with a `command_result` outcome=`superseded`, failureReason="superseded by a newer command on the same attribute; superseding command event 01KYD…" → today: FAILED. After DP-1: **DISPATCHED** (no confirm, no failure-class result, no timeout) with `resultOutcome="superseded"`; reason stays `null` in branch 5 — the supersession DISTINCTION rides `resultOutcome` (FE keys on it; the recorded prose detail stays in the log, reachable via the event stream, and is deliberately not lifted onto this wire branch). If the same command ALSO has a timeout event: **UNCONFIRMED** via branch 4 with `resultOutcome="superseded"`. Both render distinct from a bare held-DISPATCHED (`resultOutcome=null`).

**The five-modes-distinct law made testable (Nick, 2026-07-25 — "the distinction IS the product"):** after DP-1 the five honest failure modes carry pairwise-distinct wire signatures on `(outcome, resultOutcome, reason)`:

| Mode | outcome | resultOutcome | reason |
|---|---|---|---|
| dispatched-and-timed-out | UNCONFIRMED | null | "confirmation timed out" |
| superseded-same-attribute | DISPATCHED (or UNCONFIRMED if also timed out) | "superseded" | null (or timeout text) |
| acked-then-silent-forever (zigbee honest-unconfirmed) | UNCONFIRMED | "unconfirmed" | the recorded zigbee reason verbatim |
| held-DISPATCHED (in-flight/confirmation-disabled) | DISPATCHED | null (or "acknowledged") | null |
| settled-FAILED (rejected/handler_error/…) | FAILED | the failure-class string | `firstNonBlank(failureReason, outcome)` |

One test (`explainRun_fiveFailureModesDistinct`) seeds all five in one store and asserts the five tuples are pairwise distinct AND each equals its row above. Seed the parenthesized rows to their PRIMARY variant so row-exact equality is determined: mode 2 = superseded result with NO timeout event (⇒ `DISPATCHED / "superseded" / null`); mode 4 = bare dispatch, no result at all (⇒ `DISPATCHED / null / null`). (The "or" variants are covered by their own dedicated tests.)

### DP-2 — `completedVerdict` silent-skip honesty (CORE-P2, ruled)

**Record delta.** `NonFiringExplanation` gains component 9, `Boolean noCommandsIssued` — nullable; `true` exactly when the verdict derives from a terminal COMPLETED run whose payload has `actionCount() > 0 && commandCount() == 0`; `null` in every other construction (never `false` — absent means "not the skip case", the additive-nullable idiom). Javadoc names it the v1.1.2 skip marker (CORE-P2). Preserve the existing 8-arg call sites via a delegating convenience constructor passing `null`, or update all sites — Coder's choice; the compact constructor's null-checks are unchanged (the new component is NOT null-checked).

**Behavioral contract (`completedVerdict`, current `:284–:307`).** Compute the commandless condition **from the terminal payload** (`AutomationCompletedEvent.actionCount()/commandCount()` — the payload is authoritative, and per G-10 it is the ONLY log-visible disclosure of the §3.9 all-skipped case):

- `commandCount == 0 && actionCount > 0` → verdict **ACTED_BUT_UNCONFIRMED** (within the frozen 4 — SD-2), `lastRelevantRunId` = the run, `noCommandsIssued = true`, `lastEvaluation = (evaluatedAt, "true")`, explanation exactly: `"Automation '<name>' fired, but issued no device commands — its device actions were skipped or issued nothing (targets unavailable or no device actions defined)."` The clean-success "last fired and confirmed at …" text MUST be unreachable on this path (that sentence asserting confirmation with zero confirmable commands is the defect).
- Otherwise: today's two branches unchanged (any UNCONFIRMED/FAILED action → ACTED_BUT_UNCONFIRMED as today; else the DP-B2 clean-success NEVER_TRIGGERED-with-runId), both constructing `noCommandsIssued = null`.
- The `deriveNonFiring` switch's other arms (DISABLED / NEVER_TRIGGERED / CONDITION_NOT_MET / FAILED-ABORTED-INTERRUPTED / EVALUATING-RUNNING anomaly) are untouched except for the constructor arity if you choose site updates over the convenience ctor.

Note for understanding (not action): per G-10, the §3.9 skip emits NOTHING — a silent-skip run has no skip events and no SKIPPED views on its chain, so the payload arithmetic is the only detection available; the `"skipped"` completion class `nonDispatchedActionView` renders belongs to the executor's interrupt/abort path, a different animal. This also means CORE-P2's third clause ("empty derived actions") is subsumed: the payload condition catches the all-skipped case AND the designed-no-command case, both of which must stop claiming confirmation. An emitter-side per-target skip event (which would give the chain first-class skip visibility with reasons) is a separate, unruled candidate — noted for the hub, not built here (SD-3).

### DP-3 — the RUNS-TRIGGEREDAT fix, both derivation sites (ruled + the authoring-found sibling)

**Site A — `toSummary` (`:453`; the arithmetic `:466`).** Replace the unconditional subtraction with the branch-split:

```java
Instant terminalTime = completed.eventTime() != null
        ? completed.eventTime() : completed.ingestTime();          // (unchanged helper logic)
Instant triggeredAt = completed.eventTime() != null
        ? completed.eventTime()                                     // DP-G: the inherited eventTime IS the trigger instant
        : completed.ingestTime().minusMillis(Math.max(0L, payload.durationMs())); // fallback: best-effort from ingest wall-time
```

(Shape yours; the contract: **eventTime-present ⇒ `triggeredAt = eventTime`, no arithmetic; eventTime-null ⇒ `ingestTime − durationMs`**, clamped non-negative as today.) The wire (`ListRunsEndpoint.toWire`) is untouched — the VALUE corrects, the SHAPE doesn't (no v1.1.x bump for this DP; SD-5's pin proves it).

**Site B — `explainNonFiring`'s `evaluatedAt` (`:228–:229`) — the same defect, found at the mandated authoring re-enumeration.** `evaluatedAt = terminalInstant(latest).minusMillis(durationMs)` subtracts the duration from a DP-G trigger-instant `eventTime` whenever eventTime is present — understating `lastEvaluation.at` and the "last fired and confirmed at …" text by the run's duration, identically. Same contract: **eventTime-present ⇒ `evaluatedAt = eventTime`; eventTime-null ⇒ `ingestTime − durationMs`.** (Both sites may share a small private helper — e.g. `derivedTriggerInstant(EventEnvelope, long durationMs)` — Coder's freedom.)

**Doc delta.** `RunSummary`'s `triggeredAt` javadoc parenthetical becomes: "(the terminal event's inherited `eventTime` — under DP-G it is the trigger instant; when `eventTime` is absent, best-effort `ingestTime` minus the recorded duration)".

**Alignment regression:** `buildTrigger`'s `matchedAt` (G-2) already reads the triggered envelope's `eventTime` with no arithmetic; both envelopes inherit the SAME DP-G instant, so post-fix **`runs[].triggeredAt ≡ causal-chain trigger.matchedAt`** whenever eventTime is present. Pin it (test below).

### DP-4 ⛔ GATED on Nick's Q1b ruling (carried in the dispatch turn; skip this section entirely if the dispatch says OUT)

**Q1b (Rosonway §5.9):** an action outcome can settle AFTER the run reads COMPLETED (a late `command_result` appends to the still-growing correlation; the log never mutates — the DERIVATION re-reads a longer chain). The ruled candidate: additive per-action **`settled`** boolean — a pure derivation, no emission change: `settled = !(outcome == DISPATCHED && (resultOutcome == null || "acknowledged".equals(resultOutcome)))` — i.e. an action is provisional exactly while it is DISPATCHED with no settling record (a superseded DISPATCHED is settled: the ledger dropped it, nothing further will arrive). If GO: `ActionView` gains component 8 `boolean settled` (non-null), `actionsList` gains the `settled` key after `resultOutcome`, RunEndpointsTest pins extend, and two tests pin a provisional (bare-DISPATCHED ⇒ `settled=false`) and a settled (each other mode ⇒ `true`) case. If OUT: no `settled` anywhere; the derivation rule above still governs FE's client-side inference later — do not half-implement.

### Wire deltas (the endpoint layer; law (b) casing = camelCase, matching every sibling key)

- `GetRunCausalChainEndpoint.actionsList`: after `map.put("reason", …)` append `map.put("resultOutcome", a.resultOutcome());` (+ `map.put("settled", a.settled());` iff DP-4 GO). Map size hint 6→7 (8). Class javadoc gains one v1.1.2 amendment sentence.
- `GetNonFiringEndpoint.toWire`: after `lastEvaluation` append `data.put("noCommandsIssued", e.noCommandsIssued());` (nullable Boolean serializes as `true`/`null`). Size hint 8→9. Javadoc sentence likewise.
- `ListRunsEndpoint`: **zero edits.**

### Error handling

No new exception paths. `parseStatus`-unrecognized handling, null-safety idioms, and Register-C voice on all strings are unchanged. New explanation strings follow Register C (direct, neutral, no self-reference).

## Locked Decisions That Apply

- **INV-SA-03 / SP2 (Doc 16):** the explanation service stays a pure log projection — writes nothing, mints no event, consults no mutable registry for outcome derivation. Every change here is derivation/record/serialization only; DP-4's `settled` is derived, never stored.
- **DP-A2 (honest confirmation):** CONFIRMED derives ONLY from a `state_confirmed` naming the command. DP-1 must not weaken this — branch 1 is untouched, and the mutation tests re-prove it.
- **DP-G (ruled eventTime inheritance):** the run family carries the triggering event's `eventTime` — the fix's premise; the emitter stays untouched (SD-3).
- **DP-B2 (frozen non-firing vocabulary):** the 4-value verdict + the NEVER_TRIGGERED-with-runId clean-success idiom stay; DP-2 narrows when the clean-success sentence is reachable, never the vocabulary.
- **LTD-08 (JSON at the boundary):** wire keys are hand-built LinkedHashMap entries at the endpoints; the automation module gains no JSON dependency.
- **The v1.1.2 four-constraint law (SD-1)** — governs every wire delta above.

## Invariants That Must Hold

- **Never-false-CONFIRMED (AMD-97-INV-01 lineage):** no change may create a CONFIRMED without a matching `state_confirmed` — verified by mutation M1 below.
- **Never-false-ALIVE / honest-unconfirmed:** branch 3 must carry zigbee's recorded reason, not invent one; branch 5 must never upgrade a superseded/acknowledged result to CONFIRMED.
- **INV-SA-03 purity:** the existing `projection_writesNothing` test stays green over the new paths (extend its reads to cover a DP-1 chain if trivial).

## Test Requirements (tests FIRST; fixture-paired per the standing law — every new assert proves its PASS and its false-verdict boundary)

**`StandardExplanationServiceTest` (13 → 24: +11 below; +1 more iff DP-4 GO — the derivation-side `settled` pair's home):**

| Test | Scenario (seed idiom: existing `seedRun`/`publishDerived`) | Assertion (the pair) |
|---|---|---|
| `outcomeSuperseded_notFailed_carriesResultOutcome` | command + `command_result(outcome="superseded", failureReason="superseded by a newer command…")`, no timeout | outcome **DISPATCHED**, `resultOutcome="superseded"`, reason null — and NOT FAILED (kills the isFailure-restore mutant) |
| `outcomeSupersededThenTimeout_unconfirmed` | superseded result + timeout event | outcome UNCONFIRMED, `resultOutcome="superseded"` |
| `outcomeHonestUnconfirmed_fromResult_reasonVerbatim` | `command_result(outcome="unconfirmed", failureReason="DefaultResponse SUCCESS +90 ms, then no report, ever")` | outcome **UNCONFIRMED**, reason = that string verbatim, `resultOutcome="unconfirmed"` |
| `outcomeRejected_staysFailed` (boundary) | `command_result(outcome="rejected", failureReason="device offline")` | outcome FAILED, reason "device offline", `resultOutcome="rejected"` — the failure set didn't over-shrink |
| `outcomeUnknownAdapterString_staysFailed` (SD-7 pin) | `command_result(outcome="zcl_weird_vendor_code")` | outcome FAILED, `resultOutcome="zcl_weird_vendor_code"` |
| `outcomeAcknowledgedOnly_dispatched` | `command_result(outcome="acknowledged")` only | outcome DISPATCHED, `resultOutcome="acknowledged"` |
| `outcomeConfirmed_resultOutcomeCarried` | ack result + `state_confirmed` | outcome CONFIRMED, `resultOutcome="acknowledged"` (fact-carry independent of branch) |
| `explainRun_fiveFailureModesDistinct` | the five-mode store (table above) | the five `(outcome, resultOutcome, reason)` tuples pairwise distinct and row-exact |
| `listRuns_triggeredAtEqualsEventTime` (DP-3 PASS) | completed envelope with `eventTime=FIXED_INSTANT`, `durationMs=34204` | `triggeredAt == FIXED_INSTANT` **exactly** (the old code yields `FIXED_INSTANT − 34.204s` — the mutant-killer pair by construction) |
| `listRuns_triggeredAt_ingestFallback` (DP-3 boundary) | completed envelope with `eventTime=null` (publish a null-eventTime draft), `durationMs=34204` | `triggeredAt == ingestTime − 34.204s` exactly |
| `triggeredAt_equalsMatchedAt_regression` | one seeded run, eventTime present, nonzero duration | `listRuns` `triggeredAt` == `explainRun` `trigger.matchedAt` — the alignment law |

**`NonFiringExplanationServiceTest` (11 → 16: +5 below):**

| Test | Scenario | Assertion |
|---|---|---|
| `completedCommandless_actedButUnconfirmed_marker` | COMPLETED run, payload `actionCount=3, commandCount=0` (+ optionally `action_completed "skipped"` events) | verdict ACTED_BUT_UNCONFIRMED · `noCommandsIssued == TRUE` · explanation contains "issued no device commands" · explanation does NOT contain "fired and confirmed" (the false-verdict boundary: the old clean-success text) · `lastRelevantRunId` = the run |
| `completedWithConfirmedCommands_cleanPathUnchanged` (boundary) | COMPLETED, `actionCount=1, commandCount=1`, confirmed chain | verdict NEVER_TRIGGERED + non-null runId (DP-B2 idiom) · `noCommandsIssued == null` |
| `completedWithUnconfirmed_unchanged` | existing ACTED_BUT_UNCONFIRMED path | behavior as today, `noCommandsIssued == null` |
| `evaluatedAt_equalsEventTime` (DP-3b PASS) + `evaluatedAt_ingestFallback` (boundary) | run-derived verdict, eventTime present (then null), nonzero duration | `lastEvaluation.at == eventTime` exactly; fallback == `ingestTime − duration` |

**`RunEndpointsTest` (8 → 9: +`causalChain_resultOutcomeOnWire`, populated + null cases; +1 more iff DP-4 GO — the wire-side `settled` assert's home):** update the `:201` actions pin to include `resultOutcome` (+`settled` iff DP-4) and the `:278` construction; **every other pin re-runs as-is — `:79` (runs entry 6 keys) and `:209` (outcome block) MUST pass unmodified (SD-5).** (The existing `:84` exact `triggeredAt` entry-assert cannot flip — it feeds a hand-built `RunSummary` through a fake service and pins serialization only.)

**`AutomationEndpointsTest` (+1: `nonFiring_noCommandsIssuedOnWire`, true + absent-null cases):** update the `:79–:80` non-firing pin to include `noCommandsIssued`; the three 8-arg `NonFiringExplanation` constructions (`:57, :102, :150`) compile-follow the record delta (or stay untouched under the convenience-ctor option); every other pin in the file re-runs as-is.

**Mutation verification (in-session, cmp-proven restores):** M1 — restore `isFailure`'s old any-non-acknowledged body ⇒ named tests fail (superseded + honest-unconfirmed). M2 — restore the unconditional subtraction at BOTH DP-3 sites (`:466`-region AND the `:228–:229`-region) ⇒ `listRuns_triggeredAtEqualsEventTime` + `triggeredAt_equalsMatchedAt_regression` + `evaluatedAt_equalsEventTime` all fail. M3 — make `completedVerdict` ignore commandCount ⇒ the commandless test fails. Each mutant: apply, run the naming tests, verify the named failures, `cmp`-restore byte-identical.

## Code Quality Standards

Javadoc on every changed public record/method states the v1.1.2 provenance in one sentence. Comments explain why (the DP-G premise at both DP-3 sites). Register C voice on all wire strings. No new logging.

## Dependencies and Integration Points

- Consumes (unchanged): `EventStore.readByType/readByCorrelation`, `AutomationRegistry.get`.
- Produces: the enriched projection records consumed by rest-api's package-private handlers (plain `requires` — no JPMS impact) and, downstream, the dashboard + the B1/B2 bench engine (which binds runs-list `triggeredAt` — DP-3 removes its dead zone; the engine's own matchedAt rebind is B2 rider #1, separate WU).
- Cross-module: event-model record READS only. The frozen wire contract doc (hivemind) is hub-updated at WUCP P2 (SD-1).

## What to Watch Out For

- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code — use the existing `FIXED_CLOCK`/`MutableClock` idiom (`Clock.fixed(...)`) injected via the store/fixtures. (Convention per §4c; the ArchUnit rule scans production code in every module — the fix shape adds zero clock reads.)
- **Record component / static-factory collision STOP-check:** for every record gaining a component (`ActionView.resultOutcome`, `NonFiringExplanation.noCommandsIssued`, gated `settled`) confirm no method/factory/nested helper already owns that name on the record.
- **`Boolean` vs `boolean`:** `noCommandsIssued` is the nullable BOX (absent ≠ false); DP-4's `settled` (if GO) is primitive `boolean` (always derivable). Don't swap them.
- **The null-eventTime fixture leg:** the existing `publishRoot`/`publishDerived` helpers hard-pass `FIXED_INSTANT` as `eventTime` — add a variant that passes `null` (the `EventDraft` accepts it; the CMD-API POST publishes null-eventTime roots in production). Do NOT fake it by subtracting first.
- **`InMemoryEventStore` ingestTime:** verify at source how the store stamps `ingestTime` (the fallback-leg pins depend on it) — read the store before pinning the fallback expectation; state what you found in the completion report.
- **Chain-order dependence in DP-1:** "last in chain order" is `readByCorrelation`'s return order — the existing scan idiom; don't re-sort.
- **Existing tests that must NOT change behavior:** `explainRun_outcomeFailed` (rejected → FAILED stands via branch 2), `explainRun_disabledModeStaysDispatched` (bare DISPATCHED stands), the listRuns ordering/pagination set, and every SD-5 wire pin.
- **The convenience-constructor trap:** if you add the 8-arg `NonFiringExplanation` delegating ctor, keep the canonical 9-component one the ONLY place validation lives.

## Coder Pushback Welcome

If any specification here is impractical, contradicts a MODULE_CONTEXT gotcha, fights the source, or can be achieved more cleanly under the same contracts — raise it with evidence (file:line) per your skill's escalation format. One flag this instruction already anticipates you might raise: if `readByCorrelation` order is NOT stable log order, STOP and report (DP-1's last-wins premise). (The non-firing test home was located at authoring: `AutomationEndpointsTest` — G-7b; if you find yet another consumer the census missed, report it as `[INFO]` with the file:line and extend there.)

## Out of Scope

- Any emitter change (`StandardRunManager`, `StandardActionExecutor`, event records, ledger) — SD-3.
- EXEC-DETERMINISM (SD-6) and CMD-API-ACTOR — re-homed post-gate.
- The bench engine rebind (B2 rider #1), any `ListRunsEndpoint`/wire-status change, any verdict/outcome ENUM growth, delay-action surfacing (SD-4), availability semantics (§5.2's divergence — FE/design concern), the `awaitCheckpoint` deflake, the read-API doc amendment note (hub-owned).

## Build Discipline (host-CC lane)

Allow-listed for this WU: `./gradlew :core:automation:compileJava :core:automation:test :api:rest-api:compileJava :api:rest-api:test` (targeted, run early and often — both modules are `-Werror`-sensitive) and ONE full `./gradlew check` before handoff. Tests are written and run RED first (stage-A), implementation turns them GREEN (stage-B), then mutations M1–M3 with cmp-proven restores. If the sandbox cannot run Gradle, flag the deferred gate explicitly in coder-handoff per protocol.

## MODULE_CONTEXT.md Update

- `core/automation/MODULE_CONTEXT.md`: ActionView 6→7 (8) components; NonFiringExplanation 8→9; the derivation-contract paragraph (the 5-branch precedence + the fact-carry rule + both DP-3 sites' branch law); one new gotcha: "**`triggeredAt`/`evaluatedAt` derivation is branch-split on eventTime presence** — under DP-G the terminal envelope's `eventTime` IS the trigger instant; only the ingestTime fallback subtracts `durationMs`. Do not 'simplify' the two branches back into one subtraction."
- `api/rest-api/MODULE_CONTEXT.md`: the two endpoints' additive v1.1.2 keys noted with the ruling pointer.

## Work Unit Completion (WUCP Phase 1)

After the gate (or its explicit deferral): update both MODULE_CONTEXTs, update `nexsys-hivemind/context/handoff/coder-handoff.md` (Deferred Build Gate flag if applicable; next-WU pointer = B2 per the hub's sequencing), append `nexsys-hivemind/context/lessons/coder-lessons.md` if any, post the audit-request note to `nexsys-hivemind/context/handoff/cross-agent-notes.md`, and append the WUCP Phase 1 checklist to the completion report. Those three handoff files are this lane's ONLY sanctioned `nexsys-hivemind` writes (the contract-freeze decisions doc is NOT among them — SD-1). **No commit until the hub's two-layer audit ACCEPTs — report the exact core porcelain census (expected: exactly the 12 M above) in the completion report.**

## Success Criterion

DONE when: (1) all 12 files modified as specified, zero others; (2) stage-A red count stated per-test, stage-B `:core:automation:test` + `:api:rest-api:test` GREEN forced-fresh, the existing 13+11+8 (+AutomationEndpointsTest's existing set) methods green unmodified except the enumerated pin/construction updates; (3) mutations M1–M3 killed by the named tests with cmp-proven restores (M2 kills at BOTH DP-3 sites); (4) the five-modes tuple test passes; (5) `triggeredAt ≡ matchedAt` regression passes; (6) SD-5's untouched pins pass; (7) one full `./gradlew check` GREEN (or the gate explicitly deferred); (8) WUCP Phase 1 checklist complete; (9) completion report states the DP-4 gate state it executed (GO/OUT) and the `InMemoryEventStore` ingestTime finding.
