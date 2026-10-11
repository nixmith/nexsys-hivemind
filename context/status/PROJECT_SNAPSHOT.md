<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-11 (v107 beat 1 — the boot (`ed3d4c8`); BC9 INTAKEN (J2b's denial half proven; the admit half → H10-6; IR-117 closed); AVAIL-API-1 RETURNED; D-v107-1..14; Sun 2026-10-11 ~17:2x CT (2026-10-11T22:21:05Z). Next: the b1 card → b2) Prior: 2026-10-11 (v106 beat 5, THE CLOSE — REVIEW-AA1 → AVAIL-API-1 DISPATCHED 12:2x before the rig; BC9 re-stamped; v107's text; D-v106-32..39; Sun 2026-10-11 ~12:2x CT (2026-10-11T17:24:45Z). Next: the close card → BC9 13:00 → v107 ≈ 17:30) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v107 b1 — BC9 intaken; AVAIL-API-1 returned, b2 its landing)

**State:** core **`9cf0ed9`** (`CI: green`; the Pi `37f05a9`) — **`avail-api-1/amd-103`: AVAIL-API-1's two trees (T-A `a2ff9d62…` · T-B the index, 47 paths) RETURNED 16:4x, uncommitted**; bench **`32bac40`** (the Pi `cddac94`); docs `e2a5844`; skills `e9a77a8`; hivemind `ed3d4c8` (the b1 card pending). **BC9 + REHEARSAL 3 EXECUTED 13:08–14:38** (`audits/2026-10-11_BC9-REHEARSAL-3_intake-audit.md`): the scoped window ON SILICON; **J2b's denial half PROVEN** (a foreign SNZB-03P denied ×18, each a `join_rejected` row with the scope); **the admit half UNTESTED** (the sensor keeps its network across a re-power → **H10-6**: the SNZB-03P through its own scoped window, lean BC9b Oct 18–19); **IR-115's second arm REFUTED** (the WARN pair ≈ 0.2 s after every close — a false WARN); IR-117 CLOSED; P11′ CLOSED; one count lost to the card's quoting (the lesson). **THE PLAN OF RECORD:** the plan review + the freeze list; Oct 16 the go/no-go per tree; BC10 Oct 17. **v107 (→ ≤ 21:30):** b2 the intake + the two-tree card → b3 dry-run #1's packet → b4 charters → b5 the adoption → b6 the close. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149–165 (117 CLOSED) · 142 (BP9) · 143–147 · 140 · 141.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..165 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
