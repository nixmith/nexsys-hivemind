<!--
file: context/audits/2026-08-03_pi-command-history_cross-validation_v45-beat-1.md
purpose: Cross-validation of Nick's full Pi shell-history paste (:505–:1503, provided at the v45 dispatch) against the banked record — verdict, pinned extracts, environment-provenance pins, dispositions. Filed per the chat-is-not-a-storage-tier law.
audience: Hub (v45+), Nick, future audits needing operator-act timelines
state-type: evidence cross-validation (point-in-time)
status: FILED 2026-08-03 (v45 hub, beat 1)
provenance: Nick pasted `history` output from homesynapse@hs-dev-1 into the v45 dispatch chat (2026-08-03, ~00:45–02:30 CDT), offered as "(almost) fully encapsulating everything actually performed on the hardware." The Pi's own bash history remains the primary record; this file pins the load-bearing extracts and the adjudication. Physical acts (unplug/replug cycles, waves, battery pulls) are structurally invisible to shell history — their record stays the filed operator returns.
-->

# Pi Command-History Cross-Validation (v45 beat 1)

## 1. Verdict

**CORROBORATES — zero contradictions with the banked record.** Every load-bearing spine claim checked against the history either matches it or concerns acts history cannot see (physical operator acts, disclosed above). Two schedule-critical ABSENCES are themselves evidence (§4).

## 2. Load-bearing confirmations (banked claim → history evidence)

| Banked claim | History evidence | Verdict |
|---|---|---|
| KillMode=process drop-in applied by Nick's hands, unit-local (v43 beat-6 ratification) | :1421–:1433 — the `nexsys-bench-nightly.service.d/killmode.conf` heredoc + `daemon-reload` + the show read, exactly the ACTION-1 block | MATCH |
| The B3 install: linger + unit copies + timer enable (v43 beat 2) | :1026–:1032 | MATCH |
| The amended nine-leg suite order, park LAST (the F1 park; the H2 re-run) | :941 (suite ends `…,command-s31-settle`) after the 150 s report-clock clear at :938–:939 | MATCH |
| The B3 p-block / morning-1 / follow-up captures ran as filed, predictions BEFORE evidence | :1047–:1252 / :1255–:1353 / :1370–:1410 — the H1/H2/H3 PREDICTS block sits in-script before any read | MATCH |
| bench.sh path of record = `/home/homesynapse/nexsys-bench/tools/bench.sh`; `~/hs-bench` = data | :1496 (find); :1499–:1501 (path fumbles resolving to the full repo path); :1492's `~/hs-bench/tools/bench.sh` failing as expected (no `tools/` under the data dir) | MATCH |
| The Aug-2 morning gate ran (the night-2 intake's basis) | :1491–:1495 (pgrep · digest · the Aug-2 bundle ls + 60-line dumps) + :1498–:1503 (the four-read form, `--since "2026-08-02 04:00"`) | MATCH |
| The F-12 bracket experiments (GAP 8/12/16 · the ≥60 s quiet REP A/B) as filed | :879–:881 · :916–:926 | MATCH |
| The 04P adoption attempts via `permit_join_duration` add/remove cycles (the 07-19→07-21 arc) | :546–:652 (append → joins → sed-delete, three cycles) | MATCH — descriptive only; the 04P item is CLOSED-NOT-EXECUTABLE and nothing here re-opens it |
| The S-2/S-3 deploy-and-rep arc (installDist pulls · `availability_seeded` greps · entities curls · the rejoin-race scenario runs) | :1461–:1490 | MATCH |

## 3. Environment-provenance pins (Pi system state carried by no repo)

- `uhubctl` installed (:780) + the udev rule `/etc/udev/rules.d/52-usb-uhubctl.rules` (idVendor 0bda, MODE 0666; :789–:791) — the `usb-power` leg's host-side deps.
- Node 22 via nodesource (:724–:726) — the dash-serve/FE-serve era toolchain.
- `sudo loginctl enable-linger` (:1026) — the user-timer survival precondition.
- Stray files (cleanup candidates at a future trip; never urgent): `~/hs-bench/bench.sh.pre-pull-backup-20260731` (:992) · `~/joins-night-baseline-entities.json` (:534) · `~/04p-before.json` (:607) · the `/tmp/b3-*.txt` captures (volatile by location).
- Historical: `rm -rf ~/homesynapse-core/.homesynapse` (:720, the July bring-up era) — an early-arc data reset, consistent with the L-A/L-B R-1 ruling (no live acceptance evidence depends on process continuity; the A1–A3 soak evidence is banked at the certification close-out).

## 4. The absences that matter (both are evidence, not gaps)

- **No Aug-3 gate read exists in the history** — the newest journal window is `--since "2026-08-02 04:00"` (:1503). The armed experiment's adjudicating read has NOT run; it arrives as Nick's morning paste at the v45 hub.
- **Zero S31-touching commands after the Aug-2 morning reads** — everything from :1496 onward is read-only (find · pgrep · digest · show · journalctl). The park set by the Aug-2 suite's settle leg stands undisturbed; the standing hands-off order HELD.

## 5. Dispositions

Nothing in this intake changes any banked verdict, opens any thread, or owes any follow-up. The two `_scratch` 0-byte staging temps (`snapshot.v44b5.tmp.md` · `pm-handoff.v44b5.tmp.md`) noted at the same census are v44 beat-5 staging debris — Nick may delete at leisure (outside git).
