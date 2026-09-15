<!--
file: context/audits/2026-09-15_MEASURE-1_return.md
purpose: Coder return for MEASURE-1 (DUR-0 + HASH-0 probes; no production change). The tests land with DUR-1 / HASH-1, never alone.
status: DELIVERED — MEASURED; T1 RED at HEAD by design, not landable alone
-->

# MEASURE-1 return — DUR-0 red as predicted, HASH-0 salted on both sources (filed 2026-09-15 CT)

## §0 The card
- **Verdict: DELIVERED, both measured.** Baseline `3d40b5f`, porcelain empty at boot. `date -u` 2026-09-15T21:48:47Z ⇒ CT = UTC−5 = 16:48, once. Instrument: a 24-core Windows 11 desk, JDK 21.0.4, `--offline`; not the runner. Preflight PASS (Checks 6 and 12 included).
- **Census (lock-free porcelain): 2 = 1 M + 1 A** — M `DurationTimerTest.java` · A `DefinitionHashOrderProbeTest.java`; `git diff --stat -- '*/src/main/*'` EMPTY; nothing staged or committed. **P1 HELD.**
- **DUR-0 — RED at HEAD (P2 HELD).** T1 21:58:56Z: `[DUR-0: initiateRun calls after for_duration expiry; triggeringEvent types=[]] Expected size: 1 but was: 0 in: []` — ZERO calls after started 1 · expired 1 · timers 1 → 0 · the expired envelope redelivered to `onEvent` in LIVE; the other six green. IR-22 stands.
- **HASH-0 — SALTED on BOTH sources (P3 HELD).** 8 fresh worker JVMs (pids 367224 369912 370068 370780 371244 371300 371436 371644; 21:59:22→41Z; the 32 lines at `_scratch/v75/2026-09-15_HASH-0_eight-jvms.txt`). **A** (two-role `AreaSelector`): 2 distinct hashes — `67464952…47eb` ×5 with `includedRoles=[DIAGNOSTIC, PRIMARY]`, `202ada4d…98a1` ×3 with `[PRIMARY, DIAGNOSTIC]`. **B** (two-parameter `CommandAction`): 2 distinct — `ba46bcf1…eec9` ×5 with `parameters={brightness=50, transition=2}`, `303c1b94…c22f` ×3 with `{transition=2, brightness=50}`. Passes 4 and 6 flipped one source only: the salts are independent.
- **P4:** no cite moved (HEAD == the pinned sha); one mis-filed: `consumedEventType :174–:188` is in `StandardAutomationRegistry.java`, not the evaluator; its claim holds.
- **§7 run** `./gradlew :core:automation:test --offline` 22:00:33Z: **245 completed, 1 failed = T1 reported as the one red** (243 + T1 + T2; 29 XMLs fresh). `spotlessCheck` executed, green.

## §1 What changed per file
- **M `DurationTimerTest.java`** (7 `@Test`): T1 `forDurationExpiry_initiatesARun` — the W2 fixture in LIVE with a `RecordingRunManager` behind `RunInitiator`; light-on via `onEvent`; preservation lines (timer 1, started 1, no run yet, expired 1, timer 0); `advance(30 min + 1 s)` → `pollExpirations()`; the expired envelope redelivered via `onEvent`; THE MEASUREMENT `assertThat(calls).as("… types=%s", …).hasSize(1)`.
- **A `DefinitionHashOrderProbeTest.java`**: `printsHashAndRendering` — A: `StateCondition` over `AreaSelector("kitchen", LinkedHashSet[DIAGNOSTIC, PRIMARY])` + a `Map.of()` `CommandAction`; B: a single-role selector + `CommandAction("set_level", LinkedHashMap{transition=2, brightness=50})`; four `HASH0` stdout lines; asserts `[0-9a-f]{64}` ×2; every identity `Ulid.parse(…)`.

## §2 Commands and tails
1. `./gradlew :core:automation:test --tests '*DurationTimerTest*' --offline` (`compileTestJava` executed, `-Werror` clean): `7 tests completed, 1 failed`.
2. The §0 loop verbatim `| tee …` (a script run by path): 32 lines, 8 distinct pids; `cleanTest` forks a fresh worker, `--no-daemon` not needed.
3. `./gradlew :core:automation:test --offline`: `245 tests completed, 1 failed` (T1) · `:core:automation:spotlessCheck --offline`: `BUILD SUCCESSFUL`.

## §3 Pushback and observations
- **Zero [REVIEW].** [INFO] I1 one extra preservation line, `calls().isEmpty()` before expiry. I2 `System.out.println` in T2 is the instruction's order (LTD-15 binds production); whether it lands is the hub's call. I3 `spotlessCheck` beyond the two gate lines. I4 fixed parsed ULIDs: `UlidFactory` draws `SecureRandom`, so `automationId()` alone would salt the hash per launch.
- **O1 (HASH-1):** `Set12`'s REVERSE bit and `MapN`'s probe order flip independently in one JVM: the canonical rendering must cover all eight `Set.copyOf`/`Map.copyOf` records (D-v75-5); a stability test on one proves nothing about the other.
- **O2 (DUR-1):** nothing in `expire()` reaches an initiator and the redelivered expired event matches no trigger (`consumedEventType` has no expired arm); T1 covers both paths.
- **O3:** `coder/CLAUDE.md` names `context/open-questions.md` (absent, retired). **PATTERN (testing):** I4; not appended to coder-lessons (§11).

## §4 WUCP Phase 1: Coder Closeout
- [ ] MODULE_CONTEXT.md updated for: none — §8
- [ ] coder-handoff.md updated — no: the hub files the entry (§0 write-set; 114b/114c precedent)
- [x] Deferred build gate flag: YES — `./gradlew check` NOT run; owed to CI on the DUR-1 + HASH-1 landing
- [x] coder-lessons.md appended: No — §11; the pattern rides §3
- [x] Cross-agent note posted: Not needed (channel retired)
- Timestamp: 2026-09-15 22:06 UTC
- Next WU: DUR-1 + HASH-1 (one session, hub-authored), then ENERGY-READ.

RETURNED nexsys-hivemind/context/audits/2026-09-15_MEASURE-1_return.md 5107
