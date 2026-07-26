<!--
file: context/instructions/2026-06-15_Research_Key-Portability_Backup-Recovery_DOCS_Brief.md
purpose: DOCS-Project research brief — the R-δ §5 #1 follow-up (PM-graded HIGH). Web-grounded design study of a machine-local-root -> portable-recovery bridge for an event-sourced, per-scope-encrypted store: how a user recovers their encrypted corpus after hardware loss/migration WITHOUT stranding (the HA #134162 lesson), while preserving per-scope crypto-shred erasure and the local-first / no-mandatory-cloud trust brand.
audience: DOCS-Project researcher (fresh conversation, web search required) -> PM serialized assessment on return
state-type: research brief (READY TO DISPATCH — Nick veto-or-default)
status: AUTHORED 2026-06-14 (Track-4; the R-delta AX-4 follow-up). Dispatch BEFORE the Track-2 app-bootstrap charter finalizes the payloadCipher-activation beat + the AB-4 backup-key-portability seam; design the bridge BEFORE users accumulate an encrypted corpus.
routing: DOCS Project (design/architecture). Code-empirical sub-questions are flagged and routed to a CORE spike, NOT answered here.
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4; M6.3 at-rest payload encryption LANDED GREEN but INERT — main() is a stub, zero encrypted rows exist yet); machine-local-root per Doc 15; per-scope DEK + durable counter-nonce shipped M6.2/M6.3; docs watermark AMD-93; Doc 15 LOCKED.
consumes: R-delta competitive deep-dive (AX-4 backup-key-portability finding — HA made encrypted backups mandatory and STRANDED users; Nabu Casa does not store the key; hardware-migration key bug Issue #134162) + its PM assessment (sec.5 #1 = HIGH); the R-alpha backup/restore crash-safety lane (the M6.3 restore-half, DP-D non-preclusion only); Doc 15 (machine-local-root, per-scope KEK/DEK, crypto-shred erasure).
adversarial-posture: this is a DESIGN-STUDY brief, not a challenge brief. But hold one anti-goal in tension throughout: any recovery mechanism that reintroduces a mandatory cloud, a vendor key-escrow, or a single master key that defeats per-scope crypto-shred is a FAILURE, not a solution. Reward = a mechanism that recovers the corpus without any of those three.
-->

# RESEARCH BRIEF: Key-Portability — the machine-local-root -> portable-recovery bridge

## Why (the finding this answers)

R-delta's AX-4 is the most actionable near-term crypto finding in the competitive return: **Home Assistant made encrypted backups mandatory and stranded users** — "no way to restore… Nabu Casa does not store your key" — and shipped a hardware-migration key bug (Issue #134162) that locked owners out of their own encrypted history. HomeSynapse's posture is stronger on paper (machine-local-root, per-scope DEKs, durable counter-nonce, crypto-shred erasure — all shipped M6.2/M6.3) but it has **the same latent failure**: if the machine dies, what recovers the encrypted corpus? Today the root is machine-local with no portable recovery artifact. **The window to fix this cheaply is now** — `main()` is a stub, zero encrypted rows exist; once users accumulate an encrypted corpus on an immutable, hash-chained log, any recovery design becomes a migration problem instead of a design choice. This brief produces the design input for the app-bootstrap charter's `payloadCipher`-activation beat and the **AB-4 backup-key-portability seam**, and for the R-alpha backup/restore WU.

## The decision under examination

**How should HomeSynapse let a user recover their per-scope-encrypted corpus after hardware loss or migration, without (a) stranding them, (b) defeating per-scope crypto-shred erasure, or (c) introducing a mandatory cloud / vendor key-escrow?**

Ground truth to respect (LOCKED / shipped — do not re-litigate):
- Machine-local-root: a 0400 `.root-key`, per-scope KEKs via RFC-5869 HKDF, AES-256-GCM-wrapped DEKs in `scope_keys.json` (Doc 15; M6.2).
- **Crypto-shred erasure:** destroying a scope's key destroys that scope's data (the erasure primitive). Any recovery artifact MUST preserve this — recovering "everything" must not resurrect a crypto-shredded scope.
- No mandatory cloud; user-owned keys is a trust-brand property (R-delta AX-9). A recovery mechanism may *offer* optional user-chosen off-box storage, but must not *require* a vendor service.

## Research questions (web-grounded; cite primary sources)

1. **The stranding post-mortem (the anti-pattern, in detail).** What exactly went wrong with HA/Nabu-Casa encrypted-backup recovery and Issue #134162 (and any comparable: Bitwarden/1Password account-recovery, Signal SVR/PIN, Apple Advanced Data Protection recovery-key + recovery-contact, Standard Notes, Proton)? Extract the specific design choices that strand users vs the ones that recover them.
2. **Recovery-artifact designs that preserve per-scope crypto-shred.** Compare: (a) a single master recovery key that wraps the root; (b) a recovery key that wraps each per-scope KEK independently (shred-preserving — a destroyed scope KEK is simply absent from the artifact); (c) Shamir secret sharing / social recovery; (d) a user passphrase-derived recovery key (Argon2id) layered over the machine root. Which preserve "destroy the scope = gone, even from the backup"? Which break it?
3. **The portable artifact + UX.** BIP39-style mnemonic vs printed recovery code vs exported keyfile vs hardware token (FIDO2/PIV). What is the field-proven floor for "a non-expert can actually recover a year later"? What is the honest threat-model framing (machine-local-root is disk-theft Tier-2 only; a user-held recovery phrase changes that surface — state it plainly, per AX-3)?
4. **Hardware migration (the #134162 class).** What makes restore-on-new-hardware work for an event-sourced, append-only, hash-chained, per-scope-encrypted store? How does the recovery artifact rebind to a new machine-local-root without re-encrypting the whole corpus or breaking the hash chain / counter-nonce monotonicity (OR-M6-NONCE)?
5. **Interaction with backup/restore crash-safety (R-alpha).** The restore-half is already re-homed to R-alpha (M6.3 is DP-D non-preclusion only). Where does key-portability belong relative to it — same WU, or a distinct recovery-artifact layer above it? Flag any tension with DEK-rotation-on-restore.
6. **Minimal-now vs defer.** What is the smallest mechanism that must be DESIGNED now (so the on-disk format / activation beat leaves room for it) vs IMPLEMENTED later? The cost of getting the format wrong now is a corpus migration; the cost of implementing later is just schedule.

## Deliverable (what the return must contain)

- A **recommended bridge mechanism** (machine-local-root -> portable recovery), stated concretely enough to land on the app-bootstrap charter's AB-4 seam: the recovery-artifact shape, how it wraps keys (per-scope, shred-preserving), the derivation (if passphrase-based), the migration/rebind flow, and the honest threat-model wording.
- A **two-lens table** per comparable system (the mistake that strands + the strength that recovers), each mapped to a HomeSynapse design choice.
- An explicit **crypto-shred preservation proof-sketch**: show that the recommended artifact cannot resurrect a crypto-shredded scope.
- The **minimal-now set** (format/activation-beat requirements) vs the deferrable implementation, so the charter can scope AB-4 without over-building.
- **CORE-spike flags** for anything empirical (e.g., counter-nonce monotonicity across a restore-rebind) — routed to a spike, not answered here.

## Scope fences

- **Respect the R-gamma boundary.** R-gamma owns the envelope algorithm/version-discriminator (the 1-byte tag) question; this brief does NOT re-fight it. Assume R-gamma's outcome as a separate input; design the recovery artifact to be agnostic to it.
- **No mandatory cloud, no vendor escrow, no single-master-key that defeats crypto-shred** — the three anti-goals. A mechanism that needs any of them is a non-answer.
- **Web-grounded, primary sources.** Maintainer post-mortems, official recovery docs, CVEs/issue trackers, cryptographic-engineering references. Label and grade secondary/community sources. Declare connector-blind + the call-budget ceiling; name thin spots and turn them into follow-ups.
- **Design study, not a decision.** The return recommends; the PM routes it into the AB-4 seam + R-alpha; Nick decides.

## Done-when

A return that hands the PM a concrete, crypto-shred-preserving, cloud-optional recovery-bridge recommendation (artifact shape + migration flow + honest threat model + minimal-now-vs-defer split), two-lens-mapped to the field's stranding lessons, with empirical sub-questions flagged to a CORE spike — enough for the app-bootstrap charter to scope AB-4 and for R-alpha to scope the restore-half without re-opening the on-disk format later.
