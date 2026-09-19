<!--
file: context/audits/2026-09-18_v76-b6_close_ENERGY-READ-green_bench-charter_audit.md
purpose: THE v76 BEAT-6 AUDIT AND CLOSE — the ENERGY-READ landing read at the instrument (CI #253 and install-smoke #61 on `d1c2cbc`, step by step, from the GitHub API on the device VM; the counter's eighth sample); WUCP Phase 2 for ENERGY-READ; Nick's re-cut of the Java slot adjudicated (the plan §17 — MEASURE-2b as a read-path measurement with the shared boot fixture; LINK-READ as the second session; the rig-blindness sweep; the retention fact); BENCH-METER-1 chartered through the gate (its premise rows at bench `f3631cb`); the close on context health with Sunday's intakes handed to v77.
audience: the hub (the record; v77's boot) · Nick (§0; the packet)
state-type: verdict record + charter audit + close
status: FILED v76 beat 6 (Fri 2026-09-18 ~16:2x CT; instrument 2026-09-18T21:11:56Z at the beat's open)
-->

# v76 beat 6 — ENERGY-READ green at the instrument; Nick's re-cut; the bench charter; the close

## §0 Card
- **`CORE: ER d1c2cbc` and `HIVE: LANDED cfecdd2` verified:** core `d1c2cbc` = 22 at diff-tree (16 M + 6 A), porcelain 0, push 0; hivemind `cfecdd2` = 13, porcelain 0, push 0.
- **`CI: d1c2cbc green` verified at the instrument (the API from the device VM, 21:11Z):** CI #253 (id 35394284061) success — `Run check` ✓ · `Upload test reports` ✓ (`test-reports-253` 1,960,635 B) · `Run the bus soak` ✓ · `Upload bus-soak reports` ✓ (`bus-soak-253` 30,087 B); install-smoke #61 (id 35394283966) both arches ✓ through `Update-smoke` and the uploads. **The closure counter: 8/20** (`d1c2cbc`, the bus-soak step's conclusion; the XML stored, unread — as the seventh). **THE ADOPTION FENCE LIFTS** — no metering plug joins any network before Thu 09-24's CHAR session, by the calendar, not the fence.
- **WUCP Phase 2 (ENERGY-READ):** `MODULE_CONTEXT.md` updated by the lane (the ENERGY-READ section, read at b5); the deferred gate RESOLVED (coder-handoff, this beat); the register rows IR-15/24/25/28 LANDED at `d1c2cbc`; Open Risks: OR-METERING-VOLUME's status (b5) stands; the two fences re-read — the IAS fence lifts with IR-15 landed, the metering fence with CI green; Check 9 unchanged (no skill file touched this window since b1's 28/28; the skills HEAD `180375f`).
- **Nick's re-cut, ruled (the plan §17):** the rate leg closed — agreed; storage-as-disk-fill retired — agreed, with the arithmetic (a few hundred MB at most; under 10k metering events with the scaled thresholds); **the read path at run-scale row counts is the real exposure — agreed and adopted**: MEASURE-2b re-scoped as a read-path measurement on a real SQLite store with the boot shape extracted into one shared fixture; LINK-READ AFTER it as a second session (the hub's one edit: a charter through the gate is authored against a fixture at HEAD, not one the same lane is building; the cost is a paste); ENERGY-READ-b rides MEASURE-2b; the rig-blindness sweep as a § of that charter. **The hub's addition:** `RetentionPolicy.SOURCE_DEFAULT = (7, 90, 365)` days (`core/persistence/.../RetentionPolicy.java:46–:47`) — DIAGNOSTIC-class events purge after seven days; VERIFY-72H exports at the run's end; the pilot's NORMAL-class material holds 90 days.
- **BENCH-METER-1 DISPATCH-READY** (`context/instructions/2026-09-18_bench-lane_BENCH-METER-1_metering-known-load_field-within_link-quality-skeleton_charter.md`, 14,425 B; six rows): the record's method encoded (CHAR, the two chains, T1, the guaranteed band, k = 2, the shared-OEM tell); the two additive engine mechanics pre-ruled through the format's STOP gate; the skeleton behind a false flag; dry-run and selftests only.
- **v76 CLOSES at beat 6 on context health.** The deliverable's second half exceeded (ENERGY-READ landed green); the first half (Sunday's two intakes) handed to v77 by name in §HELD and the dispatch text. The navigator's Saturday 09:50 schedule stands; the hub asks nothing on Saturday.
- **The ONE act:** the packet — block 1 the BENCH-METER-1 dispatch paste (a fresh Cowork conversation); block 2 the b6 hivemind card → `HIVE: LANDED <sha>`; block 3 on SUNDAY, after `R5B-2:` — the v77 dispatch paste (`context/handoff/2026-09-18_v77_dispatch-text.md`).

## §1 BENCH-METER-1's premise rows at bench `f3631cb` (the greps as run)
| Claim | Command | Result |
|---|---|---|
| the api assert kinds carry no `field_within` | `sed -n '48p' tools/runner/engine.py` | `{…, "phase_terminal", "field_equals"}` |
| `within:` is a duration, not a tolerance | `sed -n '194,197p' engine.py` | `parse_within`: `'<N>s'` by `WITHIN_RE` |
| the positive-line key sets; the operator act keys | `sed -n '265,269p;350,360p' engine.py` | `{api, within}` / `{log, log_any, same_line, count, extract, min, within}`; `{act, goal, note, confirm, after}` |
| `field_equals` bound to a dotted field | `sed -n '1092,1101p' engine.py` | as cited |
| §5 of the format is additive and STOP-gated; `let:` binds from `api:` and `other_of:` only | `sed -n '93,110p' scenarios/SCENARIO_FORMAT.md` | as cited; no operator-entered binding |
| the capability flags live in constants; a flip is a re-mint | `grep -n '^capabilities:' scenarios/constants.yaml` | `:144` |
| the api read idiom for a state field | `sed -n '87,93p' scenarios/command-confirm.yaml` | `field_equals: {field: "data.attributes.brightness_percent.value", …}` |
| the operator act precedent | `grep -n 'operator:' scenarios/rejoin-race-operator.yaml` | `:88` |
| the runner's listing and dry-run forms | `sed -n '247p;360,375p' tools/runner/runner.py`; `grep -n __main__ tools/runner/test_engine.py` | `suite … --list` (`all` lexical, lawful for a listing); `scenario <name> --against LOGFILE`; the selftests carry a `__main__` (`:585`) |
| the desk gate | `grep -n selftest tools/runner/README.md` | `:247` `python3 -B tools/runner/nightly_digest.py --selftest` |
Not re-executed: the `power_w` wire key on the read surface (a PIN PENDING until Thursday's first read — the charter says so; format law #20).

## §2 The window, measured
Six beats · two lanes accepted in-window (the b2 brief's attack; EXT-REVIEW-1's adjudication) and one coder lane chartered, dispatched, returned, accepted and LANDED GREEN (ENERGY-READ, 22 files; a HEAD wire defect found on the way) · one bench lane chartered · hivemind `5bbbd14` · `c0158a1` · `7605dfc` · `6384e64` · `cfecdd2` + this card · the plan §14–§17 · the v76 DR (D-v76-1..10) · THE MEASUREMENT RECORD minted and first filled · IR-28..IR-32 · the spine rotated once · the counter 7 → 8 · `PROTECT: done` · the letters filed. **Hub errors owned:** the b1 ctx line's estimate; the b4 charter's five misses (the b5 audit §4); "Wed 09-24" (b2). **Not done in-window, handed:** Sunday's intakes; MEASURE-2b's charter; VERDICT-VOCAB-1; rehearsal 1's packet; `FOP: apply`; AMD-100's card; the strategy pass.

## §3 The definition of done (the skill §7)
- [x] Every return on disk at its path, audited two-layer, the audit filed (b2, b3, b5).
- [x] The core msg file + card handed; the CI verdict BANKED (`d1c2cbc` green at the instrument, this beat).
- [x] MODULE_CONTEXT updated (the lane); the deferred gate logged and RESOLVED.
- [x] The spine beats within caps; rotated once (bytes asserted); the digests rewritten.
- [x] Every hivemind commit census-exact by Nick's cards; porcelain clean after each.
- [x] Check 9: 28/28 at b1; no skill file touched since.
- [x] The next WU named: MEASURE-2b (through the gate, v77 b1 after Sunday's intakes), then LINK-READ.
