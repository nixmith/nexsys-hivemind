<!--
file: context/instructions/2026-06-06_Doc15_AMD-86_FULL_DOCS_Review_Prompt.md
purpose: FULL DOCS-Project review prompt for Doc 15 (Cryptographic Architecture, Draft) + AMD-86 (INV-PD-07 narrow + INV-PD-03 posture, PROPOSED). NOT the P4 lightweight track — this narrows a constitutional privacy invariant the trust brand rests on.
audience: DOCS-Project reviewer (independent Cowork/Claude session)
status: READY to dispatch
-->

# FULL DOCS-Project Review — Doc 15 (Cryptographic Architecture) + AMD-86 (INV-PD-07 / INV-PD-03)

You are the independent DOCS-Project reviewer. Your job is to **re-derive and validate**, not to trust the documents' own claims. This is a **full review** (not the P4 lightweight track) because AMD-86 **narrows a ratified, constitutional privacy invariant (INV-PD-07)** and states an INV-PD-03 posture — the trust brand rests on these being honest. **Your single most important duty: flag any overstated security claim.**

## Baseline + what to read (verify against source, do not trust summaries)

- **homesynapse-core HEAD `8ef9e9f`** (M4 COMPLETE). Re-verify every load-bearing code claim at this HEAD.
- **Under review:** `homesynapse-core-docs/design/15-cryptographic-architecture.md` (Draft) and `design/amendments/AMD-86_INV-PD-07_Crypto-Shred-MVP-Scope_and_INV-PD-03_At-Rest-Posture.md` (PROPOSED).
- **Provenance:** Doc 15 promotes + supersedes `research/2026-03-22_Unified_Cryptographic_Architecture_for_HomeSynapse.md` (read it — confirm Doc 15 carries its substance faithfully *except* the deliberate D2 line-move).
- **Authoritative sources to re-derive against:** `governance/Architecture_Invariants_v1.md` INV-PD-03 (`:389`), INV-PD-07 (`:405-427`, MVP-scope clause `:427`), INV-PD-08, INV-CE-02, INV-ES-01; `design/06-configuration-system.md` §3.4/§8.5 (SecretStore); `design/amendments/AMD-60_*` (CredentialRotator); `design/amendments/AMD-37_*` (chain_hash reservation); the persistence/device/config `module-info.java` files; `SqliteEventStore.java` (chain_hash bind), `PersistenceJacksonModule.java`, `AttributeValueSerializer.java`.
- **Decision context (not under review, but the intent):** `nexsys-hivemind/context/decisions/2026-06-06_post-M4_M5-window_decisions.md` (D2).

## Validation jobs (return a verdict on each)

**J1 — F-A: the at-rest threat-model claim (HIGHEST PRIORITY — flag any overstatement).** Doc 15 §3.5/§12 and AMD-86 §2.2 claim machine-local-key MVP encryption protects **only** "data copies that exclude the root-key file (key-excluding backups, synced/copied data dirs) + reads by a less-privileged process," and explicitly **NOT** medium theft (the key travels with the medium) or on-device root. Independently verify this is correct and **complete** — is there any *other* attack the docs imply protection against but don't actually cover? Confirm the docs nowhere claim "safe if your device is stolen." Confirm "user-owned keys" (INV-PD-03) is stated as **Tier-2, not MVP** (MVP = partial INV-PD-03). **If any security claim is stronger than the crypto actually delivers, that is a blocking edit.**

**J2 — the per-scope / crypto-shred design.** Validate: (a) at-rest = **app-level per-scope payload encryption, not SQLCipher whole-DB**, and that per-scope is genuinely *required* for per-category crypto-shred (a whole-DB cipher can't shred one category). (b) The chain-over-stored-bytes claim (integrity independent of encryption + shred). (c) Counter-based GCM nonces (not random) — correct avoidance of the birthday bound.

**J3 — the D2 MVP/post-MVP line.** Validate that encrypting sensitive-PII-on-write **from MVP** is justified (INV-PD-03 at-rest obligation + the now-or-never shreddability argument on the immutable log) and that deferring **only the shred operation** is sound (no MVP consumer; whole-install reset is the local erasure recourse). Confirm the §2.3 table is internally consistent with AMD-86.

**J4 — AMD-86 minimality + correctness.** Confirm AMD-86 strikes **only** INV-PD-07's "operational for ≥1 category at MVP" clause, preserves sentence 1 (infra + categories) and the design intent (`:425`, deletion via key-destruction, events remain in the log), and that the §2.2 INV-PD-03 posture text is the corrected (J1) claim. Confirm the proposed invariant text is the right minimal change — nothing broader.

**J5 — Doc 06 + AMD-60 reconciliation (§7.3).** Re-derive against AMD-60 + Doc 06 §8.5: confirm (a) the shared-root unification (secret store + event-payload encryption on one root; secret store = a scope), and (b) the requirement that the M6 `SecretStore` gains an **atomic multi-key durable write** beneath `CredentialRotator.rotate(Map)` (AMD-60-INV-03 atomicity). Flag if the reconciliation mis-states AMD-60's contract.

**J6 — the m1/m2/m3 folds.** (m1) Confirm `chain_hash` is **already** V001 / NOT NULL / zero-hash-default per AMD-37 (verify `V001` + `SqliteEventStore.java:353` + AMD-37), so Doc 15 *activates* rather than adds it, and the no-backfill claim holds. (m2) Confirm the counter-nonce crash/restore durability hazard is correctly marked **[BLOCKING-for-M6-impl]** and co-designed with backup/restore (and the "key-excluding backups protected only" corollary). (m3) Confirm the `PayloadCipher` consumer-defined-in-persistence seam (AMD-45 pattern, injected at the composition root) genuinely avoids a persistence↔config JPMS cycle — re-derive against the actual module-infos (persistence does not require config; config does not require persistence).

**J7 — open questions + status.** Confirm OQ-15-1 is correctly resolved (machine-local, with the corrected bar), the [BLOCKING-for-M6-impl] items are flagged, and the Draft is otherwise complete enough to move toward Locked after this review.

## Return format

Open with the overall verdict: **RATIFY** / **RATIFY-WITH-EDITS** / **REJECT**. Then, per job J1–J7: PASS / EDIT-REQUIRED / FAIL, with the specific evidence (file:line) and, for any EDIT-REQUIRED, the exact wording change. **List every overstated security claim separately and prominently** (J1) — even a small one is blocking. Note any source-derivation where the document's claim did not match HEAD. Commit this return to `homesynapse-core-docs/research/returns/` or `nexsys-hivemind/context/audits/` per the canonical-paths convention, and cite the path.
