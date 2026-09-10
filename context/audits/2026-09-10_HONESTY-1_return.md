<!--
file: context/audits/2026-09-10_HONESTY-1_return.md
purpose: Coder return for HONESTY-1 — the four value corrections (A lastReported null · B provenance inherited / UNKNOWN · C javadoc · D CI paths). §0 card first.
audience: the hub (audit) · Nick (commits)
state-type: lane return
status: DELIVERED 2026-09-10 CT — REPO-COMPLETE, LIVE-VERIFICATION PENDING (CI on the push = the gate; install-smoke's run on it = P4)
-->

# HONESTY-1 return — four value corrections (2026-09-10 CT)

## §0 The card

**Verdict: DONE (repo-complete); 1 [REVIEW] + 5 [INFO]; nothing STOP-grade.** Instruction: `context/instructions/2026-09-07_coder-lane_HONESTY-1_lastreported-origin-commandeventid-cipaths_coding-instruction.md`. Baseline: core `main` HEAD `39c8dd3`, porcelain empty at launch. Gates G1/G2/G3/G5 byte-exact at source; G4 passes on its intent (I3). Preflight Checks 3–7 PASS (the loaded skill == `nexsys-hivemind/coder`, `diff -rq` empty); Check 12 STALE-by-hygiene (O4). Instrument: `date -u` 22:52Z launch · 22:56Z baseline · 23:03Z red · 23:06Z green · 23:16Z filing; CT = UTC−5 → **2026-09-10**. Not a re-paste. Docs precedence met: the AMD-53 §1.5 correction is COMMITTED on the docs tree (`876a395`).

**Census — CORE (`git --no-optional-locks status --porcelain`): EXACTLY 13 = 13 M + 0 A + 0 D; ZERO staged; ZERO commits by the lane.** M `core/state-store/…/StateProjection.java` · `…/ReconciliationTest.java` · `core/state-store/MODULE_CONTEXT.md` · `core/persistence/…/CheckpointSerializerTest.java` · `core/automation/…/StandardCommandDispatchService.java` · `…/AutomationTestSupport.java` · `…/CommandDispatchSubscriberTest.java` · `…/StandardCommandDispatchServiceTest.java` · `core/automation/MODULE_CONTEXT.md` · `integration/integration-api/…/CommandEnvelope.java` · `integration/integration-api/MODULE_CONTEXT.md` · `.github/workflows/install-smoke.yml` · `distribution/ci/install-smoke.yml`. ZERO `module-info`/build/schema/event-key/interface change. HIVEMIND: 1 A (this file) + 1 M (`coder-handoff.md`).

**Red-first (predicted → observed; every run `--rerun --offline`):**
| Test | Predicted | HEAD production (23:03Z) | After A–D (23:06Z) |
|---|---|---|---|
| A-#4b `ReconciliationTest` | RED | RED `expected: null but was: 2025-09-15T08:30:00Z` | GREEN |
| A-ser `CheckpointSerializerTest` | green-by-construction | GREEN (disclosed) | GREEN |
| T-B1 dispatched inherits `USER_COMMAND` + actor | RED | RED `expected: USER_COMMAND but was: AUTOMATION` | GREEN |
| T-B2 result (unroutable) inherits | RED | RED `expected: USER_COMMAND but was: AUTOMATION` | GREEN |
| T-B3 primitive → `UNKNOWN` / null | RED | RED `expected: UNKNOWN but was: AUTOMATION` | GREEN |
| T-B4 AUTOMATION regression | green-by-construction | GREEN (disclosed) | GREEN |

Suites: state-store 164 → 165 (1 skipped at both: the pre-existing `@Disabled` AMD-51 §5.9 stub) · automation 207 → 211 · persistence 412 → 413; zero pre-existing tests red at either stage.

**Deviations by tag.**
- **[REVIEW] R1 — `EntityState.java:73` `@param lastReported … never {@code null}` is now false.** The read set names the line; the Files table does not list the file (the table governs) — NOT edited. One-line fix for the hub: `never {@code null}` → `{@code null} until the entity's first {@code state_reported} (AMD-53 §1.5 as corrected 2026-09-07)`; census +1 if applied at commit.
- **[INFO] I1** — census 13 M, not the predicted 12: the Files table's install-smoke row is two files.
- **[INFO] I2** — `EventEnvelopeAssert.hasOrigin` is not on `core/automation`'s test classpath (no `test-support` test dependency); plain AssertJ on `origin()`/`actorRef()`; no build-file edit.
- **[INFO] I3** — G4's literal grep also returns `SqliteEventStore:467/:532` (`draft.origin()` column writes — a pass-through, not a filter); the gate passes on its intent.
- **[INFO] I4** — the MC entries carry both dates, "ruled 2026-09-07 / landed 2026-09-10" (a 09-07 date on text written 09-10 would be false).
- **[INFO] I5** — `:integration:integration-api:compileJava` added to the desk gate (a touched module).

**P1–P4.** P1 (`12 M + 0 A`) **REFUTED by one** — 13 M + 0 A (I1). P2 (four RED for a value) **HOLDS** — each red an `AssertionFailedError` on the value, zero compile errors. P3 (zero existing tests red) **HOLDS** at both stages. P4 (install-smoke runs on Nick's push, both jobs green) **PENDING** — CI adjudicates; the desk proves only that both files parse, `on.push` is the two branches alone, and the pair is byte-identical.

**Deferred Build Gate: YES** — `./gradlew check` NOT run on this desk; owed to CI on Nick's push of exactly the 13 atop `39c8dd3` (the gate of record; law 16). **Completion register: REPO-COMPLETE, LIVE-VERIFICATION PENDING** (P4 + the passive `ci` sample).

## §1 What changed, per file (`git diff --numstat`)
- **`StateProjection.java`** (30/18): `initialEntityState` → `(…, 0L, seed, seed, null, null, false)`; its javadoc, the `applyToState` seed comment and the `eventTimestamp` javadoc re-worded. No `applyToState`/backfill branch touched — each already carries `prior.lastReported()`.
- **`ReconciliationTest.java`** (42/0): AMD-53 §5 #4b — LIVE adoption via a logged `state_changed` at T0 → `lastReported == null`, `lastChanged == lastUpdated == T0`, `stateVersion == 1`; a `state_reported` at T1 → `lastReported == T1`, `lastChanged == T0`, `stateVersion == 2`.
- **`CheckpointSerializerTest.java`** (24/0): `nullLastReportedPreserved` — null and non-null `lastReported` round-trip; no serializer change.
- **`StandardCommandDispatchService.java`** (52/14): `onEvent` → `event.origin()`, `event.actorRef()`; `dispatch` → `EventOrigin.UNKNOWN`, `null`; `route`/`publishDispatched`/`publishResult`/`publish` take `(EventOrigin origin, Ulid actorRef)` onto the draft's `origin`/`actorRef` (`idempotencyKey` stays null); javadocs on the class + 4 methods; `+import Ulid` (platform-api, transitive).
- **`AutomationTestSupport.java`** (18/2): the 6-arg `commandIssued(…, origin, actorRef)`; the 4-arg delegates `AUTOMATION, null` — its 4 callers unchanged.
- **`CommandDispatchSubscriberTest.java`** (68/0) T-B1/T-B2/T-B4 · **`StandardCommandDispatchServiceTest.java`** (15/0) T-B3; T-B1 re-asserts the §3.11.2 chain.
- **`CommandEnvelope.java`** (6/4): the `commandEventId` `@param` = the instruction's text.
- **`install-smoke.yml` ×2** (0/1 each): the `push: paths:` line removed; `branches`, `pull_request:`, `workflow_dispatch: {}` byte-unchanged; `diff` of the pair empty.
- **MODULE_CONTEXT ×3** (3/0 · 2/1 · 1/1): state-store (contracts bullet + the AMD-53 row's §1.5 correction) · automation (provenance contract + the `UNKNOWN` gotcha) · integration-api (the `CommandEnvelope` gotcha +1 sentence).

## §2 Gates run + counts (Windows 11 · JDK 21.0.4 · Gradle 8.8 · `--offline`)
`./gradlew :core:state-store:test --rerun :core:automation:test --rerun :core:persistence:test --rerun :core:state-store:compileJava :core:automation:compileJava :integration:integration-api:compileJava spotlessCheck --offline --continue --console plain` → **BUILD SUCCESSFUL (12 s)**; the 3 `compileJava` + the 4 touched modules' `spotlessCheck` EXECUTED (not `UP-TO-DATE`); class mtimes 23:06:27/28Z; XML newest 23:06:28–37Z. XML `<testcase>` counts: state-store 165 / 0 failed / 1 skipped · automation 211 / 0 · persistence 413 / 0. Baseline at HEAD (22:56Z, same flags): 164 / 207 / 412 green. Red stage (23:03Z): 165 / 211 / 413, exactly the four predicted reds. Wall-clock grep over the five touched test files: 0. YAML: both `yaml.safe_load` OK. CRLF working tree (autocrlf desk); every edit CRLF-consistent.

## §3 Pushback / observations
- **O1 (= R1)** the `EntityState` `@param` — above.
- **O2** No `projectionVersion` bump was ordered: a pre-landing checkpoint keeps the adoption-instant `lastReported` on a never-reported entity until it first reports or the next version-transition rebuild (from-zero replays are honest from the first boot). A 5→6 bump (one `HomeSynapseCore` literal) would heal the running Pi at the landing — a different WU, the hub's call.
- **O3** The ordering "Nick's docs commit precedes the core landing" is already satisfied: docs HEAD `876a395` carries the §1.5 paragraph (AMD-53 file, line 52).
- **O4** Check 12: `2026-08-22_research-lane_RS3-WMARKET-2_…brief.md` and `2026-09-06_H8a_real-wire_…navigator-packet.md` still carry a live `status:` — hub hygiene, not adjudicated here.
- **O5** Threading shape: two parameters, not the optional `Provenance` record — keeps "no new types" literally true (a nested record is a class file); mechanical to flip.
- **O6** `MaterializedStateQueryService:234/:285` pass `lastReported()` into a rebuilt `EntityState` (not a summary record as the survey said); no non-null check either way.

## §4 WUCP Phase 1: Coder Closeout
- [x] MODULE_CONTEXT.md updated for: core/state-store · core/automation · integration/integration-api
- [x] coder-handoff.md updated (the DELIVERED entry prepended, newest-first; Deferred Build Gate + the NEXT WU pointer)
- [x] Deferred build gate flag: YES (`./gradlew check` → CI on Nick's push = the gate of record; install-smoke's run on that push = P4)
- [x] coder-lessons.md appended: No new patterns
- [x] Cross-agent note posted: Not needed (the channel is retired; this return + the handoff entry carry it)
- [x] NEXT WU named: the hub's audit (rules R1) → the msg file + census card → Nick's commit (exactly the 13) + push → `ci` green + `install-smoke` runs green (the arm64 `.deb` = R-4c's) → **the v1.1.4 EXPLAIN batch**
- Timestamp: 2026-09-10 23:16 UTC

RETURNED context/audits/2026-09-10_HONESTY-1_return.md 9816
