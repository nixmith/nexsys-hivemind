<!--
file: context/handoff/2026-09-02_v61_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF — revised at v61 beat 9 (Wed 2026-09-02 ~23:46 CT) after his second six-part message: the posture ruling ADOPTED; O-2 MEASURED on the held card (closed); the guide endorsed (alignment); E agreed (owed before the next smart-home decision); F-R4-1 RETURNED + AUDITED ACCEPT (his commit is next); W-SKILLS-6 landed (his re-sync is next). Every act Nick performs from here, in order, with the exact command or paste. The spine outranks this file if they differ.
audience: Nick
state-type: operator brief
status: LIVE at v61 beat 9 (supersedes the beat-8 brief in place). The program that orders the sessions: context/planning/2026-09-03_next-sessions_PROGRAM_v62-onward.md.
-->

# Operator brief — what Nick does, in order (revised beat 9)

## Status of what you already did
- **C — the posture ruling: ADOPTED.** Standing law from here: name-independent public work GO · name-dependent private work GO, name-tokenized · public use FENCED to Erik's written opinion. Nothing for you to do until his reply.
- **D — O-2: MEASURED on the held card, CLOSED.** Your run confirmed the hypothesis on the shipped unit (`ExecMainStatus=143 · Result=exit-code · ActiveState=failed` after one clean stop; healthy before; back `active` after reset-failed + start). The FAILCHAN charter authors on it next. **One act it leaves you: put the bench card back in the Pi** (the nightly at ~03:32 CT does not run while `hs-fresh` is in) — unless you want the held card in for R-4b this weekend, in which case say so and the nightly pauses knowingly.
- **B — the guide: recorded as alignment.** The words themselves still come in the Part-5 shape at the sitting (or one line now: `ADOPT-ALL-RECS`, with any overrides).
- **E — agreed:** low priority, but E1 lands before the next smart-home decision (S6 in the program). E2 runs once the bench card is back.
- **F — F-R4-1: RETURNED and AUDITED ACCEPT** at the bytes (`context/audits/2026-09-02_F-R4-1_intake_two-layer-audit_v61-beat-9.md`). Your commit is the next act (§A).

## A. The landing (≈15 min) — core is your hands
**A1. The F-R4-1 commit.** The census card: exactly **13 = 12 M + 1 A**, all under `integration/integration-zigbee/`:
```
M  MODULE_CONTEXT.md
M  src/main/java/com/homesynapse/integration/zigbee/CoordinatorProtocol.java
M  src/main/java/com/homesynapse/integration/zigbee/EzspCoordinatorProtocol.java
M  src/main/java/com/homesynapse/integration/zigbee/PendingInterviewQueue.java
M  src/main/java/com/homesynapse/integration/zigbee/ZclIngestionUnit.java
M  src/main/java/com/homesynapse/integration/zigbee/ZigbeeAdoptionSlice.java
M  src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationAdapter.java
M  src/test/java/com/homesynapse/integration/zigbee/EzspProtocolTest.java
M  src/test/java/com/homesynapse/integration/zigbee/FixtureReplayTest.java
M  src/test/java/com/homesynapse/integration/zigbee/PendingInterviewQueueTest.java
M  src/test/java/com/homesynapse/integration/zigbee/ZclIngestionUnitTest.java
M  src/test/java/com/homesynapse/integration/zigbee/ZigbeeTrustCenterJoinTest.java
A  src/test/java/com/homesynapse/integration/zigbee/ZigbeeInterviewOnRejoinTest.java
```
```bash
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
git status --porcelain          # must show EXACTLY the 13 lines above (12 " M", 1 "??") — anything else: STOP and paste it to me
git add integration/integration-zigbee
git diff --cached --name-status | wc -l      # must print 13
git commit -F ../_scratch/2026-09-02_core_F-R4-1_commit-msg.txt
git push origin main
```
Paste the push line, then the CI run URL + verdict (Build & Check + install-smoke). Never re-run `main` as a fix — a red comes back to me as the URL.

**A2. The two hub pushes** (already committed by me; batches fine):
```bash
cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind && git push origin main
cd ~/Desktop/Code/ClaudeFolder/nexsys-skills && git push origin main
```
**A3. The skill re-sync (Check 9).** The three role skills were rewritten (W-SKILLS-6). Re-sync the three source folders to your Claude account exactly as before: `nexsys-hivemind/project-manager/` → `nexsys-project-manager` · `nexsys-hivemind/coder/` → `nexsys-coder` · `nexsys-skills/orchestrators/nexsys-frontend/` → `nexsys-frontend`. The three proposal cards in this chat carry the same SKILL.md bytes, but the `references/` folders gained a file each — the folder sync is what makes them whole. Tell me "synced" and I verify byte-identity at the next beat.

**A4. The bench card back in the Pi** (see D above) — then E2 whenever convenient:
```bash
ssh pi
/usr/bin/hostname                      # must print hs-dev-1
/usr/bin/tail -n 5 ~/hs-bench/digests/nightly.log
```

## B. The words — read the guide, then answer in one message
`context/planning/2026-09-02_R10-sitting_DELIBERATION-GUIDE_for-Nick.md`. Then:
```
STRATEGY: R-1 <a|b|c|d> · R-2 <a|b|c> · R-3 <a|b|c> · R-4 <a|b> · R-5 <a|b>
DOCKET:   ADOPT-ALL-RECS                    ← or overrides, e.g.  Row 2 HOLD · Row 12 b
OPTIONAL: TIER-2 GO                          ← B-1 identity starts now, name-tokenized
```
Also lawful: `DELEGATE` · `EDIT Row N: …` · `REVERT <MINT-NARROW|RATIFY|RATIFY-PLAN>`. Row 10 is worded (your dispatch); Row 6's premise is measured (your O-2).

## C. The brand paste loop (≤15 min when it fires)
**C1. Erik's reply →** paste it in full; I key it to the tree and hand you the go-ahead email from disk the same day (RS-9 §A attached; the grade order: VERDO.AI · DOMOTZ's cl. 42 vs ours · MORDOMO · EU VERDO · EU Linea 2000 DOMO · the exclusions · the translation statement · Domo consent as fallback).
**C2. No reply by Fri 09-04 midday →** send the one-line nudge (edit freely): *"Hi Erik — a quick follow-up on Wednesday's note (the VERDOMO comprehensive: the written summary, fee/turnaround, whether a knockout tier makes sense, and the filing shape). Whenever you have a moment this week. Thanks — Nick."* Then tell me "nudge sent" + time.
**C3. Fences (no act):** no public VERDOMO use; no .com before the opinion; no handles; hard stop Fri 09-18.

## E. The two once-asked items (I will not re-ask)
**E1. The Annex I paste (≈1 min) — before the next smart-home decision.** Open https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng → scroll to "ANNEX I" → copy PART A and PART B (the numbered lists) → paste them into the chat with today's date. **E2.** §A4 above.

## F. The next lanes (≈10 min of your time per landing)
**F1.** After A1's CI is green, I author S2 (the FAILCHAN instruction + the PKG-SEC-2 dispatch line as ONE evening Coder lane, the R-4b packet, the CG instruction) and hand you the one-paste dispatch line — same shape as F-R4-1's: *"Execute `<instruction path>`. §0 is RULED: <word>. Tests first. Commit NOTHING. File the return at `nexsys-hivemind/context/audits/<today CT>_<WU>_return.md`."* Each landing = my audit → your commit from my msg file → the CI verdict.
**F2. R-4b — Sat/Sun 09-06/07, ~3 h, weekend-anchored:** the held card with the CI-built F-R4-1 artifact; the four-of-four; I navigate from the packet. Tell me which day.

## G. Dated
**Fri 09-04 midday** the nudge (C2) · **09-07** SCITT (mine) · **09-09** after the Apple event: one line on what (if anything) was announced about home actuation / agents / a confirmation mechanism · **09-18** the brand hard stop.

## H. What you never need to do
Grade a name in chat · write a commit message · stage hivemind/skills files · re-run CI on main · answer E1/E2 twice · re-run O-2.
