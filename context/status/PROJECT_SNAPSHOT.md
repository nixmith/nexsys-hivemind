<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-10 (v103 beat 2 — the Pi on `37f05a9` (BC9a intaken; the Hue as predicted); bench `32bac40`, core `409547c` (CI green) landed; TRIAGE; the horizon rows; BURNIN-1 (D-v103-10..17); Sat 2026-10-10 ~08:1x CT (2026-10-10T13:10:57Z). Order: the b2 card → BURNIN-1 → `CARRIER:` → the soak 21:00.) Prior: 2026-10-10 (v103 beat 1 — BC9a re-stamped, launched 06:50; the soak Sat → Sun; HERO-U2b intaken with a rider; N1 retracted (D-v103-1..9); Sat 2026-10-10 ~07:1x CT (2026-10-10T12:14:20Z). Order: `BC9a:` → the rider → the landings → `CARRIER:` → the soak 21:00.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v103 b2 — the Pi on `37f05a9`; core `409547c` and bench `32bac40` landed)

**State:** core **`409547c`** on `main` (HERO-U2b + r1 LANDED Sat 08:06; `CI: green`); bench **`32bac40`** on `main` (BENCH-142 + 142b LANDED Sat; the Pi at `cddac94` until BP9); docs **`5e8eb8b`**; skills `e9a77a8`; hivemind `9cef3e7` (the b2 card pending; 12 live beats). **THE PI RUNS `37f05a9` BY SHA** since 07:17 CT (BC9a; boot-health 6/6 at 10/10; the Hue UNAVAILABLE · None × 3, as predicted); `da9ca3d` first deploys by dry-run #2's card (AMD-102 R-E). **THE FLEET: 10 in the registry, 9 ON THE AIR.** **The burn-in until ≈ 21:00; BURNIN-1 (≈ 10:30+) → `CARRIER:` → AMD-103 → AVAIL-API-1.** **OPEN this week:** IR-142 (BP9) · IR-143 (a Javadoc rider) · IR-144 · 145 · 146 · IR-140 · 141 (post-run). **THE FREEZE LIST:** STARTER-1 config · PROBE-ANSWERED-1 on P3′ · J3 · GRADER-S31-1 · IR-142 (BP9) · AVAIL-API-1 after FIELDS.md. **NEXT:** the b2 card → BURNIN-1 → `CARRIER:` → AMD-103 → AVAIL-API-1 · LIVE-RENDER-1 · **≈ 21:00 SOAK-NIGHT-2** → **Sun 07:00 `S2` → v104** · Sun BC9 + PKG-FRESH-1 (`SUNDAY:`).

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..142 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · the amendment quotes the principle.
