<!--
file: context/audits/2026-09-27_IR61b_independent-review.md
purpose: The independent review of the IR-61b coding instruction (D-v82-10's one-way-door read — the WU edits the composition root's boot order), run in-conversation at v84 beat 3 by an agent that had not seen the authoring, against flat copies of the 19 cited source files at core `1f1d1e0` and Doc 03 §3.8/§9. Verdict DISPATCH WITH EDITS, E1–E10; the hub re-verified E1 (`StateProjection.onCaughtUp()` :588 logs the catch-up) and E8 (`TransitionCoordinator.java` :142 `setMode(LIVE)` precedes :156 `onCaughtUp()`) at the instrument and applied all ten to the instruction the same beat (the new `state.projection_live` line DROPPED — the observable already exists; T2/T3b re-cut around the post-adoption ULID and `restart`; T4 via `configurationService().reload()`; the :647/:621/:1428 line fixes; `EntityId.parse`; the :671–:676 comment; §9.9–9.10). D-v83-25's premise "the state projection logs none" corrected in the v84 DR (D-v84-14).
audience: the hub · the Coder lane (read §2–§5 before IR-61b) · Nick
state-type: review (filed once; never edited)
status: FILED — v84 beat 3 (Sun 2026-09-27 evening); the instruction re-cut on it the same beat
-->

# IR-61b — independent review of the coding instruction (review-src @ 1f1d1e0)

## §0 Verdict
**DISPATCH WITH EDITS**
- E1 §1.4/header: "the state projection's LIVE leaves no trace" is false — `StateProjection.onCaughtUp()` (:572–:591) already logs `"StateProjection {} caught up at position {}; projection.replay.duration_ms={} events_replayed={}"` (:588) under `com.homesynapse.state`; either drop the new line and pin T3 on that one, or keep `state.projection_live` and say it is a second observable of the same event (grep uniformity).
- E2 §1.3/§3 row 3/§4: the state subscribe is :647 (not :648); the IR-61 comment is :621–:625; the registry subscribe is :606–:610.
- E3 §7 T2: the plug's ULID is minted at `adoptGen4()` AFTER boot (80-bit random, Ulid.java :14) — it cannot sit in the pre-boot YAML; re-cut as boot → adoptGen4 → rewrite `tempDir/config/homesynapse.yaml` → `fixture.restart(NO_STOPWATCH)` → seed → assert T+300 s.
- E4 §7 T3b: no report exists before the first boot; the shape is boot → adopt → seed at T → restart → first read — and a checkpoint restore (EntityState carries `staleAfter`) may mask the race, so T3b is informational, not the pin.
- E5 §7 T4: neither the fixture nor `load()` exposes issues; `reload()` returns `ReloadResult` with warnings and `core.configurationService()` (:1607, package-private) is reachable from lifecycle tests — name that path (write `bogus`, `reload()`, WARNING at `state_store.staleness.bogus`); the config-module placement needs a config-test → state-store dependency (module path, NO_REVERSE_DEPENDENCIES).
- E6 §4: a bare `staleness:` / `staleness_overrides:` key arrives as `null`, not absent — treat as NONE / `Map.of()`; decide whether `P..D` is rejected as `parseIso8601` does (:392–:395), since §1.1 says "exactly as".
- E7 §9.3: `EntityId.parse(String)` (:56) is the direct form; `Ulid.parse` also throws on invalid characters (decodeChar :144).
- E8 §7 T3: the registry line is logged in `onCaughtUp` on the subscriber VT while the gate reads bus mode on the main thread (ProcessRestartIdentityIT :130–:131 awaits the line "rather than racing the callback"); the Coder must confirm onCaughtUp precedes the LIVE flip in the bus, or T3's index assertion is timing-dependent on an empty log.
- E9 §6 row 2: the only javadoc mention is :1428.
- E10 §3 row 3: the :671–:676 comment calls :677–:678 "the ONE sanctioned composition-root addition" — re-cut it with the second await.

## §1 Premise check (A, B)
| cited premise | source says | verdict |
|---|---|---|
| §6.1 `Map.of(), Optional.empty()` :627 | :627 | HOLDS |
| §6.2 :677,:678,:1397,:1432; javadoc :1391–:1428 | calls/defs hold; javadoc hit :1428 only | MISMATCH (minor) |
| §6.3 state subscribe :648 | :647 | MISMATCH |
| §6.4 `registerCoreSchema` :527 · §6.5 `automationSection` :703,:1503 · §6.6 `LOG` :188 | as cited | HOLDS |
| §6.7 config main → SchemaRegistry :44 only · §6.8 names free | true in the 5 config copies / all copies; tree not re-runnable | HOLDS (partial) |
| §6.9 `cursorPosition` :445 · §6.10 `parseIso8601` :383,:387,:390 | as cited (:390 is private static) | HOLDS |
| §6.11 RPS :40,:107; PRIT 5 hits; `state.projection_live` 0 | RPS :40,:107; PRIT :69,:136,:137,:163,:168; 0 by name — but StateProjection :588 (E1) | name HOLDS; premise MISMATCH |
| §6.12 `attachLineCapture` :549 · §6.13 `boot` :126, yaml :182 | as cited | HOLDS |
| §1.1 Doc 03 §9 :740–:757 · comment+ctor :622–:627 | block :745–:757 · :621–:627 | HOLDS (wide) · MISMATCH (minor) |
| §1.2 root AP:false :168; AutomationSchema :34–:37; register :528 | :168; :34,:37; :527–:528 | HOLDS |
| §1.3 registry :606–:612; state :648; awaits :677–:678 | :606–:610; :647; :677–:678 | MISMATCH (:648) |
| §1.4 RPS :107; PRIT :136; :1397; :445; :1432; "polls silently, no trace" | lines hold; "no trace" false (StateProjection :588) | MISMATCH (substance) |
| §2 read ranges (13 spans) and module-info claims | all hold; RCF's yaml write is :182, outside :118–:151 | HOLDS |
| §4 resolver `requireNonNegative` :148–:154; ctor :95–:121 | as cited | HOLDS |
| §9.3 `Ulid.parse` :88; `EntityId.of` :44; throws :86–:98 | :88; :44; throws :91,:97 and :144; `EntityId.parse` :56 exists | HOLDS (incomplete) |
| §9.4 `registryProjectionMode()` reads the bus only | :1450–:1459, `eventBus.subscribers()` | HOLDS |

## §2 The gate (C) and the log line (D)
C. At HEAD: registry subscribe :606–:610, `StateProjection.create` :628–:641, state subscribe :647, awaits :677–:678 — concurrent replays (WU-IR61 row 18 agrees). Inserting `awaitRegistryProjectionLive()` before :647 is safe: it needs only `eventBus` (Phase 2) and `RegistryProjectionSubscriber.SUBSCRIBER_ID`; nothing between :606 and :647 subscribes or depends on the state projection; the registry's LIVE is bus-driven (RPS :105–:111), no reference to the state projection; the :678 call returns on its first poll. Gate correctness is independent of the onCaughtUp/mode order; only T3's log order is (E8).
D. `registry.projection_live` exists (RPS :107, in `onCaughtUp`); PRIT awaits it by `startsWith` (:133–:137) and asserts exactly one (:161–:168). `state.projection_live` is absent by name, but StateProjection :588 already logs LIVE with position and a clock-derived duration (E1). `cursorPosition()` is public (:445; used at :667). `LOG` :188 is `com.homesynapse.lifecycle.HomeSynapseCore`, under the `com.homesynapse` parent the appender attaches to (BPC :549–:565). `polls*20L`: the loop var is `i` (:1399); at return in iteration i exactly i sleeps ran, so `i*20L` is a sound lower bound; the Coder must introduce the name.

## §3 The config path (E) and the grammar (F)
E. `automationSection` (:1502–:1506) casts `rawConfig.get(SCHEMA_SECTION)` under `@SuppressWarnings("unchecked")` — the twin needs the same or `-Werror` fails. Registration :527 precedes `load()` :531. The validator maps `additionalProperties` → WARNING, "the value is accepted as-is" (JSCV :38–:39, :126–:132); `ConfigModel` :109 `Map.copyOf`s the top level only (nested nulls survive). Whether `StandardConfigurationService`'s merge/default stages keep an unregistered section in `rawMap()` is NOT in the copies — §10's pushback covers it. Core fragments embed inline as `properties.<section>` (SSR :156–:159), dialect 2020-12 (SSR :60–:61; JSCV :63); the automation fragment omits `additionalProperties`, so "state_store keeps true" is implementable by omission. A wrongly-typed value (integer) is ERROR → replaced by the schema default at load (Doc 06 §3.6) and never reaches `fromStateStoreSection`; §1.1's "never runs with a silent default" holds only for strings the schema passes (`"10m"`).
F. `parseIso8601` :390–:399 wraps `Duration.parse` and rejects `P..D`; the only duration in `homesynapse.yaml` visible is the automation `for_duration` in ISO-8601 (PT1S floor, :377); `heroMotionConfigYaml()` (BPC :635–:653) carries none. ISO-8601 is the codebase's grammar; Doc 03 §9's `"10m"`/`"1h"`/`"5m"` (:749, :757) are the outliers.

## §4 The tests (G)
T2: `boot(Path, String)` takes the full YAML (:126); `withGen4AcceptListed` appends `integrations:` (:144–:149), so a `state_store:` block goes at column 0 before or after. The `EntityId` comes from `adoptGen4()` AFTER boot (StalenessIT :77; RCF :258–:274) (E3); `restart()` (:347–:352) re-runs `startCore` on the same configDir; `tempDir()` (:171) gives the path.
T3: buildable (attach before boot; assert on `getFormattedMessage`), with E8.
T3b: reads `getSnapshot().states().get(plug)` (StalenessIT :133) — meaningful only after a restart with a prior report (E4).
T4: `load()` returns a `ConfigModel` with no issues (:65); `ReloadResult` carries "any warning-level issues" (:77–:78) and `core.configurationService()` :1607 is reachable from `com.homesynapse.lifecycle` tests (E5).

## §5 Missed risks (H)
- StateProjection already logs LIVE (:588) — §1.4 adds for the state the duplicate observable it refuses for the registry (E1).
- Unchecked/rawtypes lint on `Map<?,?>` walks in `fromStateStoreSection` under `-Xlint:all -Werror`.
- "zero → must be positive" is stricter than the resolver's `requireNonNegative` (:148–:154) — fine, but a stated choice.
- `scan_interval_seconds` (§9 :751) vs `staleness_scan_interval_seconds` (§3.8 :418) — a doc inconsistency for the docs card.

## §6 Not verifiable from the copies
`StandardConfigurationService` (rawMap retention of unknown sections; null merging; where load-time WARNINGs go; `ReloadResult`'s accessor); the bus's onCaughtUp-vs-LIVE order; `UlidFactory` determinism; both MODULE_CONTEXT.md files (:15, :122, the count); build.gradle test deps and the ArchUnit rules' scope over test classes; the repo-wide `git grep` rows (§6.7, .8, .10, .11 in part); the exit-code mapping for an IAE thrown after `load()`.
