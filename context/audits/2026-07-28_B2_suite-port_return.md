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

---

# §12 PI-HALF APPENDIX — FILED 2026-07-30 (the operator session, 2026-07-29 evening → 2026-07-30 UTC)

<!--
appendix-status: FILED 2026-07-30 by the desk-side session (Cowork/remote, Nick operating the Pi live; every paste full-body, in-session). The hub evaluates this appendix INDEPENDENTLY — every claim below cites its measurement; hypotheses are labeled as hypotheses. Timezone note: Pi log lines are America/Chicago (UTC-5); wire timestamps are UTC — 19:xx local ≡ 23:xx Z (2026-07-29) / 00:xx Z (2026-07-30).
laws-held: L1 (every wire fact below was measured in-session or re-verified at source — the two instruction paste-block defects F-1/F-5 were caught BY the L1 posture before they could burn a bench round) · L2 (every operator block was self-contained, WHERE-labeled, ⏺-either-way; deviations §12.11) · L3 (the token appears in NO paste, capture, or this appendix — the $(cat token-file) inline substitution held throughout) · lock-free porcelain spelled at every git call · NO attribution trailers on either commit.
-->

## 12.0 Session shape + deploy record

- Desk half found LANDED pre-session (bench `179daaa`, hub-audited ACCEPT ZERO DEFECTS, hivemind `ebc03ec`) — this session executed the PI HALF with a live desk (probe pastes adjudicated in-session; pins landed as bench `f3a628d`).
- **Pi deploy method of record: pull.** `~/nexsys-bench` fast-forwarded `9f2b5ad → 179daaa` (pre-probes) and `179daaa → f3a628d` (pre-suite). `~/bench.sh` is a symlink to `~/nexsys-bench/tools/bench.sh`. The Pi tree's single standing porcelain line is the Jul-13 `chmod +x` mode bit on `tools/bench.sh` (F-2, adjudicated benign — the executable bit is load-bearing; commits never happen from the Pi).
- Baselines held: core DEPLOYED `c09c61c` unchanged throughout; bench desktop tree clean at `f3a628d` at close; hivemind clean at `ebc03ec` until this appendix files.

## 12.1 P-block evidence (§4.2)

**P-1 (uhubctl install + the usb mint).** `uhubctl 2.6.0-1` installed via apt. First read required elevation (unprivileged: "permission problems while accessing USB / No compatible devices detected"). The `sudo uhubctl` read — THE MINT SOURCE:

```
Current status for hub 3-2.4 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 2: 0103 power enable connect [10c4:ea60 SONOFF SONOFF Dongle Plus MG24 0ae2dd7cecf8ef11b80168135c2a50c9]
```

`lsusb -t` corroborates: Bus 003 → hub 3-2 (VIA 2109:2822) → port 4 = hub 3-2.4 → port 2 = the dongle (cp210x, 12M). **Minted: `usb.hub-location: "3-2.4"` · `usb.port: 2` — the I3b §5.8 candidates CONFIRMED BY THE READ, not copied.**

**P-1c/Q-2 (the udev rider — F-3).** `drivers.py` invokes uhubctl UNPRIVILEGED (verified at source: `cmd = ["uhubctl", "-l", ...]`, no sudo), so the `usb-power` flip was GATED on unprivileged access working. Provisioned: `/etc/udev/rules.d/52-usb-uhubctl.rules` = `SUBSYSTEM=="usb", ATTR{idVendor}=="0bda", MODE="0666"` (hub vendor only; the dongle's 10c4 untouched). First verification attempt failed (adjudicated: raced the udev trigger); second verification clean — `/dev/bus/usb/003/003` at `crw-rw-rw-` and plain `uhubctl` prints exactly the 3-2.4 table (minimal-surface: the other hubs stay unreadable, which uhubctl tolerates). The suite later PROVED the whole chain: the engine itself ran `uhubctl -l 3-2.4 -p 2 -a cycle -d 10` unprivileged and the scenario passed.

**P-2 (fleet re-verification — the re-mint stamps, read AT the instrument, THREE boots).**

| Boot log | projection_live | network | relinked | failure sweep |
|---|---|---|---|---|
| `bench-2026-07-27-011149` (standing) | devices=6 entities=6 position=25065 | resumed ch20/0x774c | 6 | EMPTY |
| `bench-2026-07-29-191912` (post P-4 restart) | 6/6 @ 25065 | ch20/0x774c | 6 | EMPTY |
| `bench-2026-07-29-195250` + `-200106` (R-1/suite boot-health restarts) | 6/6 @ 25065 | ch20/0x774c | 6 | EMPTY |

Watermark equals the pinned 25065 at EQUALITY — correct, not stale: the registry replay-head advances only on registry-class events and nothing has been adopted since Jul-20 (the read-model viewPosition ran 50349→50522+ over the same span, the two counters correctly independent).

**P-3 (the why-not valid-id capture — WCAP-1 residual A: BANKED, with an instruction defect en route — F-5).** The instruction's `/why-not` path DOES NOT EXIST on the wire — first attempt returned `404 0.005785s` (a ROUTE miss, not an id miss). Re-pinned at source: the route is `GET /api/v1/automations/{id}/non-firing` (`RestFilters.java:310`; endpoint `GetNonFiringEndpoint.java:25`). Re-run on the live post-restart id:

```
HTTP 200 0.029699s — {"verdict":"ACTED_BUT_UNCONFIRMED", "lastRelevantRunId":"01KYR300WM3Y3A5SRN9E59T996", "explanation":"Automation 'bench-hero' fired, but a device did not confirm the requested change.", "noCommandsIssued":null, ...}
```

**200, milliseconds-class, honest body** — the valid-id half closes (the WCAP stale-id 404-in-6ms half was already banked; note WCAP's own captures used `/non-firing`, corroborating F-5 as a B2-instruction transcription defect).

**P-4 (the rotation double-read — WCAP residual B: BANKED).** `bench.sh restart` (RADIO UP 12 s, clean health). `automationId` across the restart: `01KYGZS4Q655C4FE6RWEW4F9C1 → 01KYR2SMWMC1NGQCEAFF81MW6V` — **the ULID CHANGED; rotation confirmed** (`lastRunId` reset to null on the fresh boot, consistent). Bonus corroboration: the Jul-27 history's `01KYGXTT…` id is a third distinct boot-identity.

## 12.2 S-probe evidence (the measure-then-pin block, §7.1 — full lifecycle timings)

All from the ⏺'d full-body lifecycle reads (per-phase `at` timestamps present on the command read — the §5.7 C4 fork resolves to the instrument-first arm, §12.8):

| Probe | Command | ACCEPTED→DISPATCHED | DISPATCHED→terminal | Terminal | details.result |
|---|---|---|---|---|---|
| S-1 rep 1 | S31 turn_on | 3.7 ms | **107.5 ms** | CONFIRMED (match_type exact) | — |
| S-1 rep 2 (confounded) | S31 turn_on | 3.2 ms | 5.267 s | CONFIRMATION_TIMED_OUT | — |
| S-2 first | Hue set_brightness 20 | 5.2 ms | **22.3 ms** | ACKNOWLEDGED | **"superseded"** |
| S-2 second | Hue set_brightness 50 | 5.4 ms | 5.344 s | CONFIRMATION_TIMED_OUT | — |
| S-3 rep 1 | S31 identify | 3.1 ms | **54.2 ms** | ACKNOWLEDGED | **"unconfirmed"** |
| S-3 rep 2 | S31 identify | 2.8 ms | 66.1 ms | ACKNOWLEDGED | "unconfirmed" |

**Pin adjudications:**
- **S-1: the CONFIRMED class is MEASURED on the S31** (rep 1) and the state read landed the ONE pin correction of the session — the LIVE `/state` endpoint serves `attributes.on.{"value":…}` nesting, NOT the `{t,v}` envelope the desk pinned (F-6, the STATE-DIALECT catch: `AttributeValueSerializer` feeds the ENTITY read — `GetEntityEndpoint.java:37` — not `/state`). Rep 2's TIMED_OUT is adjudicated as confounded: the report landed 1.1 s past the ~5 s window while the operator was exercising the motion sensor (bench-hero's five-command train at the Hue owned the radio; operator actions are data — the operator's own testimony supplied the variable). The quiet-bench condition for AUTO runs is the standing note.
- **S-2: pinned EXACTLY as committed, zero edits** — first command `ACKNOWLEDGED`-terminal with `lifecycle.ACKNOWLEDGED.details.result = "superseded"` (stable on a +30 s re-read), second `CONFIRMATION_TIMED_OUT`. The desk's source-derived prediction table (§4) verified on silicon end-to-end.
- **S-3: pinned EXACTLY as committed, zero edits, ×2** — `ACKNOWLEDGED` + `"unconfirmed"`, immediate-class (54–66 ms). The desk's I1 (identify-never-TIMED_OUT, adapter-immediate verdict) VINDICATED at the wire. **Reason-class finding:** the S31's recorded reason is `"no confirmation surface exists for 'identify'; the command was issued and is not tracked"` — the I3b-banked `"DefaultResponse SUCCESS +90 ms, then no report, ever"` class belongs to the HUE's identify (observed live at 19:23:18 — §12.4), i.e. the two reason strings discriminate confirmation-DISABLED (S31 mapping) from tracked-then-silent (Hue mapping). Per I2 the reason rides this ⏺ + the bundles, never a scenario assert.

## 12.3 The pin commit (bench `f3a628d`, landed + pushed + pulled pre-suite)

Census exactly 3 M (`command-confirm-s31.yaml` · `command-confirm.yaml` · `constants.yaml`): the usb mint + `usb-power: true` + the hue-online reason re-grounding + the two dialect pin fixes (s31 under the strict §5.2 license; command-confirm one hop outside it, [REVIEW]-flagged, measurement = the Hue's own `/state` read in-session). Desktop CRLF warnings adjudicated benign (blobs LF). Full rationale in the commit message itself.

## 12.4 THE HUE POWER-TOPOLOGY FINDING ([REVIEW] — the session's headline)

**Claim:** the Hue's standing "physically off-network" absence was UNPOWERED-VIA-THE-S31-RELAY — the Hue bulb lives in a lamp that was plugged into the S31.

**Evidence chain:** (1) S-1 rep 1 turned the S31 relay ON at 23:19:56Z; (2) the operator's waving (testimony, timestamped) fired bench-hero run `01KYR300WM…`, whose action train targets the Hue and ends in an identify (config read: turn_on → set_brightness 50 → set_color_temperature 4550 → 4525 → …identify); (3) that identify drew **`DefaultResponse SUCCESS +90 ms`** from the Hue (log 19:23:18 — a radio-alive proof; an unpowered device cannot ACK); (4) the operator confirmed the bulb's identity in one word; (5) the Hue's `/state` showed `lastUpdated` advancing at 23:23:18Z. **Remedy EXECUTED in-session (operator act): the lamp is UNPLUGGED from the S31** — the Hue is deterministically unpowered; the S31 carries no load (its relay reports its own state; the suite's s31 legs need none).

**Consequences:** (a) the `command-timeout-absent` premise (and `command-supersession`'s second leg) is only true while the Hue is unpowered — pre-remedy, the AUTO suite's order (s31 leaves the relay ON → the Hue powers + rejoins → the absent-premise scenarios run next) was a nondeterministic race toward the C1 automatic-STOP clause; post-remedy it is deterministic (and the suite's `command-timeout-absent` PASS proves it); (b) **HUE-RESET is now a trivial future act** — plug the lamp into wall power — and the hub can schedule the hue-online flip cheaply; (c) the availability view showed the unpowered Hue as `AVAILABLE` (staleness class — the G2 "not a live connection test" disclosure already covers it; noted for the hub, no action taken).

## 12.5 R-1/R-2 — the floor + the rebind's first silicon consumer (both [PASS])

**Stale-checkout catch first (rider #4's live save):** R-1/R-2 ran with the banner reading `@ 179daaa` — the Pi had not yet pulled the pin commit (the operator ran the Pi pull block in the desktop terminal; F-10). ADJUDICATED VALID: `f3a628d` touches neither boot-health nor usb-reenumeration-manual nor their constants dependencies. The suite was GATED on the banner reading `@ f3a628d` and did.

**R-1 boot-health [PASS]** — 6/6 positives: watermark ≥25065 ✓, rehydrated=6 ✓, relinked ×2+ ✓, ch20/0x774c ✓, `port_identity_captured … pinnedOnly=false` with the byte-exact stableId ✓, api entities 6 rows with all six remembered ULIDs ✓. Bundle `boot-health-20260729T235302Z`.

**R-2 usb-reenumeration-manual [PASS] — the rebind's first consumer.** Physical re-seat (pull → ~10 s → same port). Detection `transport_failed` at 19:53:28, `reopened` (port=/dev/ttyUSB0) at 19:53:45 (+17 s, inside 30 s/120 s). THE REBOUND OK-PAYLOAD, verbatim:

```
new run 01KYR4VCG00A46HY366JJ04TJC matchedAt 2026-07-29T23:55:09.680964Z >= M_observed 2026-07-29T23:53:45.510450+00:00
(anchor 'zigbee.reopened'; triggeredAt 2026-07-29T23:55:09.680964Z, agree=True);
chain outcomes ['UNCONFIRMED', 'UNCONFIRMED', 'DISPATCHED', 'UNCONFIRMED', 'UNCONFIRMED']
```

**Both instants quoted, `agree=True`** — on the deployed DP-3 build agreement IS the health signal; no divergence [INFO] fired. The chain outcomes are bench-hero's honest non-CONFIRMED train at the unpowered Hue (the explanation-honesty stack end-to-end). Riders #2 and #3 visibly live in the same run: the DONE-WHEN line listed all three conditions in block 1 and ONLY the outstanding `api:/api/v1/runs` in block 2 (the display fix's first silicon confirmation); the topology-neutral goal string printed. Bundle `usb-reenumeration-manual-20260729T235544Z`. **§2.5/§5.6 COMPLIANCE: the rebind was landed and demo-proven before ANY AUTO leg ran; the manual (OPERATOR) first-consumer rep preceded the AUTO suite; B3's rider-#1 gate evidence is complete.**

## 12.6 THE AUTO SUITE — first run of record (banner `runner B2-2026-07-28-rebind @ f3a628d`; boot `bench-2026-07-29-200106`)

| # | Leg | Verdict | Evidence / bundle |
|---|---|---|---|
| 1 | boot-health | **[PASS]** 6/6 | `boot-health-20260730T000118Z` |
| 2 | command-confirm | **[SKIP]-honest** `[hue-online]` | the re-grounded reason string printed verbatim |
| 3 | command-confirm-s31 | **[FAIL]** — adjudicated §12.7-B | `command-confirm-s31-20260730T000124Z` |
| 4 | command-timeout-absent | **[PASS]** — the C2 device-absent class GREEN ON DEPLOYED | `command-timeout-absent-20260730T000130Z` |
| 5 | command-supersession | **[PASS]** 2/2 — the C3 supersession leg GREEN ON DEPLOYED | `command-supersession-20260730T000136Z` |
| 6 | command-identify-honest | **[PASS]** 1/1 — the C3 identify leg GREEN ON DEPLOYED | `command-identify-honest-20260730T000137Z` |
| 7 | usb-reenumeration | **[PASS]** 2/2 — **the M9.6-RO harness's FIRST LIVE software-cycle run** (`usb cycle: uhubctl -l 3-2.4 -p 2 -a cycle -d 10`, engine-driven, unprivileged) | `usb-reenumeration-20260730T000152Z` |
| 8 | timeout-honesty-no-change | **[FAIL]** — adjudicated §12.7-A | `timeout-honesty-no-change-20260730T000152Z` |

Coverage line: `ran 7/8 — 1 SKIPPED: [hue-online]`. **`never-false-CONFIRMED` HELD across the whole run — zero false CONFIRMs anywhere; both FAILs are the instrument catching real defects, adjudicated below.**

## 12.7 The two FAILs, adjudicated

**A — `timeout-honesty-no-change` [FAIL], stimulus-class: the dialect sweep I did not run (desk process defect, owned).** `let current_brightness: field 'data.attributes.brightness_percent.v' absent` — the same F-6 STATE-DIALECT class, occurrences six and seven, in the one command scenario the desk-side session did not re-inspect when the finding landed at S-1. A five-second corpus grep would have caught it; the suite caught it instead, decisively, with the proving body quoted (`{"value":…}` at the moment the `.v` lookup died). The scenario's actual honesty teeth (the TIMED_OUT lifecycle assert) never executed — the leg is expected green once the pre-read resolves. **Fix PREPARED (not committed): `_scratch/b2pi-followup/timeout-honesty-no-change.yaml`; the corpus grep now returns ZERO `.v` field paths across all scenarios. LESSON for the standing checklist: when a wire-dialect finding lands, the license to fix extends to a FULL-CORPUS SWEEP for the class in the same beat — fixing only the files already open is how occurrence six survives to the suite.**

**B — `command-confirm-s31` [FAIL], the cadence defect (real, measured, Nick-ruled).** The asserted turn_on read `CONFIRMATION_TIMED_OUT` (fail-fast on the wrong terminal, as designed). Mechanism — hypothesis, consistent with all measurements, not independently proven: the in-file settling turn_off and asserted turn_on ran back-to-back (~100 ms; v0 has no pause between stimulus acts) with the relay entering ON; off→on netted zero state change and no report arrived inside the ~5 s window (a report-on-change device that starts and ends at `on=true` may emit nothing). The probe's green had a 20 s inter-act gap — the gap is load-bearing; the R3 settle-then-assert shape was correct about the edge but could not express the gap. The platform behaved honestly throughout. **NICK RULED 2026-07-30: the SPLIT-SETTLE PAIR** (over park-and-wait and over engine format growth, which the ladder discourages under bench pressure): NEW `command-s31-settle` (turn_off + `field_equals data.terminal == true` within 25 s — reaches SOME terminal, honest either way, guarantees the relay OFF), suite-ordered immediately before a `command-confirm-s31` reduced to the single asserted turn_on. V0-legal, zero engine changes, deterministic, self-sustaining across nightly runs (the suite ends relay-ON, so next night's settle is a real off-edge). **The 9-leg suite-of-record amendment + both files + the commit message are PREPARED at `_scratch/b2pi-followup/` — NOT committed; the hub ratifies the H2 definition change first. Desk gates owed before the re-run: lint both files, 9-leg no-tty dry parse.**

## 12.8 C4 close-out measurement block ([S]-class; the §5.7 fork RESOLVED to the instrument-first arm)

The command status read carries per-phase timestamps (`lifecycle.<PHASE>.at` — measured in every probe body), so C4's latency arm reads straight off the frozen surface; no event-store fallback needed. From the session's seven fully-timed lifecycles (§12.2 + the suite's s31 read): **accepted→dispatched = 2.8–5.4 ms across all seven** (the in-process hop, tight); **dispatched→terminal by class:** device-confirmed 107.5 ms (n=1, S31 relay incl. RTT + report); adapter-immediate identify 54.2/66.1 ms (n=2); issuance-superseded 22.3 ms (n=1); window-expiry 5.267/5.344 s (n=2, plus the suite's s31 read consistent at ~5 s). **n is disclosed and too small for honest percentiles — no p50/p99 is fabricated; B3's nightly accumulation is the correct estimator source.** Named [INFO] within this block: **the ~5 s measured confirmation window contradicts the instruction's "tuned 15,000 ms" premise (three independent expiries agree)** — the scenarios' 20 s/25 s `within` values price correctly regardless; the doctrinal number should be corrected at source (`StandardCapabilities` per-command ExpectedOutcome windows are the instrument of record).

## 12.9 Findings ledger (severity-honest)

| # | Sev | Finding |
|---|---|---|
| F-1 | [INFO] instruction defect | `$(bench.sh api_token)` is NOT a dispatched verb (usage/exit-2, measured on the Pi; the committed case statement never listed it). Every auth re-formed as inline `$(cat ~/hs-bench/config/initial_api_token)`; L3 held (token in no paste). Hub: fix the instruction template or add the verb. |
| F-2 | [INFO] | Pi tree's standing porcelain = the Jul-13 `chmod +x tools/bench.sh` mode bit. Benign, load-bearing, keep. |
| F-3 | [INFO] | uhubctl needs udev-granted access for the engine's unprivileged invocation; `52-usb-uhubctl.rules` (0bda/0666) installed + proven end-to-end by the suite's live cycle. First verification raced the udev trigger (one retry). |
| F-4 | **[REVIEW]** | THE HUE POWER-TOPOLOGY FINDING + executed remedy (§12.4). Hub: intake the standing-note correction; HUE-RESET is now trivial. |
| F-5 | [INFO] instruction defect | `/why-not` does not exist; the route is `/api/v1/automations/{id}/non-firing` (`RestFilters.java:310`). Valid-id half banked 200/29.7 ms. |
| F-6 | **[REVIEW]** | STATE-DIALECT: `/state` serves `{"value":…}` nesting (not `{t,v}`) — seven `.v` occurrences across four scenario files + two comments; four fixed in `f3a628d` (s31 in-license; command-confirm one hop outside, ratification requested), two more caught by the suite (fix prepared), one comment corrected in the prepared set. Desk-pin lesson: pin at the ENDPOINT actually read. Re-pin all when STATE-DIALECT (core P2) lands. |
| F-7 | **[REVIEW]** Nick-ruled | The s31 cadence defect + the split-settle pair ruling + the 9-leg suite-of-record amendment (§12.7-B). Hub ratification requested. |
| F-8 | [INFO] | Confirmation window measured ~5 s (three expiries), not the doctrinal 15 s (§12.8). |
| F-9 | [INFO] | Unpowered Hue renders `availability: AVAILABLE` (staleness class; the G2 disclosure covers it). |
| F-10 | [INFO] process | The banner caught a stale Pi checkout live (R-1/R-2 at `179daaa`, adjudicated valid; suite gated on `f3a628d`) — rider #4's rationale proven on its first day. Operator-block lessons minted: STOP-gates get their OWN paste block (the 0c pull ran past its gate); WHERE-labels ride INSIDE the block as a leading comment (one block was run in the wrong terminal). |

## 12.10 Gate-criteria evidence lines (stated against the criteria text — the hub flips cells, never this lane)

- **C2 [M] (device-absent class):** `command-timeout-absent` PASSED in the suite of record ON THE DEPLOYED `c09c61c` (`CONFIRMATION_TIMED_OUT`, deterministic premise post-remedy). The criterion's "ported into the suite and green on the deployed build" is satisfied for this class. Zero false CONFIRMs (the C1 law's clause held).
- **C3 [M] (supersession + identify):** both scenarios PASSED in the suite of record on the deployed build, with the S-2/S-3 full-body probe pastes (§12.2) as the wire-shape evidence the instruction ordered. The superseded disposition IS expressible on the frozen read surface (no charter-§5 contract conversation needed).
- **H2 [M]:** **NOT claimed.** The suite of record ran end-to-end headless (7/8 + honest SKIP) but carried two FAILs; the full-green run is owed after the prepared follow-up lands (post-ratification: one commit + pull + one suite run). The suite DEFINITION amendment (9 legs) awaits the same ratification.
- **C1 [M]:** accumulation rides B3. **B3's rider-#1 gate: the rebind is silicon-proven (§12.5, agree=True first-consumer rep).** B3's remaining launch precondition is the full-green suite above.
- **OBS-CONFIRM (§5.7):** the discharge-by-construction evidence is the s31 CONFIRMED + state read — MEASURED at S-1 rep 1 (§12.2) but not yet green IN THE SUITE; it completes with the re-run.
- **Jul-31 trigger:** suites ARE running as of 2026-07-30 00:01Z (this section is the evidence); the remaining follow-up is one small ratification-gated commit + a ~5-minute re-run, comfortably inside the window.

## 12.11 Compliance + deviations (operator-session process record)

§2.5 ordering law COMPLIED (§12.5). L1/L2/L3 held (frontmatter note). Operator deviations, disclosed: the Block-0c STOP-gate was overrun because gate and pull shared one paste (F-10 lesson; no harm — adjudicated post-hoc); one Pi block executed in the desktop terminal (caught by the banner gate); S-1 was executed twice in quick succession (the second rep both confounded and information-bearing — it exposed the congestion/report-timing behavior AND fed the power-topology finding); the operator exercised sensors during a non-suite interval (testimony logged, adjudicated as the S-1-rep-2 confound; the quiet-bench condition is now a standing note in the s31 header). Desktop CRLF warnings: benign (LF blobs).

## 12.12 Prepared follow-up inventory (`ClaudeFolder/_scratch/b2pi-followup/` — staged NOWHERE; the bench tree is CLEAN at `f3a628d`)

`command-s31-settle.yaml` (NEW) · `command-confirm-s31.yaml` (single-act amendment) · `constants.yaml` (9-leg suite-of-record comment + the stale `.v` comment fix) · `timeout-honesty-no-change.yaml` (`.value` ×2) · `2026-07-30_bench_B2-followup_commit-msg_DRAFT-PENDING-HUB-RATIFICATION.txt` (census: exactly 4 = 3 M + 1 ??). All four YAMLs parse; the corpus `.v` grep is zero. **Land order after ratification:** copy the four YAMLs over `nexsys-bench/scenarios/`, porcelain must show exactly the 4, commit -F the draft, push, Pi pull, lint + 9-leg no-tty dry parse, then the suite re-run (prediction: 8 decisive PASS + command-confirm SKIP-honest).

## 12.13 Recommendations to the hub (this lane recommends; the hub disposes)

1. Ratify F-7 (split-settle pair + 9-leg suite definition) and the F-6 command-confirm one-hop fix; then order the follow-up landing + re-run (H2's full-green run and OBS-CONFIRM's retirement both complete there).
2. Intake F-4: correct the Hue standing note to the measured mechanism; schedule HUE-RESET at leisure (it is now a wall-plug act) — at HUE-RESET, `command-timeout-absent` needs its re-point/retire per its own header, and the hue-online flip un-SKIPs `command-confirm` (its dialect fix is already landed).
3. Fold the lessons: full-corpus sweep on any wire-dialect finding (§12.7-A); pin-at-the-endpoint-read (F-6); STOP-gates get their own paste block + in-block WHERE comments (F-10); the ~5 s window doctrinal correction (F-8); the instruction-template defects F-1/F-5.
4. B3 authoring can proceed on the rider-#1 evidence now; its first night should run the ratified 9-leg suite.

