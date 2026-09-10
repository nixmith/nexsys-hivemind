<!--
file: context/planning/2026-09-10_v68_MOMENTUM-MAP_two-weeks_critical-path-and-Nicks-hours.md
purpose: The map re-cut at the brand landing (ritual 1): the next two weeks of development, research and testing as ONE critical path with two lanes beside it, what each landing compounds into, and Nick's hours — written so Nick can follow it without remembering anything. It re-cuts the plan of record (2026-09-06_v66_STATE-OF-THE-PROGRAM_assessment §3, adopted D4 `PLAN: adopt`); it does not replace it.
audience: Nick (§1, §4, §5) · the hub (§2, §3 — the dispatch order)
state-type: execution map (re-cut at every landing; the brief's §HELD carries the live state)
status: LIVE v68 beat 2 (Thu 2026-09-10 ~16:5x CT; instrument 2026-09-10T21:48:18Z)
-->

# The momentum map — Thu 09-10 → Thu 09-24

## §1 One screen
The brand is now a wait-state (Erik has the packet; nothing on this map waits on him). The gate everything serves is unchanged: **the MVP's 72-hour unattended run on the six-device fleet with the hero rendering the three questions — target 2026-11-25**, about three weeks of slack today. The way we compound is the program's own law: **every landing is an instrument that every later push re-runs.** Nothing on this map is a document for its own sake; each block leaves a test, a bench verb, a CI job or a wire key that the next block stands on.

Two lanes run at once, on disjoint paths (D4: one lane per path-domain — Java · web-ui), plus Nick's hands; the rig is exclusive. The hub authors ahead so a landing is followed by a dispatch within the hour, never by a day of authoring.

## §2 The critical path (Java lane; hardware-bound; in this order)
1. **HONESTY-1** — ISSUE-READY on `39c8dd3`; unattended host-side Claude Code, one evening. Three value corrections with no wire-shape change (`lastReported` seeded null until the first `state_reported`; `command_dispatched.origin` inherits the issued envelope's origin; the `commandEventId` javadoc) **plus CI-PATHS-1: every push builds the `.deb`.** *Compounds into:* Act 12 retires; R-4c and every rig session after it take their build from CI; the honesty batch is the first sample of the one-lane-per-domain law.
2. **R-4c — the fleet acceptance at the rig, Sat 09-12** (`R4C: Sat` is the default). The six devices re-adopted on the held card; the sleepy SNZB-02P by the ZDO surface is **C-003**, the exit. *Compounds into:* C-003 lifts the fence on B-2/B-3 design; the fleet becomes the soak's fixture; FE-113b gets its recorded capture.
3. **EXPLAIN v1.1.4** — the biggest WU of the month; authored while HONESTY-1 runs, dispatched the hour it lands. The additive keys HERO-0 proved the hero cannot render without: `firingValue`, the triggering `subjectRef`, `parentRunId`, the condition text, a stable definition key, `FIRED_CONFIRMED`, `disabledAt`, `confirmedAt`/`settledAt`. One bump, the CG-123 pattern, the emitter leads. *Compounds into:* the hero stops being a mock — this is where the household feels the difference, and the WU the runway's slack should buy.
4. **P-1** (the power-harness primitive as a bench verb, weeks 3–4) → **R-5** (the bench floor re-baselined on the fleet; the s31/nightly hands-off ENDS; the nightly becomes the soak's instrument) → the 72-h run rehearsals in October (kill −9 · coordinator disconnect · power-cycle recovery, all driven by P-1) → 11-25.

## §3 The lanes beside the path (the second slot; disjoint write-sets)
- **web-ui (the FE lane):** **FE-NULL-1** (the four `| null` types + the null-arm mocks; ≤½ day; runs beside HONESTY-1 — different path-domain) → **FE-113b** (the H8-a capture → a recorded fixture + its stability test) → **the hero charter** (`DESIGN: start` is lawful now; the four empty states HERO-0 wrote, outward; the `{{NAME}}` token — the name enters the design only after the opinion; EXPLAIN keys as placeholders that say "not recorded yet", never a mock that lies) → **FE-114** when v1.1.4 lands.
- **Bench / testing:** **TR-1b** (the position-census ITs + the driver; its shape needs `card-gradle:`, read at the card on Saturday) → P-1 → R-5. The three veto samples bank on ordinary pushes; FIX-2 stays on its signal.
- **Docs (one touch each, hub-applied, Nick commits):** the AMD-53 §1.5 correction (on the tree now) → the B-7 ADR ratified → the LTD-13 config-directory ruling → the v1.1.4 freeze note.
- **Brand (its own calendar; a wait-state):** Erik's sight-read on OKI/LOKI → his date → the opinion (wanted by 09-18; he expedites himself if his queue misses it) → file within days → the .com the same day → the rename program privately (`{{NAME}}` → PALOKI at the swap; the wordmark last). No public use before the opinion.
- **Research: none new before C-003.** The desk has what it needs; RS3-WMARKET-2 stays on its cadence; Matter stays PAUSED by status.

## §4 The calendar (CT) and Nick's hours (≈7 h/week; the hub carries the rest)
| When | Nick does (minutes) | The hub does meanwhile |
|---|---|---|
| **Thu 09-10 evening** | the close card: sweep the stale lock · push hivemind · the docs commit · paste HONESTY-1 into a host-side Claude Code session (≈15 min, then it runs unattended) | authors R-4c's instruction for Saturday and FE-NULL-1's instruction; files the map |
| **Fri 09-11** | reads the coder's `RETURNED` line; the landing card (push + the CI/install-smoke sample, ≈20 min); pastes FE-NULL-1 (5 min) | audits HONESTY-1 at the bytes; authors EXPLAIN v1.1.4; `EU:` is answered by the ruling (EU-DEFER) |
| **Sat 09-12** | **R-4c at the rig** (2–3 h; the instruction names every step); `card-gradle:` read once at the card | the R-4c record scaffold; TR-1b's charter on the `card-gradle:` line |
| **an evening you name** | **H8-a** (≤60 min at the rig; the packet is on disk; `H8: <day> <hh:mm>`) | sends the navigator paste AT that time |
| **Mon–Tue 09-14/15** | pastes EXPLAIN v1.1.4 (5 min); the FE-NULL-1 landing; `Activate:` 09-15 | audits FE-NULL-1; the hero charter; the B-7 ADR word |
| **Wed–Fri 09-16/18** | the EXPLAIN landing; Erik's opinion (one line back); 09-18 | FE-114's instruction; P-1's charter |
| **wk of 09-21** | the hero build's landing; P-1's paste; the .com if the opinion is clean | R-5's plan; the soak-night instrument |

## §5 What we do not do (re-affirmed, so momentum is not motion)
No B-2/B-3 code before C-003 and the bus fence closed · no second rig · no Matter · no research lane that does not name the instrument it feeds · no public name before the opinion · no second Java lane while one is open · no batched pushes · no `main` re-run as a fix · a sample vetoes a green, never grants one.

## §6 The alternative shape, rejected
Opening EXPLAIN v1.1.4 first because it is the differentiator: it would sit on the un-landed honesty keys and on a tree the .deb job does not yet build from; HONESTY-1 is one evening and makes every later landing cheaper. The order above is the compounding order, not the exciting order.
