<!--
file: context/handoff/2026-06-19_AB-3_lifecycle-reconciliation_session_prompt.md
purpose: Dispatch-ready brief for a FRESH Cowork Mode-3 Director session that AUTHORS (and, if its entry-gate is clean, ISSUES) the AB-3 coding instruction — app-bootstrap lifecycle reconciliation, the runnability-unlock substrate that lands M7.1's deferred composition-root wiring. AB-3 is the RULED next Coder slot (2026-06-19, R1).
audience: PM/Architect (a FRESH Cowork conversation, nexsys-project-manager skill — Mode 3 Director), Nick (the one API-shape call + the registry-home call)
state-type: session prompt (Phase-3 coding-instruction authoring)
status: READY — authored 2026-06-19 after the M7-forward plan + Nick's R1 ruling. AB-3 carries NO decision gate (A1–A4 ruled); the device-model registry dependency is source-verified as a contained fold (below). Run as a fresh Cowork conversation.
baseline: core `beb4bc3` (M7.1 GREEN, substantive HEAD) / docs `32afb3f` (Doc 16 DRAFT, not Locked) / hivemind `91a5afd` (M7-forward plan + rulings). M6 COMPLETE; M7.1 DONE; watermark AMD-93; Doc 12 + Doc 15 LOCKED. Confirm at preflight.
reads (in order):
  - context/process/cowork-environment-model.md (FIRST — path duality, the truncated-tail mount artifact, host-authoritative file tools)
  - context/status/PROJECT_SNAPSHOT.md (the 2026-06-19 masthead + Current-WU)
  - context/planning/2026-06-15_app-bootstrap_charter.md (§1 Seam-1; §2 AB-3 scope; §3 entry-gate — AB-3 issues FIRST as substrate; §4 independence from M7; §7 escalations)
  - context/decisions/2026-06-18_app-bootstrap-and-superiority-scope_decisions.md (A1–A4 RULED; **the Addendum** — the M7.1 composition-root wiring deferral + AB-3's inbound deps (a)(b)(c) + the device-model-breadth flag)
  - context/planning/2026-06-19_M7-forward_plan.md (R1 sequencing ruling; the registry-dependency resolution; the I2 inject-deps boundary)
  - context/handoff/coder-handoff.md (the M7.1 entry — the exact deferred wiring: the `automation_engine` subscriber, the config-loading/schema-registration via `AutomationSchema.SCHEMA_JSON` + `ConfigurationService.getCurrentModel().rawMap()` → `loader.load(...)`, and the mandated lifecycle wiring test)
  - homesynapse-core-docs/design/12-*.md (Startup, Lifecycle & Shutdown — the 6-phase model, REPLAY→LIVE, health loop §3.10) + Doc 15 §3.8 (the `ScopeKeyManager → PayloadCipher` adapter, app-hosted) for the phase-gating ordering only (cipher activation is AB-4, not AB-3)
  - core/lifecycle/MODULE_CONTEXT.md + core/automation/MODULE_CONTEXT.md + core/device-model/MODULE_CONTEXT.md + core/configuration/MODULE_CONTEXT.md + core/event-bus/MODULE_CONTEXT.md + core/state-store/MODULE_CONTEXT.md, AND each module's `module-info.java` VERBATIM (embed the touched ones in the instruction — the Research-6 lesson)
  - references/coding-instruction-format.md + references/cross-subsystem-awareness.md + references/constraint-enforcement.md
  - the R-δ AX-2 assessment (openHAB numbered startlevels as the lifecycle phase model; HA auto-backup-before-update; Apple destructive-in-place anti-lesson) — cited in the charter §2 AB-3
-->

# Session Brief — Author the AB-3 Coding Instruction (app-bootstrap lifecycle reconciliation)

PM/Architect session (**nexsys-project-manager**, Mode-3 Director). Read `context/process/cowork-environment-model.md` FIRST, then run the freshness preflight against the pinned baseline. **AB-3 is the RULED next Coder slot** (2026-06-19, M7-forward plan R1): the lifecycle/composition-root substrate that makes the system runnable and lands M7.1's deferred wiring. Your job: **author the AB-3 coding instruction** (per `references/coding-instruction-format.md`) and, if its entry-gate is clean, issue it to the Coder. Nick rules the one API-shape call and the registry-home call (below); you assemble, verify, and (if clean) dispatch.

**Step 0:** preflight; reconcile HEADs. Expected PASS. **Note the mount hazard:** the VM `git status`/`diff` may serve truncated-tail / phantom-rename artifacts (env-model §2/§5) — the host file tools are authoritative; never source a scripted edit from a VM worktree read; never act on the VM git view. **Verify no unresolved deferred build gate** (skill §4b): M7.1's gate is RESOLVED GREEN (`beb4bc3`), so the lane is clear.

---

## What AB-3 is (scope — from the charter §2 AB-3 + the decision-record Addendum)

AB-3 reconciles the lifecycle substrate so `main()` constructs a coherent, phase-ordered runtime, and it **lands the three things M7.1 deferred** (decision-record Addendum, inbound deps a/b/c). It issues FIRST (before AB-1+AB-2+AB-4, the Seam-1 go-live). **AB-3 carries no decision gate** — A1–A4 are ruled; CC-1 / R-γ / AMD-94 gate AB-1/AB-2/AB-4, NOT AB-3.

The instruction must cover:

1. **Lifecycle reconciliation + the phase model.** Reconcile the two disjoint abstractions (`SystemLifecycleManager` — today an unimplemented interface that never references the real composition root — vs `HomeSynapseCore`). **Adopt openHAB's numbered startlevel ladder** as the concrete phase model (R-δ AX-2): framework → bundles → model-load → state-restore → rules-loaded → engine-active → UI-up. **Gate cipher activation and HTTP exposure to specific phases** (HTTP must not open before AB-1's auth is wired; the cipher activates with AB-4 — AB-3 only establishes the phase gates the later pieces hook into). Wire the health loop (Doc 12 §3.10) + the systemd watchdog + the `platform-systemd` `SystemdHealthReporter` path. Add the **pre-migration snapshot + one-click rollback** hook before any schema/chain change (R-δ AX-2).

2. **The minimal production registries (source-verified contained fold — NOT device-model breadth).** AB-3 assembles `ConfigurationService` (impl exists, M6.1 — needs wiring) + minimal production impls of the three registries the composition root + the automation path need. **Verified at `beb4bc3`:** `EntityRegistry` (9 methods), `DeviceRegistry` (7), `AreaRegistry` (4) are interface-only in `core/device-model`; their signatures depend only on `com.homesynapse.platform.identity` ULID wrappers + the same-package `Entity`/`Device`/`Area` domain types **that already exist**. So a **Map-backed / config-backed, start-empty** impl (CRUD + the small query set; populated later by M9/M14 integrations) is contained — it does **NOT** pull in AMD-44 Floor/EntityRole or Research-8 breadth (that is the populate/derive side, owned downstream). The `AutomationTestSupport` in-memory registries are the behavioral shape to productionize. **Do NOT** fold `FloorRegistry`/`CapabilityRegistry` unless a wiring path provably needs them (confirm against the subscriber + selector-resolution path; M7.1's `SelectorResolver` exercises Entity/Area/Device only).

3. **Land M7.1's deferred wiring (the Addendum inbound deps).** (a) Wire the `automation_engine` subscriber into `HomeSynapseCore.start()` with **subscribe-after-state-store-catch-up** (the converge latent-defect site). (b) Wire the config-loading + schema-registration: register `AutomationSchema.SCHEMA_JSON` via `registerCoreSchema`, then `ConfigurationService.getCurrentModel().rawMap()` → `loader.load(document)` (the glue that was relocated OUT of `core:automation` to the composition root — the `core→config` edge is BANNED in core; this glue lives in `lifecycle`/`app`, which legally `requires` both). (c) Carry the **M7.1 lifecycle wiring test** (the test that could not be written against a stubbed composition root).

## Escalations to Nick (pin in the instruction; do not decide unilaterally)
1. **The lifecycle API-shape call (charter §7 / escalation #4b):** does `main()` construct `HomeSynapseCore` directly (re-homing Doc 12's 6-phase model into it), or does `SystemLifecycleManager` wrap `HomeSynapseCore`? API-shape-adjacent → Nick's call; pin at instruction authoring.
2. **The registry-home call:** do the three minimal registry impls live in `core:device-model` (same module as the interfaces; production `InMemory*Registry` classes) or are they assembled in the composition root (`app`/`lifecycle`)? Both respect the layering (device-model is a legal core dependency); the former keeps them with their interfaces, the latter keeps device-model impl-free until M9/M14. Recommend + escalate.

## Boundary (what AB-3 does NOT do)
- **No auth, no bind posture, no cipher activation, no read-contract** — those are AB-1/AB-2/AB-4 (the Seam-1 go-live), gated on CC-1/R-γ/AMD-94. AB-3 only establishes the phase gates they hook into.
- **No automation_triggered production publish** — the C1-interim no-publish pin still holds until M7.2.
- **No device-model breadth** (AMD-44 Floor/EntityRole, Research-8) — the registries start empty; populate is downstream.
- **No M7.2 work** — AB-3 lands M7.1's wiring; the run/action/dispatch path is M7.2a.

## Carry-pins (embed in the instruction)
§4c Clock-injection (AB/lifecycle/device-model modules are non-whitelisted); the lifecycle wiring test; subscribe-after-state-store-catch-up; the consumer/pin survey + a targeted `./gradlew :module:compileJava` on `-Werror`-sensitive touched modules before handoff (shift-left, skill §4b/P5); the §4b deferred-gate setup (the full `./gradlew check` becomes a deferred gate once the Coder lands the diff); module-info edits embedded verbatim with the `requires transitive`↔`api` lockstep check AND the `assertAllowedModuleDependencies` layer-allow-list check (the FIX-07 two-gate lesson — `core→config` stays banned; the composition-root glue rides `lifecycle`/`app`).

## Anti-requirements (bind)
Local-first inviolate · the `core→config` edge is banned (config wiring rides the composition root) · no destructive forced migration (the pre-migration snapshot/rollback is additive) · auth-before-network-exposure is a tracked gate for AB-1 (AB-3 must not open HTTP before it). Locked docs (07, 12, 15) move only via the formal pipeline.

## Done-when
The **AB-3 coding instruction** is authored per `references/coding-instruction-format.md` (Files-to-Read incl. the MODULE_CONTEXTs + verbatim module-infos; What-to-Watch-Out-For derived from the device-model/lifecycle/automation gotchas + the §4c reminder; the two-gate module-graph check; the consumer/pin survey rows; the deferred-gate setup), with the two escalations pinned to Nick's rulings. **EITHER** issue it to the Coder (entry-gate is clean — no decision gate, no deferred gate) **OR**, if the API-shape / registry-home calls are still open, hold as authored-and-gated pending Nick. Update the backlog AB-3 row (→ ISSUED or AUTHORED-GATED) + the snapshot Current-WU + W26 Lane 1; run the WUCP drift check; hand over a bang-free commit message (`git commit -F`).
