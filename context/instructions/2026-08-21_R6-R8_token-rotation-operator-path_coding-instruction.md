<!--
file: context/instructions/2026-08-21_R6-R8_token-rotation-operator-path_coding-instruction.md
purpose: R-6/R-8 TOKEN-OPS — close F-S5 (TOKEN ROTATION HAS NO OPERATOR PATH; minted 2026-08-20, sitting record §6) the way a trust product closes a credential-hygiene gap: a race-free, restart-time OPERATOR REQUEST mechanism in the token store (rotate · revoke · mint), the `homesynapse-token` helper's verbs over it, a read-only `token status` CLI mode in the packaged runtime, the token-admin `/internal/tokens` endpoints for token-holders (the pairing wizard's future hand-off), two store hardenings found at source during authoring (the non-atomic `persist()` rewrite; the artifact's umask-default mode), and the R-8 riders (the rotation procedure doc; PI-TZ — FENCED, ruling asked). The store's own javadoc already says "rotation is mint-new + revoke-old"; this WU gives that sentence an operator.
audience: the R-6/R-8 Coder lane (host-side Claude Code per D12; compile loop: targeted `./gradlew :api:rest-api:compileJava :api:rest-api:test :lifecycle:lifecycle:compileJava :app:homesynapse-app:compileJava :app:homesynapse-app:test`, then full `./gradlew check`) + Nick (the §OP blocks: the rotation on the bench after landing; the PI-TZ block only on the word).
status: ISSUE-READY (v55 beat 1). Baseline: core `7c9e4fa` (verify at launch; porcelain clean). Execute: Sunday 2026-08-23 or any weekday evening — post-anchor rank (3) in the weekend program; it never displaces the card sitting or R-3.
return: nexsys-hivemind/context/audits/<filing-date>_R6R8_token-ops_return.md (filing-day dated, America/Chicago). The lane commits NOTHING — the hub audits, Nick commits per repo; CI on the push is the gate of record (law 16).
dispatch: "Read nexsys-hivemind/context/instructions/2026-08-21_R6-R8_token-rotation-operator-path_coding-instruction.md and execute it. - /nexsys-coder"
pre-verification: context/pre-verifications/WU-R6R8.md (P1–P10) — READ FIRST; any mismatch is a STOP-and-flag.
rulings embedded (H10 — Nick's one word each; unre-worded rows stand as the RECOMMENDED default at dispatch): R-A the `/internal/tokens` endpoints IN (recommended) / OUT · R-B PI-TZ TZ-HOLD (recommended, the s31/nightly fence) / TZ-NOW (with the cron compensation, ⏺'d before and after).
-->

# Coding Task: R-6/R-8 TOKEN-OPS — the token-rotation operator path

**Subsystem:** REST API (`api.rest`) + lifecycle composition root + app entry point + distribution (helper + docs). **Design Docs:** Doc 09 (REST API; RFC 9457 problem model; the A2 opaque-token ruling 2026-06-19) · Doc 12 (lifecycle/boot contract) · Doc 15 (secrets/at-rest posture, INV-SE-03) — all Locked. **Phase:** 3-Implementation. **Task brief reference:** F-S5 (sitting record §6) routed to R-6 (the verb) + R-8 (the procedure doc + PI-TZ), v54 beat 6; the weekend program rank (3), v55 prompt §2.

## What this implements (the engineering why)

`OpaqueTokenStore` (rest-api) holds SHA-256 hashes of 256-bit bearer tokens in `config/api_tokens` and mints ONE full-access pairing token on an EMPTY store, delivering it once through `config/initial_api_token` (`ensureInitialToken()`, :206–:221). It already has `mint()` (:179) and `revoke(keyId)` (:230) — but nothing outside the JVM can call them, and the store file has ONE lawful writer (the running service; `persist()` rewrites the whole file under the store's `ReentrantLock`). Therefore a second-process "rotate" that edits `api_tokens` offline is a lost-update race by construction, and the only operator path today is the blunt store reset (move the file aside → restart → a fresh mint) which also throws away the revocation history. **The mechanism this WU adds:** the OPERATOR REQUEST FILE — `config/token_ops.request`, written by root (the helper) and consumed by the service at startup, immediately after `ensureInitialToken()`, under the same lock, deleted BEFORE execution so a crash can never replay it. The store stays the single writer; the operator needs no token to rotate (the F-S1 case — the compromised credential is the one you cannot present); the history stays (revoked rows persist with `revoked=1`). On top of it: the helper verbs, a read-only `token status` runtime mode, and — for token-holders and the future pairing wizard — the `/internal/tokens` endpoints (mint/list/revoke) under the existing catch-all auth filter.

## Files to read before starting

| File | Why |
|---|---|
| `context/pre-verifications/WU-R6R8.md` | THE GATE — P1–P10 verified at your checkout before any edit |
| `api/rest-api/MODULE_CONTEXT.md` | type inventory, the envelope/problem contracts, gotchas; the token-store rows |
| `api/rest-api/src/main/java/module-info.java` | verbatim below — `exports com.homesynapse.api.rest`; Jackson plain; no new edge is needed |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/OpaqueTokenStore.java` | WHOLE (379 lines) — the file format (8 tab-separated fields, Base64 display name/scopes/site, `revoked` 0/1), `persist()` :306–:325 (non-atomic `Files.writeString`), `writeArtifact()` :327–:335, `load()`/`parseLine()` :262–:303, the lock discipline |
| `api/rest-api/src/test/java/com/homesynapse/api/rest/OpaqueTokenStoreTest.java` | the 7 existing tests (fixed clock `2026-06-19T00:00:00Z`, `@TempDir`) — extend in the same idiom |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/RestFilters.java` | `installAuth` (:433 — the catch-all `app.before(ctx -> authorize(…))` at :441 with the single static-shell exemption; identity stored at `ctx.attribute(IDENTITY_ATTRIBUTE)` :464, `IDENTITY_ATTRIBUTE = "hs.api.identity"` :388) · `installAdminEndpoints` (:198–:219 — the `/internal/dlq`, `/internal/projection` registration shape) · `problem(ProblemType, String)` :534 + the RFC 9457 serializer :540–:552 |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/DlqStatusEndpoint.java` + its test | the `/internal` handler idiom: `Handler`, `data`/`meta` envelope, `X-HomeSynapse-View-Position` + weak ETag headers (:160–:175); the `RecordingEndpointContext` test fake |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/ApiKeyClaims.java` + `ApiKeyIdentity.java` | `fullAccess()` :57–:59; `ApiKeyIdentity(keyId, displayName, createdAt)` :36 |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` :885–:950 | `bringUpHttpSurface()`: the store is constructed at :895, `ensureInitialToken()` :896, `installAuth` :922, readiness :926, admin :934, run-query :944 — the composition ORDER you extend |
| `lifecycle/lifecycle/src/main/java/module-info.java` | verbatim below — `requires com.homesynapse.api.rest` (plain) already present |
| `lifecycle/lifecycle/MODULE_CONTEXT.md` | the composition-root rows + gotchas |
| `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` | `main(String[] args)` :53 — args are currently unread; `resolveBaseDir()`/`configDir` :59–:60; the Clock whitelist comment :54–:56 |
| `app/homesynapse-app/src/main/java/module-info.java` | verbatim below — `requires com.homesynapse.api.rest` already present; NO exports |
| `app/homesynapse-app/MODULE_CONTEXT.md` + `app/homesynapse-app/src/test/java/com/homesynapse/app/HomeSynapseArchRules*.java` | the arch rules that run from THIS module's test classpath |
| `config/configuration/src/main/java/com/homesynapse/config/AtomicYamlWriter.java` (the `.tmp` sibling + fsync + `ATOMIC_MOVE` at :185; the Windows note at :32–:34) + `StandardScopeKeyManager.java` :469 region | the repo's temp-then-`ATOMIC_MOVE` idiom incl. its POSIX-permission guard (the build runs on Windows too — mirror the guard, never assume POSIX) |
| `distribution/deb/homesynapse-token` | the helper (23 lines; `/bin/sh`; prints the artifact) — extend, do not rewrite its existing no-arg behavior |
| `distribution/deb/build-deb.sh` :51–:52 | the helper is copied to `usr/bin/homesynapse-token`; `distribution/` is NOT present at install time — the helper stays SELF-CONTAINED (hardcoded `/var/lib/homesynapse`, like `postinst`) |
| `distribution/image/build-image.sh` :125–:143 | the launcher (heredoc) passes `"$@"` to `com.homesynapse.app.Main` — the CLI mode rides it |
| `distribution/deb/debian/postinst` | the banner text that names `sudo homesynapse-token` — keep the verbs consistent with it |
| `context/audits/2026-08-20_midweek-FE-deploy_sitting-record.md` §3 F-S1 + §6 | the incident + the mechanism facts this WU closes |

**Verbatim `module-info.java` (no JPMS change is proposed by this WU; embedded per the rule):**

`api/rest-api`: `module com.homesynapse.api.rest { requires transitive com.homesynapse.state; requires com.homesynapse.event.bus; requires com.homesynapse.automation; requires com.fasterxml.jackson.databind; requires io.javalin; requires org.slf4j; exports com.homesynapse.api.rest; }`
`lifecycle/lifecycle`: `module com.homesynapse.lifecycle { requires transitive com.homesynapse.observability; requires transitive com.homesynapse.event; requires transitive com.homesynapse.platform; requires transitive com.homesynapse.persistence; requires transitive com.homesynapse.event.bus; requires transitive com.homesynapse.state; requires transitive com.homesynapse.integration; requires com.homesynapse.integration.runtime; requires com.homesynapse.api.rest; requires com.homesynapse.config; requires transitive com.homesynapse.device; requires com.homesynapse.automation; requires com.homesynapse.platform.systemd; requires io.javalin; requires org.eclipse.jetty.util; requires org.slf4j; exports com.homesynapse.lifecycle; }`
`app/homesynapse-app`: `module com.homesynapse.app { requires com.homesynapse.lifecycle; requires com.homesynapse.observability; requires com.homesynapse.event; requires com.homesynapse.device; requires com.homesynapse.state; requires com.homesynapse.persistence; requires com.homesynapse.event.bus; requires com.homesynapse.automation; requires com.homesynapse.integration; requires com.homesynapse.integration.runtime; requires com.homesynapse.integration.zigbee; requires com.homesynapse.config; requires com.homesynapse.api.rest; requires com.homesynapse.api.ws; requires com.homesynapse.platform; }` (comment blocks elided here only; the files carry them — do not touch them).

## Files to create or modify (census-exact — see §Files table)

### A. `OpaqueTokenStore` (rest-api, M) — the mechanism + two hardenings

1. **`public record TokenSummary(String keyId, String displayName, Instant createdAt, Instant expiresAt, List<String> scopes, String siteId, boolean revoked)`** (nested, public) + **`public List<TokenSummary> summaries()`** — a snapshot sorted by `createdAt` then `keyId`; NEVER the hash, NEVER a raw token. (The `status` CLI and `GET /internal/tokens` read this.)
2. **`public String rotate(String displayName)`** — under `writeLock`: mint a new `ApiKeyClaims.SCOPE_ALL`, unscoped token with the given display name; revoke EVERY other active (non-revoked) record; write the artifact (`writeArtifact`) so delivery rides the existing path; return the raw token once. **Persist discipline:** the existing `mint()` and `revoke()` each call `persist()` internally (:190, :239) and the lock is reentrant, so delegating to them compiles and writes the file N+1 times — lawful for correctness once persist is atomic (§A.4), but PREFER inlining the bookkeeping (one map put + the revoked copies) followed by ONE `persist()`; state in the return which you shipped. Javadoc: "all-sessions rotation — the remediation for a disclosed credential; the revoked rows stay as history".
3. **`public OperatorRequestReport processOperatorRequests()`** — `public record OperatorRequestReport(int rotated, int revoked, int minted, List<String> skipped)`; under `writeLock`: if `config/token_ops.request` (constant `OPERATOR_REQUEST_FILE = "token_ops.request"`) is absent → a zero report, no log. If present: read all lines (UTF-8), **delete the file FIRST** (`Files.delete`); if the delete throws → WARN `token_ops request at {} could not be removed; no operation executed (an unremovable request would replay on every start)` and return the zero report — fail closed. Then execute each non-blank, non-`#` line: `rotate` → `rotate("operator-rotated-" + clock.instant())`; `revoke <keyId>` → `revoke(keyId)` (count only a `true` return; a `false` return is a `skipped` entry "revoke <keyId>: no active token"); `mint <displayName…>` (the rest of the line, trimmed) → `mint(displayName, List.of(ApiKeyClaims.SCOPE_ALL), null)` + `writeArtifact(raw)`; anything else → `skipped` "unknown verb". **The read-failure arm (never bricks startup — the store's own posture at :113–:114):** if the request file exists but cannot be READ (an `IOException` — e.g. a root-owned 0600 file the service user cannot open), WARN `token_ops request at {} is unreadable by the service user; no operation executed` and return the zero report WITHOUT deleting it and WITHOUT throwing; the doc and the helper's usage text tell the operator the file must be readable by the service user (the helper's `install -o homesynapse … -m 0600` makes it so). Log ONE WARN summary at the end when anything executed: `token operator request applied: rotated={} revoked={} minted={} skipped={} — a minted token, if any, is at {}` (the ARTIFACT PATH, never a token value; this path logs no secret, unlike the ruled initial-mint WARN — disclosed asymmetry, see §Watch).
4. **Hardening 1 — atomic `persist()`:** write to `api_tokens.tmp` in the same directory (fsync per the idiom), then `Files.move(tmp, tokenFile, StandardCopyOption.ATOMIC_MOVE)` — EXACTLY the `AtomicYamlWriter` :185 form (with `ATOMIC_MOVE` the JDK ignores other options; do not invent a variant); on POSIX set `rw-------` on the tmp BEFORE the move (the same file's guard idiom: `FileSystems.getDefault().supportedFileAttributeViews().contains("posix")`); a failed move leaves the previous file intact (assert it in a test). Rationale: a crash mid-rewrite today truncates the store → an EMPTY store → the next boot MINTS A NEW PAIRING TOKEN silently (every existing client logged out, a new secret delivered) — the F-23 false-confidence class applied to credentials. The javadoc at :61 already promises "rewrite the backing file atomically"; the code did not — fix the code to the comment (the comment/code unity rule).
5. **Hardening 2 — artifact mode:** `writeArtifact()` writes through the same temp-then-move idiom with `rw-------` on POSIX (the config dir is 0700 on the packaged path, so this is defense in depth, not the fence).

### B. `TokenAdminEndpoints` (rest-api, A) + `RestFilters.installTokenAdminEndpoints(Object javalinApp, OpaqueTokenStore store, Clock clock)` (M) — **RULING R-A: IN (recommended) / OUT**

Package-private `final class TokenAdminEndpoints` with three `Handler`s registered by the new installer (the `installAdminEndpoints` shape — `Object`-typed Javalin param, `Objects.requireNonNull` guards):
- `GET /internal/tokens` → 200 `{ "data": { "tokens": [ {keyId, displayName, createdAt, expiresAt|null, scopes, siteId|null, revoked} ] }, "meta": { "timestamp" } }` — hashes and raw tokens never appear (assert in the test by scanning the serialized body for any 64-hex run).
- `POST /internal/tokens` with JSON body `{ "displayName": "…", "scopes"?: ["*"], "siteId"?: "…" }` → 201 `{ "data": { "keyId", "token" }, "meta": { "timestamp" } }` — the raw token returned ONCE; `displayName` blank/missing → 400 problem (`RestFilters.problem(ProblemType.INVALID_PARAMETERS, …)` — the 400 constant at `ProblemType.java:78`); scopes default `["*"]`.
- `DELETE /internal/tokens/{keyId}` → 204 on `revoke` true; 404 problem on false. **Self-revocation is allowed** (the caller may revoke its own token; the response still completes — document it).
- **Authorization:** every handler first resolves `ctx.attribute(RestFilters.IDENTITY_ATTRIBUTE)` → `store.claimsFor(identity.keyId())` → require `fullAccess()`, else 403 problem (`ProblemType.FORBIDDEN`, :97); a 404 uses `ProblemType.NOT_FOUND` (:38). `installAuth` already gates `/internal/*` (P5) — the handler check is the second layer for the enterprise-tier scope split the `ApiKeyClaims` javadoc anticipates. Both layers are tested.
- No `meta.viewPosition`/ETag on these (they are not projection reads; say so in the javadoc — the `/internal/dlq` header idiom is for projection-bearing responses).

### C. `HomeSynapseCore.bringUpHttpSurface()` (lifecycle, M)

After `:896 tokenStore.ensureInitialToken();` add `OpaqueTokenStore.OperatorRequestReport tokenOps = tokenStore.processOperatorRequests();` (the report is logged by the store; the root keeps no reference). After `installAdminEndpoints` (:934 block) add `RestFilters.installTokenAdminEndpoints(app, tokenStore, clock);` — same ordering class (auth → readiness → admin). If R-A = OUT, only the first line lands.

### D. `Main` (app, M) + `TokenCli` (app, A) — the read-only runtime mode

In `main`, immediately AFTER `Clock clock = Clock.systemUTC();` (:57) and BEFORE `resolveBaseDir()` (:59) and the `Files.createDirectories` calls (:62–:63 — they are writes, and the CLI mode performs NO writes): `if (args.length >= 1 && "token".equals(args[0])) { System.exit(TokenCli.run(args, resolveBaseDir().resolve("config"), clock)); }` (reuse the already-sourced `clock` — the :54–:56 comment's "single sanctioned place" stays literally true; `TokenCli` itself NEVER calls `Clock.systemUTC()`/`Instant.now()` — the arch rule applies to `com.homesynapse.app` code too? NO: `com.homesynapse.app` is on the WHITELIST — but write it injected anyway so the class is testable with a fixed clock). `TokenCli.run(String[] args, Path configDir, Clock clock)`: `token status` → open `new OpaqueTokenStore(configDir, clock)` (read-only by construction — the constructor only `load()`s; P3) → print a fixed-width table of `summaries()` (`KEY_ID  NAME  CREATED  EXPIRES  SCOPES  SITE  STATE`) + a trailer `active: N  revoked: M  store: <path>`; exit 0; any other verb → print the usage block (`token status` is the only runtime verb; `rotate|revoke|mint` are the helper's — see the doc) and exit 2. No writes ever. Register C voice in every printed line.

### E. `distribution/deb/homesynapse-token` (M) — the verbs (POSIX `sh`; self-contained)

Keep the no-arg behavior byte-for-byte (print the artifact). Add: `status` → `exec sudo -u homesynapse env HOMESYNAPSE_HOME=/var/lib/homesynapse /opt/homesynapse/bin/homesynapse token status` (when already root, `sudo -u` is still correct — the file is `homesynapse`-owned 0600 inside a 0700 dir) · `rotate` | `revoke <keyId>` | `mint <name>` → require root (`id -u` = 0, else the Register C line + exit 1) → write the request with `printf '%s\n' "<verb line>" | install -o homesynapse -g homesynapse -m 0600 /dev/stdin /var/lib/homesynapse/config/token_ops.request` (append-safe: if a request file already exists, APPEND the line instead, preserving mode) → if `/run/systemd/system` exists: `systemctl restart homesynapse.service` (this BLOCKS until `ExecStartPost`'s health probe passes — the request has been consumed when it returns) → print `Request applied at restart. A minted token, if any, is at /var/lib/homesynapse/config/initial_api_token — view it with: sudo homesynapse-token` ; if no systemd: print the request path + `Restart the service to apply it (the request is consumed at the next start).` Never print a token from these verbs. `--help`/`-h`/unknown → usage, exit 2. `set -eu` stays. Every path hardcoded (no `distribution/` at install time).

### F. `distribution/docs/token-rotation.md` (A) — the R-8 procedure doc

Sections: what the pairing token is and where it lives (the store = hashes; the artifact = delivery-only; why deleting the artifact neither revokes nor re-mints — the F-S1 lesson, cited to the store's javadoc) · **the operator path on a packaged install** (`sudo homesynapse-token status|rotate|revoke <keyId>|mint <name>` + what each does + the restart it implies) · **the bench/dev recipe** (no helper: write the request line into `$HOMESYNAPSE_HOME/config/token_ops.request` as the service user, then restart through your launcher — `bench.sh restart` on the bench) · **the emergency store reset** (the sitting-record §6 block: `mv config/api_tokens config/api_tokens.rotated-<date>` → restart → a fresh mint; loses history; last resort) · **credential hygiene rules** (read tokens on the host terminal only; screenshots of request headers are token-carriers — crop/mask `Authorization`; the artifact may be deleted after pairing — the banner's advice — and `rotate` re-creates it) · **the `/internal/tokens` API** (if R-A IN: the three routes, full-access required, raw token returned once). Register C. No product claims. `distribution/README.md` is NOT touched (its :117 fence) — a one-line pointer to this doc may ride a FUTURE README edit, not this WU.

### G. MODULE_CONTEXT rows (M ×3): rest-api (the request file + `rotate`/`summaries`/`processOperatorRequests` + the atomic-persist gotcha + the endpoints), lifecycle (the composition line + order), app (the `token` CLI mode + the injected-clock note). Delta-only rows in each file's own style.

### H. Tests (red-first where a fixture can red at HEAD — #18; disclosed otherwise)

`OpaqueTokenStoreTest` (M) +8: `rotateRevokesEveryOtherActiveToken` (mint 2 → rotate → old 2 invalid, new valid, `activeKeyCount()==1`, both old rows present with `revoked`) · `rotateWritesTheArtifact` · `summariesNeverExposeHashes` (serialize the summaries via `toString()` and assert no 64-hex run; assert the raw token string is absent) · `operatorRequestRotateIsConsumedOnce` (write the request file → process → rotated==1 AND the file is gone → process again → zero report) · `operatorRequestRevokeAndMintVerbs` · `operatorRequestUnknownVerbIsSkippedNotFatal` · `operatorRequestUndeletableFileExecutesNothing` (POSIX-only AND non-root via `Assumptions.assumeTrue` — root ignores directory write bits and container CI may run as root; make the config dir read-only for the delete → zero report + the WARN) · `persistIsAtomic` (after `mint`, no `api_tokens.tmp` remains; reopen parses every row; on POSIX the mode of `api_tokens` is `rw-------`). **RED-FIRST:** `rotate…`/`operatorRequest…`/`summaries…` cannot compile at HEAD (new API) — green-by-construction, disclosed; `persistIsAtomic`'s "no tmp remains" arm is green at HEAD and its mode arm is RED at HEAD on POSIX (`api_tokens` today carries umask-default perms — the unit sets no `UMask=`, so 0644 under systemd's 0022) — run it first on Linux-class CI semantics if your host is Windows (state which you observed).
`TokenAdminEndpointsTest` (A, if R-A IN) +6 with `RecordingEndpointContext`: list body shape + no hashes · mint 201 + token once + 400 on blank name · revoke 204/404 · 403 when the identity's claims are not full-access · 401-class absence of identity attribute → 403 problem (the handler must not NPE when the attribute is missing — the filter always sets it, but the handler is fenced anyway).
`TokenCliTest` (A, app): `status` prints the table from a temp store with a fixed clock; unknown verb exits 2; NEVER calls the real clock (the arch rule + the injected clock).

## Technical specification — contracts

- **The request file is consumed exactly once, before execution, under the store lock; an unremovable request executes nothing.** (Invariant; tested.)
- **`rotate` leaves exactly one active token** (the new one) and never deletes a record. (Invariant; tested.)
- **No method of this store ever logs or returns a hash; raw tokens are returned once by `mint`/`rotate` and written once to the artifact.** The ruled initial-mint WARN at :214–:216 (R-δ AX-9) is UNCHANGED by this WU — disclosed asymmetry; the rotation path logs the PATH only (charter-visible for R-10: credential-in-logs posture).
- **`persist()` is atomic** (temp + `ATOMIC_MOVE`); the previous store survives any failed write.
- **Thread safety** unchanged: mutations serialize on the `ReentrantLock` (LTD-11 — never `synchronized`); `summaries()` reads the `ConcurrentHashMap` snapshot.
- **Error handling (Register C):** problems via `RestFilters.problem(...)`; the CLI prints one line per failure and exits non-zero; the helper never masks a failed `install`/`systemctl` (no `|| true`).

## Locked decisions + invariants that apply

- **INV-SE-02** (auth mandatory on every external interface — the new routes inherit `installAuth` AND add the full-access check) · **INV-SE-03** (secrets never logged/persisted raw — the summaries/problem bodies carry none; the artifact is the ONE sanctioned delivery) · **LTD-11** (`ReentrantLock`, never `synchronized`) · **LTD-08** (JSON boundary = rest-api; the CLI prints text, not JSON) · **LTD-15** (SLF4J only inside modules) · the A2 opaque-token ruling (hashes, one-time delivery) · **the arch-rule reminder (§4c):** `TokenCli` lives in `com.homesynapse.app` (whitelisted) but takes an injected `Clock` by design; rest-api/lifecycle production code must not call `Clock.systemUTC()`/`Instant.now()` — the store's `clock` field is the only time source (`NO_DIRECT_TIME_ACCESS` runs from the app test classpath and catches production code in non-whitelisted modules; NON-app TEST code is NOT scanned — your review is its only enforcement: use the fixed clock in every new test).

## Verification (the lane's own gates, then CI)

`./gradlew :api:rest-api:compileJava :api:rest-api:compileTestJava :api:rest-api:test` (count pins: the module has 21 test FILES at HEAD; +1 file if R-A IN; state the test-METHOD count before/after) → `:lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test` → `:app:homesynapse-app:compileJava :app:homesynapse-app:test` (the arch rules run here) → full `./gradlew check` (spotless + ArchUnit + moduleGraphAssert; `-Werror` rides the convention plugin — never pass it as a CLI flag). `sh -n distribution/deb/homesynapse-token` + `shellcheck` if present (flag if absent). **No hardware.** CI on the push = the gate of record (Build & Check + install-smoke; the smoke's check 5 must stay green — it asserts the artifact EXISTS and is non-empty, is OWNED by `homesynapse`, and that the CONFIG DIR mode ends in 0/00; it does NOT assert the artifact's own mode, so the `rw-------` hardening is proven by your test, not by the smoke).

## Files table (census-exact; the commit stages EXACTLY these — R-A IN: 14 rows; R-A OUT: 11, drop the three rows marked †)

| File | Kind |
|---|---|
| `api/rest-api/src/main/java/com/homesynapse/api/rest/OpaqueTokenStore.java` | M |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/RestFilters.java` | M † |
| `api/rest-api/src/main/java/com/homesynapse/api/rest/TokenAdminEndpoints.java` | A † |
| `api/rest-api/src/test/java/com/homesynapse/api/rest/OpaqueTokenStoreTest.java` | M |
| `api/rest-api/src/test/java/com/homesynapse/api/rest/TokenAdminEndpointsTest.java` | A † |
| `api/rest-api/MODULE_CONTEXT.md` | M |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | M |
| `lifecycle/lifecycle/MODULE_CONTEXT.md` | M |
| `app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java` | M |
| `app/homesynapse-app/src/main/java/com/homesynapse/app/TokenCli.java` | A |
| `app/homesynapse-app/src/test/java/com/homesynapse/app/TokenCliTest.java` | A |
| `app/homesynapse-app/MODULE_CONTEXT.md` | M |
| `distribution/deb/homesynapse-token` | M |
| `distribution/docs/token-rotation.md` | A |

**Stages exactly 14 (R-A IN) / 11 (R-A OUT).** Anything else dirty at your porcelain = STOP. Zero `build.gradle.kts` edits (no new dependency; no new module edge — the instruction's own P-rows prove every `requires` already exists). `distribution/README.md` untouched. `nexsys-bench` untouched by the lane (PI-TZ is an operator act — §OP-B).

## What to watch out for

The comment/code divergence class: the javadoc's "atomically" at :61 is made TRUE by this WU — do not leave a second comment claiming it elsewhere · `Files.move` with `ATOMIC_MOVE` across the same directory only (never across filesystems) · the Windows build: every POSIX permission call guarded; tests that need POSIX use `Assumptions` · `ConcurrentHashMap.entrySet().setValue` is the existing `revoke` idiom — `rotate` must iterate and revoke the same way, under ONE lock scope, with ONE `persist()` · the request file must be READABLE by the service user (owned by it, or mode ≥ 0640 — the helper's `install -o homesynapse -g homesynapse -m 0600` satisfies it; on the bench the ssh user IS the service user, so a bare `printf >` is lawful there) or the read-failure arm fires and nothing rotates; DELETION needs write+exec on `config/` (0700, `homesynapse`-owned), which the service user has — document both in the doc and in the helper's usage text · `systemctl restart` blocks on `ExecStartPost`; if the probe fails the helper's exit code surfaces it (never swallow) · `sudo -u homesynapse` for `status` needs the runtime's `java` to be executable by `homesynapse` (it is — the image is 0755 world-readable, P9) · the launcher applies `-Xms512m -Xmx1536m`; a CLI JVM reserving that is acceptable on the Pi (Doc 12 sizing) — do NOT add a second launcher · the `postinst` banner already says "View it with: sudo homesynapse-token" — keep the no-arg verb's output identical · Register C everywhere (no "please", no "successfully!") · delta-only: do not reformat `OpaqueTokenStore` beyond the touched methods (spotless will hold the line) · **§4c:** fixed clocks in every new test; `TokenCli` takes the clock injected.

## §OP-A — after landing: the bench rotation through the NEW path (Nick; replaces the §6 store-reset if the sitting's rotation has not yet run — otherwise a second, harmless rotation that proves the path)

```
# WHERE: the bench card (`ssh pi`), after the WU's commit is pulled + installDist'd (bench.sh deploy idiom). ⏺ every line.
printf 'rotate\n' > /home/homesynapse/hs-bench/config/token_ops.request && ls -la /home/homesynapse/hs-bench/config/token_ops.request
~/bench.sh restart
ls -la /home/homesynapse/hs-bench/config/
# expect: token_ops.request GONE; api_tokens + initial_api_token with fresh mtimes; the app log carries ONE "token operator request applied: rotated=1 revoked=N …" WARN
grep -c "token operator request applied" <the bench app log path you use for boot glances>
cat /home/homesynapse/hs-bench/config/initial_api_token
# READ ON THE PI TERMINAL ONLY; re-pair the browser; ⏺ only "re-paired OK"
~/bench.sh scenario boot-health
```

## §OP-B — PI-TZ (Nick; **RULING R-B: TZ-HOLD (recommended) / TZ-NOW**)

The Pi displays +1 h vs CT (ET); Z-stamped bundles govern; the nightly fires ~08:32Z = ~03:32 CT. **A timezone change moves any LOCAL-time schedule by one hour** — if the nightly rides a local-time `crontab`, the instrument's firing time shifts, which is a nightly change and the s31/nightly fence stands until R-5. Recommendation: **TZ-HOLD** — this block runs the day R-5 lands, unchanged. If TZ-NOW is the word, the compensation is mandatory and ⏺'d before/after:

```
# WHERE: the bench card. Read first, change second, verify third.
timedatectl | head -5; crontab -l; systemctl list-timers --all --no-pager | head -8
# ⏺ all three: the CURRENT zone + the nightly's schedule line + any timer
sudo timedatectl set-timezone America/Chicago && timedatectl | head -3
# expect: Time zone: America/Chicago (CDT, -0500)
crontab -l
# if the nightly line carries a LOCAL hour, edit ONLY that hour so the UTC instant is unchanged (ET 04:32 → CT 03:32); ⏺ the edited line; if it is a systemd timer with OnCalendar in UTC, nothing changes — ⏺ that fact
date -u; date
```

IaC row (a SEPARATE bench-repo census, Nick-committed on the same word): `nexsys-bench/iac/bootstrap.sh` gains `sudo timedatectl set-timezone America/Chicago` beside its other host-provisioning lines — authored by the hub at the TZ word, not by this lane.

## Return shape

§0 P1–P10 re-verification · §1 per-file diffs (hunk summary) · §2 the invariants as shipped (the request-file consumption order; the atomic move; the log lines verbatim) · §3 gates (targeted + full `check` task counts; test-method counts before/after per module; `sh -n`/shellcheck) · §4 census at porcelain (lock-free, flag spelled) · §5 deviations/pushback (evidence over instruction) · §6 the R-A/R-B words as received · §7 next-WU pointer (R-6's remaining riders: health/status endpoint · `SuccessExitStatus=143` · real `Depends` — their own WU). Welcome technical pushback — if the bytes contradict this instruction anywhere, your flag is the deliverable.
