<!--
file: context/instructions/2026-08-04_REV-1_physics-spine_adversarial-review_lane_brief.md
purpose: REV-1 — the pre-freeze adversarial review of the physics-touching spine (command confirmation · zigbee availability/command path · persistence write path), per Nick's 2026-08-04 diligence directive and the D16 discipline (a full-check+CI-green arc still buys an independent adversarial review, because automated gates structurally cannot catch the design classes). Read-only; findings due Aug-8 EOD so HIGH items are rulable pre-freeze.
audience: the REV-1 lane (a FRESH Cowork conversation; NOT the desk)
status: DISPATCH-READY. Baseline: core `60d3ab5` (re-derive at launch — if S-5a has landed, review the new HEAD and say so). Return → `context/audits/2026-08-0X_REV-1_physics-spine_adversarial-review_return.md` (fill X with the delivery date). The lane commits NOTHING.
-->

# REV-1 — Physics-Spine Adversarial Review (lane brief)

## Section 0 — Laws (bind everything below)

1. **READ-ONLY.** You change no file in any repo. One return file is your entire output.
2. **Evidence-required findings:** every DEFECT/RISK carries a concrete trigger — file:line cites plus the input/state sequence that produces the wrong outcome. A concern without a trigger is a NOTE. Rank HIGH / MED / LOW / NOTE.
3. **Refutation-welcome BOTH directions:** the named seeds (§3) are hypotheses, not conclusions — confirming AND refuting are equally valued returns. Settled ground (Locked docs, ratified AMDs, banked criteria) is FENCED: cite it, never re-litigate it; a finding that contradicts settled ground must say so explicitly and carry the strongest evidence.
4. **FACT / INFERENCE / OPINION discipline** with confidence, throughout. Access failures disclosed, never routed around.
5. One-file return; findings ranked most-severe first; every section of §2's scope gets a coverage statement (reviewed / partially / not — with reasons). Due **Aug-8 EOD**.

## Section 1 — Read first

`CLAUDE.md` (repo root) · the MODULE_CONTEXT.md + `module-info.java` for: `core/automation`, `integration/integration-zigbee`, `core/persistence`, `core/event-bus`, `core/state-store` · the four s31-thread audits in `nexsys-hivemind/context/audits/` (2026-08-03 evidence read · 2026-08-04 blockR · R8-R9 addendum · night4 blockV) — they are the live evidence backdrop and carry the measured numbers (0.772 s window; 143 ms / 3.59 s settle confirms; ~4–5-min report cadence; the frozen-lastChanged night).

## Section 2 — Scope (the physics-touching spine)

- **A. Command confirmation** (`core/automation`, esp. `StandardPendingCommandLedger`): the confirmation calculus end-to-end — expectation selection (:737–:752 era), LIVE evaluation (:421–:442 era), the REPLAY path (:544 era) and its LIVE-equivalence, window/timeout arithmetic, supersession (ISSUANCE supersedes), terminal exclusivity, concurrency (virtual-thread + lock discipline), and the UNCONFIRMED register.
- **B. Zigbee availability + command path** (`integration/integration-zigbee`): the dispatch path from `DISPATCHED` to the radio; the availability tracker + ping arm (seeding, evidence marks, the 10-min gate, the 25-h battery window) under restart storms (the nightly's three-boot choreography is a natural harness — name anything it stresses); the port watchdog, esp. the observed shutdown-time `transport_failed → reopen` race (benign noise or a real hazard?); adoption/relink rehydration invariants.
- **C. Persistence write path** (`core/persistence`): WAL + pool topology vs the single-writer doctrine; crash-window contracts on multi-event emissions (format #15's class); checkpoint/restart interplay; anything the driver bump (S-5a, possibly landed) interacts with.

## Section 3 — Named seeds (confirm or refute, with evidence)

- **S-1 THE DELIVERY-PHASE GAP (from the night-4 no-edge verdict):** `DISPATCHED` records hand-off to the integration, not radio delivery. Verify at source whether the EZSP layer receives per-message send/delivery status (e.g. a messageSent/APS-ack surface) that the adapter discards. If yes: a HIGH-value post-gate candidate (delivery evidence in the lifecycle) — spec the seam, do not build it. If no: refute with the line evidence.
- **S-2 SAME-VALUE-REPORT CONFIRMATION:** the ledger confirms on ANY value-matching `state_reported` from the subject entity. On a chatty device (periodic same-value reports at minutes-scale), a turn_X toward the CURRENT state could be CONFIRMED by a periodic report that is not evidence of execution. Is there an input/state sequence where this produces a false-positive CONFIRMED that violates the never-false-CONFIRMED brand claim? Price it honestly (the bench's S31 cadence math is in the audits) — this is the one seed that touches the brand's core claim, so the evidence bar is highest.
- **S-3 THE BOOT-WINDOW CLASS:** is there a core-visible "mesh warm" signal (network-up age, first-command gating, route-table state) that candidate (iii) could consume? Survey only — a design input, not a design.
- **S-4 THE SHUTDOWN/WATCHDOG RACE:** the quiesced boots log `zigbee.transport_failed` + watchdog reopen DURING `hs-shutdown` (the port closed under it; one reopen landed on `/dev/ttyUSB0` mid-death). Trace the shutdown ordering — can the watchdog's reopen outlive or interleave with lifecycle teardown in a way that leaks a port handle, double-opens, or corrupts adapter state on the NEXT boot?

## Section 4 — Return shape

Frontmatter (status/provenance) → §1 verdict summary (counts by severity) → §2 findings (ranked; file:line + trigger + suggested disposition each) → §3 seed adjudications (S-1..S-4: CONFIRMED/REFUTED/PARTIAL with evidence) → §4 coverage statement per scope area → §5 NOTEs/observations → §6 what the reviewer would examine next (bounded, named). No code, no patches — findings and evidence only.
