<!--
file: context/planning/2026-06-15_M7-plus_research-avenues.md
purpose: The converge's consolidated research set — A's + B's "research avenues surfaced" merged, de-duplicated against the standing R-α…R-ε side-research set, prioritized, and routed (DOCS design-research vs CORE empirical spike vs CORE-instruction-embedded vs governance). The single routed research doc the M7-forward sessions and Nick draw from.
audience: Nick (dispatch view), PM (next sessions)
state-type: planning
status: COMPLETE 2026-06-15
inputs: the two audits (A §"Research avenues", B §"Research avenues") · context/planning/2026-06-13_side-research-candidates_CORE-DOCS.md (R-α…R-ε) · the M7 merged-disposition + charter skeleton
-->

# M7+ Research Avenues — Consolidated & Routed (converge)

Merges the research avenues surfaced by Review Sessions A and B, de-duplicates them against the **standing side-research set R-α…R-ε** (`2026-06-13_side-research-candidates_CORE-DOCS.md`), and routes each. **Routing convention (standing):** design/architecture/market → **DOCS Project**; code-empirical spikes → **CORE Project** (Coder-authored throwaway, Nick-run, never production). A third bucket — **CORE-instruction-embedded / governance** — is for items that are *not* a research dispatch (they ride an M7.x instruction or a governance pin). The no-research-without-a-consumer rule holds: every item names its consuming milestone.

**One-line orientation:** this review surfaced **no new DOCS research session** beyond what R-α…R-ε already cover — it **reinforces R-α and R-γ, refines R-ε, leaves R-β/R-δ unchanged**, adds **one high-value scope-extension to R-α (NEW-1)**, **one tracked CORE spike (NEW-3)**, and routes everything else into M7.x instructions or governance pins. The standing dispatch order (R-α + R-β first) is unchanged and endorsed.

---

## 1. De-duplication against the standing R-α…R-ε set

| Standing item | Status after this review | What A/B added |
|---|---|---|
| **R-α** — crash-safe backup/restore for the event-sourced + per-scope-encrypted store (DOCS) | **REINFORCED + scope-extended (NEW-1)** | A's F-A1 raises the **read-path** half of the same crypto-availability question: when a payload can't be decrypted (shred / key-loss), does replay **degrade-per-row** or **fail-closed-whole-store**? R-α already owns the *restore* nonce-monotonicity half (OR-M6-NONCE). Fold NEW-1 into R-α's scope, or run it as a short standalone design note **before** the crypto-shred WU. Highest-leverage near-term DOCS item. |
| **R-β** — GraalVM native-image (C15) + Gen-ZGC-vs-G1 Pi pause (C16) spikes (CORE) | **UNCHANGED** | Not touched by A/B (no module-9-22 or crypto finding bears on the replatform/JNI question). F-A5b is Pi-floor-empirical but a different harness (NEW-3). Still HIGH-readiness; gates the M13 sd_notify transport + the LTD-01 trajectory. |
| **R-γ** — M9 Integration Runtime supervisor / health-FSM / thread architecture (DOCS) | **REINFORCED** | B confirmed `integration-runtime` + `integration-zigbee` are 100% contract / 0% code, and the C10 cluster (B-9a/B-10a/B-M4) is exactly the unpinnable-until-M9 behavior R-γ exists to de-risk. R-γ now has a concrete defect-list to resolve at M9 scoping (AMD-56 AUTH_FAILED routing, AMD-62 backoff schedule). |
| **R-δ** — M14 Zigbee de-risk (DOCS) | **UNCHANGED (premise confirmed)** | B confirmed `integration-zigbee` is 38 files of pure type scaffold, zero hardware exposure — the LTD-11/concurrency/hardware audit is correctly deferred to when M14 transport classes land. No new scope; the scaffold-status premise R-δ assumes is verified. |
| **R-ε** — M12 Observability: MDC propagation on virtual threads (DOCS / CORE) | **REFINED** | B's source-check sharpens it: **no MDC surface exists repo-wide**, and `IntegrityService` (the M12 seam) "does not exist even as a seam." So R-ε is **moot-but-forward-relevant** — the vthread MDC-copy mechanism (B-211 ruling; Scoped Values trajectory-only) must be designed in **from the start** at M11/M12, not retrofitted. No code surface today; can wait until M9/M10/M11 land. |

---

## 2. Net-new items surfaced by this review

| ID | item | route | priority |
|---|---|---|---|
| **NEW-1** | **Confidentiality-vs-availability contract for the encrypted event-sourced log** (F-A1 / C2): degrade-per-row (`DegradedEvent`) vs fail-closed-whole-store on decrypt failure (shred / key-loss / downgrade). The design beat that gates **both** crypto-shred (vs INV-PD-07) and backup/restore (R-α). | **DOCS — fold into R-α** (or a short standalone design note before the crypto-shred WU) | **HIGH** — gates a near-future WU + collides with INV-RF-04 / INV-PD-07 |
| **NEW-3** | **Per-event fsync cost on the Pi-4 floor** (F-A5b): the full `encryptPayload` incl. the `scope_nonce_counters.json` atomic-rewrite + 2 fsyncs at 60 ev/s presence-burst — write-thread occupancy + p99 publish latency vs plaintext. | **CORE empirical (= CC-2)** | **LOW now** — gates a *future* decision (widening `encrypted_scopes`); dispatch when that decision is live |

---

## 3. Routed into M7.x instructions / governance — NOT a research dispatch

These came in as "avenues" but are CORE-instruction-embedded or governance actions; they need no external session.

- **Composition-root automation wiring is the M7 latent-defect surface** (B avenue 1). The M7.1 instruction carries a **composition-root manifest-survey + a lifecycle wiring test** (the AMD-92-INV-02 "full manifest before first publish" forcing point + the subscribe-after-state-store-catch-up ordering). → **CORE, M7.1 instruction-embedded.** (Also a synthesis-doc M7 carry-pin.)
- **Trigger-evaluation storm benchmark** (B avenue 2 / REC-157). Already a charter obligation — an **investigation trigger** in the M7.1 instruction (Doc 07 §10 targets), not a dispatch. → **CORE, M7.1-embedded.**
- **F5 automation event-record widening design beat** (B avenue 3 / C4 / Seam 2). The cross-seam design (widen `AutomationCompletedEvent`/`AutomationTriggeredEvent` to the F5 fields + `INTERRUPTED`/`CONDITION_NOT_MET`, flattened per type-residency, AMD-52-coded). → **CORE, settle at M7.1 scoping; build in the M7 F5 slice.**
- **`RunCausalChain` cascade-governance interface spec** (B avenue 4 / C3). Before M7.2, the AMD-91 cascade shape + the deterministic cycle-suppression contract (AMD-91-INV-01: causal-chain-and-config-only, no windowed state) needs a crisp spec so the implementer doesn't reach for the windowed Doc 01 §4.5 correlation map. → **CORE, AMD-correction / interface-spec (the C3 doc-fix is its first step).**
- **Single nonce-strategy-per-key governance pin** (A avenue 2 / C6 / F-A2). A one-paragraph enforced invariant + a NIST SP 800-38D §8.3 citation in Doc 15 §3.4. → **Governance (PM-drafted pin → Nick); not research.**
- **Cross-module mapping-agreement tests as a standing pattern** (A avenue 3 / C5 / F-A3). Generalize the `EncryptionScope`↔`encryptionScopeId` agreement test (in `app`) to any String-mirror across a deliberate module boundary. → **CORE pattern, instruction-embedded; consider a standing rule.**
- **Migration-splitter hardening** (A avenue 6 / C7 / F-B1). The one-line guard is the C7 coding instruction; the broader "replace vs extend the splitter" is a small design call, not a dispatch. → **CORE instruction.**
- **Auth + bind-posture before network exposure** (B avenue 5 / C1 / B-H1) and **the lifecycle reconciliation** (B avenue 6 / C9 / B-M1). → **needs-Nick-decision + app-bootstrap design**, not a research session (CC-1 calibrates the bind-posture urgency empirically).
- **WS backpressure design** (B avenue 8 / C11 / B-M5). The bounded-buffer / `CLIENT_TOO_SLOW` policy; M7's live-trace streaming is its first consumer. → **CORE at the WS milestone.**
- **Non-finite `AttributeValue` serde** (A avenue 5). Whether `FloatValue(NaN/±Inf)` survives the Jackson round-trip — a small confirmatory test. → **CORE confirmatory test (trivial), not a dispatch.**

---

## 4. Prioritized dispatch order (which warrant their own session — Nick runs separately)

The standing recommendation ("R-α and R-β are the highest-leverage now") is **endorsed and unchanged** by this review; the converge sharpens *why*:

1. **R-α (with NEW-1 folded) — DOCS, dispatch first.** It is the one research session adjacent to the live crypto seam **and** the app-bootstrap milestone where C2 detonates. Returns the confidentiality-vs-availability contract (NEW-1) + the restore nonce-monotonicity co-design (OR-M6-NONCE) — both needed before the crypto-shred and backup/restore WUs. HIGH readiness (Doc 15 §3.4/§6 + OR-M6-NONCE define the constraint set). **Not M7-blocking** — it serves the parallel crypto/app-bootstrap track.
2. **R-β — CORE empirical (Nick runs on the Pi), dispatch next.** Gates the M13 sd_notify transport pick + the LTD-01 replatform trajectory. Unchanged by this review; still the second-highest-leverage now.
3. **R-γ — DOCS, before M9 scoping.** Reinforced by the C10 cluster; de-risks the supervisor/health-FSM before M9 is sized (avoids the M4-style "size discovered in arrears").
4. **R-δ / R-ε — lead the next cycle.** R-δ (M14 Zigbee, runway-de-risking, long hardware lead time) and R-ε (M12 observability, refined to "design-in-from-the-start," no code surface yet) can wait until M9/M10/M11 land.

**NEW-3 (= CC-2)** is tracked, not dispatched — it fires only if/when widening `encrypted_scopes` is contemplated.

**M7 itself needs none of these to start.** Its only research-grade inputs are the two charter-obligation empirical spikes (storm benchmark REC-157; confirmation-deadline calibration REC-161), both embedded in the M7.x instructions.

---

*Companion to `context/audits/2026-06-15_core-review_CONVERGE_synthesis.md`. The R-α…R-ε definitions live in `context/planning/2026-06-13_side-research-candidates_CORE-DOCS.md`; this doc updates their status, it does not supersede them.*

## Commit message (handed to Nick — `!`-free)

```
docs(planning): consolidate M7+ research avenues (converge)

Merges Sessions A + B research avenues, de-duplicates against the standing
R-alpha..R-epsilon side-research set, prioritizes and routes each.

Outcome: this review adds no new DOCS research session beyond R-alpha..epsilon
-- it REINFORCES R-alpha (read-path confidentiality-vs-availability, NEW-1)
and R-gamma (the M9 supervisor defect-list), REFINES R-epsilon (no MDC surface
exists yet; design-in from the start), leaves R-beta/R-delta unchanged. One
tracked CORE spike NEW-3 (per-event fsync on Pi-4 = CC-2), dispatched only when
widening encrypted_scopes is contemplated. Everything else routes into M7.x
instructions or governance pins, not a dispatch.

Dispatch order endorsed unchanged: R-alpha (with NEW-1) first, then R-beta,
then R-gamma; R-delta/R-epsilon lead the next cycle. M7 needs no research-first
dispatch to start.

File: context/planning/2026-06-15_M7-plus_research-avenues.md
```
