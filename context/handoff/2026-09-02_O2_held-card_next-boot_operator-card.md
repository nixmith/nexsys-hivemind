<!--
file: context/handoff/2026-09-02_O2_held-card_next-boot_operator-card.md
purpose: THE O-2 HELD CARD — the ~5-minute operator act owed since R-4 (record 2026-08-30 O-2: the shipped unit lands in systemd state `failed` after a clean `systemctl stop`; the packet expected `inactive`). Rides WHENEVER the held card next powers. Its two pastes are ALSO the measured premise for the OR-FAILCHAN §6-B fix (R-10 Row 6) — the charter authors on these values, never ahead of them (arc-discipline 1).
audience: Nick (the operator) · the hub (the intake, one line at the next beat)
state-type: operator card (playbook §8 contract)
status: DEFERRED TO R-4b (its packet's STEP 0) — v61 beat 8. **The 09-02 run (Nick, ~21:00 CT) executed on `hs-dev-1` = THE BENCH CARD (`ssh pi`), where `homesynapse.service` does not exist (the bench runs via `~/bench.sh`); every command failed harmlessly ("Unit … not loaded/not found"); the bench is untouched.** The hub's defect: this card said "the HELD card" without its ssh target. THE HELD CARD IS `nick@hs-fresh.local` (`ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local`, per the R-4 packet §2) and it is a SEPARATE SD CARD physically swapped into the same Pi — powering it means taking the bench card out (a bench-down act; the nightly fires ~03:32 CT). The §6-B premise (exit 143 on SIGTERM) is ALREADY MEASURED at R-3a §6-B and mechanism-explained at source (the JVM's default SIGTERM exit = 143; the unit has no `SuccessExitStatus=`), so the FAILCHAN charter no longer waits on this card; Block 2 becomes a CONFIRMATION at R-4b. Do not swap cards for this alone.
-->

# O-2 — the held card's next boot (~5 min)

**Goal.** Bank three facts from the held card: (1) the unit's state after the reboot + whether the adoption maps rehydrated from the log; (2) the exit status the unit reports after ONE clean stop; (3) that it comes back ready. **Done-when:** three ⏺ lines pasted back, either way.

**Anti-actions.** Do NOT `reset-failed` before the read (it erases the value we want). Do NOT touch the bench card. Do NOT upgrade, apt, or edit config. Every command is copy-paste; nothing here needs judgment.

## Block 1 — after power-on, wait ~90 s, then (all on the held card):
```bash
# WHERE: the HELD card ONLY — `ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local` (hostname hs-fresh). NOT `ssh pi` (= hs-dev-1, the bench card). Verify first: `/usr/bin/hostname` must print hs-fresh.
/usr/bin/date -u
/usr/bin/systemctl show -p ActiveState -p SubState -p Result -p ExecMainStatus -p NRestarts homesynapse.service
/usr/bin/journalctl -u homesynapse.service -b --no-pager | /usr/bin/grep -c adoption_maps_rehydrated
/usr/bin/journalctl -u homesynapse.service -b --no-pager | /usr/bin/grep -c 'network_resumed'
```
**Expected:** `ActiveState=active` · `SubState=running` · `Result=success` · `ExecMainStatus=0` · `NRestarts=0` · rehydrated count **≥ 1** · resumed count **≥ 1**. ⏺ RECORD all six values verbatim. (A rehydrated count of 0 with `active` = a FINDING — paste it, do not retry.)

## Block 2 — ONE clean stop, then read the exit (this is the O-2 value):
```bash
# WHERE: the HELD card (hs-fresh) — `/usr/bin/hostname` must print hs-fresh
/usr/bin/sudo /usr/bin/systemctl stop homesynapse.service
/usr/bin/sleep 5
/usr/bin/systemctl show -p ActiveState -p SubState -p Result -p ExecMainStatus -p ExecMainCode homesynapse.service
```
**Expected (the O-2 hypothesis, pre-filed):** `ActiveState=failed` · `Result=exit-code` · `ExecMainStatus=143` · `ExecMainCode=exited` — i.e. the JVM exits 143 on the caught SIGTERM and systemd grades a clean stop as a failure. **The alternative reading** `ActiveState=inactive` · `Result=success` · `ExecMainStatus=0` means O-2 was pre-existing state from an earlier run and §6-B is NOT the cause — equally valuable; paste it. ⏺ RECORD all five values verbatim.

## Block 3 — bring it back:
```bash
# WHERE: the HELD card (hs-fresh) — `/usr/bin/hostname` must print hs-fresh
/usr/bin/sudo /usr/bin/systemctl reset-failed homesynapse.service
/usr/bin/sudo /usr/bin/systemctl start homesynapse.service
/usr/bin/sleep 20
/usr/bin/systemctl show -p ActiveState -p SubState homesynapse.service
/usr/bin/journalctl -u homesynapse.service --no-pager -n 40 | /usr/bin/grep -c 'network_resumed'
```
**Expected:** `active` · `running` · resumed **≥ 1**. ⏺ RECORD both. If not `active` within ~60 s: paste `/usr/bin/journalctl -u homesynapse.service --no-pager -n 60` and STOP — do not loop.

**Paste back either way** (three ⏺ groups) into the chat; the hub files them at the next beat (one line in the spine; the FAILCHAN charter's premise slot fills from Block 2).
