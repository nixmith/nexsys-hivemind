<!--
file: context/audits/2026-06-19_AMD-94_DOCS_Review_Return.md
purpose: Independent DOCS-Project review return for AMD-94 (Doc 15 §6 currency amendment — rotate-DEK-on-restore binding + the 1-byte envelope version discriminator). FULL per-AMD track (persisted shape + crypto behavioral contract + new invariants; constraint-enforcement §6). Adversarial pressure-test against the Locked Doc 15, the invariants register, decision A4, the Track-3 reversibility audit, and the R-alpha assessment. Returns a verdict; Nick ratifies (the reviewer does not, the PM does not self-ratify).
audience: Nick (ratification co-sign), PM (author of AMD-94), the AB-2/AB-4 coding sessions, the future backup/restore WU
state-type: review return (governance — amendment review)
status: COMPLETE 2026-06-19 — VERDICT: RATIFY-WITH-EDITS (2 enumerated edits E-1/E-2 + 1 optional E-3; §8.1 rider = KEEP). Run as a fresh, independent conversation per the dispatch brief.
ratification: **RATIFIED 2026-06-19** — Nick co-signed RATIFY-WITH-EDITS (independently verified E-1 + the EDIT B anchor). E-1 + E-2 folded into Locked Doc 15 (§3.4/§4.1/§5/§6/§13.4/§16); §8.1 rider KEPT; E-3 (optional §1 calibration) not taken. AMD-94-INV-01/02 registered (Architecture_Invariants_v1.md §48); watermark AMD-93→AMD-94 (165/48); §6 [BLOCKING-for-M6-impl] resolved; OR-M6-NONCE restore-half CLOSED; AB-4 un-gated. Cosmetic "eight"→"seven" anchor-count nit (flagged by Nick) corrected.
verdict: RATIFY-WITH-EDITS
reviewed:
  - homesynapse-core-docs/design/amendments/AMD-94_Doc15-sec6_Rotate-DEK-on-Restore_and_Envelope-Version-Discriminator.md (object under review — read in full)
  - homesynapse-core-docs/design/15-cryptographic-architecture.md (LOCKED owner doc — every §2.4 anchor verified verbatim)
  - homesynapse-core-docs/governance/Architecture_Invariants_v1.md (§35 AMD-86-INV-01; §17 index; §18 matrix; INV-GA-02 §15)
  - context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md (PART A, A4)
  - context/audits/2026-06-15_redteam_reversibility-audit.md (F1, F4/F5, F6, F14)
  - context/assessments/2026-06-15_Research_R-alpha_PM_Assessment.md (Problem 1; REC-216..223/235; Problem 2 exclusion)
  - homesynapse-core-docs/design/amendments/AMD-86_INV-PD-07_Crypto-Shred-MVP-Scope_and_INV-PD-03_At-Rest-Posture.md (precedent)
  - project-manager/references/constraint-enforcement.md §6 + review-and-quality.md
baseline: docs `32afb3f`; Doc 15 LOCKED (2026-06-07, AMD-86/87); on-disk watermark AMD-93 (invariants 163/47). No file edited by this review — flags only; the fold happens at ratification, by Nick or at his direction.
-->

# DOCS-Project Review Return — AMD-94 (Doc 15 §6 Currency Amendment)

## Verdict: RATIFY-WITH-EDITS

AMD-94 is sound in its two A4 decisions, accurate in its edit specifications, disciplined in scope, and correct in its invariant handling and anti-requirements. All seven §2.4 staged-edit anchors (A–F, plus G) exist **verbatim** in Locked Doc 15, and the brief's "§5 envelope/format" → **§5 Contracts + §4.1 Schema** reconciliation is the correct home. The chain-safety argument for rotate-on-restore is independently correct, and the nonce-reuse-impossibility argument is structurally sound. **The amendment does not RATIFY-AS-IS only because of one substantive wording defect (E-1) on a catastrophic-failure invariant, plus one minor internal inconsistency (E-2).** Both are zero-cost to fix while the contract is still on paper — exactly the class of pin the FULL per-AMD track exists to catch (the F6 "retain priors" precedent, audit §3.5:138-140).

Enumerated edits to fold **at ratification** (the reviewer applies nothing):

- **E-1 (substantive — boot-invariant robustness).** §2.1 / EDIT A / EDIT B / EDIT C / AMD-94-INV-01. The REC-235 boot invariant is stated as **"(a) a fresh DEK version is installed **OR** (b) the persisted counter is proven ≥ all prior nonces issued under the active DEK version"** — two co-equal alternatives evaluated at *every* boot. **Branch (b) is unsound after a restore.** A restore can roll the per-scope counter back to a value ≤ a nonce already issued, while simultaneously destroying the engine's evidence of the true high-water mark (the restored counter is not proof of the historical maximum). An implementation that restores, **skips rotation**, and evaluates (b) against the rolled-back counter will read "counter ≥ all priors I know about" as TRUE and resume encrypting under the **old** DEK version at a repeated counter — reproducing the exact OR-M6-NONCE restore-half catastrophe (R-alpha named failure: backup at N → live to N+k → restore to N → reuse N+1…N+k under the same DEK; assessment §"Why A":21). Binding rotate-on-restore (branch a) is the intended guard, but the invariant as written does **not require it post-restore**; it lets a careless restore path clear the gate through branch (b).
  - **Fix:** pin that **a restore is discharged ONLY by branch (a)** — installing a fresh additive DEK version is the restore-completion gate. Branch (b) is the **crash-recovery** branch, sound *only* because M6.3's counter is durable/fsync-ahead-of-return, so after a crash the persisted max equals the true max (Doc 15 §6 crash-half:243; assessment §"Verification ledger":30). State the mapping explicitly: **crash ⇒ (b) [persisted max is trustworthy]; restore ⇒ (a) [persisted max may be stale ⇒ rotate]**. Apply the same sharpening to EDIT B's boot-invariant clause (AMD-94:64), EDIT C's first contract paragraph (AMD-94:67), and AMD-94-INV-01 (AMD-94:126). This is the boot-invariant analogue of the F6 retain-priors pin: a plausible mis-implementation foreclosed at zero cost in the doc.

- **E-2 (minor — encoding-presumptive contract wording).** EDIT C contract 2 (AMD-94:68) and AMD-94-INV-02 (AMD-94:127) both read **"Every encrypted [at-rest] envelope carries a 1-byte version discriminator,"** which presupposes the **prefix-in-envelope** encoding. But EDIT D (AMD-94:70) and §2.2 (AMD-94:52) deliberately keep the **alternative `envelope_version` column** encoding open — where the byte is a separate column, **not** carried in the envelope and **not** chain-covered (Track-3 F14, audit:53: only the 13 metadata fields + `payload` are chain-covered). If R-gamma later selects the column, a frozen §5 contract that says "every encrypted **envelope** carries" the byte is literally falsified.
  - **Fix:** make the normative statements encoding-neutral, e.g. "Every encrypted at-rest **row is self-describing** via a 1-byte version discriminator — emitted as an envelope prefix (recommended, chain-covered) **or** an additive column; final placement R-gamma-pending." Zero semantic change; removes an internal contradiction between EDIT C/INV-02 and EDIT D inside a Locked-doc amendment. (INV-02's title "Encrypted at-rest envelopes are self-describing" is already the right framing — only the body needs the neutral phrasing.)

- **E-3 (optional — §1 calibration; non-load-bearing).** §1(2) (AMD-94:25) calls "shipping with no mechanism … the one-way door." Track-3 F1 explicitly **calibrated this down**: the agility *mechanism* is a **two-way** door — a later additive `payload_alg`/`envelope_version` column is possible, backfill-free, because the chain does not cover `payload_iv`/`dek_ref` (audit §3.1:91-92, "I will not overclaim it as irreversible"). The calibrated case for reserving now rests on the **asymmetry** (free now vs. discipline-dependent migration later) **plus** the chain-coverage advantage of the *prefix* encoding — not strict irreversibility. AMD-94's own §2.2/EDIT D record the column escape, so §1's stronger framing is in mild tension with the amendment's own body. The decision (reserve now) is correct either way; this is a framing-accuracy edit the author may take or leave. (§1 already half-calibrates by saying "worst-conditions migration," i.e. possible-but-bad — so this is polish, not a defect.)

**Nick ratifies. The reviewer does not ratify; the PM does not self-ratify.** On ratification, fold the §2.4 edits (A–F, G-kept) into Locked Doc 15 **with E-1/E-2 applied**, register AMD-94-INV-01/02 (final identifiers, INV-GA-02), and bump the watermark AMD-93 → AMD-94.

---

## Per-mandate findings

### A. Edit-spec accuracy (highest value — this is a Locked-doc amendment)

**All anchors exist verbatim; the section mapping is correct; one fold carries a minor consistency edit (E-2).** Detail per edit is in the Verification Ledger below; the load-bearing judgments:

- **EDIT B anchor — confirmed verbatim.** Doc 15 §6, the "**Counter-nonce reuse across crash/restore — [BLOCKING-for-M6-impl]**" row, Recovery cell, contains exactly "*(rotate the DEK on restore, or carry the high-water mark in the backup)*" (Doc 15:243). AMD-94 quotes it with an added bold on "**or**" (its own emphasis); the underlying text matches. The row title and the `[BLOCKING-for-M6-impl]` marker match (Doc 15:243). The replacement clause (AMD-94:64) is internally consistent with §5 and §6 and correctly resolves the marker on ratification.
- **Section mapping — correct.** The brief's "§5 envelope/format" maps, in the actual Locked doc, to **§5 "Contracts and Invariants"** (Doc 15:213) + **§4.1 "Event-store schema"** (Doc 15:164); the physical envelope (`payload`/`payload_iv`/`dek_ref`) is defined in §3.4 prose (Doc 15:132) and §4.1 schema (Doc 15:170-171). AMD-94 distributes its edits correctly: prose → §3.4 (EDIT A), schema → §4.1 (EDIT D), contract → §5 (EDIT C). **No better home exists** — the three-way split is the right reconciliation.
- **EDIT C internal consistency — one minor defect (E-2).** EDIT C's two new contracts do not contradict any existing §5 contract (Doc 15:215-229): contract 1 (no re-encrypt, retain priors) is consistent with "encrypting a scope … does not alter any stored bytes" (Doc 15:215); contract 2 (version slot) is consistent with the chain-covers-stored-bytes contract (Doc 15:215). The only issue is the **EDIT C-2 ↔ EDIT D encoding mismatch** captured in E-2.
- **EDIT A placement — clean.** The §3.4 append-anchor "DEK rotation (counter/time threshold) is the post-MVP automation; at MVP a scope uses one DEK with counter nonces." is the **last sentence of §3.4** (Doc 15:132), so appending the rotate-on-restore paragraph after it folds at the paragraph end without disturbing surrounding text.

### B. Crypto soundness of decision 1 (rotate-on-restore)

- **Chain-safety — CORRECT (independently verified).** `chain_hash[n] = SHA-256(chain_hash[n-1] ‖ canonical_metadata_bytes[n] ‖ stored_payload_bytes[n])` (Doc 15 §3.3:126), where `stored_payload_bytes` is "whatever the `payload` column holds." Minting a new DEK version writes a row to the **`scope_keys`** table, which is a separate table and **not** an input to `chain_hash`; it mutates no existing event row's metadata or `stored_payload_bytes`. Future writes are ordinary appended events, chained normally. Therefore rotation cannot break the chain. The audit reaches the same conclusion independently and harder: "even *re-wrapping the DEK* (changing `scope_keys.encrypted_dek`) touches only the `scope_keys` table, which is **not chain-covered** at all" (audit §3.5:136). **`scope_keys` is genuinely not chain-covered** (confirmed against §3.3's exclusive input list). **PASS.**
- **Nonce-reuse-impossibility — SOUND in the bound contract.** GCM's uniqueness obligation is on the **(key, nonce) pair** (NIST SP 800-38D §8). A fresh, never-used DEK version has an untouched nonce space, so `(freshDEK, k)` is a new pair for every counter `k`, including the low values reused-from-zero under the new version. "Resume from counter 0 under a never-before-used DEK version" therefore precludes a repeated pair (AMD-94:38). Counterexample hunt:
  - *Two restores in quick succession:* safe **provided each restore mints a strictly additive version** (`prior max + 1`). The structural backstop is the **`scope_keys` PRIMARY KEY `(scope_id, key_version)`** (Doc 15:191): two restores that both compute `N+1` collide on the PK and the second insert fails, forcing `N+2`. AMD-94 relies on this implicitly but does not state it — see the strengthening note below.
  - *Restore that does NOT advance the version:* this is the hazard, and it is where **E-1** bites. If rotation is skipped, safety depends entirely on the boot invariant refusing to encrypt — and branch (b) can be **falsely satisfied** against a rolled-back counter (E-1). With E-1 applied (restore ⇒ branch (a) only), this counterexample is closed.
  - *Crash during rotation:* reduces to the same dependency. If the `N+1` insert committed pre-crash, reboot resumes under `N+1` (M6.3 re-inits the counter from the durable max) — safe. If it did **not** commit, reboot must treat the restore as incomplete and refuse to encrypt until rotation completes — which again requires E-1's "restore ⇒ branch (a)" gating rather than branch (b) clearing on an ambiguous counter.
  - **Strengthening (fold into E-1 or note separately):** state that version monotonicity across successive/concurrent restores is enforced by the `(scope_id, key_version)` PK (Doc 15:191), so "prior max + 1" cannot silently collide two distinct DEKs onto one version.
- **Boot invariant (REC-235) — INCOMPLETE as stated → E-1.** The "(a) OR (b)" framing is not fail-closed against a restore that rolls back the counter branch (b) inspects. The third state it misses is **post-restore-without-rotation evaluating branch (b) on diminished knowledge.** See E-1 for the fix. Note this is a *sharpening of an already-sound-in-intent contract* (the amendment clearly intends restore ⇒ rotate), not a REJECT-level hole — the word "proven" can be read to save it, but a Locked-doc crypto invariant must not depend on an implementer reading "proven" the strict way.
- **High-water-mark demotion — CORRECT.** Keeping carry-high-water-mark as a defense-in-depth cross-check ("assert resumed counter ≥ carried max … never the sole guarantee," AMD-94:39) rather than removing it is the right call: alone it is the named-unsafe option (R-alpha; assessment §Disposition:43), but as a cross-check it can catch a rotation that failed to occur, at no cost. The "never the sole guarantee" framing is exactly correct — and is itself the reason branch (a) must bind (a restore can roll back a *carried* high-water mark too, so it cannot be load-bearing). **PASS.**

### C. Crypto soundness of decision 2 (version discriminator)

- **`v1` pin — ACCURATE.** AMD-94 pins `v1` = AES-256-GCM, 96-bit counter nonce, per-scope DEK (AMD-94:48). Doc 15 §3.4 specifies exactly this: "a **DEK** (256-bit) encrypts that scope's event payloads with AES-256-GCM … `payload_iv` = the 96-bit GCM nonce … counter-based deterministic 96-bit nonces per scope" (Doc 15:132). **PASS.**
- **`dek_ref` key_version vs envelope/algorithm version — STATED CORRECTLY; the F1 conflation is NOT re-introduced.** AMD-94 keeps the two axes orthogonal and explicit: `dek_ref`'s `key_version` selects the *key* (and is what §2.1 increments on restore); the new discriminator identifies the *envelope/algorithm* version (AMD-94:49, :62, INV-02:127). This is precisely the distinction Track-3 F1 caught as conflated in the pre-amendment design ("`dek_ref` … is a *key* version, never an *algorithm* version"; audit §3.1:82). AMD-94 does not re-conflate them. **PASS.**
- **Slot-vs-policy boundary — COHERENT; the §2.2 safe-default does not pre-empt R-gamma.** Reserving the slot + pinning `v1` while deferring the registry/downgrade/AAD-binding policy to R-gamma (AMD-94:51) is a clean boundary. The recorded safe-default (1-byte prefix + GCM-AAD binding, AMD-94:52) is explicitly framed as supersedable ("if R-gamma returns a stronger policy before AB-4 it supersedes this default") and exists only to keep AB-4 unblocked if R-gamma is late — appropriate. The AAD-binding recommendation edges toward policy (it is a downgrade-resistance mechanism R-gamma should own), but AMD-94 correctly fences it as a *default R-gamma may refine*, not a decision gate. **Acceptable.**
- **Column encoding "not chain-covered today" — CORRECTLY CHARACTERIZED.** EDIT D labels the additive-column option "not chain-covered today" (AMD-94:70). Grounded: the chain covers only the 13 canonical metadata fields + `payload` (Doc 15 §3.3:126); `payload_iv`/`dek_ref` are explicitly *not* chain-covered (Track-3 F14, audit:53). **PASS** — and this is the precise fact E-2 turns on (the contract must not assert "carried in the envelope" if the column is later chosen).
- **Chain-liveness (F4) caveat — CORRECTLY SCOPED.** §2.3 (AMD-94:56) scopes F4 as non-blocking for slot reservation / `v1` pinning (the byte's *existence* is independent of chain liveness) but load-bearing for the *tamper-evidence claim* of the recommended encoding. Grounded: `chain_hash` is `ZERO_HASH`/uncomputed at HEAD (Track-3 F4/F15, audit:54, :69; Doc 15:194 "`SqliteEventStore` currently binds the `ZERO_HASH` constant"). **PASS.**

### C2. R-alpha fidelity

- **Problem 1 — faithfully encoded.** AMD-94 binds rotate-DEK-on-restore as the contract, demotes carry-high-water-mark to a cross-check, and carries REC-235 as the boot invariant (AMD-94:38-40) — matching the R-alpha disposition exactly (assessment §Disposition:43, REC routing:57: "REC-216–223, REC-235 → app-bootstrap milestone … closes OR-M6-NONCE restore-half"). The "rotate = additive new DEK version, retain priors" pin matches Track-3 F6 (audit §3.5:138-140) and A4 (decision record:35). **PASS** (subject to E-1's sharpening of how REC-235 is stated).
- **Problem 2 / NEW-1 — correctly EXCLUDED, both directions.** AMD-94 explicitly routes the cause-discriminated read contract out of scope to A3 → AB-2 (fail-closed) + the crypto-shred WU (degrade half) (AMD-94:93, :119) — matching the assessment's routing (Problem 2 → AB-2 fail-closed + crypto-shred degrade; assessment:52, :58-59). The one cross-reference it keeps — that the shred tombstone + read-side rule key on `(scope, key_version)` "consistent with §2.1's additive versioning" — is explicitly labeled **"carried, not bound here"** (AMD-94:93), which is correct and matches the Track-3 F5 granularity pin (audit §3.4:125). **No contamination in either direction. PASS.**

### D. Scope discipline

**No silent redesign; every scope fence holds.** Verified against the §6 non-goals (AMD-94:116-122) and the staged edits:

- **AEAD algorithm — unchanged.** "AES-256-GCM stays … `v1` = today's envelope" (AMD-94:116). No edit touches the cipher.
- **Module graph / JPMS — unchanged.** "Module-info UNCHANGED" (AMD-94:121, :129). No edit touches a `module-info`. (EDIT G *describes* the §3.8 seam more accurately but adds no edge — see §G.)
- **`projectionVersion` — not bumped.** "NO `projectionVersion` change" (AMD-94:121); consistent with Track-3 F17 (additive columns, backfill-free; audit:56).
- **F3 (one-nonce-construction-per-scope) and F13 (write-path fatal dir-fsync) — correctly excluded** as sibling AB-4 envelope-finalization items, not A4 decisions (AMD-94:15, :101, :120). Confirmed these are app-bootstrap deliverables in the audit (F3 §3.3, F13:52), not folded here. The boot invariant (counter monotonicity / rotation) is a distinct axis from F3 (random-IV vs counter *construction*), so no leak.
- **Cause-discriminated read contract — excluded** (see C2). **PASS on all fences.**

### E. Invariant minting

- **AMD-94-INV-01 — well-formed, falsifiable, non-redundant.** It is testable (does a restore install an additive version with priors retained? is (key,nonce) reuse possible across restore?) and it **closes the corollary** of AMD-86-INV-01 rather than duplicating it. AMD-86-INV-01's main statement is "encrypt-on-write is irreversible; the shred operation is deferrable" (register §35:1484-1486) — a different proposition; its `[BLOCKING-for-M6-impl]` corollary is "the per-scope GCM counter-nonce must be durable and strictly monotonic across crash **AND** restore" (register §35:1486). The crash-half is discharged by M6.3; AMD-94-INV-01 discharges the **restore-half** by binding rotate-on-restore (AMD-94:126). It picks option (a) from the corollary's own menu and makes it structural — non-redundant. **PASS** (the INV-01 text inherits E-1's sharpening).
- **AMD-94-INV-02 — well-formed, falsifiable, non-redundant** (subject to E-2's encoding-neutral phrasing). Testable (does every encrypted row round-trip the discriminator? does `v1` decode as the §3.4 envelope?); no existing invariant asserts envelope self-description.
- **Candidate handling — CORRECT per INV-GA-02.** AMD-94 treats both as **candidates** now, with exact identifiers + §17 index + §18 matrix registration + watermark bump deferred to **ratification** (AMD-94:128) — matching INV-GA-02 (identifiers permanent/non-reusable once assigned; register §15:793-795) and the established registration pattern (§35 AMD-86, §36 AMD-87, §37-41 the AMD-66-71 block all register a new `AMD-NN-INV` § + §17 + §18 row at ratification; register:1482, :1502). The header's use of INV-GA-02 to justify the **AMD number** (AMD-94:8) is also sanctioned — constraint-enforcement §2 confirms INV-GA-02 "also governs retired-AMD-number reuse" (constraint-enforcement:60). **PASS.**

### F. Anti-requirements

All three honored (AMD-94:122, :55, :15):

- **Never lead with commodity encryption.** AMD-94 frames the work as correctness / forward-compat, explicitly "not a marketing claim" (AMD-94:122), and §1 grounds it in the immutable-log irreversibility, not a security boast. Consistent with the Doc 15 honest-threat-model posture (Doc 15 §3.5:140, §12:350). **PASS.**
- **Local-first inviolate (keys machine-local).** AMD-94 changes no root-key source; keys stay machine-local (AMD-94:122), consistent with Doc 15 §3.5 (Doc 15:138). The version byte and the additive DEK versioning are on-device constructs. **PASS.**
- **No destructive forced migration.** The additive new DEK version (retain priors, no re-encrypt, no replace) + the additive version tag are the explicit non-destructive path (AMD-94:118); the immutable log is never rewritten; the column option, if taken, is an additive `ALTER TABLE ADD COLUMN` backfill-free per the AMD-37 precedent (Doc 15:194). **PASS.**

### G. The optional §8.1 rider (EDIT G / §2.5) — recommendation: **KEEP**

The nit is **real and verified**, not cosmetic. Doc 15 §8.1's `ScopeKeyManager` row reads "…own `scope_keys`, **implement `PayloadCipher`**, (post-MVP) destroy KEK | config (impl of the persistence seam)" (Doc 15:280). This **directly contradicts** the E2-folded §3.8, which states the config-resident `ScopeKeyManager` "**exposes its own `encrypt`/`decrypt` surface but does *not* implement the persistence-exported `PayloadCipher` type directly** … the **composition root `com.homesynapse.app`** … wraps it in a thin `PayloadCipher` adapter" (Doc 15:156). The staleness is **traceable**: the Doc 15 Lock folded E2 into §3.8 ("§3.8 `PayloadCipher` wiring stated precisely," Doc 15:4; AMD-86 status:5) but the §8.1 *table row* was not updated to match — leaving exactly the contradiction EDIT G targets.

**Recommendation: KEEP**, for four reasons: (1) it closes a genuine internal contradiction in a Locked doc (§8.1:280 vs §3.8:156) — documentation debt that compounds if always deferred; (2) the PROJECT_SNAPSHOT earmarked this fix to "ride the next Doc-15-touching amendment," and AMD-94 is exactly that (AMD-94:82); (3) it is §3.8/seam-adjacent — rotate-on-restore and the version byte both operate through the `PayloadCipher` seam the row describes (AMD-94:82); (4) it is pure currency, introduces no new decision, and is clearly fenced (AMD-94:86).

The legitimate **strike** rationale (keep AMD-94 minimal to the two A4 decisions; currency nits ideally ride a dedicated currency amendment so the ratification record reads cleanly) is acknowledged but outweighed: the rider's explicit fencing already preserves auditability. **Fold it as clearly-attributed currency, distinct from the A4 decisions** (e.g., a separate §16 changelog/note line so a future reader sees *why* §8.1 changed under a rotate-on-restore amendment). EDIT G anchor confirmed verbatim (Doc 15:280).

---

## Verification ledger — §2.4 staged edits

| Edit | Target (Locked Doc 15) | Anchor exists verbatim | Folds cleanly | Notes |
|---|---|---|---|---|
| **A** | §3.4 — append after "DEK rotation … one DEK with counter nonces." (Doc 15:132) + envelope-def "An encrypted event has `payload`…`dek_ref` = `scope_id:key_version`." (Doc 15:132) | **PASS** | **PASS w/ E-1, E-2** | Append-anchor is §3.4's last sentence (clean paragraph-end fold). Boot-invariant text inherits E-1; the version-byte note inherits E-2's encoding-neutral phrasing. |
| **B** | §6 — "Counter-nonce reuse across crash/restore — [BLOCKING-for-M6-impl]" row, Recovery cell; clause "(rotate the DEK on restore, or carry the high-water mark in the backup)" (Doc 15:243) | **PASS** | **PASS w/ E-1** | Row title, marker, and clause all verbatim. Replacement resolves the marker + flips OR-M6-NONCE restore-half CLOSED on ratification. Boot-invariant clause inherits E-1. |
| **C** | §5 "Contracts and Invariants" — add 2 contract paragraphs (Doc 15:213) | **PASS** (section) | **PASS w/ E-1, E-2** | No contradiction with existing §5 contracts (Doc 15:215-229). Contract 1 inherits E-1; contract 2 inherits E-2 (encoding-neutral). |
| **D** | §4.1 "Event-store schema" — record the discriminator reservation; prefix (chain-covered) **or** additive `envelope_version` column (not chain-covered) (Doc 15:164-196) | **PASS** | **PASS** | Column option correctly characterized "not chain-covered today" (F14, audit:53). AMD-37 additive-no-backfill precedent accurate (Doc 15:194). No migration ships (empty corpus until AB-4). |
| **E** | §13.4 — extend the `[BLOCKING-for-M6-impl]` restore assertion "a restore-from-backup cannot resume a scope at an already-used counter under the same DEK" (Doc 15:362) | **PASS** | **PASS** | Existing assertion present + marked. Extension (additive version, priors decrypt, no (key,nonce) repeat, boot invariant, `v1` round-trip) is consistent; the boot-invariant test should assert E-1's restore ⇒ branch (a). |
| **F** | §16 "Summary of Key Decisions" — add 2 rows (Doc 15:382, table cols Decision\|Choice\|Rationale\|Section) | **PASS** | **PASS** | 4-column format matches. Section refs (§3.4/§6 and §3.4/§5) correct. |
| **G** | §8.1 — `ScopeKeyManager` row "…own `scope_keys`, implement `PayloadCipher`, (post-MVP) destroy KEK | config (impl of the persistence seam)" (Doc 15:280) | **PASS** | **PASS (KEEP)** | Real contradiction vs §3.8:156 (AMD-86-E2 leftover). Recommend KEEP; fold as attributed currency. |

**Ledger summary:** 7/7 staged edits PASS anchor-exists-verbatim. Folds-cleanly: D, E, F, G fold as-is; A, B, C fold with E-1 (and A, C with E-2) applied. No FAIL on any anchor. No anchor is fabricated, mis-quoted, or mis-located.

---

## Track classification (confirmed)

AMD-94's self-classification as **FULL per-AMD, not a shared block** is correct: it touches a persisted shape (the envelope version byte), a crypto behavioral contract (the restore key-management contract), and mints new invariants — each independently triggering the full track (constraint-enforcement §6:208; review-and-quality §6 P4:219). The independent DOCS review (this return) is the required depth.

---

## Commit message for Nick (`git commit -F`)

```
docs(review): AMD-94 DOCS-Project review return — RATIFY-WITH-EDITS

Independent full per-AMD review of AMD-94 (Doc 15 section-6 currency:
rotate-DEK-on-restore binding + the 1-byte envelope version discriminator).
Verdict RATIFY-WITH-EDITS. The two A4 decisions are soundly encoded and
chain-safe; all seven section-2.4 staged-edit anchors (A-G) exist verbatim in
Locked Doc 15; scope discipline, invariant minting (AMD-94-INV-01/02), and the
anti-requirements all hold. Problem 1 faithfully encoded; Problem 2/NEW-1
correctly excluded.

E-1 (substantive): the REC-235 boot invariant states "(a) fresh DEK installed
OR (b) counter proven >= all priors" as co-equal at every boot. Branch (b) is
unsound post-restore -- a restore can roll the counter back below a used nonce
while erasing the engine's evidence of the true high-water mark, so a restore
that skips rotation could clear the gate via (b) and reuse (key,nonce) under
the old DEK (the OR-M6-NONCE restore-half catastrophe). Pin: a restore is
discharged ONLY by branch (a) rotation; (b) is the crash-recovery branch,
sound only because M6.3's counter is durable. Mirrors the F6 retain-priors pin.
Apply to section 2.1 / EDIT A / EDIT B / EDIT C / AMD-94-INV-01.

E-2 (minor): the section-5 contract and AMD-94-INV-02 say "every encrypted
envelope carries" the discriminator, presupposing the prefix encoding, while
EDIT D keeps the additive-column option (not in the envelope, not chain-
covered) open. Make the normative statements encoding-neutral so the frozen
contract does not foreclose the column placement R-gamma may pick.

E-3 (optional): section-1 calls the missing mechanism a "one-way door"; Track-3
F1 calibrated it as two-way (a later non-chain-covered column works). Align the
framing with F1; the reserve-now decision is unchanged.

section-8.1 ScopeKeyManager rider (EDIT G): KEEP -- a real internal
contradiction (section 8.1 "implement PayloadCipher" vs the AMD-86-E2-folded
section 3.8 "does NOT implement it directly"), pure currency, earmarked to ride
the next Doc-15 touch; fold as attributed currency distinct from the A4
decisions.

Nick ratifies (the reviewer does not, the PM does not self-ratify). On
ratification: fold A-F (G kept) with E-1/E-2 applied, resolve the section-6
[BLOCKING-for-M6-impl] marker, flip OR-M6-NONCE restore-half CLOSED, register
AMD-94-INV-01/02 (INV-GA-02), bump the watermark AMD-93 -> AMD-94. No Doc 15,
invariants-register, or AMD-94 edits were made in this review.

File: nexsys-hivemind/context/audits/2026-06-19_AMD-94_DOCS_Review_Return.md
```
