<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-12 (v71 beat 6, THE POST-CLOSE INTAKE — R3 corrected; core `5f918c7` LANDED, `check` GREEN = v1.1.4 FROZEN; the bus-soak job RED `anomalies=1` = sample #15, UNREAD (the one act: the artifact); hivemind `7addbc8`; v72 opens on the read, Sat 2026-09-12 ~18:5x CT (2026-09-12T23:55Z). Order: hivemind by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v71 beat 6.) Prior: 2026-09-12 (v71 beat 5, THE CLOSE — EXPLAIN-114a RETURNED and audited ACCEPT WITH ONE CORRECTION (R3, the paste = the one act; the core card 13 M after it); sample #14 GREEN with the instrument (silent 1/10); REPRO-1 GREEN (K=200, two carriers); hivemind `7ecaffa`, docs `0d62a54`; v72 opens on the R3 return → the core card → `BUSORDER: go`; HERO-1c; 114b, Sat 2026-09-12 ~18:1x CT (2026-09-12T23:13Z). Order: hivemind by explicit paths (computed from porcelain inside the splice); core 13 M (Nick's hands). Detail: pm-handoff v71 beat 5.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v71 CLOSED at beat 5; the post-close intake at beat 6 — EXPLAIN-114a accepted with one correction; the bus fix ruled (b) and authored; the revert clock 1/10, Sat 2026-09-12 ~18:1x CT)

**State:** core `5f918c7` (EXPLAIN-114a + R3; `check` GREEN = v1.1.4 FROZEN; the `bus-soak` job RED `anomalies=1` = sample #15, UNREAD — the one act); hivemind `7addbc8` + b6; docs `0d62a54`. **The bus class:** (1) the soak's stall — instrumented (`72efb42`); (2) the census's head-miss — a notify-order artefact on a non-monotonic checkpoint; kind E names the harmful arm; sample #14 and REPRO-1 green and silent. **Ruled:** `BUSFIX: b` = BUS-ORDER-1 (AMD-101 PROPOSED; the instruction gated on the EXPLAIN landing and `BUSORDER: go`; the revert clock paused: sample #15 fired an anomaly — its kind decides). **v72 opens on:** sample #15's read → `BUSORDER: go` (kind E) or the reading (another kind) → 114b (DISABLED-2 and two refactors) → HERO-1c → `AMD101: ratify` → R-4c's record → the v1.1.4 freeze note. **Owed:** `H8A:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done` · `R4C:`. Check 9 STALE.

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP: two faces; BUS-ORDER-1 ruled; the revert clock 1/10 · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.
