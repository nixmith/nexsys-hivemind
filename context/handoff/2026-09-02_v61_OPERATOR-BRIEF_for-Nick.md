<!--
file: context/handoff/2026-09-02_v61_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF — revised at the v61 FINAL CLOSE (beat 10, Thu 2026-09-03 ~06:35 CT) after his 06:12 report: F-R4-1 LANDED on main (a1c6966, CI green); the three pushes banked; the held card shut down, the bench card back; E2 read — the 09-02 nightly BREACHED the floor (7/9, FAIL s31) and the 09-03 nightly was MISSED; the skill cards saved but the folders not re-synced. Every act Nick performs from here, in order, with the exact command or paste. The spine outranks this file if they differ.
audience: Nick
state-type: operator brief
status: LIVE at the v61 FINAL CLOSE (beat 10; supersedes the beat-9 brief in place). The program that orders the sessions: context/planning/2026-09-03_next-sessions_PROGRAM_v62-onward.md. The next hub session boots from context/handoff/2026-09-02_PM-mission-control_v62_orchestrator_session_prompt.md (§D below).
-->

# Operator brief — what Nick does, in order (revised at the v61 final close)

## Status of what you already did
- **F-R4-1: LANDED.** `f519f42..a1c6966` on `main`, 13 files exact, CI green (your read; banked). The deferred `./gradlew check` gate is closed. R-4b is unblocked.
- **The three pushes: BANKED** (`ba4983b` hivemind, `f9c0bf4` skills, `a1c6966` core). One more hivemind push after this close (§E).
- **The cards:** the held card shut down cleanly; the bench card is back and answering (`hs-dev-1`). The nightly missed one night (09-03) while `hs-fresh` was in — recorded, not a defect; tonight's fires normally.
- **E2 — the floor: BREACHED on 09-02.** `7/9 · FAIL command-confirm-s31` after four 8/9 nights. No theory yet: the rule is read the bundle first (§A). The s31/nightly hands-off fence stands — the read is read-only.
- **The skills: half-synced.** You saved the three proposal cards (the SKILL.md bodies are live and byte-identical to the sources) but the references folders were not re-synced: the account copies still lack `references/laws-ledger.md` (PM, Coder) and `references/field-evidence-and-rulings.md` (Frontend), and carry the old `pass-history.md`. Until the folders sync, the skills point at files they do not have (§B).

## A. Launch the s31 evidence read (Claude Code, ~2 min of yours; read-only on the bench card)
From `~/Desktop/Code/ClaudeFolder`, a Claude Code session, one paste:
> Execute `nexsys-hivemind/context/instructions/2026-09-03_evidence-read_s31-nightly-0902_session_prompt.md`. READ-ONLY on the bench card (`ssh pi`) — write NOTHING on the Pi, run no scenario, no systemctl, no restarts. Commit NOTHING. File the return at `nexsys-hivemind/context/audits/2026-09-03_s31-nightly-0902_evidence-read_return.md`.

Tell me "s31 read returned" when it finishes. It may run at the same time as §C — the two touch different trees.

## B. Re-sync the three skill FOLDERS (Check 9) — the cards were not enough
Upload each source folder whole to its account skill, exactly as before: `nexsys-hivemind/project-manager/` → `nexsys-project-manager` · `nexsys-hivemind/coder/` → `nexsys-coder` · `nexsys-skills/orchestrators/nexsys-frontend/` → `nexsys-frontend`. The new files that must appear: `references/laws-ledger.md` (PM and Coder) and `references/field-evidence-and-rulings.md` (Frontend); `references/pass-history.md` updates in all three. Tell me "folders synced"; the next hub session verifies byte-identity.

## C. Dispatch PKG-SEC-2 (Claude Code, core; ~10 min of yours across the landing) — CI is green, so now
Your paste IS the Row-13 word ((a′), the rec — the same form as F-R4-1). From `~/Desktop/Code/ClaudeFolder`, a fresh Claude Code session:
> Execute `nexsys-hivemind/context/instructions/2026-09-02_coder-lane_PKG-SEC-2_zigbee-schema-admission_coding-instruction_RULING-SLOTTED.md`. §0 is RULED: (a′). Baseline: core `main` at `a1c6966` (F-R4-1 landed; where the instruction's line numbers in `integration/integration-zigbee/MODULE_CONTEXT.md` have shifted by its new §F-R4-1 block, report-and-proceed). `date -u` first for every stamp. Tests first. Commit NOTHING. File the return at `nexsys-hivemind/context/audits/<today CT>_PKG-SEC-2_return.md`.

When it says done, tell me "PKG-SEC-2 returned"; the hub audits at the bytes and hands you the msg file + census card; then your commit + push exactly as A1 of the last brief, and the CI verdict.

## D. Boot the next hub session (Cowork) — this one closes with this brief
This session (v61) has run since Wednesday evening and closes at this beat. Open a fresh Cowork conversation with the `nexsys-project-manager` skill and paste:
> Boot v62. Read `nexsys-hivemind/context/handoff/2026-09-02_PM-mission-control_v62_orchestrator_session_prompt.md` whole and execute its §1 exactly; then §8. Nick's standing report: F-R4-1 landed `a1c6966` CI green · the s31 evidence read and PKG-SEC-2 dispatched (returns expected on disk) · the skill folders <synced | not yet>.

Its first authoring (the program's S2): the FAILCHAN instruction, the R-4b navigator packet, the CG instruction.

## E. The hivemind push (whenever; batches fine)
```bash
cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind && git push origin main
```

## F. The words — read the guide, then answer in one message (any time before the weekend)
`context/planning/2026-09-02_R10-sitting_DELIBERATION-GUIDE_for-Nick.md`. Then:
```
STRATEGY: R-1 <a|b|c|d> · R-2 <a|b|c> · R-3 <a|b|c> · R-4 <a|b> · R-5 <a|b>
DOCKET:   ADOPT-ALL-RECS                    ← or overrides, e.g.  Row 2 HOLD · Row 12 b
OPTIONAL: TIER-2 GO                          ← B-1 identity starts now, name-tokenized
```
Also lawful: `DELEGATE` · `EDIT Row N: …` · `REVERT <MINT-NARROW|RATIFY|RATIFY-PLAN>`. Rows 10 and 13 are worded by your dispatches; Row 6's premise is measured.

## G. The brand paste loop (≤15 min when it fires)
**Erik's reply →** paste it in full; the hub keys it to the tree and hands you the go-ahead email from disk the same day. **No reply by Fri 09-04 midday →** the one-line nudge: *"Hi Erik — a quick follow-up on Wednesday's note (the VERDOMO comprehensive: the written summary, fee/turnaround, whether a knockout tier makes sense, and the filing shape). Whenever you have a moment this week. Thanks — Nick."* Then "nudge sent" + time. **Fences:** no public VERDOMO use; no .com; no handles; hard stop Fri 09-18.

## H. Once-asked, still owed
**E1** — the Annex I paste (≈1 min; before the next smart-home decision): https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng → ANNEX I → copy PART A and PART B → paste with today's date. **R-4b** — Sat or Sun 09-06/07, ~3 h; tell the hub which day.

## I. Dated
**Fri 09-04 midday** the nudge · **09-07** SCITT (hub) · **09-09** the Apple one-liner · **09-18** the brand hard stop.

## J. What you never need to do
Grade a name in chat · write a commit message · stage hivemind/skills files · re-run CI on main · re-run O-2 · touch s31 or the nightly · answer E1 twice.
