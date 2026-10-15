<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-15 (v111 beat 2 — GATE-2 LANDED `5cf3bd0`; INTAKEN ACCEPT; N3's H10; IR-204..209; D-v111-10..16; Thu 2026-10-15 ~06:0x CT (2026-10-15T11:09:47Z). Next: the b2 card → SCHEMA-1) Prior: 2026-10-14 (v111 beat 1 — DRY-RUN #1 COMPLETE; IR-56 CLOSED; R4 PASS; D-v111-1..9; Wed 2026-10-14 ~07:1x CT (2026-10-14T12:14:54Z). Next: the b1 card → GATE-2 → SCHEMA-1) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v111 b2 — v111 b2 — GATE-2 LANDED `5cf3bd0`; N3's H10 to Nick; SCHEMA-1 next)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; the Pi `37f05a9` until BC10); bench **`5cf3bd0`** (GATE-2 over BENCH-BOOT-1 `6a40a10`; BP10 `ceb08c5`; BC10 pulls it); docs **`e2a5844`**; skills `e9a77a8`; hivemind `05c1515` (the b2 card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9 EXECUTED Sun; BC9b Sun Oct 18. **J3 LANDED** `e11ae20` (T-A) · `176adad` (T-B), `CI: green` each; **Fri Oct 16 the go/no-go per tree.** **DRY-RUN #1 COMPLETE** (v111 b1): no dark; R4 PASS ×44; 48.4 MB/day; **IR-56 CLOSED**. **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v111 b2 — GATE-2 LANDED `5cf3bd0`** (the 57 % is the Hue's; the S31 32/32 since 09-27; the fitness block additive; N3's H10 — (c) recommended; IR-204..209). **SCHEMA-1 RETURNED** (b3). **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–209 (46 · 95 · 119 CLOSED; 148 sharpened; 185–209 new) · 56 CLOSED (v111 b1, sample 7) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the b2 card → b3 SCHEMA-1 (the five checks; the retention H10) → LICENSE-1 · BC10's draft · PI-2.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..209 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
