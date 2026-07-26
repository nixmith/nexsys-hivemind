<!--
file: context/instructions/2026-06-15_Research_R-gamma_Crypto-Agility_Envelope-Versioning_CHALLENGE_Brief.md
purpose: DOCS-Project ADVERSARIAL CHALLENGE brief — R-γ. Independent web-grounded pressure-test of ONE decision the internal red-team flagged as a one-way door it cannot self-validate: the at-rest encryption envelope ships with NO algorithm/version discriminator (AES-256-GCM implicitly hardcoded) and the encrypted corpus begins accumulating at app-bootstrap on an immutable, hash-chained log. The reviewer's job is to try to BREAK the internal verdict (REVERSE-NOW-WHILE-CHEAP: add a 1-byte tag) — either by showing the hedge is unnecessary, or by showing it is insufficient. Reward = finding the flaw.
audience: DOCS-Project researcher (fresh conversation, web search required) → PM serialized assessment on return
state-type: research brief — adversarial challenge (READY TO DISPATCH — Nick veto-or-default)
status: AUTHORED 2026-06-15 (Track-3 red-team). Dispatch BEFORE the Track-2 app-bootstrap charter finalizes the envelope.
routing: DOCS Project (design/architecture). Code-empirical sub-questions are flagged and routed to a CORE spike, NOT answered here.
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4; M6.3 at-rest payload encryption LANDED GREEN but INERT — main() is a stub, zero encrypted rows exist yet); docs watermark AMD-93; Doc 15 LOCKED.
consumes: Track-3 reversibility audit (2026-06-15_redteam_reversibility-audit.md) finding F1; the R-α return + assessment (which deferred GCM-SIV to Tier-2 but never raised the agility MECHANISM).
-->

# RESEARCH BRIEF (ADVERSARIAL CHALLENGE): R-γ — Crypto-Agility & Envelope Versioning for an Immutable, Hash-Chained, Per-Scope-Encrypted Store

**Register:** engineering / systems-design (DOCS Project). Web search required. Connector-blind is acceptable — declare it and list the gaps.

**This is a CHALLENGE brief. Your job is to BREAK an internal verdict, not confirm it.** The Track-3 red-team reached a verdict it is *structurally unable to validate from the inside* — because the same project designed the envelope under test. **You are rewarded for finding the flaw in that verdict.** The flaw can run either direction, and both are valuable returns:
- **"The hedge is UNNECESSARY"** — show that shipping a non-self-describing AES-256-GCM envelope is the defensible, common, lower-regret choice, and that the implicit-version retrofit is a genuinely safe and cheap escape, so adding a discriminator now is scope-creep / YAGNI.
- **"The hedge is INSUFFICIENT"** — show that a 1-byte tag does not actually buy agility on *this* substrate (immutable + hash-chained), and that real agility requires more (e.g., the discriminator must be chain-covered, or the whole key-version/dek_ref contract needs reshaping), so the internal verdict under-scopes the problem.

A return that simply agrees with the internal verdict ("yes, add a version byte, best practice") **without having tried to defeat it** is a low-value return. Take a position *against* the internal reasoning and see if it survives.

**The load-bearing deliverable is the §4 disposition: a single position — ADD-NOW / SAFE-TO-DEFER / NEEDS-MORE-THAN-A-TAG — defensible against HomeSynapse's actual constraints (immutable append-only log, SHA-256 hash chain over stored bytes, per-scope DEKs with counter nonces, an empty corpus today that starts filling at app-bootstrap).** A generic "crypto agility is good practice" with no position against those constraints is a non-finding.

---

## 0. Quote-back gate [DO THIS FIRST]

Before any research, echo the following **verbatim** in your return's §0, then state in one line per item that you have read it and will hold it as ground (not re-litigate it). This proves you are gap-relative to the real envelope, not working from a generic crypto-agility prior. Do **not** paraphrase — copy, then react.

**QB-1 — the envelope, source-verified at HEAD `1eddd9a` (V005 migration + `EncryptedPayload.java`):**
> An encrypted event has `payload` = ciphertext (GCM tag appended), `payload_iv` = the 96-bit GCM nonce (`BLOB(12)`), `dek_ref` = `"scope_id:key_version"` (`TEXT`). Unencrypted events: `payload` = plaintext JSON, `payload_iv`/`dek_ref` NULL. The Java record is `EncryptedPayload(byte[] ciphertext, byte[] iv, int keyVersion)`. There is no algorithm or envelope-version field in the payload columns or in the `scope_keys` table.

**QB-2 — Doc 15 §3.3, the hash chain over stored bytes (verbatim):**
> `chain_hash[n] = SHA-256(chain_hash[n-1] ‖ canonical_metadata_bytes[n] ‖ stored_payload_bytes[n])` … Canonical metadata is length-prefixed big-endian binary (event_id, event_type, schema_version, ingest_time, event_time, subject_ref, subject_sequence, priority, origin, actor_ref, correlation_id, causation_id, event_category) … `stored_payload_bytes` is whatever the `payload` column holds (plaintext or ciphertext) — the chain is format-agnostic. **The canonical-format version is recorded in the genesis event; format changes require a new version number and dual-format verification.**

> Note for your analysis: `payload_iv` and `dek_ref` are **NOT** in the canonical-metadata field list above, and are **NOT** `stored_payload_bytes`. So the IV and the key-reference are **not covered by the hash chain.** Doc 15 §5 says loosely "the chain covers stored bytes"; precisely it covers the 13 metadata fields + the `payload` column only. Factor this into RQ-3.

**QB-3 — Doc 15 §5, the immutability/irreversibility contract (verbatim):**
> Any mutation of a persisted event's metadata or stored payload breaks `chain_hash[n]` and every subsequent hash. … Sensitive-PII categories are written encrypted-at-rest under per-scope DEKs from MVP (INV-PD-03). … This is the irreversible contract — it cannot be retrofitted onto already-written plaintext (the log is immutable).

**QB-4 — the R-α disposition that deferred the algorithm but not the mechanism (verbatim, from `context/assessments/2026-06-15_Research_R-alpha_PM_Assessment.md`):**
> **AES-256-GCM-SIV (RFC 8452)** would downgrade R-α from blocking→advisory … Cost: Informational status, two-pass/non-online, not FIPS-validatable today. … Park as a Tier-2 crypto-agility option. … a *mere* extended-nonce move (XAES-256-GCM) does **not** meet the bar — by its own spec it is "not nonce misuse-resistant, nor key-committing."

If any quote-back no longer matches the cited source at dispatch, STOP and flag it — do not proceed on a stale anchor.

## 0.1 Authoritative state (do not work from memory)

- **HEAD `1eddd9a`** — M6.3 at-rest payload encryption LANDED GREEN, but **INERT**: `main()` is a stub, `payloadCipher` is wired only in tests, so **zero encrypted rows exist.** The encrypted corpus begins accumulating the instant the **app-bootstrap milestone** activates the cipher. **This is the window this brief exists to inform: the corpus is empty now and permanent-per-row thereafter.**
- **AEAD:** AES-256-GCM. DEKs (256-bit) wrap under `HKDF-SHA256(root, "scope:"+id)` scope KEKs; the DEK-wrap is also AES-256-GCM. Nonces are per-scope counter-based deterministic 96-bit (never random) on the `encryptPayload` path.
- **`chain_hash` is RESERVED but NOT YET COMPUTED** — `BLOB(32) NOT NULL DEFAULT x'00..00'` exists (AMD-37, V001); every row currently carries the zero hash. Doc 15 "activates" real computation but that activation is **unbuilt** at HEAD (Doc 01 §14 "not implemented"). Treat "the chain will be live" as a planned-but-future property, and say where your recommendation depends on it.
- **Encrypted scopes (OQ-15-2):** `[identity, presence_personal]`. Low-volume sensitive-PII.
- **This is a DESIGN brief.** Nothing here is implemented by the researcher. Code-empirical questions (e.g., per-row storage overhead of a tag at the Pi-4 floor) are flagged and routed to a CORE spike, not answered.

## 0.2 The internal verdict you are challenging (Track-3 F1)

> The envelope carries no algorithm/version discriminator; AES-256-GCM is implicitly hardcoded. Deferring GCM-SIV *the algorithm* to Tier-2 is correct (not FIPS-approvable; NIST is mid-revision). But the agility *mechanism* (a version tag) is orthogonal to the algorithm choice and was never considered. Re-encrypting the corpus to change AEAD is impossible once the chain is live (it mutates stored bytes → breaks `chain_hash`). The only forward path is "tag new rows, treat tagless as AES-256-GCM v1" — which works (additive `ALTER TABLE ADD COLUMN`, NULL ⇒ v1) but is discipline-dependent and overloads the already-fragile `dek_ref` `:`-split. **Verdict: REVERSE-NOW-WHILE-CHEAP (narrow) — reserve a 1-byte AEAD/version discriminator before app-bootstrap.** The underlying door is conceded to be two-way (the implicit-v1 escape exists); the argument is that the asymmetry (≈1 byte now vs. an immutable-log migration later) plus active NIST flux make the cheap hedge correct, and it should be decided explicitly rather than by omission.

**Attack this.** The two weakest joints, by the internal team's own admission, are: (i) the concession that the implicit-v1 escape makes the door two-way — *is that escape actually safe, or does it fail in ways the internal team waved away?* and (ii) the claim that 1 byte is sufficient — *on a hash-chained store where the tag would live outside the chain coverage (QB-2), is it?*

## 0.3 Decided ground — do not re-open

- **The log is immutable + event-sourced + (will be) hash-chained.** No recommendation may mutate stored events or re-randomize nonces. Re-encryption-in-place is off the table by construction (QB-3).
- **Counter-based per-scope nonces, never random** on the payload path (Locked, birthday-bound rationale).
- **Zero new runtime dependencies on the MVP path** unless explicitly justified (AES-GCM/SHA-256/Ed25519 are JDK-intrinsic). A discriminator must not drag in a crypto library.
- **The algorithm stays AES-256-GCM for MVP.** This brief is NOT "pick a new AEAD." GCM-SIV/wGCM/committing-AEAD remain Tier-2 *algorithm* options (R-α). The question is purely whether/how the envelope should be able to *name* its algorithm so a future swap is possible without rewriting history.
- **Fail-closed bias.** Where ambiguous, HomeSynapse prefers fail-closed + loud diagnostic over silent fallback.

---

## 1. Research questions (answer ALL; engineering register, cite prior art + the cited HomeSynapse ground)

**RQ-1 — How do real immutable / append-only / at-rest encrypted stores version their envelopes?** Survey systems that encrypt records they can never rewrite and must still be able to change algorithms: at minimum look at **age** (file version line + recipient stanzas), the **AWS Encryption SDK / S3 encryption** message format (algorithm-suite ID in the header), **Tink** keyset key-IDs + the 5-byte ciphertext prefix, **JOSE/JWE** (`alg`/`enc`), **COSE**, **Fernet** (leading version byte `0x80`), **PASETO** (version+purpose footer), **GPG/OpenPGP** packet versioning, **SQLCipher / LUKS** (cipher recorded in header/metadata), and any **event-sourcing crypto-shred** stack (Axon/Kurrent/patchlevel) that records the cipher per event. For each: does it carry an explicit algorithm/version discriminator in the ciphertext envelope? Where does it live (per-record, per-stream header, per-key)? **What is the consensus, and is a no-discriminator design ever the deliberate, defended choice?** Cite specifics.

**RQ-2 — Try to DEFEAT the "implicit-v1 retrofit is a safe escape" claim.** The internal team conceded the door is two-way because you can later add a `payload_alg` column and adopt "NULL ⇒ AES-256-GCM v1, present ⇒ named algorithm." **Find the failure modes that concession glosses.** At minimum address: (a) the discipline dependency — what real process/operational conditions cause a second algorithm to be written *without* a tag, making the corpus ambiguous? (b) the cost of the retrofit migration on a *live hash-chained* store specifically — is "additive column, NULL ⇒ v1" actually free, or are there ordering/verification/dual-read costs once `chain_hash` is computed over the rows? (c) does the retrofit interact badly with key-versioning (`dek_ref = scope_id:key_version`) or with crypto-shred (a shredded scope you can no longer decrypt-to-detect-algorithm)? **Then take a position: is the escape safe enough that the hedge is unnecessary, or not?**

**RQ-3 — The discriminator-vs-chain-coverage problem (the joint the internal team flagged but did not resolve).** Per QB-2, `payload_iv`/`dek_ref` are NOT chain-covered. If an algorithm/version discriminator is added as a new column or as part of `dek_ref`, it would also sit **outside** the hash chain — so an attacker who can mutate stored bytes could flip the algorithm tag without breaking `chain_hash` (though AES-GCM authentication and a wrong-key lookup would presumably cause a fail-closed decrypt). **Questions:** Does an *out-of-chain* algorithm discriminator create a downgrade/confusion surface, or is it benign because any mismatch fails closed at decrypt? **Should the discriminator instead be folded into the chain canonicalization** (i.e., added to the QB-2 metadata field list, mirroring how the chain already versions its *own* canonical-metadata format in the genesis event)? Compare: discriminator as (i) a new chain-covered metadata field, (ii) a non-chain-covered column, (iii) a prefix byte on the ciphertext (which *is* `stored_payload_bytes` and therefore *is* chain-covered). Which is correct for this substrate, and why? This is the question most likely to show the 1-byte hedge is *insufficient* as stated.

**RQ-4 — If a discriminator is warranted: the design.** Take a position on: (a) **what it names** — AEAD algorithm only, or algorithm + envelope-structure-version (so the *shape* of the envelope, not just the cipher, can evolve)? (b) **where it lives** — chain-covered ciphertext prefix vs new column vs `dek_ref` extension (note the existing `:`-split fragility); (c) **width/encoding** — 1 byte / registry-of-suites (cf. the Encryption-SDK algorithm-suite-ID and Tink key-type-URL models) vs a free-form string; (d) **the relationship to the genesis-recorded canonical-format version** already in Doc 15 §3.3 — should the payload envelope reuse that exact versioning pattern (one project-wide format register) or carry its own? (e) zero-new-dependency and Pi-4 storage-overhead constraints. Give the recommended concrete shape.

**RQ-5 — Steelman the NULL choice, then rule on it.** State the strongest case for shipping the envelope with **no** discriminator (YAGNI; most systems never change AEAD; the corpus is low-volume sensitive-PII that could be re-keyed via crypto-shred + re-ingest rather than re-decrypted; an extra column/byte is needless surface; AES-256-GCM is a 25-year horizon cipher). Then say whether that case survives **given** (i) the immutable+chained substrate makes this the most-extreme "can't rewrite" case, (ii) NIST's active SP 800-38D Rev.1 revision (wGCM / nonce-derivation modes, second pre-draft June 2026, comments through 31 Jul 2026), and (iii) the corpus is **empty today** and permanent-per-row after app-bootstrap. Is app-bootstrap genuinely the last cheap moment, or can this safely wait — and if it can wait, until what concrete trigger?

**RQ-6 — Precedent for the failure being prevented.** Find documented real-world incidents/post-mortems where a non-versioned or under-versioned crypto envelope forced a painful migration, a downgrade attack, or a "we can't tell which algorithm encrypted this" ambiguity (e.g., JWE `alg:none`/confusion issues, early-Fernet-style format lock-in, WhatsApp/Signal/database-at-rest cipher migrations, TLS version-downgrade lessons, any "we hardcoded the cipher and regretted it" engineering write-up). The point is calibration: *how often does the deferred-agility risk actually bite, and how badly?* This is the evidence that decides whether F1 is a real now-or-never or a paranoid one.

---

## 2. Mandatory return document format

Save the return to `homesynapse-core-docs/research/returns/` (PM rehomes/assesses on intake). Structure:

```
# R-γ: Crypto-Agility & Envelope Versioning — DOCS Challenge Return

## 0. Quote-back gate [M — FIRST]  — QB-1..QB-4 verbatim + one-line "held as ground" each.
## 1. Executive Summary [M]  — 6–10 verdict bullets; LEAD with the §4 position (ADD-NOW / SAFE-TO-DEFER /
                                NEEDS-MORE-THAN-A-TAG) and the single sentence that most damages the internal F1 verdict.
## 2. Prior-Art Deep Dives [M]  — one subsection per system surveyed (RQ-1), with citations: where the
                                  discriminator lives, what it names, and any deliberate no-discriminator design.
## 3. Cross-Cutting Analysis [M]  — (a) the implicit-v1 retrofit failure-mode table (RQ-2); (b) the
                                    discriminator-vs-chain-coverage comparison, all three placements (RQ-3);
                                    (c) the incident calibration (RQ-6).
## 4. Findings + Recommendations [M — THE DELIVERABLE]  — a disposition:
       position ∈ {ADD-NOW, SAFE-TO-DEFER (until trigger X), NEEDS-MORE-THAN-A-TAG} | the concrete
       discriminator design if any (RQ-4) | rationale vs the cited HomeSynapse constraint | confidence |
       what it changes about the app-bootstrap charter's envelope-finalization gate.
       Explicitly state whether you CONFIRM, NARROW, or OVERTURN the internal F1 verdict, and on what evidence.
## 5. Caveats and Open Questions [M]  — source reliability A/B/C per load-bearing claim; anything needing a
                                       CORE empirical spike (flag it, do not measure); residual unknowns.
## 6. Appendix: Sources [M]  — URL families grouped by system; every factual claim traceable.
```

## 3. Evidence standards (non-negotiable)

- Every external claim carries a citation (URL family + enough specificity to verify). For the NIST anchor, cite SP 800-38D and its Rev.1 pre-draft document history directly (CSRC), not a secondary summary.
- Distinguish **standard/spec** (NIST, RFC, IETF) from **field practice** (a system's docs/source) from **your inference**. Label inferences.
- No fabricated HomeSynapse internals. The only HomeSynapse facts you assert are the ones quoted/cited in §0; if a recommendation needs a detail not in §0 (e.g., the exact `dek_ref` parser behavior, or whether the genesis-format-version mechanism is built), name it as an *assumption to verify with the PM* — do not invent it. (Known: the chain itself is not yet computed — 0.1.)
- A recommendation that contradicts a Locked decision (immutable log, counter nonces, zero-new-deps, AES-256-GCM-for-MVP) must say so explicitly and argue the amendment case — it does not get to silently assume it away.

## 4. Guardrails (violations = the finding is discarded)

- **Adversarial, not confirmatory.** A return that agrees with F1 without having genuinely tried RQ-2 and RQ-5 (defeat the hedge / steelman NULL) is low-value. Show the attack.
- **Stay design-level.** Do not write HomeSynapse code. Code-empirical questions (per-row overhead, parser changes) route to a CORE spike.
- **Gap-relative, not generic.** "Crypto agility is best practice" / "version your formats" are non-findings on their own — every finding is relative to a §0.3 decided-ground item or the immutable+chained substrate, and must engage the implicit-v1 escape and the chain-coverage question specifically.
- **Don't re-fight the algorithm choice.** GCM-SIV/wGCM/committing-AEAD adoption is Tier-2 and out of scope (R-α owns it). This is about the *mechanism to name the algorithm*, not which algorithm.

## 5. What the PM does with the return (so you aim at it)

The PM assesses serially on return, grades it, and folds the §4 position into the **Track-2 app-bootstrap charter's envelope-finalization gate** (alongside F2 scope-width, F3 nonce-construction binding, F4 chain-liveness). If the position is **ADD-NOW**, the discriminator design (RQ-4) becomes a coding-instruction line item that must land *before* `payloadCipher` activates. If **SAFE-TO-DEFER**, the return must name the concrete trigger and the PM records an explicit, dated "ship tagless, rely on implicit-v1" rationale so the choice is on the record, not defaulted by omission. If **NEEDS-MORE-THAN-A-TAG**, the chain-coverage finding reshapes the envelope work. **The return's leverage is that internal red-teaming cannot validate this — the project designed the envelope, so an outside, web-grounded adversarial read is the only way to know whether F1 is a real now-or-never or a paranoid one.**

---

## Routing & dispatch note

**DOCS Project, fresh conversation, web search required.** Dispatch **before** the Track-2 app-bootstrap charter finalizes the envelope — this return is an input to that gate. It is parallel to R-α (which owns the *algorithm* question and the backup/restore/read-path contract) and does not compete for the Coder or the ratification gate. It is unblocked now. Connector-blind acceptable; declare gaps.
