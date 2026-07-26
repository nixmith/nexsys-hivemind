<!--
file: context/instructions/2026-06-19_AB-1-AB-2-AB-4_Seam-1_go-live_coding-instruction.md
purpose: Phase-3 coding instruction for the Seam-1 go-live — AB-1 (auth + bind), AB-2 (fail-closed read contract), AB-4 (payloadCipher activation + envelope-finalization). Wires into the seams AB-3 deliberately left.
audience: Coder (nexsys-coder), Nick (the two RULED escalations + the deferred build gate)
status: AB-1 + AB-2 = ISSUE-READY (issued 2026-06-19). AB-4 = ⛔ GATED on AMD-94 ratification (authored, held — do NOT build AB-4 until the un-gate condition below is met).
baseline: homesynapse-core HEAD 60d50ce (AB-3 landed GREEN) / docs 32afb3f / hivemind bcd7376 ; watermark AMD-93 ; Doc 09/10/12/15 LOCKED. Re-verify HEAD + the Doc 15 watermark at the Coder's Step-0.
amd-gate: AB-4 only — un-gates when AMD-94 is RATIFIED + folded into Doc 15 (§3.4 nonce/DEK, §5 envelope version byte, §6 failure modes) and the on-disk watermark reads AMD-94. Until then AB-4 is HELD; AB-1 + AB-2 carry NO AMD-94 dependency and proceed now. **State at authoring (2026-06-19):** AMD-94 was authored by the parallel governance session and is now on disk at `homesynapse-core-docs/design/amendments/AMD-94_Doc15-sec6_*.md` but is **PROPOSED, untracked, NOT ratified** — its own status line reads "watermark stays AMD-93 until then," Doc 15 carries no version-byte fold, and docs HEAD is unchanged at `32afb3f`. So the gate is **OPEN**: AB-4 stays HELD until Nick ratifies after the DOCS-Project review. Do NOT read "the AMD-94 file exists" as "the gate cleared."
-->

# Coding Task: AB-1 + AB-2 + AB-4 — The Seam-1 Go-Live (authenticated HTTP surface · fail-closed read contract · at-rest cipher activation)

**Subsystem:** REST/WebSocket API (auth), Persistence (read contract + write-path hardening), Config (key manager F3/F13), Lifecycle + App composition root (wiring), Crypto (Doc 15 §3.8 adapter)
**Design Docs:** Doc 09 REST API (Locked) · Doc 10 WebSocket API (Locked) · Doc 12 Startup/Lifecycle (Locked) · Doc 15 Cryptographic Architecture (Locked; AB-4 also consumes **AMD-94** once ratified)
**Phase:** 3-Implementation
**Task Brief Reference:** 2026-06-19 AB-1+AB-2+AB-4 Seam-1 go-live session prompt; app-bootstrap charter §2; decisions A1–A4 (2026-06-18)

> **⛔ READ THIS FIRST — the gate.** This instruction covers **three** first-class pieces. **AB-1 and AB-2 are ISSUED — build them now.** **AB-4 is GATED on AMD-94 and is HELD — do NOT build any AB-4 row until AMD-94 is ratified + folded into Doc 15 and the watermark reads AMD-94** (re-confirm at your Step-0). The reason is irreversibility: the first encrypted write finalizes the on-disk envelope **permanently** on the immutable (soon hash-chained) log, and the envelope's **version discriminator (F1) has no slot in Locked Doc 15 today** — AMD-94 is the formal vehicle that adds it. Activating the cipher before that slot exists would freeze a v-less envelope forever. AB-1 + AB-2 do **not** activate the cipher and write no sensitive data, so they are safe to land first (nothing writes sensitive data at HEAD — no integrations, no automation publish; the "expose-before-cipher" window is currently empty).

## What This Implements

At the instant `main()` exposes the system, five things go live or lock together (charter §1 "Seam 1"): the HTTP surface becomes live + authenticated (AB-1), the at-rest cipher activates so a read-path decrypt failure becomes a live availability risk (AB-2/C2), and the one-way crypto doors lock as the first encrypted row is written (AB-4/F1/F2/F3). AB-3 built the runnable composition root but deliberately left the integration points **closed/inert**: HTTP is gated CLOSED behind a test-only `exposeHttpSurface()`, and the `PayloadCipher` is `null`. This work flips them on — **AB-1** wires authentication + a loopback-default bind into the production phase progression and opens HTTP **only behind auth**; **AB-2** makes the read path fail **closed** with a distinct, loud, typed error on any decrypt failure (and designs — but does not build — the post-MVP degrade seam); **AB-4 (held)** passes the existing `Main.payloadCipher(...)` adapter into the 6-arg `HomeSynapseCore` ctor to activate the cipher and finalize the envelope.

## RULED escalations (Nick, 2026-06-19 — settled; not open questions)

- **Auth scheme (A2 → scheme) = OPAQUE BEARER TOKENS.** Random 256-bit tokens (URL-safe Base64, 43 chars) presented as `Authorization: Bearer {token}`, validated against a local token store; per-token claims (`scopes[]`, `site_id`) held **server-side** keyed by the token. **No JWT, no signing-key management, no new catalog dependency.** Token-at-rest hashing uses a **JDK-native** one-way hash (SHA-256 over the high-entropy token) — NOT bcrypt (there is **no bcrypt/password-hash library in the version catalog**, and bcrypt's work-factor exists for *low-entropy* passwords; a 256-bit random token does not need it). See the Doc 09 §12.1 currency note in "What to Watch Out For."
- **Bundling/sizing = ISSUE AB-1 + AB-2 NOW; HOLD AB-4 (⛔ AMD-94).** One instruction (this file) for Seam-1 coherence; AB-4's rows are ⛔-marked and do not build until the gate clears.

## Files to Read Before Starting

| File | Why |
|---|---|
| `api/rest-api/MODULE_CONTEXT.md` | Auth/error/rate-limit type inventory; the `RestFilters`/`ReadinessFilter` plumbing AB-1 extends |
| `api/rest-api/src/main/java/module-info.java` | Verbatim JPMS name `com.homesynapse.api.rest`; exports + requires (embedded below) |
| `api/websocket-api/MODULE_CONTEXT.md` | WS subsystem; shared-auth-types contract from rest-api |
| `api/websocket-api/src/main/java/module-info.java` | Verbatim `com.homesynapse.api.ws`; `requires transitive com.homesynapse.api.rest` (embedded below) |
| `core/persistence/MODULE_CONTEXT.md` | `SqliteEventStore` read/write path, the `PayloadCipher` seam, the `encryptedScopes` gotchas |
| `core/persistence/src/main/java/module-info.java` | Verbatim `com.homesynapse.persistence` (embedded below) |
| `core/event-model/MODULE_CONTEXT.md` | `DegradedEvent` (the degrade-seam type AB-2 reuses) |
| `core/event-model/src/main/java/module-info.java` | Verbatim `com.homesynapse.event` (embedded below) |
| `config/configuration/MODULE_CONTEXT.md` | `ScopeKeyManager`/`StandardScopeKeyManager`; the `encrypt` (random IV) vs `encryptPayload` (counter) split — F3 |
| `config/configuration/src/main/java/module-info.java` | Verbatim `com.homesynapse.config` (embedded below) |
| `lifecycle/lifecycle/MODULE_CONTEXT.md` | `HomeSynapseCore` composition root; the AB-3 phase model + the two phase gates |
| `lifecycle/lifecycle/src/main/java/module-info.java` | Verbatim `com.homesynapse.lifecycle`; the `requires com.homesynapse.api.rest` edge (embedded below) |
| `app/homesynapse-app/MODULE_CONTEXT.md` | `Main` composition-root host; the held-not-consumed `payloadCipher(...)` adapter |
| `app/homesynapse-app/src/main/java/module-info.java` | Verbatim `com.homesynapse.app` (embedded below) |
| `homesynapse-core/lifecycle/.../HomeSynapseCore.java` | The `exposeHttpSurface()` seam (l.552), the 6-arg ctor (l.237), the Phase-5 gate (l.463–466), `boundHttpPort()` |
| `homesynapse-core/api/rest-api/.../AuthMiddleware.java` + `RateLimiter.java` | The zero-impl interfaces AB-1 implements; `RestFilters.java` (the `before("/api/*")` readiness gate + `installAdminEndpoints` `/internal/*`) |
| `homesynapse-core/core/persistence/.../SqliteEventStore.java` | `fromRow` (l.774) → `decryptStoredPayload` (l.896); the read-batch abort (C2); the ctor write guard (l.~401) |
| `homesynapse-core/app/.../Main.java` | The 6-arg-ctor call site + the existing `payloadCipher(configDir, clock)` adapter (l.151–169) |
| `homesynapse-core-docs/design/09-*.md §3.3/§3.8/§12` · `10-*.md §3.5` · `12-*.md §3.7` · `15-*.md §3.4/§3.8/§5/§6` | The locked auth/error/WS-auth/phase/crypto contracts |

**Minimum read set (MANDATORY floor):** `HomeSynapseCore.java` regions `start()` (Phase 5 EXTERNAL_INTERFACES) + `exposeHttpSurface()` + the two ctors; `RestFilters.java` (`installReadinessGate`, `installEntityQueryEndpoints`, `installAdminEndpoints`); `SqliteEventStore.java` regions `readRows`/`fromRow`/`decryptStoredPayload` + the ctor guard; `Main.java` (`main`, `payloadCipher`); `AuthMiddleware`/`RateLimiter`/`PayloadCipher` in full. Read more freely; this is the floor.

## STOP-on-Mismatch Gates

Before writing any code, read each file and confirm it matches. **If any diverges, STOP and report — do not proceed on stale assumptions.** (Baseline `60d50ce`; the PM source-verified all of these — re-confirm at the issue HEAD.)

| File | Expected State | What to Check |
|---|---|---|
| `lifecycle/.../HomeSynapseCore.java` | **Two public ctors:** `(Path dbPath, Path configDir, HomeSynapseConfig config, Clock clock, HomeId homeId)` delegating to the **6-arg** `(…, PayloadCipher payloadCipher)`. `public void exposeHttpSurface()` at ~l.552 installs `installReadinessGate` + `installEntityQueryEndpoints` + `installAdminEndpoints` then `app.start(config.httpPort())` **with NO `.host(`**. Phase 5 `EXTERNAL_INTERFACES` is **gated CLOSED** (`setPhase(...)` only, no bind). `payloadCipher` is `null` in production boot. | Confirm the 6-arg ctor arity (AB-4 fills the trailing `PayloadCipher`), the missing `.host(` (AB-1 adds loopback), the closed Phase 5 (AB-1 opens it behind auth), and `boundHttpPort()` reflects not-exposed. |
| `api/rest-api/.../AuthMiddleware.java` + `RateLimiter.java` | Both are **interfaces with NO implementing class repo-wide** (`grep -rl "implements AuthMiddleware"` and `"implements RateLimiter"` → empty). Supporting types present: `ApiKeyIdentity`, `ApiException`, `ProblemType`, `RateLimitResult`, `ProblemDetail(Mapper)`, `ReadinessFilter`. | AB-1 CREATES the impls. The contracts (`authenticate(String) → ApiKeyIdentity throws ApiException`; `check(String apiKeyId) → RateLimitResult`) are frozen — implement against them. |
| `api/rest-api/.../RestFilters.java` | `installReadinessGate` registers `app.before("/api/*", new ReadinessFilter(...))`. `installAdminEndpoints` registers `app.get("/internal/dlq", …)` + `app.get("/internal/projection", …)` — **`/internal/*` lives OUTSIDE the `/api/*` readiness gate**. | The auth filter AB-1 adds must cover **every** route (`/api/*`, `/internal/*`, `/ws/v1`), not the readiness gate's narrow `/api/*`. |
| `core/persistence/.../SqliteEventStore.java` | `readRows` (l.~764) loops `fromRow` with **no per-row catch**. `fromRow` (l.~774) reads `dek_ref`; `null` → plaintext; else `decryptStoredPayload` (l.~896) which **throws `IllegalStateException`** at l.~898 (no cipher wired) and l.~904 (malformed `dek_ref`), then `payloadCipher.decrypt(...)` at l.~912 (which can throw per `PayloadCipher`'s contract). The ctor (l.~302) takes `(…, PayloadCipher payloadCipher, Set<String> encryptedScopes)` as its two trailing args; the existing write-path guard (encrypted scope + null cipher → throw) is at l.~402; `decodeCategories` (l.~842) falls back to SYSTEM "so the read still succeeds" (the DegradedEvent posture). | This is C2/OR-RF-DECRYPT: one bad row aborts the whole batch with a raw, untyped exception. AB-2 makes it a **distinct, typed, loud** fail-closed error (and keeps the whole-batch abort — see SCOPE pin). |
| `core/persistence/.../PayloadCipher.java` | Interface: `EncryptedPayload encrypt(String scopeId, byte[] plaintext)`; `byte[] decrypt(String scopeId, int keyVersion, byte[] ciphertext, byte[] iv)` — **`decrypt` throws `IllegalArgumentException` if the key is absent/destroyed (crypto-shred, CASE-a) and `IllegalStateException` if GCM auth fails (CASE-b).** | AB-2's fail-closed logic keys off these two exception types (CASE-a vs CASE-b) when designing the degrade seam. |
| `app/.../Main.java` | `main()` constructs `HomeSynapseCore` via the **5-arg** ctor (cipher inert). `static PayloadCipher payloadCipher(Path configDir, Clock clock)` exists (l.~151–169) and wraps `ScopeKeyManager.create(...)`, calling **`keyManager.encryptPayload`** (counter path) in `encrypt` — held-not-consumed. | AB-4 flips `main()` to the 6-arg ctor passing `payloadCipher(configDir, clock)`; fixes the stale "five-argument ctor" Javadoc/comment nits (l.~141 Javadoc, l.~62 comment). |
| `config/.../ScopeKeyManager.java` + `StandardScopeKeyManager.java` | `encrypt` (fresh **random** 96-bit IV — M6.2 secrets path) + `encryptPayload` (per-scope **counter** nonce — M6.3 event path) + `decrypt`. Javadoc warns the two constructions must not be generalized across paths. | F3 (AB-4): enforce one nonce-construction-per-scope (NIST SP 800-38D §8.3). |
| `core/event-model/.../DegradedEvent.java` | `record DegradedEvent(String eventType, int schemaVersion, String rawPayload, String failureReason) implements DomainEvent` — currently for **schema-upcast** failures (strict/lenient). | AB-2 reuses this type for the crypto degrade **seam** (design-only); does NOT change it. |
| `build.gradle.kts` (root) | `moduleGraphAssert.allowed` includes `:lifecycle:.* -> :api:.*` (l.~58). | Any NEW module edge AB-1/AB-4 add must be in this allow-list AND pass the `requires transitive`↔`api` lockstep (two-gate check below). |
| **Doc 15 watermark + AMD-94 ratification (AB-4 gate)** | The AMD-94 file **exists** (`design/amendments/AMD-94_Doc15-sec6_*.md`) but at authoring is **PROPOSED / untracked / NOT folded**: on-disk watermark = **AMD-93**, Doc 15 body has **no version-byte slot** (`grep -i "version byte\|payload_alg\|envelope.version" 15-*.md` → empty), docs HEAD still `32afb3f`. | **The gate keys on RATIFICATION, not file-presence.** Build AB-4 **only when** AMD-94's status reads RATIFIED **and** Doc 15 §4.1/§5 carries the version-byte fold **and** the watermark reads **AMD-94**. If the file is present but still PROPOSED / watermark still AMD-93 → **STOP, AB-4 is GATED.** (Do not mistake the PROPOSED file's appearance for the gate clearing.) |

## Settled Decisions

These are resolved — implement exactly, do not re-open.

- **A1 bind = loopback-default.** Bind `127.0.0.1` by default; LAN exposure is an explicit, **authenticated** config opt-in; **never bind-all-by-default**; treat **no** interface as "internal."
- **A2 auth = token issuance → opaque bearer tokens** (RULED scheme, above). WS is an external interface and **is authenticated**. Zero-config stays **authenticated** (no default/shared bootstrap secret; no pre-auth account enumeration; no unauthenticated stream/media path). Carry the **enterprise per-scope/per-site-claims hook** (design the token-claims record now; MVP may issue a single full-access claim).
- **A3 read = fail-closed at MVP + design the degrade seam now.** Distinct loud error on decrypt failure; the degrade *behavior* is OUT (crypto-shred WU). **F4 pin:** the degrade half + the chain-validity check stay DISABLED until `chain_hash` + mandatory startup-verify are live (32-byte ZERO today).
- **A4 (AB-4, ⛔ AMD-94) = rotate-DEK-on-restore + reserve the 1-byte envelope version tag.** Rotate = **additive new DEK version, retain priors** (never re-encrypt/replace — F6); high-water-mark = defense-in-depth cross-check only; **v1 = the current envelope.** The slot is AMD-94's to add to Doc 15 §5; AB-4 consumes the ratified format.
- **F2 scope width = `[identity, presence_personal]`** (resolved, OQ-15-2) — already the wired `encryptedScopes`; no change.

---

## Technical Specification — AB-1 (Auth + bind posture) · ISSUE NOW

### A1.1 `StandardAuthMiddleware implements AuthMiddleware`
**Package:** `com.homesynapse.api.rest` · **Responsibility:** validate an `Authorization: Bearer {token}` header against the local opaque-token store and return the caller identity (or reject).

**Behavioral contract:**
- Parse the header; missing/malformed (`null`, blank, not `Bearer `-prefixed) → `throw new ApiException(ProblemType.AUTHENTICATION_REQUIRED)` (401, `WWW-Authenticate: Bearer`).
- Hash the presented token (JDK-native SHA-256 of the raw token bytes) and look it up in the token store. Absent / revoked / expired → `ApiException(ProblemType.FORBIDDEN)` (403).
- Valid → return `ApiKeyIdentity` (today `keyId`, `displayName`, `createdAt` — **never** the raw token). **The enterprise per-scope/per-site-claims hook is NEW design — `ApiKeyIdentity` does not carry claims today.** Add the claims (`scopes[]`, `siteId`) either as new fields on `ApiKeyIdentity` or as a separate claims type the middleware resolves and attaches; design the record now (A2 caveat) even though MVP enforcement is binary (a valid token grants access — Doc 09/10 Tier-1). Flag the record-shape change `[REVIEW]` (public-API shape).
- **Thread-safe** for concurrent virtual-thread invocation. Use `ReentrantLock`/concurrent structures, **never `synchronized`** (LTD-11 — VT pinning). The raw token is **never logged** (reference by `key_id` only).

### A1.2 The opaque-token store
**Responsibility:** persist `{token_hash → (key_id, display_name, created_at, scopes[], site_id)}`; mint (first-run/pairing), validate, revoke, rotate.
- Tokens are **256-bit random** (`SecureRandom`), URL-safe Base64 (43 chars), shown **once** at creation, stored only as the SHA-256 hash (INV-SE-03 — at rest in the config dir).
- **Storage location + module edge (Coder's call within the constraint):** the key store may be config-resident (mirroring `secrets.enc`/`scope_keys.json`) and injected at the composition root — if so, define the store **interface in `api.rest`** (consumer-defined seam, the `PayloadCipher`/AMD-45 pattern) and host the impl/construction in `lifecycle`/`app` so **no new forbidden module edge** is created. A self-contained file-backed store inside `api.rest` (reading a config-dir path passed in) is also acceptable. **Run the two-gate module check on whatever edge you choose.** Flag your choice as `[REVIEW]`.
- **Pairing/first-run flow (PM design within the ruling):** on first boot with no token store, mint one initial token and surface it once via the boot log / a first-run artifact (no network call — R-δ AX-9 Insteon-brick check). **Rotation** = mint-new + revoke-old (no in-place mutation). Keep it minimal; the full pairing UX is post-MVP.

### A1.3 `StandardRateLimiter implements RateLimiter`
**Package:** `com.homesynapse.api.rest` · **Responsibility:** per-key token bucket.
- `check(String apiKeyId) → RateLimitResult`. Defaults from Doc 09 §9: `requests_per_minute: 300`, `burst_size: 50`. `ConcurrentHashMap<String, bucket>`; one `long` token count + one `long` last-refill per key; bounded by active-key count. On exceed → `RateLimitResult.allowed()==false` with `retryAfterSeconds()` → the filter returns `429` + `Retry-After` + `ProblemType.RATE_LIMITED`.
- **Clock-injected** (do not call `Instant.now()`/`System.nanoTime()` — §4c). Thread-safe, `ReentrantLock`/atomics only.

### A1.4 The auth filter + the bind posture (the C1 close)
- Add an **auth filter** registered as a Javalin **catch-all** `before("*")` (or explicit coverage of `/api/*` **and** `/internal/*` **and** the `/ws/v1` upgrade) that runs `StandardAuthMiddleware` (then `StandardRateLimiter` for authenticated calls) **before any path resolves**. **Canonicalize the request path first** (reject `..`/encoded-traversal before the auth decision — R-δ AX-1 / CVE-2023-27482). This filter must run **before** `installReadinessGate`'s `/api/*` gate. Surface it as a new `RestFilters.installAuth(app, authMiddleware, rateLimiter)` (or equivalent) so the composition root wires it.
- **Bind posture:** in `exposeHttpSurface()` change `app.start(config.httpPort())` → bind **loopback by default** (`app.start("127.0.0.1", config.httpPort())` or the Javalin host-config equivalent). LAN exposure is an explicit config opt-in (e.g., a `config`-surfaced bind-host / `lan_exposure` flag) that, only when set, binds the configured non-loopback host. **Never bind `0.0.0.0` unless LAN opt-in is explicitly configured.** (Javalin/Jetty default to `0.0.0.0` when host is unset — that is exactly the C1 hole.)
- **Wire into the production progression:** make Phase 5 `EXTERNAL_INTERFACES` in `start()` actually invoke the (now auth-gated, loopback-bound) HTTP bring-up — i.e., production `start()` opens HTTP **only after `AuthMiddleware`/`RateLimiter` are installed**. The auth-before-network-exposure ordering is a hard invariant: **no port binds before the auth filter is registered.** Keep `exposeHttpSurface()` idempotent; the test path and the production path converge on the auth-gated bring-up.
- **WebSocket auth (Doc 10 §3.5):** the WS client's **first message must be `authenticate`** with the opaque token (`api_key` field); validate against the **same** token store; a non-`authenticate` first message or an invalid token → close **4403**; no `authenticate` within 5 s → close **4408**. No event data to an unauthenticated connection (INV-SE-02).

### A1.5 CC-1 confirm-mechanics gate (folds in per A1 — not a standalone spike)
- Assert (test) that after the production `start()` opens HTTP, the bound socket **answers only on loopback** unless LAN opt-in is configured: connect via `127.0.0.1` (must succeed) and via a non-loopback local address (must **refuse** in the default config).
- Static check: `grep -rn "\.host(" lifecycle api app` must now show **exactly** the loopback-default bind in the production start path (it flips from today's "no matches" — the vulnerable state — to the explicit loopback bind).

### A1.6 Flip the C1 regression test
- `start_doesNotOpenHttpSurface` becomes **`opensHttpOnlyBehindAuth`**: production `start()` now binds the loopback HTTP port **with the auth filter installed**; assert (a) the port is bound, (b) an unauthenticated `/api/*` **and** `/internal/*` request → 401, (c) a non-loopback connection is refused by default. **Grep every caller of any HSC public method you reshape** (`exposeHttpSurface`, `boundHttpPort`, the Phase-5 invocation) across production + test + **`testing:integration-tests`** (`HomeSynapseE2eHarness`, `EndpointE2eIT`) and enumerate them in Files-to-Modify (the AB-3 public-signature-fan-out lesson).

---

## Technical Specification — AB-2 (Read contract, fail-closed half) · ISSUE NOW

### A2.1 Make the read path fail closed with a distinct, loud, typed error
**File:** `core/persistence/.../SqliteEventStore.java` (+ a new exception type in `com.homesynapse.persistence`).
- Introduce a **typed** fail-closed exception (e.g., `PayloadDecryptionException extends RuntimeException`) carrying the **cause**: `globalPosition`, `scopeId` (when parseable), `keyVersion` (when parseable), and a `failureKind` enum — `NO_CIPHER_WIRED`, `MALFORMED_DEK_REF`, `GCM_AUTH_FAILED` (from `PayloadCipher.decrypt`'s `IllegalStateException` — CASE-b), `KEY_ABSENT_OR_DESTROYED` (from `IllegalArgumentException` — CASE-a). Replace the raw `IllegalStateException`s in `decryptStoredPayload` and wrap the `payloadCipher.decrypt(...)` call to classify its two exception types.
- **Message: Register C voice** (direct, neutral, no self-reference/apology). Include the path + required perms for the missing-root-key case (INV-HO-04), per Doc 15 §6: "no silent plaintext fallback."

### A2.2 Pin the fail-closed SCOPE explicitly (the AB-3 SD-9 lesson — state the failure domain)
- **Failure domain = per read-batch / per replay-segment.** A decrypt failure in `fromRow` aborts the **entire `readRows` batch** loudly with the typed error above. This is **NOT** per-row degrade (the degrade half is OUT/F4-gated) and **NOT** a silent skip and **NOT** whole-store-silent-corruption. The whole-batch abort is the *intended* MVP contract (A3): a lost/corrupt root key making the store unreadable is a **loud, visible** failure, not a quiet one. Do not "rescue" the read by degrading — that masks CASE-b tampering (R-α REC-234, disproven).
- The boot-time consequence (a replay that hits an undecryptable row fails closed) is the correct MVP posture vs INV-RF-04: the store is *intentionally* unreplayable when the key is gone, surfaced loudly, rather than silently dropping events.

### A2.3 Design the degrade SEAM now (design-only; behavior OUT)
- Document, in code/Javadoc + MODULE_CONTEXT, how a **future** CASE-a (intended crypto-shred, where `chain_hash` validates) would map to a `DegradedEvent` carrying the `(scope, key_version)` cause via a new `failureReason` — i.e., a `(scope, key_version)`-keyed cause lookup + a chain-validity check. **Do NOT wire it.** Leave the `DegradedEvent` type unchanged (it exists for schema-upcast today; the crypto reuse is a later additive `failureReason`).
- **F4 pin (verbatim intent):** the degrade half and the chain-validity check **must not be enabled until `chain_hash` computation + mandatory startup verification are live** (all-ZERO today). The MVP fail-closed half does not need the chain. Wire fail-closed now; gate the chain-dependent parts on chain activation.
- **Carry (design note only):** the rotate-DEK-on-restore **boot invariant** (R-α REC-235) — refuse to encrypt in a scope until a fresh DEK is installed OR the persisted counter is proven ≥ all prior nonces (assert resumed counter ≥ carried max). The full mechanics ride AB-4 + the backup/restore WU; note it so AB-4 inherits it.

### A2.4 Tests (both decrypt-failure paths — currently NONE)
**Test class:** `SqliteEventStoreDecryptFailClosedTest` (Clock-injected, §4c).

| Test Method | Scenario | Assertion |
|---|---|---|
| `missingCipherOnRead_failsBatchClosed` | An encrypted row (non-null `dek_ref`/`payload_iv`) is present; `payloadCipher == null` | `readRows`/the query throws `PayloadDecryptionException(NO_CIPHER_WIRED)` carrying `globalPosition`; the whole batch aborts; no plaintext is returned and no silent fallback occurs |
| `undecryptableKeyOnRead_failsBatchClosed` | `payloadCipher` present but `decrypt` throws (stub a cipher that throws `IllegalStateException` for GCM-auth-fail and, separately, `IllegalArgumentException` for a destroyed key) | `readRows` fails the batch closed with `PayloadDecryptionException` classified `GCM_AUTH_FAILED` / `KEY_ABSENT_OR_DESTROYED` respectively, carrying `(scopeId, keyVersion, globalPosition)` |

---

## Technical Specification — AB-4 (payloadCipher activation + envelope-finalization) · ⛔ GATED ON AMD-94 — DO NOT BUILD YET

> **⛔ Every row in this section is HELD.** Build only after AMD-94 is ratified + folded into Doc 15 and the watermark reads AMD-94 (re-confirm at Step-0). Re-read AMD-94 for the exact ratified envelope format before implementing F1.

### A4.1 ⛔ Activate the cipher
- In `Main.main()`, switch to the **6-arg** `HomeSynapseCore` ctor: `new HomeSynapseCore(dbPath, configDir, HomeSynapseConfig.HOME_DEFAULT, clock, homeId, payloadCipher(configDir, clock))`. The adapter already exists (held-not-consumed) and already calls `encryptPayload` (counter path). Fix the stale **"five-argument ctor"** Javadoc nits in `Main` (the cipher ctor is **6-arg**). The cipher activates at Phase 2 (`DATA_INFRASTRUCTURE` ≡ Doc 15's "PERSISTENCE_READY") — before any sensitive read/write, well before Phase 5 HTTP exposure.

### A4.2 ⛔ F1 — envelope version discriminator
- Implement **exactly the format AMD-94 ratifies** (1-byte algorithm/version tag, **v1 = current envelope**; mechanism — in-band ciphertext/IV prefix vs a `payload_alg`/`envelope_version` column — is AMD-94's call). **Do NOT invent the slot or default-by-omission.** R-γ later refines the version *policy*, not the slot's existence.

### A4.3 ⛔ F3 — one nonce-construction-per-scope (NIST SP 800-38D §8.3)
- In `StandardScopeKeyManager`, **enforce** that a given scope binds to exactly one nonce construction: the encrypted event scopes (`identity`, `presence_personal`) use the **counter** path (`encryptPayload`); the secrets scope (`config_secrets`) uses the **random-IV** path (`encrypt`). Reject the cross-construction call (a scope that has issued a counter nonce must not also issue a random IV, and vice versa). Encode the NIST citation + the enforced invariant per AMD-94's §3.4 text. (The adapter is already correct; this hardens the manager so it cannot be misused.)

### A4.4 ⛔ F13 — write-path hardening
- **(a)** `SqliteEventStore` ctor: add the **fail-closed guard** — if `payloadCipher == null` then `encryptedScopes` MUST be empty (today the ctor only assigns; the Javadoc promises the guard). Throw a clear `IllegalStateException` otherwise.
- **(b)** On the **nonce-counter write** specifically (`config`/`AtomicYamlWriter` dir-fsync path), treat a dir-fsync `IOException` as **FATAL/fail-closed**, not swallowed at DEBUG — the OR-M6-NONCE durability rests on it.

### A4.5 ⛔ Backup-key portability SEAM (R-δ AX-4 — design now, mechanics later)
- Decide + document the **seam** for an exportable, re-enterable recovery artifact tied to the per-scope keys (so a zero-config machine-local-key install can restore on new hardware). **Seam only** — the export/import mechanics are the backup/restore WU. Carry the rotate-DEK-on-restore contract (A4: additive new DEK version, retain priors; boot invariant from A2.3).

⛔ **Un-gate condition (repeat):** AMD-94 RATIFIED + folded into Doc 15 §3.4/§5/§6, watermark = AMD-94 on disk. Until then, AB-4 ships nothing.

---

## Verbatim module-info embeds (re-confirm at HEAD; show a proposed diff for any new `requires`/`exports`)

Per the Research-6 lesson, the current `module-info.java` of each touched module is embedded verbatim. **Any JPMS change AB-1/AB-4 introduces must be shown as a diff against these AND pass the two-gate check below.** AB-1 may need a new edge only if the token store lives in another module (see A1.2 — prefer the consumer-defined-seam pattern that adds **zero** edges).

**`api/rest-api/src/main/java/module-info.java`** (AB-1 adds auth impls — likely same exported package, no new edge unless the store crosses a module):
```java
module com.homesynapse.api.rest {
    requires transitive com.homesynapse.state;
    requires com.homesynapse.event.bus;
    requires io.javalin;
    requires org.slf4j;
    exports com.homesynapse.api.rest;
}
```

**`api/websocket-api/src/main/java/module-info.java`** (AB-1 adds WS first-message auth using the shared rest-api auth types — already `requires transitive`):
```java
module com.homesynapse.api.ws {
    requires transitive com.homesynapse.api.rest;
    exports com.homesynapse.api.ws;
}
```

**`lifecycle/lifecycle/src/main/java/module-info.java`** (already `requires com.homesynapse.api.rest`, non-transitive, for the composition-root filter wiring — AB-1 reuses this edge; the `:lifecycle:.* -> :api:.*` graph edge is allow-listed):
```java
// (head) requires transitive observability, event, platform;
//        requires transitive persistence, event.bus, state;
//        requires integration; requires api.rest;  // M3.6e.1 — the Javalin filter wiring
//        AB-3 added: requires config, device, automation; requires platform.systemd
```
*(Embed the full current file verbatim in your working copy; the load-bearing line is the existing non-transitive `requires com.homesynapse.api.rest` — AB-1's auth filter wiring rides it.)*

**`core/persistence/src/main/java/module-info.java`** (AB-2 adds a fail-closed exception type in the already-exported `com.homesynapse.persistence` package — no new edge; `DegradedEvent` is in `com.homesynapse.event`, already `requires transitive`):
```java
// requires transitive platform, state, event, event.bus; requires value, device,
// java.sql, org.slf4j, jackson(core/databind/jsr310/blackbird); exports com.homesynapse.persistence;
```

**`app/homesynapse-app/src/main/java/module-info.java`** (AB-4 — already `requires` both config + persistence + lifecycle; the adapter adds **no** edge):
```java
// requires lifecycle, observability, event, device, state, persistence, event.bus,
//   automation, integration, integration.runtime, integration.zigbee, config, api.rest, api.ws, platform;
```

## Error Handling (Register C voice — direct, neutral; no "we"/"sorry"/"please")

| Condition | Type | Message Pattern | Recovery |
|---|---|---|---|
| Missing/malformed `Authorization` | `ApiException(AUTHENTICATION_REQUIRED)` → 401 + `WWW-Authenticate: Bearer` | RFC 9457 `authentication-required` Problem body (`type`,`title`,`status`,`detail`,`instance`,`correlation_id`) | Caller supplies a valid bearer token |
| Invalid/expired/revoked token | `ApiException(FORBIDDEN)` → 403 | RFC 9457 `forbidden` | Caller obtains a valid token |
| Rate exceeded | `RateLimitResult.allowed()==false` → 429 + `Retry-After` | RFC 9457 `rate-limited` | Caller backs off `retryAfterSeconds` |
| WS non-`authenticate` first msg / bad token | close **4403** | `auth_result {success:false, error:{error_type:"forbidden"}}` | Client re-handshakes with a valid token |
| WS no auth within 5 s | close **4408** | — | Client authenticates within the window |
| Read: encrypted row, no cipher wired | `PayloadDecryptionException(NO_CIPHER_WIRED)` — **fail batch closed** | "event at global_position %d is encrypted (dek_ref=%s) but no PayloadCipher is wired" | Operator restores the root key; no plaintext fallback (Doc 15 §6) |
| Read: GCM auth-fail / destroyed key | `PayloadDecryptionException(GCM_AUTH_FAILED|KEY_ABSENT_OR_DESTROYED)` — **fail batch closed** | distinct loud error carrying `(scope, key_version, global_position)` | MVP: surface loudly. CASE-a degrade is post-MVP (F4-gated) |

All RFC 9457 bodies carry the `correlation_id` extension (= `X-Correlation-ID`), per Doc 09 §3.8 (AMD-15). Error `type` URIs are documentation, not network resources.

## Locked Decisions That Apply
- **Doc 09 §3.3/§3.8/§12** — the `Authorization: Bearer` auth model, the RFC 9457 (`application/problem+json`) error model + Problem-type registry, per-key token-bucket rate limiting (300 rpm / burst 50). **INV-SE-02** (auth mandatory on every external interface; no local-trust exception), **INV-SE-03** (keys encrypted at rest).
- **Doc 10 §3.5** — WS first-message `authenticate`, close codes 4403/4408, same key store as REST.
- **Doc 12 §3.7 / C12-08** — Phase 5 EXTERNAL_INTERFACES; `READY=1` only after the APIs are serving; the fixed phase order (cipher at Phase 2 → core domain Phase 3 → APIs+auth Phase 5 → integrations Phase 6).
- **Doc 15 §3.4/§3.8/§5/§6** — counter-nonce-per-scope, the app-hosted `ScopeKeyManager→PayloadCipher` adapter, the envelope/failure-mode contracts. **AB-4 also consumes AMD-94** (the version-byte slot) — gated.
- **LTD-11 (No Broker / VT):** `ReentrantLock`, never `synchronized` (VT pinning) — auth store, rate limiter, any lock on the publish/read path. **LTD-04 (ULID):** typed ULID wrappers; Crockford Base32 only at boundaries.

## Invariants That Must Hold
- **INV-SE-02** — every external route (`/api/*`, `/internal/*`, `/ws/v1`) is authenticated; the auth filter runs before any path resolves. **Test:** unauthenticated `/api/*` AND `/internal/*` → 401; unauthenticated WS first message → close 4403.
- **Auth-before-network-exposure (tracked gate)** — no HTTP port binds before the auth filter is installed. **Test:** the production progression installs auth in Phase 5 strictly before `app.start(...)`; `opensHttpOnlyBehindAuth` proves it.
- **CC-1 loopback-default** — the bound socket answers only on loopback unless LAN opt-in is configured. **Test:** A1.5.
- **INV-RF-04 / fail-closed** — a decrypt failure fails the read batch closed loudly (no silent corruption, no silent plaintext). **Test:** A2.4 (both paths).
- **INV-PD-07 (design-only)** — the crypto-shred seam (`DegradedEvent` type + `(scope,key_version)` lookup) is *designed*, not wired; the degrade behavior + tombstone are OUT.

## P2 Consumer/Pin (Fan-Out) Survey (MANDATORY)

AB-1 + AB-2 mint **no new event type, no enum value, no sealed permit, no manifest entry** (they wire existing pieces + add impls/an exception type). The fan-out to sweep — run each grep at the **issue HEAD**, do not assume the lists are exhaustive:

- **Public-method-signature change (the AB-3 lesson — first-class category):** AB-1 reshapes the External-Interfaces invocation and may touch `exposeHttpSurface()`/`boundHttpPort()`/`start()`. **Grep every caller of any HSC public method you change** — production + test, **all modules** — `grep -rn "exposeHttpSurface\|boundHttpPort\|\.start()" lifecycle app testing api` — and enumerate each (esp. `testing:integration-tests` `HomeSynapseE2eHarness` + `EndpointE2eIT`, which AB-3's gate-flip already touched). The `start_doesNotOpenHttpSurface` → `opensHttpOnlyBehindAuth` flip is one such consumer.
- **Auth-middleware route registrations:** every registered route must sit behind the auth filter. Sweep `RestFilters` (`installReadinessGate` `/api/*`, `installEntityQueryEndpoints`, `installAdminEndpoints` `/internal/dlq`+`/internal/projection`) **and** the WS upgrade handler (`/ws/v1`). The filter is catch-all `before("*")` (or explicit coverage of all three) — **not** the readiness gate's narrow `/api/*`.
- **`module-info` / contract-direction (JPMS):** if the token store crosses a module, verify the edge direction (consumer-defined seam in `api.rest`, impl injected from `lifecycle`/`app` — zero new edge, the `PayloadCipher` pattern). Any new `requires` on an **exported** signature → `requires transitive` + Gradle `api(...)` (lockstep).
- **Count pins / manifest aggregators:** AB-2's new `PayloadDecryptionException` is not a `DomainEvent` and mints no manifest entry. **If you add a `system_root_key_unavailable` (or any) lifecycle EVENT**, that is a manifest fan-out — sweep `EventTypes`, `CORE_PRODUCTION_EVENT_CLASSES`, `EventCategoryMapping.TABLE`, the `HomeSynapseCore` aggregation (the latent-runtime site no test pins), and every `hasSize(N)`/`isEqualTo(N)` count pin. **Prefer to throw the typed exception + log loudly rather than mint a new event type** unless Doc 15 §6's `system_root_key_unavailable` is required at boot — if so, flag `[REVIEW]` and run the full manifest sweep.
- **Behavioral publish-count pins:** AB-1/AB-2 add no event publish site on an existing path. If you do, sweep the producing module's whole test suite for publisher-interaction assertions.

## Two-gate module-graph check (FIX-07 — run for EVERY new edge)
For any new module edge (auth store crossing modules; any AB-4 config/persistence touch): run **BOTH** gates — **(1)** `assertAllowedModuleDependencies` (is the `from→to` LAYER edge allow-listed in root `build.gradle.kts` `moduleGraphAssert.allowed`? `:lifecycle:.* -> :api:.*` is; a `:api:.* -> :config:.*` or any backward/cross-layer edge is **not** and must move the type to `lifecycle`/`app`), **AND** **(2)** the `requires transitive`↔Gradle `api(...)` lockstep for any type that appears on an **exported** signature. Package-private confinement keeps a type off the exported API (plain `requires`/`implementation` for an **allowed** edge) but **cannot rescue a forbidden layer edge.** Re-run the lockstep against any NEW public type the WU adds.

## Internal-consumer survey
- **`SqliteEventStore` ctor / `decryptStoredPayload`:** enumerate every construction site + read caller before changing the throw behavior. The write-path guard (encrypted scope + null cipher → throw, l.~401) is the existing fail-closed write half; AB-2 adds the symmetric **read** half. Confirm both halves agree (write rejects, read fails closed).
- **`exposeHttpSurface()` callers:** today only test/IT harnesses. AB-1 adds the production caller — ensure idempotency holds (the `httpServer != null` early-return).

## What to Watch Out For

- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in `rest-api`, `websocket-api`, `persistence`, `config`, or `lifecycle` **test** code — `NO_DIRECT_TIME_ACCESS` scans non-whitelisted classes. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)` injected via ctor/`@BeforeEach`. (§4c caveat: the rule actively scans only `app`'s test classpath — treat clock-injection as a self-enforced convention everywhere else; `app`/`platform`/`test` production code is whitelisted.)
- **AB-3 lessons (carry all):** (1) **public-method-signature fan-out** — grep every caller, prod + test, all modules (above). (2) **Pin the fail-closed SCOPE** — AB-2 states per-read-batch explicitly; a green test encoding the wrong domain is worse than a red one. (3) **Verify cross-layer wiring against the consuming subsystem's own contract with a POPULATED fixture, not the zero-config path** (the AB-3 loader-nesting bug compiled + passed an empty boot). (4) **Re-run the api↔requires-transitive check against any NEW public type** even when you believe a module-info is unchanged.
- **Reconciliation flags discovered by the PM (do not be surprised by these):**
  - **`/internal/*` is real in code but absent from Doc 09's endpoint taxonomy** — `installAdminEndpoints` registers `/internal/dlq`+`/internal/projection` outside the `/api/*` gate. The auth filter MUST cover them. *(Doc 09 currency nit — flag for a later doc fix; non-blocking.)*
  - **REST default-port disagreement:** Doc 12 §5.1 says 8123, Doc 09 §9 says 8080. **Use `config.httpPort()`** (the existing code path); pin no literal. *(Doc 09/12 currency nit; non-blocking.)*
  - **No bcrypt/password-hash library in the version catalog** — hence the JDK-native SHA-256 over the 256-bit token (RULED). Do **not** add a catalog dependency without Nick's approval. *(Doc 09 §12.1 says "bcrypt" — currency nit; the high-entropy-token rationale is in the masthead.)*
  - **The 1-byte envelope version tag has no slot in Locked Doc 15 §5** — that is precisely AMD-94's job; AB-4 consumes the ratified format. This is *why* AB-4 is gated.
  - **`Main` Javadoc says "five-argument ctor"** for the AB-4 fill — the cipher ctor is **6-arg**; fix the nit when you build AB-4.
- **Javalin/Jetty bind:** unset host ⇒ `0.0.0.0` (all-interfaces). The loopback default must be **explicit** in the production start path.
- **Auth-before-path-resolve:** canonicalize the path before the auth/authorization decision; an un-canonicalized `..`/encoded-traversal must not bypass the filter (CVE-2023-27482).
- **WS transport constraint:** browsers can't set custom WS headers — auth is the **first message**, not a header (Doc 10 §3.5). Existing authenticated WS connections stay valid if the auth store goes unavailable (validated at connect time).
- **Do NOT activate the cipher in AB-1/AB-2** — `payloadCipher` stays `null`/inert until AB-4. AB-2's read contract is pure safety wiring for when AB-4 lands; it writes/encrypts nothing.

## Files to Create or Modify (indicative — confirm at HEAD; the Files table governs over prose)

| Action | File | Piece |
|---|---|---|
| CREATE | `api/rest-api/.../StandardAuthMiddleware.java` (+ token-store seam/impl) | AB-1 |
| CREATE | `api/rest-api/.../StandardRateLimiter.java` | AB-1 |
| MODIFY | `api/rest-api/.../RestFilters.java` (add `installAuth(...)` catch-all + path canonicalization) | AB-1 |
| MODIFY | `api/websocket-api/.../` WS upgrade/auth handler (first-message `authenticate`, 4403/4408) | AB-1 |
| MODIFY | `lifecycle/.../HomeSynapseCore.java` (Phase 5 invokes auth-gated, loopback-bound bring-up; flip the C1 test) | AB-1 |
| MODIFY | `lifecycle/.../HomeSynapseCoreTest.java` + `testing/integration-tests/.../HomeSynapseE2eHarness.java` + `EndpointE2eIT.java` | AB-1 |
| CREATE | `core/persistence/.../PayloadDecryptionException.java` | AB-2 |
| MODIFY | `core/persistence/.../SqliteEventStore.java` (`decryptStoredPayload` typed fail-closed; classify CASE-a/CASE-b) | AB-2 |
| CREATE | `core/persistence/.../SqliteEventStoreDecryptFailClosedTest.java` (2 tests) | AB-2 |
| MODIFY | `core/persistence/MODULE_CONTEXT.md` + `api/rest-api/MODULE_CONTEXT.md` + `lifecycle/.../MODULE_CONTEXT.md` | AB-1/AB-2 |
| ⛔ MODIFY | `app/.../Main.java` (6-arg ctor + adapter; Javadoc nit) | AB-4 (HELD) |
| ⛔ MODIFY | `config/.../StandardScopeKeyManager.java` (F3 enforcement) · `core/persistence/.../SqliteEventStore.java` ctor guard (F13a) · `config/.../AtomicYamlWriter.java` (F13b) · F1 per AMD-94 | AB-4 (HELD) |

## Dependencies and Integration Points
- **Consumes:** `AuthMiddleware`/`RateLimiter` (rest-api, l zero-impl), `ApiKeyIdentity`/`ApiException`/`ProblemType`/`RateLimitResult` (rest-api), `RestFilters`/`ReadinessFilter` (rest-api), `PayloadCipher`/`EncryptedPayload` (persistence), `ScopeKeyManager`/`ScopeCipherResult` (config), `DegradedEvent` (event-model), `HomeSynapseConfig`/`SystemLifecycleManager` (lifecycle).
- **Produces:** the auth filter + bind posture on the live HTTP/WS surface; the typed fail-closed read contract; (AB-4) the active cipher + finalized envelope.
- **Cross-subsystem:** lifecycle wires rest-api auth into the composition root (the allow-listed `:lifecycle:.* -> :api:.*` edge); app hosts the `PayloadCipher` adapter (AB-4); WS shares the rest-api token store.

## Coder Pushback Welcome
If any spec here is impractical, contradicts a MODULE_CONTEXT gotcha or the actual source at HEAD, or could be done better at the same contract — **raise it** (escalation format in your skill doc). In particular: the token-store **module placement** (A1.2) is left to your judgment within the zero-new-forbidden-edge constraint — if the cleanest placement implies an edge, flag it before wiring. If you find AB-1/AB-2 cannot be built without touching an AB-4-gated surface, STOP and report (they are designed to be separable).

## Out of Scope (do not build)
- The **degrade behavior** (CASE-a → `DegradedEvent`), the **KEK-destruction API**, the **shred tombstone** — post-MVP crypto-shred WU.
- **`chain_hash` activation** + the chain-validity check (F4-gated; ZERO today).
- **Backup/restore mechanics** (AB-4 decides the *seam* only).
- **Per-entity/per-area authorization** (Tier-1 is binary), **TLS/WSS** (Tier-2), the **R-γ version-policy** refinement (AB-4 reserves only the slot).
- **M7.2 run/action/dispatch**, **device-model breadth/integrations (M9)**, any **`automation_triggered` production publish** (C1-interim holds to M7.2).
- **AB-4 itself** until AMD-94 ratifies.

## Build Discipline
You produce files; you do **NOT** run `./gradlew`. Nick runs the build gate. **Deferred build gate** — flag in `coder-handoff.md` + the WUCP Phase 1 checklist: (1) targeted `./gradlew :api:rest-api:compileJava :api:websocket-api:compileJava :core:persistence:compileJava :lifecycle:lifecycle:compileJava :app:homesynapse-app:compileJava` (the `-Werror`/`[exports]`-sensitive touched modules — shift-left the lockstep class), then (2) full `./gradlew check` (touched: rest-api, websocket-api, persistence, lifecycle, app, testing:integration-tests).

## MODULE_CONTEXT.md Update
After the files are written: `api/rest-api/MODULE_CONTEXT.md` (the new auth impls + the catch-all auth filter + loopback bind), `core/persistence/MODULE_CONTEXT.md` (the typed fail-closed read contract + the designed-not-wired degrade seam + the F4 pin), `lifecycle/.../MODULE_CONTEXT.md` (Phase 5 now opens HTTP behind auth). Note new gotchas (the `/internal/*`-must-be-behind-auth catch; the loopback-default-must-be-explicit Javalin trap).

## Success Criterion (binary) — AB-1 + AB-2
The work is DONE when:
1. `StandardAuthMiddleware` + `StandardRateLimiter` + the opaque-token store exist and satisfy the Doc 09 §12 / §3.8 contracts; the auth filter covers `/api/*` **and** `/internal/*` **and** `/ws/v1` with path canonicalization before the auth decision.
2. The production `start()` Phase 5 opens HTTP **only behind auth**, **loopback-bound by default**; `start_doesNotOpenHttpSurface` is replaced by `opensHttpOnlyBehindAuth` and the CC-1 loopback assertion passes; every reshaped-HSC-method caller (prod + test + integration-tests) is enumerated and updated.
3. WS first-message `authenticate` is enforced (4403/4408).
4. `SqliteEventStore` fails the read batch **closed** with the typed `PayloadDecryptionException` carrying the cause; the degrade seam is **designed-not-wired** (F4 pin documented); both `SqliteEventStoreDecryptFailClosedTest` cases pass.
5. The two-gate module-graph check is clean for any new edge; the P2 fan-out survey is complete.
6. MODULE_CONTEXT updates applied; WUCP Phase 1 checklist appended to the Completion Report; the deferred build gate flagged.
7. **AB-4 remains ⛔ un-built** (no cipher activation, no envelope change) until AMD-94 ratifies.

## Work Unit Completion (WUCP Phase 1)
After the compile gate passes (or is deferred to Nick), execute WUCP Phase 1: update the MODULE_CONTEXTs, update `coder-handoff.md` (with the Deferred Build Gate flag + next-WU pointer = **AB-4 when AMD-94 ratifies**), append to `coder-lessons.md` if applicable, post a cross-agent note, and append the WUCP Phase 1 checklist here. The WU is not done until the checklist is complete and the deferred gate is explicitly flagged.
