<!--
file: context/instructions/2026-07-28_B2_suite-port-and-rebind_bench-instruction.md
purpose: THE B2 INSTRUCTION — the §5.1 suite port onto the DEPLOYED `c09c61c` + THE ENGINE REBIND (rider #1, MANDATED FIRST) + the three-flip constants re-mint + the WCAP-residual riders. Bench lane (nexsys-bench repo); hub-authored at v40 beat 1; two halves: a DESK half (engine + scenarios + fixtures, Coder/host-CC) and a PI half (uhubctl prep + the re-mint completion + the suite runs, operator per playbook §8).
audience: the Coder (desk half); Nick as operator (Pi half); the hub (two-layer audit + intake).
state-type: coding/bench instruction (ISSUE-READY).
status: AUTHORED 2026-07-28 (v40 hub, beat 1). Baselines: bench `9f2b5ad` (tree clean at authoring) · core DEPLOYED ON THE PI = `c09c61c` (the 2026-07-27 deploy evening; CMD-API + SKIP-VIS + DASH-SERVE all aboard) · fleet 6/6 @ watermark 25065 · ch20/0x774c.
returns: THE RETURN FILES TO `context/audits/` (never handoff/) — name it `2026-07-XX_B2_suite-port_return.md`. State this in the return's own frontmatter.
laws-held: L1 every-hop (every line-number below RE-ENUMERATED at source 2026-07-28; every live-behavior premise cites its filed measurement or is EXPLICITLY a measurement act — format #19) · L2 copy-paste-complete (every placeholder carries its own FILL-IN-BEFORE-RUNNING line) · L3 token-paste poison (the API token appears in NO paste, NO capture, NO return — always `$(bench.sh api_token)` inline) · lock-free porcelain = `git -C <repo> --no-optional-locks status --porcelain` (SPELL THE FLAG — the skills-pass lane's §4b mechanism finding, adopted) · fixture-paired asserts (doctrine §3) · API-first (charter §5 — raw SQLite is human debug, never a scenario assert) · anti-vacuous · NO attribution trailers on any commit message.
launch-precondition: ⚠ Nick's skills-mirror sync must have run before the Coder (host-CC) session launches (Check 9 — the skills-pass edits are on disk, commits + sync pending at authoring). The Pi half needs no skills.
-->

# B2 — the §5.1 suite port + THE ENGINE REBIND (bench lane; lands against the deployed `c09c61c`)

## §0 — Context: why B2, why now

The evidence engine's suite has been waiting on the command write plane. CMD-API landed `5b4797e` and is **deployed and serving on the Pi inside `c09c61c`** (2026-07-27 deploy evening, three `[PASS]` floors). Every SKIPPED-honest stub minted since the 2026-07-12 "(c)+(a)" ruling can now flip live. The gate needs this: **C2 [M] and C3 [M] close only through "ported into the suite and green on the deployed build"; H2 [M] closes only through the ported AUTO suite green.** C1 [M] needs ~200 recorded verdicts (~25 banked; ~13/day) — **B3 nightly is the accumulation engine and it authors immediately behind B2; the Jul-31 suites-running trigger governs: if suites are not running by EOD 2026-07-31, escalate to Nick with the named slide cost — scope moves, never the gate.**

**Priority inside the WU is absolute: rider #1 (the engine rebind) lands and proves BEFORE any AUTO leg runs on the Pi. B3 GATES on the rebind.** The instrument must be sound before the corpus compounds on it.

## §1 — Scope

**IN (desk half, bench repo):**
1. **RIDER #1 — THE ENGINE REBIND** (§2; Nick-directed, v37 beat 3 "take this one regardless"; MANDATED FIRST).
2. Rider #2 — the `pending_positive_tokens()` display fix (§3.1; I3b §5.5).
3. Rider #3 — the scenario goal-string de-hardcode (§3.2; I3b §5.6).
4. Rider #4 — RUNNER-VERSION-BANNER (§3.3; **ruled IN at this authoring** — doctrine §3 instrument self-identification; B2 is the engine-touching WU, the banner rides it).
5. The runner-demo fixture-pair extension for the rebind (§2.4).
6. The constants re-mint, DESK STAGE (§4.1): `command-api` → `available: true` + the lifecycle wire-path re-pin at rest-api source; the NEW `hue-online` capability minted `false`.
7. The stub flip + the new command scenarios (§5): `command-confirm` gains the `hue-online` gate; NEW `command-confirm-s31` · `command-timeout-absent` · `command-supersession` · `command-identify-honest`.
8. The AUTO-suite list definition for H2/B3 (§7.3).

**IN (Pi half, operator):** uhubctl install; the constants re-mint PI STAGE (`usb-power` flip from uhubctl's OWN read + fleet re-verification at the live boot log); the two 30-second WCAP-residual riders; the measure-then-pin probes (§5.4–§5.5); the suite runs + bundles.

**OUT (named owners — never silent):** B3 nightly (the NEXT bench WU; authors behind this one; gates on rider #1) · the charter-§2 remaining acceptance ports (restart-identity [NQ-6 shape] · IAS-twin absorption · restore-path — deferred to B2b/B3 nights, non-gate: C2/C3/H2's ported-legs language is satisfied by §5's set) · STATE-DIALECT (core P2, separate WU) · anything core-side or FE-side · any step toward an operator-facing product CLI (the charter §5 hsctl STOP — if the work drifts that way, STOP and route to the hub).

## §2 — RIDER #1: THE ENGINE REBIND (`eval_new_run_after` binds `trigger.matchedAt`)

### 2.1 The defect and the ruling (evidence, all filed)

`runs[].triggeredAt` is understated by exactly `durationMs` on the frozen read surface (RUNS-TRIGGEREDAT, I3b §4 — field-measured twice, microsecond-exact; `matchedAt` is the externally-corroborated true instant, I3b §4.2). The SKIP-VIS core fix (DP-3) landed `da11f46` and is DEPLOYED in `c09c61c`, so live `triggeredAt ≡ trigger.matchedAt` wherever eventTime is present — **agreement is health; divergence is a NEW finding.** Nick's ruling (v37 beat 3): the engine binds **`matchedAt`** regardless — the instrument must be sound against ANY deployed build, past or future.

### 2.2 The current code (RE-ENUMERATED at source 2026-07-28; bench `9f2b5ad`)

`tools/runner/engine.py` — `eval_new_run_after` at **:919–:984**. The premise holds at today's source exactly as v37 verified it: the `triggered < m_observed` discard (`:951–:958`) `continue`s **before** the per-run causal-chain fetch (`:959`). The ok-payload (`:975–:977`) is `{runId, triggeredAt, mObserved, anchor, outcomes}`. The scenario note line printing `triggeredAt >= M_observed` is at **:859–:861**. `parse_iso_utc` (`:1186–`) already documents under-count-never-false-PASS on unparseable timestamps — that posture is PRESERVED.

### 2.3 The rebind (fetch-first; every arm preserved on the new field)

For each run in `new` (the snapshot-diff set — snapshot semantics UNCHANGED):

1. **Fetch the causal chain FIRST** (`/api/v1/runs/{runId}/causal-chain`). `status != 200` ⇒ `ignored.append("<id>: causal-chain read HTTP <s>")` — ignored-with-reason, never vacuous.
2. **Bind `data.trigger.matchedAt`.** Trigger view absent or `matchedAt` missing ⇒ ignored-with-reason (`"<id>: trigger view absent — cannot bind matchedAt"`). Unparseable `matchedAt` ⇒ ignored-with-reason. **NEVER fall back to `triggeredAt` silently** — a fallback would resurrect the dead zone the rebind kills.
3. **The anti-false-PASS arm PRESERVED, on `matchedAt`:** `matched < m_observed` ⇒ ignored-with-reason ("predates M_observed") — a pre-anchor run never satisfies, even materializing late into the window.
4. Executed-chain arm unchanged (≥1 action with an outcome; outcome-agnostic — REV2's contract).
5. **The ok-payload carries BOTH fields:** `{runId, matchedAt, triggeredAt, mObserved, anchor, outcomes, agree: <bool>}` where `agree` = the two instants match to the second. Update the `:859–:861` note line to quote `matchedAt` (and print `triggeredAt` beside it). **Divergence does NOT fail the assert — it prints as its own `[INFO]` finding line** (the free diagnostic: |matchedAt − triggeredAt| ≈ durationMs is the old defect's live signature).
6. Anchor-unmatched refusal (`:930–:934`) and no-snapshot pending (`:935–:938`) — byte-preserved.

**Docstring:** rewrite to name the rebind + the I3b §4 finding + the both-fields law. **Lint (`:228–:251`) unchanged.**

### 2.4 Fixture pairs (doctrine §3; predictions per format #18)

Extend `fixtures/runner-demo/` (the desk gate — run the demo suite before and after):

| Fixture | Prediction at the rebound engine |
|---|---|
| `synthetic-liveness-pass.api.yaml` — add `trigger.matchedAt` ≥ M to its chain | **PASS** (the pair's green half) |
| `synthetic-liveness-pre-reopen-run.api.yaml` — `matchedAt` < M | **ignored-with-reason → no-new-run FAIL** (the matchedAt<M_observed mutant-killer: a mutant deleting the arm flips this fixture's verdict) |
| NEW `synthetic-liveness-missing-trigger-view.api.yaml` — populated chain, NO `trigger` object | **ignored-with-reason → FAIL, reason quoted** (kills a silent-fallback mutant) |
| `synthetic-liveness-empty-chain` / `no-new-run` / `snapshot-member` | behavior-preserved — **disclosed green-by-construction against the rebind** (their asserts never reach the matchedAt bind; format #18: predict green, disclose, do not claim them as reds) |

**Red-first order:** write/adjust fixtures first; the pre-rebind engine must FAIL the `missing-trigger-view` fixture *for the wrong reason* (it passes on `triggeredAt` — quote that as the red evidence that the rebind changes behavior), then the rebound engine must produce the predicted table above.

### 2.5 The ordering law

**The rebind + its fixture table land and are demo-suite-proven BEFORE the Pi half runs any AUTO leg. B3 gates on this rider.** State compliance explicitly in the return.

## §3 — Riders 2–4

**3.1 `pending_positive_tokens()` (`:736–:747` — re-enumerated; the I3b §5.5 mechanism confirmed at source).** The function tests display strings against `self.satisfied_at_index`, which is keyed by individual RESOLVED log tokens — so `log_any` joins (`"A OR B"`), `api:`-prefixed lines, and even unresolved plain tokens can never filter. Fix: resolve per-token; a `log_any` line filters when ANY of its resolved tokens is satisfied; an `api` line filters when its own evidence line has been satisfied (track satisfaction per evidence-line index, not by string). DONE-WHEN must list only genuinely outstanding conditions — §8's whole point. Verdict-neutral; still fixture-check via a demo run's printed operator block quoted in the return.

**3.2 The goal string (`usb-reenumeration-manual.yaml:74` — re-enumerated; still reads `"…(direct-attached topology)"`).** The file has closed BOTH topology legs (I3b §5.6). De-hardcode to topology-neutral: `"Prove honest detection + autonomous reopen on a physical re-seat"`. One line; nothing else in the file moves (the 90 s within and the `after:` gate are adjudicated law — v31 lengthen-only).

**3.3 RUNNER-VERSION-BANNER (ruled IN).** The runner self-identifies at every `scenario`/`suite` invocation start: print `runner <ENGINE_VERSION> @ <bench-repo short SHA if resolvable, else "no-git">` before the first verdict line. Add a module-level `ENGINE_VERSION = "B2-2026-07-28-rebind"` to `engine.py`, bumped at every engine-touching WU henceforth (doctrine §3: deploy-state is re-derived AT the instrument — the 2026-07-18 stale-instrument hour is the price of assuming). Resolve the SHA lock-free (`git --no-optional-locks -C <dir> rev-parse --short HEAD`, tolerate failure silently).

## §4 — The constants re-mint (`scenarios/constants.yaml`; two stages, three flips)

### 4.1 DESK stage (Coder)

1. **`capabilities.command-api.available: false → true`.** Replace `reason` with the source citation: CMD-API landed `5b4797e`, deployed on the Pi in `c09c61c` 2026-07-27. **Wire truth verified by the hub and RE-PINNED by you at rest-api source before the flip commits** (enumerate-at-source): the command endpoints hand-build **camelCase `{data,meta}`**, phases are **UPPERCASE**, and the PROVISIONAL guesses **HOLD**: `terminal-field: "data.terminal"` · `phase-field: "data.currentPhase"`. Read the actual endpoint + submission types in `homesynapse-core` `api/rest-api` at `c09c61c` (the POST `/api/v1/entities/{entityId}/commands` + GET `/api/v1/commands/{commandId}` families) and quote file:line for each of: the `data.commandId` capture path, `data.terminal`, `data.currentPhase`, and the phase vocabulary — in the return. If ANY differs from the constants block, the re-pin edits the CONSTANTS (never the scenario asserts' semantics) and the delta is a named finding.
2. **Mint `capabilities.hue-online: {available: false, reason: "HUE-RESET pending — the Hue is physically off-network (standing note 2026-07-21; I3b §5.1)"}`.** This is what keeps the original `command-confirm` SKIPPED-honest instead of false-FAILING against an absent lamp (§5.1 below).
3. `usb.*` stays PLACEHOLDER at desk — the Pi stage owns it (constants law: minted from `uhubctl`'s OWN output, never from a report).

### 4.2 PI stage (operator, session prep — before any suite run)

Paste-blocks below are self-contained; each states WHERE it runs. ⏺ = record the output either way.

**Block P-1 (Pi): uhubctl install** (I3b §5.7: absent at last check)
```
sudo apt-get install -y uhubctl
uhubctl
```
⏺ the full `uhubctl` output. **The `usb.hub-location` + `usb.port` mint comes from THIS output and nothing else.** The I3b §5.8 CANDIDATES (`hub-location "3-2.4"`, `port 2` — physical port 5 = logical `3-2.4.2`) are PREDICTIONS to check against, never values to copy. If the read disagrees with the candidates, the read wins and the disagreement is a ⏺ finding.

**Block P-2 (Pi): the fleet re-verification** (constants charter: re-read AT the instrument)
```
bench.sh status
grep -E "projection_live|network_resumed|network_formed" ~/hs-bench/current.log | tail -5
```
⏺ the positions/channel/panId lines. Expected: 6/6, position ≥ 25065, ch20/0x774c. The re-mint stamp records these as the 2026-07-28 re-mint-of-record values (watermark = the projection_live replay-head, NEVER viewPosition).

**Block P-3 (Pi): WCAP residual rider A — the why-not VALID-id capture** (~30 s; closes the WCAP-1 residual)
```
curl -s -H "Authorization: Bearer $(bench.sh api_token)" http://127.0.0.1:7070/api/v1/automations | head -40
```
⏺ the bench-hero row's CURRENT `id`. Then — **FILL IN `<CURRENT_ID>` from the output above BEFORE running; do not paste this line with the placeholder still in it:**
```
curl -s -o /dev/null -w "%{http_code} %{time_total}s\n" -H "Authorization: Bearer $(bench.sh api_token)" http://127.0.0.1:7070/api/v1/automations/<CURRENT_ID>/why-not
```
⏺ status + latency. Prediction: **200, milliseconds-class** (the endpoint proven healthy at 404-in-6ms on a stale id — WCAP; this banks the valid-id half).

**Block P-4 (Pi): WCAP residual rider B — the rotation-confirm double-read** (~30 s; upgrades AUTO-IDENT's evidence from near-proven to proven)
```
bench.sh restart
curl -s -H "Authorization: Bearer $(bench.sh api_token)" http://127.0.0.1:7070/api/v1/automations | head -40
```
⏺ the bench-hero `id` again. Prediction: **the ULID CHANGED across the restart** (identity rotates every boot — the WCAP mechanism). Same = a NEW finding (rotation inference falsified; ⏺ and continue — verdict-neutral for B2).

## §5 — The stub flip + the command scenario set

**The authoring hazard this section exists to avoid:** flipping `command-api` alone would send `command-confirm` (brightness-CONFIRMED against the Hue) into a guaranteed false-FAIL — the Hue is off-network (HUE-RESET pending). The set below makes every scenario's premise match the fleet's MEASURED reality, and it deliberately converts the Hue's absence into gate evidence (the C2 device-absent class).

**Shared mechanics (all AUTO tier; all API-first; all `bundle: always`):** stimulus/asserts use only existing SCENARIO_FORMAT mechanics (api POST + `capture`, `let` + `other_of`, `phase_terminal`, `field_equals`, `within`). NO format growth. Every `within` prices the instrument's resolution: the tuned confirmation window is **15,000 ms**, so CONFIRMED-class asserts get `within: 20s` (decisive headroom above the window — the command-confirm precedent) and TIMED_OUT-class asserts get `within: 25s` (the window must EXPIRE before the terminal can exist — out-wait the instrument, doctrine §3).

### 5.1 `command-confirm` (existing stub — MODIFIED)
`requires: [command-api]` → `requires: [command-api, hue-online]`. Header gains one paragraph naming the gate (SKIPPED-honest until HUE-RESET; the scenario itself is already correct as authored). PROVISIONAL markers on the wire paths are REMOVED where §4.1's re-pin confirms them (cite the re-pin in the header).

### 5.2 NEW `command-confirm-s31` — the CONFIRMED-class leg on silicon that exists
Target: the S31 Lite switch `01KXW1W1SBJZERC9MBAMV2DWKE` (mains-powered, reachable). Shape: `let:` pre-read the switch state → command the OPPOSITE (`turn_on`/`turn_off` — **re-pin the command names + the state attribute field path at source at authoring**: the S31's capability mapping + the state read, quote file:line in the return) → `phase_terminal: CONFIRMED` within 20s → `field_equals` the commanded state within 20s. Add `command.s31-entity: "01KXW1W1SBJZERC9MBAMV2DWKE"` to constants (the command block grows a second target; the Hue row stands untouched).
**Honesty gate (format #19): the S31's confirm path is UNMEASURED** — the CONFIRMED class is proven on the Hue (acceptance record, brightness 0.33 s), never on the S31. **The Pi half runs a probe rep FIRST** (Block S-1, §7.1): one commanded toggle, ⏺ the full lifecycle read + the state read. The scenario's asserts bind only after the probe measures the path; if the probe times out (e.g. relay state not reported), that is a FINDING routed to the hub, and the scenario stays parked — never retuned blind.

### 5.3 NEW `command-timeout-absent` — the C2 device-absent class, scripted
Target: the Hue (constants `command.entity` — absent by measured fact, I3b §5.1: five commands, zero CONFIRMED). Shape: POST `set_brightness` (either level; no `let` needed — the target cannot confirm anything) → `phase_terminal: CONFIRMATION_TIMED_OUT` within 25s. `requires: [command-api]` ONLY (the absence IS the premise). Header: this scenario's premise dies at HUE-RESET — when `hue-online` flips true, re-point it at whatever device is then honestly absent or retire it to OPERATOR (unplug-driven); the note is the standing owner.
Prediction: TIMED_OUT, per I3b §5.1's five-for-five. A CONFIRMED here = **never-false-CONFIRMED broken = automatic STOP** (the C1 ruling's one-false-CONFIRM law — quote it in the header).

### 5.4 NEW `command-supersession` — the C3 supersession leg (MEASURE-THEN-PIN)
Shape: two rapid POSTs to the SAME attribute on the Hue (`set_brightness` 20 then 50, back-to-back stimulus acts) → the FIRST command's status read must show the superseded disposition; the SECOND times out honestly. **The superseded command's terminal wire shape via the DIRECT command read is UNMEASURED** (the banked C3 proof is event-record positions 589/593; §5.1's superseded evidence is chain-side `resultOutcome`). **Pi Block S-2 measures it** (§7.1): run the two POSTs by hand, ⏺ BOTH `GET /api/v1/commands/{id}` bodies in full; the desk pins the scenario assert to exactly what the wire serves (constants-side if a new field path is needed — a mint, not a guess). If the read surface cannot express supersession, that is the charter §5 rider verbatim: **a contract conversation brought to Nick — never a raw-SQLite fallback inside a scenario.**

### 5.5 NEW `command-identify-honest` — the C3 identify leg (MEASURE-THEN-PIN)
Target: the S31 (reachable, ACKs). Shape: POST `identify` → the honest non-CONFIRMED terminal with the measured reason class (`"DefaultResponse SUCCESS +90 ms, then no report, ever"` — the exact string class banked at I3b §5.1 and acceptance pos 644). Same measure-then-pin protocol (Pi Block S-3): ⏺ the full lifecycle read; pin the assert to the wire's actual terminal + wherever the reason surfaces on the API-first read. Never-CONFIRMED is the load-bearing assert; the reason quote is the evidence line.

### 5.6 `usb-reenumeration` (existing AUTO stub) — flips live via the §4.2 `usb-power` mint. NO file edit (the §3.2 goal fix is the MANUAL variant). Runs ONLY after rider #1 is landed (§2.5) — its liveness sibling is the rebind's first consumer, and the AUTO variant's detection/reopen legs ride the same session ordering discipline.

### 5.7 Ruled at this authoring (the v40 charge's three standing questions)
- **OBS-CONFIRM: DISCHARGED BY CONSTRUCTION in this WU.** The D-1 gap ("the bench cannot show *did it actually confirm?* without inference") closes via the per-command lifecycle read — `phase_terminal: CONFIRMED` + the state `field_equals` IS the bench entity-value read the candidate row named. No core-side INFO needed. The backlog row retires at the intake on this WU's green.
- **C4 [S] latency arm: the instrument-first fork is RULED.** IF the §5.4/§5.5 probe bodies show per-phase timestamps on the command read, add a close-out measurement block (p50/p99 dispatch→terminal split from those fields, device RTT reported separately). IF NOT: C4 rides a close-out measurement block from event-store timestamps (`bench.sh events` — global_position + ingest_time deltas across the bench-hero path), computed once at session close, ⏺'d in the return — [S]-class, never blocking, no scenario assert on an unmeasured wire.
- **RUNNER-VERSION-BANNER: IN** (§3.3).

## §6 — Auth note (standing; L3)

Every API call in every scenario and every paste-block authenticates: the engine re-reads `~/hs-bench/config/initial_api_token` per scenario start (DP-3; constants `api.token-file`); operator curls use `$(bench.sh api_token)` inline — proven ×many on silicon. **The token appears NOWHERE**: no paste, no capture body, no bundle note, no return, no commit message.

## §7 — The Pi session (operator; playbook §8 contract governs every block)

Order (one session, ~45–60 min; each block self-contained, WHERE-labeled, ⏺-either-way):

1. **Prep:** P-1 (uhubctl + mint) → P-2 (fleet re-verify + re-mint stamp) → P-3/P-4 (the 30-s riders). The desk half must already be deployed to the Pi's bench checkout (scp/pull per playbook; state which in the return).
2. **§7.1 The probe block (measure-then-pin):** S-1 (S31 toggle probe) → S-2 (supersession probe) → S-3 (identify probe). ⏺ full bodies. **The desk pins §5.2/§5.4/§5.5 asserts from these pastes in-session**, then the scenarios run. This is the I3b pre-flight-baseline pattern made standard (its §6 marked it load-bearing; it is how a wrong premise costs 3 minutes instead of a wrong scenario).
3. **`bench.sh scenario boot-health`** — the floor. [PASS] required before anything else.
4. **The rebind's first consumer:** `bench.sh scenario usb-reenumeration-manual` (OPERATOR; interactive TTY required — plain `ssh pi`, never `ssh pi '<cmd>'`; the C-1 lesson). Green here = the rebound liveness assert's first silicon rep. ⏺ the ok-payload — it now quotes BOTH matchedAt and triggeredAt with `agree`.
5. **The AUTO suite:** `bench.sh suite boot-health,command-confirm,command-confirm-s31,command-timeout-absent,command-supersession,command-identify-honest,usb-reenumeration,timeout-honesty-no-change` — **the explicit AUTO list IS the H2/B3 suite definition of record** (OPERATOR scenarios are deliberately absent: headless, `print_operator_block` opens the window immediately with no hands present — C-1). Expected: `command-confirm` **SKIPPED-honest** (hue-online) and every other verdict decisive. ⏺ the full suite output + bundle ids.
6. **Close:** the C4 measurement block per §5.7's ruled fork. ⏺.

## §8 — Gates, census, commit, return

**Desk gates (all in-session, before the Pi half):** (1) the runner-demo fixture suite — the §2.4 table exactly, reds quoted pre-rebind, greens ×2 post; (2) lint clean on every new/modified scenario; (3) a no-tty `suite` dry parse (scenarios load; SKIPPED paths print reasons).

**Expected bench-repo census at commit time (lock-free porcelain, flag spelled — §laws):**
`M tools/runner/engine.py` · `M scenarios/constants.yaml` · `M scenarios/command-confirm.yaml` · `M scenarios/usb-reenumeration-manual.yaml` · `?? scenarios/command-confirm-s31.yaml` · `?? scenarios/command-timeout-absent.yaml` · `?? scenarios/command-supersession.yaml` · `?? scenarios/command-identify-honest.yaml` · `?? fixtures/runner-demo/synthetic-liveness-missing-trigger-view.api.yaml` · `M fixtures/runner-demo/synthetic-liveness-pass.api.yaml` · `M fixtures/runner-demo/synthetic-liveness-pre-reopen-run.api.yaml` (+ any `.txt` expectation siblings the demo harness pairs with — enumerate exactly at commit time). **Sweep-guard: the commit is safe IFF a fresh lock-free porcelain shows exactly the enumerated set; no bench-logs/, no bundles, no token-bearing file ever stages.** Commit via `git commit -F` from `ClaudeFolder/_scratch/`; explicit paths; exact count stated to Nick; NO attribution trailers.

**The return** (to `context/audits/`, per the frontmatter law): per-rider evidence · the fixture table with observed verdicts · every re-pin quoted file:line · the probe pastes · the suite output · the re-mint stamp values · deviations as [INFO]/[REVIEW] · the C2/C3/H2/C1 evidence lines stated against the criteria text (the hub flips cells at intake, never the lane) · compliance statement for §2.5's ordering law.

**Escalation:** any [REVIEW]-class surprise (a CONFIRMED where TIMED_OUT is predicted = STOP per §5.3; a supersession shape the read surface cannot express = the charter §5 contract conversation) STOPS the affected leg and routes to the hub — the rest of the suite continues.
