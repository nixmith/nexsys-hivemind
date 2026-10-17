# HomeSynapse R&D Guide: Hard Problems and Resources

Oct 15, 2026 · @Nick

## What HomeSynapse is building

HomeSynapse is being built as the evidence layer under home automation and AI: a local-first, event-sourced home OS where "the harness enforces; the model only proposes," and every physical action ends in a verdict that never claims more than its evidence. The long-term company objective, in the strategy of record, is to "hold the reference implementation AND the measured corpus of the enforcement floor when that floor becomes a purchase requirement — liability and insurance first, regulation later."

**Where it stands (Oct 15, 2026):** about 94,000 lines of main-source Java in 19 production modules, and about 3,660 tests. It runs Zigbee only (EZSP v13 on one MG24 stick), on one Raspberry Pi 5 rig with 10 registered devices. The rig's record (GATE-2, Oct 15) holds 185 CONFIRMED commands out of 3,009, each backed by the device's own report and none false: 13% of the 1,399 that could confirm. The claim register calls that "honest, not fit."

**What changed in September:** the August Technical Roadmap, a presence-sensing curriculum, is marked not maintained, and Strategy v1.2 (ratified Sep 3) moved the trunk to the evidence floor. This guide replaces that curriculum. The program of record (K-13) and HORIZON-1 remain the plan, and sensing becomes one branch (the B-5 presence corpus).

| Horizon | Objective | Done when |
| --- | --- | --- |
| Now → Nov 25, 2026 | Ship V1 to the first outside household: one-command install, Zigbee on a curated device set, and the explainability view (why did it fire, why didn't it, did it actually happen) | The 72-hour run passes (Oct 30–Nov 2); pilot zero installs in 30 minutes or less; one outside household is live by Nov 25 |
| Dec 2026 → Mar 2027 | Harden the record and the radio; grow to 5–10 pilot homes; rule the beachhead segment (Dec 1–14) | Power-loss durability (TAIL-1), APS acks (ACK-1), backup and restore (RESTORE-1), schema rules (SCHEMA-1) and signed packages have landed |
| 2027 | Build the deterministic floor and put AI behind it: delivery guarantee (B-1), then the policy kernel (B-2), proposers in shadow mode (B-3) and counterfactual replay (B-4) | Research stages S1–S5 exit on their sentences; the hash chain is live with an independent verifier; a first device-signed witness verifies off-hub |
| After the beachhead | Win one paying segment; add Matter as a second radio; build a fabless reference appliance; push a provenance standard into compliance and insurance (Fusion P1–P2) | Paid pilots in one segment; a verifier other parties use; a seat at the CSA |
| Long term | An edge-AI appliance with attestable privacy: "proving how your home ran — and what never left it" (Fusion P3) | Attestation works at the silicon-to-log boundary, outside the Apache core |

## The moat, and what it rests on

The moat is not the code: the core is planned as Apache-2.0, and an AI-assisted clone can copy code and docs in days. What a clone cannot copy is time-indexed evidence — a measured device corpus, a dated claim register, external anchors — kept by a deterministic floor that platforms built without a single writer find hard to retrofit.

| Advantage | Why it compounds | What could erase it | What must become true |
| --- | --- | --- | --- |
| Evidence, not instruction: a custody chain over each device's own witness statement, with graded verdicts | "Model progress absorbs instruction. It cannot absorb evidence." | F-1: someone else ships a default-path signed result of an action, rooted outside the agent stack (in Matter, MCP or a platform) | Witness channels measured per device (Tracks 2, 3); a device-signed witness of your own (Track 6) |
| The deterministic floor: an L1 policy kernel at the single writer | Hard to retrofit into platforms built without a single writer | F-2: it proves cheap to retrofit. Fragments already ship: Apple's App Intents confirmation, Gemini agent hooks, MHS device limits | The kernel exists and is proven (Track 4) on a bus that never loses events (B-1) |
| Honest explanation: the confirmation leg, the never-evicted projection, the general why-not | Home Assistant and Hubitat record that a command was sent, not that it took effect | Home Assistant's "did not trigger" traces (2026.7) put the why-not lead at 12 months or less | Why-not provenance (HORIZON-1 R3); observed vs reconstructed explanations (P-05) |
| Time-indexed assets: device corpus, claim register, external anchors | A clone cannot back-date them. From Dec 9, 2026, the EU's revised Product Liability Directive treats software and AI as products and lets courts presume a defect when evidence isn't disclosed, so a verifiable record becomes a liability asset | Worthless if the record can silently lose or rewrite events | Power-loss durability (Track 1); a live hash chain and anchors (Track 6) |
| Local-first privacy, later attestable privacy | Big Tech's business model can't copy it | "A segment lead, not the lead"; data-value plans can drift into a data-collection product | Household-level privacy accounting (P-07); attestation (Track 6) |
| A standards position: a SCITT profile for actuation evidence, and sensing-consent semantics | Owning an interface others must speak | "Losing this race quietly is the worst outcome" (tripwire T6) | An Internet-Draft before the IETF 129 cut-off, Jul 5, 2027 (Track 6) |

**On regulation:** your v58 strategy beat read the EU Machinery Regulation (from Jan 20, 2027) as favoring a deterministic floor. Its Art. 2(2)(p) excludes household appliances and IT equipment covered by the Low Voltage or Radio Equipment directives, so it likely does not reach a home hub or plug. Confirm with counsel before citing it; the Product Liability Directive is the stronger "liability first" argument.

**Three load-bearing sentences are not true yet.** They come first, ahead of anything new:

- **The log is not hash-chained.** `chain_hash` is written as 32 zero bytes (`SqliteEventStore.java:530`).
- **Durability at a power cut is untested.** The hub survived one unplanned outage in August (the R3a record), but SQLite runs with `synchronous = NORMAL`: a cut can roll back a committed `command_issued` after the relay already switched (HORIZON-1 F1). The invariant (INV-ES-04) and the pragma disagree.
- **The policy kernel and the proposer port do not exist in code.** AI has no seam to enter through yet.

## Problem map

&#91;embedded content: problem map · 7 tracks in 4 layers\]

Read it bottom up: a promise at the top holds only if every layer under it is measured, which is why the accented tracks start first even though the moat is sold at the top.

## Research tracks

Seven tracks cover the open problems, plus one deferred branch. Each track names the problems it closes, what to learn in order, and one spine resource with practice in the same place. Each starts with an experiment that is already a planned work unit, because your study hours come out of NexSys hours.

### Track 1 — Power, storage and time: make the record survive the physical world

Every verdict assumes the log survives a power cut, fits its storage for years, and is ordered in trusted time. None of the three is measured yet.

- **Closes:** HORIZON-1 F1 and TAIL-1 (IR-192, durability at a power cut); bytes written per event and flash life (IR-213); clock trust at boot (`clock_status`, IR-212); NVMe drives without power-loss protection; the state projection's 30 s boot gate at a year-three log size (IR-148's registry walk is already fixed on main).
- **Learn, in order:** crash consistency (fsync, WAL, SQLite's `synchronous` modes); how flash fails (FTL, write amplification, endurance, power faults); power hold-up (a supercapacitor or UPS HAT, a power-fail signal into a GPIO); clocks (RTC, chrony, monotonic vs wall time).
- **Spine:** *Operating Systems: Three Easy Pieces* (free), the Persistence part: crash consistency, journaling, flash-based SSDs. Its homework simulators give the practice.
- **Papers and docs:** Pillai et al., "All File Systems Are Not Created Equal" (OSDI 2014); Zheng et al., "Understanding the Robustness of SSDs under Power Fault" (FAST 2013); SQLite's "Atomic Commit" and "Write-Ahead Logging" pages.
- **Write envelope to measure:** each event commits on its own, and each commit appends a 4 KiB WAL page for every B-tree it touches: the table plus up to six indexes. That is up to about 28 KiB per 501-byte event, or roughly 2.7 GB a day at the rig's 95,600 rows. Group commit cuts both fsyncs and flash wear; IR-213's `/proc/diskstats` reading settles the real figure.
- **Cheap fixes:** the Pi 5's power chip has a built-in real-time clock that only needs the SC1163 rechargeable cell; add `dtparam=rtc_bbat_vchg=3000000` to `config.txt` so it charges. The R3a record's "the Pi has no RTC" should read "no RTC battery fitted"; keep `clock_status`, since an RTC gives approximate time, not trusted time. Also log `vcgencmd get_throttled` and `pmic_read_adc` readings as events: a free under-voltage witness, since a sagging supply can reset the Zigbee stick.
- **First experiment (TAIL-1):** cut power with the P-1 harness, commanded from a second controller, at fixed offsets after a command: 0.5, 2, 10 and 60 s. Run `NORMAL` first as the positive control: it must show losses at the short offsets, or the trial cannot detect a loss at all. Then repeat with an fsync before acknowledging safety-priority writes, and test that the SSD honors flushes.
- **Done when:** fsync-before-acknowledge is in place for safety-priority writes and the SSD honors flushes; no acknowledged event is lost at any offset (20 clean cuts bound the loss rate only below 15%, so the mechanism carries the claim, not the count); hold-up time and bytes written per event are measured; boot emits `clock_status`.

### Track 2 — Radio and protocols: make the witness channel measurable

The confirmation leg is the durable differentiator, yet APS delivery acks are dropped, windows are a fixed 5 s, and timeouts have no recorded mechanism.

- **Closes:** ACK-1 (the APS `messageSentHandler` is never consumed); S31 timeouts with no mechanism on record (22 of 59 runs in HORIZON-1's count); φ-accrual availability (R2, PROBE-1); mesh health (R6, the topology scan is a stub); channel choice from measured spectra; USB 3.0 and PCIe noise near the stick, which already sits on an extension in a USB 2.0 port; the EZSP v13 pin while new sticks ship v14 (IR-202); frame-counter custody on a stick swap (RESTORE-1); Matter or Thread as a second radio with no schema change (MATTER-1).
- **Learn, in order:** IEEE 802.15.4 PHY and MAC (O-QPSK, CSMA-CA, MAC acks, LQI and RSSI); Zigbee NWK, APS, ZDO and ZCL (APS acks, reporting configuration, source routes, frame counters, the trust center); EZSP and ASH; Thread and Matter (RCP vs NCP, subscriptions, sleepy devices, fabrics); RF measurement (spectrum, link budget, antenna isolation).
- **Spine:** the Zigbee PRO specification and Zigbee Cluster Library revision 8 (free from the CSA), read beside Silicon Labs UG100 (EZSP reference) and AN1017 (Zigbee and Thread coexistence with Wi-Fi). For Thread and Matter, Nordic Developer Academy's free *Matter Fundamentals* course, which has hands-on exercises and covers Thread.
- **Papers:** Hayashibara et al., "The φ Accrual Failure Detector" (SRDS 2004); Chandra & Toueg, "Unreliable Failure Detectors for Reliable Distributed Systems" (JACM 1996); Intel, "USB 3.0 Radio Frequency Interference Impact on 2.4 GHz Wireless Devices" (2012). The Pi 5's PCIe Gen 2 link to the NVMe runs at the same 5 GT/s, so it radiates near 2.5 GHz too.
- **Watch:** Zigbee 4.0 (Nov 18, 2025) adds Trust Center Swap Out and Advanced Frame Counter Synchronization, a standard answer to "a stick swap re-pairs every device" once devices support it. Matter 1.6 (mid-2026) ships Joint Fabric, the co-equal controllers P-11 anticipates; P-11's trigger stays the first B-3 run with two principals.
- **Tools:** an nRF52840 dongle running nRF Sniffer for 802.15.4 into Wireshark (one sniffer hears only the hops within its range); a tinySA Ultra spectrum analyzer; the spare MG24 for v14.
- **First experiment:** sniff the air during S31 timeouts and sort each one into MAC ack missing, APS ack missing, report late or report absent. Then run energy-detect scans of channels 11–26 (through EZSP or the sniffer) with the NVMe busy vs idle and the stick on and off its extension, and repeat on the pilot's MG21.
- **Done when:** every UNCONFIRMED in a night's run has a mechanism class; per-device windows come from measured report distributions; v14 runs on the spare stick.

### Track 3 — Verdict statistics and metrology: put an error bar on every CONFIRMED

GATE-2's record (185 of 3,009 commands CONFIRMED, none falsely) comes from one rig and was never treated statistically. The sentence a buyer pays for needs an error rate per device class.

- **Closes:** P-03 (verdict soundness as an anytime-valid test); P-04 (diagnosability of silent failure); the coincidence bound min(1, W/T\_d); SP-4 (a hardware-in-the-loop method for an n = 1 rig); the g4 metering witness (plug bias of +2% to +9% against the P4460 reference).
- **Learn, in order:** probability (the math plan's probability phase, moved up to right after Calc II; see Sequencing); sequential testing, from Wald's SPRT to e-values and anytime-valid inference; diagnosability of discrete-event systems; measurement uncertainty (Type A and B, coverage factor) and design of experiments.
- **Spine:** Blitzstein & Hwang, *Introduction to Probability* (free, with the Stat 110 problem sets; already in your math plan); then Wasserman, *All of Statistics*; then Cassandras & Lafortune, *Introduction to Discrete Event Systems* (3rd ed., Springer, 2021) for diagnosability, shared with Track 4.
- **Papers and standards:** Ramdas, Grünwald, Vovk & Shafer, "Game-theoretic statistics and safe anytime-valid inference" (Statistical Science, 2023), sections 1–3; Sampath et al., "Diagnosability of discrete-event systems" (IEEE TAC, 1995); Dawid & Skene (1979); Peeves (CCS 2019) and HAWatcher (USENIX Security 2021) as prior art on physical plausibility; JCGM 100:2008 (the GUM) and NIST TN 1297 for uncertainty, both free.
- **Sample-size rule to own:** zero failures in n trials bounds the rate below 3/n at 95% confidence (the rule of three; Hanley & Lippman-Hand, 1983). Soundness is P(CONFIRMED | the actuation failed), so the trials must be induced failures, such as the target de-powered through P-1 or its parent router pulled. Claiming "below 1.5%" for one device class takes about 200 induced failures with no false CONFIRMED.
- **First experiment:** run a pre-registered script per device class with three arms: commands toward the current state, where nothing should change; commands that cause a change; and commands to a target you have de-powered, where any CONFIRMED is false. Estimate the coincidence rate against min(1, W/T\_d), and per-device report-latency distributions with confidence bands.
- **Done when:** a P-03 return reaches DESK with a stopping rule validated on the bench corpus; each device class has a window with a stated coverage; the metering witness has an uncertainty budget.
- **Thesis fit:** this is the EE-shaped thesis candidate, sequential detection over unreliable witnesses. It reuses the detection-and-estimation core of the August roadmap.

### Track 4 — The deterministic floor: runtime assurance, formal methods and functional safety

The kernel is the moat's hardest-to-retrofit layer and the gate for every hazardous load in 2027. Today it exists only on paper.

- **Closes:** P-01 (enforceability under an evidence floor); P-02 (bounded composition as admission control); the B-2 kernel; C-S0-3 reversibility and consequence classes, including the time-dependent freezer case; HORIZON-1 R4 (TLA+ models of the ledger and availability tracker) and R10 (a Simplex layer for loads that heat, lock or pump); partial runs with nothing to compensate.
- **Two findings to fix:** Doc 08's Aqara example sets decoupled mode, which would leave the wall switch dead whenever the hub is down, against INV-HO-01 (physical controls always win). And no document defines a device's fail-safe state when the hub dies mid-run.
- **Learn, in order:** security automata and edit automata; supervisory control of discrete-event systems; model checking with TLA+; Simplex and shielding; hazard analysis with STPA, plus the vocabulary of IEC 61508 and UL/IEC 60730-1 Annex H (software classes B and C).
- **Spine:** Lamport's free *Specifying Systems* with learntla.com for TLA+ practice; Baier & Katoen, *Principles of Model Checking* (MIT Press, 2008) for the theory; Leveson, *Engineering a Safer World* (MIT Press, open access), with the free *STPA Handbook* (Leveson & Thomas, 2018).
- **Papers and standards:** Schneider, "Enforceable Security Policies" (TISSEC, 2000); Ligatti, Bauer & Walker, edit automata (2005); Sha, "Using Simplicity to Control Complexity" (IEEE Software, 2001); Alshiekh et al., "Safe Reinforcement Learning via Shielding" (AAAI, 2018); ASTM F3269-21 on runtime assurance.
- **First experiment:** write the TLA+ model of the pending-command ledger and the availability tracker; HORIZON-1 sized it at 2–3 weeks, as a December project. Then run STPA on one load, a space heater on a plug, and turn its unsafe control actions into kernel rules and L0 requirements. On a lamp, test whether your plugs honor the ZCL "On With Timed Off" command. Its timer counts tenths of a second up to 0xFFFE, about 109 minutes, so it acts as a lease the hub must keep renewing. Also set StartUpOnOff (attribute 0x4003) to Off, or a power blip turns the load back on with no timer.
- **Hazardous-load gate, before the first heater, lock or valve in 2027:** an STPA analysis with every unsafe control action mapped to a kernel rule or a device-side mitigation; the timed-off lease and StartUpOnOff verified on each device model; a safe state defined per class (a heater off, a lock that never auto-unlocks); a run that kills the hub under the P-1 harness and shows the load reaching its safe state within the lease; TAIL-1 green.
- **Done when:** TLC or Apalache checks the ledger's invariants; one STPA analysis is filed; a kernel AMD is ratified; P-01(a) reaches DESK.

### Track 5 — AI proposers and agent compatibility

P-10 bets that a floor makes small local models good enough. That bet needs the proposer seam, shadow mode, and a benchmark that scores what physically happened.

- **Closes:** the B-3 seams (`action_proposed`, `proposal_adjudicated`, an AGENT principal type); AIOT-INV-1's E3 test (no AI path can dispatch); P-10 (rejection rate ρ vs model size); P-08 (agent memory as a provenance-carrying fold); C-S0-10 (local-model feasibility); B-8 (kill the proposer host and the home keeps running); the external-agent gateway over MCP ("adopt and sit above"). Not yet registered: prompt injection through device-supplied strings (proposed P-13), a proposer starving the single writer, and the supply chain of model weights.
- **Learn, in order:** how LLM inference works and what limits it on small hardware; constrained decoding to a JSON schema; agent security (prompt injection, keeping control flow apart from untrusted data); evaluation design and experiment tracking.
- **Spine:** MIT 6.5940, *TinyML and Efficient AI Computing* (Fall 2026 lectures are public, with labs on quantization and LLM deployment); then the MCP specification for the gateway.
- **Papers:** Debenedetti et al., "Defeating Prompt Injections by Design" (CaMeL, arXiv 2503.18813); the OWASP Top 10 for LLM Applications (2025); Dong et al., XGrammar (2024) on grammar-constrained decoding.
- **Back-of-envelope to own:** decode speed is capped near memory bandwidth ÷ bytes read per token. The Pi 5's LPDDR4X peaks around 17 GB/s, so a model of about 1.5 GB caps near 11 tokens/s. That fits Google's 7.6 decode tokens/s for Gemma 4 E2B; independent runs measured 2.6–11.7 across 1.5–3B models. The AI HAT+ 2 brings its own memory but needs the Pi 5's only PCIe lane, which the SSD uses, and the Pi's CPU outruns it on LLM decode.
- **First experiment (C-S0-10):** on a spare Pi 5, never PI-2 (the first household's hub), run a 2–4B model in llama.cpp. Measure tokens/s and watts, and check the single writer's p99 does not move: a cgroup caps CPU, not memory bandwidth, and decoding competes with the event writer for the same memory bus. At Google's 133 prefill tokens/s, C-S0-10's 2,000-token prompt takes about 15 s before the first output token, so cache the fixed part of the prompt. Then run the rules engine as proposer number one in shadow mode, and build a test set of hostile device names and attribute strings.
- **Done when:** ρ is measured for two model sizes, with zero unsafe admissions by construction; proposer load stays out of the writer's latency band; a benchmark scores proposals by the device-witnessed outcome, which none of the benchmarks your corpus surveyed does.

### Track 6 — Trust and attestation: the record, the keys and the signed witness

F-1 says the moat falls only to a signature over an action's result rooted outside the agent stack. The safest response is to ship that mechanism yourself: first the log's own chain, then a device-signed sensor node.

- **Closes:** B-7 chain activation (ADR D1–D5, not yet ratified), designed together with retention and crypto-shred and waiting on C-S0-2's column census; external anchors (Rekor v2 plus an RFC 3161 timestamp); P-06 coverage; P-09's rungs (a) to (e); root-key custody with backup (F19) and the separate Zigbee key root; signed, atomic updates (R7, APPLIANCE-1); plugin isolation before any ecosystem, since an in-JVM plugin "can forge the attribute reports that feed ConfirmationPolicy"; CRA and RED basics (SBOM, vulnerability disclosure, EN 18031).
- **A finding to fix in Doc 15:** §3.5 and OQ-15-1 say the Pi 5 has a TPM. Raspberry Pi's security documentation describes OTP-based signed boot and a device-unique secret, and no TPM. The zero-config path exists anyway: Raspberry Pi OS's encrypted-disk flow derives its passphrase from the OTP secret through `rpi-fw-crypto`, and wrapping the root key the same way protects a pulled drive, though not a stolen whole unit or an attacker with root. For rung (b), any root process can make the board sign, so a signature shows which board signed, not that its software was clean.
- **Learn, in order:** hash chains, Merkle trees, signatures and AEAD; transparency logs and remote attestation (RATS, EAT, SCITT); secure boot and TPM 2.0; firmware on a microcontroller with a secure element; enough analog electronics to build the node's sensing front end.
- **Spine:** Aumasson, *Serious Cryptography* (2nd ed., No Starch, 2024), with the Cryptopals challenges as practice; Arthur & Challener, *A Practical Guide to TPM 2.0* (Apress, open access). For the node's electronics, Hayes & Horowitz, *Learning the Art of Electronics* (2016), a lab course, with *The Art of Electronics* (3rd ed.) as the reference.
- **Standards and papers:** RFC 9334 (RATS architecture); RFC 9711 (Entity Attestation Token); RFC 9943 (SCITT architecture, June 2026); RFC 9162 (Certificate Transparency 2.0); Crosby & Wallach, "Efficient Data Structures for Tamper-Evident Logging" (USENIX Security, 2009).
- **The signed sensor node, your one custom board:** a pre-certified radio module, either a Nordic nRF52840- or nRF54L15-class part or an EFR32MG24 part with Secure Vault High from the coordinator's own family (upstream Zephyr has no Zigbee stack, so on Nordic parts use the nRF Connect SDK's Zigbee add-on). Add a factory-provisioned secure element whose certificate chains to its vendor, such as Microchip's Trust&GO ATECC608B, Infineon's OPTIGA Trust M or NXP's SE050 (integrate one, don't design one), and a current-sense chip such as TI's INA228. The node signs (reading, the hub's command nonce, the secure element's monotonic counter) rather than a time, since the hub sets the node's clock. It sends the result on a manufacturer-specific Zigbee cluster; a 64-byte signature nearly fills one secured APS frame, so use APS fragmentation or sign a batch of readings. Start on a 12 V DC load; a mains version waits for an isolated, enclosed design.
- **First experiment:** once C-S0-2's column census is intaken and the B-7 ADR is ratified, activate the chain on a bench branch and measure per-insert p95 on the Pi. Then have a breadboard node sign a current reading that a separate machine verifies against the secure element vendor's certificate chain.
- **Done when:** the chain is live with boot verification inside P-06's cost budget; one signed witness verifies off-hub with a tool that trusts neither the hub nor a key you issued; the RATS/EAT profile (C-S0-7b) is drafted; an Internet-Draft is in before the IETF 129 cut-off (Jul 5, 2027).

### Track 7 — Scale and longevity: run on the next board, the next radio and year three of data

The on-disk format becomes one-way at the first household event (planned Nov 19). After that, versioning, retention, replay time and multi-hub order decide whether the record outlives its hardware and its releases.

- **Closes:** SCHEMA-1's rules (upcasters with golden-bytes tests; snapshots; a reserved hybrid logical clock); retention, still an open one-way word (`RETENTION`, due Nov 2), where the hub recommends a per-install policy, off by default and never before RESTORE-1 (SCHEMA-1 prices a household at 0.44–0.86 GB settled); replay of a settled store taking about 45 s against a 30 s boot gate; deterministic simulation with power-loss injection (HORIZON-1 R1, SIM-1); a multi-hub merge order (R8); the 4 GB and single-SQLite ceilings above about 200 devices; the Matter sidecar's RAM budget; the separate fleet engine.
- **Learn, in order:** schema evolution in event-sourced systems; database internals (B-trees, WAL, query planning); distributed systems (logical clocks, replication, consensus); deterministic simulation testing; performance analysis on ARM.
- **Spine:** Kleppmann & Riccomini, *Designing Data-Intensive Applications* (2nd ed., O'Reilly, March 2026), with MIT 6.5840's free Raft labs as practice; Gregg, *Systems Performance* (2nd ed.) for profiling on the Pi.
- **Papers:** Zhou et al., "FoundationDB: A Distributed Unbundled Transactional Key Value Store" (SIGMOD 2021), on simulation testing; Overeem et al., "The dark side of event sourcing: Managing data conversion" (SANER 2017); Kulkarni et al., "Logical Physical Clocks" (OPODIS 2014).
- **First experiment:** measure replay on the Pi itself, with a cold cache, in seconds per million events, at today's store and at a synthetic year-three store. Then size snapshots so boot stays under the 30 s gate.
- **Done when:** golden-bytes tests guard every event type; boot at year-three size is measured under the gate; SIM-1 reproduces HORIZON-1 F1 in simulation.

### Branch — Sensing and privacy (deferred to stage S5, mid-2027)

Presence sensing moved from the trunk to the B-5 corpus. Keep it alive with one measurement, not a curriculum.

- **Closes:** the four presence metrics (latency to detect, latency to clear, false clear while someone is still, false hold after the room empties) with ground truth; P-07 household-level privacy accounting (release derived artifacts only, never streams); a sensing-consent object, since 802.11bf-2025 has no consent provisions; an ethics determination before instrumenting anyone else's home.
- **Resources:** the August roadmap's detection core stays valid here: Kay, *Fundamentals of Statistical Signal Processing* (Vols. I–II), and Poor & Hadjiliadis, *Quickest Detection*. For privacy, Dwork & Roth, *The Algorithmic Foundations of Differential Privacy* (free).
- **First experiment:** compare the SNZB-06P24 presence sensor with the SNZB-03P PIR on the four metrics, against a simple ground-truth log.

### Problems to add to the register

The analysis found problems the register (P-01 to P-11) does not hold. Power-cut durability, storage wear and clock trust are already engineering rows (IR-192, IR-213, IR-212), so only four research rows are proposed:

| Proposed row | Problem | Track |
| --- | --- | --- |
| P-12 | Radio interference as evidence: how coexistence and channel health move each device's evidence envelope (ε\_d) | 2 |
| P-13 | Prompt injection through device-supplied strings (names, model strings, profiles) | 5 |
| P-14 | A device's fail-safe state when the hub is lost mid-run | 4 |
| P-15 | Mapping the kernel's consequence classes to a safety case (STPA, UL/IEC 60730-1 Annex H) | 4 |

## Sequencing

&#91;embedded content: proposed sequencing · Oct 2026 to Dec 2027\]

Each bar is a proposed window, not a commitment: a track ends on its "done when" sentence, never on the calendar.

**One change to the math plan:** move its probability phase up to right after Calc II (mid-January 2027), ahead of Calc III. Stage S3, graded verdicts, runs about February to April, and Track 3 needs probability first; ODEs are not needed until circuits.

**Choosing the thesis problem.** You chose to make NexSys research your thesis. Three register problems can carry one:

| Problem | Field | Lab to look for | Why it fits |
| --- | --- | --- | --- |
| P-03 with P-04: verdict soundness and silent-failure diagnosability | EE: detection, estimation and controls | Signal processing, controls or cyber-physical systems | The most EE-shaped problem, and your bench already produces the data |
| P-09: the attestation boundary of the witness | EE and CE: hardware security, embedded systems | Hardware security or embedded systems | Builds the signed node; the closest link to F-1 |
| P-01 with P-02: enforceability and bounded composition | CS: formal methods, runtime verification | Formal methods or CPS verification | Publishable theory, but the least EE |

For an EE program, lead with P-03 and P-04 and keep P-09 as the applied chapter; that thesis needs Track 3 first and the Track 6 node second. Timing is a trade-off: most US deadlines for fall 2027 fall in December 2026 and January 2027, so applying then means writing the statement of purpose mid-pilot, before there is a result to cite. A later cycle lets you apply with a P-03 measurement in hand. Either way, name the problem in the statement and write to faculty whose papers appear in your moat curriculum.

## Resource library

Everything the tracks name, in one place, sorted by track. Most of the spines are free; read only the chapters a work unit needs. Hold the purchases (sniffer dongle, spectrum analyzer, secure-element boards, RTC cell) until the households answer, per the v112 purchase rule, then buy them as one line.

| Resource | Track | Format | Start with |
| --- | --- | --- | --- |
| [*Operating Systems: Three Easy Pieces*](https://pages.cs.wisc.edu/~remzi/OSTEP/) (Arpaci-Dusseau) | 1 | Free book with homework simulators | Persistence: crash consistency, journaling, flash-based SSDs |
| Pillai et al., OSDI 2014; Zheng et al., FAST 2013 | 1 | Free papers | Zheng first: how SSDs actually fail on power cuts |
| [RTC battery for Raspberry Pi 5 (SC1163)](https://www.pishop.us/product/rtc-battery-for-raspberry-pi-5/) | 1 | Part, a few dollars | Fit it to the bench Pi and PI-2, with trickle charging enabled |
| Zigbee PRO specification; Zigbee Cluster Library rev. 8 (CSA) | 2 | Free specifications | APS acks and frame counters; ZCL reporting and the On/Off cluster |
| Silicon Labs UG100 (EZSP reference) and AN1017 (coexistence with Wi-Fi) | 2 | Free vendor documents | The EZSP frames you already send; AN1017's isolation figures |
| Intel, "USB 3.0 Radio Frequency Interference Impact on 2.4 GHz Wireless Devices" (2012) | 2 | Free white paper | The noise-floor plots; the same physics applies to the Pi 5's PCIe link |
| [Nordic Developer Academy](https://academy.nordicsemi.com): *Matter Fundamentals*, *nRF Connect SDK Fundamentals* | 2, 6 | Free courses with exercises | *nRF Connect SDK Fundamentals* before building the node |
| nRF52840 Dongle with nRF Sniffer for 802.15.4, and Wireshark | 2 | Tool, about $11 | Capture one S31 timeout end to end |
| [tinySA Ultra](https://tinysa.org) | 2 | Tool, small spectrum analyzer | A 2.4 GHz sweep with the NVMe idle vs busy |
| Blitzstein & Hwang, *Introduction to Probability*, with Harvard's Stat 110 | 3 | Free book and problem sets | Already in your math plan; move it up |
| Wasserman, *All of Statistics* | 3 | Book with exercises | Hypothesis testing, confidence intervals, the bootstrap |
| Cassandras & Lafortune, *Introduction to Discrete Event Systems*, 3rd ed. | 3, 4 | Book with problems | Diagnosability, then supervisory control |
| Ramdas, Grünwald, Vovk & Shafer, *Statistical Science* 2023 | 3 | Free paper | Sections 1–3: e-values and anytime-valid tests |
| JCGM 100:2008 (GUM); NIST TN 1297 | 3 | Free standards | TN 1297 first; it is short |
| [Lamport, *Specifying Systems*](https://lamport.azurewebsites.net/tla/book.html) and [learntla.com](https://learntla.com) | 4 | Free book and tutorial | learntla.com end to end, then model the ledger |
| Baier & Katoen, *Principles of Model Checking* | 4 | Book with exercises | Safety properties and LTL |
| Leveson, *Engineering a Safer World*; Leveson & Thomas, *STPA Handbook* | 4 | Free (open access) | The handbook's STPA steps, applied to one heater |
| [MIT 6.5940, *TinyML and Efficient AI Computing*](https://hanlab.mit.edu/courses/2026-fall-65940) | 5 | Free lectures and labs | Quantization lectures; the LLM deployment lab |
| [Model Context Protocol specification](https://modelcontextprotocol.io) | 5 | Free specification | Tools, authorization, and what the gateway must enforce |
| [Debenedetti et al., CaMeL](https://arxiv.org/abs/2503.18813) | 5 | Free paper | Separating control flow from untrusted data |
| Aumasson, *Serious Cryptography*, 2nd ed., with [Cryptopals](https://cryptopals.com) | 6 | Book plus free challenges | Hashing, authenticated encryption, signatures; Cryptopals sets 1–4 |
| Arthur & Challener, *A Practical Guide to TPM 2.0* | 6 | Free (open access) | Keys, sealing and attestation, for rung (e) or an add-on TPM |
| Hayes & Horowitz, *Learning the Art of Electronics*; *The Art of Electronics*, 3rd ed. | 6 | Lab-course book; reference | The early labs, through op-amps, before laying out the node |
| [RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html) (SCITT), RFC 9334 (RATS), RFC 9711 (EAT), RFC 9162 (CT 2.0) | 6 | Free standards | RFC 9943 first |
| [Raspberry Pi security architecture](https://www.raspberrypi.com/documentation/security/security-architecture.html) | 6 | Free vendor documentation | Signed boot, OTP keys, `rpi-fw-crypto` and the encrypted-disk flow |
| Factory-provisioned secure elements (Trust&GO ATECC608B, OPTIGA Trust M, SE050); [KiCad](https://www.kicad.org) | 6 | Parts; free CAD | One secure element on a breadboard before any PCB |
| [Kleppmann & Riccomini, *Designing Data-Intensive Applications*, 2nd ed.](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) | 7 | Book (March 2026) | Encoding and schema evolution; transactions |
| [MIT 6.5840, Distributed Systems](https://pdos.csail.mit.edu/6.824/) | 7 | Free lectures and labs | The Raft labs |
| Gregg, *Systems Performance*, 2nd ed. | 7 | Book | Methodology, then CPU and memory |
| Kay, *Fundamentals of Statistical Signal Processing*, Vols. I–II | Branch | Books | Vol. II, detection |
| [Dwork & Roth, *The Algorithmic Foundations of Differential Privacy*](https://www.cis.upenn.edu/~aaroth/privacybook.html) | Branch | Free book | Chapters 1–3 |

**Rules and standards to watch** (as of Oct 15, 2026):

| Item | Status | Why it matters | Source |
| --- | --- | --- | --- |
| EU Cyber Resilience Act | Reporting duties apply from Sep 11, 2026; full application Dec 11, 2027 | Secure updates, SBOM and vulnerability handling for anything sold in the EU | [Espressif](https://developer.espressif.com/blog/2026/09/esp32-cra-obligations-and-deadlines/) |
| EU Product Liability Directive 2024/2853 | Applies to products placed on the market after Dec 9, 2026 | Software and AI count as products; courts can order evidence disclosed and presume a defect when it isn't; missing security updates can be a defect | [A&L Goodbody](https://www.algoodbody.com/insights-publications/eu-revised-product-liability-directive-what-you-need-to-know) |
| EU Radio Equipment Directive, cybersecurity | Mandatory since Aug 1, 2025 (Articles 3.3(d), (e), (f)); harmonised standards EN 18031-1, -2 and -3 | Applies to any radio product sold in the EU, including the node; a notified body is needed where a standard's restrictions apply | [SGS](https://www.sgs.com/en-dk/news/2025/06/red-cybersecurity-requirements-mandatory-on-1-august-2025) |
| EU Machinery Regulation 2023/1230 | Applies from Jan 20, 2027; Art. 2(2)(p) excludes household appliances and IT equipment covered by the Low Voltage or Radio Equipment directives | Likely out of scope for a home hub and plugs; confirm with counsel before citing it | [Regulation text](https://ce-marking.help/pdf/Directives/Machinery%20Reg_2023_06_29.pdf) |
| US Cyber Trust Mark | UL stepped down Dec 19, 2025; the FCC chose the ioXt Alliance on Apr 13, 2026 | Voluntary US security label for consumer IoT | [Broadband Breakfast](https://broadbandbreakfast.com/fcc-picks-ioxt-alliance-to-head-cyber-trust-mark-program/) |
| Matter 1.6 | Released mid-2026: Joint Fabric, thermostat suggestions with standard explanations, security-sensor event history | Joint Fabric ships the co-equal controllers P-11 anticipates; the release summary mentions no signed command results, so F-1 has not fired | [CNX Software](https://www.cnx-software.com/2026/06/19/matter-1-6-specification-adds-nfc-based-commissioning-thermostat-suggestions-various-core-enhancements/) |
| Zigbee 4.0 and Suzi | Announced Nov 18, 2025; Suzi certification opened Sep 2, 2026 | Trust Center Swap Out and frame-counter sync for replacing a coordinator | [CSA](https://csa-iot.org/newsroom/the-connectivity-standards-alliance-announces-zigbee-4-0-and-suzi-empowering-the-next-generation-of-secure-interoperable-iot-devices/) |
| RFC 9943, SCITT architecture | Published June 2026, Standards Track | The base for an actuation-evidence profile | [RFC Editor](https://www.rfc-editor.org/rfc/rfc9943.html) |

## How to run the R&D

Run this guide through the machinery you already have — the problem register, charters, two-layer audits and the measurement record — and add the five things a hardware research program needs that the method lacks.

**Attach the learning to work units.** Your study hours come from NexSys hours, so read only what the next unit needs, in the two weeks before it starts, and budget about 2–4 hours of reading per unit:

| Work unit | Track | Read first |
| --- | --- | --- |
| TAIL-1 power cuts (after the run) | 1 | OSTEP on crash consistency; SQLite's atomic-commit page; Zheng et al. (FAST 2013) |
| ACK-1, APS acks | 2 | The Zigbee specification's APS chapter; UG100's send-path frames |
| TLA+ model of the ledger (December) | 4 | learntla.com; Part I of *Specifying Systems* |
| B-7 chain activation (after C-S0-2) | 6 | *Serious Cryptography* on hashing and signatures; Crosby & Wallach (2009) |
| SCHEMA-1 rules and RESTORE-1 | 7 | DDIA (2nd ed.) on encoding and evolution; Overeem et al. (2017) |
| Policy kernel (stage S1) | 4 | Schneider (2000); Ligatti et al. (2005); Cassandras & Lafortune on supervisory control |
| C-S0-10 and shadow mode (stage S2) | 5 | MIT 6.5940's quantization lectures; CaMeL |
| Graded verdicts (stage S3) | 3 | Blitzstein & Hwang; *All of Statistics* on testing; Ramdas et al. (2023), sections 1–3 |
| Signed node and the P-09 profile (stage S4) | 6 | *Learning the Art of Electronics*, early labs; *nRF Connect SDK Fundamentals*; RFC 9334 and RFC 9711 |

**Five additions to the method:**

1. **A lab notebook per experiment:** setup and wiring, firmware versions and serial numbers, ambient temperature, photos, the prediction filed before the run, and the result. Today these are scattered across bundles and returns.
2. **Uncertainty on every number:** each measurement-record row carries n, an interval and a GUM-style uncertainty, and sample sizes are planned before the run (the rule of three, in Track 3).
3. **Experiment tracking for models:** model, quantization, prompt, schema version, seed and dataset version on every P-10 run, so a model change re-runs the same suite.
4. **A mains safety rule:** no open mains wiring on the bench; switched loads only through enclosed, listed devices; prototypes on DC loads; a GFCI-protected bench strip. The harness's safety table protects devices, not people.
5. **A literature log:** one line per source with its DOI, what it claims, and which P-row it feeds, so the "two lines per source" practice becomes searchable.

**Cadence and gates.** Keep one study thread at a time, even when November and December run several work units at once; that matches the register's rule of one theorem at DESK. Each quarter, scan the F-1 tripwires (Matter, Zigbee 4.0, MCP, platform agent hooks) and the rules table above. A track closes on its "done when" sentence, and nothing leaves the building except through the claim register.

## Sources

**From ClaudeFolder (read Oct 15, 2026):** the strategy files in `nexsys-hivemind/context/strategy/` (north-star overview, Substrate Thesis v0, instruction-vs-evidence moat note, strategy of record, COMMERCIAL-1); THE HORIZON plan (v93) and the v111 decision record; the HORIZON-1, SCHEMA-1 and COMPARATOR-1 research returns; the research design package in `_archive/Claude outputs/2026-09-20_RESEARCH-PROJECT-DESIGN/` (the frame, problem register P-01 to P-11, program of record); Docs 01–18, the Locked Decisions and Architecture Invariants in `homesynapse-core-docs/`; `SqliteEventStore.java`, `DatabaseExecutor.java` and `EzspCoordinatorProtocol.java` in `homesynapse-core/`; `nexsys-bench/` and the Matter design program; the August Technical Roadmap in `_archive/root-plans/`.

**Web pages opened:**

- [Raspberry Pi: security architecture](https://www.raspberrypi.com/documentation/security/security-architecture.html)
- [PiShop: RTC battery for Raspberry Pi 5](https://www.pishop.us/product/rtc-battery-for-raspberry-pi-5/)
- [Espressif: CRA obligations and deadlines](https://developer.espressif.com/blog/2026/09/esp32-cra-obligations-and-deadlines/)
- [A&L Goodbody: the revised EU Product Liability Directive](https://www.algoodbody.com/insights-publications/eu-revised-product-liability-directive-what-you-need-to-know)
- [SGS: RED cybersecurity requirements mandatory on Aug 1, 2025](https://www.sgs.com/en-dk/news/2025/06/red-cybersecurity-requirements-mandatory-on-1-august-2025)
- [Regulation (EU) 2023/1230 on machinery, text](https://ce-marking.help/pdf/Directives/Machinery%20Reg_2023_06_29.pdf)
- [EU-OSHA: Regulation (EU) 2023/1230 on machinery](https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery)
- [Broadband Breakfast: FCC picks ioXt Alliance for the Cyber Trust Mark](https://broadbandbreakfast.com/fcc-picks-ioxt-alliance-to-head-cyber-trust-mark-program/)
- [CNX Software: Matter 1.6](https://www.cnx-software.com/2026/06/19/matter-1-6-specification-adds-nfc-based-commissioning-thermostat-suggestions-various-core-enhancements/)
- [CSA: Zigbee 4.0 and Suzi](https://csa-iot.org/newsroom/the-connectivity-standards-alliance-announces-zigbee-4-0-and-suzi-empowering-the-next-generation-of-secure-interoperable-iot-devices/)
- [RFC Editor: RFC 9943](https://www.rfc-editor.org/rfc/rfc9943.html)
- [Silicon Labs: On With Timed Off command](https://docs.silabs.com/zigbee/7.1/zigbee-af-api/zcl-on-off-cluster-on-with-timed-off-command)
- [Martin Kleppmann: DDIA, 2nd edition](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html)
- [Nordic Developer Academy](https://academy.nordicsemi.com)
- [MIT 6.5940, Fall 2026](https://hanlab.mit.edu/courses/2026-fall-65940)
