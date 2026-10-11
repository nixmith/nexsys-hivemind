<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-11 (v107 beat 2 — `b6f0115`; AVAIL-API-1 LANDED `74d3926` · `2a54145`, CI green each; ADMIT-CARD (b); COMMERCIAL-1; IR-166..170; D-v107-15..23; Sun 2026-10-11 ~17:5x CT (2026-10-11T22:50:25Z). Next: the b2 card → b3 the packet) Prior: 2026-10-11 (v107 beat 1 — the boot (`ed3d4c8`); BC9 INTAKEN (J2b's denial half proven; the admit half → H10-6; IR-117 closed); AVAIL-API-1 RETURNED; D-v107-1..14; Sun 2026-10-11 ~17:2x CT (2026-10-11T22:21:05Z). Next: the b1 card → b2) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v107 b2 — AVAIL-API-1 LANDED: `74d3926` + `2a54145`, CI green each)

**State:** core **`2a54145`** (T-B over T-A `74d3926` over `9cf0ed9`; **`CI: green` per tree**; the Pi `37f05a9` until BC10); bench **`32bac40`** (the Pi `cddac94`); docs `e2a5844`; skills `e9a77a8`; hivemind `b6f0115` (the b2 card pending). **AVAIL-API-1 LANDED** (`audits/2026-10-11_v107-b2_AVAIL-API-1_return_intake_two-layer_audit.md`; seven [REVIEW] deviations accepted — IR-166..170; two cards, rehearsed; the instruction EXECUTED); **the Java slot FREE (J3 authored v108) and the web-ui slot FREE (HERO-U3's charter b4)**; Fri Oct 16 the go/no-go per tree. **BC9 EXECUTED**: J2b's denial half PROVEN; **ADMIT-CARD = (b)** BC9b Oct 18–19 on three conditions (the bench re-mint · an exit before the freeze · hardware in series), authored v108; IR-117 CLOSED. **COMMERCIAL-1** (Nick 17:36) chartered at b4. **THE PLAN OF RECORD:** the plan review + the freeze list; BC10 Oct 17. **v107 (→ ≤ 21:30):** b3 dry-run #1's packet → b4 charters → b5 the adoption → b6 the close. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149–170 (117 CLOSED) · 142 (BP9) · 143–147 · 140 · 141.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..170 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
