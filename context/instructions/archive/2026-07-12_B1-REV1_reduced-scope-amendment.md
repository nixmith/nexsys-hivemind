<!--
file: context/instructions/2026-07-12_B1-REV1_reduced-scope-amendment.md
purpose: B1-REV1 — the GOVERNING revision of the B1 scenario-runner instruction after the ruled G-B1-2 STOP. Consumes Nick's 2026-07-12 "(c) + (a)" ruling (five riders; verbatim: pm-handoff v30 beat 3). DELTAS ONLY — everything in the base instruction not named here stands as authored.
audience: the fresh Coder lane (bench repo); Nick (dispatch + Pi operator half); the PM hub (audit).
state-type: coding-instruction amendment (REV1 supersedes the base where they conflict).
status: ISSUE-READY — authored 2026-07-12, v30 hub beat 3. DISPATCH GATE unchanged: desk half only; NOTHING lands on the Pi until the exit act + close-out + deploy.
baseline: bench `e48f04d` · core `1aa809d` — unchanged from the base; re-verify at dispatch.
base: context/instructions/2026-07-12_B1_scenario-runner-v0_coding-instruction.md (read FIRST, in full).
-->

# B1-REV1 — Reduced-Scope Amendment (the ruled "(c)": stubs + the OPERATOR liveness leg; CMD-API is a SEPARATE ruled core WU)

## Ruling context (settled — not open questions)

Nick ruled the G-B1-2 escalation 2026-07-12: **"(c) + (a)"** — B1 re-dispatches REDUCED (this REV); the command write plane (**CMD-API**) is a separate, named, ruled CORE WU sequenced at the first post-silicon-legs core slot, riding the existing Phase-2 contract with the full bar. Rider 1 (verbatim-in-force here): *"The SKIPPED-honest stubs are the right shape: present in the suite, reported SKIPPED with the named reason (missing command plane), never silently absent, never vacuously green. They flip live with B2's port once CMD-API lands."* Full ruling text: pm-handoff v30 beat 3.

## Settled facts replacing G-B1-2 (verify-not-redo)

The command endpoints do NOT exist at core `1aa809d`; the wired v1.1 HTTP surface is READ-ONLY (nine GET routes). This is a SETTLED FACT of record (the STOP session's six-leg census, hub layer-2 confirmed) — **G-B1-2 is RETIRED as a gate; do NOT re-derive the census.** Your prior session's banked verification is an INPUT OF RECORD: the G-B1-3 token table (file:line cites) and the phase vocabulary + the LTD-08-vs-live-camelCase casing caveat in `coder-handoff.md` (the B1-STOP entry). Spot-check any banked token at source before binding it; a spot-check failure is a STOP (the currency guard replacing G-B1-2). All other base gates stand: G-B1-1 (re-run at dispatch) · G-B1-3 (the banked table satisfies it — spot-check, do not re-derive) · G-B1-4 · G-B1-5.

## Deltas to the base (supersede where they conflict; everything else stands)

- **REV-1 (DP-8 rows 2–3 → SKIPPED-honest stubs):** author `command-confirm.yaml` and `timeout-honesty-no-change.yaml` IN FULL as the base specifies, but with **`requires: [command-api]`** — a new named capability, unmet by construction until CMD-API lands. The suite reports them per rider 1: `SKIPPED: [command-api] — the command plane is unwired (CMD-API pending)`. Capability resolution rides a `capabilities:` map in `scenarios/constants.yaml` (`command-api: false` · `usb-power: false` until the uhubctl hub is placed; a flip = a constants re-mint, never a code edit). The banked phase vocabulary (`ACCEPTED|DISPATCHED|ACKNOWLEDGED|CONFIRMED|CONFIRMATION_TIMED_OUT`) rides constants.yaml marked **PROVISIONAL-until-CMD-API** (cite `CommandLifecyclePhase.java:36-84` + the casing caveat; re-pin at flip time — rider 2: the shape freezes when CMD-API lands, token-freeze from day one).
- **REV-2 (DP-9 → the liveness third moves to the OPERATOR variant):** `usb-reenumeration.yaml` (AUTO, `requires: [usb-power]`) = detection + reopen legs ONLY — positives: `zigbee.transport_failed` OR `zigbee.port_unhealthy` within 30s of the cycle · `zigbee.reopened` within 120s; forbiddens unchanged (`zigbee.reopen_no_target` · `device_proposed` · `network_parameter_mismatch`). **`usb-reenumeration-manual.yaml` (OPERATOR) GAINS the liveness leg:** after `zigbee.reopened`, the printed act "ONE wave at the SNZB-03P, then HANDS OFF" → the runner polls the frozen runs surface — a NEW run appears after the run-window marker (`GET /api/v1/runs`) and its causal chain reads `actions[].outcome == CONFIRMED` (`GET /api/v1/runs/{runId}/causal-chain`; outcome vocabulary {DISPATCHED, CONFIRMED, UNCONFIRMED, FAILED, SKIPPED} — banked; spot-check at source) `within: 30s` of the wave (anchor: brightness confirmed 0.33 s on the record; the wave→run trigger is sub-second; 30 s is decisive headroom). **API-first holds — this is the frozen READ surface; no sqlite, no log-scraping-as-API (rider 1).** Scope the run lookup to the run-window marker (organic-traffic tolerance, base DP-7).
- **REV-3 (done-when, Pi half):** `boot-health` decisive with bundle · `usb-reenumeration-manual` GREEN direct-attached — **this satisfies the ratified I3a AS FROZEN** (rider 4, adjudicated: the OPERATOR variant is one of B1's two tiers; recorded with the criteria ratification block) · `suite all` prints the honest coverage line (expected Monday shape: 1 run · 2 SKIPPED [command-api] · 1 SKIPPED [usb-power] · 1 OPERATOR-deferred) · the AUTO usb scenario runs when the Rosonway hub is placed (I3b, non-blocking). Desk half unchanged (the five demonstrations; the SKIPPED demo uses `command-api`).
- **REV-4 (Out of Scope grows):** **never implement any part of CMD-API in this lane** — no route registration, no handler, no probe-the-POST logic. The `command-api` capability flag is the ONLY coupling point. CMD-API is a core WU with its own instruction, audit, and gate.

## Completion (unchanged shape)

Coder-handoff entry (deliverables + the five desk demos + the Pi half owed + the NEXT-WU pointer = the Pi half on Nick's post-close-out word, then B2 pending CMD-API) · cross-agent note with the §8 operator paste-blocks · the exact file count from a fresh porcelain (expected: the base file set unchanged — the stubs still ship as full YAML files). The hub two-layer audit precedes any commit order.
