<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-12 (v108 beat 4 — `78e93f9`; OUTREACH-2 drafted; COMMERCIAL-1's brief filed; J3 running; D-v108-18..21; Mon 2026-10-12 ~07:1x CT (2026-10-12T12:14:25Z). Next: the b4 card → `OUTREACH-2: go` → B-1 + the unit cards → the close) Prior: 2026-10-12 (v108 beat 3 — `708d446`; HERO-U3 LANDED `ba08dd8`; REVIEW-J3 intaken, J3 v2 dispatched; the bridge's degraded form; D-v108-13..17; Mon 2026-10-12 ~07:0x CT (2026-10-12T12:04:36Z). Next: the b3 card → J3 · COMPARATOR-1 → the outreach · COMMERCIAL-1 → the close) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v108 b4 — OUTREACH-2 + COMMERCIAL-1 drafted; J3 RUNNING; Mon ≈ 19:00 CT dry-run #1)

**State:** core **`ba08dd8`** (HERO-U3 over `2a54145`; **`CI: green`**; the Pi `37f05a9` until BC10); bench **`32bac40`** (BP9 rides BC10); docs **`e2a5844`**; skills `e9a77a8`; hivemind `78e93f9` (the b4 card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9 EXECUTED Sun; BC9b Sun Oct 18. **THE RENDERER ADOPTED** (b1; `--check` at every boot). **J3 RUNNING since 07:00** — lands Thu Oct 15 if green; **Fri Oct 16 the go/no-go per tree.** **DRY-RUN #1 ≈ 19:00 CT** · Tue D2. **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **OUTREACH-2 DRAFTED; COMMERCIAL-1's BRIEF FILED** (A1–A7; the open-core line; five words at the Dec re-read); HERO-U3 LANDED `ba08dd8`; **COMPARATOR-1** on Nick's line. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–174 (150–152 CLOSED at b1) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the b4 card → `OUTREACH-2: go` → J3 RUNNING 07:00 → its return → COMPARATOR-1's line → the outreach · COMMERCIAL-1 · B-1 · the unit cards → dry-run #1's intake.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..174 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
