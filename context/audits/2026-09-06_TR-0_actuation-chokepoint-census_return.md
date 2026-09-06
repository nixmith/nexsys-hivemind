<!--
file: context/audits/2026-09-06_TR-0_actuation-chokepoint-census_return.md
purpose: TR-0 return: the actuation chokepoint census at HEAD 093d5b4 (Q1-Q5 receipted; P1-P4 adjudicated first).
status: RETURNED 2026-09-06 CT (boot 15:49Z; nexsys-coder skill, READ-ONLY; one file; nothing staged or committed)
-->

# TR-0 - the actuation chokepoint census (return, 2026-09-06 CT)

## §0 THE CARD
**HEAD `093d5b4033fabcb54ed668a02471c91acef6a202`** (`main`; core porcelain empty at boot and at return). Instrument: `git grep` over `*/src/main/*.java` + `cat -n`. **Receipts: `ROOT/File.java:line`**, ROOT = the module dir (`src/main/java/com/homesynapse/<pkg>` elided): IA=integration-api, IR=integration-runtime, ZB=integration-zigbee, AU=core/automation, RA=rest-api, EM=event-model, SS=state-store, LC=lifecycle. Aliases: CRS=IR/CommandRoutingSubscriber.java, SCDS=AU/StandardCommandDispatchService.java, SAE=AU/StandardActionExecutor.java, CE=IA/CommandEnvelope.java. A bare `:n` continues the last-named file.

| P | Verdict | The separating receipt |
|---|---|---|
| P1 `CommandRoutingSubscriber` is the ONLY production consumer | **HOLDS** | `commandHandler()` at ONE `src/main` site (CRS:215); `handle(...)` at ONE (CRS:249) - §1 |
| P2 REST + automation share ONE ledger path | **HOLDS** | two `command_issued` producers (§2); ONE `command_dispatched` producer, bus-fed only (SCDS:221, :165); `.dispatch(` has 0 production callers |
| P3 the envelope carries NO principal | **HOLDS, sharpened** | 6 fields, none a principal (CE:60-67); `principal` absent from `src/main`; `command_dispatched` stamps AUTOMATION/actorRef=null for EVERY command (SCDS:233-235) - §3 |
| P4 zero direct adapter calls outside the subscriber | **HOLDS** | `.adapter()` at ONE `src/main` site (CRS:215); `routeTarget(` router-only; the adapter class is package-private (ZB/ZigbeeIntegrationAdapter.java:79) - §4 |

**One door:** every production actuation passes CRS:249 (`handler.handle(command)`), reached only via :235-236. **B-2 is a bounded insertion at one line.** The precondition gap (P3, §3): the principal must ride the `command_issued` envelope through the join cache, or the gate sits at :232 with the cached issued envelope. Docket rows in §6. The charter's `:87` is the class declaration; the actuation line is :249.

## §1 Q1 - production consumers of `CommandHandler` / `commandHandler()`
- Interface IA/CommandHandler.java:41-42, one method `handle(CommandEnvelope) throws Exception` :61; provider IA/IntegrationAdapter.java:122.
- **`src/main`, whole tree:** `commandHandler()` -> CRS:215 ONLY; `.handle(` on a `CommandHandler` -> CRS:249 ONLY (`invokeHandler` :246, submitted at :235-236).
- Implementation ZB/ZigbeeCommandHandler.java:66, exposed by ZB/ZigbeeIntegrationAdapter.java:450-451; the adapter never calls its own handler (`\.handle\(` in ZB `src/main` = empty).
- Test-only direct calls (not production): ZigbeeAvailabilityWiringTest.java:755, RecordingIntegrationFactory.java:112, the testFixtures stubs.

## §2 Q2 - producers of `command_dispatched` and `command_issued`
**`command_issued` - two producers:** (1) REST, RA/IssueCommandEndpoint.java:213-220 (`USER_COMMAND`, actorRef `null` :217, `publishRoot` :220). (2) Automation `CommandAction`, SAE:208 -> :236 -> `emitCommandIssued` :264-277 (`AUTOMATION`, actorRef = `automationId.value()` :276; correlation = the triggering event's, :400-402).
- Scenes (`ActivateSceneAction`) and `InvokeIntegrationAction`: zero-field records (AU/ActivateSceneAction.java:12, AU/InvokeIntegrationAction.java:13); the executor THROWS `UnsupportedOperationException("Tier 2 action reserved...")` SAE:222-225, caught :188 -> `"skipped"` :192. **No producer.**
- `EmitEventAction` (SAE:218-221 -> :383-386) emits an arbitrary `eventType`, but as an `EmittedDomainEvent` under `SubjectRef.automation` (AU/EmittedDomainEvent.java:32); the dispatch service requires `instanceof CommandIssuedEvent` (SCDS:169) and an ENTITY subject (AU/CommandDispatchAssembly.java:96-99). No side door.
- WebSocket: a Phase-2 scaffold; no event-model edge (api/websocket-api/src/main/java/module-info.java:15-17 requires only `api.rest`), no lifecycle wiring (LC/module-info.java:56); MODULE_CONTEXT:1 "read-only (no commands)". **No producer.**
- Lifecycle: LC/HomeSynapseCore.java publishes no command event (its `command_*` hits are comments, :707..:1063); it WIRES the subscribers (:747-753 dispatch, :772-783 ledger, :827-848 router).

**`command_dispatched` - ONE producer:** SCDS:217-222 -> `publish` :231-237, reached ONLY from its bus `onEvent` :165-178 (LIVE-only :166-168); the public `dispatch(...)` :135-146 has **zero** production callers. **The one ledger path:** REST | automation -> `command_issued` -> bus -> `command_dispatch_service` -> `command_dispatched` -> bus -> router (filter `{command_issued, command_dispatched}, DIAGNOSTIC, ENTITY`, IR/IntegrationSupervisorAssembly.java:82-85) -> CRS:249. Readers only: RA/GetCommandStatusEndpoint.java:143.

## §3 Q3 - what a gate one line before `handler.handle(...)` SEES
At CRS:249 (the adapter's command-executor thread, :233-236) the gate holds: `handler`; **`command` = CE:60-67:** `EntityId entityRef`, `String commandName`, `Map<String,Object> parameters` (unmodifiable :85), `Ulid commandEventId`, `Ulid correlationId`, `IntegrationId integrationId`; and `resultCause` = `CausalContext(Ulid correlationId, Ulid causationId)` (EM/CausalContext.java:47-49).
- **Principal: NONE** - no field, no `principal` type in `src/main`. The REST identity exists one layer up (`ApiKeyIdentity`, RA/RestFilters.java:573-580, `ctx.attribute` :580) but `EndpointContext` (RA/EndpointContext.java:29) has no identity accessor and `IssueCommandEndpoint` passes actorRef `null` (:217). `USER_COMMAND`'s own contract (EM/EventOrigin.java:37-42) requires that identity.
- **Automation id:** on the `command_issued` envelope's `actorRef` (SAE:276) - DROPPED by the router's cache (`CachedCommand(commandType, parameters, cachedAt)` CRS:305, filled :166-167). **Run id: on NO command envelope;** recoverable only by a store read on the correlation (`automation_action_started.runId`, SAE:365-367).
- **Correlation: YES** - the Run's for automation (SAE:400-402), a root for REST (RA/IssueCommandEndpoint.java:220, :231). **`commandEventId` = the `command_issued` id** (the router passes `causationId`, CRS:182 -> :229), not the `command_dispatched` id its javadoc claims (CE:46-49) - §6.1.
- A gate at **CRS:232 (bus thread; W5: never block)** also sees the `command_dispatched` `EventEnvelope` (EM/EventEnvelope.java:99-113), but its origin is **AUTOMATION for every command** and actorRef **null** (SCDS:233-235): it cannot tell a user's command from an automation's. Only `command_issued` can (USER_COMMAND/null vs AUTOMATION/automationId); the router receives it in `cacheIssued` (CRS:152) and discards both fields.

## §4 Q4 - paths to an adapter WITHOUT CRS:249
- `.adapter()` in `src/main`: CRS:215 only. `routeTarget(IntegrationId)` (package-private, IR/StandardIntegrationSupervisor.java:368; `RouteTarget` :359): production caller = the router (CRS:206-207) only; one test caller (StandardIntegrationSupervisorTest.java:283).
- The supervisor's own adapter touches are lifecycle: `initialize()` IR/StandardIntegrationSupervisor.java:494, `run()` :596, `close()` :823.
- `IntegrationAdapter` outside IR/IA `src/main`: only the zigbee implementation (ZB/ZigbeeAdapter.java:42; ZB/ZigbeeIntegrationAdapter.java:79, package-private). `ZigbeeIntegrationFactory.lastCreated()` :180: testFixtures callers only (ZigbeeHardwareFreeRig.java:200). Only `app` requires the zigbee module (app/homesynapse-app/src/main/java/module-info.java:30); `Main.java:114` builds the factory only.
- Fence (stated, not censused): the adapter's own protocol I/O inside ZB is module-internal, not a command path.

## §5 Q5 - SS/DispatchingProjectionAdvancer.java:135 is NOT actuation
`handler` there is `EnvelopeHandler` (SS/EnvelopeHandler.java:31, package-private; `handle(EventEnvelope, Consumer<EventEnvelope>)` :47; "MUST NOT call EventPublisher.publish() or open writes" :37-39). Its only implementation is `ForwardingHandler` (SS/DispatchingProjectionAdvancer.java:150) -> `processor.accept(envelope)` :158-159, wired :106-111. The state-store module has no edge to `com.homesynapse.integration` (core/state-store/src/main/java/module-info.java:9-19): `CommandHandler` is not resolvable there. **A projection read/forward seam; confirmed.**

## §6 Side-findings -> docket rows (the hub rules)
1. **[REVIEW] javadoc != code on `commandEventId`:** CE:46-49 says "the originating `command_dispatched`"; the router passes the `command_issued` id (CRS:182, :229) and the zigbee handler chains its `command_result` to it (ZB/ZigbeeCommandHandler.java:334, :345-346), while the router's OWN failure results chain to the `command_dispatched` id (CRS:203-204). Two causation conventions; B-2's REJECT result must pick one.
2. **B-2 precondition (P3):** carry `origin` + `actorRef` from the issued envelope into `CachedCommand` (CRS:305), then into `CommandEnvelope` (a public IA record: a Phase-2 interface change, `[REVIEW]`) or gate at CRS:232 on the cached envelope. REST half: the identity is already at RA/RestFilters.java:580; `IssueCommandEndpoint` need only set actorRef (:217), though `EndpointContext` is deliberately unwidened (rest-api MODULE_CONTEXT:257).
3. **`command_dispatched`'s origin is not evidence-based:** SCDS:234 stamps AUTOMATION for REST-issued commands too (Doc 01 §3.9; EM/EventOrigin.java:11-13). Inherit the issued envelope's origin at :176-177, or stamp SYSTEM.

## §7 Instrument limits, closeout
Read whole: the three named sources, EventOrigin, EnvelopeHandler, the websocket-api MODULE_CONTEXT, the protocol §2/§6. The other four MODULE_CONTEXTs (37-110 KB each) by heading scan + targeted grep (`command|dispatch|scene|invoke|actor|principal|gotcha|adapter`); a gotcha outside those terms could be unread. Tests READ as receipts, never run. No build, test or edit. Filed 2026-09-06 CT; reports to the hub.

RETURNED nexsys-hivemind/context/audits/2026-09-06_TR-0_actuation-chokepoint-census_return.md 10225
