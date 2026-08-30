<!--
file: context/audits/2026-08-30_R3b_unit-loosening_return.md
purpose: R-3b Coder-lane return — the MEASURED serial-coordinator loosening landed in `distribution/systemd/homesynapse.service` (H13: byte-identical to the R-3a §7 drop-in) + the boot-contract-map row. Instruction: context/instructions/2026-08-27_R3b_PKG-E2E-1_unit-loosening_coding-instruction.md. Baseline core `5051fa5`, verified at checkout.
audience: the hub (audit: H13 byte-diff) → Nick (commit + push + the CI read).
status: DELIVERED — 2 M staged, uncommitted, on the coder desk. In-lane gates GREEN (incl. systemd-analyze verify exit 0 via WSL systemd 255). Gate of record: CI on Nick's push.
-->

# R-3b return — the unit loosening (2 M; the measured text shipped verbatim)

## §0 Census — exactly 2 M

Baseline verified at checkout: `git rev-parse HEAD` = `5051fa5a2370f296c123e9f55a71672e7684f1f1`, porcelain EMPTY pre-edit. Post-edit:

```
$ git --no-optional-locks status --porcelain
 M distribution/docs/boot-contract-map.md
 M distribution/systemd/homesynapse.service
```

Modes unchanged (`git diff --raw`: both `:100644 100644`). Endings LF-only preserved (`git ls-files --eol`: `i/lf w/lf` + `eol=lf` attr on both targets, before and after). Zero Java · `distribution/README.md` untouched · CI workflow twins untouched · the DANGER block (`Type=notify`) and the `ExecStartPost` probe line untouched · nothing committed, nothing pushed.

## §1 The seam diff (verbatim) + the H13 byte-diff

The unit diff is EXACTLY the seam hunk — one hunk, nothing else in the file:

```diff
@@ -88,12 +88,20 @@ MemoryDenyWriteExecute=no
 RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6
 SystemCallFilter=@system-service
 SystemCallErrorNumber=EPERM
-# RAMP (post-M9): the Zigbee coordinator is a serial device. PrivateDevices=yes
-# blocks /dev access, so loosen it then and allowlist the coordinator, e.g.:
-#   PrivateDevices=no
-#   DeviceAllow=/dev/ttyUSB0 rw
-#   SupplementaryGroups=dialout
-PrivateDevices=yes
+# Serial coordinator access — MEASURED on the held card (R-3a rehearsal,
+# 2026-08-30, drop-in 10-serial-coordinator.conf; nexsys-hivemind
+# context/audits/2026-08-30_R3a_rehearsal_operator-record.md): the packaged
+# service resumed the six-device network under exactly these lines
+# (`zigbee.network_resumed: channel=20 panId=0x774c`). Class rules
+# (`char-ttyUSB`/`char-ttyACM`, majors 188/166) survive replug renumbering
+# where a node path would not; `DevicePolicy=closed` keeps only the standard
+# pseudo-devices; `SupplementaryGroups=dialout` matches the node's
+# root:dialout 0660.
+PrivateDevices=no
+DevicePolicy=closed
+DeviceAllow=char-ttyUSB rw
+DeviceAllow=char-ttyACM rw
+SupplementaryGroups=dialout
 
 # Journald capture (Console output is plain text per Doc 12 §0.3).
 StandardOutput=journal
```

**H13 byte-diff — three-way, all identical.** Extraction was content-anchored, not retyped: the record's §7 block via `awk '/THE MEASURED TEXT/{f=1} f&&/^```ini$/{g=1;next} g&&/^```$/{exit} g{print}'` (first block after the §7 heading), the shipped lines via `sed -n '/^PrivateDevices=no$/,/^SupplementaryGroups=dialout$/p'` on the edited unit, the instruction's stamped block via `awk '/^# MEASURED-TEXT/...'`.

```
== diff record-§7-body vs shipped ==      (empty)   diff exit: 0
== diff instruction-stamp vs shipped ==   (empty)   diff exit: 0
== cmp record-§7-body vs shipped ==       cmp: byte-identical
```

Comparison basis, stated: the record's §7 drop-in text is `[Service]` + the five directive lines; the `[Service]` header is positional (the standalone drop-in file needed its own section header) and is correctly ABSENT from the shipped hunk — the five lines land inside the unit's existing `[Service]` section at the exact seam where `PrivateDevices=yes` stood, in the drop-in's exact order. The five directives are byte-identical to both the record and the stamp.

## §2 The docs row (verbatim)

`distribution/docs/boot-contract-map.md` — one new minimal section (heading + one `| Decision | Value | Source |` row, the file's row idiom), placed after "Network surface" / before "First-run pairing token". No hardening table existed in the file, so "ONE row" required a minimal host heading — disclosed as a placement choice for the diff review:

```markdown
## Serial coordinator access — the measured device posture

| Decision | Value | Source |
|---|---|---|
| Serial-device posture (Zigbee coordinator) | class-based `DeviceAllow=char-ttyUSB rw` + `DeviceAllow=char-ttyACM rw` (majors 188/166 — class rules survive replug renumbering where a node path would not) + `SupplementaryGroups=dialout` + `PrivateDevices=no` / `DevicePolicy=closed`, measured R-3a 2026-08-30 (`zigbee.network_resumed: channel=20 panId=0x774c` on the held card). What STAYS hardened: `ProtectSystem=strict`, `PrivateTmp=yes`, the syscall filter (`SystemCallFilter=@system-service` / `SystemCallErrorNumber=EPERM`), `RestrictAddressFamilies` — all unchanged. | the provenance comment above the device lines in `distribution/systemd/homesynapse.service`; measurement: nexsys-hivemind `context/audits/2026-08-30_R3a_rehearsal_operator-record.md` §7/§9 |
```

(The `integration/integration-zigbee/MODULE_CONTEXT.md` gotcha row is the HUB's own fold at intake per the instruction — not in this census.)

## §3 Gates — run / flagged

- **`systemd-analyze verify` — RUN, exit 0** (WSL, systemd 255 / 255.4-1ubuntu8.14). First attempt against the `/mnt/c` (9p) path failed environmentally before parsing (`Couldn't process aliases: No such file or directory`, exit 1); rerun after `cp` to native `/tmp` inside WSL: **exit 0**, ZERO unknown-key/parse complaints on the five new directives. Only environmental messages remained, both expected on the desk: `is marked executable` (the NTFS→WSL copy gains +x; the repo file is 0644 in the index and `build-deb.sh` pins 0644 in-package) and 2× `Command /opt/homesynapse/... is not executable: No such file or directory` (no image installed in WSL).
- **H13 byte-diff — GREEN** (§1: two diffs empty, cmp byte-identical).
- **Porcelain — exactly 2 M** (§0).
- **WU-R3 launch-column re-verifications:** P1 seam re-read at `5051fa5` — RAMP comment `:91–:95`, `PrivateDevices=yes` `:96`, DANGER block `:103+`, no `DeviceAllow`/`DevicePolicy`/`SupplementaryGroups` anywhere pre-edit — all as pinned. P4 fourteen-token re-grep under `integration/integration-zigbee/src/main/java` — **14/14 present** (`network_resumed` 1 · `network_formed` 2 · `network_parameter_mismatch` 3 · `port_identity_captured` 2 · `device_cache_loaded` 1 · `adopt_list_loaded` 1 · `adoption_maps_rehydrated` 1 · `device_relinked` 1 · `device_proposed` 1 · `proposal_accepted` 1 · `device_adopted` 1 · `device_announce` 1 · `transport_unbound` 2 · `transport_failed` 1). P7 re-read: `build-deb.sh:49` copies the repo unit verbatim — one copy, no second edit site.
- **Red-first accounting (#18), disclosed not simulated:** no fixture can red at HEAD for a unit-file change. The red leg is the rehearsal's own RED arms: **E3-RED fired and PASSED on hardware** (artifact absent at `7c9e4fa`: 90 s → `TIMEOUT`, `ExecMainStatus=143`, `Failed to start`, restart loop; same card at `dec35be`: 4 s → `active`). **P-b and P-c did NOT fire** — §9 resolved **P-a on first measurement** (no `transport_unbound`, no `EPERM`/`Permission denied`), so no forced additions ride the shipped text.
- **`systemctl show` caveat carried forward:** on a live host the merged view will also show `DeviceAllow=char-rtc r` — systemd's own implied rule from the base unit's clock protection (`ProtectClock=yes`), NOT ours, benign (R-3a §7 [AMEND]). Verify effective config with `systemctl show --no-pager`, never `cat` alone.
- **Gate of record — CI on Nick's push** (`distribution/**` triggers install-smoke). H12 predictions as filed in the instruction: `CI / Build & Check` GREEN · install-smoke BOTH legs GREEN — the loosened lines are inert on runners with no serial device (run-smoke 18/18, update-smoke zero-loss, the rig's 34 checks) · the echo step prints `hs_version=0.1.0+git<push-commit-UTC-date>.g<sha>` · **the arm64 leg's `version-grammar echo green: … sha256 …` line is R-4's origin hash** (hub pins it into the R-4 packet) · zero Node-20 annotations.

## §4 Pushback / disclosures

1. **Stale record pointer in the instruction (one day), resolved in favor of the stamp + disk — flagged, nothing shipped against it.** The instruction's status line and §1 name `context/audits/2026-08-29_R3a_rehearsal_operator-record.md`; no such file exists. The record on disk is `2026-08-30_R3a_rehearsal_operator-record.md` (the run was DEFERRED from Sat 08-29 per the record's own frontmatter; the 08-29 file is the DEFERRED desk-audit return). The §2 stamped provenance comment already cites the 08-30 path and date, so the shipped bytes are correct and internally consistent; only the instruction's read-pointers lag the deferral (authored AHEAD at v57 beat 3).
2. **Measured-text source check — nothing seems wrong at the source.** Comment claims cross-verified against the record: major 188 observed live on both cards (`crw-rw---- root dialout 188, 0` — also = root:dialout 0660, §2/§8); channel 20 / panId 0x774c observed at §9. One honesty note: major **166** (ttyACM) is the standard class constant, not observed on-card — the dongle enumerates as ttyUSB; the ttyACM rule is deliberate breadth from the measured drop-in itself.
3. **Adjacent-not-mine, so its absence isn't a miss:** R-3a finding §6-B (graceful stop exits 143 → unit `failed`) recommends the app-side exit-0 root fix and explicitly disfavors a unit-side `SuccessExitStatus=143` (it would mask a genuine SIGTERM kill). No unit line shipped for it; candidate WU home per the record is PKG-SEC-1's neighbourhood.
4. Rendering choice, disclosed: the §2(a) provenance comment ships byte-verbatim as quoted in the instruction (backticks included), wrapped across `#` lines at the file's ~80-col comment width — wrapping is the only transformation.

## Harvest (≤ 3)

- `systemd-analyze verify` fails environmentally on `/mnt/c` (9p) paths (`Couldn't process aliases`, exit 1) BEFORE parsing; `cp` the unit to a native WSL path first — then it parses (exit 0) and only missing-binary noise remains. Addendum to the desk's WSL facts.
- For H13 byte-diffs against a living record, extract content-anchored (awk: heading → first fence), never by line number — the 1666-line record repeats the drop-in text in its verbatim appendix; and state the comparison basis explicitly when a drop-in's `[Service]` header is positional rather than shipped.
- A "ONE row" docs delta into a file with no matching table needs a minimal host heading in the file's own idiom — decide it, ship it single-hunk, and disclose the placement in the return rather than forcing the row into a wrong-subject table.
