<!--
file: context/instructions/2026-06-28_AB-4_cipher-activation_coding-instruction.md
purpose: The AB-4 coding instruction — activate the at-rest payload cipher (the last Seam-1 piece) on the live composition root: flip Main to the 6-arg HomeSynapseCore ctor (M6.3 at-rest encryption goes live for [identity, presence_personal]); land the F1 1-byte envelope version discriminator (v1, prefix-in-envelope + GCM AAD); enforce F3 one-nonce-construction-per-scope; make the F13b nonce-counter dir-fsync fail-closed (scoped to not break Windows); document the backup-key portability seam. The ready, un-gated M9-prerequisite (leapfrog M7.5c, Nick-ruled 2026-06-28).
audience: the Coder (Claude Code); Nick (runs the gate + routes); the v11 PM hub (authored from a source-verified grounding packet; reconciles the return).
status: ISSUE-READY (authored 2026-06-28 by the v11 hub against COMMITTED core HEAD eed477e, from a source-verified grounding pass). AMD-94 RATIFIED + folded (the prior ⛔-gate is CLEARED).
baseline: core eed477e (M7.5b committed; AB-1 auth + AB-2 fail-closed read + M6.3 at-rest write-path + the F13a write guard ALL LANDED — AB-4 is the cipher-activation remainder, much smaller than the 2026-06-19 spec). docs 75d0345 (Doc 15 LOCKED; AMD-94 folded f6c0c64; watermark AMD-94). Re-verify HEAD at issue.
supersedes-in-part: context/instructions/2026-06-19_AB-1-AB-2-AB-4_Seam-1_go-live_coding-instruction.md (its AB-4 section — re-derived against eed477e; that instruction's gate framing, line numbers, and STOP-gates are STALE; see §Drift).
zero-mint: AB-4 mints NO event types (71/41/53 hold), adds NO module-info edge, and — with the F1 prefix-in-envelope encoding (AMD-94's recommended default) — needs NO schema migration. It activates an existing path; it does not add one.
grounding: authored from a 2026-06-28 source-verification grounding pass against eed477e (every signature/site/quote below re-derived from live source; drift from the 2026-06-19 instruction reconciled in §Drift).
-->

# Coding Task: AB-4 — cipher activation (the last Seam-1 piece)

**Subsystem:** app (composition-root activation) + config (the scope-key manager: F3, F13b) + persistence (the F1 envelope version byte on the write/read path). **Design Doc:** Doc 15 (Cryptographic Architecture) — **LOCKED** (AMD-94 folded, watermark AMD-94). **Phase:** 3-Implementation. **Task Brief Reference:** the V1 launch-scope record (Seam-1) + the Core sequence (the ruled leapfrog: AB-4 before M7.5c, ahead of M9).

## What This Implements

M6.3 built the at-rest event-payload encryption path (AES-256-GCM, per-scope DEK, counter nonce) for `encrypted_scopes = [identity, presence_personal]` — but it is **inert**: `Main` constructs `HomeSynapseCore` with a `null` cipher, so `SqlitePersistenceLifecycle` runs plaintext-for-all. **AB-4 activates it** — the trust-hygiene hard-order step that must land **before M9** writes the first real device data, because the immutable log is encrypted-from-genesis or never (you cannot retro-encrypt a log; the now-or-never property). AB-4 is five obligations, all small: (1) flip the cipher on; (2) reserve the F1 1-byte envelope version discriminator (`v1`) so the at-rest format is forward-evolvable from the first encrypted byte; (3) enforce F3 (one nonce construction per scope — the GCM nonce-reuse guard); (4) make the F13b nonce-counter directory fsync fail-closed; (5) document the backup-key portability seam. It is **zero-mint, zero-edge, zero-DDL** (with the recommended F1 encoding).

## ⚠ Drift — reconcile against `eed477e`, NOT the 2026-06-19 instruction (read this first)

The 2026-06-19 AB-1/AB-2/AB-4 instruction was authored against `60d50ce` and treats AB-4 as ⛔-gated with AB-1/AB-2/M6.3 still ahead. **That is all stale.** At `eed477e`, source-verified:
1. **The gate is CLEARED** — AMD-94 is RATIFIED + folded into Doc 15 (`f6c0c64`); watermark AMD-94. Discard all ⛔/HELD framing.
2. **AB-1 (auth + loopback bind) and AB-2 (typed `PayloadDecryptionException` fail-closed read) have LANDED.** `HomeSynapseCore` Phase 5 already `bringUpHttpSurface()` auth-gates + loopback-binds; the read path already throws the typed exception. The old instruction's STOP-gate table describes the pre-AB-1 source and will mismatch on every HTTP/auth/read row — **ignore it; use the gates in this instruction.**
3. **M6.3 write-path + the durable nonce counter (`scope_nonce_counters.json`) + the F13a write guard have LANDED** (`SqliteEventStore` throws if an encrypted scope has no cipher). So AB-4's A4.4(a) is largely already satisfied — verify, don't rebuild.
4. **Genuinely unbuilt (the real AB-4 work):** F1 (the envelope version byte — no `EncryptedPayload`/`ScopeCipherResult` field and no column carries it today), F3 (the nonce-construction fence is documentation-only), and F13b (the dir-fsync is swallowed at DEBUG).
5. **Line numbers in the old instruction are from `60d50ce` and have shifted** — re-cite at `eed477e` (the gates below carry the current lines).

## Settled Decisions (AMD-94, RATIFIED — not open questions)

- **DP-1 — Cipher activation = the 6-arg ctor.** In `Main.main()`, switch to `new HomeSynapseCore(dbPath, configDir, HomeSynapseConfig.HOME_DEFAULT, clock, homeId, payloadCipher(configDir, clock))`. The `payloadCipher(...)` adapter already exists and already calls the counter path (`encryptPayload`) — it is held-not-consumed. This single change flips `SqlitePersistenceLifecycle`'s cipher-presence gate (`payloadCipher != null` → `encryptedScopes = [identity, presence_personal]`). Fix the three stale "five-argument ctor" Javadoc/comment nits in `Main`.
- **DP-2 — F1 = a 1-byte version discriminator, `v1` = the current envelope, prefix-in-envelope + GCM AAD (AMD-94 §2.2 recommended default).** Emit the discriminator as the **first byte of the stored AEAD envelope** (so it is chain-covered once the chain is live) AND **bind it as GCM AAD** (so the auth tag covers it → downgrade-resistant). `v1` = AES-256-GCM, 96-bit per-scope counter nonce, per-scope DEK — exactly Doc 15 §3.4 today. **This encoding is zero-DDL** (no `envelope_version` column; the byte rides the existing `payload` BLOB). Do **not** invent the slot's meaning beyond `v1`, and do **not** default-by-omission (an absent/unknown leading byte is a hard decrypt failure, not an implicit `v1`).
  - **Honesty caveat (Doc 15 §2.3, AMD-94 §2.3):** the AAD/chain tamper-evidence is only *real* once `chain_hash` is live; `chain_hash` is **ZERO today**. AB-4 reserves the byte + binds it as AAD (downgrade-resistance is real now via the tag); it must **not** claim chain-coverage tamper-evidence in logs/docs until chain activation (post-MVP).
- **DP-3 — Rotate-DEK-on-restore is additive (AMD-94 §2.1, folded Doc 15 §3.4/§6).** Carry the boot invariant (R-α REC-235): the engine **refuses to encrypt in a scope** until either a fresh DEK version is installed (the restore path) or the persisted counter is proven ≥ all prior nonces under the active DEK version (the crash-recovery path). Rotate = additive new `scope_keys` row (`key_version` = prior max + 1); **retain all priors; never re-encrypt or overwrite** (F6). AB-4 carries this as the seam contract; the restore *mechanics* are the backup/restore WU (A4.5).
- **DP-4 — F2 scopes are settled:** `encrypted_scopes = [identity, presence_personal]`, already wired in `EncryptionScope`. AB-4 changes the scope set's *liveness*, not its membership.

## Files to Read Before Starting

| File | Why |
|---|---|
| `homesynapse-core-docs/design/15-*crypto*.md` §3.4 (envelope format + DEK/scope) + §4.1 (the 1-byte discriminator) + §5 (the contract) + §6 (rotate-on-restore / failure modes) + §2.3 (the chain-coverage honesty caveat) | The LOCKED spec AB-4 implements — F1, rotate-on-restore, the envelope layout. |
| `homesynapse-core-docs/design/amendments/AMD-94_*.md` | The ratified A4 decisions verbatim (rotate additive; `v1`; prefix-in-envelope + AAD; AMD-94-INV-01/02). |
| `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` | The activation site: `main()` ctor call (currently 5-arg) + the `payloadCipher(Path,Clock)` adapter (built, held) + the 3 "five-argument ctor" nits. |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | The 6-arg ctor (the cipher arg) + the Phase-2 `PersistenceFactory.start(... payloadCipher)` wiring + the `cipher inert={}` RUNNING log. |
| `core/persistence/.../SqlitePersistenceLifecycle.java` | **The activation lever** (`payloadCipher != null ? DEFAULT_ENCRYPTED_SCOPES : Set.of()`). |
| `core/persistence/.../SqliteEventStore.java` | The write path (`doAppend` — encrypt + store `payload`/`payload_iv`/`dek_ref`; the F13a write guard) + the read path (`decryptStoredPayload`) — the F1 byte is written/read here (or in the manager — your design call, §A4.2). |
| `core/persistence/.../PayloadCipher.java` + `EncryptedPayload.java` + `PayloadDecryptionException.java` | The cipher seam (java.base-only, DP-5) + the record shapes (neither carries a version byte today) + the AB-2 typed exception (extend its `FailureKind` if F1 needs an `UNKNOWN_ENVELOPE_VERSION`). |
| `config/configuration/.../ScopeKeyManager.java` + `StandardScopeKeyManager.java` | F3 (the `encrypt` random-IV vs `encryptPayload` counter-nonce fence — doc-only today) + the durable counter (`scope_nonce_counters.json`, `nextNonceLocked`/`persistNonceCountersLocked`) + the GCM runner. |
| `config/configuration/.../AtomicYamlWriter.java` | F13b: `fsyncDirectory` swallows the `IOException` at DEBUG (the Windows-deliberate swallow — scope the fix). |
| `core/persistence/MODULE_CONTEXT.md` + `config/.../MODULE_CONTEXT.md` + the `module-info.java` of app/lifecycle/persistence/config | JPMS posture — **all edges already exist; AB-4 adds none** (app already requires config + persistence; the cipher threads `app → lifecycle → persistence` over the existing `payloadCipher` param; F3/F13b are config-internal). |

### Minimum read set (MANDATORY floor)
Doc 15 §3.4/§4.1/§5/§6 + AMD-94; `Main.main()` + the `payloadCipher` adapter; `SqlitePersistenceLifecycle` the cipher-presence gate; `SqliteEventStore` the write/read payload path; `StandardScopeKeyManager` `encrypt`/`encryptPayload`/the counter; `AtomicYamlWriter.fsyncDirectory`; `PayloadCipher`/`EncryptedPayload`/`PayloadDecryptionException`.

## Files to Create or Modify

| Action | File Path | Description |
|---|---|---|
| MODIFY | `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` | A4.1: 5-arg → 6-arg ctor passing `payloadCipher(configDir, clock)`; fix the 3 "five-argument ctor" nits (the comments at the ctor call + the adapter Javadoc). |
| MODIFY | `config/.../StandardScopeKeyManager.java` (+ the F1 envelope assembly if you site it here) | A4.3 (F3): enforce one nonce-construction-per-scope (reject a scope that mixes `encrypt`/random-IV with `encryptPayload`/counter). A4.2 (F1): prepend/parse the `v1` byte + bind it as GCM AAD, IF you site the envelope assembly in the manager (vs the persistence write path — your call, keep it in ONE place). |
| MODIFY | `core/persistence/.../SqliteEventStore.java` (or wherever the AEAD envelope is assembled/parsed) | A4.2 (F1): the leading `v1` byte on write + the strict parse on read (unknown byte → typed decrypt failure, never implicit-v1); GCM AAD binds the byte. A4.4(a): confirm the F13a write guard meets the intent (ctor-time vs write-time). |
| MODIFY | `core/persistence/.../PayloadDecryptionException.java` | A4.2: add a `FailureKind.UNKNOWN_ENVELOPE_VERSION` (or similar) for an unrecognized leading byte — fail-closed + typed (the AB-2 pattern). |
| MODIFY | `config/.../AtomicYamlWriter.java` (or a nonce-counter-scoped caller) | A4.4(b) (F13b): the nonce-counter dir-fsync `IOException` is FATAL/fail-closed — **scoped so it does not break the Windows/non-POSIX dev path** (see §Watch-out). |
| MODIFY | Doc 15 (a small docs note) OR a hivemind seam note | A4.5: document the backup-key portability seam (the exportable recovery artifact) + the rotate-DEK-on-restore boot contract. **Seam only** — no mechanics. (If this is a docs-repo edit, flag it for Nick to land in the docs repo; the hub can also record the seam in the spine.) |
| CREATE/MODIFY | the relevant test classes (config + persistence) | §Test Requirements — F1 round-trip + AAD downgrade-resistance + unknown-byte-fails-closed; F3 cross-construction rejection; F13b fail-closed (scoped); the activation flips `encryptedScopes`. Inject `Clock`. |
| MODIFY | `core/persistence/MODULE_CONTEXT.md` + `config/.../MODULE_CONTEXT.md` | Per §MODULE_CONTEXT Update. |

> **The Files table governs.** Where prose and the table disagree, the table wins; flag the conflict `[INFO]`.

## Technical Specification (the five obligations)

**A4.1 — Activate the cipher.** `Main.main()`: replace the 5-arg `HomeSynapseCore(dbPath, configDir, HOME_DEFAULT, clock, homeId)` with the 6-arg form passing `payloadCipher(configDir, clock)` (the existing adapter — confirm it wraps `ScopeKeyManager.create(...)` and calls `encryptPayload`). Fix the three "five-argument ctor" Javadoc/comment nits (they say "five-arg" but mean the 6-arg cipher ctor). **Net effect:** `SqlitePersistenceLifecycle`'s `payloadCipher != null ? DEFAULT_ENCRYPTED_SCOPES : Set.of()` now yields `[identity, presence_personal]` — encryption is live. No other call site changes.

**A4.2 — F1 the envelope version discriminator.** Reserve a 1-byte discriminator, value `v1` = the current AES-256-GCM/counter-nonce/per-scope-DEK envelope. **Encoding (DP-2): prefix-in-envelope + GCM AAD.** On write: prepend the byte to the stored envelope bytes AND pass it as the GCM AAD (so the auth tag covers the version → an attacker cannot strip/downgrade it). On read: read the leading byte, verify it (`v1`), pass it as AAD to the GCM decrypt; an unknown/absent byte → throw the typed `PayloadDecryptionException` (`FailureKind.UNKNOWN_ENVELOPE_VERSION`), never implicit-`v1`. Keep the assembly in **one** place (the manager's GCM runner OR the persistence envelope codec — your call; do not split it). Zero-DDL: the byte rides the existing `payload` BLOB, no `envelope_version` column.

**A4.3 — F3 one-nonce-construction-per-scope.** In `StandardScopeKeyManager`, make the random-IV (`encrypt`, for `config_secrets`) vs counter-nonce (`encryptPayload`, for event scopes) fence **programmatic**, not documentation-only: a scope binds to exactly one construction; a cross-construction call (e.g. `encrypt` then `encryptPayload` on the same `scopeId`, or vice versa) is rejected (`IllegalStateException` with a Register-C message). This is the GCM nonce-reuse guard (NIST SP 800-38D §8.3) — a (key, nonce) collision across constructions breaks confidentiality + authenticity. Track the per-scope construction (first-use wins, or a static scope→construction map if the scope set is fixed).

**A4.4 — F13 write-path hardening.** (a) Confirm the F13a guard (`SqliteEventStore` throws if an encrypted scope has `payloadCipher == null`) meets the AB-4 intent; if the intent wants a ctor-time assertion (not just write-time), add it. (b) **F13b:** the nonce-counter directory fsync (`AtomicYamlWriter.fsyncDirectory`, reached from `persistNonceCountersLocked`) currently swallows the `IOException` at DEBUG. For the **nonce-counter write**, a dir-fsync failure means the high-water mark may not be durable → a crash could replay a nonce → catastrophic GCM reuse. Make it **fail-closed/fatal for the nonce-counter path**, **scoped so it does not break Windows/non-POSIX** (where a directory channel cannot be opened and the swallow is deliberate — see §Watch-out for the resolution options).

**A4.5 — Backup-key portability seam (document only).** Record the seam for an exportable recovery artifact (so a restored backup can re-derive/install DEKs) + the rotate-DEK-on-restore boot contract (DP-3). **Seam only** — the export/import mechanics are the backup/restore WU. If documenting in Doc 15, flag it for Nick (docs-repo edit); else the hub records the seam in the spine.

## Locked Decisions That Apply

- **AMD-94 + AMD-94-INV-01/02** (rotate-on-restore additive; the reserved 1-byte discriminator; `v1`). **Doc 15 §3.4/§4.1/§5/§6.** **INV-PD-03** (at-rest posture) + **INV-PD-07** (the encrypted-scope contract). **LTD-04** (ULIDs at boundaries — `dek_ref` = `scope_id:key_version`). The **chain_hash-ZERO caveat** (Doc 15 §2.3): no over-claim of chain-coverage tamper-evidence pre-chain.

## Invariants That Must Hold

- **Zero-mint:** no new `EventTypes`/`@EventType`/category → counts stay **71/41/53**. (Recommend NO new `system_root_key_unavailable` event — the read path already throws the typed `PayloadDecryptionException`; if you want a boot event, STOP + flag `[REVIEW]` + run the manifest sweep.) Test: the count-pins stay green + unchanged.
- **Rotate-on-restore boot invariant (R-α REC-235):** refuse-to-encrypt-until-fresh-DEK-or-counter-proven. (AB-4 carries the contract; the restore mechanics are deferred — test the refuse-to-encrypt guard if it is reachable.)
- **F1 round-trip + downgrade-resistance:** an encrypted payload round-trips through the `v1` byte; the byte is GCM-AAD-bound (flipping it fails the auth tag); an unknown byte fails closed.
- **F3:** a scope cannot mix nonce constructions (test the rejection).
- **Pure/no-new-edge:** module-infos + `build.gradle.kts` UNCHANGED.

## STOP-on-Mismatch Gates

| File | Expected state (at `eed477e`) | What to check |
|---|---|---|
| `HomeSynapseCore.java` | a **6-arg** ctor `(Path, Path, HomeSynapseConfig, Clock, HomeId, PayloadCipher)` delegated-to by the 5-arg; the Phase-2 `PersistenceFactory.start(... payloadCipher)` wiring | the cipher arg is the only AB-4 ctor change; do NOT alter the 5-arg or the phase model |
| `Main.java` | `main()` builds the **5-arg** ctor; `payloadCipher(Path,Clock)` adapter present + calls `encryptPayload`; 3 "five-argument ctor" nits | the exact activation site |
| `SqlitePersistenceLifecycle.java` | `payloadCipher != null ? DEFAULT_ENCRYPTED_SCOPES : Set.of()` (`DEFAULT_ENCRYPTED_SCOPES = [identity, presence_personal]`) | the activation lever — do NOT change its logic, only feed it a non-null cipher |
| `SqliteEventStore.java` | F13a guard present (encrypted scope + null cipher → throw); `doAppend` stores `payload`/`payload_iv`/`dek_ref`; `decryptStoredPayload` on read | the F1 byte site (write/read) + confirm F13a |
| `PayloadDecryptionException.java` | `enum FailureKind {NO_CIPHER_WIRED, MALFORMED_DEK_REF, GCM_AUTH_FAILED, KEY_ABSENT_OR_DESTROYED}` | add the F1 unknown-version kind |
| `StandardScopeKeyManager.java` | `encrypt` (random IV) + `encryptPayload` (counter) + the durable counter; the construction fence is **doc-only** | F3 is genuinely unbuilt — add the programmatic guard |
| `AtomicYamlWriter.java` | `fsyncDirectory` swallows `IOException` at DEBUG (deliberate for Windows) | F13b — scope the fail-closed change |
| `EncryptedPayload`/`ScopeCipherResult` | records `(byte[] ciphertext, byte[] iv, int keyVersion)` — **no version field** | decide: carry `v1` in the envelope bytes (preferred, zero-DDL) vs a new record field |
| the count-pin tests | `EventTypesTest`(71)/`EventTypeAnnotationTest`(41)/`EventCategoryMappingTest`(53) | zero-mint guard — untouched |

## P2 Consumer/Pin (Fan-Out) Survey

- **count pins:** none change (zero-mint). Confirm 71/41/53 untouched.
- **JPMS / edges:** none. The cipher threads `app → lifecycle → persistence` over the existing `payloadCipher` param (app already `requires` config + persistence); F3/F13b are `config`-internal. Confirm all four `module-info` + `build.gradle.kts` UNCHANGED.
- **envelope-format consumers (the F1 fan-out):** every site that assembles OR parses an at-rest envelope must agree on the leading byte — the write path (`SqliteEventStore.doAppend`/the manager GCM runner) AND the read path (`decryptStoredPayload`) AND any test fixture that hand-builds an encrypted row. Grep for `payload_iv`/`dek_ref`/the GCM runner; ensure exactly one assemble + one parse, both version-aware.
- **construction-fence consumers (F3):** every caller of `encrypt` / `encryptPayload` (the `SecretStore` uses `encrypt`; the event write path uses `encryptPayload`) — confirm the fence doesn't reject a legitimate caller (secrets→random-IV, events→counter are correct and must stay allowed).
- **fsync-fatal consumers (F13b):** `AtomicYamlWriter` is shared by `scope_keys.json`, `scope_nonce_counters.json`, and secrets — a blanket fatal-fsync has blast radius; scope it to the nonce-counter path (or POSIX-only) so the other writers + Windows dev are unaffected.

## Test Requirements

- **Activation:** with a non-null cipher, `encryptedScopes == [identity, presence_personal]`; with null, `Set.of()` (the gate). A round-trip write→read of an `identity`/`presence_personal` payload is ciphertext-at-rest + plaintext-on-read.
- **F1:** `v1` round-trips; the GCM-AAD binding makes a flipped version byte fail the auth tag (downgrade-resistance); an unknown leading byte → `PayloadDecryptionException(UNKNOWN_ENVELOPE_VERSION)` (never implicit-v1).
- **F3:** `encrypt` then `encryptPayload` on the same scope (and vice versa) → rejected; the legitimate secrets-random-IV + events-counter paths stay allowed.
- **F13b:** a simulated nonce-counter dir-fsync `IOException` → fail-closed (the encrypt does not silently proceed); the Windows/non-POSIX path is NOT broken (the scoping holds).
- **Clock injection** (config + persistence are non-whitelisted): `Clock.fixed(...)` via ctor/`@BeforeEach`; no `Instant.now()`/`systemUTC()`.

## What to Watch Out For

- **F13b's Windows tension is real — do NOT blanket-flip the fsync to fatal.** `AtomicYamlWriter.fsyncDirectory`'s DEBUG-swallow is deliberate: Windows cannot open a directory channel, and `AtomicYamlWriter` is shared by `scope_keys`/`scope_nonce_counters`/secrets. A blanket fatal breaks Windows dev/test + over-reaches. Resolve by **scoping**: make fail-closed apply only to the **nonce-counter** write (the path where a lost fsync risks nonce reuse), and/or gate it POSIX-only (Windows logs + continues, or the nonce-counter durability uses the file-fsync that already works — the temp-file `channel.force(true)` before rename is solid; the *directory* fsync is the rename-durability belt-and-suspenders). State your chosen scoping in a `[Design point]`.
- **The chain_hash is ZERO today — do not over-claim F1 tamper-evidence.** The AAD binding gives real downgrade-resistance now (the tag covers the version byte); the *chain-coverage* tamper-evidence is inert until chain activation (post-MVP). Word logs/Javadoc accordingly (Doc 15 §2.3).
- **AB-4 activates a path with ~zero live producers today — that is BY DESIGN, not a defect.** `identity` resolves zero MVP events; `presence_personal` maps from `EventCategory.PRESENCE` (whether anything publishes it pre-M9 is moot). Encrypt-from-genesis is the point: the path must be live before the first sensitive write so the log is encrypted from the start (now-or-never on the immutable log). Do not "optimize away" the activation because the scope looks empty.
- **Keep the F1 byte assembly in ONE place.** Two divergent assemble/parse sites is a latent corruption bug. One writer, one reader, both AAD-aware.
- **Record component / static-factory collision STOP-check** for any new/changed record (if you add a `FailureKind` or a version-carrying field).
- **Cipher cold-start (OQ-15-2) — a `[Design point]`:** the first ~100 encrypts cost 80–700µs (C2 compiling the software-AES path on the Pi-4 floor; no ARM crypto extensions). A `JacksonWarmup`-style cipher warmup was recommended (OQ-15-2) but never landed. **Decide: add a small cipher warmup (mirroring `JacksonWarmup` in `core/persistence`) at activation, or consciously defer it** (it is a latency-smoothing nicety, not a correctness gate). Flag your choice.

## Coder Pushback Welcome

If any spec here is impractical or contradicts source — raise it (escalation format in your skill doc). The explicit `[Design point]`s: the F1 siting (manager vs persistence codec), the F13b scoping (the Windows tension), and the cipher-warmup add-vs-defer. If F1's AAD binding requires touching the GCM runner in a way that risks the M6.3 counter-path correctness, STOP and report rather than reshaping the counter logic.

## Out of Scope

`chain_hash` activation (F4-gated, ZERO today); the crypto-shred operation / KEK destruction / tombstones (post-MVP); backup/restore *mechanics* (A4.5 is seam-only); any AEAD algorithm change (`v1` = AES-256-GCM only); R-γ's final F1 *policy* (AB-4 proceeds on AMD-94's recorded safe default); any M9 device/integration scope; any new event type or module edge.

## Build Discipline

You produce files. You do NOT run `./gradlew`. Nick runs the gate. Flag the deferred gate in `coder-handoff.md` + the WUCP Phase 1 checklist, naming the commit. If your sandbox can run Gradle, a targeted `./gradlew :app:homesynapse-app:compileJava :core:persistence:compileJava :config:configuration:compileJava` shift-left self-check (≈20s) is welcome — the full `check` stays the deferred gate. Target GREEN in one round (zero-mint, zero-edge posture).

## MODULE_CONTEXT.md Update

- `core/persistence/MODULE_CONTEXT.md`: the F1 envelope version byte (v1, prefix + AAD) on the write/read path; the new `FailureKind`; the cipher is now LIVE (the activation flipped at app-bootstrap); no module-info change.
- `config/.../MODULE_CONTEXT.md`: F3 (the programmatic one-construction-per-scope guard); F13b (the nonce-counter fsync fail-closed, scoped); the rotate-on-restore boot contract carried.

## Success Criterion

DONE when: (1) `Main` activates the cipher via the 6-arg ctor (the nits fixed); (2) at-rest encryption is live for `[identity, presence_personal]` (the round-trip test passes); (3) the F1 `v1` byte is written + strictly parsed + GCM-AAD-bound (downgrade-resistant; unknown-byte fails closed); (4) F3 rejects cross-construction; (5) F13b is fail-closed for the nonce-counter write, scoped to not break Windows; (6) the backup-key seam + rotate-on-restore contract are documented; (7) counts stay 71/41/53 and module-infos + build.gradle.kts are unchanged; (8) both MODULE_CONTEXTs updated; (9) WUCP Phase 1 complete. The gate of record is `./gradlew check` GREEN on the pushed commit (Nick).

## Work Unit Completion (WUCP Phase 1)

After the compile gate passes or is deferred, execute WUCP Phase 1: update both MODULE_CONTEXTs; update `coder-handoff.md` (Deferred Build Gate flag + next-WU pointer = M9 [or M7.5c if Nick re-sequences]); append any `coder-lessons.md` entry; post a cross-agent note (the `[Design point]` resolutions: F1 siting, F13b scoping, cipher-warmup add/defer; any `[REVIEW]`s); append the WUCP Phase 1 checklist. Flag every `[REVIEW]`/`[Design point]` explicitly so the PM hub can rule it.
