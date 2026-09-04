<!--
file: context/handoff/2026-09-03_v62_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF for the v62 session — every act he is asked to perform, in order, FULLY ARTICULATED (his standing directive, 2026-09-03). Each act carries WHAT · WHY · HOW (the exact command or paste) · EXPECTED RESULT · REPORT BACK. Supersedes the v61 brief in place.
audience: Nick
state-type: operator brief
status: LIVE at v62 beat 4 (Fri 2026-09-04, instrument ~12:4xZ = 07:4x CT) — revised whole on FAILCHAN's return (ACCEPT-WITH-RULINGS; the commit block is §A) and on Nick's word "R-4b: Friday — the whole day". The four-day plan (§0-ter) shifts one day earlier: Fri R-4b · Sat CG → FE · Sun/Mon H8 + the menu. The spine (pm-handoff newest beat) outranks this file if they disagree.
-->

# Operator brief — what Nick does, in order (v62, beat 4 — THE DAY: Friday 09-04)

## §0 Banked, and today's shape (no action)
- **DONE:** the hivemind push `d66eeed..f0ee4ee` (in sync) · the FAILCHAN lane RETURNED and AUDITED — **ACCEPT-WITH-RULINGS** (R1 ACCEPT: `homesynapse.yaml` is the real root document; R2 ACCEPT: the 19th file is the §10-M ruling comment the instruction itself prescribed — the hub's Files-table miss). The audit: `context/audits/2026-09-04_FAILCHAN_intake_two-layer-audit_v62-beat-4.md`.
- **TODAY, in order:** §A commit + push FAILCHAN (≤5 min) → CI runs (~20–30 min: Build & Check + install-smoke on two architectures) while the hub authors the R-4b packet → §B the R-4b hardware session (~3 h) on whichever artifact guard 1 selects → midday: §C Erik's nudge if silent → afternoon: the R-4b audit; C-002 mints on four-of-four → §D the CG-1/2/3 Core lane if hours remain (else Saturday). **Guard 1, re-keyed to today:** the FAILCHAN artifact rides R-4b only if BOTH CI legs are GREEN before the packet's install step; otherwise the packet installs `ef02d13`'s artifact — the packet carries both paths, you choose by one glance at Actions. **Guard 2:** any R-4b Core defect takes the next core-tree slot before CG. **Guard 3:** the afternoon is a menu — the audit first.

## §A NOW — commit + push FAILCHAN (your hands; ≤5 min)
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
