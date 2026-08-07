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
