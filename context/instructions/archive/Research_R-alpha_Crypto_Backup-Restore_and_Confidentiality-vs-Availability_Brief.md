<!--
file: context/instructions/Research_R-alpha_Crypto_Backup-Restore_and_Confidentiality-vs-Availability_Brief.md
purpose: DOCS-Project research brief — R-α (crash-safe backup/restore for the event-sourced + per-scope-encrypted store) with NEW-1 folded (the confidentiality-vs-availability contract for a read-path decrypt failure). Returns the design inputs the crypto-shred WU and the backup/restore feature need BEFORE either is scoped. Parallel to the M7 track; NOT M7-blocking.
audience: DOCS-Project researcher (fresh conversation, web search required) → PM serialized assessment on return
state-type: research brief (READY TO DISPATCH — Nick veto-or-default)
status: AUTHORED 2026-06-15 (Cowork PM, converge follow-on). Dispatch order: FIRST of the standing side-research set (R-α + NEW-1), endorsed by the 2026-06-15 converge.
routing: DOCS Project (design/architecture). Code-empirical sub-questions are flagged and routed to a CORE spike, NOT answered here.
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4; M6.3 at-rest payload encryption LANDED GREEN); docs watermark AMD-93; invariants 163/47; Doc 15 LOCKED.
consumes: side-research-candidates R-α (2026-06-13) + NEW-1 (converge research-avenues 2026-06-15) + OR-M6-NONCE restore-half + the converge C2/F-A1 finding.
-->

# RESEARCH BRIEF: R-α — Crash-Safe Backup/Restore + the Confidentiality-vs-Availability Contract for an Event-Sourced, Per-Scope-Encrypted Store

**Register:** engineering / systems-design (DOCS Project). Web search required. Connector-blind is acceptable — declare it and list the gaps.

**The load-bearing deliverable is the §4 disposition: two design recommendations, each defensible against the cited invariants and failure modes — (R-α) a backup/restore design that preserves GCM nonce-monotonicity across restore, and (NEW-1) the read-path confidentiality-vs-availability contract.** A "best practice" with no position against HomeSynapse's actual constraints (immutable log, per-scope DEKs, counter nonces, fail-closed write path) is unusable. A recommendation that contradicts a Locked invariant poisons the pipeline.

**Why this brief exists now.** M6.3 (at-rest payload encryption) has LANDED. Its write-path nonce durability is solved (OR-M6-NONCE half (a)). Two design beats remain open and *both gate near-future work that is NOT on the M7 critical path*: the **restore half** of nonce-monotonicity (OR-M6-NONCE half (b)) and the **read-path failure contract** (the converge C2/F-A1 HIGH finding). The converge ranked this **the single highest-leverage near-term DOCS research item** and folded NEW-1 into R-α's scope. It runs **in parallel** to the M7 automation track and to Nick's energy/erasure interviews — it competes for nothing on the critical path.

---

## 0. Quote-back gate [DO THIS FIRST]

Before any research, echo back the following **verbatim** in your return's §0, then state in one line per item that you have read and will hold it as ground (not re-litigate it). This proves you are gap-relative to the real design, not working from a generic crypto-backup prior. Do **not** paraphrase these — copy them, then react.

**QB-1 — Doc 15 §6, the catastrophic failure-mode row (verbatim):**
> **Counter-nonce reuse across crash/restore — [BLOCKING-for-M6-impl]** | the per-scope nonce counter repeats after a crash, **or** a restored backup reintroduces a counter value already used under the same DEK | **Catastrophic:** (key, nonce) reuse breaks AES-GCM confidentiality *and* authentication for that scope | The per-scope counter **must be durable and strictly monotonic across crash AND restore**: persist the counter high-water mark atomically with (or ahead of) the encrypted write; on boot re-init from the persisted max, never from memory. The deferred backup/restore feature (foundation-readiness F3) **must be co-designed** so a restore can never resume a scope at a counter ≤ any value already used under that DEK (rotate the DEK on restore, or carry the high-water mark in the backup). **Corollary to F-A:** "key-excluding backups are protected" holds only if the backup excludes (or separately wraps) the root key — a backup carrying ciphertext + counter state but *not* the key is safe; one carrying the key is not.

**QB-2 — Doc 15 §3.4, nonce discipline (verbatim):**
> **Nonce discipline:** counter-based deterministic 96-bit nonces per scope (stored alongside the DEK) — never random — to avoid the GCM birthday bound (random nonces collide at ~2³² per key; at 1k events/s on one scope that is ~50 days).

**QB-3 — the converge C2 / F-A1 finding (the read-path beat NEW-1 must settle), verbatim from `context/audits/2026-06-15_core-review_CONVERGE_synthesis.md`:**
> a read-path decrypt failure throws and aborts the whole replay — no per-row `DegradedEvent` degrade like codec failures get. The moment `main()` activates `payloadCipher`, a lost/corrupt key makes the store unreplayable (vs INV-RF-04), and the future crypto-shred breaks replay (vs INV-PD-07).

**QB-4 — the OR-M6-NONCE status (verbatim from `context/handoff/pm-handoff.md`):**
> the write-path half (a) is **DISCHARGED** … The restore half (b) **remains OPEN**, re-homed to side-research **R-α** … M6.3 only "does not preclude" DEK-rotation-on-restore (instruction DP-D); the full backup/restore co-design (foundation-readiness F3) carries the remaining obligation.

If any quote-back no longer matches the cited source at dispatch, STOP and flag it — do not proceed on a stale anchor.

## 0.1 Authoritative state (do not work from memory)

- **HEAD `1eddd9a`** — M6.3 at-rest payload encryption LANDED GREEN (full `./gradlew check`, 147 tasks). M6 is COMPLETE (4-of-4). Docs watermark **AMD-93**; invariants **163/47**; Doc 15 (Cryptographic Architecture) **LOCKED**.
- **Encrypted scopes (OQ-15-2 RESOLVED):** `[identity, presence_personal]` — confirmed default, no fallback. Both categories encrypt-on-write. Non-sensitive telemetry stays plaintext-at-rest at MVP.
- **What shipped at M6.3:** per-scope DEKs (AES-256-GCM), wrapped by `HKDF-SHA256(root, "scope:"+id)` KEKs; the durable per-scope counter-nonce high-water mark (fsync-ahead-of-return, re-init from persisted max on boot); the Doc 15 §13.4 kill-mid-encrypt nonce-monotonicity test GREEN.
- **What is NOT built (the consumers of THIS research):** (1) the **backup/restore** feature itself (foundation-readiness F3 — deferred); (2) the **crypto-shred operation** (the `destroyed_at` field + the decrypt guard exist; the KEK-destruction API does not — Doc 15 §3.6, operation post-MVP); (3) **`main()` runtime activation** of `payloadCipher` (app-bootstrap milestone — the cipher is wired only in tests today, so the crypto is shipped-but-inert).
- **This is a DESIGN brief.** Nothing here is implemented by the researcher. Code-empirical questions (e.g., per-event fsync cost) are flagged and routed to a CORE spike (NEW-3 / CC-2), not answered.

## 0.2 Source ground (verified at HEAD `1eddd9a` this session — hold as fact, do not re-derive)

The JPMS / write-path facts your design must respect. These are source-verified; if your design needs a different shape, name it as a *delta with rationale*, do not assume it.

- **`PayloadCipher` is a consumer-defined interface in `com.homesynapse.persistence`** (`PayloadCipher.java:36`): `EncryptedPayload encrypt(String scopeId, byte[] plaintext)` (`:47`) + a decrypt counterpart; `EncryptedPayload` is a `java.base`-only record (`EncryptedPayload.java:34`). **Persistence does NOT `requires com.homesynapse.config`** and config does not require persistence — the cycle is closed in both directions (Doc 15 §3.8).
- **The key manager lives in `com.homesynapse.config`** (`ScopeKeyManager`); the **adapter that bridges `ScopeKeyManager` → the persistence-exported `PayloadCipher`** is constructed in the composition root **`com.homesynapse.app` (`Main`)** — the only module that already `requires` both config and persistence (Doc 15 §3.8). The `scope_keys` store and the durable nonce-counter state are owned on the **config / key-manager side**.
- **The read path (the C2/F-A1 site):** `SqliteEventStore.fromRow` routes any `dek_ref`-bearing row through `decryptStoredPayload` (`SqliteEventStore.java:808` → `:896`), which **throws `IllegalStateException`** on missing cipher (`:899`) or malformed `dek_ref` (`:906`) — with **no per-row catch**, so one undecryptable row fails the whole `readRows` batch. This deliberately contrasts with the category-decode fallback at `:846` ("SYSTEM so the read still succeeds (matches DegradedEvent posture)") and the class Javadoc at `:88` (parse failure → `DegradedEvent` so the read continues).
- **The chain covers stored bytes** (Doc 15 §5): encrypting a scope or destroying its key does **not** alter stored bytes and does **not** invalidate any `chain_hash`. Integrity is independent of encryption and of shredding. This is the property that makes per-scope crypto-shred coherent on an immutable log.

## 0.3 Decided ground — your recommendations must be gap-relative to these (do not re-open)

- **The log is immutable and event-sourced.** Backup/restore operates on an append-only event store with a hash chain from genesis (INV-PD-08). A restore reconstitutes state from events; it does not mutate history.
- **Nonces are counter-based per scope, never random** (QB-2). This is a Locked decision (the birthday-bound rationale). Any restore design that could re-issue a counter value already used under a live DEK is a **catastrophic** defect, not a tradeoff (QB-1).
- **Root-key loss is data loss by design** (Doc 15 §5: "Without the root key … encrypted scopes are irrecoverable. Chain verification and package-signature verification remain fully functional"). Crypto-shred *intends* unreadability. So "the data won't decrypt" is sometimes **correct behavior**, not a fault — the contract you design must distinguish *intended* unreadability (shred / key-excluded backup) from *unintended* loss (corruption / misconfiguration).
- **The MVP threat model** (Doc 15 §3.5): machine-local root key on the same medium; protects key-excluding copies + less-privileged process reads; does **NOT** protect against medium theft or on-device-root. Media-theft + user-owned-key resistance is a Tier-2 property (passphrase- or TPM-derived root). Do not design a backup story that quietly overclaims media-theft protection.
- **Anti-requirements (bind all recommendations):** no destructive forced migration (REC-151); fail-closed over silent fallback (Doc 15 §6 "no silent plaintext fallback"); zero new dependencies on the MVP path unless explicitly justified (SHA-256/AES-GCM/Ed25519 are JDK-intrinsic; a Tier-2 Argon2id KDF is the one sanctioned exception — OQ-15-3).

---

## 1. Research questions (answer ALL; engineering register, cite prior art + the cited HomeSynapse ground)

### Part A — R-α: crash-safe backup/restore (the OR-M6-NONCE restore half)

**RQ-A1 — Nonce-monotonicity across restore.** For a per-scope AES-256-GCM store with deterministic counter nonces, what backup/restore design *guarantees* a scope can never resume at a counter ≤ a value already used under that DEK? Compare at least: **(i) DEK-rotation-on-restore** (the restored scope gets a fresh DEK + reset counter; old ciphertext re-wrapped or re-encrypted), vs **(ii) carry-the-high-water-mark-in-backup** (the backup records the counter high-water per scope; restore re-inits strictly above it). State the failure surface of each (e.g., restoring an *old* backup onto a system that has since advanced the counter; restoring onto a *different* device; partial/interrupted restore). Which is robust under crash *during* restore?

**RQ-A2 — Crash-atomicity of the restore itself.** What makes a restore crash-atomic for an event-sourced store with a hash chain + a separate key/nonce-counter store? Prior art for atomic multi-file restore (the event DB + `scope_keys` + the nonce-counter state must be mutually consistent — a restore that lands events but not the advanced counter, or vice versa, is the exact catastrophic window). How do mature systems sequence/fence this (staging dir + atomic rename, restore journal, two-phase, fsync ordering)?

**RQ-A3 — Partial / per-entity / per-scope backfill.** Doc 15 + OQ-05-07 flag partial backfill as a residual. What designs support restoring *a subset* (one scope, one entity, a time range) without violating chain continuity or nonce-monotonicity? Is partial restore even coherent on a single hash chain, or does it require a documented epoch break (cf. the AMD-37 zero-hash epoch-break precedent)? Take a position.

**RQ-A4 — Key material in backups.** Per QB-1's F-A corollary: a backup carrying ciphertext + counter state but *not* the root key is safe; one carrying the key is not. What is the recommended posture for the **root key** in a backup (exclude entirely; separately wrap under a passphrase/Tier-2 KDF; user-exported out-of-band)? How does this interact with the "media-theft is Tier-2" threat model — i.e., can backup ever be the vector that *introduces* the user-owned-key property ahead of the Tier-2 root, and should it?

### Part B — NEW-1: the read-path confidentiality-vs-availability contract (the converge C2/F-A1 HIGH)

**RQ-B1 — Degrade-per-row vs fail-closed-whole-store.** On a read-path decrypt failure, what is the right contract: emit a per-row `DegradedEvent` (replay continues, the undecryptable event is marked degraded) — mirroring the existing codec-parse-failure posture (`SqliteEventStore.java:846`/`:88`) — vs the current throw-and-abort-the-whole-replay? Survey how event-sourced + encrypted systems (and adjacent: encrypted WAL/replication, encrypted append-only logs) handle an un-decryptable record on replay. **The decisive sub-question:** the contract must differ by *cause* — distinguish (a) **intended** unreadability (crypto-shred destroyed the KEK; a key-excluding backup was restored) → degrade-and-continue is almost certainly right (the data is *meant* to be gone, the store must stay replayable — INV-RF-04); from (b) **unintended** unreadability (root key missing/corrupt at boot, GCM auth failure on otherwise-present data) → fail-closed may be right (something is wrong; silently degrading hides corruption). Propose the decision tree.

**RQ-B2 — INV-RF-04 vs INV-PD-07 collision.** The converge frames the collision: degrade-per-row serves **INV-RF-04** (the store stays replayable/recoverable even across a shredded event) but a careless degrade could mask a real integrity problem; fail-closed serves integrity but makes a single lost key a whole-store-unreplayable event (and makes crypto-shred *break replay* — directly against the point of INV-PD-07's shred-without-breaking-the-chain design). Resolve: what contract honors *both* invariants? (Hint to test against, not to assume: the chain covers stored bytes and stays valid across shred — Doc 15 §5 — so a `DegradedEvent` for a shredded row need not break integrity; the open question is detection + signalling, not chain validity.)

**RQ-B3 — `DegradedEvent` semantics for the crypto case.** If degrade-per-row wins for the shred/key-excluded case: what should the `DegradedEvent` carry (scope_id, dek_ref, reason ∈ {shredded, key-absent, auth-failed}, position)? What downstream consumers (state projection, REST read, integrity health, observability) must be told, and how does this interact with the integrity indicator (Doc 15 §3.3 RED-on-mismatch) so a *legitimate* shred does not light up as an integrity violation? What is the operator-facing signal that distinguishes "this is your erasure working as designed" from "your key is corrupt"?

**RQ-B4 — Interaction with the crypto-shred operation (the consuming WU).** Doc 15 §3.6 makes crypto-shred a post-MVP operation (the schema seam is MVP). Given your RQ-B1/B2 contract, what must the crypto-shred operation guarantee on the *read* side so that shredding a scope is a clean, replay-safe, observable transition rather than a store-breaking event? This is the direct hand-off to the crypto-shred coding instruction.

---

## 2. Mandatory return document format

Save the return to `homesynapse-core-docs/research/returns/` (PM rehomes/assesses on intake). Structure:

```
# R-α: Crash-Safe Backup/Restore + Confidentiality-vs-Availability — DOCS Research Return

## 0. Quote-back gate [M — FIRST]  — QB-1..QB-4 verbatim + one-line "held as ground" each.
## 1. Executive Summary [M]  — 6–10 verdict bullets; each TAKES A POSITION (recommend X over Y because Z),
                                not "it depends". Lead with the RQ-A1 and RQ-B1 recommendations.
## 2. Prior-Art Deep Dives [M]  — one subsection per system/domain surveyed (encrypted event stores,
                                  encrypted WAL/replication, backup-restore of keyed stores, GCM nonce
                                  management in practice). What each does, with citations.
## 3. Cross-Cutting Analysis [M]  — the nonce-monotonicity-across-restore matrix (RQ-A1 options × failure
                                    modes); the degrade-vs-fail-closed decision tree (RQ-B1) keyed by cause.
## 4. Findings + Recommendations [M — THE DELIVERABLE]  — a disposition table:
       ID | question (RQ) | recommendation | rationale vs the cited invariant/failure-mode | confidence | consuming WU
       The two headline rows: R-α restore design (RQ-A1/A2) and the NEW-1 read contract (RQ-B1/B2).
## 5. Caveats and Open Questions [M]  — source reliability; anything that needs a CORE empirical spike
                                       (flag it as such — e.g., per-event fsync cost = NEW-3/CC-2, do NOT
                                       attempt to measure); residual OQ-05-07 backfill items.
## 6. Appendix: Sources [M]  — URL families grouped by system; every factual claim traceable.
```

## 3. Evidence standards (non-negotiable)

- Every external claim carries a citation (URL family + enough specificity to verify). NIST SP 800-38D (the GCM nonce-reuse / construction constraint) is the canonical anchor for the nonce questions — cite the relevant §8.x.
- Distinguish **standard / spec** (NIST, RFC) from **field practice** (a given system's docs/source) from **your inference**. Label inferences.
- No fabricated HomeSynapse internals. The only HomeSynapse facts you assert are the ones quoted/cited in §0 of this brief; if a recommendation needs a HomeSynapse detail not in §0, name it as an *assumption to verify with the PM*, do not invent it.
- A recommendation that contradicts a Locked invariant (INV-PD-03/07/08, INV-RF-04, the §6 catastrophic row) must say so explicitly and argue the amendment case — it does not get to silently assume the invariant away.

## 4. Guardrails (violations = the finding is discarded)

- **Stay design-level.** Do not write HomeSynapse code. Code-empirical questions are routed to a CORE spike, not answered here.
- **Gap-relative, not generic.** "Use authenticated encryption" / "test your backups" are non-findings — the system already does AEAD and tests the write path. Every finding is relative to a §0.3 decided-ground item or names a specific delta.
- **Respect the immutable log + counter-nonce decisions.** A recommendation that re-randomizes nonces, or mutates stored events, or silently falls back to plaintext, is discarded — those are Locked.
- **Fail-closed bias.** Where the contract is genuinely ambiguous, the HomeSynapse default is fail-closed + loud diagnostic over silent degrade — argue against this only with strong, cited reason.

## 5. What the PM does with the return (so you aim at it)

The PM assesses serially on return (the established cycle), grades it, and routes the §4 dispositions: the **RQ-A1/A2 restore design** closes the OR-M6-NONCE restore half (b) and seeds the backup/restore feature (foundation-readiness F3); the **RQ-B1/B2 read contract** becomes the design beat the **crypto-shred coding instruction** and the **app-bootstrap milestone** (which activates `payloadCipher` and makes C2 live) are built against. **NEW-1's answer is a prerequisite for the crypto-shred WU and de-risks the C2 HIGH** — that is the leverage. Neither consuming WU is on the M7 critical path, so this return can mature in parallel with M7.x.

---

## Routing & dispatch note

**DOCS Project, fresh conversation, web search required.** This is the FIRST dispatch of the standing side-research set (R-α + NEW-1), per the converge's endorsed order (R-α first, then R-β CORE, then R-γ DOCS). It is fully unblocked now and parallel to both the M7 track and the energy/erasure interviews — dispatch it this week to put the research long-pole in the water; it does not compete for the Coder or the ratification gate. **R-β** (GraalVM native-image / Gen-ZGC Pi spikes — CORE empirical) is the recommended next dispatch after this one. **NEW-3 / CC-2** (per-event fsync cost on the Pi-4 floor) is tracked, NOT dispatched — it fires only when widening `encrypted_scopes` is contemplated.
