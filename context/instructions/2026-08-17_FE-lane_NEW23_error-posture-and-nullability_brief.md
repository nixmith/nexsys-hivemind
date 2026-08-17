<!--
file: context/instructions/2026-08-17_FE-lane_NEW23_error-posture-and-nullability_brief.md
purpose: THE WEEK-1 FE LANE — NEW-2 (error-posture enforcement app-wide) + NEW-3 (contract-vs-wire nullability, corpus-swept) + riders NEW-6/NEW-7. The first post-gate dispatch of the ratified semester program. Kills the reproduced July-27 incident class at the CLASS level, re-opens the why-not surface (the demo's canonical (b)), and installs the LIVE-WIRE VERIFICATION RULE (H8) as this lane's acceptance bar.
audience: a FRESH Cowork FE-lane session under /nexsys-frontend (NOT the hub; write-isolated; returns to the hub).
state-type: lane brief / dispatch (Phase-3 FE work; frontend.yml is the CI gate).
dispatch-line: "Read nexsys-hivemind/context/instructions/2026-08-17_FE-lane_NEW23_error-posture-and-nullability_brief.md and execute it. - /nexsys-frontend"
baseline: homesynapse-core `d26777c` (main; HEAD==origin/main at authoring). All work in `web-ui/dashboard/`. ZERO core-Java changes — any apparent need for one is a STOP + escalate finding, never an edit.
due: Wed 2026-08-19 EOD (graceful degrade: a partial return with the census honest beats silence).
return: `context/audits/2026-08-17_FE-lane_NEW23_return.md` (ONE file, uncommitted; the hub stages it). Returns file to context/audits/ — state this in your frontmatter.
laws: technical pushback WELCOME (flag, never silently implement what you believe wrong) · the v1.1 read-API contract is FROZEN — this lane is consumer-side ONLY (see charge 2's framing) · the five-modes verdict vocabulary and all honesty copy laws in the FE skill govern · L3 — no token material ever enters the session · a11y + design tokens per the FE skill · deviations declared in the return, never silent.
-->

# FE Lane — Error Posture + Nullability (NEW-2/NEW-3 + riders)

## §0 Evidence base (READ FIRST, in order)

1. This brief, whole.
2. `context/audits/2026-08-16_G1_rehearsal_complete-record_and_gate-day-brief.md` **§4.5, §5 (DX-14/15/16), §6 WHOLE** — the four-link defect chain this lane closes, with every claim at file:line. The hub layer-2-verified §6's cites at the git objects on 2026-08-16; trust them, then re-verify at your own checkout (truth hierarchy: source wins).
3. The FE skill + its references (you are under /nexsys-frontend; its contract-consumer and honesty-copy laws bind).
4. Source, at your checkout: `web-ui/dashboard/src/app.tsx` · `components/ErrorBoundary.tsx` (its header comment IS the law you are enforcing) · `components/AppShell.tsx` · `views/WhyNotView.tsx` · `views/RunChainView.tsx` (the one existing mount — your reference pattern) · `lib/api/contract.ts` · `lib/poll.survival.test.tsx` (the red-first test shape to extend) · `components/Resource.tsx` + `lib/feedback.tsx` (the honest fetch-failure path — the counter-exhibit that already works).

## §1 Charge 1 — NEW-2: the error-posture law, enforced app-wide

**The defect class:** `ErrorBoundary` is documented LOAD-BEARING ("neither is ever a silent blank or an eternal spinner") and is mounted in exactly ONE of nine views (`RunChainView.tsx:26`). The 2026-07-27 incident reproduced verbatim on `WhyNotView` at the G1 rehearsal because the fix was applied to the surface, not the class (arc-discipline 25's named pattern).

**The work:** mount `ErrorBoundary` at the view-switch level (in `app.tsx`'s `renderView()` or in `AppShell` — your call on placement, justified in the return; preserve per-view `resetKey`/`onRetry` semantics so a view change or retry clears a contained error). **Red-first:** for EVERY view, a test proving a render throw inside that view degrades to the honest render-failure card and does NOT kill the app or the polling loop — the `poll.survival.test.tsx` shape extends; each new test is shown FAILING at baseline in your return (green-by-construction exceptions disclosed per the preservation-fixture rule). The eternal-spinner state becomes unreachable by construction: after this lane, no view can render an unresolved `Loading…` past a thrown render.

## §2 Charge 2 — NEW-3: contract-vs-wire nullability, corpus-swept

**The defect:** `contract.ts:350` declares `lastEvaluation: { at: string | null; conditionsResult: string | null }` non-nullable; the deployed wire sends `"lastEvaluation": null` (proven at the rehearsal: 200 OK / 395 B / 17 ms with the full body on record). The type system concealed the need for a guard; the mock that always populated the field manufactured the false type (H8's origin exhibit).

**Framing — state this in your return so no one misreads the act:** the v1.1 wire contract is FROZEN and the SERVER is its reality. Correcting `contract.ts` to declare what the wire actually sends is a CLIENT-TYPE correction toward the frozen truth, not a contract change. Nothing server-side moves.

**The work:** (a) correct `contract.ts:350` to `| null`; (b) guard both `WhyNotView` dereferences (`:88` and the `conditionsResult` sibling) rendering the null case honestly (the row simply doesn't render — absence, not fabrication); (c) **THE CORPUS SWEEP (arc-discipline 25, mandatory):** enumerate every FE dereference of a contract-declared-non-nullable field the server can null — walk `contract.ts` type by type against the server's serialization reality (the v1.1.2 comments in `contract.ts` themselves flag OPTIONAL/nullable semantics; where the wire truth is unknowable from the FE side, LIST the field as UNVERIFIED-AT-WIRE rather than guessing) — and fix every found site with a fixture proving its null case renders honestly. The sweep's enumeration table (field · site · verdict · fix/fixture) is a REQUIRED return section; "fixed the two open files" without the sweep is the exact failure mode 25 names.

## §3 Charge 3 — the riders (small, same lane)

**NEW-6 (device-detail copy):** fix the self-contradiction — prose `"last heard from —"` beside table `"Last reported: 9:40 AM"` (the availability-honesty surface must not claim ignorance a row disproves); add dates to clock-only stamps where a report can be >24 h old. **Do NOT touch the `Updated X ago` mechanism** — DX-22 is an open question with a named post-gate discriminator; changing it now would be theorizing at the silence. **NEW-7 (Activity nav → unbuilt endpoint):** PROPOSE the disposition in your return (options: keep-as-is with the honest 404 · feature-flag the nav item until the endpoint ships · label it "coming" honestly) — the hub rules; do not unilaterally remove a nav surface.

## §4 The acceptance bar — H8, THE LIVE-WIRE VERIFICATION RULE (this lane's DoD)

Every surface this lane touches carries a live-wire verification plan, in two tiers, both REQUIRED in the return:

1. **Real-payload fixtures NOW:** the rehearsal's captured wire bodies are REAL payloads — the non-firing response (§4.5 of the rehearsal record, byte-complete) becomes a fixture VERBATIM, labeled with its capture provenance. Any other real captures on record (the WCAP returns) are fair game. A mock hand-authored to be convenient does not satisfy this tier.
2. **The live re-exercise plan:** a short scripted browser pass (surface · URL · expected rendering · what would falsify) for Nick to run against the Pi after the next warm rebuild/deploy. **This lane's scope is repo-only — no deploy.** Your return therefore concludes the touched surfaces as **REPO-COMPLETE, LIVE-VERIFICATION PENDING THE DEPLOY** — per H7, they are not "verified" until measured live, and the return says so in those words rather than rounding up.

## §5 Gates + return contract

`frontend.yml` GREEN on the push = the CI gate of record. The return (ONE file at the named path): (1) the changed-file census, exact; (2) the sweep enumeration table (§2c); (3) the test census with red-first evidence per test; (4) fixture provenance (real-wire labels); (5) the NEW-7 proposal; (6) the live re-exercise plan (§4.2); (7) deviations declared; (8) the route-back line: "Intakes at the hub for two-layer audit; the deploy + live re-exercise ride the next Pi trip." Refutation welcome in both directions. If anything in this brief contradicts source at your checkout, SOURCE WINS — flag it in the return rather than obeying the brief into an error.
