<!--
file: context/handoff/2026-09-03_v62_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF for the v62 session — every act he is asked to perform, in order, FULLY ARTICULATED (his standing directive, 2026-09-03: "ensure that any/all instructions specifically for me are explicit and fully articulated"). Each act carries WHAT · WHY · HOW (the exact command or paste) · EXPECTED RESULT · REPORT BACK (the exact line to paste to the hub). Supersedes the v61 brief in place.
audience: Nick
state-type: operator brief
status: LIVE at v62 beat 2 (Fri 2026-09-04, instrument 02:xxZ = Thu ~21:xx CT) — revised whole on THE WORDS (given 09-03 ~20:40 CT; the record: context/strategy/2026-09-04_R10-sitting_THE-WORDS_ruling-record.md) and on his four-day plan, ADOPTED as the plan of record for 09-03..09-07 with the hub's three guards (§0). Revised again at beat 3 (the FAILCHAN dispatch line) and beat 4 (the R-4b packet path). The spine (pm-handoff newest beat) outranks this file if they disagree.
-->

# Operator brief — what Nick does, in order (v62, beat 2 — the four days)

## §0 Banked, and the three guards on your plan (no action)
- **DONE:** the hivemind push `5ce1f72..d66eeed` · CI GREEN on `ef02d13` (the PKG-SEC-2 gate closed) · skills 28/28 · **THE WORDS** — strategy **v1.2 RATIFIED** (R-1 b · R-2 b · R-3 b · R-4 a · R-5 a); the docket **RULED** at ADOPT-ALL-RECS with your two EDITs (Row 2 · Row 12); TIER-2 GO; EXITCODE a · FOP-DATES a · ORPHANS a — all spliced at beat 2. §F of the old brief was a FUTURE act (the docs commit arrives as a block later); your `git status` there was correct and nothing was owed — no error on your side.
- **Your four-day plan is ADOPTED as the plan of record (the September plan §0-ter) with three guards, each a STOP-gate, not a doubt:** (1) **the FAILCHAN free rider is decided by CI, not by hope** — Saturday's artifact is the FAILCHAN commit's only if its CI is GREEN by Sat 08:00 CT; otherwise R-4b installs `ef02d13`'s artifact (the packet names both paths; you choose by one glance at Actions). (2) **Sunday's core-tree slot yields to any R-4b Core defect** — if criterion 0 misses or the audit finds a Core fault, the fix WU takes Sunday morning and CG shifts to the evening or Monday; the FE fast-follow never runs on a tree with an unlanded Core fix. (3) **Monday is a menu, not a commitment** — H8 first (it converts FE-HONEST-1 to VERIFIED and rules `sys_*`); the Doc 12/docs commit, the F-S8 charter and the Row 2 dispatch only with hours left; A-14 says every commitment sizes to the floor, and Labor Day is yours.

## §A TONIGHT (Thu 09-03) — launch the FAILCHAN Coder lane (≤5 min of your hands; the lane is the evening)
- **WHAT:** one Coder session on `homesynapse-core` executing the FAILCHAN instruction (Row 6 (a) + EXITCODE (a)): the unit's `Restart=`/`SuccessExitStatus` ruling, the `ExitCode` wiring in `Main` (your caveat: `System.exit(code)` in `main` after `start()` threw and teardown ran — never in a shutdown hook; the exit behind a thin seam so the mapping is unit-tested), the unit-lint assert, and the orderly-path emission classification table (§6-B · §10-O · §10-M · §10-I).
- **WHY:** two boot-honesty defects gone before the hardware session; the unit fix rides Saturday's artifact if CI is green in time.
- **HOW:** the dispatch line is handed at beat 3 (in chat, and as §0 of the instruction file `context/instructions/2026-09-04_coder-lane_FAILCHAN_boot-honesty-sweep_coding-instruction.md`). Paste it into a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core`. **One lane on the core tree: nothing else touches `homesynapse-core` until its return is audited.**
- **EXPECTED RESULT:** the return file exists at the path the instruction names (`context/audits/2026-09-04_FAILCHAN_return.md`); the hub audits two-layer; you commit from the hub's msg file + census card; CI on your push is the gate of record.
- **REPORT BACK:** `FAILCHAN: returned` (then the hub's audit → the commit block) · after your push: `FAILCHAN pushed <sha>, CI <green|red: <run URL>>`.

## §B Fri 09-04 midday — Erik's nudge (≤2 min) — yes, do it, as a reply-in-thread
- **WHAT:** if no reply by midday, one line, sent as a REPLY on your Wednesday email (keeps the thread; lowest pressure).
- **WHY:** the go-ahead fires the same day as his quote; the hard stop is Fri 09-18; Friday-before-Labor-Day means his answer likely lands Tuesday — that is fine, and the nudge makes Tuesday more likely than Thursday.
- **HOW — verbatim:**
  > Hi Erik — a quick follow-up on Wednesday's note (the VERDOMO comprehensive: the written summary, fee/turnaround, whether a knockout tier makes sense, and the filing shape). Whenever you have a moment this week. Thanks — Nick.
- **FENCES (unchanged):** no public VERDOMO use; no .com; no handles; no repo rename; no name grading in chat. TIER-2 GO means only: private, `{{NAME}}`-tokenized identity work may start; the wordmark is the last layer.
- **REPORT BACK:** `Erik: <reply pasted in full below | nudge sent <time>>`.

## §C Sat 09-06 — R-4b on the held card (~3 h; the weekend's highest-leverage hour)
- **WHAT:** install the CI-built arm64 artifact on `hs-fresh`; step 0a SET `permit_join_duration` for the run (absent = no window; the rejoin hook admits only inside one) and remove it after; step 0b pre-validate the held card's `integrations/zigbee.yaml` against the fragment (unknown keys WARN, out-of-range ERROR + key REMOVED, boot continues); then the four-of-four through the rejoin path — **criterion 0 first** (the 0x0061 hop's first ⏺); the evening is the audit; on four-of-four **C-002 mints** and Row 12 closes.
- **THE FALLBACK (your EDIT, Row 12):** if criterion 0 MISSES on Saturday, the announce-class fallback (b) fires THEN — the packet carries the branch; you do not wait for 09-14.
- **HOW:** the navigator packet lands at beat 4 (Friday) at `context/handoff/2026-09-05_R-4b_navigator-packet_held-card.md`: self-contained paste blocks (§8 contract), first line `hostname` must print `hs-fresh`, every criterion pre-checked reachable against the rig census, both artifact paths (§0 guard 1). **Do not start before the packet is on disk.** The bench card goes back afterwards (the nightly runs 03:30 CT on the bench card; a swap DELAYS it — the spine records the shifted stamp).
- **WHAT TO HAVE ON HAND:** the held card + the bench card · ssh to `nick@hs-fresh.local` · the Actions page for the artifact choice (guard 1) · ~3 h with the rig.
- **REPORT BACK:** the packet's own paste-back lines (it names them; each block ends in one).

## §D Sun 09-07 — the dashboard's honesty, sequential on the core tree
- **AM — the CG-1/2/3 Core WU** (Row 14 (a): one v1.1.x additive bump, all three fields): the instruction is authored Friday/Saturday; you launch the Coder lane, the hub audits, you commit + push, CI reads. ≤30 min of hands.
- **PM — the FE fast-follow** (after CG's CI is GREEN): a fresh Cowork FE conversation; the instruction authored alongside CG; you launch, the hub audits, you commit + push. ≤30 min of hands.
- **GUARD 2 applies:** any R-4b Core defect takes the AM slot first.
- **REPORT BACK:** `CG pushed <sha>, CI <verdict>` · `FE pushed <sha>, CI <verdict>`.

## §E Mon 09-07 (Labor Day) — the real-wire day, as a menu
1. **H8 — the real-wire exercise on the clone rig** (~2–3 h): rules `sys_*` (Row 16) and converts FE-HONEST-1's register line from LIVE-VERIFICATION PENDING to VERIFIED. The navigator packet is authored by Sunday evening (path in that beat).
2. **With hours left, in this order:** the docs-repo correction commit (the hub's block: the Doc 12 §3.3 note + the four dangling-reference fixes; ~5 M; your hands) → the F-S8/FE-STATE-DIALECT charter (hub authors; you give one word) → the Row 2 design-note lane dispatch (a fresh Cowork strategy/design conversation; weeks 3–4; no hours of yours beyond the launch line).
- **REPORT BACK:** the H8 packet's paste-back lines; `docs committed <sha>, pushed` if you reach it.

## §F E1 — the Annex I read (BLOCKED by the EUR-Lex outage; re-routed)
- The hub tried both surfaces on 09-04 02:xxZ: WebFetch returns a truncated cached copy (ends at Art. 14); the desktop browser lands on the same outage banner you saw. **The hub retries at every beat** and files the text the moment it loads — you do nothing unless asked.
- **If it is still down on Mon 09-07,** one alternative (≤3 min): https://op.europa.eu/en/web/eu-law-in-force → search `2023/1230` → open the PDF → Annex I (Parts A and B, near the end of the articles) → paste with `E1 Annex I, read <date>` on top. The EU word (`EU: ship|defer`) is due 09-11 on W-C6's closure — a week of slack.

## §G One decision, not blocking — the post-MVP deep-reasoning session(s)
- **Your shower thought is right, and it is chartered now, to RUN at its gate.** The direction "beyond the MVP" is exactly what R-1 (b) just ratified — THE MEASURED CORPUS — and the session is worth far more argued from R-4b's evidence + Erik's quote than from taste this weekend. **Proposed:** STRAT-BEYOND-MVP = two hub-authored strategy beats (read-set: v1.2 · the Substrate Thesis §5–§7 (the unproven ledger + falsifiers) · Doc 16/17/18 §0 · the RS-5 return · the R-4b audit · the FOP §8) producing ONE card in the R-1..R-5 form (the fall/winter arc: corpus → Matter → the agent seams → the fleet), for your words at the R-5 charter.
- **Word:** `BEYOND: at-go-ahead | at-C-002 | now` — **PM rec: at-go-ahead** (Erik's quote → the filing go-ahead; the window 09-12..09-20). **Refutable-by:** the go-ahead slipping past 09-18 (then: at-C-002).

## §H Dated tripwires (the hub watches; you act only where named)
**Fri 09-04 midday** Erik (§B) · **09-04..08** IFA (hub) · **Sat 09-06** R-4b (§C) · **Sun 09-07** CG + FE (§D) · **Mon 09-07** H8 (§E); SCITT CCF LC ends (hub) · **09-09** the Apple one-liner (hub hands the paste) · **09-11** `EU: ship|defer` · **09-14** (no longer the fallback date — Row 12 EDIT) · **09-15** `Activate: apply|hold` · **09-17** Silabs · **09-18 THE BRAND HARD STOP** · **10-01** the quarterly gate check · **10-31** the rename-slip fallback.

## §I What you never need to do
Grade a name in chat · write a commit message · stage hivemind/skills files · re-run CI on `main` · re-run O-2 · touch s31 or the nightly · answer E1 twice · read the whole grounding audit (its §0 suffices) · edit a Locked-doc body · start R-4b or H8 before its packet is on disk.
