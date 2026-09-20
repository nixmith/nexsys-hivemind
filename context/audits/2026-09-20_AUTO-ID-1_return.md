<!--
file: context/audits/2026-09-20_AUTO-ID-1_return.md
purpose: the Coder's return for AUTO-ID-1 (durable automation identity: the automations.ids.yaml companion behind an I/O seam; the restart IT)
status: filed Sun 2026-09-20 CT — `date -u` first: 12:35:06Z (07:35 CT); baseline core `c819a02`, porcelain EMPTY; ZERO commits by the lane
-->

# AUTO-ID-1 — return

## §0 Card
**DELIVERED, uncommitted. Census EXACT, computed from §1's column — 15 = 8 M + 7 A:** core 14 = 8 M + 6 A (porcelain 8 ` M` + 6 `??`, nothing staged, HEAD `c819a02`); hivemind 1 A (this file) beside the hub's beat (4 M + 4 `??` at dispatch). `RealCoreFixture.java` untouched.
**Mid-lane ruling (the hub, 2026-09-20):** row 1/R3 as written cannot pass the gate — `NO_DIRECT_FILESYSTEM_IN_CORE` (`HomeSynapseArchRules.java:191–:204`) bans `Files`/`File` in `com.homesynapse.automation..`. Raised with T1 already red and no store code written; RULED the I/O seam, MAP form — policy in `core/automation`, bytes in `lifecycle`; rows 1–4 re-cut, P1/P5 re-read. Built as ruled.
**Sort:** RED→GREEN: T1 at the baseline, first; then the staged red (seams declared, hooks inert; predictions filed before the results were read — §7) — store 15 of 16, file companion 6 of 7, root T8 + T9, every prediction MET (§2). GREEN-BY-CONSTRUCTION, disclosed: T6b · absent→empty (inert stage); T7 (2 + 3, unchanged); T8 (Hero 5/5 · the smoke). Written AFTER its fix, so mutation-verified: T2c.
**Gate line, verbatim — GREEN in one round:** 13:08:09Z→:40Z `BUILD SUCCESSFUL in 30s`, the three test tasks EXECUTED; XML: automation 267 (31 files) · lifecycle 93 (22) · app 30 (7; ArchRules 11) · 0 failures/errors/skipped, mtimes 13:08:12–:39Z. **Round 2, same line, GREEN** 13:11:04Z→:32Z after a cite correction (one javadoc sentence + one `@DisplayName`, zero logic — R-7): automation + lifecycle re-executed (267 · 93); app's test UP-TO-DATE on byte-identical inputs — round 1 is its verdict. The two `bus-soak` ITs (excluded by tag) ran by their own line 13:10Z: `loops=20 ok=20 timed_out=0 anomalies=0`, census 1/1.
**P1** VOID as ruled; computed 15 — three rows past the re-cut, each [REVIEW] (R-3). **P2 MET** — T1 RED at `c819a02`: `expected: FIRED_CONFIRMED but was: NEVER_TRIGGERED` (+ id `…8M58`→`…8M68`, run id → null, no file; ONE soft failure); GREEN after; the smoke: `rows=2013 q2_verdict=FIRED_CONFIRMED/FIRED_CONFIRMED hero_id_stable=true`. HEAD's `false` is MEASURE-2b's filed reading, not re-measured; T1's red reads the same fact. **P3 MET, one nuance** (R-2): one write per load that minted or retired; a no-change load writes nothing (store: 1 attempt over three brackets; file: a counting delegate reads 0, bytes identical) — but a LATER-instant load re-stamps `last_seen`, a change: one write. **P4 MET on the grep (0); MISSED on "two lines"** by row 6's own bracket: +12 −3. **P5 MET as re-read** — the one `requires` + the one `implementation`, both on lifecycle; automation's two files untouched; no `-Xlint:exports` red; `config` exports no YAML facade (checked). **P6 MET** — a bare `Load` parses the file, header and all; bytes identical across read→replace and across two boots; golden bytes pinned.
**Deviations:** [BLOCKING→RULED] 1 · [REVIEW] 7 · [INFO] 6 (§5).

## §1 Files (the census's source)
| # | File | A/M | What |
|---|---|---|---|
| 1 | `core/automation/src/main/…/AutomationIdentityCompanion.java` | A | the seam: `read()` (empty = absent) · `replace(Map)`; every failure an ISE with location + cause; `toString()` = the location |
| 2 | `…/CompanionAutomationIdentityStore.java` | A | the policy: R2 as a Map · minting · `beginLoad()`/`endLoad()` (two void methods) · 30-day `RETENTION` · fail-closed · write-once-if-changed |
| 3 | `core/automation/src/test/…/CompanionAutomationIdentityStoreTest.java` | A | 17, over a `Map` holder: T2/b/c · T3/b · P3/b · T4/b/c · T5/b/c · T6/b · R3 · the bracket |
| 4 | `…/AutomationIdentityStore.java` | M | javadoc only (R-3) |
| 5 | `…/InMemoryAutomationIdentityStore.java` | M | javadoc only (R-3) |
| 6 | `core/automation/MODULE_CONTEXT.md` | M | the banner · a gotcha · the Phase-3 bullet · the header count re-derived from source (91) |
| 7 | `lifecycle/lifecycle/src/main/…/FileAutomationIdentityCompanion.java` | A | the bytes: snakeyaml `Load`/`Dump`, the header line, temp + `force` + `ATOMIC_MOVE, REPLACE_EXISTING`, best-effort dir fsync |
| 8 | `lifecycle/lifecycle/src/test/…/FileAutomationIdentityCompanionTest.java` | A | 8 (the ruling's four + golden bytes · typed keys → strings · T2 over the FILE · odd slugs) |
| 9 | `lifecycle/lifecycle/src/main/java/module-info.java` | M | + the `requires` |
| 10 | `lifecycle/lifecycle/build.gradle.kts` | M | + the `implementation`, a one-line comment |
| 11 | `…/HomeSynapseCore.java` | M | `:677` the wiring · the bracket · the import |
| 12 | `…/AutomationIdentityRestartIT.java` | A | T1; the YAML = `BusPositionCensusIT.heroMotionConfigYaml()` (shared with `MeasureReadPathIT`/`BusSoakIT`; the hero IT's own is `private`); `restart(() -> 0L)` |
| 13 | `…/HomeSynapseCoreStartupFailureTest.java` | M | T8 · T9 (R-3) |
| 14 | `lifecycle/lifecycle/MODULE_CONTEXT.md` | M | the AUTO-ID-1 section; a pointer on MEASURE-2b's now-historical sentence |
| 15 | this file | A | |

## §2 Red-first (XML + logs banked `_scratch/v77/2026-09-20_AUTO-ID-1_*`)
| Run | Predicted | Observed |
|---|---|---|
| T1 at `c819a02`, 12:41Z | RED: `NEVER_TRIGGERED`, the ids differ | RED — four soft failures in one: id · verdict · run id null · no file |
| store ×16, inert, 12:58Z | 15 RED · T6b GREEN | as predicted |
| file companion ×7, inert | 6 RED · absent GREEN | as predicted (after one test-compile fix: a wildcard capture) |
| root T8 · T9, unwired | RED no throw · RED 0 lines | `Expecting actual not to be null` · `Expected size: 1 but was: 0` |
| all, the real code, 13:02Z | GREEN | GREEN on the first run (16 · 7 · 6 · T1); the R2 golden bytes matched the library with NO re-pin |
| T2c + odd slugs, 13:05Z | — (added after the fix) | GREEN; **M1**: restoring `!name.isBlank()` → T2c RED (`key '' in automations is not a string`), restored `cmp`-identical |

Behind M1, a self-review find: a blank slug was written, then refused on read — the store would have bricked its own next boot. Any string is a slug key now.

## §3 The shape (detail and the four tokens: the two MODULE_CONTEXTs)
- `beginLoad()`: the FIRST call reads the companion (absent = first boot); not-exactly-R2 → ISE naming the companion, nothing minted, nothing written. `endLoad()`: stamp `last_seen` (forward only) on the slugs the load named → retire what is OLDER than 30 days (exactly 30 kept) → `replace` once if the document changed.
- A write failure: ERROR `automation.identity_write_failed: path= cause=`, no throw, the store stays dirty, the next `endLoad()` retries.
- The file: the header verbatim, written by the class before the library's dump (its object `Dump` emits no comment); on read the parser skips it as the comment it is. The trigger-index key is emitted `'0'` — the library's quoting; the same scalar as R2's `"0"`.
- At the root a malformed companion is `(CORE_DOMAIN, automation)`, the ISE unwrapped, bytes untouched (T8); an unwritable one boots to RUNNING (T9). A zero-automation boot writes no file.

## §4 The §6 survey, as run
`new InMemoryAutomationIdentityStore` = 2, both tests (root 0). `new AutomationDefinitionLoader|loader.load(` in main = the root only — **R1: no hot-reload site exists**. Config-dir listings: `Files.list(configDir)` ×2 in `config` main, both prefix-filtered; in tests only `TokenCliTest:116` (boots no core) — nothing flips. ARCH-RULE-REACH: `grep -n automation HomeSynapseArchRules.java` → `:150` (reverse deps) and `:197` — the finding.

## §5 Deviations by tag
- **[BLOCKING→RULED]** the ArchUnit conflict (§0). The hub owned §6's un-run grep and the `AtomicCheckpointSink` cite (a SQLite seam; the idiom is `AtomicYamlWriter:185`).
- **[REVIEW] R-1** the bracket is STRICTER than row 5's "persists nothing": an identity asked for outside it throws. A quiet mint there is F-1 again with no symptom until a restart.
- **[REVIEW] R-2** the `last_seen` write (P3). Unpersisted, a slug removed on day 35 of continuous use retires at the next boot, not 30 days after removal (P3b pins it). Cost: one ~1 KB atomic write per boot.
- **[REVIEW] R-3** three rows past the re-cut: rows 4–5 (the sentences "not yet wired" / "pending the file-backed store" became false) and row 13 — R7's conditional test: the FATAL-path home EXISTS, in `HomeSynapseCoreStartupFailureTest` (T4), not `HomeSynapseCoreTest`; T9 rides it as the only place the ERROR token can be pinned (`core/automation`'s test tree has no logback).
- **[REVIEW] R-4** the FATAL arm's operator surface: `recommendationFor` has no `automation` arm → the default sentence and exit 99. The ISE names the path and the recovery (restore, or remove to re-mint). An arm is a row for the hub; row 6 said "nothing else".
- **[REVIEW] R-5** `beginLoad()` reads ONCE per store, not per call: after a failed write, memory must not be replaced by the older file; this store is the only writer.
- **[REVIEW] R-6** the STORE sorts, the companion preserves order (the ruling listed "sorted keys" under the companion): an alphabetical re-sort there would put `automations` above `schema_version` and order indices `"10" < "2"`.
- **[REVIEW] R-7** §5's `INV-GA-02` is "Invariant Identifiers Are Permanent" (`Architecture_Invariants_v1.md:809`) — INV labels, not runtime ids. The property holds by `UlidFactory`'s monotonic mint (LTD-04); my three repeats of the cite were corrected → round 2.
- **[INFO]** two positive-evidence INFO tokens added (ledger 17) · `last_seen` truncated to whole seconds · T1 passes `() -> 0L`, so not even the carve-out's `System::nanoTime` · one id under two slugs also fails closed · cite drift `HeroLoopHardwareFreeIT:515` → `:455` · the cap: the skill's arithmetic gives 18 KB for 15 rows; filed under the instruction's 13.

## §6 INV/LTD sweep
LTD-11 (`ReentrantLock`, never across the seam's I/O) · LTD-04 (`AutomationId`; trigger ids stay `String` per the interface) · NO_DIRECT_TIME_ACCESS (every instant from the injected clock; tests: `MutableClock` STARTING 31 days before `FIXED_INSTANT` and advancing TO it — `UlidFactory`'s guard is JVM-wide) · Doc 12 §4 verified at `:198/:501` · Doc 07 §4.1 `:622` · AMD-93 §2.3 `:43–:47` verified.

## §7 Instrument limits
`./gradlew check` NOT run — **Deferred Build Gate: owed to CI on the landing sha.** The desk is Windows: the two failure provocations (a directory on the `.tmp` sibling; a non-empty directory at the target) are reasoned for POSIX, first run there by CI. T9's squatter is not a read-only filesystem — the same `FileChannel.open` arm, a different errno. The directory fsync takes its DEBUG arm here. `identity_loaded` / `identity_retired` / `identity_load_ended` carry no log pin (the retirement itself is T4c's). The staged-red predictions were filed 12 s AFTER that run ended (12:58:06Z vs :18Z), its output unopened — before the reading, not before the launch.

## §8 R5, for the deploy card
The first boot of this build mints every automation's id once more and writes `automations.ids.yaml`; run history before that boot is orphaned exactly as every restart orphaned it until now, and from that boot on the ids hold.

## §12 Closeout (WUCP Phase 1)
- [x] tests first, red for the right reason, then green; the gate verbatim; freshness from executed-state lines + XML mtimes
- [x] both MODULE_CONTEXTs; the four tokens documented
- [x] census exact; nothing staged, nothing committed
- [x] deviations by honest severity; the pushback raised BEFORE implementing
- [x] **the `coder-handoff.md` entry, for the hub to file:** `AUTO-ID-1 DELIVERED 2026-09-20, uncommitted 15 = 8 M + 7 A on c819a02 (core 8 M + 6 A) — automation identity is durable: CompanionAutomationIdentityStore (core/automation, policy) over AutomationIdentityCompanion, the bytes in lifecycle's FileAutomationIdentityCompanion (the hub's mid-lane I/O-seam ruling: NO_DIRECT_FILESYSTEM_IN_CORE); T1 red→green, hero_id_stable=true; gate line green (automation 267 · lifecycle 93 · app 30). Deferred Build Gate: ./gradlew check owed to CI on the landing sha. Seven [REVIEW]s await the hub. NEXT WU: LINK-READ.`
- Lessons (file outside the write-set): (1) run the ARCH-RULE grep before a row places I/O in a core package — the red appears only at `:app:…:test`, never in the module's own tests; (2) in Git Bash `grep -c $'\r'` matches EVERY line — count CR bytes with `tr -cd '\r' | wc -c`; (3) what a store accepts on write it must read back — test the ugly keys.
RETURNED nexsys-hivemind/context/audits/2026-09-20_AUTO-ID-1_return.md 12987
