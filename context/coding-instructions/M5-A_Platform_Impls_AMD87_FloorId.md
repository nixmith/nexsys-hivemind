<!--
file: context/coding-instructions/M5-A_Platform_Impls_AMD87_FloorId.md
amd-number-note: the Expectation codec is **AMD-87** (reassigned from the retired AMD-65 per INV-GA-02 — AMD-64/65 retired post Research 5 v2; AMD-86 = INV-PD-07/crypto; AMD-87 next clean). The live `@Disabled("AMD-65 pending")` annotation in EventPayloadCodecTest is the retired number in existing code — delete it, do not re-number.
purpose: M5-A coding instruction — platform deployment impls (PlatformPaths/HealthReporter) + AMD-87 Expectation codec + FloorId Jackson registration. The small-Core lane of the M5 window (decisions D1–D8; charter weeks/2026-W24).
audience: Coder (Claude Code), PM
status: ISSUE-READY for the platform + FloorId parts; the AMD-87 codec part is ⛔ GATED on AMD-87 lightweight ratification (un-gate when AMD-87 RATIFIED).
baseline: homesynapse-core HEAD `8ef9e9f` (M4 COMPLETE; build GREEN 145 tasks). Re-verify at issue.
-->

# Coding Task: M5-A — Platform Deployment Impls + AMD-87 Expectation Codec + FloorId Registration

**Subsystem:** platform (platform-api impls) + persistence (codec + typed-ID registration)
**Design Doc:** Doc 12 §8.2/§8.3 (HealthReporter/PlatformPaths, Locked); AMD-87 (Expectation codec, PROPOSED — gates Part 2); AMD-44 (FloorId, RATIFIED).
**Phase:** 3-Implementation
**Task Brief Reference:** M5 window charter (`context/planning/weeks/2026-W24_jun08-jun14.md`), lane M5-A; decisions D1–D8.

## What This Implements

The small, dependency-free Core lane of the M5 window. Three independent pieces: **(1)** the deployment-tier implementations of the two already-frozen `platform-api` interfaces — `PlatformPaths` (filesystem layout) and `HealthReporter` (supervisor health reporting) — which exist today only as interfaces (Doc 12 §8.2/§8.3); **(2)** the **AMD-87** `Expectation` persisted codec so a command-bearing `CapabilityAdded` round-trips (clears the M9 prerequisite; gated on AMD-87 ratification); **(3)** the one-line `FloorId` Jackson registration (the B-S1 carry-item). These do not depend on the crypto design (Doc 15) and run in parallel with its DOCS review. **Deliberately small** — do not expand it.

## Files to Read Before Starting

| File | Why |
|---|---|
| `platform/platform-api/MODULE_CONTEXT.md` | `PlatformPaths`/`HealthReporter` contracts; Phase-3 Notes name the impls (`LinuxSystemPaths`/`LocalPaths`, `SystemdHealthReporter`/`NoOpHealthReporter`) |
| `platform/platform-api/src/main/java/module-info.java` | verbatim — see embed below |
| `platform/platform-api/src/main/java/com/homesynapse/platform/PlatformPaths.java` | the 6-method interface to implement (binaryDir/configDir/dataDir/logDir/backupDir/tempDir) |
| `platform/platform-api/src/main/java/com/homesynapse/platform/HealthReporter.java` | the 4-method interface (reportReady/reportWatchdog/reportStopping/reportStatus); sd_notify contract C12-03 |
| `platform/platform-systemd/MODULE_CONTEXT.md` + `build.gradle.kts` | scaffold module (no `module-info.java` yet); already has `implementation(project(":platform:platform-api"))` |
| `core/persistence/MODULE_CONTEXT.md` + `src/main/java/module-info.java` | verbatim module-info below; the Jackson-isolation rule |
| `core/persistence/src/main/java/com/homesynapse/persistence/PersistenceJacksonModule.java` | the registration pattern (`registerTypedWrapper`; `addSerializer(AttributeValue.class, …)`) — FloorId + Expectation register here |
| `core/persistence/src/main/java/com/homesynapse/persistence/AttributeValueSerializer.java` | **the precedent the Expectation codec mirrors** — tagged-union `{"t":…,"v":…}`, bit-anchored float, no-`default` switch |
| `core/device-model/src/main/java/module-info.java` | verbatim below — the new persistence→device edge target |
| `core/device-model/src/main/java/com/homesynapse/device/Expectation.java` + `ExactMatch`/`WithinTolerance`/`EnumTransition`/`AnyChange.java` | the 4 permit shapes the codec serializes |
| `core/persistence/src/test/java/com/homesynapse/persistence/EventPayloadCodecTest.java` | the `capabilityAdded_onOff_roundTrips` acceptance test to un-disable — **its annotation literally reads `@Disabled("AMD-65 pending")` at HEAD** (AMD-65 is the *retired* number; this WU is AMD-87 — just delete the annotation, do not re-number it) + `TestEventSamples.capabilityAddedOnOff()` |
| `design/amendments/AMD-87_Expectation_Persisted_Codec.md` | the codec spec (Part 2) — implement to it |

### Verbatim `module-info.java` (embedding rule — do not paraphrase module names)

**platform-api (unchanged):**
```java
module com.homesynapse.platform {
    exports com.homesynapse.platform;
    exports com.homesynapse.platform.identity;
}
```
**platform-systemd (does NOT exist yet — CREATE it):**
```java
// NEW — platform/platform-systemd/src/main/java/module-info.java
module com.homesynapse.platform.systemd {
    requires com.homesynapse.platform;
    exports com.homesynapse.platform.systemd;
}
```
**persistence (current — Part 2 adds ONE requires):**
```java
module com.homesynapse.persistence {
    requires transitive com.homesynapse.platform;
    requires transitive com.homesynapse.state;
    requires transitive com.homesynapse.event;
    requires transitive com.homesynapse.event.bus;
    requires com.homesynapse.value;
    requires java.sql;
    requires org.slf4j;
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.databind;
    requires com.fasterxml.jackson.datatype.jsr310;
    requires com.fasterxml.jackson.module.blackbird;
    exports com.homesynapse.persistence;
}
// Part 2 (AMD-87) PROPOSED DIFF:  + requires com.homesynapse.device;
```
**device-model (unchanged — the edge target; confirms acyclic, device does NOT require persistence):**
```java
module com.homesynapse.device {
    requires transitive com.homesynapse.value;
    requires com.homesynapse.event;
    requires transitive com.homesynapse.platform;
    exports com.homesynapse.device;
}
```

## Files to Create or Modify

| Action | File Path | Description |
|---|---|---|
| CREATE | `platform/platform-systemd/src/main/java/module-info.java` | `module com.homesynapse.platform.systemd { requires com.homesynapse.platform; exports com.homesynapse.platform.systemd; }` |
| CREATE | `platform/platform-systemd/.../platform/systemd/LinuxSystemPaths.java` | `PlatformPaths` impl — Tier-1 FHS paths (`/opt/homesynapse`, `/etc/homesynapse`, `/var/lib/homesynapse`, `/var/log/homesynapse`, `/var/lib/homesynapse/backups`, `/var/lib/homesynapse/tmp`); resolve+cache once; create writable dirs; clean `tempDir()` |
| CREATE | `platform/platform-systemd/.../platform/systemd/LocalPaths.java` | `PlatformPaths` impl — development tier, all dirs under CWD (DP-1: see Watch-Out) |
| CREATE | `platform/platform-systemd/.../platform/systemd/SystemdHealthReporter.java` | `HealthReporter` impl — sd_notify (`READY=1`/`WATCHDOG=1`/`STOPPING=1`/`STATUS=…`) via the `$NOTIFY_SOCKET` Unix datagram socket |
| CREATE | `platform/platform-systemd/.../platform/systemd/NoOpHealthReporter.java` | `HealthReporter` impl — all methods no-op (non-systemd/dev) |
| CREATE | `platform/platform-systemd/src/test/...` | unit tests for all four (see Test Requirements) |
| MODIFY ⛔ | `core/persistence/src/main/java/module-info.java` | **+ `requires com.homesynapse.device;`** (AMD-87 — the JPMS STOP-gate) |
| CREATE ⛔ | `core/persistence/.../persistence/ExpectationSerializer.java` + `ExpectationDeserializer.java` | package-private; AMD-87 tagged-union codec over the 4 permits |
| MODIFY ⛔ | `core/persistence/.../persistence/PersistenceJacksonModule.java` | + `addSerializer(Expectation.class, …)` / `addDeserializer(Expectation.class, …)` (AMD-87) **and** + `registerTypedWrapper(FloorId.class, FloorId::toString, FloorId::parse)` (FloorId, NOT gated) |
| MODIFY ⛔ | `core/persistence/.../persistence/EventPayloadCodecTest.java` | remove `@Disabled` from `capabilityAdded_onOff_roundTrips` (AMD-87 acceptance) |
| CREATE | `core/persistence/.../persistence/...Test` | FloorId round-trip test (NOT gated) |

⛔ = the AMD-87 codec + persistence→device edge are **gated on AMD-87 lightweight ratification**. The platform impls (Part 1) and the FloorId registration + its test (Part 3) are **NOT gated** — they may land first. (FloorId registration is in `PersistenceJacksonModule` but is independent of the device edge.)

## Technical Specification

### Part 1 — Platform impls
Implement `PlatformPaths` (6 methods, absolute `Path`, resolved-once-and-cached, writable dirs created at construction, `tempDir()` cleared on construction per C12-10) and `HealthReporter` (4 methods). `SystemdHealthReporter`: open the `AF_UNIX` `SOCK_DGRAM` socket named by `$NOTIFY_SOCKET`, send the `sd_notify` datagrams; `reportReady()` exactly once; thread-safe (`reportStatus` callable from any thread). `NoOpHealthReporter`: every method a no-op. `LinuxSystemPaths`/`LocalPaths`: thread-safe immutable-after-construction. **No selection/wiring logic** — instantiation/tier-detection is the composition root's job (lifecycle/M13), OUT of scope here.

### Part 2 — AMD-87 Expectation codec (⛔ gated)
Implement exactly to `AMD-87_Expectation_Persisted_Codec.md` §2: hand-rolled `Expectation` `JsonSerializer`/`JsonDeserializer` pair, **keyed on the `Expectation` interface**, registered in `PersistenceJacksonModule`, tagged-union `{"t":"<permit-simple-name>", …}` mirroring `AttributeValueSerializer`, **exhaustive `switch` with NO `default`** over `ExactMatch(AttributeValue)` / `AnyChange(AttributeValue)` (both delegate `v` to the existing `AttributeValue` codec) / `EnumTransition(String)` / `WithinTolerance(double target, double tolerance)` (**AMD-52 bit-anchored-float treatment** — `Double.doubleToLongBits`, non-finite sentinels, `−0.0`→`+0.0`). Add `requires com.homesynapse.device;` to persistence module-info.

### Part 3 — FloorId registration (not gated)
One line in `PersistenceJacksonModule`: `registerTypedWrapper(FloorId.class, FloorId::toString, FloorId::parse)` — the generic `TypedUlidSerializer`/`TypedUlidDeserializer` pattern (the same as the 8 existing wrappers + `EventId`). `FloorId` is in `com.homesynapse.platform.identity` (already readable — persistence `requires transitive com.homesynapse.platform`). Closes the platform-api MODULE_CONTEXT OPEN item.

## Locked Decisions That Apply
- **LTD-04 (ULID):** `FloorId` is a typed ULID wrapper; register via `toString`/`parse` (Crockford Base32 at the serde boundary), never expose Jackson on `platform-api`.
- **LTD-08 (Jackson):** all serde in `core/persistence` only; domain types stay Jackson-annotation-free.
- **LTD-11 / AMD-26 (VT safety):** any locking in `SystemdHealthReporter` uses `ReentrantLock`, never `synchronized`.
- **LTD-13 (jlink/systemd):** `SystemdHealthReporter` targets the systemd `$NOTIFY_SOCKET`; `NoOpHealthReporter` is the non-systemd fallback.

## Invariants That Must Hold
- **AMD-87-INV-01:** every `Expectation` permit round-trips losslessly; `WithinTolerance` doubles are bit-anchored (AMD-52). Test: the un-`@Disabled` acceptance + a per-permit round-trip suite.
- **`NO_JACKSON_IN_DOMAIN_MODEL` (ArchUnit Rule 10):** the codec lives in persistence; `Expectation`/permits gain no annotations. Test: `./gradlew check` ArchUnit.
- **C12-03 (watchdog):** after `reportReady()`, `reportWatchdog()` is the heartbeat; `SystemdHealthReporter` sends `WATCHDOG=1`. (The *scheduling* of the heartbeat is lifecycle's; the reporter just sends.)

## Event Types Produced or Consumed
None produced. The AMD-87 codec round-trips `capability.added` / `capability.removed` payloads (already-registered event types) — it adds no event type. **P2 survey result (below): no event-type set, count-pin, or manifest aggregator is touched by M5-A.**

## P2 Consumer/Pin (Fan-Out) Survey
Run before issue (done at authoring; re-confirm at code time):
- **Registered-typed-wrapper set (FloorId):** no test pins the *count* of registered wrappers in `PersistenceJacksonModule` (grep clean). `FloorId` registration is purely additive — no count-pin to update. The platform-api `TypedIdTest` (9 wrappers incl. FloorId) is separate and already current (M4.B-S2).
- **Expectation codec:** the only consumer/pin is the `@Disabled` acceptance test (un-disable it). No count-pin, no manifest, no exhaustive switch elsewhere over `Expectation` (the codec's own switch is the only one; it is no-`default` so a future permit compile-breaks here — intended).
- **Event-class manifests / category tables:** untouched (no new event types).
- **module-info:** the only JPMS change is persistence `+requires com.homesynapse.device` (Part 2). platform-systemd gets a new module-info (Part 1). No other module-info changes. Verify both at the build gate.

## Test Requirements
### Unit
- **platform-systemd:** `LinuxSystemPaths` (6 paths correct + cached + dirs created + tempDir cleared); `LocalPaths` (CWD-relative); `SystemdHealthReporter` (datagram content `READY=1`/`WATCHDOG=1`/`STOPPING=1`/`STATUS=…` against a test datagram socket; `reportReady` once); `NoOpHealthReporter` (no I/O — pairs with `NoRealIoExtension`).
- **persistence (⛔ AMD-87):** per-permit `Expectation` round-trip (all 4); `WithinTolerance` bit-identity (e.g. `0.1`, `NaN`, `−0.0`); the un-`@Disabled` `capabilityAdded_onOff_roundTrips` passes.
- **persistence (FloorId):** `FloorId` serialize→deserialize round-trip (Crockford Base32).

### §4c Arch-Rule Reminder (persistence test code — non-whitelisted)
> **Tests must inject `Clock`.** Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in `core/persistence` test code — the `NO_DIRECT_TIME_ACCESS` ArchUnit rule scans non-whitelisted test classes and fails `./gradlew check`. Use `Clock.fixed(Instant.parse("2026-01-01T00:00:00Z"), ZoneOffset.UTC)`. (The Expectation/FloorId serde tests likely need no clock at all — but if any fixture does, inject it.) This does NOT apply to `platform-systemd` tests (`com.homesynapse.platform..` is whitelisted).

## What to Watch Out For
- **STOP-on-mismatch — the persistence→device JPMS edge (G3, the load-bearing gate).** Adding `requires com.homesynapse.device` must keep the graph acyclic. Verified at authoring (device requires value/event/platform, NOT persistence). If the build reports a cycle, STOP and report — do not restructure the codec silently.
- **DP-1 (placement of the dev impls) — pushback welcome.** This instruction puts all four impls in `platform-systemd` (one module, smallest footprint). `NoOpHealthReporter`/`LocalPaths` are not strictly "systemd." If you judge a cleaner split (e.g., dev impls in `app/homesynapse-app` with the composition-root selector), STOP and propose it — do not just do it. Either way, **no selection/tier-detection logic in M5-A** (that's lifecycle/M13).
- **sd_notify is a Unix *datagram* (`SOCK_DGRAM`) socket**, not a stream; `$NOTIFY_SOCKET` may be an abstract socket (leading `@` → NUL byte). Send-and-forget; do not block on a reply. If `$NOTIFY_SOCKET` is unset, `SystemdHealthReporter` should not be selected (composition root's job) — but guard defensively.
- **Expectation codec keying:** key on the `Expectation` *interface* (Jackson walks interfaces) exactly as `AttributeValue` is keyed — do NOT register per-permit. Mirror `AttributeValueSerializer` for the float handling; do not re-invent the float encoding.
- **Jackson isolation:** no `@JsonTypeInfo`, no annotations on `Expectation`/permits — the `"t"` discriminator is written by the serializer (Rule 10).
- **`WithinTolerance.evaluate()` still throws** — that's correct; AMD-87 is the *codec*, not the evaluator (automation, M7/M8). Do not implement `evaluate()`.

## Coder Pushback Welcome
Raise anything: if the sd_notify socket handling, the dev-impl placement (DP-1), or the persistence→device edge looks wrong or has a cleaner form at the same contract, flag it via the escalation format rather than silently diverging.

## Out of Scope
- Composition-root tier-detection / impl-selection / boot wiring (lifecycle / M13).
- `Expectation.evaluate()` implementations (automation, M7/M8).
- Any crypto / at-rest encryption / `chain_hash` activation (Doc 15 / M6 — separate).
- DEK/key-management, the secret store, `CredentialRotator` (M6).
- The verification-foundation test harness (M5 C4, separate quick-scope).

## Build Gate (deferred to Nick)
Coder produces files only. Nick runs `./scripts/clean.sh && ./gradlew check --continue` (full — ArchUnit `NO_DIRECT_TIME_ACCESS` + `NO_JACKSON_IN_DOMAIN_MODEL` + spotless). Flag the deferred gate in the coder-handoff so the PM tracks it under Open Risks (P3/§4b). Target: GREEN in one round (the P2 survey above is why).

## Work Unit Completion (WUCP Phase 1)
After the gate passes (or is deferred), execute WUCP Phase 1: update `platform-systemd` + `persistence` MODULE_CONTEXT.md (platform-systemd: scaffold→populated, the 4 impls + new module-info; persistence: the Expectation codec + FloorId registration + the new device edge); update coder-handoff.md (next-WU pointer + Deferred Build Gate flag); append to coder-lessons.md if anything bit you (esp. sd_notify or the JPMS edge); post a cross-agent note if the DP-1 placement changed. Not done until the checklist is complete.
