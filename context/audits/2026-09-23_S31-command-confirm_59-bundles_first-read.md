<!--
file: context/audits/2026-09-23_S31-command-confirm_59-bundles_first-read.md
purpose: OR-S31-INTERMITTENT's instrument, first read — every `command-confirm-s31` bundle still on the bench card (59, 2026-07-30 → 2026-09-23), copied home by Nick's morning read and read at the bytes by the hub: the verdict, the terminal phase, the DISPATCHED → terminal time from `api-captures.json`, and the A-9 post-window state read. It replaces the record's partial count, states the classes the bundles show, and names the next instruments. It names no mechanism (arc 28).
audience: the hub (rehearsal 1's packet; `HARNESS-PLUG:`) · Nick (§0) · a later S31 lane
state-type: instrument read (primary: the bundles at `ClaudeFolder/_scratch/v79/s31-bundles/`, copied from `~/hs-bench/bundles/` on hs-dev-1; the Pi keeps its copies)
status: FILED v79 beat 2 (Wed 2026-09-23 ~07:0x CT; instrument 2026-09-23T12:04:18Z).
-->

# `command-confirm-s31` — 59 bundles, the first read

## §0 What the bundles say
- **22 of 59 runs FAIL (37 %)** — July 2 of 3 · August 12 of 32 · September 8 of 24. The record had read only the nights it was pasted (09-01..09-04, 09-12 onward) and counted "the fourth FAIL since 09-12"; the bundles add 09-05, 09-09, 09-10 and every August night. The v79 b1 OR row's list of FAIL nights was drawn from that partial record: corrected here (the lesson of 2026-09-23: a count is read from the uncapped listing).
- **Every FAIL is `CONFIRMATION_TIMED_OUT`.** 20 of 22 land 5.03–5.99 s after `DISPATCHED`. Two (08-14, 08-15) land 8–9 ms after it, with the plug's last report at 08-13T12:13:30Z — a separate class (the plug silent for ~20 h), not this one.
- **PASS latencies split in two:** 27 of 37 at ≤ 0.66 s (median of all 37: 0.30 s); 10 at 1.70–3.65 s (07-31, 08-01, 08-07, 08-24, 08-26, 08-30, 08-31, 09-06, 09-13, 09-19). The confirmation window (~5 s) sits 1.4 s past the slowest PASS.
- **The A-9 state read (~+0.9 s after the terminal, ~6 s after `DISPATCHED`; present from 08-04, 18 reads):** 15 read `on=false · AVAILABLE` — 13 in the 5-s class, the plug's last report 131–220 s before the command (no edge seen within ~6 s), and the two fast-class nights (last report 20 h and 44 h before). **3 read `on=true`** (08-27, 09-05, 09-18) with the last report 96–372 s BEFORE the command: the relay was already ON when the turn_on went out, so no edge was possible. The settle leg that precedes it asserts only `data.terminal == true` ("SOME terminal, either disposition — the relay is OFF after it regardless", `command-s31-settle.yaml`) — on those three nights the relay was not OFF. That is the settle leg's claim refuted, not the confirm leg's.
- **The app log carries nothing for the command window** on 55 of 59 runs (`app-log-slice.log ABSENT — the app wrote nothing in the run window`); the four slices present (07-31, 08-01, 08-14, 08-15) predate the class's September runs. The journal slice was DROPPED at B3.1 A-6 (`tools/runner/README.md`), so the pre-registration's "api-captures.json against the journal's zigbee lines" has no journal to read inside a bundle: the Core does not log command frames at INFO.
- **What the data rules out, and what it does not:** the load (FAILs all August with nothing on the plug; 09-22 unloaded). It does not name a mechanism: "no edge within ~6 s" is consistent with a frame that never reached the relay and with a report later than ~6 s; the bundles cannot split them.

## §1 The next instruments (ordered, cheapest first)
1. **The settle leg's own bundles** (`command-s31-settle-*`) for the three `on=true` nights and a sample of the rest — did its turn_off end `CONFIRMED` or `CONFIRMATION_TIMED_OUT`? (the v79 b2 carrier read copies them home).
2. **A second post-window read** (+30 s and +120 s after a FAIL) — splits a late report from no edge beyond ~6 s. A bench-runner change (IR-52), not a rig act.
3. **LINK-READ on the bench card** (after THE THURSDAY ORDER; its deploy is step 0b re-run): the S31's link reading at each transition and the ten-minute summary on the nights a FAIL lands.
4. Only then a mechanism, and only then the confirmation window's policy (IR-53).

## §2 What it decides now
- `HARNESS-PLUG:` stays open (STEER 2): an instrument that must cut power on command cannot be a device whose ON goes unconfirmed one night in three.
- Rehearsal 1's packet does not lean on the S31's ON-edge.
- THE THURSDAY ORDER is untouched: the S31 stays OFF and unloaded, and the adoption is three new plugs. The Friday digest may read 7/9 on this class alone; the packet's step 4 reads boot-health and the drift check, not the S31 leg.

## §3 The table (every bundle; read from `verdict.txt`, `api-captures.json`, `post-window-state.json`, `MANIFEST.txt`)
| Bundle (UTC) | Verdict | Terminal phase | DISPATCHED → terminal (s) | A-9 state read (~+0.9 s after the terminal): on · availability · lastReported (s before DISPATCHED) | app-log slice |
|---|---|---|---|---|---|
| 20260730T000124Z | FAIL | CONFIRMATION_TIMED_OUT | 5.076 | — | ABSENT |
| 20260730T013743Z | FAIL | CONFIRMATION_TIMED_OUT | 5.911 | — | ABSENT |
| 20260731T042204Z | PASS | CONFIRMED | 3.623 | — | present |
| 20260801T083055Z | PASS | CONFIRMED | 3.652 | — | present |
| 20260802T083057Z | FAIL | CONFIRMATION_TIMED_OUT | 5.127 | — | ABSENT |
| 20260803T083057Z | FAIL | CONFIRMATION_TIMED_OUT | 5.189 | — | ABSENT |
| 20260804T083057Z | FAIL | CONFIRMATION_TIMED_OUT | 5.197 | on=false · AVAILABLE · 146 | ABSENT |
| 20260805T083057Z | FAIL | CONFIRMATION_TIMED_OUT | 5.228 | on=false · AVAILABLE · 146 | ABSENT |
| 20260806T083127Z | PASS | CONFIRMED | 0.302 | — | ABSENT |
| 20260807T001211Z | PASS | CONFIRMED | 2.114 | — | ABSENT |
| 20260807T083127Z | PASS | CONFIRMED | 0.169 | — | ABSENT |
| 20260808T083127Z | PASS | CONFIRMED | 0.361 | — | ABSENT |
| 20260809T083132Z | FAIL | CONFIRMATION_TIMED_OUT | 5.418 | on=false · AVAILABLE · 179 | ABSENT |
| 20260810T083135Z | FAIL | CONFIRMATION_TIMED_OUT | 5.721 | on=false · AVAILABLE · 181 | ABSENT |
| 20260811T083127Z | PASS | CONFIRMED | 0.162 | — | ABSENT |
| 20260812T083146Z | PASS | CONFIRMED | 0.302 | — | ABSENT |
| 20260813T083132Z | FAIL | CONFIRMATION_TIMED_OUT | 5.987 | on=false · AVAILABLE · 176 | ABSENT |
| 20260814T083338Z | FAIL | CONFIRMATION_TIMED_OUT | 0.008 | on=false · AVAILABLE · 73207 | present |
| 20260815T083334Z | FAIL | CONFIRMATION_TIMED_OUT | 0.009 | on=false · AVAILABLE · 159604 | present |
| 20260816T083217Z | FAIL | CONFIRMATION_TIMED_OUT | 5.937 | on=false · AVAILABLE · 220 | ABSENT |
| 20260817T083214Z | PASS | CONFIRMED | 0.162 | — | ABSENT |
| 20260818T083213Z | PASS | CONFIRMED | 0.120 | — | ABSENT |
| 20260819T083215Z | PASS | CONFIRMED | 0.651 | — | ABSENT |
| 20260820T083217Z | FAIL | CONFIRMATION_TIMED_OUT | 5.031 | on=false · AVAILABLE · 131 | ABSENT |
| 20260821T083216Z | PASS | CONFIRMED | 0.072 | — | ABSENT |
| 20260822T083215Z | PASS | CONFIRMED | 0.294 | — | ABSENT |
| 20260823T083215Z | PASS | CONFIRMED | 0.277 | — | ABSENT |
| 20260824T083118Z | PASS | CONFIRMED | 1.703 | — | ABSENT |
| 20260825T083118Z | PASS | CONFIRMED | 0.085 | — | ABSENT |
| 20260826T083118Z | PASS | CONFIRMED | 1.890 | — | ABSENT |
| 20260827T083123Z | FAIL | CONFIRMATION_TIMED_OUT | 5.222 | on=true · AVAILABLE · 372 | ABSENT |
| 20260828T083118Z | PASS | CONFIRMED | 0.337 | — | ABSENT |
| 20260829T083117Z | PASS | CONFIRMED | 0.502 | — | ABSENT |
| 20260830T083121Z | PASS | CONFIRMED | 3.290 | — | ABSENT |
| 20260831T083120Z | PASS | CONFIRMED | 3.523 | — | ABSENT |
| 20260901T083117Z | PASS | CONFIRMED | 0.101 | — | ABSENT |
| 20260902T083122Z | FAIL | CONFIRMATION_TIMED_OUT | 5.496 | on=false · AVAILABLE · 140 | ABSENT |
| 20260903T111217Z | PASS | CONFIRMED | 0.090 | — | ABSENT |
| 20260904T083155Z | PASS | CONFIRMED | 0.321 | — | ABSENT |
| 20260905T083148Z | FAIL | CONFIRMATION_TIMED_OUT | 5.428 | on=true · AVAILABLE · 165 | ABSENT |
| 20260906T083145Z | PASS | CONFIRMED | 2.072 | — | ABSENT |
| 20260907T083142Z | PASS | CONFIRMED | 0.165 | — | ABSENT |
| 20260908T083143Z | PASS | CONFIRMED | 0.298 | — | ABSENT |
| 20260909T083150Z | FAIL | CONFIRMATION_TIMED_OUT | 5.102 | on=false · AVAILABLE · 165 | ABSENT |
| 20260910T083147Z | FAIL | CONFIRMATION_TIMED_OUT | 5.647 | on=false · AVAILABLE · 162 | ABSENT |
| 20260911T083144Z | PASS | CONFIRMED | 0.434 | — | ABSENT |
| 20260912T083148Z | FAIL | CONFIRMATION_TIMED_OUT | 5.791 | on=false · AVAILABLE · 162 | ABSENT |
| 20260913T083146Z | PASS | CONFIRMED | 3.567 | — | ABSENT |
| 20260914T083209Z | PASS | CONFIRMED | 0.535 | — | ABSENT |
| 20260915T083209Z | PASS | CONFIRMED | 0.144 | — | ABSENT |
| 20260916T083208Z | PASS | CONFIRMED | 0.331 | — | ABSENT |
| 20260917T083209Z | PASS | CONFIRMED | 0.116 | — | ABSENT |
| 20260918T083214Z | FAIL | CONFIRMATION_TIMED_OUT | 5.930 | on=true · AVAILABLE · 96 | ABSENT |
| 20260919T083209Z | PASS | CONFIRMED | 1.920 | — | ABSENT |
| 20260919T185610Z | PASS | CONFIRMED | 0.076 | — | ABSENT |
| 20260920T083121Z | FAIL | CONFIRMATION_TIMED_OUT | 5.981 | on=false · AVAILABLE · 179 | ABSENT |
| 20260921T083116Z | PASS | CONFIRMED | 0.155 | — | ABSENT |
| 20260922T083122Z | FAIL | CONFIRMATION_TIMED_OUT | 5.101 | on=false · AVAILABLE · 179 | ABSENT |
| 20260923T083118Z | PASS | CONFIRMED | 0.084 | — | ABSENT |
