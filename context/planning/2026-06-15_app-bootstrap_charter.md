<!--
file: context/planning/2026-06-15_app-bootstrap_charter.md
purpose: The CHARTER for the app-bootstrap milestone — the high-density latent-defect milestone where main() wires HomeSynapseCore into a running system. It carries, in ONE coherent gate, the two converge HIGHs (C1 unauth surface, C2 read-path decrypt contract) + C9 (lifecycle reconciliation) + the Track-3 red-team's envelope-finalization one-way doors (F1/F2/F3/F4), because all of them go live / lock at the instant the cipher activates and the HTTP surface opens. This is PLANNING (a charter), not a coding instruction — permitted now; OFF the M7 critical path.
audience: PM, Nick, the future app-bootstrap coding-instruction session
state-type: charter (planning) — AUTHORED with explicitly-PENDING gates; finalize when the gates close
status: FINALIZED-TO-RULED-STATE 2026-06-18. Authored 2026-06-15 (Track-2); UN-PARKED + advanced 2026-06-18 (converge); **the four decision gates RULED by Nick 2026-06-18** (A1 bind posture = loopback-default · A2 auth model = token issuance, carry enterprise-scoping hook · A3 read contract = fail-closed-at-MVP + design degrade seam now, F4 pin · A4 Doc 15 §6 = ratify rotate-DEK-on-restore now + reserve 1-byte envelope tag now, via the AMD-94 pipeline). Decision record: `context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md`. The energy/erasure interview gate (F2) was **RETIRED** 2026-06-15 (M5-D desk research). **Residual before the first AB coding instruction = empirical/mechanical only: CC-1 (bind mechanics, rides AB-1 as a confirm-gate) · R-γ (refines version-tag policy; slot already reserved) · AMD-94 ratification of the §6 amendment.** No decision gate remains open. This is the PRIORITY lane (the runnability unlock).
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4; M6.3 at-rest crypto landed but INERT — main() is a stub). Watermark AMD-93; Doc 12 + Doc 15 LOCKED.
consumes: 2026-06-15_core-review_CONVERGE_synthesis.md (C1/C2/C9, Seam 1/3, CC-1) · 2026-06-15_redteam_reversibility-audit.md (F1/F2/F3/F4, the envelope-finalization gate) · 2026-06-15_Research_R-alpha_PM_Assessment.md (the C2 read contract + rotate-DEK) · 2026-06-15_Research_R-delta_PM_Assessment.md (AX-1 auth/bind, AX-2 startlevels, AX-4 backup-key portability) · Doc 12 (lifecycle), Doc 15 §3.8/§5/§6.
-->

# App-Bootstrap Milestone — Charter

## 1. Scope + anti-scope (lead with Seam 1)

**App-bootstrap turns the built-but-inert system into a runnable one:** `main()` constructs/wires `HomeSynapseCore`, the at-rest cipher (`payloadCipher`) activates, the HTTP surface is exposed, and the lifecycle abstractions are reconciled.

**The single most important fact governing this milestone (converge Seam 1, sharpened by the Track-3 red-team): five independent things go live or lock at the *same instant* — the moment `main()` wires the system.** It must NOT be scoped as "just wire `main()`":

1. **C1** — the HTTP surface becomes a *live unauthenticated* surface (INV-SE-02 has no enforcing code today).
2. **C2** — `payloadCipher` activates, so a read-path decrypt failure becomes a *live availability* risk (today it throws and aborts the whole replay).
3. **C9** — the two disjoint lifecycle abstractions (`SystemLifecycleManager` vs `HomeSynapseCore`) must be reconciled or the system has no coherent init/health path.
4. **The one-way crypto doors lock (Track-3 F1/F2/F3):** the first encrypted row is written here, freezing the envelope format, the encrypted-scope set, and the per-scope nonce construction *permanently* on the immutable, (soon-)hash-chained log.
5. **F4** — the cause-discrimination/tombstone safety argument assumes a *live* `chain_hash`, which is all-ZERO today; the sequencing matters here.

**One-line why it is gated separately from M7:** app-bootstrap is where the two HIGHs go live AND where the irreversible crypto doors shut — M7.x touches none of this, so M7 proceeds independently and app-bootstrap is gated on its own evidence (the crypto red-team + the interviews + CC-1), not on engine readiness.

## 2. Decomposition into first-class sub-milestones (P1 sizing — these are 4 real pieces, not one)

Final numbering rides the placement escalation (§7); labelled AB-1..AB-4 here. **AB-1 + AB-2 + AB-4 must land together** (Seam 1 — auth, the read contract, and cipher activation are the same go-live event); AB-3 (lifecycle) is the substrate they wire into.

### AB-1 — Auth + bind posture (C1 / INV-SE-02)
- `AuthMiddleware` enforced on **every** external route — including `/internal/*`, which today sits outside even the readiness gate. `RateLimiter`. Auth enforced at the router/middleware **before any path resolves** (canonicalize paths first — R-δ AX-1, the HA CVE-2023-27482 path-traversal lesson, web-verified class).
- **Bind posture: loopback-default, LAN exposure is explicit opt-in** (R-δ AX-1, calibrated by CC-1; the HA CVE-2026-34205 host-network LAN-exposure CVSS 9.7 was web-verified this cycle). **Never bind-all-by-default; never treat an interface as "internal."**
- **Zero-config must stay *authenticated* and must not leak:** no default/shared bootstrap secret (R-δ AX-9, the Mirai default-credential class); no pre-auth account enumeration (HA 2023.12 username-leak class); no unauthenticated stream/media path ever (R-δ AX-9, the Eufy-VLC class).
- **Open design decision (escalate, §7): the auth model** (token issuance + scheme). R-δ AX-1(S): adopt a token-issuance model and treat the WebSocket as an external interface needing auth.

### AB-2 — Read contract, fail-closed half (C2 / F-A1)
- On GCM-auth-fail / missing-or-corrupt root key / chain-hash failure → **fail the read batch closed with a distinct, loud error** (the app-bootstrap bucket of the R-α disposition; R-α REC-225/226/231/232 fail-closed half).
- **Design the seam now so the post-MVP degrade half slots in cleanly:** the cause-carrying `DegradedEvent` type, the `(scope, key_version)`-keyed cause lookup, and the chain-validity check (Track-3 F5 granularity note). The *degrade* behavior itself is OUT (crypto-shred WU, §6).
- Carry the **rotate-DEK-on-restore boot-time invariant** (refuse to encrypt in a scope until a fresh DEK is installed or the persisted counter is proven ≥ all prior nonces — R-α REC-235).
- **Track-3 F4 sequencing gate:** the MVP fail-closed half does **not** need a live chain (it fails closed on any decrypt failure). The *degrade* half and the chain-validity check **must not be enabled until `chain_hash` computation + mandatory startup verification are live** — which they are not today. Wire fail-closed now; gate the chain-dependent parts on chain activation.

### AB-3 — Lifecycle reconciliation (C9 / B-M1)
- **Decide and pin (escalate if it has API-shape implications):** does `main()` construct `HomeSynapseCore` directly (re-homing Doc 12's 6-phase model into it), or does `SystemLifecycleManager` wrap `HomeSynapseCore`? Today `SystemLifecycleManager` is an unimplemented interface that never references the real composition root.
- **Adopt openHAB's numbered startlevel ladder as the concrete phase model** (R-δ AX-2, directly transferable): framework → bundles → model-load → state-restore → rules-loaded → engine-active → UI-up. **Gate cipher activation and HTTP exposure to specific phases** — HTTP must not open before AB-1's auth is wired; the cipher must activate before any sensitive read/write; subscribe-after-state-store-catch-up (the converge latent-defect site).
- Wire the health loop (Doc 12 §3.10) + the systemd watchdog + the `platform-systemd` `SystemdHealthReporter` path to the running system (today it has none). Pin with a **lifecycle wiring test**.
- **Pre-migration snapshot + one-click rollback wired into lifecycle before any schema/chain change** (R-δ AX-2: HA's auto-backup-before-update strength; Apple's destructive in-place migration anti-lesson). Bears on chain activation + the V-series migrations.

### AB-4 — `payloadCipher` activation + the envelope-finalization gate (the Track-3 one-way doors)
- Wire the `ScopeKeyManager → PayloadCipher` adapter (Doc 15 §3.8, app-hosted; the M6.2 E2 bridge is held-not-consumed) into the persistence read+write path. **This is the instant the crypto goes live — it lands *with* AB-1 + AB-2, not before.**
- **Carry the red-team envelope-finalization gate (cheap-now / irreversible-later — finalize BEFORE the first encrypted write):**
  - **F1** — the AEAD/envelope **version discriminator** (add a 1-byte algorithm/version tag, or record an explicit written rationale for relying on implicit-v1). *Pending R-γ (§3).*
  - **F2** — the **encrypted-scope width** — **RESOLVED 2026-06-18 (no longer interview-gated):** default to the confirmed set `[identity, presence_personal]` (OQ-15-2; encrypt-on-write, cost measured-trivial ≤0.12%/core). The 2026-06-15 M5-D desk research closed the interview question — energy stays plaintext-at-rest at MVP (Doc 15 §3.4 PII grounds; zero energy event types exist), and "default-to-encrypt under uncertainty" already holds given the trivial cost. No interview needed; widening to future scopes is a post-MVP additive call.
  - **F3** — **bind each scope to exactly one nonce construction** (C6, NIST SP 800-38D §8.3) before first write.
  - **F13 (converge C8)** — write-path hardening: ctor fail-closed guard + treat the nonce dir-fsync `IOException` as FATAL (today swallowed at DEBUG).
- **Backup-key portability (R-δ AX-4 — design now, before a corpus exists):** an exportable, re-enterable recovery artifact tied to the per-scope keys, so a zero-config machine-local-key install can restore on new hardware (HA's mandatory-encrypted-backup key-stranding is the anti-lesson). Co-designed with the backup/restore WU; the *seam* is decided here.

## 3. Entry-gate — what must be GREEN before the first AB coding instruction issues

| Gate | Owner | Status |
|---|---|---|
| Doc 15 §6 currency amendment (rotate-DEK-on-restore binding; "rotate = additive new DEK version, retain priors" per Track-3 F6; high-water-mark → cross-check) | Nick | **RULED 2026-06-18 (A4) — ratify now.** Residual: **AMD-94** pipeline (PM authors → DOCS review → Nick ratifies); Doc 15 is Locked, no silent edit. Decision-gate CLOSED; mechanical ratification pending. |
| **CC-1** run (bind-address empirical → AB-1 bind posture) | Code | **DECISION CLOSED (A1) — posture ruled loopback-default without it.** CC-1 demoted to a *confirm-mechanics* gate on the AB-1 instruction (spec `context/instructions/2026-06-15_CC-1_bind-address_spike_spec.md`, not yet run; non-blocking). |
| **R-γ** returned + assessed → F1 envelope-discriminator | DOCS → PM | **DECISION CLOSED (A4) — 1-byte version tag ruled IN now; slot reserved (v1 = current envelope).** R-γ (still in flight) refines version *policy*, not slot existence; non-blocking. |
| ~~Energy/erasure interviews → F2 encrypted-scope-width~~ | Nick | **RETIRED 2026-06-18** — closed via the M5-D desk research; F2 = `[identity, presence_personal]`, energy plaintext-at-MVP. No longer a gate. |
| Read-contract design beat settled (R-α) + chain-liveness sequencing (F4) | PM | **RULED 2026-06-18 (A3) — fail-closed at MVP + design degrade seam now.** F4 pin held: degrade/chain-validity disabled until `chain_hash` + startup verification are live. CLOSED. |
| Auth model decided (AB-1) | Nick + PM | **RULED 2026-06-18 (A2) — token issuance; WS authenticated; zero-config stays authenticated.** Carry the enterprise per-scope/per-site-claims hook now. CLOSED. |
| Key-portability mechanics (R-δ AX-4 follow-up brief) | DOCS → PM | **OPEN** — recommended dispatch alongside R-γ; co-designed with the backup/restore WU; the *seam* is decided in AB-4, the mechanics are a follow-up (non-blocking for AB issue). |

**All four decision gates are now RULED (2026-06-18, Nick).** The charter is **finalized to that state.** The first AB coding instruction issues once the **mechanical residual** closes — **CC-1** run (confirms AB-1 bind mechanics), **R-γ** returned (refines the already-reserved version-tag policy), and **AMD-94** ratified (the Doc 15 §6 amendment). None is a decision gate. Issue order: **AB-3 first** (lifecycle substrate), then **AB-1 + AB-2 + AB-4 together** (the Seam-1 go-live event).

> **[2026-06-18 — RULED-STATE finalization]:** A1 loopback-default · A2 token issuance (+ enterprise-scoping hook) · A3 fail-closed-at-MVP + degrade-seam-now (F4 pin) · A4 ratify rotate-DEK-on-restore + reserve 1-byte envelope tag (AMD-94 pipeline). Full rationale + Nick's caveats in the decision record. This is the project's priority lane — it produces the first runnable, secure HomeSynapse. Tracked: snapshot 2026-06-18 masthead + `weeks/2026-W26_jun22-jun28.md` Lane 1; backlog AB-1..AB-4 rows.

## 4. Sequencing + independence from M7
- **Independent of M7.** App-bootstrap touches no automation contract; M7.1/7.2/7.3 touch no crypto and no composition root. They run in parallel. The **M6.3-vs-M7 ordering call** (entry-gate row 3 — does app-bootstrap activate before or after M7?) is resolved by the interviews and is a placement question (§7), not an M7.1-readiness question.
- **Within the milestone:** AB-3 (lifecycle substrate) is wired first; **AB-1 + AB-2 + AB-4 land together** as the single go-live event (Seam 1). The **F1/F2/F3 envelope-finalization gate must close before AB-4 activates the cipher** — that is the whole point of gating it here.

## 5. Carry-pins + invariants
INV-SE-02 (auth on every external interface, no local-trust exception) · INV-RF-04 (the store stays replayable) · INV-PD-07 (crypto-shred seam, design-only here) · the chain-validity check (gated on chain liveness, F4) · the lifecycle wiring test · §4c Clock-injection (AB modules are non-whitelisted) · CC-1 (bind calibration) · **Track-3: F1 envelope discriminator, F2 scope width, F3 one nonce-construction-per-scope, F4 chain-liveness sequencing, F13 write-path fatal dir-fsync.**

## 6. In / out scope vs the crypto-shred WU (explicit boundary so they don't double-build)
- **IN (app-bootstrap):** the read-contract **seam** + the **fail-closed half** (CASE-b) + the cause-carrying `DegradedEvent` **type** + the chain-validity check design + the rotate-DEK boot invariant + the backup-key-portability **seam**.
- **OUT (post-MVP crypto-shred WU):** the crypto-shred **operation** (KEK-destruction API, retention/erasure triggers, UI) + the **degrade half** (CASE-a, intended-shred → `DegradedEvent`) + the shred **tombstone** machinery (which Track-3 F5 says must key on `(scope, key_version)` and must not ship before the chain is live).

## 7. Escalations to Nick (do not decide unilaterally)
1. **Milestone placement/numbering.** App-bootstrap likely gates the **first runnable/shippable product**, so it is strategically significant. Proposed placement: **immediately after M7.1** (so the engine has a minimal trigger/condition path *and* the product is runnable early) **or** as a dedicated milestone after M7.3 — **the interviews' ordering call (row 3) decides which.** Propose; escalate; do not lock.
2. **The auth model** (AB-1) — token scheme + WS auth has public-API-shape implications → strategy-adjacent.
3. **(From R-δ, charter-adjacent) the versioning/deprecation policy** (AX-7) and **the retry-vs-REC-162 tension** (AX-5) — both surfaced in the R-δ assessment; the retry one routes to M7.2, the deprecation one should be committed before users author definitions.

## 8. Deliverables / done-when
This charter names the sub-milestones (sized: AB-1..AB-4), the entry-gate (with owners + open/closed), the within-milestone sequencing, the in/out boundary vs the crypto-shred WU, the carry-pins/invariants, the CC-1 calibration, and the explicitly-pending gates; the milestone placement + auth model + locked-decision touches are escalated, not decided. **It is FINALIZED when the §3 gates close** (R-γ + interviews + CC-1 + the Doc 15 §6 amendment). A future session can then open the app-bootstrap coding work knowing exactly what it must carry and why.

## Commit message (handed to Nick — bang-free, quote-free; use git commit -F)
```
docs(plan): add app-bootstrap milestone charter (Track-2)

Charter for the high-density app-bootstrap milestone where main() wires
HomeSynapseCore. Seam-1 insight: five things go live/lock at one instant -
C1 (unauth HTTP surface), C2 (read-path decrypt contract), C9 (lifecycle
reconciliation), the Track-3 one-way crypto doors (F1 envelope version tag /
F2 scope width / F3 nonce-construction), and F4 (chain-liveness sequencing).
Scoped as 4 first-class sub-milestones AB-1..AB-4; AB-1+AB-2+AB-4 land
together (the go-live event).

Resolved beats filled from R-delta (AX-1 loopback-default + auth-before-path-
resolves; AX-2 openHAB numbered startlevels as the lifecycle phase model +
pre-migration snapshot/rollback; AX-4 backup-key portability seam) and R-alpha
(fail-closed read half + rotate-DEK boot invariant).

Entry-gate enumerated with owners; four gates OPEN (Doc 15 sec6 amendment
ratify; CC-1 bind empirical; R-gamma -> F1; interviews -> F2). Charter authored
with gates pending; finalize when they close. In/out boundary vs the crypto-
shred WU made explicit. Escalated, not decided: milestone placement (the
interviews ordering call), the auth model, the deprecation policy + retry
tension. OFF the M7 critical path.

File: context/planning/2026-06-15_app-bootstrap_charter.md
```
