<!--
file: context/audits/2026-09-28_v85-b1_BOOT-and-INTAKE_audit.md
purpose: The v85 hub's beat-1 audit — the boot at the instrument (the read-set inside the byte budget; the five HEADs; the preflight 12/12), Nick's first message intaken at the porcelain, THE ONE DELIVERABLE named and REHEARSAL 1 handed as the noon act on his word ("consider this noon").
audience: the hub (v85 and after) · Nick (§2 and §4 are his)
state-type: audit (beat 1 of v85)
status: FILED — Mon 2026-09-28 ~12:0x CT (instrument 2026-09-28T17:07:29Z)
-->

# v85 beat 1 — the boot and the intake (Mon 2026-09-28 ~12:0x CT; instrument 2026-09-28T17:07:29Z)

## §0 The boot read-set (the v67 prompt §1; the budget ≤ 45 KB = 46,080 B)
| # | File | Range | Bytes |
|---|---|---|---|
| a | `context/handoff/2026-09-06_PM-mission-control_v67_orchestrator_session_prompt.md` | whole | 13,017 |
| b | `context/handoff/pm-handoff.md` | line 8 · the newest beat (lines 15–20, v84 b6) | 1,734 · 2,409 |
| c | `context/status/PROJECT_SNAPSHOT.md` | whole | 3,485 |
| d | `context/handoff/OPERATOR-BRIEF_for-Nick.md` | whole | 12,194 |
| e | `context/planning/2026-09-27_v84_decision-record.md` | §3f + the Carried row (lines 53–58) | 3,295 |
| f | the plan of record · THE WEEKS AHEAD | §30 (lines 219–224) · §7 (lines 54–64) | 2,512 · 2,954 |
| g | `context/lessons/pm-lessons.md` | entries newer than the ledger | 0 (the newest three are dated 2026-09-26, as the dispatch said) |
| | **Total** | | **41,600** |

Reads a block sent the hub to, outside the budget: the v84 b1 audit §3 (the preflight's form, 2.6 KB); the rehearsal packet's status line, §0 and its return sentence (≈ 3 KB, `grep`/`sed`); `_scratch/v84/v84b1_splice_a.py` and the splice library (md5 `d6780d1302288b85910a1e44315703ec` asserted at load).

## §1 The five HEADs at the instrument (one call; 2026-09-28T16:5xZ)
| Repo | HEAD | porcelain (`-uall`) | ahead of origin | locks |
|---|---|---|---|---|
| core | `40412f9` feat(state-store,lifecycle): IR-61b | 0 | 0 | none |
| hivemind | `8a062da` hivemind: v84 beat 6 — THE CLOSE at six | 0 | 0 | none |
| skills | `180375f` skills: W-SKILLS-9 (the FE half) | 0 | 0 | none |
| bench | `352296d` bench: VERIFY-72H-A2 | 0 | 0 | none |
| docs | `7221ddc` docs(amendments): AMD-101 §6 | 0 | 0 | none |

Against the record: core, docs and skills = the newest beat; hivemind `8a062da` = the v84 close card (`diff-tree` 7 M + 4 A; parent `eb1d822`); bench `352296d` = the A2 card (`diff-tree` 5 M; parent `9fa2382`). No drift; nothing to adjudicate.

## §2 Nick's first message, at the porcelain
| His line | The instrument | The reading |
|---|---|---|
| `HIVE: LANDED 8a062da` — his terminal paste: `[main 8a062da] … 11 files changed`, `eb1d822..8a062da  main -> main`, the trailer grep `0` | hivemind HEAD `8a062da`, porcelain 0, ahead 0; `diff-tree` 7 M + 4 A; `_scratch/v84/2026-09-28_hivemind_v84-b6_commit-msg.txt` greps 0 | BANKED — v84 CLOSED at the porcelain |
| `BENCH: LANDED 352296d (A2)` — `[main 352296d] … 5 files changed`, `9fa2382..352296d  main -> main`, the grep `0` | bench HEAD `352296d`, porcelain 0, ahead 0; `diff-tree` 5 M; the A2 message file greps 0 | BANKED — VERIFY-72H-A2 EXECUTED at the record; IR-89 CLOSES (D-v84-26's condition) |
| `CI: a5b9e33` | not said | OPEN — the closure counter reads 16; passive (it gates no act) |
| `REH1:` | "current local time is 1147 CT, but we shall consider this noon" | the rehearsal HANDED at 11:5x CT as the noon act (D-v85-1) |
| `TM:` | not said | COMMISSIONED, NOT FILED stands; THE PREMISE holds |
| `HOURS:` | not said | asked at the intake, where it gates BC6 (D-v85-2) |

The dispatch text: `context/handoff/2026-09-28_v85_dispatch-text.md` (11,152 B; md5 `8c72df74ef259d52426c9f814e5fa575`; the body from line 9: 10,046 B, md5 `78c64c2cfd87c8b34fbc8e3c6230b8f4`). The paste matched the file at its first sentence, its last sentence and four distinctive strings (the library md5; IR-92's `ApiResponse.java:14` line; the `REH1: <at 12:00 | RETURNED` slot; the dispatch-of-record sentence). A whole-paste diff was NOT run: the paste is the file's own body, handed to him by v84's §NEXT. Its status flips LIVE → PASTED this beat. His terminal paste is filed whole at `_scratch/v85/2026-09-28_v85_first-message_as-pasted.txt`.

## §3 The preflight (one line per check)
1. PASS — the snapshot `last-verified: 2026-09-28 (v84 beat 6` = the handoff chain's newest segment.
2. PASS — the plan of record resolves (§30 at its path; the two `*plan-of-record.md` files present).
3. PASS — core HEAD `40412f9` = the snapshot's.
4. PASS — `phase-3-milestone-backlog.md` present (29 DONE rows); the per-milestone triple not re-run (unchanged since v81 b1's 12/12).
5. PASS — the Open Risks section's newest date reads 2026-09-23 by this boot's grep of the section (5 days; the rule is 7); the v84 b1 audit read 2026-09-27 by its own instrument — both inside the rule, the section unedited (D-v85-8).
6. PASS — coder-handoff's chain names PJ-2 as the NEXT WU (`PJ2: endpoint` GIVEN; reviewed before its dispatch line).
7. PASS — 22 modules in `settings.gradle.kts`; MODULE_CONTEXT.md for 21 (`spike/wal-validation` the known absence).
8. PASS — cross-agent-notes the retired stub (ARCHIVED-WITH-POINTER; 1,024 B).
9. PASS — the three SOURCE skill trees vs the session's synced copies: 28/28 files, per-file md5 identical (the sorted lists' md5 `25d6572b0d07ce6550caff0d1c6cfc03` on both sides; the device side's list at `_scratch/v85/2026-09-28_v85-b1_device-skills-md5.txt`).
10. PASS — the strategic context map unchanged since `30f800d` (2026-09-07); its resolution not re-run this boot — carried from v83 b1.
11. PASS — the v84 b6 audit's `ApiResponse.java` :12–:15 resolve at `40412f9` (the Javadoc's `SNAKE_CASE` clause is in the tree — IR-92's premise stands).
12. PASS — 0 / 0 / 0; the exclusion list as run: `2026-09-27_REHEARSAL-1_…operator-session-prompt.md` (DISPATCH-READY; handed this beat), `2026-09-27_desk-lane_KREFRESH-1_…charter.md` (DISPATCH-READY; after the intake), `2026-09-28_desk-lane_W-SKILLS-10_…charter.md` (today's date; Wednesday by Nick's word); the CT date 2026-09-28; one LIVE orchestrator prompt (v67); `context/planning/weeks/` 0 tracked.

## §4 The window (D-v85-2)
| Beat | When | The work | Nick's hands |
|---|---|---|---|
| b1 | Mon 11:48 → | the boot; the intake; REHEARSAL 1 handed at noon; the v85 DR; the brief; the spine. While the sitting runs: PJ-2's instruction authored on WU-PJ2, its independent review filed | the rehearsal's paste; `REH1: RETURNED …` |
| b2 | on the return | THE DELIVERABLE'S INTAKE two-layer (P1–P6 first; THE MEASUREMENT RECORD; sample 4 → D-v83-17; IR-83; the S31 → IR-88); the packet → EXECUTED; BENCH-PULL-3 handed; EXPORT-1 cut from the sitting's stamps; ONE hivemind card (b1 + b2) | BENCH-PULL-3; EXPORT-1; the card |
| b3 | afternoon | EXPORT-1's grade read two-layer; KREFRESH-1 handed; PJ-2's dispatch line; `OUTREACH:` lines; the docs card if the desk is quiet | KREFRESH-1's paste; PJ-2's line; `OUTREACH:` |
| b4 | evening, only inside the hardware rules | BENCH-CORE-6 by the BC5 form through the prior-ledger gate (PI-PROBE-3 inside; P4 sample 5); Tuesday's nightly pre-registered on the named pair; else BC6 to Tuesday | the BC6 card |
| b5–b6 | the close | v86's text (Tuesday evening: the strategy pass); the DR closed; the close on the intake or EXPORT-1's grade, never on a cliff | the close card |

## §5 Layer 2 — re-executed and not
Re-executed: the HEADs, porcelains, push counts and lock listings; `8a062da`'s and `352296d`'s name-status censuses and parents; both message files' trailer greps; the twelve checks at their instruments (Check 9 both sides; Check 12's three greps with the list re-derived); the dispatch text's size, md5 and status line; the rehearsal packet's status line, pre-conditions and return sentence. Not re-executed: the Pi (untouched — the fleet, the key and the bench card's core are the record's, re-read by the guide's STATE line at action 0); the CI run on `a5b9e33` (Nick's line owed); Check 4's per-row triple and Check 10's resolution (carried; their inputs unchanged at `git log`); a whole-paste diff of the dispatch text (the paste is the file's body).

The splice: `_scratch/v85/v85b1_splice_a.py` failed its PHASE-0 probe (the snapshot at 3,691 B > the 3,500 B cap; nothing written; the porcelain clean after — THE GUARDED-SPLICE LAW held); `v85b1_splice_b.py` failed the same probe at 3,566 B; `v85b1_splice_c.py` passed the snapshot and failed the brief's cap at 12,442 B — the three scripts asserted the caps ONE AT A TIME, so each run found one (the PROBE-EVERY-CAP RULE's letter: one block, every region); `v85b1_splice_d.py` measures every capped region in one printed probe, trims the brief (the Java-slot row's history folded to shas; §NEXT and the Given line shortened) and ran. The library `context/process/splice_lib_v1.py` md5-asserted at load.

## §6 PJ-2 — the desk while the sitting ran (D-v85-5, D-v85-9, D-v85-10)
The instruction cut (`context/instructions/2026-09-28_coder-lane_PJ2_pairing-window-endpoint_permit-join-events_coding-instruction.md`: 39,582 B at the draft, 49,709 B after the re-cut) on WU-PJ2's §1 re-run at `40412f9` — every line number held; the design fork's option (a) on `PJ2: endpoint`. The review by an agent that had not seen the authoring, on 25 flat copies at `_scratch/v85/review-src/` (the deep Java paths cannot be staged — 10 folders below the connected folder, the bridge's cap is 7; the flat copy is v84's workaround); verdict RE-CUT, E1–E14 (`context/audits/2026-09-28_PJ2_independent-review.md`). Re-executed by the hub before applying: E1 `Z` :914 `protocol.enablePreconfiguredKeyJoins();` precedes :915 `permitJoin`; E2 `IntegrationEventTypeAnnotationTest` :54 (`List<Class<? extends IntegrationLifecycleEvent>>`), :147 (the prefix), :169 (`isEqualTo(10L)`); E3 nine `published()).isEmpty()` lines (Rejoin :286, :313, :360, :444, :647, :675, :696; TCJ :293, :377 — the reviewer's TCJ :263 not matched by the hub's grep; the Coder reads each); E4 `Z` :246–:257 (run-thread confined); E5 `runCycleOnce()` :572; E6 `bootProduction` :265–:283 (`initialize()` + `awaitNetworkUp()`, no `run()`) and `logCapture` :71–:79; E8 `RestFilters` :580 stores the identity, `TokenAdminEndpoints` :252 reads `caller.keyId()`; E10 state-store `requires transitive com.homesynapse.platform` :10 — `IntegrationId` IS readable through rest-api's chain, so the port keeps the type (the finding resolved the other way, said in the instruction's row 13); E12 `respondAccepted` :364–:383 the `{data, meta}` envelope; E14 the HTTP install (:1103) runs from Phase 5 (:841) before Phase 6 assigns the supervisor (:870). Not re-executed: E7's :223/:225 and :346–:356, E9's :235–:243, E11's :804, the reviewer's line-citation table beyond the ten above. The bench fence (D-v85-10) is the register's next row at the landing.
