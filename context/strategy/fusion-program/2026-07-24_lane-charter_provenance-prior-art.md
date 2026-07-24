<!--
file: context/strategy/fusion-program/2026-07-24_lane-charter_provenance-prior-art.md
purpose: Dispatch-ready charter for the provenance prior-art study lane (FQ-2) — profile the existing verifiable-log/attestation standards, produce the v0 spec skeleton (INTERNAL until the ruled trigger), scope the standalone verifier tool, and package the counsel questions. The "own an interface" play, executed to the profile-don't-invent discipline.
audience: a fresh write-isolated Cowork research session (primary); Nick; the PM hub (audit).
state-type: lane charter (dispatch-ready).
status: CHARTERED 2026-07-24 on the FQ-2 ruling. Trigger: launches POST-GATE (after 2026-08-16) on Nick's word — desk work, but the runway before the read belongs to the gate.
write-isolation: the lane writes ONLY context/strategy/fusion-program/provenance/* (new subtree) + nothing else. No spine writes; no design-doc writes (a future Doc-19/20-class provenance design doc rides the MAIN hub's Lock pipeline if/when v0 graduates); the hub audits; Nick commits explicit-paths.
publication-law (binding, from the FQ-2 ruling): NOTHING in this lane publishes. Public v0 requires (i) the publish gate open (G-2 + W-2/W-5), (ii) discovery-confirmed demand, AND (iii) the counsel publication-vs-patent checkpoint executed. Formalization additionally requires an engaged counterparty. not-a-lawyer: patent/FTO/standards-essential questions are framed for counsel, never concluded here.
sources-discipline: ANTI-FABRICATION — every claim [VERIFIED] (primary source fetched, dated) / [UNVERIFIED] / [INFERENCE]; the SafeGate lesson binds; only opened links are cited.
-->

# Lane Charter — Provenance Prior-Art Study → v0 Skeleton + Verifier Scoping

## 1. Mission

Make the tamper-evident building-event provenance standard REAL at desk cost: a rigorous profile of existing primitives (credibility in one paragraph, less to defend), an internal v0 spec skeleton that is a PROFILE of those primitives rather than new cryptography, a scoped design for the standalone verifier (the adoption instrument), and the counsel-question package that gates publication. The play this serves: device-connectivity is owned (Matter/HA); **a tamper-evident provenance/audit standard for smart-home/building events does not exist** — we drive it, permissively licensed, with HomeSynapse as reference implementation and one consuming counterparty as the graduation test.

## 2. Reads-first (priority order)

`context/strategy/fusion-program/2026-07-24_FQ-rulings_decision-package.md` (FQ-2 is law) · the deliberation record §1.7/§2.8 · `design/15-cryptographic-architecture.md` (what the core already commits to: chain_hash lineage, envelope crypto, crypto-shred) · `design/17-aiot-and-cloud-readiness.md` (substrate thesis; SBOM/signed-update seam; RATS-adjacent posture) · `design/16-superior-automation.md` §3.3 (the enterprise audit projection this standard externalizes) · `design/01` §envelope (correlation/causation IDs, the event-shape ground truth) · `2026-06-23_explainability-differentiator-moat_research.md` + the 2026-06-27 currency return Cluster 2/3 (the honest-claim rails + the patent-scan state) · Revenue_Model_and_Licensing_Strategy.md (Assure = the counterparty seed; Apache-2.0 grounds).

## 3. The study — profile these, with a dated currency pass on each

Anchor set (as-of-authoring knowledge; the lane's first act is to verify current status, versions, and adoption of each — [VERIFIED]-tag everything):

| Primitive | What we take from it | The profiling question |
|---|---|---|
| **RFC 9162** (Certificate Transparency v2) | Merkle-tree append-only logs; inclusion + consistency proofs; the log-ecosystem roles (log/monitor/auditor) | Which proof structures map onto an event-log segment export? What does "gossip/monitoring" become at building scale? |
| **COSE** (RFC 9052/9053) | Signature/envelope encoding for constrained devices | The signing envelope for exported segments + attestations |
| **IETF SCITT** (Supply Chain Integrity, Transparency & Trust — WG drafts as of mid-2025; verify current state) | Transparency-service architecture; signed statements → receipts; registration policies | Is a building-event provenance profile expressible AS a SCITT profile? (If yes, we ride a standards train instead of laying track.) |
| **in-toto / SLSA** | Attestation predicate model; layout/policy verification; supply-chain analog | Predicate vocabulary shape for "who changed what, when, provably" |
| **W3C PROV** (PROV-DM/PROV-O) | Provenance vocabulary (entity/activity/agent) | The semantic layer over our correlation/causation chains — adopt terms, not machinery |
| **RATS** (RFC 9334) | Remote-attestation roles (attester/verifier/relying party); evidence vs endorsement | The Phase-3 bridge: how device/platform attestation composes with log integrity (the fusion thesis dependency) |
| **C2PA** (content provenance) | An adjacent industry's deployed provenance profile — adoption lessons, manifest design, what worked | The "how a provenance standard actually got adopted" case study |
| The **key-transparency / binary-transparency** family (deployed CT-derivatives; survey) | Existence proofs that CT machinery generalizes beyond certificates | Precedent inventory for the credibility paragraph |

Also inventory: any existing IoT/building audit-log standard attempts (BACnet audit trails, industrial historians, syslog-signing RFC 5848-class work) — the "why hasn't this been done for buildings" section must name what exists and why it doesn't answer the need [the honest-competition discipline].

## 4. The v0 skeleton (INTERNAL deliverable — a profile, not an invention)

Sections the skeleton must draft: **(1) Scope + threat model** — what tamper-evidence claims v0 makes and expressly does not (insider-with-root, pre-log suppression, and physical-sensor spoofing are named non-goals or bounded; honesty section mandatory). **(2) Data model** — the exported event-segment format profiled over the as-built envelope (ULIDs, correlation/causation, three-level lifecycle, verdict vocabulary); PROV term mapping. **(3) Integrity layer** — hash-chain + Merkle segment roots per RFC 9162 machinery; inclusion/consistency proof formats. **(4) Signature layer** — COSE envelopes; key custody posture (Doc 15 alignment); selective disclosure via Merkle-proof-over-redacted-leaves (attest a property without raw data — the Assure pattern). **(5) Attestation composition (reserved)** — the RATS-shaped seam where platform attestation later binds "this log came from this attested runtime" (Phase-3; reserved, not built — mirrors the Doc 17 reserve-don't-build method). **(6) The verifier contract** — the CLI's verbs. **(7) Conformance language** — what "verifiable per v0" means for a third party.

Rails: zero new cryptographic constructions (profile only — the credibility argument IS the discipline) · the core's Apache-2.0 cleanliness untouched · nothing in v0 requires cloud (local-first inviolate) · the spec is token-parameterized (no candidate mark; R-1).

## 5. Verifier-tool scoping (the "openssl of building-event provenance")

Scope a standalone, dependency-light CLI: `verify segment` (chain + Merkle + signature integrity) · `verify inclusion <event>` · `verify consistency <segment A> <segment B>` · `inspect` (human-readable rendering of what is and is not proven — the honesty surface). Design constraints: runs anywhere (an insurer's analyst laptop), no HomeSynapse install required, reads the exported format only, states its verdict with the same honest vocabulary as the platform (verified / unverifiable(reason) / tampered). Deliverable is a SCOPING NOTE (interface + effort estimate in WU terms), not code — implementation rides the FQ-5 signed-audit-export design brief so the exporter and verifier are designed as one contract.

## 6. Counsel-question package (publication gate input; not-a-lawyer)

(1) Defensive-publication vs patent-first for the v0 material and, separately, for the attestation-boundary layer (the EE-arc candidate — silicon↔log binding); what publishing v0 forecloses. (2) The 2026-06-27 return's patent follow-up scope (Samsung/SmartThings 2024–26; WO2025024326A2; Apple US20250077786A1; CN/EP/KR; 18-month lag) — extended with any provenance-specific findings from §3. (3) Standards-essential/FRAND exposure if v0 later formalizes. (4) License election for the spec text + verifier (permissive; which instrument). Package these as questions with our facts attached — no conclusions.

## 7. Deliverables + done-when

`provenance/prior-art-profile.md` (the §3 matrix, fully cited) · `provenance/v0-spec-skeleton.md` (INTERNAL watermark on page 1: "not for publication — FQ-2 trigger not met") · `provenance/verifier-scoping-note.md` · `provenance/counsel-questions.md` · one return file in this tree for the hub audit. **Done-when:** a reader can (a) defend the profile choices in one paragraph each, (b) hand the skeleton to a future design-doc author with no re-research, (c) hand the counsel package to Pelton-or-successor as-is. Sized: one focused research session + one authoring session (the two-session pattern); everything [VERIFIED]-tagged.
