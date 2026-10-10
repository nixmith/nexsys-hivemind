<!--
file: context/audits/2026-10-10_v104-b1_PKG-FRESH-1_restore-rulings_verbatim.md
purpose: The six rulings of PKG-FRESH-1's restore, filed VERBATIM in the order they were ruled: v103's post-close rulings (left for v104 to file) and v104 beat 1's five. Each text sits between `~~~~` fences under a heading that names its source path, bytes and md5; the bytes between the fences are the file's.
audience: the record · the v105 boot · Nick
state-type: rulings, verbatim
status: FILED v104 beat 1 (Sat 2026-10-10 ~12:1x CT; instrument 2026-10-10T17:18:49Z).
-->

# PKG-FRESH-1 — the restore's rulings, verbatim

## 1. The v103 post-close rulings (≈ 10:38 CT; v103 left them for v104 to file) — `_scratch/v103/b3/2026-10-10_v103_post-close_rulings_PKG-FRESH-1_STOP.md` · 4,234 B · md5 `e31a9907e8b532898398609bd30696be`
~~~~markdown
<!--
file: _scratch/v103/b3/2026-10-10_v103_post-close_rulings_PKG-FRESH-1_STOP.md
purpose: The v103 hub's rulings on PKG-FRESH-1's STOP at A3 (Nick, 10:33 CT), made after v103's close was spliced (D-v103-27) and before v104 booted. v104 files them in its DR (D-v104-n) beside the guide's return.
audience: the v104 hub (its beat 1) · Nick
state-type: post-close rulings (one page; not in the tree until v104 files it)
status: RULED Sat 2026-10-10 ~10:4x CT by the v103 hub.
-->

# PKG-FRESH-1 STOP at A3 — the hub's rulings (v103, post-close)

**The return:** `_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_guide-notes.md` (24,284 B) · `…_outputs.txt` (4,983 B).

**The finding, accepted:** the card in the Pi is the months-old second card, `hs-fresh`, not a fresh flash.
- Its host key is the Sep 4 `rzZU…` key (E1) and it runs Debian 13 (E2).
- Its records run R-4 … H8a, with HomeSynapse installed as the packaged service (E6).
- Thursday's "Part 0 DONE (debs=1; FLASHED hs-fresh-1)" was a template line with an unfilled `<HH:MM>` (E7).
- No login was made and nothing changed on that card. Fence 1 held.

1. **RESTORE NOW** — the restore before any gap. Any re-flash or imaging needs the second card in the desk's reader anyway, while the held card runs.
2. **The read-only identity probe FIRST** (the guide's §12), in one paste, in the PINNED form of ruling 3.
   - Its ssh options become `-o UserKnownHostsFile=~/.ssh/known_hosts.old -o StrictHostKeyChecking=yes -o BatchMode=yes`. That checks the `.80` key against the pre-removal file (the Sep 4 key), writes nothing, and never prompts.
   - It adds one read: `sudo -n du -sh /var/lib/homesynapse 2>/dev/null || echo "store: none or unreadable"`.
   - **If the probe's ssh fails, STOP and paste it to the hub.** No power is pulled on a guess.
3. **D1's ssh form: the card's D1 with the same pinned options** in place of the bare `ssh -i ~/.ssh/id_ed25519_pi nick@<IP>`, and `<IP>` = `192.168.1.80`.
   - The hands list is verbatim, with hand (3) corrected: the SECOND card OUT, labelled `SECOND · hs-fresh · NOT flashed · PKG-FRESH-1 STOP 2026-10-10 · keep intact`.
   - **D2 is verbatim.** A metering plug (G4-1 · G4-2 · TR3) in D2's `unavailable=[…]` is **P12′'s predicted long-gap pair** (the gap ≈ 1 h ≫ 660 s): RECORD it, not a STOP.
   - This D2 boot is the soak's LOG0.
4. **The second card: DO NOT flash it. Keep it intact.**
   - It is evidence (R-4 … H8a, packaged HomeSynapse, configs, perhaps a store).
   - It is also the natural **UPGRADE-1 card** (Nov 10): an old packaged install upgraded to a new `.deb` is exactly that row's path.
   - **The re-sit uses a THIRD blank card** (≥ 16 GB). If none is at hand, it waits for one, or for PI-2's card (Oct 20; then PKG-FRESH-2 is the first fresh install).
5. **The OS: the Raspberry Pi Imager's current default "Raspberry Pi OS Lite (64-bit)" on the flash day,** its codename recorded at A3. Trixie is expected; `hs-fresh` already runs Debian 13.
   - That is the household's path.
   - The card's bookworm lines (Part 0b, A3, the one line) are re-stamped by v104.
6. **Thursday: no card was flashed.** P7 records Part 0 as uncorroborated (the template line), a hub miss beside D-v103-28's two.
   - **The lesson (v104 files it):** a state line with an unfilled slot is a template, not a report; a re-stamp re-reads every DONE at an outputs file's bytes.
7. **The re-sit's timing:**
   - Not today (the soak at 21:00; today's hands act is spent).
   - **Rec: Wed Oct 14 evening**, after dry-run #1's harvest. The third card is flashed at the desk beforehand, as a Part 0b with a RECORDED output (the flash time, the hostname, the card's label).
   - The `49455fc` artifact is on the desk and verified (`.deb` `bc5185ed…4bfb34` = the run page = the desk; the zip = GitHub's digest), so GitHub's retention no longer gates it. Keep the zip.
   - **v104 re-stamps the card:**
     - a per-card `UserKnownHostsFile` for every fresh-card ssh/scp;
     - D1's pinned form;
     - Part 0b's recorded output;
     - A2's "plugging in boots the Pi";
     - A3/B's codename.
   - `CAPACITY:` can pull it to Sunday morning (09:00–11:00, between S2 and BC9) if you want two hands acts on Sunday.
~~~~

## 2. The v104 restore ruling (11:17 CT) — `_scratch/v104/b1/2026-10-10_v104_b1_RESTORE-ruling_PKG-FRESH-1_fence-1-breach.md` · 4,825 B · md5 `a22ac9438da0900fe4da66de2a2dbfc7`
~~~~markdown
<!--
file: _scratch/v104/b1/2026-10-10_v104_b1_RESTORE-ruling_PKG-FRESH-1_fence-1-breach.md
purpose: The v104 hub's ruling on the guide's proposed restore after PKG-FRESH-1's fence-1 breach (Nick's line, 11:07 CT). Filed before it is handed.
audience: the PKG-FRESH-1 guide (runs it) · Nick (the hands) · the v104 intake
state-type: ruling (one page)
status: RULED Sat 2026-10-10 11:17 CT (instrument 2026-10-10T16:17:03Z) by the v104 hub.
-->

# PKG-FRESH-1 fence-1 breach — the restore, ruled (v104)

**Read at the bytes before ruling:** the line (11:07 CT) · guide-notes §13 (40,146 B) · outputs.txt (10,390 B; D1 → D2-capture) · hs-fresh's boot journal (443 lines, 92,572 B) · the card's D2 block (:113–:124) · the v103 post-close rulings (4,234 B).

**The hub's own reads (layer 2), at the journal:** `network_formed` 0 · `network_resumed` 1 · ERROR-level lines 0 (WARN 380 · INFO 55) · no permit-join, leave, bind-request or reporting-configuration line (the one "bind" hit is `bindHost=127.0.0.1`) · the "probe" hits are the loopback health-probe and the migration runner, not radio reads · the four `rejoin_ignored_window_closed` lines are host-side (senders hs-fresh's registry does not know; no adoption). The breach changed hs-fresh's store, not the fleet's network. The restore needs no repair act.

**One premise was unmeasured:** no record puts the held card at 192.168.1.80. The .80 records are hs-fresh's (R-4b :226 · H8a :14 · R-5B :8), and the Aug 23 sitting left "the held card inherits .80" NOT TESTED (E-P3). The gate below therefore tries the tailnet before the LAN, under the same host-key pin.

## RULED: the guide's restore, ADOPTED with three edits

**R1 — hs-fresh off.** D1's pinned command exactly as it ran at 15:44:01Z, header `=== R1`. EXPECTED `poweroff-sent <Z>` · `desk-clock <Z>`. The ssh fails → STOP; no power is pulled on a guess.

**R2 — the hands, one act per message (the guide's list, with read-backs):** (1) the green LED dark ≈ 20 s; (2) power out; (3) the card in the Pi OUT, its label read aloud (expected `SECOND…`; anything else is RECORDED — R3 decides); (4) the card labelled `HELD` IN, its label read BEFORE it goes in — no card on the desk reads `HELD` → STOP before power-in; (5) power in, the dongle still OUT; (6) wait 90 s. Say back ONE line: `RESTORE-SWAP: <HH:MM:SS CT> out=<label> in=<label> dongle-out yes`.

**R3 — the identity gate (edit 1: one paste, the tailnet then the LAN):**
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== R3 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh -o StrictHostKeyChecking=yes -o BatchMode=yes -o ConnectTimeout=10 pi 'echo "via=tailnet $(hostname) $(uptime -p)"' || ssh -o HostName=192.168.1.80 -o HostKeyAlias=hs-dev-1 -o StrictHostKeyChecking=yes -o BatchMode=yes -o ConnectTimeout=10 pi 'echo "via=LAN $(hostname) $(uptime -p)"'; } 2>&1 | tee -a "$OUT"
```
EXPECTED: a line `via=tailnet hs-dev-1 up …` or `via=LAN hs-dev-1 up …`. Both forms check the key saved for `hs-dev-1` (known_hosts:9, the entry `ssh pi` passed at 14:38 and 14:39Z), write nothing and never prompt. Both TIMED OUT (no "Host key verification failed" line) → wait 60 s, run R3 once more under the header `=== R3b`. A "Host key verification failed" line, or a second failure → STOP; the dongle stays OUT.

**R4 — the dongle.** Only after R3 printed `hs-dev-1`: the dongle into the Rosonway port it came from; wait 15 s. Say back `R4: <HH:MM:SS CT> dongle-in yes`.

**D2 — verbatim (edit 2: the LAN fallback named).** EXPECTED as the card's, plus: uptime longer than "2–3 min" (RECORD — the new order); a metering plug (G4-1 · G4-2 · TR3) or the sensor in `unavailable=[…]` = P12′'s predicted pair → RECORD. If R3 passed only `via=LAN`, or D2's `ssh pi` times out: D2 once with R3's five LAN options inserted after `ssh`, recorded in §11. `formed ≠ 0` → POWER OFF and STOP (the standing law).

**After D2 (edit 3): one hands act.** Add `CORE ENABLED · NEVER WITH THE DONGLE` to the SECOND card's label; say back `label yes`. Then Part E (its 12:00 CT time holds; D2 comes before it).

## For the record
- This D2 boot is the soak's LOG0 (v103 ruling 3 stands).
- The gap: 09:44:56 CT (A2's `poweroff-sent`) → the `zigbee.network_resumed` line in D2's boot-log (the Pi's clock, EDT, converted where read). Inside it, hs-fresh held the fleet's NCP ≈ 10:46:45 → 10:55:16.5 CT (its journal; pi-clock = desk ± 1 s).
- P12′'s first read names both legs: 09:44:56 → ≈ 10:46:45, and 10:55:16.5 → D2.

## The standing fence (from M-4; filed in the v104 intake)
The dongle goes into the Pi only after an identity gate has printed `hs-dev-1` on the card that is in the Pi at that moment. Every card text that swaps cards carries it.
~~~~

## 3. Amendment 1 — R2 by name (11:33 CT) — `_scratch/v104/b1/2026-10-10_v104_b1_RESTORE-ruling_AMENDMENT-1_R2-by-name.md` · 1,774 B · md5 `68f61c22475e58e964f1d79d5e1835de`
~~~~markdown
<!--
file: _scratch/v104/b1/2026-10-10_v104_b1_RESTORE-ruling_AMENDMENT-1_R2-by-name.md
purpose: Amendment 1 to the v104 restore ruling (a22ac943…bfc7): R2 by NAME. The ruling's label rule stopped the restore because no card carries a written label; the root cause (Nick, 11:29 CT) is the word "HELD" — a role name in the card texts, the card-in-use in Nick's usage.
status: RULED 11:33 CT (instrument 2026-10-10T16:33:41Z) by the v104 hub.
-->
# The restore — AMENDMENT 1: R2 by name

**R2 (AMENDED; the label rule WITHDRAWN).** The Pi stays unpowered and empty; the dongle stays OUT. (1) Nick puts **hs-dev-1** into the Pi, the card he identifies as hs-dev-1; **hs-fresh** (SanDisk Ultra 128GB, 6271YUATL02Z) stays set apart. (2) Power in, the dongle still OUT. (3) Wait 90 s. Say back ONE line: `RESTORE-SWAP: <HH:MM:SS CT> hs-dev-1 in · dongle-out yes`.

**R3, R4 and D2: exactly as ruled.** R3 is the proof: it must print `hs-dev-1` before the dongle goes in; anything else, or two failures → the dongle stays OUT; STOP.

**Edit 3 WITHDRAWN.** The cards carry no written labels. hs-fresh's fence fact (its packaged Core starts on every boot) is carried by the record and by UPGRADE-1's card.

**The names, from now on, in every card text and every message:** `hs-dev-1` and `hs-fresh`, nothing else. "HELD", "the held card", "the second card" and "the fresh card" are retired as names for a card. The card texts used HELD as a role; Nick uses "held" for the card in use; the two senses named one card at A2 and two different cards at D1.

**The miss is the hub's:** the card texts minted a role word that collided with the operator's word, and the restore ruling then gated power-in on a physical label nobody had written, without reading whether one existed.
~~~~

## 4. The D2-FAIL read block (11:47 CT) — OVERTAKEN, never run: the guide's own capture answered it — `_scratch/v104/b1/2026-10-10_v104_b1_D2-FAIL_read-block.md` · 2,231 B · md5 `5272fa1ec2afccf4b23260cd5ea6c749`
~~~~markdown
<!--
file: _scratch/v104/b1/2026-10-10_v104_b1_D2-FAIL_read-block.md
purpose: The hub's read-only block after D2's boot-health FAIL (the card: "the hub reads the log"): the two newest bench logs and the boot-health bundle copied to the desk at the bytes; disk, memory and the process count printed. Nothing on the Pi changes.
status: RULED 11:47 CT (instrument 2026-10-10T16:47:50Z) by the v104 hub.
-->
# D2 FAIL — the read (read-only; one paste; Git Bash)

**Why:** D2 at 16:43Z on **hs-dev-1** (R3 proved it): the Core failed at startup twice — `lifecycle.startup_failed: phase=CORE_DOMAIN subsystem=state-store … exiting code=99` — once at `bench.sh restart` and once at boot-health's launch (`bench-2026-10-10-124506.log`); `formed=0 resumed=0 relinked=0`; the API down. Nothing formed; no Core holds the dongle. The fleet still has no Core.

**The block (read-only on the Pi; it writes three files beside the outputs file and appends its lines to it):**
```bash
D=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1; OUT=$D/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== D2-logs (read-only) $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'cd ~/hs-bench && echo "pi-clock $(date -u +%H:%M:%SZ) running=$(pgrep -fc homesynapse)" && ls -lt --time-style=+%H:%M:%S bench-2026-10-10-*.log | head -3 && df -h / | tail -1 && free -m | sed -n 2p'; for L in $(ssh pi 'cd ~/hs-bench && ls -t bench-2026-10-10-*.log | head -2'); do ssh pi "cat ~/hs-bench/$L" > "$D/2026-10-10_PKG-FRESH-1_D2_$L" && echo "copied $L $(wc -c < "$D/2026-10-10_PKG-FRESH-1_D2_$L") B"; done; ssh pi 'tar -C ~/hs-bench/bundles -czf - boot-health-20261010T164636Z' > "$D/2026-10-10_PKG-FRESH-1_D2_boot-health-bundle.tgz" && echo "bundle $(wc -c < "$D/2026-10-10_PKG-FRESH-1_D2_boot-health-bundle.tgz") B"; } 2>&1 | tee -a "$OUT"
```
**EXPECTED:** `pi-clock …` with `running=0` (pgrep counts its own shell, so 0 or 1) · three log names · the root filesystem line · the memory line · `copied bench-2026-10-10-<stamp>.log <bytes> B` ×2 · `bundle <bytes> B`. Any ssh failure → paste what printed. **Then STOP**: the hub reads the logs at the bytes and rules the fix. Nothing else runs; the dongle may stay in (no Core is running, and none starts by itself).
~~~~

## 5. The warm-up ruling, W1 then D2b (11:54 CT) — `_scratch/v104/b1/2026-10-10_v104_b1_D2-FAIL_ruling_warm-up_D2b.md` · 2,956 B · md5 `183040e4252b5e9ace99fa8c223ddc5c`
~~~~markdown
<!--
file: _scratch/v104/b1/2026-10-10_v104_b1_D2-FAIL_ruling_warm-up_D2b.md
purpose: The v104 hub's ruling on the guide's D2 STOP (11:46 CT): the bench Core's two cold launches overran the registry projection's ~30 s startup budget. The guide's warm-up ADOPTED with two edits. Supersedes the hub's D2-FAIL read block (5272fa1e…, not run: the guide's own capture answered it).
status: RULED 11:54 CT (instrument 2026-10-10T16:54:54Z) by the v104 hub.
-->
# D2 STOP — ruled: the warm-up, then D2b

**Read at the bytes:** `_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_hs-dev-1_startup-failure.txt` (9,824 B, md5 `95b407d9…254b`): both launches have persistence up in ≈ 2 s ("Loaded 10 entities from checkpoint for view state_projection at position 1654229"), then 44.8 s (12:43:09.158 → 12:43:53.987 EDT) and 38.3 s (12:45:08.086 → 12:45:46.384) in `awaitRegistryProjectionLive` → `IllegalStateException: registry projection did not reach LIVE within ~30s` → a clean teardown (the WAL checkpoint completed) → exit 99. Disk 16% used. The budget is `maxPolls = 1_500` × `Thread.sleep(20L)` (`HomeSynapseCore.java`, unchanged from `37f05a9` to `409547c`); the wall time exceeds 30 s because the sleeps overrun under the replay's I/O load. **Not corruption: a cold page cache under an 829 MB store on the SD card.** This morning's launches were warm.

**RULED: the guide's proposal ADOPTED, with two edits.**
1. **W1, the warm-up (read-only; edit 1: memory printed before and after, so the read is also the record's cold-read number):**
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== W1 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'free -m | sed -n 1,2p; time cat ~/hs-bench/data/homesynapse-events.db > /dev/null; free -m | sed -n 2p'; } 2>&1 | tee -a "$OUT"
```
EXPECTED: the memory header and line · `real …` (the time to read 828,829,696 B from the SD card; write it) · the memory line after, its buff/cache grown by ≈ 0.8 GB.
2. **D2b — D2's block verbatim under the header `=== D2b` (edit 2: a distinct header; D2 has four headers in the file already).** EXPECTED as D2's: RADIO UP · `formed=0 resumed=1` · `relinked ≥ 9` · `registry rows=10` · boot-health PASS 6/6 (or RECORD). A metering plug or the sensor in `unavailable=[…]` = P12′'s pair → RECORD. `formed ≠ 0` → POWER OFF and STOP.
3. **If D2b's launch fails again: STOP. No further launch;** the hub rules the next act.
4. **Part E** runs after D2b (its 12:00 CT time yields to D2b by minutes).
5. **This boot is the soak's LOG0** (v103 ruling 3 stands).

**For the record (the intake carries it):** a cold boot of a ≈ 1.65 M-event store on an SD card overruns a hard-coded 30-s registry budget and exits 99. A household Pi rebooting after a power cut would do the same. This is a J8-class product finding, and it bears directly on AMD-103 R-F (a whole-log pass at boot, measured on the Pi today).
~~~~

## 6. PE-1, P12′'s long-gap resume read (12:03 CT) — `_scratch/v104/b1/2026-10-10_v104_b1_PE-1_P12-long-gap-resume_read.md` · 1,572 B · md5 `a98a9f362ff366b95c41647340f7792d`
~~~~markdown
<!--
file: _scratch/v104/b1/2026-10-10_v104_b1_PE-1_P12-long-gap-resume_read.md
purpose: One read-only block in Part E's slot: P12′'s long-gap resume read from the log that holds it. D2b's restart resumed the fleet at 12:00:49 CT; boot-health relaunched the Core at 12:01:22 CT (bench-2026-10-10-130122.log = LOG0), seeded from the sidecar the restart's ≈ 30-s run wrote at its stop. The pairs P12′ predicts, if any, are in the restart's log.
status: RULED 12:03 CT (instrument 2026-10-10T17:03:23Z) by the v104 hub.
-->
# PE-1 — P12′'s long-gap resume, from the restart's log (read-only)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_outputs.txt; { echo "=== PE-1 (read-only; P12 long-gap resume) $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'cd ~/hs-bench; ls -t bench-2026-10-10-1[23]*.log | head -3; R=$(ls -t bench-2026-10-10-1[23]*.log | sed -n 2p); C=$(basename $(readlink -f current.log)); for L in $R $C; do echo "--- $L $(wc -c < $L) B"; grep -m 1 "zigbee.network_resumed" $L | cut -c1-160; grep -m 24 -E "zigbee\.availability_(ping|link)" $L | cut -c1-220; echo "last: $(tail -1 $L | cut -c1-140)"; done'; } 2>&1 | tee -a "$OUT"
```
**EXPECTED:** three log names, newest first (`…130122.log`, the restart's `…1300xx.log`, `…124506.log`); then for the restart's log and for LOG0: its `network_resumed` line · its first availability lines (`availability_ping` outcomes; `availability_link … available=false/true`) · its last line. RECORDED, never judged by the guide. Then Part E as written; then the one line.
~~~~
