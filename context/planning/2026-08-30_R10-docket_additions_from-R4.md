<!--
file: context/planning/2026-08-30_R10-docket_additions_from-R4.md
purpose: R-10 DOCKET ADDITIONS harvested from the R-4 sitting (2026-08-30, three-of-four; record + intake audit at context/audits/2026-08-30_R4_*). The September plan (PROPOSED) §wk-1 carries the standing R-10 docket; this file rides beside it so the plan text is not amended pre-ratification.
audience: the R-10 sitting (Fri–Sat 9/5–6) · the hub
status: FILED at v59 beat 5.
-->

# R-10 docket additions (from R-4)

1. **F-R4-1 — the silent-rejoiner adoption gap (design ruling, then a coding WU).** The shipped pipeline converts ONLY announce-class devices; a mains device on SECURED_REJOIN reports forever without proposing (evidenced: the D-g bounded Hue attempt, zero adoption-chain events across a full 254 s window). Questions for the ruling: should a permit-join window admit KNOWN-custody devices via an interview-on-rejoin path? What event-model shape (a first-class `device_relinked`→`device_adopted` promotion? a new proposal source?)? Where does the relink-vs-adopt doctrine live (Doc 02/08)? INV/LTD sweep owed at ruling time.
2. **F-R4-2 — custody clones the NETWORK, not the REGISTRY (doctrine + docs row).** Bench pos 25065/devices 6 vs held pos 40/devices 2 for the SAME physical fleet. Owes: the cloning runbook states it in one loud sentence · boot-contract-map row · pointer notes where Doc 02/08 imply otherwise. This is the mechanism that made R-4's C4 unreachable.
3. **R-4b — the four-of-four re-rep (charter AFTER item 1 lands).** The full D-1 lift needs C4 on real hardware. The R-4b packet AUTHORS UNDER THE MINTED LESSON: every lift criterion is checked REACHABLE against the instrument's own census at packet authoring (second §9-B-class occurrence — this row is the carrier).
4. **PKG-SEC-2 — the zigbee schema admission** (C-1: boots on a WARNING every start): charter at `context/instructions/2026-08-30_PKG-SEC-2_zigbee-schema-admission_charter.md`; small ruling, then a small WU; carries the D-f path-correction sweep.
5. **O-2 wait-state (pointer):** held card next boot — `systemctl show -p ExecMainStatus -p Result` + the `adoption_maps_rehydrated` check (~5 min operator act; rides whenever the held card next powers).
6. **The R-4 packet instrument defects → the lessons fold:** artifact nests at `deb/build/` (top-level globs blind) · `journalctl -b`+`head` returns the pre-change invocation (scope to the service invocation) · the token gate `test ${#TOK} -eq 44` cannot pass a valid 43-char token (file 44 B = 43 + newline) · the `/etc/...` yaml path never existed (D-f) · msys `TZ=` silent-GMT fallback + `MSYS2_ARG_CONV_EXCL` (desk gotchas, from PKG-SEC-1's lane).

## Appended v59 beat 6 (2026-08-30 evening) — from the RS-5 + FE-HONEST-1 intakes

7. **The batched additive contract amendment (CG-1/2/3, from FE-HONEST-1):** CG-1 HIGH — optional entity refs on the non-firing/automations reads (unblocks the full §10-J loud surface); CG-2 — optional `deviceId` on entity reads (entity-row → `device_adopted` correlation); CG-3 — optional `lastReported` on A1 rows (evidence-based list freshness). ONE bump in the v1.1.x additive pattern, formal amendment path; Core WU + FE fast-follow. Evidence: `audits/2026-08-30_FE-HONEST-1_return.md` §CG.
8. **The strategy beat rules the RS-5 convergence finding** (plugins-as-data-with-a-measured-verdict = branch C wearing the plugin story; the code SDK at its fenced rung) **+ confirms the Apache-2.0 flip's calendar line** (S-1 — the flip gates every inbound surface, data included; already the 10-01 quarterly's LICENSE-flip gate). Evidence: `research/2026-08-30_RS5_plugin-ecosystem_return.md` §0 + the beat-6 audit.
9. **FE-STATE-DIALECT** — the FE lane's named next WU (closes the §10-G unreadable class at the root once Core conforms); sequences with/after the CG batch.
