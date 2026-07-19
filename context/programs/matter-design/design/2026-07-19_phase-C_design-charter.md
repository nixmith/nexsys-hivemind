<!--
file: context/programs/matter-design/design/2026-07-19_phase-C_design-charter.md
purpose: The Phase-C authoring charter — the self-contained brief from which the Doc-19-class Matter integration design DRAFT is authored to the full DESIGN_DOC_TEMPLATE bar. Carries the ruled design law (B1–B5 + Nick's sharpenings), the per-section input inventory, the BLOCKING-question inventory, the adversarial-review lane plan, and the continuation line. Authorable by this program hub or a fresh program-hub session (ONE at a time).
audience: the program hub (the author); the independent adversarial review lane (reads the same charter); Nick (rulings already landed — this file executes them).
state-type: charter (Phase C of the Matter design program; write-isolated).
status: ACTIVE — authored 2026-07-19 at beat 3, on the B1–B5 rulings.
continuation line (if a fresh session authors): Follow all instructions in nexsys-hivemind/context/programs/matter-design/design/2026-07-19_phase-C_design-charter.md — /nexsys-project-manager  (first act: read 00_PROGRAM_STATUS.md in full, then this file, then the required reads §4; the prior program-hub session retires on this launch.)
-->

# Phase C Charter — Authoring the Doc-19-class Matter Integration Design DRAFT

**The work product:** `context/programs/matter-design/design/19-matter-integration_DRAFT.md` — a full-bar design document to `homesynapse-core-docs/governance/DESIGN_DOC_TEMPLATE.md` (skeleton §0–§16; every section substantive; every cited INV/LTD addressed by a specific decision; open questions marked BLOCKING/NON-BLOCKING; the template §4 quality checklist self-applied before the review lane sees it). Mode-1 Architect. **The DRAFT lives in this program tree; the PROPOSED handoff into homesynapse-core-docs + the Lock ceremony ride the MAIN hub + Nick — never this program directly.** Zero code.

## §1 Design LAW (ruled — the draft treats these as settled ground; the review lane may still refute with evidence, both directions)

1. **Stack = matterjs-server sidecar (B1(a))** with the four riders: **r1** dual-layer capture (WS semantic stream + debug message log) from day one, with a priced DataVersion path (upstream schema-gated WS event or decode-layer tap) — the capture doctrine ships WITH the stack; **r2** the IsolationLevel/descriptor amendment is PROPOSED in this draft (activation/extension of AMD-63's slot or new first-party external-process vocabulary), ratification at Lock via the MAIN hub, code never before it; **r3** WS loopback-only binding + supervisor-enforced port hygiene as LAW (the seam is unauthenticated, default-binds all interfaces); **r4** fabric-custody locus, our-VID posture, and the DCL-outbound walk are resolved IN this draft (§3 rows below).
2. **Scope (B2):** controller-only · Matter-over-WiFi/Ethernet wave 1 with the honest coverage statement ("a phase, not a resting place"; the trigger layer is 100% Thread and arrives phase 2 on a dedicated radio, **channel 25 pinned at dataset formation**) · device wave 1 = native plug/switch (OnOff), native bulb (Level/CT, Q-aware settled-value + clamp-aware CT expectations), mains presence (MS600 class) · bridges IN the design on the **O1+O3 provenance direction** (confirmation graded per measured behavior with provenance `NATIVE | BRIDGE_ATTESTED` recorded; ALIVE strictly provenance-gated — bridged `Reachable` NEVER feeds ALIVE), implementation sequenced after rows 1–3 · commissioning: IP/on-network + ECM second-fabric day one; BLE→WiFi in scope, sequenced behind; NFC/Joint-Fabric out.
3. **ALIVE LAW:** the predicate is positive-evidence-with-timestamp against per-class negotiated ceilings (A4 §2.5); the stack's `available` flag is a diagnostic, never an input; the #843 wedge scenario is the first authored Matter bench scenario family.
4. **Node 24.x LTS pinned at packaging time** (Nick 2026-07-19; the 22.13 floor hits security-EOL 2027-04-30 inside product life; 24.x → 2028-04-30).
5. Inherited house law: conservative-default LAW (absent key opens/adopts NOTHING — the M9.4-PJ/ADP rulings transfer verbatim) · PIE-bare discipline · the AMD-97 vocabulary unchanged (Invoke-SUCCESS is never confirmation evidence; only Leg-3 report evidence earns CONFIRMED) · every characterization value is bench-gated (fixture-paired asserts; no spec seed is asserted pre-measurement) · token-parameterization per R-1 (no new brand-coupled names) · J1/gate fences absolute.

## §2 Template-section map (inputs per section; returns cited by § at authoring)

| Template § | The Matter-specific content | Primary inputs |
|---|---|---|
| 0 Purpose | Second protocol; the moat generalization thesis; controller-only V1-Matter | A4 §0/§6; roadmap §3 |
| 1 Design Principles | Evidence-graded verdicts; provenance honesty; sidecar-as-implementation-detail (INV-RF-01 line 270); honest-downgrade posture | A4 §1–§3; A3 §2 |
| 2 Scope & Boundaries | The B2 cut verbatim + owns/does-not-own vs integration-runtime/device-model/event-model (Doc 08 §2 as the model) | B2; A3 §1/§6 |
| 3 Architecture | Adapter (NETWORK, virtual thread) ↔ WS client ↔ sidecar topology; **the topology ruling (child-of-core vs systemd sibling — A3 B3) is MADE here with rationale**, resolving the initialize()-spawn tension (A3 B2) per the chosen shape; supervision machinery (liveness split: seam-alive-process-dead + process-alive-seam-dead; W5 law — health from protocol behavior, never socket state); restart choreography vs the ledger | A3 §1–§3, §8(a) machinery list; A1 §6 |
| 4 Data Model | Interview→adoption grammar (AMD-99 unchanged); the near-empty Matter profile source keyed by Matter identity (VID/PID-class); bridged-endpoint modeling with provenance; the mint census (core-roster delta 0–2; `matter.*` dotted namespace; Q-A4-3 DataVersion/intervals metadata resolved here) | A3 §5–§6; A4 §1.1/§3 |
| 5 Contracts & Invariants | The INV walk: INV-RF-01/02/03, INV-LF-02 (the DCL-outbound walk), INV-CE-04/05, INV-SE-02/03/04, EXT-INV-1/2 (the descriptor-gap + first-party-sidecar readings stated), AIOT-INV-1 untouched; AMD-97-INV-01 composition | A3 §1/§2/§6/§9; A1 §8.5/§10-1 |
| 6 Failure Modes & Recovery | Sidecar death mid-command/mid-commissioning (failsafe rollback); WS drop vs server-shutdown; subscription silent-death (#843) → honest staleness; bridge-node loss fanout; DCL unreachable at commissioning; storage corruption/custody loss (⇒ fleet re-commission, stated plainly) | A1 §6.6; A4 §2; A2 §6 |
| 7 Interaction w/ Other Subsystems | Event bus/state store/automation untouched paths; the confirm-before-ack ordering ruling (**Q-A4-1** — if Doc-01 §3.8 prose must change ⇒ STOP, escalate via MAIN hub BEFORE Lock); frontend read-API provenance field = a CONTRACT conversation, never a workaround | A4 §1.4/§7; Doc 01 §3.8 |
| 8 Key Interfaces | The adapter's factory/descriptor (14-arg; NETWORK; the r2 amendment PROPOSAL text); the WS-client seam (schema floor + skew policy from A1 §3.3/§6.4); no core interface changes | A3 §1/§4; A1 §3.3 |
| 9 Configuration | `integrations.matter.*` schema (factory-registered; conservative defaults; commissioning accept-list; discovery off; static-first); sidecar launch config; SecretStore refs | A3 §7; A2 §6 |
| 10 Performance Targets | **THE PI MEMORY BUDGET — BLOCKING (Nick 2026-07-19):** a priced total-device budget (JVM `-Xmx1536m`/`MemoryMax=2G` cgroup + Node old-space [`--max-old-space-size` tuned; no published absolutes — the spike's RSS measurements are the evidence] + OS headroom on Pi-class); latency targets stay investigation-triggers per MVP §8 | A1 §3.5; A3 §2.2; the spike |
| 11 Observability | Journald identity for the second stream; the dual-layer capture (r1) as the observability spine; instrument self-identification (version banners); sidecar liveness INFO (anti-vacuous) | A4 §5; A3 §3.1 |
| 12 Security Considerations | WS loopback LAW (r3); fabric-CA custody in SecretStore (INV-SE-03; never chip-tool's `/tmp`/test-IPK class); test-VID→production-VID posture (B4 r2 path); DCL trust-store integrity/staleness split; the published-analyses threat frame | A2 §6; A1 §10-2/3; A5 §4.3 |
| 13 Testing Strategy | The Matter bench doctrine: dual-layer capture, stack+version-conditioned fixture provenance, ciphertext pcap ring, second-implementation virtual-DUT cross-check, `import_test_node` for registry tests, the #843 wedge family first, session-establishment segmented from confirm envelopes; FakeMatterServer-class WS peer for unit tier | A4 §5; A3 machinery (a).7 |
| 14 Future Considerations | Thread phase 2 (dedicated radio, ch25, OTBR posture per A2 §2); BLE full scope; locks wave (the showcase class); Joint Fabric/NFC watch; ESPHome-era interplay | A2 §2/§7; A4 §4 row 4 |
| 15 Open Questions | Whatever survives, each BLOCKING/NON-BLOCKING (candidates: Q-A4-5..9; Node-lifecycle detail; schema-pin cadence; NB2 NETWORK-first-customer hardening notes) | all returns' §-open-questions |
| 16 Summary of Key Decisions | The B1–B5 rulings + the in-draft rulings (topology, custody, ordering, provenance option), each with rationale + alternatives-considered | this charter |

## §3 The BLOCKING inventory (the draft resolves each IN-DOCUMENT, or marks it BLOCKING with its owner)

1. Topology: child-of-core vs systemd sibling (A3 B3) — **ruled in §3 of the draft.**
2. initialize()-spawn vs INV-RF-03 purpose (A3 B2) — resolved by the topology ruling.
3. The IsolationLevel/descriptor amendment PROPOSAL text (A3 B1 / B1-r2) — drafted; ratifies at Lock (MAIN hub).
4. Fabric custody locus + our VID + backup unit (A3 B4; A2 §7-4; A1 §10-2) — ruled in §12 of the draft.
5. The DCL outbound-fetch posture vs INV-LF (A1 §10-1) — ruled in §5/§12 (seed-only default vs live-fetch-with-consent are the candidate shapes).
6. WS seam security (A1 §10-3) — LAW per r3; the draft specifies the enforcement.
7. Confirm-before-ack ordering (Q-A4-1) — ruled in §7; Doc-01-prose escalation path armed.
8. Bridged provenance O1/O2/O3 (Q-A4-2) — ruled on the O1+O3 direction in §4/§5.
9. DataVersion/negotiated-intervals metadata (Q-A4-3) — ruled in §4 under the mint census.
10. Corpus-fidelity mechanism (Q-A4-4 / r1) — ruled in §13.
11. **The Pi memory budget (Nick 2026-07-19)** — priced in §10; the spike's RSS numbers are its evidence obligation.
12. BLE commissioning sequencing detail (B2 item 5; A2 §7-2) — stated in §2/§14 with the bootstrap path.

## §4 Required reads at authoring (priority order; MODULE_CONTEXTs fast, source truth)

00_PROGRAM_STATUS.md (the ledger IS the ruling record) → the B1–B5 memo → all five returns (A3 and A4 deepest) → DESIGN_DOC_TEMPLATE.md in full (§1 rules + §4 checklist + §6 review process) → Doc 05 + Doc 08 (the structural models) → Doc 18 §3.3/§3.5/§7 + Doc 17 §2–§4 → integration-api/-runtime/-zigbee MODULE_CONTEXTs + module-infos at HEAD → Doc 01 §3.2/§3.8/§4.3–4.4 → Doc 12 §3.3/§3.8/§3.9 + `distribution/` (unit, install.sh, boot-contract-map) → `Architecture_Invariants_v1.md` for every INV cited → the doctrine brief. Re-derive all volatile state at the spine; every count in this charter is a claim.

## §5 The independent adversarial review lane (after the draft)

Fresh write-isolated session; read-only; the Doc 16/17/18 precedent: evidence-required findings (concrete trigger or it's a NOTE), settled-ground fenced WITH refutation-welcome both directions (a ruled item may be challenged only with evidence that would change the ruling's factual basis), one return file (`design/2026-07-XX_doc19-draft_adversarial-review_return.md`), two-layer audited like any lane. The hub folds, then hands the PROPOSED doc to the MAIN hub for the docs-repo flow + Lock ceremony with Nick.

## §6 The spike (B5-ratified; held)

Post-gate-read (after Sun 2026-08-16) + post-B1 (satisfied). ≤2 WU-equivalents. DUTs per B3 (P110M first); network per B3 Option C; Gen4s nowhere. Deliverables: commissioning happy-path logs · first subscription-liveness/invoke-status timings · custody files observed on disk · **measured sidecar RSS on Pi-class (the §10 budget's evidence — Nick's sharpening)**. Its appendix is citable by the draft (sections that depend on it say so and remain honest without it — spec-seeded, bench-gated).
