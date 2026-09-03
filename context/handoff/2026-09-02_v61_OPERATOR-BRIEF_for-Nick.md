<!--
file: context/handoff/2026-09-02_v61_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF at the v61 hub's beat 7 (Wed 2026-09-02 ~20:16 CT) — every act Nick performs from here to the R-10 sitting and through week 2, in order, with the exact command or paste and what to paste back. Written on Nick's ask ("ensure any and all instructions or commands I need to follow are clearly and fully articulated"). The spine (pm-handoff newest block) outranks this file if they ever differ.
audience: Nick
state-type: operator brief
status: LIVE at v61 beat 7. Superseded by the next brief the hub writes.
-->

# Operator brief — what Nick does, in order

## A. Tonight (≈5 minutes)
**A1. Push the hivemind** (7 hub commits since your last push; more may follow — push whenever, batches are fine):
```bash
cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind
git status
git push origin main
```
Expected: `nothing to commit, working tree clean` and a line like `34137aa..<newest> main -> main`. **Paste the push output back** (I bank the push state at the next beat).

**A2. (Optional, 10–15 min of reading, for the sitting):** the strategy card `context/strategy/2026-09-02_v61-b2_strategy-beat_card_convergence-flip-arc.md` (§0 is the five-word table) and the docket cards `context/planning/2026-09-02_R10-docket_ruling-cards_v61-b3.md` (sixteen rows; each ends with what it buys the household / the company). Nothing to do but read.

## B. The words — at the sitting (Fri–Sat 09-05/06) or any time earlier
Answer in this exact shape (one message; I parse it and splice every ruling into the plan, the OR register, and strategy v1.2):
```
STRATEGY: R-1 <a|b|c|d> · R-2 <a|b|c> · R-3 <a|b|c> · R-4 <a|b> · R-5 <a|b>
DOCKET:   ADOPT-ALL-RECS            ← or per-row overrides, e.g.  Row 5 HOLD · Row 12 b · Row 13 a′
```
Lawful alternatives: `DELEGATE` (the beat-1 form — I decide on the V/C/I frame and record it) · `EDIT Row N: …` · `REVERT <MINT-NARROW|RATIFY|RATIFY-PLAN>` if you disagree with any of the three words I decided by your delegation at beat 1 (zero cost; the register row goes RETIRED, never deleted). The recs are in bold in each card; you never need to restate them.

## C. The brand paste loop (≤15 min whenever it fires)
**C1. Erik's reply:** when it lands, **paste it in full** into the chat, headers and all. I key it to the decision tree (assessment §4) and hand you the go-ahead email from the file on disk (§5) the same day. No grading in chat, no new names in chat.
**C2. No reply by Fri 09-04 midday:** send the one-line nudge. Draft (edit freely; it is yours):
> *Hi Erik — a quick follow-up on Wednesday's note (the VERDOMO comprehensive: the written summary, fee/turnaround, whether a knockout tier makes sense, and the filing shape). Whenever you have a moment this week. Thanks — Nick.*
Then tell me "nudge sent" + the time.
**C3. RS-9:** nothing to do. When the lane returns, tell me "RS-9 returned" — I verify the file on disk and run its one audit beat. Its counsel appendix goes to Erik with or after the go-ahead, on my card.
**C4. Fence reminders (no act):** no public use of VERDOMO anywhere; no .com purchase before the written opinion; counsel hears a candidate only at commissioning. Hard stop for the whole name program: Fri 09-18.

## D. The held card — O-2 (≈5 minutes, whenever the HELD card next powers; before Saturday if convenient)
Open `context/handoff/2026-09-02_O2_held-card_next-boot_operator-card.md` and run its three paste blocks in order on the **HELD card** (the R-4 rig card — **not** the bench card; s31/nightly stay hands-off until R-5). **Paste back all the ⏺ values either way** — the Block-2 reading (`ExecMainStatus`/`Result` after one clean stop) is the measured premise the FAILCHAN charter (Row 6) is written on; a "0 / success" reading is as valuable as "143 / exit-code".

## E. Two standing items — once, no rush, and I will not re-ask
**E1. The Annex I paste (W-C6 → [VERIFIED], ≈1 min):** open EUR-Lex CELEX 32023R1230 (Regulation (EU) 2023/1230), copy **Annex I Parts A and B verbatim**, paste into the chat with the access date. I file it; the lane could not fetch it (418).
**E2. The bench floor:** paste the newest bench-floor line (`[PASS] n/9` or `[FAIL] …`) from wherever you read it. Read-only — no action on the bench card.

## F. Week 2 — the Coder lanes (after the words; each ≈10 min of your time per landing)
**F1. Dispatch F-R4-1 first** (it proves the loop). Host-side Claude Code session in `homesynapse-core`, the `nexsys-coder` skill loaded, targeted gradle allow-listed. Paste this one line:
> *Execute `nexsys-hivemind/context/instructions/2026-09-02_coder-lane_F-R4-1_interview-on-rejoin_coding-instruction_RULING-SLOTTED.md`. §0 is RULED: (a). Tests first. Commit NOTHING. File the return at `nexsys-hivemind/context/audits/<today CT>_F-R4-1_return.md`.*
When the lane says done, tell me "F-R4-1 returned". I audit at the bytes and hand you **the msg file + the census card** (N files, named).
**F2. Your commit (CORE IS YOUR HANDS):**
```bash
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
git status --porcelain            # must match the census card EXACTLY (count + paths); if not, STOP and paste it to me
git add <the exact paths from the card>
git commit -F ../_scratch/<the msg file I name>
git push origin main
```
Paste the push line. Then **relay the CI verdict** when the run finishes (the run URL + green/red) — it banks as one spine line (law 16). Never re-run main as a fix; a red run comes back to me.
**F3. Then PKG-SEC-2** the same way, with `§0 is RULED: (a′)` in the dispatch line (`…_PKG-SEC-2_zigbee-schema-admission_coding-instruction_RULING-SLOTTED.md`).
**F4. The CG batch, FE-STATE-DIALECT, and the H8 real-wire exercise** — I author those instructions next (the v62 session if this one closes first); you dispatch on the same one-line shape when I hand you each.

## G. Dated pastes
**09-09 (Wed) after the Apple event:** tell me in one line what, if anything, was announced about home actuation, agents, or a confirmation/policy mechanism — I execute the §9-2 paste from the pre-ruling file. **09-07 SCITT** and the IFA watch I read myself; no act from you.

## H. What you never need to do
Grade a name in chat · write a commit message · stage hivemind or skills files (hub-run) · answer a question twice (the Annex paste and the bench floor were asked once, here) · re-run CI on main.
