<!--
file: context/handoff/2026-09-03_v62_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF for the v62 session — every act he is asked to perform, in order, FULLY ARTICULATED (his standing directive, 2026-09-03). Each act carries WHAT · WHY · HOW (the exact command or paste) · EXPECTED RESULT · REPORT BACK. Supersedes the v61 brief in place.
audience: Nick
state-type: operator brief
status: RETIRED IN PLACE at v63 beat 1 (Fri 2026-09-04, instrument 23:10Z = 18:10 CT) — superseded by context/handoff/2026-09-05_v63_OPERATOR-BRIEF_for-Nick.md (Nick's operator queue; its Act 1 re-issues this file's §CLOSE Act 1 verbatim — the census was not filed at the v62 close). Everything below is the v62 day's history (R-4b DONE four-of-four; C-002 LIVE and STANDS; FAILCHAN on main with CI #225 RED; PR #5 merged → dc3328b, RED on ReplayTransitionIT:212 — banked at v63 beat 1).
-->

# Operator brief — what Nick does, in order (v62 — CLOSED at beat 8; §CLOSE is the only live section)

## §CLOSE (beat 8, Fri ~16:52 CT) — v62 IS CLOSED; five acts, in order (≈12 min of your hands, then v63 takes over)
**Your words are banked** (`C-002: STANDS` · `P-1: charter` → a bench row after CG · `BEYOND: at-C-002` → the post-MVP horizon INPUT this weekend · Erik Monday evening · `0x15ac` = the SNZB-02P). **One thing I could not keep:** the Row 33 entity→device mapping you gave — my context was compacted mid-session and the verbatim line was lost; I did not reconstruct it. You restate it in one line to v63 (act 3's paste has the slot). The same compaction is why v62 closes now: FAILCHAN-FIX-1 must be authored on the census BYTES, and a fresh window holds them whole — so act 1 puts them on disk.

### Act 1 — file the §A2 census to disk (≤3 min; your desktop, the terminal where `~/ci-225/…` lives)
**WHAT:** re-run the census and write it into the hivemind repo as a text file (v63 commits it at its beat 1 — you stage nothing). **WHY:** an instrument a WU authors on is filed at the bytes, never held in chat (a v62 mint). `cd` to your `nexsys-hivemind` checkout first (the directory you push from).
```bash
R=~/ci-225/lifecycle/lifecycle/build/reports/tests/test/classes/com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.html
OUT=context/audits/2026-09-04_CI-225_HeroLoopHardwareFreeIT_stdout-census.txt
test -f "$R" && test -d context/audits && { echo "# CI #225 (run 33875188761) on 7af2d6c — the HeroLoopHardwareFreeIT class report; filed by Nick $(date -u +%Y-%m-%dT%H:%M:%SZ) at the v62 close"; echo; echo "## token census (the §A2 regex)"; grep -oE 'zigbee\.[a-z_]+|lifecycle\.[a-z_]+|integration\.[a-z_]+|automation\.[a-z_]+' "$R" | sort | uniq -c | sort -rn; echo; echo "## <N> journald-prefix count (both raw and HTML-escaped forms)"; grep -cE '^(<|&lt;)[0-9](>|&gt;)' "$R"; echo; echo "## the report's text, last 150 lines (tags stripped)"; sed 's/<[^>]*>//g' "$R" | tail -150; } > "$OUT" && wc -c "$OUT" || echo "STOP: wrong directory or the report is missing — tell v63"
git status --porcelain; ls ~/ci-225/lifecycle/lifecycle/build/test-results/test/ 2>/dev/null | head -3; test -d ~/ci-225/lifecycle/lifecycle/build/test-results/test || echo "no test-results XML in the artifact"
```
**EXPECTED:** `wc -c` prints a few thousand bytes; `git status --porcelain` prints exactly one line `?? context/audits/2026-09-04_CI-225_HeroLoopHardwareFreeIT_stdout-census.txt`; the last line names the XML (`TEST-com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.xml`) or says none is in the artifact (a datum for I-2). **REPORT BACK (to v63):** `census filed (<bytes>) · XML: <present | absent>`.

### Act 2 — DONE (22:0xZ): `f0ee4ee..204c5ba  main -> main`, banked at beat 9.

### Act 2b — push beat 9 (≤1 min; the same directory)
**WHAT/WHY:** beat 9 (post-close) put the dispatch prompt and the PR rulings on disk; the push is yours.
```bash
git log --oneline -1 | cut -c1-60; git rev-list --count origin/main..HEAD; git push origin main
```
**EXPECTED:** the line begins `<sha> hivemind: v62 beat 9 — POST-CLOSE`; the count `1`; the push ends `204c5ba..<sha>  main -> main`.

### Act 2c — I-0 + two words on GitHub (≤4 min; read-only except your two clicks)
**WHAT:** (i) **I-0** — open PR #5 → the **Checks** tab → `Build & Check` → the job → expand the `Run actions/checkout` step → find the line `HEAD is now at … Merge <sha> into <base>` and read the **base** sha. **WHY:** `ci.yml` runs `./gradlew check` on every PR with no path filter, so that green run executed the lifecycle suite — `HeroLoopHardwareFreeIT` included — on the PR's merge ref. If the base is `7af2d6c`, the test PASSED on Java bytes identical to the red run's: the failure is non-deterministic on this tree, which weighs the fix toward branch (a)/(c) and away from a deterministic guard bug (b). **REPORT (in the dispatch slot):** `I-0: into 7af2d6c` | `into <sha>` | `not read`.
(ii) **`PR5:`** — the hub's recommendation is **merge** (a HIGH dev-dep alert closed; the merge commit's own `main` run is a second sample; a sample NEVER clears the gate — only FIX-1's green does; the FIX-1 lane's dispatch will begin `git pull --ff-only`). Your click, your word: `PR5: merged | held`.
(iii) **`PROTECT:`** — the banner. Recommendation **(a)**: Settings → Branches → add a rule for `main` with ONLY "Block force pushes" + "Do not allow deletions" (safe; changes nothing about how you push). **Not** "Require status checks" now — that rejects your direct pushes and forces a PR workflow for every core commit; it is named docket Row 34 for the public-flip sitting. Your word: `PROTECT: a | b | dismissed`.

### Act 3 — dispatch v63 (≤3 min; a FRESH Cowork conversation with the ClaudeFolder connected)
**The copy-source is the file on disk:** open `context/handoff/2026-09-04_v63_dispatch-prompt.md`, fill every ⟨slot⟩ in its STATE AT DISPATCH paragraph (PR5 · PROTECT · the census file · I-0 · Row 33's mapping · I-1 · the nightly), then paste the fenced block WHOLE as the first message. It is the v57 dispatch's shape, re-cut for v63: how to read (a one-screen executive model checked against the documents), how to reason (three horizons), and independent thought as a deliverable (one hub-originated contribution per beat, in ruling form; disagreement with evidence attached).
**EXPECTED:** it boots from the v63 prompt, confirms the five HEADs and the fold grep, writes its executive model and names any document it disagrees with, commits the census file at beat 1, hands you the v63 brief, then authors FAILCHAN-FIX-1 on the file and on source. **This v62 conversation is then retired.**

### Act 4 — Erik (Monday 09-07, evening; your words)
No nudge over Labor Day (your call, banked). Monday evening you email; if you want a draft, ask v63 Monday and it hands you one in the brief. **REPORT BACK:** `Erik: sent` (or his reply, whole).

### Act 5 — OPTIONAL, I-1 (≤5 min, any time before v63's Block 1; read-only)
**WHAT:** in GitHub → Actions → the `Build & Check` workflow, open runs **#169, #183, #206** → the red job → the `Test` step's failure summary. **WHY:** if the same test (`HeroLoopHardwareFreeIT`) with the same message failed before FAILCHAN existed, the red is a pre-existing determinism class (branch a) and the fix WU starts there; if not, FAILCHAN is the suspect (branch b). **REPORT BACK (in act 3's slot):** one line per run: `#183: <test class · the one-line message>`.

## §0 Banked, and today's shape (no action)
- **DONE:** the hivemind push `d66eeed..f0ee4ee` (in sync) · the FAILCHAN lane RETURNED and AUDITED — **ACCEPT-WITH-RULINGS** (R1 ACCEPT: `homesynapse.yaml` is the real root document; R2 ACCEPT: the 19th file is the §10-M ruling comment the instruction itself prescribed — the hub's Files-table miss). The audit: `context/audits/2026-09-04_FAILCHAN_intake_two-layer-audit_v62-beat-4.md`.
- **TODAY, in order:** §A commit + push FAILCHAN (≤5 min) → CI runs (~20–30 min: Build & Check + install-smoke on two architectures) while the hub authors the R-4b packet → §B the R-4b hardware session (~3 h) on whichever artifact guard 1 selects → midday: §C Erik's nudge if silent → afternoon: the R-4b audit; C-002 mints on four-of-four → §D the CG-1/2/3 Core lane if hours remain (else Saturday). **Guard 1, re-keyed to today:** the FAILCHAN artifact rides R-4b only if BOTH CI legs are GREEN before the packet's install step; otherwise the packet installs `ef02d13`'s artifact — the packet carries both paths, you choose by one glance at Actions. **Guard 2:** any R-4b Core defect takes the next core-tree slot before CG. **Guard 3:** the afternoon is a menu — the audit first.

## §R-4b-DONE (beat 7) — FOUR OF FOUR on `ef02d13`; **C-002 IS LIVE**; the bench floor is back `[PASS]`
The record and the audit are on disk; the mint is worded on exactly what rendered (the S31 adopted via the rejoin path in 315 ms; `bench-hero` re-bound and CONFIRMED in 10,051 ms; Path B). The six-device fleet sentence is now the C-003 slot behind F-R4-1b (the ZDO `IEEE_addr_req` WU the miss arm evidenced). **Nothing is public** (G-2; the register is a source, not a surface). Your one word if you disagree with the scoping: `REVERT C-002` (it retires, never deletes).

**What remains TODAY, in order:** (1) §A2 below — the 3-minute token census (still owed; `main` is red and nothing else on the core tree moves before FAILCHAN-FIX-1) · (2) `Erik: <reply | nudge sent>` · (3) `git push origin main` in `nexsys-hivemind` (ahead 4 after this beat) · (4) one word each, any time: `BEYOND:` · `P-1: charter | hold` (the power-harness primitive, your own idea, recorded in full in the record §9). CG moves to tomorrow behind the fix; FE Sat; H8 Sun/Mon.

## §A-DONE — FAILCHAN committed `7af2d6c` and pushed (07:54 CT); **CI #225 RED** (`HeroLoopHardwareFreeIT` — "timed out awaiting the dispatched On frame"; local re-run green after a full clean; prior reds exist in the Actions history). Guard 1 is answered: **R-4b runs on `ef02d13`'s artifact.** `main` is red until the fix lands — no other core lane dispatches before it (the deferred-gate rule); the fix WU is the exception.

## §A2 NOW — the token census from the CI test report (≤3 min; the instrument the fix WU authors on)
```bash
grep -oE 'zigbee\.[a-z_]+|lifecycle\.[a-z_]+|integration\.[a-z_]+|automation\.[a-z_]+' ~/ci-225/lifecycle/lifecycle/build/reports/tests/test/classes/com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.html | sort | uniq -c | sort -rn | head -40
```
Paste the whole output. Then the last 60 lines of the class's standard output: open that `.html` in a browser → the "Standard output" tab → copy the tail → paste. (If the tab is empty, say so — that is a datum too.)
**REPORT BACK:** the census + the tail. The hub hands you `FAILCHAN-FIX-1` within ~30 min of the paste.

## §A3 NOW — dispatch the R-4b NAVIGATOR session (a fresh Cowork conversation with the ClaudeFolder connected; ≤2 min)
Paste this as its first message, verbatim:
```
Boot as the R-4b NAVIGATOR. Read nexsys-hivemind/context/handoff/2026-09-04_R-4b_navigator_session-prompt.md WHOLE and execute its §A–§F exactly; your read-set is its §B, in order; the record you fill is nexsys-hivemind/context/audits/2026-09-04_R-4b_re-rep_operator-record.md. State at dispatch: ARTIFACT = ef02d13's (CI on the FAILCHAN commit 7af2d6c is RED — skip the §5 stop-proof block; §9's stop reads failed/143, the known lie); the BENCH card is in the Pi; the hub session stays open in parallel for any STOP. date -u first. Start me at the packet's §0 and walk me one block at a time.
```
**EXPECTED:** it reads the five files, confirms the state line back to you, and hands you §0/§1. **REPORT BACK (to the hub, only at a STOP or at the close):** `STOP at §X` + the record's §X, or `R-4b record filed`.

## §A-ORIGINAL (executed) — commit + push FAILCHAN (your hands; ≤5 min)
- **WHAT:** ONE commit in `homesynapse-core` of exactly the 19 files the lane produced, from the hub's message file; then push; then read CI.
- **WHY:** CI on your push is the gate of record (the full `./gradlew check` + the install-smoke matrix did not run on the desk); guard 1 needs its verdict before R-4b installs.
- **THE CENSUS CARD — 19 = 14 M + 5 A:**
  ```
  M  .github/workflows/install-smoke.yml
  M  app/homesynapse-app/MODULE_CONTEXT.md
  M  app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java
  M  distribution/ci/install-smoke.yml
  M  distribution/docs/boot-contract-map.md
  M  distribution/smoke/run-smoke.sh
  M  distribution/systemd/homesynapse.service
  M  integration/integration-zigbee/MODULE_CONTEXT.md
  M  integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZclIngestionUnit.java
  M  integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java
  M  integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZigbeeProductionTransportTest.java
  M  lifecycle/lifecycle/MODULE_CONTEXT.md
  M  lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java
  M  lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/SystemLifecycleManager.java
  A  app/homesynapse-app/src/main/java/com/homesynapse/app/ExitCodes.java
  A  app/homesynapse-app/src/test/java/com/homesynapse/app/ExitCodesTest.java
  A  distribution/smoke/unit-directives-test.sh
  A  lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/StartupFailureReport.java
  A  lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreStartupFailureTest.java
  ```
- **HOW (git-bash), verbatim:**
  ```bash
  cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
  git log -1 --format=%h                  # EXPECT: ef02d13
  git status --porcelain | wc -l          # EXPECT: 19  — anything else: STOP and paste `git status --porcelain`
  git add -A .github/workflows/install-smoke.yml app/homesynapse-app distribution integration/integration-zigbee lifecycle/lifecycle
  git diff --cached --name-status | wc -l # EXPECT: 19
  git status --porcelain | grep -v '^[MA] ' # EXPECT: no output (nothing unstaged or untracked remains)
  git commit -F ../_scratch/2026-09-04_core_FAILCHAN_commit-msg.txt
  git push origin main
  ```
  (No attribution trailers on your commits — your standing directive.)
- **EXPECTED RESULT:** the commit lands atop `ef02d13`; the push prints `ef02d13..<sha>  main -> main`; Actions starts three workflows (CI · install-smoke · possibly not Frontend — no `web-ui/` file changed).
- **THEN READ CI (≤2 min, when the runs finish):** the Actions page → the two runs on your sha. **GREEN =** both `Build & Check` and `install-smoke` (amd64 + arm64) passed; in install-smoke's log look for `[unit-directives-test] PASSED ✓ (7 directives)` and `clean stop grades success (Result=success ExecMainStatus=143)`. **RED =** paste the run URL — never re-run `main`; the hub authors a fix WU.
- **REPORT BACK:** `FAILCHAN pushed <sha>, CI <green | red: <run URL> | pending>` — and, if green, the arm64 artifact name from the install-smoke run (`distribution-artifacts-arm64`), which the packet's install step uses.

## §B TODAY — R-4b on the held card (~3 h; the hub navigates live)
- **WHAT:** install the CI-built artifact on `hs-fresh` (guard 1 decides which); step 0a SET `permit_join_duration` for the run (absent = no window; the rejoin hook admits only inside one) and remove it after; step 0b pre-validate the held card's `integrations/zigbee.yaml` against the fragment; then the four-of-four through the rejoin path — **criterion 0 first** (the 0x0061 hop's first ⏺); **the FAILCHAN proof rides for free if its artifact is installed: the first `systemctl stop` must read `inactive`/`success`**; the evening is the audit; on four-of-four **C-002 mints** and Row 12 closes.
- **THE FALLBACK (your EDIT, Row 12):** if criterion 0 MISSES today, the announce-class fallback (b) fires today — the packet carries the branch.
- **HOW:** the navigator packet lands at beat 5 (this morning, while CI runs) at `context/handoff/2026-09-04_R-4b_navigator-packet_held-card.md`: self-contained paste blocks (§8 contract), first line `hostname` must print `hs-fresh`, every criterion pre-checked reachable against the rig census, both artifact paths. **Do not start before the packet is on disk and CI has answered guard 1.** The bench card goes back afterwards (the nightly runs 03:30 CT on the bench card).
- **WHAT TO HAVE ON HAND:** the held card + the bench card · ssh to `nick@hs-fresh.local` · the Actions page · ~3 h with the rig.
- **REPORT BACK:** the packet's own paste-back lines (each block ends in one); the hub audits live between blocks.

## §C Midday — Erik's nudge (≤2 min) — only if silent
- As a REPLY on the Wednesday thread, verbatim:
  > Hi Erik — a quick follow-up on Wednesday's note (the VERDOMO comprehensive: the written summary, fee/turnaround, whether a knockout tier makes sense, and the filing shape). Whenever you have a moment this week. Thanks — Nick.
- Fences unchanged: no public VERDOMO use; no .com; no handles; no repo rename; no name grading in chat.
- **REPORT BACK:** `Erik: <reply pasted in full below | nudge sent <time>>`.

## §D Afternoon or Saturday — the CG-1/2/3 Core lane, then the FE fast-follow
- The instruction is authored after the R-4b packet (beat 6); you launch a Coder lane (≤5 min of hands); the hub audits; you commit + push; CI. **One lane on the core tree** — after FAILCHAN's commit is on `main` and R-4b's audit has cleared the tree (guard 2). The FE fast-follow (a fresh Cowork FE conversation) runs after CG's CI is GREEN — Saturday.
- **REPORT BACK:** `CG pushed <sha>, CI <verdict>` · later `FE pushed <sha>, CI <verdict>`.

## §E Sunday / Monday — H8 real-wire (rules `sys_*`; FE-HONEST-1 → VERIFIED), then the menu
- The H8 navigator packet is authored Saturday; then, with hours left: the docs-repo correction commit (the hub's block: the Doc 12 §3.3 note + the dangling-reference fixes + the three FAILCHAN drift rows — Doc 12 §8.4 `System.exit(1)`, §6.4/§6.6 + LTD-13 `Restart=on-failure`, Doc 12 §9 `config.yaml`) → the F-S8/FE-STATE-DIALECT charter (one word) → the Row 2 design-note lane dispatch (no hours of yours beyond the launch line).

## §F E1 — the Annex I read (BLOCKED by the EUR-Lex outage; the hub retries each beat)
- If still down on Mon 09-07: https://op.europa.eu/en/web/eu-law-in-force → search `2023/1230` → the PDF → Annex I Parts A and B → paste with `E1 Annex I, read <date>` on top. The 09-11 `EU: ship|defer` word rides W-C6's closure.

## §G Words owed (any time, not blocking)
- `BEYOND: at-go-ahead | at-C-002 | now` — the post-MVP deep-reasoning sessions (STRAT-BEYOND-MVP, chartered; PM rec: at-go-ahead, window 09-12..09-20).

## §H Dated tripwires
**Today 09-04:** FAILCHAN CI · R-4b · Erik midday · IFA watch (hub) · **09-05/06** CG → FE · **09-07** H8; SCITT CCF LC ends (hub) · **09-09** the Apple one-liner (hub hands the paste) · **09-11** `EU: ship|defer` · **09-15** `Activate: apply|hold` · **09-17** Silabs · **09-18 THE BRAND HARD STOP** · **10-01** the quarterly gate check · **10-31** the rename-slip fallback.

## §I What you never need to do
Grade a name in chat · write a commit message · stage hivemind/skills files · re-run CI on `main` · re-run O-2 · touch s31 or the nightly · answer E1 twice · read the whole audit (its §0 suffices) · edit a Locked-doc body · start R-4b or H8 before its packet is on disk.
