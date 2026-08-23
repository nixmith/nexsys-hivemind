<!--
file: context/audits/2026-08-22_R9_E3-HEALTH_return.md
purpose: Coder return for WU R-9 / E3-HEALTH — the unauthenticated loopback `/health` (R-H1 LOOPBACK-ONLY) + rider R-H2 (the last-full-access-token guard) + riders R-9-a (SUSPENDED in the 503 matrix) and R-9-b (the unit's M13 flip block → a DANGER note). Filed 2026-08-22 (America/Chicago) against core HEAD 89a912e (the instruction's baseline "62dbca3 + the R-7 commit" — R-7 IS 89a912e; tree clean at launch).
audience: the hub (audit), Nick (commit + the CI read + §OP-H on the bench), the next lane.
instruction: context/instructions/2026-08-22_R9_E3-HEALTH_unauthenticated-loopback-health_coding-instruction.md · pre-verification: context/pre-verifications/WU-R9.md (P1–P15)
status: DELIVERED — the lane commits NOTHING; the hub audits, Nick commits; CI on the push (Build & Check + install-smoke BOTH legs) is the gate of record (law 16); the WU CLOSES at §OP-H.
-->

# R-9 / E3-HEALTH — return (2026-08-22)

**One line:** `GET`/`HEAD /health` lands (200 ⇔ the state projection is LIVE, 503 + the gate's own two headers otherwise, body exactly `{"status":"<mode>"}`), exempted from the catch-all auth filter for LOOPBACK literals only (R-H1) — the exemption lives inside `authorize()` as a second independently-reversible early-return, never a route bypass; the whole distribution flips to `--health-path /health` (the unit + five script probes), `run-smoke.sh` gains check 3b (the unit's instrument re-run in the smoke → 19 PASS lines), the helper stops touching the pairing artifact, the doc caveat retires to a History note, E3 → CLOSED; R-H2 makes `revoke()` return `RevokeOutcome` and REFUSE the last active full-access token (409 at HTTP, a `skipped` entry at the request file). Red-first captured at 89a912e (the lifecycle e2e: `expected: 200 but was: 401`); targeted + Spotless + full `./gradlew check` GREEN on this desk; **24 at porcelain = the 23 ruled rows + `StandardAuthMiddlewareTest.java`** (a `revoke()` caller the P2 survey missed — §4/§5). Nothing committed.

## §0 — P1–P15 re-verification at the checkout (89a912e; R-7 landed, tree clean)

| # | Verified at 89a912e | Outcome |
|---|---|---|
| P1 | `health-probe.sh`: `HEALTH_PATH="/api/v1/entities"` :24 · `--health-path` :37 · `NEEDS_AUTH` case :49–:53 · `load_token` :85–:93 (returns 0 at :86 when `NEEDS_AUTH`=0) · no `Authorization` header when `_auth` empty :68–:70 · `probe_once` :95–:108 (200→0, 503→1, 401/403→3, 000→1) · `--wait` loop :114–:124 (rc 3 exits 3 at :119) · header :8–:15 as quoted | ✓ — only :8–:15 touched (8 lines → 8 lines; :16–EOF byte-identical to HEAD, diff-proven) |
| P2 | unit: `StartLimitIntervalSec=300` :19 · `StartLimitBurst=5` :20 · `Type=exec` :23 · `ExecStartPost=… --wait --timeout 90` :50 (no `--health-path`) · comment :46–:49 · `TimeoutStartSec=120` :55 · `Restart=on-failure` :61 · `PrivateDevices=yes` :93 + :88–:92 · the M13 block :100–:106 | ✓ — the ONLY directive delta is `ExecStartPost` (non-comment diff vs HEAD = that one line); `PrivateDevices` block untouched; :100–:106 → the DANGER block (R-9-b) |
| P3 | `RestFilters`: `IDENTITY_ATTRIBUTE` :431 · `installAuth` :476–:485 (`app.exception` :483, `app.before` :484) · `authorize` :487–:508 (`isPathSafe` :490, ORDER comment :494–:496, the single early-return :497–:499, `authenticate` :500, rate-limit :501–:506, attribute :507) · `isPublicShellRequest` :528–:536 · `isPathSafe` :548–:565 · `problem` :577–:581 · `writeProblem` :584–:595 · "EXACTLY ONE exemption" :438–:441 · `installReadinessGate` :91–:97 · `installTokenAdminEndpoints` :252–:263 · Javalin pinned 6.7.0 (`libs.versions.toml:19`) | ✓. **(a) `Context.ip()`:** `javap -p io.javalin.http.Context` → `public default java.lang.String ip()`; its body reads `ContextResolverConfig.ip` (a `Function1<Context,String>`), whose DEFAULT (`ContextResolverConfig$ip$1.invoke`) is `Context.req()` → `HttpServletRequest.getRemoteAddr()`; the composition root never overrides `cfg.contextResolver`, so `ctx.ip()` IS `getRemoteAddr()`. Jetty 11.0.25 `Request.getRemoteAddr()` = `InetSocketAddress.getAddress().getHostAddress()` → `formatAddrOrHost` (`HostPort.normalizeHost` brackets a colon-bearing host) — an IPv6 peer may arrive as `[0:0:0:0:0:0:0:1]`; the classifier strips the brackets. **(b) HEAD on a GET route:** `DefaultTasks` (javap -c): the HTTP task dispatches only when `findHttpHandlerEntries(ctx.method(), uri)` has an entry; its fallback (`HTTP$lambda$11$lambda$10`) runs `method()==HEAD && router.hasHttpHandlerEntry(GET, uri)` → `areturn` — **a bare 200 with the GET handler NEVER run**. So Javalin DOES answer HEAD-for-GET automatically, but dishonestly for a conditional-status route: `HEAD /health` would read 200 during REPLAY. `app.head("/health", h)` is registered explicitly (`JavalinDefaultRoutingApi.head(String, Handler)` confirmed). §5 item 1. |
| P4 | `ReadinessFilter`: `RETRY_AFTER_SECONDS = "5"` :72 · `PROJECTION_STATE_HEADER` :75 (both package-private) · `apply` :113–:124 · `ReadinessSource` = `com.homesynapse.state.ReadinessSource` :8 · `SubscriberMode` = `com.homesynapse.event.bus.SubscriberMode`: `COLD` :16 · `REPLAY` :19 · `TRANSITION` :22 · `LIVE` :25 · **`SUSPENDED` :28** — exactly five | ✓ — rider R-9-a executed: the 503 matrix names all FOUR non-LIVE constants, and `HealthEndpointTest.subscriberModeSetIsPinned` pins the set so a sixth constant fails there first |
| P5 | `HomeSynapseCore implements SystemLifecycleManager, ReadinessSource` :178 · `bringUpHttpSurface()` :888–:988: `new OpaqueTokenStore` :895 · `ensureInitialToken` :896 · `processOperatorRequests` :903 · `Javalin.create` :911–:925 · `installAuth` :929 · `app.get("/", …)` :932 · `installReadinessGate` :933 · `installEntityQueryEndpoints` :934 · `installAdminEndpoints` :941 · `installTokenAdminEndpoints` :950 · `installRunQueryEndpoints` :958 · `installAutomationQueryEndpoints` :964 · `installCommandEndpoints` :974 · `app.start` :980 | ✓ — the one line lands between :932 and :933 (+5 comment lines); nothing else moves (`git diff --numstat` 6/0) |
| P6 | `OpaqueTokenStore`: `TokenRecord` :147–:154 · `rotate` :370–:401 (revokes via `revokedCopy` :379–:384, never `revoke()`) · `revoke` :416–:438 · the request `revoke` arm :510–:520 · `activeKeyCount` :578–:584 · `ApiKeyClaims.SCOPE_ALL` :42, `fullAccess()` :58–:60 | ✓ — callers of `revoke(`: `TokenAdminEndpoints:275` · `OpaqueTokenStore:513` · `OpaqueTokenStoreTest` ×5 · `TokenAdminEndpointsTest` (via the endpoint) · **`StandardAuthMiddlewareTest:84`** · **`TokenCliTest:71`** (`git grep -n "\.revoke("`). The last two are not in the instruction's survey: `TokenCliTest` revokes a SCOPED token (unaffected by R-H2; untouched); `StandardAuthMiddlewareTest` revokes its ONLY full-access token → refused under R-H2 → the test would fail → census +1 (§4) |
| P7 | `TokenAdminEndpoints`: the `DELETE` bullet :39–:43 · `revokeHandler()` :132–:134 · `revoke(…)` :264–:282 (validation :270, `if (!store.revoke(keyId))` :275 → `NOT_FOUND` :276, `audit` :280, `ctx.status(204)` :281) · the 403 layer :302/:308 | ✓ — :275 is now a three-arm `switch`; the audit line stays in the REVOKED arm only |
| P8 | `ProblemType`: the 13 constants at the cited lines (`DEVICE_ORPHANED` :158 last, `;`). Survey at execution: `git grep -n "ProblemType.values\|ProblemType.class\|hasSize(1[0-9])" -- '*Test.java'` → 28 `hasSize(1x)` hits, NONE on `ProblemType` (record-component / permits / byte-length pins of other types); zero `ProblemType.values`/`.class` | ✓ — `TOKEN_REVOKE_REFUSED` after `IDEMPOTENCY_KEY_CONFLICT`, 14 constants; NO count pin found → no +1 from this survey |
| P9 | `run-smoke.sh`: `set -uo pipefail` :15 · `ok`/`bad` :27–:28 · check 3 :72–:77 (:73 the authed probe) · check 4 :79–:125 · 5 :127–:137 · 6 :139–:147 · 7–9 :149–:186 · verdict :188–:194 · `grep -c '\bok "'` = 20 | ✓ — check 3b inserted after :77 (now :79–:90); `ok` sites 20 → 21; systemd-path PASS lines 18 → **19** |
| P10 | `install.sh:89` (the hub cited :92 — the file's line is :89; same statement) · `update.sh:60` + `:77` · `update-smoke.sh:44` + `:65` — all `--wait --timeout 90 --token-file "${HS_TOKEN_FILE}"` · `common.sh:40–:44` · `git grep HS_HEALTH_PATH` → only `common.sh:43–:44` (+ a mention in `escalations.md:41`) · `common.sh:57–:68` = R-7's arm | ✓ — the five sites flipped; `--token-file` now appears in `distribution/` ONLY at `run-smoke.sh:73` (check 3, by design) and the probe's own usage/parse lines; the R-7 hunk untouched (the `common.sh` diff is exactly one hunk, `@@ -40,5 +40,6 @@`) |
| P11 | helper: usage :33 · :40 · CAUTION :46–:49 · no-arg :71 · `queue_request` ends :105 · `apply_request()` :108 · `[ -d /run/systemd/system ]` :109 · `if [ "$1" = rotate ]` :110 · comment :111–:119 · `rm -f` :120 · `fi` :121 · `systemctl restart` :124 · the consumption assert :128–:132 | ✓ — :110–:121 removed whole; no `rm -f` remains; the no-arg output is BYTE-IDENTICAL to HEAD under dash, artifact present AND absent (`cmp`); :71 unchanged |
| P12 | `token-rotation.md`: `## The operator path…` :33 · `### The readiness-probe caveat` :71–:103 · `## The bench / dev recipe` :104 · `## Credential hygiene` :147, the cross-reference :156 · `## The /internal/tokens API` :164 · `escalations.md` §E3 :33–:43 | ✓ — :71–:103 → the History note; :156 reworded; the `revoke` row + the `DELETE` API row carry R-H2 (§5 item 5); E3 → CLOSED line + the return pointer |
| P13 | `HomeSynapseCoreTest`: `Clock.systemUTC()` by design :61–:63 · the auth-posture test :191–:226 · the loopback-only bind test :228–:252 (`firstNonLoopbackSiteLocal()` :242, `assumeTrue`) · `get` :255 / `send` :264–:276 · the DASH-SERVE trio :296–:361 (`%2e%2e` exact-400 :360) · `mode returns LIVE` :376. **`HomeSynapseConfig`** is a 5-component public record whose `bindHost` is a plain non-blank `String` (the documented LAN opt-in, :40–:49, :63–:66) — a site-local bind is constructible in a test with NO production code | ✓ — the OPTIONAL R-H1 e2e arm IS built (`healthStaysGuardedOffLoopback`); it RAN on this desk (not skipped) |
| P14 | `RestFiltersAuthTest`: `isPathSafe_acceptsNormalPaths` :30 · `…rejectsTraversalAndControl` :39 · `isPublicShellRequest_exactAllowlist` :52 · `…rejectsEverythingElse` :64 · `shellExemption_neverPrecedesTraversalGate` :82 · `problem_…` :95 · `RecordingEndpointContext` present (headers as a `LinkedHashMap`) | ✓ — the three shell tests byte-identical; six new tests beside them |
| P15 | Baselines by test-results XML (the CI count): rest-api **130**, app **24**, lifecycle **60** (the earlier `grep -c @Test` of 125 under-counts; the XML is the instrument). `git grep -n "api.rest" HomeSynapseArchRules.java` → :268 (`QUERY_SERVICE_READ_ONLY` — no persistence access) and :308–:312 (`REST_ENDPOINTS_NO_EVENT_PUBLISHING`, exempting `IssueCommandEndpoint`/`RestFilters`); no rule names `/health`, `ReadinessSource`, `java.net`, or the rest-api→lifecycle direction. `build.gradle.kts`: `api(project(":core:state-store"))`, `implementation(project(":core:event-bus"))`; module-info verbatim as embedded | ✓ — ZERO module-info / build-file edits; the app's ArchUnit suite re-ran fresh in the full check (11/11) |

**Standing facts carried:** H-1/H-2 close with this WU (the interim operator law — never revoke the artifact's key, never delete the artifact — RETIRES the beat CI banks green AND §OP-H passes); the packaged-unit artifact-absent restart proof rides R-3b's held-card packet (not a bench act).

## §1 — per-file hunk summary (24 files: 22 M + 2 A)

| File | Kind | Hunks |
|---|---|---|
| `api/rest-api/src/main/java/com/homesynapse/api/rest/HealthEndpoint.java` | A (109) | package-private `final class HealthEndpoint implements Handler`; `PATH = "/health"`; ctor `(ReadinessSource)` + `requireNonNull`; `handle(Context)` → `apply(new JavalinEndpointContext(ctx))`; `apply(EndpointContext)`: LIVE → `status(200)`; else DEBUG + `status(503)` + `header(PROJECTION_STATE_HEADER, mode.name())` + `header("Retry-After", RETRY_AFTER_SECONDS)`; both arms `header("Cache-Control","no-store")` then `json(Map.of("status", mode.name()))`. Class Javadoc: the body law (no envelope — a probe body is not a data route), the auth posture, LTD-15. |
| `…/RestFilters.java` | M (+193/−15) | imports `java.net.InetAddress`/`UnknownHostException`; class Javadoc `@link`/`@see HealthEndpoint`; **`installHealthEndpoint(Object, ReadinessSource)`** after `installReadinessGate` (`app.get` + `app.head`, one handler); `installAuth` Javadoc: "EXACTLY ONE exemption" → the TWO exemptions, each with its invariant, "two early-returns, each independently reversible"; `authorize`: the second `if (isHealthProbeRequest(ctx.method().name(), ctx.path(), ctx.ip())) return;` after the shell return — ORDER UNCHANGED (`isPathSafe` first); **`isHealthProbeRequest(String,String,String)`** + **`isLoopbackLiteral(String)`** + private `isLoopbackDottedQuad`/`isAsciiHexDigit` after `isPublicShellRequest` (whose Javadoc is untouched). |
| `…/OpaqueTokenStore.java` | M (+103/−24) | class Javadoc: the R-H2 paragraph; `OperatorRequestReport.skipped` Javadoc (+ the refused case); **`public enum RevokeOutcome { REVOKED, NOT_FOUND, REFUSED_LAST_FULL_ACCESS }`**; `revoke(String)` → `RevokeOutcome`: under the lock, the matching active row → `isLastActiveFullAccess(r)` ? WARN (key id only) + `REFUSED_LAST_FULL_ACCESS` (nothing persisted) : revoke as before + `REVOKED`; no row → `NOT_FOUND`; the stranded-artifact WARN text drops "or the packaged readiness probe"; private `isLastActiveFullAccess`/`isActiveFullAccess` (the `activeKeyCount` predicate narrowed to `*` rows; reference identity for "other rows"); `processOperatorRequests` Javadoc item 4 + the `revoke` arm → a `switch`: `REVOKED → revoked++` · `REFUSED_LAST_FULL_ACCESS → skipped "line N: revoke <keyId>: refused — the last active full-access token (use rotate)"` · `NOT_FOUND` → the two existing sub-arms. |
| `…/ProblemType.java` | M (+13) | `TOKEN_REVOKE_REFUSED("token-revoke-refused", 409, "Token Revoke Refused")` after `IDEMPOTENCY_KEY_CONFLICT`, Javadoc in the file's voice. |
| `…/TokenAdminEndpoints.java` | M (+20/−11) | the class Javadoc `DELETE` bullet gains the 409 arm ("self-revocation is allowed while another full-access token is active"); `revoke(...)`: `switch (store.revoke(keyId))` — `REVOKED` → audit + 204 · `NOT_FOUND` → 404 · `REFUSED_LAST_FULL_ACCESS` → `problem(ctx, TOKEN_REVOKE_REFUSED, "Token <keyId> is the last active full-access token; rotate instead of revoking")`, no audit. |
| `api/rest-api/src/test/java/com/homesynapse/api/rest/HealthEndpointTest.java` | A (5 tests) | the `SubscriberMode` set pin · LIVE 200 + exactly `{"status":"LIVE"}` (Jackson-serialized string pinned) + no-store + no readiness headers · the four-mode 503 matrix (COLD/REPLAY/TRANSITION/SUSPENDED: header = mode, `Retry-After: 5`, no-store, one-key body) · per-call read (REPLAY→LIVE→SUSPENDED on one handler) · null ctor. |
| `…/RestFiltersAuthTest.java` | M (6 → 12) | class Javadoc; three literal tables (15 loopback spellings incl. bracketed/zoned/mapped; 13 non-loopback literals; 24 non-literals incl. hostnames, hex-only words, `127.0.0.1:8080`, `2130706433`, `127.1`, leading zeros, 5-part, empty/blank/zone-only, half-brackets, `::g1`, a trailing newline); `isHealthProbeRequest_exactPathFromLoopback` · `…rejectsOtherPathsMethodsAndNulls` (11 paths, 6 methods, 3 nulls, lowercase `get`) · `…rejectsNonLoopbackSources` · `isLoopbackLiteral_acceptsEveryLoopbackSpelling` · `…rejectsNonLoopbackAndNonLiterals` · `healthExemption_neverPrecedesTraversalGate` (5 traversal spellings: `isPathSafe` false AND the classifier false). The three shell tests byte-identical. |
| `…/OpaqueTokenStoreTest.java` | M (21 → 26) | imports `Base64`/`StandardCharsets` + `b64()`; class Javadoc (R-H2 paragraph); `revokedTokenRejected` (+ keeper; `REVOKED`/`NOT_FOUND` ×2) · `operatorRequestRevokeAndMintVerbs` (fixture reordered `mint` then `revoke` — the doc's one-liner order; expectations unchanged) · `persistIsAtomic` (+ token c; `REVOKED` asserted; 3 rows) · `revokingTheArtifactTokenIsFlagged` (+ keeper; `REVOKED` asserted); NEW: `revokeRefusesTheLastActiveFullAccessToken` (store bytes identical before/after; a scoped sibling does not change the verdict) · `scopedTokenRevokesEvenWhenLast` · `expiredFullAccessRowDoesNotRescueTheLastLiveOne` (an expired `*` row written in the documented 8-field format; the live one still refused; the expired row revokes freely) · `rotateIsNeverRefusedOnASingleTokenStore` · `operatorRequestRevokeOfTheLastFullAccessKeyIsSkipped` (the exact `skipped` text; `revoked=0`; file consumed). |
| `…/TokenAdminEndpointsTest.java` | M (9 → 10) | `selfRevocationCompletes` (+ keeper minted first; DisplayName says "while another full-access token is active"); NEW `revokeOfTheLastFullAccessKeyIs409` (409 · `application/problem+json` · `type` ends `/token-revoke-refused` · `title` · `detail` names the key + "rotate" · no-store · the token still validates · row not revoked · audit empty). |
| `…/StandardAuthMiddlewareTest.java` | M (4 → 4; **the +1 census row**) | `revokedTokenIs403`: mints a second full-access "keeper" and ASSERTS `revoke(...) == REVOKED` before asserting 403 — without it the R-H2 guard refuses the single-token fixture and the test fails (red at HEAD+R-H2, green now). |
| `api/rest-api/MODULE_CONTEXT.md` | M | the `ProblemType` inventory cell (13 → 14); **§E3-HEALTH** after §R-6/R-8 (8 rows: `HealthEndpoint` · `installHealthEndpoint` · `isHealthProbeRequest` · `isLoopbackLiteral` · the `authorize` order law with TWO exemptions + the stated residue incl. the tunnel disclosure · `RevokeOutcome` · the `revoke` guard · `TOKEN_REVOKE_REFUSED`; two gotchas: the HEAD-for-GET trap is general; `ctx.ip()` is the socket peer, never a proxy header; the test counts 130 → 147); the R-6/R-8 `mint()/rotate()` gotcha's probe sentence marked RETIRED-as-history. |
| `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | M (+6) | `RestFilters.installHealthEndpoint(app, this);` between `app.get("/", …)` and `installReadinessGate`, with a five-line comment in the file's voice. |
| `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreTest.java` | M (+92/−1; 15 → 17 tests) | `send` → `sendTo(host, port, …)` (IPv6 bracketed for the URI); NEW `healthServesHeaderlessOnLoopbackWhileDataRoutesStayGuarded` (200 + exactly `{"status":"LIVE"}` + `Cache-Control: no-store` + no projection-state header · HEAD 200 with an empty body · authed 200 · POST/`/health/`/`/healthz`/`/api/v1/entities`/`/internal/dlq` 401 · `GET /dashboard/%2e%2e/health` EXACTLY 400) and `healthStaysGuardedOffLoopback` (site-local `bindHost` via the 5-arg `HomeSynapseConfig`; headerless GET/HEAD 401, authed 200, `/api/*` 401; `assumeTrue`-gated). Both under `Clock.fixed` (the DASH-SERVE idiom). |
| `lifecycle/lifecycle/MODULE_CONTEXT.md` | M | one blockquote at the top in the R-6/R-8 form (the line, its position, the invariants, the packaged consequence, the two tests). |
| `distribution/systemd/homesynapse.service` | M (+31/−15) | header :8–:13 reworded (the "two-line edit" claim removed — the same false claim R-9-b kills at the bottom; §5 item 4); the probe comment :46–:49 rewritten; **`ExecStartPost=… --wait --timeout 90 --health-path /health`**; :100–:106 → the DANGER block (R-9-b): the exact bricking mechanism (`Type=notify` → `$NOTIFY_SOCKET` → `SystemdHealthReporter` throws → `NoOpHealthReporter` → no `READY=1` → `TimeoutStartSec=120` → `StartLimitBurst=5/300 s` → start-limited DOWN; `WatchdogSec=60` SIGABRT), the precondition (a working transport in platform-systemd, OR-M13-SDNOTIFY), the source pointer (R10-IN-L return §3 f1), the eventual shape kept commented (`Type=notify` / `NotifyAccess=main` / `WatchdogSec=60` / `Restart=on-watchdog`), the `boot-contract-map.md` pointer. `PrivateDevices` :88–:93 untouched. |
| `distribution/common.sh` | M (+6/−5; ONE hunk `@@ -40,5 +40,6 @@`) | the :40–:44 comment rewritten; `HS_HEALTH_PATH="${HS_HEALTH_PATH:-/health}"`. The R-7 version arm :57–:68 (now :58–:69) untouched. |
| `distribution/smoke/health-probe.sh` | M (+7/−7; comment only) | :8–:15 rewritten as 8 lines (the readiness model names `/health` as the unit's path and the authed default as the smoke's token-validity check; every caller names its path); `HEALTH_PATH` default :24 STAYS `/api/v1/entities`; :16–EOF byte-identical to HEAD. |
| `distribution/smoke/run-smoke.sh` | M (+13/−1) | check 3 banner → "READINESS PROBE (authed loopback — the minted token validates)"; **check 3b** after it: the same binary, `--wait --timeout 30 --health-path "${HS_HEALTH_PATH}"`, NO token file → `ok "unauthenticated loopback /health green (HTTP 200 — the unit's probe path, E3)"` else `bad` + `dump_logs`; the passes-but-false line in-file; digit scheme kept (4–9 unrenumbered). |
| `distribution/install/install.sh` | M (1/1) | :89 `--token-file "${HS_TOKEN_FILE}"` → `--health-path "${HS_HEALTH_PATH}"`. |
| `distribution/update/update.sh` | M (2/2) | :60 + :77 likewise. |
| `distribution/update/update-smoke.sh` | M (2/2) | :44 + :65 likewise. |
| `distribution/deb/homesynapse-token` | M (+7/−17) | usage: two lines under `revoke <keyId>` (refused when it would revoke the last active full-access token — use `rotate`); CAUTION :46–:49 → a three-line NOTE (the probe reads `/health`, never the artifact — deleting after pairing is safe; the R-H2 refusal); `apply_request`: the :110–:121 block REMOVED whole (`rm -f` gone), the `$1` comment made honest. No-arg output byte-identical (cmp). |
| `distribution/docs/token-rotation.md` | M (+14/−36) | `### The readiness-probe caveat` :71–:103 → `### History — the readiness-probe caveat (R-6 → R-9)` (one paragraph; the one-liner kept, now lawful, `mint` first); :156 reworded; the `revoke <keyId>` row + the `DELETE /internal/tokens/{keyId}` API row carry R-H2. |
| `distribution/docs/escalations.md` | M (+2/−1) | §E3: `**Status: CLOSED at R-9 (2026-08-22).**` + what landed + the pointer to this return; the original text kept as "Context (as filed)". |

Untouched by design: `module-info.java` (both modules) · every `build.gradle.kts` · `README.md` (:117) · `web-ui/**` · `PrivateDevices` · `common.sh`'s version arm · `.github/workflows/*` + `distribution/ci/install-smoke.yml` (twins byte-identical, porcelain-clean) · `postinst`/`install.sh` banners ("then delete the token file" — TRUE again, no edit) · `distribution/docs/boot-contract-map.md` (stale, outside the census — §5 item 7b) · `TokenCliTest` (revokes a scoped token; unaffected).

## §2 — the exemption + the endpoint as shipped, and the red-first captures

`RestFilters.authorize` (the order law, two exemptions):
```java
        if (!isPathSafe(ctx.path())) {
            throw problem(ProblemType.INVALID_PARAMETERS,
                    "request path contains an illegal traversal or control sequence");
        }
        // Order is load-bearing: traversal/control rejection FIRST (a
        // `GET /dashboard/../internal/dlq` dies at the gate before either exemption
        // can see it), the two exemptions second, authentication third, rate-limit
        // fourth. Each early-return is independently reversible.
        if (isPublicShellRequest(ctx.method().name(), ctx.path())) {
            return;   // posture (A): the static shell serves without auth; no identity, no rate-limit key
        }
        if (isHealthProbeRequest(ctx.method().name(), ctx.path(), ctx.ip())) {
            return;   // R-9: the loopback readiness bit — one enum word, no data; no identity, no rate-limit key
        }
        ApiKeyIdentity identity = authMiddleware.authenticate(ctx.header("Authorization"));
```
The classifiers:
```java
    static boolean isHealthProbeRequest(String method, String path, String remoteAddress) {
        if (!"GET".equals(method) && !"HEAD".equals(method)) {
            return false;
        }
        if (!HealthEndpoint.PATH.equals(path)) {
            return false;
        }
        return isLoopbackLiteral(remoteAddress);
    }

    static boolean isLoopbackLiteral(String address) {
        if (address == null) {
            return false;
        }
        String literal = address;
        int end = literal.length() - 1;
        if (end >= 1 && literal.charAt(0) == '[' && literal.charAt(end) == ']') {
            literal = literal.substring(1, end);
        }
        int zone = literal.indexOf('%');
        if (zone >= 0) {
            literal = literal.substring(0, zone);
        }
        if (literal.isEmpty()) {
            return false;
        }
        if (literal.indexOf(':') < 0) {
            return isLoopbackDottedQuad(literal);
        }
        char first = literal.charAt(0);
        if (!isAsciiHexDigit(first) && first != ':') {
            return false;
        }
        for (int i = 0; i < literal.length(); i++) {
            char c = literal.charAt(i);
            if (!isAsciiHexDigit(c) && c != ':' && c != '.') {
                return false;
            }
        }
        try {
            return InetAddress.getByName(literal).isLoopbackAddress();
        } catch (UnknownHostException e) {
            return false;
        }
    }
```
(`isLoopbackDottedQuad`: exactly four decimal octets, each 1–3 digits with no leading zero, ≤ 255, first octet 127 — `InetAddress` never touched for IPv4.) The DNS-safety claim is pinned from the JDK 21 source (`src.zip`, `InetAddress.java`): the literal branch opens at `:1635–:1636` (`IPAddressUtil.digit(host.charAt(0), 16) != -1 || host.charAt(0) == ':'`) and a failed IPv6 parse on a colon-bearing host THROWS at `:1661–:1663` (`(host.contains(":") || ipv6Expected) → invalidIPv6LiteralException`); `:1615–:1617` maps an EMPTY host to `impl.loopbackAddress()` — the classifier never passes one.

The gateway and the handler:
```java
    public static void installHealthEndpoint(Object javalinApp, ReadinessSource readinessSource) {
        Objects.requireNonNull(javalinApp, "javalinApp");
        Objects.requireNonNull(readinessSource, "readinessSource");
        Javalin app = (Javalin) javalinApp;
        HealthEndpoint health = new HealthEndpoint(readinessSource);
        app.get(HealthEndpoint.PATH, health);
        app.head(HealthEndpoint.PATH, health);
    }
```
```java
    void apply(EndpointContext ctx) {
        SubscriberMode mode = readinessSource.mode();
        if (mode == SubscriberMode.LIVE) {
            ctx.status(200);
        } else {
            log.debug("/health not ready: projection mode={}", mode);
            ctx.status(503);
            ctx.header(ReadinessFilter.PROJECTION_STATE_HEADER, mode.name());
            ctx.header("Retry-After", ReadinessFilter.RETRY_AFTER_SECONDS);
        }
        ctx.header("Cache-Control", "no-store");
        ctx.json(Map.of("status", mode.name()));
    }
```
The composition root: `RestFilters.installHealthEndpoint(app, this);` at the former :932/:933 seam.

**Red-first captures (run ONCE against HEAD 89a912e production code, the tests already written):**
- **lifecycle (the true red):** `./gradlew :lifecycle:lifecycle:test --tests …HomeSynapseCoreTest` → `16 tests completed, 2 failed` — `healthServesHeaderlessOnLoopbackWhileDataRoutesStayGuarded` FAILED, `AssertionFailedError at HomeSynapseCoreTest.java:396` = **`expected: 200 but was: 401`** (the headerless `GET /health`); `healthStaysGuardedOffLoopback` FAILED at `:449` = **`expected: 200 but was: 404`** (the authed `GET /health` off loopback — no route at HEAD; its two preceding 401 assertions PASSED at HEAD, the preservation half). `BUILD FAILED in 17s`.
- **rest-api (compile-red, disclosed as red-by-absence):** `./gradlew :api:rest-api:compileTestJava` → **31 errors**, every one `cannot find symbol`: `HealthEndpoint` (`HealthEndpointTest:43`, `:118`) · `RestFilters.isHealthProbeRequest`/`isLoopbackLiteral` (`RestFiltersAuthTest` :124–:206, 13 sites) · `OpaqueTokenStore.RevokeOutcome` (`OpaqueTokenStoreTest` ×11, `StandardAuthMiddlewareTest:89`) · `ProblemType.TOKEN_REVOKE_REFUSED` (`TokenAdminEndpointsTest:338`, `:341`). `BUILD FAILED in 2s`.

## §3 — gates (this desk: Windows 11, JDK 21.0.4, Gradle 8.8; Git Bash + dash + WSL Ubuntu-24.04/systemd 255)

**Java.** Targeted `./gradlew :api:rest-api:compileJava :api:rest-api:compileTestJava :api:rest-api:test :lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test` → `BUILD SUCCESSFUL in 19s` (executed: rest-api `compileJava`/`compileTestJava`/`jar`/`test`; lifecycle `compileJava`/`compileTestJava`/`test`); zero `-Xlint` warnings. Test-results XML: **rest-api 147 tests, 0 failures, 0 errors, 3 skipped** (the three POSIX/non-root-gated `OpaqueTokenStoreTest` arms — they run on the Linux runner); per class `HealthEndpointTest` 5 · `RestFiltersAuthTest` 12 · `OpaqueTokenStoreTest` 26 · `TokenAdminEndpointsTest` 10 · `StandardAuthMiddlewareTest` 4; **lifecycle 62 tests, 0 failures, 0 skipped** — `healthStaysGuardedOffLoopback` RAN (a site-local interface exists on this desk; the bind and the loopback-routed connect worked). Spotless: `:api:rest-api:spotlessCheck :lifecycle:lifecycle:spotlessCheck` exit 0 — nothing to apply. **Full `./gradlew check` → `BUILD SUCCESSFUL in 7s`, 156 actionable tasks: 7 executed, 149 up-to-date** (executed: `:api:websocket-api:compileJava`, `:lifecycle:lifecycle:jar`, `:app:homesynapse-app:compileJava`/`compileTestJava`/`test`/`check`, `:testing:integration-tests:compileTestJava`; the app suite fresh — **24/24, `HomeSynapseArchRulesTest` 11/11** incl. `NO_DIRECT_TIME_ACCESS`, `QUERY_SERVICE_READ_ONLY`, `REST_ENDPOINTS_NO_EVENT_PUBLISHING`; the rest-api/lifecycle tests up-to-date from the targeted run on the identical final bytes — result mtimes `HealthEndpointTest.xml` 18:38:33 · `HomeSynapseCoreTest.xml` 18:38:49 · `HomeSynapseArchRulesTest.xml` 18:42:10, read at 18:44:06). Run once (the second of the R-6/R-8 precedent would add nothing: no bytes changed after the targeted run). Disclosed: `testing/integration-tests` is excluded from the default `check` by its own build file ("On-device integration tests (Pi 4 profile). Excluded from the default check task.") — compiled, not run. **Clock:** every new rest-api test is `Clock`-free or uses the class's `FIXED_CLOCK`; both new lifecycle tests boot under `Clock.fixed(2026-08-22T00:00:00Z)`; no `Instant.now`/`System.currentTimeMillis`/`Clock.systemUTC` added (grep-clean on the new test bodies).

**Shell / unit / docs.** `bash -n` ×7 (every touched `.sh` + the helper) + the CI lint loop over ALL `distribution/**/*.sh` → clean; `dash -n` AND `sh -n` on `common.sh`, `health-probe.sh`, the helper → clean; `shellcheck` ABSENT on this host (flagged; CI's Static-lint step re-runs `bash -n`). The helper: no-arg output BYTE-IDENTICAL to HEAD under dash, artifact present AND absent (`cmp`); `--help`/bogus/`revoke`/`revoke 'bad key'`/`mint`/`status extra` → exit 2 each; `rm -f` absent. `run-smoke.sh` check 3b's `if`-line grepped verbatim and its body run as a fragment under `set -uo pipefail` against a stub probe: green arm → `[smoke] PASS  unauthenticated loopback /health green (HTTP 200 — the unit's probe path, E3)` / `FAILS=0`; red arm → `[smoke] FAIL  unauthenticated loopback /health never went green` + diagnostics / `FAILS=1` (routes through `bad`, never exits the script). `ok` sites 20 → 21; every `╔══` banner 79 columns (the new two match). Probe call sites after the sweep: `--health-path` at the unit :53, `install.sh:89`, `update.sh:60/:77`, `update-smoke.sh:44/:65`, `run-smoke.sh:85`; `--token-file` only at `run-smoke.sh:73` (check 3, by design). `health-probe.sh` :16–EOF byte-identical to HEAD (`diff`); `common.sh` diff = one hunk at :40. The unit under `systemd-analyze --man=no verify` (WSL, systemd 255): parses; the two "Command … is not executable: No such file" lines are the desk's (no install); the non-comment diff vs HEAD is the one `ExecStartPost` line. LF + trailing newline on all ten distribution files (`tr -cd '\r' | wc -c` = 0; `git ls-files --eol` = `i/lf w/lf` under `.gitattributes` `text=auto eol=lf`). Twins byte-identical and porcelain-clean.

**CI prediction (the gate of record):** Build & Check GREEN with rest-api 130 → **147**, app 24, lifecycle 60 → **62**; install-smoke BOTH legs GREEN with **19** `[smoke] PASS` lines each (check 3b's line quoted above) and update-smoke green through `--health-path /health` ×2. The unit's `ExecStartPost` on the runner IS the first live-wire proof that the packaged unit starts on `/health` with no token read — H8 closes at §OP-H.

## §4 — census at porcelain (lock-free: `git --no-optional-locks status --porcelain`)

**EXACTLY 24 paths: 22 M + 2 A** — the instruction's 23 (R-H2 IN census) **+ 1**, the flag spelled: **`api/rest-api/src/test/java/com/homesynapse/api/rest/StandardAuthMiddlewareTest.java` (M)**. The instruction's P2 caller survey listed `TokenAdminEndpoints.revoke`, `processOperatorRequests`, `OpaqueTokenStoreTest`, `TokenAdminEndpointsTest`; `git grep -n "\.revoke("` at execution also finds `StandardAuthMiddlewareTest.java:84` (its `revokedTokenIs403` fixture mints ONE full-access token and revokes it — under R-H2 the revoke is REFUSED, the token stays valid, `authenticate` succeeds, the test fails) and `TokenCliTest.java:71` (revokes a SCOPED token — `REVOKED` under R-H2, untouched). The `ProblemType` count-pin survey (the instruction's +1 clause) found nothing; this +1 is the same class of finding (a consumer the survey missed, where the build would be RED without the edit) and is reported under the same clause. Nothing else is dirty: `.github/`, `distribution/ci/`, `README.md`, `web-ui/`, every `build.gradle.kts` and `module-info.java` — clean. Nothing committed; nothing staged.

## §5 — deviations and pushback (evidence over instruction)

1. **[REVIEW] `HEAD /health` is registered explicitly — the instruction's binary had a third answer.** "If Javalin 6 does not answer HEAD for a GET route automatically … register `app.head`": at the 6.7.0 bytecode Javalin DOES answer it automatically — with a bare 200 and the GET handler NEVER executed (`DefaultTasks`, the HTTP task's fallback arm: `method()==HEAD && hasHttpHandlerEntry(GET, uri)` → return). For a route whose status is conditional that is a passes-but-false: `HEAD /health` would read "ready" during REPLAY. `installHealthEndpoint` therefore registers `app.head(PATH, health)` beside `app.get` (one handler; Jetty drops the body for HEAD — e2e-pinned: HEAD 200 with an empty body on loopback, HEAD 401 off loopback). Public surface impact: none beyond the route table; `isHealthProbeRequest` admits HEAD as specified.
2. **[INFO → census +1] `StandardAuthMiddlewareTest`** — §4. The fixture asserts `REVOKED` so a future guard change cannot make it vacuous.
3. **[INFO] `isLoopbackLiteral` is stricter than the instruction's charset rule, for the instruction's own reason.** The specified guard ("any character outside `[0-9A-Fa-f:.]` → false, else `InetAddress.getByName`") would still hand hex-only hostnames (`cafe.babe`, `deadbeef`, `1e3`) and colon-free non-quads (`1.2.3.4.5`, `127.000.000.001`, `2130706433`) to `getByName`, and JDK 21 RESOLVES a colon-free string that fails the IPv4 parse (`InetAddress.java:1635–:1663`: only a colon-bearing failure throws) — exactly the DNS stall the instruction forbids. Shipped: the IPv4 arm parsed locally (strict dotted quad, `InetAddress` untouched), the IPv6 arm charset-guarded plus the JDK's own first-char precondition; brackets stripped (Jetty 11.0.25 `formatAddrOrHost` brackets IPv6 peers); the empty-after-strip case guarded (`getByName("")` returns loopback). Every listed literal in the instruction is covered; 52 literals pinned.
4. **[INFO] The unit's header (:8–:13) carried the same "two-line edit" claim R-9-b kills at the bottom** — reworded in the same file (comment-only; zero directive change) so the unit does not contradict its own DANGER block.
5. **[INFO] `token-rotation.md`: the `DELETE /internal/tokens/{keyId}` API row gained the 409 clause** (a row, not a section move) — without it the wire table would be false by omission. The `revoke <keyId>` row carries the R-H2 line the instruction asked for.
6. **[INFO] The helper's `# $1 = the verb just queued.` comment** became "(informational — since R-9 every verb applies the same way …)" — `apply_request` still receives the verb (call sites unchanged) but no longer branches on it.
7. **Findings outside the census — filed, not edited:**
   - **(a) `homesynapse.service:31` `LogDirectory=homesynapse` is not a systemd directive** — the directive is `LogsDirectory=`. `systemd-analyze verify` (systemd 255) on the unit: `:31: Unknown key name 'LogDirectory' in section 'Service', ignoring.` Consequence: `/var/log/homesynapse` exists only because `install.sh:72` / `postinst` create it, and under `ProtectSystem=strict` it is NOT implicitly writable (only the `*Directory=` paths are). Harmless today (the runtime logs to journald and resolves every dir from `$HOMESYNAPSE_HOME` = the StateDirectory); load-bearing the day `LinuxSystemPaths` wires `logDir()` (E4/M13). A one-token directive fix + a `systemd-analyze verify` step in Static lint would close it; the hub rules (pre-existing since the skeleton; not this WU's census).
   - **(b) `distribution/docs/boot-contract-map.md:70–:82`** still says "There is no unauthenticated health endpoint … (E3)" and "The M13 flip is staged and commented in the unit" — stale after R-9; the unit's DANGER block points at it. Doc-only; outside the 23-row census; left for the hub's fold.
   - **(c) Doc 09 §15 Q1 (`homesynapse-core-docs/design/09-rest-api.md:998`)** — "[Resolved]: The health endpoint requires authentication … No unauthenticated endpoint is needed." — the R10-IN-L return's owed fold under every C-option; a docs-repo AMD, not a core-lane edit.
   - **(d)** `postinst:74` / `install.sh` banner ("then delete the token file") and the helper's no-arg line :71 — TRUE again after this WU; no edit needed (H-1b closes by construction).
   - **(e)** The probe's file-sourced token CACHE (the R-6 §7 item 1b root cause) is now moot for the unit (no token is read on `/health`) and remains as-is for check 3's authed run (read once at exec is fine when nothing rotates mid-smoke).
8. **Rider R-9-a executed** (the four-mode matrix names `SUSPENDED`) plus a set pin; **rider R-9-b executed** as the DANGER block with the source pointer.
9. **Red-first accounting** — §2: the lifecycle row is the true red (`expected: 200 but was: 401` / `…404`); the rest-api rows are compile-red by absence (31 errors, the four missing symbols), disclosed as such.
10. **The glossary spot-check**: `HomeSynapse_Core_v1_Glossary.md` carries no readiness/health/loopback/revoke vocabulary (it is the API-token + concept glossary); the five names checked against SOURCE instead — `SubscriberMode` (event-bus), `ReadinessSource` (state-store), `ProblemType`/`ApiKeyClaims.SCOPE_ALL`/`EndpointContext` (rest-api) — all match; the one wire key `status` is a single lowercase word (snake = camel).

NO BLOCKING DEVIATIONS.

## §6 — the rulings as received (H10, Nick 2026-08-22)

**R-H1 = LOOPBACK-ONLY (RULED)** — executed: `isHealthProbeRequest` requires a loopback literal; off loopback `/health` needs a token (e2e-pinned on a site-local bind). **R-H2 = IN (RULED)** — executed: `RevokeOutcome`, the guard, `TOKEN_REVOKE_REFUSED` (409), the request-file `skipped` text, the helper + doc lines; the 23-row census (+1, §4). **R-9-a** (SUSPENDED in the matrix) and **R-9-b** (the DANGER block) — executed. The `module-info.java` embed honored verbatim (zero change); zero build-file change.

## §7 — next-WU pointers (their own WUs; nothing here changed)

- **R-7b** (hub design at the beat-6 audit §4): the `0.1.0+git<date>.g<sha>` scheme BEFORE any CI-built artifact reaches a card · the `0.1.0-skeleton` fence · `HS_DIST_DIR` (the cwd-dependent `VERSION` lookup) · `setup-node`/`upload-artifact` majors · E1.
- **R-3b**: the packaged-unit artifact-absent restart proof (delete `config/initial_api_token` on purpose → `systemctl restart homesynapse` → `is-active` = active) rides the held-card packet as its first block — the H8 close of THIS WU's availability fix.
- **`LogsDirectory=`** (§5 7a) + a `systemd-analyze verify` lint step · **`boot-contract-map.md`** §Health fold (§5 7b) · **Doc 09 §15 Q1** fold (§5 7c, docs repo).
- The F-V2 residue (`IssueCommandEndpoint.problemWithFields`, `ReadinessFilter`'s 503 — still `application/json`) — unchanged by this WU; the `/health` 503 body is `application/json` by design (not a problem+json document).
- `/readyz` as the gated successor (R10-IN-L: trigger = any external prober) — not built; `/health` stays the one readiness bit.

## §OP-H refinements (Nick; the instruction's block stands)

- The bench runs from `installDist`, so `/opt/homesynapse/libexec/health-probe.sh` is absent there: run `bash ~/homesynapse-core/distribution/smoke/health-probe.sh --health-path /health 2>&1 | tail -1` (the same bytes the image ships) — expect `[health-probe] ready (200) at http://127.0.0.1:7070/health`. The bench app must be rebuilt from the landed commit first; against the OLD build the line is `unexpected status 404` (the route does not exist) — that is the red-first shape, not a fault.
- `curl -sS -w '\n' http://127.0.0.1:7070/health` → exactly `{"status":"LIVE"}` (Jackson compact; the e2e pins the same bytes). `curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:7070/api/v1/entities` → `401`. Optional fourth line: `curl -sS -I http://127.0.0.1:7070/health | head -1` → `HTTP/1.1 200 OK` (the explicit HEAD route).
- If the bench is reached through the `cloudflared` tunnel, `/health` answers there unauthenticated too — the disclosed tunnel-presents-as-loopback residue (§5 / MODULE_CONTEXT), not a defect.

## WUCP Phase 1: Coder Closeout

- [x] MODULE_CONTEXT.md updated for: `api/rest-api` (§E3-HEALTH, 8 rows + 2 gotchas + the inventory cell + the retired gotcha marked), `lifecycle/lifecycle` (the top blockquote)
- [x] coder-handoff.md updated (the R-9 DELIVERED entry prepended; frontmatter `last-verified` advanced)
- [x] Deferred build gate flag: **NO** — targeted + Spotless + full `./gradlew check` ran GREEN on this desk (§3); CI on Nick's push remains the gate of record (law 16)
- [x] coder-lessons.md appended: two entries (the framework's automatic HEAD-for-GET is a bare 200 without the handler — pin the fallback arm from bytecode; a refusal guard on a mutator re-fixtures every single-token test — walk `git grep` callers, not the survey, and assert the non-refused outcome; the DNS-safe address-literal classifier)
- [x] Cross-agent note posted: Not needed (the channel is retired; the hub carries §5 items 7a–7c at intake)
- Timestamp: 2026-08-22 23:50 UTC
