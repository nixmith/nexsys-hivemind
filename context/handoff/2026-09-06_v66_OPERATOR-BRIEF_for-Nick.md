<!--
file: context/handoff/2026-09-06_v66_OPERATOR-BRIEF_for-Nick.md
purpose: Nick's operator brief in THE OPERATOR-LOAD LAW's shape (his word, 2026-09-06): §NEXT carries exactly ONE act — one paste or one command, what "done" looks like, the one line he says back; §HELD-BY-THE-HUB carries everything else (running lanes under the cap, owed lines, open words, when each becomes due) and is re-printed every beat by the hub; §DONE is the day's ledger. Nick reads; he never remembers.
audience: Nick (§NEXT, then nothing until he reports) · the v66 hub (maintains §HELD every beat; hands the next act on each report)
state-type: operator queue (the file on disk is the copy-source of record, never a chat card)
status: LIVE — re-printed at v66 beat 8, THE v66 CLOSE (Sun 2026-09-06 ~18:12 CT; instrument 2026-09-06T23:12Z). v67 boots on the STABLE prompt (context/handoff/2026-09-06_PM-mission-control_v67_orchestrator_session_prompt.md §3 carries the paste) — dispatch it when you next sit down; it reads THIS brief's §HELD as the state. H8-a is your word `H8: tonight <hh:mm> | Tue` (default Tue). The decisions D1–D7 (DELEGATE; `REVERT <D-n>`) are in context/planning/2026-09-06_v66_SESSION-SYNTHESIS_and_decision-record.md. Acts 1–4 DONE (v66 booted 15:29:56Z · FE-113 dispatched 10:42 CT · the hivemind pushed 7f14059 · TR-0 dispatched 10:50 CT). THE H8-a PACKET IS ON DISK (its act = Act 8 at ~14:50 CT). Supersedes context/handoff/2026-09-05_v65_OPERATOR-BRIEF_for-Nick.md (its §CONTEXT stays a valid state read; its queues are retired).
-->

# Operator brief — v66 (one act at a time)

## §NEXT — the ONE act now
### Act 9 — LAND F-R4-1b (your commit + push; Git Bash — `~/Desktop/Code/ClaudeFolder/homesynapse-core`; one line; wait ≈20 s; then the Actions page)
The audit is filed (`context/audits/2026-09-06_F-R4-1b_intake_two-layer-audit_v66-b8.md`: ACCEPT; both `[REVIEW]`s ruled ACCEPT); the msg file is on disk; no trailers.
```
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core && git status --porcelain | wc -l && git add -u && git diff --cached --name-status | wc -l && git -c user.name='Nick Smith' -c user.email='nickdsmith1@gmail.com' commit -q -F ../_scratch/2026-09-06_core_F-R4-1b_commit-msg.txt && git log -1 --format='%h' && git push 2>&1 | tail -1
```
**Done looks like:** `6` · `6` · a new sha · `d192d17..<sha>  main -> main`; then Actions → **CI (Build & Check)** GREEN (the gate; passive sample 5/20). **STOP** if the first count is not 6. **Your one line back (to v67, or here if this window is still open):** `F-R4-1b: landed <sha> — ci <green|red>`. **Then the next act is the artifact:** Actions → **install-smoke** → **Run workflow** on `main` (both jobs green → the `.deb` R-4c installs; `integration/**` is outside the workflow's push filter, so the push alone builds none).

## §HELD-BY-THE-HUB (re-printed every beat; you read it, you never remember it)
**Running / to run (the cap: TWO + your hands; RAISED by your word today for the five below; hardware exclusive):**
| Lane | Window | State at v66 beat 1 (23:12Z) | The paste lives at | Returns to |
|---|---|---|---|---|
| FE-113 (the v1.1.3 mirror) | — | **LANDED `d192d17`** (frontend GREEN · ci GREEN = passive sample 4/20); VERIFIED on H8-a's B2 | — | — |
| TR-0 the chokepoint census | — | **RETURNED 16:07Z · AUDITED ACCEPT** — B-2 = one line at `CommandRoutingSubscriber:249`; nothing for your hands | — | v66 |
| HERO-0 the null census | — | **RETURNED 16:48Z · AUDITED ACCEPT** (F1 → LASTREPORTED-1 · F2 → FE-NULL-1 · EXPLAIN → the v1.1.4 batch; `DESIGN: start` lawful) | — | v66 |
| RS-12-F the fanciful-domus sprint | — | **RETURNED ≈16:1x CT · AUDITED ACCEPT** — no displacement; the row is on the decision card; Tuesday stands | — | v66 |
| TR-1 the position census | fresh Cowork | Act 10 (after the landing + the artifact act) | the program §5 "TR-1" | v67 |
| W-SKILLS-7 (the ledgers) | fresh Cowork | state UNKNOWN (no card on disk at 23:12Z; skills `f9c0bf4` clean) — tell v66 in one line when you know | the v65 brief Act 4 | v66 |
| **H8-a (the rig; EXCLUSIVE)** | a fresh Cowork window (the navigator) + Git Bash + the two cards | **PACKET ON DISK** — `context/instructions/2026-09-06_H8a_real-wire_v113-keys_and_failchan-proof_navigator-packet.md` (+ the record scaffold `context/audits/2026-09-06_H8a_real-wire_operator-record.md`). **MISSED TODAY (the hub's) — RESCHEDULED on your word `H8: tonight <hh:mm> | Tue`:** at the time you name, v66/v67 sends you the §N paste (a fresh Cowork window); §0 + §1 are desktop work first; ≤60 min at the rig; nothing else opens while you are there | the packet §N | the navigator files the record; you paste ONE line to v66: `H8-a: RETURNED <path> <bytes>` |
| F-R4-1b (coder; the core tree) | — | **RETURNED 17:44 CT · AUDITED ACCEPT** — 6 M on your core tree; **Act 9 = the landing (§NEXT)**; then the install-smoke `workflow_dispatch` (R-4c's artifact); `R4C: Sat 09-12` under D4 | the audit §4/§5 | v67 |

**Your own hands (each ONE act when v66 hands it):** the hivemind push after each hub beat (`git push` in `nexsys-hivemind`; v66 says when — `7f14059..<sha>`) · the ASR test on the redirect candidate (5 min, your phone; RS-9 §6's protocol) → `ASR-VERDOMU: pass <spellings> | fail` · the pane read (3 min) → `RS10-STAR: <the sentence>` (TSDR sn 99144181's "no conflicting marks" sentence, or 99001229's `251 0 251 0`) · your card acts (the 2029 sentences · S7 ≤15 per cell · any veto — ON THE CARD) · **BLOCK 6 — READY:** the edits are already in your docs working tree (5 files; nothing staged); the card `context/handoff/2026-09-06_BLOCK6_docs-correction_operator-card.md` is one command (review the stat · commit with the hub's msg file · push) — v66 hands it AFTER H8-a; report `docs: BLOCK6 landed <sha>`.

**Owed lines (give each when you have it; one line each; no rush unless marked):**
- `samples: k/3 <verdicts>` — the three `workflow_dispatch` runs you fired (this evening; a red VETOES).
- `sample4: green | red: <FAILED line>` (`5ed9178`'s run).
- `act3: <the dc3328b ReplayTransitionIT.html message>` · `nightly 09-05: <line>` · `nightly 09-06: <line>`.
- `W-SKILLS-7: running since <time> | RETURNED <path> <bytes> | not dispatched`.
- Each remaining lane's `RETURNED <path> <bytes>` line as it lands (RS-12-F · TR-1 · F-R4-1b) — the line alone; the hub reads the file.

**Open words (asked only when they gate an act — the fact each needs, and where it comes from):**
- `H8: tonight <start hh:mm> | Tue` — default Tue (the packet is unchanged; if F-R4-1b's artifact exists by then, the navigator may use it — v67 re-cuts guard 1 in one line).
- **Monday, one message** — the seven recs are ADOPTED PROVISIONALLY (D4); send `REVERT <word>` for any you refuse (`PLAN` · `LANE-LAW` · `F1` · `CLEAN` · `SKILLS` · `MATTER` · `R4C`), else nothing — the facts: the assessment §0/§7 and the decision record §3.
- `R4C: Sat 09-12 | Sun 09-13` — due before v66 hands the F-R4-1b instruction (it names the acceptance date); the fact: which day the rig gets 3–4 uninterrupted hours; **rec Sat 09-12** (Sunday stays the fallback).
- `SEARCH-NAME:` — given provisional VERDOMO; re-given (or not) **Tue 07:00 CT** after RS-12-F's row is on the card; the fact: the card §3 with the POST-HOC row.
- `ASR-VERDOMU:` · `RS10-STAR:` — due **before Tuesday's send**; the facts: your phone; the TSDR pane.
- `EU: ship|defer` (09-11) · `Activate: apply|hold` (09-15) — not yet due.

**Given (banked; no act):** `H8: today ~15:00 CT on the packet; fallback Tue evening` · `BEYOND-LETTERS: keep` · `DESIGN: hold — until HERO-0 returns; then from the four empty states outward under the NAME token` · `BLOCK6: pull` · `SEARCH-NAME: VERDOMO — provisional` · THE OPERATOR-LOAD LAW.

## §DONE — today's ledger (Sun 09-06)
CG-123 `f25291b` CI green → the nanoid lock bump `093d5b4` CI green (Dependabot #12 FIXED) → the hivemind pushed `6542ef3..20182e3` → the operator-load law given → the program adjudicated (your edits accepted: H8-a today; all four read-only windows open) → the v66 brief → **Act 1: v66 dispatched and booted (15:29:56Z; zero drift; preflight PASS 11/11; your dispatch text filed verbatim at `context/handoff/2026-09-06_v66_dispatch-text_verbatim.md`)** → Act 2 FE-113 dispatched 10:42 → Act 3 the hivemind pushed `7f14059` → Act 4 TR-0 dispatched 10:50 → **THE H8-a PACKET on disk (v66 beat 2, 10:53 CT — 2 h+ ahead of 13:30)** → the F-R4-1b instruction on disk (v66 beat 3, 11:03 CT) → BLOCK 6 applied to the docs tree + the freeze doc at v1.1.3 (v66 beat 4, 11:12 CT) → FE-113 + TR-0 returned and audited (v66 beat 5, 11:18 CT) → **FE-113 LANDED `d192d17`** (Act 6, 11:25 CT; frontend + ci green) → HERO-0 audited · the B-7 ADR · **THE ASSESSMENT filed** (v66 beat 6, 12:05 CT) → RS-12-F dispatched 13:16, returned, audited (no displacement) → the rig missed (the hub's) → the decisions D1–D7 filed (v66 beat 7, 16:25 CT) → F-R4-1b dispatched 17:19, returned 17:44, audited ACCEPT → **the v66 CLOSE; the v67 stable prompt** (v66 beat 8, ~18:12 CT).

## §WHAT YOU DO NOT DO (today)
Open a second lane on the core tree (FE-113 is it) · take the samples' verdicts as GRANTS (they can only veto) · touch s31 or the nightly · `--allow-downgrades` · anything else while you are at the rig · grade a name in chat · hold Tuesday's send for RS-12-F.
