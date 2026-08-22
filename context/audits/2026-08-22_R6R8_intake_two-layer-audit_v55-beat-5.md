<!--
file: context/audits/2026-08-22_R6R8_intake_two-layer-audit_v55-beat-5.md
purpose: The hub's two-layer audit record for the R-6/R-8 TOKEN-OPS coder return (`2026-08-22_R6R8_token-ops_return.md`) — layer 1 = the return's claims, layer 2 = the bytes at the instrument (the core working tree at 33861ad + 16, exported to _scratch/v55-audit/ and read whole). Verdict, the corrections applied, the findings the return does not carry, the CI predictions filed BEFORE the push (H12), the follow-on rulings (E3-HEALTH as the root fix; the interim operator law), and the harvest.
audience: Nick (the commit + the rulings); the hub (the chain of custody); the next lane (the E3 instruction's inputs).
posture: hypercritical by instruction (Nick, 2026-08-22 06:30 CT: "instead of just confirming everything … think hypercritically and proactively").
verified-at: 2026-08-22 ~06:35–07:20 CT, v55 hub beat 5; core HEAD 33861ad; hivemind HEAD 8f2cb08.
-->

# R-6/R-8 TOKEN-OPS — intake audit (v55 beat 5, 2026-08-22)

## §0 Verdict

**ACCEPT.** The lane delivered what the instruction ordered, with three rulings honored (R-A IN + the audit rider; R-B TZ-HOLD; R-C IN by P11) and its deviations disclosed with evidence. One byte was changed by the hub before the commit (a test-count line in `api/rest-api/MODULE_CONTEXT.md`, §2 D-C). Five findings the return under-states or does not carry are recorded (§3) and ruled (§5). The commit order is 16-exact (core) + 6-exact (hivemind).

**The dispatch label.** Nick's 06:30 message called the session "the R7 ARM64 instruction"; the lane ran the **R-6/R-8** instruction (its own return, its census, its rulings). Verified at the instrument: the 16 dirty paths are exactly the R-6/R-8 census; **zero R-7 files touched** (`install-smoke.yml` ×2, `common.sh`, `build-image.sh`, `docs/architecture.md` clean; no `smoke/version-grammar-test.sh`). Effect nil; the one-lane-at-a-time law is intact; R-7 is next.

## §1 Layer 1 vs layer 2 — the claims at the bytes

| Claim (return) | At the instrument | Verdict |
|---|---|---|
| Census 16 = 11 M + 5 A; nothing else dirty; nothing committed | `git --no-optional-locks status --porcelain -uno` → the 11 M verbatim; the scoped untracked scan → the 5 A verbatim; the rest of the tree clean; HEAD `33861ad` | ✓ exact |
| `RecordingEndpointContext` needs no bytes ("records every header … :378–:380") | `headers` is a `LinkedHashMap` at **:32**, `header()` puts at **:100**; the file is **107 lines** — the claim is TRUE, the citation is WRONG (H-3) | ✓ claim / ✗ cite |
| `git diff --stat` 11 files `+942/−37` | `--numstat` on the final bytes: **11 files +1067/−38** (the return's figure predates the review-fleet adoptions) | stale figure (H-3) |
| L3 — no hash, no raw token on any surface | Hub scan over the return + every diff + every new file + the handoff/lessons diffs: **zero 64-hex runs, zero 43-char base64url runs** beyond identifiers/paths; the tests mint at runtime (no literal token fixtures) | ✓ |
| Request-file order: exists → read → **delete FIRST** → execute; unreadable → WARN + zero + file LEFT; undeletable → WARN + zero + nothing | `OpaqueTokenStore.processOperatorRequests()` at the diff: exactly that, under `writeLock`; `revoke`/`rotate`/`mint` nest re-entrantly; `skipped` = `line N: <reason>`, the only echo a key id `claimsFor` already knows | ✓ |
| Atomic owner-only persist | `writeOwnerOnlyAtomically`: `deleteIfExists(tmp)` → `CREATE_NEW`+`WRITE` (+`rw-------` attrs on POSIX) → write → `force(true)` → re-assert perms → `ATOMIC_MOVE`; failure → temp removed best-effort, `UncheckedIOException(prefix + target)`. No directory fsync (same as the `AtomicYamlWriter` idiom — a power-loss window on the rename, not a correctness gap; note only) | ✓ |
| `rotate`: mint → revoke every other active → ONE persist → artifact; WARN + rethrow if the artifact write fails after the persist | at the diff, verbatim; `entrySet().setValue` on the CHM | ✓ |
| R-C: header AFTER `json()`; RED at `:73` first | `EndpointResponses.problem`: `status → json → header("Content-Type", PROBLEM_JSON)`; `RestFilters.writeProblem` at HEAD :549–:551 = `json` then `contentType("application/problem+json")` with the "Override…" comment — the precedent is real | ✓ |
| Wiring: after `ensureInitialToken()` before any bind; token admin after `installAdminEndpoints` | `HomeSynapseCore` +2 calls at the cited sites; the "AB-1 … BEFORE binding any socket" comment sits directly above | ✓ |
| Helper: no-arg byte-identical; `install -o homesynapse -g homesynapse -m 0600 /dev/null` + `printf >>`; consumption asserted; `rm -f` of the artifact in the systemd+rotate branch only; `runuser`/`sudo -u` for `status`; the launcher path | `print_token()` = the HEAD body verbatim incl. line 71 ("then delete the file: sudo rm …" — see H-1b); `queue_request`/`apply_request` as described; `HS_LAUNCHER=/opt/homesynapse/bin/homesynapse` = the unit's `ExecStart` | ✓ |
| Audit line key-ids-only | `auditLine()` = `token admin: actor= verb= target=`; pinned with no-name/no-43-char/no-64-hex assertions | ✓ |
| app MODULE_CONTEXT: "the JVM reserves the launcher's `-Xms512m -Xmx1536m`" | `common.sh:87` `HS_JVM_FLAGS` is baked into the generated launcher by `build-image.sh` §3 (`${HS_JVM_FLAGS}` inside the heredoc) — TRUE | ✓ |
| rest-api MODULE_CONTEXT: "`OpaqueTokenStoreTest` 7 → 19" | The diff adds **14** `@Test` methods → **21** (the return's §3 says 21 — the MODULE_CONTEXT line was written before the two fleet pins landed) | ✗ → corrected (§2) |
| Gates: targeted + Spotless + full `check` GREEN ×2 (Windows); 3 POSIX pins SKIP there | Accepted as the lane's gate. **The three POSIX pins have never executed anywhere** — their first run is CI (§4) | ✓ / CI-risk row |

## §2 The hub's one byte

**D-C (applied in place, via the bridge, before the commit):** `api/rest-api/MODULE_CONTEXT.md:269` — `7 → 19 (… request file ×5 …)` → `7 → 21 (… request file ×6 — two POSIX/non-root-gated, one the cross-platform delete-BEFORE-execute pin — · the mint scope precondition · …)`, marked "hub count-correction at intake". md5 after: `96814cef28439ade625e07281946e87b`; the file stays 1 M (+27/−0). Nothing else in the 16 was touched by the hub.

## §3 What the return does not say (the hypercritical layer)

**H-1 — the packaged probe's artifact dependence is an AVAILABILITY class, now operator-reachable by three verbs.** `homesynapse.service` is `Type=exec`, `ExecStartPost=health-probe.sh --wait --timeout 90`, `Restart=on-failure`, `RestartSec=10`, **`StartLimitBurst=5 / StartLimitIntervalSec=300`**. The probe authenticates with `config/initial_api_token`, read ONCE at `:87`. Consequences at source, each ending in a start-limited (DOWN) unit after 5 failed starts: (a) `revoke` of the artifact's key (CAUTION text only; no guard); (b) **deleting the artifact — which `postinst:74`, `install.sh:98` AND the helper's own no-arg output (line 71, byte-identical by the instruction's pin) still ADVISE** — the probe's file-absent arm waits out 90 s then fails; (c) a `rotate` whose restart fails for any reason after the helper's `rm -f` — the artifact is absent until a rotation succeeds (recovery: `mint`). The coder's F1 mitigation (remove the artifact before a `rotate` restart so the probe can never present a stale token) is **sound and deterministic for the happy path — ACCEPTED as transitional** — but it is a workaround layered on a design flaw, and (a)/(b) stay live. **Root fix = escalation E3** (the probe already supports `--health-path` for an unauthenticated endpoint, `:48–:53`): ruled in §5 as the next Core WU after R-7.

**H-2 — the doc's "single-restart batch" one-liner suffers F1.** `token-rotation.md` §probe-caveat offers `printf 'mint ops\nrevoke <oldKey>\n' > …/token_ops.request && … systemctl restart` as the single-restart form. The probe caches the PRE-batch artifact token (= `<oldKey>`) at exec; the batch mints (artifact rewritten) then revokes it; the probe's first connect → 401/403 → exit 3 → one failed start; `Restart=` brings the service back with the new artifact. Works after one failure — the doc presents it as clean. Not edited now (E3 retires the section); recorded.

**H-3 — citations/figures in the coder's records:** `RecordingEndpointContext` ":378–:380" (a 107-line file; `:32`/`:100`); `+942/−37` (final `+1067/−38`); the A-file sizes `313/316/≈190/≈155/160` (final 335/324/191/156/181 lines). Claims true, numbers pre-fleet. Recorded, not edited (coder-owned records of what the coder saw).

**H-4 — cosmetic:** the coder-handoff entry carries a literal newline inside "`$(printf '\n')`" (a lazy-continuation line in the blockquote). Left as is.

**H-5 — the hub's own mechanics (disclosed):** the first `device_bash` porcelain (status + `diff --numstat` in one call) was killed at the bridge's 45 s ceiling and left `homesynapse-core/.git/index.lock` (0 B, the VM user, 11:34:04Z). Cleared by `mv` to `_scratch/_to_delete/core-index.lock_stale_2026-08-22T113404Z_hub-device-bash-timeout` (delete-nothing); no git process was alive. Harvest H14 (§6).

**H-6 — the `token status` JVM on the packaged host:** the helper launches a SECOND JVM as the service user with the launcher's locked flags (`-Xms512m -Xmx1536m …`, committed lazily) beside the running service. Acceptable on the Pi 4/5 class; the store's ctor logs nothing on a clean load, so stdout carries only the table + trailer — **§OP-A observation row added:** the output has no log lines.

## §4 CI predictions — filed BEFORE the push (H12; law 16 banks whatever lands)

| Run | Trigger | Prediction |
|---|---|---|
| `ci.yml` Build & Check | push to main | **GREEN**, ~3 min. `:api:rest-api:test` **130 / 0 skipped / 0 failed** (Linux, non-root `runner`: the three POSIX pins EXECUTE for the first time anywhere — `operatorRequestUndeletableFileExecutesNothing` via `r-x------` on the @TempDir, `operatorRequestUnreadableFileExecutesNothing` via `---------` on the request file, `storeAndArtifactAreOwnerOnlyOnPosix` asserting exact `rw-------` on both files under umask 022). `:app:homesynapse-app:test` 24 / 0 / 0. lifecycle 60. |
| `install-smoke.yml` | paths `api/**`, `app/**`, `lifecycle/**`, `distribution/**` all touched → RUNS | **GREEN**; the **18 `[smoke] PASS` lines byte-identical** to the 33861ad run (check 5 asserts `-s`, owner `homesynapse`, config-dir mode `*0|*00` — the now-0600 artifact passes; no check reads a problem content-type; the helper is not `.sh` so the static lint does not touch it); `distribution-artifacts` uploaded; update-smoke GREEN. |
| Frontend CI | `web-ui/**` only | **NOT triggered**. |

**The only plausible RED:** the three POSIX pins. If RED: adjudicate-first at the job log (the exact mode strings / the exception class) — no re-run, no edit until the cause is named at primary text.

## §5 Rulings (hub; Nick's words where marked)

1. **R-6/R-8 → LANDING.** Commit + push now; CI = the gate of record; **WU CLOSES at §OP-A** (the bench rotation through the NEW path is the live-wire proof of the boot-time consumption — no lifecycle test covers a present request file, H8).
2. **The F1 mitigation (the helper's `rm -f`) — ACCEPTED as TRANSITIONAL**, to be removed by E3.
3. **INTERIM OPERATOR LAW (binds every packaged host until E3 lands; Nick is the only operator):** never `revoke` the key the artifact carries; never delete `config/initial_api_token`; mutate tokens only through `homesynapse-token rotate|mint|revoke`; after any helper verb, `systemctl is-active homesynapse` is the glance.
4. **E3-HEALTH = the next Core WU after R-7 (hub-authored; working id R-9/E3-HEALTH).** Scope: an unauthenticated readiness route (`/health` → 200 when the projection is LIVE, 503 otherwise, body `{"status":"ready"|"starting"}` only — no data, no version), the filter exemption (**R-H1, Nick's word: LOOPBACK-ONLY (rec) vs ANY-SOURCE** — the probe is loopback; loopback-only costs one `ctx.ip()` check and keeps INV-SE-02 visibly intact), the unit's `--health-path /health`, the helper's `rm -f` REMOVED, the three banner lines restored to "the artifact may be deleted after pairing", `token-rotation.md` §probe-caveat retired, run-smoke check "+1": unauthenticated `/health` = 200 AND `/api/v1/entities` unauthenticated stays 401 (the fence proof in the same breath), the lifecycle e2e pins (the return's §7 item 3) as a rider. **R-H2 (rec IN):** the store refuses to revoke the LAST active full-access token unless the verb is `rotate` — 409 at HTTP, a `skipped` entry at the request file — the self-lockout class (`DELETE /internal/tokens/{own}` on the only key today = every client out + the next restart start-limited; recoverable only by a root `mint`).
5. **R-7 dispatches NOW, on the new baseline** (the R-7 census trees are byte-identical between 33861ad and the R-6/R-8 commit; the only distribution files this WU changed — `deb/homesynapse-token`, `docs/token-rotation.md` — are outside R-7's census → report-and-proceed at P1, the disclosure pattern this lane used).
6. **R-3b may carry an OPTIONAL tail block** — `homesynapse-token rotate` on the held card after the R-3 predictions are banked (a service restart with a cloned coordinator is a resume, not a form — P-d holds) — decided at the R-3 finalization, not now.
7. **Doc 09 §12.1 currency** (the `api-key create|list|revoke` sketch vs the shipped `token status` + helper verbs) + **the skills `java-patterns §11` wording** ("plus app's own test classes" contradicts `HomeSynapseArchRules.java:98–:103`) → R-10 docket + the next skills touch. The helper's `100644` mode: leave (packaging chmods 0755).

## §6 Harvest

- **H14 (hub mechanics):** a bridge-killed git process leaves `index.lock`; the hub checks for and clears its OWN stale locks (mv, never rm) before any order, and splits porcelain reads (`-uno` + a scoped `--untracked-files=all -- <dirs>`) to stay under the 45 s ceiling.
- **Walk a credential consumer's TIMING, not only its existence** (the coder's lesson, adopted as a hub authoring rule): every instruction that adds a rotate/revoke-class verb lists each consumer of the credential AND when it reads — probes, sidecars, crons, watchers.
- **A byte-identity pin can pin a defect:** the instruction pinned the helper's no-arg output byte-identical for regression safety and thereby pinned line 71's harmful advice; future pins say "byte-identical EXCEPT the lines this WU is allowed to change".
- **A dispatch label is not the lane:** the porcelain decides which WU ran; the hub verifies the census before believing the label.
