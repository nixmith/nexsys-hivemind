<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-12 (v71 beat 4 — AMD-101 authored (a realization correction: Doc 01 §3.4 already says notify-then-poll) and BUS-ORDER-1's instruction ISSUE-READY, gated on the EXPLAIN-114a landing; the docs card queued, Sat 2026-09-12 ~16:1x CT (2026-09-12T21:15Z). Order: hivemind 22 = 12 M + 10 A (computed from porcelain inside the splice); docs 1 A (Nick's hands). Detail: pm-handoff v71 beat 4.) Prior: 2026-09-12 (v71 beat 3 — core `72efb42` LANDED, CI GREEN = sample #14 (artifact owed); `BUSFIX: b` RULED and filed with Nick's acceptance bar; BUS-ORDER-1 after EXPLAIN-114a; EXPLAIN-114a re-baselined to `72efb42` and handed, Sat 2026-09-12 ~16:0x CT (2026-09-12T21:09Z). Order: hivemind 21 = 12 M + 9 A (computed from porcelain inside the splice). Detail: pm-handoff v71 beat 3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v71 beat 4 — (i) landed `72efb42`, CI green; the bus fix ruled (b); EXPLAIN-114a in Nick's hands, Sat 2026-09-12 ~16:0x CT)

**State:** core `72efb42` (FIX-2b-ii (i); `check` · install-smoke · `bus-soak` GREEN = sample #14, the first with the instrument; artifact owed); hivemind `e16eb06` + b1–b3 (12 M + 9 A); docs `73c204b`. **The class:** (1) the soak's stall after `automation_triggered` — instrumented by (i)'s four tokens; (2) the census's `missed=1` at the head — REV-1: out-of-order delivery on a non-monotonic checkpoint (benign) beside a guard drop of a late notify (harmful, kind E). **Ruled and authored:** `BUSFIX: b` = **BUS-ORDER-1** (AMD-101 PROPOSED in docs — a realization correction; the instruction ISSUE-READY; after EXPLAIN-114a; closes on twenty green samples with kind E at zero; reverts to (c) on ten silent samples + a green REPRO-1). **In Nick's hands:** EXPLAIN-114a's paste (re-baselined to `72efb42`). **Then:** the hivemind card · HERO-1c (b5) · R-4c today · the EXPLAIN intake (v72 if long). **Owed:** `SAMPLE: 72efb42` · `H8A:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done`. Skills `c630c5c` · bench `4539f13`. Check 9 STALE.

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP: two faces; the notify-reorder drop proven at source; BUS-ORDER-1 ruled · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.
