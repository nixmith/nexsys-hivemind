<!--
file: context/programs/matter-design/memos/2026-07-19_B1-B5_deliberation-memos.md
purpose: Phase-B deliberation memos B1–B5 — the consolidated one-turn-rulable decision surface for the Matter design program (the AMD-99 R-A..R-E ruling-box pattern). Consolidates the five ACCEPTED Phase-A returns; every load-bearing input is pointered to its return §. Nick rules each box in one turn; rulings are recorded verbatim in 00_PROGRAM_STATUS.md's ledger and pointered onto the spine by the MAIN hub.
audience: Nick (the rulings); the program hub (records rulings, then opens Phase C); the MAIN hub (§-pointer consumption only).
state-type: decision memo (program-tree; write-isolated).
status: AWAITING RULINGS — authored 2026-07-19 by the program hub (beat 2) after two-layer audit ACCEPT ×5.
-->

# Phase B — Deliberation Memos B1–B5 (rule each box in one turn)

## §0 The audit record this memo stands on

**All five Phase-A returns: ACCEPT** (A4 accept-with-notes). Layer 1 = the lanes' own evidence tags (~230 primary-source fetches, all dated 2026-07-19). Layer 2 = hub adjudication, executed this session:

- **Repo claims re-verified at source over the bridge (6/6 CONFIRM):** `IsolationLevel` javadoc verbatim ("rejects this value with UnsupportedOperationException… AMD-63-INV-01") · the supervisor's RESERVED_SUBPROCESS startup rejection at source · the SERIAL→platform / else→virtual thread fork · the Zigbee descriptor's `IoType.SERIAL` + the "a lie the supervisor cannot honor" comment · **Doc 12 §3.8 Step 6.1 doc-drift CONFIRMED verbatim** ("uses ServiceLoader (LTD-17)" vs the as-built explicit factory list + ArchUnit `noServiceLoader`) · `registerIntegrationSchema` production-wired (`HomeSynapseCore.java:1343/1350` — Doc 18 §4 row 6's "built, unwired" is stale).
- **Web claims spot re-fetched (5/5 CONFIRM):** the CSA fee table exact (incl. Associate $0 + transfer pricing) · matterjs-server `--vendorid` default `0xFFF1 (65521)` + the unauthenticated-WS all-interfaces warning verbatim + port 5580 · matter.js 0.17.5 (2026-07-13): Thread network-name derivation + "Upgraded to Matter specification version 1.6.0" · the TP-Link rep's energy-cluster statement (P110M/P210M/P316M yes; KP125M/P125M no) · python-matter-server "archived by the owner on Jun 23, 2026… read-only."
- **Adjudication notes (none blocking):** (1) A1 cites `@matter/main` 0.17.6 from the npm registry while the repo CHANGELOG shows 0.17.5 + WIP — registry governs publish existence; benign. (2) A4's spec quotes ride [VERIFIED-mirror] PDFs, honestly tagged; its own §8-7 names four claims for further re-check — folded into Phase C as the Q-A4-6 verbatim pass (a licensed 1.6 copy). (3) The banked-base corrections (openHAB record = t/127907; the "2–4 versions behind" phrasing; SPAKE2+ absence) are accepted as corrections-with-evidence.
- **Doc-drift findings for the MAIN hub (this program never writes docs):** Doc 12 §3.8 ServiceLoader text · Doc 18 §4 row 6 "built, unwired." Pointered via the status file; they ride the MAIN hub's docs flow whenever convenient — nothing here depends on them.

**The standing fences, restated once:** J1 FROZEN (criteria §2 item 2 fences all of this out of the mid-Aug gate) · Gen4 Shellys stimulus-only, radios never provisioned · zero code, zero core writes from this program · Matter code sequencing = the MAIN hub's post-M14-sweep-at-earliest call, and never before the Doc-19 Lock.

---

## B1 — THE STACK CHOICE

**Question:** which stack shape does the Doc-19 design target for the Matter controller?

| Option | The decisive evidence (returns §) |
|---|---|
| **(a) matterjs-server sidecar** (Node 22.13+/24.x, WS API) | Production at HA scale (`stage: stable` 9.1.0, one-way migration; 16 stable releases in 5 weeks); openHAB independently converged on matter.js after abandoning the CHIP-Java route ("a maintenance nightmare over time"); fastest spec tracking observed (1.6.0 in <4 weeks); licenses clean end-to-end (199-package tree, zero copyleft); full WS API enumerated [A1 §3, §6, §7, §9(a)]. Fit: SPI-frontable as the first `IoType.NETWORK` adapter; INV-RF-01 blast-radius CLEAN (line 270 pre-authorizes out-of-process); the gaps are enumerable machinery — child-process supervision, packaging (first non-JVM production process), the IsolationLevel vocabulary hole, fabric-custody locus, the unauthenticated WS seam [A3 §1–§3, §8(a)]. Corpus caveat: the WS stream drops DataVersion; dual-layer capture required [A4 §5.2] |
| **(b) CHIP-JNI in-process** | **VIOLATES INV-RF-01 as written** — a SIGSEGV in ~1.1M lines of C++ is whole-JVM death; the supervisor's isolation is exception-catching and cannot contain it; the enum's own javadoc names "misbehaving native/JNI adapters" as what RESERVED_SUBPROCESS was reserved for [A3 §2.2, §8(b); A1 §2.3]. Zero known headless-JVM adopters; full-tree GN builds per release per arch, no Maven artifacts ("20G+", "builds are SLOW") [A1 §1] |
| **(c) CHIP-FFM in-process** | Everything in (b) + a from-scratch C shim (jextract binds C, not C++; CHIP has no C-ABI controller surface) + FFM is preview-on-Java-21 (per-release-incompatible under `--enable-preview`; stable FFM implies a core JDK move) [A1 §2; A3 §8(c)] |
| **(d) pure Java** | Architecturally cleanest (CLEAN down the whole fit-matrix column) — and honestly priced at **~5–10× the Zigbee arc (~70–140 WUs)** before device breadth, with **no maintained Java SPAKE2+ in existence** and sole-maintainer duty against a spec revving 2×/yr with a 483-script conformance surface [A1 §5, §9(d); A3 §8(d)] |

**PM REC: (a) — matterjs-server sidecar — with four riders that become Phase-C design law:**
- **r1 (corpus fidelity, the A4 condition):** dual-layer capture (WS semantic stream + `MATTER_LOG_LEVEL=debug` message log) is mandatory from the first bench day; the design prices a DataVersion path (upstream a schema-gated WS event, or a decode-layer tap) — the capture doctrine ships WITH the stack, not after it [A4 §5.2, Q-A4-4].
- **r2 (the amendment-class work, named now):** a first-party sidecar has no truthful `IsolationLevel` value today (RESERVED_SUBPROCESS is startup-rejected at source AND ruled as the marketplace rung; IN_JVM mis-states the topology). The Doc-19 draft PROPOSES the descriptor/enum resolution; ratification rides the Lock ceremony with the MAIN hub (AMD-63-INV-01's recorded process). Code never starts before it [A3 §1.4, §9-B1].
- **r3 (the WS seam):** loopback-only binding + supervisor-enforced port hygiene is a design LAW day one — the seam ships unauthenticated and default-binds all interfaces [A1 §6.3, §10-3].
- **r4 (custody):** the fabric-identity locus (sidecar-owned storage vs SecretStore-owned; our VID, never HA's 0x134B; the DCL outbound-fetch-vs-INV-LF walk) = named BLOCKING design rows for Phase C [A1 §10-1/2; A2 §6; A3 §9-B4].
- **(b)/(c) rejected** on the INV-RF-01 violation (accepting whole-hub restart as "isolation" would defeat battlefield 4 — the crash-isolation demo IS the moat claim); **(d) rejected on price, honorably** — it remains the only total-custody route and re-opens on its own merits if the ecosystem's economics ever change; nothing in (a) forecloses it (the SPI seam and the seeded-log substrate are stack-agnostic).

**Default if unruled:** (a) with all four riders.

**RULING (B1):** ______________________________

---

## B2 — THE V1-MATTER SCOPE CUT

**Question:** what does the first shipped Matter integration cover?

**PM REC (each line independently vetoable):**
1. **Controller-only.** No device/bridge-role component (we never present ${PRODUCT} devices INTO other ecosystems at V1-Matter) [A5 §4.3(iv)].
2. **Matter-over-WiFi/Ethernet at wave 1; Thread = phase 2 on a dedicated radio.** The honest coverage statement ships with it: WiFi covers the actuator/appliance market (~73% of native SKUs) + everything behind bridges; the trigger layer (battery sensing) is 100% Thread and arrives with phase 2 — "a phase, not a resting place" [A2 §1]. The future Thread network pins **channel 25** at dataset formation (25 MHz from the ch20 fleet) [A2 §2.4].
3. **Device-type wave 1 = A4 rows 1–3:** native plug/switch (OnOff), native bulb (Level/CT with Q-aware settled-value expectations + the clamp-aware CT variant), and the mains mmWave presence class (MS600 — the subscription-liveness/ALIVE story). Locks = the showcase class whenever their wave arrives [A4 §4].
4. **Bridges are IN the design scope (the C2 differentiator lives there), implementation sequenced after rows 1–3 land.** Evidence direction for the provenance ruling: **O1+O3 compose** — confirmation graded per measured behavior with provenance recorded (`NATIVE | BRIDGE_ATTESTED`); ALIVE strictly provenance-gated (bridged `Reachable` is testimony with no freshness bound — it NEVER feeds ALIVE) [A4 §3]. The formal O1/O2/O3 ruling is Phase C's (Q-A4-2), on this stated direction.
5. **Commissioning scope:** IP/on-network + ECM second-fabric join = day one (both works-headless-today); **BLE→WiFi in scope but sequenced behind them** (live crash classes #164/#806), with the phone-ecosystem-first + ECM-second bootstrap as the sanctioned bench de-risk path [A2 §3.6, §7-2; A1 §10-4]. NFC and Joint Fabric: out (spec-only / zero implementations) [A2 §3.4–3.5].
6. **ALIVE is design LAW:** the predicate is positive-evidence-with-timestamp against per-class negotiated ceilings (the §2.5 table) — never the stack's `available` flag; the #843 wedge scenario is the FIRST authored Matter bench scenario family [A4 §2].
7. **Named Phase-C BLOCKING questions (accepted into the design charter):** confirm-before-ack ordering (Q-A4-1 — touches Doc-01-class contract prose ⇒ escalates via the MAIN hub if any core doc text must change) · the bridged-provenance ruling (Q-A4-2) · DataVersion/negotiated-intervals in `state_reported` metadata (Q-A4-3, governed by the A3 §5 mint census: core-roster delta 0–2) · the corpus-fidelity mechanism under B1-r1 (Q-A4-4) · fabric custody + DCL posture (B1-r4).

**Default if unruled:** as REC.

**RULING (B2):** ______________________________

---

## B3 — DUT PURCHASES + BUDGET + BENCH ISOLATION

**Question:** what hardware does Nick buy, when, and onto what network?

**The purchase table (lifted from A2 §4; all prices dated 2026-07-19; re-verify at order):**

| Bundle | Contents | Total |
|---|---|---|
| **Phase-1 core (REC: APPROVE)** | Tapo P110M 2-pack $24.99 · Tapo L535E ×2 $29.98 · Meross MS600 $32.99 · Aqara Hub M3 $159.99 · Aqara D/W child $17.99 | **$265.94** |
| Optional add (checkbox) | Meross MSS315 4-pack (second energy vendor) | +$52.99 |
| **RCP radio (REC: front-load with phase 1)** | HA Connect ZBT-2 | +$48.95 |
| Phase-2 Thread endpoints (REC: DEFER, just-in-time at Thread phase) | Eve Energy $34.45 · Eve D&W $31.80 · IKEA MYGGSPRAY $7.99 · MYGGBETT $7.99 | $82.23 (deferred) |

**PM REC:**
- **Approve phase-1 core ($265.94; $314.89 with the ZBT-2; $367.88 with the MSS315 add).** Order timing: at the B5 spike charter (post-gate-read, ~Aug 17) per endpoints-just-in-time — or earlier at your discretion; lead times are days either way.
- **Sub-ruling (i) — REC AFFIRM: ALL Shelly SKUs excluded from the DUT set** (incl. the Flood Gen4, the only native-WiFi Matter sensor) — "Shelly = stimulus, never provisioned" stays a one-rule invariant [A2 §4.0].
- **Sub-ruling (ii) — REC: the ZBT-2 front-loads with the phase-1 order** (the standing radios-front-load principle; official firmware, unlocked bootloader; $48.95), Thread endpoints stay deferred [A2 §2.2, §4.3].
- **The bench-isolation ruling (A5 routed it here) — REC: Option C** — dedicated bench AP + dual-homed controller (~$35–110): the community-validated isolated shape; link-local IPv6 suffices, zero reflectors, zero conntrack in the Matter path; channel plan house-ch1 / bench-ch6-or-11 / Zigbee ch20 in the gap / Thread ch25 later; USB-2 + extension-cable + ~1 m antenna-separation discipline per the Intel/AN1017 record. Options A ($0, no isolation) and B (~$90–260, documented-flaky cross-VLAN mDNS) stay on the table [A2 §5, §2.4].
- **Rider:** pre-order CSA-DB per-SKU verification spot-check (the DB's transport facet is broken to fetches; a browser session closes it) + re-verify the two single-citation prices (MSS315, M3) [A2 §8-2/3/4].

**Default if unruled:** nothing is purchased (the deferral is the default state); the spike then runs later or not at all — the honest cost of silence [A5 §8.1].

**RULING (B3):** ______________________________

---

## B4 — THE CERTIFICATION POSTURE

**Question:** CSA membership/certification — when and what.

| | (a) Uncertified + honest wording | (b) Adopter + certify at Matter-arc ship | (c) Certify at named trigger |
|---|---|---|---|
| Cash | $0 | ~$11k–$21k yr-1 (Adopter $7,500/yr + cert $3,000 + lab [quote-only; hardware-scoped ceiling $7–10k] + application $2–3k) | $0 until trigger, then (b) at then-current fees |
| Calendar | 0 | weeks-not-quarters (join immediate · VID days–weeks · quote+test ~1–2 mo) | (b)'s calendar from trigger |
| Brand | The honesty rule kept literally; HA's 3-year uncertified precedent normalizes it | Logo + listings + production VID + the member forward-looking claim template | Mark lands when it converts (Hub on-box) |
| Reversibility | TOTAL | membership annual; cert lifetime-of-product | is the deferral |

**PM REC (adopting A5 §8.2): (a) now → (c) with T1 = the Layer-4 Hub hardware as the presumptive trigger**, plus two riders:
- **r1:** authorize the **$0 lab-quote engagement** (Resillion + one comparator) during Phase B/C so the next posture decision prices from a real software-component number, not a hardware ceiling [A5 §4.2].
- **r2:** hold the **early-Adopter-join ($7,500, one-week fuse)** in reserve — it buys the production VID (retiring the 0xFFF1 test-VID default) + the sanctioned forward-looking claim template, any time, without certifying [A5 §6(b)].
- **C-1..C-4** (nominative wording envelope · forward-looking claims for non-members · naming/R-1 interplay · test-VID posture) go to the counsel program's queue as written — questions, not conclusions [A5 §5.3].
- Launch-messaging envelope under (a): **F1 ∪ F2** (design-evidence framing unconditionally; measured-evidence framing if the B5 spike runs); F3 only ever under r2 [A5 §7].

**Default if unruled:** (a) is the de-facto state; nothing foreclosed.

**RULING (B4):** ______________________________

---

## B5 — INTEGRATION-#2 SEQUENCING + THE SPIKE RE-CHARTER

**Question:** what fills the code slots around the Matter design program?

| Option | One line |
|---|---|
| **O1 (standing order)** | M14 Shelly holds its ruled conditional slot (pre-gate if the Jul-31 trigger clears; post-gate arc #0 if it slides) · Matter code post-Lock · ESPHome stays skipped · Z-Wave stays professional-era |
| O2 | Waive M14; Matter becomes the first NETWORK adapter — forfeits first watts, the two-adapter kill demo, and the substrate rehearsal for ZERO Matter acceleration (the Lock binds, not the queue) [A5 §1.2] |
| O3 | O1 + ESPHome reopened Sep–Oct — the idle-runway premise is gone [A5 §1.3] |

**PM REC: O1 — reaffirm the standing order; no re-ruling needed.** The evidence strengthened it: M14 is now additionally the cheap rehearsal for the exact substrate the Matter arc needs (first `IoType.NETWORK` customer · LAN bench discipline · TelemetryWriter wiring · the criteria §2-item-5 two-adapter demo), and the zero-procurement premise is honestly retired (the third-plug rider governs) [A5 §1.1].

**The one NEW ruling this box owns — the spike re-charter (REC: RATIFY):** the program's ONE hardware exercise, re-chartered as the Phase-C bench input: **post-B1-ruling AND post-gate-read (after Sun 2026-08-16)** · ≤2 WU-equivalents of bench sessions · DUTs = B3's phase-1 rows (P110M first) · network = B3's isolation ruling · the Gen4 plugs appear nowhere in it · deliverable = a measured-evidence appendix (commissioning happy-path, first subscription-liveness/invoke-status timings, custody files observed on disk) that the Doc-19 draft cites instead of citing forums — and that unlocks the F2 launch claim [A5 §3, §7.1-F2].

**Also riding this box, no action now:** the Tier-2 proof-scenario wording amendment ("Zigbee, Z-Wave, energy monitoring" → "multi-protocol + energy") — strategy-layer, yours alone, whenever [A5 §7.3].

**Default if unruled:** O1 stands by construction; the spike doesn't run; Phase C designs from citations alone.

**RULING (B5):** ______________________________

---

## §After-the-rulings: what Phase C opens with

On the B1/B2 rulings the hub authors the **Doc-19-class design draft** to the full 13-section DESIGN_DOC_TEMPLATE bar, carrying: the ruled stack + riders as design law · the B2 scope cut · the BLOCKING inventory (Q-A4-1..4 · A3 §9-B1..B4 · A1 §10-1..3 · A2 §7-3/4) each resolved-or-marked-BLOCKING in the draft · the AMD-63/IsolationLevel amendment PROPOSAL (ratification at Lock, MAIN-hub flow) · the A4 §4 characterization table as the confirmation-design seed (every value bench-gated) · the §2.5 ALIVE ceilings · the capture doctrine (§5) as the test-strategy section's spine. Then the **independent adversarial review lane** (Doc 16/17/18 precedent), fold, and the PROPOSED handoff to the MAIN hub for the Lock ceremony. Phase D (implementation plan + Matter bench charter) follows the Lock path. The spike (if ratified) runs inside Phase C's window, after the gate read.
