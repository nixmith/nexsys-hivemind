<!--
file: context/instructions/2026-08-05_S-5c_sidecar-atomic-write_coding-instruction.md
purpose: S-5c — the pre-freeze micro-WU ruled at R-B(a) (Nick, 2026-08-05): make the zigbee sidecar write atomic (temp-then-move, copying the in-module PersistentNetworkParameterStore idiom) so a power-cut mid-flush cannot silently discard the availability seed (the REV-1 F-3 finding, MED, byte-verified). Nick's scope fence binds: temp-then-move ONLY — no fsync, no durability crusade; the N-4 documented contract (synchronous=NORMAL posture) governs power-cut tail durability.
audience: the Coder (core lane, host-CC desk)
status: ISSUE-READY. baseline: core `60d3ab5` at authoring — S-5a may land first; RE-DERIVE HEAD at launch and state which baseline you ran on (either is lawful; the touched files do not overlap S-5a). Return → `context/audits/2026-08-05_S-5c_return.md`. The lane commits NOTHING.
-->

# Coding Task: S-5c — atomic sidecar write (`ZigbeeDeviceCache`)

**Subsystem:** integration-zigbee · **Design Doc:** Doc 05 Integration Runtime (Locked) — no contract change · **Phase:** 3-Implementation · **Brief ref:** REV-1 F-3 + Nick's R-B(a) ruling with the scope fence

## What This Implements

`ZigbeeDeviceCache.write` persists the sidecar via in-place `Files.writeString` (`:470–472`) — a crash or power cut mid-write leaves a partial file the loader lawfully discards (`:648–649` class), silently defeating the WU-AVAIL-SEED availability seed for that boot (the F2 producer; an SD-card Pi with a three-boot nightly multiplies flush windows). The fix copies the module's own proven idiom — `PersistentNetworkParameterStore` writes temp-then-move (`:134–136`) — so a torn write can no longer replace a good file. **Nick's fence: temp-then-move ONLY; no fsync additions anywhere.**

## Files to Read (minimum set)

`integration/integration-zigbee/MODULE_CONTEXT.md` + `module-info.java` · `ZigbeeDeviceCache.java` whole (the write path :460–:490, the F-14 outside-the-lock comment, the loader/discard path ~:640–:660) · `PersistentNetworkParameterStore.java` :120–:145 (the idiom to copy, including its `.tmp` naming and `REPLACE_EXISTING` move) · the REV-1 return §F-2/F-3 region (`context/audits/2026-08-04_REV-1_physics-spine_adversarial-review_return.md`).

## STOP-on-Mismatch Gates

| Check | Expected |
|---|---|
| `ZigbeeDeviceCache.java:470–472` region | in-place `Files.writeString(file, json, UTF_8)` with the F-14 outside-the-lock comment above it |
| `PersistentNetworkParameterStore.java:134–136` | `.tmp` sibling + `Files.move(…, REPLACE_EXISTING)` |
| core porcelain | CLEAN at the launch-derived HEAD before any edit |

## Files to Create or Modify

| Action | File | Description |
|---|---|---|
| MODIFY | `integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeDeviceCache.java` | The write lands to a `.tmp` sibling then `Files.move(temp, file, REPLACE_EXISTING)`; the F-14 outside-the-lock structure and the debounce/flush seams are UNCHANGED; update the racing-writers comment to state the new invariant (a reader/loader can never observe a partial file) |
| MODIFY or CREATE | the module's cache test class (Coder locates; likely `ZigbeeDeviceCacheTest`) | The torn-write red-first test (below) |

## Test Requirements (red-first per format #18)

1. **The torn-write pin (RED at baseline):** simulate the pre-fix hazard — write a truncated/invalid JSON to the sidecar path, then assert load discards-and-WARNs (this doubles as the load-path pin Nick's rider requested — currently untested); THEN assert the new write path cannot produce that state: after `write`, a crash-window simulation (the `.tmp` exists or the move completed — never a partial at the final path) leaves the FINAL path either the old complete file or the new complete file. Realize the crash-window assert honestly within JUnit's reach (e.g. verify the write goes through a temp sibling and the final path is only ever replaced by a completed move — inspect the mechanism, do not fake a power cut); disclose the reach honestly in the return.
2. Preservation: the existing cache round-trip tests stay green.

**§4c applies (non-whitelisted module):** *Tests must inject `Clock`.* Do NOT use `Clock.systemUTC()`, `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()` in this module's test code. Use `Clock.fixed(...)` injected via constructor/`@BeforeEach`. Enforcement reach: `NO_DIRECT_TIME_ACCESS` runs from `com.homesynapse.app`'s test classpath — it does **not** scan this module's test source set; Clock-injection here is a self-enforced convention that PM review, not `./gradlew check`, enforces.

## P2 Survey

Module-internal single-consumer change (the write path's callers — the debounced cycle write + `flush()` — are enumerated in the Files-to-Read region and unchanged in signature). No module-info change; no boundary crossed; ARCH-RULE-REACH N/A beyond §4c above. No count pins on this class known; the Coder's launch grep for `ZigbeeDeviceCache` consumers confirms.

## Out of Scope (Nick's fence + standard)

fsync/durability changes of ANY kind (N-4's documented posture governs) · the loader's discard semantics (pin them, don't change them) · F-2/F-4/F-5/F-6/F-7/F-8 (shelved) · S-5a's toml (parallel WU) · the Pi deploy (H3 carries it).

## Gates & Success Criterion

Targeted `:integration:integration-zigbee` compile + tests → **full `./gradlew check` (CC-lane grant; quote the count)**. DONE when: the write is temp-then-move; the torn-write/load-pin test exists and the red-first record is honest; census (expect **exactly 2 entries**: the main file M + the test file M/A — state which); WUCP Phase 1 complete; return filed. Pushback welcome — evidence over instruction.
