<!--
file: context/instructions/2026-09-02_coder-lane_PKG-SEC-2_zigbee-schema-admission_coding-instruction_RULING-SLOTTED.md
purpose: PKG-SEC-2 — THE ZIGBEE SCHEMA ADMISSION (R-4 C-1: "Configuration issue [WARNING] … integrations.zigbee … not defined in the schema and the schema does not allow additional properties" ON EVERY START). The coding instruction for the second Coder WU of wk 2, authored AHEAD at v61 beat 6 (Wed 2026-09-02 ~20:12 CT, instrument 01:11Z) against R-10 Row 13 — SHARPENED by this session's source read: the per-integration contract EXISTS (Doc 06 §3.2; `zigbee-config-schema.json` ships; `Main.java:130` registers it) — the defect is COMPOSITION ORDER: `config.load()` validates in Doc 12 Phase 1 with only CORE schemas composed (`HomeSynapseCore.java` :455–:467), the zigbee fragment registers only AFTER `manager.start()` returns (the "W10" deferral, `Main.java` :125–:131), and `HomeSynapseCore.registerIntegrationSchema` THROWS if called earlier (:1390–:1397). At Phase-1 validation the root's `integrations` node is `{"properties":{}, "additionalProperties":false}` (the composed schema on disk shows exactly that) → the WARNING.
audience: the Coder lane (host-side; `nexsys-coder`) · Nick (the commit + push — CORE IS NICK'S HANDS) · the hub (the audit)
state-type: coding instruction (Phase 3 — tests first)
status: AUTHORED AHEAD — RULING-SLOTTED. Dispatches when §0 reads RULED. Return: `context/audits/<CT-filing-date>_PKG-SEC-2_return.md` (≤10 KB; §0 first; the porcelain census; the deferred-gate line; the D-f sweep table).
-->

# Coding Task: PKG-SEC-2 — admit `integrations.zigbee` at Phase-1 validation (pre-start fragment registration)

**Subsystem:** lifecycle (`com.homesynapse.lifecycle`) + app (`com.homesynapse.app`) + configuration (read-only unless the registry needs a drain hook) · **Design Docs:** Doc 06 §3.2 (schema composition; LOCKED) · Doc 12 §3.3 Phase 1 (LOCKED) · **Phase:** 3-Implementation (tests first) · **Task Brief Reference:** the PKG-SEC-2 charter (08-30) + R-10 additions item 4 + Row 13.

## §0 THE RULING SLOT
**Row 13 word:** ⟨RULED: (a′) | (b′) | EDIT: … | HOLD⟩. The card's (a)/(b)/(c) are SUPERSEDED by the source read; the live options: **(a′) PRE-START FRAGMENT REGISTRATION — integration schema fragments are static JSON text (no adapter instance needed: `ZigbeeIntegrationFactory.configSchemaJson()` is a resource read), so the composition root supplies them BEFORE `start()`, the lifecycle drains them into the registry right after `cfg.schemaRegistry()` is assembled and BEFORE `configurationService.load()`; the post-start path stays for late registrants** (rec) · (b′) late re-validation: Phase 1 treats `integrations.*` as deferred (root `integrations.additionalProperties: true` at Phase 1), a second strict validation pass runs after the late registration — weaker: Phase 1 no longer validates what Doc 06 §3.2 says it composes · (c) the carve-out alone — NEVER. **Doc 12 conflict check (owed in the return):** Doc 12 §3.3 says Phase 1 "loads and validates" and names Doc 06 §3.1–§3.2 (which composes integration schemas from descriptors); the "integration schemas defer past Phase 6" sentence lives in CODE comments (W10, M9.1-era) not in Doc 12's text — quote both in the return; if Doc 12's text is found to forbid pre-load integration composition, STOP and return (an AMD, not a Coder call).

## What This Implements
Authored to (a′). `HomeSynapseCore` gains a pre-start intake for integration schema fragments (constructor/builder parameter `Map<String,String> integrationSchemaFragments` or a pre-start `registerIntegrationSchema` that QUEUES instead of throwing), drained into `schemaRegistry` immediately after assembly and before `load()`. `Main` passes `ZigbeeIntegrationFactory.INTEGRATION_TYPE → configSchemaJson()` at construction; the post-start call at `Main.java:130` is removed (or kept as a no-op-if-already-registered — the Coder decides, states why). Result: the config validates against the real fragment at Phase 1 — a malformed `integrations.zigbee` block is CAUGHT at boot (today it is invisible: the WARNING says "unknown", not "wrong"), and a well-formed one boots with ZERO configuration issues.

## Files to Read Before Starting
| File | Why |
|---|---|
| `lifecycle/lifecycle/MODULE_CONTEXT.md` · `lifecycle/lifecycle/src/main/java/module-info.java` (verbatim below) | the composition root's contracts; the M3.6e.1 gateway pattern (why `registerIntegrationSchema` is `java.base`-only on the exported API) |
| `config/configuration/MODULE_CONTEXT.md` (§types :99–:110 · INV-CE-02 :177 · the two GOTCHAs :220–:222) · its `module-info.java` | `SchemaRegistry` semantics (JSON TEXT, not paths); `StandardSchemaRegistry` composition; INV-CE-02 (every key has a default) |
| `HomeSynapseCore.java` :430–:470 (Phase 1) · :1370–:1400 (the guarded registration) · the 7-/8-arg ctors | where the drain goes; the guard you relax pre-start |
| `Main.java` :100–:135 | the W10 call you move |
| `StandardSchemaRegistry.java` :90–:120 | does a late `registerIntegrationSchema` recompose + rewrite the on-disk schema (C7)? read before asserting |
| `ZigbeeIntegrationFactory.java` :100–:125 · `integration/integration-zigbee/src/main/resources/schema/zigbee-config-schema.json` | the fragment; check it declares defaults for every key (INV-CE-02) and `permit_join_duration`'s range [1, 254] |
| `app/homesynapse-app/.homesynapse/config/schemas/config.schema.json` | the dev-run composed schema showing `integrations: {properties: {}, additionalProperties: false}` — the exhibit |
| `homesynapse-core-docs/design/12-startup-lifecycle-shutdown.md` §3.3 · `06-configuration-system.md` §3.2 | the conflict check |
| the existing lifecycle/app tests around Phase 1 + any test asserting the post-start registration guard | locks to extend / re-pin with disclosure |

**module-info.java, lifecycle (verbatim, comments stripped):** `module com.homesynapse.lifecycle { requires transitive com.homesynapse.observability; requires transitive com.homesynapse.event; requires transitive com.homesynapse.platform; requires transitive com.homesynapse.persistence; requires transitive com.homesynapse.event.bus; requires transitive com.homesynapse.state; requires transitive com.homesynapse.integration; requires com.homesynapse.integration.runtime; requires com.homesynapse.api.rest; requires com.homesynapse.config; requires transitive com.homesynapse.device; requires com.homesynapse.automation; requires com.homesynapse.platform.systemd; requires io.javalin; requires org.eclipse.jetty.util; requires org.slf4j; exports com.homesynapse.lifecycle; }` — **no JPMS change**: the fragment travels as `String`/`Map<String,String>` (java.base), exactly the M3.6e.1 gateway idiom. **app:** `requires com.homesynapse.integration.zigbee` already present.

## Files to Create or Modify
| Action | File | Description |
|---|---|---|
| MODIFY | `lifecycle/…/HomeSynapseCore.java` | the pre-start intake + the drain (between `this.schemaRegistry = cfg.schemaRegistry();` and `registerCoreSchema(automation)` or right after it — before `load()`); the post-start guard: pre-start → queue, post-start → direct |
| MODIFY | `app/…/Main.java` | supply the zigbee fragment at construction; remove/neutralize the post-start call at :130 (state which) |
| MODIFY | `lifecycle/lifecycle/MODULE_CONTEXT.md` · `config/configuration/MODULE_CONTEXT.md` (only if the registry changed) · `app/homesynapse-app/MODULE_CONTEXT.md` | the PKG-SEC-2 blocks |
| CREATE | tests (below) | red-first |
| MODIFY (the D-f sweep) | each `/etc/homesynapse` hit in `distribution/README.md` · `distribution/docs/boot-contract-map.md` · `distribution/docs/escalations.md` · `scripts/dev/pi-health.sh` · `config/configuration/MODULE_CONTEXT.md` · `platform/platform-systemd/MODULE_CONTEXT.md` | **CLASSIFY, never blind-replace**: a claim that the config YAML lives under `/etc/homesynapse/…` → correct to the measured root `/var/lib/homesynapse/config/` (+ `integrations/zigbee.yaml` via include); any OTHER `/etc/homesynapse` use (env file, token pair, unit `EnvironmentFile=`) is KEPT — `distribution/systemd/homesynapse.service`, `common.sh`, `build-deb.sh` are expected keeps; the return carries the table (file · line · classification · action) |

## Technical Specification (contracts)
1. **Ordering contract:** every integration schema fragment supplied pre-start is part of the composed root schema BEFORE `configurationService.load()` runs — the `integrations` node's `properties` carries one entry per supplied type; `additionalProperties: false` at the root and at `integrations` STAYS (an unknown integration key remains a WARNING — Doc 06 §3.6 tier).
2. **Post-start registration stays lawful** (a late fragment recomposes; the C7 on-disk schema rewrite behavior is read from `StandardSchemaRegistry` and preserved, not assumed).
3. **INV-CE-02:** the zigbee fragment's keys keep their defaults; an EMPTY `integrations.zigbee:` block validates to defaults; an ABSENT block validates.
4. **No config-key or event change.** No new dependency.
5. **Logging:** on the drain, one INFO per fragment: `lifecycle.integration_schema_registered: type=zigbee stage=pre-load` (LTD-15).

## Test Requirements (RED FIRST — predictions filed in the return)
(T1) a config carrying a well-formed `integrations.zigbee` block + the fragment supplied pre-start → `load()` reports ZERO issues — **RED at HEAD** (today: the WARNING) · (T2) `integrations.notatype:` → the WARNING still fires (root strictness kept) — GREEN-by-construction, disclosed · (T3) `integrations.zigbee.permit_join_duration: 999` → the fragment's range violation reports at Phase 1 (severity per the fragment/§3.6 — read, then predict) — **RED** (today: invisible behind "unknown") · (T4) the composed schema (C7 write) contains `integrations.properties.zigbee` — **RED** · (T5) post-start `registerIntegrationSchema` still works and never throws after start — GREEN-by-construction · (T6) pre-start call no longer throws `IllegalStateException` (the guard re-pinned WITH DISCLOSURE if a test locks the throw) — **RED**.

## Locked Decisions / Invariants
Doc 06 §3.2 composition · Doc 06 §3.6 issue tiers · Doc 12 §3.3 Phase 1 FATAL semantics (a validation ERROR stays fatal; this WU must not soften it) · INV-CE-02 · C7 · the M3.6e.1 gateway (no `com.homesynapse.config` type on lifecycle's exported API) · the M9.1 lockstep rule (`requires transitive` ⇔ `api(...)`) — untouched · SK-INV-02 Clock injection (tests inject `Clock`). **INV/LTD sweep owed in the return.**

## What to Watch Out For
- **The guard's message** ("Integration schemas register after start()") encodes the OLD design — rewrite it, do not leave it lying.
- **Do not register the zigbee fragment as a CORE schema** (`registerCoreSchema`) to dodge the guard — it composes into the wrong node and breaks `ConfigurationAccess` scoping (`integrations.{type}`).
- **The dev-run `config.schema.json` under `app/homesynapse-app/.homesynapse/`** is a generated artifact — do not hand-edit; T4 regenerates it.
- **The SK-INV-02 arch rule** runs only from the app's test classpath; lifecycle test code is self-enforced — inject `Clock`.
- **`-Werror` / `-Xlint:exports`:** a `Map<String,String>` on a public ctor is java.base — safe; anything from `com.homesynapse.config` on the public surface trips the lint.
- **Targeted gates in-session:** `./gradlew :lifecycle:lifecycle:compileJava :lifecycle:lifecycle:test :app:homesynapse-app:compileJava :app:homesynapse-app:test`; the full `./gradlew check` is the DEFERRED GATE (Nick's environment) — name it in the return with the commit.

## Coder Pushback Welcome
If `StandardSchemaRegistry` cannot compose a fragment before the core schemas without a change the Coder judges non-trivial, return the smallest change with its line evidence. If Doc 12's text is found to forbid (a′), STOP and return (§0).

## Out of Scope
Any change to the fragment's keys · the config-reload path (§3.3 hot reload) beyond what T5 touches · the packaging (.deb) · FE.

## Work Unit Completion (WUCP Phase 1 — the return's shape)
§0 verdict-first; the porcelain census EXACT (expected ≈ 3–5 M source + 1–3 M MODULE_CONTEXT + the D-f sweep files + N test files A; ZERO commits by the lane); the red-first table T1–T6; the D-f classification table; the Doc 12 conflict-check quotes; the Deferred Build Gate line; INV/LTD sweep; instrument limits; CT filing date. **THE MSG FILE (hub-authored at the audit, for Nick's hands):** `../_scratch/<date>_core_PKG-SEC-2_commit-msg.txt`. **R-4b's rig check** (post-landing, at the next power-on): `journalctl -u homesynapse.service -b --no-pager | grep -c 'Configuration issue'` → expected **0**.
