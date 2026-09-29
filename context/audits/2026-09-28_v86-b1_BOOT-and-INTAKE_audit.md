<!--
file: context/audits/2026-09-28_v86-b1_BOOT-and-INTAKE_audit.md
purpose: The v86 hub's beat-1 audit — the boot inside the byte budget, the preflight at one line per check, the five HEADs at the instrument, the dispatch text verified against the pasted text, EXPORT-1's pre-registration BEFORE its line lands, and the hold on the hivemind tree until Part C's card runs.
audience: the v86 hub (its own record) · v87 (the boot's exhibit) · Nick (§0)
state-type: audit (filed once; never edited after the beat)
status: FILED — v86 beat 1 (Mon 2026-09-28 ~18:4x CT; instrument 2026-09-28T23:42:00Z). Authored under `_scratch/v86/` during the hold (§6) and spliced into the tree after `HIVE: LANDED`.
-->

# v86 beat 1 — BOOT and INTAKE audit (Mon 2026-09-28 ~18:4x CT)

## §0 The verdict
**BOOT PASS.** The boot read-set 44,283 B (≤ 45 KB). The preflight 12/12 PASS (Check 9: 28/28 identical; Check 12: 0 · 0 · 0). The five HEADs at the instrument equal the record's (§3); nothing of the evening packet had run at 22:5x Z (no `_scratch/v84/*BENCH-PULL-3*`, no `_archive/runs/`, the hivemind porcelain 19 = 9 M + 10 A, core porcelain 0). Nick's first message at 17:47 CT (`HOURS: 3–4`) filed verbatim; the dispatch text is the file the v85 hub cut (§4). THE ONE DELIVERABLE named: EXPORT-1's grade intaken two-layer. ONE act handed at 17:5x CT: Part A (BENCH-PULL-3). The window starts 47 minutes behind the packet's 17:00; BC6's 20:15 CT start gate is the clock that binds the order (the DR D-v86-2).

## §1 The boot read-set (bytes at `wc -c`; the order of the prompt's §1.2)
| Read | Bytes |
|---|---|
| (a) `context/handoff/2026-09-06_PM-mission-control_v67_orchestrator_session_prompt.md` whole | 13,017 |
| (b) `pm-handoff.md` line 8 (the chain) · the newest ONE beat (v85 b4, lines 15–20) | 1,502 · 1,999 |
| (c) `context/status/PROJECT_SNAPSHOT.md` whole | 3,492 |
| (d) `context/handoff/OPERATOR-BRIEF_for-Nick.md` whole | 12,273 |
| (e) the v85 DR §3c + §3d + the Carried row (lines 49–57) | 4,819 |
| (f) the plan of record §30 (lines 219–224) · THE WEEKS AHEAD §7 (lines 54–64) | 2,512 · 2,954 |
| (g) `pm-lessons.md` — the one entry newer than the ledger (2026-09-28, lines 385–387) | 1,715 |
| **Total** | **44,283** |

`date -u` first: `Mon Sep 28 22:47:06 UTC 2026` → 17:47 CT (UTC−5), the same minute as Nick's line.

## §2 The freshness preflight (one line per check)
1. PASS — the snapshot `last-verified: 2026-09-28` (v85 beat 4).
2. PASS — the plan of record resolves: §30 present (1); THE WEEKS AHEAD §7 present (1).
3. PASS — the snapshot's five shas are the five HEADs (`40412f9` · `352296d` · `7221ddc` · `180375f` · `8a062da`; 1 hit each).
4. PASS — `context/status/` carries the snapshot + READ-ME-FIRST + archive; no milestone backlog file is expected under the plan of record.
5. PASS — `## Open Risks` present once; 10 distinct `OR-` names in the section = the snapshot's "ten".
6. PASS — `coder-handoff.md` `last-verified: 2026-09-28` (v84 b5: LOCK-1 + IR-61b intaken); the next WU it points at is PJ-2, the record's Part D.
7. PASS (carried) — 21 `MODULE_CONTEXT.md` under `git ls-files` against 22 `include(` lines, unchanged since v85 b1's PASS (no core landing since `40412f9`); the one uncovered include is not re-derived this beat (disclosed in §7).
8. PASS — `cross-agent-notes.md` 1,024 B, 0 active entries.
9. PASS — 28/28 per-file md5 identical: the device trees `nexsys-hivemind/project-manager` (10) · `nexsys-hivemind/coder` (9) · `nexsys-skills/orchestrators/nexsys-frontend` (9) vs the synced `nexsys-project-manager` · `nexsys-coder` · `nexsys-frontend`; the lists at `_scratch/v86_device-skills-md5.txt` (device) and the container scratchpad.
10. PASS — `context/strategy/` 34 files; the north star named in 11 of them.
11. PASS — the source round-trip on the record's two cited lines: `StateProjection.java` :588 is the `caught up at position` log line the BC6 card greps; `RegistryProjectionSubscriber.java` has 112 lines (the IR-93 row's :107–:110 inside it).
12. PASS — 0 over-current instruction files after the exclusions re-derived from the v85 b4 beat (PJ-2's instruction · the BC6 card · KREFRESH-1's charter · W-SKILLS-10's charter · `2026-09-28_`); 0 LIVE orchestrator prompts other than the v67 file; 0 tracked files under `context/planning/weeks/`. The four DISPATCH-READY/LIVE instruction files present are exactly the four excluded.

## §3 The five HEADs at the instrument (one call, 22:5x Z)
| Repo | HEAD | porcelain (`-uall`) | ahead of origin | locks |
|---|---|---|---|---|
| core | `40412f9` feat(state-store,lifecycle): IR-61b | 0 | 0 | 0 |
| hivemind | `8a062da` hivemind: v84 beat 6 | 19 (9 M + 10 ??) — Part C's card, unrun | 0 | 0 |
| skills | `180375f` W-SKILLS-9 (the FE half) | 0 | 0 | 0 |
| bench | `352296d` VERIFY-72H-A2 | 0 | 0 | 0 |
| docs | `7221ddc` AMD-101 §6 | 0 | 0 | 0 |

No drift from the record. The Java slot FREE (core porcelain 0 — PJ-2 not yet dispatched); the bench slot FREE. `_scratch/v85/` holds the packet (8,301 B), the three retired message files and the live one (`…_v85-b1b2b3b4_commit-msg.txt`).

## §4 The dispatch text and the first message
`context/handoff/2026-09-28_v86_dispatch-text.md`: 12,882 B, md5 `527f0bd836b2…`, `status: LIVE — cut v85 beat 4`. The pasted text was checked against it at six anchors, each found exactly once: the identity line, the splice library's md5, the REFUSE head, the READ BEYOND head, the MY FIRST MESSAGE head, the sixth-beat/60 % close rule. The pasted text IS that file; it is not filed twice. Nick's first message (17:47 CT: "Time now is 1747 CT on 9/28 and we have 3-4 hours left in the day …") filed verbatim at `_scratch/v86/2026-09-28_v86_first-message_as-pasted.txt` (255 B). Read as `TIME: 17:47 CT` · `HOURS: ~3–4` (to ≈ 21:00–21:45 CT).

## §5 EXPORT-1 — the pre-registration (filed BEFORE Part B's line; adjudicated first at its intake)
The instrument: Part B's `_scratch/v85/2026-09-28_EXPORT-1_outputs.txt` + the copy `_archive/runs/2026-09-28_rehearsal-1/` (`verdict.json`, `report.md`, `window.json`, `MANIFEST.txt`, `events.jsonl`). The window 17:15:00Z–18:50:00Z.
- **P-X1 (the export):** one `export-dir:` line; `rows:` between 3,000 and 6,000 (the kill's own span wrote 3,193 rows 12:21→13:06 CT; the window is 95 min). FAILS on: no directory, or rows outside that band (then the band was mis-derived and the store's cadence is re-read from `window.json`'s min/max positions).
- **P-X2 (the verdict):** the word is one of the frozen vocabulary + `CANNOT-GRADE`; my prediction is **NOT PASS** — exit 2 or 3 — because a first real window carries at least one event type outside the grader's whitelist (invariant (iv) → CANNOT-GRADE naming the first unplaced event) or an opaque `command_result` (decision 4 → CANNOT-GRADE with the count). A PASS on the first real window refutes this and is the surprise to read hardest. A CANNOT-GRADE is a RESULT that names the next lane (a whitelist row or a decrypting export), never a guess.
- **P-X3 (IR-94, the walk run `01M3MM0QXR3QF7MDX5AJ60H05W`):** `walk-run-rows ≥ 2` (`automation_triggered` + `automation_completed`); ≥ 4 if the bench-hero's command was dispatched (`command_issued` · `command_dispatched` · `command_confirmation_timed_out` carrying the run's id in `causation_id`/`correlation_id`). Adjudicated on `events.jsonl` by the id, the event types listed in position order.
- **A1/A2/A3:** A1 = 0 `permit_join_opened` (the key ABSENT); A2 applicable (core `1f1d1e0` on the card → `staleAfter` live) but the window has no runner captures → the grader says NOT-APPLICABLE or reads the store alone; A3 = no REP receipts in the window (no bundle ran) → NOT-APPLICABLE.

## §6 The hold on the tree
Part C's card reads `Porcelain before: 19` and `staged: 19 (expect 19)`; a byte written into `nexsys-hivemind/` before it runs re-cuts the card (D-v85-19's refutable-by) and confuses Nick's read. So beat 1 writes NOTHING into the hivemind tree: this audit, the v86 DR and the beat's spine texts are authored under `_scratch/v86/` and spliced in ONE guarded splice (every cap probed in one printed block) after `HIVE: LANDED`, with the intakes of Parts A and B in the same beat.

## §7 Not re-executed (disclosed)
The Pi (no read of the rig from here); the CI run on `a5b9e33` (its line still OPEN); Check 7's one uncovered `include(` (the count 21/22 is carried from v85 b1's PASS); the byte-identity of the pasted dispatch text beyond the six anchors (its md5 could not be taken on the paste itself).
