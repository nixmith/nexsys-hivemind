<!--
file: context/audits/2026-09-06_TR-0_intake_two-layer-audit_v66-b5.md
purpose: The hub's two-layer audit of the TR-0 return (the actuation chokepoint census at 093d5b4) under the program §5's pre-filed predictions P1–P4; the B-2 shape RULED on its receipts; the side-findings → docket rows.
audience: the hub · the B-2 charter (when C-003 is minted and the fence has closed — not before) · Nick (the rows, by pointer)
state-type: intake audit
status: FILED v66 beat 5 (Sun 2026-09-06 ~11:2x CT; instrument 2026-09-06T16:1xZ). Return: context/audits/2026-09-06_TR-0_actuation-chokepoint-census_return.md (10,225 B; RETURNED 16:07Z). Verdict: ACCEPT — P1–P4 all HOLD at the bytes; the B-2 shape RULED: a bounded insertion at ONE line.
-->

# TR-0 intake — two-layer audit (v66 beat 5)

## §0 Verdict card
**ACCEPT.** Every receipt the hub re-executed resolves at `093d5b4`: `commandHandler()` has ONE production call site (`CommandRoutingSubscriber:215`) and `handler.handle(command)` ONE (`:249`); `CommandEnvelope` is six fields (`entityRef` · `commandName` · `parameters` · `commandEventId` · `correlationId` · `integrationId`) and the word `principal` does not occur in any `src/main` Java file; `.adapter()` has ONE production call site (`:215`). **P1–P4 HOLD** as the return adjudicates them (P3 sharpened: `command_dispatched` stamps `origin=AUTOMATION`, `actorRef=null` for EVERY command, REST-issued ones included — `StandardCommandDispatchService:233–:235`). **THE RULING THE PROGRAM §1.3 ASKED FOR: B-2 (the policy kernel's gate) is a BOUNDED INSERTION AT ONE LINE — immediately before `CommandRoutingSubscriber:249`, reached only through `:235–:236`; not a refactor.** The precondition gap stands as the lane names it: the gate would see no principal today (§3 below → a row). The return is 10,225 B against a ≤10 KB cap (10,240) — under by 15 B (the b5 mint, third time today). **Disclosed non-re-executions:** the `command_dispatched` producer count (SCDS:221/:165) read at the return's cites, not re-grepped whole (the hub's grep sampled javadoc hits only); the four MODULE_CONTEXTs the lane scanned by heading were not re-read.

## §1 Layer 2 — at the bytes
| P | The hub's instrument | Result |
|---|---|---|
| P1 | `git grep -n 'commandHandler()' -- '*/src/main/*.java'` → the interface `:122` + CRS `:215` + the Zigbee provider `:450`; `git grep -n '\.handle(command)'` → CRS `:249` only | HOLDS |
| P2 | read at the return's receipts (SCDS `:221`/`:165`; `.dispatch(` zero production callers; scenes/invoke throw `UnsupportedOperationException` at SAE `:222–:225`) | HOLDS (read, not re-grepped) |
| P3 | `CommandEnvelope.java:55–:62` six components; `git grep -ci principal -- '*/src/main/*.java'` = 0 | HOLDS, sharpened |
| P4 | `git grep -n '\.adapter()' -- '*/src/main/*.java'` → CRS `:215` only | HOLDS |

## §2 The ruling (recorded for the B-2 charter; no code before C-003 + the fence closed — the adopted law)
**B-2's shape = one gate call immediately before `CommandRoutingSubscriber:249`** (`handler.handle(command)`), on the run of `:235–:236`. Everything that actuates passes it: REST (`IssueCommandEndpoint:213–:220` → `command_issued`) and the automation engine (`StandardActionExecutor:264–:277` → `command_issued`) both reach the ONE `command_dispatched` producer (`StandardCommandDispatchService`) and then the subscriber. **What the gate would SEE today:** the six envelope fields — an entity, a command, its parameters, the issued event's id, the correlation, the integration — and NO principal. **The precondition (the "principal grammar"):** carry `origin` + `actorRef` from the issued envelope into `CachedCommand` (`:305`) and either into `CommandEnvelope` (a PUBLIC integration-api record → a Phase-2 interface change, an AMD) or gate at `:232` on the cached issued envelope (no interface change). The hub's lean, recorded not ruled: **gate at `:232` on the cached envelope first** (zero interface change; the AMD later if adapters ever need the principal).

## §3 The side-findings → docket rows (the hub's numbering; the addendum carries them at its next beat)
- **TR0-1 `[REVIEW]` — two causation conventions on one field.** `CommandEnvelope.commandEventId`'s javadoc (`:46–:49`) says "the originating `command_dispatched`"; the router passes the `command_issued` id (`CRS:182/:229`) and the Zigbee handler chains `command_result` to it (`ZigbeeCommandHandler:334/:345–:346`), while the router's OWN failure results chain to the `command_dispatched` id (`CRS:203–:204`). A javadoc fix now (one line, the coder's next touch of `integration-api`); the convention itself is a B-2 REJECTED-result question — decide there.
- **TR0-2 — the principal precondition** (§2): a charter row under B-2, not a WU now.
- **TR0-3 — `command_dispatched.origin` is not evidence-based:** `SCDS:234` stamps `AUTOMATION` for REST-issued commands too (Doc 01 §3.9; `EventOrigin.java:11–:13`). Inherit the issued envelope's origin at `:176–:177` (or stamp `SYSTEM`) — a small core WU (**ORIGIN-1**) with a value correction on a frozen-shape event (no key change; the value becomes true). Charter after F-R4-1b lands (one lane on the core tree); the hero's "why did it fire" reads this field.

## §4 What this closes and opens
Closes the program §1.3 question (bounded insertion: YES). Opens ORIGIN-1 (a candidate core WU), TR0-1 (a javadoc line), TR0-2 (a B-2 charter row). Nothing for Nick's hands.
