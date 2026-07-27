<!--
file: context/instructions/2026-07-27_DASH-SERVE_dashboard-serve-path_coding-instruction.md
purpose: Coding instruction for WU-DASH-SERVE — give the dashboard a serve path: real packaging from :web-ui:dashboard, the Javalin /dashboard mount + root redirect, and the RULED posture-(A) static-shell auth exemption. P1; core lane (host-CC); gates G2's close and all of FE-LIVE-V112.
audience: Coder.
status: ISSUE-READY 2026-07-27 (v39 hub, beat 1). Companion pre-verification: context/pre-verifications/WU-DASH-SERVE.md (P0–P15 — READ FIRST, verify every pin, STOP on mismatch).
rulings-of-record: the dashboard auth posture = (A) THE STATIC-SHELL EXEMPTION (Nick, by delegation, 2026-07-26 — pm-handoff v38 beat 8); the sequencing (DASH-SERVE first, the idle Coder runs it) ratified same beat.
-->

# Coding Task: WU-DASH-SERVE — the dashboard serve path (package · mount · the ruled auth exemption)

## What This Implements

The 2026-07-26 deploy evening proved the Pi runs `2040a66` — and that the dashboard the FE lane built and audited is unreachable from any browser: three independent, source-verified blockers (pre-verification header; pm-handoff v38 beat 7). This WU closes the seam end-to-end so the NEXT deploy evening's browser-block redux can run its three glances and close G2:

1. **B-2 PACKAGE** — `:web-ui:dashboard` becomes a real resources-only artifact: the staged SPA is packaged into its jar under `/dashboard`, so the app's existing `runtimeOnly(project(":web-ui:dashboard"))` carries it onto the runtime classpath and `installDist`/the image build pull the npm pipeline into their graph. **`./gradlew check` stays Node-free — that is a hard invariant of this WU, with its own mechanism (DP-2) and its own gate assert.**
2. **B-1 SERVE** — the composition root mounts the classpath `/dashboard` resources at hostedPath `/dashboard` with the SPA fallback to `index.html`, plus a `/` → `/dashboard/` redirect.
3. **B-3 AUTH** — the catch-all auth filter gains the RULED posture-(A) exemption: EXACTLY GET/HEAD on `/dashboard`, `/dashboard/**`, and `/` — nothing else. Every `/api/*` and `/internal/*` request stays token-guarded. One-line-reversible.
4. **CI rider** — `install-smoke` (which builds the image via `installDist` and now needs Node) gains a pinned `setup-node` step in BOTH workflow copies, and `run-smoke.sh` gains the serve-path asserts — the standing CI instrument for exactly the seam class this WU closes (L1/L4, pm-lessons 2026-07-26).

**Seam I/O contract (format addition #17 — the seam this WU owns, hop by hop):** Vite `dist/` (base `/dashboard/`, verified P7) → `stageDashboard` staging → **jar entry `dashboard/index.html`** (DP-1; self-asserting) → app runtime classpath via `runtimeOnly` (P6: classpath launch, both distribution paths) → Javalin classpath mount at `/dashboard` (DP-3) → the GET/HEAD shell exemption (DP-4) → a browser renders it. Each hop carries its own proof (DP-1's jar doLast assert · install-smoke on the push · the DP-3/DP-4 tests · the deploy evening's glances). A claim about any hop cites that hop's own evidence — never a neighbor's.

## Files to Read Before Starting

1. `context/pre-verifications/WU-DASH-SERVE.md` — P0–P15; verify every pin against the working tree.
2. `web-ui/dashboard/MODULE_CONTEXT.md`, `api/rest-api/MODULE_CONTEXT.md`, `lifecycle/lifecycle/MODULE_CONTEXT.md` — inventories, contracts, gotchas.
3. `web-ui/dashboard/build.gradle.kts` + `app/homesynapse-app/build.gradle.kts` + `settings.gradle.kts` (P1–P3).
4. `api/rest-api/src/main/java/com/homesynapse/api/rest/RestFilters.java` + `StandardAuthMiddleware.java` (P4) and `api/rest-api/src/test/java/com/homesynapse/api/rest/RestFiltersAuthTest.java` (P8 — the helper-test pattern).
5. `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` `:895–:958` (P5) and `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreTest.java` (P9 — the boot harness; `opensHttpOnlyBehindAuth` is the pattern).
6. `.github/workflows/install-smoke.yml`, `distribution/ci/install-smoke.yml`, `distribution/smoke/run-smoke.sh`, `distribution/image/build-image.sh` (P10, P6).
7. Both module-info.java files are embedded verbatim at P13 — no module-info changes in this WU.

## Files to Create or Modify (the census — EXACTLY 13: 12 M + 1 new)

| # | Path | Kind |
|---|---|---|
| 1 | `web-ui/dashboard/build.gradle.kts` | M — DP-1 |
| 2 | `app/homesynapse-app/build.gradle.kts` | M — DP-2 |
| 3 | `api/rest-api/src/main/java/com/homesynapse/api/rest/RestFilters.java` | M — DP-4 |
| 4 | `lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` | M — DP-3 |
| 5 | `api/rest-api/src/test/java/com/homesynapse/api/rest/RestFiltersAuthTest.java` | M — tests (3 → 6 @Test) |
| 6 | `lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreTest.java` | M — tests (11 → 14 @Test) |
| 7 | `lifecycle/lifecycle/src/test/resources/dashboard/index.html` | **NEW** — test fixture (sentinel shell) |
| 8 | `.github/workflows/install-smoke.yml` | M — DP-5 (active copy) |
| 9 | `distribution/ci/install-smoke.yml` | M — DP-5 (source copy, byte-identical delta) |
| 10 | `distribution/smoke/run-smoke.sh` | M — DP-5 serve asserts |
| 11 | `api/rest-api/MODULE_CONTEXT.md` | M — beat |
| 12 | `lifecycle/lifecycle/MODULE_CONTEXT.md` | M — beat |
| 13 | `web-ui/dashboard/MODULE_CONTEXT.md` | M — beat (packaging model) |

Anything outside this set appearing in porcelain is a STOP. `package.json` / lockfiles / any `web-ui/dashboard/src/**` file must NOT appear (P7 — the frontend is already serve-ready).

## Technical Specification

### DP-1 — B-2: `:web-ui:dashboard` becomes a self-asserting resources jar

In `web-ui/dashboard/build.gradle.kts`:

- Replace `plugins { base }` with `plugins { java }` — **bare `java`, deliberately NOT `homesynapse.java-conventions`** (resources-only module: no Java sources, no toolchain need, no spotless-java surface; document this rationale in the header comment).
- Re-point staging OUT of the source tree: `val staticOut = layout.buildDirectory.dir("staged-dashboard")` (was `src/main/resources/dashboard`). Grounds: with the `java` plugin, anything under `src/main/resources` is swept by `processResources` — stale staged content would ride into every jar nondeterministically AND wiring `processResources → stageDashboard` would drag npm into `check` via test classpaths. Staging into `build/` keeps `processResources` empty/NO-SOURCE forever. Update `clean` accordingly (the default `clean` already deletes `build/`; keep the explicit `delete(dist)` for the Vite output).
- Package via the jar task, which is the ONLY npm-consuming seam:
  ```kotlin
  tasks.named<Jar>("jar") {
      from(stageDashboard) { into("dashboard") }   // task dependency carried automatically
      doLast {
          // Packaging self-assert (L1: the hop proves itself) — fail the build
          // if the SPA shell is not actually inside the artifact.
          val jarFile = archiveFile.get().asFile
          java.util.zip.ZipFile(jarFile).use { zip ->
              requireNotNull(zip.getEntry("dashboard/index.html")) {
                  "dashboard jar is missing dashboard/index.html — the npm pipeline did not stage the SPA"
              }
          }
      }
  }
  ```
- Delete the now-redundant `tasks.named("assemble") { dependsOn(stageDashboard) }` line (`assemble → jar → stageDashboard` subsumes it).
- Rewrite the header DECOUPLING NOTE to state the NEW mechanism and its proof obligations: npm attaches to the **jar task only**; `processResources` is never wired to npm; the app-side test-classpath exclusion (DP-2) is the second half; `./gradlew check` must execute ZERO `:web-ui:dashboard:npmInstall|npmBuild|stageDashboard|jar` tasks (the gate assert below).
- Do NOT set `group`/`version`, do NOT add a module-info, do NOT register extra artifacts/configurations.

### DP-2 — the check-stays-Node-free mechanism (app side)

In `app/homesynapse-app/build.gradle.kts`, directly below the existing `runtimeOnly(project(":web-ui:dashboard"))` block:

```kotlin
// DASH-SERVE: keep the core gate Node-free. The dashboard artifact is inert
// static bytes for PACKAGING only — no test reads it. Without this exclusion,
// testRuntimeClasspath (which extends runtimeClasspath) would resolve the
// :web-ui:dashboard jar and drag npmInstall/npmBuild into `./gradlew check`,
// violating the module's DECOUPLING NOTE. One line; reversible.
configurations.named("testRuntimeClasspath") {
    exclude(module = "dashboard")
}
```

**Why this is safe:** the jar contains zero classes (nothing for ArchUnit or any test to lose — P12); `testCompileClasspath` never saw it (runtimeOnly); production `runtimeClasspath` (start scripts, installDist, the image) still carries it.

### DP-3 — B-1: the mount + the root redirect (composition root)

In `HomeSynapseCore.java` (P5 sites):

- Extend the EXISTING `Javalin.create(cfg -> { … })` lambda (`:903`) — after `cfg.showJavalinBanner = false;`:
  ```java
  // DASH-SERVE (Doc 13 §3.2–§3.3, composed at last): serve the packaged SPA
  // from the classpath at /dashboard, with the SPA fallback for client-side
  // routes. The bytes arrive via :web-ui:dashboard's resources jar
  // (runtimeOnly). Auth posture: the (A) static-shell exemption — see
  // RestFilters.installAuth.
  cfg.staticFiles.add(sf -> {
      sf.hostedPath = "/dashboard";
      sf.directory = "/dashboard";
      sf.location = Location.CLASSPATH;
  });
  cfg.spaRoot.addFile("/dashboard", "/dashboard/index.html", Location.CLASSPATH);
  ```
  (Verify exact 6.7.0 member names against the pinned Javalin API — P14; a mismatch is pushback, not improvisation. Add the `io.javalin.http.staticfiles.Location` import; `requires io.javalin` already present, no module-info change.)
- Immediately after `RestFilters.installAuth(app, …)` (`:910`), register the root redirect:
  ```java
  // DASH-SERVE: the human entrypoint — http://host:port/ lands on the SPA.
  // Covered by the same GET/HEAD shell exemption (posture (A)).
  app.get("/", ctx -> ctx.redirect("/dashboard/"));
  ```
- Touch nothing else in the install sequence; `app.start(...)` and the bind posture are unchanged.

### DP-4 — B-3: the RULED posture-(A) static-shell exemption (RestFilters)

- New package-private classifier beside `isPathSafe` (strings in, boolean out — the established unit-testable shape, P4/P8):
  ```java
  /**
   * The posture-(A) static-shell exemption (ruled 2026-07-26): TRUE exactly for
   * GET/HEAD requests to the inert public shell — "/", "/dashboard", or
   * "/dashboard/**". Every other method and every other path — notably every
   * /api/* and /internal/* route — remains token-guarded. The exemption's own
   * invariant: no DATA route is ever unauthenticated; the shell is inert public
   * bytes (the same trust class as a downloaded app binary); removing the single
   * early-return in authorize() restores the unconditional guard (one-line-
   * reversible). Runs strictly AFTER isPathSafe — the traversal gate still
   * precedes every auth decision.
   */
  static boolean isPublicShellRequest(String method, String path) {
      if (!"GET".equals(method) && !"HEAD".equals(method)) {
          return false;
      }
      return "/".equals(path) || "/dashboard".equals(path) || path.startsWith("/dashboard/");
  }
  ```
- In `authorize(...)`, insert the early-return BETWEEN the `isPathSafe` gate and `authenticate(...)`:
  ```java
  if (isPublicShellRequest(ctx.method().name(), ctx.path())) {
      return;   // posture (A): the static shell serves without auth; no identity, no rate-limit key
  }
  ```
  Order is load-bearing: traversal/control rejection FIRST (a `GET /dashboard/../internal/dlq` dies at the gate before the exemption can see it), exemption second, authentication third, rate-limit fourth.
- Update the `installAuth` Javadoc: the "covering every other path" sentence gains the exemption statement + the invariant text above (the register amendment itself is hub-owned — Out of Scope).
- **Stated residue (accepted at ruling, record in the completion report):** exempted shell requests bypass rate-limiting (no authenticated key exists for them); the surface is loopback-bound by default (P5) and serves inert bytes; the posture-(B) cookie-session successor re-visits this post-gate.

### DP-5 — the CI rider (install-smoke needs Node; the smoke asserts the seam)

- In BOTH `install-smoke.yml` copies (`.github/workflows/` active + `distribution/ci/` source — byte-identical delta; the WIRING SEAM header explains the duality), add after the `Setup Gradle` step:
  ```yaml
      - name: Set up Node 22 (dashboard packaging — installDist now builds the SPA)
        uses: actions/setup-node@v4
        with:
          node-version: '22'
  ```
- In `distribution/smoke/run-smoke.sh`, directly after the existing UNAUTH assert (`:92–:96`), add the serve-path asserts (same style/tooling as the surrounding code, no `-f`):
  - headerless `GET http://${HS_BIND}:${HS_PORT}/` → expect `302` (the redirect; also accept `301` only if Javalin emits it — verify and pin ONE code);
  - headerless `GET http://${HS_BIND}:${HS_PORT}/dashboard/` → expect `200`;
  - failure of either = smoke FAIL with a named message ("dashboard serve path broken — B-1/B-2/B-3 class").
  This makes the gate of record assert artifact→packaging→serving→auth on every push — the standing seam-detector (L4).

## Locked Decisions That Apply

- **Posture (A) static-shell exemption — RULED 2026-07-26** (Nick, by delegation; pm-handoff v38 beat 8). The allowlist is EXACTLY GET/HEAD on `/`, `/dashboard`, `/dashboard/**`. (B) is the named post-gate successor; (C) was rejected.
- **Doc 13 §3.2–§3.3** — the serving design this WU composes (classpath static files at `/dashboard/`, SPA fallback).
- **INV-SE-02** — substance preserved: no DATA route ever unauthenticated; amended in place with the exemption's invariant (hub-owned docs edit at landing).
- **The DECOUPLING NOTE law** — `./gradlew check` never needs Node (DP-1/DP-2 are its realization under packaging).
- **DEC-M3-16 / Object-erasure gateway** — untouched; no new exported signatures on RestFilters.
- **AB-1 / C1-close** — auth-before-everything install order unchanged; the exemption lives INSIDE the filter, never as a route bypass.

## Invariants That Must Hold

- Headerless `GET/HEAD` on the shell paths serve; **every** other method on those paths and **every** request to `/api/*` + `/internal/*` behaves exactly as at HEAD (401 missing-header / 403 bad-token / 429 semantics byte-identical).
- The traversal gate (`isPathSafe`) precedes the exemption — encoded/raw traversal on `/dashboard/**` still 400s.
- `./gradlew check` executes ZERO `:web-ui:dashboard:` npm/stage/jar tasks (the gate assert below).
- The jar self-assert: a dashboard jar without `dashboard/index.html` fails its own build.
- Wire shapes, event model, projections: untouched (this WU emits nothing and derives nothing).

## Test Requirements (tests FIRST; fixture-paired; every new assert names its false-verdict boundary)

**`RestFiltersAuthTest` — 3 → 6 @Test (unit, strings-in):**
1. `isPublicShellRequest_exactAllowlist` — TRUE rows: GET+HEAD × `/`, `/dashboard`, `/dashboard/`, `/dashboard/assets/app.js`, `/dashboard/deep/route`.
2. `isPublicShellRequest_rejectsEverythingElse` — FALSE rows: POST/PUT/DELETE/PATCH/OPTIONS on `/dashboard/`; GET on `/dashboardevil`, `/dash`, `/api/v1/entities`, `/internal/dlq`, `/apidashboard`; empty/`null`-guard behavior pinned (match `isPathSafe`'s null posture).
3. `shellExemption_neverPrecedesTraversalGate` — pins the ORDER contract: `isPathSafe("/dashboard/../internal/dlq")` is false (the row that would let an exemption-first refactor lie its way to green).

**`HomeSynapseCoreTest` — 11 → 14 @Test (end-to-end on the real boot, the `opensHttpOnlyBehindAuth` harness; inject `Clock` per the arch-rule reminder — lifecycle is outside the enforced classpath, the convention is self-enforced):**
4. `rootRedirectsToDashboardUnauthenticated` — headerless `GET /` → 302 + `Location: /dashboard/`; PAIRED in the same test: headerless `GET /api/v1/entities` still 401 (the preservation fixture — the false-verdict boundary for an over-broad exemption).
5. `dashboardShellServesUnauthenticated` — headerless `GET /dashboard/` → 200 + body contains the fixture sentinel; headerless `GET /dashboard/nonexistent/route` → 200 + sentinel (SPA fallback); `HEAD /dashboard/` → 200.
6. `dashboardWriteAndDataRoutesStayGuarded` — headerless `POST /dashboard/x` → 401; headerless `GET /internal/dlq` → 401; a traversal probe `GET /dashboard/%2e%2e/internal/dlq` → **EXACTLY 400** (the encoded form survives client-side URI normalization and reaches `isPathSafe`; the EXACT status is load-bearing — a mutant that lets the exemption precede the gate yields 404/401/200 there, never 400).

Fixture: `lifecycle/lifecycle/src/test/resources/dashboard/index.html` — a minimal shell carrying the sentinel string `HS-DASH-FIXTURE-SENTINEL` (the lifecycle test classpath supplies what production gets from the resources jar; state this in a fixture comment).

**Red-first discipline:** run the six new legs at HEAD pre-edit; expect the two unit tests red-by-compile (helper absent — disclosed as such), and ALL THREE e2e tests red for behavioral reasons (401 where 302/200 expected). Record exact red counts. Stage-B: full green ×2 fresh JVMs on the final tree.

**Mutation legs (cmp-restored, named kills):** M1 — flip the exemption to also allow POST (`|| "POST".equals(method)`): `dashboardWriteAndDataRoutesStayGuarded` must kill it. M2 — widen `startsWith("/dashboard/")` to `startsWith("/dash")`: `isPublicShellRequest_rejectsEverythingElse` must kill it. M3 — move the exemption ABOVE the `isPathSafe` gate in `authorize`: the EXACT-400 traversal e2e row must kill it (under the mutant the probe resolves through the exemption to a non-400 outcome; the order is the security property, and the exact status is its instrument).

## Code Quality Standards

`-Xlint:all -Werror` rides the convention plugin on rest-api/lifecycle/app (never pass it as a CLI flag); spotless license headers on touched Java; explicit test-class constructors per the existing pattern; Register-C comment tone; no new dependencies, no version-catalog changes, no attribution trailers anywhere.

## Dependencies and Integration Points

- Consumers of the auth filter's behavior: every REST/bench client (bench.sh `api_token()` flows are untouched — `/api/*` semantics identical), the FE dashboard (FE-LIVE-V112 builds the token UX against `/dashboard/` + `Authorization: Bearer` fetches — this WU is its unblock), install-smoke (DP-5 keeps it green + makes it the seam's standing instrument).
- The Pi op-order (Node one-time install; the first `installDist` gains npm-ci + Vite minutes — 23s is no longer the lawful envelope) rides the NEXT deploy brief, NOT this WU.

## What to Watch Out For

- **The npm-into-check trap is the WU's central hazard.** Three innocent-looking alternatives all break the law: wiring `stageDashboard → processResources` (drags npm into every test classpath); staging under `src/main/resources` with the `java` plugin (same, via the implicit resources sweep — this is WHY `staticOut` moves to `build/`); omitting DP-2 (app's `testRuntimeClasspath` builds the jar → npm). If `check` output shows ANY `:web-ui:dashboard:npmInstall`/`npmBuild`/`stageDashboard`/`jar` line, the mechanism has failed — STOP and report, do not rationalize.
- **Do not run `assemble`/`installDist`/`:web-ui:dashboard:jar` in-session** — npm is not a granted tool in this lane; the packaging leg's gate of record is `install-smoke.yml` on the pushed commit (plus the jar's own doLast assert whenever any host builds it).
- **Javalin before-handler vs static files:** Javalin runs `before(*)` ahead of static-file resolution (the deploy evening's 401-on-`/` is the live proof) — the exemption is therefore sufficient; no static-handler-level auth config exists or is needed.
- **`ctx.method()` returns an enum in Javalin 6** (`HandlerType`) — `.name()` for the string, or compare enums; keep the helper string-typed for unit-testability.
- **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in test code. Enforcement reach (corrected 2026-06-13): the ArchUnit rule scans app's test classpath only — for lifecycle/rest-api test code this is a self-enforced convention. Use the harness's existing fixed-clock pattern.
- **The two install-smoke copies must stay byte-identical in their delta** — a drift between the active and source copies is exactly the stale-context class the sweep discipline exists for.
- **`exclude(module = "dashboard")`** keys on the project NAME (P3); if Gradle resolution surprises you (group-qualification, variant errors), that is pushback material with the resolution error quoted — do not silently switch mechanisms.
- The `verdicts`/explanation surfaces, `ListRunsEndpoint`, and every wire shape: NOT in this WU's blast radius; their appearance in a diff is a STOP.

## Coder Pushback Welcome

Flag, with evidence, anything that contradicts the pins: Javalin 6.7.0 API-shape mismatches (quote the real signatures), Gradle exclude/variant behavior that defeats DP-2 (quote the resolution error), a `spaRoot`+`staticFiles` interaction that double-serves or shadows (quote observed behavior), smoke-script portability concerns (BusyBox wget vs curl — match the file's own conventions). The contract (WHAT: served shell, exact allowlist, Node-free check) is ruled; the HOW inside these files is yours where the spec above marks intent.

## Out of Scope

- **CMD-API-ACTOR** — adjudicated OUT of this WU at authoring (v39 beat 1): it is a write-path event-payload change (actorRef on `command_issued`) inside a freeze-window serve-path WU — different risk class, single-concern discipline. It stays parked for the first post-gate rest-api touch. (The standing-ledger pairing question is hereby answered on the record.)
- Posture (B) cookie-session pairing (post-gate design successor; launch-runway-charter candidate).
- The FE token UX / any `web-ui/dashboard/src/**` change (FE-LIVE-V112, blocked on this WU's landing).
- The INV-SE-02 register amendment + Doc 13 §3.2–§3.3 as-built note (hub-owned docs-repo edits at landing intake, folded with the doc-drift ×3 batch).
- The Pi Node install + build-envelope reset (the NEXT deploy brief's op-order).
- Any vite/base change (P7: already `/dashboard/`).

## Build Discipline (this WU's CC-lane grant)

Targeted loop: `./gradlew :api:rest-api:compileJava :api:rest-api:test :lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test :app:homesynapse-app:test` — plus ONE full `./gradlew check` against the final tree (run it twice if the first needed any fix). **Baselines forced-fresh pre-edit** (record exact counts for rest-api / lifecycle / app test tasks; carry no prior-session numbers). **The Node-free gate assert:** after the full `check`, grep the build output for `:web-ui:dashboard:` — the ONLY lawful appearances are `compileJava`/`processResources`/`test`-family tasks in NO-SOURCE/SKIPPED/UP-TO-DATE states; any `npmInstall`/`npmBuild`/`stageDashboard`/`jar` line is a FAIL. Quote the grep result in the completion report (the anti-vacuous positive-evidence line: also quote the `:web-ui:dashboard:test SKIPPED`-class lines proving the module WAS in the graph).

## Work Unit Completion (WUCP Phase 1)

Standard five: completion report (per-DP realization + the deviation ledger + the stated residue + the red/green/mutation arithmetic + the Node-free grep quotes) · coder-handoff entry (next WU = **B2**, bench lane — the hub authors it; core goes QUIET until the M14 WUs) · cross-agent note to the hub requesting the two-layer audit BEFORE any commit · MODULE_CONTEXT beats (#11–#13 in the census) · lessons if any. The hub's audit precedes any commit order; commit staging will be EXPLICIT paths, exactly the 13-file census, core-repo only.
