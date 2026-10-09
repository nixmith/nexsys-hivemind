<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-09 (v102 beat 2 — BENCH-142 + HERO-U2a cut and DISPATCHED; the AMD-102 docs card handed (D-v102-6..9); Fri 2026-10-09 ~17:2x CT (2026-10-09T22:24:09Z). Order: the two lines → the docs card → the b2 card → BC9a → the close → v103.) Prior: 2026-10-09 (v102 beat 1 — THE BOOT: CI green for `da9ca3d`; `FE-SLOT: tonight` RULED; the deliverable named (D-v102-1..5); Fri 2026-10-09 ~17:0x CT (2026-10-09T22:04:04Z). Order: the b1 card → b2 → BC9a → the close → v103 Sat 07:00.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v102 b2 — two lanes dispatched beside the rig; the docs card handed; BC9a + SOAK-NIGHT-2 tonight; v103 Sat 07:00)

**State:** core **`da9ca3d`** on `main` (CONFIG-ERROR-1 LANDED Fri; `CI: green` 16:52; the bus-soak counter 19/20); bench **`cddac94`** (on `main`; on the Pi after BC9a's BP8) — **BENCH-142 RUNNING** (IR-142; ≤ 2 h; staged, never committed); docs `055832c` → **the AMD-102 card in Nick's hands**; skills `e9a77a8`; hivemind `c4dc654` + the b2 card (12 live beats; the close rotates). **THE PI RUNS `df2bc62` BY SHA** until BC9a tonight, which pins **`37f05a9`**; `da9ca3d`'s first deploy is dry-run #2's card (AMD-102 R-E). **THE FLEET: 10 in the registry, 9 ON THE AIR.** **The web-ui slot: HERO-U2a RUNNING** (design mode; `design/recovery-card-v1/`; FIELDS.md → AVAIL-API-1). **OPEN this week:** IR-141 DEPRECATE-1 (post-run) · IR-142 (in flight) · IR-140 (BEAT-RENDERER-2, post-run). **THE FREEZE LIST:** STARTER-1 config · PROBE-ANSWERED-1 on P3′ · J3 · GRADER-S31-1 · IR-142 (in flight) · AVAIL-API-1 after FIELDS.md. **TONIGHT:** the b2 card → BC9a ≈ 19:30 → the close (b3: the rotation; v103's text) → SOAK-NIGHT-2 → Sat 07:00 `S2` → v103 (the harvest; the two intakes; `TRIAGE: adopt`). **NEXT:** the bench line · the FE line · the docs card · the b2 card.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..142 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · the amendment quotes the principle.
