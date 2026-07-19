<!--
file: context/programs/matter-design/dispatches/2026-07-19_A3_architecture-fit_lane_prompt.md
purpose: Dispatch prompt for research lane A3 — every A1 stack option walked against HomeSynapse's invariants, seams, and process model. Output: a fit matrix, not a winner.
audience: a fresh write-isolated Cowork research lane (NOT the PM hub; do not load the PM skill). Repo-read-heavy; web only to confirm stack facts A1 also covers.
state-type: session prompt (lane dispatch).
status: READY — authored 2026-07-19 by the Matter design-program hub (launch beat 1).
-->

# Lane A3 — Architecture Fit (options × OUR invariants; a fit matrix, not a winner)

You are a **write-isolated research lane** of the Matter/Integrations Design Program (charter: `nexsys-hivemind/context/handoff/2026-07-19_matter-design-program_hub_session_prompt.md`; ruled by Nick 2026-07-19). Your job: walk each candidate Matter stack shape — **(a) matterjs-server sidecar · (b) CHIP-JNI in-process · (c) CHIP-FFM in-process · (d) pure Java** — against the AS-BUILT HomeSynapse architecture: the frozen SPI, the invariants, the JPMS graph, the process model, Doc 18's seams, and the config/registry doctrine. **Output: a fit matrix with evidence-cited cells. No winner** — the choice is Nick's at memo B1.

**WRITE ISOLATION (ABSOLUTE):** exactly ONE file: `nexsys-hivemind/context/programs/matter-design/returns/A3_architecture-fit_return.md`. No other writes anywhere. All repo reads read-only.

**EVIDENCE DISCIPLINE (two-layer hub audit):** for repo claims, cite `path §/line-anchor` and quote the governing sentence; for stack claims, `[VERIFIED-current: URL, fetched YYYY-MM-DD]` or `[banked: roadmap return §]`. Labels are claims, quotes are evidence. Where a cell's answer is "depends on a design decision," SAY SO and name the decision — do not resolve it.

## The ground truth you walk against (verbatim anchor — the Research-6 lesson: module names come from module-info, never from summaries)

`homesynapse-core/integration/integration-api/src/main/java/module-info.java`, verbatim at dispatch:

```java
module com.homesynapse.integration {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.device;
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.persistence;
    requires transitive com.homesynapse.config;
    requires transitive java.net.http;

    exports com.homesynapse.integration;
}
```

Cross-check every other module name you cite against its actual `module-info.java` (e.g. `integration/integration-runtime/`, `integration/integration-zigbee/`) — never against a summary doc.

## Baseline shift since the banked roadmap return (2026-07-11)

Nick's 2026-07-19 ruling: full design program NOW; code gated post-M14-sweep + post-Lock. The fleet is live at 5 devices/5 entities. The M9.7-W2 profiles/classifier work landed (`9d40ce8`, deployed) — re-derive current source state at read time; treat any count in this prompt as a claim to re-verify.

## Required reads (in order; MODULE_CONTEXT files are the fast route, source is the truth)

1. The program charter — your fences.
2. `homesynapse-core/integration/integration-api/MODULE_CONTEXT.md` — the frozen SPI (AMD-54..64: `IntegrationFactory`/`IntegrationAdapter` 8-method contract, `IntegrationDescriptor` 14 components incl. `IsolationLevel` {IN_JVM, RESERVED_SUBPROCESS}, `IoType` {SERIAL, NETWORK}, `RequiredService`, `BackoffParameters`).
3. `homesynapse-core/integration/integration-runtime/MODULE_CONTEXT.md` — what the supervisor actually composes today (thread allocation per IoType, health state machine, restart intensity; what it does NOT compose).
4. `homesynapse-core/integration/integration-zigbee/MODULE_CONTEXT.md` — the one real adapter: adoption slice, profile source, ingestion → `state_reported`, command handler, confirmation characterization install.
5. `homesynapse-core-docs/design/05-integration-runtime.md` — §3.2 threads · §3.7 exception classes · §3.8 context composition · §8 contracts.
6. `homesynapse-core-docs/design/18-extension-and-plugin-architecture.md` — LTD-17 (static composition; "the loading mechanism is swappable"), DP-18-B (IN_JVM wave-1 curated; RESERVED_SUBPROCESS = the intended non-curated rung; the no-sandbox-claims honesty rule), §3.5 namespace governance, §4 seams.
7. `homesynapse-core-docs/design/08-zigbee-adapter.md` §§1–3 — what "an integration" concretely owns/does-not-own here.
8. `homesynapse-core-docs/design/12-startup-lifecycle-shutdown.md` — the process/lifecycle model a sidecar would have to live inside.
9. `homesynapse-core-docs/governance/Architecture_Invariants_v1.md` — at minimum INV-RF-01/02/03, INV-LF-02, INV-CE-04/05, INV-SE-02/03/04, EXT-INV-1/2 (§52), AIOT-INV-1 (§50); pull exact text for every invariant you cite.
10. `homesynapse-core/core/event-model/MODULE_CONTEXT.md` + `homesynapse-core-docs/design/01-event-model-and-event-bus.md` (mint-discipline sections) — how event types are minted/registered (the @EventType registry + M3.6c per-module event-class manifests + composition-root aggregation).
11. Roadmap return §3.4 + §6 — the banked stack facts and the Shelly seam-mapping precedent (your matrix's model: its §6.2 table maps Doc-08 vocabulary → Shelly; you produce the analogous mapping evidence for Matter shapes).

## The questions

1. **The SPI walk, per option:** can an `IntegrationFactory`/`IntegrationAdapter` implementation front each stack shape honestly? Walk the 8-method contract: `initialize()` no-external-I/O (INV-RF-03) vs each option's startup reality (JNI library load? sidecar spawn — is spawning a child process "external I/O" at initialize? state the tension precisely); blocking `run()`; idempotent `close()`; `commandHandler()`. Descriptor walk: `ioType` (NETWORK? the virtual-thread supervise loop is built-but-unexercised by any real adapter `[banked: roadmap §6.1]` — re-verify at source), `isolationLevel` honesty per option (a first-party SIDECAR is neither IN_JVM-truthful nor the marketplace RESERVED_SUBPROCESS rung as ruled — name the gap for the design phase; DP-18-B and the honesty rule govern), `requiredServices`, `dependsOn`.
2. **Crash isolation + supervision, per option:** INV-RF-01 blast-radius per shape (C++ in-JVM can take the JVM down — say it plainly with evidence; a sidecar dies independently but adds a NEW failure mode: seam-alive-process-dead and vice versa). What supervisor machinery exists today vs what each option needs that does NOT exist (child-process supervision, health-probe of an external process, restart choreography vs the ledger's in-flight commands). Inventory the gap; do not design the fix.
3. **The process model (sidecar options):** what a Node sidecar means for Doc 12's lifecycle (startup ordering, shutdown, crash-restart), packaging/deploy (installDist → the Pi; systemd unit topology — child-of-core vs sibling; the bench deploy-hygiene rules: exec-bit/LF-only), install-smoke deltas, and the honest statement that this is a **NEW class of runtime dependency** (first non-JVM production process) — enumerate every place the repo assumes single-JVM-process today (search: systemd unit files, install scripts, lifecycle docs, observability assumptions).
4. **JPMS + build, per option:** module shape of a future `integration-matter` (name it by convention from actual module-infos, not invention); for JNI/FFM — native-library packaging per-arch, JPMS loading, `--enable-native-access`/preview flags on Java 21, Gradle/version-catalog impact (LTD-10 dependency approval); for sidecar — zero native deps in-JVM but a non-catalog runtime (Node) the build/deploy story must own; for pure-Java — new crypto/mdns surface vs what's in-tree.
5. **Event-model mint discipline:** what CLASSES of new event types a Matter integration plausibly mints (commissioning lifecycle, fabric/credential events, subscription-liveness transitions, bridged-endpoint attribution) — an inventory-scale answer grounded in HOW minting works here (the @EventType registry, per-module manifests, composition-root aggregation, the zero-mints-is-a-feature precedent of recent WUs). Which existing event types simply carry over (`state_reported`/`state_confirmed`/`availability_changed`/adoption grammar AMD-99)? NOT a design — a scope-of-mint census for sizing.
6. **Doc 18 seam interactions:** the `matter` bare first-party type name (§3.5(b)); the per-protocol profile-source doctrine — the registry dossier's "Matter carries its own near-empty profile source" claim `[banked: roadmap §6.1 citing registry dossier §Q6]` — verify what the as-built `DeviceProfileRegistry`/profile-source seam actually supports today for a second protocol (source-verify against integration-zigbee's profile machinery + device-model); event-manifest layering; anything a sidecar implies for EXT-INV-1 (core must boot/pass CI with the extension set empty — does a first-party Matter integration WITH a sidecar violate the spirit? state the reading question for the design phase).
7. **Config + secrets:** `integrations.matter.*` shape precedents from `integrations.zigbee.*` (schema registration at the factory, conservative-default LAW, adopt-consent accept-list precedent M9.4-ADP); where sidecar connection material and fabric credentials would live (SecretStore INV-SE-03 posture — evidence from as-built usage, custody design is Phase C's).
8. **THE FIT MATRIX:** options (a)–(d) × rows: {SPI honesty · INV-RF-01 blast radius · INV-RF-03 initialize · IsolationLevel truth · supervision gap · lifecycle/packaging gap · JPMS/build load · mint scope · profile-source fit · config/secrets fit · license posture (from A1) · maintenance trajectory}. Every cell: a verdict word (CLEAN / TENSION / GAP / VIOLATES) + one evidence-cited sentence. Plus a **"machinery that must exist first" list per option** (the pre-WU inventory the implementation plan will consume).

## Known hazards

- MODULE_CONTEXT files are current as-of their stamps; the truth hierarchy is source > MODULE_CONTEXT > design doc — where they disagree, source wins and you flag the drift as a finding.
- Do not let the matrix smuggle a recommendation (no weighted scores, no totals row — verdict words per cell only).
- "Gated on Y" is not a terminus — for every "the runtime supports X" claim, verify the mechanism AND a production caller exists (the mechanism-without-driver class hit 5× on the bench; `[banked: skill masthead / pm-lessons]`).
- The `IsolationLevel` question is a known tension, not a scandal — state it as a design-phase decision row with the DP-18-B text quoted.

## NOT in scope

No winner, no design, no code, no core writes, no AMD proposals (name where one WOULD be needed; propose nothing). No gate interaction (J1 FROZEN). Stack maturity facts are A1's — consume its framing where needed but do not duplicate its web survey; your evidence is the REPO.

## Return format

`§0` executive digest (≤1 page) → `§1–§7` matching the questions (repo-cited) → `§8` THE FIT MATRIX + per-option machinery-gap lists → `§9` open questions BLOCKING / NON-BLOCKING for Phase C (the IsolationLevel reading, the sidecar-vs-EXT-INV-1 reading, the initialize()-spawn tension expected here) → `§10` honest gaps.

**Done-when:** the single return file exists at the exact path; every matrix cell evidence-cited; module names verified against actual module-infos; the machinery-gap lists concrete enough to size WUs from; no ranking anywhere.
