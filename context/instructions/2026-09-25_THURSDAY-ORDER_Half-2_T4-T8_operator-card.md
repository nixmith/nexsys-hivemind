<!--
file: context/instructions/2026-09-25_THURSDAY-ORDER_Half-2_T4-T8_operator-card.md
purpose: THE THURSDAY ORDER — Half 2 (T4 → T8) cut at the re-mint beat (v80 b3) from T3b's capture (`_scratch/thu0924/pi-capture-2/`; devices=9 entities=9): T4 the constants re-mint (already written to the desktop working tree by the hub's guarded splice — Nick commits and pushes), T5 the Pi's pull, T6 boot-health on the new counts + the drift cmp + the state read that pins the `power_w` wire path, T7 the CHAR scenario in tmux (the P4460 as reference A; B1 + B2; the three plugs; the 80 W lamp pair), T8 the capture home. Every value read, none predicted.
audience: Nick (T4 at the desk; T5–T8 at the rig) · the hub (the intake on T8's capture)
state-type: operator card (hardware session — exclusive; one card at a time)
status: PARTIAL — T4 · T5 · T6 EXECUTED Fri 2026-09-25 (`a45686f`; the pull; boot-health PASS 9/9; the wire pin CONFIRMED); T4b `df4a2d7` (the load at one 40 W lamp); T7 aborted at its first prompt; T7–T8 SUPERSEDED by v81's METER-2 (THE SIMPLER WAY) (v80 b4, 2026-09-26T03:40:57Z). Was: DISPATCH-READY v80 beat 3 (Fri 2026-09-25 ~21:1x CT).
-->

# THE THURSDAY ORDER — Half 2 (T4 → T8)

**Tonight or Saturday: T4 + T5 + T6 are ten minutes at the desk and make Saturday's 03:30 CT nightly read the new fleet (9/9) instead of going RED; T7 is the ≈ 45–60 min CHAR at the rig — tonight if you have it in you, else Saturday first thing (before anything else at the rig). Say one line after each card.**

## §1 Before T4
- Git Bash on the desktop, a NEW window; paste the variables once:
```
D=~/Desktop/Code/ClaudeFolder/_scratch/thu0924; S=~/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/instructions/2026-09-24_THURSDAY-ORDER_scripts; mkdir -p $D
```
- For T7 only: the P4460 out of its box; B1 and B2; both clamp lights, one 40 W bulb in each; a short power strip or 2-way splitter so both lamps hang off ONE plug (the 80 W pair); the CHAR sheet and the rep sheet (paper: the scenario tells you what to write at every prompt). The S31 untouched. The three plugs stay in.

## §2 T4 — the constants re-mint lands (Git Bash; one command; `nexsys-bench`)
The hub has already written `scenarios/constants.yaml` on your desktop (fleet 9/9 · remembered-ulids + 3 · metering.plug-entity minted · metering-plug: true). This card commits it and pushes.
```
cd ~/Desktop/Code/ClaudeFolder/nexsys-bench && git --no-optional-locks status --porcelain | wc -l && ls .git/*.lock 2>/dev/null; git add -- scenarios/constants.yaml && echo "staged: $(git diff --cached --name-status | wc -l) (expect 1)" && grep -c 'Co-Authored\|Claude-Session' ../_scratch/v80/2026-09-25_bench_T4-remint_commit-msg.txt; git commit -F ../_scratch/v80/2026-09-25_bench_T4-remint_commit-msg.txt && git push && git log -1 --oneline
```
Read: `1` · `staged: 1` · `0` · the new sha. **Say back:** `BENCH: LANDED <sha>`

## §3 T5 — the Pi's pull (Git Bash; one command)
```
ssh pi 'cd ~/nexsys-bench && git pull --ff-only 2>&1 | tail -2; git log -1 --oneline; md5sum scenarios/constants.yaml | cut -c1-12'
```
Read: the same sha as T4 · `d9eb0efd5f96` (the md5 of the file as the hub wrote it; a different md5 is not a stop — say it). **Say back:** `T5: <sha> · <md5>`

## §4 T6 — boot-health on the new counts, the drift cmp, the wire pin (Git Bash; one command; no restart — the T3b boot is the boot under test)
```
ssh pi '~/bench.sh suite boot-health 2>&1 | tail -6; cmp -s ~/hs-bench/config/homesynapse.yaml ~/hs-bench/quiesce-hold/homesynapse.live-basis.yaml && echo CMP-IDENTICAL || echo CMP-DIFFERS; echo "== state TR3:"; ~/bench.sh state 01M3DM74SGEY7RXVDYSM4PK2XA | head -c 700; echo' > $D/T6.txt 2>&1; cat $D/T6.txt
```
Read: boot-health's verdict line — PASS on `devices=9 entities=9` (its forbidden `device_proposed` absent at the T3b boot) · `CMP-IDENTICAL` · the TR3's state JSON. **Paste the whole T6 output to me** (it is short; no token is in it — `bench.sh state` prints the response only). The hub reads the JSON for the `power_w` path: the scenario's field is `data.attributes.power_w.value` (marked WIRE PIN PENDING); if the wire spells it differently, the hub edits the scenario before T7 and hands a one-line bench card. A boot-health FAIL: stop and say the verdict line.
**Say back:** `T6: boot-health <PASS|FAIL 9/9> · <CMP-…> · state pasted`

## §5 T7 — the CHAR scenario in tmux (at the rig; ≈ 45–60 min; the hub's `T6: pinned` word first)
1. Open the tmux session (Git Bash; this one stays attached):
```
ssh -t pi 'tmux new -s metering'
```
2. Inside tmux, window 0, start the scenario. It prompts you step by step (CHAR-BEFORE with the chain wall → A → B1 → B2 → LAMP and its three tares; then for each plug in turn — G4-1, TR3, G4-2 — the TARE, the OFFSET, two volts readings, three REPs; then CHAR-AFTER). Read each prompt whole, do what it says, write the numbers on the sheet, type what it asks, Enter.
```
~/nexsys-bench/tools/bench.sh scenario metering-known-load
```
3. The `power_w` watcher in a second tmux window: press **Ctrl-b then c** (a new window), then run the watcher for the plug under test; switch windows with **Ctrl-b n** / **Ctrl-b p**. Change the ULID when the scenario moves to the next plug (**Ctrl-c** stops a watch):
```
watch -n 2 '~/bench.sh state 01M3DPGF6Y4YXNXDHBW38ZEX2G | head -c 400'
```
(G4-1 `01M3DPGF6Y4YXNXDHBW38ZEX2G` · TR3 `01M3DM74SGEY7RXVDYSM4PK2XA` · G4-2 `01M3DPKN9WD9B88Q4SVDMSBJVS`.)
4. **Every REP begins with a LOAD STEP**: the lamp pair out of the plug for at least 15 s, then back in — the prompt's own alternative; no command, no dashboard toggle. Read A (the P4460) and the platform's `power_w` (the watcher) at the instant the prompt names; the meters' `no-load` and tares are CHAR-BEFORE's first prompt.
5. The scenario ends with its verdict line and writes a bundle under `~/hs-bench/bundles/metering-known-load-<stamp>/`. Leave tmux with **Ctrl-b d** (detach) — never close the window mid-scenario; re-attach with `ssh -t pi 'tmux attach -t metering'`.
**Say back:** `T7: <the verdict line as printed> · bundle <stamp>` — plus one clause for anything odd (a prompt you could not satisfy, a watcher that never changed, a plug that read 0 under load).

## §6 T8 — the capture home (Git Bash; one command)
```
ssh pi 'ls -d ~/hs-bench/bundles/metering-known-load-* | tail -1; B=$(ls -d ~/hs-bench/bundles/metering-known-load-* | tail -1); grep -rc Bearer "$B" | awk -F: "{s+=\$2} END {print \"Bearer in the bundle:\", s+0}"; tail -3 "$B/verdict.txt"' ; scp -rq "pi:$(ssh pi 'ls -d ~/hs-bench/bundles/metering-known-load-* | tail -1')" $D/bundle-T7; ls $D/bundle-T7 | wc -l
```
Read: the bundle's path · `Bearer in the bundle: 0` · the verdict's last lines · the file count. **Say back:** `T8: files <k> · Bearer 0` — then the hub intakes the CHAR at the bytes (the datum; THE MEASUREMENT RECORD rows CHAR-1..3 and REP-1) and the metering datum is banked.

## §7 What this card does not do
No S31 act; no device outside the three plugs; no `--allow-downgrades`; no token printed or captured (the Bearer count is 0 at T8); no scenario edit at the rig — a wire-pin mismatch at T6 is the hub's edit and a new one-line card.
