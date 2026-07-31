<!--
file: context/handoff/2026-07-30_FE-LIVE-V112-item1_lane_session_prompt.md
purpose: Dispatch brief for a fresh Cowork FRONTEND lane executing FE-LIVE-V112 **item 1 ONLY** — the causal-chain render hardening that is the last named G1 gate-day blocker. Write-isolated to web-ui/dashboard/**.
audience: a fresh Cowork lane loading `nexsys-frontend`; Nick (launcher); the PM hub (intakes the return at v41).
state-type: session prompt (lane dispatch, single-charge)
status: READY — authored 2026-07-30 (v41 hub, beat 1). Nick approved the parallel launch and the item-1-only slice.
returns-to: `context/audits/2026-07-30_FE-LIVE-V112-item1_return.md` (the standing returns-file law).
skill: `nexsys-frontend`. The account-synced copy is CURRENT at v1.8 (39,453 bytes — byte-matches the skills-pass-2 landing). **This lane does NOT gate on Nick's local mirror sync** — that gates host-CC lanes; a fresh Cowork lane loads the account-synced copy, verified current at the v41 beat-1 preflight.
parallel-safety: this lane runs CONCURRENTLY with the B2 bench adjudication and touches nothing it touches. Zero core files, zero bench files, zero contract files, zero hivemind spine writes.
-->

# Lane Brief — FE-LIVE-V112 item 1 (the causal-chain render hardening)

You are a **frontend lane** (`nexsys-frontend`), write-isolated, single-charge. You do not implement anything outside this brief's scope. You return to the hub; you commit nothing.

## §1 The charge, in one paragraph

The dashboard's causal-chain view **crashes on live data**. The wire is healthy and the payloads are populated — the defect is entirely client-side. Your charge is to make the chain view survive the payload shapes production actually emits, and to make it *honest* about what it is showing when it cannot render a chain. That is three things: **null-guards** on the fields that throw, **an error boundary** so a render throw cannot take the application down with it, and **an honest empty state** that distinguishes the reasons a chain is not on screen. Nothing else.

This is the **last named blocker on gate row G1**. It is small. Do it exactly, and do not grow it.

## §2 The evidence — read this before writing a line

Read in this order:

1. `context/audits/2026-07-27_devtools-chain-glance_return.md` — the filed instrument reading. **This is your primary source.** It records: the SPA's own 10 polls returning 304s against a chain proven populated; the client throwing on `toLowerCase` applied to a null in the chain render; and the crash killing the polling loop, which is why the UI then appears frozen rather than merely blank.
2. `context/handoff/pm-handoff.md` v39 beats 8 and 9 — the WCAP-2 measurement (**fresh runs hydrate 3/3**, 1693–1717 B against the 507 B skeleton) and the beat-9 adjudication that resolved the G1 watch to this item.
3. The FROZEN v1.1 dashboard read-API contract, and the mock fixtures under `web-ui/dashboard/`.

**The seam, stated precisely.** Live payloads carry optionals that are **present-but-null**. The mocks have never emitted that shape — they emit either a populated field or an absent one. The SPA was written against the mocks, so a `null` where the code expects `string | undefined` reaches a string method and throws. This is a **tri-state** problem (populated / present-but-null / absent), not a binary one, and a fix that only handles absence will pass your tests and fail in production exactly as the current code does.

**There is a second, older mechanism you must NOT chase.** Action hydration follows the event ERA — runs from before the 2026-07-19↔25 correlation-stamping boundary hydrate differently, and that is a known history artifact tracked separately as a P3 core-side look. If you find a chain that is legitimately sparse because it is old, that is not your bug. Render it honestly and move on.

## §3 Scope — IN

Everything below is confined to `web-ui/dashboard/**`.

1. **Null-guards on the throwing paths.** Find every site in the chain render that applies a method or property access to a value the live contract permits to be null. Do not patch only the reported `toLowerCase` — sweep the render path for the class. (The corpus-sweep discipline: fixing only the occurrence you were handed is how occurrence six survives to production.) Enumerate what you found in the return.
2. **An error boundary** around the chain view, such that a render throw is contained and — critically — **the polling loop survives it**. The loop dying is what turned a cosmetic defect into an apparently-hung application. Prove the loop survives, do not assume it.
3. **An honest empty state.** This is the part that is a product decision, not a defensive one, and it is the part to get right. The whole promise of this product is that it tells you the truth about what it does and does not know. A spinner that spins forever, or a blank panel, or a silently-swallowed error, is that promise broken in the one view that exists to demonstrate it. The view must visibly distinguish, in the user's language:
   - **the request failed** (network/HTTP error — say so, and let the user retry),
   - **the chain is empty** (a real, successful, genuinely empty response),
   - **the chain is partial** (present-but-null or era-sparse fields — show what resolved and mark what did not, rather than hiding the row or inventing a value).

   Never display a placeholder that could be mistaken for data. An honest "not recorded" outranks a plausible-looking blank every time.
4. **Fixtures for the shape that actually broke.** Add mock fixtures emitting **present-but-null** optionals, plus an empty chain and an error response. The existing mocks are structurally blind to the live failure mode; without these your tests prove nothing about it.
5. **Red-first.** Write the failing test that reproduces the null crash *before* the fix, and record its red output in the return. House law: tests before implementation, and a fix with no test that could have caught it is not landed.

## §4 Scope — OUT (each of these has an owner; none of them is you)

- **FE-LIVE-V112 items (a)–(g) and (i)** — out. This lane is item 1 alone.
- **Item (h) is specifically and deliberately excluded**: it couples to the **STATE-DIALECT** ruling (the `/state` wire serves a third dialect; three dialects, nobody contract-true). That ruling has not been made and is a core-P2 work unit with its own bench scenario-sweep rider. **Do not change how any value is parsed off the wire, and do not "fix" a dialect mismatch you notice.** File it in the return as an observation; the hub disposes.
- `firingValue: null` — observed across all eras, already minted as its own row, priority ruled at STATE-DIALECT authoring. **Guard it so it cannot throw; do not otherwise act on it.**
- The favicon rider and the npm-audit advisory — out.
- Any core, bench, docs, or hivemind file. Any change to the FROZEN v1.1 contract. Any new dependency.

## §5 Gate and environment

- The gate is `npm run verify` in `web-ui/dashboard` (tokens, lint, typecheck, test, build, bundle, contract check), CI-enforced by `frontend.yml`, path-filtered to `web-ui/dashboard/**`.
- **Your green is not the gate of record.** CI on the pushed commit is, and Nick's native host run outranks any sandbox result. State your gate output verbatim; claim nothing beyond it.
- **Known sandbox hazard (env-model §9):** esbuild's native binary SIGSEGVs in this sandbox class. If the build dies there, the working pattern is a `/tmp` copy proven byte-identical to the mount, with an `esbuild → esbuild-wasm` override applied **to the build copy only** — the committed tree stays native, and the lockfile is not to be regenerated as a side effect. Also check free disk before `npm ci`; the shared disk has hit 100% before.
- Read `context/process/cowork-environment-model.md` before your first write. Lock-free porcelain only, flag spelled: `git --no-optional-locks status --porcelain`.

## §6 The return

File `context/audits/2026-07-30_FE-LIVE-V112-item1_return.md` carrying: the enumerated throwing sites you found and what each was guarded with; the red-first evidence (the failing test, its output, then green); proof the **polling loop survives** a contained throw; the three empty-state cases with what each renders; the new fixtures and what shape each emits; your verbatim gate output; every deviation, severity-honest ([REVIEW] vs [INFO]); any dialect or contract observation you are forbidden from acting on; and the **exact porcelain census** (lock-free) with a per-file mapping to a claimed deliverable, plus the explicit `git add` command listing every path by name. Never `-A`. No attribution trailers on the commit message — no `Co-Authored-By`, no AI-attribution, no session links, in any repo.

Nick commits; you do not.

## §7 Done-when

G1's last named blocker is retired when: the chain view renders a populated live-shaped payload without throwing; a present-but-null payload renders honestly rather than crashing or lying; an error and an empty response each produce their own truthful state; the polling loop provably survives a render throw; and `npm run verify` is green with the output quoted. Anything short of that is a partial return — say so plainly rather than rounding up.
