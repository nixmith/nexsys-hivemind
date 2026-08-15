<!--
file: context/handoff/2026-08-14_G1_gate-day-demo_runbook.md
purpose: G1's remaining evidence act — the scripted ≤10-minute gate-day live demo (the ledger §121 row: the three questions answered on REAL bench data over the FROZEN v1.1 read-API; never mocks, never improvised shapes; read LAST at the READ per the ledger's own §4 protocol). Mechanics inherit the PROVEN dash-serve routes (2026-07-27 brief; G2 closed on them).
audience: Nick (runs it at the READ, Sun Aug-16; one timed rehearsal Sat evening per the weekend plan); the hub (evidence steward at the read).
state-type: runbook (gate artifact; the demo's ⏺ records + screenshots file into the READ record).
laws: L3 — THE TOKEN NEVER ENTERS A CONVERSATION (read on the Pi terminal, typed into the browser only; enter it BEFORE the demo clock starts). Scope — the demo DEMONSTRATES, never debugs: a broken tile is a ⏺ FINDING narrated honestly ("and this is the system showing an honest failure state"), never a mid-demo fix. Anti-actions — no config edits, no constants.yaml, no scenario runs, no retunes, HANDS OFF the s31 legs. The freeze governs: nothing deploys on gate day.
pre-flight-dependency: the chain-render check in TODAY'S operator block (2026-08-14_freeze-day_operator-block.md §1) — the FE-LIVE-V112 item-1 fix is repo-landed but its Pi-deploy state is UNVERIFIED; if the check crashes, the warm rebuild runs TODAY (before the freeze), never on gate day.
-->

# G1 — The Gate-Day Demo Runbook (≤10 min, read LAST)

**What G1 must show (the frozen row, restated):** live against the bench Pi over the frozen v1.1 read-API — **(a)** *why did it fire* — a real bench-hero run's causal chain end-to-end; **(b)** *why didn't it* — a real non-firing explanation including the no-change class (log-derived; the explanation NEVER upgrades or replaces a verdict); **(c)** *did it actually confirm* — the verdict vocabulary on real data: CONFIRMED with latency · honest-UNCONFIRMED with its measured reason · deliberately-superseded verdict-free. Each tile's log token matches the underlying event (log-token↔tile continuity).

## Setup (BEFORE the clock; ~3 min, not counted)

On Windows (leave running):

```
ssh -N -L 7070:127.0.0.1:7070 pi
```

Browser → `http://localhost:7070/` (lands on `/dashboard/`, the AuthGate). On the **Pi** terminal:

```
cat /home/homesynapse/hs-bench/config/initial_api_token
```

Read on screen, type into the browser field only (⚠ L3 — if absent, try `cat /home/homesynapse/.homesynapse/config/initial_api_token`). Dashboard renders → leave it on Overview. Have the previous night's digest line at hand (the §3 paste from the freeze-day block) — its run is tonight's exhibit material.

## The demo (start the timer)

**Act 1 — "Why did it fire?" (~3 min).** Runs surface → the most recent NIGHTLY bench-hero run (last night's fire) → open its causal chain. Walk it aloud, one hop per sentence: the trigger event (name the log token on the tile) → the condition evaluation → each action with its verdict. **The continuity line, stated once:** "every tile here carries the same token the event log carries — this is a projection of the log, not a story about it." ⏺ RECORD which run (its timestamp/id) + screenshot the full chain.

**Act 2 — "Why didn't it?" (~2.5 min).** The explain surface → a real NON-FIRING explanation, preferring the no-change class (a night where a leg's condition held state and nothing fired). Read the explanation verbatim; state the law it demonstrates: "the system distinguishes never-triggered / condition-false / didn't-confirm — and this explanation is derived from the log; it never upgrades or replaces a verdict." ⏺ RECORD which explanation + screenshot.

**Act 3 — "Did it actually happen?" (~3 min).** The run detail's action verdicts, three exhibits on real data:
1. **CONFIRMED with latency** — any confirmed action from a recent nightly (the ON-latency legs carry measured values; read the number aloud).
2. **Honest-UNCONFIRMED with its measured reason** — a `CONFIRMATION_TIMED_OUT` from the s31 leg's recent nights IS the exhibit: "expected CONFIRMED, the device didn't report within the window — the system says so instead of lying. Across ~1,700+ recorded verdicts on this bench, zero false CONFIRMs." (The D-2 language at the read carries the distribution context; the demo just shows the tile.)
3. **Deliberately-superseded, verdict-free** — a superseded action rendering with no verdict claim (the five-modes-distinct rendering: label + glyph + tone).
⏺ RECORD + screenshot each.

**Close (~1 min).** Overview → the availability tile's honest rows (`Available / Offline / Not determined yet / Stale` + the "last report — not a live connection test" line): "even the summary tile refuses to claim what it hasn't measured." Stop the timer. ⏺ RECORD the elapsed time.

## If something breaks mid-demo

Narrate it as evidence, don't fix it: the error boundary and the honest empty state ARE the product's posture ("no data beats fake data"). ⏺ RECORD what rendered, move to the next act. Three broken acts = the demo still completes as a FINDINGS record; the hub adjudicates at the read. Nothing retro-fails the ledger's closed rows.

## Rehearsal (Sat evening, once)

Run the whole script timed, screenshots included, against whatever last night's digest produced. One run only — findings ⏺ to the hub; no iteration, no tuning. If the rehearsal surfaces a render defect: it is a FINDING for the read (the freeze forbids fixing it), and the demo's fallback narration above is the plan of record.
