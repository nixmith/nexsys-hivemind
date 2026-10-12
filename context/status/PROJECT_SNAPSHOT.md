<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-11 (v108 beat 2 — `bc3cd5c`; J3 DRAFT v1 + REVIEW-J3; HERO-U3 intaken LANDING-READY, its card handed; IR-172..174; D-v108-8..12; Sun 2026-10-11 ~19:5x CT (2026-10-12T00:50:19Z). Next: `CORE: LANDED` → the b2 card → J3 v2) Prior: 2026-10-11 (v108 beat 1, THE ADOPTION — `fa140ab`; `state.yaml` v3; `--check` 7 MATCH before and after the splice; IR-150..152 CLOSED; D-v108-1..7; Sun 2026-10-11 ~19:2x CT (2026-10-12T00:24:23Z). Next: the b1 card → J3 on `CAPACITY: Mon 12+` → Mon Oct 12 ≈ 19:00 CT dry-run #1) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v108 b2 — HERO-U3 LANDING-READY; J3 DRAFT v1 in review; Mon Oct 12 ≈ 19:00 CT dry-run #1)

**State:** core **`2a54145`** (AVAIL-API-1 T-B; **`CI: green`**; HERO-U3 landing); bench **`32bac40`** (BP9 rides BC10); docs **`e2a5844`**; skills `e9a77a8`; hivemind `bc3cd5c` (the b2 card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9 EXECUTED Sun; BC9b Sun Oct 18. **THE RENDERER ADOPTED** (b1; `--check` at every boot). **J3 DRAFT v1 FILED** (IR-46 + IR-95 + IR-119; two trees; REVIEW-J3 running) → v2 → an empty porcelain; **Fri Oct 16 the go/no-go per tree.** **DRY-RUN #1 Mon ≈ 19:00 CT** · **Tue D2.** **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **HERO-U3 INTAKEN LANDING-READY** (24 files; the ff-merge card; `frontend.yml` the gate; IR-172..174); **COMPARATOR-1** Monday. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–174 (150–152 CLOSED at b1) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the HERO-U3 card → `CI:` → the b2 card → J3 v2 → the outreach · COMMERCIAL-1 · B-1 · the unit cards → dry-run #1's intake.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..174 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
