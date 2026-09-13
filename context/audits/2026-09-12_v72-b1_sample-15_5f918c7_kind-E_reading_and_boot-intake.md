<!--
file: context/audits/2026-09-12_v72-b1_sample-15_5f918c7_kind-E_reading_and_boot-intake.md
purpose: v72 beat 1 — the reading of sample #15 (core `5f918c7`, the `bus-soak` job) at the bytes, the ruling it triggers, and the boot intake (Nick's dispatch text verbatim, the HEADs, the twelve preflight lines, the byte budget). The exhibit AMD-101 §6 cites.
audience: the hub (every beat of v72) · Nick (§0 and §2) · the BUS-ORDER-1 lane (§1, the line it is written to remove)
state-type: intake audit + evidence reading
status: FILED Sat 2026-09-12 ~19:5x CT (instrument 2026-09-13T00:53:13Z)
-->

# v72 beat 1 — sample #15 read: kind E; the boot intake

## §0 The verdict
Sample #15 is the first `bus.delivery_anomaly` line under FIX-2b-ii's instrument and its kind is `NOTIFY_SKIPPED_LIVE` (kind E). Under Nick's ruling of 2026-09-12 (`context/planning/2026-09-12_v71_BUSFIX-b_ruling-of-record.md`) and the v71 beat-6 record, that kind is the exhibit AMD-101 §6 reserved; the revert clock to (c) stops at 1/10; BUS-ORDER-1 dispatches on the clean core tree at `5f918c7` on his paste, and `BUSORDER: go` is his line when the lane runs. No delivery was missed in the run: the census shows 254 of 254 delivered to both scored subscribers.

## §1 The reading at the bytes
The artifact Nick unzipped: `ClaudeFolder/_scratch/v71/ci-5f918c7/` (`reports/tests/test/…` and `test-results/test/…`; the run number was not kept with the unzip). The file read: `test-results/test/TEST-com.homesynapse.lifecycle.BusSoakIT.xml`, 28,929 B; testsuite timestamp `2026-09-12T23:47:03`, hostname `runnervmlun5p`, `tests="1" failures="1"`. The census IT beside it: `TEST-com.homesynapse.lifecycle.BusPositionCensusIT.xml`, `tests="1" skipped="0" failures="0" errors="0"`.

The failure (XML line 5, the stack at line 8): `org.opentest4j.AssertionFailedError: [bus.soak: anomalies] expected: 0L but was: 1L` at `BusSoakIT.soak_kHeroLoops_reportsLatencyAndAnomalies(BusSoakIT.java:204)`; the source line at `5f918c7` reads `assertThat(anomalies).as("bus.soak: anomalies").isZero();` (verified by `git ls-files` + `sed -n 204p`).

The anomaly line (XML line 114), verbatim:
```
23:47:05.464 [Test worker] WARN  c.h.lifecycle.HomeSynapseCore -- bus.delivery_anomaly: kind=NOTIFY_SKIPPED_LIVE subscriber=automation_engine position=206 detail=notifyEvent: checkpoint=207 at or past position at=2026-01-01T00:00:00Z
```
Its neighbours: the 16th `automation.run_handoff` line at 23:47:05.405 (`runId=…RQ`, `mode=admitted`) and the 17th at 23:47:05.471 (`runId=…S4`). The line is on the `[Test worker]` thread, the publisher side; every hand-off line is on `[hs-sub-automation_engine]`.

The soak and census tokens (XML lines 127–131), verbatim:
```
bus.soak_host: available_processors=2 vt_parallelism=default
bus.soak: loops=20 ok=20 timed_out=0 p50_ms=21 p99_ms=70 max_ms=70 anomalies=1
bus.position_census: subscriber=state_projection matched=254 delivered=254 missed=0 first_missed=none checkpoint=254 dlq=0 pending=0 atomic=true
bus.position_census: subscriber=automation_engine matched=254 delivered=254 missed=0 first_missed=none checkpoint=254 dlq=0 pending=0
bus.position_census: subscriber=command_dispatch_service matched=20 delivered=20 missed=0 first_missed=none checkpoint=247 dlq=0 pending=0
```
What the lines say together: twenty loops completed, none timed out; at position 206 the LIVE notify for `automation_engine` was skipped because the persisted checkpoint already read 207 — the checkpoint ran ahead of the position at notify time, the non-monotonic-checkpoint arm the v71 REV-1 read named and AMD-101 §1 describes; a later notify carried the loop on, so the skip did not become a miss in this run (254/254). The harm the kind names is the run where no later notify comes.

Not re-executed, disclosed: the GitHub run number (not on disk); the CI job log (not staged; the artifact carries the kind, the log only the count); the sample's runner-class beyond the printed `available_processors=2`.

## §2 What follows under the ruling
1. AMD-101 §6's reserved row is filled with this exhibit (the docs working tree, 1 M; it lands on the `AMD101: ratify` card with the §4 edit — no docs card is handed tonight).
2. The revert clock stops at 1/10 (`72efb42` was its one silent sample); `BUSFIX: b` stands.
3. BUS-ORDER-1's gate, at the instrument: core HEAD `5f918c7`; `git log --oneline 72efb42..HEAD` = one commit (EXPLAIN-114a's); porcelain 0; no other lane on the Java path-domain (HERO-1b landed; EXPLAIN-114a landed). The instruction stays ISSUE-READY with its status line noting the gate met; §8 is the paste handed as the one act; his `BUSORDER: go` is the report that the lane is running.
4. OR-BUS-SILENT-DROP's closure counter restarts at BUS-ORDER-1's landing (twenty green samples with kind E at zero).

## §3 The boot intake
**Nick's dispatch text, verbatim (his `My lines:` slot was left as the placeholder — no lines were given):**
```
You are the v72 PM MISSION-CONTROL hub for NexSys / HomeSynapse. Boot from `nexsys-hivemind/context/handoff/2026-09-06_PM-mission-control_v67_orchestrator_session_prompt.md` (the STABLE form — no state in it) and execute its §1 EXACTLY, inside its boot byte budget: date -u first; `pm-handoff.md` line 8 + the newest ONE beat; `PROJECT_SNAPSHOT.md`; `context/handoff/OPERATOR-BRIEF_for-Nick.md` whole — its §HELD-BY-THE-HUB is the wait-state ledger; the decision record §3; the plan of record §3; the five HEADs in one call; the preflight as one line per check. THE OPERATOR-LOAD LAW and THE CONTEXT-BUDGET LAW (§1b) bind every message and every call. Beat 1: name the window's ONE deliverable, the intake at the bytes, this text verbatim, §HELD re-printed, hand me ONE act. STATE AT DISPATCH (the record wins): core `5f918c7` (EXPLAIN-114a + R3; check GREEN; the bus-soak job RED anomalies=1 = sample #15, unzipped at `_scratch/v71/ci-5f918c7/`, UNREAD — read it first: the kind decides BUS-ORDER-1's dispatch); hivemind `3209101`; docs `0d62a54` (AMD-101 PROPOSED). My lines: <paste each one-line report here>.
```
**The boot read-set (the ≤45 KB budget):** the prompt 13,017 · `pm-handoff.md:8` 2,192 · the newest beat 2,430 · the snapshot 3,471 · the brief 12,234 · the v66 decision record §3 1,969 · the plan of record §3 4,800 (capped of 5,399) · pm-lessons after the ledger 3,600 (capped of 7,640) = 43,713 B.

**The HEADs (one call, 2026-09-13 00:4xZ):** core `5f918c7` · hivemind `3209101` · skills `c630c5c` · bench `4539f13` · docs `0d62a54`; porcelain 0 in all five; `origin/main..HEAD` 0 in all five; no `.git/*.lock`. The state at dispatch and the record agree.

**The preflight, one line per check:**
- Check 1 PASS — snapshot and handoff both `2026-09-12 (v71 beat 6)`.
- Check 2 PASS — the same beat in both spine files; `context/planning/2026-09_september_plan-of-record.md` exists (the STATE-OF-THE-PROGRAM assessment is the plan of record by D4).
- Check 3 PASS — core HEAD `5f918c7` = the snapshot's state line.
- Check 4 PASS-per-proxy — 29 DONE rows; the backlog's own `last-verified:` is 2026-08-01 (v43); no milestone closed since; the v1.1.4 freeze row rides the freeze note.
- Check 5 PASS — Open Risks dated through 2026-09-12; six open.
- Check 6 PASS-per-record — the newest coder-handoff entry is FIX-2b-ii (i) (2026-09-12); the next WU is named by the spine (BUS-ORDER-1); the file's frontmatter chain is a Coder-side line last cut 2026-08-23.
- Check 7 PASS — 22 modules in `settings.gradle.kts`, 21 MODULE_CONTEXT files; the one without is `spike/wal-validation` (a spike, not a Phase-2 module); none under 1,500 B.
- Check 8 PASS — cross-agent-notes carries no active entry.
- Check 9 STALE — 27/28 identical at the bytes; `project-manager/SKILL.md` differs (source `bda340b1…`, synced `76bf4ce6…`): the known one file since v71; Nick's sync clears it; no lane waits on it.
- Check 10 PASS — 97 cited `.md` paths resolve; the three unresolved are the map's own `YYYY-…` templates.
- Check 11 PASS — `BusSoakIT.java:204` is the assertion the spine quotes.
- Check 12 STALE by one, fixed this beat — six `status: ISSUE-READY|LIVE` instruction files: RS3-WMARKET-2 (running on cadence), H8-a (record owed), R-4c (record owed), P-1 (gated), BUS-ORDER-1 (gated → handed), and the R3 correction paste, which had executed — flipped to EXECUTED in this splice; LIVE prompts other than v67: 0; `weeks/`: 0.
**Aggregate:** PASS with Check 9 STALE (known; not blocking) — forward work lawful.

**Context discipline note:** one boot call in this beat exceeded the result cap (a `grep -rn` whose file argument resolved empty recursed the repo; the result was saved to disk and read by range). Every later grep names its file and caps its lines.

## §4 The window
The deliverable: BUS-ORDER-1 running and its return audited. Blocks: b1 this; b2 HERO-1c's charter; b3 114b from the EXPLAIN return; then the intakes as the lines come (`BUSORDER: RETURNED` · `R4C:` · `H8A:` · `AMD101: ratify`); the close ≤ b8, no new block after b6.
