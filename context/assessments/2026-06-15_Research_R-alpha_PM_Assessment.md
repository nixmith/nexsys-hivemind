<!--
file: context/assessments/2026-06-15_Research_R-alpha_PM_Assessment.md
purpose: PM assessment + disposition of the R-α / NEW-1 research return (restore nonce-monotonicity + the cause-discriminated read-path contract). Grades the return, verifies its HomeSynapse-fact claims against the source companion, routes REC-216..235, records the governance actions, and names the consuming WUs.
audience: Nick, PM, Coder (crypto-shred WU + app-bootstrap milestone)
state-type: assessment
status: COMPLETE 2026-06-15
grade: A
return: docs/research/returns/2026-06-15_Research_R-alpha_Restore_Nonce_Monotonicity_and_Cause-Discriminated_Read_Contract.md (rehomed from context/instructions/)
brief: context/instructions/Research_R-alpha_Crypto_Backup-Restore_and_Confidentiality-vs-Availability_Brief.md
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4; M6.3 landed); watermark AMD-93; Doc 15 LOCKED.
-->

# PM Assessment — R-α + NEW-1 (Restore Nonce-Monotonicity + Cause-Discriminated Read-Path Contract)

## Grade: A

The strongest research return of the side-research set to date. It is gap-relative (not generic), primary-sourced with verbatim standards quotes and exact identifiers, takes decisive positions, steelmans **both** extremes before earning the middle, engages and **defeats the decisive objection using HomeSynapse's own invariants**, honors the register fences (recommends, does not mint), uses the assigned REC range (REC-216..235), and declares its own gaps. It answers both questions the brief posed and hands the consuming WUs an implementable contract.

## Why A (against the research-quality bar)

- **Decisive positions, not "it depends."** R-α: rotate-DEK-on-restore (a) is the binding contract; carry-high-water-mark (b) is a defense-in-depth cross-check only — with the failure mode of (b) named precisely (backup at N → writes to N+k → restore to N → reuse N+1…N+k). NEW-1: the cause-discriminated contract is correct and **earned**, with a crisp decision rule (REC-232).
- **Steelman discipline.** REC-233 (flat fail-closed) and REC-234 (always-degrade) are both steelmanned with their weaknesses, before the cause-discriminated middle is taken. REC-231 is the decisive objection (forged "intended" signal via AES-GCM's non-committing property + the Len–Grubbs–Ristenpart partitioning-oracle work), and REC-232 defeats it **specifically** for HomeSynapse: the intended-erasure signal is not "decrypt failed" but "decrypt impossible because a recorded, chain-covered shred destroyed the key while chain_hash still validates" — forging that requires breaking the integrity chain, which is the same bar as defeating fail-closed.
- **Evidence hierarchy held.** NIST SP 800-38D §8 verbatim; RFC 8452 verbatim; the age STREAM spec verbatim; SQLCipher's per-page HMAC design verbatim; crypto-shred behavior pinned to primary READMEs/source with exact identifiers (`@EncryptedField`, `CryptoShreddingKeyService.deleteSecretKey`, `#[PersonalData(fallback: 'anon')]`, `GetDecryptedOrDefault`); source-reliability graded A/B+/B per claim.
- **Register fences honored.** §"Scope discipline": "does not mint binding milestone/type/contract obligations and makes no market/positioning claims, per the engineering-register frame." Findings routed to two buckets (crypto-shred WU + app-bootstrap).

## Verification ledger (HomeSynapse-fact claims vs. the source companion — no fabrication)

Every HomeSynapse internal the return asserts traces to the source companion provided in the brief/clarification:
- **chain_hash-over-stored-bytes invariant** (the load-bearing enabler, used in REC-226/232/§Details) = **Doc 15 §5 verbatim** ("the chain covers stored bytes, so integrity is independent of encryption and of shredding"). ✅ Correctly applied.
- **Write-path discharged** (durable, fsync-ahead-of-return, re-init from persisted max) = the OR-M6-NONCE write-path resolution. ✅
- **The two restore mitigations** ((a) rotate DEK, (b) carry high-water mark) = **Doc 15 §6 recovery clause verbatim**. ✅ The return's judgment that (a) ≫ (b) is a refinement, not a contradiction (Doc 15 lists both as options).
- **DegradedEvent placeholder** for CASE (a) = the existing read-path degrade-posture (codec-parse-failure → DegradedEvent; converge §Verification). ✅ Reused, not invented.
- **The shred tombstone (REC-227)** is a **new design recommendation**, correctly framed as such and routed to the crypto-shred WU — not asserted as existing code. ✅ (Doc 15 §3.6 today ships only the `destroyed_at` field + the unreadability property; the operation is post-MVP.)
- The return reasons from the **behavioral** read-path contract, not from the CORE `SqliteEventStore` line numbers (which the clarification explicitly relieved it of verifying). ✅ No fabricated CORE source.

**Honesty section accepted as graded.** The return's own caveats are correct and well-labeled: (i) AxonIQ's *commercial* module read-path behavior unverified (OSS extension + patchlevel + Kurrent firmly establish the degrade finding); (ii) Signal backup-format internals partly reverse-engineering-grade (the key-loss-means-data-gone fact is primary); (iii) SP 800-88r2 §3.2 sub-section numbering via a secondary compliance summary cross-checked to the primary PDF.

**One PM verification flag (non-load-bearing):** the **June 1 2026 "second pre-draft / wGCM (Rijndael-256)"** claim (§Details / Stage-3) is past the PM's reliable-knowledge horizon and could not be independently confirmed this session. It is **not load-bearing** — it sits only in Stage-3 strategic-tracking, and the MVP contract (rotate-on-restore + cause-discrimination) does not depend on it. Spot-confirm against the NIST CSRC SP 800-38D document history before it informs any decision. The Jan-2025 first pre-draft is consistent with prior knowledge.

## Disposition — how we use this

### Problem 1 (R-α) — RESOLVED. OR-M6-NONCE restore-half can now CLOSE.
**Disposition (PM): adopt rotate-DEK-on-restore (strategy a) as the binding restore contract; (b) carry-high-water-mark = defense-in-depth cross-check only (assert resumed counter ≥ carried max), never the sole guarantee.** This is the design input OR-M6-NONCE half (b) was waiting on. It changes no shipped M6.3 code (the backup/restore feature itself is unbuilt — foundation-readiness F3); it is a **design decision for the future backup/restore WU**.
- **Governance action → Nick (escalation; Doc 15 is LOCKED):** Doc 15 §6 currently offers (a) **or** (b) as equal options. Recommend a small **Doc 15 §6 currency amendment** binding (a) and demoting (b) to cross-check. Closes OR-M6-NONCE restore-half on ratification. (Lightweight — selects among Doc-15-sanctioned options + downgrades one; not a supersession.)

### Problem 2 (NEW-1) — RESOLVED. This is the C2/F-A1 design answer.
**Disposition (PM): adopt the cause-discriminated read-path contract** — the decision rule from REC-232:
- **CASE (a) intended unreadability** (decrypt impossible because a recorded, chain-covered shred destroyed the KEK **AND** chain_hash validates) → **degrade the row to a DegradedEvent placeholder carrying the cause, continue the read.**
- **CASE (b) unintended unreadability** (GCM auth-fail on chain-valid bytes / root key missing-corrupt at boot / chain_hash itself fails) → **fail the whole read batch closed, surface a distinct loud error.**
- **Enabling primitive (new): the shred tombstone** — a chain-covered event recording (scope, timestamp, reason) of KEK destruction, so CASE (a) is a *lookup*, not an inference from a bare decrypt failure (REC-227).

This **sharpens the converge C2 (=F-A1) HIGH finding's disposition.** The converge tentatively suggested "catch decrypt failure in `fromRow` and emit `DegradedEvent`." R-α corrects that: a flat catch-and-degrade is **wrong** (REC-234 — it masks corruption/tampering = the CASE (b) failure). The fix is the cause-discriminated contract, which requires the shred tombstone + the chain-validity check. **C2's fix is therefore not a one-line catch; it is a small design beat the app-bootstrap milestone (fail-closed half) + the crypto-shred WU (degrade half) must carry.**

### REC routing (REC-216..235)
| Bucket | RECs | Consuming WU |
|---|---|---|
| **Restore / nonce contract** (rotate-DEK binding; (b) cross-check; boot-time refuse-to-encrypt-until-safe) | REC-216–223, REC-235 | **app-bootstrap milestone** (+ the future backup/restore WU); closes OR-M6-NONCE restore-half |
| **Cause-discrimination DETECTION** (chain_hash as the integrity-independent signal; fail-closed on CASE b) | REC-225, 226, 231, 232 (fail-closed half) | **app-bootstrap milestone** (carries C2 fail-closed + C1 auth + C9) |
| **Cause-discrimination DEGRADE** (CASE a; shred tombstone; DegradedEvent-by-cause) | REC-224, 227, 232 (degrade half), Stage-2 items 1/3/4 | **crypto-shred work unit** (post-MVP per Doc 15 §3.6 — design now ready) |
| **Strategic / Tier-2 (FUTURE)** | REC-222, 223, 229, 230, Stage-3 | LTD-01-adjacent strategic ledger — **not MVP** |

### Strategic / FUTURE (parked, not MVP)
- **AES-256-GCM-SIV (RFC 8452)** would downgrade R-α from blocking→advisory (nonce reuse reveals only plaintext equality, not catastrophic). Cost: Informational status, two-pass/non-online, not FIPS-validatable today. **Threshold note (REC-222/Stage-1):** a *mere* extended-nonce move (XAES-256-GCM) does **not** meet the bar — by its own spec it is "not nonce misuse-resistant, nor key-committing." Park as a Tier-2 crypto-agility option.
- **Committing-AEAD / Encrypt-then-MAC wrapper** (Stage-3 item 1) to close the non-committing-AEAD surface under REC-231 — Tier-2 hardening.
- **Track SP 800-38D Rev.1** (the pre-draft process) for an approved nonce-derivation / 256-bit-block mode — watch item (subject to the verification flag above).

## Escalations to Nick
1. **Doc 15 §6 currency amendment** (rotate-DEK-on-restore binding; (b) cross-check) — ratify to close OR-M6-NONCE restore-half. Recommended option; it's a refinement among existing Doc-15 options, not a supersession.
2. **Register the shred tombstone + cause-discriminated read contract** as design inputs on Doc 15 §3.6/§6 (forward note) so the crypto-shred WU and app-bootstrap milestone build against them.
3. **Confirm or wave the strategic-tracking flag** (the June-2026 wGCM second-pre-draft) — non-blocking.

## Closeout actions (PM)
- Raw return REHOMED → `homesynapse-core-docs/research/returns/2026-06-15_Research_R-alpha_Restore_Nonce_Monotonicity_and_Cause-Discriminated_Read_Contract.md`.
- Side-research status: **R-α → ASSESSED** (update `context/planning/2026-06-13_side-research-candidates_CORE-DOCS.md` + the converge `2026-06-15_M7-plus_research-avenues.md` dispatch order). Next side-research dispatch per the endorsed order = **R-β** (GraalVM native-image / Gen-ZGC Pi spikes — CORE empirical).
- REC high-water → **235** (was 215).
- This disposition is **not on the M7 critical path** — it serves the parallel crypto / app-bootstrap track. M7.x is unaffected.

## Commit message (handed to Nick — `!`-free)
```
docs(research): assess R-alpha/NEW-1 return (grade A) + rehome

PM assessment + disposition of the restore nonce-monotonicity (R-alpha) +
cause-discriminated read-path (NEW-1) survey. Grade A: primary-sourced,
steelmans both extremes, defeats the forged-intended-signal objection via the
chain_hash-over-stored-bytes invariant. No fabricated internals.

Disposition: rotate-DEK-on-restore is the BINDING restore contract (carry-
high-water-mark = cross-check only) -> closes OR-M6-NONCE restore-half via a
Doc 15 section-6 currency amendment (Nick ratifies). Cause-discriminated read
contract adopted: CASE-a intended-shred (chain-valid + recorded tombstone) ->
degrade-to-DegradedEvent; CASE-b unintended (GCM-auth-fail/missing-key/chain-
fail) -> fail-closed. This sharpens the converge C2 fix (a flat catch-and-
degrade is wrong). New primitive: chain-covered shred tombstone.

REC-216..235 routed: app-bootstrap milestone (restore/nonce + fail-closed
detection) + crypto-shred WU (degrade half + tombstone). GCM-SIV / committing-
AEAD / SP 800-38D Rev.1 parked Tier-2. REC high-water -> 235. Not on the M7
critical path.

Files: context/assessments/2026-06-15_Research_R-alpha_PM_Assessment.md;
docs research/returns rehome.
```
