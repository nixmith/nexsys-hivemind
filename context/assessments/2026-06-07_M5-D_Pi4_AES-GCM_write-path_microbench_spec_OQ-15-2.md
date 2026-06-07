<!--
file: context/assessments/2026-06-07_M5-D_Pi4_AES-GCM_write-path_microbench_spec_OQ-15-2.md
purpose: M5-D evidence lane — a RUNNABLE Pi-4 AES-256-GCM write-path microbench specification + per-category pass/fail decision rule that resolves OQ-15-2 (the exact MVP encrypted-scope set) and gates the M6 at-rest-encryption WU. PM authors; Nick runs on Pi-4 hardware.
audience: Nick (runs it), PM, Coder (builds the harness if Nick delegates)
update-cadence: once (spec), then the RESULTS BLOCK is filled when Nick runs it
state-type: decision-support / spec
status: SPEC READY — awaiting Pi-4 run. Independently reviewed 2026-06-07 (separate agent, adversarial re-derivation vs source) → RATIFY-WITH-EDITS; the 3 precision/citation/ordering edits are folded (none changed a number or decision; RESULTS block confirmed blank — no fabricated measurements).
last-verified: 2026-06-07 against Doc 15 (LOCKED) §3.2/§3.4/§9/§10/§13.3, HEAD homesynapse-core 8028337
guardrail: This microbench TUNES the encrypted-scope LIST inside Locked Doc 15 (§2.3/§15.2/§16 explicitly delegate the list to it). It is NOT a Doc 15 re-open. If a result implies a DESIGN change (not a list-tuning) — STOP and escalate to Nick (see §7).
-->

# M5-D — Pi-4 AES-256-GCM Write-Path Microbench: Spec + Decision Rule (resolves OQ-15-2)

**Lane:** M5-D (evidence). **Owner of the run:** Nick (Pi-4 hardware). **Author:** PM.
**Resolves:** OQ-15-2 (Doc 15 §15.2 / §16 "Encrypted-scope boundary"). **Gates:** the M6 at-rest-encryption WU (the encrypted-scope set must be fixed before M6 writes the sensitive categories encrypted-on-write — irreversible on the immutable log).
**Status:** SPEC READY. The **Results / Decision** block (§8) is empty until the run lands.

---

## 0. Why this exists, in one paragraph

Locked Doc 15 (§2.3, §3.4) encrypts the **sensitive-PII categories** (`identity`, person-linked presence) **on write** at MVP, and deliberately leaves *one* variable open: **exactly which categories** are encrypted-on-write, "with a category falling back to plaintext-at-rest **only where Pi-4 perf genuinely forces it**" (§3.4, §15.2, OQ-15-2). The decision is now-or-never because the event log is immutable — a category written plaintext at launch can never be retro-encrypted or later crypto-shredded (§0/§1, §5). This microbench produces the Pi-4 numbers that turn that conscious default into an evidence-backed list. **The list is a tuning *inside* the Locked design; this spec does not — and must not — re-open Doc 15 (§7).**

---

## 1. The candidate set — what is and is NOT being measured for encryption

**Candidate categories to evaluate for encrypt-on-write (the Doc 15 §9 / §3.4 set):**

- `identity` — identity records / person-linked identity events.
- `presence_personal` — person-linked presence (the `presence_signal` / `presence_changed` events and any person-linked presence record). Doc 15 §3.4.

These two are **in by default** (Doc 15 §3.4, §9, §15.2; AMD-86 §2.2). The microbench either **confirms both stay encrypted** (the expected outcome — sensitive-PII is low-volume) or **falls a category back to plaintext-at-rest** with measured justification (§6).

**Explicitly NOT a candidate for encryption at MVP (do not measure for the encrypt/plaintext decision — it is the plaintext baseline):**

- `energy` / `telemetry_summary` / device-state / generic telemetry. Doc 15 §3.4 is explicit: *"Non-sensitive high-volume telemetry (e.g., generic `telemetry_summary`, device state) stays plaintext-at-rest at MVP — it is not PII under INV-PD-03 and carries the write-path cost the microbench measures."*

> **Reconciliation note (due diligence — do not let a stale assumption drive the candidate set).** The strategy layer (`context/strategy/HomeSynapse_MVP_Data_Readiness_Specification.docx` §1/§6; `NexSys_Data_Value_Engine_Strategy.docx`) lists **energy** among the "crypto-shredding scopes / sensitive categories." That framing **predates and is superseded by Locked Doc 15's D2 line**: at MVP, energy is **plaintext-at-rest** (non-PII, high-volume; it is the *rate driver* the sustained-throughput gate must survive, not an encryption candidate). Encrypting energy/telemetry is a Doc 15 §14 "extending encryption to additional categories" **post-MVP** item (its cost is set by *this same* microbench when/if a future threat model or buyer requires it). **For OQ-15-2, the candidate encrypted set is `identity` + `presence_personal` only.** Treat energy as the high-volume plaintext load in the throughput rig (§3.B), never as an encrypt/plaintext candidate.

---

## 2. The budget this measures against (the §10 anchors — source of record, not invented)

The pass/fail thresholds come **verbatim from Locked Doc 15 §10 "Performance Targets (Raspberry Pi 4 — the constraint floor)"** and §3.4. These are the GIVEN budget; the microbench produces the measured values to compare against them.

| Anchor (Doc 15 §10 / §3.4) | Value (Pi-4) | Role in the decision |
|---|---|---|
| AES-256-GCM encrypt **per sensitive event** | **~30–60 µs/event** | the per-event cost ceiling; "the microbench (OQ-15-2) sets the encrypted-scope boundary; **Pi 4 has no ARM crypto extensions**" |
| Chain-hash per event (context, not gated here) | ~5–10 µs/event | already-budgeted write-path cost that runs *alongside* encryption (§3.3); included so the combined write-path tax is visible |
| **Pi-4 sustained throughput with encryption on sensitive scopes** | **≥ 500 ev/s** | the aggregate floor that must hold with the candidate encrypted set active |
| Storage overhead (`chain_hash` 32 B/event) | 6–16% of a 200–500 B payload | fixes the representative **payload size band** (200–500 B) for §4 |

Two facts about the environment that the methodology must honor (Doc 15 §1, §10, §3.5):

1. **No ARM crypto extensions on Pi-4.** The Pi-4 (Broadcom BCM2711 / Cortex-A72) ships **without** the optional ARMv8 Cryptographic Extensions. HotSpot's AES-GCM intrinsic requires those instructions, so on real Pi-4 silicon the JDK **falls back to the software AES path automatically** — which is exactly why §10 budgets ~30–60 µs (vs ~3–6 µs on the Pi-5 / Cortex-A76, which *has* the extensions). The microbench MUST reflect intrinsics-off (§3.D). The Pi-5 number is out of scope for the MVP boundary — **the Pi-4 is the constraint floor.**
2. **AES-256, not AES-128.** The DEK is 256-bit (Doc 15 §3.4, §4.2). On a no-AES-intrinsic core, AES-256 runs 14 rounds vs AES-128's 10 (~40% more work). Pin `AES-256-GCM`, 256-bit key, **96-bit (12-byte)** GCM nonce, 128-bit tag (Doc 15 §3.4, §4.1 `payload_iv BLOB(12)`).

---

## 3. What to measure (the four measurements)

Run on **real Pi-4 hardware** (the authoritative environment). Two harnesses, because two different questions are being answered — a per-event cost number that must be *defensible to the microsecond*, and a *system-level* sustained-throughput number.

### 3.A — Per-event AES-256-GCM encrypt cost (JMH; the µs number)

The cost of the `encrypt(DEK(scope), payload_bytes) → (ciphertext, iv)` step at the **Doc 15 §3.2 write-path point** (between `EventSerializer.serialize()` and the single-writer INSERT, on the publishing virtual thread). Measure as a **pure function** so the number is the cipher cost alone, isolated from I/O and scheduling.

- **Operation under test:** one `Cipher.getInstance("AES/GCM/NoPadding")` `doFinal` over one representative payload, with the per-scope counter-nonce assembled as in Doc 15 §3.4 (deterministic 96-bit counter nonce — **never random**; do not call `SecureRandom` on the hot path, that is not the design and would corrupt the number).
  - **Cipher-object reuse must match the intended production shape.** GCM forbids reusing a `Cipher` instance across encryptions without re-`init` (nonce reuse = catastrophic, Doc 15 §6 / OR-M6-NONCE). Measure the realistic path: `cipher.init(ENCRYPT, dek, new GCMParameterSpec(128, nonce))` + `doFinal` per event. (If the eventual impl caches a thread-local `Cipher` and only re-`init`s, measure that; the `init` cost is part of the per-event cost.)
- **Metrics:** **p50 and p99** ns/op (convert to µs). Use JMH `SampleTime` mode (captures the percentile distribution), plus `AverageTime` for the headline mean. Report µs/event.
- **Warm AND cold (Doc 15 §10 "warm/cold"):**
  - **Warm:** standard JMH steady-state (forks ≥ 3, ≥ 5 warmup iters, ≥ 10 measurement iters). This is the number the budget is written against.
  - **Cold:** first-N-operations latency from a fresh JVM (JMH `-wi 0` single-shot `SingleShotTime`, or a separate cold harness capturing the first ~100 encrypts before C2 has compiled the path). Cold matters because the Pi-4 has no AES intrinsic to "warm into" — the software path is the steady state, so warm≈cold is the *expected* result; a large warm/cold gap is itself a finding (flag it).
- **Across the payload-size distribution** (§4): run the benchmark parameterized by payload size (`@Param`) over the representative byte sizes, because AES-GCM cost ≈ fixed setup + per-byte throughput, so the per-event cost is a function of payload size.

### 3.B — Sustained write-path throughput with the candidate encrypted set ON (fixed-corpus soak; the ≥500 ev/s number)

Sustained throughput is a *system* property (VT publish → serialize → **encrypt** → single-writer INSERT → WAL commit), so a pure microbench cannot answer it. Drive a **fixed corpus** through the real persistence write path.

- **Rig:** a fixed-corpus timer (NOT JMH — this is a soak, not a nanobenchmark) that publishes a representative event mix at a **controlled rate** through the production write coordinator, with the candidate encrypted scopes (`identity`, `presence_personal`) actually encrypting and the high-volume plaintext categories (energy/telemetry/state) NOT encrypting — i.e., the real MVP mix.
- **Measure:** sustained ev/s the single writer holds without unbounded queue growth, and the per-event encrypt duration via the **already-specified** `crypto.encryption.encrypt.duration` histogram (Doc 15 §11.1) — reuse production observability, do not hand-instrument.
- **Two load points:**
  1. **Floor check:** the realistic MVP mix at projected peak (§5) — assert sustained **≥ 500 ev/s** aggregate on the write path *with* sensitive-scope encryption active (Doc 15 §10).
  2. **Headroom probe:** ramp the sensitive-category rate up until the writer saturates, to find how much margin exists above each category's projected peak (so the decision is "passes with N× headroom," not "passes at exactly the projected rate").

### 3.C — Combined write-path tax (context)

Report encrypt cost (§3.A) **alongside** the chain-hash cost (§3.3 / §10 ~5–10 µs) so the *total* per-event write-path crypto tax (chain + encrypt) is visible for sensitive events. Chain hashing runs on *every* event regardless; encryption adds on top for sensitive scopes. This contextualizes the encrypt cost against the whole write path but is **not itself a gate**.

### 3.D — Intrinsics-active confirmation (mandatory guard)

The number is only valid if AES intrinsics are genuinely inactive (the Pi-4 reality). Confirm and record:

- Run with `-XX:+UnlockDiagnosticVMOptions -XX:+PrintIntrinsics` (or `-XX:+PrintFlagsFinal | grep -i aes`) and **record** that `UseAESIntrinsics` / `UseAESCTRIntrinsics` / GHASH intrinsics did **not** install on the Pi-4.
- Use the Doc 15 §10 startup SHA-256 micro-benchmark (the "logs whether ARM crypto intrinsics are active" diagnostic) as a cross-check.
- **If the run is done on non-Pi-4 hardware for a sighting shot** (e.g., a dev x86 box or a Pi-5): it is an *approximation only*, and you MUST force intrinsics off to emulate the Pi-4 — `-XX:-UseAESIntrinsics -XX:-UseAESCTRIntrinsics -XX:-UseGHASHIntrinsics` (and `-XX:-UseSHA*Intrinsics` for the chain comparison). **Mark any non-Pi-4 result NON-AUTHORITATIVE** — the OQ-15-2 resolution requires real Pi-4 silicon, because software-AES throughput is microarchitecture-specific (A72 ≠ x86 ≠ A76).

### 3.E — Measurement-hygiene gotchas (a µs-scale benchmark on a Pi-4 is easy to corrupt)

- **Thermal throttling.** A hot Pi-4 down-clocks and will inflate the µs numbers → false FAIL. Use active cooling; monitor `vcgencmd measure_temp` and `vcgencmd get_throttled` (must read `0x0`) before and after each run; discard any run with throttling flags set.
- **CPU frequency scaling.** Set the governor to `performance` (`cpupower frequency-set -g performance`) so DVFS doesn't skew sub-100-µs measurements. Record the locked frequency.
- **Core pinning.** Pin the bench with `taskset -c` to a fixed core (and keep the single-writer on its own core for §3.B) to reduce scheduler noise.
- **Match the deployment JVM exactly** (§7) — heap, GC, flags. A microbench under a different GC/heap than production is not measuring production.

---

## 4. Sourcing representative payloads (do not invent sizes)

The encrypt cost is payload-size-dependent, so the payloads must be the *real* serialized sensitive-PII event bytes, not synthetic blobs.

1. **Use the production serializer.** Serialize representative `identity` and `presence_personal` events through the **real** `EventSerializer` (the AMD-52 typed `{"t":…,"v":…}` payload — Doc 15 §3.2 places the encrypt step on the write path and §7 names the AMD-52 typed payload "the plaintext input to encryption"). The bytes the microbench encrypts must be the bytes persistence would store.
2. **Seed corpus:** start from the existing `TestEventSamples` (`core/persistence/src/test/.../TestEventSamples.java`) and the presence/identity event records in the device/event models; extend with a handful of realistic instances (a presence transition, an identity record). These are already in-repo and contract-shaped.
3. **Derive the size band from the corpus, anchored to §10.** Doc 15 §10 fixes the representative band at **200–500 B/payload**. Measure the actual serialized sizes of the seed corpus, then benchmark across at least: **min, p50, p95, max** of the observed distribution, plus a deliberate **large outlier** (e.g., a presence event with a fat attribute map) to see the per-byte slope. Record the exact sizes used — the result table is keyed on them.

> Do not fabricate a size. If the observed sensitive-PII payloads fall outside 200–500 B, **report the real distribution** and run against it; the §10 band is the expected case, not a constraint on the measurement.

---

## 5. Sourcing the per-category projected write rate (do not invent rates)

The throughput gate (§3.B) needs each candidate category's **projected peak sustained write rate** `R_C`. Derive it; do not guess.

- **`identity`:** account/person/identity changes are **very low frequency** — events per *day*, not per second. `R_C(identity)` ≈ near-zero steady-state with rare bursts (initial household setup). Derive from: the identity/entity model's change cadence (identity records change on person add/remove/edit, not on sensor activity).
- **`presence_personal`:** **episodic**, bounded by sensor report cadence and occupancy transitions. Derive `R_C(presence_personal)` from:
  1. the presence-sensor report cadence in the integration/Zigbee layer (Doc 08 / integration-runtime) — e.g., motion/occupancy/radar sensors report on transition + periodic keep-alive;
  2. a stated **worst-case burst** (e.g., a whole-home multi-occupant presence change — every person-linked presence entity transitioning within a short window);
  3. a stated **safety multiple** over the burst (e.g., 2–3×) so the gate is conservative.
- **Plaintext load context:** from the data-readiness spec (`§4`), the plaintext rate driver is energy/telemetry — Path 1 ≈ 28,800 events/day at 10 plugs @30 s (~0.33 ev/s avg, bursty); Path 2 (Tier-2 whole-home monitors) ≈ 691,200 samples/day aggregated to `telemetry_summary`. The MVP plaintext mix is modest; use it as the §3.B background load so the ≥500 ev/s floor is tested against a realistic *aggregate*, not the sensitive categories in isolation.

> These are **methodology**, not numbers to assume. Record the derived `R_C` per category with its basis (which adapter cadence, which burst assumption, which multiple) in the §8 results block. A reviewer must be able to re-derive `R_C` from the cited basis (the Research-6 module-info discipline, applied to rates).

---

## 6. The decision rule (per category: encrypt-on-write at MVP vs plaintext-at-rest fallback)

For each candidate category **C** ∈ {`identity`, `presence_personal`}, with measured per-event encrypt cost (§3.A) and derived peak rate `R_C` (§5):

**C is ENCRYPTED-ON-WRITE at MVP (the default — keep it in `encrypted_scopes`) iff ALL of:**

- **(G1) Per-event cost within budget.** Warm **p99 encrypt cost ≤ 120 µs** AND **p50 ≤ 60 µs** on Pi-4 (intrinsics confirmed off, §3.D), across the representative payload sizes (§4). *Rationale:* Doc 15 §10 budgets the per-event cost at **~30–60 µs**; p50 ≤ 60 µs holds the §10 upper target, and a p99 ceiling at **2× the §10 upper bound** allows for software-AES tail/scheduling variance without admitting a pathological tail. The 30 µs lower figure is the expected-best, not a gate.
- **(G2) The sustained floor holds.** With C in the encrypted set, the **whole write path** sustains **≥ 500 ev/s** at the realistic MVP mix (sensitive scopes encrypting + bulk telemetry plaintext) and projected peak (§3.B floor check). This is the Doc 15 §10 **aggregate write-path floor with sensitive-scope encryption active** — not a sensitive-scope-only rate — i.e., **adding C does not pull the sustained write-path throughput below the §10 floor**. Pass requires the floor met **with positive headroom** above `R_C` (record the headroom multiple from §3.B's ramp).
- **(G3) Core-budget sanity (soft — a flag, not a hard fail).** The encryption tax for C (`R_C × per-event cost`) consumes a **bounded, documented share of one Pi-4 core**. Flag if a single category's tax exceeds **~10% of one core** — that is a signal C is higher-volume than the "sensitive-PII is low-volume" assumption (Doc 15 §10 rationale) and warrants a conscious second look, even if G1/G2 pass.

**C FALLS BACK to plaintext-at-rest (consciously, documented) iff it fails (G1) or (G2)** — this is the Doc 15 §3.4 / §15.2 "only where Pi-4 perf genuinely forces it." A fallback MUST record:

1. the measured numbers that forced it (which gate, by how much);
2. the **threat-model consequence** (Doc 15 §12): that category's PII is then **plaintext-at-rest** — a live exfiltration hole for key-excluding-copy / less-privileged-read scenarios — until Tier-2 or whole-install-reset; AND that category is **never crypto-shreddable on the launch-era corpus** (immutable log, Doc 15 §5) — the permanent, now-or-never cost;
3. an explicit statement that the fallback is the **conscious tuning Doc 15 delegates to this microbench** (§2.3/§15.2/§16), **not** a Doc 15 re-open.

**Expected outcome (stated so a surprising result is visible as surprising):** both `identity` and `presence_personal` are low-volume sensitive-PII; at ~30–60 µs/event and `R_C` in the events-per-minute range, the encryption tax is a fraction of one core and the ≥500 ev/s floor is held with large headroom — so **both should PASS and stay encrypted**. If a candidate *fails*, treat it as a notable result: re-verify the rate derivation (§5) and the intrinsics-off guard (§3.D) before accepting a fallback (a false FAIL from a thermally-throttled Pi or a mis-derived rate is the likely cause — see §3.E above).

---

## 7. JVM flags — match the Pi-4 deployment profile (not a default JVM)

The run is only valid if it matches the **Pi-4 Tier-1 deployment profile** (the `DeploymentProfile` the persistence/lifecycle layer ships — heap ceiling, GC, and compilation settings). Concretely:

- **Heap:** `-Xms == -Xmx` set to the Pi-4 Tier-1 profile heap ceiling (under the INV-PR-02 <512 MB steady-state budget — confirm the exact value from the active `DeploymentProfile` / Pi-4 profile, do not guess a number here). `-XX:+AlwaysPreTouch` for stable measurement.
- **GC:** the deployment collector. **Today that is tuned G1 (LTD-01).** Note the open entanglement: the M5-D **Generational-ZGC-vs-G1 Pi-4 spike (C16)** may change the deployment collector — but GC choice barely moves an AES-GCM number (the cipher allocates little if output buffers are reused), so run the microbench under the **current** deployment GC and record which it was. If the GC decision flips later, the encrypt-cost number does not need re-running; the throughput soak (§3.B) should be re-confirmed under the chosen collector.
- **Compilation:** production tiered compilation (match deployment); do **not** disable C2 (the software-AES path benefits from C2; disabling it would over-state cost).
- **Crypto intrinsics:** on real Pi-4, none install (§3.D) — confirm. On non-Pi-4 sighting shots, force them off (§3.D).
- **Preview features:** none required for the cipher path (JDK `javax.crypto` AES-GCM is stable, not preview).

Record the **full, verbatim** JVM command line in §8 — the result is only interpretable with the exact flags.

---

## 8. What the result writes back into (and what it must NOT touch)

**Resolves OQ-15-2** and feeds two Locked-Doc-15 locations — as a **list/config tuning**, the way Doc 15 §2.3/§15.2/§16 explicitly delegates:

- **Doc 15 §9 `crypto.encryption.encrypted_scopes`** — currently `[identity, presence_personal]`. The result confirms this default or removes a category. This list is a **configuration default** value M6 implements; tuning it is a config-default decision, **not a design-doc edit**.
- **Doc 15 §3.4 "the *exact* category list"** — the prose names the default set and explicitly says it "is tuned by the Lane D Pi-4 microbench." The resolved set is recorded as the OQ-15-2 resolution.
- **Prerequisite for the M6 at-rest-encryption WU:** M6 writes the resolved sensitive categories encrypted-on-write under per-scope DEKs. The set must be fixed *before* M6 freezes the write path (irreversible on the immutable log).

**How the resolution is recorded (no Doc 15 re-open):**

- Fill the **Results / Decision** block below with the measured numbers, the per-category PASS/FALLBACK verdict, and the resolved `encrypted_scopes` set.
- Log the OQ-15-2 resolution in the M5-D evidence trail + the LTD-01 reversal-criteria ledger reference (the spikes' shared home), and carry the resolved set verbatim into the **M6 coding instruction** as the `encrypted_scopes` default.
- **If — and only if — both candidates PASS (the expected case):** Doc 15 needs **no change at all** — OQ-15-2 simply resolves "default confirmed," and §15.2's `[NON-BLOCKING]` status is discharged. Whether to add a one-line currency note to Doc 15 §9/§15.2 ("OQ-15-2 resolved 2026-06-DD; default confirmed by Pi-4 microbench") is a **documentation-hygiene call for Nick**, not a re-open, and is the *only* Doc-15 touch this microbench can ever justify.

**STOP-and-escalate (the guardrail — Locked Doc 15 stays inviolate):**

> The microbench may move a category **between the encrypted set and plaintext-at-rest within the existing framework** — nothing more. If a result instead implies a **design** change — e.g., "AES-256-GCM is unviable on Pi-4 even for low-volume sensitive-PII," "the write-path point (§3.2) is wrong," "per-scope app-level encryption can't meet the floor and whole-DB/SQLCipher is needed," or "a different cipher (ChaCha20-Poly1305, OQ-15-4) is required at MVP" — that is **NOT a list-tuning**. **STOP. Do not edit Doc 15. Escalate to Nick** with the numbers, framed as an `ESCALATION` (a possible Doc 15 supersession / OQ-15-4 re-open, Nick's call). The same applies if the run reveals an OR-M6-NONCE-adjacent correctness issue (counter-nonce durability is M6-impl, not this bench, but flag anything observed).

---

## RESULTS / DECISION — (empty until Nick runs it on Pi-4)

```
Run date:                __________   Hardware: Raspberry Pi 4 (BCM2711 / Cortex-A72)  [confirm: no ARMv8 crypto ext]
JDK / build:             __________   Deployment profile: __________  (heap ___ MB, GC ____)
Full JVM command line:   __________________________________________________________________
Intrinsics guard (§3.D): UseAESIntrinsics installed?  NO / YES   (PrintIntrinsics evidence: ______)
Thermal (§3.E):          get_throttled = 0x____   measure_temp before/after = ____ / ____ °C   governor = ________

Payload sizes used (§4): min ___ B, p50 ___ B, p95 ___ B, max ___ B, outlier ___ B   (corpus: TestEventSamples + ____)

Per-event AES-256-GCM encrypt cost (§3.A), Pi-4, warm:
   payload p50 size:  p50 ___ µs   p99 ___ µs
   payload p95 size:  p50 ___ µs   p99 ___ µs
   (cold first-N):    ___ µs   (warm/cold gap notable? ___)
Chain-hash per event (§3.C context): ___ µs    Combined sensitive-event write-path crypto tax: ___ µs

Sustained throughput (§3.B), realistic MVP mix, encryption ON for sensitive scopes:
   floor check:  ___ ev/s sustained   (≥500 required) → PASS / FAIL
   headroom:     saturates at ___ ev/s on sensitive scopes  (= ___× over projected peak)

Derived peak rates (§5):  R_C(identity) = ___ ev/s  (basis: ______)
                          R_C(presence_personal) = ___ ev/s  (basis: ______)
Core-budget (§G3):        identity tax = ___% core   presence_personal tax = ___% core

PER-CATEGORY VERDICT (§6):
   identity:           G1 __  G2 __  G3 __   →  ENCRYPT-ON-WRITE / PLAINTEXT-FALLBACK
   presence_personal:  G1 __  G2 __  G3 __   →  ENCRYPT-ON-WRITE / PLAINTEXT-FALLBACK

RESOLVED encrypted_scopes (Doc 15 §9 default):  [ __________ ]
OQ-15-2:  RESOLVED ____-__-__   |  Any fallback? (record §6.1–6.3 if so): __________
Design implication / STOP-escalate triggered (§7)?  NO / YES → escalation: __________
```

---

## Appendix — source citations (everything above traces to source, HEAD 8028337 / Doc 15 LOCKED)

- **Budget anchors:** Doc 15 §10 (AES-256-GCM ~30–60 µs/event Pi-4; ≥500 ev/s sustained; "Pi 4 has no ARM crypto extensions"; 200–500 B payload band), §3.3 (chain-hash ~5–10 µs).
- **Measurement point:** Doc 15 §3.2 (write-path integration; encrypt between serialize and INSERT, on the VT; JDK-intrinsic) + §3.4 (per-scope AES-256-GCM, 96-bit counter nonce, 256-bit DEK).
- **Candidate set + tuning mandate:** Doc 15 §3.4, §9 (`encrypted_scopes: [identity, presence_personal]`), §15.2 (OQ-15-2, `[NON-BLOCKING]` — "the list is a tuning"), §16 ("Encrypted-scope boundary … exact list tuned by Pi-4 microbench"); AMD-86 §2.2 ("tuned against the Raspberry-Pi-4 AES-256-GCM write-path benchmark, with a category falling back to plaintext-at-rest only where Pi-4 performance genuinely forces it, documented consciously").
- **Irreversibility / now-or-never:** Doc 15 §0/§1/§5, AMD-86 §1/§2.1; decision D2 + its write-path-encryption sub-decision (`context/decisions/2026-06-06_post-M4_M5-window_decisions.md` §D2).
- **Observability reuse:** Doc 15 §11.1 (`crypto.encryption.encrypt.duration` histogram).
- **Payload corpus:** AMD-52 typed payload (Doc 15 §3.2 write-path point + §7 interaction table); `TestEventSamples` (in-repo).
- **Plaintext-load context:** `context/strategy/HomeSynapse_MVP_Data_Readiness_Specification.docx` §4 (energy Path 1/Path 2 rates) — used only as the plaintext background load, NOT as an encryption candidate (Doc 15 §3.4 governs).
- **Energy-is-plaintext reconciliation:** Doc 15 §3.4 (energy/telemetry plaintext-at-rest at MVP) supersedes the strategy docs' "energy is a sensitive/shred scope" framing (data-readiness §1/§6; data-value-engine) — that becomes a Doc 15 §14 post-MVP item.
