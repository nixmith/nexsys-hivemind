<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-09 (v101 post-close beat 8 — THE FINAL CLOSE: CONFIG-ERROR-1 LANDED `da9ca3d` (CI on main open); the four rows CLOSED; v102 re-cut for TONIGHT (D-v101-38..40); Fri 2026-10-09 ~16:4x CT (2026-10-09T21:41:42Z). Order: the b8 card → v102 tonight → BC9a → v103 Sat 07:00.) Prior: 2026-10-09 (v101 post-close beat 7 — CONFIG-ERROR-1 INTAKEN ACCEPT (tree `fca2020…` over `37f05a9`; D-v101-35/36); IR-142; the landing cards (D-v101-37); Fri 2026-10-09 ~16:1x CT (2026-10-09T21:18:15Z). Order: the b7 card → the commit card → CI → the ff-merge → BC9a → v102.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v101 b8 — CONFIG-ERROR-1 LANDED; v102 tonight; BC9a + SOAK-NIGHT-2 tonight; v103 Sat 07:00)

**State:** core **`da9ca3d`** on `main` (CONFIG-ERROR-1 LANDED 16:2x CT, PR #12 ff-merged — **`CI:` on `main` is the open word**; the bus-soak counter 19/20); bench **`cddac94`** (on `main`; on the Pi after BC9a's BP8); docs `055832c` (AMD-102's file lands by v102's docs card); skills `e9a77a8`; hivemind the b8 card's sha (10 live beats; v102's close rotates). **THE PI RUNS `df2bc62` BY SHA** until BC9a tonight, which pins **`37f05a9`**; `da9ca3d`'s first deploy is dry-run #2's card (AMD-102 R-E). **THE FLEET: 10 in the registry, 9 ON THE AIR.** **CLOSED today:** IR-90 · 122 · 126 · 132 (`da9ca3d`). **OPEN this week:** IR-141 DEPRECATE-1 (post-run) · IR-142 (the bench re-point before dry-run #2) · IR-140 (BEAT-RENDERER-2, post-run). **THE FREEZE LIST:** STARTER-1 config · PROBE-ANSWERED-1 on P3′ · J3 · GRADER-S31-1 · IR-142 · AVAIL-API-1 after the FE note. **TONIGHT:** v102 SHORT beside the rig (the FE charter on `FE-SLOT:`; IR-142's charter; the docs card) → BC9a ≈ 19:30 → SOAK-NIGHT-2 → Sat 07:00 `S2` → v103. **NEXT:** the b8 card → v102's text from line 8.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..142 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · the amendment quotes the principle.
