<!--
file: context/audits/2026-09-27_v84-b1_BOOT-and-INTAKE_audit.md
purpose: The v84 hub's beat-1 audit — the boot at the instrument (the read-set inside the byte budget; the five HEADs; the preflight 12/12), Nick's paste and his one message intaken at the bytes, the window re-shaped (v84 opened Sunday evening, not Monday morning), THE ONE DELIVERABLE named.
audience: the hub · Nick · v85
state-type: audit (filed once; never edited)
status: FILED — Sun 2026-09-27 ~20:0x CT (instrument 2026-09-28T01:01:01Z)
-->

# v84 beat 1 — the boot and the intake

## §0 Verdict
BOOT CLEAN (12/12; the HEADs = the record with the two expected deltas: hivemind `db5e0bc` = the close card, bench porcelain 9 = VERIFY-72H-A's returned tree). THE ONE DELIVERABLE: REHEARSAL 1 EXECUTED Monday at `REH1:`'s hour (defaulted 12:00 CT) and intaken the same day (D-v84-1). The window re-shaped to open tonight at the desk (D-v84-2). The decisions: `context/planning/2026-09-27_v84_decision-record.md` (D-v84-1..9).

## §1 The boot at the instrument
- `date -u` 2026-09-28T00:44:53Z at the first call; CT = UTC−5 → Sun 2026-09-27 19:44 CT. The beat's stamp 2026-09-28T01:01:01Z (Sun 2026-09-27 ~20:0x CT).
- **The read-set 39,672 B of the 45 KB budget:** the prompt §0–§1b 10,090 (lines 9–33) · pm-handoff line 8 1,622 · the v83 b4 beat 2,465 · the snapshot 3,473 · the brief 12,240 · the v83 DR §3d + Carried 2,246 + the two Carried rows · the plan §30 2,512 · THE WEEKS AHEAD §7 2,954 · the hub-read §5 634 (the four words' options, read to record D-v84-4 exactly); pm-lessons: nothing newer than the three of 2026-09-26 (the last three headings dated 2026-09-26).
- **The five HEADs (one call):** core `1f1d1e0` porcelain 0 ahead 0 · hivemind `db5e0bc` porcelain 1 (`?? context/audits/2026-09-27_VERIFY-72H-A_return.md`) ahead 0 · skills `180375f` 0/0 · bench `58b5b45` porcelain 9 (4 M + 5 ??) ahead 0 · docs `7221ddc` 0/0; no `.git/*.lock` in core, hivemind or bench. `db5e0bc` = the b3 + b4 card: 8 M + 8 A, parent `ba313ad`, 18:35:05 CT, 0 trailer hits — the census the close card promised.
- The v84 dispatch text: the file's body (from line 9) 11,107 B, md5 `329854011566acdfa4d35ed403aa2a2e`; the paste as received re-typed to `_scratch/v84/2026-09-27_v84_dispatch-text_as-pasted.md` (11,108 B) — `diff` = one blank line (a paragraph break between the STATE and MY FIRST MESSAGE paragraphs); every other byte equal. The file on disk is the record.

## §2 The intake of Nick's message (19:44 CT) at the bytes
| Line | Said | Read at the instrument | Verdict |
|---|---|---|---|
| `HIVE: LANDED <sha>` | not yet said | hivemind HEAD `db5e0bc`, the b3 + b4 message (8 M + 8 A), porcelain 1 = the return only | LANDED — banked at the porcelain (D-v84-5) |
| `V72HA: RETURNED context/audits/2026-09-27_VERIFY-72H-A_return.md 8172` | said | the file EXISTS, 8,172 B, saved 23:30Z (18:30 CT), last line `RETURNED … 8172`; bench porcelain 9 = its §0 P6 list byte for byte | VERIFIED; the intake at b2 |
| `NIGHTLY:` | — | Mon 03:30 CT is the first on `1f1d1e0`; `tools/nightly.sh` pulls nothing (`git grep 'git pull\|git fetch'` at `58b5b45`: one docs line, no script) | NOT YET; the pre-registration stands |
| `BC5:` | — | the record (D-v83-24) | as the record |
| `REH1: 09:00|12:00` | "whenever" | the record 09:00; his 17:28 word noon | DEFAULTED 12:00; rec 09:00 (D-v84-3) |
| `TM:` | "whenever" | COMMISSIONED, NOT FILED (the brief) | OPEN; THE PREMISE stands |
| the four naming words | "silence = the recs" | the hub-read §5: product · authors · cut · cut | ADOPTED at the recs (D-v84-4) |
| `HOURS:` | — | — | not given; the acts default by the record |

## §3 The preflight (one line per check)
1. PASS — the snapshot `last-verified: 2026-09-27 (v83 beat 4` = the handoff chain's newest segment.
2. PASS — the plan of record resolves (§30 at its path; the two `*plan-of-record.md` files present).
3. PASS — core HEAD `1f1d1e0` = the snapshot's.
4. PASS — `phase-3-milestone-backlog.md` present (29 DONE rows); the per-milestone triple not re-run (unchanged since v81 b1's 12/12).
5. PASS — Open Risks newest date 2026-09-27 (today).
6. PASS — coder-handoff's chain names IR-61b as the NEXT WU.
7. PASS — 22 modules in `settings.gradle.kts`; MODULE_CONTEXT.md for 21 (`spike/wal-validation` the known absence).
8. PASS — cross-agent-notes the retired stub (ARCHIVED-WITH-POINTER; 1,024 B).
9. PASS — the three SOURCE skill trees vs the session's synced copies: 28/28 files, per-file md5 identical (the sorted lists' md5 `a14ecbbb0638af2769fa6fcc17c353dc` on both sides).
10. PASS — the strategic context map unchanged since `30f800d` (2026-09-07); its resolution (100 of 103 cited names; 3 template placeholders) not re-run this boot — carried from v83 b1.
11. PASS — the v83 b4 audit's `awaitProjectionLive()` resolves at `1f1d1e0` (`lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java`, 3 hits).
12. PASS — 0 / 0 / 0; the exclusion list as run: `2026-09-27_REHEARSAL-1_…operator-session-prompt.md` (cut, Monday), `2026-09-27_bench-lane_VERIFY-72H-A_…charter.md` (RUNNING by the v83 b4 beat; RETURNED at this boot — its status flips at b2), `2026-09-27_desk-lane_KREFRESH-1_…charter.md` (DISPATCH-READY); the CT date 2026-09-27; one LIVE orchestrator prompt (v67); `context/planning/weeks/` 0 tracked.

## §4 The window (D-v84-2)
| Beat | When | The work | Nick's hands |
|---|---|---|---|
| b1 | Sun 19:44 → | the boot; the intake; the DR; the brief; the spine | none |
| b2 | Sun evening | VERIFY-72H-A intaken two-layer (the selftests and the grader re-run at the instrument; the fixtures' keys vs the codec); the charter → EXECUTED; the bench card (commit + push tonight; the BENCH-PULL block Monday after the nightly's line) | the bench card |
| b3 | Sun evening | IR-61b's and LOCK-1's instructions authored; IR-61b's independent review filed; the hivemind card for the night | the hivemind card |
| b4 | Mon | the nightly's line banked; the rehearsal at its hour (Nick's paste; the guide paces); IR-61b + LOCK-1 dispatched after the paste; the BENCH-PULL block; PI-PROBE-2 | the paste; two dispatch lines; the pull |
| b5 | Mon | THE DELIVERABLE'S INTAKE two-layer (P1–P6; THE MEASUREMENT RECORD; sample 4 → D-v83-17; IR-83; the S31 → IR-88); EXPORT-1 cut; KREFRESH-1 handed | KREFRESH-1's paste; `OUTREACH:` lines |
| b6 | Mon evening | THE CLOSE: the docs card if the context allows; v85's text (Tuesday evening: the strategy pass) | the close card |

## §5 Layer 2 — re-executed and not
Re-executed: the HEADs, porcelains and push counts; `db5e0bc`'s name-status census; the twelve checks at their instruments (Check 9 both sides; Check 12's three greps); the return file's size, mtime and last line; the bench porcelain against the return's P6 list; the nightly's pull grep; the dispatch text's md5 and the paste's diff. Not re-executed: the return's P1–P5 (b2); the Pi (untouched; the nightly's first line is Monday's); the rehearsal packet's pre-conditions (the guide's STATE line at action 0); Check 4's per-row triple and Check 10's resolution (carried; their inputs unchanged at `git log`).
