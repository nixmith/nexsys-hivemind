<!--
file: context/instructions/2026-09-11_coder-lane_CI-1_bus-soak-off-the-gate_coding-instruction.md
purpose: CI-1 — take the bus-soak amplifier OFF the gate without losing it as a sample source. BusSoakIT and BusPositionCensusIT reproduce the bus class on the two-processor runner on nearly every push (samples #10, #11, #12 all RED at lifecycle), which makes `check` red for every landing while FIX-2b-ii is still being authored. This lane tags the two ITs, excludes the tag from every `check` run unless a property asks for them, and adds a second, non-gating CI job that runs exactly those two ITs on every push and uploads their XML. The hero IT stays in `check` (the class's original signal, now carrying the diagnostic and the dump).
audience: the Coder (a host-side Claude Code session on homesynapse-core at 6af76f7; the Java slot) · the hub
state-type: coding instruction
status: ISSUE-READY (authored v70, after beat 9, Fri 2026-09-11 ~22:3x CT; instrument 2026-09-12T03:35:42Z). Dispatches on Nick's paste (§8). Small: 4 M + 0 A, ≤30 minutes.
baseline: core `6af76f7` (HERO-1b). Re-verify: `git log -1 --oneline` prints `6af76f7`; `git status --porcelain` empty.
-->

# CI-1 — the soak off the gate, kept as a sample source

## §0 The lane contract
`date -u` first. Read-set: this file · `.github/workflows/ci.yml` whole (52 lines) · `build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts` `:44–:80` · the class headers of `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusSoakIT.java` and `BusPositionCensusIT.java` (`:1–:110` each). Return: `context/audits/<CT date>_CI-1_return.md`, ≤6 KB, §0 card first, `RETURNED <path> <bytes>` last. Instrument limit: `./gradlew :lifecycle:lifecycle:test --offline` with and without `-PincludeBusSoak`; the workflow YAML is verified by reading, not by running (CI on Nick's push is the proof). Commit nothing; stage nothing.

## §1 What this implements
1. **The tag.** `@Tag("bus-soak")` on the two IT classes (`org.junit.jupiter.api.Tag`, already on the test classpath — ground: `grep -rl 'org.junit.jupiter.api' lifecycle/lifecycle/src/test | head -1`). The hero IT is NOT tagged.
2. **The exclusion.** In the conventions' `tasks.withType<Test>().configureEach` block, replace `useJUnitPlatform()` with `useJUnitPlatform { if (!project.hasProperty("includeBusSoak")) excludeTags("bus-soak") }`. Every `check` and every `:module:test` excludes the two ITs unless `-PincludeBusSoak` is on the command line.
3. **The non-gating job.** In `.github/workflows/ci.yml`, a second job `bus-soak` (name: `Bus soak (non-gating sample)`), `runs-on: ubuntu-latest`, `timeout-minutes: 15`, `continue-on-error: true`, the same three setup steps as `check` (checkout, JDK 21 corretto, setup-gradle), then `run: ./gradlew :lifecycle:lifecycle:test --tests '*BusSoakIT*' --tests '*BusPositionCensusIT*' -PincludeBusSoak --no-daemon`, then an upload step `if: always()` of `lifecycle/lifecycle/build/test-results/` and `lifecycle/lifecycle/build/reports/tests/` as `bus-soak-${{ github.run_number }}`, `retention-days: 14`. The `check` job is untouched.

## §2 Files (exact)
| Path | M/A |
|---|---|
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusSoakIT.java` | M (the import + the annotation) |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/BusPositionCensusIT.java` | M |
| `build-logic/src/main/kotlin/homesynapse.java-conventions.gradle.kts` | M (one line becomes a block) |
| `.github/workflows/ci.yml` | M (the second job) |
Census: **4 = 4 M + 0 A.**

## §3 STOP gates
`ci.yml:17–:20` = the `check` job header as quoted above · `ci.yml:39` = `run: ./gradlew check --no-daemon --continue` · `ci.yml:46–:52` = the upload step with `**/build/test-results/` · the conventions block contains exactly one `useJUnitPlatform()` (`grep -c`) · `@Tag(` appears in no test file today (`git grep -c '@Tag(' -- '*.java'` = 0) · the lifecycle suite at HEAD = 83 testcases (a fresh `--rerun`).

## §4 Predictions (adjudicate first)
P1 — after the change, `./gradlew :lifecycle:lifecycle:test --rerun --offline` runs **81** testcases (the two ITs excluded) and `… -PincludeBusSoak` runs **83**; both green on the desk. P2 — `grep -n 'bus-soak' .github/workflows/ci.yml` shows the job name, the tag property and the artifact name; `yamllint`-free: the file parses (`python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/ci.yml'))"` if python3 with PyYAML exists on the desk; else disclose). P3 — the hero IT still runs in the 81 (its class name in the XML set).

## §5 What to watch out for
The tag exclusion applies to every module's test task (harmless: only two classes carry the tag). The `hasProperty` check reads the project property, not a system property. Keep the second job's steps byte-identical to `check`'s setup steps except the `run` and the upload. Do not touch the hero IT, the diagnostic, or the soak's body.

## §6 Out of scope
FIX-2b-ii (the fix) · any change to the two ITs beyond the annotation · frontend.yml · install-smoke.yml.

## §7 Success criterion
The desk counts 81 / 83 as P1 says; the YAML parses; the return filed. On Nick's push: `check` runs without the two ITs (the hero IT's red rate returns to its own); `bus-soak` runs them and uploads their XML on every push — sample source intact, gate restored.

## §8 Nick's paste (a host-side Claude Code session in `homesynapse-core` on `main` at `6af76f7`)
```
date -u first. You are the Coder for CI-1 on homesynapse-core (the nexsys-coder skill governs). Read ../nexsys-hivemind/context/instructions/2026-09-11_coder-lane_CI-1_bus-soak-off-the-gate_coding-instruction.md WHOLE and its §0 read-set. Verify the baseline (git log -1 --oneline prints 6af76f7; git status --porcelain is empty) and every §3 gate before you write. Four files, 4 M + 0 A, nothing else. Measure P1 both ways with --rerun --offline. Commit nothing; stage nothing. Write the return to ../nexsys-hivemind/context/audits/<today CT>_CI-1_return.md (≤6 KB; §0 card first; P1–P3 first; the last line `RETURNED <path> <bytes>`) and say that one line to Nick.
```
