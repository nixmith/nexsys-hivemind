<!--
file: context/audits/2026-09-27_v82-b2_IR18-intake_audit.md
purpose: The v82 beat-2 audit — IR-18's return intaken two-layer (the Coder's claims read critically; the hub's own re-execution at the bytes on the core tree); the core landing and the CI verdict banked; BENCH-CORE-4's card cut under the prior-ledger gate; the weeks-ahead plan cut on Nick's word. The non-re-executions named.
audience: the hub (the record) · Nick (§0)
state-type: intake audit
status: FILED — v82 beat 2 (Sun 2026-09-27 ~12:0x CT; instrument 2026-09-27T17:05:28Z)
-->

# v82 beat 2 — IR-18 intaken; the core landed; BENCH-CORE-4 cut; the weeks ahead (Sun 2026-09-27 ~12:0x CT)

## §0 The verdicts
- **IR-18's return** (`context/audits/2026-09-27_IR18_return.md`, 9,945 B; RETURNED 16:24:01Z): **ACCEPT.** Every claim the hub could re-execute holds (§2); the three [INFO] deviations ACCEPTED (§3); three findings → IR-71..73, one lesson → coder-lessons (§4).
- **The core landing:** `e96dce8` (Sun 11:48:56 CT) — HEAD at the instrument; porcelain 0; ahead 0; the message carries no trailer. **CI green on Nick's word** ("all checks passed green in GitHub for the `e96dce8` commit"; the run number not given — the Actions page is the instrument; banked as the gate of record). **The closure counter 14/20.**
- **BENCH-CORE-4 cut** (`context/instructions/2026-09-27_bench-card_BENCH-CORE-4_core-to-e96dce8_installDist_operator-session-prompt.md`) under THE PRIOR-LEDGER GATE (§5); handed for tonight (D-v82-13 re-sequences D-v82-6: CI green arrived before the rehearsal, so the bench card moves first and the rehearsal sits on `e96dce8`).
- **THE WEEKS AHEAD cut** (`context/planning/2026-09-27_v82_THE-WEEKS-AHEAD_program-and-company-plan.md`; the plan §29 points at it) on Nick's word of 11:52 CT; its §7 carries the H10 rows, IR-61's design fork first (§6).
- **METER-3 running** (`M3: running`, 11:52 CT); the model the hub recommended: Fable 5.1 (D-v82-12); the model chosen is not in the record.

## §1 The core landing at the instrument
`git log -2`: `e96dce8 2026-09-27 11:48:56 -0500 feat(zigbee): IR-18 — …` ← `d22a8a4`; `status --porcelain -uall` 0; `rev-list --count origin/main..HEAD` 0; the trailer grep on `log -1 --format=%B` 0. The message is the file `_scratch/v82/2026-09-27_core_IR18_commit-msg.txt` (3,370 B; Nick's form: Why · What changed · Evidence · Census 11 = 9 M + 2 A). Not re-executed: the CI run itself (no GitHub access from the hub); Nick's word is the line.

## §2 IR-18's return — two layers
**Layer 1 (the return read critically, whole — 9,945 B ≤ the 10,000 B ceiling):** §0 the card (DELIVERED; `check` green EXIT 0 in 54 s; 692/0/1 in zigbee; Σ 3,621; porcelain 9 M + 2 `??`; red-first in three stages; §10's four points; three [INFO] deviations; the cap note) · §1 the spans per file · §2 the observed reds and the seven mutants · §3 the deviations · §4 the survey as re-run (widened for A1 to every module's fixtures, the testFixtures rig included) · §5 three findings + one lesson · §6 the coder-handoff text · §7 the instrument limits.
**Layer 2 (the hub's own re-execution on the working tree before the commit, then at `e96dce8`):**
| The claim | The instrument | Result |
|---|---|---|
| porcelain = §3's eleven files, 9 M + 2 `??`, nothing staged | `git status --porcelain -uall`; `diff --cached` | CONFIRMED (11; cached 0) |
| `git diff --stat` 9 files, +237 −25; the two new files 76 + 133 lines | the same commands; `wc -l` | CONFIRMED |
| `MODULE_CONTEXT.md` +2 rows, 0 deletions | `diff --numstat` → `2 0` | CONFIRMED |
| `EntityType.java` javadoc only | `git diff` filtered to changed lines: one `-` and five `+`, all ` * ` javadoc | CONFIRMED |
| the handler: sentinel before the band; the band at 0xFFFF; DP-1 its own branch; one decimal; the dialect string | `IlluminanceMeasurementHandler.java` :34–:75 read | CONFIRMED (matches §4 Row 1 as re-cut) |
| `withMeasurements`: the three-row table; append-if-absent by capability id; SENSOR when empty | `EndpointClassifier.java` :64–:75, :228–:261 read | CONFIRMED (matches §4 Row 3 as re-cut) |
| the reporting row `0x0400 → (0x0000, 0x21, 10, 3600, 1000)` | `ReportingConfigurator.java` :86 | CONFIRMED |
| `@Test` 679 → 692 in the zigbee test tree | the count at HEAD (`git show HEAD:<file>` per tracked test file) vs the working tree | CONFIRMED (679 / 692) |
| `check` green; the zigbee XML fresh | `check.log` :309 `BUILD SUCCESSFUL in 54s`, `156 actionable tasks: 23 executed, 133 up-to-date`; `check.start` 16:20:06Z; the zigbee XML 83 files, tests 692, failures 0, newest mtime 16:20:33Z; the census file's module rows | CONFIRMED |
| T11 asserts the key and the dialect on the published event | `ZclIngestionUnitTest.java` :686 (`illuminance_lux`), :690 (`log10x10000+1`) | CONFIRMED |
| no clock API in the new test; no token; no trailer; no secret in the diff | greps over the new test and the diff | CONFIRMED (0 · 0 · 0 · 0) |
Not re-executed: `./gradlew check` itself on the hub's VM (no Gradle distribution; CI is the gate and it is green); the seven mutants (the logs under `_scratch/v82/2026-09-27_IR18/mutations*/` exist; not replayed); the three up-to-date test tasks (the lane's own disclosure).

## §3 The deviations, ruled
- **D-1 [INFO] the uint16 band + T6b — ACCEPTED.** A mis-typed record reaching `normalize` (`ZclCodec` :199–:204 decodes uint24/32/48 to `Long` without checking the attribute's type) would otherwise publish ≈ 9.2e17 lux; the guard is F-9's own rule; the first cut at 0xFFFE that made the sentinel check dead code was caught by the lane's own mutant and corrected — the return says so at honest severity.
- **D-2 [INFO] the names moved with the counts — ACCEPTED** (hygiene the instruction's row 6 implied).
- **D-3 [INFO] the T10 fake records attribute and type — ACCEPTED** (T10 could not pin 0x0000 / 0x21 otherwise; nothing else reads the field).
- **T9's third leg** (`[0x0000, 0x0400]` → SENSOR + illuminance) — named in Row 3's pin list, placed by the Coder; correct.
- **B2 not taken** (`hasSize` kept, `containsOnlyKeys` declined) — the Coder's call, as allowed.
- **Two errata of the instruction, recorded:** (i) §1's "0 hits" grep has one hit — `MeteringHandler.java` :32, a javadoc line naming attribute 0x0400 (harmless); (ii) the return contract asked the MESSAGE to end with `RETURNED …` while the bridge convention reads a return file's LAST LINE — the file ends with the WUCP line; Nick's transcript carried the `RETURNED` line. → IR-74 (the format law: the file's last line IS the `RETURNED` line; the coder skill's 3 KB + 1 KB/row arithmetic reconciled with the instruction's ceiling).

## §4 The findings → the register; the lesson → coder-lessons
IR-71 (F-1: `EntityType`'s LIGHT / SWITCH / ENERGY_METER optional-capability sentences name neither the meters nor the measurements) · IR-72 (F-2: the rig's `wireType` has no 0x0400 row) · IR-73 (F-3: `buildCommand_ingestionOnlyHandlersThrow` omits 0x0400) · IR-74 (§3's errata). L-1 → `context/lessons/coder-lessons.md`: a band guard can shadow a spec'd sentinel; mutate each guard alone. The coder-handoff entry (the return's §6) spliced verbatim; the NEXT WU pointer → IR-61 on the word of the weeks-ahead plan §7 row 2.

## §5 BENCH-CORE-4 — the cut under THE PRIOR-LEDGER GATE
The prior record: BC3's guide notes (`context/audits/2026-09-27_BENCH-CORE-3_guide-notes.md`) grepped for every reused command string and witness (`tail -2` 1 · `BUILD pid` 2 · `ff-only` 1 · `bench.sh restart` 1 · `boot-health` 5 · `.backup` 3 · `current.log` 2 · `relinked` 3 · `network_resumed` 2 · `installDist` 3 · `STOP` 6). Hits carried as named deviations from BC3's strings: obs. 3 (the pull's `tail -2` hid the fast-forward word → the pull's output filtered for the mode word); obs. 4 / IR-64 (the `BUILD pid=… log=…build-.log` echo → the stamp set before the build; only the build backgrounded). Carried as an EXPECTED note: obs. 6 (two boots inside Block 3). Dropped: Block 0b's REP-1 queries (closed at v81 b6). Added to Block 3: the JVM's pid + start time; IR-18's class counted in the installed zigbee jar (`ir18-class-in-tree`), the two proofs BC3 could not give. Every fenced block passes `bash -n`; `pgrep -f "[j]ava.*homesynapse-app"` so the shell's own command line never matches. The sha strings: `d22a8a4` ×4 (the from-sha and BC3's references), `e96dce8` ×6.

## §6 THE WEEKS AHEAD — the inputs read
The horizon re-cut §0–§3 (the frame; the three postures; the eight questions; the P6/P7 rows under `pilot-first`) · the plan §2 (the critical path's seven rows) · the plan §28 · the brief's company row · the v82 text's window · Doc 03 §3.8 (AMD-11's staleness model: the threshold chain, `staleAfter = eventTime + resolvedThreshold`, the scan, the read-time evaluation) and AMD-53-INV-02 (the real-time carve-out; "threshold resolution is not yet wired") · `StateProjection.java` :994–:1016 (`staleAfter` stays null at adoption; carried as `prior.staleAfter()` on every event) · `MaterializedStateQueryService` :43–:52 (the read-time recomputation exists) · the §9 config keys at Doc 03 :747/:754 · grep: no `state_stale`, no `staleness_overrides`, no `expected_report_interval` in core main. From these, IR-61's fork (§7 row 2 of the plan): the register's per-device cadence is a fourth threshold source Doc 03 does not have — an AMD — while the chain as designed, with a capability default of 180 s on `power_meter`, already flags G4-2's silence at 3 min. The rec: as-designed now; the AMD after the run only if the pilot fleet demands it.

## §7 Not re-executed, disclosed
The CI run (Nick's word); `./gradlew check` on the hub's VM; the mutants' replay; the review of Doc 02 §3.5's capability-schema declaration site for `expected_report_interval` (the pre-verification precedes IR-61's instruction); the model METER-3 runs on.
