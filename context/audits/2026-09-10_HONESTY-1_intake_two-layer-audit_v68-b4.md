<!--
file: context/audits/2026-09-10_HONESTY-1_intake_two-layer-audit_v68-b4.md
purpose: The hub's two-layer intake audit of the HONESTY-1 return (four value corrections on Core: lastReported seeds null · command-event provenance inherited / UNKNOWN · the commandEventId javadoc · install-smoke's push paths filter) — the claims read critically, then the hub's own re-executions at the bytes; R1 ruled and APPLIED; O2 docketed instrument-first; the landing card handed.
audience: the hub · Nick (§3 the ruling; the card is in the brief §NEXT)
state-type: intake audit (FILED)
status: FILED v68 beat 4 (Thu 2026-09-10 ~18:4x CT; instrument 2026-09-10T23:33Z). Return: context/audits/2026-09-10_HONESTY-1_return.md (9,816 B; RETURNED line in the file and printed). Verdict: ACCEPT — R1 applied by the hub's guarded splice (census 13 → 14 M); the landing is Nick's card; CI + install-smoke on the push = the gate of record and the sample.
-->

# HONESTY-1 — intake audit (two layers)

## §0 Verdict: ACCEPT
The return does what the instruction ordered, in the order it ordered it, and says plainly what it could not prove. Red-first held on a value, not a compile: A-#4b `expected: null but was: 2025-09-15T08:30:00Z`; T-B1/T-B2 `expected: USER_COMMAND but was: AUTOMATION`; T-B3 `expected: UNKNOWN but was: AUTOMATION`; A-ser and T-B4 disclosed green-by-construction. After Parts A–D every suite is green and no pre-existing test moved: state-store 164 → 165 · automation 207 → 211 · persistence 412 → 413. One `[REVIEW]`, ruled §3. Nothing STOP-grade.

## §1 Layer 1 — the claims, read critically
The §0 card leads with the census (13 M + 0 A + 0 D, zero staged, zero commits), the red-first table with the observed failure strings, the deviations by tag, and the gate line — the shape the instruction asked for. The one prediction it refutes (P1: 12 M) it refutes honestly: the YAML row names two files (`.github/workflows/install-smoke.yml` + `distribution/ci/install-smoke.yml`, kept byte-identical). The lane did not touch `EntityState.java` because the Files table did not list it — the table governs; it filed the fix as R1 instead of silently widening the census, which is the discipline we want. Two observations are hub-grade and are ruled below (O2 the `projectionVersion` question; O5 the threading shape). The `RETURNED` line is the file's last line AND was printed — the W-SKILLS-9 template sentence already obeyed.

## §2 Layer 2 — the hub's re-executions at the bytes (2026-09-10T23:33Z)
1. **Census at porcelain — VERIFIED:** `git --no-optional-locks status --porcelain` in core = exactly the 13 ` M` paths the card lists; `??` 0; `web-ui/` 0 (the FE lane had not written yet); HEAD `39c8dd3`; hivemind porcelain = ` M coder-handoff.md` + `?? 2026-09-10_HONESTY-1_return.md`.
2. **The return file — VERIFIED:** 9,816 B at the named path; last line `RETURNED context/audits/2026-09-10_HONESTY-1_return.md 9816`.
3. **Part A at the diff — VERIFIED:** `StateProjection.initialEntityState` now seeds `seed, seed, null, null, false` (lastChanged · lastUpdated · **lastReported null** · staleAfter · stale) with the javadoc re-cut to say so; the `applyToState` comment names the corrected §1.5.
4. **Part B at the diff — VERIFIED:** `StandardCommandDispatchService`: `publish(...)` takes `(…, cause, origin, actorRef)` and writes `origin` / `actorRef` into the envelope where `EventOrigin.AUTOMATION, null` was hard-coded; the subscriber path passes `event.origin(), event.actorRef()`; the in-process primitive passes `EventOrigin.UNKNOWN, null`; `publishDispatched` / `publishResult` thread both through; `+import Ulid`.
5. **Part C at the diff — VERIFIED:** `CommandEnvelope.commandEventId` javadoc now says the originating `command_issued` id (the supervisor passes the `command_dispatched` envelope's causation id, Doc 07 §3.11.2).
6. **Part D at the diff — VERIFIED:** the `push:` block lost its `paths:` line in `.github/workflows/install-smoke.yml`; `diff` of the two copies is empty (pair identical); `on.push` = `branches: [main, develop]` alone; `pull_request` keeps its paths; `workflow_dispatch` stays.
7. **The test evidence — VERIFIED at the XML:** `build/test-results/test/*.xml` newest 23:06:28 / :29 / :37Z (three minutes after the red run's 23:03Z stamps); testcases 165 / 211 / 413; failures 0 / 0 / 0.
8. **R1 at source — VERIFIED and APPLIED:** `EntityState.java:73–:74` read `@param lastReported … never {@code null}`; the hub re-cut it by a guarded splice (line-anchored, the file's own line ending preserved, no line over 100 chars) to `… or {@code null} until the entity's first {@code state_reported} (AMD-53 §1.5 as corrected 2026-09-07; HONESTY-1)`. Core porcelain is now **14 M**.
**NOT re-executed (disclosed):** the Gradle run itself (the VM has no toolchain; the XMLs and class mtimes are the coder's run, read by the hub); the `-Werror` compile freshness (the log's `> Task … compileJava` lines are the claim); `spotlessCheck` on the R1 javadoc (a 2-line wrap in the file's own style — CI is the gate; a red there is a one-line fix, never a re-run of the WU).

## §3 Rulings
- **R1 — APPLIED** (above). The alternative — land a commit named "honesty" with a javadoc that lies — was rejected on its face.
- **O2 — the `projectionVersion` bump — DOCKETED as LASTREPORTED-1b, instrument-first (arc 28), NOT ordered:** a checkpoint written before this landing keeps the adoption-instant `lastReported` on never-reported entities until they report or the next version-transition rebuild. Whether the fleet's entities are healed by R-4c's re-adoption or need a 5 → 6 bump is a question the wire answers: **H8-a / R-4c read `lastReported` on the card for one never-reported entity after the `.deb` is installed.** If the adoption stamp persists, the bump is a one-literal WU; if re-adoption heals it, no WU. No theory before the read.
- **O5 — two parameters, not a `Provenance` record — STANDS.** "No new types" is a contract line; a nested record is a class file. Mechanical to flip later if a third provenance field ever appears.
- **I3 — G4's grep hits on `SqliteEventStore:467/:532`** are column writes, not a reader filtering by origin — the gate's intent holds; recorded so the next instruction's G4 says "readers", not "any use".
- **P4 (install-smoke runs on the push without a manual dispatch)** banks on Nick's push as one spine line; **Act 12 retires on that line.**
- **The deferred gate:** the full `./gradlew check` is CI's on the push (Open Risks row added this beat; closes when `ci` is green on the landed sha).

## §4 The landing (Nick's hands; the card is the brief's §NEXT)
Scoped `git add` of the 14 paths by name (the FE lane may have `web-ui/` on porcelain by then — it is NOT part of this landing); the msg file `_scratch/2026-09-10_core_HONESTY-1_commit-msg.txt` (no trailers on Nick's commits); push; the report-back is one line: `HONESTY-1: <sha> · ci <green | red: FAILED line> · install-smoke <ran green | ran red: line | did not run>`. The hivemind side (the return + the handoff entry + this audit) is hub-run in this beat's commit.

## §5 Definition of done (this WU)
- [x] The return exists at the named path; audited two-layer; this audit filed.
- [x] The core msg file + the census card handed (14 paths); the CI wait-state recorded in §HELD.
- [x] MODULE_CONTEXT updated by the lane (state-store · automation · integration-api — in the 14).
- [x] The deferred gate logged under Open Risks (closes on CI green).
- [ ] CI green + install-smoke ran on the push (Nick's line) → Act 12 retires; the EXPLAIN v1.1.4 instruction dispatches on it.
