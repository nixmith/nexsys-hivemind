<!--
file: context/instructions/2026-06-15_Research_R-delta_Competitive-Ecosystem-Architecture_Deep-Dive_Brief.md
purpose: DOCS-Project / deep-research brief — R-δ. A broad, web-grounded competitive deep dive across the smart-home / IoT ecosystem, run under TWO lenses: (1) MISTAKES TO AVOID — design errors, breaking-change disasters, data-loss / shutdown / bricking post-mortems, security incidents, authoring-UX failures that other systems made; (2) STRENGTHS TO ADOPT — architectural wins worth borrowing. Findings are mapped onto HomeSynapse's about-to-lock decision surfaces (the app-bootstrap charter + the M7 automation engine + the crypto lane). Cowork PM assesses the return and issues follow-up briefs where gaps surface.
audience: DOCS-Project researcher / deep-research harness (web search required) → PM serialized assessment on return
state-type: research brief — competitive deep dive (READY TO DISPATCH)
status: AUTHORED 2026-06-15 (Track-3 follow-on; Nick-directed "full competitive deep dive → Cowork assesses + follow-ups").
routing: DOCS Project (design/architecture) OR the deep-research harness. Code-empirical sub-questions are flagged and routed to a CORE spike, NOT answered here.
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4; M6.3 at-rest encryption landed but inert). Doc 15 LOCKED; AMD watermark 93. The point of this brief is to pressure-test our about-to-lock choices against the field BEFORE app-bootstrap.
consumes: the Track-3 reversibility audit (F1-F4), the CONVERGE synthesis (C1/C2/C9 + the M7 contract), Doc 15 (crypto), the AMD-88..93 automation block.
-->

# RESEARCH BRIEF (COMPETITIVE DEEP DIVE): R-δ — What the Smart-Home / IoT Ecosystem Got Wrong, and Right

**Register:** systems-design / product-architecture (DOCS Project). **Web search required, broad.** Connector-blind acceptable — declare it and list gaps.

**The job: two lenses, one goal.** For each decision surface below, surface BOTH:
- **MISTAKES TO AVOID** — concrete, cited design errors, breaking-change disasters, data-loss / shutdown / bricking events, security incidents, and authoring-UX failures that real smart-home/IoT systems made. *Post-mortems, incident write-ups, maintainer retrospectives, and CVEs are the gold here.*
- **STRENGTHS TO ADOPT** — concrete architectural wins, patterns, and "they nailed this" features worth borrowing, with enough detail to actually reuse.

**The goal is not a survey for its own sake — it is to de-risk HomeSynapse's about-to-lock decisions** (the app-bootstrap charter, the M7 automation engine, the crypto/backup lane) by learning from a decade of other people's scar tissue and wins. **A finding that does not map onto one of the §3 decision surfaces, or that re-states a generic best practice we already follow, is a non-finding.**

**The deliverable is the §4 mapped-findings table + the §1 "five things this most changes or confirms."** The PM assesses the return in Cowork, routes each finding to the consuming charter/WU, and issues follow-up briefs where the return opens a gap — so flag your own thin spots explicitly (they become the next dispatch).

---

## 0. Ground to hold (do NOT re-litigate; surface DELTAS against these)

HomeSynapse is a **local-first, on-device, event-sourced smart-home OS** targeting a Raspberry-Pi-class floor. The following are LOCKED — a finding may argue one is a mistake *only* with strong cited evidence and an explicit amendment case; otherwise, map findings as deltas/refinements, not re-openings:

- **Local-first, no cloud dependency for core function.** The "cloud death" graveyard (§2) is a *motivation*, not a question. Do not recommend a cloud-required design.
- **Event-sourced, append-only, immutable log** with a SHA-256 hash chain over stored bytes (tamper-evidence). Crypto-shred (per-scope key destruction) is the erasure mechanism, not row deletion.
- **At-rest encryption of sensitive-PII scopes** under per-scope AES-256-GCM DEKs, counter nonces, machine-local root key at MVP (passphrase/TPM = Tier-2). *(The Track-3 audit's F1 question — should the envelope carry an algorithm/version tag — is owned by the separate R-γ brief; do not duplicate it here. Here, the relevant question is the broader one: how does the field do at-rest crypto + agility + key management, and what did they get wrong?)*
- **Automation as a sealed trigger/condition/action model with NO templating DSL** (deliberate — the Jinja/template-string fragility class is an explicit anti-requirement). Stable trigger IDs, scenes-as-automations, deterministic replay, bounded cascade governance.
- **Auth mandatory on every external interface, no local-trust exception** (INV-SE-02). Zero-config install (no passphrase prompt) is a brand property.
- **Constrained-hardware floor** (Pi-4 validation): the design must run there.

Your job is to find where the field's experience *confirms*, *sharpens*, or *warns against the implementation of* these — not to re-argue the theses.

## 0.1 Authoritative state (do not work from memory)

- HomeSynapse is pre-runnable: `main()` is a stub; the at-rest crypto is shipped but inert; the automation engine (M7) is contract-ratified (AMD-88..93) but unbuilt. **So this research informs choices that are still cheap to change** — that is the timing leverage.
- The imminent lock points this de-risks: the **app-bootstrap milestone** (wires `main()`, activates the cipher, exposes the HTTP surface, reconciles lifecycle) and the **M7.1+ automation build**.

---

## 1. Systems to survey (the living and the graveyard)

**Living platforms (architecture + strengths + their documented mistakes):**
- **Home Assistant** (Core + Supervisor + OS + Add-ons) — the dominant local-first comparable; the richest source of both wins and scar tissue (breaking-change cadence, the YAML→UI migration, the template-fragility class, the auth model, the Supervisor watchdog, backups, the Recorder/history DB).
- **openHAB** (rules engine, OSGi modularity, item/thing model).
- **Hubitat** (local-first hub, app/driver model, the "we left SmartThings cloud" positioning).
- **SmartThings** (the Groovy cloud IDE → its 2022-23 shutdown and forced migration to the new Edge/Rules API — a major *mistake/migration* case study).
- **Apple HomeKit / Home** (security + privacy posture, HAP, the closed but trusted model; the "Home architecture upgrade" reliability stumbles).
- **Node-RED** (visual flow automation — study what makes flows powerful AND what makes them unmaintainable; informs our no-DSL stance).
- **ESPHome** (declarative YAML device config — a strength to study for config ergonomics).
- **Zigbee2MQTT / ZHA**, **Z-Wave JS** (local radio stacks, security pairing S0/S2, device-reachability/availability semantics).
- **Matter / Thread** (the interoperability standard + its rollout reception — onboarding complexity, multi-admin, the gap between promise and field experience).
- **openHAB/Domoticz/FHEM/Homey/Indigo** as breadth/contrast where useful.

**The graveyard (cautionary post-mortems — longevity, data-loss, bricking, cloud-death):**
- **Revolv** (Nest, 2016 — hubs bricked when the cloud was shut down; the canonical "smart home cloud death" case).
- **Insteon** (2022 — abrupt shutdown, servers dark, hubs/app dead overnight; later revival; the data-and-control-loss lesson).
- **Wink** (2020 — sudden subscription-or-brick).
- **Staples Connect, Lowe's Iris, Best Buy Insignia/Connect, Charter/Spectrum** — discontinued ecosystems; what users lost and why.
- **SmartThings Groovy sunset** — forced migration pain even when the platform survived.
- **Z-Wave/Zigbee security incidents, IoT botnets (Mirai), the Ring/Eufy/Wyze privacy incidents** — security/privacy cautionary tales relevant to our trust brand.

---

## 2. Why the graveyard matters (the motivation, stated once)

These are not for re-arguing local-first — they are for **extracting the specific failure mechanisms** so HomeSynapse's app-bootstrap and data model structurally cannot repeat them: What exactly broke when the cloud went dark (control? history? device pairing? the hub itself)? What could a local-first, event-sourced design have preserved? Where did "forced migration" destroy user automations/data, and what versioning/export discipline would have prevented it? Map each lesson to a concrete HomeSynapse design property that already prevents it — or a gap that doesn't.

---

## 3. Decision surfaces (research axes — answer ALL; two-lens each)

For each: **(M) mistakes to avoid** (cited) · **(S) strengths to adopt** (cited) · **(Δ) the delta/refinement for HomeSynapse** mapped to the named lock point.

**AX-1 — App-bootstrap: auth, bind posture, and the local HTTP/API surface (maps to C1/INV-SE-02).**
How do local-first systems secure the on-device API/UI surface? (M) auth-bypass / local-trust-assumption incidents (e.g., unauthenticated local APIs, HA/Hubitat/SmartThings local-API exposure, default-bind-all-interfaces footguns, CSRF/websocket-auth gaps). (S) the strongest local-auth + zero-config models (token issuance, loopback-vs-LAN posture, onboarding without a passphrase prompt while still authenticating). Δ: what should the app-bootstrap charter enforce before `main()` exposes the surface?

**AX-2 — App-bootstrap: lifecycle, health, and watchdog orchestration (maps to C9).**
(M) startup-ordering / partial-init / split-brain failures; watchdog/self-heal designs that mask vs surface faults. (S) HA Supervisor's health/watchdog model, systemd integration patterns, init-phase sequencing, readiness/liveness for a single-box home OS. Δ: how to reconcile `SystemLifecycleManager` vs `HomeSynapseCore` and wire a health loop + systemd watchdog correctly.

**AX-3 — At-rest crypto, key management, and agility in the field (maps to the crypto lane; complements R-γ, does not duplicate F1).**
(M) at-rest crypto mistakes others made — hardcoded ciphers that couldn't migrate, key-management failures, "encrypted but the key is on the same disk" overclaims, nonce/IV reuse incidents. (S) the best at-rest + key-management designs for local devices (LUKS, SQLCipher, age, mobile keystores, TPM/secure-enclave use on hobbyist hardware). Δ: confirm/sharpen the machine-local-root threat model and the Tier-2 passphrase/TPM upgrade path; flag anything our posture overclaims.

**AX-4 — Backup, restore, and user-facing erasure (maps to R-α's backup/restore WU + F2 scope width).**
(M) backup/restore data-loss incidents; restores that corrupted state or leaked keys; erasure that didn't actually erase. (S) how mature systems do encrypted backup, atomic restore, and GDPR-style/user erasure on an append-only or stateful store; **which data categories the field treats as sensitive/erasable** (directly feeds F2 — is energy/occupancy treated as erasable elsewhere?). Δ: inputs for the backup/restore co-design and the encrypted-scope width decision.

**AX-5 — The automation engine: model, governance, and the authoring-UX trap (maps to AMD-88..93).**
(M) **the templating-DSL failure class** — document HA's Jinja-template fragility, silent-never-fires misconfigurations, and the broader "automations that break on edits / are non-deterministic / loop" problem (Node-RED flow sprawl, SmartThings rule limits, cascade/infinite-loop incidents). (S) the best trigger/condition/action models, stable-trigger-ID designs, scenes-as-automations, run-trace/lineage UX, and deterministic/replayable execution. Δ: does the field's scar tissue confirm our sealed-permit + no-DSL + bounded-cascade + stable-trigger-ID choices, and what authoring affordances are we missing?

**AX-6 — Event-sourcing, data model, integrity, and the history DB (maps to the spine + Doc 01).**
(M) history/recorder DB blowups (HA Recorder/SQLite growth + purge pain), schema-migration breakages, tamper/integrity gaps. (S) append-only/event-sourced designs in the wild, integrity/tamper-evidence (Merkle/transparency-log patterns), retention/compaction that works on Pi-class storage. Δ: retention + integrity refinements; the chain-activation/verification design.

**AX-7 — Breaking-change and config-versioning discipline (maps to LTD / config posture).**
(M) the breaking-change tax — HA's monthly breaking changes, YAML→UI migration churn, deprecations that broke user setups; how much trust/goodwill it cost. (S) ecosystems with strong backward-compat / migration discipline; config schema versioning that doesn't strand users. Δ: the versioning + deprecation policy HomeSynapse should commit to before users author definitions (ties to AMD-88/89 user-YAML lock-in).

**AX-8 — Integration model: radios, Matter/Thread, and device reachability (maps to the integration subsystem / M9+).**
(M) Matter/Thread onboarding + multi-admin pain, Zigbee/Z-Wave pairing-security gaps (S0 downgrade), cloud-integration fragility. (S) the strongest local integration + device-availability/reachability models (Z-Wave JS, Zigbee2MQTT, Matter local control). Δ: inputs for the reachability/availability semantics our triggers consume (AMD-88 ReachabilityTrigger) and the integration roadmap.

**AX-9 — Privacy posture & trust brand (maps to strategy + INV-PD).**
(M) the privacy incidents that destroyed trust (Ring/Eufy/Wyze camera leaks, cloud data-sharing surprises). (S) what privacy-forward designs do — data minimization, on-device processing, transparency, user-owned keys — and how they communicate it. Δ: what sharpens HomeSynapse's trust positioning and the sensitive-data classification (feeds F2 + the strategy layer).

**AX-10 — Constrained-hardware performance & footprint (maps to the Pi-4 floor).**
(M) where comparable systems fall over on Pi-class hardware (memory, SD-card wear, startup time, DB I/O). (S) what runs well + the techniques that got them there. Δ: performance risks for our write-path/automation engine on the floor.

---

## 4. Mandatory return document format

Save the return to `homesynapse-core-docs/research/returns/` (PM rehomes/assesses on intake). Structure:

```
# R-δ: Competitive Ecosystem Architecture Deep Dive — DOCS Research Return

## 0. Scope + method [M]  — systems actually examined; search strategy; connector-blind gaps declared.
## 1. The five things this most CHANGES or CONFIRMS for HomeSynapse [M — LEAD WITH THIS]
        Five ranked bullets, each: the finding, whether it CONFIRMS / SHARPENS / WARNS-AGAINST one of our
        locked choices or an about-to-lock charter beat, and the one action it implies.
## 2. Per-system deep dives [M]  — one subsection per major system (HA, openHAB, Hubitat, SmartThings,
        HomeKit, Matter/Thread, Node-RED, ESPHome, + the graveyard cluster): architecture in brief, the
        notable MISTAKE(s) with citation/post-mortem, the notable STRENGTH(s) with citation.
## 3. Mapped findings table [M — THE DELIVERABLE]
        axis (AX-1..10) | lens (Mistake/Strength) | the finding (system + specifics + citation) |
        delta/refinement for HomeSynapse | consuming lock point (app-bootstrap charter / M7 / crypto lane /
        strategy) | confidence (A/B/C)
## 4. Cautionary post-mortems [M]  — the graveyard: per dead/forced-migrated system, the exact failure
        mechanism and the HomeSynapse property that already prevents it (or the gap that doesn't).
## 5. Open gaps + recommended follow-up briefs [M]  — where this deep dive is thin; phrase each as a
        crisp follow-up research question the PM can dispatch next (this is how the assess→follow-up loop runs).
## 6. Appendix: Sources [M]  — URL families grouped by system; every load-bearing claim traceable;
        post-mortems / CVEs / maintainer retrospectives flagged as such.
```

## 5. Evidence standards (non-negotiable)

- Every claim carries a citation (URL family + enough specificity to verify). For **mistakes**, prefer **primary post-mortems, maintainer retrospectives, official deprecation/shutdown notices, issue trackers, and CVEs** over secondary commentary — a "mistake" finding with only a blog opinion behind it is graded C.
- Distinguish **documented fact** (incident report, official docs, source) from **community consensus** (forum/reddit sentiment — usable for *where the pain is*, labeled) from **your inference** (labeled).
- No fabricated HomeSynapse internals — the only HomeSynapse facts you assert are in §0/§0.1. If a delta needs a HomeSynapse detail not stated, name it as an *assumption to verify with the PM*.
- Date your sources — the ecosystem moves fast (Matter, SmartThings Edge, HA releases). Note freshness, especially for anything past mid-2025.

## 6. Guardrails (violations = the finding is discarded)

- **Two lenses or it doesn't count.** A system write-up with only strengths or only mistakes is incomplete — every major system gets both lenses where evidence exists.
- **Gap-relative, mapped, actionable.** Every finding maps to an AX axis and a consuming lock point, and implies an action or a confirmation. "HA has lots of integrations" is a non-finding; "HA's `2021.x` template-evaluation change silently broke automations that referenced removed entities — confirms our no-DSL + fail-closed-on-load stance, and suggests an explicit definition-validation-at-load gate" is a finding.
- **Respect the LOCKED ground (§0).** Don't recommend cloud-required designs, row-deletion erasure, or a templating DSL. Argue against a locked choice only with strong cited evidence + an explicit amendment case.
- **Don't duplicate R-γ.** The envelope-version-tag question (F1) is owned by the R-γ challenge brief. Here, at-rest crypto is the *broad field-practice* lens (AX-3), not the tag decision.
- **Stay design-level.** No HomeSynapse code. Code-empirical questions route to a CORE spike (flag them).

## 7. What the PM does with the return (the assess → follow-up loop, so you aim at it)

The PM assesses the return serially in Cowork: grades it, verifies load-bearing claims, and **routes each §3 finding to its consuming lock point** — the app-bootstrap charter (AX-1/2/3/4), the M7.x instructions (AX-5/8), the crypto/backup lane (AX-3/4), the strategy layer (AX-9), or the performance pins (AX-10). **The §5 open-gaps become the next dispatch** — the PM turns each into a focused follow-up brief (the loop Nick described). So the most valuable return both answers broadly AND names precisely where it is thin, because that thinness is the next research question.

---

## Routing & dispatch note

**DOCS Project (fresh conversation, broad web search) OR the deep-research harness.** This is a wide pass — if dispatched as deep-research, allow it to fan out across the §1 systems and §3 axes. It is **parallel to everything** (R-γ, R-β, M7, the interviews) and competes for nothing on the critical path. Returns feed the app-bootstrap charter (target: authored early next week, after the Thu/Fri interviews + R-γ). Connector-blind acceptable; declare gaps. The PM will issue follow-up briefs from §5 on return.
