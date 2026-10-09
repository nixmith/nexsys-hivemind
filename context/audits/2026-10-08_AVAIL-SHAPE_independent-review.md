<!-- file: context/audits/2026-10-08_AVAIL-SHAPE_independent-review.md
purpose: independent review of the AVAIL-SHAPE instruction against 49455fc, every row re-run on the desk (`Z/`=integration-zigbee main, `ZT/`=its test twin, `L/`=lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/) -->

## §0 Verdict
NOT-READY — three blocking edits (an out-of-table IT that cannot stay green, a discriminator that is constant-false at the bytes, an incomplete one-timeout sweep); the design otherwise holds.

## §1 Premise rows
| row | result | command (`git --no-optional-locks show 49455fc:<path> \| …`) | printed |
|---|---|---|---|
| 1 | HOLDS | `grep -n MAINS_PING_SILENCE` tracker | `:71`; compare `:409` inside `if (isMainsPowered(` `:407`; `silenceLimitFor` else-arm `:413` |
| 2 | HOLDS | `sed -n 425,440p` | `silenceLimitFor` `:431–:439`; WARN `:435` |
| 3 | IMPRECISE | `grep -n expectedSilenceFor` adapter | method `:779–:788` (cited `:775–:786`); passed `:462` in the ctor call `:459` |
| 4 | HOLDS | `sed -n 62,113p` configurator | rows as stated; `0xFFFF` `:68`; `PowerMeter.java:52` = 1200 |
| 5 | HOLDS | `sed -n 296,312p` | `:297–:309` → `transition`; `DeviceState` `:159–:178`, no counter |
| 6 | HOLDS | `sed -n 751,768p` | `log.debug("zigbee.availability_ping: …` `:758` |
| 7 | HOLDS | `sed -n 814,826p`; grep | `pingBasic` `:814–:826`; `:186 = 5_000` |
| 8 | HOLDS | grep | `:284` |
| 9 | HOLDS +fact | grep; `sed -n 650,668p` | `:665` after `processCycle()` `:660`; the period is a CONSTANT `PRODUCTION_CYCLE_MILLIS = 50` `:171` (`:1236–:1237`) |
| 10 | HOLDS | `sed -n 385,392p` | `:389` |
| 11 | HOLDS | `grep -n containsExactly ZT/*`; MODULE_CONTEXT | changed `:368`, `:1025`, `:1125`; link `:1059`, `:1090`, `:1113`; ping `singleElement()` `:373`, `:608`; FROZEN `:636`, `:864` |
| 12 | FAILS (incomplete) | `git grep -n 'rig.silence(\|ping_timeout\|isEqualTo("offline")' 49455fc -- '*.java'` | the four cited hold; ALSO one-timeout→dark: `ZT/ZigbeeAvailabilityWiringTest.java:482–:515` (T-4, `"offline"` `:512`) and `L/AvailabilityBootTruthIT.java:72–:118`, `:122–:156` (`rig.silence(HUE)` + ONE `deliverAndCycle()` = one `runCycleOnce()`, rig `:259–:262`) |
| 13 | HOLDS | grep | captures `:299` INFO, `:339` DEBUG, `:572`, `:598`; restore `:137` |
| 14 | HOLDS (read) | `sed -n 1154,1161p` | `mainsInterview()`: EP 11, clusters `0x0000,0x0003,0x0006,0x0008`, mains; adopted via `recordInterview(interview, null)` `:1192` → no profile → under `b` 3,660 s |
| 15 | FAILS | `git grep -n 'D-v94-25' 49455fc -- '*.java'` | 3 files: tracker `:57`, `ZT/StandardAvailabilityTrackerTest.java:216` (`.as` text), `L/AvailabilityBootTruthIT.java:147` AND `:155` `isLessThanOrEqualTo(Duration.ofSeconds(90))` — a test literal DOES pin 90 |
| 16 | HOLDS | greps; bench log | `:1395`, `:1409`, def `:1422`; 0; log 0 / 10 |
| 17 | HOLDS | seds | record as stated; `deviceProfile()` `:616–:627`; `inputClusters` `:35` |
| 18 | HOLDS +arms | seds | walk `:219–:270`; metering override `:381–:389`; `effectiveRow` `:522–:534`; see F5/F6 |
| 19 | not checkable | runtime | the S31 profile has an `exact_model` match only (zigbee-profiles.json `:122–:141`); its clusters are not in the repo |

## §2 Findings
1. [BLOCKING] `L/AvailabilityBootTruthIT` runs at the default `check` gate (lifecycle `build.gradle.kts:96–:103`); both tests script ONE unanswered ping → UNAVAILABLE on the rig's Hue (`ZigbeeHardwareFreeRig.java:102–:106`: clusters `0x0006,0x0008,0x0300`, mains; profile `philips_hue_white_color_a19`, no skip/override). Under K = 2 one `deliverAndCycle()` never reaches dark (`awaitTrue` polls, never cycles, `:201–:207`); under `b` the 61 s / 11 min advances sit inside 3,660 s so NO probe fires; `:155` pins ≤ 90 s. It is in neither §3 nor §6 nor §12. Edit: add it as the 8th M row (census 0 A + 8 M), re-script both tests (a second cycle; under `b` advance 3,661 s and re-cut the 90-s assertion to the amended acceptance), widen row 12's instrument to `git grep -n 'rig.silence(\|ping_timeout' -- '*.java'`.
2. [BLOCKING] `seen_during_probe` as written is constant-false: `zclGlobalExchange` (`Z/EzspCoordinatorProtocol.java:2009–:2037`) waits in `awaitIncomingLocked` (`:1874–:1908`), which ENQUEUES every non-matching callback (`:1906` → `enqueueCallbackLocked` `:937–:946`); nothing ingests until the next `processCycle()` (`:660`), so `tracker.lastSeen()` cannot advance in the window (the wiring fake is the same: `handleUnicast` `:1461–:1498` returns frames the real protocol parks). W-1 scenario 2 (`=true`) is unsatisfiable. Edit: define the discriminator by a mechanism that sees the window — (A) a package-private peek `EzspCoordinatorProtocol.pendingCallbackFrom(nwk)` read after the exchange (one more M file), or (C) `ingestion.processCycle()` after a TIMEOUT before the line (the ingested frame then also resets the miss counter, coherent with §4.3) — and script W-1(2) by the fake's unicast handler adding a report frame beside the silent ping.
3. [BLOCKING] The one-timeout sweep (row 12, W-2) misses in-scope scenarios: T-4 `ZT:482–:515` (K = 2, both words); under `b` also DP-5(b) `:582–:618` (`:612–:617` re-pings at 61 s — W-4 says it "stays green"; it does not) and "mains ping-success" `:744–:776` (`:755–:758` 11 min → 1 unicast; `:767–:774` the 61-s re-ping). Edit: W-2 lists seven ZT scenarios + the IT's two; drop W-4's claim; §12's "four" becomes the full count.
4. [REVIEW] Row 15 fails: the amended acceptance DOES move a test literal (`L/…IT.java:155`); §4.2's "not a test literal" must name it.
5. [REVIEW] The walk is a SUPERSET of the configured contract on the metering arm: `configureMetering` (`:348–:371`) configures 0x0B04/0x0702 only when the R3 formatting read succeeded (`hasElectrical()`/`hasMetering()`; kWh for 0x0702); the MAX depends on the override only (`:385–:389`), never on the formatting. Direction: under `b` an unreadable-formatting plug gets 660 not 3,660; under `b-metered` 660 not the floor. Edit: state the assumption in §4.2 (or gate the metering rows on `formattingStore.cached(device, ep)` `:291` — memory, not wire) and name it a [REVIEW] row.
6. [REVIEW] The 0xFFFF "skipped" rule is the instruction's, not `configureDevice`'s: `:470` tests the READBACK; an override's 0xFFFF is SENT as-is (`:429–:430`). Right as a limit rule; §4.2/§9 bullet 5 should call it an intentional divergence so the lane does not hunt for a branch to mirror. Name the IAS arm too (`:231–:234`, no row).
7. [REVIEW] §4.3 vs §9 bullet 2: `recordFrame` (`:239–:246`) holds NO lock — it delegates to `transition`, which locks at `:477`; "reset in `recordFrame` before its existing work" is an unlocked write. Edit: the reset lives in `transition`'s `if (available)` block (`:489–:495`) under the lock; `recordCommandResult(false)` counts under its own acquisition (ReentrantLock `:185`), releases, then calls `transition`, using `computeIfAbsent` as `:479` does (an untracked device has no state). The K = 2 mechanics otherwise hold: a missed device keeps state and lastSeen, is snapshotted again next cycle (`:384–:396`), no per-device throttle in the sweep (`:751–:767`) — the second probe fires one 50-ms cycle later.
8. [REVIEW] T-1's `singleElement()` on the ping line (`ZT:373`) becomes two lines under its K = 2 re-script — row 11 should say that pin moves to `hasSize(2)`.
9. [INFO] `mainsContractFor` should call the existing public `deviceProfile(ieee)` (`:616–:627`) rather than copy `:621–:626`; `record.endpoints()` may be null (`:836` null-checks) → empty; `profile` is nullable (`:205`) — say so on the new signature.
10. [INFO] §9's "-Werror: an unused Probe component or an unused import fails the build" is not javac: `build-logic/…/homesynapse.java-conventions.gradle.kts:29` is `-Xlint:all -Werror` only (no Checkstyle/ErrorProne); javac has no unused category. Live traps: `lossy-conversions`, `this-escape`; none here.
11. [INFO] §6's bench grep expects 0; it is 1 — `nexsys-bench/scenarios/rejoin-race-operator.yaml:28`, a comment, not a consumer. Row 9: cite `PRODUCTION_CYCLE_MILLIS = 50` in §4.5 instead of measuring.
12. [INFO] Contracts: DP-1 (seed path `:224–:235` untouched, counter per process), M-1, LTD-11 (contract lookup in phase 2 outside the lock, as `expectedSilenceFor`), the FROZEN `availability_changed` (`:513–:514`) and `availability_link` (`:1918–:1921`, carries `available=` as §4.3 says) — no contradiction. Ctor callers: exactly `Z/…Adapter.java:459` and `ZT/…TrackerTest.java:94`.

## §3 Not checked
Row 19 and the S31 Lite's real clusters (not in the repo); `./gradlew check` not run; the Pi log; whether `FormattingStore` survives a restart (F5's gating option); the profile-registry cost per cycle.

REVIEWED /root/mnt/ClaudeFolder/_scratch/v100/b2/avail_shape_review.md 8942
