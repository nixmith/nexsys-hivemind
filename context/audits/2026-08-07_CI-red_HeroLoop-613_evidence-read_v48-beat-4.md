<!--
file: context/audits/2026-08-07_CI-red_HeroLoop-613_evidence-read_v48-beat-4.md
purpose: The v48 beat-4 evidence read on the Build & Check CI red at core 8955e23 (:lifecycle:lifecycle:test — HeroLoopHardwareFreeIT, AssertionError :613). Per-hypothesis predictions FILED BEFORE the discriminating reads (law 9). Also owns a gate-record hole found during grounding.
audience: hub; Nick (three discriminating reads); the fix WU when authored.
status: FILED 2026-08-07, v48 beat 4. OPEN until the fix WU's CI-green closes it.
-->

# CI-RED — HeroLoopHardwareFreeIT :613 — Evidence Read (v48 beat 4)

## 1. The intake (verbatim facts from Nick's CI paste)

Build & Check on core `8955e23` (pushed 2026-08-07): `:lifecycle:lifecycle:test` FAILED — `HeroLoopHardwareFreeIT` ("the hero loop: a motion edge fires the automation…honest state_confirmed") FAILED, `java.lang.AssertionError at HeroLoopHardwareFreeIT.java:613`; **60 tests completed, 1 failed**; every other module's `check` green; BUILD FAILED in 3m 9s. (The 60-test count matches the S-5c desk gate record exactly — same suite.)

## 2. Grounded at source (this beat, at `8955e23`)

- **:613 IS the `awaitTrue` timeout throw** (`throw new AssertionError("timed out awaiting " + what)`; 500 polls × 20 ms ≈ 10 s). :604 is the sibling `awaitEnvelope` throw — NOT the line that fired.
- **`awaitTrue` call sites inside the failing test** (`heroLoop_motionToHonestConfirmed`): `:98` (occupancy values non-empty) · `:102` (occupancy contains "true") · `:115` ("the dispatched On frame"). **The AssertionError's message string names the exhausted await — this is the primary discriminator.**
- **The delta chain since the last spine-banked CI GREEN (`60d3ab5`, v43 beat 3):** `0c57856` (web-ui lockfile, zero Java) → `b3d31b8` (S-5a, toml-only) → `96d9efb` (S-5c, `ZigbeeDeviceCache` + its test — desk gates: full `check` green 156 actionable, `:lifecycle` 60/0/0 forced-fresh on final bytes) → `3723e31` (the dependabot merge commit) → `8955e23` (MODULE_CONTEXT.md only). **The 8955e23 delta is zero-Java and cannot compile into a test failure** — the trigger commit is not the causal commit for any deterministic defect.
- **The prior incident of record:** the `a1f0f77` CI-red — same suite, same shape (count-bounded await exhausted on a starved 2-core runner; HeroLoop:562 `awaitEnvelope` then) — diagnosed as the registry-projection self-delivery racing the test's direct `label()` (`updateEntity`), fixed TEST-ONLY at `7e4426b` (M9.5-DURc) with `awaitRegistryProjectionCaughtUp()` barriers in three ITs, under the **flake-is-a-defect doctrine (never retry-until-green)**. That commit NAMES the structural residual: **LC-LABEL-LOG** — "test labeling rides the log; direct updateEntity from tests races REG-INV-1's projection **by construction**" — the barrier is a mitigation, not a retirement.

## 3. The gate-record hole (owned, §4b class)

Grounding surfaced this independent of today's red: **no CI verdict for the `b3d31b8` / `96d9efb` / `3723e31` pushes was ever intaken into the spine.** The v46 beat-2 order said "push + CI watch"; the push landed, the WATCH has no banked intake anywhere in the record. The last spine-banked core CI GREEN remains `60d3ab5` (Jul-31). Consequence: today's red is not provably the FIRST red — the Actions history read below is therefore mandatory, not optional. Lesson (pm-lessons candidate, minted at the fix WU's close): **a "push + CI watch" order creates a WAIT-STATE that lives in the spine until the verdict banks — an unintaken watch is the deferred-gate class wearing CI clothes.**

## 4. Hypotheses — predictions FILED BEFORE the reads

- **H-A — the label-race family re-fired past the DURc barrier** (a post-barrier registration-fact delivery — candidate mechanism: the M9.4-RPT posture routing's idempotent F1 `entity_registered` re-emit, which the DURc barrier does not await — wipes the label after `label()` ran; the label-targeted automation resolves zero entities silently; no dispatch). **Predicts:** the message = "timed out awaiting **the dispatched On frame**" (:115); occupancy awaits passed; desk forced-fresh stays green; a re-run is probabilistically green. *Prior: the leading hypothesis (same starved-runner physics, same silent-zero-entities signature, a named structural residual).*
- **H-B — pipeline starvation upstream of occupancy** (a new class). **Predicts:** the message names an occupancy await (:98/:102).
- **H-C — the red has been standing since the S-5-era pushes** (the §3 watch hole). **Predicts:** the Actions history shows red on the `96d9efb` and/or `3723e31` runs with the same signature. Compatible with H-A (a probabilistic defect red-ing intermittently across runs).
- **H-D — an S-5c interaction** (the cache write-path change perturbing timing). **Predicts:** deterministic red on re-run AND first-red at the `96d9efb` run. *Prior: low (the cache path is not on the hero-loop assert chain; desk 60/0/0 forced on final bytes) — kept honest, not dismissed.*

## 5. The discriminating reads (operator, in order — read-only, ~5 minutes total)

1. **The Actions-history glance:** for the workflow runs since `60d3ab5` — one line per run: commit → green/red. (Five pushes expected: `0c57856`/`b3d31b8`/`96d9efb`/`3723e31`/`8955e23`; dependabot PR runs count too.) ⏺ RECORD as a table, paste either way.
2. **The failing run's assertion MESSAGE:** open the failed run → the `:lifecycle:lifecycle:test` step / test summary or report artifact → the `HeroLoopHardwareFreeIT` failure block. The string "timed out awaiting …" is the discriminator. ⏺ RECORD verbatim (with the stack's second frame line number if shown — it names the call site directly).
3. **THEN one re-run of the failed job** (an instrument, never a fix — the flake-is-a-defect doctrine stands): pre-stated — H-A/H-C predict probabilistically green; H-D predicts red. ⏺ RECORD the verdict.

## 6. Pre-ruled paths (so no outcome needs a new deliberation)

Whatever the diagnosis: the fix is a **coder-lane WU** (D12 host-CC; test-only expected per the DURc precedent — if diagnosis confirms H-A, the WU evaluates promoting the named **LC-LABEL-LOG** follow-up from mitigation to retirement, scoped test-only), verified desk forced-fresh ×N + full `check`, pushed, **CI green ON that push = the gate of record and closes this file.** Freeze arithmetic: diagnosis this weekend on the three reads → instruction authored same beat → coder lane by Monday → CI green before the skeleton ships. **The freeze (Aug-14 EOD) requires a green gate of record — a probabilistically-green main is not a gate.** The L-E/L-F lanes are read-only and unaffected; S-9 and the skeleton hold schedule.

---

## 7. ADDENDUM — the read intakes (v48 beat 5, 2026-08-07)

**Read 1 (the Actions history, screenshot intaken): H-C REFUTED AT THE INSTRUMENT.** CI #202 `60d3ab5` GREEN (Jul-31) · #203 dependabot PR GREEN (Aug-1) · #204 `96d9efb` (S-5c) GREEN (Aug-5 19:36) · #205 `3723e31` GREEN (Aug-5 19:48) · **#206 `8955e23` RED (Aug-7 06:38) — the FIRST red.** The gate was watched and green throughout the S-5 era.

**The §3 hole, CORRECTED against the operator's record:** Nick DID report the S-5-era greens in-chat at the time. The accurate finding is **REPORTED-NOT-BANKED** — the verdicts reached the hub in chat and were never filed to the spine (the law-11 mild form: chat is not a storage tier), not an unwatched gate. §3's "never intaken" overstated and is corrected here. **Standing rule, minted now:** every CI verdict banks as a one-line spine entry at the next beat — "CI GREEN/RED on <sha> (run #N)" — no exceptions, no deferral to context.

**Read 3 (executed by Nick ahead of sequence, disclosed): TWO re-runs, BOTH RED** — the failed-jobs re-run with debug AND a full all-jobs re-run; same test, same `:613`, 60/1 both times. **The failure is DETERMINISTIC on the current CI environment (3/3).**

**The combined adjudication:** green ×2 on Aug-5 and red ×3 on Aug-7 **on code identical up to one `.md` file** ⇒ no code change caused the flip; the trigger is ENVIRONMENTAL, and the defect is LATENT IN THE TEST/CODE — an environment-sensitive race or assumption whose outcome flipped with the runner environment. The workflow floats on every axis that can drift: `runs-on: ubuntu-latest` (image rollouts), `java-version: '21'` (minor floats), actions at major tags (ci.yml :15/:23–:26). **H-D is DEAD** (the same S-5c code was green twice). **H-A stands refined:** not probabilistically-green — a race now deterministically LOST on the new environment (the DURc doctrine's own words for the prior instance: "04f5f70's green CI was probabilistic"). **H-B remains open** pending the message. The re-run instrument is now exhausted — no further re-runs; the next evidence is the report.

**The completion reads (supersede §5; two remain):**
- **R-1 (decisive):** the failed run's **`test-reports` artifact** (uploaded on failure by ci.yml :34–:40) → `lifecycle/lifecycle/build/reports/tests/test/` → the `HeroLoopHardwareFreeIT` class page → paste (or attach the HTML file to the hub chat) the failure block — the assertion MESSAGE ("timed out awaiting …") + the full stack with the call-site frame. This alone forks the diagnosis (:115 dispatch ⇒ the label-race family; :98/:102 ⇒ occupancy-upstream).
- **R-2 (the trigger pin, 60 s):** run #205 vs run #206 → "Set up job" → the **Runner Image / version** lines — paste both. If the image version differs, the environment-change trigger is pinned at the instrument.

**Shelf note (post-gate, W-2-adjacent):** the gate of record floats its own environment (`ubuntu-latest` + unpinned Java minor). The reproducible-install discipline extends to CI — pinning the runner image + toolchain post-gate makes the gate's environment a declared input instead of a drifting one. Joins the enterprise-grade schedule; nothing moves pre-freeze.

---

## 8. ADDENDUM — R-1 delivered; H-A's prediction CONFIRMED; the fix WU authored (v48 beat 6, 2026-08-07)

**R-1 (the test-reports artifact — read by the hub directly from Nick's extraction on disk):** the failure block reads verbatim: **`java.lang.AssertionError: timed out awaiting the On frame reaching the scripted NCP`** at `awaitTrue` (:613) from the call site **`:115`** — duration 10.344 s (the full poll ceiling). **H-A's prediction CONFIRMED; H-B REFUTED** (both occupancy awaits passed). The failing run's own stdout shows the signature the DURc diagnosis documented: both devices adopt cleanly, then TEN SECONDS OF TOTAL SILENCE — no automation, no `command_issued`, no `command_result`, no frame. The green desk report's hero-loop segment is log-quiet in the same region, so the silence localizes nothing further at INFO level — the within-family fork (label-wipe vs downstream-stall) is an INSTRUMENT QUESTION, assigned to the fix WU's Phase A.

**Extraction hygiene note:** the artifact extracted INTO the worktree nests a full `**/build/reports/tests/` tree under `lifecycle/lifecycle/build/reports/tests/test/` BESIDE a pre-existing local desk report (Windows paths, green) — both under gitignored `build/`, porcelain-invisible, no action needed; the hub read the nested CI copy.

**THE FIX WU AUTHORED ISSUE-READY:** `context/instructions/2026-08-07_M9.5-DURd_heroloop-ci-red_diagnose-and-label-log_coding-instruction.md` — host-CC lane (D12), baseline `8955e23`, TEST-ONLY expected. Shape: **Phase A diagnosis at the instrument** (reproduce under `-XX:ActiveProcessorCount=2` ×5; at timeout capture the fork pair — does the log carry `command_issued`, does the registry record still carry the label; the wiping delivery named at source) → **Phase B pre-authorized only on the confirmed label-wipe arm: the LC-LABEL-LOG promotion** (label rides an idempotent F1 `entity_registered` re-emit through the log, publish-first, barrier-awaited at the re-emit's own position — the structural retirement DURc named) → **Phase C gates** (repro-config ×5 green · lifecycle forced-fresh · full check · §4c grep · diagnostics reverted). DP-2 forbids every flake-paper-over; DP-3 rules the three CI reds AS the red (addition #18). **CI green on the fix push closes this file.** R-2 (the runner-image pair) remains a corroborating read at leisure — no longer blocking.

---

## 9. ADDENDUM — the DURd Phase-A STOP intake: ACCEPT · H-A's mechanism arm dead at source · H-E filed · the A2 discriminator issued (v48 beat 7, 2026-08-07)

**The lane executed the instruction's own pre-ruled STOP** (11/11 green at `-XX:ActiveProcessorCount=2`/`=1`, instrument fidelity PROVEN not assumed; the honest gap disclosed — the flag constrains JVM sizing, not OS scheduling, so the CI starvation axis is unreachable at a 24-core desk). Return ON DISK (law 4; 14,013 B). **Hub layer-2 spot-checks HELD VERBATIM at source:** `awaitRuntimeSubscribersLive` gates exactly {automation_engine, command_dispatch_service, pending_command_ledger, integration_supervisor} (:483–:486) — `state_projection` ABSENT; `StateProjection`'s javadoc rules derived publishes LIVE-only ("No publishes" outside LIVE). The G-2 census matches the hub's own beat-4 grep. **VERDICT: ACCEPT.** Zero code deltas, zero commits, both porcelains clean — every law held.

**Adjudications:** the **H-A MECHANISM arm** (the posture F1 re-emit wiping the label) is **DEAD AT SOURCE for these flows** (no reachable producer: `adoptAcceptList` empty ⇒ posture routing unreachable; driven-mode `run()` parks; `ENTITY_REGISTERED` publisher census = exactly two; the bus boundary fenced) — the H-A PREDICTION (dispatch-leg failure) survives with its mechanism reassigned. **H-E FILED — source-verified, instrument-unproven:** a pre-LIVE `state_projection` processes the occupied report in REPLAY/TRANSITION, where the derived `state_changed` is NEVER published ⇒ the motion edge is swallowed permanently ⇒ the exact `:115` silence; the occupancy awaits read the STORE and prove ingestion only, which is why they pass. Its disclosed weakness (the boot-to-pump wall clock) stands on the record.

**THE A2 DISCRIMINATOR ISSUED:** `context/instructions/2026-08-07_M9.5-DURd-A2_instrumented-branch-capture_packet.md` — test-only fork-capture instrumentation (the lane's documented scratch, generalized), committed by Nick to a THROWAWAY diagnostic branch + DO-NOT-MERGE PR (the PR trigger proven at CI #203); the red run's stdout carries the `=== DURD-A2 FORK CAPTURE ===` block; diagnostic-branch re-runs are lawful (an instrument, not the gate of record). **The fork pre-ruled:** H-E confirmed ⇒ Phase B′ = gate `state_projection` LIVE in the IT harness (test-only, the DURc class) → main push → **CI green closes this file** · labels wiped ⇒ LC-LABEL-LOG re-arms · else ⇒ an engine-stall evidence read with predictions filed first. Coder-lessons +2 intaken; **LC-LABEL-LOG stands as a named post-gate hygiene shelf item on its own merits** (it would not have closed this red).

---

## 10. ADDENDUM — the A2 capture verdict: THREE GREENS on PR #4 — the environment-variance datum; Nick rules Phase B′ = the WINDOW-CLOSURE WU (v49 beat 1, 2026-08-07)

**The capture outcome:** the instrumented diagnostic branch (`af82c16` = `8955e23` + the desk-proven-inert fork capture) ran on the red environment as PR #4 — **GREEN ×3** (the first run + two lawful diagnostic-branch re-runs; Build & Check and install-smoke green throughout; verdicts ⏺ RECORDED at the v49 beat-1 ask and banked per law 16). The instrument did not capture because CI did not red — the packet's own pre-priced contingency, twice over. Re-runs are exhausted; **no further runs anywhere** (MAIN stays forbidden).

**The adjudication:** the environment that was deterministically red 3/3 Thursday morning is green 3/3 Thursday evening against the same test content — the trigger's environmental character is now measured from BOTH sides (the §7 flip in, this flip out). The DURc probabilistic-green doctrine governs: **the greens do not disprove the defect — the 3/3 morning reds proved it exists.** And H-E's race window is **proven at source independent of reproduction** (`awaitRuntimeSubscribersLive` gates four ids with `state_projection` absent :483–:486; LIVE-only derived publishing is fact). The #206 mechanism therefore stands **UNCONFIRMED-PROBABLE-H-E** — permanently, unless a future red re-opens the capture path.

**The ruling (Nick, v49 beat 1):** Phase B′ proceeds **reframed as the WINDOW-CLOSURE WU** — M9.5-DURd-B′ (`context/instructions/2026-08-07_M9.5-DURd-Bprime_state-projection-liveness-window-closure_coding-instruction.md`): the four IT liveness-gate copies gain the `state_projection` LIVE conjunct — test-only, no assertion or timeout touched — a hole-closure, not a paper-over, and not a claimed fix for an unconfirmed mechanism. PR #4 closes unmerged NOW and the diag branch deletes with it — full disposal (Nick's final word at the beat-1 ask, superseding the keep-until-green REC); this section and the return §A2 preserve the instrument verbatim.

**The close condition, restated with the caveat traveling:** this file CLOSES at **CI green on the B′ main push** — the gate of record for the Aug-14 freeze — carrying verbatim: *the #206 mechanism remains UNCONFIRMED-PROBABLE-H-E; the window-closure retires the source-proven readiness gap, and any future recurrence of the :115 signature re-opens this read at the capture step with the A2 instrument pattern re-armed on a fresh diagnostic branch.*
