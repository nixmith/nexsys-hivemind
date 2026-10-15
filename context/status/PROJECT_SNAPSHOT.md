<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-15 (v111 beat 4 — BENCH-HYGIENE-1 DISPATCHED; BC10 DRAFTED; D-v111-25..30; Thu 2026-10-15 ~06:5x CT (2026-10-15T11:58:39Z). Next: the b4 card → LICENSE-1 + PI-2) Prior: 2026-10-15 (v111 beat 3 — SCHEMA-1 INTAKEN ACCEPT; the RETENTION H10; IR-210..215; D-v111-17..24; Thu 2026-10-15 ~06:2x CT (2026-10-15T11:21:27Z). Next: the b3 card → BC10's card) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v111 b4 — v111 b4 — BENCH-HYGIENE-1 running; BC10 drafted; LICENSE-1 + PI-2 next)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; the Pi `37f05a9` until BC10); bench **`5cf3bd0`** (GATE-2 over BENCH-BOOT-1 `6a40a10`; BP10 `ceb08c5`; BC10 pulls it); docs **`e2a5844`**; skills `e9a77a8`; hivemind `69167b9` (the b4 card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9 EXECUTED Sun; BC9b Sun Oct 18. **J3 LANDED** `e11ae20` (T-A) · `176adad` (T-B), `CI: green` each; **Fri Oct 16 the go/no-go per tree.** **DRY-RUN #1 COMPLETE** (v111 b1): no dark; R4 PASS ×44; 48.4 MB/day; **IR-56 CLOSED**. **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v111** b2 GATE-2 LANDED `5cf3bd0` ; b3 SCHEMA-1 INTAKEN (J3 T-B → Friday; RETENTION H10; IR-210..215); **b4 BENCH-HYGIENE-1 DISPATCHED** (06:50 → BP11); **BC10 DRAFTED** (both forms). **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–215 (46 · 95 · 119 CLOSED; 148 sharpened; 185–215 new) · 56 CLOSED (v111 b1, sample 7) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the b4 card → b5 LICENSE-1 + PI-2's card + the caveats; b6 the deliberation → the close; BH-1's landing tonight.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..215 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
