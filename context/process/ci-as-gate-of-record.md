<!--
file: context/process/ci-as-gate-of-record.md
purpose: The CI-as-gate-of-record policy (V1 record D5a) — CONFIRMED live on the core remote; the push→gate→adjudicate model that converts the hub/Nick from per-WU gate-runner to failure-adjudicator (the parallel-lane multiplier's mitigation); the Coder pre-handoff self-step; the extension plan to the new lanes.
audience: the hub, Nick, the Coder, the frontend-dev + Distribution lanes
state-type: process / policy
status: CONFIRMED 2026-06-21 (v3 hub) — core CI live + verified at source.
-->

# CI as the Gate of Record (confirmed 2026-06-21)

## Confirmed live (core)
`homesynapse-core/.github/workflows/ci.yml` exists and is live on the remote `github.com/nexsys-io/homesynapse-core`:
- **Triggers:** `push` + `pull_request`.
- **Job:** `Build & Check` on `ubuntu-latest`, JDK 21 (Corretto), **`./gradlew check --no-daemon`**, uploads test reports as an artifact.
- This is the **full gate** (compile + spotless + ArchUnit + moduleGraphAssert + all count pins + serde) — the same 149-task gate Nick has been running by hand.

docs + hivemind repos have no CI (correct — not buildable Java).

## The model — push → gate → adjudicate (D5a)
The parallel-lane plan triples demand on the one node that reviews/ratifies/runs gates (Nick + the hub). CI is the mitigation: it converts that node from **gate-runner** to **failure-adjudicator**.
1. A lane pushes its branch.
2. CI runs `check` (Core) / the lane's gate (Web-UI, Distribution).
3. The hub **adjudicates from the CI report** — it does NOT run gradlew per-WU. A fresh hub re-grounds from the spine + the CI status, not from a local build.
4. On GREEN → WUCP Phase 2 closeout. On RED → the hub reads the failing task/test and routes a fix to the lane.

**This supersedes the per-WU "Nick runs the deferred gate locally" loop as the default** — the deferred-gate discipline remains the fallback when CI is unavailable, and Nick still owns the merge/commit decision. The Coder still hands back **fix-applied / NOT gate-verified**; CI is now what verifies, in place of a manual local run.

## The Coder pre-handoff self-step (shift-left, P5) — ADD the spotless step
The M7.2a-1 gate bounced on a **spotless unused-import** that the Coder's LLM "compile-clean" pass missed. Standing addition to every coding instruction's Build Discipline (now in the M7.2a-2 instruction):
- When the sandbox can run Gradle, run a targeted `./gradlew :module:compileJava` on each touched `-Werror`-sensitive module **AND** `./gradlew :module:spotlessApply` (or `spotlessCheck`) before handoff. ~20s; converts the unused-import / `[exports]` / redundant-cast class of misses from a CI round-trip into an in-session fix. The full `check` stays CI's job.

## Extension plan to the new lanes (when they stand up)
The core `ci.yml` is the template. Add, per lane:
- **Web-UI (`homesynapse-core/web-ui/` or its own repo):** a job running the frontend toolchain's lint + typecheck + unit tests + production build (fail the gate on any). Add a contract-check step that the dashboard read-API client matches the frozen contract (`2026-06-21_dashboard-read-API-contract-freeze.md`) — a mock/schema check so a drift surfaces in CI, not at integration.
- **Distribution (devops workspace):** a job that builds the jlink image + assembles the `.deb`/install-script and runs an **install-smoke** (the artifact boots as a systemd service and answers a loopback health probe). Keep it fast; the full on-device 72h run is the validation lane, not CI.
- **Cross-lane contract guard:** when the Core lane changes an A-class read shape, CI on the Web-UI lane should fail the contract-check — making a silent cross-lane break loud (the §D change-discipline of the contract freeze, enforced).

## Open item for Nick (non-blocking)
Confirm CI is **green on the current HEAD** (`1541446`, M7.2a-1) on the remote — the spine records M7.2a-1 as gate-verified GREEN (149 tasks); a glance at the Actions tab closes the loop between "Nick ran it locally" and "CI records it." Going forward, the M7.2a-2 branch's CI run is the gate of record for that WU.
