<!--
file: context/audits/2026-08-02_B3_night2_command-confirm-s31_evidence-read.md
purpose: The night-2 (Aug-2 04:30 fire) command-confirm-s31 FAIL — the instrument-first evidence read of record, filed per the chat-is-not-a-storage-tier law. Bundle: command-confirm-s31-20260802T083057Z.
audience: Hub, Nick, the B3.1/B3.2 authoring beat
state-type: evidence read (point-in-time)
status: FILED 2026-08-02 (v44 hub, beat 1) — hub adjudication: ACCEPT
provenance: The verdict text (§2) was produced by the analysis pass on Nick's Aug-2 Pi bundle paste and delivered in-chat at the v44 dispatch; the hub verified its load-bearing claims against the pasted primary evidence (§1) before filing. The Pi paste itself (ls + full-file dumps + the bench.sh find) is the primary record; key extracts are pinned in §1.
-->

# B3 Night-2 Evidence Read — command-confirm-s31 FAIL (2026-08-02)

## 1. The primary evidence (pinned extracts, hub-verified against the paste)

- **Bundle:** `/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260802T083057Z/` — 7 files (api-captures.json · journal-slice.txt · MANIFEST.txt · quiesce-evidence.txt · resolved.json · scenario.yaml [mtime Jul-31, as-run] · verdict.txt). `app-log-slice.log ABSENT` per MANIFEST (the G-4 widening candidate rides B3.1).
- **Lifecycle (api-captures, command `01KZ0SHTCKAMR9TCGEDK54R39N`, entity `01KXW1W1SBJZERC9MBAMV2DWKE`, `turn_on`):** ACCEPTED `08:30:51.795524Z` → DISPATCHED `08:30:51.805077Z` (integration `6V1CMGY2HKF4H1FGZ4H7F257FS`) → CONFIRMATION_TIMED_OUT `08:30:56.931802Z`, `terminal: true`. **Window arithmetic (hub-verified): 5.136 s.**
- **verdict.txt:** `FAIL — terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT`; started 08:30:51Z; duration 6.1 s; log `/home/homesynapse/hs-bench/bench-2026-08-02-043039.log`.
- **quiesce-evidence.txt:** post-quiesce read 04:30:32 EDT — `"data":[]` (bench-hero ABSENT, HTTP 200) ✓; post-restore read 04:31:51 EDT — bench-hero PRESENT enabled (HTTP 200) ✓. **The app was alive through the wrapper run** (both reads answered).
- **journal-slice.txt:** two tailscaled `magicsock derp-16` lines only — untargeted noise, benign (the night-1 G-2/D-6 class again).
- **resolved.json:** constants consistent with the committed suite (s31 entity/ieee pins exact; auto-suite order intact).
- **bench.sh of record:** `find` returned exactly `/home/homesynapse/nexsys-bench/tools/bench.sh` — **the repo clone is the tool path of record; `~/hs-bench/` is data.** Future gates and operator blocks use the full repo path.

## 2. The verdict as delivered (verbatim)

> The bundle verdict: honest failure, mechanism identified — P-C REFUTED
>
> The lifecycle read is unambiguous: ACCEPTED 08:30:51.795 → DISPATCHED 08:30:51.805 → CONFIRMATION_TIMED_OUT 08:30:56.931, terminal true. The command reached the radio; no confirming report arrived inside the ~5.1s; the runner asserted exactly what the API said. No false CONFIRMED anywhere, no runner defect, no core regression. Never-false-CONFIRMED held again, unattended this time.
>
> The mechanism class is written in the scenario's own header: this leg asserts CONFIRMED on the worst-confirming device on the bench (best_effort posture since 07-19; reporting unverified at source), and its soundness rests on the park invariant — the previous night's settle leaving the relay OFF with an idle report clock. The park for this run was night-1's settle (Aug-1, 04:31)… and your entire attended Saturday sat between the park and the suite: two unplug/replug cycles, the race commands, the bonus cycle. If the relay was ON at 04:30 (replug restore, or the day's exercise), turn_on = zero edge = no report = timeout — the exact documented 07-30 mechanism, this time caused by the attended day breaking the park, not by scenario design. The bundle can't fully discriminate late-report vs no-edge (no post-window state read — a bench-improvement candidate for the B3.x dispatch), but the class is pinned.
>
> The natural experiment is already armed: last night's suite ended with the settle PASS (08:31:32) — the relay is parked OFF right now. Pre-stated prediction: tonight's 04:30 fire reads 8/9 PASS with ON-latency restored, provided nobody touches the S31 today. A second FAIL under a clean park escalates it to a real thread under the two-fails law. So the standing order for today: hands fully off the bench — especially the S31. (Don't even toggle it to check; the park is the check.)
>
> Recorded: bench.sh lives at /home/homesynapse/nexsys-bench/tools/bench.sh (the repo clone; ~/hs-bench/ is data) — future gates use that path.

## 3. Hub adjudication (v44 beat 1) — ACCEPT

- **Honesty verdict BANKED: never-false-CONFIRMED held UNATTENDED — the first unattended exhibit.** The runner asserted the API's own terminal phase; no false CONFIRMED, no runner defect, no core regression claimed or observed.
- **Mechanism class CONFIRMED against the record:** the documented 07-30 no-edge class (relay already ON ⇒ `turn_on` nets zero state change ⇒ no report inside the ~5.1 s core window), reached this time by the ATTENDED SATURDAY breaking the park invariant (Aug-1 04:31 settle park → the F2 close-out's two S31 unplug/replug cycles + the rejoin-race commands + the bonus cycle, all post-park). Not a scenario-design defect; the 2026-07-31 re-based precondition header priced exactly this dependency.
- **Discrimination gap ADOPTED into B3.1 scope:** the bundle cannot discriminate late-report vs no-edge — **a post-window state read (relay on/off at timeout) joins the night-1 §9 amendment set as item 10.** `app-log-slice` absence on a FAIL leg reinforces §9 item 6 (widen G-4).
- **The natural experiment is ARMED and the predictions are PRE-STATED** (recorded here before the Aug-3 read, per the instrument-first law): the Aug-2 run's own settle leg re-parked the relay OFF (post-restore evidence + settle-last suite order). **Prediction for the Aug-3 04:30 fire: command-confirm-s31 PASS; digest returns to the 8/9 PASS · 1 SKIP(hue-online) form with an ON-latency line present.** If it FAILS under this clean park: escalate to a real thread under the two-fails law — the FIRST act is the post-window state read / evidence read, never a retune (arc-discipline 28).
- **Standing order for 2026-08-02: hands fully off the bench — especially the S31.** No toggles, no "checks"; the park is the check. (The 04P battery leg is unaffected: the pull, if it happened, is passive-watch only; replug on hub order.)
- **Caveat held open:** the KillMode pgrep gate is NOT banked by this bundle — the app was alive DURING the wrapper, but the night-1 kill fired AT wrapper exit. Survival is proven only by the post-`Finished` pgrep read (the morning-gate block, issued in-chat v44 beat 1).
