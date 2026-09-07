<!--
file: context/handoff/2026-09-05_v65_OPERATOR-BRIEF_for-Nick.md
purpose: Nick's operator queue for the v65 session — every act fully articulated (WHAT · WHY · the paste · EXPECTED · REPORT BACK), in dependency order, under a §CONTEXT preamble any helper session can boot from. Re-cut at every beat; the newest §NOW is the live plan.
audience: Nick (executes, in order) · any helper Claude session Nick hands it to (§CONTEXT is self-contained; every line has a path)
state-type: operator queue (hub-authored; the file on disk is the copy-source of record, never a chat card)
status: SUPERSEDED 2026-09-07 — by: context/handoff/2026-09-06_v66_OPERATOR-BRIEF_for-Nick.md · was: SUPERSEDED at v65 beat 7 (Sun 2026-09-06) by context/handoff
-->

# Operator brief — what Nick does, in order (v65 — CLOSED at beat 4; §CLOSE is the live section)

## §CLOSE (beat 4, Sat 2026-09-05 ~22:03 CT) — v65 IS CLOSED on context health; v66 takes the returns. Three acts for you, in order; §QUEUE below stays valid for Acts 1 · 2 · 3 · 4 and the words.

**Why close now, in one sentence:** this window carried the boot, Lane C, the W-SKILLS-7 dispatch, the four-lane map, Monday's frame and the FE-113 instruction; four lanes are running and their returns — CG's 17-file census, two research verdicts, a 22-mint ledger pass — each deserve a fresh window that audits them at the bytes with the rules already pre-filed.

### Act C1 — push the hivemind (≤1 min; `~/Desktop/Code/ClaudeFolder/nexsys-hivemind`)
```bash
git log --oneline -1 | cut -c1-70; git rev-list --count origin/main..HEAD; git push origin main
```
**EXPECTED:** the line begins `<sha> hivemind: v65 beat 4 — THE v65 CLOSE`; the count is the number of v65 commits not yet pushed (5 if none were); the push ends `6542ef3..<sha>  main -> main` (or from your last pushed sha). **REPORT BACK (to v66):** `pushed <sha>`.

### Act C2 — dispatch v66 (≤2 min; a FRESH Cowork conversation with the ClaudeFolder connected) — when the FIRST return lands (CG's, most likely; or Sunday morning either way)
```
You are the v66 PM MISSION-CONTROL hub for NexSys / HomeSynapse. Boot from nexsys-hivemind/context/handoff/2026-09-05_PM-mission-control_v66_orchestrator_session_prompt.md — execute its §1 EXACTLY (date -u first; the spine — pm-handoff.md line 8 + the newest THREE beat blocks + PROJECT_SNAPSHOT.md — outranks its §2; the five HEADs; the fold grep; the preflight). Every §0 law of that prompt holds by reference; the posture of record is context/handoff/2026-09-04_v63_dispatch-prompt.md (+ its v65 addendum); the five rituals of record are context/handoff/2026-09-05_v65_dispatch-text_verbatim.md — hold every line. This window's ONE deliverable is THE RETURNS' AUDITS under the pre-filed rules (context/audits/2026-09-05_v65-b1_boot-and-intake_audit.md §6–§7) and, if both RS returns are in, THE DECISION CARD as the pre-registered frame applied (context/strategy/brand-program/2026-09-05_monday-decision-frame_pre-registered.md). STATE AT DISPATCH (verify each at the instrument; the record wins): CG: audited ACCEPT (v65 b5) · landed ⟨sha | not yet⟩ · CI ⟨green | red: line | not yet⟩ · RS-10 · RS-11: audited, THE DECISION CARD cut (v65 b5) · SEARCH-NAME: ⟨Nick's word | not yet⟩ · ASR-VERDOMU: ⟨…⟩ · RS10-STAR: ⟨…⟩ · FE-113: ⟨not yet | dispatched hh:mm | returned <path> <bytes>⟩ · W-SKILLS-7: ⟨not yet | dispatched hh:mm | returned <path> <bytes>⟩ · sample4: ⟨…⟩ · samples: ⟨…⟩ · act3: ⟨…⟩ · nightly 09-05: ⟨…⟩ · BLOCK6: ⟨pull | hold⟩ · DESIGN: ⟨start | hold | not yet⟩ · hivemind pushed through ⟨sha⟩. First acts: §1 → beat 1 (name the deliverable; the intake at the bytes; this text verbatim) → the CG audit first → RS-10 → RS-11 → the card → W-SKILLS-7 → FE-113's slots filled and its line handed on CG's landing → the F-R4-1b charter ahead. Author ahead of need; commit at every block with a census-exact card; past mid-session the v67 skeleton; close on context health, never on a cliff.
```
**EXPECTED:** it boots from the v66 prompt, names its deliverable, censuses the returns on disk, and audits CG first. **This v65 conversation is then retired — except for banking any lines you send it before v66 boots (a post-close beat, census-exact).**

### Act C3 — the returns, to v66
Each lane's `RETURNED <path> <bytes>` line verbatim (CG · RS-10 · RS-11 · W-SKILLS-7); the six owed lines (Act 3) whenever you have them; `DESIGN: start | hold`; your words on THE BEYOND when you read it. CG's commit + push is YOUR hands after v66's audit hands you the card — never before.

---

## §POST-CLOSE-2 (beat 6, Sun 2026-09-06 ~09:41 CT) — CG LANDED `f25291b`, CI GREEN (banked). Eight acts; the first two are the leverage acts, the rest fill your spare windows. The program of record: `context/planning/2026-09-06_v65-b6_post-landing_program_and_four-charters.md`.

### Act Q1 — the nanoid lock-only bump (≤5 min; `~/Desktop/Code/ClaudeFolder/homesynapse-core`; Dependabot #12 — BEFORE FE-113)
**WHAT:** bump the transitive `nanoid` 3.3.16 → 3.3.18 in `web-ui/dashboard/package-lock.json` only. **WHY:** GHSA-2v37-7h3g-55p8 (an infinite loop in `customAlphabet`/`customRandom` at size 0); a build-time dependency of postcss — not in the served bundle, so no household exposure — but hygiene is five minutes, and a security fix never rides a feature commit; FE-113's baseline becomes this sha. `3.3.18` exists on the registry (2026-08-07) and is inside every `^3.3.16` range — Dependabot's "cannot update" is a stale read.
```bash
cd web-ui/dashboard && npm ls nanoid 2>/dev/null | grep nanoid | head -3      # EXPECTED: nanoid@3.3.16 (deduped) lines
npm update nanoid --package-lock-only && npm ls nanoid 2>/dev/null | grep -c '3.3.18'   # EXPECTED: ≥1 (and zero 3.3.16 lines)
cd ../.. && git --no-optional-locks status --porcelain                          # EXPECTED: exactly " M web-ui/dashboard/package-lock.json"
git add web-ui/dashboard/package-lock.json && git commit -m "chore(deps): nanoid 3.3.16 -> 3.3.18 (lock-only; GHSA-2v37-7h3g-55p8, Dependabot #12; a build-time dependency of postcss, not in the served bundle)" && git push origin main
```
**EXPECTED:** one file in the commit; `f25291b..<sha>`; both workflows green (frontend.yml runs `npm ci` + `verify`; the alert closes on its next scan). If `npm update` leaves 3.3.16 in place (an unexpected resolver hold), STOP and report the `npm ls nanoid` output — the fallback is an `overrides` entry, ruled on the hub's word, not improvised. **REPORT BACK:** `NANOID: landed <sha> · CI <green | red: line>`.

### Act Q2 — FE-113, the fast-follow (one paste; a FRESH Cowork window) — after Q1's CI is green, with Q1's sha as the baseline
The line is in §POST-CLOSE Act P3 above — fill `⟨CG's landed sha⟩` with **Q1's sha** (the tree FE-113 must find clean). **REPORT BACK:** `FE-113: dispatched <hh:mm CT>`; later its `RETURNED` line.

### Act Q3 — the words (one message; the first three before Tuesday morning)
`SEARCH-NAME: <…>` · `ASR-VERDOMU: pass <spellings> | fail` · `RS10-STAR: <line>` · **`H8: <Tue | Wed evening>`** · **`R4C: <Sat 09-12 | Sun 09-13>`** · `BEYOND-LETTERS: X | keep` · `DESIGN: start | hold` · `BLOCK6: pull | hold` · the six owed lines · W-SKILLS-7's state.

### Acts Q4–Q7 — four read-only lanes, any order, each its own FRESH Cowork window (the pastes are in the program file §5; none touches the core tree; none waits on CI)
**Q4 RS-12-F** (the fanciful-domus sprint; 3–5 h; scoped to the redirect and runner-up slots — Tuesday's send does not wait on it) · **Q5 TR-0** (the actuation chokepoint census; ≤2 h; decides whether B-2 is one line or a refactor) · **Q6 TR-1** (the position census as a bench verb; ≤3 h; the MVP's event-loss audit instrument = the fence's evidence closure = B-1's measurement) · **Q7 HERO-0** (the null census of v1.1.3; ≤2 h; the hero's four empty states before a pixel). **REPORT BACK:** `<lane>: dispatched <hh:mm>`; later each `RETURNED` line.

### Act Q8 — push the hivemind (`6542ef3..<sha>`, count 7 with this beat) and dispatch v66 (Act C2's paste; its prompt is re-cut) when the first of these returns lands.

---

## §POST-CLOSE (beat 5, Sat 2026-09-05 ~22:55 CT) — the returns landed Saturday night and were audited HERE on your directive; five acts, in order

**Leverage line:** Act P1 — your CG commit + push. CI green on it releases FE-113, the core slot for F-R4-1b, H8 and Block 6; nothing else tonight unblocks anything.

### Act P1 — commit + push CG-123 = THE LANDING (your hands; ≤5 min; `~/Desktop/Code/ClaudeFolder/homesynapse-core`)
**WHAT:** the audit is ACCEPT (`context/audits/2026-09-05_CG-123_intake_two-layer-audit_v65-b5.md`; the lane's one `[REVIEW]` ruled ACCEPT as implemented). **WHY:** the one core lane is done; CI on your push is the gate of record and the ArchUnit gate the desk deferred.
```bash
git --no-optional-locks status --porcelain | wc -l          # EXPECTED: 17 — STOP if not
git add -u && git diff --cached --name-status | wc -l       # EXPECTED: 17 — STOP if not
git commit -F ../_scratch/2026-09-05_core_CG-123_commit-msg.txt && git push origin main
```
**EXPECTED:** 17 · 17 · the push ends `e5fa035..<sha>  main -> main`; Actions → the run is green. **REPORT BACK:** `CG: landed <sha> · CI <green | red: the FAILED line>`. A red on this push is read against the pre-registered HeroLoop prediction FIRST (a `route_join_miss ×1` with zero `bus.delivery_anomaly` lines = FIX-2), never as CG's fault by default.

### Act P2 — your words on THE DECISION CARD (≤10 min; `context/audits/2026-09-05_RS10-RS11_intake_two-layer-audit_and_DECISION-CARD_v65-b5.md` §3)
**WHAT:** the frame applied mechanically says `SEARCH-NAME: VERDOMO` (RS-10 = SPEND-JUSTIFIED; no RS-11 cell displaces the control by ≥10 of 85). **WHY:** the go-ahead is Tuesday morning; your taste enters once, on the card. **REPORT BACK, in one message:** `SEARCH-NAME: <VERDOMO | VERDOMU | HUSHDOMA | VERDOMA | KEELORA | ask-Erik-sight-read-first>` · optional S7 numbers (≤15 per cell) or a veto ("I will not commission <cell>") · **`ASR-VERDOMU: pass <the spellings you got> | fail`** — the 5-minute listener/ASR protocol (RS-9 §6) on the redirect candidate, so the on-sight redirect clause can name it · **`RS10-STAR: <line>`** — ONE pane read the hub could not make from its container: TSDR for 99144181 (MORDOMO), the office action's "no conflicting marks" sentence (≤3 min; or leave it to v66's browser Monday).

### Act P3 — FE-113, the fast-follow (one paste; a FRESH Cowork window with `ClaudeFolder` connected) — ONLY after Act P1's CI is GREEN
**WHAT:** the instruction's slots are filled (`context/instructions/2026-09-05_frontend-lane_FE-113_read-API-v1.1.3-mirror_fast-follow_instruction.md` §2); fill `⟨CG's landed sha⟩` in the line below with the sha from Act P1. **WHY:** one lane on the core tree — the dashboard lives in it; the FE mirror of v1.1.3 is the next unit on the map.
```
date -u first. You are the FE-113 frontend lane for NexSys/HomeSynapse — boot as the nexsys-frontend skill. Baseline: homesynapse-core must be at ⟨CG's landed sha⟩ with `git status --porcelain` empty (STOP and report if not); work only under web-ui/dashboard/. Execute nexsys-hivemind/context/instructions/2026-09-05_frontend-lane_FE-113_read-API-v1.1.3-mirror_fast-follow_instruction.md exactly: §0 first, then §1's read-set in order; the wire literals are §2's as the hub filled them from the CG audit at nexsys-hivemind/context/audits/2026-09-05_CG-123_intake_two-layer-audit_v65-b5.md. Tests first (red at HEAD), then the edits, 11 M + 1 A. Return ONE file at nexsys-hivemind/context/audits/<today's CT date>_FE-113_return.md, §0 card first, ≤12 KB. Stage nothing; commit nothing; the hub audits and Nick commits. Your last line: RETURNED <path> <bytes>.
```
**REPORT BACK:** `FE-113: dispatched <hh:mm CT>`; later its `RETURNED` line.

### Act P4 — W-SKILLS-7 (Act 4 above) — `W-SKILLS-7: dispatched <hh:mm> | not yet | returned <path> <bytes>`; and the six owed lines (Act 3) whenever you are at GitHub / the Pi.

### Act P5 — push the hivemind (`6542ef3..<sha>`, count 6 with this beat) and dispatch v66 on the next return (Act C2 — its STATE slots now read: CG audited ACCEPT, landing yours · RS-10/RS-11 audited, the card cut · FE-113 slots filled).

---

## §CONTEXT — the state of record (every line has a path; nothing here is from memory)
- **The gate is CLEARED.** Core `e5fa035` (FIX-1b, "all checks pass" — banked v64 b8, law 16) on top of `5ed9178` (FIX-1a = sample #4). Porcelain clean, in sync. One lane may open on the core tree: **CG-1/2/3** (`context/instructions/2026-09-05_coder-lane_CG-123_read-API-v1.1.3-additive_coding-instruction.md`; 17 M + 0 A; the dispatch line at its end; the audit rules and the hub's predictions PRE-FILED at `context/audits/2026-09-05_v65-b1_boot-and-intake_audit.md` §6).
- **The hivemind is at `6542ef3`** (v64 b10), pushed, in sync. Your v65 paste was byte-identical to the on-disk text (7,444 B); its ⟨slots⟩ arrived unfilled, so the six lines below are still owed. The dispatch-text file had been deleted in the working tree after you copied it; the hub restored it from HEAD (the audit §2) — say `DISPATCH-FILE: delete` only if that deletion was deliberate.
- **The brand: the Erik go-ahead is HELD by your word** (`ERIK: hold-for-RS10`). The pre-spend program is chartered (`context/strategy/brand-program/2026-09-05_RS10-RS11_pre-spend-program_…_research-charter.md`); the lane prompts of record are `…_RS10-RS11_dispatch-prompts_long-form.md`. Both lanes report to THIS session: Mon 09-07 (Labor Day; counsel closed; zero business days spent) the hub audits both two-layer and cuts the decision card (charter §0.3); Tue 09-08 morning you send the go-ahead re-cut to the chosen name, expedited. Wed 09-09 = the last day for a named-gap RS-12 · Thu 09-10 = the last commissioning date with redirect room · **Fri 09-18 = the hard stop, unchanged.** Two paid searches = the cap. No name is graded in chat; your taste rulings go on the card, after the returns.
- **The refinement program** (`REFINE: go` · `W-SKILLS-7: fresh-window`): Lane C (the deep-work window protocol) is the hub's NEXT commit; W-SKILLS-7's fresh-window line is handed after it — not before (guard 1), and not before the CG line is in your hands (guard 4 — it is: Act 1).
- **Fences, unchanged:** one lane on the core tree · `main` red ⇒ no other core lane · a sample VETOES a green, never GRANTS one · never a `main` re-run · s31/nightly HANDS OFF until R-5 · `network_formed` = POWER OFF + STOP · `TOKLEN-OK` · FENCE-BUS (no delivery-completeness sentence until OR-BUS-SILENT-DROP closes on 20 ordinary `main` runs from `e5fa035`) · no public brand use before the written opinion · push is always yours.

## §NOW (beat 1) — the plan from here at three horizons, and the leverage line
**Leverage line:** the single act that unblocks the most downstream work is **Act 1, the CG dispatch** — the FE fast-follow (Block 4), H8's real-wire read of the new keys, the freeze-doc v1.1.3 note and Block 6's one docs touch all wait on CG's landing; nothing waits on anything else you do tonight.
*Horizon 1 — tonight → Sunday:* Act 1 (CG) → Act 2 (RS-10, then RS-11) → Act 3 (the six owed lines, one message, whenever you are at GitHub/the Pi) → the hub commits Lane C and hands you the W-SKILLS-7 line (Act 4) → beat 2: THE FOUR-LANE MAP + the pre-registered decision frame (hub; no act of yours). While CG runs the hub drafts Block 4 (the FE fast-follow) ahead.
*Horizon 2 — the week:* Mon the two research audits → the decision card → your words on it (`SEARCH-NAME:` · taste rulings on any RS-11 cell) → Tue the go-ahead (with one added sentence asking Erik what expedite buys in DAYS — the audit §5) → CG lands (your commit + push; CI = the gate) → the FE fast-follow dispatches → H8 real-wire on FIX-1b's CI artifact (the §6-B/EXITCODE proof riding) → Block 6 (one docs touch, the freeze note inside) → P-1 + F-R4-1b charters → 09-09 the Apple one-liner (the hub hands the paste) · `EU: ship|defer` 09-11.
*Horizon 3 — the runway:* the BEYOND card at three horizons when the calendar has slack (the harness enforces; the model proposes) · `Activate: apply|hold` 09-15 · Silabs 09-17 · the hard stop 09-18 · the Apache-2.0 flip inside the rename window (10-31 fallback).

## §QUEUE — the acts, in order

### Act 1 — ⚠ FIRST: dispatch CG-1/2/3 (≤2 min; a host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core`; the ONE core lane)
**WHAT:** open a Claude Code session in the core repo and paste the line below whole. **WHY:** the gate is cleared and the tree is clean at `e5fa035`; CG is the only lane allowed on the core tree and everything in Horizon 2 waits on its landing. The lane runs unattended (≈2–4 h): tests first (T1–T11 red at HEAD), then 17 M + 0 A, then a ≤12 KB return; it stages nothing and commits nothing — the hub audits, you commit.
```
date -u first. Boot as the nexsys-coder skill. Baseline: this tree must be at e5fa035 and clean — verify with `git log -1 --format=%h` and `git status --porcelain` (STOP and report if not). Execute nexsys-hivemind/context/instructions/2026-09-05_coder-lane_CG-123_read-API-v1.1.3-additive_coding-instruction.md exactly: read its §0 contract and the minimum read set first; confirm every STOP gate. Words: CG2-SCOPE: A1-only. ROW30: as-ruled. Tests first (T1–T11 red at HEAD), then the production edits, 17 M + 0 A. Return ONE file at nexsys-hivemind/context/audits/<today's CT date>_CG-123_return.md, §0 card first, ≤12 KB. Stage nothing; commit nothing; the hub audits and Nick commits.
```
**EXPECTED:** the lane prints `e5fa035` and an empty porcelain, reads the instruction's §0, and starts on the tests; a STOP at the baseline means the tree moved — report the two lines it printed and do nothing else on the core tree. **REPORT BACK:** `CG: dispatched <hh:mm CT>` now; later the lane's last ~10 lines + `CG: returned <path> <bytes>`.

### Act 2 — dispatch RS-10, then RS-11 (≤3 min; two FRESH Cowork conversations with `ClaudeFolder` connected; sequential is fine — RS-10 first)
**WHAT:** open `context/strategy/brand-program/2026-09-05_RS10-RS11_dispatch-prompts_long-form.md`; paste the RS-10 prompt whole into one fresh window, the RS-11 prompt whole into another. **WHY:** both lanes are read-only web research that writes one file each; they run 4–8 h; Monday's audits and card need them on the mount by Monday morning; the desk fences moved by your word and the paid cap is untouched. RS-10 is load-bearing (the DOMO-family verdict), RS-11 is Tuesday's insurance — if you open only one tonight, open RS-10. **EXPECTED:** each lane reads the charter's §0 + its own section + §3, then the read-set, and works; its last line is `RETURNED <path> <bytes>`. **REPORT BACK:** `RS-10: dispatched <hh:mm>` · `RS-11: dispatched <hh:mm>`; later each lane's `RETURNED` line verbatim.

### Act 3 — the six owed lines, one message, whenever you are next at GitHub and the Pi (≤10 min total; all read-only)
**WHAT / WHY / EXPECTED, per line:**
1. `sample4: green | red: <the FAILED line>` — Actions → the `5ed9178` run's verdict. Informative only (sample #4 is never a gate); a red is read against the pre-registered prediction (a HeroLoop red with `route_join_miss ×1` and zero `bus.delivery_anomaly` lines = the fan-out reorder → FIX-2).
2. `samples: not yet | k/3 green | red on #k: <line>` — Actions → CI → Run workflow on `main`, three times, any time now (a push run is green, so they are lawful). A red VETOES the clearance and re-opens the gate with its mechanism named.
3. `act3: <the ReplayTransitionIT failure message, verbatim>` — the `dc3328b` red run → Summary → Artifacts → `test-reports` → `core/event-bus/build/reports/tests/test/classes/com.homesynapse.event.bus.ReplayTransitionIT.html` → the text under the test name. `did not reach 1000 within 15000 ms` = phase 1 (closed by the drain fix); `did not reach <N> within 30000 ms` = phase 2 (a mechanism the desk never saw remains). If the artifact is gone: `act3: artifact absent`.
4. `nightly 09-05: <the digest line>` — `~/hs-bench/digests/nightly.log` on the bench card (fires ~03:30 CT; 09-03 and 09-04 read `8/9`). Read-only; s31 HANDS OFF.
5. `BLOCK6: pull | hold` — rec `hold` (one docs touch after CG lands, the freeze note inside).
6. `DISPATCH-FILE: delete` — ONLY if you deleted `context/handoff/2026-09-05_v65_dispatch-text_for-Nick.md` on purpose; otherwise nothing (the hub restored it).
**REPORT BACK:** the six lines in one message; `not read` is a valid value for 1–4.

### Act 4 — W-SKILLS-7 in a fresh window — LIVE (≤2 min; a FRESH Cowork conversation with `ClaudeFolder` connected; parallel-safe — two repos, neither the core tree)
**WHAT:** paste the line below whole. **WHY:** Lane C is committed (`context/process/deep-work-window_protocol.md`, guard 1) and the CG line is in your hands (guard 4); the lane folds the v63 AND v64 mints (22 candidates) into the three skills' `references/` ledgers with every `SKILL.md` byte-unchanged (guard 2), ≈2–3 h; it stages and commits nothing — the hub audits at the bytes and commits both repos; you then re-sync the account skills once. The dispatch of record: `context/instructions/2026-09-05_W-SKILLS-7_skills-pass_lane-dispatch.md`.
```
date -u first. You are the W-SKILLS-7 skills lane for NexSys/HomeSynapse. Read nexsys-hivemind/context/instructions/2026-09-05_W-SKILLS-7_skills-pass_lane-dispatch.md WHOLE, then its §1 read-set in order and nothing older. Execute §2 exactly under §4's fences: every SKILL.md byte-unchanged (md5 before/after in your §0); the write-set only; stage nothing, commit nothing. Adjudicate §3's predictions first in your §0. Return ONE file at nexsys-hivemind/context/audits/<today's CT date>_W-SKILLS-7_return.md (§0 card ≤3 KB first: the census exact · the mint→arc mapping table · the SKILL.md md5s; whole ≤12 KB). ≈2–3 h; a partial return with an honest §0 outranks a complete one later. Your last line: RETURNED <path> <bytes>. You report to the v65 hub, not to me.
```
**EXPECTED:** the lane reads the dispatch, the protocol and the charter, then the mints, then the ledgers; its §0 card grows from the first hour. **REPORT BACK:** `W-SKILLS-7: dispatched <hh:mm CT>`; later its `RETURNED` line verbatim; after the hub's commit and your re-sync, `SKILLS: synced`.

### Act 5 — push the hivemind after every hub beat (≤1 min each; `~/Desktop/Code/ClaudeFolder/nexsys-hivemind`)
```bash
git log --oneline -1 | cut -c1-70; git rev-list --count origin/main..HEAD; git push origin main
```
**EXPECTED (this beat):** the line begins `<sha> hivemind: v65 beat 1`; the count `1`; the push ends `6542ef3..<sha>  main -> main`. **REPORT BACK:** `pushed <sha>`.

### Standing (no act tonight)
- **Erik:** HELD until Tuesday's card; the go-ahead draft (`…/2026-09-05_pelton-reply_go-ahead_H10_and_draft.md` §3) is re-cut by the hub Monday night to the chosen name, with the expedite-days sentence added.
- **Monday:** E1 (the hub, EUR-Lex) · SCITT CCF Last Call ends (record the outcome) · your words on the decision card.
- **09-09:** the Apple one-liner (the hub hands the paste). **09-11:** `EU: ship|defer`. **09-15:** `Activate: apply|hold`. **09-17:** Silabs. **09-18:** the hard stop.
- **Two words, no rush (the four-lane map §3–§4):** `DESIGN: start | hold` — whether you spend the identity block's hours before the opinion (Tier 2 makes it lawful; rec `start` on the token audit now, the block after Tuesday) · your words on THE BEYOND INPUT's rows (`context/strategy/2026-09-05_post-MVP-horizon_strategy-card-INPUT.md`; nothing adopts before them; TR-1 charters on them) — with, if you agree, `BEYOND-LETTERS: X` to re-letter its rows X-1…X-8 so "B-1" stops naming two things.

## §WHAT YOU DO NOT DO (this weekend)
Touch the core tree while CG runs (one lane) · re-run `main` CI · take the samples before a push run is green (one is) · hand a name to Erik before Tuesday's card · grade a name in chat · touch s31 or the nightly · `--allow-downgrades` anything · push anything but the hivemind and (after the hub's audit) CG's commit.

## §IF YOU HAND THIS TO ANOTHER CLAUDE SESSION
Give it §CONTEXT whole and the one act you want done; it reads the file paths named there and nothing older; it reports to v65 in the REPORT BACK forms above; it commits nothing.
