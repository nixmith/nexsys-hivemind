<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-11 (v107 beat 3 — `df5017e`; DRY-RUN #1's packet FILED; the calendar (Sat Oct 17 BC10); v108 b1 = the adoption; D-v107-24..34; Sun 2026-10-11 ~18:1x CT (2026-10-11T23:19:06Z). Next: the b3 card → b4 → the close) Prior: 2026-10-11 (v107 beat 2 — `b6f0115`; AVAIL-API-1 LANDED `74d3926` · `2a54145`, CI green each; ADMIT-CARD (b); COMMERCIAL-1; IR-166..170; D-v107-15..23; Sun 2026-10-11 ~17:5x CT (2026-10-11T22:50:25Z). Next: the b2 card → b3 the packet) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v107 b3 — dry-run #1's packet filed; the week on the calendar)

**State:** core **`2a54145`** (T-B over T-A `74d3926` over `9cf0ed9`; **`CI: green` per tree**; the Pi `37f05a9` until BC10); bench **`32bac40`** (the Pi `cddac94`); docs `e2a5844`; skills `e9a77a8`; hivemind `df5017e` (the b3 card pending). **AVAIL-API-1 LANDED** (`audits/2026-10-11_v107-b2_AVAIL-API-1_return_intake_two-layer_audit.md`; seven [REVIEW] deviations accepted — IR-166..170; two cards, rehearsed; the instruction EXECUTED); **the Java slot FREE (J3 authored v108) and the web-ui slot FREE (HERO-U3's charter b4)**; Fri Oct 16 the go/no-go per tree. **BC9 EXECUTED**: J2b's denial half PROVEN; BC9b Sun Oct 18 on four conditions. **COMMERCIAL-1** → v108. **DRY-RUN #1's PACKET FILED** (`instructions/2026-10-12_DRY-RUN-1_…`; Mon ≈ 19:00 CT D0a–D1 · Tue ≈ 19:00 D2; `.backup`; K-4 on the copy; the cold start LAST). **THE WEEK:** Fri Oct 16 the go/no-go · **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v108 b1 = THE ADOPTION.** **v107:** b4 HERO-U3 + the comparator → b5 the close. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149–170 (117 CLOSED) · 142 (BP9) · 143–147 · 140 · 141.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..170 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
