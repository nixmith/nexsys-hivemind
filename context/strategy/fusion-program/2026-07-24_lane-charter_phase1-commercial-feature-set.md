<!--
file: context/strategy/fusion-program/2026-07-24_lane-charter_phase1-commercial-feature-set.md
purpose: Dispatch-ready charter for the Phase-1 commercial feature-set DESIGN BRIEF lane (FQ-5) — org/site hierarchy · RBAC · retention policy · signed audit export · fleet view, designed as projections on the as-built seams. DESIGN ONLY; produces design-doc/AMD candidates and milestone shapes for the MAIN hub's pipeline, never code.
audience: a fresh write-isolated Cowork design session (nexsys-project-manager skill, Mode-1-Architect-leaning); Nick (rulings); the PM hub (audit + Lock-pipeline routing).
state-type: lane charter (dispatch-ready).
status: CHARTERED 2026-07-24 on the FQ-5 ruling. Trigger: launches POST-GATE ONLY (after the 2026-08-16 read; the hub sequences it against the post-gate stack). The discovery re-cut checkpoint (beachhead lane synthesis, ~mid-Oct) gates the PRIORITY ORDER, not the lane start — seam analysis is order-independent.
write-isolation: writes ONLY context/strategy/fusion-program/phase1-design/* (new subtree). Design-doc DRAFTS live there; anything graduating to homesynapse-core-docs rides the MAIN hub's independent-review → co-sign → Lock pipeline (the Doc 16/17/18 path). No code, no core writes, no spine writes.
honest-claim law (binding): until a feature EXISTS, no external copy claims it in the present tense. This lane's output includes the claim-unlock map — which sentence each landed milestone makes true.
rename-readiness: token-parameterized; R-1/G-2 state consumed from the spine at launch. not-a-lawyer where compliance language appears.
-->

# Lane Charter — Phase-1 Commercial Feature Set (design brief: the five projections)

## 1. Mission

Convert the ruled Phase-1 scope definition into ratification-ready design: for each of the five features, the design that expresses it as a **projection/extension over the existing events and seams** (never a re-architecture — Doc 17 §1's test applied to the commercial set), the governance artifacts it requires (AMDs named below), the milestone decomposition (P1 smell-test sized), and the claim-unlock map. This is the artifact that closes the record's honesty gap: "the beachhead claim is currently ahead of the product" becomes a dated, sequenced plan for the product to catch up.

## 2. Reads-first (priority order)

The FQ-rulings decision package + phase plan (this tree) · the discovery synthesis + FQ-5 re-cut REC when available (`discovery/synthesis-memo.md` — gates priority order only) · `design/16-superior-automation.md` §3.3/§3.5 (enterprise audit projection; federation/ScopeRef seam) · `design/17-aiot-and-cloud-readiness.md` (substrate; cloud-additive; the §4 seam table) · `design/15-cryptographic-architecture.md` (chain_hash; crypto-shred; key custody) · `design/18` (namespace governance; DP-18 rulings) · `design/09-rest-api.md` (the auth/admin open question) · `design/04` §3.4 + AMD-40 (retention) · `design/01` §envelope (AMD-94 version slot — the ScopeRef compatibility check) · relevant MODULE_CONTEXT.md files at authoring time (the lane re-derives the current list; minimum: event-model, persistence, state-store, rest-api-adjacent modules) · the invariants register (`Architecture_Invariants_v1.md`) for every INV cited below · `context/status/PROJECT_SNAPSHOT.md` newest beat at launch (the as-built state will have advanced past this charter — source outranks charter).

## 3. Per-feature design charges (each ends in a named artifact)

1. **Org/site hierarchy** — materialize `ScopeRef` (Doc 16 §3.5 / INV-SA-02): scope additive at the envelope, absent-defaults-to-local, no payload-resident scope, no log migration, AMD-94 version-slot compatibility confirmed. **Artifact: a formal AMD draft** (the envelope-shape change class) + the multi-site projection design. Hard rail: single-home deployments feel ZERO change (the free tier is never complicated by the commercial tier).
2. **RBAC** — the auth/authz design on the REST/WS surface (Doc 09's open admin/auth question is the home): principals, roles, scope-binding to (1); local-first (no cloud IdP dependency in core; enterprise IdP federation is a reserved seam, not V1.x); audit of authz decisions AS events (the substrate eats its own dog food). **Artifact: Doc 09 amendment draft + design note.**
3. **Retention policy** — per-scope/per-class retention surfaces over AMD-40's engine + the D4 lineage; interaction with crypto-shred (Doc 15) and the audit projection's never-evicted claims stated precisely (what "retention" means when the moat is "never deleted" — the honest resolution: verdict/audit artifacts have their own retention class, and the claim language follows the design, not vice versa). **Artifact: design note + config-schema delta.**
4. **Signed audit export** — the exporter for the provenance v0 format (the verifier's product twin — designed as ONE contract with `provenance/verifier-scoping-note.md`): segment export, chain_hash/Merkle roots, COSE signing, selective disclosure. Dependency stated honestly: gated on `chain_hash` live (post-MVP with crypto-shred, per the Doc 15/17 sequencing). **Artifact: design note + the provenance-lane contract handshake.**
5. **Fleet view** — the multi-site read-side projection + API + Web-UI surface (contract-versioned per the frozen read-API discipline; the FE lane consumes, never invents shapes). **Artifact: design note + read-API version-increment proposal.**

Cross-cutting: every design names its invariant citations (INV-SA-02, INV-ES-02, INV-LF-01/02, INV-PD-07/08, EXT-INV-1/2 where extension-adjacent, AIOT-INV-1 untouched) · every design passes the "single-home unaffected" test · nothing weakens DP-18-C or the four-layer revenue boundaries (commercial features are Layer-behavior decisions Nick rules at pricing time; the DESIGN keeps the free core fully functional).

## 4. Deliverables + done-when

`phase1-design/` — five design artifacts per §3 + `milestone-map.md` (V1.x decomposition, P1-sized, dependency-ordered, each milestone's claim-unlock line) + `claim-unlock-map.md` (feature → the exact external sentence it makes true) + one return file for the hub audit. **Done-when:** the MAIN hub can route the AMD/design-doc candidates into the Lock pipeline and author the first V1.x coding instruction without re-research; Nick can see, on one page, when each commercial claim becomes honestly speakable. Sized: one grounding session + one-to-two authoring sessions (the lane proposes a split if it exceeds the P1 smell test — no epics under one label).
