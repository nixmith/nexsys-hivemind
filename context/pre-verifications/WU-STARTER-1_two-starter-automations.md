<!--
file: context/pre-verifications/WU-STARTER-1_two-starter-automations.md
purpose: STARTER-1's pre-verification at core `49455fc` (J10 pulled left by the v98 strategy note: "two starter automations shipped as CONFIG + a Getting Started page, product-visible, no NCP risk"). The hub's greps against the automation engine's config path and the trigger types the two starters need. Finding: the engine IS wired and reads `automations.yaml` under the `automation` section, but BOTH starters as named (presence → lamp when dark; a plug schedule) need Tier-2 triggers whose records are EMPTY (`SunTrigger()`, `TimeTrigger()`, `PresenceTrigger()` — "schema defined, implementation deferred; requires scheduler integration"). STARTER-1 is therefore not config-only as written; the config-only shape uses the Tier-1 triggers the evaluator implements. Decision to Nick (H10 at the v99 close).
audience: the hub (authors STARTER-1 or re-shapes it) · Nick (the H10 row) · the Coder lane that implements TimeTrigger if that is the ruling
state-type: pre-verification (read-only; one cut)
status: FILED v99 beat 3 (Wed 2026-10-07 ~21:1x CT; instrument 2026-10-08T02:11:44Z) at core `49455fc`.
-->

# WU-STARTER-1 — pre-verification (the two starter automations) at `49455fc`

## §1 The premise as written (THE HORIZON :34, J10; the v98 strategy note)
"STARTER-1 — two starter automations shipped as CONFIG (presence → lamp when dark; a plug schedule), documented in Getting Started, exercised at pilot zero — R7." Pulled left from Nov 3–9 by the v98 note as product-visible work with no NCP risk.

## §2 What exists at the bytes (every row an instrument)
| # | Claim | At `49455fc` | Instrument |
|---|---|---|---|
| 1 | The automation engine is wired in the composition root | **YES.** `HomeSynapseCore.java:714` `new AutomationDefinitionLoader(…)`; `:539` registers `AutomationSchema.SCHEMA_SECTION` / `SCHEMA_JSON`; `:720–:733` the loader reads `automations` / `schema_version` UNDER the `automation` config section (the loader's ratified contract: a malformed document is a config error); `:712` `FileAutomationIdentityCompanion(configDir.resolve("automa…"))`; `:1098` the M7.5b read endpoints `GET /api/v1/automations…`. | `git grep -n 'AutomationDefinitionLoader\|AutomationSchema' 49455fc -- lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java` |
| 2 | The document format | `AutomationDefinitionLoader.load(Map<String,Object> document)` parses an `automations.yaml` root map (`:28`, `:84–:87`; 561 lines). | `git show 49455fc:core/automation/src/main/java/com/homesynapse/automation/AutomationDefinitionLoader.java` |
| 3 | The trigger types the evaluator IMPLEMENTS | `StandardTriggerEvaluator.java:504–:510`: `StateTrigger` · `StateChangeTrigger` · `NumericThresholdTrigger` · `AvailabilityTrigger` · `ReachabilityTrigger` · `EventTrigger` · `ManualTrigger`. | `git grep -n 'case .*Trigger' 49455fc -- core/automation/src/main/java/com/homesynapse/automation/StandardTriggerEvaluator.java` |
| 4 | The trigger types the two starters NAME | **`PresenceTrigger()`, `SunTrigger()`, `TimeTrigger()` are EMPTY records: "Tier 2 — schema defined, implementation deferred. Requires scheduler integration (Doc 05 §3.8 SchedulerService)."** (`TimeTrigger.java:6–:13`; the same sentence in `SunTrigger.java` and `PresenceTrigger.java`.) `CalendarTrigger` and `WebhookTrigger` likewise Tier 2. | `git show 49455fc:core/automation/src/main/java/com/homesynapse/automation/TimeTrigger.java` (+ Sun, Presence) |
| 5 | The real shapes available | `StateChangeTrigger(Selector selector, String attribute, String from, String to, …)` (`:36–:40`); `CommandAction(Selector target, String commandName, Map<String,Object> parameters, UnavailablePolicy onUnavailable)` (`:36–:40`); `TimeCondition`, `StateCondition`, `DelayAction`, `DurationTimer` carry no "Tier 2" sentence (their tier is read at the authoring — `StandardConditionEvaluator`). | `git show 49455fc:core/automation/src/main/java/com/homesynapse/automation/{StateChangeTrigger,CommandAction}.java` |
| 6 | The fleet's devices that could carry a starter | the SNZB-06P24 motion sensor (occupancy; 9-on-the-air since Sunday), the Hue (IR-112 — reporting dead; a CommandAction target that cannot confirm), G4-1/G4-2 (Shelly plugs; `on_off`), the S31 (hands-off). | the register; the v98 brief |

## §3 The finding
STARTER-1 as named is **not a CONFIG unit**: "presence → lamp when dark" needs `PresenceTrigger` (or a presence-derived state) AND a dark condition (`SunTrigger`/sun-aware `TimeCondition`); "a plug schedule" needs `TimeTrigger`. All three are deferred Tier-2 records with no fields and no evaluator case; implementing `TimeTrigger` alone needs the `SchedulerService` seam (Doc 05 §3.8) — a Java unit in `core/automation` + `lifecycle` (the composition root → the one-way-door review). Shipping them as config at pilot zero means that Java lands first (R6–R7's window, Nov 3–9 as THE HORIZON dates J10 — the pull-left buys nothing if the triggers are not there).

The **config-only shape that IS possible today** (Tier-1 triggers; no Java): (a) **motion → lamp**: `StateChangeTrigger` on the motion sensor's occupancy attribute (`to: occupied`) → `CommandAction` `on` to a lamp or plug; the "when dark" clause becomes a `TimeCondition` window (e.g. 18:00–07:00) IF `TimeCondition` is implemented (row 5's open read) — else the starter is "motion → light", honestly described; (b) **the plug schedule** has no Tier-1 form; the nearest product-visible starter without a schedule is **"nobody moving for N minutes → plug off"** (`StateChangeTrigger` `to: unoccupied` + a `DelayAction`/`DurationTimer` hold, if the `for:` form exists — row 5's read) — or an `AvailabilityTrigger` starter ("a device goes dark → tell me", J1's own feature, product-visible and confirmable).

## §4 Decision to Nick (H10 — at the v99 close)
```
ESCALATION TO NICK
Task: STARTER-1 (J10) — two starter automations as config
Question: re-shape the two starters to the triggers the engine implements today, or implement TimeTrigger (+ SchedulerService) first and keep the named pair?
Options: (a) RE-SHAPE — "motion → light" + "device goes dark → notify" as config + Getting Started (no Java; a desk hour + the FE lane's page; exercised at pilot zero on the real sensor and J1's availability line) · (b) IMPLEMENT FIRST — TimeTrigger/SunTrigger via SchedulerService (a J-class unit, the composition root touched → one-way-door review; ≈ a desk day; then the named pair as config) · (c) AS-DATED — J10 stays Nov 3–9; the pull-left retired
PM recommendation: (a) now, (b) as J3-class work after the freeze — the starters' purpose is a household's first "it did something" and J1's "it told me something went dark" is the product's own differentiator; a schedule is table stakes the engine does not have yet and should not be faked by config.
Refutable-by: TimeCondition/DurationTimer read as Tier 2 too at the authoring (then (a) shrinks to "motion → light" alone and (b) gains weight); or Nick's word that a schedule is the pilot's first ask.
Blocking: no — STARTER-1's authoring waits on the word; nothing else does.
```
