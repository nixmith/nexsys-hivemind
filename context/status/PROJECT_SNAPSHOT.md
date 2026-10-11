<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-11 (v106 beat 3 — `dba134d`; Nick's five rulings → the review v1.1; HERO-U2c RETURNED → LANDING-READY (4 M; the core card handed); Q9–Q12 ruled; IR-160..162; D-v106-19..26; Sun 2026-10-11 ~09:5x CT (2026-10-11T14:50:31Z). Next: `CORE: LANDED` · `HIVE: LANDED` → b4 AVAIL-API-1) Prior: 2026-10-11 (v106 beat 2 — `0445eef`; `HERO-U2c: running`; THE PLAN REVIEW FILED on Nick's word (the plans HOLD; no date moves; the whole tree before BC10; PROBE-ANSWERED-1 RETIRED; five words; D-v106-12..18); Sun 2026-10-11 ~09:1x CT (2026-10-11T14:11:43Z). Next: the b2 card → b3 AVAIL-API-1) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v106 b3 — the review ruled; HERO-U2c landing; AVAIL-API-1 authored next)

**State:** core **`6a03403`** (`CI: green`; REGISTRY-COLD-1 on `main`, the Pi at `37f05a9` until BC10); bench **`32bac40`** (the Pi at `cddac94` until BP9); docs **`e2a5844`** (AMD-103 RATIFIED); skills `e9a77a8`; hivemind `dba134d` (the b3 card pending); **HERO-U2c LANDING-READY (the core card handed)**. **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT;** **SOAK-NIGHT-2 RAN AND IS READ:** 0 unprovoked flaps in 10 h 38 min (AVAIL-SHAPE SHIPS to BC9 today, dry-run #1 Mon); the S31 510/510 `ok`; the nightly fired (no exit 99); the audit `audits/2026-10-11_SOAK-NIGHT-2_intake-audit.md`. **THE PLAN REVIEW (v106 b2, RULED at b3) + the freeze list = the plan of record**: the whole tree before BC10 (one evidence line per unit); J3 Oct 14–16 if green by Thu; STARTER-1 at BC10 last; HERO-U3 the web-ui slot. **v106 (→ ≈ 13:00):** b3 AVAIL-API-1 in two trees · HERO-U2c landed, the review, the §14 line · b4 dry-run #1's packet, the comparator charter, BC9 · b5 the adoption (or v107) · v107's text. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149–162 · 142 (BP9) · 143–147 · 140 · 141.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..162 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
