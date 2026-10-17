<!--
file: context/strategy/2026-10-17_DELIB-1_outline_the-Oct-12-notes-against-the-record_and-pass-3.md
purpose: the OUTLINE of the deliberation the record dates for Sunday (D-v111-43 (4): Nick's §B–§D of 2026-10-12 tested against the record; ≤ 10 KB; ROADMAP-1's seed) and of pass 3 (ROADMAP-1 = the strategy of record v2, Dec 1) — the order Sunday's session takes, the evidence each section stands on, the hub's lean, and the decisions that are Nick's. v112's deliverable; v113 writes the deliberation itself from it.
audience: the v113 hub (Sunday's quiet half) · Nick (the leans to push back on; the eight questions) · ROADMAP-1 (Nov 10 → Dec 1)
state-type: strategy outline (not a ruling; nothing here binds until Nick rules it)
status: FILED v112 b6 (Sat 2026-10-17) — from the source pack `audits/2026-10-17_v112-b6_DELIB-PACK_source-pack.md` (a hub-side helper's, every row cited; 69 cited lines spot-checked by its script); the hub re-reads every row it rules on, Sunday
-->

# DELIB-1 — your Oct 12 notes against the record, and pass 3's outline

Your §B–§D (`planning/2026-10-12_v110_decision-record.md:27–97`) asked three things: is the plan right (§B), is the runtime right (§C), is the process right (§D). Five days on, the record answers most of §B, sharpens §C, and contradicts the premise of §D's request — the process got heavier. Sunday's deliberation runs in the four sections below, then adopts pass 3's outline (§5) and puts the eight questions (§6) in front of you.

## §1 §B, the plan — where each item stands (the pack §1, B1–B11)
- **Done or re-dated:** GATE-2 (B2: 1,714 timeouts = Hue 1,671 · S31 43; `N3:` by Oct 20, the hub leans (c)) · SCHEMA-1 early (B3; `RETENTION:` by Nov 2 — the lean corrected to (c′), D-v112-30) · pass 2 ruled and mapped (B6).
- **Re-planned by fact:** B1's MG24 reflash — no 7.4.x image existed (D-v111-36) → `KIT-DONGLE: both`; the MG21's first pairing a corpus entry on PI-2 — and PI-2's draft is not runnable as written (IR-222), DRAFT-3 in v113.
- **Open, and outside the hub's hands:** N1 (B4) — counsel is the pilot's longest pole (IR-218: the flip or a per-household permission before the first outside install; LICENSE-1's consent needs re-scoping for (b), IR-217).
- **Untested:** B5's hours (≈ 29 of yours in nine weeks, on paper; the hours spent are not recorded) · B7's "one strategy file that replaces the others" (one was added since — the R&D guide).
- **The lean:** §B holds; the one item to change is the pilot's critical path, which now runs through counsel and the kit rather than through code.

## §2 §C, the runtime — tested against the record (C1–C13; anchors A1, A2, A4)
- **What the record now shows:** none of HORIZON-1's bottlenecks is a language problem (C2 — IR-148, which looked like JVM startup, was a whole-log walk fixed in Java: 0.584 s cold on 2.32 M events, A4) · Java is memory-safe (C3) · startup is not today's cost (C4, A4) · footprint at today's store is UNKNOWN (A2: the only RSS on record is July's 205–212 MB at 13,790 events) · C7 ("nothing measured on the Pi") was already false on Oct 12 (X1).
- **What it cannot yet show:** the board case for Rust (C5) has no target — no 1–2 GB board or BOM is on record, and the price gap is about $15 a hub · the cheaper fixes (C6: JDK 25 + FFM `sd_notify`, the AOT cache, heap tuning, native-image) have no measurement · IR-197's watchdog transport is contested inside the record (A1, X2).
- **The lean:** Java stays for the core (C9); a second language waits for a measured trigger, and LTD-01 already holds the triggers (RSS > 2.5 GB, GC > 500 ms, carriers > 75 % — C11, one place); RUNTIME-1 is a measurement, scheduled where it touches no run and no household (PI-2 is the first household's hub — the guide keeps experiments off it; a spare card on hs-dev-1 after the run is the honest place).
- **Yours:** Q2 · Q3 · Q4 · Q6 · Q8 (§6).

## §3 §D, the process — the measure moved the wrong way (D1–D3; X5)
- **The two measures you asked for:** spine-touching commits 75 % (v110) → 100 % (v111) → 100 % (v112); cards 7 → 9 → v112's count at its close. The DR bytes per window: 32,551 · 71,058 · v112's at its close. The caps rose by named edit; no rule retires a rule; the measurement ledger stopped on Sep 28, so today's numbers live in audits only.
- **What worked this weekend:** independent checks before a hand (BC11's six cuts; PI-2's clone hazard; the RETENTION invariant) and lanes in parallel (HERO-U4 in 50 minutes).
- **The lean:** nothing re-plumbed before the run (the riskier move); PROCESS-2 (Nov 3 →) does three things — (1) a beat writes the DR and `state.yaml` and nothing else by default (the chain line, the snapshot chain and the beat block retire or render from them); (2) one measurement ledger revived as the one place for numbers; (3) a retirement rule — a law not cited in thirty days is archived. The process then measures itself by the same two numbers, and they must fall.

## §4 The seven weeks (A5) — what gates what
Oct 18 BC11 (the rollback slot) · Oct 19 the bench-boot sitting (reads BC11's P5, IR-221) · Oct 20 `N3:` · Oct 21 AVAIL-2's return (Q1 → dry-run #2's packet) · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run · Nov 2 `LICENSE:` and `RETENTION:` · Nov 3–9 the flip and TAIL-1's trial · by ≈ Nov 10 PI-2's two sittings (the kit) and the kit list · Nov 18 the two gates (a fresh-card end-to-end; the filing receipt) or the outside installs slip to December · Nov 19–25 the first outside install · Nov 10 → Dec 1 ROADMAP-1. **The pilot's three poles are yours or the run's:** counsel, the kit, the verdict.

## §5 Pass 3's outline — ROADMAP-1, the strategy of record v2 (Dec 1)
One file that replaces the scattered ones (B7):
1. **The thesis and the beachhead** — one page; what the run and the pilot proved, by their numbers.
2. **The product as built** — the record's facts only (the run's verdict, the pilot's first homes, the claims register as filed).
3. **The one-way doors, dated** (B8) — the license, retention, the on-disk format at the first household event, ACK-1's vocabulary, the name.
4. **The R&D program and the 2027 skeleton** (A6) — HORIZON-1's Q1 lanes and the guide's B-1 → B-4 path reconciled into one quarter-by-quarter plan (Q1 in §6 decides the frame); the guide's sensing branch and P-12..P-15 enter only through this test.
5. **The runtime ADR** — LTD-01 kept or amended in place (Q8), with RUNTIME-1's numbers.
6. **The process plan** — PROCESS-2's three changes and its two measures.
7. **The company plan** — counsel and the license; the pilot's pace (one, two or three homes by Nov 25: Q5 — the record says all three); the money it needs.
8. **What it retires** — the strategy files it replaces, listed by path, archived the day it is ratified.

## §6 The eight questions (yours; in the order their decisions fall due)
1. **Q5 (before Nov 18):** one outside home by Nov 25, two, or three? (X7: the guide, OUTREACH-2 and THE HORIZON each say a different number.)
2. **Q7 (before the pilot's build):** keep-everything grows past the board's free page cache around Dec 8 — accept the rebuild exposure until R3's snapshot rule lands, or bound it sooner (the (c′) mark)?
3. **Q4 (post-run):** the watchdog — IR-197's child process now, or FFM with the move to JDK 25 — and when?
4. **Q2 (with the kit list):** is a 1–2 GB board a target? Is PI-2 a 4 GB or an 8 GB board, and is it the first home's hub?
5. **Q6 (post-run):** RUNTIME-1 on a spare card in hs-dev-1, after the run — yes?
6. **Q8 (pass 3):** the runtime ADR — amend LTD-01 in place, or a new record?
7. **Q3 (pass 3):** does "no new C/C++" bind a signed device of our own (the guide plans one on the nRF Connect SDK or an EFR32MG24 — X4)?
8. **Q1 (pass 3):** the 2027 frame — HORIZON-1's Q1 lanes, or the guide's B-1 → B-4?

## §7 The contradictions the deliberation resolves (X1–X7)
X1 C7 false on Oct 12 · X2 IR-197 corrects F6 without August's caveats · X3 B1's MG24 reflash impossible · X4 "no new C/C++" against the guide's node · X5 §D's "lighter" against the 100 % · X6 the guide's "45 s against a 30 s gate" prices a rebuild, not a boot · X7 Nov 25's pace in three numbers.
