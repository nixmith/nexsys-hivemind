<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-11 (v106 beat 4 — HERO-U2c LANDED `9cf0ed9` (CI green); AVAIL-API-1 DRAFT v1 in two trees + the review brief; `REVIEW-AA1: launch` asked; D-v106-27..31; Sun 2026-10-11 ~10:2x CT (2026-10-11T15:22:11Z). Next: the review → v2 → the §14 line → v107's text) Prior: 2026-10-11 (v106 beat 3 — `dba134d`; Nick's five rulings → the review v1.1; HERO-U2c RETURNED → LANDING-READY (4 M; the core card handed); Q9–Q12 ruled; IR-160..162; D-v106-19..26; Sun 2026-10-11 ~09:5x CT (2026-10-11T14:50:31Z). Next: `CORE: LANDED` · `HIVE: LANDED` → b4 AVAIL-API-1) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v106 b4 — HERO-U2c landed; AVAIL-API-1 drafted, under review)

**State:** core **`9cf0ed9`** (`CI: green`; HERO-U2c's design files over REGISTRY-COLD-1 `6a03403`; the Pi at `37f05a9` until BC10); bench **`32bac40`** (the Pi at `cddac94` until BP9); docs **`e2a5844`** (AMD-103 RATIFIED); skills `e9a77a8`; hivemind `8162b49` (the b4 card pending); **AVAIL-API-1 DRAFT v1 (two trees) under REVIEW-AA1**. **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT;** **SOAK-NIGHT-2 RAN AND IS READ:** 0 unprovoked flaps in 10 h 38 min (AVAIL-SHAPE SHIPS to BC9 today, dry-run #1 Mon); the S31 510/510 `ok`; the nightly fired (no exit 99); the audit `audits/2026-10-11_SOAK-NIGHT-2_intake-audit.md`. **THE PLAN REVIEW (v106 b2, RULED at b3) + the freeze list = the plan of record**: the whole tree before BC10 (one evidence line per unit); J3 Oct 14–16 if green by Thu; STARTER-1 at BC10 last; HERO-U3 the web-ui slot. **v106 (→ ≈ 13:00):** b5 the review → v2 FILED → the §14 line → BC9's re-stamp · the close: v107's text. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149–162 · 142 (BP9) · 143–147 · 140 · 141.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..162 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
