<!--
file: context/audits/2026-09-13_v73-b1_boot-and-intake_audit.md
purpose: The v73 boot-and-intake audit — the boot read-set with its bytes, the five HEADs at the instrument, the intake of both v72 cards at the bytes, the freshness preflight as run (one line per check, the two STALE verdicts and what reconciled each), Nick's dispatch text verbatim, the window's ONE deliverable and its blocks. The record of beat 1; the transcript is not.
audience: the v73 hub (beat 1) · every later hub (the boot exhibit after 2026-09-13) · Nick (§5 is his text)
state-type: audit (filed once; never edited)
status: FILED — v73 beat 1, Sun 2026-09-13 ~13:5x CT (instrument 2026-09-13T18:58:21Z)
-->

# v73 beat 1 — boot and intake

## §1 The clock and the boot read-set (the budget ≤45 KB)
`date -u` → `Sun Sep 13 18:44:38 UTC 2026`; CT = UTC−5 → Sun 2026-09-13 13:44. Read in the prompt's order, each by range: (a) the v67 prompt whole 13,017 B · (b) `pm-handoff.md` line 8 2,878 B + the v72 b7 block (lines 15–22) 2,449 B · (c) `PROJECT_SNAPSHOT.md` whole 3,482 B · (d) the operator brief whole 12,185 B · (e) the v66 decision record §3 1,969 B · (f) the plan of record's §4 2,259 B + §6 1,403 B (Nick's dispatch names these two; §3's 2,102 B not read) · (g) pm-lessons: six entries dated after 09-10 fold at W-SKILLS-9; none read at boot. **Total 39,642 B.** Consulted after the boot, by range: `freshness-preflight.md` (the command blocks of Checks 1–12, ≈14 KB) and the v72 b7 splice script's structure (≈6 KB).

## §2 The five HEADs at the instrument (one call)
core `a458a64` porcelain 0 · hivemind `7540662` porcelain 0 · skills `c630c5c` porcelain 0 · bench `1201368` porcelain 0 · docs `2235845` porcelain 1 (` M design/amendments/AMD-101_…md` — the §6 run id, held). Every `origin/main..HEAD` count 0; no `.git/*.lock` in any repo. The dispatch line's STATE matches the instrument on all four named repos.

## §3 The intake at the bytes (the two v72 cards, Nick's hands)
- bench `1201368` (`git diff-tree --name-status`): `A docs/2026-09-13_P-1_power-harness_design.md` · `M scenarios/constants.yaml` · `A tools/harness/harness.py` · `A tools/harness/test_harness.py` — 3 A + 1 M, the b7 card's four explicit paths exactly.
- hivemind `7540662`: `A context/audits/2026-09-13_P-1_return.md` · `A …/2026-09-13_v72-b7_P-1_intake_two-layer-audit.md` · `M` OPERATOR-BRIEF · `M` archive/chains-rotated-2026-08-27.md · `M` pm-handoff.md · `M` instructions/2026-09-11_bench-lane_P-1_…charter.md · `M` planning/2026-09-13_v72_PROGRAM-RECUT_….md · `M` status/PROJECT_SNAPSHOT.md — 6 M + 2 A, the b7 card's eight paths exactly.
- The P-1 return's last line: `RETURNED nexsys-hivemind/context/audits/2026-09-13_P-1_return.md 12286` (a return, not a living card).

## §4 The freshness preflight as run (one line per check)
1. PASS — the snapshot's `last-verified: 2026-09-13` is the newest beat (v72 b7).
2. PASS — the plan of record resolves (`context/planning/2026-09-13_v72_PROGRAM-RECUT_…`).
3. PASS — core HEAD `a458a64` = the snapshot's cite.
4. PASS (spot) — `phase-3-milestone-backlog.md` present, 29 DONE rows; the three-way cross-reference NOT re-executed this boot (disclosed).
5. PASS — `## Open Risks` carries dates through 2026-09-13 (≤7 days).
6. PASS — coder-handoff's newest entry is BUS-ORDER-1 with a next-WU pointer (114b per the spine).
7. PASS — 21 `MODULE_CONTEXT.md` tracked against 22 `include(` lines; none at template size.
8. PASS — cross-agent-notes: 0 active entries above `## Archived`.
9. STALE — 27/28 identical at the bytes; `nexsys-project-manager/SKILL.md` differs (SOURCE `bda340b1…` at v69 b1 — the hands re-cut of the commit-boundary law; the synced copy `76bf4ce6…` lags). The lag is Nick's sync; per the reference's own rule authoring rides SOURCE, and this hub holds the v69 b1 law: every repo is Nick's hands.
10. PASS — 101 cited paths in `strategic-context-map.md`; the 5 unresolved are template globs (`YYYY-MM-DD_topic.md`, `weeks/YYYY-WNN_…`), not files.
11. PASS (spot) — `settledAt` resolves in 5 core Java files.
12. STALE → RECONCILED in this beat — grep 1 named two files: `2026-09-06_H8a_…navigator-packet.md` (LIVE — the spine's dispatch-ready rig lane; excluded by the check's own rule; B5 re-cuts it) and `2026-08-22_research-lane_RS3-WMARKET-2_market-currency-refresh_brief.md` (DISPATCH-READY-ON-CADENCE since v56 b1; its 08-31 trigger passed with no paste and no spine beat records the lane) → its `status:` line set to FILED, the prior status kept after "Was:", the body untouched. Greps 2 and 3: 0 and 0.
**Aggregate: STALE on 9 (Nick's act; non-blocking by the reference) and on 12 (reconciled here). Forward work is lawful.**

## §5 Nick's dispatch text, verbatim
You are the v73 PM MISSION-CONTROL hub for NexSys / HomeSynapse. Boot from `nexsys-hivemind/context/handoff/2026-09-06_PM-mission-control_v67_orchestrator_session_prompt.md` (the STABLE form — no state in it) and execute its §1 EXACTLY, inside its boot byte budget: `date -u first`; `pm-handoff.md` line 8 + the newest ONE beat; `PROJECT_SNAPSHOT.md`; `context/handoff/OPERATOR-BRIEF_for-Nick.md` whole — its §HELD-BY-THE-HUB is the wait-state ledger; the decision record §3; the plan of record §3; the five HEADs in one call; the preflight as one line per check. THE OPERATOR-LOAD LAW and THE CONTEXT-BUDGET LAW (§1b) bind every message and every call. Beat 1: name the window's ONE deliverable, the intake at the bytes, this text verbatim, §HELD re-printed, hand me ONE act. STATE AT DISPATCH (the record wins): core `a458a64` (BUS-ORDER-1; CI green; the closure counter 1/20); hivemind `7540662`; bench `1201368`; docs `2235845` (+1 M held: AMD-101's §6 run id). Read `context/planning/2026-09-13_v72_PROGRAM-RECUT_git-read_objectives_and_v73-window-plan.md` §4 and §6 by range at beat 1 — they shape this window: 114b's instruction first (the Java domain is free), R-5's charter second, HERO-1c's charter on FE: `6af76f7`, H8-a's packet re-cut through THE PRIOR-LEDGER GATE on H8:, the strategy fold at beat 6 by range. It's imperative that you take ownership and accountability, and are always seeking to optimize how we contextualize/articulate any coding and/or research or other sessions as necessary — and perhaps most important — we must be able to carefully and strategically manage all this context for future maintainability and scalability.

## §6 The window's ONE deliverable and its blocks
**Deliverable:** EXPLAIN-114b LANDED green on the Java domain (the closure counter advances by its push). **Blocks:** B1 this boot and intake · B2 114b's instruction authored from the 114a return by range and handed (the Java domain is free) · B3 HERO-1c's charter on `FE: 6af76f7 frontend green` · B4 R-5's charter (the C-003 counterfactual window, the null-arm block, the re-seen/adopted split, the ULID audit, P-1's fold: the `plug:` key, exit codes, the time bound) · B5 H8-a's packet re-cut through THE PRIOR-LEDGER GATE, handed on `H8:` · B6 the strategy fold by range · beats 7–8 intakes and the close on the deliverable, never on a cliff. **Adopted at this beat (the plan §4 refinement):** `context/process/splice_lib_v1.py` — stateless, md5-asserted by every beat script, versioned by file name. **Nick's standing directive in this dispatch** — ownership; every session contextualized and articulated for maintainability and scalability — is answered structurally: the record is the memory (this audit, the beat, the brief), the library removes repeated bytes from every future beat, and each authored artifact this window names its read-set, its return path and its cap.

## §7 Disclosed non-re-executions
Check 4's three-way cross-reference; Check 11 beyond one spot; the pm-lessons entries (folding at W-SKILLS-9); the R-4c record and the P-1 return bodies (audited at v72 b6–b7; not re-read).
