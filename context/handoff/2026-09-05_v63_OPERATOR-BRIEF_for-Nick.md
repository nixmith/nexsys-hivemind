<!--
file: context/handoff/2026-09-05_v63_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR QUEUE for v63 — every act he performs, in order, fully articulated (WHAT · WHY · the exact command or paste · EXPECTED RESULT · REPORT BACK), with a self-contained CONTEXT preamble so Nick — or any other Claude session he hands this file to — can understand the state of record and the hub's reasoning WITHOUT inventing context. The copy-source of record is this file on disk, never a chat card. Nick's directive (09-03) + his v63 ask (09-04 evening): "an operator queue/guide … in order, and with all context necessary".
audience: Nick · any helper session (read §CONTEXT first; every claim there has a file path)
state-type: operator brief (live; the hub re-cuts it at every beat that changes an act)
status: LIVE from v63 beat 1 (Fri 2026-09-04, instrument 23:0xZ = 18:0x CT). Retires context/handoff/2026-09-03_v62_OPERATOR-BRIEF_for-Nick.md in place (its §CLOSE Act 1 is re-issued here as Act 1, verbatim).
-->

# Operator brief — v63: what Nick does, in order

## §CONTEXT — the state of record, for you or any helper session (every line has a path; nothing here is from memory)

**The product and the plan, in three lines.** HomeSynapse Core is a local-first, event-sourced smart-home runtime (Java 21, SQLite event store, an in-process event bus, a real Zigbee adapter, one systemd unit on a Pi). Its wedge is THE MEASURED CORPUS — claims minted only on measured objects (`nexsys-hivemind/context/strategy/claim-register.md`: C-001 LIVE narrow · C-002 LIVE and standing · C-003 a slot). The critical path for September: FAILCHAN-FIX-1's green → CG-1/2/3 → the FE fast-follow → H8 real-wire → R-4c/C-003 → the R-5 charter, alongside the brand's dated words (09-07 Erik · 09-11 EU · 09-15 Activate · 09-18 the hard stop). The plan: `context/planning/2026-09_september_plan-of-record.md`; the strategy: `context/strategy/2026-08-27_company-and-brand-build_strategy-of-record.md` (v1.2, ratified).

**Where the code is tonight (the gate).** `homesynapse-core` `main` = **`dc3328b`** (your PR #5 merge; Java bytes identical to `7af2d6c`, the FAILCHAN commit). **`main` is RED on two different runs, two different tests:** CI #225 on `7af2d6c` failed `HeroLoopHardwareFreeIT` (lifecycle); `dc3328b`'s own run failed `ReplayTransitionIT:212` (core:event-bus) and never reached lifecycle; PR #5's run on the same Java bytes was GREEN. Three runs, three outcomes, identical code → **non-determinism, established at the instrument** (`git log` shows Dependabot's commit `8e6e0e1` has `7af2d6c` as its parent — so I-0 is answered without your click). The whole analysis, with the CI log you pasted filed verbatim and every source line cited: `context/audits/2026-09-04_v63-b1_boot-grounding_executive-model-and-intake.md` (§3 the three-run table · §4 the source reads · §5 where the documents were wrong · §6 the ruling).

**What the hub found at source (why the fix is shaped the way it is).** The bus's LIVE delivery loop and its TRANSITION drain have **four places where a position whose read comes back empty or throws is silently skipped forever** (`InProcessEventBus.java:250 :480 :487`; `TransitionCoordinator.java:100`) — no log, no metric. A skipped `command_issued` produces exactly the `integration.route_join_miss` WARN your census counted once — the fingerprint of the red HeroLoop method. The FAILCHAN §10-O hunk the v62 ruling wanted reverted lives in `productionLoop()`, which the hardware-free rig NEVER runs (driven mode) — so that instrument was retired. And CI (`ci.yml`) stops at the first failing module and uploads only HTML on failure, which is why no red run has ever carried its own mechanism.

**The rule the hub is proposing (your word, Act 4):** FIX-1's charter is THE CLASS (both tests; the silent drops made visible, then fixed on the measurement; CI made to report everything), not the single HeroLoop instance — because with two independent flaky tests, fixing one leaves every later push a coin flip, and `main` red means no other core lane. Cost: about one extra lane-day; CG slips the same. The alternative (`instance`) is faster to one green and pays for it on every later push. Details and the refutation conditions: the audit §6.

**The fences (unchanged; the hub holds them):** the hub never implements · one lane on the core tree · `main` red = no other core lane before the fix · never re-run `main` CI as clearance (a dispatch sample may VETO a green, never GRANT one — Act 8) · never `--allow-downgrades` · `network_formed` anywhere = POWER OFF + STOP · s31/nightly HANDS OFF until R-5 · token VALUES never (`TOKLEN-OK`) · no public brand use before the written opinion, hard stop 09-18 · no name-by-name brand grading in chat · core/bench/docs commits are YOUR hands; hivemind/skills are the hub's at the bridge; **push is always yours**.

**The files the hub wrote at v63 beat 1 (all in `nexsys-hivemind/`):** the grounding audit above · the FIX-1 instruction `context/instructions/2026-09-04_coder-lane_FAILCHAN-FIX-1_CI-nondeterminism_coding-instruction.md` · this brief · the spine (`context/handoff/pm-handoff.md` v63 beat 1 + `context/status/PROJECT_SNAPSHOT.md`). The hub committed them (hivemind is hub-run); the push is yours (Act 9).

---

## §QUEUE — the acts, in order (≈25 min of your hands tonight, then the lane runs; the rest is dated)

### Act 1 — file the §A2 census to disk (≤3 min; the terminal where `~/ci-225/…` lives) — re-issued verbatim from the v62 brief; it was not run
**WHAT:** re-run the census and write it into the hivemind repo as a text file (the hub commits it at its next beat — you stage nothing). **WHY:** an instrument a WU authors on is filed at the bytes, never held in chat (a v62 law); the FIX-1 lane reads the `route_join_miss` WARN line's ids from it. `cd` to your `nexsys-hivemind` checkout first.
```bash
R=~/ci-225/lifecycle/lifecycle/build/reports/tests/test/classes/com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.html
OUT=context/audits/2026-09-04_CI-225_HeroLoopHardwareFreeIT_stdout-census.txt
test -f "$R" && test -d context/audits && { echo "# CI #225 (run 33875188761) on 7af2d6c — the HeroLoopHardwareFreeIT class report; filed by Nick $(date -u +%Y-%m-%dT%H:%M:%SZ) at the v62 close"; echo; echo "## token census (the §A2 regex)"; grep -oE 'zigbee\.[a-z_]+|lifecycle\.[a-z_]+|integration\.[a-z_]+|automation\.[a-z_]+' "$R" | sort | uniq -c | sort -rn; echo; echo "## <N> journald-prefix count (both raw and HTML-escaped forms)"; grep -cE '^(<|&lt;)[0-9](>|&gt;)' "$R"; echo; echo "## the report's text, last 150 lines (tags stripped)"; sed 's/<[^>]*>//g' "$R" | tail -150; } > "$OUT" && wc -c "$OUT" || echo "STOP: wrong directory or the report is missing — tell v63"
git status --porcelain; grep -n 'route_join_miss' "$OUT" | head -3
```
**EXPECTED:** `wc -c` prints a few thousand bytes; `git status --porcelain` prints exactly `?? context/audits/2026-09-04_CI-225_HeroLoopHardwareFreeIT_stdout-census.txt`; the last command prints the WARN line with `event_id=… causation_id=… integration_id=… correlation_id=…` (if it prints nothing, the WARN fell outside the last 150 lines — say so; the hub widens the tail). **REPORT BACK:** `census filed (<bytes>) · route_join_miss line: <present | absent>`. If `~/ci-225` no longer exists, report `census: artifact gone` — the lane rebuilds per-method truth on the FIX-1a tree and the act closes.

### Act 2 — I-1: the prior reds' identity (≤5 min; GitHub, read-only) — was optional, now the highest-value five minutes you have
**WHAT:** GitHub → `homesynapse-core` → Actions → the `CI` workflow → open runs **#169, #183, #206** → the red `Build & Check` job → the `Run check` step → the `… FAILED` line(s) and the `java.lang.… at <File>.java:<line>` beneath. **WHY:** if any of them failed on `ReplayTransitionIT` or `HeroLoopHardwareFreeIT`, the flaky class predates FAILCHAN by weeks (branch (a) for that class) and the instruction's §A.5 prediction row is confirmed before a single loop runs; if all three were a THIRD test, the class is "timing-bounded ITs on the runner" in general and the CI instrumentation is the larger half of the WU. **REPORT BACK:** one line per run, verbatim from the log — `#169: <TestClass> · <the FAILED display name> · <the exception line>` (and the same for #183, #206). `not read` is a legal answer; the lane proceeds without it.

### Act 3 — the `dc3328b` run's failure MESSAGE (≤3 min; GitHub, read-only)
**WHAT:** open `dc3328b`'s red `CI / Build & Check` run → the **Summary** page → the `Artifacts` box → download `test-reports` → unzip → open `core/event-bus/build/reports/tests/test/classes/com.homesynapse.event.bus.ReplayTransitionIT.html` in a browser → copy the failure text under the test name. **WHY:** the console showed only `java.lang.AssertionError at ReplayTransitionIT.java:212`; the HTML carries the message, which says WHICH wait timed out — `did not reach 1000 within 15000 ms` (phase 1: a plain bus, no concurrent publisher — a lost wakeup on a single subscriber) or `did not reach 1500 within 30000 ms` (phase 2: the REPLAY→TRANSITION→LIVE race under a live publisher — the mechanism the test exists to catch). The hub predicted phase 2; a mismatch is adjudicated first. **REPORT BACK:** the message, verbatim, in one line. If the artifact is absent (7-day retention; it should exist), say `artifact: absent`.

### Act 4 — four words (≤2 min; in your reply to the hub)
- `PROTECT: a | b | dismissed` — what you did with the "main isn't protected" banner (rec (a): block force-pushes + deletions only; (b) "require status checks" = docket Row 34, a process change for the public-flip sitting; `dismissed` is fine tonight).
- `ROW33: <one line>` — the entity→device mapping for `01M19RHWXYZYJMM26SX0E41HXN` in your own words (the hub lost the verbatim at v62's compaction and will not reconstruct it; it goes into the docket Row 33 and the R-4b audit §6 as YOUR line).
- `FIX1: class | instance` — the ruling in §CONTEXT (rec `class`; it is the default if you paste Act 5 as written).
- `SAMPLES: veto-only | none` — whether, after FIX-1b's push run is green, you take three `workflow_dispatch` samples of the landed sha that can veto the clearance but never grant it (rec `veto-only`; Act 8 carries the how).

### Act 5 — dispatch the FIX-1 lane (≤2 min; then the lane runs ~4–8 h on its own: the instruments, ≥60 timed test runs, the fix)
**WHAT:** open a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core` and paste this as its first message, verbatim. **WHY:** it is the one permitted lane on the core tree; it executes the instruction's Part A (make every silent drop visible; make CI report everything; measure both tests under runner-shaped scheduling) BEFORE Part B (fix the mechanism the measurement names) — instrument-first is the ruling, and the lane's pushback is first-class evidence. Its tree must be at `dc3328b` and clean (it checks).
```
date -u first. Boot as the nexsys-coder skill. Baseline: this tree must be at dc3328b and clean — verify with `git log -1 --format=%h` and `git status --porcelain` (STOP and report if not). Execute nexsys-hivemind/context/instructions/2026-09-04_coder-lane_FAILCHAN-FIX-1_CI-nondeterminism_coding-instruction.md exactly: read its §0 contract, the grounding audit §2–§4 it points at, and the minimum read set first. FIX1: class. Part A before Part B — the instruments (FIX-1a, census 9 = 7 M + 2 A, tests T1–T4 red at HEAD) and then the loops (§A.3/§A.4, ≥60 runs, the corpus to nexsys-hivemind/context/audits/2026-09-05_FIX-1_loops/); fill the §A.5 table BEFORE writing a line of FIX-1b; declare FIX-1b's branch per class from the table. Return ONE file at nexsys-hivemind/context/audits/2026-09-05_FIX-1_return.md, §0 card first, ≤12 KB target. Stage nothing; commit nothing; the hub audits and Nick commits FIX-1a first, then FIX-1b.
```
(If your word is `instance`, replace `FIX1: class.` with `FIX1: instance.` — the lane then narrows Part B to HeroLoop; Part A is unchanged.) **EXPECTED:** it prints `date -u`, confirms `dc3328b` clean, reads the instruction and the audit, and starts FIX-1a. It will need WSL (or any Linux shell) for the `taskset` loops — if it asks, say which you have; if neither, it states the limit and uses the `-PvtParallelism=2` knob alone. **REPORT BACK (to the hub):** `FIX-1 lane: dispatched <time>` — then nothing until it returns; when it does, `FIX-1 lane returned` (the file exists at the path; the hub audits it at the bytes — you do not summarize it).

### Act 6 — hand the return to the hub (≤1 min; when the lane says it is done)
**WHAT:** tell v63 `FIX-1 lane returned` and paste the lane's last ~10 lines. **WHY:** the hub's two-layer audit (its own re-execution at the bytes: the census vs the Files table, the red-first table, the §A.5 measurements vs the predictions) is what turns a return into a landing. **EXPECTED:** the hub files the audit, then hands you TWO msg files + census cards, in order. **REPORT BACK:** nothing further until Act 7's paste arrives.

### Act 7 — commit + push FIX-1a (your hands; ≤5 min; the exact census card + msg-file path arrive with the audit — the shape is fixed now)
**WHAT:** ONE commit in `homesynapse-core` of exactly FIX-1a's files (9 = 7 M + 2 A per the instruction; the audit's card is authoritative if the lane declared a deviation), from the hub's msg file; then push; then read CI. **WHY:** this push is SAMPLE #4 — the first `main` run that reports every failing task (`--continue`), per-method XML, full assertion messages, and the new `bus.delivery_anomaly` WARN tokens. Whether it is green or red, it is the first self-describing run; it does NOT clear the gate (only FIX-1b's does).
```bash
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
git log -1 --format=%h                  # EXPECT: dc3328b
git status --porcelain | wc -l          # EXPECT: the card's N — anything else: STOP and paste `git status --porcelain`
# the `git add` line arrives with the card (exact paths; never `git add -A .`)
git diff --cached --name-status | wc -l # EXPECT: N
git commit -F ../_scratch/<the msg file the hub names>
git push origin main
```
(No attribution trailers on your commits — your standing directive.) **EXPECTED:** the push prints `dc3328b..<sha>  main -> main`; Actions starts `CI` (and `install-smoke` only if a matching path changed — FIX-1a touches none, so likely not; `Frontend` no). **THEN READ CI (~5 min later):** GREEN or RED, and if RED the `… FAILED` lines (now possibly more than one, by design). **REPORT BACK:** `FIX-1a pushed <sha> · CI <green | red: <the FAILED lines> | pending>`.

### Act 8 — commit + push FIX-1b = THE GATE (your hands; ≤5 min; then the samples)
**WHAT:** the second commit, exactly FIX-1b's census from its card; push; read CI. **WHY:** its green is the clearance of record — `main` green for a reason, with the mechanism named in the return's §1 table. Then, if your word was `SAMPLES: veto-only`: Actions → `CI` → **Run workflow** (the button exists once FIX-1a is on `main`) → branch `main` → run it **3 times**, reading each. **A red sample re-opens the gate** (the hub reads its XML — the next instrument); three greens add nothing to the clearance the push run already gave — they can only take it away. (Same commands as Act 7 with FIX-1b's N and msg file; `git log -1` EXPECTs FIX-1a's sha.) **REPORT BACK:** `FIX-1b pushed <sha> · CI <green | red: …> · samples <3/3 green | red on #k: <the FAILED line>>`. On green: CG-1/2/3 dispatches (the hub has the instruction drafted ahead).

### Act 9 — push the hivemind after every hub beat (≤1 min each; `~/Desktop/Code/ClaudeFolder/nexsys-hivemind`)
```bash
git log --oneline -1 | cut -c1-70; git rev-list --count origin/main..HEAD; git push origin main
```
**EXPECTED:** the count = the beats since your last push (1 after beat 1); the push ends `2e3f733..<sha>  main -> main` (then the new sha next time). **REPORT BACK:** `pushed <sha>`. Tonight: once, after this beat.

### Act 10 — Saturday morning: the 09-05 nightly digest line (≤1 min; read-only; s31 HANDS OFF)
**WHAT:** paste the nightly's one-line digest (it fires ~03:30 CT on the bench card; the 09-03 and 09-04 nights read `8/9`). **WHY:** the bench floor is the corpus's truth engine; the hub banks the line and touches nothing (the fence holds until R-5). **REPORT BACK:** `nightly 09-05: <the line>`.

### Act 11 — Monday 09-07, evening: Erik (your words)
No nudge over Labor Day (your call, banked). Monday evening you email; if you want a draft, ask the hub Monday and it hands you one here. **REPORT BACK:** `Erik: sent` (or his reply, whole).

### Later, on the words — the hub authors ahead so you never wait on it:
- **CG-1/2/3** (the contract-gap batch, one core lane) — dispatches ONLY on FIX-1b's green (Act 8); the hub drafts the instruction while the FIX-1 lane runs; you paste one line.
- **THE BEYOND INPUT** (docket Row 26; your `BEYOND: at-C-002`) — hub-authored this weekend at `context/strategy/2026-09-0x_post-MVP-horizon_strategy-card-INPUT.md`; you read it when it lands and give words at a sitting; nothing adopts until then.
- **The FE fast-follow** (after CG) · **the H8 real-wire packet** (Sun/Mon; a navigator prompt if you want a session) · **the docs correction block** (`homesynapse-core-docs`, your hands; one msg file + card) · **the P-1 bench-row and F-R4-1b charters** (after CG).
- **E1** (EU Annex I via op.europa.eu, Mon) · **09-09 the Apple one-liner** (the hub hands the paste) · **09-11 `EU: ship|defer`** · **09-15 `Activate: apply|hold`** · **09-17 Silabs** · **09-18 the brand hard stop** · **10-01 the quarterly gate check** · **10-31 the rename-slip fallback**.

## §WHAT YOU DO NOT DO (tonight or this weekend)
Re-run any `main` CI job to "see if it goes green" (a sample can veto, never grant — Act 8 is the only sanctioned shape) · open a second core lane while FIX-1 runs · touch s31 or the nightly · use the candidate name anywhere public · grade names in chat · stage or commit in `homesynapse-core` except exactly Acts 7–8 from the hub's cards.

## §IF YOU HAND THIS TO ANOTHER CLAUDE SESSION
Give it this file whole plus `context/audits/2026-09-04_v63-b1_boot-grounding_executive-model-and-intake.md`. Tell it: the state of record is `pm-handoff.md` line 8 + the newest three beat blocks + `PROJECT_SNAPSHOT.md`; the hub's rulings above are REVERT-able by you and no one else; it should not re-derive what those files carry, and it should say "not in the files" rather than fill a gap.
