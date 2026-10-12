<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-12 (v108 beat 6, THE CLOSE — `150f29b`; J3 LANDED `e11ae20` · `176adad` (CI green each); v109's text; six rotated; D-v108-29..35; Mon 2026-10-12 ~10:1x CT (2026-10-12T15:14:01Z). Next: the close card → v109 → dry-run #1) Prior: 2026-10-12 (v108 beat 5 — `98f9e82`; J3 RETURNED + INTAKEN LANDING-READY, the landing cards; B-1's stub; the unit cards drafted; D-v108-22..28; Mon 2026-10-12 ~08:5x CT (2026-10-12T13:52:33Z). Next: Card A → the b5 card → the close) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v108 b6 — J3 LANDED `176adad`; v108 CLOSED at b6 — v109's text on disk)

**State:** core **`176adad`** (J3 T-B over T-A `e11ae20` over `ba08dd8`; **`CI: green` each**; the Pi `37f05a9` until BC10); bench **`32bac40`** (BP9 rides BC10); docs **`e2a5844`**; skills `e9a77a8`; hivemind `150f29b` (the close card pending). **THE PI (hs-dev-1): `37f05a9` BY SHA since Sat 12:00:49 CT** — bench `cddac94`; BC9 EXECUTED Sun; BC9b Sun Oct 18. **THE RENDERER ADOPTED** (b1; `--check` at every boot). **J3 LANDED Mon 09:3x** — `e11ae20` (T-A) · `176adad` (T-B), `CI: green` each; IR-46 · 95 · 119 CLOSED; **Fri Oct 16 the go/no-go per tree.** **DRY-RUN #1 ≈ 19:00 CT** · Tue D2. **Sat Oct 17 BC10** · Sun Oct 18 the rollback + BC9b · Tue Oct 20 PI-2 · Oct 22–23 dry-run #2 → the freeze · Oct 30 – Nov 2 the run. **v108 CLOSED at b6; v109's text on disk** — b1 the returns' intake, else GRADER-S31-1; OUTREACH-2 · the unit cards await Nick's words. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **OPEN:** IR-148 (FIXED on `main`) · 149 · 153–178 (46 · 95 · 119 CLOSED at `e11ae20` / `176adad`) · 142 (BP9) · 143–147 · 140 · 141. **NEXT:** the close card → v109 (its text on disk) → `OUTREACH-2: go` → COMPARATOR-1's line → GRADER-S31-1 (v109 b1) → dry-run #1's intake.

**Open risks:** eleven — OR-COLD-BOOT-REGISTRY · OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..174 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no public name before its protocol row · the hub never commits or pushes · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the amendment quotes the principle · cards named by hostname; the dongle in only after the identity gate.
