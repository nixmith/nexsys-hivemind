<!--
file: context/audits/2026-09-15_DUR-1_HASH-1_return.md
purpose: Coder return for DUR-1 + HASH-1 (the run on expiry; the ordered views). §0 first; Nick commits the 14.
status: DELIVERED — REPO-COMPLETE, hub audit pending
-->

# DUR-1 + HASH-1 return — the run initiates on expiry; one hash per definition (filed 2026-09-15 CT)

## §0 The card
- **Verdict: DELIVERED.** Baseline `3d40b5f` + MEASURE-1's two files exactly. `date -u` 2026-09-15T23:36:10Z ⇒ CT 18:36, once. Instrument: a 24-core Windows 11 desk, JDK 21.0.4, `--offline`; not the runner. Preflight PASS (Checks 6 and 12 included).
- **Census (lock-free porcelain): 14 = 12 M + 2 A** — M `MODULE_CONTEXT.md` · M the 10 `src/main` rows (the eight records, the registry, the evaluator) · M `DurationTimerTest` · A `DefinitionHashOrderProbeTest` · A `DefinitionHashStabilityTest`; the `src/main` diff = those 10; `DefinitionHashes` untouched; nothing staged or committed. **P1 HELD.**
- **§12-1** the gate line verbatim, 23:54:34→42Z, ONE round: automation **250** (243 + 7) · rest-api **157**/3 skipped · lifecycle compiled · every `spotlessCheck` green; XMLs fresh 23:54:38/:41Z; `-Werror` clean.
- **§12-2 DUR-1 (P2 HELD):** T1 GREEN; T1b's one `InitiateCall`: `eventType` = `trigger_duration_expired`, `eventId` = the redelivered envelope's, `matchedTriggers` = `[0]`, correlation = the started event's = the state event's, causation = the state event id; T1c GREEN (REPLAY: the match exists, zero calls). Finding: a second redelivery records a SECOND call — the initiator never dedups; `StandardRunManager`'s C2 key `(automationId, triggeringEventId)` `:222–:225` does — pinned, not fixed. Rows 1 + 2 landed in one splice; row 2 is off T1's path.
- **§12-3 HASH-1 (P3, P4 HELD):** the loop 23:54:18→34Z, **64 lines, 8 distinct pids** (`_scratch/v75/2026-09-15_HASH-1_eight-jvms.txt`): A = A-twin = `202ada4d…98a1` ×16 (`[PRIMARY, DIAGNOSTIC]`); B = B-twin = `ba46bcf1…eec9` ×16 (`{brightness=50, transition=2}`) — HASH-0's ordered values, one per definition. T4: C `6fa283b7…f8d4`, D `c419d1c4…9f2e` recorded at the untouched baseline, equal after.
- **Red-first:** baseline 23:46:39Z: T1 · T1b · T1c RED (`Expected size: 1 but was: 0`; T1c on its non-vacuity line); T3-B RED in all three baseline launches; T3-A RED at 23:46Z, GREEN at 23:48Z/23:49Z — salt-dependent; T4 GREEN at the baseline (preservation). All GREEN after, 23:53:35Z.
- **P5:** no cite moved; `pollExpirations() :256` → its javadoc (signature `:258`). `rebuildTimer :295–:296` publishes the same expired event — the redelivered path serves it, no change. `AggregateValue.java:59` is unreachable from `AutomationDefinition.toString()`.
- **Deviations:** **[REVIEW] R1** (the `EventTrigger` carve-out); [INFO] I1–I8; one lesson appended.

## §1 What changed per file
- **`StandardAutomationRegistry`** (1a): `Snapshot.build` also indexes a trigger carrying a `forDuration` under `TRIGGER_DURATION_EXPIRED` (`dedup` collapses the double entry).
- **`StandardTriggerEvaluator`** (1b): the expired-payload arm in `evaluateMatches`' loop (the rule in §3 R1) → an IMMEDIATE match, then `continue` (never `maybeStartDurationTimer`); `forDurationOf` package-private static.
- **The eight records** (2): selectors → `unmodifiableSet(EnumSet…)` (`isEmpty()` branch); the three maps → `unmodifiableMap(new TreeMap<>(Map.copyOf(…)))`; `WebhookTrigger` → `unmodifiableSet(new TreeSet<>(Set.copyOf(…)))`.
- **`MODULE_CONTEXT.md`**: the M7.4b sentence amended (DUR-1); two status paragraphs after 114c's.
- **`DurationTimerTest`** (7 → 9): T1 untouched; + T1b `forDurationExpiry_runCarriesTheExpiredEnvelope`, T1c `forDurationExpiry_inReplay_initiatesNothing`.
- **`DefinitionHashOrderProbeTest`** (kept — row 13's first option): builders package-private and reused; `HASH0` ×4 unchanged + `HASH1` twin ×4.
- **`DefinitionHashStabilityTest`** (A): T3 ×2 (insertion-order equality, golden literals, ordered rendering); T4 soft-asserts C and D against the baseline literals.

## §2 Commands and tails
1. Baseline, production untouched: `./gradlew :core:automation:test --tests '*DurationTimerTest*' --tests '*DefinitionHashStabilityTest*' --tests '*DefinitionHashOrderProbeTest*' --offline` 23:46:39Z `13 tests completed, 6 failed`; re-runs 23:48:36Z / 23:49:09Z.
2. After the splice `./gradlew :core:automation:test --offline` 23:53:30Z: 250/0.
3. The §0 loop verbatim `| tee ../_scratch/v75/2026-09-15_HASH-1_eight-jvms.txt`: 64 lines, 8 pids.
4. `./gradlew :core:automation:test :api:rest-api:test :lifecycle:lifecycle:compileJava spotlessCheck --offline`: `BUILD SUCCESSFUL in 7s`.

## §3 Pushback and observations
- **[REVIEW] R1 — the `EventTrigger` carve-out.** Specified: on an expired payload only the armed trigger matches (iff `forDuration` non-null, `automationId` and `triggerIndex` equal). Implemented: that rule for every permit EXCEPT `EventTrigger`, which keeps HEAD's type-equality arm (`triggerMatchesEvent :491`). Reason: an `EventTrigger` on `trigger_duration_expired` is loadable today (`requireKnownEventType` admits every `EventTypes` constant) and fires at HEAD; the literal rule would silently stop it. The `continue` still shields the rest — else a `ManualTrigger` (`:492`, keyed on the automation subject) would fire once 1a buckets its definition. Contract impact: yes; the revert is one line.
- [INFO] I1 `forDurationOf` hoisted, not duplicated. I2 T4 pins TWO definitions (C as specified; D the other five records + the empty set and map), soft-asserted. I3 T3 also pins HASH-0's golden literals. I4 T1c asserts the REPLAY match exists, so it is RED → GREEN, not pure preservation. I5 the probe: `HASH0` + `HASH1` twin lines; `System.out` under the `-i` grep contract. I6 T1b pins the second-redelivery count at 2. I7 the cap arithmetic (17 KB vs 7 KB). I8 one lesson: hash fixtures mint identities by `Ulid.parse` — `UlidFactory` draws `SecureRandom`.
- **O1 (JDK 21 `src.zip`):** `Set.copyOf` routes a mutable collection through `new HashSet<>(coll)` — enum identity hashes, per JVM — into `Set12` (+ `REVERSE`), so the two-role twins render alike within a launch and flip across launches; `Map.copyOf` → `MapN`, per-launch salted.
- **O2 (§6):** one index caller (`:174`), one `consumedEventType` site (`:131`); no test pins the bucket, `triggerIndex()` or a rendering; wire: `ConditionDefinitionRenderer :97–:101` sorts role names, rest-api main touches none of the eight components.

## §4 WUCP Phase 1: Coder Closeout
- [x] MODULE_CONTEXT.md updated for: core/automation
- [ ] coder-handoff.md updated — no: the hub files the entry (§13)
- [x] Deferred build gate flag: YES — `./gradlew check` NOT run; owed to CI on Nick's push of the 14 atop `3d40b5f`
- [x] coder-lessons.md appended: one entry (I8)
- [x] Cross-agent note posted: Not needed (channel retired)
- Timestamp: 2026-09-16 00:06 UTC
- Next WU: ENERGY-READ (hub-authored).

RETURNED nexsys-hivemind/context/audits/2026-09-15_DUR-1_HASH-1_return.md 7074
