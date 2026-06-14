<!--
file: context/audits/2026-06-14_core-review_A_data-crypto-spine.md
purpose: Review Session A deliverable — static read-and-reason audit of the data/storage/crypto spine (modules 1–8), per 2026-06-14_core-review_FRAMEWORK.md. Feeds the converge session.
audience: Nick, the converge session
state-type: audit (review-specific, one-shot)
status: COMPLETE
-->

# Review Session A — Data, Storage & Crypto Spine

**Reviewer:** PM / senior systems architect (`nexsys-project-manager` hat), Cowork, static review (no Gradle).
**Baseline reviewed:** core source at the M6.3-landed working tree (Framework baseline `1eddd9a`; treated as committed per the Framework's known-staleness note). Watermark AMD-93, invariants 163/47, projectionVersion 5, 22 subprojects.
**Method:** every claim verified against `.java`/`.sql` source with host Read/Grep (no sandbox `git`); `file:line` cited; each finding tagged **[VERIFIED-FROM-SOURCE]** or **[HYPOTHESIS — NEEDS GATE]** with the exact Claude Code check.

---

## Step 0 — preflight result

```
FRESHNESS PREFLIGHT — 2026-06-13 (review lens)
Snapshot / masthead:        consistent with baseline (M6 4-of-4, AMD-93, 163/47, pv5, 22 subprojects, check GREEN 147)
Known staleness:            M6.3 "UNCOMMITTED in working tree" — the one Framework-acknowledged staleness; treated as committed at 1eddd9a
CONFLICTED checks:          none
Source round-trip (Ch.11):  spot-checked types resolve in source; the MinimalDerivationRule fabrication is GONE (now real ProductionDerivationRule)
Verdict:                    CLEARED TO REVIEW (no CONFLICTED state; no escalation-before-review trigger)
```

Read-first lenses consumed: `PROJECT_SNAPSHOT.md`, `pm-handoff.md` (Open Risks), `Architecture_Invariants_v1.md` (§2 ES, §6 PD incl. the AMD-86 at-rest posture, §0.3 index), `freshness-preflight.md`, `deviation-and-quality.md` §6 (Source Trust Hierarchy), all 8 modules' `module-info.java`.

---

## Executive summary

**Health verdict: the foundation is correct and the M6.3 at-rest crypto is sound end-to-end for what is shipped — there is no BLOCKING finding.** The event-sourcing spine (per-entity sequence, `eventTime`/`ingestTime` separation, write-ahead durability, immutable validating envelope) is built right. The crypto write/read path is genuinely good: counter-nonce allocation is fsync-durable *ahead of return* inside the `ScopeKeyManager` lock (OR-M6-NONCE write-path discharged, and the config-side durability test actually crash-reloads the real manager), the write path is fail-closed, `dek_ref` uses a robust last-colon parse, and the YAML security surface (AMD-71 `toRealPath` containment, write-path secret rejection, load+reload resolution) is well-implemented. The hand-rolled `UlidFactory`, the `Expectation` tagged-union codec (compile-exhaustive, no `default`), and the derived-event `eventTime` discipline (`ProductionDerivationRule` — the historical Q21 trap) are all correct.

The findings are **forward-risks, test-weaknesses, and one confirmed latent migration trap** — concentrated, as expected, on the crypto seam and its boundaries. The five that matter:

| # | Sev | One-line | Tag |
|---|-----|----------|-----|
| **F-A1** | HIGH (forward) | Read-path **decrypt failure aborts the whole read/replay** — no per-row `DegradedEvent` degrade like codec failures get; a lost/corrupt key → unreplayable store (vs INV-RF-04), and the future crypto-shred would break replay (vs INV-PD-07's "operation unaffected by shredded events"). | VERIFIED (mechanism) |
| **F-A2** | MEDIUM | Random-IV and counter-nonce constructions **share one per-scope DEK** with no structural guard; the config test actively mixes both on scope `identity` — the **NIST SP 800-38D §8.3** anti-pattern. Production is safe only by unenforced scope-disjointness. | VERIFIED |
| **F-A3** | MEDIUM | The event→scope mapping is **duplicated** (config `EncryptionScope` canonical + persistence `encryptionScopeId` String mirror); the pin test checks the mirror in isolation, not against the canonical — a silent-drift hazard (plaintext-write of sensitive data, or scope/key mismatch). | VERIFIED |
| **F-B1** | MEDIUM | **`MigrationRunner.splitSqlStatements` still emits a comment-only fragment as a statement** (the CONFIRMED finding) — broke all DB-init in V005 gate-fix round 2; the fix was in the SQL file, not the splitter, so it remains a latent trap for every future migration author. | VERIFIED (CONFIRMED) |
| **F-A4** | MEDIUM | `SqliteEventStore` constructor does **not enforce its documented "null cipher ⇒ empty scopes" invariant**; the fail-closed test deliberately violates it. Write-time fail-closed protects correctness, but the misconfig surfaces late (first sensitive publish), not at startup. | VERIFIED |

Plus **F-A5** (durability/perf forward-risk: the nonce-counter directory-fsync is best-effort/swallowed, and per-event encryption runs on the single write thread) and **F-C1** (event-bus retry/backoff is dead code while its Javadoc says otherwise).

### Reserved-but-unbuilt register (Session A's half — a B-side or M7 consumer must not assume these work)

| Item | Status in source | Premature-reliance risk |
|---|---|---|
| **Crypto-shred operation** (Doc 15 §3.6) | `ScopeKey.destroyedAt` field + the `decrypt` guard exist (`StandardScopeKeyManager.java:215`), but **no setter** — nothing ever sets `destroyedAt`. | A consumer must not assume key-destruction/erasure is callable; only the *unreadability property* ships. **Interacts with F-A1.** |
| **OR-M6-NONCE restore half (R-α)** | Write-path durability discharged; **restore-rotation is NOT built** — `restoreCannotResumeUsedCounter` drives `cipher.rotate()` on a *test double*; production `StandardScopeKeyManager` has no rotate-on-restore. | A backup/restore that resumes a counter ≤ a used value under the same DEK breaks GCM. The backup/restore co-design owes this. |
| **`identity` scope (keyed, unpopulated)** | `EncryptionScope.IDENTITY` has **no event category**; `encryptionScopeId` can never return `"identity"` (safe by construction). `encrypted_scopes=[identity, presence_personal]` keys an inert scope. | A future person-identity event type must wire the mapping in **both** config and the persistence mirror (F-A3) or it ships plaintext. |
| **`main()` runtime construction** | `Main.main()` prints "not yet implemented"; `payloadCipher(...)` is package-private, exercised only by `PayloadCipherBridgeTest`. | **At-rest encryption is NOT active at runtime** until the app-bootstrap milestone wires the cipher into `HomeSynapseCore`. Do not assume encryption is live. |
| **Chain-hash activation** (Doc 15 §3.3/§5) | `chain_hash` written as a 32-byte `ZERO_HASH` for every event (`SqliteEventStore.java:463`); column is a reservation, **computation not built**. | A tamper-evidence consumer (INV-PD-08) must not treat `chain_hash` as integrity — it is all zeros. Doc 01 §14 "not implemented" is accurate. |
| **Ed25519 signing** (Doc 15 §3.7) | **Absent** from main source (grep: no `Ed25519`/`Signature`/`.sign(`). | Design-only; no signing capability exists. |

---

## Cross-cutting findings (detail)

`ID | severity | type | file:line | issue | recommendation | disposition | tag`

### F-A1 — Decrypt failure on read aborts the whole read/replay (no graceful degrade)
- **HIGH (forward-risk) · correctness/security · `core/persistence/.../SqliteEventStore.java:804-810` + `:896-913`**
- **Issue:** `fromRow` routes any `dek_ref`-bearing row through `decryptStoredPayload`, which **throws** on every decrypt failure — missing cipher (`:898`), malformed `dek_ref` (`:905`), GCM auth-fail, or a destroyed (shredded) key. There is **no per-row catch**, so one bad row fails the entire `readRows` batch. This contrasts deliberately with codec **parse** failures, which degrade to a `DegradedEvent` so the read continues (class Javadoc `:88`). Consequences: (a) a lost/corrupt `.root-key` → **the entire event store becomes unreplayable**, in tension with INV-RF-04 (recover "without manual repair"); (b) when the post-MVP **crypto-shred** operation lands, replay across a shredded event will throw — directly contradicting INV-PD-07's test ("Verify that system operation is unaffected by the presence of shredded events"). Untested: the missing-cipher-on-read and shredded-key-on-read paths have no test (all read tests wire the cipher).
- **Recommendation:** decide the confidentiality-vs-availability contract *before* crypto-shred is built. Most likely: catch decrypt failure in `fromRow` and emit a `DegradedEvent` (mirroring the codec posture) for the shredded/undecryptable case, while keeping a hard fail only for the "cipher entirely unwired but encrypted rows exist" misconfiguration. Add tests for both read-side failure modes.
- **Disposition:** needs-Nick-decision (design tradeoff) + needs-coding-instruction (crypto-shred WU). **Tag:** [VERIFIED-FROM-SOURCE] for the throw/no-catch mechanism; the INV implications are reasoned, not runtime-observed.
- **CC check (optional):** `:core:persistence:test --tests '*AtRestEncryption*'` after adding a test that reads an encrypted DB with a `null` cipher — expect the whole-batch throw today.

### F-A2 — Random-IV and counter-nonce share one DEK; the "fence" is convention, not structure
- **MEDIUM · security/forward-risk · `config/.../StandardScopeKeyManager.java:149-196` (both `encrypt` + `encryptPayload`); test `config/.../ScopeKeyManagerPayloadNonceTest.java:164-178`**
- **Issue:** `encrypt()` (fresh **random** 96-bit IV) and `encryptPayload()` (deterministic **counter** nonce) both resolve `activeDekLocked(scopeId)` — i.e. **the same per-scope DEK**. Nothing binds a scope to one construction. The `fence_randomIvPathUnchanged` test exercises *both* on scope `"identity"`, demonstrating the manager permits mixing random + deterministic IV construction under one key — the pattern **NIST SP 800-38D §8.3 forbids** ("For a given key… the deterministic construction and the RBG-based construction shall not both be used"). Production is safe today *only* because the scope IDs are disjoint (`config_secrets` via `encrypt`; `presence_personal` via `encryptPayload`), which is unenforced and one careless future call breaks.
- **Recommendation:** bind each scope to exactly one nonce strategy — e.g. namespace payload scopes vs secret scopes, or guard (`encryptPayload` rejects a scope that has issued a random IV and vice-versa), or at minimum encode the disjointness as an enforced invariant with a test. Reconsider whether `fence_randomIvPathUnchanged` should use one scope.
- **Disposition:** needs-Nick-decision / needs-coding-instruction. **Tag:** [VERIFIED-FROM-SOURCE].

### F-A3 — Event→scope mapping duplicated; the pin checks the mirror in isolation
- **MEDIUM · drift/test-weakness · canonical `config/.../EncryptionScope.java:123-133`; mirror `core/persistence/.../SqliteEventStore.java:881-885`**
- **Issue:** the category→scope mapping exists twice: config's `EncryptionScope.scopeIdFor` (canonical) and persistence's `encryptionScopeId` String mirror (intentional, to avoid a `persistence→config` edge — Doc 15 §3.8). The mirror is "pinned by `AtRestEncryptionWritePathTest`," but that test asserts persistence's mirror behavior **in isolation** (presence → `presence_personal:1`); it never cross-checks against config's canonical mapping (it can't — persistence has no `config` dependency). A future change to the canonical mapping (a new sensitive category, or a scope rename) would silently diverge: an event config deems sensitive could be written **plaintext** by persistence, or under a `scope_id` that doesn't match the key store (decrypt fails per F-A1).
- **Recommendation:** add a cross-module agreement test in `app` (which sees both) asserting persistence's classification matches `EncryptionScope.scopeIdFor` for every `EventCategory` — drive it through the public publish/read path since `encryptionScopeId` is private.
- **Disposition:** needs-coding-instruction. **Tag:** [VERIFIED-FROM-SOURCE].

### F-A4 — `SqliteEventStore` constructor doesn't enforce the "null cipher ⇒ empty scopes" invariant
- **MEDIUM · security-hygiene/doc · `core/persistence/.../SqliteEventStore.java:302-318` (Javadoc `:293-298`)**
- **Issue:** the ctor Javadoc states "When `null`, `encryptedScopes` MUST be empty… the fail-closed [default]," but the ctor only assigns — no guard. The fail-closed test deliberately constructs `(…, null, Set.of("presence_personal"))` (`AtRestEncryptionWritePathTest.java:324`), so the code in fact relies on the invariant **not** being enforced. Write-time fail-closed (`:402`) still protects correctness (no silent plaintext), but a real misconfiguration surfaces late — at the first sensitive-PII publish — instead of at startup, and the Javadoc is contradicted by usage.
- **Recommendation:** either add a fail-fast ctor guard (`payloadCipher == null && !encryptedScopes.isEmpty()` → throw) and adjust the fail-closed test to inject a cipher-that-throws, **or** correct the Javadoc to state that null-cipher + non-empty-scopes is permitted and yields write-time fail-closed.
- **Disposition:** needs-coding-instruction / needs-doc-fix. **Tag:** [VERIFIED-FROM-SOURCE].

### F-A5 — Nonce-counter durability: best-effort dir-fsync swallowed + per-event write-thread cost
- **MEDIUM · forward-risk · `config/.../AtomicYamlWriter.java:131-142`; `core/persistence/.../SqliteEventStore.java:388-409`**
- **Issue (a):** the OR-M6-NONCE high-water durability rests on `AtomicYamlWriter.writeAtomically` → `fsyncDirectory(parent)`. That dir-fsync is **best-effort: a POSIX `IOException` is swallowed at DEBUG** (`:138-141`). On the catastrophic-if-wrong nonce path, a (rare) silent dir-fsync failure would leave the rename non-durable — after a crash the high-water could roll back and a nonce repeat under one DEK breaks AES-GCM. The temp-file `force(true)` is correct; only the rename-durability step is silently best-effort.
- **Issue (b):** encryption (and therefore the per-event atomic-rewrite + double-fsync of `scope_nonce_counters.json`) runs on the **single write thread**, not the publishing VT (a conscious deviation from Doc 15 §3.2, documented at `:391-393`). Fine at MVP scopes (OQ-15-2: identity ≈0 ev, presence ~60 ev/s burst, tax ≤0.12%), but it is write-amplification + serialization that becomes a single-writer bottleneck if `encrypted_scopes` ever expands to a high-volume category.
- **Recommendation:** (a) on the nonce-counter write specifically, treat a POSIX dir-fsync failure as fatal (fail-closed) rather than DEBUG-swallow; (b) leave (b) as accepted for MVP but flag it as a gate on any future expansion of `encrypted_scopes`.
- **Disposition:** needs-Nick-decision (a) + needs-claude-code-verification (b). **Tag:** [VERIFIED-FROM-SOURCE] for the swallow + thread placement; **[HYPOTHESIS — NEEDS GATE]** for the perf impact at scale.
- **CC check (b):** a JMH-style bench of the full `encryptPayload` (incl. the `scope_nonce_counters.json` atomic rewrite + 2 fsyncs) at 60 ev/s on the Pi-4 floor, measuring write-thread occupancy and p99 publish latency vs the plaintext path; expect a per-event fsync pair on the writer.

### F-B1 — `MigrationRunner.splitSqlStatements` emits comment-only fragments (CONFIRMED)
- **MEDIUM · correctness/forward-risk · `core/persistence/.../MigrationRunner.java:429-463`**
- **Issue:** the splitter appends comment characters into the current buffer (`:437,:445`); a `--` line comment **after** the final `;` (or any comment-only span after a terminator) becomes a non-empty trailing fragment (`:458-461`) emitted as a statement, which sqlite-jdbc rejects → migration fails. This **broke every DB-init in V005 gate-fix round 2** (2026-06-13). The fix was applied **in the SQL file** (V005 header note `V005__…sql:17-20`, "keep all commentary in this header block"), **not in the splitter** — so the bug remains a latent trap: the next author who writes a trailing comment re-triggers a full DB-init failure. **Sibling sweep: CLEAN at HEAD** — no current migration (V001–V005, plus the DLQ/snapshot files) has an inline `;--` or a comment after its last statement; all `--` lines are top-of-file headers (handled correctly as leading comments).
- **Recommendation:** one-line guard — before adding a fragment, strip `--`-to-EOL comments and skip if the remainder is blank (so a comment-only fragment is never emitted). Keep the V005 header note as belt-and-suspenders.
- **Disposition:** needs-coding-instruction. **Tag:** [VERIFIED-FROM-SOURCE] (CONFIRMED).
- **CC check:** add a `MigrationRunner` unit test with a migration whose body ends `INSERT …;\n-- trailing` — assert it applies cleanly (fails today).

### F-C1 — Event-bus retry/backoff is dead code; the class Javadoc says it is active
- **MEDIUM · drift/forward-risk · `core/event-bus/.../SubscriberSupervisor.java:18-32` vs `:84-86,:108`**
- **Issue:** the class header advertises "exponential backoff (MIN=3s, MAX=30s, jitter=0.2)… retry scheduling," but `:84-86` admits the retry loop (`computeBackoff`/`sleepForBackoff`/`MAX_RETRIES`) "is reserved for a future WU and is currently dead code. Each failed delivery parks immediately with `attemptCount=1`." So a `RuntimeException` from `onEvent` parks straight to the DLQ with no in-place retry. No correctness hole — events park durably (UPSERT-idempotent on `(subscriber_id, event_position)`) and the circuit breaker (5 crashes/10-min → SUSPENDED) works — but the resilience story is half-built and the header oversells it.
- **Recommendation:** reconcile the class Javadoc with `:84-86`; catalog "subscriber retry-with-backoff" as a tracked reserved item so no consumer assumes failed events are retried before parking.
- **Disposition:** needs-doc-fix / reserved-register. **Tag:** [VERIFIED-FROM-SOURCE].

---

## Per-module sections

### 1 · `platform/platform-api` (`com.homesynapse.platform`) — medium
**Model.** Leaf platform module (no HomeSynapse deps; exports `platform` + `platform.identity`). Owns typed-ULID identity and the hand-rolled monotonic `UlidFactory` (LTD-04, `ulid-creator` removed per DECIDE-02). **Verification.** `UlidFactory` (`:30-117`) is correct: `ReentrantLock` not `synchronized` (LTD-11, VT-safe), strict in-process monotonicity with lsb→random-high carry and an overflow guard (`:95-103`), clock-backward tolerance by reusing `lastTimestamp` (`:85-87`), correct 48-bit-time/80-bit-random layout; production callers pass the injected clock (`SqliteEventStore.publish` → `UlidFactory.generate(clock)`), and `platform..` is whitelisted for the no-arg `Clock.systemUTC()`. **Findings:** none (1 INFO: the static lock serializes all ULID generation process-wide — inherent to strict monotonicity, cheap, acceptable).

### 2 · `core/value-model` (`com.homesynapse.value`) — medium
**Model.** The relocated `AttributeValue` leaf (broke the AMD-52 event↔device cycle; `module-info` requires only `java.base`). 8-variant sealed hierarchy, immutable records. **Verification.** Sealed permits exactly the 8 documented variants (`AttributeValue.java:28-30`); `FloatValue(double)` (`:19`) relies on the **record-default** equality, which is `Double.compare`-based bit-identity (NaN==NaN, −0.0≠+0.0) — the correct "float-bit identity" discipline, distinct from the comparator's epsilon (used only for change-detection). **Findings:** none. *Minor (rolled up):* JSON serde of non-finite doubles (NaN/±Infinity) is an untested round-trip edge — see research avenues. **Note:** `value-model` has **0 test files of its own** — its serde/identity is exercised transitively (persistence codec, state-store comparator); acceptable for a value leaf but worth awareness.

### 3 · `core/event-model` (`com.homesynapse.event`) — DEEP
**Model.** The spine's origin: `EventEnvelope`/`DomainEvent`/`EventDraft`, `EventStore`/`EventPublisher`, `CausalContext`, `EventCategory`/`EventTypes`, `SequenceConflictException`. **Verification.** `EventEnvelope` (`:99-163`) is an immutable record with a thorough validating compact constructor (null checks; `eventType` blank; `schemaVersion≥1`; `subjectSequence≥1`; `globalPosition≥0`; `categories` non-empty) and a `List.copyOf` defensive copy — and crucially **no fabricated category-dedup** (the Q38 benchmark trap is absent in source). `CausalContext` (`:47-107`) is exactly 2 fields with `actorRef` on the envelope (INV-MU-01), correct `root`/`chain`/`isRoot` semantics. `eventTime` nullable, `ingestTime` required (INV-ES-08). **Findings:** none (clean — the contracts are exact).

### 4 · `core/event-bus` (`com.homesynapse.event.bus`) — DEEP
**Model.** Subscriber lifecycle/isolation, checkpoints, backpressure, DLQ, the COLD→REPLAY→TRANSITION→LIVE(+SUSPENDED) mode FSM. **Verification.** `SubscriberMode` (`:13-29`) is the documented CAS-driven FSM (INV-SUB-ISO-04). `SubscriberSupervisor` (`:37-170`) is confined to the subscriber's own VT (isolation), with a sound exception taxonomy (RuntimeException → DLQ-park + crash-window + circuit-breaker; `Error`/checked → immediate SUSPENDED), a rolling 10-min window, a null-message guard (`:105-107`), and idempotent DLQ park (V002 `UNIQUE(subscriber_id, event_position)` UPSERT). **LTD-11 sweep: CLEAN** across all production code — every `synchronized` token is a comment explaining the `ReentrantLock`/`ReentrantReadWriteLock` choice or third-party pinning (sqlite-jdbc `synchronized native`, Jackson cache paths). **Findings:** F-C1 (dead-code retry/backoff + Javadoc oversell).

### 5 · `core/device-model` (`com.homesynapse.device`) — medium
**Model.** Devices/entities/capabilities, the `Expectation` sealed tagged-union (Pending Command Ledger), `EntityRole`. **Verification.** `Expectation` (`:27-28`) seals exactly 4 permits (`ExactMatch`, `WithinTolerance`, `EnumTransition`, `AnyChange`); the persistence `ExpectationSerializer` switches on all 4 with **no `default`** (compile-time exhaustive — a 5th permit breaks the build), and `ExpectationDeserializer` fails-closed on an unknown tag (`:82`). `FloorRegistry`/`AreaRegistry` use `ReentrantLock` (LTD-11, with the VT-pinning rationale in-Javadoc). **Findings:** none (clean — the tagged-union codec is the correct pattern).

### 6 · `core/persistence` (`com.homesynapse.persistence`) — DEEP
**Model.** SQLite WAL store, `MigrationRunner`, the single-writer coordinator, checkpoint stores, the Jackson codecs, and the M6.3 at-rest write/read path (`SqliteEventStore` encrypt-on-write, `PayloadCipher`/`EncryptedPayload`). **Verification.** Event-sourcing write path is correct: per-entity `subject_sequence` via `MAX+1` on the **single write thread** (no race) with `UNIQUE(subject_ref, subject_sequence)` (V001:54, LTD-05) as backstop → `SequenceConflictException` (`:512-543`); `eventTime` from `draft.eventTime()` not `Instant.now()` (`:428`, INV-ES-08); `ingestTime` from the clock. Crypto write path fail-closed (`:401-409`); read path fail-closed + robust **last-colon** `dek_ref` parse (`:896-913`); `encryptionScopeId` can only ever yield `presence_personal` or null (`:881-885`). `chain_hash` = `ZERO_HASH` reservation (`:463`). **Findings:** F-B1 (CONFIRMED splitter trap), and shares F-A1/F-A3/F-A4/F-A5. *Minor (rolled up):* a colon-bearing-but-non-numeric `dek_ref` version yields `NumberFormatException` rather than the nicer `IllegalStateException` (trivial).

### 7 · `core/state-store` (`com.homesynapse.state`) — medium
**Model.** Materialized views, `projectionVersion` (5), the derivation model. **Verification.** The Check-11 fabrication is **resolved**: the production rule is a real class `ProductionDerivationRule` reached via the `DerivationRule.production()` factory on the `@FunctionalInterface` — the old fabricated `MinimalDerivationRule` is gone. `ProductionDerivationRule.evaluate` (`:102-140`) is a pure, deterministic function (INV-PROJ-01) and honors the derived-event discipline exactly: `eventTime` **inherits from the inbound envelope, never `Instant.now()`** (`:132`, the historical Q21 trap), `actorRef` inherited, null idempotency key. **Findings:** none (clean).

### 8 · `config/configuration` (`com.homesynapse.config`) — DEEP
**Model.** The security center of gravity: YAML load (safe-load, AMD-71 traversal guard, `!include`/`!secret`/`!env`), schema validation, hot-reload atomic swap, the secret store + `ScopeKeyManager` (root key, HKDF KEKs, wrapped DEKs, the M6.3 counter-nonce path + `scope_nonce_counters.json`). **Verification.** Key hierarchy per Doc 15 §4.2 (root 256-bit `SecureRandom` at `.root-key` 0400 via two-step create+tighten; KEK = HKDF-SHA256(root,"scope:"+id), never stored; DEK wrapped, `scope_keys.json`). `encryptPayload` (`:168-196`) allocates the counter and **fsyncs the high-water mark inside the lock before the nonce returns** (OR-M6-NONCE durable-ahead-of-return); the config-side test (`ScopeKeyManagerPayloadNonceTest`) genuinely proves re-init-from-disk (fresh manager resumes at persisted max+1) and durable-ahead-of-return (reads the file after the call). `AtomicYamlWriter.writeAtomically` does the correct temp→`force`→`ATOMIC_MOVE`→dir-fsync sequence. YAML traversal guard (`YamlLoader.java:297-357`) is textbook-correct: `toRealPath` on **both** base and target + element-wise `startsWith` containment (not string-prefix), one-level includes, `!secret`/`!env` rejected in the write-back form, missing-secret errors name the key never the value (LTD-15). **Findings:** F-A2, F-A5(a), and shares F-A1. **Crypto-shred:** `destroyedAt` guard present, no setter (reserved).

---

## Coverage ledger (the honesty contract)

| # | Module | Depth | Findings | Notes |
|---|--------|-------|----------|-------|
| 1 | platform-api | medium | 0 (+1 INFO) | UlidFactory verified correct |
| 2 | value-model | medium | 0 (+1 minor) | 8-variant sealed; bit-identity via record default; 0 own tests |
| 3 | event-model | **deep** | 0 | envelope/causal contracts exact; no fabricated dedup |
| 4 | event-bus | **deep** | F-C1 | isolation/FSM/DLQ sound; LTD-11 clean; retry/backoff dead-code |
| 5 | device-model | medium | 0 | Expectation 4-permits + compile-exhaustive codec |
| 6 | persistence | **deep** | F-B1 (+shares A1/A3/A4/A5) | write path + crypto sound; splitter trap remains |
| 7 | state-store | medium | 0 | DerivationRule fabrication resolved; Q21 discipline honored |
| 8 | configuration | **deep** | F-A2, F-A5a (+shares A1) | crypto + YAML security solid; durability nuance |

**Cross-cutting:** F-A1 (read-path decrypt abort), F-A2 (IV-construction mixing), F-A3 (scope-mapping drift), F-A4 (ctor invariant), F-A5 (durability/write-thread). **Nothing faked; every module earned a model + contract + test-strength pass.** Depth was spent foundation-up with the crypto end-to-end trace and the event-sourcing invariants as the spine, per the Session-A emphases.

---

## Research avenues surfaced (raw — the converge consolidates)

1. **Confidentiality-vs-availability contract for an encrypted event-sourced log.** F-A1 forces the question the crypto-shred WU must answer first: when a payload can't be decrypted (shred / key-loss / downgrade), does replay degrade-per-row or fail-closed-whole-store? This is the design beat that gates both crypto-shred *and* backup/restore (R-α). Likely a short design note before any M-crypto-shred coding.
2. **A single nonce-strategy-per-key discipline.** F-A2 suggests a small, regret-proof invariant: a scope is bound to exactly one IV construction. Worth a one-paragraph governance pin (and a NIST SP 800-38D §8.3 citation in Doc 15 §3.4) so the disjointness is a contract, not an accident.
3. **Cross-module mapping-agreement tests as a pattern.** F-A3 is one instance of a general hazard: any String-mirror across a deliberate module boundary (here `EncryptionScope` ↔ `encryptionScopeId`; elsewhere `EncryptedPayload` ↔ `ScopeCipherResult`) needs an agreement test in the module that sees both (`app`). Consider a standing rule.
4. **Per-event fsync cost on the Pi-4 floor.** F-A5(b) — the OQ-15-2 microbench measured the encrypt op; it did not (visibly) include the `scope_nonce_counters.json` atomic-rewrite + double-fsync per sensitive event. Worth a confirmatory on-device bench at presence-burst before `encrypted_scopes` is ever widened.
5. **Non-finite `AttributeValue` serde.** Whether `FloatValue(NaN/±Infinity)` survives the Jackson JSON round-trip (and the typed `StateChangedEvent` payload) — a small confirmatory test; JSON has no native NaN/Infinity token.
6. **Migration splitter hardening.** F-B1's one-line guard is trivial; the broader avenue is whether the "replace the splitter rather than extend it" note (MigrationRunner Javadoc) should be acted on now that two comment-idiom traps have been hit.

---

## Commit message (handed to Nick — `!`-free)

```
docs(audit): Review Session A — data/storage/crypto spine (modules 1-8)

Static read-and-reason audit per 2026-06-14_core-review_FRAMEWORK.md. No
BLOCKING finding: the event-sourcing foundation is correct and the M6.3
at-rest crypto is sound end-to-end for what is shipped. Findings are
forward-risks, test-weaknesses, and one confirmed latent migration trap,
concentrated on the crypto seam.

Top findings:
- F-A1 HIGH (forward): read-path decrypt failure aborts the whole replay
  (no DegradedEvent degrade); tension with INV-RF-04 and the future
  crypto-shred vs INV-PD-07. Decide before crypto-shred is built.
- F-A2 MED: random-IV and counter-nonce share one per-scope DEK with no
  guard (NIST SP 800-38D 8.3); safe only by unenforced scope-disjointness.
- F-A3 MED: event-to-scope mapping duplicated (config canonical vs
  persistence mirror); pin checks the mirror in isolation -> drift hazard.
- F-A4 MED: SqliteEventStore ctor does not enforce its null-cipher invariant.
- F-A5 MED: nonce-counter dir-fsync is best-effort/swallowed; per-event
  encryption on the single write thread (forward-risk if scopes expand).
- F-B1 MED (CONFIRMED): MigrationRunner.splitSqlStatements still emits a
  comment-only fragment as a statement; fixed in V005 SQL, not the splitter.
- F-C1 MED: event-bus retry/backoff is dead code while its Javadoc says
  otherwise.

Reserved-but-unbuilt (verified from source): crypto-shred operation,
OR-M6-NONCE restore half (R-alpha), identity scope, main() runtime wiring,
chain-hash activation (chain_hash = zeros), Ed25519 signing (absent).

Coverage: all 8 modules earned a model+contract+test-strength pass; deep on
event-model, event-bus, persistence, configuration. No production code
touched; deliverable is the audit file only.
```

---

*End of Session A. Parallel-capable with Session B; the converge merges both. No production code, tests, or governance files were modified — the sole write is this audit.*
