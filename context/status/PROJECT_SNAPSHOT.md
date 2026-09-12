<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-12 (v71 beat 5, THE CLOSE — EXPLAIN-114a RETURNED and audited ACCEPT WITH ONE CORRECTION (R3, the paste = the one act; the core card 13 M after it); sample #14 GREEN with the instrument (silent 1/10); REPRO-1 GREEN (K=200, two carriers); hivemind `7ecaffa`, docs `0d62a54`; v72 opens on the R3 return → the core card → `BUSORDER: go`; HERO-1c; 114b, Sat 2026-09-12 ~18:1x CT (2026-09-12T23:13Z). Order: hivemind by explicit paths (computed from porcelain inside the splice); core 13 M (Nick's hands). Detail: pm-handoff v71 beat 5.) Prior: 2026-09-12 (v71 beat 4 — AMD-101 authored (a realization correction: Doc 01 §3.4 already says notify-then-poll) and BUS-ORDER-1's instruction ISSUE-READY, gated on the EXPLAIN-114a landing; the docs card queued, Sat 2026-09-12 ~16:1x CT (2026-09-12T21:15Z). Order: hivemind 22 = 12 M + 10 A (computed from porcelain inside the splice); docs 1 A (Nick's hands). Detail: pm-handoff v71 beat 4.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v71 CLOSED at beat 5 — EXPLAIN-114a accepted with one correction; the bus fix ruled (b) and authored; the revert clock 1/10, Sat 2026-09-12 ~18:1x CT)

**State:** core `72efb42` + EXPLAIN-114a's 13 M uncommitted (the R3 correction pending, then Nick's card; `check` on the push = the gate + sample #15); hivemind `7ecaffa` + b5; docs `0d62a54` (AMD-101 PROPOSED). **The bus class:** (1) the soak's stall — instrumented (`72efb42`); (2) the census's head-miss — a notify-order artefact on a non-monotonic checkpoint; kind E names the harmful arm; sample #14 and REPRO-1 green and silent. **Ruled:** `BUSFIX: b` = BUS-ORDER-1 (AMD-101 PROPOSED; the instruction gated on the EXPLAIN landing and `BUSORDER: go`; reverts to (c) at ten silent samples — 1 so far). **v72 opens on:** the R3 return → the EXPLAIN core card (`_scratch/2026-09-12_core_EXPLAIN-114a_commit-msg.txt`) → CI → `BUSORDER: go` → 114b (DISABLED-2 and two refactors) → HERO-1c → `AMD101: ratify` → R-4c's record → the v1.1.4 freeze note. **Owed:** `H8A:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done` · `R4C:`. Check 9 STALE.

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP: two faces; BUS-ORDER-1 ruled; the revert clock 1/10 · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.
