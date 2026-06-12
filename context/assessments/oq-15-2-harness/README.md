<!--
file: context/assessments/oq-15-2-harness/README.md
purpose: OQ-15-2 microbench harness — archival source + exact run protocol. The harness is SPIKE-class: it runs on the Pi / desktop working tree only and NEVER enters the production repo. This dir is the reviewable source of record.
audience: Nick (runs), PM (authored 2026-06-12), reviewer
status: AUTHORED 2026-06-12 — Pi-evidence session (R2/R3 defaults per session record)
-->

# OQ-15-2 Microbench Harness (spike — archival copy)

Implements `context/assessments/2026-06-07_M5-D_Pi4_AES-GCM_write-path_microbench_spec_OQ-15-2.md`
§3.A (per-event cost), §3.C (chain-hash context), §3.D (intrinsics-off guard), §3.E (hygiene guards).

**Methodology deviations (ruled veto-or-default this session, recorded in §8):**
R2 — JMH replaced by a zero-dep SampleTime-equivalent standalone harness (no JMH in the
version catalog; one-shot bench doesn't justify a production build change). R3 — §3.B's
production-write-path-encrypting rig is unbuildable pre-M6.3 (E2 bridge held-not-consumed);
G2 = measured plaintext baseline (D1 spike ceilings + Pi4SustainedLoadIT current-HEAD run)
+ analytic composition at derived R_C. R1 — device is a Pi 5: NON-AUTHORITATIVE per spec
§3.D, intrinsics forced OFF (Pi-4 emulation), conditional-accept ruling per session record.

## Run protocol

1. **Corpus (desktop):** copy `CorpusDumpOQ152Test.java` into
   `core/persistence/src/test/java/com/homesynapse/persistence/`, run
   `./gradlew :core:persistence:test --tests "*CorpusDumpOQ152*"`,
   corpus lands in `core/persistence/build/corpus-oq15-2/`. **Delete the file after — never commit.**
2. **Deploy (desktop → Pi):**
   `ssh pi 'mkdir -p ~/bench-oq15-2/corpus'`
   `scp core/persistence/build/corpus-oq15-2/*.bin pi:bench-oq15-2/corpus/`
   `scp ../nexsys-hivemind/context/assessments/oq-15-2-harness/{BenchOQ152.java,bench-oq15-2-driver.sh} pi:bench-oq15-2/`
3. **Governor (Pi, once per boot):**
   `echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`
4. **Run (Pi):** `cd ~/bench-oq15-2 && chmod +x bench-oq15-2-driver.sh && ./bench-oq15-2-driver.sh`
   (~2–3 min). Paste the ENTIRE output.
5. PM transcribes into the spec's §8 RESULTS/DECISION block verbatim and applies the §6 per-category rule.
