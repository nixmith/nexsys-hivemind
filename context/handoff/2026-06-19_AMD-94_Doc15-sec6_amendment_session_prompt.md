<!--
file: context/handoff/2026-06-19_AMD-94_Doc15-sec6_amendment_session_prompt.md
purpose: Dispatch-ready brief for a FRESH Cowork governance session that AUTHORS AMD-94 — the Doc 15 §6 currency amendment ruled by Nick at A4 (2026-06-18): bind rotate-DEK-on-restore + reserve the 1-byte envelope version discriminator. Author the AMD (PROPOSED) + its DOCS-Project review prompt. Nick ratifies. Doc 15 is LOCKED — the AMD is the vehicle; no silent edit.
audience: PM/Architect (a FRESH Cowork conversation, nexsys-project-manager skill — governance/amendment authoring), Nick (ratification co-sign)
state-type: session prompt (governance — amendment authoring)
status: READY — authored 2026-06-19; **currency-refreshed 2026-06-19 post-AB-3**. **AB-3 is DONE (core `60d50ce`, gate-verified GREEN), so AMD-94 is now the immediate critical-path prerequisite for the next Coder slot** — it gates **AB-4** (cipher activation + the F1 envelope-finalization gate), which lands with AB-1+AB-2 as the Seam-1 go-live. No longer "behind AB-3." Run as its own fresh Cowork conversation (independent of the Doc 16 review session — see the note in the reads); it parallels the AB-1+AB-2+AB-4 instruction authoring and unblocks AB-4.
baseline: core `60d50ce` (AB-3 landed GREEN; substantive HEAD past `beb4bc3`) / docs `32afb3f` / hivemind `bcd7376` ; watermark AMD-93 → this amendment mints AMD-94 ; Doc 15 LOCKED (2026-06-07, AMD-86/87) ; M6 + M7.1 + AB-3 COMPLETE. Confirm at preflight.
reads (in order):
  - context/process/cowork-environment-model.md (FIRST — path duality, the truncated-tail mount artifact, the §5 bulk-edit-source rule: governance-class files edited HOST-side or git-object-sourced, never from a VM worktree read; the §4 index.lock hazard)
  - context/status/PROJECT_SNAPSHOT.md (state; the open Doc-15 §8.1 ScopeKeyManager-row currency nit that may ride this amendment)
  - context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md — **A4 (the ruling this amendment implements) + its binding process caveat.** (You will read this whole record; that is expected for AMD-94. NOTE: this is why the AMD-94 session must be SEPARATE from the independent Doc 16 review — this record's Part B contains the Doc-16 scope rationale, which would contaminate that review's independence.)
  - homesynapse-core-docs/design/15-*.md (the LOCKED Cryptographic Architecture — §3.4 counter-nonce per scope, §6 Failure Modes incl. counter-nonce reuse across crash/restore, §3.8 the app-hosted PayloadCipher adapter, §5 envelope/format, §13.4 testing, §16 summary) + governance/Architecture_Invariants_v1.md (§35 AMD-86-INV-01 the nonce corollary; the §17 index + §18 matrix; the watermark/numbering convention) + the AMD-88..93 files as the authoring template (frontmatter, §7 invariant block, §9/§10 status)
  - context/planning/2026-06-15_app-bootstrap_charter.md (AB-4 envelope-finalization gate F1/F2/F3; the entry-gate row for the §6 amendment) + the Track-3 reversibility-audit (F1 version discriminator, F6 rotate=additive-new-DEK-version) + the R-α PM assessment (REC-234 fail-closed-not-degrade; REC-235 rotate-DEK boot invariant; Problem 1 = the restore-half this closes)
  - references/constraint-enforcement.md §6 (amendment track — this touches a PERSISTED SHAPE + a crypto behavioral contract → a FULL independent DOCS-Project review, not a shared block) + references/review-and-quality.md
-->

# Session Brief — Author AMD-94 (Doc 15 §6 currency amendment)

PM/Architect session (**nexsys-project-manager**, governance/amendment authoring). Read `context/process/cowork-environment-model.md` FIRST, then run the freshness preflight. **Doc 15 is LOCKED** — AMD-94 is the formal re-open → DOCS review → ratify vehicle (A4's binding process caveat); **never a silent edit to the Locked doc.** This session AUTHORS the amendment (PROPOSED) + its DOCS-Project review prompt; **Nick ratifies** (you do not ratify in-session).

**Step 0:** preflight; reconcile HEADs; confirm watermark is **AMD-93** on disk (AMD-94 is the next number; do not reuse a reserved slot). Governance-class edits are HOST-side / git-object-sourced only (env-model §5); prefer `git --no-optional-locks` for read-only state.

## What AMD-94 binds (from A4, RULED 2026-06-18)

Author AMD-94 as a Doc 15 §6 (+ §3.4) currency amendment with two bound decisions and the invariant(s) they imply:

1. **Rotate-DEK-on-restore = the restore contract.** On restore, **rotate the scope DEK = install an additive NEW DEK version and RETAIN priors** (Track-3 F6), so pre-restore rows stay readable under their original DEK version. **Demote carry-the-high-water-mark to a defense-in-depth cross-check** (assert the resumed counter ≥ any carried max; never the sole guarantee). This **closes OR-M6-NONCE restore-half** (R-α Problem 1) on ratification — the catastrophic (key, nonce) reuse across restore is prevented because a restored scope never resumes counting under a DEK version already used. Carry the **boot invariant** (R-α REC-235): refuse to encrypt in a scope until a fresh DEK is installed OR the persisted counter is proven ≥ all prior nonces.
2. **Reserve the 1-byte envelope version discriminator now.** Add a 1-byte algorithm/version tag to the AEAD envelope, **v1 = the current envelope** — irreversible after the first encrypted write (which happens at AB-4/app-bootstrap), so the slot must exist before then. **R-γ later refines the version POLICY, not whether the slot exists** (R-γ is in flight; do not block on it — record that the policy is R-γ-pending).

**Scope discipline:** AMD-94 is a currency/forward-compat amendment, NOT a redesign. Record it into Doc 15 §3.4 (nonce/DEK) + §6 (failure modes) + §5 (envelope format, the version byte) per the AMD-88..93 mechanics. Mint the invariant(s) (e.g., AMD-94-INV-01 rotate-on-restore-prevents-nonce-reuse; AMD-94-INV-02 envelope-version-byte-present) — exact identifiers assigned at ratification (INV-GA-02). The optional Doc 15 §8.1 `ScopeKeyManager`-row currency nit (snapshot Open flags) MAY ride this amendment if it is genuinely §6-adjacent — else leave it.

## Anti-requirements (bind)
Doc 15 is LOCKED — the AMD is the only sanctioned vehicle; no silent edit. **Never lead with commodity encryption** (this is correctness/forward-compat, not a marketing claim). Local-first inviolate (keys stay machine-local). No destructive forced migration — the version byte + additive DEK versioning are explicitly the non-destructive path.

## Escalations to Nick
- **Ratification co-sign** — AMD-94 is authored PROPOSED; Nick ratifies after the DOCS-Project review. Do not self-ratify.
- **Any new invariant** minted (AMD-94-INV-*) — flagged for Nick at ratification (skill §4); registered into Architecture_Invariants §17/§18 + watermark bump AMD-93→AMD-94 at ratification, NOT now.
- The R-γ version-POLICY refinement is a separate, later input — note it as pending; AMD-94 reserves only the slot.

## Done-when
**AMD-94 is on disk PROPOSED** (`homesynapse-core-docs/design/amendments/AMD-94_*.md`) following the AMD-88..93 template (frontmatter status PROPOSED; §7 invariant block; the §3.4/§5/§6 Doc-15 edit specifications staged but NOT folded into the Locked doc until ratification); **the AMD-94 DOCS-Project review prompt is authored + dispatch-ready** (full independent review per constraint-enforcement §6 — persisted shape + crypto contract). Update the backlog (AB-4 row: the §6 amendment moves PROPOSED) + snapshot Open flags (OR-M6-NONCE restore-half → "PROPOSED-closes-on-AMD-94-ratify"); run the WUCP drift check; hand over a bang-free commit message (`git commit -F`). **NOT ratified, NOT folded into Locked Doc 15** — that is Nick's step after the DOCS review.
