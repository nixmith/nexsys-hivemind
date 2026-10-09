<!--
file: context/audits/2026-10-08_AVAIL-SHAPE_intake_two-layer-audit_v100-b3.md
purpose: The hub's two-layer intake of AVAIL-SHAPE's return (`context/audits/2026-10-08_AVAIL-SHAPE_return.md`, 11,234 B; the lane: Claude Code on Nick's desk, Thu 2026-10-08 20:27 → 21:10 CT; the instruction `context/instructions/2026-10-09_coder-lane_AVAIL-SHAPE_IR-137_IR-138_probe-at-INFO_declared-silence_K2_LOCAL_desk-coding-instruction.md`): the claims read, the hub's own re-execution at the core repo, the five [REVIEW] rows ruled, the findings routed, the landing cards cut.
audience: the v100 hub (beat 3) · Nick (the landing) · v101 (the CI bank)
state-type: intake audit (terminal)
status: FILED — v100 beat 3 (Thu 2026-10-08 ~21:2x CT; instrument 2026-10-09T02:25:53Z); D-v100-13. Verdict: ACCEPT (DELIVERED).
-->

# AVAIL-SHAPE — intake audit (two layers)

## §1 Layer 1 — the return's claims, read critically
The card: DELIVERED; the branch `avail-shape/ir-137-138` over `main` `49455fc` with 0 commits; 8 M all staged; tree `a12087ceef5bab892aa54aa0562add6d085f5c51`; +937/−81; `./gradlew check` with the three gate tasks re-executed, BUILD SUCCESSFUL, 0 warnings; XML zigbee 85/747/0/0/1 · lifecycle 27/104/0/0/0 · app 7/30/0/0/0. The reds observed in two stages (15 compile errors on the three missing seams; 18 behaviour failures with the seams inert) then green. Every §0b row re-run and HELD; §4.5 measured (the floor class 71 s on the fixtures; the ActivePower class 0 unicasts at 660 s, 1 at 661, dark at 671). §1's spans name the staged tree's lines; §2 names every test with its red text; §3 five [REVIEW] + eleven [INFO]; §4 the survey as re-run equals the hub's counts; §5 five findings; §6 the coder-handoff entry; §7 the instrument limits. The return is 11,234 B under its 11,264 B ceiling, CRLF like the core tree's files, 0 trailer hits, the last line in the ordered form. The lane wrote nothing in the hivemind but the return.

## §2 Layer 2 — the hub's re-execution at the core repo (23:xxZ–00:xxZ; the commands as run)
| # | check | command | printed |
|---|---|---|---|
| 1 | the branch, the parent, the commit count, the porcelain | `git --no-optional-locks branch --show-current`; `rev-parse --short HEAD`; `rev-list --count 49455fc..HEAD`; `status --porcelain` | `avail-shape/ir-137-138` · `49455fc` · `0` · 8 lines, all `M ` (staged), 0 unstaged |
| 2 | the staged diff's size | `git --no-optional-locks diff --cached --stat \| tail -1` | `8 files changed, 937 insertions(+), 81 deletions(-)` |
| 3 | the tree sha is the index | `git cat-file -t a12087ce…` = `tree`; `diff <(git diff --cached --stat) <(git diff-tree -r --stat 49455fc a12087ce…)` | IDENTICAL |
| 4 | the eight files | `git --no-optional-locks diff --cached --name-status` | the three production files, their three tests, the lifecycle IT, MODULE_CONTEXT — the instruction's Files table exactly |
| 5 | the frozen tokens untouched | `git diff --cached \| grep -c '^[-+].*"zigbee.availability_changed: \|^[-+].*"zigbee.availability_link: '` | `0` |
| 6 | the seams at the staged bytes | `git show :Z/StandardAvailabilityTracker.java \| grep -n …`; the adapter; the configurator | `PROBE_MISSES_TO_DARK = 2` :110 · `int probeMisses` :222 · the sixth ctor arg :228/:264 · `++state.probeMisses` :375 · the mains compare `mainsSilenceLimitFor` :485/:515 · the reset :598; `MAINS_CONTRACT_METERING_ONLY = true` :205 · `logDrainedProbes()` first in the sweep :777, defined :818, `log.info("zigbee.availability_ping: device={} nwk={} ep={} outcome={} rttMs={} seen_during_probe={}")` :825 · `probesAwaitingDrain` :870 · `mainsContractFor` :906 → `contractMaxIntervalFor` :912; the configurator's `contractMaxIntervalFor(List<EndpointDescriptor>, DeviceProfile, boolean meteringOnly)` :237 |
| 7 | the XML counts per module | the JUnit XML under each module's `build/test-results/test/`, summed by a script | zigbee 85 files / 747 / 0 / 0 / 1 (01:55:11Z) · lifecycle 27 / 104 / 0 / 0 / 0 (01:55:37Z) · app 7 / 30 / 0 / 0 / 0 (01:55:06Z) — the return's numbers to the digit |
| 8 | the test clock | `grep -c 'Clock.systemUTC\|Instant.now()\|System.nanoTime\|currentTimeMillis'` over the four staged test files (`git show :path`) | `0` |
| 9 | the return's bytes and trailers | `wc -c`; `grep -c 'Co-Authored\|Claude-Session'` | `11234` · `0` |

Not re-executed: `./gradlew check` itself (the XML stamps and the lane's log lines are the evidence; CI on the push is the gate of record); the rendered log line (the lane quoted it from W-1's XML); the fake channel's 5-s deadline arithmetic (71 s on the fixtures vs the 70.05-s silicon derivation — SOAK-NIGHT-2 measures the real one).

## §3 The [REVIEW] rows, ruled
- **D1 — DP-5(b)'s line pin moved one cycle: OK, the lane's call right.** The instruction's W-4 said DP-5(b) "stays green UNCHANGED"; §4.1's deferral moves EVERY ping line one cycle, DP-5(b)'s included — the hub's wording, not the lane's work, was wrong. Its limit assertions are byte-unchanged (re-read at `:644–:653` by the lane; the hub reads the diff: one assertion's cycle). The W-4 sentence is a hub authoring miss, carried to the lesson.
- **D2 — four one-timeout scenarios, not five: OK.** The "powerSource routing" scenario (`:947–:989`) answers its probe; the hub's premise row 12 over-counted (the reviewer listed it too). Unchanged, green under K = 2.
- **D3 — a non-edge ping success does not move `lastReason`: OK, pre-existing.** `transition` sets the reason only on a state change; U-4b pins AVAILABLE + the count reset + the unchanged reason. The instruction's U-4 wording ("`PING_SUCCESS`") assumed otherwise; the behaviour is J1's, untouched.
- **D4 / D5 — the walk's two named divergences (the formatting-read gate; a SLEEPY/NONE posture): OK**, as the instruction named them; carried on IR-139.
- The [INFO] rows D6–D16: read; none changes a verdict. D15 (the hivemind writes: the return only; the handoff entry in §6) is the J2 precedent — the hub splices it at this beat.

## §4 The findings, routed
- **F-1** (the ≤ 90-s word under K = 2 holds for N ≤ 2 simultaneously silent floor-class devices; the run's floor class is the S31 and the Hue) → the javadoc says it; a note on IR-138's row; nothing for the run.
- **F-2** (`seen_during_probe` on an `ok` line reads the reply itself) → SOAK-NIGHT-2's reading rule: the field is read on `timeout` lines only (the packet draft `_scratch/v100/b3/soak2_packet_DRAFT.md` carries it; v101 cuts the packet).
- **F-3** (lines owed at `close()` are not printed — a restart between a probe and the next sweep drops one line) → a note on IR-137's row (≈ 3 lines to flush; after SOAK-NIGHT-2 if the digest misses a line).
- **F-4** (71 s on the fixtures, 70.05 s derived) → SOAK-NIGHT-2's F-6 row measures the silicon number per class.
- **F-5** (no `reportingOverrides` in the bundle; no Shelly/TR3 profile → 660 s at the bytes) → confirms §4.2's number; IR-138's row.

## §5 The verdict and the landing
**ACCEPT (DELIVERED).** The instruction → EXECUTED. The landing in Nick's hands (THE COMMIT-BOUNDARY LAW): `_scratch/v100/b3/card_avail_commit.txt` — one commit from the lane's exact tree (`git commit-tree a12087ce… -p 49455fc -F …`, `update-ref`), the push, the PR by `gh pr create` with `_scratch/v100/b3/pr-body.txt`; the message `_scratch/v100/b3/2026-10-08_core_AVAIL-SHAPE_commit-msg.txt` (6,133 B; `Why:` · `What changed:` per file · the evidence · the census; 0 trailers) → `AVAIL-SHAPE: COMMITTED <sha> PR <n>`; then, on `CI: green` (his word — the hub reads no GitHub), `card_avail_land.txt` — the ff-merge onto `main` guarded by `main` = `49455fc` → `CORE: LANDED <sha>`; `CI: green` on `main` banks at v101's boot. BC9a (Fri night) pins that sha BY SHA. WUCP Phase 2 at v101's boot once landed: the coder-handoff entry (spliced here from the return §6), MODULE_CONTEXT (edited by the lane in the tree), the register rows (IR-137 · 138 · 139 → the landing sha), Check 9 unaffected (no skill tree touched).
