<!--
file: context/audits/2026-07-28_B2_suite-port_return.md
purpose: THE B2 RETURN (desk half) — rider #1 the engine rebind (landed, red-first, demo-proven ×2 + final-tree ×2) · riders 2–4 · the desk-stage constants re-mint · the §5 scenario set (command-confirm gated on hue-online; four new command scenarios, two of them measure-then-pin with source-derived predictions) · the §8 desk gates all GREEN · census 14 (8 M + 6 ??) = the enumerated set + the .txt sibling + TWO flagged [REVIEW] deltas. PI HALF PENDING (operator blocks P-1..P-4, S-1..S-3, the suite runs — sections below carry labeled evidence slots).
audience: the hub (two-layer audit + intake); Nick (the Pi half's operator).
state-type: WU return (audit input).
status: FILED 2026-07-28 (Coder, host-CC session). Location law honored: returns file to context/audits/, never handoff/ (the instruction's frontmatter law).
baselines: bench 9f2b5ad (clean at session start, re-verified) · core c09c61c (clean, re-verified at session start — the deployed build of record).
laws-held: L1 every-hop (every instruction anchor RE-verified at source in-session before code; the wire re-pins quoted file:line below) · L2 (the Pi blocks live in the instruction; nothing here is paste-with-placeholder) · L3 (the API token appears NOWHERE in this return, in any fixture, or in any scenario — only $(bench.sh api_token)/token-file indirection) · lock-free porcelain spelled at every git call · NO attribution trailers (no commit was made — the hub audit precedes any commit order).
-->

# B2 return — the §5.1 suite port + THE ENGINE REBIND (desk half)

## §0 Dispatch integrity

- Duplicate-dispatch check FIRST: the newest coder-handoff entry IS the WU-B2 desk-half dispatch (v40 beat 1); DASH-SERVE shows DELIVERED and committed as core `c09c61c` HEAD. Fresh dispatch confirmed; bench `9f2b5ad` clean at start (lock-free porcelain, empty).
- Launch preconditions verified: the skills mirror carries the 2026-07-28 post-v39 currency-pass masthead (Check 9 satisfied); the v40 beat-1 hivemind push present (the dispatch entry exists).
- **Pre-verification file note:** the dispatch prompt referenced `context/pre-verifications/2026-07-28_B2_...md`; no such file exists (the directory holds only WU-SKIP-VIS and WU-DASH-SERVE, and the B2 dispatch entry names no pre-verification). Treated as intended: the instruction's L1 every-hop law IS the pre-verification obligation — every §2.2 anchor was re-enumerated at source in-session (§1 below), zero mismatches, so no STOP fired.

## §1 Anchor re-verification (L1, all at source in-session)

Bench `9f2b5ad` `tools/runner/engine.py`: `eval_new_run_after` :919–:984 ✓ · the `triggered < m_observed` discard :951–:958 `continue`s BEFORE the chain fetch :959 ✓ · ok-payload :975–:977 `{runId, triggeredAt, mObserved, anchor, outcomes}` ✓ · the note line :859–:863 prints `triggeredAt >= M_observed` ✓ · `parse_iso_utc` :1186– with the under-count-never-false-PASS docstring ✓ · lint :228–:251 ✓ · anchor-unmatched refusal :930–:934 ✓ · no-snapshot pending :935–:938 ✓ · `pending_positive_tokens` :736–:747 with exactly the I3b §5.5 mechanism (display strings vs resolved-token keys — joins/`api:`-prefixes/unresolved tokens can never filter) ✓ · `scenarios/usb-reenumeration-manual.yaml:74` reads the direct-attached goal string ✓.

## §2 Rider #1 — THE ENGINE REBIND (landed; red-first; §2.5 ordering law COMPLIED)

**Compliance statement (§2.5):** the rebind + its fixture table landed and were demo-suite-proven (×2 mid-tree, ×2 again on the FINAL tree) BEFORE any Pi AUTO leg ran (none has run — the Pi half is pending). B3's gate on rider #1 is satisfiable on this evidence.

**The rebind as landed (engine.py, `eval_new_run_after`):** for each snapshot-diff run — (1) causal chain fetched FIRST; non-200 ⇒ `"<id>: causal-chain read HTTP <s>"` ignored-with-reason; (2) `data.trigger.matchedAt` bound; trigger view absent ⇒ `"<id>: trigger view absent — cannot bind matchedAt"`; unparseable ⇒ `"<id>: unparseable matchedAt %r"`; NEVER a silent fallback to triggeredAt; (3) the anti-false-PASS arm PRESERVED on matchedAt (`"<id>: matchedAt %s predates M_observed %s"`); (4) the executed-chain arm unchanged (≥1 action with an outcome, outcome-agnostic); (5) ok-payload `{runId, matchedAt, triggeredAt, mObserved, anchor, outcomes, agree}` — `agree` = the two instants equal truncated to the second; divergence prints its own `[INFO] matchedAt/triggeredAt DIVERGE …` detail line, verdict unaffected. Docstring rewritten naming the rebind + I3b §4 + the both-fields law. The evidence note line now quotes matchedAt with triggeredAt + agree beside it. Snapshot semantics UNCHANGED.

**Byte-preservation proof (HEAD-slice search, worktree):** anchor-unmatched refusal :930–:934 (258 B) TRUE · no-snapshot :935–:938 (238 B) TRUE · the new_run_after lint :228–:251 (1523 B) TRUE · the combined-asserts refusal :251–:257 (435 B) TRUE · `eval_new_confirmed_run` whole :891–:917 (1530 B) TRUE · `parse_iso_utc` whole :1186–:1204 (790 B) TRUE · the snapshot first-attempt pin :528–:552 (1483 B) TRUE.

**The §2.4 fixture table — predictions vs observed:**

| Fixture | PRE-rebind (red run, quoted) | POST-rebind observed (×2 + final-tree ×2) | Prediction |
|---|---|---|---|
| `synthetic-liveness-pass` (+`trigger.matchedAt` 2099) | PASS (old note: `triggeredAt 2099-01-01T00:00:05Z >= M_observed`) | **PASS** — `new run 01KXSYNTHPOSTREOPENRUN0000 matchedAt 2099-01-01T00:00:05Z >= M_observed … (anchor 'zigbee.reopened'; triggeredAt 2099-01-01T00:00:05Z, agree=True); chain outcomes ['DISPATCHED', 'UNCONFIRMED']` | PASS ✓ |
| `synthetic-liveness-pre-reopen-run` (+`matchedAt` 2020-06-01) | FAIL (old reason: `triggeredAt … predates`) | **FAIL** — `ignored: 01KXSYNTHPREREOPENTRIG0000: matchedAt 2020-06-01T00:00:00Z predates M_observed …` (the rejection now rides matchedAt; the CONFIRMED chain present and read — rejection purely temporal) | FAIL, matchedAt-predates ✓ (the matchedAt<M mutant-killer) |
| **NEW** `synthetic-liveness-missing-trigger-view` (populated chain, NO trigger) | **[PASS] — THE RED**: `new run 01KXSYNTHNOTRIGGERVIEW0000 triggeredAt 2099-01-01T00:00:05Z >= M_observed … chain outcomes ['DISPATCHED', 'UNCONFIRMED']` — the pre-rebind engine passes ON triggeredAt, the wrong-reason evidence §2.4 demanded | **FAIL** — `ignored: 01KXSYNTHNOTRIGGERVIEW0000: trigger view absent — cannot bind matchedAt` (reason quoted) | FAIL, reason quoted ✓ (kills the silent-fallback mutant) |
| `synthetic-liveness-no-new-run` | FAIL | **FAIL** (0 new runs, polls exhaust) | behavior-preserved ✓ |
| `synthetic-liveness-snapshot-member` | FAIL | **FAIL** (member filtered before any fetch; its chain still never read) | behavior-preserved ✓ |
| `synthetic-liveness-empty-chain` (+`trigger.matchedAt` 2099 — **[REVIEW] R1**) | FAIL — `ignored: … chain shows no executed action yet` | **FAIL** — same reason, same ignore | behavior-preserved ✓ (see R1: the table's "never reach the matchedAt bind" parenthetical was false at implementation depth for THIS fixture; the edit keeps both the reason and the condition-(c) mutant-killer alive) |

Mutation coverage after the rebind (fixture-paired, the standing rule): membership arm — snapshot-member; temporal arm — pre-reopen-run; fallback arm — missing-trigger-view; executed-chain arm — empty-chain (alive only because of R1).

## §3 Riders 2–4

**Rider #2 (`pending_positive_tokens`)** — rewritten per §3.1: log lines filter on their resolved token; `log_any` filters when ANY resolved member is satisfied; api lines filter per evidence-line index (`satisfied_lines`, stamped at each line's satisfaction in live + dry + scripted paths). Verdict-neutral. Harness evidence (the REAL `print_operator_block` against `synthetic-reseat-healthy`, quoted):
- STATE 0 (nothing satisfied): `DONE-WHEN: zigbee.transport_failed OR zigbee.port_unhealthy then zigbee.reopened then api:/api/v1/runs`
- STATE 1 (log_any satisfied): `DONE-WHEN: zigbee.reopened then api:/api/v1/runs`
- STATE 2 (both logs satisfied — the gated second act's live state): `DONE-WHEN: api:/api/v1/runs`
Pre-B2 all three states printed all three conditions.

**Rider #3 (goal string)** — `usb-reenumeration-manual.yaml:74` → `"Prove honest detection + autonomous reopen on a physical re-seat"`. One line; the 90 s window and the `after:` gate untouched (adjudicated law). The edited goal is visible in the reseat-healthy demo's operator plan (quoted in §5).

**Rider #4 (RUNNER-VERSION-BANNER)** — `ENGINE_VERSION = "B2-2026-07-28-rebind"` module-level in engine.py; `emit_version_banner()` prints `runner <ENGINE_VERSION> @ <short SHA|no-git>` once per process, called from the engine's own entry points (`load_constants` + `run_scenario`) so BOTH `scenario` and `suite` invocations self-identify before the first verdict line with ZERO runner.py surface (census stays exact — I3). SHA resolve: `git --no-optional-locks -C <engine-dir> rev-parse --short HEAD`, failure-silent. Observed on every gate run: `runner B2-2026-07-28-rebind @ 9f2b5ad`.

## §4 The desk-stage constants re-mint (§4.1) + wire re-pins quoted (all at core `c09c61c`, clean tree re-verified)

Flips landed in `scenarios/constants.yaml`: `capabilities.command-api.available: true` (reason = the source citation: CMD-API landed `5b4797e`, deployed in `c09c61c` 2026-07-27) · `capabilities.hue-online` minted `{available: false, reason: "HUE-RESET pending — the Hue is physically off-network (standing note 2026-07-21; I3b §5.1)"}` · `command.s31-entity: "01KXW1W1SBJZERC9MBAMV2DWKE"` · the AUTO-suite-of-record comment block (§7.3) · `usb.*` UNTOUCHED PLACEHOLDER (Pi stage owns it). The desk-stage re-mint note rides the file header; the Pi stage (P-1/P-2) completes the stamp.

**The re-pin table (every §4.1/§5.2 obligation, file:line):**

| Wire fact | Source at c09c61c | Verdict |
|---|---|---|
| 202 body `{data, meta}` camelCase, hand-built | `IssueCommandEndpoint.java:364-378` | HOLDS |
| `data.commandId` capture path | `IssueCommandEndpoint.java:365` (`respondAccepted`) | HOLDS |
| `data.terminal` | `GetCommandStatusEndpoint.java:198` | HOLDS |
| `data.currentPhase` (UPPERCASE via `currentPhase.name()`) | `GetCommandStatusEndpoint.java:197` | HOLDS |
| Phase vocabulary `[ACCEPTED, DISPATCHED, ACKNOWLEDGED, CONFIRMED, CONFIRMATION_TIMED_OUT]` | `CommandLifecyclePhase.java:36-84` (:45/:54/:64/:73/:83) | HOLDS — constants list exact |
| POST body: `capability` + `command` + `parameters` ALL REQUIRED (`{}` floor for parameterless) | `IssueCommandEndpoint.java:263-277` | **DELTA — the R2 finding** (the pre-B2 stub bodies omitted `capability`; scenario-side fix, constants untouched — the constants block gained the documentation row) |
| S31 commands `turn_on`/`turn_off`/`toggle`; attribute `on` boolean; EXACT_MATCH; capability id `on_off`; turn_on outcome window 5000 ms | `StandardCapabilities.java:133-155` (:139-141 attr, :143-150 cmds, :146 window, :155 id) | pinned |
| S31 state path `data.attributes.on.v` ({t,v} envelope; no derived twin for `on`) | `AttributeValueSerializer.java:68/:70`; `GetEntityEndpoint.java:37`; `MaterializedStateQueryService` BRIGHTNESS_PERCENT_KEY `:113` (brightness-only derivation) | pinned |
| Supersession: issuance supersedes; `command_result(outcome="superseded")` threads the EXPIRED command's correlation; read renders ACKNOWLEDGED-terminal, `lifecycle.ACKNOWLEDGED.details.result` = the outcome | `StandardPendingCommandLedger.java:153` (OUTCOME_SUPERSEDED), `:331`, `:358-:366`, `:905-:915`; `GetCommandStatusEndpoint.java:150-158` | pinned (S-2 confirms on silicon) |
| Identify: confirmation DISABLED at root — the ledger NEVER tracks it (⇒ `CONFIRMATION_TIMED_OUT` structurally impossible for identify); the adapter renders the immediate honest `command_result(outcome="unconfirmed")` with recorded reason | `StandardCapabilities.java:195-203` + `:215-216`; `ZigbeeCommandHandler.java:45-53` | pinned (S-3 confirms) — **I1** |
| The recorded reason does NOT surface on the command status read (`details` carries only `{result}`) | `GetCommandStatusEndpoint.java:154` | **I2 finding** — the reason-class evidence rides S-3's ⏺ + the bundle, not a scenario assert |

## §5 The stub flip + the scenario set (§5)

- **`command-confirm` (M):** `requires: [command-api, hue-online]`; header banner rewritten to the hue-online gate (ruling shape preserved); PROVISIONAL markers replaced with the B2 re-pin citations; body gains the REQUIRED `capability: brightness` (the R2 class, in-census file). Demo: `[SKIP] command-confirm — SKIPPED: [hue-online] — HUE-RESET pending — the Hue is physically off-network (standing note 2026-07-21; I3b §5.1)` — the §5.1 gate proven.
- **`command-confirm-s31` (new):** deterministic turn_off-settling + turn_on-asserted shape (**R3** — the instructed let-pre-read→opposite-command-NAME is inexpressible in v0 mechanics; header carries the full reasoning + the S-1 measure-then-pin honesty gate verbatim); asserts `phase_terminal: CONFIRMED` within 20s + `field_equals data.attributes.on.v == true` within 20s.
- **`command-timeout-absent` (new):** Hue, fixed level 20, `requires: [command-api]` only (the absence IS the premise); `phase_terminal: CONFIRMATION_TIMED_OUT` within 25s; the one-false-CONFIRM STOP law quoted in the header; the premise-lifetime note (dies at HUE-RESET; re-point or retire to OPERATOR) is the standing owner.
- **`command-supersession` (new, measure-then-pin):** two back-to-back POSTs (20 then 50); FIRST asserts `phase_terminal: ACKNOWLEDGED` + `field_equals lifecycle.ACKNOWLEDGED.details.result == "superseded"` within 20s (issuance-driven — I9); SECOND `CONFIRMATION_TIMED_OUT` within 25s; the charter-§5 contract-conversation rider quoted for the cannot-express case; S-2 pins before it runs.
- **`command-identify-honest` (new, measure-then-pin):** S31 identify; asserts `phase_terminal: ACKNOWLEDGED` + `result == "unconfirmed"` within 20s — the source-derived honest terminal (NOT the naive TIMED_OUT guess — I1); never-CONFIRMED load-bearing via phase_terminal's fail-fast; the reason-surfacing gap named (I2); S-3 pins before it runs.
- **`timeout-honesty-no-change` (M — [REVIEW] R2):** the REQUIRED `capability` body field + banner rewrite (LIVE now) + re-pin citations. Without the fix its AUTO-suite leg 400s on the live wire — a guaranteed false-FAIL in the §7 suite this instruction defines.
- **`usb-reenumeration`:** ZERO edits (§5.6 honored); SKIPs on [usb-power] until the Pi-stage mint; runs only after rider #1 (satisfied — the rebind is landed and proven).

**Shared mechanics held:** every scenario uses only existing SCENARIO_FORMAT mechanics; NO format growth; every `within` prices the instrument (20s CONFIRMED-class / 25s TIMED_OUT-class; supersession's first read 20s as issuance-driven — I9); all `bundle: always`; all API-first; the token only ever via the engine's token-file re-read (L3).

## §6 The §8 desk gates (all GREEN, in-session)

1. **Runner-demo fixture suite:** the §2 table — red quoted pre-rebind, predicted verdicts ×2 post-rebind + ×2 on the FINAL tree (byte-identical shape). Collateral demos on the final tree: reseat-healthy **PASS** (the edited goal string visible in the plan print: `'goal': 'Prove honest detection + autonomous reopen on a physical re-seat'`), reseat-flap **FAIL** on the scoped forbidden, boot-proposed **FAIL** on the forbidden hit, empty-positives **REFUSED** (anti-vacuous lint intact). Boot-pass/missing-relink both FAIL dry at HEAD — PRE-EXISTING (I5), not B2.
2. **Lint:** zero REFUSED across every new/modified scenario (each dry-ran against a boot fixture; lint precedes the requires-gate, so the SKIP/PASS verdicts prove lint-clean). All asserts resolve (${C.*} incl. the new s31-entity substituted correctly in the printed plans).
3. **No-tty suite dry parse (×2, byte-identical):** the exact §7.3 AUTO list, stdin closed. Output: banner first; all 8 scenarios LOAD (ZERO REFUSED); `[SKIP] command-confirm … [hue-online]` + `[SKIP] usb-reenumeration … [usb-power]` with reasons; six decisive env-FAILs (desk has no bench: bash/bench.sh unresolvable → fast 127-class DriverErrors; no token file) — no launches attempted, no $HOME writes (I7); coverage line `ran 6/8 — 1 SKIPPED: [hue-online] · 1 SKIPPED: [usb-power]`.

## §7 Census (lock-free porcelain, final tree — 14 entries: 8 M + 6 ??)

```
 M fixtures/runner-demo/synthetic-liveness-empty-chain.api.yaml      <- [REVIEW] R1 (census delta)
 M fixtures/runner-demo/synthetic-liveness-pass.api.yaml
 M fixtures/runner-demo/synthetic-liveness-pre-reopen-run.api.yaml
 M scenarios/command-confirm.yaml
 M scenarios/constants.yaml
 M scenarios/timeout-honesty-no-change.yaml                          <- [REVIEW] R2 (census delta)
 M scenarios/usb-reenumeration-manual.yaml
 M tools/runner/engine.py
?? fixtures/runner-demo/synthetic-liveness-missing-trigger-view.api.yaml
?? fixtures/runner-demo/synthetic-liveness-missing-trigger-view.txt  <- the anticipated .txt sibling (§8's clause)
?? scenarios/command-confirm-s31.yaml
?? scenarios/command-identify-honest.yaml
?? scenarios/command-supersession.yaml
?? scenarios/command-timeout-absent.yaml
```
Sweep-guard: no bench-logs/, no bundles, no token-bearing file, no README/runner.py churn. NO COMMIT was made — the hub's audit precedes any commit order; at that order the staging is these explicit 14 paths, `git commit -F` from `ClaudeFolder/_scratch/`, NO attribution trailers.

## §8 Deviations (severity-honest)

**[REVIEW] R1 — `synthetic-liveness-empty-chain.api.yaml` M (outside the §8 enumerated census).** The §2.4 table's parenthetical ("their asserts never reach the matchedAt bind") is FALSE at implementation depth for empty-chain under the mandated fetch-first arm order: its run would die at "trigger view absent," silently duplicating missing-trigger-view and leaving the executed-chain arm with NO mutant-killer (the fixture-paired-asserts standing rule broken). The minimal edit — `trigger.matchedAt: 2099` on its scripted chain — preserves the verdict, the reason, AND the condition-(c) teeth (observed: the post-rebind ignore is still `chain shows no executed action yet`). no-new-run and snapshot-member genuinely never reach the bind and are byte-untouched. Ratification requested (the dispatch's welcome-pushback clause: the anti-false-PASS/never-vacuous arms are contract — this edit is what keeps the executed-chain arm's contract mutation-covered).

**[REVIEW] R2 — `timeout-honesty-no-change.yaml` M (outside the enumerated census) + the same fix inside in-census `command-confirm.yaml`.** The live wire REQUIRES a non-blank `capability` body field (`IssueCommandEndpoint.java:263-277` — capability/command/parameters all required); both pre-B2 stub bodies omitted it (authored from Phase-2 javadoc guesses before the endpoint existed). Un-fixed, the §7 AUTO suite's timeout-honesty leg 400s → a guaranteed false-FAIL on the very first Pi run. Minimal edits: `capability: brightness` + banner/citation updates. Ratification requested.

**[REVIEW] R3 — `command-confirm-s31` shape deviates from §5.2's letter.** The instructed pre-read→command-the-OPPOSITE cannot be expressed in v0 mechanics: `other_of` selects VALUES, not command NAMES; `turn_on`/`turn_off` are parameterless (`StandardCapabilities.java:143-150`) so no value-carrying command exists; `toggle` declares ZERO ExpectedOutcomes (`:150`) — nothing for the ledger to confirm, the wrong instrument for a CONFIRMED-class leg. Realized shape: an UNASSERTED turn_off settling act then the ASSERTED turn_on — the on-edge is structurally a real change (the pre-read shape's purpose), deterministic, zero conditionals, zero format growth. The settling command's own fate (no-change timeout or issuance-supersession by the asserted command — `StandardPendingCommandLedger.java:331`) is documented in-header and asserted by nothing. S-1 still probes first (the honesty gate stands verbatim). Alternative if the hub prefers the letter: a format/engine growth ruling (a conditional-command mechanic) — NOT taken unilaterally.

**[INFO] I1** — identify's desk prediction is ACKNOWLEDGED-terminal with `result="unconfirmed"`, not a TIMED_OUT class: confirmation is DISABLED at the capability root and the ledger never tracks identify (`StandardCapabilities.java:195-203/:215-216`), so `command_confirmation_timed_out` is structurally impossible; the adapter owns the immediate honest verdict (`ZigbeeCommandHandler.java:45-53`). §5.5's "honest non-CONFIRMED terminal" realized per source; S-3 measures before the scenario runs.
**[INFO] I2** — the recorded reason ("DefaultResponse SUCCESS +90 ms…" class) does NOT surface on the command status read: `details` carries only `{result: outcome}` (`GetCommandStatusEndpoint.java:154`). The reason evidence rides Block S-3's ⏺ and the bundle's captures. If the hub wants the reason on the command read, that is a charter-§5 contract conversation (named here, not acted on).
**[INFO] I3** — the version banner rides the engine's own entry points (`load_constants` + `run_scenario`, once-per-process guard) rather than runner.py — §3.3 mandates only that ENGINE_VERSION live in engine.py; this realization keeps the census exact and provably prints before the first verdict line in BOTH invocation modes (suite-path evidence in §6.3).
**[INFO] I4** — `_resolved_or_raw` display helper in `pending_positive_tokens`: a token whose `${let.*}` is unbound at print time cannot have been satisfied — shown raw instead of refusing mid-operator-print (defensive, display-only).
**[INFO] I5** — PRE-EXISTING: the boot demo fixtures still carry the 2-device era (`devices=2 entities=2 position=6417` at `9f2b5ad`), stale since the 2026-07-21 fleet re-mint (6/6 @ 25065) — boot-pass and boot-missing-relink both FAIL dry at HEAD, before any B2 edit (verified against the committed fixture). Out of B2's census; a hub-owned fixture re-mint candidate. The forbidden-hit and refusal demos still demonstrate their machinery.
**[INFO] I6** — `fixtures/runner-demo/README.md` NOT updated (census law): the new missing-trigger-view pair and the three trigger-block edits are undocumented there; a hub-side README amendment is suggested at intake.
**[INFO] I7** — the suite-parse gate used a scratchpad stub via `--bench-sh` to guarantee zero desk side effects (the real `bench.sh restart` on a desk would attempt a launch + a 90 s poll + `$HOME` writes); on this host bash exits 127 before even the stub runs — either way the FAILs are fast decisive environment faults, no launch attempted, and the gate's assertions (8/8 load, zero REFUSED, SKIP reasons, coverage) are unaffected. The stub never stages.
**[INFO] I8** — `agree` is `False` when the row's triggeredAt is absent/unparseable (the divergence [INFO] prints) — conservative realization of "match to the second."
**[INFO] I9** — the supersession scenario's FIRST read gets the 20 s CONFIRMED-class window (the disposition is ISSUANCE-driven — lands at the second POST, no window expiry involved), the SECOND the 25 s TIMED_OUT-class window; the shared-mechanics pricing rule applied by mechanism, not by label.

## §9 Gate-criteria evidence lines (the hub flips cells, never this lane)

- **C2 [M] (device-absent class):** `command-timeout-absent` authored + lint-green + suite-listed; the class closes at "ported into the suite and GREEN ON THE DEPLOYED BUILD" — the Pi suite run completes it. A CONFIRMED there = the C1 one-false-CONFIRM STOP (header-quoted).
- **C3 [M] (supersession + identify):** `command-supersession` + `command-identify-honest` authored measure-then-pin with source-derived predictions (the supersession read-shape IS expressible on the frozen surface — §4's re-pin table); S-2/S-3 pastes + the suite green complete the cells.
- **H2 [M]:** the AUTO suite of record DEFINED (§7.3; of-record comment in constants.yaml): `boot-health,command-confirm,command-confirm-s31,command-timeout-absent,command-supersession,command-identify-honest,usb-reenumeration,timeout-honesty-no-change`; desk parse proves 8/8 load + honest SKIP shape; green on the deployed build = the Pi run.
- **C1 [M]:** accumulation rides B3 nightly; **B3's gate (rider #1) is satisfied by §2's evidence** — the instrument is sound before the corpus compounds.
- **Jul-31 trigger:** desk half done 2026-07-28; the Pi half is a single operator session (~45–60 min per §7). If suites are not running by EOD 2026-07-31 → escalate to Nick with the named slide cost (standing).

## §10 PI HALF — PENDING (operator; the instruction's §4.2/§7 blocks are the runbook)

Evidence slots the operator/hub fills at the Pi session (⏺-either-way): P-1 uhubctl output + the usb.* mint (from the read, never the candidates) · P-2 fleet re-verify stamp (expect 6/6, ≥25065, ch20/0x774c) · P-3 valid-id why-not (predict 200 ms-class) · P-4 rotation double-read (predict ULID changed) · S-1 S31 toggle probe ⏺ (binds §5.2's asserts) · S-2 supersession probe ⏺ BOTH bodies (binds §5.4) · S-3 identify probe ⏺ (binds §5.5) · boot-health floor · usb-reenumeration-manual (the rebind's first silicon consumer — ⏺ the ok-payload with BOTH instants + agree) · the AUTO suite + bundle ids · the C4 §5.7 fork ⏺. Deploy of the desk half to the Pi's bench checkout: scp or pull — state which in the appended evidence.

## §11 Next WU (refuse-to-close)

**B3 nightly** (bench lane, hub-authored) — authors immediately behind B2; its gate on rider #1 is DELIVERED-and-demo-proven (§2); the Pi half's first-consumer rep + suite green are the remaining B3 preconditions. Carried candidates unchanged from the DASH-SERVE entry.
