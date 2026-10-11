<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-11 (v106 beat 1 — THE BOOT (`de88139`; the preflight PASS); S2 INTAKEN → §P′: 0 UNPROVOKED FLAPS in 10 h 38 min — AVAIL-SHAPE SHIPS; the S31 510/510 `ok`; P11′ 0; P12′ CLOSED (`ok`); IR-121's battery half CLOSED; IR-158, IR-159; HERO-U2c's §9 line HANDED (D-v106-1..11); Sun 2026-10-11 ~08:4x CT (2026-10-11T13:43:49Z). Next: `HERO-U2c: running` · the b1 card → b2 AVAIL-API-1 in two trees) Prior: 2026-10-10 (v105 beat 5, THE CLOSE — SOAK-NIGHT-2 S0 + S1 ran; R-F's number BANKED `avail-rows-total=479`; the review against the plans; v106's text cut (Sun 07:00: S2 → HERO-U2c → AVAIL-API-1 in two trees → dry-run #1's packet → the adoption); the adoption deferred (D-v105-34..38); Sat 2026-10-10 ~21:4x CT (2026-10-11T02:47:05Z). Next: the close card → Sun 07:00 S2 → v106) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v106 b1 — S2 read, AVAIL-SHAPE ships; HERO-U2c running; AVAIL-API-1 authored next)

**State:** core **`6a03403`** (`CI: green`; REGISTRY-COLD-1 on `main`, the Pi at `37f05a9` until BC10); bench **`32bac40`** (the Pi at `cddac94` until BP9); docs **`e2a5844`** (AMD-103 RATIFIED); skills `e9a77a8`; hivemind `de88139` (the b1 card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT;** **SOAK-NIGHT-2 RAN AND IS READ:** 0 unprovoked flaps in 10 h 38 min (AVAIL-SHAPE SHIPS to BC9 today, dry-run #1 Mon); the S31 510/510 `ok`; the nightly fired (no exit 99); the audit `audits/2026-10-11_SOAK-NIGHT-2_intake-audit.md`. **v106 (→ ≈ 13:00):** b2 AVAIL-API-1 authored in two trees · b3 HERO-U2c landed, the review, the §14 line · b4 dry-run #1's packet, the comparator charter, BC9 re-stamped · b5 the adoption · the close: v107's text. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149–159 · 142 (BP9) · 143–147 · 140 · 141.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..159 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
