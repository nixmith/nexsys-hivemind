<!--
file: context/handoff/OPERATOR-BRIEF_for-Nick.md
purpose: Nick's operator brief in THE OPERATOR-LOAD LAW's shape: §NEXT carries exactly ONE act — one paste or one command card, what "done" looks like, the one line he says back; §HELD-BY-THE-HUB carries everything else and is EDITED (by row) every beat by the hub; §DONE is one line per act. STABLE PATH since v66 beat 10 (2026-09-07): one file, edited in place, git history is the past — the boot prompt names this path. Nick reads; he never remembers.
audience: Nick (§NEXT, then nothing until he reports) · the hub (edits §HELD every beat; hands the next act on each report)
state-type: operator queue (the file on disk is the copy-source of record, never a chat card)
status: LIVE — edited at v66 beat 10 (Mon 2026-09-07 ~11:2x CT; instrument 2026-09-07T16:2xZ). HIVE-CLEAN-1 LANDED 30f800d (ACCEPT) · W-SKILLS-8 LANDED 90529d1 + skills c630c5c (ACCEPT-WITH-ONE-RULING) · the v67 prompt re-cut for context · the spine rotated (95 beats → archive). Session: v66 → v67 boots on Act A's report. Supersedes the per-session briefs: the v66 brief's past is this file's git history (git recorded the move as D + A — the rewrite fell under the rename threshold); v65 and earlier live under context/handoff/archive/2026-09/.
-->

# Operator brief (one act at a time)

## §NEXT — Act A: the Git Bash card (everything that is yours before v67 boots; run top to bottom; stop at the first surprise and paste me its LAST line only)
```bash
# 1. hivemind — push the five hub commits (v66 beats 8–10 + the hygiene pair: 68e183b · 7ae6a63 · 30f800d · 90529d1 · this beat's — `git log -1` names it); nothing to stage, the tree is clean
cd /c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind && git status --porcelain | wc -l && git log --oneline -1 && git push
# 2. skills — push the FE half of W-SKILLS-8 (c630c5c)
cd /c/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-skills && git status --porcelain | wc -l && git log --oneline -1 && git push
# 3. docs — BLOCK 6 (the five corrected files are already in your working tree, unstaged — porcelain = exactly 5 ` M`; `git add -u` stages tracked changes only; the card of record: context/handoff/2026-09-06_BLOCK6_docs-correction_operator-card.md)
cd /c/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core-docs && git status --porcelain && git diff --stat | tail -1 && git add -u && git diff --cached --name-status | wc -l && git -c user.name='Nick Smith' -c user.email='nickdsmith1@gmail.com' commit -q -F ../_scratch/2026-09-06_docs_BLOCK6_commit-msg.txt && git log -1 --format='%h %s' | cut -c1-80 && git push 2>&1 | tail -1
# 4. _scratch — the hygiene lane's cleanup (13 stale dirs + 297 files older than 7 days; v66/ and every 2026-09-06_* file are KEPT; the v29-*/v55-* lines are COMMENTED — uncomment them first if you want them gone)
cd /c/Users/Nick/Desktop/Code/ClaudeFolder/_scratch && bash CLEANUP_2026-09-07.sh
```
**5. Re-sync the account skills ONCE** (the Claude desktop app → Skills → re-sync `nexsys-project-manager`, `nexsys-coder`, `nexsys-frontend` from `ClaudeFolder/nexsys-hivemind/{project-manager,coder}` and `ClaudeFolder/nexsys-skills/orchestrators/nexsys-frontend`) — two SKILL.md files changed bytes (the hub's four count-string fixes); Check 9 at v67's boot expects the new md5s.
**Done looks like:** `git push` printed `33f2127..<the sha git log -1 printed>` (hivemind) · `f9c0bf4..c630c5c` (skills) · `a53f474..<sha>` (docs; 5 files); the script printed its removal count; the sync finished.
**One line back:** `pushed: hivemind <sha> · skills c630c5c · docs <sha> · cleanup: done · SKILLS: synced` — then **Act B** (below) is yours whenever you next sit down.

**Act B — dispatch v67** (a FRESH Cowork conversation with `ClaudeFolder` connected): the paste is §3 of `context/handoff/2026-09-06_PM-mission-control_v67_orchestrator_session_prompt.md` with `<N>` = 67 and `STATE AT DISPATCH:` = your Act A line. v67's ONE deliverable is Block 4 (the Erik go-ahead + the one-page RS-10 appendix, due Tue 07:00 CT); it hands TR-1's paste as its first act.

## §HELD-BY-THE-HUB (edited every beat; you read it, you never remember it)
**Lanes (the cap: TWO + your hands; hardware exclusive):**
| Lane | State (v66 beat 10, 16:2xZ) | Next |
|---|---|---|
| HIVE-CLEAN-1 (hygiene) | **LANDED `30f800d`** (188 = 130 R + 55 M + 3 A) · audited ACCEPT · `context/audits/2026-09-07_HIVE-CLEAN-1_intake_two-layer-audit_v66-b10.md` | your push (Act A) |
| W-SKILLS-8 (the ledgers) | **LANDED `90529d1`** (14 = 12 M + 2 A) + skills **`c630c5c`** (4 M) · ACCEPT-WITH-ONE-RULING (the four SKILL.md count strings fixed by the hub; `REVERT SKILL-COUNTS`) · `…_W-SKILLS-8_intake_two-layer-audit_v66-b10.md` | your push + re-sync (Act A) |
| FE-113 · F-R4-1b · TR-0 · HERO-0 · RS-12-F | LANDED `d192d17` · LANDED `39c8dd3` · ACCEPT · ACCEPT · ACCEPT (closed) | — |
| TR-1 (the position census; read-only) | not dispatched | v67 beat 1 hands the paste (the program §5 "TR-1") |
| **H8-a (the rig; EXCLUSIVE)** | packet on disk: `context/instructions/2026-09-06_H8a_real-wire_v113-keys_and_failchan-proof_navigator-packet.md` (+ the record scaffold under `context/audits/`) | **your word `H8: Tue <hh:mm> | tonight`** (default Tue evening); v67 sends the §N paste AT that time; ≤60 min at the rig |
| R-4c (the fleet acceptance; the rig) | after F-R4-1b's artifact (Act 12) | **Sat 09-12** (rec; `R4C: Sat | Sun`) — the coder instruction names it |
| Act 12 — the install-smoke `workflow_dispatch` on `main` | not run | two clicks any day before Sat: Actions → install-smoke → Run workflow → both jobs green = R-4c's `.deb`; one line: `act12: green | red <FAILED line>` |

**v67's blocks, in order (the hub's list, not yours):** Block 4 the Erik go-ahead re-cut + the RS-10 appendix (Tue 07:00) → the honesty-batch coding instruction (LASTREPORTED-1 · ORIGIN-1 · TR0-1; CI-PATHS-1 rides it) → TR-1's audit → FE-NULL-1 (web-ui domain; may run beside the Java lane, D4) → R-4c's instruction (Sat) → the v1.1.4 EXPLAIN batch → the B-7 ADR word (`B7:` / `B7-DOCS:`) → W-SKILLS-9 (the PM ledger split · the F-R4-1 pattern · the FE brand-literal strip · a preflight script — PREFLIGHT-SCRIPT-1).

**Owed lines (one line each, when you have them; none gates Act A):**
- `samples: k/3 <verdicts>` (the three `workflow_dispatch` runs; a red VETOES) · `sample4: green | red: <FAILED line>` (`5ed9178`'s run).
- `act3: <the dc3328b ReplayTransitionIT.html message>` · `nightly 09-05: <line>` · `nightly 09-06: <line>`.

**Open words (asked only when they gate an act):**
- **Today (Monday), one message or none:** the seven recs are ADOPTED PROVISIONALLY (D4) — `REVERT <word>` for any you refuse (`PLAN` · `LANE-LAW` · `F1` · `CLEAN` · `SKILLS` · `MATTER` · `R4C`); add `REVERT SKILL-COUNTS` if you want the literal counts back.
- `PELTON: executed | armed` — the 2026-08-28 same-day card is still ARMED on disk; the hygiene lane skipped it; your word moves it.
- `H8: Tue <hh:mm> | tonight <hh:mm>` — default Tue evening.
- `R4C: Sat 09-12 | Sun 09-13` — before v67 authors the R-4c instruction (rec Sat).
- `SEARCH-NAME:` — provisional VERDOMO; re-given (or not) **Tue 07:00 CT** on the card §3 with the POST-HOC row.
- `ASR-VERDOMU: pass <spellings> | fail` (your phone; RS-9 §6) · `RS10-STAR: <the TSDR sentence>` — **before Tuesday's send**.
- `EU: ship|defer` (09-11) · `Activate: apply|hold` (09-15) — not yet due.

**Given (banked; no act):** `BEYOND-LETTERS: keep` · `DESIGN: hold` until HERO-0 (returned — `DESIGN: start` is lawful when you say it) · `BLOCK6: pull` (in Act A) · `SEARCH-NAME: VERDOMO — provisional` · THE OPERATOR-LOAD LAW · the v66 decisions D1–D7.

## §DONE — the ledger (Sun 09-06 → Mon 09-07)
v66 booted 15:29:56Z → FE-113 dispatched 10:42, LANDED `d192d17` → TR-0 dispatched 10:50, ACCEPT → the H8-a packet on disk 10:53 → the F-R4-1b instruction 11:03 → BLOCK 6 applied to the docs tree 11:12 → HERO-0 ACCEPT; the B-7 ADR; the assessment filed 12:05 → RS-12-F dispatched 13:16, ACCEPT (no displacement) → the rig missed (the hub's) → D1–D7 filed 16:25 → F-R4-1b dispatched 17:19, returned 17:44, ACCEPT, LANDED `39c8dd3` → the v67 stable prompt → HIVE-CLEAN-1 + W-SKILLS-8 dispatched ~10:33 CT Mon, returned ~11:00, audited, LANDED `30f800d` · `90529d1` · skills `c630c5c` → the v67 prompt re-cut for context; the spine rotated (v66 beat 10).

## §WHAT YOU DO NOT DO
Open a second lane on the same core path-domain · take a sample's green as a GRANT · touch s31 or the nightly · `--allow-downgrades` · anything else while at the rig · grade a name in chat · paste a transcript (save it under `_scratch/`, tell me the path) · hold Tuesday's send for RS-12-F.
