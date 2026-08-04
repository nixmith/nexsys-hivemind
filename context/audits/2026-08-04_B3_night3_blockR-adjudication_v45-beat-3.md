<!--
file: context/audits/2026-08-04_B3_night3_blockR-adjudication_v45-beat-3.md
purpose: The hub's adjudication of the BLOCK-R escalation reads (run 2026-08-03 ~19:49 EDT) against the night-3 evidence read's pre-stated hypotheses — level-1 verdict, the source-grounded mechanism re-ranking, the pre-stated night-4 arithmetic, and the interpretation caveats that must be on the record BEFORE tomorrow's gate.
audience: Hub (v45), Nick, the fix-ruling beat
state-type: adjudication (point-in-time)
status: FILED 2026-08-04 (v45 hub, beat 3; the reads ran 2026-08-03 evening — crossed-midnight filename per the standing law)
provenance: Nick's BLOCK-R paste (R-0..R-5) + BLOCK-P paste (the refresh, verified) are the primary record; the source reads (ping implementation; module layout) ran at host git-clean worktree, homesynapse-core @ 60d3ab5. Predictions for these reads were pre-filed in 2026-08-03_B3_night3_command-confirm-s31_clean-park-FAIL_evidence-read.md §4–§6.
-->

# BLOCK-R Adjudication — night-3 s31 thread (v45 beat 3)

## 1. Level-1 verdicts

- **H-2a (standing settle-impotence) is DEAD.** R-5 at 23:49:03Z: `on=false`, `availability=AVAILABLE`, `lastChanged=1785745896.014` = **08:31:36.014Z — the Aug-3 settle's own confirmation moment to the millisecond** (CONFIRMED event 08:31:36.025Z rode the report at .014). The relay is OFF and the settle put it there.
- **EDGE-OCCURRED is STRONGLY FAVORED for both FAIL nights.** The Aug-2 settle turn_off CONFIRMED in **143 ms** (ACCEPTED 08:31:31.432 → CONFIRMED .575, match_type exact) — a sub-second value-matching report is a real off-edge to near-certainty (coincidence would require device traffic inside a 143 ms window), which means **night-2's timed-out turn_on HAD physically turned the relay ON**. Night-3 has the same shape at 3.59 s (settle ACCEPTED 08:31:32.428 → report 08:31:36.014). So both nights read as: **the command executed, the relay clicked, and the ON-edge report did not arrive inside the ~5.2 s window** — late/absent evidence, not command loss, not core dishonesty. H-2b (command loss) is DISFAVORED, final closure by tonight's arithmetic (§4). Caveat held open: a value-matching *periodic* report could in principle confirm a no-change settle — the ledger's matching semantics get a source read at beat 4; the 143 ms case is effectively immune to this caveat.
- **The asymmetry is now measured:** OFF-edges reported at 0.14 s and 3.59 s (both CONFIRMED); ON-edges exceeded 5.19 s twice (TIMED_OUT). Same device, same minute — the difference is WHEN in the boot the command fires, not which direction (see §2).

## 2. The mechanism re-ranking (two hypotheses materially moved)

- **NEW STRUCTURAL PIN — the three-boot choreography:** R-2/R-0 show the nightly runs THREE app boots (quiesced boot #1 04:30:20 → quiesce-evidence read :32 → SIGTERM; **suite boot #2 04:30:39** — the boot-health leg's own restart; restored boot #3 04:31:43). The s31 turn_on fires at 04:30:51.78 — **~12.4 s after process start, ~1–2 s after boot #2's network resume**, on a coordinator whose previous session was cut mid-close seconds earlier (boot #1's teardown logged `transport_failed` + a watchdog reopen racing shutdown at 04:30:32–34). The settles that CONFIRM run at ~+53 s, where the path is demonstrably healthy.
- **H-3a (boot ping wave) is WEAKENED AT SOURCE, two independent ways:** (1) the availability ping is **one ZCL Basic-cluster Read Attributes** (`ZigbeeIntegrationAdapter.java:539–561`, `AVAILABILITY_PING_TIMEOUT_MILLIS=5000`) — a Basic read neither carries the on/off attribute nor touches the on/off cluster's reporting clock; (2) pings are gated on **>10 min silence** (`StandardAvailabilityTracker.MAINS_PING_SILENCE=10min`), and the nightly's boots seed evidence from the sidecar written seconds earlier (`availability_seeded: devices=6 from_sidecar=6 unknown=0` at 04:30:24) — **no ping wave is due near the command window on a nightly boot.** The deploy-night "first-boot mains pings" fired because THAT boot's sidecar was stale; nightly boots are not that case. Good product news: the availability arm is NOT interfering with confirmation.
- **THE LEAD IS NOW H-1: MARGIN EXHAUSTION AT THE BOOT-ADJACENT WINDOW.** The leg asserts a ~5.2 s CONFIRMED on the worst-confirming device ~1–2 s after a double-restart network resume. The margin finding already on file said 3.652 s = 68% of window (n=3) — **the best observed pass had 1.35 s of headroom at exactly this offset.** Nights 2–3 read as that latency distribution's tail crossing the window, possibly aggravated by boot-adjacent radio state (route re-establishment after the messy teardown). The build correlation (one pre-deploy PASS vs two post-deploy FAILs) is n=1-vs-2 and now mechanism-weakened — H-3 demotes to *unexcluded contributor*, testable only by accumulating nights.
- Residuals recorded, not load-bearing: the settle-latency spread (0.14 s vs 3.59 s) is consistent with report-clock state left by each night's late ON-report; R-5's `lastReported` was 38 s fresh at 23:49 with `stateVersion=4708` — the S31 produces device-originated traffic at minutes-scale all day, whose exact source (native periodic reporting vs ping-evidence bookkeeping) R-9 measures cheaply.

## 3. Instrument state (BLOCK P verified)

Pull `a791c99..41a7a3c` FF-clean · both script modes 100755 · zero CR · units re-copied + daemon-reload · `KillMode=process` `Type=oneshot` · timer next fire Tue 04:30 EDT. **Tonight's fire runs the hardened instrument: A-9 post-window state read, A-6 tiered app-log capture, A-3/A-4/A-5 wrapper legibility.** The scenarios are byte-identical — no retune occurred. Beat-2 landed `7027283` (exactly 3, pushed).

## 4. PRE-STATED for the Aug-4 gate (filed before the fire)

Baseline pinned at 23:49:03Z: **`stateVersion=4708` · `lastChanged=08:31:36.014Z` · `on=false`.** Tomorrow's gate adds ONE read (`bench.sh state` on the S31) beside the standard four; the arithmetic:

- **If the s31 leg FAILs again:** `post-window-state.json` in the bundle. **⚠ INTERPRETATION CAVEAT, pre-stated: A-9 reads the STATE VIEW ~seconds after the verdict — under a late-report mechanism the view may still read `on=false` at that moment. `on.value=true` PROVES the edge; `on.value=false` does NOT prove no-edge.** The decisive arithmetic is the morning state read: an overnight `lastChanged` pair (an ON transition ~04:30:5x–04:31:3x and the settle's OFF after it) and/or a `stateVersion` advance consistent with an ON+OFF pair ⇒ EDGE + LATE REPORT confirmed ⇒ the mechanism is the margin class and the fix ruling proceeds on H-1. A morning read showing `lastChanged` STILL 08:31:36.014Z from Aug-3 with the settle having TIMED_OUT no-change ⇒ genuine no-edge ⇒ H-2b revives and the thread re-opens at the delivery layer.
- **If the s31 leg PASSes:** the ON-latency line prints its value — expect it near the window edge (>3 s); the thread closes as the margin class with variance, and the C4 estimator inherits the distribution question.
- Either way: **the fix ruling happens AFTER this read, on Nick's word** (§5). Hands off the S31 until then.

## 5. The fix space (priced now, ruled later — nothing here authorizes a change)

- **(i) Bench-side precondition amendment (F1-class, Nick-ruled, pre-freeze eligible, cheap):** move `command-confirm-s31` later in the suite (the settles prove the path healthy at ~+55 s post-resume) or give the leg a post-resume settle delay. This aligns the leg with its own measured physics — an evidence-backed precondition fix in the exact lineage of the split-settle and park rulings, NOT a truth-dodging retune. REC-pending-tonight.
- **(ii) Window retune (5 s → measured percentile):** only with a latency distribution in hand — the ON-latency digest line exists to feed exactly this (the C4 estimator). Blunt; not preferred alone.
- **(iii) Product-feature candidate for the charter (post-gate): report-physics-aware confirmation** — the ledger knowing a device's report constraints (min-interval, best_effort posture) and extending/annotating the window honestly ("confirmation pending — device report-limited; window extended") instead of a flat timeout. This turns the s31 lesson into the explainability moat applied to the write path — a differentiator no incumbent ships. Charter input, named here.
- The never-false-CONFIRMED property is untouched by all three — we tune WHEN evidence is demanded, never invent it.

## 6. Owed follow-ups

R-8 (the suite-boot `bench-2026-08-03-043039.log` full read — boot #2's exact resume timestamp + any command_result lines) and R-9 (two spaced state reads — the day-cadence + stateVersion semantics) ride tonight's small operator block; the ledger matching-semantics source read rides beat 4 with the S-5 grounding. The Hue re-power H3 line item gains a constraint from resolved.json: the Hue's lamp previously rode the S31 relay — **re-power the Hue on a DIRECT outlet, never back through the S31** (a nightly-toggled supply would power-cycle it nightly).
