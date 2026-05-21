<!--
file: context/pre-verifications/README.md
purpose: Explains the pre-WU verification artifact convention — what triggers one, what it contains, when it rotates.
audience: PM, Coder
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Pre-Verifications

The PM writes a pre-verification artifact here before issuing a coding instruction whose correctness depends on multi-module or signature-specific source state. The Coder reads it before executing. The artifact closes the source-vs-brief mismatch class (see `context/lessons/strategic-lessons.md` 2026-05-21 entry "M3.6d-a 7-mismatch discovery").

## Trigger

Create a pre-verification when **either** is true:

1. The WU touches **≥3 modules** (where a mistaken assumption in one module compounds across the others).
2. The brief depends on a **specific class signature, method shape, or visibility level** that's worth pinning to source before specifying — e.g., "expects `WriteCoordinator.queueSize()` to exist," "assumes `Lifecycle.Phase.STARTED` is a constant," "assumes `SqlitePersistenceLifecycle` constructs N stores."

Single-module narrow WUs with no cross-module shape assumptions don't need one. Use judgment; over-producing these is fine, under-producing is what failed M3.6d.

## Filename convention

`WU-<id>.md` where `<id>` matches the milestone or work-unit identifier — e.g., `WU-M3.6d-b.md`, `WU-M3.6e.1.md`. One pre-verification per WU.

## Content shape

Each entry in the file should list, per verified element:

- **Element:** type name, method, or visibility claim being verified.
- **Source location:** path + (optionally) commit SHA observed.
- **Observed signature:** the actual shape, copied or paraphrased from source.
- **Status:** `VERIFIED` (matches assumption), `VERIFIED-RETROACTIVELY` (matches after the work has shipped), or `ABSENT → MUST BE CREATED` (the WU includes creating this element).
- **Confirmation method:** how the PM checked — direct file read, grep, commit message, etc.

## Lifecycle

- **Created** by the PM during brief drafting, before the coding instruction is issued.
- **Read** by the Coder before executing the WU.
- **Status-shifted** to `state-type: history` after the WU's WUCP Phase 2 closes.
- **Rotated to archive** on the same cadence as the handoffs (monthly).

## Worked example

`WU-M3.6d-b.md` (retrospective seed against `dfb045e`) demonstrates the format using the three OR-M3-14 prerequisites.
