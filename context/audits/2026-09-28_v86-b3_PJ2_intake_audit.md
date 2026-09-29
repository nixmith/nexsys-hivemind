<!--
file: context/audits/2026-09-28_v86-b3_PJ2_intake_audit.md
purpose: PJ-2's intake two-layer at the bytes of the pushed branch (pj2/pairing-window-endpoint, ed26a4c + cf86802; PR #7) — the return's §0 against the instruction's §0 contract, the file table, the safety properties, the four REVIEW deviations ruled, the landing card cut.
audience: the hub · Nick (§0) · v87 (WUCP Phase 2 on the landing)
state-type: audit (filed once)
status: FILED — v86 beat 3 (Mon 2026-09-28 ~20:0x CT; instrument 2026-09-29T01:07:59Z). Layer 2 = the hub's own git fetch of the public branch into its container and the greps below; the return copied verbatim from commit 2 into `context/audits/2026-09-28_PJ2_return.md`.
-->

# v86 beat 3 — PJ-2 intake at the branch (Mon 2026-09-28 ~20:0x CT)

## §0 The verdict
**ACCEPT-WITH-NOTES.** The branch is what the lane said: commit `ed26a4c` = 33 files (22 M + 11 A; +2,295/−229) = the instruction's §3 table (30 rows incl. 19b/19c and the six MODULE_CONTEXT files) + the three count-pin test files of deviation D1; commit `cf86802` = the return alone (`docs/lane-returns/2026-09-28_PJ2_return.md`, 31,409 B, its last line `RETURNED …`). Trailer grep on both commits: 0. `git diff 40412f9 ed26a4c -- '**/module-info.java'`: 0 bytes. No `EventCategoryMapping`, migration or hash-namespace file in the diff (LOCK-1 safe). The safety property at the bytes: the adapter's `openPermitJoinWindow(` count 4 → 0 (the boot-time window is gone); `warnIfPermitJoinKeyConfigured();` at :525 on the start path; the WARN `zigbee.permit_join_key_ignored` at :915; the three CAS closers (:949, :999/:1001, :1010, :1027) each publish one `permit_join_closed`; `implements PairingWindowControl`. The endpoint (`PermitJoinEndpoint` :44–:49, `PORT_TIMEOUT` 5 s :59) maps not-running/no-supervisor/timeout/adapter-throw → 503, unsupported → 409, a bad body → 400, and reserves 500 for the port itself; wired in `HomeSynapseCore` :1123. The four REVIEW deviations are ruled in §2; the landing is a squash under Nick's identity (§3). The author on the branch is the VM's (`Claude <noreply@anthropic.com>`) — replaced by the squash, never merged as-is.

## §1 Layer 1 → Layer 2
| The lane's claim (§0 of the return) | The hub's re-execution |
|---|---|
| 33 = 22 M + 11 ?? at porcelain, the list printed | `git diff --name-status 40412f9 ed26a4c`: 22 M + 11 A, the same 33 paths |
| `check` green; the seven gate lines; the XML census | NOT re-executed (the VM's build); CI on the landing sha is the gate of record |
| module-info diff empty | re-executed: 0 bytes |
| the red-first in three stages with texts | read at §0/§2 of the return; not re-run |
| T7 green-by-construction + a throwaway round-trip instrument (snake_case `closes_at`) | consistent with the A2 return's finding on the store's keys |
| `RETURNED nexsys-hivemind/context/audits/2026-09-28_PJ2_return.md 31409` | the file is on the branch at `docs/lane-returns/`; copied verbatim into `context/audits/` (31,409 B) by this beat |

## §2 The deviations ruled
- **D1 [REVIEW] → ACCEPTED.** `EventTypesTest` :44/:46 (73 → 75), `EventTypeRegistryTest` and `JacksonWarmupTest` (55 → 57) — count pins outside the file table that two new event types must move; mechanical, named with their lines and red texts. The miss is the hub's pre-verification (WU-PJ2 listed twelve signatures and no count pin) → **IR-98**.
- **D2 [REVIEW] → ACCEPTED as §1.6.** An adapter throw is 503 `INTEGRATION_UNHEALTHY` naming the class and message, never 500 (E9's word). Row 14's "anything else → 500" was the instruction's own inconsistency, which the review E1–E14 did not catch → **IR-99** (one status table per instruction; the review's checklist gains "the status codes appear once").
- **D3 [REVIEW] → HELD for the docs card.** `permit_join_opened/closed` resolve to the `[SYSTEM]` fallback of `EventCategoryMapping` (:55–:56, :230–:231); the lifecycle siblings are `[SYSTEM, DEVICE_HEALTH]`. A Doc 01 §4.4 row decision (the hub's), then a one-line mapping edit in a later Java unit → **IR-100**.
- **D4 [REVIEW] → ACCEPTED.** The fourth WARN token `zigbee.permit_join_close_failed` (:1039) on the shutdown close's best-effort catch; §9.9's three tokens stay exact and once each; the MODULE_CONTEXT rows carry the fourth (the lane's row) — the docs card lists it.
- **[INFO] I1–I8 and §5 F1–F7:** not read this beat (the context rule); v87 reads them at WUCP Phase 2. F1 restates THE BENCH FENCE: after the landing a key-driven card opens nothing — BH-3 before PJ-2's core reaches the Pi.

## §3 The landing
`context/instructions/2026-09-28_core-card_PJ2-LANDING_squash-to-main_operator-card.md`: `git merge --squash origin/pj2/pairing-window-endpoint` on `main` at `40412f9`, the return directory dropped from the index (`git rm -rq docs/lane-returns`), `staged: 33`, the trailer grep on the hub's message file (`_scratch/v86/2026-09-28_core_PJ2_commit-msg.txt`), `git commit -F`, the push. `CORE: LANDED <sha>`; CI on the push is the gate (the closure counter's 18th line when green); PR #7 closed by Nick as landed. The coder-handoff entry (the return's §6) and a coder-lessons line are filed by this beat; the VM's hivemind edits are not recovered (the return carries them).

## §4 Not re-executed (disclosed)
The build and every test (the VM's; CI on the landing decides); the eight [INFO] rows; the schema description's text; the six MODULE_CONTEXT rows' wording (read at Phase 2).
