<!--
file: context/process/bench-troubleshooting-playbook.md
purpose: The integration-bench troubleshooting doctrine, distilled from the M9.4 silicon arc (iterations 1–4, 2026-07-06/07: TCJ → NCFG → ADP → RPT → KEY/DUR). Read by the PM hub before any bench-iterative WU and by the Coder when authoring observability/instrument arms. THE SEED of a future dedicated troubleshooting/integrations skill — when that skill is built, it starts from this file.
audience: PM hub, Coder, Nick (the operator sections)
state-type: process / discipline
status: CURRENT — authored 2026-07-07 by the v23 hub at close (beat 7). Every rule below was paid for on the bench that week; citations are pointers into the bench record + pm-handoff beats, not copies.
state-pointer: NO project state lives here. HEADs, counts, device IDs, current blockers → the spine (PROJECT_SNAPSHOT + pm-handoff) + the bench record.
-->

# Bench Troubleshooting Playbook (integration silicon work)

The M9.4 arc found FIVE ship-blocking gaps in four bench nights, every one invisible to a green build: TCJ (joins silent — TC never enabled), NCFG (NCP never configured), ADP (proposals never adopted — no acceptance driver), RPT (reporting never configured — no binding/driver), DUR (identities re-mint every restart — no rehydration). The unit suites were green the whole time. These rules are how each was found, and how the finding cost one bench night instead of the go/no-go.

## 1. Instrument first — the next log must be measurement, not theory

Never theorize twice about the same silence. When a bench outcome is ambiguous, the NEXT work unit adds the instrument that makes the following run decisive: the NCFG §1.2 read-back INFO (`ncp_configured` — proved config was APPLIED, not just accepted), the RPT anti-vacuous INFO (`reporting_configured: verified=/degraded=`), the §B key-establishment log (0x009B — turned three iterations of leave-speculation into `status=0x11 ×3`, measured). Corollary for the Coder: **any arm that can succeed silently ships with ONE positive-evidence INFO**; any wire-fact the silicon could contradict lives in an isolated **BENCH-VERIFY constants block** so a correction is a one-constant edit fixing code + tests together (4× proven: 0x0019/0x90, TCJ, NCFG, RPT).

## 2. The mechanism-without-driver sweep — walk THROUGH the gate

A green mechanism with no production caller reads as done and ships as nothing. The class hit FIVE times. The sweep rule: for every runbook-expected behavior, grep-verify the FULL production chain — emitter, caller chain, driver — and when a sweep marks X "gated on Y," sweep X's own driver THROUGH the gate to a production call site. A sweep may terminate only at code that runs in production, never at a classification. (The beat-4 sweep stopped at "reporting is adoption-gated" — the gate opened on silicon and nothing was behind it.)

## 3. Vacuous-VERIFY pairing — absence of failure is not success

A VERIFY step whose healthy state is "no output" is vacuous over a mechanism that never ran (step-11's REPORTING-CLEAN passed while zero reporting code executed). Every no-output-is-healthy check gets a PAIRED positive-evidence line (the runbook's amended step-11 shape: positive grep FIRST, failure sweep second). Also: a grep on an EMPTY `$LOG` prints failure-shaped noise and a misleading `|| echo CLEAN` — shell variables die with the ssh session; re-export before re-running (paid for at iteration 4).

## 4. Closures require timeline-consistent evidence; design the discriminator

A closure claim must survive the timestamp arithmetic. "Operator pressed the button" cannot explain a leave 18 s AFTER a hands-off join — the OBS-2 saga ran three nights because an early plausible attribution masked a device-initiated pattern. Rules: (a) **operator actions are data** — the operator logs every physical act with a timestamp ("pressed ~5 s, ended before :37, hands off after"); (b) diagnosis claims carry confidence labels, and a closure that contradicts recorded testimony is CONTESTED, not merged; (c) when hypotheses disagree, **design the cheap discriminator experiment** — state each hypothesis's predicted outcome BEFORE running it (stays-joined ⇒ benign; leaves in 15–30 s ⇒ device-initiated), then run once, hands off. The same experiment often doubles as a pending silicon leg — take the two-for-one.

## 5. The escalation ladder (never improvised, always WITH Nick)

Silicon fix ordering: (1) decode the evidence against the reference vocabulary FIRST (an unmapped status byte is a decode task, not a guess — 0x11 before any constant moves); (2) one-constant BENCH-VERIFY correction; (3) policy-family adjustment (grounded against the reference stack — bellows/ZHA pairs these devices on this exact stick, so A/B against it isolates OUR config as the variable); (4) architecture-class changes and SD-5-class fallbacks — options framed, Nick rules, never under bench pressure. A flag like "droppable if silicon shows it unneeded" cuts both ways: silicon can also show it LOAD-BEARING and mis-valued.

## 6. Operator procedure bank (Nick's hands — verified behaviors)

- **Hue LCA017 (mains router):** plain wall power-cycle ⇒ re-announce (NO re-join, no TCLK dance); the 6× cycle = factory reset (fresh join) — don't use it unless a fresh join is the point. Joins immediately on power-up when factory-fresh; tolerates TCLK-update irregularities (Signify — a confound, not exoneration, for key-exchange hypotheses).
- **SNZB-03P (sleepy end device):** ONE ~5 s hold until LED flash = leave-if-joined + pairing mode; joined devices that fail the Z3.0 TCLK update LEAVE ~15–30 s post-join (BDB device-side timer) — watch hands-off for 60 s after every join before concluding anything. Sleepy writes must land in the post-announce awake window (~seconds); a sleepy Configure-Reporting TIMEOUT is a posture, not a failure.
- **Session hygiene:** stale NCP after another host's teardown ⇒ power-cycle the dongle (the `bytesReceived=0` false-transport-defect signature); ONE process owns `/dev/zigbee`; the PJ window is 254 s max and re-opens per launch while the key is present — REMOVE the key before the soak; `pkill -f "[c]om.homesynapse.app.Main"` (bracket avoids self-match); logs via `nohup … > "$LOG" 2>&1 &` + `tail -f`.
- **Every iteration records:** the SHA the bench runs, the config diff from the previous iteration (one variable at a time), timestamps of every physical act, and the ⏺ RECORD lines verbatim.

## 7. Restart semantics (until DUR lands — check the spine for its status)

In-memory registries rebuild EMPTY at boot (`InMemoryDeviceRegistry` — no rehydration): post-restart, an adopted device RE-PROPOSES fresh (new deviceId/entityId; the accept-list re-adopts it; old view rows orphan). Consequences to plan around: re-link/`onRejoin` arms are only exercisable WITHIN a process lifetime; entity-ID-bound anything breaks across restarts; view-row counts ≠ live-device counts after any restart. Any bench recipe promising "re-link" must not have a restart between the adoption and the re-announce.

## 8. Communicating with the operator (Nick) — the handoff contract

Every operator mistake in the M9.4 arc traced to a handoff that assumed context the moment didn't have. Instructions to Nick are a CONTRACT with these clauses — violating any of them has already cost a bench round:

- **Every paste-block is self-contained.** Shell state dies with the ssh session (`$LOG` empty → three void greps read as REPORTING-CLEAN). Re-establish every variable at the TOP of every block (`LOG=~/hs-bench/bench-<explicit>.log`); never reference a variable an earlier block set. Label each block with WHERE it runs (desktop repo vs Pi) — terminal confusion is real when two ssh sessions are open.
- **Lead with the goal + done-when, then the steps.** He performs better knowing what success looks like before moving ("done-when: `device_adopted` ×2 + non-empty entities"). One numbered physical act per line; ONE device at a time; state the EXPECTED log line after each act (he verifies by tail-glance, sometimes from across the room — name the distinctive token, e.g. "`proposal_accepted`", not "check the output").
- **Name the anti-actions explicitly.** "ONE power-cycle at the wall — NOT the 6× reset" · "then HANDS OFF for 60 s" · "do NOT restart the app — the live view is evidence." He follows stated constraints reliably; unstated ones don't exist. Include window timing ("the PJ window is 254 s from launch — pair within it or restart to reopen").
- **Ask questions whose answers are timestamps and counts, not judgments.** "Did you touch the button after the join at :37?" beats "was the leave you?" — his "Yes (I pressed it once, to pair)" to a compound question cost a full contested-closure round. One decision per message; options lettered (a)/(b)/(c) with a REC first; a one-word answer must be able to dispatch work ("(b), go").
- **Give expected counts everywhere a glance can verify:** "stages exactly N files" (his commit-check pattern — it has caught real drift) extends to the bench: "expect exactly 2 rows," "≥1 `reporting_configured` line per device."
- **⏺ RECORD + "paste either way."** Mark the paste-points explicitly; "either way" matters — he should never withhold a log because it looks like failure. His timestamps + button-press log ARE instrument data (§4); ask him to note the clock on every physical act.
- **What-if branches: max three, each keyed to a log signature he can grep,** with the action attached ("`reporting_ack_lies` ⇒ STOP-and-ping; `proposal_incomplete_not_adopted` ⇒ power-cycle to re-propose, expected iteration").

**§8 additions (2026-07-10 — the acceptance-run arc; ruled at the v27 retrospective):**

- **Operator blocks get red-first rigor, like code.** Name the expected token AND the failure-mode tokens for every glance (the grep that matched `transport_failed` but not `transient_failure`/`integration.failed` masked the supervisor-retry signature twice); never gate a verification on a race (`sleep`-then-grep is dead — `bench.sh`’s poll-to-decisive-verdict is the pattern); never name a subcommand/flag you have not verified exists (the phantom zigpy subcommand cost a round-trip).
- **Every physical act names its observable success signal IN ADVANCE, and journalctl is a first-class instrument.** “Did the reset take?” must be answerable at act time (the Hue 6× dance failed silently 3+ times; the kernel journal adjudicated both physical questions of the night after the fact). If no app-side token exists for a physical act, name the journal signature.
- **Design runbooks for a tired human.** 3 a.m. operation is a standing condition, not an exception: fewer steps, hard go/no-go gates, zero judgment calls at night, the remedy ladder stated (pkill → sleep → dongle power-cycle; NO reboot unless ruled — a reboot voids the incident timeline; paid for when the foreign-network writer window went un-witnessed).
- **Multi-line heredoc pastes are DEAD as an operator interface** (Git Bash mangled a ~40-line block outright). Files travel by scp/the bridge; paste-blocks stay short, one act per line.
- **All bench operations go through `tools/bench.sh`** (decisive-verdict launches; refuses double-launch; kills the `$LOG`/sleep/grep race class). Operator shell improvisation is the exception and gets a named reason.

## 9. Environment discipline (pointers)

Cowork env-model (`cowork-environment-model.md`) governs: host file tools are truth; VM worktree reads/diffs of fresh writes are phantom-suspect (5 hits across this arc — including a diffstat showing net deletions on a net-addition change and a grep missing a line that existed); `--no-optional-locks` only; git-object sourcing for rotations; §11 for parallel-writer/restart merges (treat the other instance's product as an un-audited return: verify its claims at source, correct against primary evidence, merge — never duplicate; the canonical block is the one the staged commit message describes).
