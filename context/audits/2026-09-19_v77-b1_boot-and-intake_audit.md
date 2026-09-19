<!--
file: context/audits/2026-09-19_v77-b1_boot-and-intake_audit.md
purpose: v77 beat 1 — the boot at the instrument: the read-set at the bytes, the five HEADs, the preflight (12 lines), the two shas of the b8 cards verified at census, Nick's paste diffed against the filed v77 text, the window's ONE deliverable, the reconciliation of Check 12, the spine rotation.
audience: the v77 hub (every later beat) · Nick (§0 only)
state-type: boot audit (dated; never edited after the beat)
status: FILED Sat 2026-09-19 ~08:0x CT (instrument 2026-09-19T13:09:00Z)
-->

# v77 beat 1 — the boot and the intake at the instrument

## §0 One screen
- **The clock:** `date -u` → `Sat Sep 19 12:56:31 UTC 2026` at the first call; CT = UTC−5 → Sat 2026-09-19 ~07:5x CT. The splice's own reading: 2026-09-19T13:09:00Z.
- **The five HEADs (one call):** core `d1c2cbc` · hivemind `ad273c2` · skills `180375f` · bench `fa01cad` · docs `7221ddc`; porcelain 0 in every repo; `origin/main..HEAD` 0 in every repo; no `.git/*.lock` anywhere. The dispatch line's two placeholders are filled by the instrument: `<the b8 sha>` = `ad273c2`, `<the BM1B sha>` = `fa01cad`.
- **The two cards verified at census, not at word:** `ad273c2` = 8 paths = 6 M + 2 A, the b8 order exactly (the two A: the 1b return, the b8 audit; the six M: the v77 text, the brief, the chains archive, pm-handoff, the plan, the snapshot); `fa01cad` = 4 M, the 1b table exactly (`scenarios/SCENARIO_FORMAT.md`, `scenarios/metering-known-load.yaml`, `tools/runner/engine.py`, `tools/runner/test_engine.py`). Both pushed (ahead 0). The words `BENCH: BM1B fa01cad` and `HIVE: LANDED ad273c2` bank from porcelain; Nick did not have to type them.
- **The paste = the filed text at the bytes:** Nick's dispatch text, saved as received to `_scratch/v77/2026-09-19_v77_dispatch-paste_as-received.md` (11,598 B), diffed against `context/handoff/2026-09-18_v77_dispatch-text.md` (12,744 B) after its frontmatter: the only differences are the file's `# v77 — the dispatch text` heading and its two fence lines. The filed text is therefore the dispatch of record verbatim; its `status:` line is marked PASTED at this beat (a frontmatter edit; the body untouched). No second copy is filed.
- **The preflight: 12/12 after one reconciliation** (§4) — Check 9 28/28 identical at the bytes; Check 12 was STALE on three landed charters (ENERGY-READ, BENCH-METER-1, BENCH-METER-1b still `DISPATCH-READY`) → each marked `EXECUTED` with its prior status kept after `Was:`, bodies untouched, in this beat's census.
- **The window's ONE deliverable:** THE THURSDAY ORDER step 0 done — Sunday's two intakes (H8-a, R-5B) CLOSED two-layer on `R5B-2:` and the Pi pull card handed → `PI: pulled <sha>`. Saturday's block toward it: MEASURE-2b through THE PREMISE GATE (beat 2; the paste before 09:45 CT or after the sitting), then the knockout charter, VERDICT-VOCAB-1 and PELTON-READY drafted while Nick is at the rig (no asks).
- **The act:** the b1 hivemind card (10 = 8 M + 2 A) → `HIVE: LANDED <sha>`. Nothing else before the sitting unless beat 2 is dispatch-ready before 09:45.

## §1 The boot read-set at the bytes (the budget ≤45 KB)
(a) the orchestrator prompt whole 13,017 · (b) `pm-handoff.md` line 8 2,008 + the newest beat (lines 15–22) 2,350 · (c) `PROJECT_SNAPSHOT.md` whole 3,495 · (d) the operator brief whole 12,246 · (e) the v76 DR §3 5,005 · (f) the plan §17 5,140 + §2 the first 1,700 of 3,487 (trimmed to the budget; rows 1–4 read, rows 5+ not) · (g) pm-lessons: none read at boot (the three newest entries are read when beat 2's charter sends there). **Total 44,961 B.**

## §2 The record's claims re-executed
| Claim (the dispatch / the b8 beat) | The instrument | Result |
|---|---|---|
| core `d1c2cbc`, 22 files, CI #253 green | `git log -1`; CI not re-read from here (no token; banked at v76 b6 at the instrument) | HEAD ✓; CI **not re-executed** (disclosed) |
| hivemind = the b8 card, 8 = 6 M + 2 A | `git show --name-status ad273c2` | 8 rows: 2 A + 6 M, the paths of the b8 order ✓ |
| bench = the 1b card, 4 M | `git show --name-status fa01cad` | 4 M, the table ✓ |
| the 1b return's last line | `tail -1 context/audits/2026-09-19_BENCH-METER-1b_return.md` | `RETURNED nexsys-hivemind/context/audits/2026-09-19_BENCH-METER-1b_return.md 5780` ✓ (5,780 B on disk) |
| the b8 audit filed | `git ls-files` + `wc -c` | 13,090 B ✓ |
| the splice library md5 | `md5sum context/process/splice_lib_v1.py` | `d6780d1302288b85910a1e44315703ec` ✓ |
| the Pi runs the OLD engine until `PI: pulled` | not reachable from here | **not re-executed**; `PI: pulled <sha>` is the instrument (Sunday) |
| the sitting's pins (`6bd8508`, run #56; the packets untouched) | the two packets' `status:` lines read (LIVE; re-pinned v75 b1; not edited since) | consistent ✓; the artifacts' presence not re-read (GUARD 1 downloads on the day) |

## §3 The paste diff (§0's fourth line, the command)
`diff <(sed '1,/^-->/d' the-filed-text | sed '/^$/d') <(sed '/^$/d' the-paste)` → three lines: `1,2d0` (the heading + the opening fence) and `17d14` (the closing fence). Every other line identical.

## §4 The preflight, one line per check
1. Snapshot `last-verified: 2026-09-19` (v76 b8) vs the newest commits (hivemind `ad273c2`, bench `fa01cad`, both 07:53 CT today; the snapshot's own order, landed) — PASS.
2. The plan of record resolves: `context/planning/2026-09-15_v75_PROGRAM-PLAN_the-six-weeks-to-the-72-hour-run.md` 41,417 B, §18 the newest addendum — PASS.
3. Recent commits vs the snapshot: five of five HEADs are the snapshot's state or its predicted landings (`90e3348` + b8 → `ad273c2`; `764e537` + 1b → `fa01cad`) — PASS.
4. Milestone consistency: the plan §2 row 1 = today's sitting; row 3 ENERGY-READ landed (§17); the counter 8/20 — PASS.
5. Open Risks: `## Open Risks` at :111; 8 `#### OR-` blocks = the snapshot's "eight" — PASS.
6. `coder-handoff.md` next-WU pointer: MEASURE-2b (hub-authored at v77), then LINK-READ — PASS (matches D-v76-10).
7. MODULE_CONTEXT.md: 21 files for 22 `include(` lines; the one without is `spike/wal-validation` (a spike, not a Phase-2 module) — PASS.
8. `cross-agent-notes.md`: 1,024 B, the retired-channel pointer only; ACTIVE 0 — PASS.
9. The three SOURCE skill trees vs the session's synced copies, per-file md5: **28/28 identical at the bytes** — PASS.
10. Strategic map: every path the dispatch names resolves at its byte count (the naming frame 5,940 + 9,222; the RS-13 ruling 12,043; the engagement tracker 8,815; BRAND-G2-EXEC 12,729; the counsel navigator 19,258; the claim register 14,079; the measurement record 8,238; the improvement register 30,592; the b7 audit 15,278; the b5 audit 15,022; the b3 audit present) — PASS.
11. Source round-trip at `d1c2cbc`: every file the MEASURE-2b brief names exists (`BusSoakIT.java` with `bootAndAdopt` at :144/:309; `HeroLoopHardwareFreeIT.java`; `SqliteEventStore.java`; `SqliteSubscriberReadExecutor.java`; `StandardExplanationService.java` with `SCAN_BATCH = 500` at :115; `RetentionPolicy.SOURCE_DEFAULT` at :46; `ZigbeeHardwareFreeRig.java`; `FakeNcp.java`) — PASS; **one cite off:** `ZigbeeAdoptionSlice.java:377–:378` is the `EndpointClassifier.classify` call, not the `device=` log line — beat 2 re-derives the line by grep before the charter cites it.
12. The archive convention: (2) 0 · (3) 0 · (1) five files — H8-a and R-5B are LIVE by the record (today's sitting); three landed charters STALE → **reconciled in this beat** (`status: EXECUTED — LANDED … Was: DISPATCH-READY …`) — PASS after the edit.

## §5 The spine rotation
The live blocks were 12 (v75 b5 → v76 b8); the cap admits no thirteenth. v75 b5–b8 (4 blocks) rotated VERBATIM into `context/handoff/archive/pm-handoff-beats-v75b5-v75b8-rotated-2026-09-19.md`; the archive-map row added; bytes(kept) + bytes(archived body) = bytes(before) + bytes(the map row), asserted inside the splice before the first byte. The chain: the v76 b7 segment rotated into `archive/chains-rotated-2026-08-27.md` as rotation 143.

## §6 The window (≤8 beats; no new block after 6)
b1 the boot (this) · b2 MEASURE-2b through the gate → the paste (before 09:45 or after the sitting) · b3 the knockout charter DISPATCH-READY + VERDICT-VOCAB-1 + PELTON-READY drafted (Nick at the rig; no asks) · b4 the evening: `H8A:` / `R5B: RETURNED` read at the bytes, the knockout paste · b5 Sunday: `R5B-2:` → the two intakes CLOSED → the Pi pull card (the deliverable) · b6 MEASURE-2b's intake, the core card, LINK-READ through the gate · b7 FE-115 + the strategy pass · b8 the close (Mon–Tue hand to v78's §HELD if the window runs out).
**The alternative shape, rejected:** naming MEASURE-2b as the deliverable — it is the hub's block, but Thursday hangs on the Pi and the intakes, and a window that closes on a charter with the Pi still on the old engine has not moved the run.
**Leverage line:** the two cards banked from porcelain cost Nick no words; the paste diffed identical costs no second file; the rotation now leaves nine live blocks for the weekend's beats.
**2029 test:** why the deliverable is the Sunday close and not the coder paste; why the three charters were marked EXECUTED at a boot beat (Check 12) and not left for a hygiene lane.
