<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-10 (v103 beat 1 — BC9a re-stamped, launched 06:50; the soak Sat → Sun; HERO-U2b intaken with a rider; N1 retracted (D-v103-1..9); Sat 2026-10-10 ~07:1x CT (2026-10-10T12:14:20Z). Order: `BC9a:` → the rider → the landings → `CARRIER:` → the soak 21:00.) Prior: 2026-10-09 (v102 post-close beat 5 — the words banked: HIVE 1219fae · CORE 2b4be09 · ENTITIES 10 · U2A · HERO-U2b running 19:16 (D-v102-26..27); last beat; Fri 2026-10-09 ~19:2x CT (2026-10-10T00:24:42Z). Order: BC9a → the landing → the b5 card → v103.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v103 b1 — BC9a this morning; the soak Sat → Sun; HERO-U2b intaken with a rider)

**State:** core **`2b4be09`** on `main` (the design folder over `da9ca3d`; `CI:` OPEN; HERO-U2b's 25 files uncommitted under `src/`); bench **`cddac94`** (on `main`; on the Pi after BC9a's BP8) — **BENCH-142 + its rider 142b INTAKEN ACCEPT; the landing card after BC9a**; docs **`5e8eb8b`**; skills `e9a77a8`; hivemind `aa15d3e` (the b1 card pending; 11 live beats). **THE PI RUNS `df2bc62`** until BC9a (running since 06:50) pins **`37f05a9`**; `da9ca3d` first deploys by dry-run #2's card (AMD-102 R-E). **THE FLEET: 10 in the registry, 9 ON THE AIR.** **HERO-U2b INTAKEN ACCEPT-WITH-RIDER (v103 b1); N1 retracted; `CARRIER:` (on the burn-in) + AMD-103 before AVAIL-API-1.** **OPEN this week:** IR-141 (post-run) · IR-142 (the landing + BP9) · IR-143 (a Javadoc rider) · IR-140 (post-run). **THE FREEZE LIST:** STARTER-1 config · PROBE-ANSWERED-1 on P3′ · J3 · GRADER-S31-1 · IR-142 (in flight) · AVAIL-API-1 after FIELDS.md. **NEXT:** `BC9a:` → the bench landing → the rider → HERO-U2b's landing → the burn-in's read → `CARRIER:` → AMD-103 → AVAIL-API-1 · **≈ 21:00 SOAK-NIGHT-2** → **Sun 07:00 `S2` → v104** · Sun BC9 · Sun ≈ 19:00 PKG-FRESH-1.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..142 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · the amendment quotes the principle.
