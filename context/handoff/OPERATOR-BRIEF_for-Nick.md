<!--
file: context/handoff/OPERATOR-BRIEF_for-Nick.md
purpose: Nick's operator brief in THE OPERATOR-LOAD LAW's shape: §NEXT carries exactly ONE act — one paste or one command card, what "done" looks like, the one line he says back; §HELD-BY-THE-HUB carries everything else and is EDITED (by row) every beat by the hub; §DONE is one line per act. STABLE PATH since v66 beat 10 (2026-09-07): one file, edited in place, git history is the past — the boot prompt names this path. Nick reads; he never remembers.
audience: Nick (§NEXT, then nothing until he reports) · the hub (edits §HELD every beat; hands the next act on each report)
state-type: operator queue (the file on disk is the copy-source of record, never a chat card)
status: LIVE — edited at v68 beat 3 (Thu 2026-09-10 ~18:1x CT; instrument 2026-09-10T23:04:06Z). §NEXT = the FE-NULL-1 paste (the second lane, web-ui). HONESTY-1 is running; H8-a defaults Fri 19:00 CT.
-->

# Operator brief (one act at a time)

## §NEXT — the FE-NULL-1 paste (5 minutes; the second lane, beside HONESTY-1)
Open a **FRESH Cowork conversation** with `ClaudeFolder` connected (leave the HONESTY-1 Claude Code session running — the two never touch the same files) and paste this whole block as the first message:
```
date -u first. You are the FE-NULL-1 frontend lane for NexSys/HomeSynapse — boot as the nexsys-frontend skill. Baseline: homesynapse-core HEAD must be 39c8dd3 and `git status --porcelain -- web-ui/dashboard` must be EMPTY (other paths may be dirty — a Java lane is running; never touch them; STOP and report only if web-ui/dashboard is dirty). Execute nexsys-hivemind/context/instructions/2026-09-10_frontend-lane_FE-NULL-1_chain-null-arms_fast-follow_instruction.md exactly: read its §0 contract and §1 read-set first; adjudicate P1–P4 in your §0. Tests first (RED at HEAD as §3 states), then the eight files of §3, then MODULE_CONTEXT. Work only under web-ui/dashboard/; run `npm run verify` there; stage nothing, commit nothing, no git add/stash/checkout; do not write coder-handoff.md. Write nexsys-hivemind/context/audits/<today's CT date>_FE-NULL-1_return.md (≤12 KB, §0 card first). Your last line, in the file and printed: RETURNED <path> <bytes>. You report to the hub.
```
**Done looks like:** the lane acknowledges, prints its `date -u`, and starts reading. **One line back:** `FE-NULL-1: dispatched <hh:mm>`. Whenever either lane finishes, its `RETURNED …` line is the next one-liner; I audit and hand you the landing card (each lane lands separately — no batched pushes).
**Standing default (no act now):** H8-a at the rig **Fri 09-11 19:00 CT** (≤60 min); the navigator paste reaches you at 18:45 CT. Say `H8: <day> <hh:mm>` only to move it.

## §HELD-BY-THE-HUB (edited every beat; you read it, you never remember it)
**Lanes (the cap: TWO + your hands; hardware exclusive):**
| Lane | State (v68 beat 3, 22:55Z) | Next |
|---|---|---|
| **HONESTY-1 (Core Java; slot 1)** | **RUNNING** — launched by Nick Thu ~17:5x CT on `39c8dd3` (core porcelain 0 at 22:55Z; unverified until its return file exists) | its `RETURNED` line → the hub's audit → a scoped landing card (`git add -A` of the Java paths) → CI + install-smoke = the sample; Act 12 retires |
| **FE-NULL-1 (web-ui; slot 2)** | ISSUE-READY (`…/2026-09-10_frontend-lane_FE-NULL-1_chain-null-arms_fast-follow_instruction.md`) | **§NEXT — the paste**; its return → audit → `git add -A web-ui/dashboard` card → `frontend.yml` |
| **Erik — the PALOKI comprehensive search (wait-state)** | packet SENT Thu ~12:00 CT (PDF + DOCX) | his sight-read → his date → the opinion (by 09-18, or his own expedite); `ERIK: <his line>` when it comes |
| TR-1 (the position census; read-only) | **RETURNED ~19:2x CT (12,243 B) · ACCEPT** (`context/audits/2026-09-07_TR-1_intake_two-layer-audit_v67-b5.md`); `TR1-B2 = DRIVER` ruled under DELEGATE | closed; TR-1b (the census ITs + the driver) docketed after HONESTY-1 lands |
| **H8-a (the rig; EXCLUSIVE)** | packet on disk: `context/instructions/2026-09-06_H8a_real-wire_v113-keys_and_failchan-proof_navigator-packet.md` (+ the record scaffold under `context/audits/`) | **default Fri 09-11 19:00 CT** (`H8: <day> <hh:mm>` only to move it); the §N paste is handed at 18:45 CT by a scheduled send; ≤60 min at the rig |
| R-4c (the fleet acceptance; the rig) | after Act 12's `.deb` | **Sat 09-12** (rec; `R4C: Sat \| Sun`) — the coder instruction names it |
| Act 12 — the install-smoke `workflow_dispatch` on `main` | not run — **RETIRES when HONESTY-1 lands** (CI-PATHS-1 makes every push build the `.deb`) | only if HONESTY-1 has not landed by Fri: two clicks (Actions → install-smoke → Run workflow); `act12: green \| red <FAILED line>` |
| **RS-13 (PALOKI — Nick's own clearance lane, Tue 16:35 CT)** | RETURNED 55,600 B · **ACCEPT** (`context/audits/2026-09-09_RS-13_PALOKI_intake_two-layer-audit_and_RULING_v67-b6.md`) | closed; its §A rides the packet |
| HIVE-CLEAN-1 · W-SKILLS-8 · FE-113 · F-R4-1b · TR-0 · HERO-0 · RS-12-F | LANDED + PUSHED (Act A verified at the bytes: `30f800d` · `90529d1` + skills `c630c5c` · `d192d17` · `39c8dd3` · ACCEPT ×3) | closed |

**v68's blocks, in order (the hub's list, not yours; the map: `context/planning/2026-09-10_v68_MOMENTUM-MAP_two-weeks_critical-path-and-Nicks-hours.md`):** the PALOKI packet — SENT (done) → HONESTY-1 dispatched (done) → FE-NULL-1 authored (done; §NEXT dispatches it) → R-4c's instruction (the hub, next) → HONESTY-1's landing audit (after your push; CI + install-smoke = the sample; Act 12 retires) → TR-1b's charter (the census ITs + the driver) → FE-NULL-1's landing (the return → audit → the scoped card) → R-4c's instruction (Sat) → the v1.1.4 EXPLAIN batch → the B-7 ADR word → W-SKILLS-9 (+ the RETURNED-line template sentence · THE WHOLE-PASTE LAW as arc 52 (v)). **RETIRED this beat:** Block 4 / the VERDOMO packet (UNSENT) · NAMING-B (overtaken).

**Owed lines (one line each, when you have them; none gates an act — your word tonight):**
- `samples: k/3 <verdicts>` (the three `workflow_dispatch` runs; a red VETOES) · `sample4: green | red: <FAILED line>` (`5ed9178`'s run).
- `act3: <the dc3328b ReplayTransitionIT.html message>` · `nightly 09-05: <line>` · `nightly 09-06: <line>`.
- `card-gradle: <the first line of ./gradlew --version on the card | absent>` — next time you are at the card (with H8-a or R-4c), not tonight; TR-1b's shape depends on it.

**Open words (asked only when they gate an act):**
- `ERIK: <his line>` — when he replies (sight-read · date · surcharge); verbatim is fine, one line.
- `H8: <day> <hh:mm>` — only to MOVE the default (Fri 09-11 19:00 CT); silence = it stands.
- `REVERT TR1-B2` — only if you refuse the driver-outside-the-format ruling (TR-1 audit §3); silence = it stands.
- `R4C: Sat 09-12 | Sun 09-13` — before v67 authors the R-4c instruction (rec Sat).
- `REVERT EU-DEFER` — only if you refuse the ruling §3's EU line (the EUTM after the US opinion; the Finnish exclusion from the first filing; CN/JP/KR early); silence = it stands. · `Activate: apply|hold` (09-15) — not yet due.

**Given (banked; no act):** `EAR-PALOKI: pass` (Thu) → `SEARCH-NAME: PALOKI` FINAL · the packet SENT Thu ~12:00 CT · the DOMO family RETIRED (your word) · `TR1-B2 = DRIVER` · `EU-DEFER` (provisional) · D4's seven recs STAND · Erik = U.S. only · `BEYOND-LETTERS: keep` · `DESIGN: hold` until HERO-0 (returned — `DESIGN: start` is lawful when you say it; the wordmark waits for the opinion) · `BLOCK6: pull` (LANDED `8262a3c`) · THE OPERATOR-LOAD LAW · the v66 decisions D1–D7.

## §DONE — the ledger (Sun 09-06 → Wed 09-09)
v66 booted 15:29:56Z → FE-113 dispatched 10:42, LANDED `d192d17` → TR-0 dispatched 10:50, ACCEPT → the H8-a packet on disk 10:53 → the F-R4-1b instruction 11:03 → BLOCK 6 applied to the docs tree 11:12 → HERO-0 ACCEPT; the B-7 ADR; the assessment filed 12:05 → RS-12-F dispatched 13:16, ACCEPT (no displacement) → the rig missed (the hub's) → D1–D7 filed 16:25 → F-R4-1b dispatched 17:19, returned 17:44, ACCEPT, LANDED `39c8dd3` → the v67 stable prompt → HIVE-CLEAN-1 + W-SKILLS-8 dispatched ~10:33 CT Mon, returned ~11:00, audited, LANDED `30f800d` · `90529d1` · skills `c630c5c` → the v67 prompt re-cut for context; the spine rotated (v66 beat 10) → Act A run by Nick (five pushes verified; Check 9 28/28; the cleanup) → **v67 booted 23:22:01Z Mon (~18:22 CT)**: the dispatch filed verbatim; Block 4 pulled to tonight by Nick's word; TR-1's paste handed as the one act (dispatched 18:30 CT); 8 blocks rotated (v67 beat 1) → **Block 4 authored + handed** — the Erik go-ahead re-cut for tonight + Appendix B (v67 beat 2, ~18:4x CT) → NAMING-B chartered as one file, gated (v67 beat 3) → the email made ONE paste file on Nick's word; HONESTY-1 authored; the AMD-53 correction on the docs tree (v67 beat 4) → TR-1 returned ~19:2x, audited ACCEPT; the Erik packet built as PDF + DOCX on Nick's second word (v67 beat 5) → **Wed 07:00: the email NOT sent; VERDOMO retired by Nick's word; RS-13 (PALOKI) audited ACCEPT; the ruling filed — proceed, do not skip the search (v67 beat 6) → **v67 CLOSED on context health, 7 beats, no compaction; the stable prompt re-cut in place (arc 52 (v)); the close card handed (v67 beat 7) → **v68 booted 00:04:38Z Thu (~19:04 CT Wed)**: the dispatch + Erik's 09-05 note filed verbatim; the close card's steps 1–3 found NOT RUN (hivemind 7 ahead · docs 1 M · HONESTY-1 unverified) and re-queued as Act 2; the PALOKI packet authored (PDF 8 pp + DOCX + the one paste) and handed with the ear test as its gate; EXPEDITE = the 09-18 date rule (v68 beat 1) → **Thu: the ear test PASSED; Nick sent Erik the packet ~12:00 CT; the momentum map filed; the close card handed whole (v68 beat 2) → **Thu ~17:5x CT: Nick ran the close card (hivemind + docs pushed; the stale lock swept) and launched HONESTY-1; FE-NULL-1 authored and handed as the second lane (v68 beat 3).**

## §WHAT YOU DO NOT DO
Open a second lane on the same core path-domain · take a sample's green as a GRANT · touch s31 or the nightly · `--allow-downgrades` · anything else while at the rig · grade a name in chat · paste a transcript (save it under `_scratch/`, tell me the path) · file or use PALOKI publicly before the written opinion (the .com is yours to buy at your own risk; the plan buys it the day the opinion is clean).
