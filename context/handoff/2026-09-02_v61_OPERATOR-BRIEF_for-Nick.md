<!--
file: context/handoff/2026-09-02_v61_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF — revised at v61 beat 8 (Wed 2026-09-02 ~21:20 CT) after his Parts A–F: the push BANKED; RS-9 intaken (audit + the confidence/posture ruling); O-2 adjudicated (wrong card — harmless — now R-4b step 0); Part B answered by the deliberation guide; Part E explained plainly; Part F confirmed (the dispatch IS the Row-10 word). Every act Nick performs from here, in order, with the exact command or paste. The spine outranks this file if they differ.
audience: Nick
state-type: operator brief
status: LIVE at v61 beat 8 (supersedes the beat-7 brief in place).
-->

# Operator brief — what Nick does, in order (revised beat 8)

## Status of what you already did
- **A — the push: BANKED** (`34137aa..e9cb9a1`, 8 commits; origin in sync). Push again whenever; batches fine.
- **RS-9: RETURNED and AUDITED** (ACCEPT-WITH-NOTES; `context/audits/2026-09-02_RS9_intake_two-layer-audit_v61-beat-8.md`). Nothing for you to do: its counsel appendix rides WITH the go-ahead email on Erik's quote.
- **D — O-2: ran on the wrong card, harmlessly.** `ssh pi` = `hs-dev-1` = the BENCH card, where the systemd unit does not exist (the bench runs via `~/bench.sh`); every command failed with "not loaded/not found" and changed nothing. My defect — the card named "the held card" without its address. The held card is `nick@hs-fresh.local`, a SEPARATE SD card physically swapped into the same Pi. **Do NOT swap cards tonight:** the measurement the FAILCHAN charter needed (exit 143 on SIGTERM) is already on record from R-3a and is explained at source, so O-2 is now step 0 of R-4b's packet — it rides the next planned swap.
- **F — the F-R4-1 dispatch: CONFIRMED.** Pasting the dispatch line with "§0 is RULED: (a)" IS your Row-10 word; recorded as such. Nothing else in that instruction waits on the sitting.

## B. The words — read the guide, then answer in one message
`context/planning/2026-09-02_R10-sitting_DELIBERATION-GUIDE_for-Nick.md` walks every decision in plain language: what it is about, the rec and why, what changes if you choose otherwise, where I am unsure. Then:
```
STRATEGY: R-1 <a|b|c|d> · R-2 <a|b|c> · R-3 <a|b|c> · R-4 <a|b> · R-5 <a|b>
DOCKET:   ADOPT-ALL-RECS                    ← or overrides, e.g.  Row 2 HOLD · Row 12 b
OPTIONAL: TIER-2 GO                          ← B-1 identity starts now, name-tokenized (see C)
```
Also lawful: `DELEGATE` · `EDIT Row N: …` · `REVERT <MINT-NARROW|RATIFY|RATIFY-PLAN>`. Row 10 is already worded by your dispatch.

## C. The brand paste loop (≤15 min when it fires) — and the assumed-name posture
The ruling on your Part C is at `context/strategy/brand-program/2026-09-02_VERDOMO_post-RS9_confidence-and-public-posture_ruling.md`. In one line: act as if the name is VERDOMO for everything that stays inside; put it on nothing a stranger can see until Erik's written opinion. Three tiers: name-independent public work — GO now · name-dependent PRIVATE work — GO now, name-tokenized (B-1 may start early on your `TIER-2 GO`) · PUBLIC use, handles, the .com, the repo rename — FENCED until the opinion.
**C1. Erik's reply →** paste it in full; I key it to the tree and hand you the go-ahead email from disk the same day (now with RS-9's §A attached and the grade order: VERDO.AI · DOMOTZ's cl. 42 vs ours · MORDOMO · EU VERDO · EU Linea 2000 DOMO · the exclusions · the translation statement · Domo consent as fallback).
**C2. No reply by Fri 09-04 midday →** send the one-line nudge (edit freely): *"Hi Erik — a quick follow-up on Wednesday's note (the VERDOMO comprehensive: the written summary, fee/turnaround, whether a knockout tier makes sense, and the filing shape). Whenever you have a moment this week. Thanks — Nick."* Then tell me "nudge sent" + time.
**C3. Fences (no act):** no public VERDOMO use; no .com before the opinion; no handles; hard stop Fri 09-18.

## E. Two standing items, explained plainly (once; I will not re-ask)
**E1. The Annex I paste (≈1 min; LOW priority).** Background: one of our adopted positions (W-C6) says the EU Machinery Regulation (EU) 2023/1230 is the legal carrier that makes a deterministic safety floor the cheaper conformity path from 2027-01-20, because ML-based safety functions land in its Annex I and draw notified-body assessment. The research lane confirmed the articles but could not fetch the ANNEX I text (the site blocked it), and my fetch truncates before the annexes. To close the last gap we want the annex VERBATIM. **Do:** open https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng in your browser → scroll to "ANNEX I" → copy PART A and PART B (the numbered lists) → paste them into the chat with today's date. That is all.
**E2. The bench floor (≈30 s, read-only).** Background: the bench card runs a nightly test suite; its verdict line is the "floor" (e.g. `[PASS] 8/9`). We track it; it has not been relayed since 09-01. **Do:**
```bash
ssh pi
/usr/bin/tail -n 5 ~/hs-bench/digests/nightly.log
```
Paste the output. Touch nothing else on that card (s31/nightly are hands-off until R-5).

## F. Week 2 — the Coder lanes (≈10 min of your time per landing)
**F1. F-R4-1 — DISPATCHED tonight (your word).** When the lane says done, tell me "F-R4-1 returned"; I audit at the bytes and hand you the msg file + the census card.
**F2. Your commit (core is your hands):**
```bash
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
git status --porcelain     # must match the census card EXACTLY — if not, STOP and paste it to me
git add <the exact paths from the card>
git commit -F ../_scratch/<the msg file I name>
git push origin main
```
Paste the push line, then relay the CI verdict (run URL + green/red). Never re-run main as a fix.
**F3. PKG-SEC-2 — dispatch after the words (or now, if you give Row 13 (a′) by dispatch the same way):** *"Execute `nexsys-hivemind/context/instructions/2026-09-02_coder-lane_PKG-SEC-2_zigbee-schema-admission_coding-instruction_RULING-SLOTTED.md`. §0 is RULED: (a′). Tests first. Commit NOTHING. File the return at `nexsys-hivemind/context/audits/<today CT>_PKG-SEC-2_return.md`."*
**F4. Next from me:** the FAILCHAN instruction (its premise is now measured), the CG batch, FE-STATE-DIALECT, the H8 packet — each with the same one-line dispatch shape.

## G. Dated
**09-09** after the Apple event: one line on what (if anything) was announced about home actuation / agents / a confirmation mechanism. SCITT (09-07) and IFA I read myself.

## H. What you never need to do
Grade a name in chat · write a commit message · stage hivemind/skills files · swap SD cards for O-2 alone · answer E1/E2 twice · re-run CI on main.
