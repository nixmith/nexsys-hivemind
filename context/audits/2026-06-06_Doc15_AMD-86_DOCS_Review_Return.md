<!--
file: context/audits/2026-06-06_Doc15_AMD-86_DOCS_Review_Return.md
purpose: Full (M6-entry-gate) DOCS-Project review return for Doc 15 (Cryptographic Architecture, Draft) + AMD-86 (INV-PD-07 crypto-shred MVP-scope narrow + INV-PD-03 at-rest posture, PROPOSED).
audience: Nick (ratify), PM
status: COMPLETE — RATIFY-WITH-EDITS (E1 schema naming; E2 §3.8 JPMS-wiring clarification)
baseline: homesynapse-core HEAD `8ef9e9f`; watermark AMD-64; projectionVersion 5
reviewer: DOCS-Project (independent session, 2026-06-06)
captured: 2026-06-07 — verbatim from the review conversation (via Nick); tool-use narration omitted, review content unaltered
-->

# Doc 15 (Cryptographic Architecture) + AMD-86 — Full DOCS Review Return

## Overall Verdict: **RATIFY-WITH-EDITS**

Both Doc 15 and AMD-86 are architecturally sound, internally consistent with the invariant registry and the codebase at HEAD `8ef9e9f`, and carry the research's substance faithfully except for the deliberate and well-documented D2 line-move. The threat model is one of the most honestly stated at-rest crypto postures I have reviewed. Two edits are required — one genuine naming inconsistency in the schema/key-hierarchy description, one clarification in the JPMS-cycle text. Neither is a security overstatement; neither is blocking for the design intent. No overstated security claim was found.

---

### J1 — F-A: the at-rest threat-model claim. **PASS.**

**Re-derivation.** A machine-local key (`0400`) on the same medium as the ciphertext protects exactly two scenarios:

(a) *Key-excluding copies* — a backup, sync, or directory copy that includes `payload` ciphertext but excludes `.root-key`. The attacker has ciphertext but no key material. AES-256-GCM is CCA-secure; the data is confidential.

(b) *Less-privileged process reads* — a process running under a different user than the HomeSynapse service user cannot read the `0400` key file at runtime. It can read the SQLite WAL (if world-readable — an operational detail), but obtains only ciphertext for encrypted scopes.

It does **not** protect against:

(c) *Medium theft* — an attacker who images or removes the SD card/NVMe mounts it on their own OS, reads `.root-key` regardless of POSIX permissions, derives every scope KEK via the same HKDF, and decrypts everything. Doc 15 §3.5 states this explicitly: "the `0400` permission is a runtime OS control, meaningless once the medium is mounted on the attacker's machine."

(d) *On-device root* — `root` reads `.root-key`, attaches to the JVM, or reads `/proc/<pid>/mem` (the Research 5 T3 threat).

**Completeness check.** I looked for any *other* attack the docs imply protection against but don't actually cover. One implicit scenario worth noting: a backup that *includes* the root-key file alongside ciphertext is NOT protected. Doc 15 §6 (Failure Modes table, counter-nonce section) explicitly states this corollary: "a backup carrying ciphertext + counter state but *not* the key is safe; one carrying the key is not." So this case is covered.

**Overstatement scan.** Doc 15 §3.5 says "never 'safe if your device is stolen.'" Doc 15 §12 says the MVP claim is "encrypted at rest and designed to be cryptographically destroyable; key-excluding copies are protected." AMD-86 §2.2 posture text repeats the same language with additional precision on the partial-vs-full INV-PD-03 distinction. "User-owned keys" is stated as Tier-2, not MVP. **No security claim is stronger than what the crypto delivers.** This is clean.

---

### J2 — Per-scope / crypto-shred design. **EDIT-REQUIRED** (naming inconsistency, not a design flaw).

**(a) App-level per-scope, not SQLCipher whole-DB.** Confirmed. Doc 15 §1/§3.4 states this and the rationale is correct: a whole-DB cipher encrypts everything under one key, so you cannot destroy one category's key without destroying all data. Per-scope is the *only* mechanism that makes per-category crypto-shred possible (INV-PD-07). Sound.

**(b) Chain-over-stored-bytes.** Confirmed. Doc 15 §3.3: `stored_payload_bytes` is whatever the `payload` column holds — plaintext or ciphertext. The chain is format-agnostic. Encrypting a scope does not alter any stored byte that was already chained; destroying a scope KEK does not alter any stored ciphertext — both the chain and other scopes survive. This is the critical design insight, correctly inherited from the research §2.7 and re-stated in Doc 15 §5.

**(c) Counter-based GCM nonces.** Confirmed. Doc 15 §3.4: "counter-based deterministic 96-bit nonces per scope (stored alongside the DEK) — never random — to avoid the GCM birthday bound (random nonces collide at ~2³² per key; at 1k events/s on one scope that is ~50 days)." The research §4.1 identified this risk and proposed the same mitigation. Counter nonces eliminate the birthday-bound collision risk entirely. Sound.

**Finding E1 — schema/key-hierarchy naming inconsistency (EDIT-REQUIRED).**

Doc 15 §3.1 defines a 3-level hierarchy: `Root → HKDF → Scope KEK → wraps → Scope DEK → encrypts payloads`. Doc 15 §4.2 table confirms: Scope KEK is "Not stored directly — re-derived HKDF(root, 'scope:'+id) on demand"; Scope DEK is stored in "`scope_keys.encrypted_kek` (wrapped by KEK)."

But the §4.1 schema declares:

```sql
encrypted_kek   BLOB    NOT NULL,    -- scope KEK wrapped under the root key (AES-256-GCM)
```

This is inconsistent on two axes. The column *name* says "encrypted KEK" but the §4.2 table says the stored blob is the *DEK* wrapped by the KEK. The column *comment* says "scope KEK wrapped under the root key (AES-256-GCM)" but per §3.1 the KEK is derived via HKDF (deterministic, not wrapped), and what is wrapped (AES-256-GCM) is the DEK *by* the KEK. The §8.2 `ScopeKey` record uses `encryptedKek` (the Java camelCase of the SQL name), propagating the error to the interface layer.

**Required fix:** rename the column to `encrypted_dek` (or `wrapped_dek`), fix the comment to "scope DEK wrapped by the scope KEK (AES-256-GCM)", and update the §8.2 `ScopeKey` record field accordingly. Alternatively, if the intent is actually a 2-level hierarchy where the KEK *is* the DEK, §3.1 and §4.2 must be corrected instead. Either way the doc must be self-consistent before an M6 coding instruction is derived from it — an implementor who reads "encrypted_kek" and "scope KEK wrapped under the root key" will build the wrong wrapping layer.

---

### J3 — D2 MVP/post-MVP line. **PASS.**

The research deferred *all* envelope encryption and crypto-shredding to Tier 2. D2 separates two things the research conflated:

(i) *Encrypt-on-write* — now MVP. Justified by INV-PD-03 (a live at-rest obligation; plaintext PII on a removable SD card is a real exfiltration hole) **and** the now-or-never argument (the event log is immutable; a category can only ever be crypto-shredded if it was written encrypted under a per-scope key in the first place). Since the key infrastructure is already MVP for the secret store (Doc 06), at-rest encryption is a small increment, not new scope.

(ii) *The shred operation* — deferred post-MVP. No MVP consumer: a local, single-home, zero-telemetry installation's "delete my data" is served by whole-installation reset. The immutability-vs-erasure conflict crypto-shredding resolves only bites when there is a reason to *retain* data after erasure (institutional audit) or data has left the device (cloud) — both post-MVP.

**§2.3 table vs AMD-86 consistency.** The Doc 15 §2.3 table's six rows (hash chain MVP, Ed25519 MVP, key infra MVP, at-rest encryption MVP, shred operation post-MVP, passphrase root post-MVP) match AMD-86 §5 scope fences verbatim. Internally consistent.

**The re-scope-up trigger is correctly documented:** AMD-86 §3 ("M5-D energy/institutional interviews carry the verifiable-erasure question; if a launch-window buyer requires it, this amendment is revisited before M6 freezes the write path"). This is the right governance: the deferral is evidence-gated, not final.

---

### J4 — AMD-86 minimality + correctness. **PASS.**

**§2.1 text change.** The amendment preserves INV-PD-07's first sentence ("The MVP must implement the per-scope key management infrastructure and define the encryption scope categories") unchanged. It strikes *only* the operational-shred sentence ("Crypto-shredding must be operational for at least one data category…") and replaces it with text that (a) makes the sensitive-PII encrypt-on-write obligation explicit, (b) defers operational crypto-shredding to the first cloud/institutional consumer, and (c) preserves the design intent (`:425`, deletion via key-destruction, events remain in the log). This is the minimal change — nothing broader is struck or added.

**§2.2 INV-PD-03 posture.** The posture note appended to INV-PD-03 (`:389`) uses the corrected threat-model language (J1-verified): partial satisfaction, key-excluding copies + less-privileged reads, NOT medium theft or on-device root, user-owned keys = Tier-2. The language matches Doc 15 §3.5 and §12 verbatim in all load-bearing claims. Sound.

**AMD-86-INV-01.** "Encrypt-on-write is irreversible; the shred operation is deferrable." This captures the irreversibility constraint on the immutable log correctly — the *encrypt* decision is now-or-never; the *shred* decision can be made later. Clean invariant.

---

### J5 — Doc 06 + AMD-60 reconciliation (§7.3). **PASS.**

**(a) Shared-root unification.** Doc 15 §7.3 unifies the existing `.secret-key` (Doc 06's single static AES-256-GCM key for the secret store) and the event-payload encryption root into one machine-local root key at MVP. The secret store becomes one scope (`scope_id = "config_secrets"`) in the per-scope key hierarchy. This avoids two parallel key systems and is architecturally elegant — M6 builds one key manager that serves both consumers. Correct.

**(b) Atomic multi-key durable write.** AMD-60-INV-03 (Architecture_Invariants_v1.md §30): "`rotate` is integration-scoped (LTD-17), atomic across all entries of a single call (all-or-nothing — a token+refresh-token pair can never be torn), and durable-before-return." Doc 06 §8.5 today exposes only single-key `set(key,value)`. Doc 15 §7.3 correctly identifies this gap and states: "M6 must add an all-or-nothing multi-key write (e.g., `setAll(Map)`) beneath the rotator." This doc owns the *requirement*; Doc 06/M6 owns the store API change (AMD-66–71 scope). The reconciliation correctly states AMD-60's contract — I verified against AMD-60 §2.1, AMD-60-INV-03, and the arbitration A5 history.

**(c) CredentialRotator vs crypto-shred distinction.** §7.3 correctly distinguishes rotating a credential (overwriting a secret value — the old credential is gone once the store write commits) from crypto-shredding (destroying a scope key to render an event-log scope unreadable). Both consume the shared root; they are different operations on it. No contract mis-statement.

---

### J6 — the m1/m2/m3 folds. **EDIT-REQUIRED** (m3 text clarification; m1 and m2 PASS).

**(m1) chain_hash activation.** AMD-37 (APPLIED 2026-05-02) changed V001 in place from nullable to `BLOB(32) NOT NULL DEFAULT x'00…00'`. The M3 Audit Gap Closure (§3.3) independently confirms: "Every event row gets `chain_hash = 0x00...00`. There is no chain computation, no dependency on prior events' hashes." `SqliteEventStore` binds `ZERO_HASH` at line 353 (per the audit and AMD-37's prescribed resolution). AMD-37 explicitly anticipates "the crypto milestone activates chaining." Doc 15 activates it — replaces the `ZERO_HASH` bind with real single-writer chain computation. The no-backfill claim holds: every pre-activation row already carries the zero-hash, which is a known deterministic value. **PASS.**

**(m2) Counter-nonce crash/restore durability.** Correctly marked `[BLOCKING-for-M6-impl]` in Doc 15 §6 (Failure Modes), §13.4 (Testing Strategy: "kill mid-encrypt then restart and assert the per-scope nonce counter never repeats"), and the §16 summary table. The backup/restore corollary is also correctly stated in §6: "a restore can never resume a scope at a counter ≤ any value already used under that DEK (rotate the DEK on restore, or carry the high-water mark in the backup)." The hazard, the blocking gate, and the co-design requirement are all correctly flagged. **PASS.**

**(m3) PayloadCipher JPMS cycle avoidance.** The design is sound — but the §3.8 text contains a misleading claim.

**Finding E2 — §3.8 JPMS cycle claim needs clarification (EDIT-REQUIRED).**

Doc 15 §3.8 says: "Persistence thus gains no static config dependency. Symmetrically, the `scope_keys` store is owned on the config/key-manager side…, so **config never `requires` persistence either — closing the cycle from both directions.**"

The critical JPMS property — *no cycle* — is correct: persistence does NOT `requires com.homesynapse.config` (verified at HEAD via the AMD-52 §7.1 module-info embed), so there is no cycle regardless of the config→persistence direction. But the statement "config never requires persistence either" needs clarification. If `ScopeKeyManager` (in `com.homesynapse.config`) directly implements `PayloadCipher` (exported from `com.homesynapse.persistence`), then `com.homesynapse.config` *must* `requires com.homesynapse.persistence` to see that interface. That is a one-way edge (config → persistence), not a cycle — but the text claims both directions are closed, which is misleading.

The likely design intent — consistent with the AMD-45 `AtomicCheckpointSink` precedent — is that the composition root (`com.homesynapse.app`) creates an adapter or lambda that bridges the config-side `ScopeKeyManager` to the persistence-side `PayloadCipher`, so neither persistence nor config references the other directly. If so, the text should state this explicitly: "The composition root (`HomeSynapseCore`) bridges `ScopeKeyManager` to `PayloadCipher` — neither persistence nor config requires the other; the `app` module requires both." This is the pattern that genuinely closes both directions.

**Required fix:** replace the "config never requires persistence either" sentence with an explicit statement of the wiring mechanism — either (a) config implements `PayloadCipher` directly (one-way config → persistence edge, no cycle, but correct the "both directions" claim) or (b) the composition root bridges them (both directions genuinely closed — the intended reading). In either case, mandate the verbatim module-info evidence in the M6 coding instruction (the doc already does this, but the clarification anchors it to the correct scenario).

---

### J7 — Open questions + status. **PASS.**

**OQ-15-1 (root-key source): RESOLVED.** Machine-local key file with the corrected threat bar (J1-verified). The resolution text in §15.1 matches the §3.5 threat model and the AMD-86 §2.2 posture note. Residual (key-file generation/permission/rotation) is correctly classified as an M6 implementation detail, not an open design question.

**[BLOCKING-for-M6-impl] items:** counter-nonce durability (m2) is the only blocking item, correctly flagged in §6, §13.4, and the §16 summary. It blocks the M6 *implementation*, not the locking of this *design* — correctly classified.

**Template completeness.** All 13 mandatory sections are present (Purpose through Open Questions). The doc has a §16 Summary of Key Decisions table (a useful addition beyond the template). Provenance and supersession are documented in the header and in §16. The currency note about Doc 01 §14/§4.2 staleness is properly flagged in §15.5. OQ-15-2/3/4 are [NON-BLOCKING] and appropriately deferred.

**Draft readiness.** After the two edits (E1, E2), the document is ready to move toward Locked. No structural gap prevents locking.

---

## Summary of Findings

| # | Job | Type | Description | Fix |
|---|---|---|---|---|
| E1 | J2 | EDIT-REQUIRED | §4.1 column `encrypted_kek` + comment "scope KEK wrapped under the root key" is inconsistent with §3.1 (KEK derived via HKDF, not wrapped) and §4.2 (stored blob is the DEK wrapped by KEK). | Rename to `encrypted_dek`; fix comment to "scope DEK wrapped by the scope KEK (AES-256-GCM)"; update §8.2 `ScopeKey` record field. |
| E2 | J6/m3 | EDIT-REQUIRED | §3.8 claims "config never requires persistence either — closing the cycle from both directions." The critical no-cycle property holds, but the "both directions" claim needs the wiring mechanism stated explicitly (composition-root bridge or one-way edge). | Add 1–2 sentences in §3.8 stating the exact injection path: composition root bridges `ScopeKeyManager` ↔ `PayloadCipher`, so neither module references the other. |

No overstated security claims. No spec↔code mismatches at HEAD `8ef9e9f`. No locked-decision or frozen-fork violations. The D2 line-move from the research is correctly documented and well-justified. AMD-86 is appropriately minimal — it strikes only what it needs to and adds only the INV-PD-03 posture note. The design is defensible, the governance is clean, and the honest threat model is the document's strongest quality.

---

**Canonical return path:** `nexsys-hivemind/context/audits/2026-06-06_Doc15_AMD-86_DOCS_Review_Return.md`
