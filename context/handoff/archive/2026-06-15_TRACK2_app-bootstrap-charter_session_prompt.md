<!--
file: context/handoff/2026-06-15_TRACK2_app-bootstrap-charter_session_prompt.md
purpose: Track 2 — a fresh Cowork PM session that produces the APP-BOOTSTRAP milestone CHARTER: the high-density latent-defect milestone where main() wires HomeSynapseCore into a running system and the two converge HIGH findings (C1 unauth surface, C2 read-path decrypt contract) + C9 (lifecycle reconciliation) go live. Scoped OFF the M7 critical path. This is PLANNING (a charter), not a coding instruction — it does NOT violate the W25 Lane-4 P6 floor.
audience: PM (nexsys-project-manager hat), Nick
state-type: session prompt
status: READY — paste into a fresh Cowork conversation. Best run AFTER (or consuming) the Track-3 red-team's verdicts on the crypto one-way-doors.
-->

# Track 2 — Author the App-Bootstrap Milestone Charter

**You are the PM and most-senior engineer (`nexsys-project-manager` hat).** Produce the **charter** for the **app-bootstrap milestone** — the milestone that turns the built-but-inert system into a runnable one: `main()` wires `HomeSynapseCore`, the at-rest cipher activates, the HTTP surface is exposed, and the lifecycle abstractions are reconciled. The converge's single most important conclusion governs this work: **app-bootstrap is a high-density latent-defect milestone — it must NOT be scoped as "just wire `main()`."** Three findings go live at exactly this moment, so the charter must carry all three in one coherent gate.

This is a **charter (scoping/planning)**, not a coding instruction — so it is permitted now, independent of the W25 Lane-4 P6 floor. It is **OFF the M7 critical path**; M7.x proceeds independently.

## Step 0
Invoke `nexsys-project-manager`; run the freshness preflight (baseline: **M6 COMPLETE 4-of-4, core HEAD `1eddd9a`**; watermark AMD-93; the project-knowledge spine was reconciled 2026-06-15; the R-α return is assessed). Same environment realities: host Read tools authoritative; Cowork cannot run Gradle; sandbox git quarantined.

**Read (the inputs — treat as ground, but see the Track-3 caveat below):**
- `context/audits/2026-06-15_core-review_CONVERGE_synthesis.md` — **C1 (=B-H1)**, **C2 (=F-A1)**, **C9 (=B-M1)**, **Seam 1** ("the two HIGHs detonate at one milestone: app-bootstrap"), **Seam 3** (crypto shipped but dormant), the **reserved-but-unbuilt register**, and **CC-1** (the bind-address verification).
- `context/assessments/2026-06-15_Research_R-alpha_PM_Assessment.md` — the **C2 design answer**: the cause-discriminated read contract (CASE-a degrade / CASE-b fail-closed), the **shred tombstone** primitive, **rotate-DEK-on-restore** as the binding restore contract, and the REC-216..235 routing (the app-bootstrap bucket: restore/nonce + fail-closed detection).
- Doc 12 (Startup, Lifecycle & Shutdown) — the 6-phase model, the health loop (§3.10), the systemd watchdog, `SystemLifecycleManager` as the named `main()` entry point.
- Doc 15 §3.8 (the `PayloadCipher` adapter hosted in `com.homesynapse.app`), §5 (the chain-covers-stored-bytes invariant), §6 (the read/restore failure modes).
- MODULE_CONTEXT.md for **lifecycle, persistence, config, rest-api, platform-systemd**; and the source: `lifecycle/.../HomeSynapseCore.java` (`start()` in full), `app/.../Main.java` (the stub), `lifecycle/.../SystemLifecycleManager.java` (interface, no impl), `RestFilters`, the absent `AuthMiddleware`/`RateLimiter`, the `SqliteEventStore` read path.

**Track-3 caveat (important):** the Track-3 red-team is auditing the recent crypto/architecture decisions for one-way-door mistakes (AES-GCM crypto-agility, the cause-discriminated contract, rotate-DEK, the encrypted-scope set). **If Track-3 has produced verdicts, consume them** — incorporate any "reverse-now-while-cheap" or "pause-for-evidence" findings into the charter. **If Track-3 has not run yet, gate the affected charter pieces on it** (flag them as "pending the Track-3 red-team verdict") rather than locking them. Do not let the charter bake in a crypto decision the red-team might overturn.

## Charter tasks (what the charter must contain)
1. **Scope statement + the anti-scope.** What app-bootstrap IS (wire `main()`→`HomeSynapseCore`; activate `payloadCipher`; expose the HTTP surface safely; reconcile lifecycle) and the explicit warning that it is NOT "just wire `main()`." State the one-line reason it is gated separately from M7.
2. **Decompose into first-class sub-milestones** (apply the P1 sizing smell test — if it spawns >~3 pieces, they are first-class with their own backlog rows). At minimum:
   - **Auth + bind posture (C1):** `AuthMiddleware` on every external route (incl. `/internal/*`, which today sits outside even the readiness gate), `RateLimiter`, the **bind-posture decision** (loopback-default vs all-interfaces — calibrated by **CC-1**), enforcing **INV-SE-02** (auth mandatory on every external interface; no local-trust exception). Name the auth model as an open design decision to settle in the charter or escalate.
   - **The read contract — fail-closed half (C2):** on GCM-auth-fail / missing-or-corrupt root key / chain-hash failure → fail the read batch closed with a distinct loud error (the app-bootstrap bucket of the R-α disposition). The **degrade half** (intended-shred → `DegradedEvent`) belongs to the post-MVP crypto-shred WU, but the **seam + the cause-carrying `DegradedEvent` + the chain-validity check** must be designed here so the contract is coherent. Carry the **rotate-DEK-on-restore** boot-time invariant (refuse-to-encrypt-in-a-scope until a fresh DEK is installed or the persisted counter is proven ≥ all prior nonces).
   - **Lifecycle reconciliation (C9):** decide and pin — does `main()` construct `HomeSynapseCore` directly (re-homing Doc 12's 6-phase/health-loop model), or does `SystemLifecycleManager` wrap `HomeSynapseCore`? Wire the health loop + systemd watchdog (and the `platform-systemd` `SystemdHealthReporter` path to the running system, which today has none). Pin it with a lifecycle wiring test.
   - **`payloadCipher` activation:** wire the `ScopeKeyManager`→`PayloadCipher` adapter (Doc 15 §3.8, app-hosted; the M6.2 E2 bridge is held-not-consumed) into the persistence read+write path. This is the moment the crypto goes live — so it must land *with* C1+C2, not before.
3. **Entry-gate** (what must be GREEN before the first app-bootstrap coding instruction issues): the R-α Doc 15 §6 amendment ratified; **CC-1** run (the bind-address empirical); the read-contract design beat settled; the auth model decided; any Track-3 crypto verdicts in.
4. **Sequencing within the milestone**, and the explicit statement of independence from M7 (it can run parallel to or after M7.x).
5. **Carry-pins + invariants:** INV-SE-02 (auth), INV-RF-04 (replayability), INV-PD-07 (crypto-shred seam), the chain-validity check, the lifecycle wiring test, the §4c Clock-injection reminder, CC-1.
6. **In/out scope:** OUT = the crypto-shred *operation* (post-MVP) and its degrade half (crypto-shred WU); IN = the read-contract seam + fail-closed half + the cause-carrying `DegradedEvent` type. Be explicit about the boundary so the crypto-shred WU and app-bootstrap don't collide or double-build.
7. **Milestone placement/numbering — PROPOSE and ESCALATE to Nick.** Where app-bootstrap sits (it likely gates the first runnable/shippable product, so it is significant) is a scope/strategy call. Propose a placement with rationale; do not decide it unilaterally.
8. **Fold in CC-1** as the pre-charter or early-charter empirical calibration (a test that starts `HomeSynapseCore` and asserts the bound socket's address; `grep -rn "\.host(" lifecycle api`).

## Output discipline
A **charter** in the house style (cf. `context/planning/2026-06-08_M6-charter.md`, `2026-06-12_M7-M8-charter-skeleton.md`) — short, ranked, decision-bearing; the artifact a future app-bootstrap coding-instruction session builds from. Lead with the scope + the Seam-1 insight. Escalate to Nick: the milestone placement, the auth model if it has strategic/API-shape implications, and any locked-decision touch (Doc 12/Doc 15).

## Deliverables
1. `context/planning/2026-06-15_app-bootstrap_charter.md` — the charter.
2. A completion report to Nick: the scope, the pieces + proposed sizing, the entry-gate, what's escalated, and what (if anything) is gated on the Track-3 red-team. Commit message handed over (`!`-free).

## Done-when
The charter names the sub-milestones (sized), the entry-gate, the within-milestone sequencing, the in/out boundary vs the crypto-shred WU, the carry-pins/invariants, and the CC-1 calibration; the milestone placement + locked-decision touches are escalated, not silently decided; the Track-3 dependency is either consumed or explicitly flagged. Success = a future session can open the app-bootstrap coding work knowing exactly what it must carry and why.
