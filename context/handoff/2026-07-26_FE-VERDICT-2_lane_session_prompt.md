<!--
file: context/handoff/2026-07-26_FE-VERDICT-2_lane_session_prompt.md
purpose: Dispatch brief for the FE-VERDICT-2 Cowork lane — consume the ruled v1.1.2 contract deltas on the explanation surfaces, render the five honest failure modes DISTINCT (Nick's 2026-07-25 law) on WCAG-clean mode-paired tokens, close G2 [S] (the availability tile renders the honest states), and bank the dashboard-deps watch. Authored by the v38 hub (beat 2); v38 charge 4.
audience: a FRESH Cowork conversation (nexsys-frontend skill — load it first; it is the lane's constitution); the PM hub (two-layer audit on return); Nick (launch + the return paste).
status: READY TO LAUNCH — parallel-safe (write-isolated; zero core/bench writes; core stays serialized on SKIP-VIS).
baseline: core `4bc1258` (the two dependabot web-ui merges are IN — the deps watch item this lane closes); the SKIP-VIS core WU is AUTHORED but NOT LANDED — law (c) below governs the gap.
write-isolation (ABSOLUTE): this lane writes ONLY under `homesynapse-core/web-ui/dashboard/` + ONE return file at `nexsys-hivemind/context/audits/2026-07-26_FE-VERDICT-2_lane_return.md`. No other hivemind file, no core Java, no bench file, no commit — the return routes to the hub's two-layer audit first.
-->

# FE-VERDICT-2 — the honest-verdict rendering lane (v1.1.2 consumption · five-modes-distinct · G2)

## 0. Constitution (read IN FULL, in this order, before any write)

1. The **nexsys-frontend** skill (your role; its §4a ten-value vocabulary + §4b identity-durability + §4c explanation-surface field evidence are the currency layer — re-verify each cited fact at source per its own rule).
2. `nexsys-hivemind/context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md` — the FROZEN v1.1 contract (the base that stays byte-stable).
3. `nexsys-hivemind/context/decisions/2026-07-22_nick-rulings-1-5_verbatim.md` **ruling 1** — the v1.1.2 four-constraint law. Law (c) verbatim-class: *the emitter leads, the consumer follows — you consume OBSERVED payloads; where the core has not emitted yet, you MOCK to the ruled v1.1.2 shape and FLAG, never invent beyond it.*
4. `nexsys-hivemind/context/instructions/2026-07-26_SKIP-VIS_explanation-honesty_coding-instruction.md` — **the ruled v1.1.2 shape you consume** (the emitter's spec): additive `resultOutcome` on causal-chain actions; additive `noCommandsIssued` on non-firing; `triggeredAt`/`lastEvaluation.at` VALUE corrections; the five-modes signature table (your rendering input); DP-4 `settled` is ⛔ GATED — if the dispatch turn says GO it will exist, else derive provisionality client-side per the rule stated there. **Until SKIP-VIS lands on silicon, every one of these is MOCK-ONLY for you.**
5. Your own prior return: `nexsys-hivemind/context/audits/2026-07-19_explainability-ux-lane_return.md` — you wrote GAP-1..5 and D-1..D-5; this lane retires D-4's limitation and swaps `classifyRecordedReason` recovery to the first-class field.
6. The Rosonway evidence: `nexsys-hivemind/context/handoff/2026-07-25_rosonway-topology-move_I3b_bench-session-report.md` §5.1 (the five-distinguished-failures exhibit — your hero material), §5.3 (**AVAILABLE ≠ RX proof; `staleAfter: null`** — render availability honestly, never as live-contact proof), §5.9 (the provisional-outcome window — what you render while an outcome may still settle).
7. The brand lane's WCAG deliverables (token values live HERE — pointer-not-copy, read at source): `nexsys-hivemind/context/assessments/2026-07-22_brand-program_lane_return.md` (the light-mode failure finding + the corrected MODE-PAIRED token values) + `nexsys-hivemind/context/strategy/brand-program/2026-07-22_identity-system_exploration.md` (the token system). Constraint: rename-readiness — every UI string stays token-parameterized; never hardcode the brand.

## 1. The law of this lane (Nick, 2026-07-25 — verbatim-class)

**The five honest failure modes render DISTINCT, never collapsed — the distinction IS the product:** dispatched-and-timed-out · superseded-same-attribute · acked-then-silent-forever · held-DISPATCHED · settled-FAILED-on-window-close. The SKIP-VIS instruction's signature table gives you the wire tuples `(outcome, resultOutcome, reason)` for each. Design law on top of it, per the §3a ALL-USERS/CVD mandate (the brand addenda): **the distinction NEVER rides hue alone** — each mode gets a distinct label + shape/icon; color reinforces, in BOTH themes, at AA contrast on the corrected mode-paired tokens. A provisional outcome (§5.9: DISPATCHED that may still settle) renders as visibly provisional — the calm honest-can't-know register, never a settled pill.

## 2. Scope (IN)

1. **The verdict/outcome rendering pass:** consume `resultOutcome` endpoint-by-endpoint (causal chain first); retire the D-4 recovery limitation (`classifyRecordedReason` swaps to the first-class field where present, keeps the recovery path as fallback for pre-v1.1.2 payloads — additive consumption, graceful degrade); render the five modes per §1; render `SKIPPED` actions and the `noCommandsIssued` non-firing marker honestly (a do-nothing run is NEVER a clean success tile — the silent-skip class, frontend-skill §4c).
2. **G2 [S] — the availability tile renders the honest states** (the criteria row's own words: integrates F with G): UNKNOWN-at-boot as honest, UNAVAILABLE-on-evidence, AVAILABLE **without** implying live radio contact (§5.3: `staleAfter: null`, `lastReported` may be hours old — surface the age, not a false liveness claim). This row's demo evidence is the lane's deliverable; the hub re-statuses the ledger row.
3. **The provisional/settled rendering** (§5.9): if DP-4 `settled` arrives GO, key on it; else derive client-side (`outcome === 'DISPATCHED' && (!resultOutcome || resultOutcome === 'acknowledged')` ⇒ provisional) — the SAME rule the core instruction states, so the swap to the field is a one-liner later.
4. **Mocks:** extend the existing mock layer to the ruled v1.1.2 shape (both new keys, both value corrections), clearly marked MOCK-pending-SKIP-VIS-landing; every mock-consuming surface FLAGGED in the return (law (c) discipline).
5. **The dashboard-deps watch:** `npm ci` against the dependabot-bumped lockfile (`4bc1258`), full build + existing test suite green, one line in the return — the standing watch item closes on your evidence.
6. **The FE-4-style visual sweep:** both themes, AA spot-check on every NEW/CHANGED surface (the corrected tokens), keyboard reachability on anything interactive.

## 3. OUT (hard fences)

Core Java (SKIP-VIS is the serialized core lane — never touch it) · the bench · any wire-shape invention beyond the ruled v1.1.2 spec (a needed-but-unruled key = FLAG in the return, build nothing) · the frozen v1.1 base keys (byte-stable) · availability SEMANTICS (render honestly what the API says; the availability≠reachability divergence is a design question routed elsewhere) · brand-final decisions (R-1 HELD; tokens stay swappable) · any commit (the return orders none; the hub audits first).

## 4. Deliverables + return contract

Code under `web-ui/dashboard/` (components/tokens/mocks/tests per the skill's conventions). ONE return file at the write-isolation path above, carrying: the §10-style exact file census (the hub's pre-commit audit consumes it) · per-mode screenshots or storybook refs BOTH themes · the AA numbers on changed surfaces · the deps-watch evidence line · every law-(c) FLAG · your own next-WU pointer (refuse-to-close). Two-layer audit precedes any commit; expect layer-2 source spot-checks against your quoted evidence.

## 5. Sequencing truth (so the lane never blocks)

You are parallel-safe NOW: everything IN-scope renders against mocks pinned to the ruled shape, and the swap-to-live is designed to be a flag flip when SKIP-VIS deploys. If the SKIP-VIS DP-4 ruling (GO/OUT) has not reached you, build the client-side derivation (it is identical either way) and note which branch you shipped. G2's demo may run against the LIVE deployed `4bc1258` read surface (availability needs no SKIP-VIS delta) — do that half live, not mocked.
