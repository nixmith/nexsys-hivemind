<!--
file: context/handoff/2026-06-19_AMD-94_DOCS-Project_review_prompt.md
purpose: Dispatch-ready brief for a FRESH, independent DOCS-Project review of AMD-94 (the Doc 15 §6 currency amendment — rotate-DEK-on-restore + the 1-byte envelope version discriminator). FULL per-AMD review track (persisted shape + crypto behavioral contract + new invariants), NOT a shared block (constraint-enforcement §6 / P4). The reviewer pressure-tests the amendment adversarially and returns RATIFY-AS-IS / RATIFY-WITH-EDITS / REJECT; Nick ratifies after the return. The PM does NOT self-ratify.
audience: DOCS-Project independent reviewer (fresh conversation) + Nick (ratification co-sign)
state-type: session prompt (governance — amendment review)
status: READY — authored 2026-06-19 alongside AMD-94 (PROPOSED). Run as its own fresh conversation, independent of the AMD-94 authoring session and of the Doc 16 review.
reads (in order):
  - homesynapse-core-docs/design/amendments/AMD-94_Doc15-sec6_Rotate-DEK-on-Restore_and_Envelope-Version-Discriminator.md (THE OBJECT UNDER REVIEW — read in full)
  - homesynapse-core-docs/design/15-cryptographic-architecture.md (the LOCKED owner doc — §3.4 envelope + nonce/DEK, §4.1 schema, §5 contracts, §6 failure modes incl. the [BLOCKING-for-M6-impl] counter-nonce row, §8.1 ScopeKeyManager row, §13.4 testing, §16 summary). VERIFY each AMD-94 §2.4 staged edit's anchor exists verbatim in this doc.
  - homesynapse-core-docs/governance/Architecture_Invariants_v1.md (§35 AMD-86-INV-01 — the nonce corollary AMD-94 closes; §17 index + §18 matrix conventions; the AMD-NN-INV registration pattern; INV-GA-02 identifier permanence)
  - context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md PART A, A4 only (the ruling AMD-94 implements + its binding process caveat). NOTE: Part B is Doc-16 scope rationale — IRRELEVANT to this review; do not let it bleed in.
  - context/audits/2026-06-15_redteam_reversibility-audit.md (§3.1 F1 envelope discriminator + §3.5 F6 rotate=additive-retain-priors + §3.4 F4 chain-liveness — the technical pins AMD-94 encodes)
  - context/assessments/2026-06-15_Research_R-alpha_PM_Assessment.md (Problem 1 / restore-half; REC-216..223 rotate-binding; REC-235 boot invariant) — confirm AMD-94 faithfully encodes the disposition
  - homesynapse-core-docs/design/amendments/AMD-86_INV-PD-07_Crypto-Shred-MVP-Scope_and_INV-PD-03_At-Rest-Posture.md (the closest Doc-15/crypto amendment precedent — structure + the corollary it left open)
  - references/constraint-enforcement.md §6 (amendment track) + references/review-and-quality.md (review discipline)
-->

# DOCS-Project Review — AMD-94 (Doc 15 §6 Currency Amendment)

You are the **independent DOCS-Project reviewer**. AMD-94 was authored by the PM and is **PROPOSED**; **Doc 15 is LOCKED** and AMD-94 is the sanctioned re-open -> review -> ratify vehicle. Your job is to **pressure-test it adversarially** — you are rewarded for finding a real defect, an inaccurate edit specification, an unsound crypto claim, or a scope violation, **not** for confirming the PM's work. Return a verdict; **Nick ratifies** (you do not, and the PM does not self-ratify).

This is a **FULL per-AMD review** (persisted shape + crypto behavioral contract + new invariants -> not a shared block; constraint-enforcement §6). Apply full scrutiny.

## What AMD-94 binds (so you can test it against intent)

A4 (RULED by Nick 2026-06-18) -> AMD-94 binds **two** decisions and reserves the invariants they imply:

1. **Rotate-DEK-on-restore = the restore contract.** On restore, rotate the scope DEK = install an **additive new DEK version, retain priors** (no re-encrypt, no replace); the restored scope resumes counter-nonce counting from zero under the fresh version, so cross-restore (key, nonce) reuse is structurally impossible. Carry-high-water-mark demoted to a defense-in-depth **cross-check**. Boot invariant: refuse to encrypt until a fresh DEK is installed or the counter is proven ≥ all priors (REC-235). Closes **OR-M6-NONCE restore-half**.
2. **Reserve the 1-byte envelope version discriminator** (v1 = the current envelope) before the first encrypted write at app-bootstrap AB-4. Distinct from `dek_ref`'s key_version. The version **policy** is R-gamma-pending; AMD-94 reserves only the **slot**.

## Your review mandate — verify, don't assume

Work through each; cite the specific source line/section for every judgment (the review-and-quality discipline). Sort findings into RATIFY-AS-IS, or enumerated edits, or a REJECT with cause.

**A. Edit-spec accuracy (highest value — this is a Locked-doc amendment).** For **each** AMD-94 §2.4 staged edit (A–F, and G if retained), open Locked Doc 15 and confirm: (i) the cited anchor text exists **verbatim** (e.g., EDIT B quotes the §6 row's "rotate the DEK on restore, **or** carry the high-water mark in the backup" clause — is that the exact current text?); (ii) the replacement is internally consistent with the rest of Doc 15 (e.g., does EDIT C's new §5 contract contradict any existing §5 contract?); (iii) the section mapping is right (AMD-94 maps the brief's "§5 envelope/format" to §5 Contracts + §4.1 Schema — is that the correct reconciliation, or is there a better home?). **A staged edit that won't fold cleanly is a RATIFY-WITH-EDITS finding.**

**B. Crypto soundness of decision 1 (rotate-on-restore).**
- Is the **chain-safety** argument correct — that minting a new DEK version + writing a new `scope_keys` row + retaining priors touches **no** `stored_payload_bytes` and therefore cannot break `chain_hash` (§5)? Is re-wrapping/`scope_keys` genuinely not chain-covered?
- Is the **nonce-reuse-impossibility** argument airtight — does "resume from counter 0 under a never-before-used DEK version" truly preclude a repeated (key, nonce) pair across restore? Find a counterexample if one exists (e.g., two restores in quick succession; a restore that does NOT advance the version; a crash *during* rotation).
- Is the **boot invariant** (REC-235) fail-closed and complete as stated? Does AMD-94's "(a) fresh DEK installed OR (b) counter proven ≥ all priors" cover the gap, or is there a third state it misses?
- Is demoting high-water-mark to a **cross-check** (not removal) the right call, and is the "never the sole guarantee" framing correct?

**C. Crypto soundness of decision 2 (version discriminator).**
- Is `v1` = the current §3.4 envelope an accurate pin (AES-256-GCM, 96-bit counter nonce, per-scope DEK)?
- Is the **`dek_ref` key_version vs envelope/algorithm version** distinction stated correctly and unambiguously? (This is the exact conflation Track-3 F1 caught — confirm AMD-94 does not re-introduce it.)
- Is reserving the **slot** while deferring the **policy** to R-gamma a coherent boundary, or does the slot reservation smuggle in a policy decision that R-gamma should own? Specifically scrutinize the §2.2 **recorded safe-default** (1-byte prefix on the envelope + GCM-AAD binding): is presenting it as a default (R-gamma may supersede) appropriate, or does it pre-empt R-gamma? Is the alternative column encoding (§4.1 / EDIT D) correctly characterized as **not chain-covered today**?
- Is the **chain-liveness (F4)** caveat (§2.3) correctly scoped as non-blocking for slot reservation but load-bearing for the tamper-evidence *claim*?

**C2. R-alpha fidelity.** Does AMD-94 faithfully encode the R-alpha **Problem 1** disposition (rotate binds; (b) cross-check; REC-235), and does it correctly **exclude** R-alpha **Problem 2 / NEW-1** (the cause-discriminated read contract — which is A3/AB-2 + the crypto-shred WU, not this AMD)? Flag any contamination in either direction.

**D. Scope discipline.** AMD-94 claims to be currency/forward-compat, **not** a redesign. Confirm it does **not** silently: change the AEAD algorithm, alter the module graph / JPMS, bump `projectionVersion`, fold in F3 (one-nonce-construction-per-scope) or F13 (write-path fatal dir-fsync), or pull in the cause-discriminated read contract. If any of those leaked in, that is a finding.

**E. Invariant minting.** Are AMD-94-INV-01/02 well-formed, falsifiable, and non-redundant with existing invariants (especially AMD-86-INV-01 §35 — INV-01 *closes its corollary*; confirm it doesn't *duplicate* it)? Is the handling correct — **candidates** now, exact identifiers + §17/§18 registration + watermark bump **at ratification** (INV-GA-02), not now?

**F. Anti-requirements.** Confirm AMD-94 honors: never lead with commodity encryption (correctness framing, not a marketing claim); local-first inviolate (keys machine-local); no destructive forced migration (additive version + additive tag = the non-destructive path).

**G. The optional §8.1 rider (EDIT G / §2.5).** AMD-94 includes the `ScopeKeyManager`-row currency fix as an explicitly **strikeable** rider. Rule: **keep** (it is genuinely §3.8-adjacent and the snapshot says it rides the next Doc-15-touching amendment) or **strike** (keep AMD-94 minimal to the two A4 decisions). State your recommendation with reasoning.

## Return format

Write the return to `context/audits/2026-06-19_AMD-94_DOCS_Review_Return.md` with:
- **Verdict:** `RATIFY-AS-IS` | `RATIFY-WITH-EDITS` (enumerate each edit E-1, E-2, … with exact target + replacement) | `REJECT` (with the load-bearing defect).
- **Per-mandate findings** (A–G), each citing the specific Doc 15 / source line that grounds it.
- **Verification ledger:** for every §2.4 staged edit, PASS/FAIL on anchor-exists-verbatim + folds-cleanly.
- **The §8.1 rider recommendation** (keep / strike).
- A `!`-free commit message for Nick (`git commit -F`).

Do **not** edit Doc 15, the invariants register, or AMD-94 — this is a review; the fold happens at ratification, by Nick or at his direction. Flag anything you would change; do not change it.
