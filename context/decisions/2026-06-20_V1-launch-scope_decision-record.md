<!--
file: context/decisions/2026-06-20_V1-launch-scope_decision-record.md
purpose: The ratified V1 launch-scope decision record — the thin-slice MVP, the IN/OUT line, the backward-scheduled timeline, the parallel-lane model, the corrected build sequence, the enabling investments, and the open items. The forcing function that keeps scope disciplined toward Nov 25.
audience: Nick, PM hub, the Core / Web UI / Distribution lanes, the DOCS/design lanes
state-type: decision record
status: RATIFIED 2026-06-20 (strategy forks ruled by Nick); **D-OPEN-1/2/3 RESOLVED 2026-06-21 (Nick) + the wave sequence SET — see ## Open items and ## Wave sequence below**. Supersedes nothing; sits above the milestone backlog as the scope authority.
-->

# V1 Launch Scope — Decision Record (2026-06-20)

## The reframe (the anchor sentence)

**The differentiator is a UX surface, and we have been building it where no one can see it.** The product is the demo, and the demo is the **explainability view over a live automation running real devices**. Everything sequences backward from that sentence. The honest unit of progress is no longer "another Core milestone GREEN" — it is: *a stranger installs this, pairs a sensor and a light, watches an automation fire, clicks "why did this fire?", and understands the answer.* Nothing built so far moves that needle on its own.

## Decisions ruled (Nick, 2026-06-20)

**D1 — Fixed date, flexible scope. Thin slice, hold Nov 25.** A hard date with scope as the release valve is the correct discipline for our failure mode: Core had no deadline pressure, so it expanded to fill available depth and the user-facing lanes went to zero. Re-introduce the date and force the cuts. Rejected: *minimal* (a product without the differentiator visible is a worse Home Assistant — no reason to exist) and *slip the date* (removes the forcing function precisely when we have proven we cannot self-regulate scope without one — "slip" drifts, it does not converge). Slip is held only as a **controlled fallback**, taken — if at all — as a defined decision at the mid-point checkpoint, never as a November panic.

**D2 — Three parallel lanes, shaped.** Core (serial Coder), **Web UI sustained**, **Distribution skeleton-then-ramp**. Staying Core-first is the strategy that already failed. See "The lanes" below for the shape.

**D3 — Differentiator = explainability hero + two supporting surfaces.** The "why did this fire? / why didn't it?" causal-chain view is the unmistakable hero (the thing a stranger immediately gets and that Home Assistant visibly cannot do well). The other two Doc-16 surfaces are *present, not built out*: expressiveness shows as **component-based automation definitions** in the automation list; run-coupled reliability shows as **deterministic terminal state + recorded reason** on run outcomes. Hero + two supporting; nothing fully built out.

**D4 — Corrected build sequence (Core lane): M7.2a → M7.2b → thin causal-query API → AB-4 → M9 → validation.** AB-4 moves **before** M9 (was after). Complete the trust story, then turn on real-world inputs. (See "Sequencing rationale" — the binding reason is trust-hygiene, corrected from the original "fail-closed" framing.)

**D5 — Enabling investments come first (the first ~1–2 weeks).** The parallel model rests on machinery that does not exist yet: (a) **CI as the gate-of-record** (already exists — `./gradlew check` on push; adopt it as the gate so the hub/Nick adjudicates failures instead of running gradlew per-WU; extend to the new lanes); (b) **lane machinery** — a frontend-dev session prompt/skill and a packaging/devops session prompt/skill, plus the conventions for how the hub feeds them API contracts and reconciles their returns (the write-isolated, single-spine-writer model extended from Core+DOCS to a five-lane fleet); (c) **this scope record**, ratified, as the anti-creep forcing function.

## IN (V1 — Nov 25)

- The **superior automation engine**: M7.2a (run lifecycle / `RunManager` FSM / `RunCausalChain` / dispatch / the run-lifecycle event slice) + M7.2b (action-model freeze: computed-param resolution, run-coupled-reliability terminal contract, the D2/REC-162 disposition).
- The **explainability hero view** in the dashboard, reading a **thin causal-chain query API** (a focused slice of future-M12 observability, sequenced right after M7.2b — must not pull in all of M12).
- The two **supporting differentiator surfaces** (component-based automation list; run outcomes with terminal-state + reason).
- A **focused dashboard**: app shell, design system, auth against AB-1 tokens, device-state + event + health views, the hero view.
- **Real Zigbee (M9)** for a **curated device set** (D-OPEN-2) — coordinator + interview + pairing + control for the demo archetypes.
- **AB-4** — at-rest cipher activation (the trust-brand at-rest story).
- **One-command install** (Distribution): jlink runtime image, systemd unit, `.deb`/install-script, first-run wizard to the dashboard.
- **72h-stable on the curated set** (validation), zero event loss across kill-9, event trace explains any state change.

## OUT (post-launch — Locked-design seams already reserve these)

- **50-device scale** (V1 validates the curated set, not 50).
- **Federation / multi-site** (Doc 16 §3.5 seam; INV-SA-02 reserves it).
- **Enterprise audit projection** (Doc 16 §3.3; default-off; `chain_hash` inert until crypto-shred anyway).
- **Component-authoring UX** (AX-7 versioning policy is a prerequisite; Doc 16 §15-Q2).
- **Full M12 observability** (only the thin causal-query slice ships).
- **D-OPEN-3: the WebSocket real-time runtime** — *recommended OUT*. The hero view is request/response (click → query → render), and the live views can poll the REST surfaces at 1–2s, which reads as real-time for a home dashboard. If confirmed, deferring WS removes an entire Core lane (the WS Phase-3 runtime WU) and simplifies the Web UI (REST polling, no WS client). Confirm at D-OPEN-3.

## The backward-scheduled timeline (Nov 25 is a plan, not a hope)

| Window | Weeks | Must be true |
|---|---|---|
| Nov 16–25 | ~1.5 | Launch prep + buffer. Untouchable. |
| Oct 26 – Nov 15 | ~3 | Distribution + install-flow end-to-end. Needs a finished installer. |
| Oct 12 – 25 | ~2 | Validation: the **72h** stability run (a wall-clock pole you cannot compress) + fix-and-rerun buffer. |
| **by ~Oct 11** | — | **The full thin-slice system running + stable enough to validate** (engine + explainability dashboard + AB-4 + real Zigbee on the curated set). |
| **Jun 20 – Oct 11** | **~16** | The real build window. Fits **only with three lanes in parallel** (Core ~8–9 serial wks; Web UI ~6–8; Distribution ~3–4). Serial-at-full-scope is ~16+ wks of Core *alone* — which is why it misses. |

**Mid-point go/no-go — ~mid-August (≈ week 8).** Test: is the engine done, is the explainability view rendering against **real `RunCausalChain` data**, and is hardware validating? If clearly behind, that is the moment to cut another increment or take a small defined slip — a controlled decision at maximum information, not a November panic.

## The lanes

- **Core (serial Coder):** the D4 sequence. Highest-leverage but it is the one lane that cannot parallelize internally.
- **Web UI — start now, sustained (the long pole among non-Core; ~6–8 wks; no slack).** Builds immediately on what does *not* depend on unbuilt Core: app shell, design system, auth against AB-1 tokens, device-state/event/health views over the existing REST surfaces. The one scheduled seam: the **hero view reads `RunCausalChain`, which does not exist until M7.2a** — so build the shell + device views first, integrate the hero view as M7.2a/b + the causal-query API land. A known, scheduled dependency, not a blocker.
- **Distribution — start now as a de-risking skeleton, then ramp.** Stand up the Core-independent parts now (jlink image, systemd unit, `.deb`/install-script packaging, update mechanism) as a skeleton that already boots the current artifact as a service — cheap, and it removes the classic "the install flow doesn't work and it's November" failure. Ramp the device-discovery wizard + live first-run flow after M9 stabilizes.

## Sequencing rationale — AB-4 before M9 (corrected mechanism)

The original "fail-closed throw" framing is not how the code behaves. Verified at source (`SqlitePersistenceLifecycle:327`, `SqliteEventStore:401–409`, comment L320–326): the composition root **gates `encryptedScopes` on cipher-presence** — cipher null ⇒ sensitive set forced empty ⇒ a sensitive scope writes **plaintext, silently**. The `:402` fail-closed throw is a defensive guard that "cannot occur through this wiring." So the risk of M9-before-AB-4 is a **silent, permanent plaintext write of person-linked data into the immutable hash-chained corpus** (unrecoverable — the log is append-only; AMD-94 rotate-on-restore is additive, not a re-encrypt) — *worse* than a throw, and with no loud signal. Mitigant (holds): raw Zigbee device-state maps to non-sensitive scopes, so basic M9 telemetry would not trip it on event one. **Conclusion:** AB-4 before M9 is the right ordering on trust-hygiene grounds (a trust brand must not ingest real data with at-rest crypto off), AB-4 is small, and its crypto context is maximally fresh now (AMD-94 / Doc 15 just folded). It is a correctness/hygiene ordering, not a hard first-event gate — which preserves a little schedule flex if ever needed, provided nothing person-linked writes before AB-4.

## Critical-path risks

1. **Hardware is the #1 risk, not a footnote (D-OPEN-1).** Real-Zigbee + the 72h run is the longest physical-world pole: procurement lead time you cannot compress + 72 wall-clock hours + fix-and-rerun cycles. If a coordinator stick and the curated device set are not already on a desk, **ordering them is the highest-priority action in this entire plan — ahead of any code.**
2. **The integration point is you, not agent capacity.** Three lanes is 3× demand on the one node that reviews, ratifies, and runs gates. CI-as-gate-of-record (D5a) is the mitigation — it converts that node from gate-runner to failure-adjudicator.
3. **The hero view's Core dependency** (`RunCausalChain` + the thin causal-query API) is the seam that most affects whether the differentiator is demoable at the mid-August checkpoint. Sequence it deliberately; do not let the causal-query slice expand into all of M12.

## Open items — RESOLVED 2026-06-21 (Nick)

- **D-OPEN-1 — Hardware. RESOLVED.** Spec confirmed against Doc 08 §3.2–3.3 + the integration-zigbee scaffold (hub-verified host-side: the two-layer coordinator architecture is real). Buy **one coordinator per transport path** — de-risks M9's adapter work AND gives the two-path abstraction a real validation target: **primary** Sonoff ZBDongle-P (**TI CC2652P**, Z-Stack/**ZNP** path); **second path** Sonoff ZBDongle-E (**Silicon Labs EFR32MG21**, **EZSP** path) or SMLIGHT SLZB-06MG24 (EFR32MG24, more future-proof). Paths are **auto-detected at startup** (INV-CE-04 → no manual config selection); EZSP target is **v13+ / EmberZNet 7.4+** (both candidate sticks satisfy this). For the demo alone the CC2652P is sufficient; the second stick is cheap insurance that validates the EZSP adapter. **Action: order now if not in hand** — procurement lead time + the 72h validation run is the longest, non-compressible pole, ahead of any code.
- **D-OPEN-2 — Curated device set. RESOLVED** (≡ the D-OPEN-1 shopping list — one decision). Archetypes confirmed; **models adjusted off IKEA** (TRÅDFRI line wound down in 2026 → procurement risk) to ZCL-standard parts: **dimmable light** = Philips Hue White (pairs direct to the coordinator, no Hue bridge) or an Innr/Sonoff Zigbee-3.0 bulb; **motion** = Sonoff SNZB-03P (the hero trigger); **contact** = Sonoff SNZB-04; **button/scene** = Sonoff SNZB-01; **plug** = Sonoff S26R2 ZB / S31 Lite ZB (energy); **temp/humidity** = Sonoff SNZB-02P. ~$80–120 all-in. All six map to standard ZCL clusters the device model already expresses (Doc 08 §3.5 cluster table + Doc 02 §3.6 — hub-verified, no gaps). Hero demo path: **motion → light on**, then click "why did this fire?". Tuya/Xiaomi codec quirks are deliberately OUT of the first validation (add later if wanted).
- **D-OPEN-3 — Defer the WebSocket runtime. RESOLVED: YES, defer.** Poll the REST surfaces at 1–2s for V1. The hero view is request/response (click → query → render) and needs no push; the live device/event/health views read as real-time at a 1–2s poll for a home dashboard. Deferring removes the WS Phase-3 runtime WU from the serial Core lane AND simplifies the Web-UI lane (REST polling, no WS client / reconnection logic). The shared `OpaqueTokenStore`/`AuthMiddleware` are already built for the post-launch WS WU — nothing wasted. **The anti-requirement "no WebSocket runtime in V1" is now FIRM (not pending D-OPEN-3).**

## Wave sequence — SET 2026-06-21 (Nick)

Not "launch all four blind." Dependency-ordered, with the hardware decision sitting first as the schedule-critical item:
1. **M7.2a (Core)** — zero dependencies, the longest internal pole — author + launch **now**.
2. **Read-API contract freeze + CI-as-gate-of-record** — fast enabling steps (≈ half-day each) — run **immediately, in parallel** with kicking off M7.2a. The contract freeze is a **hard prerequisite** for the Web-UI lane.
3. **Frontend-dev + Distribution-skeleton** — launch **right after** the contract is frozen. (Launching the UI lane against an *unfrozen* read API invites exactly the cross-lane rework the parallel model exists to prevent.)

Rejected: "author all four now" (frontend-before-frozen-contract churn) and "CI + contracts first, alone" (idles the Core long-pole for no benefit — M7.2a needs neither). Net: **M7.2a + contracts/CI in the same beat → the two new lanes next.**

## Immediate actions (ordered)

1. **Nick:** resolve hardware (D-OPEN-1) — procure if not in hand. Confirm D-OPEN-2 (device list) and D-OPEN-3 (WS defer).
2. **Hub:** author the **lane machinery** — the frontend-dev + packaging/devops session prompts and the five-lane reconciliation conventions (D5b).
3. **Hub:** confirm CI is live on the remote and adopt it as the gate-of-record; plan its extension to the new lanes (D5a).
4. **Hub:** author the **M7.2a coding instruction** (Core lane, the differentiator's engine — Q3-ruled next slot) and the **AB-4 dispatch** (fresh crypto context; now sequenced before M9 per D4).
5. **Hub:** spin up the **Web UI lane** on the Core-independent surface (shell, design system, AB-1 auth, device/event/health views).
