<!--
file: context/decisions/2026-06-06_post-M4_M5-window_decisions.md
purpose: Records Nick's decisions D1–D8 on the post-M4 plan + M5 scoping (the blended, lane-tracked M5 window). The authoritative decision record the W24 charter and the M6 entry-gate work execute against.
audience: Nick (owner), PM, Coder
update-cadence: once (decision), then reference
state-type: decision
status: DECIDED 2026-06-06 by Nick — D1–D8 settled; D2 carries an open sub-decision (the write-path-encryption boundary) routed to the crypto owner-doc.
last-verified: 2026-06-06 against the synthesis (2026-06-06_post-M4-plan-and-M5-scoping.md) + homesynapse-core HEAD `8ef9e9f`.
-->

# Post-M4 / M5-Window Decisions — D1–D8 (DECIDED)

**Decision owner:** Nick. **Author:** PM. **Status:** DECIDED 2026-06-06.
**Source synthesis:** `context/planning/2026-06-06_post-M4-plan-and-M5-scoping.md` (the candidate work universe C1–C20; the three alternatives; the open decisions framed with defaults).
**Executes via:** the W24 charter (`context/planning/weeks/2026-W24_jun08-jun14.md`) — four lane-tracked first-class pieces M5-A…M5-D.
**Headline:** Adopt **Alternative 3 — the blended, lane-tracked M5 window**, chartered for its primary purpose (de-risk M6), sized to Nick's review/ratification gate, with the website/docs floor protected. The key reframing the synthesis surfaced and Nick adopted: the originally-planned M5 (Platform API + test-support) is **thinner than it looked** — the test-support doubles already shipped in the M1.x wave — so the real leverage is the design/decision work that is either **regret-proof** or **gates M6**.

---

## D1 — M5 posture: ADOPTED (blended multi-lane window), with two disciplines

Charter the window for its **primary purpose — de-risk M6** — not as "M5 = Platform API." Size it to **Nick's review/ratification gate capacity, not agent output** (Nick is the serial bottleneck). Accordingly: **trim Lane B to the M6 entry-gate (C6/C7/C12) + the three regret-proof schema decisions (C8/C9/C10) only**; defer C11 (INV-SE-04), C13 (Doc 02 currency), C18 (doc hygiene) to just-before-their-consumer. Keep **Lane A small** (C1/C2 + C5 + the `FloorId` registration). **Lane-track each lane as a first-class piece with its own backlog row + done-when (P1)** — the window is only sound if it never becomes an untracked epic.

## D2 — Crypto MVP scope: DECIDED (diverges from the synthesis default). Operational crypto-shredding is POST-MVP; build the infrastructure/seams now.

**Decision.** Build the **per-scope key-management infrastructure + the encryption-scope categories + at-rest encryption at MVP** (regret-proof, leaves room); **defer operational per-category crypto-shredding to its first real consumer** (the first cloud/institutional data-sharing product) — *unless* the energy/institutional interviews (M5-D) surface a launch-window buyer requiring verifiable erasure, in which case re-scope up.

**Reasoning (Nick).** Crypto-shredding is load-bearing when there's PII at scale, cloud/multi-party data flow, or institutional buyers — the Connect/Assure/Grid era, which is post-MVP. At launch (local-first, single-home, free), the privacy story is already carried by zero-telemetry-by-default + at-rest secret encryption, without operational shredding.

**PM assessment (endorsed, not flipped).** The defer-call is right: (1) operational shredding has **no MVP consumer** — the immutability-vs-erasure conflict it resolves (INV-PD-07 deletion-via-key-destruction, `:425`) only bites when there is a *reason to retain data after erasure* (institutional audit) or *off-device replication* (cloud), both post-MVP; a local single-home user's erasure is served by whole-install reset. (2) Deferring it forfeits **no claimed MVP differentiator** — the strategy scopes the crypto/verifiable-transparency first-mover play as *horizon* ("when the engineering maturity… is proven," `:835`), not a launch claim. (3) Opportunity cost on critical-path M6 is real, and the decision is evidence-gated + governance-correct.

**Reconciliation mechanism.** Author an **INV-PD-07 amendment proposal** through the normal AMD/ratification pipeline, narrowing the MVP mandate from *"crypto-shredding must be operational for ≥1 category"* to *"MVP establishes the key-management infrastructure + encryption-scope categories; operational crypto-shredding lands with the first cloud/institutional data-sharing product."* Keep the amendment **minimal** (strike only the operational clause; preserve sentence 1 + the design intent). **Widen it by one line** to also state the **INV-PD-03 at-rest posture** decided in the sub-decision below, so INV-PD-03 and INV-PD-07 are reconciled in **one** pass, not two. **Full DOCS-Project review — NOT the P4 lightweight block-track** (this narrows a constitutional privacy invariant the moat rests on). **Assign the AMD number at authoring** (66–71 = the M6 config amendments; Research 7 reserved 72–85 — give the privacy amendment a clean number per P2 assign-at-authoring). Do not let the unpromoted Draft silently override a ratified invariant — amend it explicitly.

**Sub-decision — the write-path-encryption boundary (PM refinement, then Nick-sharpened 2026-06-06).** "Defer the operation" is only **regret-proof if the boundary is drawn at the irreversible seam.** Crypto-shredding can only destroy data *written encrypted under a per-scope key in the first place*, and the event log is immutable — so the now-or-never decision is **from what point sensitive categories (identity, person-linked presence) are envelope-encrypted-on-write under per-scope DEKs.** The crypto owner-doc (M5-B/B1) **must pin two things, not one:**

- **(i) The at-rest posture for the event DB itself** (not just the secret store): encrypted at rest at MVP, and *by what mechanism* — **SQLCipher** (whole-DB; an LTD-03/dependency decision) vs **application-level per-scope payload encryption**. With vanilla xerial sqlite-jdbc (no SQLCipher today) the app-level path is likely — and it is the **same machinery** that enables future per-category shred, so "encrypt sensitive PII at rest" (**INV-PD-03**) and "stay shreddable later" (**INV-PD-07**) collapse into one decision.
- **(ii) From what point** sensitive categories are envelope-encrypted-on-write.

**Decided posture (Nick, sharpening the earlier default).** Two separable things are being deferred and **only one is safe to defer:** the **shred operation** (key-destruction + erasure triggers/UI) has no MVP consumer — **defer freely**; but **encrypting sensitive PII categories on write is NOT the shred feature** — it is an **INV-PD-03 at-rest obligation in its own right** (identity/person-linked presence are the named sensitive PII; plaintext on a Pi's removable storage is a live privacy hole) *and* the preservation of future shreddability. Since the per-scope key-management **infrastructure is already MVP**, encrypting those categories on write *using those keys* is a **small increment, not new scope.** **Therefore: envelope-encrypt the sensitive PII categories on write under per-scope DEKs from MVP; defer only the shred operation.** The one genuine open variable is **Pi-4 write-path performance** on higher-frequency sensitive categories — resolve the exact category-by-category boundary with the **Lane D Pi-4 data** (the GC/GraalVM spikes carry an **AES-256-GCM write-path microbench**), and fall a category back to whole-install-reset-only **only where Pi-4 perf genuinely forces it — consciously, not by omission.** (This costs M6 a little more than the pure-defer default — write-path encryption for the sensitive categories — but it closes a permanent at-rest privacy gap on a trust-brand product; the maximally regret-proof line.) The M5-D interviews carry the verifiable-erasure question as the re-scope-up trigger for the *operation*.

**Sizing effect.** M6 sizes down to config pipeline + at-rest secret encryption + key-management infrastructure/seams — **not** a full operational crypto-shred subsystem. The crypto owner-doc (C6) is written to this scope and reconciled with Doc 06 + AMD-60.

## D3 — Non-Core floor: ADOPTED (option a)

Protected, **non-preemptable** website/docs floor in the window (M5-C); Core may not trade it away (P6). W23 proved "interleave when Core allows" resolves to "never"; M5's small Core size is the cheapest place to install the floor.

## D4 — Energy bet: ADOPTED (default)

Author the **regret-proof energy event *shape* now** (C9 — cheap, schema-irreversible); **commission the interviews near-term** (M5-D); **do NOT build energy *features* until the interviews return.** Shape/infrastructure now, features/operation on real demand — the same logic as D2.

## D5 — Language-deliberation interaction: ADOPTED (yes)

The GraalVM + GenZGC spikes and the energy interviews ride the window as **Lane D**. Explicit: the schema decisions (C8/C9/C10) are **regret-proof under both the stay-Java and go-Rust futures**, so **the window does not wait on the language call** — the spikes/interviews generate the evidence in parallel. The spikes double as LTD-01 reversal-criteria data.

## D6 — AMD-65 timing: ADOPTED

Author the `Expectation` codec **in the window (Lane A)**, lightweight block-track (P4). Context fresh; AMD-52 float-determinism precedent; slips to just-before-M9 with no harm if the window is tight.

## D7 — Verification-foundation (C4): ADOPTED

**Quick-scope it first**; lean toward a *small* dedicated property/fault-injection harness; leave time-series + hardware-in-the-loop to M12/M14 JIT. Do **NOT** rebuild the C3 doubles that already exist (`TestClock`/`SynchronousEventBus`/`NoRealIoExtension`/`InMemoryEventStore`).

## D8 — Process adoption (P1–P6): ADOPTED

Adopt **P1** (lane-tracking — this window depends on it), **P2** (consumer/pin survey), **P3** (ticked WUCP-Phase-2 closeout — retire the placeholder-`sed`), and **P6** (non-Core floor) into the PM skill / `coding-instruction-format.md` now; **P4/P5** as they apply.

---

## Guardrails (Nick)

Keep Lane A genuinely small; don't rebuild existing test doubles; don't build energy features yet; don't wait on the language decision; **hold P1 — if any lane sprawls past its charter, split it rather than let "M5" hide the size.**

## Status of the work these decisions authorize

- **W24 charter:** WRITTEN (`context/planning/weeks/2026-W24_jun08-jun14.md`).
- **First piece to execute:** M5-B / B1 — the M6 entry-gate (INV-PD-07 amendment + crypto owner-doc reconciled with Doc 06 + AMD-60 + the write-path-encryption boundary decision; AMD-66–71). NOT authored in this decision/closeout session — scheduled by the charter.
- **Open Risk logged (pm-handoff):** the INV-PD-07 amendment is pending authoring + full DOCS ratification; until ratified, INV-PD-07's text and the crypto Draft's phasing remain in contradiction (tracked, not silently resolved).
