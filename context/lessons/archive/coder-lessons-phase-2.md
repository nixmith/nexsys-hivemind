<!--
file: context/lessons/archive/coder-lessons-phase-2.md
purpose: Frozen Phase 2 coder lessons (Sprint 1 Block A; Blocks N, P, R) archived from coder-lessons.md.
audience: Coder
update-cadence: frozen
state-type: history
status: ARCHIVED
last-verified: 2026-05-21 against `homesynapse-core` commit `dfb045e`
-->

# Coder Lessons — Phase 2 Archive (2026-03-15 → 2026-03-20)

Archived from `context/lessons/coder-lessons.md` on 2026-05-21 as part of Batch F of the 2026-05-20 reorganization. 11 entries covering Sprint 1 Block A and Blocks N/P/R Phase 2 work. Rotation rule: `REORGANIZATION_PLAN_2026-05-20.md §4c`. Greppable — entries are frozen.

---

## 2026-03-15 | Category: build | Source: Sprint 1 Block A — first compile attempt
**Discovery:** The build machine's JDK version may not match the project's `sourceCompatibility`. JDK 21 had to be manually downloaded and configured — it was not pre-installed.
**Detail:** The Gradle scaffold targets Java 21 (via `JavaLanguageVersion.of(21)` in build-logic convention plugins), but the build environment only had JDK 11 installed. Fixed by downloading Adoptium JDK 21 from the API (`https://api.adoptium.net/v3/binary/latest/21/ga/linux/x64/jdk/hotspot/normal/eclipse`), extracting it, and passing `JAVA_HOME` plus `-Porg.gradle.java.installations.paths` to Gradle. The Gradle toolchain auto-detection did not find it without explicit configuration.
**Impact:** Any new build environment (CI, new machine, new session) must verify JDK 21 availability before attempting compilation. Consider adding a `check-jdk.sh` script or documenting the Adoptium download in a CONTRIBUTING.md. The Gradle toolchain feature handles this gracefully once the path is provided.

## 2026-03-15 | Category: module-boundaries | Source: Sprint 1 scaffold fix — empty package exports
**Discovery:** Scaffold `module-info.java` files that `exports` a package must have at least one `.java` source file in that package (beyond `package-info.java`). The compiler treats a package with only `package-info.java` as empty and fails with `-Xlint:all -Werror`.
**Detail:** Both `device-model` and `integration-api` modules had `module-info.java` files that exported their respective packages, but those packages contained only placeholder `package-info.java` files — no interfaces or types yet (those are Sprint 2+ work). The compiler warning became an error under `-Werror`. Fixed by commenting out the `exports` lines with `// TODO: uncomment in Sprint 2` comments.
**Impact:** When scaffolding new modules, either (a) don't add `exports` clauses until the package has real types, or (b) add a marker interface/class to prevent the empty-package issue. Option (a) is cleaner — the `exports` clause should be added in the same block that adds the first type to the package.

## 2026-03-15 | Category: build | Source: Sprint 1 — Gradle build-logic cache corruption
**Discovery:** The `build-logic/build/generated-sources/` directory can develop permission issues that prevent Gradle from cleaning it, causing `Unable to delete directory` errors.
**Detail:** Occurred when running `./gradlew check` — the build-logic subproject's cache directory had stale artifacts that couldn't be deleted. Fixed with `rm -rf build-logic/build` (which required explicit file-delete permission in the sandbox environment). Root cause unclear — possibly related to interrupted previous builds or file system permission changes.
**Impact:** If a Gradle build fails with "Unable to delete directory" errors in `build-logic/build/`, the first remedy is `rm -rf build-logic/build`. This is safe — the directory is fully regenerated. Consider adding `build-logic/build/` to `.gitignore` if not already present.

## 2026-03-15 | Category: other | Source: Sprint 1 payload types — dynamic-typed fields
**Discovery:** Doc 01 §4.6 specifies fields like `value: Any (typed per schema)` and `parameters: JSON Object` on event payload records. Since capabilities aren't defined yet (Doc 02), these fields use `String` (serialized JSON form) in Phase 2.
**Detail:** Fields affected: `StateReportedEvent.value`, `StateReportedEvent.rawProtocolValue`, `CommandIssuedEvent.parameters`, `StateConfirmedEvent.expectedValue/actualValue`, and similar. The design docs specify these as dynamically-typed based on the device capability schema, but the capability system (Doc 02) is Sprint 2 work. Using `String` for the serialized form is a pragmatic Phase 2 decision — the actual type resolution happens at deserialization time in Phase 3 when the capability registry exists.
**Impact:** When implementing these types in Phase 3, the `String` fields will need to be replaced with or augmented by proper typed representations. This is a known, documented tradeoff. The Phase 3 implementation should introduce an `AttributeValue` sealed interface or similar typed wrapper, with `String` as the serialization transport.

## 2026-03-15 | Category: other | Source: Sprint 1 Javadoc quality pass
**Discovery:** First-pass Javadoc on records often lacks cross-references (@see), nullability documentation, and thread-safety statements. A dedicated quality pass after initial creation catches these consistently.
**Detail:** Four files needed Javadoc fixes after initial creation: AutomationCompletedEvent (minimal class docs, inconsistent @param tags), TelemetrySummaryEvent (bare class docs missing aggregation semantics), StateChangedEvent (missing @see cross-references), EventPublisher (missing explicit thread-safety paragraph). The pattern: initial creation focuses on correctness and compilation; Javadoc completeness is a second concern that benefits from a separate pass.
**Impact:** Future blocks should build in a Javadoc review step after the compile gate passes. The quality pass should check: (1) every @param has nullability documented, (2) every type has @see cross-references to related types, (3) thread-safety is explicitly stated on interfaces, (4) class-level Javadoc explains the "why" not just the "what."

## 2026-03-20 | Category: module-boundaries | Source: Block N — websocket-api JPMS analysis
**Discovery:** The JPMS `requires transitive` rule from Block K applies universally — handoff-specified `requires` directives must always be verified against the expanded rule before trusting them.
**Detail:** Block N handoff (Locked Decision #10) specified `requires com.homesynapse.api.rest` (non-transitive). However, `ApiKeyIdentity` appears as a record component type in `WsClientState`, and `ApiException` appears in throws clauses of `MessageCodec.decode()`, `SubscriptionManager.subscribe()`, and `SubscriptionManager.unsubscribe()`. Both patterns require `requires transitive` per the Block K expanded JPMS rule. Changed proactively to `requires transitive com.homesynapse.api.rest` — same fix as Block K but applied before the compile gate rather than after a failure.
**Impact:** The expanded JPMS rule (record components, method params, return types, exception superclasses, exception types in throws clauses) is now confirmed across three blocks (I, K, N). Future handoffs should assume `requires transitive` for any inter-module dependency where the depended-on module's types appear anywhere in the public API surface. The PM has been advised, but the Coder should always verify independently.

## 2026-03-20 | Category: other | Source: Block N — nullable collection fields in records
**Discovery:** Nullable list fields in records require a conditional defensive copy pattern: `field != null ? List.copyOf(field) : null`. This is distinct from the non-null pattern used in all previous blocks.
**Detail:** `WsSubscriptionFilter` has 6 nullable `List<String>` fields (eventTypes, subjectRefs, areaRefs, labelRefs, entityTypes, capabilities). These use AND across fields, OR within arrays — a null field means "no constraint on this dimension." `List.copyOf(null)` throws NPE, so the compact constructor must guard each nullable list field individually. Previous blocks only had non-null collections where `List.copyOf(field)` was safe unconditionally.
**Impact:** Any future record with nullable collection fields must use the conditional pattern. This will likely appear in filter/query types. The pattern extends to `Map` fields: `field != null ? Map.copyOf(field) : null`.

## 2026-03-20 | Category: other | Source: Block P — byte array defensive copy in records
**Discovery:** Records with `byte[]` fields require TWO defensive copy operations — one in the compact constructor and one as an accessor override — because the record-generated accessor returns the internal array reference.
**Detail:** `ZnpFrame.data`, `EzspFrame.parameters`, and `ZclFrame.payload` are all `byte[]` fields. The compact constructor clones: `data = data.clone()`. But the auto-generated accessor `data()` returns the internal `data` field directly, allowing callers to mutate the record's state. The fix is to override the accessor: `@Override public byte[] data() { return data.clone(); }`. This was anticipated in the handoff and applied proactively to all three frame records.
**Impact:** Any future record with mutable array fields (byte[], int[], etc.) must apply this two-step pattern. This is a Java records design limitation — records are "shallowly immutable" for array fields. The pattern should be added to java-patterns.md as a standard reference.

## 2026-03-20 | Category: module-boundaries | Source: Block R — JPMS transitive chain audit revert
**Discovery:** A codebase audit that downgraded `requires transitive` to `requires` in observability's module-info.java was incorrect — transitive dependency analysis must trace the FULL type graph through all transitive chains, not just direct imports from the immediately-required module.
**Detail:** The audit changed observability's `requires transitive com.homesynapse.event` to `requires com.homesynapse.event`, reasoning that no event-model types appeared directly in observability's exported API. This caused a compile failure: `-Xlint:all -Werror` produced `[exports]` warnings on `TraceQueryService.java` because `Ulid` and `EntityId` (from `com.homesynapse.platform`) appeared in its method signatures. These platform-api types were only reachable through the transitive chain: `observability → event-model → platform-api`. The event-model module declares `requires transitive com.homesynapse.platform`, which makes platform-api types visible to observability's consumers — but ONLY if observability itself uses `requires transitive com.homesynapse.event`. When `transitive` was removed, the compiler correctly identified that observability's consumers would lose access to platform-api types used in the exported API. The device-model audit change was safe because device-model independently declares `requires transitive com.homesynapse.platform`, providing an alternate path.
**Impact:** When auditing or reviewing JPMS `requires transitive` directives: (1) identify ALL types used in the module's exported API signatures, (2) for each type, trace every possible path through which consumers receive it, (3) if removing `transitive` from any link in the chain would break a consumer's access to a type in the exported API, the `transitive` must stay. The `-Xlint:all -Werror` `[exports]` warning is the compiler's enforcement of this rule — trust it.

## 2026-03-20 | Category: other | Source: Block R — conditional null validation in records
**Discovery:** Records can enforce status-dependent null constraints in compact constructors — a pattern where a field's nullability is conditional on another field's value.
**Detail:** `SubsystemState.error` is nullable, but its nullability depends on `SubsystemState.status`: when status is `FAILED`, error MUST be non-null (the failure reason); when status is `RUNNING` or `STOPPED`, error MUST be null (no error in healthy/terminated state). The compact constructor enforces this with two conditional checks after the requireNonNull calls for non-nullable fields. This is the first record in the project with this pattern — previous nullable fields (TraceEvent.causationId, WsSubscriptionFilter lists) had unconditional nullability.
**Impact:** Future records where field validity depends on another field's value should use this conditional validation pattern in the compact constructor. Document the constraints explicitly in Javadoc on both the record class and the affected fields.

## 2026-03-20 | Category: module-boundaries | Source: Block P — `non-sealed` for interface subtypes of sealed interfaces
**Discovery:** Java 21 requires all direct subtypes of a sealed interface to declare one of `sealed`, `non-sealed`, or `final`. Interfaces cannot be `final`, so implementable interface subtypes must use `non-sealed`.
**Detail:** `ManufacturerCodec` is a sealed interface permitting `TuyaDpCodec` and `XiaomiTlvCodec`. Both subtypes are interfaces (not classes or records) because they need Phase 3 implementations. Java 21 requires the `non-sealed` modifier: `public non-sealed interface TuyaDpCodec extends ManufacturerCodec {}`. Without it, the compiler reports: "sealed, non-sealed or final modifiers expected." This is the first sealed interface in the project where the permits are themselves interfaces rather than records.
**Impact:** Future sealed interfaces that permit interface subtypes (as opposed to record subtypes) must use `non-sealed` on those subtypes. All prior sealed interfaces (DomainEvent, IntegrationLifecycleEvent, WsMessage, ZigbeeFrame) permitted only records, so this pattern wasn't needed before.
