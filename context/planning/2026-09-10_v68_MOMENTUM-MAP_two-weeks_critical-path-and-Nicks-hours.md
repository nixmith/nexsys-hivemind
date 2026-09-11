<!--
file: context/planning/2026-09-10_v68_MOMENTUM-MAP_two-weeks_critical-path-and-Nicks-hours.md
purpose: The map re-cut at the brand landing (ritual 1): the next two weeks of development, research and testing as ONE critical path with two lanes beside it, what each landing compounds into, and Nick's hours — written so Nick can follow it without remembering anything. It re-cuts the plan of record (2026-09-06_v66_STATE-OF-THE-PROGRAM_assessment §3, adopted D4 `PLAN: adopt`); it does not replace it.
audience: Nick (§1, §4, §5) · the hub (§2, §3 — the dispatch order)
state-type: execution map (re-cut at every landing; the brief's §HELD carries the live state)
status: LIVE v69 beat 1 — RE-CUT on Nick's three edits (R-4c MEASUREMENT-ONLY on the core tree · P-1 chartered directly after R-4c · H8-a Fri 09-11 19:00 CT with the fallback) and the Thursday landings (HONESTY-1 `94ae99d` · FE-NULL-1 `eabdbb1`) (Thu 2026-09-10 ~20:1x CT; instrument 2026-09-11T01:12:55Z). Prior: LIVE v68 beat 2 (2026-09-10T21:48:18Z).
-->

# The momentum map — Thu 09-10 → Thu 09-24

## §1 One screen
The brand is now a wait-state (Erik has the packet; nothing on this map waits on him). The gate everything serves is unchanged: **the MVP's 72-hour unattended run on the six-device fleet with the hero rendering the three questions — target 2026-11-25**, about three weeks of slack today. The way we compound is the program's own law: **every landing is an instrument that every later push re-runs.** Nothing on this map is a document for its own sake; each block leaves a test, a bench verb, a CI job or a wire key that the next block stands on.

Two lanes run at once, on disjoint paths (D4: one lane per path-domain — Java · web-ui), plus Nick's hands; the rig is exclusive. The hub authors ahead so a landing is followed by a dispatch within the hour, never by a day of authoring.

## §2 The critical path (Java lane; hardware-bound; in this order)
1. **HONESTY-1** — **LANDED `94ae99d` Thu 09-10** (ci GREEN; install-smoke ran by itself on the push — P4 MET; Act 12 RETIRED). Was: ISSUE-READY on `39c8dd3`; one unattended evening. Three value corrections with no wire-shape change (`lastReported` seeded null until the first `state_reported`; `command_dispatched.origin` inherits the issued envelope's origin; the `commandEventId` javadoc) **plus CI-PATHS-1: every push builds the `.deb`.** *Compounds into:* Act 12 retires; R-4c and every rig session after it take their build from CI; the honesty batch is the first sample of the one-lane-per-domain law.
2. **R-4c — the fleet acceptance at the rig, Sat 09-12 — MEASUREMENT-ONLY on the core tree (Nick's edit, Thu)** (`R4C: Sun` moves it; no Core write Saturday — EXPLAIN keeps slot 1 through it; LASTREPORTED-1b read after the `.deb`; `card-gradle:` read once at the card). The six devices re-adopted on the held card; the sleepy SNZB-02P by the ZDO surface is **C-003**, the exit. *Compounds into:* C-003 lifts the fence on B-2/B-3 design; the fleet becomes the soak's fixture; FE-113b gets its recorded capture.
3. **EXPLAIN v1.1.4** — the biggest WU of the month; **v69's ONE deliverable**: authored Thu night → Fri, dispatched Fri into a host-side Claude Code session (slot 1; it holds the Java domain through R-4c). The additive keys HERO-0 proved the hero cannot render without: `firingValue`, the triggering `subjectRef`, `parentRunId`, the condition text, a stable definition key, `FIRED_CONFIRMED`, `disabledAt`, `confirmedAt`/`settledAt`. One bump, the CG-123 pattern, the emitter leads. *Compounds into:* the hero stops being a mock — this is where the household feels the difference, and the WU the runway's slack should buy.
4. **P-1** (the power-harness primitive as a bench verb) — **chartered directly after R-4c's packet (Nick's edit); its paste the week of 09-14** → **R-5** (the bench floor re-baselined on the fleet; the s31/nightly hands-off ENDS; the nightly becomes the soak's instrument) → the 72-h run rehearsals in October (kill −9 · coordinator disconnect · power-cycle recovery, all driven by P-1) → 11-25.

## §3 The lanes beside the path (the second slot; disjoint write-sets)
- **web-ui (the FE lane):** **FE-NULL-1 LANDED `eabdbb1` Thu** (frontend GREEN) → **the hero design charter** (`DESIGN: start` GIVEN Thu; v69 charters it at beat 2; slot 2, BESIDE EXPLAIN; the four empty states HERO-0 wrote, outward; first row = the L1 headline per outcome (FE-NULL-1's O1); the `{{NAME}}` token — the name enters the design only after the opinion; EXPLAIN keys as placeholders that say "not recorded yet", never a mock that lies) → **FE-113b** (the H8-a capture → a recorded fixture + its stability test; folds into the hero lane when H8-a returns Fri) → **FE-114** when v1.1.4 lands.
- **Bench / testing:** **TR-1b** (the position-census ITs + the driver; its shape needs `card-gradle:`, read at the card on Saturday) → P-1 → R-5. The three veto samples bank on ordinary pushes; FIX-2 stays on its signal.
- **Docs (one touch each, hub-applied, Nick commits):** the AMD-53 §1.5 correction (LANDED docs `876a395`) → the B-7 ADR ratified → the LTD-13 config-directory ruling → the v1.1.4 freeze note.
- **Brand (its own calendar; a wait-state):** Erik's sight-read on OKI/LOKI → his date → the opinion (wanted by 09-18; he expedites himself if his queue misses it) → file within days → the .com the same day → the rename program privately (`{{NAME}}` → PALOKI at the swap; the wordmark last). No public use before the opinion.
- **Research: none new before C-003.** The desk has what it needs; RS3-WMARKET-2 stays on its cadence; Matter stays PAUSED by status.

## §4 The calendar (CT) and Nick's hours (≈7 h/week; the hub carries the rest)
| When | Nick does (minutes) | The hub does meanwhile |
|---|---|---|
| **Thu 09-10 evening — DONE** | the close card run · HONESTY-1 + FE-NULL-1 pasted, returned, LANDED (`94ae99d` · `eabdbb1`) · five words given · v69 booted 20:00 CT | the map re-cut (this file); the hero charter; EXPLAIN v1.1.4 authored |
| **Fri 09-11** | the PROTECT card (3 min, any time) · pastes the hero charter into a fresh Cowork conversation (5 min) · pastes EXPLAIN v1.1.4 into a host-side Claude Code session when handed (5 min; then it runs unattended) · **H8-a at the rig 19:00 CT** (≤60 min; the 18:45 send is armed — if no paste arrives, open the packet yourself at 19:00) | EXPLAIN's instruction (the deliverable); R-4c's packet by evening; the H8-a paste AT 18:45 |
| **Sat 09-12** | **R-4c at the rig — MEASUREMENT-ONLY** (2–3 h; the packet names every step; no Core write); `card-gradle:` read once at the card | the R-4c record scaffold; **P-1's charter directly after**; TR-1b's charter on the `card-gradle:` line |
| **Mon–Tue 09-14/15** | EXPLAIN's `RETURNED` line → its landing card (push + CI, ≈20 min); P-1's paste (5 min); `Activate:` 09-15 | audits EXPLAIN at the bytes; FE-114's instruction; the B-7 ADR word |
| **Wed–Fri 09-16/18** | the hero design return → its landing; Erik's opinion (one line back); 09-18 | FE-114 dispatched on the EXPLAIN landing; R-5's plan; W-SKILLS-9 |
| **wk of 09-21** | the hero build's landing; the .com if the opinion is clean | the soak-night instrument; the 72-h rehearsal plan on P-1 |

## §5 What we do not do (re-affirmed, so momentum is not motion)
No B-2/B-3 code before C-003 and the bus fence closed · no second rig · no Matter · no research lane that does not name the instrument it feeds · no public name before the opinion · no second Java lane while one is open · no batched pushes · no `main` re-run as a fix · a sample vetoes a green, never grants one.

## §6 The alternative shape, rejected
Opening EXPLAIN v1.1.4 first because it is the differentiator: it would sit on the un-landed honesty keys and on a tree the .deb job does not yet build from; HONESTY-1 is one evening and makes every later landing cheaper. The order above is the compounding order, not the exciting order.
