<!--
file: context/audits/2026-10-13_v110-b4_unit-card-A2_stub-ssh-dry-run.md
purpose: The hub's own stub-ssh dry-run of the unit cards' §A.2 (the BENCH-BOOT-1 operator card, re-cut on IR-185/186/187) against the landed tree `a17a7754…` (= bench `6a40a10`), run Mon 2026-10-12 ≈ 21:00 CT on the device shell; the record that makes §A.2 LIVE (law 15; the quoting-layer law of 2026-10-11).
audience: the hub (v111: the sitting's guide session is cut from §A.2) · Nick
state-type: dry-run record
status: FILED v110 beat 4 (Tue 2026-10-13 ~19:4x CT)
-->
# Unit card §A.2 — the stub-ssh dry-run (five blocks)

**The harness** (`/tmp/uc`, ephemeral): a stub `ssh` that echoes the received string and runs the stdin script under `bash -s` (the transport the card crosses); a stub `systemctl` keyed on a state file (`is-enabled` reads the wants link; `enable` makes it; `start` posts a request a stand-in user-manager loop answers by running `bench.sh run`; `stop`/`disable --now`/`reset-failed`/`show`/`show-environment` modelled); stub `loginctl`, `pgrep`/`pkill` (a state file), `curl`, `git`; the app a stub printing `zigbee.network_up` and holding until stopped. `HOME` a temp tree holding `git archive a17a7754…` as `nexsys-bench`. No real systemd ran — the model is the stub's (the same limit BENCH-BOOT-1's return §6 states).

**Quoting layers per block:** ssh (one quoted arg `bash -s`) · the quoted heredoc `<<'EOF_Bn'` (no local expansion) · remote bash. No block's inner quote class equals its wrapper's (the heredoc delimiter is quoted; the bodies use double quotes and `$(...)` only).

| Block | Read | The stub's call log |
|---|---|---|
| 1 the state | `6a40a10 …` · `tools/systemd/bench-boot.service` · `Failed to get unit file state for bench-boot.service` · `4242 java com.homesynapse.app.Main` · the current log · `unit-PATH: PATH=/usr/local/sbin:… · java: /usr/lib/jvm/…/bin/java` | `is-enabled` · `show-environment` |
| 2 the legacy stop, then install/enable/linger | `[OK] stopped` · `Created symlink …/default.target.wants/bench-boot.service → …` · `enabled` · `Linger=yes` | **`pkill -f [c]om.homesynapse.app.Main` ONCE, before `enable`** (IR-185) · `daemon-reload` · `enable` · `is-enabled` |
| 3 the delegated start | `[OK] started bench-boot -> …/bench-<stamp>.log` · `[OK] RADIO UP after 1s` · the health tokens · `ActiveState=active` · `NRestarts=0` · `Result=success` · the NEW log's path | `show -p ActiveState --value` · `start` · `show …` — **no `nohup`, no `pkill`** |
| 4 the delegation proof (`bench.sh restart`) | `[OK] stopped (bench-boot)` · `[OK] started bench-boot -> …` (a NEW log) · `RADIO UP` · `ActiveState=active` · `[OK] running (pid 4242)` · `[--] unit bench-boot (enabled): ActiveState=active SubState=running Result=success NRestarts=0` | `stop` · `show -p ActiveState --value` · `start` · `show …` ×2 |
| 5 the restore | `Removed "…/default.target.wants/bench-boot.service".` · the legacy start's health tokens (`zigbee.network_up`) · the link gone | `disable --now` · `reset-failed` (IR-186) · then the nohup path |

**Hazards found and carried:** the harness's own `$(systemctl start)` hung when the stub backgrounded the app from inside the command substitution (the pipe stayed open) — the stand-in manager loop was the fix; a real user manager returns at once. BLOCK 3's `start-limit-hit` branch (IR-186) and the `203/EXEC` branch (IR-187) are the card's EXPECT text, not exercised by the stub. The prior-ledger gate: BENCH-BOOT-1's return §3 D1–D4 and §4 F1–F5 grepped for every reused string — F1 (the stop order), F2 (`reset-failed`), F4 (the PATH read) are the re-cut; D4's guard lines are the EXPECTs of BLOCK 3.
