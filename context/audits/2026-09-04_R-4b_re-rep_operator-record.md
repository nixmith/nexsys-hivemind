<!--
file: context/audits/2026-09-04_R-4b_re-rep_operator-record.md
purpose: THE R-4b OPERATOR RECORD — every ⏺ of the Fri 2026-09-04 held-card session, verbatim, in packet order (context/handoff/2026-09-04_R-4b_navigator-packet_held-card.md), filed by the R-4b navigator session as it lands; §0 rewritten into the verdict surface at the close; §9 the findings card for the hub; §10 the hub's audit verdict (the hub writes it at intake — the C-002 mint or the fallback's record).
audience: the navigator (writes §0–§9) · the hub (audits; writes §10) · Nick
state-type: operator record (evidence)
status: CLOSED-PENDING-HUB-AUDIT — filed by the R-4b navigator 2026-09-04T20:45Z. FOUR OF FOUR (C1 C2 C3 C4) + criterion 0 on BOTH arms. C4 path B, verdict word CONFIRMED. Zero STOPs; 13 deviations (D-1..D-13), all T1/T2, all filed. Bench floor restored GREEN ([PASS] boot-health 6/6 positive, 0 forbidden, PAN 0x774c unchanged). Artifact: ef02d13 (the FAILCHAN stop-proof is still owed; its CI is RED). The navigator commits nothing — the hub commits at intake and writes §10.
-->

# R-4b — operator record (Fri 2026-09-04, hs-fresh)

## §0 VERDICT SURFACE

### ★ FOUR OF FOUR — AND CRITERION 0 ON BOTH ARMS. ★
**Artifact `ef02d13` = `0.1.0+git20260903.124041.gef02d13` · sha256 `48a33b0dc614a7f74fd0e0a279480e3c2f1f8e1e952f3195f0ffdbad1c626003` · install-smoke run https://github.com/nexsys-io/homesynapse-core/actions/runs/33756606012**
**Navigator dispatched `2026-09-04T16:06:27Z` · record closed `2026-09-04T20:45Z` · card `hs-fresh` @ 192.168.1.80 · zero STOPs.**

### CRITERION 0 — MET, AND MEASURED ON BOTH ARMS IN ONE SESSION
The F-R4-1 `lookupEui64ByNodeId` (EZSP `0x0061`) hop was bellows-derived and explicitly NOT silicon-verified. It is now both.
- **THE HIT** — `2026-09-04 17:51:15.203Z  zigbee.rejoin_candidate: device=0x00124B002FA8D1C5 nwk=0xf87d source=unknown_sender` → full chain to `device_adopted` in **315 ms**, `source=rejoin`, `status=COMPLETE`.
- **THE MISS** — `2026-09-04 18:28:41.461Z  zigbee.lookup_eui64_failed: nwk=0x15ac status=0x1` + `rejoin_candidate_unresolved … reason=lookup_miss`. The status byte the WU pre-wired was read on the first attempt.
- **THE BOUNDARY THIS EXPOSES (F-R4b-F):** `0x0061` resolves the coordinator's OWN table entries — it hit the mains ROUTER and missed the router-parented SLEEPY device. **F-R4-1 as shipped closes the silent-rejoiner gap for mains routers only.** The ZDO `IEEE_addr_req` follow-on the WU named as its own trigger condition is now EVIDENCED.

### THE FOUR R4b-4 CRITERIA
| | criterion | verdict | the evidence |
|---|---|---|---|
| **C1** | network RESUMES, zero formed | **✓ MET** | `network_resumed` ch20 PAN `0x774c`; **`network_formed` = 0 on all FIVE service starts, by count** |
| **C2** | ≥1 AVAILABLE + freshness in-window | **✓ MET** | 3/3 entities `AVAILABLE`/`stale:false`; `state_reported` 20:03:57 · 20:08:57 · 20:13:57 · 20:18:57, all inside 19:08:58Z–20:22:55Z |
| **C3** | rows grow, discriminator 0 | **✓ MET** | ROWS-W0 `173` @ 19:08:58Z → ROWS-W1 `212` @ 20:09:35Z (**+39** over **60 m 37 s**); discriminator **0** |
| **C4** | one run + rendered explanation, held card's OWN entities, incl. a device ADOPTED TODAY | **✓ MET** | run `01M1PX64EREVX8XAVACQNZNQGG` `COMPLETED`, `durationMs 10051`; trigger AND action both on `01M1PRQN03X8H4MNEZQ62F76F1` = the S31 adopted 17:51:15.518Z via `source=rejoin` |
**C4 PATH TAKEN: B** (no light entity existed; the Hue never answered). **THE VERDICT WORD THAT RENDERED: `CONFIRMED`** — `/api/v1/runs/{runId}/causal-chain` → `actions[0].outcome: "CONFIRMED"`, `settled: true`, and the store's own `state_confirmed` at position 186. Not `ACTED_BUT_UNCONFIRMED`.
**§6-F fallback fired: NO.** Branch 1 selected at the harvest; the S31 was never factory-reset.

### PER-SECTION
| § | verdict |
|---|---|
| §1 fetch + hash | **MET** · R4b-1 CLOSED — one .deb, hash identical on three surfaces |
| §2 swap + boot glance | **MET** — `hs-fresh`, incumbent `g7c57d7f`, formed 0, ROWS-A 105 (after D-1, D-2) |
| §3 config pre-read | **MET** — six adopt IEEEs, `permit_join_duration` absent (after D-3) |
| §4 install | **MET** · R4b-2 CLOSED — ordinary upgrade, no downgrade, 107→109, integrity `ok` (after D-4, D-5) |
| §5 measured boot | **MET** · R4b-3 CLOSED — **`Configuration issue` = 0: PKG-SEC-2 PROVEN, R-4's C-1 GONE**; schema line ×1 pre-load; stop-proof skipped (`ef02d13`) (after D-6) |
| §6 the arm | **MET — CRITERION 0** (after D-7, D-8) |
| §7 C4 | **MET — Path B, `CONFIRMED`** (after D-9, D-10, D-11, D-12) |
| §8 evidence window | **MET — C1 · C2 · C3, four of four with C4** |
| §9 restore | **MET — `[PASS] boot-health — 6/6 positive · 0 forbidden`, PAN unchanged, bundle `boot-health-20260904T203821Z`** (after D-13) |
| §10 | the hub's |
**⏺ census: 37 operator paste-backs banked** (including the two voided attempts, both filed). **Deviations: 13 (D-1…D-13), all T1/T2, all filed the same minute. STOPs: NONE — no T3 was reached at any point.** **Findings: F-R4b-A…H + proposal P-1.**

### ASKS OF THE HUB
1. **Mint C-002.** Four of four, criterion 0 on both arms. Word it on: artifact `ef02d13`; **Path B**; the verdict word **`CONFIRMED`**; the criterion-0 line quoted above; the window 19:08:58Z→20:09:35Z.
2. **Charter the ZDO `IEEE_addr_req` follow-on WU.** `0x0061` missed a router-parented sleepy device with `status=0x1`; the F-R4-1 gotchas named exactly this as the trigger for a second over-the-air surface.
3. **Rule on P-1 (the power-harness primitive, §9)** — operator-originated, recommended as a charter candidate in its own right.
4. **Demote playbook §6's "Hue LCA017: wall power-cycle ⇒ re-announce" from VERIFIED to CONTESTED** (F-R4b-G): three failures to reproduce, today's under ideal instrumented conditions. The bulb is adopted in the bench registry and **absent from the air**.
5. **Correct the packet's five instrument defects** (D-2 nested-quote `dpkg-query`, D-3 the `/etc` config path never re-derived against R-4's own D-f, D-9 the half-fixed token extraction, D-12 the invented `/api/v1/runs/{id}` route, D-13 gate sharing a block with its act), and **adopt the self-timing window block (D-8) as the standing pattern** for every windowed provocation.
6. **Restore `entity_registered` to the journal or rewrite §7's mapping step** (F-R4b-E) — the entity registers, the log line does not appear, and the packet instructs the operator to map ids from lines that are not there.
7. **Adjudicate two read-API shape gaps** (F-R4b-H) against the FROZEN v1.1 contract: `trigger.firingValue` is `null` on a trigger that matched, and `actions[].resultOutcome` is `null` while `outcome` is `CONFIRMED`.
8. **O-2 remains OPEN and is now confirmed across two artifacts** (`g7c57d7f` and `gef02d13`): a clean operator stop grades `Result=exit-code · ActiveState=failed · ExecMainStatus=143`. **The FAILCHAN stop-proof is still owed** — its CI is RED on `HeroLoopHardwareFreeIT`.
9. **`reporting_configured: clusters=1 verified=0 degraded=1` on a MAINS device** (F-R4b-C) — the sleepy-device excuse does not apply; not a stop, but unexplained.
10. **RECORD SIZE — a ruling is requested.** This record is ~99 KB against the packet's "≤ ~14 KB". It was not trimmed, deliberately: today produced 37 paste-backs including a 27-column schema, three JSON payloads and two full harvests, and §10 requires "every ⏺, in order". R-4's comparable record was already 29.8 KB, so the cap appears unreachable for a session of this scope. **Navigability was solved instead of length** — this §0 and the §9 findings card are the two screens the hub needs; everything below is drill-down. Say the word and a trimmed variant follows.

## §1 Fetch + hash (desktop)

**§1-a THE ORIGIN HASH — MET @ 16:27Z.** arm64 job → "Version-grammar echo" step, ⏺ verbatim:
```
hs_version=0.1.0+git20260903.124041.gef02d13
version-grammar echo green: 0.1.0+git20260903.124041.gef02d13 (scheme 0.1.0+git<YYYYMMDD.HHMMSS>.g<sha>; .deb Version=0.1.0+git20260903.124041.gef02d13; image VERSION=0.1.0+git20260903.124041.gef02d13; sha256 48a33b0dc614a7f74fd0e0a279480e3c2f1f8e1e952f3195f0ffdbad1c626003 homesynapse_0.1.0+git20260903.124041.gef02d13_arm64.deb)
```
ORIGIN SHA256 = `48a33b0dc614a7f74fd0e0a279480e3c2f1f8e1e952f3195f0ffdbad1c626003`. Version = `0.1.0+git20260903.124041.gef02d13` — carries §0's chosen sha `ef02d13` ✓ (the held card's incumbent is `…g7c57d7f`, so §4 is a forward upgrade). Artifact zip ⏺ saved as `~/Downloads/distribution-artifacts-arm64.zip` — NO `(1)` suffix (the stale-download trap from R-4's identically-named zip did not fire; the hash gate below is the backstop either way).

**§1-b UNPACK + HASH — MET @ 16:31:34Z · STOP-GATE R4b-1 CLOSED.** ⏺ verbatim:
```
$ mkdir -p ~/r4b-artifact ~/r3-history && mv ~/r4b-artifact/*.deb ~/r3-history/ 2>/dev/null; cd ~/r4b-artifact && powershell.exe -NoProfile -Command "Expand-Archive -LiteralPath \"$(cygpath -w ~/Downloads/distribution-artifacts-arm64.zip)\" -DestinationPath \"$(cygpath -w ~/r4b-artifact)\" -Force" && find . -name '*_arm64.deb' -exec sha256sum {} \;
48a33b0dc614a7f74fd0e0a279480e3c2f1f8e1e952f3195f0ffdbad1c626003 *./deb/build/homesynapse_0.1.0+git20260903.124041.gef02d13_arm64.deb
```
EXACTLY ONE `.deb` ✓ · nested at `./deb/build/` exactly as the packet's fix predicts (R-4 instrument defect (i) CONFIRMED FIXED — the corrected `find` form worked first time, zero operator cost) · hash `48a33b0d…626003` **EQUALS** the §1-a origin echo byte-for-byte ✓ · name carries `gef02d13` = §0's choice ✓. (The `*` before the path is `sha256sum`'s binary-mode marker under MINGW — instrument noise, not a datum.) Zero PowerShell error output. **R4b-1: one .deb · hash = the run log · sha in the name = §0's choice — ALL THREE MET.**

## §2 The swap + the held card's boot glance

**§2-i DIGEST — first attempt RAN ON THE WRONG HOST (instrument, not rig). ⏺ verbatim @ 16:36:52Z:**
```
Nick@DESKTOP-SRK0P9D MINGW64 ~/r4b-artifact
$ tail -2 ~/hs-bench/digests/nightly.log; ls -t ~/hs-bench/bundles | head -2
tail: cannot open '/c/Users/Nick/hs-bench/digests/nightly.log' for reading: No such file or directory
timeout-honesty-no-change-20260730T013228Z
usb-reenumeration-20260730T013228Z
```
**READ:** the block is `# WHERE: the bench card (ssh pi)` but executed in the DESKTOP Git Bash (prompt `Nick@DESKTOP-SRK0P9D`; the `tail` error resolves `~` to `/c/Users/Nick`). **THE TRAP, and it is a real one:** the desktop carries a STALE `~/hs-bench/bundles/` from **2026-07-30**, so the second half of the block returned two plausible bundle names (`timeout-honesty-no-change-20260730T013228Z`, `usb-reenumeration-20260730T013228Z`) with NO error. Had the `tail` half also existed on the desktop, this block would have returned a complete, well-formed, entirely FALSE digest read. **These two names are NOT bench data and are NOT the ⏺ for §2-i** — they are 5-week-old desktop residue. Filed as finding F-R4b-A (playbook §8 C-class: a glance that returns a plausible non-answer on the wrong surface). No rig state was touched — both commands are read-only. Re-issued as §2-i′ with a `hostname` first line (D-1).

**§2-i′ DIGEST — MET @ 16:40:08Z** (D-1 fix applied; the bench never goes down un-read). ⏺ verbatim:
```
homesynapse@hs-dev-1:~ $ hostname; tail -2 ~/hs-bench/digests/nightly.log; ls -t ~/hs-bench/bundles | head -2
hs-dev-1
2026-09-03 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.09s
2026-09-04 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.32s
command-s31-settle-20260904T083156Z
command-confirm-s31-20260904T083155Z
```
Host ⏺ **`hs-dev-1`** (bench card; ssh alias `pi`, login user `homesynapse`) — the D-1 `hostname` line did its job. **TWO nightlies present, not one:** 09-03 AND **09-04 @ ~08:31:56Z** (bundle stamps `20260904T0831xx`, consistent with the playbook §12 ~08:32Z nightly). Both `8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓`. **BASELINE FOR TONIGHT'S §9 FLOOR: green as of 08:31Z today** — a §9 failure tonight is therefore attributable to this session, not to a pre-existing regression. ON-latency 0.09 s → 0.32 s across the two nights (both well inside the ~5 s S31 confirmation window measured in the B2 return; noted, not a finding).
**OBS carried forward to §6:** `1 SKIP(hue-online)` on both nights — the Hue is not answering on the bench floor. R-4 D-g recorded the Hue as unpowered at the wall until mid-session. Its wall state MUST be established before §6's provocation 3, or that provocation is unfalsifiable.

**§2-ii SHUTDOWN + SWAP — MET.** ⏺ `sudo shutdown -h now` → `Read from remote host hs-dev-1: Connection reset by peer` / `Connection to hs-dev-1 closed.` (the halt, not a fault). Card swapped, coordinator dongle UNTOUCHED in its port, rig powered on. Operator wall clocks for power-off/power-on not captured (minor; the Z anchors below supersede). **Hue at the wall: OFF** (operator-confirmed) — see the §6 note.
**§2-iii BOOT GLANCE — 5 of 6 tokens MET, token 3 (version) BLANK → ruled T1 INSTRUMENT, re-read as §2-iii′.** ⏺ verbatim @ 16:47:52Z:
```
$ ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'hostname; date -u +%H:%M:%SZ; dpkg-query -W -f "${Version}\n" homesynapse; systemctl is-active homesynapse.service; sudo journalctl -u homesynapse.service --no-pager -n 400 | grep -E "zigbee\.(network_resumed|network_formed)" | tail -2; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" "SELECT COUNT(*) FROM events;"'
hs-fresh
16:47:52Z

active
Sep 04 12:43:18 hs-fresh homesynapse[859]: 12:43:18.651 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
105
```
`hs-fresh` ✓ (O-2 guard holds) · Z clock `16:47:52Z` ✓ · **version line EMPTY — see D-2** · `active` ✓ · `zigbee.network_resumed: channel=20 panId=0x774c`, **zero `network_formed`** in the same grep ✓ · **ROWS-A = 105** ⏺.
**PI-TZ RE-DERIVED ON THE INSTRUMENT (not from memory):** journalctl renders `Sep 04 12:43:18` while `date -u` reads `16:47:52Z` → the card's local rendering is **UTC−4**, matching the R-4 record's ET mapping (19:17:28 ET ↔ 23:17:28Z). So the service came up at **12:43:18 ET = 16:43:18Z**, ~4.5 min before the glance — consistent with the power-on. Every journalctl timestamp today is Z−4.
**ROWS-A note:** R-4 closed at ROWS-W1 = 80 (08-30 23:50Z); the store now reads 105 (+25). The held card was therefore powered at least once between R-4 and today. Not a mismatch (§2 asserts only "a row count"), but the delta is why §2-iii′'s version re-read is load-bearing rather than cosmetic — ROWS-A = 105 is the honest pre-install baseline.

**§2-iii′ BOOT GLANCE (D-2 instrument) — MET, 8/8 @ 16:59:54Z. §2 CLOSES MET.** ⏺ verbatim:
```
nick@hs-fresh:~ $ hostname; date -u +%H:%M:%SZ; date "+%Z %z"; dpkg-query -W homesynapse; cat /opt/homesynapse/VERSION; INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "zigbee\.network_formed"; sudo journalctl _SYSTEMD_INVOCATION_ID=$INV --no-pager | grep -cE "zigbee\.network_resumed"
hs-fresh
16:59:54Z
EDT -0400
homesynapse     0.1.0+git20260830.201400.g7c57d7f
0.1.0+git20260830.201400.g7c57d7f
INV=b0d791c7ee0747a1b29ac3c44f42d638
0
1
```
`hs-fresh` ✓ · Z `16:59:54Z` ✓ · **`EDT -0400` — Pi-TZ measured, not assumed** ✓ · incumbent version `0.1.0+git20260830.201400.g7c57d7f` AGREEING across `dpkg-query` and `/opt/homesynapse/VERSION` ✓ (so §4 is a genuine forward upgrade `g7c57d7f` → `gef02d13`) · `INV=b0d791c7ee0747a1b29ac3c44f42d638` (pre-install invocation) · **`network_formed` COUNT = 0 — the hard fence, proven by count not by absence-of-tail** ✓ · `network_resumed` count = 1 ✓. Login banner `Last login: Thu Sep 3 07:08:50 2026` corroborates the ROWS-A 80→105 delta (the card was up 09-03).

## §3 Step 0b — the config pre-read

**§3-i CONFIG-ROOT LOCATE (T2 read-only probe 1 of ≤3; issued BEFORE any copy, because the packet's path is contested by R-4's D-f) — INCONCLUSIVE ON EXISTENCE, CONCLUSIVE ON AUTHORITY.** ⏺ verbatim (the operative run; two identical repeats and one stray-prompt mis-paste elided, all read-only, no state touched):
```
nick@hs-fresh:~ $ systemctl show -p WorkingDirectory -p Environment --value homesynapse.service; for D in /etc/homesynapse/config /var/lib/homesynapse/config; do echo "== $D"; ls -la "$D" 2>&1 | head -8; done
HOMESYNAPSE_HOME=/var/lib/homesynapse
/var/lib/homesynapse
== /etc/homesynapse/config
ls: cannot access '/etc/homesynapse/config': Permission denied
== /var/lib/homesynapse/config
ls: cannot access '/var/lib/homesynapse/config': Permission denied
```
**(1) THE UNIT'S AUTHORITY — ⏺ CONFIRMED:** `Environment=HOMESYNAPSE_HOME=/var/lib/homesynapse`, `WorkingDirectory=/var/lib/homesynapse`. R-4's D-f is re-confirmed on this artifact at the unit, independently of the filesystem.
**(2) A CORRECTION TO HOW D-f SHOULD BE READ (finding F-R4b-B):** BOTH probes returned **`Permission denied`**, not `No such file or directory`. `ls` distinguishes these: a non-existent parent yields ENOENT. **Therefore `/etc/homesynapse` EXISTS on this card** and is simply not traversable by the unprivileged `nick` user — as is `/var/lib/homesynapse`. R-4's D-f recorded only `cp: cannot stat` without its errno clause, so **D-f's conclusion "the packet's `/etc/homesynapse/config/homesynapse.yaml` DOES NOT EXIST" is not established by the evidence quoted for it** — a `cp: cannot stat … Permission denied` reads identically at that level of quotation. The live config root is still `/var/lib/homesynapse/config/` on the unit's authority; but whether `/etc/homesynapse/config/` also holds files (a packaged default, a stale copy, or a symlink) is OPEN and is probe 2's question. This matters beyond today: a packet that edits the wrong one of two extant config trees edits a file the service never reads.
**(3) sudo posture ⏺:** `sudo -v` PROMPTED for `nick`'s password interactively (`[sudo] password for nick:`), yet the §2-iii′ one-shot `ssh … 'sudo journalctl …'` returned data with no TTY. So specific commands are NOPASSWD while general validation is not. Operationally: sudo works in this interactive session; a future non-interactive `ssh 'sudo …'` is not guaranteed for an arbitrary command.

**§3-ii CONFIG-ROOT RESOLVED (T2 probe 2 of ≤3) — DECISIVE.** ⏺ verbatim:
```
nick@hs-fresh:~ $ sudo ls -la /etc/homesynapse /var/lib/homesynapse; echo "=== config dirs ==="; sudo ls -la /etc/homesynapse/config /var/lib/homesynapse/config; echo "=== integrations ==="; sudo ls -la /etc/homesynapse/config/integrations /var/lib/homesynapse/config/integrations
/etc/homesynapse:
total 12
drwxr-x---  2 root homesynapse 4096 Aug 30 18:41 .
drwxr-xr-x 94 root root        4096 Sep  4 12:43 ..
-rw-r--r--  1 root root        1572 Aug  9 22:27 homesynapse.env

/var/lib/homesynapse:
total 24
drwx------  6 homesynapse homesynapse 4096 Aug 13 07:35 .
drwxr-xr-x 27 root        root        4096 Aug 13 07:35 ..
drwx------  2 homesynapse homesynapse 4096 Aug 13 07:35 backups
drwx------  4 homesynapse homesynapse 4096 Aug 30 08:58 config
drwx------  4 homesynapse homesynapse 4096 Sep  4 12:43 data
drwx------  2 homesynapse homesynapse 4096 Aug 13 07:35 tmp
=== config dirs ===
ls: cannot access '/etc/homesynapse/config': No such file or directory
/var/lib/homesynapse/config:
total 32
drwx------ 4 homesynapse homesynapse 4096 Aug 30 08:58 .
drwx------ 6 homesynapse homesynapse 4096 Aug 13 07:35 ..
-rw-r--r-- 1 homesynapse homesynapse  132 Aug 13 07:35 api_tokens
-rw-r--r-- 1 homesynapse homesynapse   26 Aug 13 07:35 home_id
-rw------- 1 homesynapse homesynapse 1208 Jul  9 22:26 homesynapse.yaml
-rw-r--r-- 1 homesynapse homesynapse   44 Aug 13 07:35 initial_api_token
drwx------ 2 homesynapse homesynapse 4096 Aug 30 19:37 integrations
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 13 07:35 schemas
=== integrations ===
ls: cannot access '/etc/homesynapse/config/integrations': No such file or directory
/var/lib/homesynapse/config/integrations:
total 16
drwx------ 2 homesynapse homesynapse 4096 Aug 30 19:37 .
drwx------ 4 homesynapse homesynapse 4096 Aug 30 08:58 ..
-rw------- 1 homesynapse homesynapse  299 Aug 30 19:37 zigbee.yaml
-rw------- 1 homesynapse homesynapse  299 Jul 21 07:33 zigbee.yaml.pre-repair-2026-08-30
```
**F-R4b-B RESOLVES AGAINST THE NAVIGATOR'S OWN HYPOTHESIS — recorded as such.** `/etc/homesynapse` exists but holds ONE file, `homesynapse.env` (1572 b, Aug 9), and **NO `config/` subdirectory** (`No such file or directory` under sudo). The unprivileged `Permission denied` at §3-i was produced by `/etc/homesynapse` being `drwxr-x--- root:homesynapse` — the kernel denies traversal to `nick` BEFORE it can report the child's non-existence, so EACCES masked ENOENT. **R-4's D-f is CORRECT as written; the doubt raised at §3-i is withdrawn.** The residual, and it is the transferable one: *`Permission denied` on a path probe is never evidence of existence OR non-existence — only `sudo` (or a stat by an entitled user) settles it.* A packet asserting a path's absence must quote the errno.
**THE LIVE CONFIG TREE (single, unambiguous): `/var/lib/homesynapse/config/`.** Fingerprints match R-4 exactly: `homesynapse.yaml` **1208 b** (mtime **Jul 9 22:26** — UNCHANGED since before R-4, so `bench-hero` stands exactly as R-4 found it, refs and all) · `integrations/zigbee.yaml` **299 b**, mtime **Aug 30 19:37** = the minute of R-4's §6-iv disarm (`19:37:48 ET` restart) — the file's own mtime corroborates that the `permit_join_duration` key was removed and never re-added · `initial_api_token` **44 b**, corroborating R-4's O-1 `size=44` and the 43-char-token instrument defect · aside `zigbee.yaml.pre-repair-2026-08-30` (299 b, Jul 21) present, nothing deleted. Also present and not previously censused: `api_tokens` (132 b), `home_id` (26 b), `schemas/`, `backups/`, `tmp/`, and `/etc/homesynapse/homesynapse.env` (the unit's EnvironmentFile).
**CONSEQUENCE FOR THE REST OF THE PACKET:** every `/etc/homesynapse/config/...` path in §3, §6 (step 0a `sed`), §6-F and §7 (the `cp` + `nano` + the disarm `sed`) is wrong on this rig and must read `/var/lib/homesynapse/config/...`. Applied as D-3.

**§3-iii THE PRE-READ — MET @ 17:09Z (13:09 ET).** ⏺ verbatim:
```
nick@hs-fresh:~ $ sudo mkdir -p /root/r4b-history && sudo cp /var/lib/homesynapse/config/integrations/zigbee.yaml /root/r4b-history/zigbee.yaml.pre-R4b && sudo ls -la /root/r4b-history/ && echo "--- zigbee.yaml as found ---" && sudo cat -n /var/lib/homesynapse/config/integrations/zigbee.yaml
total 12
drwxr-xr-x 2 root root 4096 Sep  4 13:09 .
drwx------ 4 root root 4096 Sep  4 13:09 ..
-rw------- 1 root root  299 Sep  4 13:09 zigbee.yaml.pre-R4b
--- zigbee.yaml as found ---
     1  serial_port: /dev/zigbee
     2  channel: 20
     3  adopt_devices:
     4    - "0x00178801101A09BB"    # Hue LCA017
     5    - "0xF044D3FFFE9C78D7"    # SNZB-03P
     6    - "0x00124B002FA8D1C5"    # S31 Lite zb
     7    - "0xF044D3FFFED2A201"    # SNZB-02P
     8    - "0xF044D3FFFE1C1E8E"    # SNZB-01P
     9    - "0x449FDAFFFE688F57"    # SNZB-04P contact
```
Copy-aside landed: `/root/r4b-history/zigbee.yaml.pre-R4b`, **299 b** — byte-count identical to the source ✓, nothing deleted. **Content EXACTLY the §3 expectation:** `serial_port: /dev/zigbee` · `channel: 20` · `adopt_devices` with **all six** IEEEs in the R-4 order (Hue `…1A09BB`, SNZB-03P `…9C78D7`, S31 `…A8D1C5`, SNZB-02P `…D2A201`, SNZB-01P `…1C1E8E`, SNZB-04P `…688F57`) ✓ · **`permit_join_duration` ABSENT** ✓ (independently corroborated by the file's Aug 30 19:37 mtime = R-4's §6-iv disarm minute) · **every key present is a fragment key** — `serial_port`, `channel`, `adopt_devices` — so **ZERO `Configuration issue` lines is the honest bar at §5**; no out-of-schema key exists to produce the "expected one WARN" arm. 9 lines total.
**§6 STEP-0a PRE-VERIFIED ON THE REAL BYTES:** line 1 = `serial_port: /dev/zigbee`, so `sed -i '1a permit_join_duration: 254'` lands the key at **line 2**, exactly as the packet's expect states, and as a top-level mapping key (YAML order-independent — `channel` merely shifts to line 3). The §7 disarm `sed -i '/^permit_join_duration:/d'` will anchor that same column-0 active line ✓ (playbook 2026-07-19 rule satisfied). **The one live hazard is a DOUBLE paste of step 0a — it would insert the key twice and produce a duplicate YAML key; the packet's own `head -4` read-back is the guard, and the operator will be told to run it once.**
**§3 CLOSES MET.**

## §4 The install

**§4-i COPY-ACROSS — first attempt PARTIAL: act 1 landed, act 2 failed on NAME RESOLUTION (transport, not rig).** ⏺ verbatim @ 17:14Z:
```
$ ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'mkdir -p ~/r3-history && mv ~/homesynapse_*_arm64.deb ~/r3-history/ 2>/dev/null; ls ~/homesynapse_*_arm64.deb 2>/dev/null; echo "---"' && cd ~/r4b-artifact && scp -i ~/.ssh/id_ed25519_pi $(find . -name '*_arm64.deb') nick@hs-fresh.local: && ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
---
ssh: Could not resolve hostname hs-fresh.local: Name or service not known
scp: Connection closed
```
**READ:** the FIRST `ssh` to `hs-fresh.local` RESOLVED AND RAN (it emitted the bare `---`, so the old R-4 `.deb` was moved to `~/r3-history/` and nothing remains at `~`); the `scp`, seconds later, could not resolve the SAME name. Intermittent mDNS on the desktop resolver — the card never went away (its ssh session stayed live throughout and answered the next block). **The `---`-alone assertion is MET** — no second `.deb` on the card.
**§4-ii ADDRESS PIN (T2 probe, read-only, run in the live card session so no resolution was required) — ⏺ verbatim:**
```
nick@hs-fresh:~ $ hostname -I; echo "--- interfaces ---"; ip -4 -o addr show scope global | awk '{print $2, $4}'
192.168.1.80 2600:1702:6e8a:aff0::47 2600:1702:6e8a:aff0:ebde:ae1b:776c:c32c
--- interfaces ---
eth0 192.168.1.80/24
```
Card = **`192.168.1.80`** on `eth0` (single global v4; two global v6; no Tailscale interface on this card, unlike `hs-dev-1` whose banner showed a 100.74/16 CGNAT peer). Pinned as D-4.

**§4-i′ COPY-ACROSS (D-4 pinned) — MET 6/6 @ 17:19Z (13:19 ET).** ⏺ verbatim:
```
$ ssh -o StrictHostKeyChecking=accept-new -i ~/.ssh/id_ed25519_pi nick@192.168.1.80 'hostname; mkdir -p ~/r3-history && mv ~/homesynapse_*_arm64.deb ~/r3-history/ 2>/dev/null; ls ~/homesynapse_*_arm64.deb 2>/dev/null; echo "---"; ls -la ~/r3-history/' && cd ~/r4b-artifact && scp -o StrictHostKeyChecking=accept-new -i ~/.ssh/id_ed25519_pi $(find . -name '*_arm64.deb') nick@192.168.1.80: && ssh -o StrictHostKeyChecking=accept-new -i ~/.ssh/id_ed25519_pi nick@192.168.1.80 'sha256sum ~/homesynapse_*_arm64.deb; dpkg-deb --field ~/homesynapse_*_arm64.deb Version Architecture'
Warning: Permanently added '192.168.1.80' (ED25519) to the list of known hosts.
hs-fresh
---
total 122840
drwxrwxr-x 3 nick nick     4096 Sep  4 13:12 .
drwx------ 6 nick nick     4096 Sep  4 13:12 ..
-rw-r--r-- 1 nick nick 62905262 Aug 30 08:34 homesynapse_0.1.0+git20260823.231355.gdec35be_arm64.deb
-rw-r--r-- 1 nick nick 62854240 Aug 30 18:24 homesynapse_0.1.0+git20260830.201400.g7c57d7f_arm64.deb
drwxr-xr-x 2 root root     4096 Aug 30 09:04 homesynapse.service.d-removed-20260830
-rw------- 1 root root     1208 Aug 30 19:09 homesynapse.yaml.pre-R4
-rw------- 1 root root      299 Aug 30 19:09 zigbee.yaml.pre-R4
homesynapse_0.1.0+git20260903.124041.gef02d13_arm64.deb    100%   60MB  62.8MB/s   00:00
48a33b0dc614a7f74fd0e0a279480e3c2f1f8e1e952f3195f0ffdbad1c626003  /home/nick/homesynapse_0.1.0+git20260903.124041.gef02d13_arm64.deb
Version: 0.1.0+git20260903.124041.gef02d13
Architecture: arm64
```
`hs-fresh` at `.80` ✓ (no DHCP reassignment) · **`---` ALONE** ✓ (exactly one `.deb` at `~` after the copy) · **THE THIRD INDEPENDENT HASH `48a33b0d…626003` — CI echo = desktop unzip = post-scp on the card, three surfaces, byte-identical** ✓ · `Version: 0.1.0+git20260903.124041.gef02d13` · `Architecture: arm64` ✓.
**⏺ `~/r3-history/` CORROBORATES THE R-4 RECORD INDEPENDENTLY** — nothing deleted, ever: both prior artifacts preserved (`…gdec35be` Aug 30 08:34, `…g7c57d7f` Aug 30 18:24), R-4's own copies-aside `homesynapse.yaml.pre-R4` (**1208 b**) and `zigbee.yaml.pre-R4` (**299 b**) present with matching sizes, and `homesynapse.service.d-removed-20260830/` — the systemd drop-in that came off at R-4 §4, the run's crux, still parked rather than deleted. The "move aside, delete nothing" fence has held across three sessions.

**§4-ii INTEGRITY GATE — MET @ 17:21:41Z. ROWS-pre = 107 · `integrity_check` = `ok`.** ⏺ verbatim:
```
nick@hs-fresh:~ $ sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;' && echo "--- homesynapse.yaml as found (pre-install) ---" && sudo cat -n /var/lib/homesynapse/config/homesynapse.yaml
107
ok
--- homesynapse.yaml as found (pre-install) ---
     1  integrations:
     2    zigbee: !include integrations/zigbee.yaml
     3
     4  automation:
     5    automations:
     6      - name: bench-hero
     7        triggers:
     8          - type: state_change
     9            entity_ref: 01KX1PB9AAB4VB3E10BD477TV3
    10            attribute: occupied
    11            to: "true"
    12        actions:
    13          - type: command
    14            target: { entity_ref: 01KX1PA4HSJ581GASYB7DHE40F }
    15            command: turn_on
    16          - type: delay
    17            duration: PT6S
    18          - type: command
    19            target: { entity_ref: 01KX1PA4HSJ581GASYB7DHE40F }
    20            command: set_brightness
    21            parameters: { level: 50 }
    22          - type: delay
    23            duration: PT6S
    24          - type: command
    25            target: { entity_ref: 01KX1PA4HSJ581GASYB7DHE40F }
    26            command: set_color_temperature
    27            parameters: { kelvin: 4550 }
    28          - type: delay
    29            duration: PT2S
    30          - type: command
    31            target: { entity_ref: 01KX1PA4HSJ581GASYB7DHE40F }
    32            command: set_color_temperature
    33            parameters: { kelvin: 4525 }
    34          - type: delay
    35            duration: PT20S
    36          - type: command
    37            target: { entity_ref: 01KX1PA4HSJ581GASYB7DHE40F }
    38            command: identify
    39            parameters: { duration_s: 5 }
```
ROWS-pre `107` (ROWS-A was 105 @ 16:47Z; +2 over 37 min of uptime) ✓ · `ok` ✓ — the store is sound, the install may proceed.
**⏺ `bench-hero` PRE-INSTALL, AT THE BYTES — 39 lines, content-identical to the R-4 record's description, mtime still Jul 9.** THE RE-BIND MAP FOR §7 IS NOW EXACT AND WAS CAPTURED BEFORE THE INSTALL (so a post-install re-read also proves the `.deb` did not touch it):
- **line 9** — trigger `entity_ref: 01KX1PB9AAB4VB3E10BD477TV3` (the BENCH card's MOTION entity), with `attribute: occupied` on line 10 and `to: "true"` on line 11.
- **lines 14, 19, 25, 31, 37** — FIVE action targets, every one `entity_ref: 01KX1PA4HSJ581GASYB7DHE40F` (the BENCH card's LIGHT entity): `turn_on` → PT6S → `set_brightness 50` → PT6S → `set_color_temperature 4550` → PT2S → `set_color_temperature 4525` → PT20S → `identify 5 s`.
**SIX entity_ref sites in total, at six known line numbers.** This is what R-4's C4 could not get past: the trigger ref was re-bindable but no light entity existed on this card at all to receive the five CommandActions (R-4 §6: "the action target could not — no light entity exists in the registry"). Whether §7 takes Path A or Path B is therefore decided by exactly one question at §6: **does the Hue adopt today?**

**§4-iii THE INSTALL — MET @ 17:23Z · STOP-GATE R4b-2 CLOSED.** ⏺ verbatim:
```
nick@hs-fresh:~ $ sudo apt install -y ~/homesynapse_*_arm64.deb 2>&1 | tail -8 && dpkg-query -W -f '${Version}\n' homesynapse && cat /opt/homesynapse/VERSION && sleep 25 && systemctl is-active homesynapse.service && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;' && sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'PRAGMA integrity_check;'
HomeSynapse Core is running.
----------------------------------------------------------------
 HomeSynapse Core installed.
 First-run pairing token: /var/lib/homesynapse/config/initial_api_token
   View it with:  sudo homesynapse-token
   Pair a client with that bearer token to reach the dashboard,
   then delete the token file.
----------------------------------------------------------------
0.1.0+git20260903.124041.gef02d13
0.1.0+git20260903.124041.gef02d13
active
109
ok
```
NO `downgrad` token anywhere in the tail — the `0.1.0+git<YYYYMMDD.HHMMSS>` ordering scheme sorts `20260903 > 20260830` numerically under dpkg's digit-run comparison, so this was an ORDINARY FORWARD UPGRADE with no flag ✓ · **version `0.1.0+git20260903.124041.gef02d13` from BOTH `dpkg-query` and `/opt/homesynapse/VERSION`** ✓ · `active` ✓ · **ROWS 107 → 109, zero loss** ✓ · `integrity_check` = `ok` ✓. **R4b-2: all four MET.**
**O-1 RE-SIGHTED (not inherited):** the postinst printed the first-run pairing-token banner on an UPGRADE, exactly as R-4 recorded. Its cosmetic-only status is re-proved at §5 on the file mtimes, not assumed. The banner's own advice ("then delete the token file") is NOT followed — the delete-nothing fence outranks it.

## §5 The measured boot (PKG-SEC-2's proof · the stop-proof if it rode)

**§5 THE MEASURED BOOT — MET 4/4 @ 17:26Z · STOP-GATE R4b-3 CLOSED.** ⏺ verbatim:
```
nick@hs-fresh:~ $ INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; echo -n "Configuration issue count: "; ... ; echo "--- config tree post-install ---"; sudo ls -la /var/lib/homesynapse/config /var/lib/homesynapse/config/integrations
INV=2a6c8ca049d64d6a8765b6bf2dd43d85
Configuration issue count: 0
schema_registered count: 1
network_formed count: 0
--- lines ---
Sep 04 13:22:49 hs-fresh homesynapse[1537]: 13:22:49.075 [main] INFO  c.h.lifecycle.HomeSynapseCore -- lifecycle.integration_schema_registered: type=zigbee stage=pre-load
Sep 04 13:22:58 hs-fresh homesynapse[1537]: 13:22:58.308 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
Sep 04 13:22:58 hs-fresh homesynapse[1537]: 13:22:58.425 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
--- config tree post-install ---
/var/lib/homesynapse/config:
-rw-r--r-- 1 homesynapse homesynapse  132 Aug 13 07:35 api_tokens
-rw-r--r-- 1 homesynapse homesynapse   26 Aug 13 07:35 home_id
-rw------- 1 homesynapse homesynapse 1208 Jul  9 22:26 homesynapse.yaml
-rw-r--r-- 1 homesynapse homesynapse   44 Aug 13 07:35 initial_api_token
drwx------ 2 homesynapse homesynapse 4096 Aug 30 19:37 integrations
drwxr-xr-x 2 homesynapse homesynapse 4096 Aug 13 07:35 schemas
/var/lib/homesynapse/config/integrations:
-rw------- 1 homesynapse homesynapse  299 Aug 30 19:37 zigbee.yaml
-rw------- 1 homesynapse homesynapse  299 Jul 21 07:33 zigbee.yaml.pre-repair-2026-08-30
```
- **`Configuration issue` COUNT = 0 — PKG-SEC-2 IS PROVEN ON SILICON. R-4's C-1 is GONE.** R-4 recorded this WARNING on every one of five starts (`property 'zigbee' is not defined in the schema and the schema does not allow additional properties`); on the first boot of `gef02d13` it does not occur once. And the bar was the honest one: §3 established that every key in this `zigbee.yaml` is a fragment key, so no out-of-schema key existed to excuse a warning.
- **`lifecycle.integration_schema_registered` COUNT = 1** — exactly one, `type=zigbee stage=pre-load`, at `13:22:49.075` ET (**17:22:49Z**), i.e. on the `[main]` thread BEFORE the adapter thread starts. That is precisely the re-timing PKG-SEC-2 claims: the fragment is supplied to `registerIntegrationSchema` ahead of `start()`, so `integrations.zigbee` validates at Phase-1. ✓
- **`network_formed` COUNT = 0** ✓ (proven by count, not by absence-from-a-tail) · **`zigbee.network_resumed: channel=20 panId=0x774c`** at `13:22:58.425` ET (17:22:58Z) ✓ — custody intact across the upgrade.
- **BONUS ⏺ (not in the packet's expect, captured by the widened grep): `zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false`** — the coordinator is a SONOFF Dongle Plus MG24 (CP210x, 10c4:ea60), captured by stable-id, and `pinnedOnly=false`. This is the byte-exact `stableId` the playbook's Rosonway rule says reopen-target gates must bind. Adapter came up 9.4 s after `[main]`.
- **O-1 RESOLVED AGAIN, ON EVIDENCE:** every operator-owned file is byte- and mtime-UNCHANGED across the install — `initial_api_token` 44 b **Aug 13 07:35**, `api_tokens` 132 b **Aug 13 07:35**, `home_id` 26 b, `homesynapse.yaml` 1208 b **Jul 9 22:26**, `integrations/zigbee.yaml` 299 b **Aug 30 19:37**. The postinst banner is cosmetic on an upgrade; the token pair was NOT rewritten and `bench-hero` was NOT touched by the `.deb`. §7's API reads and the re-bind both stand on this.
**⏺ `stop-proof: skipped (ef02d13)`** — §0 chose `ef02d13`'s artifact, so the §5 FAILCHAN stop-proof block is not run, per the packet's own instruction. The FAILCHAN §10-O behaviour remains unproven on hardware and waits for the next card session.

## §6 THE ARM — the window, the three provocations, the harvest (criterion 0)

**§6 STEP 0a — THE KEY IS SET. MET @ 17:37:35Z (13:37:35 ET).** ⏺ verbatim:
```
nick@hs-fresh:~ $ sudo grep -qE '^[[:space:]]*permit_join_duration:' /var/lib/homesynapse/config/integrations/zigbee.yaml && echo "GUARD: already present — NOT adding" || sudo sed -i '1a permit_join_duration: 254' /var/lib/homesynapse/config/integrations/zigbee.yaml; echo "--- after ---"; sudo cat -n /var/lib/homesynapse/config/integrations/zigbee.yaml; date -u +%H:%M:%SZ
--- after ---
     1  serial_port: /dev/zigbee
     2  permit_join_duration: 254
     3  channel: 20
     4  adopt_devices:
     5    - "0x00178801101A09BB"    # Hue LCA017
     6    - "0xF044D3FFFE9C78D7"    # SNZB-03P
     7    - "0x00124B002FA8D1C5"    # S31 Lite zb
     8    - "0xF044D3FFFED2A201"    # SNZB-02P
     9    - "0xF044D3FFFE1C1E8E"    # SNZB-01P
    10    - "0x449FDAFFFE688F57"    # SNZB-04P contact
17:37:35Z
```
`permit_join_duration: 254` on **line 2** exactly as §3 predicted from the real bytes; `channel: 20` shifted to line 3; the six adopt IEEEs intact at lines 5–10; file now 10 lines. **No `GUARD:` line** — confirming this was a first insertion, not a duplicate. **The key is SET but NO WINDOW IS OPEN:** under the M9.4-PJ semantic (and PKG-SEC-2's now schema-honest "absent ⇒ no window · set ⇒ ONE window per boot"), the window opens only at service start — so the rig is armed and quiet until the restart.

**§6 THE WINDOW — OPENED CLEAN.** ⏺ `PRE: old INV=2a6c8ca049d64d6a8765b6bf2dd43d85  permit_join_opened in it: 0` — the pre-arm invocation had **zero** windows, so every operator act before 17:50:30Z happened with the door shut (see §6-vii). Restart issued **17:50:30Z** (13:50:30 ET) by the block's own clock-wait. ⏺:
```
17:50:30Z
RESTARTED — window opens in ~10s
17:52:38Z
NEW INV=d77f224231c44bb28e83fa6fe80dac9d
Sep 04 13:50:42 hs-fresh homesynapse[2515]: 13:50:42.170 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
Sep 04 13:50:42 hs-fresh homesynapse[2515]: 13:50:42.200 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.permit_join_opened: duration=254s
```
`network_resumed: channel=20 panId=0x774c` ✓ · **`permit_join_opened: duration=254s`, NO `permit_join_clamped`** ✓ — 254 accepted exactly, as at R-4. **WINDOW-OPEN = 17:50:42.200Z · WINDOW-CLOSE = 17:54:56.200Z.** Restart→resumed latency 12.0 s; window opened 30 ms after resume.

### §6 THE HARVEST — ⏺ WHOLE (read at 17:55:24Z, close+28 s)
```
Sep 04 13:50:33 hs-fresh homesynapse[2515]: 13:50:33.929 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=2 entities=2 position=40
Sep 04 13:51:15 hs-fresh homesynapse[2515]: 13:51:15.203 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.rejoin_candidate: device=0x00124B002FA8D1C5 nwk=0xf87d source=unknown_sender
Sep 04 13:51:15 hs-fresh homesynapse[2515]: 13:51:15.204 [integration-zigbee-0] WARN  c.h.i.zigbee.ZclIngestionUnit -- zigbee.ingestion_unknown_sender: nwk=0xf87d cluster=0x6; frame skipped
Sep 04 13:51:15 hs-fresh homesynapse[2515]: 13:51:15.435 [integration-zigbee-0] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_proposed: device=0x00124B002FA8D1C5 manufacturer=SONOFF model=S31 Lite zb profile=sonoff_s31_lite_zb status=COMPLETE source=rejoin
Sep 04 13:51:15 hs-fresh homesynapse[2515]: 13:51:15.440 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.proposal_accepted: device=0x00124B002FA8D1C5 source=config
Sep 04 13:51:15 hs-fresh homesynapse[2515]: 13:51:15.518 [integration-zigbee-0] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_adopted: device=0x00124B002FA8D1C5 deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 entities=1
Sep 04 13:51:20 hs-fresh homesynapse[2515]: 13:51:20.649 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reporting_configured: device=0x00124B002FA8D1C5 clusters=1 verified=0 degraded=1
```

**§6-vii PROVOCATIONS 2 AND 3 ARE VOID, NOT NEGATIVE — the distinction matters and is recorded as such.** Operator statement, ⏺ verbatim: *"I had done each act, in order, 2 or 3 times thinking I simply had to do it then run the command, and did not know everything was structured and timed in the command"* and *"act 3 started with the Hue switched on"*. Consequences, read at the mechanism:
- **ACT 1 (S31) is SOUND.** The `rejoin_candidate` at 17:51:15.203Z sits **33 s after WINDOW-OPEN**, ~20 s after the ACT-1 banner, and inside invocation `d77f2242…` — it can only be the in-window press. The earlier presses fell in invocation `2a6c8ca0…`, which the PRE read proves had **zero** windows.
- **ACT 2 (SNZB-03P) — NO READING TAKEN.** The sensor had been waved at repeatedly in the minutes before the window. An occupancy sensor in its `occupied=true` hold does not re-report on further motion, so a wave inside the window plausibly generated no frame at all. Absence of a `rejoin_candidate` for `0xF044D3FFFE9C78D7` is therefore **uninformative**, not evidence about the rejoin hook.
- **ACT 3 (Hue) — NO READING TAKEN, and for a sharper reason: the Hue was ALREADY ON when the ACT-3 banner fired.** The provocation's whole mechanism is a power transition; there was none. A mains bulb sitting idle and joined emits little or nothing. Absence of any Hue chain is therefore **uninformative**. Note this also leaves the playbook §6 "verified behavior" — *Hue LCA017: plain wall power-cycle ⇒ re-announce* — still untested on this rig after R-4 D-g failed to reproduce it.
- **NO device other than the S31 was adopted. NO light entity exists on this card.** That is the standing state going into §7 and it decides the path.
**⏺ THE SILENCE AFTER ADOPTION IS ITSELF CORRECT BEHAVIOR, and is the second-strongest datum in the harvest.** Exactly ONE `ingestion_unknown_sender` line exists in the whole invocation — at 17:51:15.204Z, the admitting frame. The plug's scheduled `:54 s` report was due at **17:53:54Z, inside the window**, and produced NO second `rejoin_candidate` and NO further `unknown_sender`: once adopted, the device's frames route normally and `admitRejoinCandidate` short-circuits at `already_adopted`. The gap R-3a/R-4 measured — a mains device speaking forever into a skip — closed at 17:51:15 and stayed closed.

**§6-viii THE CLOSED-DOOR READ (old invocation `2a6c8ca0…`, which the PRE check proved had ZERO windows) — ⏺ verbatim, tail 20 of 20:**
```
Sep 04 13:33:57 … zigbee.ingestion_unknown_sender: nwk=0xf87d cluster=0x6; frame skipped
Sep 04 13:38:57 … zigbee.ingestion_unknown_sender: nwk=0xf87d cluster=0x6; frame skipped
Sep 04 13:43:33 … zigbee.ingestion_unknown_sender: nwk=0x15ac cluster=0x402; frame skipped
Sep 04 13:43:43 … nwk=0x15ac cluster=0x402   |  13:43:53 … 0x15ac  |  13:43:57 … 0xf87d cluster=0x6
Sep 04 13:44:03 / 13:44:19 / 13:44:29 / 13:44:39 / 13:44:49 / 13:44:59 / 13:45:09 … nwk=0x15ac cluster=0x402
Sep 04 13:45:47 … nwk=0xf87d cluster=0x6
Sep 04 13:46:30 / 13:46:40 … nwk=0x15ac cluster=0x402
Sep 04 13:46:54 … nwk=0xf87d cluster=0x6
Sep 04 13:48:52 / 13:48:54 / 13:48:57 … nwk=0xf87d cluster=0x6
```
**⏺ FINDING F-R4b-D — A SECOND SILENT REJOINER WAS LIVE ON THIS RIG AND IS NOT IN ANY PRIOR RECORD: `nwk=0x15ac`, `cluster=0x402` (Temperature Measurement).** Cluster 0x0402 points to the SNZB-02P temp/humidity sensor (`0xF044D3FFFED2A201`, adopt-list line 8). Its traffic is BURSTY, not periodic: a burst every ~10 s from 13:43:33→13:45:09, a second 13:46:30→13:46:40, then **silence from 13:46:40 onward — it did not transmit once inside the 13:50:42→13:54:56 window**, which is why the harvest carries no second candidate. This is a MISSED ADOPTION OF OPPORTUNITY, not a failure of the hook: F-R4-1 admits on a frame, and no frame arrived. **For the hub: this rig has at least TWO silent rejoiners, and a single 254 s window catches only the devices that happen to speak inside it. A future packet wanting N adoptions should either open successive windows or provoke each device explicitly rather than rely on ambient traffic.**
**⏺ PRECISION CORRECTION TO THE PLUG'S CADENCE (supersedes R-4's `:54 s`, appended not rewritten):** the S31's scheduled reports land at **13:33:57 · 13:38:57 · 13:43:57 · 13:48:57** — minutes ≡ 3 mod 5 confirmed, but the SECOND has drifted from R-4's `:54 s` to **`:57 s`** over five days (~0.6 s/day). The packet's window geometry (open at ≡0 mod 5 between :20 and :40 s, 254 s long) still swallows it with ~60 s to spare, so the design is robust to the drift — but a packet that pinned `:54 s` tightly would now be wrong.
**⏺ CORROBORATION OF THE PRE-WINDOW ACTS:** `13:48:52` and `13:48:54` are two operator presses ~2 s apart, immediately before the scheduled `13:48:57` report — matching the operator's account of pressing repeatedly before the timed run, and confirming those presses landed in the OLD invocation where no window was open.
**⏺ NAVIGATOR INSTRUMENT ERROR, DISCLOSED:** this read used `tail -20`, which truncates the invocation's FIRST zigbee lines. The invocation began 13:22:49 and the first `0xf87d` frame is expected ~13:23:57 — so the `zigbee.rejoin_ignored_window_closed` line (emitted ONCE per nwk per epoch, on the FIRST closed-door frame) falls before the visible range. **The absence of `rejoin_ignored_window_closed` in the output above is therefore NOT evidence that it did not fire** — it is my own tail/head defect, the same "absence proven by a tail" class I corrected in the packet at §5. Re-read with `head` is pending.

### ★ CRITERION 0 — MET. THE 0x0061 HOP IS PROVEN ON SILICON. ★
**The line, quoted for the hub's C-002 sentence:**
`2026-09-04 17:51:15.203Z  zigbee.rejoin_candidate: device=0x00124B002FA8D1C5 nwk=0xf87d source=unknown_sender`
This is the first execution of EZSP frame **`0x0061` (`lookupEui64ByNodeId`)** against real silicon. It was bellows-derived and explicitly **NOT silicon-verified** at authoring (F-R4-1 gotchas: "if silicon disagrees the WU is not wrong… the fix is a one-constant/one-layout edit"). **Silicon agreed.** The SONOFF Dongle Plus MG24 answered the lookup for `nwk=0xf87d` with `0x00124B002FA8D1C5` — the S31 Lite zb plug, the exact device R-4 could only ever see as an anonymous `ingestion_unknown_sender`. **There is NO `zigbee.lookup_eui64_failed` line and NO `zigbee.rejoin_candidate_unresolved` line in this invocation.** The status byte the WU pre-wired for the miss case was never needed.

**THE WHOLE CHAIN RAN, IN THE DOCUMENTED GRAMMAR, IN 315 ms:**
| Δ from candidate | token | what it proves |
|---|---|---|
| +0 ms | `rejoin_candidate … source=unknown_sender` | H-ii, the primary evidenced arm: unknown-sender HA frame inside an open window → IEEE resolved |
| +1 ms | `ingestion_unknown_sender: nwk=0xf87d cluster=0x6; frame skipped` | the pin holds exactly as designed — detection fires BEFORE the WARN, and the admitting frame is still skipped (the report is lost; the interview follows) |
| +232 ms | `device_proposed … model=S31 Lite zb profile=sonoff_s31_lite_zb status=COMPLETE **source=rejoin**` | the interview walk completed COMPLETE, and the NEW provenance key renders — one interview path, two triggers, never a bypass |
| +237 ms | `proposal_accepted … source=config` | the IEEE was on the `adopt_devices` accept-list (§3 line 7) |
| +315 ms | `device_adopted … deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 entities=1` | **A DEVICE ADOPTED TODAY, THROUGH THE REJOIN PATH** — R4b-4's C4 clause |
| +5.4 s | `reporting_configured … clusters=1 verified=0 degraded=1` | reporting bound, but DEGRADED — see below |
`cluster=0x6` is On/Off — the frame was the plug's own state report following the operator's short press, exactly the frame class R-4 recorded as forever-skipped. **PACKET BRANCH 1 SELECTED: `rejoin_candidate` ×1 AND `device_adopted` ×1 → criterion 0 MET, adoption MET → §7. §6-F DOES NOT FIRE; the S31 is NOT factory-reset.**

**⏺ FINDING F-R4b-C — `reporting_configured: clusters=1 verified=0 degraded=1`.** The S31 is a MAINS device, not a sleepy end device, so the playbook's "a sleepy Configure-Reporting TIMEOUT is a posture, not a failure" does not excuse this. Reporting is bound but unverified on the one cluster. Functionally the plug still reports on its own 5-minute `:54 s` cadence, so C2/C3 are unaffected; recorded as a real observation for the hub, not a stop.
**⏺ OBSERVATION — `entity_registered` DID NOT APPEAR IN THE JOURNAL** despite `device_adopted … entities=1`. The grep carried the token. Either the line is below INFO on this path or it is emitted by a surface this grep does not reach. The read API is the authority and settles it at §7; flagged because the packet's §7 instructs the operator to map ids to devices *using the `entity_registered` lines*, and on this artifact those lines are not there to map. **Second glance-semantics defect of the day.**
**⏺ `registry.projection_live: devices=2 entities=2 position=40` at 13:50:33.929 (17:50:33Z) is a BOOT-TIME value, frozen at `onCaughtUp()` 42 s BEFORE the adoption** — it is NOT a post-adoption census and must not be read as one (playbook 04P D-2, verbatim re-fire). The post-adoption count is §7's `/api/v1/entities`.

### §6-F The announce-class fallback (only if fired)

**§6-F DID NOT FIRE.** The harvest selected packet BRANCH 1 (`rejoin_candidate` ×≥1 AND `device_adopted` ×≥1 → criterion 0 MET, adoption MET → §7). The S31 was **NOT** factory-reset; the announce-class fallback was never entered and the 5 s button hold was never performed.

## §7 C4 — the re-bind, the trigger, the run + the explanation

**§7-i THE REGISTRY READ — MET @ 18:08:26Z. D-9's token fix works: `token_len=43`, `http=200`** (R-4's 403 at this exact step is GONE, and the cause is confirmed to have been the extraction regex, not the token). ⏺ verbatim:
```
nick@hs-fresh:~ $ TOK=$(sudo cat /var/lib/homesynapse/config/initial_api_token | tr -d '\r\n'); echo "token_len=${#TOK}"; echo "--- entities ---"; curl -s -w "\nhttp=%{http_code}\n" -H "Authorization: Bearer $TOK" http://127.0.0.1:7070/api/v1/entities
token_len=43
--- entities ---
{"data":[{"entityId":"01M19RHWXYZYJMM26SX0E41HXN","availability":"UNAVAILABLE","stale":false},{"entityId":"01M19XN7NNQQ8S3JJF09T6YKKY","availability":"AVAILABLE","stale":false},{"entityId":"01M1PRQN03X8H4MNEZQ62F76F1","availability":"AVAILABLE","stale":false}],"meta":{"viewPosition":136,"timestamp":"2026-09-04T18:08:26.096780091Z"}}
http=200
```
**THREE entities — the registry grew by one, and the new one is TODAY'S ADOPTION.**
- `01M1PRQN03X8H4MNEZQ62F76F1` — **AVAILABLE** — **THE S31 PLUG, adopted at 17:51:15.518Z.** Mapped WITHOUT the missing `entity_registered` lines: ULIDs are time-ordered and this entity's `01M1PRQ…` prefix shares the millisecond-scale timestamp of the adoption's `deviceId 01M1PRQMZHFV4SAWT1E96B9BQ2`; the other two are `01M19…` (August). **This is C4's "an entity of the held card's own, from a device adopted TODAY through the rejoin path."**
- `01M19XN7NNQQ8S3JJF09T6YKKY` — AVAILABLE, `stale:false`.
- `01M19RHWXYZYJMM26SX0E41HXN` — **UNAVAILABLE** (⏺ CHANGE FROM R-4, where both pre-existing entities read AVAILABLE/`stale:false`). Recorded; C2's bar (≥1 AVAILABLE) is met twice over regardless.
- `viewPosition` **136** — the read API and the store agree; rows have advanced from ROWS-pre 109.
**⏺ THE `entity_registered` GAP IS NOW FULLY CHARACTERISED (finding F-R4b-E):** the entity demonstrably EXISTS and is AVAILABLE on the read API, yet no `entity_registered` line was emitted to the journal in that invocation. The registration is real; only its log surface is missing. **The packet's §7 instruction — "the newest `entity_registered` lines carry the device", used to map ids to devices — is therefore unexecutable on this artifact.** The workable instrument is the one used here: diff the entity list against the known-prior ids, and corroborate by ULID timestamp prefix against `device_adopted`'s `deviceId`. Recommend the hub either restore the log line or re-write that mapping step.

**§7-ii THE AUTOMATION READ — MET @ 18:13:12Z.** ⏺ verbatim:
```
{"data":[{"automationId":"01M1PRPCF45DHFT4QJAW4F1X54","name":"bench-hero","enabled":true,"components":[StateChangeTrigger, CommandAction, DelayAction, CommandAction, DelayAction, CommandAction, DelayAction, CommandAction, DelayAction, CommandAction],"lastRunId":null}],"pagination":{"nextCursor":null,"hasMore":false,"limit":50},"meta":{"viewPosition":137,"timestamp":"2026-09-04T18:13:12.669490008Z"}}
http=200
```
`bench-hero` present · `enabled:true` · **10 components — 1 StateChangeTrigger + 5 CommandAction + 4 DelayAction**, parsing exactly as the 39-line yaml declares (§4-ii) · **`lastRunId: null`** — C4's starting line; this field must carry a run id before C4 can be claimed. Loads clean on `gef02d13` exactly as it did on `g7c57d7f` at R-4 — the automation was never the defect; its refs were.
**⏺ OBSERVATION (minor, recorded): `automationId` is `01M1PRPCF45DHFT4QJAW4F1X54`, minted at the 17:50:30Z boot** (`01M1PRP…` shares the prefix band of that boot's adoption ids). R-4 recorded `01M1AGJHC9JMDJ4YX1AQQDY37R` for the same automation. **The automation id is therefore per-load, not persistent across restarts** — it cannot be used as a cross-session handle, and any future packet or dashboard reference must resolve `bench-hero` by NAME.

### §7-A THE HUE-VIA-PLUG EXPERIMENT (operator-proposed; navigator-approved; filed as D-10)
**Origin:** the operator proposed converting the S31's relay into a remotely-timeable mains switch for the Hue lamp — plug the lamp into the adopted S31, lamp switch ON, relay OFF, then close the relay INSIDE an open permit-join window. **Why it was approved rather than escalated:** the packet's own provocation 3 already orders a Hue wall power-cycle; this is the same ordered act performed with a better switch, and "a second window" is named in §E among the branches the packet contains. Both prior attempts at this bulb (R-4 §6-iii D-g, and today's ACT 3) were void for the same reason — the power transition was hand-timed and did not land inside a window. **What makes this the first fair test in the arc:** `gef02d13` carries BOTH admission paths — `handleAnnounce` (if the bulb announces on power-up, the M9.4 path) and F-R4-1's H-i/H-ii (if it rejoins silently holding the network key) — and the window is open. R-4 had neither path available. A silent result today is therefore a genuine finding about the device, not another instrumentation gap. **Fence stated to the operator and enforced: exactly ONE Hue power cycle in the run (the 6× factory dance is out of scope today).** ACT 2 (SNZB-03P wave) was re-run in the same window, this time validly — the sensor had been undisturbed ~20 min, clearing its occupancy hold.

**§7-A RESULT — THE SECOND WINDOW. WINDOW-OPEN `18:25:42.749Z` → CLOSE `18:29:56.749Z` · INV `38bb5e64dd5c4b36ae81181032335b8c`.** ⏺ verbatim:
```
18:25:30Z RESTARTED
Sep 04 14:25:42 hs-fresh homesynapse[4052]: 14:25:42.719 … zigbee.network_resumed: channel=20 panId=0x774c
Sep 04 14:25:42 hs-fresh homesynapse[4052]: 14:25:42.749 … zigbee.permit_join_opened: duration=254s
18:30:30Z
===== HARVEST =====
Sep 04 14:28:41 hs-fresh homesynapse[4052]: 14:28:41.461 [integration-zigbee-0] WARN  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.lookup_eui64_failed: nwk=0x15ac status=0x1
Sep 04 14:28:41 hs-fresh homesynapse[4052]: 14:28:41.462 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.rejoin_candidate_unresolved: nwk=0x15ac cluster=0x402 reason=lookup_miss
--- unknown senders seen, by nwk ---
      8 ingestion_unknown_sender: nwk=0x15ac
```
**Operator ⏺: S31 button pressed at `18:26:19Z` (window-open +36 s, well inside), "right at the turn of the second"; the lamp lit "no more than half a second later" — POWER DELIVERY TO THE HUE IS PHYSICALLY CONFIRMED**, so the provocation itself is sound this time and any silence is the device's, not the method's. `network_formed` absent; `permit_join_opened: duration=254s`, no clamp.

### ★★ THE MISS ARM OF CRITERION 0 IS ALSO MEASURED — BOTH ARMS, SAME RIG, SAME SESSION ★★
```
2026-09-04 18:28:41.461Z  zigbee.lookup_eui64_failed: nwk=0x15ac status=0x1
2026-09-04 18:28:41.462Z  zigbee.rejoin_candidate_unresolved: nwk=0x15ac cluster=0x402 reason=lookup_miss
```
The packet named this exact line "a first-class datum … as valuable a datum as a candidate line — it is the one thing no desk could measure." **We now hold BOTH:** `0xf87d` resolved and adopted at 17:51:15Z; `0x15ac` **missed**, with the status byte the WU pre-wired precisely so that reading it would need no second run. **`status=0x1`** — EmberStatus `0x01` (`EMBER_ERR_FATAL`) / the v14 `sl_Status` replacement `0x01` (`SL_STATUS_FAIL`): a generic failure, i.e. the coordinator holds no EUI64 for `0x15ac`. Both WARNs are on the expected loggers (`EzspCoordinatorProtocol` for the protocol-level failure, `ZigbeeIntegrationAdapter` for the policy-level unresolved) and land **1 ms apart**, exactly the spec's order.
**⏺ MECHANISM — THE SHAPE OF THE MISS (F-R4b-F, the day's second headline).** `lookupEui64ByNodeId` (0x0061) reads the coordinator's OWN tables. `0xf87d` is the S31 — a MAINS ROUTER, and by its 5-minute direct reporting almost certainly a neighbour/child of the coordinator, so its entry is local and the lookup hits. `0x15ac` is cluster `0x0402` traffic — the SNZB-02P temp/humidity sensor, a SLEEPY END DEVICE, which parents to whichever router it joined through and need not appear in the coordinator's address table at all. **The emerging rule: 0x0061 resolves the devices the coordinator already knows locally, and misses the ones that joined through another router.** That is a device-CLASS boundary, not a flake — and it means F-R4-1 as shipped closes the silent-rejoiner gap for mains routers and leaves it open for router-parented sleepy devices.
**⏺ THIS IS THE TRIGGER CONDITION THE WU ITSELF NAMED.** F-R4-1's gotchas: *"NO ZDO IEEE_addr_req in this WU — a second over-the-air surface is a second WU if 0x0061 misses on silicon."* It missed on silicon, today, with the status byte quoted. **The second WU is now evidenced rather than speculative, and this record is its justification.**
**⏺ THE ONCE-PER-EPOCH DEDUP IS CONFIRMED ON SILICON (T7).** `0x15ac` produced **EIGHT** `ingestion_unknown_sender` frames in the window and **exactly ONE** `lookup_eui64_failed` + **exactly ONE** `rejoin_candidate_unresolved`. `rejoinLookupAttempted` asked the coordinator once per nwk per window epoch and stayed silent thereafter while the standing WARN continued per frame — spec-exact, on hardware.

**⏺ THE HUE: ABSOLUTE SILENCE — and this is now a REAL negative result, not another void (F-R4b-G).** Zero frames of ANY kind from `0x00178801101A09BB`: no `device_announce`, no `device_join`, no `rejoin_candidate`, and not even an `ingestion_unknown_sender` (the by-nwk census shows `0x15ac` and nothing else). The conditions were the best in the whole arc: an OPEN 254 s window · BOTH admission paths live (`handleAnnounce` and F-R4-1's H-i/H-ii) · a cold power-up at a known second, physically confirmed by the lamp lighting · 3 min 37 s of window remaining afterwards. **Reading:** the most economical explanation is that the Hue LCA017 is NOT A MEMBER OF THIS NETWORK. Corroborating: both nightly digests carry `1 SKIP(hue-online)`; the playbook's own verified behavior says a factory-fresh Hue *joins immediately on power-up* when a window is open, and it did not; and a joined, powered mains router would at minimum have produced routed traffic or a rejoin. **Recommendation to the hub: demote playbook §6's "Hue LCA017: plain wall power-cycle ⇒ re-announce" from VERIFIED BEHAVIOR to CONTESTED** — three attempts (R-3a, R-4 D-g, R-4b today) have failed to reproduce it, and today's was properly instrumented. Re-joining that bulb needs the 6× factory dance, which is out of scope today by §E.
**⏺ THE SNZB-03P (ACT 2): silence, and it is AMBIGUOUS BY CONSTRUCTION — do not read it as a failure.** `registry.projection_live` shows TWO devices/TWO entities already adopted before today. If the SNZB-03P is one of them, its frames route normally and can never appear as an unknown sender, so the rejoin hook is not even reachable for it. The absence is consistent with correct behaviour and carries no information either way.
**CONSEQUENCE: no light entity exists. §7 proceeds on PATH B, as planned.**


**§7-iii THE RE-BIND WRITTEN — MET @ 18:56Z (14:56 ET).** ⏺ verbatim read-back:
```
--- new homesynapse.yaml ---
     1  integrations:
     2    zigbee: !include integrations/zigbee.yaml
     3
     4  automation:
     5    automations:
     6      - name: bench-hero
     7        triggers:
     8          - type: state_change
     9            entity_ref: 01M1PRQN03X8H4MNEZQ62F76F1
    10            attribute: "on"
    11            to: "true"
    12        actions:
    13          - type: delay
    14            duration: PT10S
    15          - type: command
    16            target: { entity_ref: 01M1PRQN03X8H4MNEZQ62F76F1 }
    17            command: turn_off
-rw------- 1 root        root        1208 Sep  4 14:56 /root/r4b-history/homesynapse.yaml.pre-rebind
-rw------- 1 homesynapse homesynapse  426 Sep  4 14:56 /var/lib/homesynapse/config/homesynapse.yaml
```
Pre-rebind copy preserved at **1208 b** (byte-identical size to the original) ✓ · new file **426 b**, ownership `homesynapse:homesynapse`, mode `0600` — unchanged from the original's posture ✓ · both `entity_ref` sites carry `01M1PRQN03X8H4MNEZQ62F76F1`, the plug adopted TODAY ✓.
**THE VOCABULARY WAS VERIFIED AT SOURCE BEFORE IT WAS WRITTEN, not taken from the packet** (playbook: never name a verb the emitting surface does not produce). From `core/device-model/…/StandardCapabilities.java` `onOff()`: capability id `on_off`, **attribute `on`** (boolean, READ/WRITE/NOTIFY), commands `turn_on` / `turn_off` / `toggle`, `ConfirmationPolicy(EXACT_MATCH, ["on"], 5000 ms)`, and `turn_off`'s `ExpectedOutcome(on, ExactMatch(false), 5000 ms)`. From `integration/integration-zigbee/src/main/resources/zigbee-profiles.json`, profile `sonoff_s31_lite_zb`: `capability: on_off · confirmationMode: EXACT_MATCH · authoritativeAttribute: OnOff/0x0000 · reportsAuthoritative: VERIFIED_REPORTS · reportingPosture: ON_CHANGE · confirmability: CONFIRMABLE · recommendedTimeoutMs: 5000`. **The plug is declared CONFIRMABLE with a 5 s envelope — so `CONFIRMED` is a reachable verdict word for this run, not a hope.** (The profile's own note flags that its 5000 ms is the Hue's SEED value, not measured, and that the S31 envelope is still to be minted by the bench — a standing item the day's run now has data for.) `attribute` is QUOTED (`"on"`) defensively: the parser is `snakeyaml-engine 2.9` (YAML 1.2, where bare `on` is a string, not a boolean) — quoting removes the YAML-1.1 `on`-as-true hazard from the file permanently, and is recommended as a standing convention.

**§7-iv DISARM + LOAD CHECK — MET 4/4 @ 19:04:39Z. INV `95c7f1fc1c7a4ae6b0b6dcf767e0949f`.** ⏺ verbatim:
```
--- zigbee.yaml disarmed ---
     1  serial_port: /dev/zigbee
     2  channel: 20
     3  adopt_devices:
     4    - "0x00178801101A09BB"    # Hue LCA017
     5    - "0xF044D3FFFE9C78D7"    # SNZB-03P
     6    - "0x00124B002FA8D1C5"    # S31 Lite zb
     7    - "0xF044D3FFFED2A201"    # SNZB-02P
     8    - "0xF044D3FFFE1C1E8E"    # SNZB-01P
     9    - "0x449FDAFFFE688F57"    # SNZB-04P contact
INV=95c7f1fc1c7a4ae6b0b6dcf767e0949f
permit_join_opened + Configuration issue count: 0
--- automations ---
{"data":[{"automationId":"01M1PWX6JF2FC01Y9DKP9X43HJ","name":"bench-hero","enabled":true,"components":[StateChangeTrigger, DelayAction, CommandAction],"lastRunId":null}],…,"meta":{"viewPosition":170,"timestamp":"2026-09-04T19:04:39.133398028Z"}}
http=200
```
- **DISARMED:** `zigbee.yaml` back to its original 9 lines, `permit_join_duration` gone, content-equivalent to `/root/r4b-history/zigbee.yaml.pre-R4b` ✓. The column-0 anchored delete worked as §3 predicted.
- **`permit_join_opened + Configuration issue` COUNT = 0** ✓ — one number carrying two proofs. (a) **The M9.4-PJ "absent ⇒ NO window" semantic is re-confirmed ON THE PKG-SEC-2 SCHEMA**, which is a load-bearing check today and not a repeat of R-4's: PKG-SEC-2 deliberately REMOVED `default: 120` from the fragment because a composed default would have opened a 120 s join window on every unconfigured boot. Zero here is that removal working on hardware — the door is shut and stays shut. (b) Zero `Configuration issue` again, on a fourth boot.
- **THE RE-BIND PARSED: exactly 3 components** — `StateChangeTrigger` + `DelayAction` + `CommandAction`, down from 10 ✓. The read API confirms the file the operator wrote is the automation the engine loaded.
- **`lastRunId: null`** ✓ — no spurious boot-time trigger despite the plug standing in the `on` state through the restart. State rehydration does not synthesise a `state_change`; the trigger's edge semantics hold across a restart. (Recorded because it was an explicit pre-stated failure mode, not an assumption.)
- `automationId` is `01M1PWX6JF2FC01Y9DKP9X43HJ` — third distinct id for `bench-hero` today (R-4: `01M1AGJ…`; 17:50 boot: `01M1PRP…`), re-confirming the id is per-load and only the NAME is a stable handle.

**§7-v ⏺ ROWS-W0 = `173` @ `19:08:58Z`. THE ≥45-MIN EVIDENCE WINDOW OPENS HERE; §8's floor is `19:53:58Z`.**


### ★★★ §7-vi C4 — bench-hero RAN. `lastRunId` IS NO LONGER NULL. ★★★
⏺ verbatim:
```
--- runs ---
{"data":[{"runId":"01M1PX64EREVX8XAVACQNZNQGG","automationId":"01M1PWX6JF2FC01Y9DKP9X43HJ","automationName":"bench-hero","triggeredAt":"2026-09-04T19:09:04.323238Z","status":"COMPLETED","terminalReason":null}],"pagination":{"nextCursor":null,"hasMore":false,"limit":50},"meta":{"viewPosition":186,"timestamp":"2026-09-04T19:10:23.678512884Z"}}
http=200
--- automations ---
{"data":[{"automationId":"01M1PWX6JF2FC01Y9DKP9X43HJ","name":"bench-hero","enabled":true,"components":[StateChangeTrigger, DelayAction, CommandAction],"lastRunId":"01M1PX64EREVX8XAVACQNZNQGG"}],…,"meta":{"viewPosition":186,…}}
http=200
```
**`runId 01M1PX64EREVX8XAVACQNZNQGG` · `automationName: bench-hero` · `triggeredAt 2026-09-04T19:09:04.323238Z` · `status: COMPLETED` · `terminalReason: null` · `lastRunId` = that run id.**
**This is the exact field that read `{"data":[]}` and `lastRunId: null` at R-4, where C4 was MISS-BLOCKED.** The blocker was never the automation — it loaded clean on both artifacts — it was that `bench-hero`'s refs belonged to the bench card and no adoptable target existed here. Both halves are now closed: the plug was **adopted TODAY at 17:51:15.518Z through the F-R4-1 rejoin path**, and the automation is bound to **its** entity `01M1PRQN03X8H4MNEZQ62F76F1` at both the trigger and the action. **R4b-4's C4 clause — "one run + a rendered explanation on the held card's OWN entities including a device adopted TODAY" — is satisfied on the entity-provenance half; the rendered-explanation half is §7-vii.**
**Timing ⏺:** trigger fired **6.3 s after ROWS-W0** and **~1 s after the operator's press**; the run reached `COMPLETED` inside the 79 s before the read. `viewPosition` 173 → **186** (+13 rows minted by the trigger, the run and the confirmation traffic) — the store and the read API agree at 186.


### ★★★ §7-vii THE RENDERED EXPLANATION — `outcome: "CONFIRMED"`. C4 IS COMPLETE. ★★★
**The packet's stated fallback route `GET /api/v1/runs/<id>` DOES NOT EXIST — `http=404`, "Endpoint GET /api/v1/runs/01M1PX64EREVX8XAVACQNZNQGG not found".** Resolved by reading the route table at source (`api/rest-api/src/main/java/com/homesynapse/api/rest/RestFilters.java`, `installRunQueryEndpoints` / `installAutomationQueryEndpoints`). The REGISTERED read surface is exactly four routes: `GET /api/v1/runs` · **`GET /api/v1/runs/{runId}/causal-chain`** (the hero causal-chain tree for one terminal run) · `GET /api/v1/automations` · `GET /api/v1/automations/{id}/non-firing`. Filed as D-12. ⏺ verbatim from the real route:
```
{"data":{"runId":"01M1PX64EREVX8XAVACQNZNQGG","automationId":"01M1PWX6JF2FC01Y9DKP9X43HJ","automationName":"bench-hero","trigger":{"type":"StateChangeTrigger","subjectRef":{"type":"entity","id":"01M1PRQN03X8H4MNEZQ62F76F1"},"matchedAt":"2026-09-04T19:09:04.323238Z","firingValue":null},"conditions":[],"actions":[{"type":"CommandAction","targetRef":{"type":"entity","id":"01M1PRQN03X8H4MNEZQ62F76F1"},"command":"turn_off","params":{},"outcome":"CONFIRMED","reason":null,"resultOutcome":null,"settled":true}],"outcome":{"status":"COMPLETED","reason":null,"durationMs":10051,"actionCount":2,"commandCount":1},"cascade":{"parentRunId":null,"depth":0}},"meta":{"viewPosition":211,"timestamp":"2026-09-04T20:05:30.307937721Z"}}
http=200
```
**THE VERDICT WORD THE HUB WORDS C-002 ON: `CONFIRMED`.** Not `ACTED_BUT_UNCONFIRMED`. The `turn_off` was dispatched to the plug and the plug's OWN state report satisfied the `EXACT_MATCH` policy on attribute `on` inside its 5 000 ms envelope — the actuator confirmed its own action in-band. `settled: true`, `reason: null`, `terminalReason: null`.
**Every field of the chain, read at the token:**
- `trigger.subjectRef.id` = `01M1PRQN03X8H4MNEZQ62F76F1` and `actions[0].targetRef.id` = `01M1PRQN03X8H4MNEZQ62F76F1` — **BOTH ends of the automation bound to the entity of a device adopted TODAY, at 17:51:15.518Z, through the F-R4-1 rejoin path.** R4b-4's C4 clause is satisfied in full: one run · a rendered explanation · the held card's OWN entities · a device adopted today.
- `matchedAt: 2026-09-04T19:09:04.323238Z` ≡ the list endpoint's `triggeredAt` to the microsecond — the B2/DP-3 field agreement the playbook calls the health signal HOLDS on this artifact (divergence would have been a new finding).
- **`durationMs: 10051`** — the `PT10S` delay plus 51 ms of dispatch. The declared duration is honoured to 0.5 %.
- `actionCount: 2, commandCount: 1` — the delay and the command, counted separately and correctly.
- `conditions: []` · `cascade: {parentRunId: null, depth: 0}` — no conditions, not a cascade.
**⏺ THE PHYSICAL SEQUENCE — instrument over recollection, disclosed.** The operator's account was that at STEP 2 he "pressed the S31 off, then ~10s later it came on automatically." The instrument says the opposite and is unambiguous: a `state_change … to: "true"` trigger can only match a transition INTO `on=true`, `matchedAt` is 1.3 s after the STEP-2 banner, and the single action was `turn_off … CONFIRMED` 10.051 s later. **The record therefore states: the STEP-2 press turned the plug ON (lamp lit); 10.05 s later the automation turned it OFF and the plug confirmed it (lamp dark).** The operator's recollection is recorded as inverted, not as a contradiction of the data — a ~90-minute gap separated the act from the description. Filed as a lesson: a physical witness must be captured at the act, in the same minute, or the instrument becomes the only record.
**⏺ TWO SMALL EXPLAINABILITY GAPS (F-R4b-H, for the frontend lane, not stops):** `trigger.firingValue` is **null** on a trigger that demonstrably matched — the hero cannot render "because `on` became true" from this payload; and `actions[0].resultOutcome` is **null** while `outcome` is `CONFIRMED`, so the two outcome fields are not both populated on the happy path. Both are read-API shape observations against the FROZEN v1.1 contract, worth an adjudication before the dashboard tries to render them.


## §8 The evidence window (C1 · C2 · C3)

**§8-i C1 AND C3 — BOTH MET @ 20:09:35Z.** ⏺ verbatim:
```
nick@hs-fresh:~ $ echo -n "ROWS-W1: "; sudo sqlite3 "file:/var/lib/homesynapse/data/homesynapse-events.db?mode=ro" 'SELECT COUNT(*) FROM events;'; echo -n "at: "; date -u +%H:%M:%SZ; INV=$(systemctl show -p InvocationID --value homesynapse.service); echo "INV=$INV"; echo -n "throw-discriminator: "; …; echo -n "network_resumed: "; …; echo -n "network_formed: "; …
ROWS-W1: 212
at: 20:09:35Z
INV=95c7f1fc1c7a4ae6b0b6dcf767e0949f
throw-discriminator: 0
network_resumed: 1
network_formed: 0
```
**THE WINDOW: ROWS-W0 `173` @ `19:08:58Z` → ROWS-W1 `212` @ `20:09:35Z`. ELAPSED 60 min 37 s — the ≥45-min floor (`19:53:58Z`) is cleared by 15 min 37 s.**
- **C3 — MET.** Row delta **+39** (173 → 212), strictly increasing ✓, and the **throw-discriminator is `0`**: zero `NoClassDefFoundError`, zero `jdk.jfr`, zero `BusMetrics` across the entire invocation. The store grew under load with no class-loading or metrics throw anywhere in the window.
- **C1 — MET.** `zigbee.network_resumed` = **1**, `zigbee.network_formed` = **0**. **THE ONE-COORDINATOR / ONE-NETWORK INVARIANT HELD ACROSS THE ENTIRE SESSION: five service starts today (16:43:18, 17:22:49, 17:50:30, 18:25:30, 19:04:xx Z) and `network_formed` measured ZERO on every one, by count, never by absence-from-a-tail.** Channel 20 / PAN `0x774c` custody survived an artifact upgrade, two permit-join windows, an adoption, a config edit and a re-bind.
- **INV `95c7f1fc1c7a4ae6b0b6dcf767e0949f`** is the SAME invocation as the §7-iv disarm restart — so the whole ≥45-min window sits inside ONE continuous service lifetime, and every count above is scoped to it. No restart split the evidence window (the R-4 instrument defect (ii) class, structurally avoided).

**§8-ii THE C2 INSTRUMENT — `.schema events` READ BEFORE ANY COLUMN WAS NAMED.** ⏺ verbatim:
```
CREATE TABLE events (
    global_position   INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id          BLOB(16) NOT NULL,
    home_id           BLOB(16) NOT NULL,
    event_type        TEXT     NOT NULL,
    schema_version    INTEGER  NOT NULL DEFAULT 1,
    ingest_time       INTEGER  NOT NULL,
    event_time        INTEGER,
    subject_ref       BLOB(16) NOT NULL,
    subject_type      TEXT     NOT NULL,
    subject_sequence  INTEGER  NOT NULL,
    priority          TEXT     NOT NULL DEFAULT 'NORMAL',
    origin            TEXT     NOT NULL DEFAULT 'UNKNOWN',
    actor_ref         BLOB(16),
    idempotency_key   TEXT,
    correlation_id    BLOB(16) NOT NULL,
    causation_id      BLOB(16),
    event_category    TEXT     NOT NULL,
    payload_size      INTEGER  NOT NULL,
    batch_id          BLOB(16),
    external_ref      TEXT,
    intent_kind       TEXT     NOT NULL DEFAULT 'UNSPECIFIED',
    logical_time      INTEGER  NOT NULL DEFAULT 0,
    node_id           INTEGER  NOT NULL DEFAULT 0,
    payload           BLOB     NOT NULL,
    chain_hash        BLOB(32) NOT NULL DEFAULT x'00…00', payload_iv BLOB, dek_ref TEXT,
    UNIQUE(subject_ref, subject_sequence)
);
CREATE INDEX idx_events_type        ON events(event_type, global_position);
CREATE INDEX idx_events_correlation ON events(correlation_id, global_position);
CREATE INDEX idx_events_ingest_time ON events(ingest_time);
CREATE INDEX idx_events_event_time  ON events(COALESCE(event_time, ingest_time));
CREATE INDEX idx_events_actor       ON events(actor_ref) WHERE actor_ref IS NOT NULL;
CREATE UNIQUE INDEX idx_events_idempotency ON events(home_id, idempotency_key) WHERE idempotency_key IS NOT NULL;
```
**⏺ CORRECTION TO THE R-4 RECORD (appended, not rewritten): the position column is `global_position`, not `pos`.** R-4's §6-vi wrote "pos 75 / pos 73" — a readable abbreviation that is NOT a column name and would fail if pasted into a query. The real column set for C2 is `global_position` · `event_type` · `ingest_time` (INTEGER, NOT NULL, microseconds) · `event_time` (INTEGER, NULLABLE, microseconds) · `subject_ref` (BLOB(16)) · `subject_type`. 27 columns confirmed (the last three — `chain_hash`, `payload_iv`, `dek_ref` — share a line, which is why a naive column count can read 25). The `idx_events_event_time` index on `COALESCE(event_time, ingest_time)` is the shipped freshness instrument and the query below uses exactly that expression. **This is why the packet's "read the schema, never invent column names" rule earns its place: the abbreviation in the prior record would have produced `no such column: pos`.**

**§8-iii C2 — MET @ 20:22:55Z.** ⏺ verbatim:
```
--- newest state rows ---
214|state_reported|2026-09-04 20:18:57|2026-09-04 20:18:57|01A06D8BD403
213|state_reported|2026-09-04 20:13:57|2026-09-04 20:13:57|01A06D8BD403
212|state_reported|2026-09-04 20:08:57|2026-09-04 20:08:57|01A06D8BD403
211|state_reported|2026-09-04 20:03:57|2026-09-04 20:03:57|01A06D8BD403
--- in-window census (global_position > 173) ---
state_reported|23|214
state_changed|8|206
automation_action_completed|2|182
automation_action_started|2|179
automation_completed|1|183
automation_triggered|1|176
availability_changed|1|188
command_dispatched|1|181
command_issued|1|180
state_confirmed|1|186
--- entities ---
{"data":[{"entityId":"01M19RHWXYZYJMM26SX0E41HXN","availability":"AVAILABLE","stale":false},{"entityId":"01M19XN7NNQQ8S3JJF09T6YKKY","availability":"AVAILABLE","stale":false},{"entityId":"01M1PRQN03X8H4MNEZQ62F76F1","availability":"AVAILABLE","stale":false}],"meta":{"viewPosition":214,"timestamp":"2026-09-04T20:22:55.749610438Z"}}
http=200
```
- **≥1 AVAILABLE — ALL THREE entities `AVAILABLE`, `stale:false`** ✓, including `01M19RHWXYZYJMM26SX0E41HXN`, which read **UNAVAILABLE** at 18:08:26Z and has since recovered — the census's single `availability_changed` at position **188** is that recovery, in band and inside the window. C2's bar is met three times over.
- **FRESHNESS IN-WINDOW — four consecutive `state_reported` rows at `20:03:57 · 20:08:57 · 20:13:57 · 20:18:57`**, every one inside `19:08:58Z → 20:22:55Z` ✓. `ingest_time` and `event_time` agree exactly on all four (no ingest lag).
- **⏺ THE CLOSING DATUM OF THE DAY, AND THE PRETTIEST ONE: those rows ARE the S31.** Their cadence is 5 minutes at **`:57 s`** on minutes ≡ 3 mod 5 — byte-for-byte the plug's scheduled reporting cadence measured at §6-viii, and on a NEW `subject_ref` prefix (`01A06D8BD403`; R-4's reporting entity was `01A053DA9EB5`). **This morning those exact frames landed as `zigbee.ingestion_unknown_sender: nwk=0xf87d cluster=0x6; frame skipped`, every five minutes, forever. Tonight the same frames land as `state_reported` rows in the event store.** That is the F-R4-1 gap closing, measured end-to-end on the same device, in the same session, on the same cadence.
- **⏺ THE AUTOMATION'S COMPLETE IN-BAND FOOTPRINT, in position order** — the causal chain minted as events, not merely returned by an API: `176 automation_triggered` → `179 automation_action_started` (×2: the delay and the command) → `180 command_issued` → `181 command_dispatched` → `182 automation_action_completed` (×2) → `183 automation_completed` → **`186 state_confirmed`**. `state_confirmed` is the store's own record of the `CONFIRMED` verdict — the read API and the event log agree.
- Census total = 41 = ROWS 214 − 173 ✓ — every row minted in the window is accounted for by type; nothing unexplained entered the store.

**§8-iv THE CLEAN STOP — ⏺ @ 20:25:45Z, EXACTLY AS THE PACKET PREDICTED. NOT A FINDING.**
```
nick@hs-fresh:~ $ sudo systemctl stop homesynapse.service; sleep 3; systemctl show -p Result -p ActiveState -p ExecMainStatus homesynapse.service; date -u +%H:%M:%SZ
Result=exit-code
ExecMainStatus=143
ActiveState=failed
20:25:45Z
```
`Result=exit-code · ExecMainStatus=143 · ActiveState=failed` — **the known lie (R-4's O-2), reproduced byte-for-byte on `ef02d13` and ⏺ without alarm** per the packet's own instruction. `143` = 128+15 = SIGTERM: an ORDERLY operator stop that systemd grades as a failure because the process does not install a handler that exits 0. FAILCHAN (`7af2d6c`, the §10-O orderly-close classification) is the fix for exactly this and did NOT ride today — its CI is RED on `HeroLoopHardwareFreeIT`. **So O-2 remains OPEN on the shipped unit, its persistence is now confirmed across two artifacts (`g7c57d7f` and `gef02d13`), and the FAILCHAN stop-proof is still owed.** This ⏺ is the standing "before" that a future FAILCHAN session's `Result=success · ActiveState=inactive · ExecMainStatus=143 → active` will be measured against.

### ★ STOP-GATE R4b-4 — FOUR OF FOUR. ★
| # | criterion | verdict | evidence |
|---|---|---|---|
| **C1** | network RESUMES, zero formed | **✓ MET** | `network_resumed` count 1 in the window's invocation; `network_formed` count **0** on ALL FIVE service starts today, by count |
| **C2** | ≥1 entity AVAILABLE + store freshness in-window | **✓ MET** | 3/3 entities `AVAILABLE`, `stale:false`; `state_reported` at 20:03:57 / 20:08:57 / 20:13:57 / 20:18:57, all inside 19:08:58Z–20:22:55Z |
| **C3** | event store grows, zero throw-discriminator | **✓ MET** | ROWS 173 → 212 (+39) over 60 m 37 s; discriminator **0** |
| **C4** | one `bench-hero` run + rendered explanation, re-bound to the held card's OWN entities incl. a device ADOPTED TODAY through the rejoin path | **✓ MET** | run `01M1PX64EREVX8XAVACQNZNQGG`, `COMPLETED`, `durationMs 10051`; trigger AND action both on `01M1PRQN03X8H4MNEZQ62F76F1` — the S31 adopted 17:51:15.518Z via `source=rejoin`; causal-chain `outcome: **CONFIRMED**` |
**AND CRITERION 0 — the F-R4-1 `0x0061` hop's first real-silicon ⏺ — MET, on BOTH arms: the hit (`rejoin_candidate … 0x00124B002FA8D1C5 … source=unknown_sender`, 17:51:15.203Z) and the miss (`lookup_eui64_failed: nwk=0x15ac status=0x1`, 18:28:41.461Z).**

## §9 Deviations ledger + THE FINDINGS CARD FOR THE HUB
- Deviations (tier · block · what · why):
- Findings (what the day taught: the rejoin path · the 0x0061 surface · the window timing · the re-bind ergonomics · three packet changes):

- **D-1 · T1 · §2 digest block · 16:36:52Z** — the packet's §2 digest block carries `# WHERE: the bench card (ssh pi)` as a comment only; it was pasted into the desktop Git Bash and returned a half-error / half-plausible result off a stale 07-30 desktop `~/hs-bench/bundles/`. **Fix applied:** re-issued the identical two measurements with `hostname` prepended as the first command, so the host is on the ⏺ line itself (the §2 held-card block's own "first line must print hs-fresh" pattern, applied to the bench block). Nothing measured or asserted was changed. **Why:** playbook §8(2) — a WHERE-label that is not itself executable is lost to the clipboard; this is its second recorded firing.

- **D-2 · T1 · §2 boot glance, token 3 · 16:47:52Z** — `dpkg-query -W -f "${Version}\n" homesynapse` is inside a single-quoted ssh argument, so `${Version}` reaches the REMOTE shell still inside DOUBLE quotes and the remote shell expands it to empty; the command degenerates to `dpkg-query -W -f '\n' homesynapse` and prints a bare newline. Not a rig fact: the package is provably installed (`systemctl is-active` = `active`, and the adapter's own `network_resumed` line is in the journal). **Fix applied:** re-read the version with `dpkg-query -W homesynapse` (no format string, no `$` to expand) plus `/opt/homesynapse/VERSION` as an independent second surface, and folded in `date "+%Z %z"` (Pi-TZ calibration — every timestamp correlation today depends on it) and invocation-scoped `network_formed`/`network_resumed` COUNTS (the `network_formed` fence is hard; `tail -2` shows presence, a count proves absence). All read-only. Nothing measured or asserted was weakened. **Class:** the same nested-quote defect will bite any future packet that puts a `dpkg-query -f` format string inside a single-quoted ssh argument — recommend the packet standardise on `dpkg-query -W <pkg>`.

- **D-3 · T1 (on T2 evidence) · §3 · §6 step 0a · §6-F · §7 · 17:03Z** — the packet addresses the config tree at `/etc/homesynapse/config/`; that directory does not exist on this card (sudo-confirmed ENOENT). **Fix applied:** every config path in the remainder of the packet is read as `/var/lib/homesynapse/config/…` (the unit's `HOMESYNAPSE_HOME`; fingerprint-confirmed by R-4's own 1208 b / 299 b file sizes). Nothing measured or asserted changed — the same two files, at their real location. **Why it was not applied blind:** R-4's D-f quoted `cp: cannot stat` without its errno, and an unprivileged probe returns `Permission denied` for both a missing child and an untraversable parent; two read-only sudo probes were spent to make the correction evidence-backed rather than inherited. **Recommend to the hub:** the R-4b packet's §3/§6/§7 paths were never re-derived against R-4's own D-f — this is the packet's fourth instrument defect and the only one that would have written to a file the service does not read.

- **D-4 · T1 (on T2 evidence) · §4 block 1, and every desktop→card hop after it · 17:16Z** — `hs-fresh.local` resolved for one `ssh` and failed for the `scp` issued seconds later in the same `&&` chain (`Could not resolve hostname … Name or service not known`). **Fix applied:** all desktop→card hops are pinned to the measured address `nick@192.168.1.80` with `-o StrictHostKeyChecking=accept-new` (the IP is a new host-key alias for a host already trusted by name; a CHANGED key is still refused), and `hostname` is prepended to the first hop so a DHCP reassignment cannot silently redirect the block. Nothing measured or asserted changed. **Why it matters beyond convenience:** §4's copy-and-verify is the one chain where a mid-chain transport failure could leave a partially-written `.deb` on the card that a later glob would still match; removing the resolver from the path removes that failure mode before the install rather than after it. **Recommend to the hub:** operator packets that cross the desktop→card boundary should pin an address measured at §2, not an mDNS name.

- **D-5 · T1 · §4 integrity-gate block · 17:21Z** — appended `sudo cat -n /var/lib/homesynapse/config/homesynapse.yaml` (read-only) to the gate block. **Why:** it captures `bench-hero`'s exact bytes and its six `entity_ref` line numbers BEFORE the install, so (a) §7's edit can be specified line-by-line while unhurried instead of improvised under the ≥45-min clock, and (b) a post-install re-read proves the `.deb` left the operator's automation file untouched. Nothing measured or asserted was changed; the gate's own two assertions (ROWS-pre, `integrity_check`) ran first and unmodified.

- **D-6 · T1 · §5 measured boot · 17:26Z** — the packet asserts "exactly ONE `integration_schema_registered`" and "ZERO `network_formed`" but reads both with `head -4`, which can show presence and can prove neither uniqueness nor absence. **Fix:** both converted to `grep -c` COUNTS; the line display retained at `head -6`; the post-install config-tree listing appended for the O-1 re-check. Read-only; nothing weakened. **Class:** an assertion of absence or uniqueness requires a count, never a head/tail — this defect recurred THREE times today (§5 ×2, and my own §6-viii `tail -20`).
- **D-7 · T1 · §6 step 0a · 17:37Z** — the packet's `sed -i '1a permit_join_duration: 254'` has no idempotency guard; a double paste inserts a duplicate YAML key. **Fix:** wrapped in the playbook's own active-line grep guard (`grep -qE '^[[:space:]]*permit_join_duration:'`) with an explicit `GUARD:` message, plus a full `cat -n` read-back instead of `head -4`. Nothing measured changed; the key landed on line 2 exactly as specified.
- **D-8 · T1 · §6 the arm · 17:45Z / 18:25Z** — the packet says "watch the clock; at a minute ≡ 0 mod 5 and :20–:40 s, restart", i.e. it puts an unbounded human paste latency inside a ±10 s requirement, on the single least-repeatable measurement of the day. **Fix:** the block computes the next lawful boundary ITSELF, waits for it to the second, counts the last 15 s down aloud, then fires the restart and issues the provocations as bell-terminated banner prompts on its own schedule, harvesting itself at close+30 s. **First attempt failed for exactly the reason the fix addresses** — a silent 2-minute block with no countdown lost the operator's attention and the run was void. The second design (operator pastes when ready; the block picks the boundary) worked first time and produced criterion 0. **Recommend the hub adopt the self-timing block as the standing pattern for every windowed provocation.**
- **D-9 · T1 · §7 token block · 18:08Z** — R-4's instrument defect (iii) is only HALF fixed in this packet. R-4 found the extraction regex class `[A-Za-z0-9+/=_-]` contains `-`, so `tail -1` selects the helper's 64-dash rule; the packet corrected the length GATE to `-ge 40` but left the extraction untouched — and 64 dashes is also ≥ 40, so `TOKLEN-OK` would have printed and the curl would have 403'd exactly as it did at R-4. **Fix:** R-4's actual recommendation applied — read the token from `/var/lib/homesynapse/config/initial_api_token`, print only its LENGTH. Result: `token_len=43`, `http=200` on every call. No token value entered the record at any point.
- **D-10 · operator-proposed, navigator-approved · §7-A · 18:25Z** — a second permit-join window, with the Hue lamp powered THROUGH the adopted S31 so the bulb's cold-boot could be fired at a known second inside the window. Approved rather than escalated because the packet's own provocation 3 orders a Hue wall power-cycle and §E names "a second window" among the branches the packet contains — this is the packet's own act performed with a better switch. Fence stated and honoured: exactly ONE Hue power cycle. **Outcome: the day's second headline (the `lookup_eui64_failed status=0x1` miss arm) plus a decisive negative on the Hue.** Full result in §7-A.
- **D-11 · T1 · §7 the re-bind · 18:56Z** — the packet specifies `sudo nano` for an edit touching SIX `entity_ref` sites plus a trigger attribute plus a five-action replacement. **Fix:** a single deterministic `printf | sudo tee` write of the whole 17-line file, ownership/mode re-asserted, followed by a numbered `cat -n` read-back, with the original preserved at `/root/r4b-history/homesynapse.yaml.pre-rebind` (1208 b) first. **Why:** playbook §8 rules interactive editors and multi-line pastes dead as an operator interface, and a nano session leaves no auditable artifact — a written-then-read-back file is evidence the hub can check at the bytes. The vocabulary written was verified at source first (§7-iii).


### ★ P-1 — THE POWER-HARNESS PRIMITIVE (operator-originated, 2026-09-04; Nick's, and he asked for it recorded in full)
**The observation, in one line: an adopted, commandable, self-confirming smart plug is not just a device under test — it is a software-addressable mains power switch, and therefore a test instrument.** Anything mains-powered plugged into it becomes power-cyclable *on command, at a known instant, inside a chosen window*, with the plug's own state report standing as the in-band, timestamped proof that power actually changed.

**Why it matters here, concretely.** Every provocation failure in the R-3a → R-4 → R-4b arc failed on TIMING, not on physics: a human power-cycle that landed outside the window (R-4 D-g), or that did not happen because the device was already on (R-4b ACT 3, first run). §7-A removed the human from the timing loop and the very next attempt produced a decisive answer about the Hue after three inconclusive ones. The harness converts "we could not tell whether the device is silent or the method was wrong" into "the device is silent."

**What it buys, generalised (this is the part to design from):**
1. **Repeatability.** The same power transition at the same offset from window-open, every run, so results are comparable ACROSS devices and across sessions instead of being one-off anecdotes.
2. **In-band ground truth.** The harness plug's own `state_reported` lands in the SAME event store as the device-under-test's response (or silence). "Power was applied at T" stops being an operator's wall-clock note — the discriminator and the stimulus share one timeline, which is exactly what playbook §4 asks of every closure.
3. **Protocol independence — the strongest property.** The harness acts on POWER, not on a protocol. The plug is Zigbee; the device under test can be Wi-Fi, Matter, Thread, Z-Wave, or a vendor cloud box. A Zigbee-adopted plug can therefore instrument integrations this project has not written yet. That is Nick's "in or perhaps not in the same class of integration/protocol" point and it is the reason this belongs in the platform rather than in a runbook.
4. **Scale and matrix sweeps.** N harness plugs = N independently addressable channels. A device-class matrix (mains router · router-parented sleepy · self-powered sensor · actuator) can be swept in one sitting rather than one device per session.
5. **Cold-boot behaviours become testable at all.** Announce-on-power-up, rejoin-on-power-up, boot-time reporting posture, availability transitions, watchdog re-arm, restart-storm behaviour — all of these need a power event, and until now the only power event available was a human at a wall switch.
6. **Regression value.** Once a device class's cold-boot signature is captured, the harness can re-fire it on every artifact — the same class of coverage the nightly gives software, extended to silicon behaviour.

**What it needs to become a real capability (the honest build list):**
- A **reserved role**: a "power-harness" plug is declared as such and is never also a device under test in the same leg — today's run used the same S31 as harness AND as trigger source, which is fine but must be a named, deliberate configuration rather than an accident.
- A **bench verb**: something of the shape `harness cycle <plug> --at <offset-from-window-open>` so a scenario can open a window and fire power at t+N without an operator present.
- **Per-profile safety limits, enforced in code, not in a runbook.** Some devices read N rapid cycles as a factory reset — the Hue LCA017's 6× dance is precisely this hazard, and a harness that can cycle power is a harness that can silently factory-reset an expensive bulb. Every profile needs `maxCyclesPerWindow` and `minSecondsBetweenCycles`, and the harness must refuse to exceed them.
- **Load limits.** Never harness anything above the plug's electrical rating; never harness a load that must not lose power (today's charger was moved deliberately, and the operator was asked before the first press).
- **Settle time in every sequence.** A device mid-boot does not accept commands. Any leg that powers a device and then commands it must wait for the device's own readiness signal, not a fixed sleep — this is what would have bitten a Path A run today had the Hue adopted.
- **An explicit limit on what it proves.** The harness proves POWER WAS APPLIED. It does not prove the device booted, joined, or is healthy. The harness's state report is the stimulus record; the device's response is still the measurement.

**Why the hub should care beyond the bench:** the stated long-term objective is a system that survives contact with other people's fleets — many vendors, many classes, many protocols, most of them devices this team will never own. A power harness is the cheapest general way to reproduce the ONE event class that every smart device in the world shares regardless of protocol: losing power and coming back. Building a device dossier that is honest about cold-boot behaviour is otherwise a manual, unrepeatable, operator-bound activity — which is exactly what the last three bench sessions demonstrate. **Recommended as a charter candidate in its own right, not folded in as a runbook note.**

- **D-12 · T2→T1 · §7 the rendered explanation · 20:05Z** — the packet names `GET /api/v1/runs/<id>` as the fallback "rendered explanation of record". **That route does not exist**; it returns `http=404` with "Endpoint GET … not found". This is the playbook's F-1/F-5 class verbatim (`$(bench.sh api_token)` was never a verb; `/why-not` was never a route) — the instruction's own invention, caught on the bench at operator cost. **Fix:** the route table was read at source (`RestFilters.installRunQueryEndpoints`/`installAutomationQueryEndpoints`) rather than guessed a second time, and the real endpoint **`GET /api/v1/runs/{runId}/causal-chain`** was called — which is strictly better, being the causal-chain tree the dashboard's explain hero itself renders. **Recommend to the hub: the four registered read routes are `GET /api/v1/runs`, `GET /api/v1/runs/{runId}/causal-chain`, `GET /api/v1/automations`, `GET /api/v1/automations/{id}/non-firing`; any future packet naming a fifth is inventing it.**

- **D-13 · T1 · §9 the clean stop · 20:25Z** — the packet puts the stop-GRADE read and `sudo shutdown -h now` in one block; if the shutdown races the read, ssh drops and the O-2 evidence is lost for the session. **Fix:** split into two blocks — the grade gets its own paste, the shutdown follows (playbook §8(1): a gate that shares a block with the act it gates WILL be overrun). Nothing measured changed.


### §9-RESTORE (the bench night) — part 1: the floor is UP
Held card halted cleanly (`shutdown -h now` → `Connection reset by peer`, the halt). Rig restored by the operator to its pre-session configuration: **laptop charger back in the S31 (relay off), Hue lamp back on its own wall outlet (switched off)** — so tonight's nightly runs against the same physical load as the 09-03/09-04 nights and the `8/9 PASS` baseline stays comparable. Bench card `hs-dev-1` booted, `up 1 min` @ 20:31:07Z.
**⏺ FLOOR START — MET @ 20:34:19Z (16:34:19 ET):**
```
hs-dev-1
BENCH=/home/homesynapse/bench.sh
lrwxrwxrwx 1 homesynapse homesynapse 45 Jul 13 21:32 /home/homesynapse/bench.sh -> /home/homesynapse/nexsys-bench/tools/bench.sh
  [!!] NOT running
  [OK] launched pid 2185 -> /home/homesynapse/hs-bench/bench-2026-09-04-163358.log
  [--] waiting for a decisive radio state (up to 90 s)...
  [OK] RADIO UP after 22s
  [OK] running (pid 2185)
16:34:11.596 registry.projection_live: devices=6 entities=6 position=25065
16:34:12.185-.188 zigbee.device_relinked ×6: 0x00178801101A09BB→01KX1PA4GRZHY2GD37B5CFVQHY · 0x449FDAFFFE688F57→01KY12MQVQ204M1VP39F1ZDM33 · 0xF044D3FFFE9C78D7→01KX1PB9A5931A8G0F0X03QXT2 · 0x00124B002FA8D1C5→01KXW1W1RR66GV98D9QDPB4VXY · 0xF044D3FFFE1C1E8E→01KXW13WEGRCT5C0XSQT8WZBG9 · 0xF044D3FFFED2A201→01KXW0156Z1GJ3WCV2G516AKWS
16:34:12.189 zigbee.adoption_maps_rehydrated: devices=6
16:34:19.899 zigbee.network_resumed: channel=20 panId=0x774c
16:34:19.899 zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---   (EMPTY)
```
NOT running → started (pid 2185) → **RADIO UP after 22 s** → running ✓ · **`network_resumed: channel=20 panId=0x774c` — PAN UNCHANGED after a day of held-card work on the same coordinator** ✓ · failure-token section EMPTY ✓.
**⏺ THE `~/bench.sh` PATH TENSION IS RESOLVED, NOT ARBITRATED:** `~/bench.sh` is a SYMLINK (Jul 13) to `~/nexsys-bench/tools/bench.sh`. The packet's spelling and the playbook's F-11 "invocation of record" are the same file — neither is wrong on this card. Recommend the playbook note the symlink so the rule stops reading as a contradiction.
**⏺ R-4's ASK #4 IS ANSWERED: `zigbee.adoption_maps_rehydrated: devices=6` DOES appear** — R-4 asked "whether `adoption_maps_rehydrated` appears there at all". It does, on the bench card, immediately after the six `device_relinked` lines. (It was not grepped on the held card today; a held-card read would have shown `devices=2` pre-session and `devices=3` after the adoption. Small gap, cheap to close next sitting.)
**⏺ F-R4-2 IS NOW VISIBLE IN FULL, FROM BOTH SIDES.** The bench card carries **six** devices / **six** entities (`position=25065`); the held card carried **two**, and three after today. Both cards share ONE physical fleet and ONE Zigbee custody (channel 20 / PAN 0x774c) but hold DIVERGENT registries — exactly R-4's F-R4-2, now quantified 6-vs-3. The device ids also settle the `bench-hero` ref question: the bench card's Hue deviceId `01KX1PA4GRZHY2GD37B5CFVQHY` and SNZB-03P deviceId `01KX1PB9A5931A8G0F0X03QXT2` sit in the same ULID millisecond bands as `bench-hero`'s configured entity refs `01KX1PA4HSJ581GASYB7DHE40F` (light) and `01KX1PB9AAB4VB3E10BD477TV3` (motion) — device and entity minted together, on the BENCH card. `bench-hero` as shipped is a bench-card automation; today's Path-B re-bind is the held card's own.
**⏺ REFINEMENT TO F-R4b-G (the Hue), appended not rewritten:** the bench card DOES relink `0x00178801101A09BB` on boot — so the bulb is ADOPTED IN THE BENCH REGISTRY. But `device_relinked` is a registry rehydration from persisted state ("re-pairing, no new adoption"), not device contact, and both nightlies still report `1 SKIP(hue-online)`. The honest statement is therefore: **the Hue is adopted in the registry and ABSENT FROM THE AIR** — it did not answer on the held card under ideal conditions today, and it does not answer on the bench card's nightly. That is a stronger and more precise finding than "not a member", and it still contradicts playbook §6's "power-cycle ⇒ re-announce" as a *verified* behavior.


### §9-RESTORE part 2 — ★ THE FLOOR IS GREEN. `[PASS] boot-health — 6/6 positive · 0 forbidden` ★
⏺ verbatim @ 20:38:21Z (16:38:21 ET), runner `B3.1-2026-08-02-postwindow @ 16e672d`:
```
  [--] stimulus bench: restart → [OK] stopped → [OK] launched pid 2354 → [OK] RADIO UP after 13s
    [ok] log 'registry.projection_live: devices=6 entities=6' min=25065 — 16:38:12.418 … position=25065 (within 90s)
    [ok] log 'zigbee.adoption_maps_rehydrated: devices=6' — 16:38:12.819 (within 90s)
    [ok] log 'zigbee.device_relinked' x2(at-least) — 16:38:12.817 … 0xF044D3FFFE9C78D7 (within 90s)
    [ok] log 'zigbee.network_resumed: channel=20 panId=0x774c' — 16:38:20.533 (within 90s)
    [ok] log 'zigbee.port_identity_captured:' same-line ['pinnedOnly=false'] — 16:38:20.418 … stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false (within 90s)
    [ok] api /api/v1/entities {"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3", "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K", "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX"]} — all asserts satisfied (within 90s)
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260904T203821Z
--- resumed/port tokens ---
16:38:20.418 … zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false
16:38:20.533 … zigbee.network_resumed: channel=20 panId=0x774c
```
**`[PASS] boot-health — 6/6 positive · 0 forbidden` ✓ · `network_resumed: channel=20 panId=0x774c` — PAN UNCHANGED ✓ (a changed PAN was the §9 STOP condition; it did not occur). BUNDLE `boot-health-20260904T203821Z`. §9 CLOSES MET — THE BENCH FLOOR IS GREEN AND THE NIGHTLY WILL FIRE ON AN UNDISTURBED RIG.**
**⏺ THE COORDINATOR IS PROVEN TO BE THE SAME PHYSICAL DONGLE ACROSS BOTH CARDS.** The bench card's `port_identity_captured` `stableId` is `usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0` — **byte-identical to the held card's at §5 (17:22:58Z)**. The "coordinator STAYS in its port" fence held through the swap, and the two cards' identical channel-20/PAN-0x774c resumes are therefore the same radio, not a coincidence of configuration.
**⏺ F-R4-2 IS NOW PROVEN AT THE ENTITY ULID, NOT INFERRED.** The scenario's own API assert lists the bench card's six entity ULIDs and **the first two are `01KX1PA4HSJ581GASYB7DHE40F` and `01KX1PB9AAB4VB3E10BD477TV3` — EXACTLY the two refs `bench-hero` was configured with** (§4-ii, lines 9 and 14/19/25/31/37 of the original `homesynapse.yaml`). **`bench-hero` as shipped is, definitively, a BENCH-CARD automation**: both its refs are live entities there and neither has ever existed on the held card. R-4's C4 was not a defect and not a regression — it was an automation pointed at another machine's registry. Today's Path-B re-bind is the held card's own, and that is why it ran.


### ★ THE FINDINGS CARD FOR THE HUB (the five things the day taught — design from this)
**1 · THE REJOIN PATH WORKS, AND ITS BOUNDARY IS A DEVICE CLASS.** `0x0061` resolved the mains ROUTER (S31 `0xf87d`) and carried it to `device_adopted` in 315 ms with `source=rejoin`. It MISSED the router-parented SLEEPY device (SNZB-02P `0x15ac`, `status=0x1`) — the coordinator's local tables hold its neighbours, not its grandchildren. **F-R4-1 as shipped closes the silent-rejoiner gap for mains routers only.** The ZDO `IEEE_addr_req` WU its own gotchas named is now evidenced, not speculative.
**2 · THE 0x0061 SURFACE IS SOUND.** Bellows-derived constant and layout both confirmed on MG24 silicon; hit and miss logged exactly as specified, on the specified loggers, 1 ms apart; the once-per-nwk-per-epoch dedup held (8 unknown-sender frames → 1 lookup, 1 WARN). Nothing in F-R4-1 needs a constant or layout edit.
**3 · WINDOW TIMING: TAKE IT AWAY FROM THE HUMAN.** 254 s is generous; operator paste latency is unbounded. A hand-timed window was voided by ordinary distraction; the self-timing block (computes the next lawful boundary, counts the last 15 s down, banners each provocation with a bell, harvests itself) produced criterion 0 on its first run. **Also: never pin a second** — the plug's cadence drifted `:54 s` → `:57 s` in five days while minutes ≡ 3 mod 5 held.
**4 · RE-BIND ERGONOMICS: SIX REFS, ONE WRITE, ONE READ-BACK.** `nano` over ssh for six `entity_ref` sites is the wrong instrument and leaves no artifact; `printf | sudo tee` + `cat -n` is deterministic and auditable. **Verify the vocabulary at SOURCE before writing** — `attribute: on`, `turn_off`, and `CONFIRMABLE/5000 ms` were all read out of `StandardCapabilities.java` and `zigbee-profiles.json`, which is why `CONFIRMED` was a prediction rather than a hope. Quote `"on"` in YAML as a standing convention.
**5 · THREE PACKET CHANGES.** (a) **Re-derive paths against the prior record's own deviations** — `/etc/homesynapse/config` does not exist on this rig and §3/§6/§7 all addressed it; this was the one defect that would have edited a file the service never reads. (b) **Never assert absence or uniqueness with `head`/`tail` — use `grep -c`**; that class fired three times today, once by me. (c) **Verify every route and verb at the source table** — `/api/v1/runs/{id}` was invented; the four real read routes are `/runs`, `/runs/{runId}/causal-chain`, `/automations`, `/automations/{id}/non-firing`.

## §10 Hub verdict surface (the hub writes this at intake)

**HUB VERDICT (v62 beat 7, 2026-09-04 ~20:5xZ): ACCEPT — FOUR OF FOUR; CRITERION 0 MET ON BOTH ARMS; C-002 MINTED at `ef02d13` on the measured objects (Path B; `CONFIRMED`); the six-device fleet sentence → the C-003 slot (F-R4-1b + R-4c). Layer 2: every load-bearing ⏺ re-executed against Nick's verbatim terminal paste; the route table (`RestFilters.java:348/:350`) and the 0x0402 profile re-executed at source. Record size ACCEPTED as filed (the cap re-cut to §0 + §9; the drill-down is uncapped). The hub's own packet defects (D-3 the config path · D-6 counts · D-9 the token regex · D-12 the invented route · D-13 the shared block · D-8 the hand-timed window) OWNED; the lessons fold at the v62 close. Findings routed to docket rows 27–33; P-1 accepted as a charter candidate. The audit: `context/audits/2026-09-04_R-4b_intake_two-layer-audit_v62-beat-7.md`.**
