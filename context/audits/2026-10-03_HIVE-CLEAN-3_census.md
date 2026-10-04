<!--
file: context/audits/2026-10-03_HIVE-CLEAN-3_census.md
purpose: HIVE-CLEAN-3's read-only census return (charter §3); rows abbreviated here, verbatim + full proofs in the TSV beside it (102 rows).
status: RETURNED — Sun 2026-10-04 ~06:5x CT. Nothing edited, moved, staged or committed.
-->
# HIVE-CLEAN-3 — census return
## §0 Clock · tree · predictions
- `date -u` Sun Oct 4 11:13:43 UTC 2026. Hivemind HEAD `c5166bc` (05:59 CT, "v96 beat 3, the close") = 7 files = SUPERSEDED `card_b3`'s paths, its message; the b3b4 card (9) did NOT run — porcelain ` M …improvement-register.md` (IR-114/115) + `?? …WU-J2_scoped-recovery-window_IR-114.md` (19,530 B): beat 4's files unstaged while HEAD's spine carries beat 4. Core df2bc62 · bench ba846c2 · docs 055832c · skills e9a77a8. My `??`: the two census files.
- P1 TRUE (B:23) · P2 TRUE (H:25) · P3 TRUE (v91:6 LIVE) · P4 TRUE, 9 PASTED (v83–v90, v92; "ten" measures 9) · P5 TRUE, 6/15 · P6 TRUE, this-lane "HIVE-CLEAN-2" in 7 files/17 lines (B 1 · P 4 · v95DR 3 · v96DR 1 · v96 text 4 · b1 audit 2; the register's 2 name the real hygiene lane; snapshot 0) · P7 TRUE (H:112) · P8 TRUE (R:108/:118 end `CLOSED v96 b2 (D-v96-8)`; IR-45 CLOSED; IR-121 stands).
- 58 calls · ≈190 KB read. B brief · H HORIZON · R register · S snapshot · P pm-handoff · T/ handoff.
## §1 Rows (`C-nn path:line "stale" → "correct" · proof`)
### S1 the brief (11)
- C-01 B:23 "State (v81 b1)" → "State (v96 b4)" · B:7 edited at v96 b4
- C-02 B:26 "two gsdk cites owed at its pre-verification (D-v95-4)" → "read at the source; J2 PRE-VERIFIED at df2bc62 (v96 b4, D-v96-14)" · P:8/:15
- C-03 B:28 "(a frontend lane; v96)" → "(a frontend lane; v97, D-v96-11)" · P:21 Sunday's text; v96DR:6 CLOSED
- C-04 B:29 "The bench lane — `0232c69` (…the Pi's clone at `0232c69` by BENCH-PULL-6)" → "— `ba846c2` on main (the Pi's clone 0232c69 until BENCH-PULL-7)" · bench `log -1`
- C-05 B:29 "BENCH-PULL-7 at BC8 (cut; not tonight)" → "(Mon 10-05, v99)" · P:21
- C-06 B:33 "the v96 DR LIVE" → "CLOSED (D-v96-1..14)"; "v84–v95 DRs CLOSED" → "v84–v96" · v96DR:6
- C-07 B:37 Open word "`HIVE: LANDED` (the close card)" → banked by the instrument: c5166bc 05:59 CT · `git log -1`
- C-08 B:39 Given "`HIVE: LANDED 309be17` (v95 b8)" → "c5166bc (v96 b3) · cbfeaec (b1+2) · 309be17" · `git log -3`
- C-09 B:42 "HIVE-CLEAN-2 (D-v95-1..29)" → "HIVE-CLEAN-3 (D-v96-7)" · v96DR:29
- C-10 B:25 Next cell "1b, BC7, BC7b DONE (the v90–v92 DRs) →" → drop (history) · v90/v92 DR:6 CLOSED
- C-11 B:12 "landed today … landed tonight" → "landed Sat 10-03 (df2bc62 16:30; ba846c2 20:34 CT)" · date -u = Sun
### S2 THE HORIZON (7)
- C-12 H:25 "| J1 | Oct 15–17 | LINK-READ-2 if not landed by 10-12" → "LANDED Oct 3 (df2bc62; D-v95-23)" · core `log -1`; v95DR:59
- C-13 H:26 "| J2 | Oct 17–19 |" → LISTED, not moved: J2 PRE-VERIFIED v96 b4 (D-v96-14); Nick's word · P:15
- C-14 H:40 "| B2 | by Oct 11 | VERIFY-72H-B (the desk Sat → lands Sun → BC8)" → "DELIVERED Oct 3; LANDED main ba846c2 (D-v96-8)" · bench `log -1`
- C-15 H:50 "| R1 | Sat 10-03 | rehearsal 2 — … tonight's REJOIN" → "| R1 | Sun 10-04 17:30 (D-v95-25) |" · v95DR:65; P:45
- C-16 H:92 W3 "RULED defer … PAIRING-UX … returns before the" → "→ PAIRING-UX-1 ACCEPT → `WIZARD: b′` (D-v94-24)" · v94DR; 3fe5b4c
- C-17 H:98 W9 word cell "—" (rec "from J1") → "RULED from J1 (D-v95-1)" · v95DR:21
- C-18 H:112 "| Thu 10-15 – Sun 10-18 | the J1/J2 landing cards … (B2 landed by 10-11)" → J1, B2 LANDED Oct 3; J2's card only · as C-12/14
### S3 the register (4)
- C-19 R:6 "status: LIVE — IR-93 CLOSED, IR-81 RETIRED, IR-112..115 minted v90 b6…" → prefix "IR-45 CLOSED v95 b6; IR-96/107 CLOSED v96 b2; IR-116..123 minted" · R:57/:108/:118
- C-20 R:128 IR-117 "rehearsal 2's FIRST card tonight" → "Sun 10-04 17:30 (D-v95-25)" · v95DR:65
- C-21 R:129 IR-118 "will relink Saturday" → "Sunday 10-04 (D-v95-25)" · v95DR:65; P:21 "≈ 54 h dark"
- C-22 R:132 IR-121 "for tonight's P1 (D-v95-13)" → "Sunday's P1 (REHEARSAL 2; D-v95-25)" · v95DR:65; S:16
### S4 the DRs (7) — 16 live DR status lines all CLOSED/FILED
- C-23 v95DR:6 "HIVE-CLEAN-2 chartered for v96" → "HIVE-CLEAN-3 … (id D-v96-7)" · v96DR:29 · C-24/25/26/28/29 v95DR:70/:73 · v96DR:3 · b1 audit:17×2 same fix
- C-27 v95DR:74 "Carried into v96 (final): `V72B: PUSHED PR <n>` · `CI: green | red`" → given PR 2, `BENCH: LANDED ba846c2`; `CI:` RETIRED D-v96-1 · P:27/:33
### S5 the dispatch texts (14)
- C-30 T/2026-10-01_v91_dispatch-text.md:6 "status: LIVE — cut v90 beat 4 …" → "SUPERSEDED — never pasted; folded (v92DR:65); its LINK-READ-2 ran as J1 (D-v95-1/23)" · no v91 DR exists
- C-31…39 T/{v83–v90,v92}_dispatch-text.md:6 "status: PASTED …" → "EXECUTED; Was: PASTED …" · each window's DR:6 CLOSED
- C-40…43 T/2026-10-03_v96_dispatch-text.md:6/:10/:12/:18 "HIVE-CLEAN-2" → "HIVE-CLEAN-3" · v96DR:29
### S6 the instructions (6) — 46 live, 9 non-terminal; gate-excluded: ACCOUNT-2 HELD · HIVE-CLEAN-3 · REHEARSAL-2
- C-44 THURSDAY-ORDER_Half-2:6 "PARTIAL — … T7–T8 SUPERSEDED" → "EXECUTED" · every part terminal · C-45 v81_CHAR-sitting:6 "PARTIAL — … 4–7 SUPERSEDED" → "EXECUTED" · same
- C-46 PJ2_CLOUD-DISPATCH:6 "NOT PASTED FOR THIS RUN" → "SUPERSEDED" · PJ2 EXECUTED, 146468c · C-47 BH3_CLOUD-DISPATCH:6 "PASTED 08:4x CT" → "EXECUTED" · BH-3 EXECUTED · C-48 IR67_CLOUD-DISPATCH:6 "PASTED Wed…" → "EXECUTED" · IR67 EXECUTED · C-49 SENSOR-REJOIN-1:6 "OVERTAKEN" → "SUPERSEDED" · not terminal
### S7 the snapshot (2)
- C-50 S:16 "hivemind `cbfeaec` + the b3b4 card" → "`c5166bc` (the b3 card's 7 paths landed; register + WU-J2 unstaged)" · `git log -1`; porcelain
- C-51 S:16 "NEXT: the b3b4 card; HIVE-CLEAN-3; …" → "the 2 unstaged paths; HIVE-CLEAN-3 running; …" (S:8 Order likewise) · same
### S8 `_scratch/v90–v96` cards (39; 5 marked) — proof: the hivemind commit with the card's file count
- C-52…70 → `_RAN-<sha>` (19: v90 b4,b6 · v92 b1234,b5,b6 · v93 b1,b2,b3b4b5b6 · v94 b1–b5 · v95 b4–b8 · v96 b1b2; the shas in the TSV)
- C-71…80 → `_SUPERSEDED` (subsumed): v90 b1/b2/b3→b4, b5→b6 · v92 b1/b12/b123→b1234 · v93 b3/b3b4/b3b4b5→b3b4b5b6 · C-81…89 docs→055832c · bench→0232c69 · bc7/bc7b RAN · card_sensor Part 1 only · j1 ×2→df2bc62 · v72b ×2→ba846c2 · C-90 card_b3b4 NOT RUN — stands
### S9 K-00 size table (6) — K-00:17/18/19/21/25/27
- C-91…96 `wc -m`: K-03 53,138→53,429 · K-04 38,454→39,087 · K-05 25,788→27,571 · K-07 31,482→32,665 · K-11 49,303→49,576 · K-13 55,880→59,460 (tokens=chars/4); 9 others match
### S10 pm-handoff Open Risks (6) — 10 open of 12; the snapshot's "ten" holds
- C-97 P:126 "Now (v79 b5): … 13/20 at `d22a8a4`" → "Now (v95 b6): 19/20 at `df2bc62` (D-v95-23)" · v95DR:59; S:16
- C-98 P:88 OR-HUE-REPORTING-DEAD: no status since v90 b6 → add "Status 2026-10-03 (v96 b1, D-v96-4; V72B §5 F3): dark Sep 25–28; silent since July" · R:123
- C-99…102 P:33/:36/:39/:40 "HIVE-CLEAN-2" → "HIVE-CLEAN-3" · P:27; v96DR:29
## §2 REHEARSAL 2 packet — date-bound lines (LISTED only; 24,825 B)
- :6 `the sitting opens 17:30 CT Sat 2026-10-03; flips to EXECUTED at v96's intake` → `Sun 2026-10-04 17:30 CT (D-v95-25); … v98's intake` (P:21).
- :14 `≈ 26 h dark` → `≈ 54 h dark` (lastReported 2026-10-02T16:19:36Z → Sun 22:30Z = 54.17 h; P:21 "≈ 54 h").
- :3 `§10 Sat 10-03` → `Sun 10-04 (D-v95-25)` · :3/:11/:21/:65 `tonight` relative, true Sunday · :37 `clone: 5b0e20c` STANDS (P:21).
## §3 Instrument limits (left out)
- B:22 `the fortnight — D-v88-8` (Wed 09-30) runs to 10-14 — not stale · B:39 Given duplicates: `uniq -d` = 0.
- R:118 `:922` already reads "42 lines stale (:964)"; `A:1033` at 5b0e20c IS a PERMIT_JOIN_CLOSED publish (:1007/:1016/:1033) — no row.
- Register cells open `OPEN (v..)`, end `CLOSED` — convention · H:71 `NAMED (tonight; D-v93-15)` unprovable by grep · the Pi's sha from P:21 (no ssh).
RETURNED context/audits/2026-10-03_HIVE-CLEAN-3_census.md 8191