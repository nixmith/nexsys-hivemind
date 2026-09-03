<!--
file: context/strategy/claim-register.md
purpose: THE CLAIM REGISTER — the ONLY source any public surface may draw from (H9; strategy v1.1 §1 asset 2). Every row: dated, commit-hashed, evidence-pointed, scope-fenced, minted WITH its own falsifier (the refutable-by column, v58 beat 2 ruling) and its theory ancestry (the claims-to-canon crosswalk, v58 beat 4).
audience: Nick (the mint word) · the hub (the sole writer) · every future public surface (B-5, the website, any external sentence)
state-type: REGISTER (append/supersede only; a claim is never edited — it is SUPERSEDED by a new row)
status: **ONE ROW LIVE — C-001 (NARROW), minted v61 beat 1 (2026-09-02) at `7c57d7f` by Nick's delegation (the record: `context/strategy/2026-09-02_v61-b1_three-words_delegated-ruling.md`). C-002 stays SLOT, fenced to R-4b. THE REGISTER IS A SOURCE, NOT A SURFACE: nothing here is PUBLIC until a surface exists under G-2 (a written-opinion-backed R-1) and `README.md:117` lifts at W2-3.** Prior: SCAFFOLD — NO CLAIM IS LIVE (authored ahead v58 beat 9, 2026-08-30; the mint was to happen only on a four-of-four record + Nick's word — amended v61 b1, see the mint protocol).
-->

# The claim register (C-001 LIVE — narrow · C-002 pre-mint)

## §0 The field-language preamble (binds every register sentence; dated)

1. **Explainability (RS-3 §6.1-1, 2026-08-28):** *"Home Assistant 2026.9 answers 'why did it fire' from its logbook (a cause path from trigger to entity change); it still records no reason for a legitimate non-fire, no confirmation verdict, and no command that produced no state change — and the chain rides a self-purging store. The durable differentiators are the confirmation leg (lead), the never-evicted projection, and the general why-not."* Any surface implying the field lacks a "why did it" answer is refutable from 09-02.
2. **Enforcement (RS-3 §6.1-2, 2026-08-28):** *"The field ships L2/L3 stories plus four fragment classes — category exclusions written as 'convenience only' disclaimers, entity/API allowlists, an agent-runtime deny gate outside the home, and an OS-runtime confirmation gate for app intents outside the home — plus a device-envelope limit standard in laboratories. The deterministic policy kernel — invariants, rate limits, reversibility classes, attributed durable record — is missing from every shipping home product."* Never "no platform confirms risky actions"; never "superior." (The IFA 09-04..08 watch: a FIFTH fragment class re-prices on sight; the rows are date-armored.)
3. **Sensing (RS-3 §6.1-3 as AMENDED by RS-4, 2026-08-29):** *"802.11bf appears in 2026 infrastructure-silicon briefs; no consumer product cites it; no certification program exists; no consent framework exists for Wi-Fi sensing in homes — the sensing-consent vocabulary exists next door in cellular 6G ISAC (ETSI GR ISC 004; 3GPP TS 22.137) and has not crossed."* The bare universal is BANNED. **The four-qualifier law (RS-4 harvest 1, ADOPTED):** every sensing capability sentence carries hardware · environment count · obstruction definition · training regime, or it does not leave this register.
4. **The D5 layered form** on every enforcement sentence: the floor is MISSING from the field, never "ours is superior"; L2/L3 without L1 unsound; L1 without L2 insufficient.

## §1 The register

| id | claim (D5 form) | date | commit | evidence | scope fence (what it does NOT claim) | refutable-by | status |
|---|---|---|---|---|---|---|---|
| C-001 | **Verified on real hardware at commit `7c57d7f` (artifact `0.1.0+git20260830.201400.g7c57d7f`; GitHub artifact digest `452a2f95a89c…` re-derived 3-hop byte-identical): the CI-built arm64 `.deb` installs on the held Raspberry Pi as an ordinary apt upgrade (no downgrade flag; zero event-row loss; integrity ok), boots under its own shipped unit with the R-3a drop-in removed, RUNS the Zigbee integration — network resumed on 5/5 service starts, zero networks formed, both rig entities AVAILABLE with state reported inside the 45-min window — and PUBLISHES events to the durable store (70→80 rows in the window; throw-discriminator 0).** | 2026-09-02 | `7c57d7f` | `context/audits/2026-08-30_R4_re-rep_operator-record.md` + `context/audits/2026-08-30_R4_intake_two-layer-audit_v59-beat-3.md` (ACCEPT-WITH-NOTES; C1–C3 MET); six checks re-executed at the record bytes at mint (v61 b1) | ONE card · ONE rig of TWO sensor entities · ONE integration (Zigbee) · ONE 45-min window. NOT the six-device bench fleet (custody cloned the NETWORK, not the REGISTRY — F-R4-2) · NOT adoption of a silent rejoiner (F-R4-1) · NOT an automation firing on the shipped artifact (C4 unreached) · NOT fleet-scale, multi-home, availability, uptime, or comparative · no enforcement sentence rides this row (D5) | a reproduction on `7c57d7f` + the pinned artifact failing C1, C2, or C3 as the R-4 packet defines them; or the record's ⏺s shown inconsistent with the audit | **LIVE — MINT-NARROW** (v61 b1, 2026-09-02, by Nick's delegation; refutable by Nick's REVERT → RETIRED, never deleted) |
| C-002 | ⟨the fleet/adoption/automation sentence: the six-device fleet RE-ADOPTED on cloned custody + the bench-hero automation firing on the shipped artifact⟩ | ⟨R-4b mint date⟩ | ⟨R-4b sha⟩ | the R-4b record + its audit | C-001's shape + the fleet count | same shape | SLOT — FENCED pending R-4b (four-of-four; criteria checked REACHABLE at packet authoring; F-R4-1 fixed first — v61 b1) |

**Mint protocol:** the R-4 record arrives → the hub's two-layer audit → anomaly-free four-of-four → the D-1 sentences copied VERBATIM from the claim-fence register into the slots → Nick's word confirms → status flips LIVE → the D-1 DO-NOT-SAY fence retires for exactly these two sentences and no others. `distribution/README.md:117` does NOT lift (W2-3 owns it). **Amended v61 b1 (2026-09-02, by delegation):** on a THREE-of-four audited record a NARROW row may mint — scoped to exactly the criteria MET, its fence naming each criterion not met — on Nick's word or his recorded delegation; the WIDE row waits on four-of-four. The D-1 DO-NOT-SAY fence retires ONLY within C-001's scope fence (the two-entity rig, one integration, one card); every fleet/adoption/automation sentence stays fenced.

## §2 The claims-to-canon crosswalk (one line per claim; the corpus assessment §4.2)

| claim | theory ancestors |
|---|---|
| C-001/C-002 (the packaged-artifact hardware chain) | Schneider 2000 (what a runtime monitor can enforce = the deterministic floor's charter) → the Simplex lineage (verified supervisor over unverified controller = harness-enforces/model-proposes) → Lamport 1978 + the event-sourced durable record (the evidence chain's ordering) → end-to-end verification at the artifact boundary (Saltzer/Reed/Clark — the hash chain's justification) |
| ⟨future claims add their line at mint — the rule: no row without ancestry⟩ | |

## §3 Supersession law

A claim is never edited. A stronger/corrected claim enters as a NEW row; the old row's status flips SUPERSEDED-BY-⟨id⟩ (or RETIRED with the reason). The register only grows; its history IS the honesty record.
