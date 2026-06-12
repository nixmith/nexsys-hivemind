<!--
file: context/assessments/2026-06-12_OQ-15-2_disposition_encrypted-scopes-CONFIRMED.md
purpose: The dated OQ-15-2 decision record — the MVP encrypted-scope list is FIXED. Companion to the filled §8 block in the microbench spec (the numbers live there; the raw pastes in oq-15-2-harness/). M6.3 gate 1-of-3 CLOSED.
audience: Nick, PM, Coder (M6.3 instruction carries the resolved set verbatim), DOCS reviewer
status: DECIDED 2026-06-12 (PM applied the session R1/R2/R3 defaults, Nick veto-or-default; R1 veto re-opens the hardware-authority residual only — the gates were met with ≥13× margins)
-->

# OQ-15-2 RESOLVED — `encrypted_scopes` default CONFIRMED: `[identity, presence_personal]`

**Decision.** Both candidate categories **stay ENCRYPTED-ON-WRITE at MVP**. The Doc 15 §9
`crypto.encryption.encrypted_scopes` configuration default is **confirmed unchanged** —
per the spec §8 write-back rule, **Doc 15 needs no edit** (the expected-case outcome; §15.2's
`[NON-BLOCKING]` status is discharged). Whether to add the optional one-line currency note to
Doc 15 §9/§15.2 ("OQ-15-2 resolved 2026-06-12; default confirmed by microbench") is **Nick's
documentation-hygiene call** — the only Doc-15 touch this resolution can justify.

**Gates (spec §6, numbers from the filled §8):** G1 — at the real payload distribution (44/82 B)
p50 2.82–4.46 µs, p99 3.28–4.61 µs vs the 60/120 µs gates → 13–37× margins; holds at every
measured size through the 1 KB outlier. G2 — floor PASS by composition (method ruling R3):
24,473 ev/s measured plaintext ceiling (D1 spike, same device) = 49× the 500 ev/s floor;
encryption tax at derived peak rates ≤0.12% of one core; current-HEAD 42-min Pi IT suite GREEN
the same evening. G3 — identity ≈0.0005%, presence ≤0.12% of one core: no flag.

**Hardware-authority residual (R1).** Run on the Pi 5 (A76, crypto extensions present, intrinsics
FORCED OFF per spec §3.D) → formally NON-AUTHORITATIVE; accepted as resolving because the
conditional (≥10× margins) was met with room, and a conservative 3× A72 derating keeps every gate
green. No evidence in the lane has ever touched Pi-4 silicon (the D1 spike was also this Pi 5).
**Optional Pi-4 confirmation run → advisory queue.** A surprising Pi-4 result re-runs the spec §6
rule on authoritative numbers; it does not re-open Doc 15.

**Consequences (applied this session):**

1. **M6.3 triple gate → 1-of-3 CLOSED** (OQ-15-2 ✅ · AMD-86 §3 interview signal ⛔ · OR-M6-NONCE
   rides the M6.3 instruction). M6.3 stays do-NOT-issue until all three close.
2. **M7 entry-gate row 3** (the M6.3-vs-M7 ordering call): the microbench half of the evidence is
   DELIVERED; the energy/erasure interviews remain the open half (Nick-paced, calendar-bound).
3. **The M6.3 coding instruction carries verbatim:** `encrypted_scopes: [identity, presence_personal]`
   as the implemented default, plus the cold-start finding (first ~100 encrypts at 80–700 µs after
   JVM start — consider a JacksonWarmup-style cipher warmup in the M6.3 scope discussion) and the
   OR-M6-NONCE counter-nonce durability obligation (unchanged, co-designed there).
4. **C9 §3.4 energy-scope staging item → RECONCILED/CLOSED** (the C9 record's "the microbench
   resolves whether volume/perf supports encrypting energy"): the measured cost says perf would
   NOT have forced energy out (3.5–19 µs/event at aggregate sizes is trivially affordable at
   energy's ~0.33 ev/s Path-1 rate), but MVP membership stays **plaintext-at-rest on Doc 15
   §3.4's PII-classification grounds** (energy is not PII under INV-PD-03; the data-readiness §6
   shred-scope framing is superseded by Locked Doc 15's D2 line). Extending encryption to energy
   is the Doc 15 §14 post-MVP item, now WITH its cost input measured. The C9 shape decision is
   unaffected either way (its own record says so).
5. **Findings → pm-handoff:** F1 (pi4-validation PI_HOST default ≠ the `pi` alias + no BatchMode),
   F3 (no rsync on Git Bash — the script cannot run as written from Nick's host; tar-pipe manual
   equivalent used and validated), F4 (intrinsic toggles are diagnostic flags — UnlockDiagnosticVMOptions
   required; driver v1 died silently, v2 hardened), F2 (no on-Pi repo at ~/homesynapse-core — intentional).
6. **pi4-validation.sh first exercise: PASS** (manual-equivalent: tar-deploy + remote gradle;
   BUILD SUCCESSFUL 42 m 5 s, 56 tasks, zero failures — the suite's first-ever on-device run).

**Methodology deviations on record (veto-or-default, defaults applied):** R1 hardware (above) ·
R2 JMH→zero-dep SampleTime-equivalent standalone harness (no JMH in the catalog; harness archived
at `oq-15-2-harness/`, 6 warm forks + 2 cold forks across 2 reproducing runs, ±0.5% cross-run
agreement) · R3 §3.B rig→baseline+composition (rig unbuildable pre-M6.3 — the circularity the spec
didn't anticipate).
