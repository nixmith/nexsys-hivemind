<!--
file: context/audits/2026-10-17_v112-b5_PI-2_section-B_inventory.md
purpose: the hub-side inventory for PI-2's §B DRAFT-3 (read-only at hivemind `f9ab3ed`, bench `7e03c81`, core `176adad`): DRAFT-2's blocks as they stand, what changes for LIVE, the blockers, a proposed block list in two sittings (A: the SSD, no radio · B: the MG21), the risks — the input v113 cuts DRAFT-3 from.
audience: v113 (DRAFT-3's cut) · DRAFT-3's independent check · Nick (the rulings X1 · R2 · R4 when DRAFT-3 asks them)
state-type: audit input (a hub-side inventory; every row cites file:line)
status: FILED v112 b5 (Sat 2026-10-17) — drafted by a hub-side helper; the hub re-read R1 at the bytes (`NetworkFormation.java:281–298` and `Main.java:104` at `176adad` → IR-222) and the `.deb`'s 7-day artifact retention (`.github/workflows/install-smoke.yml:167`, on every push to `main` and on `workflow_dispatch`); every other row is DRAFT-3's to re-read at the block that uses it
-->
# PI-2 §B -> LIVE: inventory (2026-10-17)

**Keys** (hivemind `context/`): U instructions/2026-10-12_unit-cards_…_drafts.md; PF instructions/2026-10-07_…PKG-FRESH-1_…; C9 instructions/2026-10-10_…BENCH-CORE-9_…; C10 instructions/2026-10-15_…BENCH-CORE-10_…; A9 audits/2026-10-11_BC9-REHEARSAL-3_intake-audit.md; R111/R112 planning/2026-10-14_v111_, 2026-10-16_v112_decision-record.md; J2 pre-verifications/archive/WU-J2_…IR-114.md; HZ planning/2026-10-02_v93_THE-HORIZON_…; ZY audits/2026-09-25_THURSDAY-ORDER_capture/run2/zigbee.yaml.after-T3. B4 `_scratch/v112/b4/b4_frag.md` (UNLANDED). Core: ZA ZigbeeIntegrationAdapter; NF NetworkFormation; PS PersistentNetworkParameterStore; EP EzspCoordinatorProtocol; ZS ZigbeeAdoptionSlice; JS JSerialCommByteChannel; EC/SV ExceptionClassifier/StandardIntegrationSupervisor; MN Main.java; UNIT distribution/systemd/homesynapse.service; ENV …/homesynapse.env.example; CS distribution/common.sh; PI deb/debian/postinst; BI image/build-image.sh; SM .github/workflows/install-smoke.yml. Bench: BS tools/bench.sh; BT tools/runner/boot_timing.py; MG24 corpus/coordinators/sonoff-dongle-plus-mg24_efr32mg24_ezsp.md.

**Read first:** R1, X2, X3, X5, X6; X1 is the hub's ruling.

## 1 §B DRAFT-2 as it stands
- B.0: B.1 U:73 PI-2 runs the package, hs-dev-1 keeps bench-boot; B.2 U:74 `KIT-STORAGE: a` (SSD Kit 256 GB); first boot = RUNTIME-1's point; B.3 U:75 online-backup copy, md5 on both COPIES; file-sink readers; postinst start FENCED by mask; evidence `registry.projection_rebuilt: … skipped=0`; B.4 U:76 Tue Oct 20 or next evening, <= 2 h, rig dongle NEVER in PI-2, hostnames; B.5 U:77 only the one read-only backup touches hs-dev-1; a failure leaves PI-2 off.
- BLOCK 0 U:81 Imager -> SSD, `hs-pi2`, key, Tailscale, BOOT_ORDER=0xf416; EXPECTED `hs-pi2 · nvme0n1 238G / (the SSD root) · Raspberry Pi 5 · the RAM line`; BLOCK 1 U:82 one-step backup + `cp -a ~/hs-bench/config` on hs-dev-1, the .db to hs-pi2:/tmp, md5 = md5-pi; BLOCK 2 U:83 mask, `apt install`, `masked` + no process, install store/config; BLOCK 3 U:84 append: drop-in, daemon-reload, unmask, start, BT/RSS/replay; BLOCK 4 U:85 readers; rows=10 all UNAVAILABLE; BLOCK 5 U:86 PI-2 off, copy (~1.2 GB) kept; one line U:88 (path still `_scratch/v111/pi2/`).
- B.6 U:91 `KIT-DONGLE: both` RULED; MG21 first pairing = corpus entry; first boot NO radio, `integration.failed` EXPECTED; probe U:92 `protocol 13` PASS / `protocol 14` STOP+label; reflash only with a named file ("on the desk VM": superseded); B.7 U:94 desk: tool + `.gbl` + sha256 in `_scratch/kit/`; flash on PI-2 only; flags from `--help`; `FLASHER:`; §C U:98-99 LIVE after the stub-ssh dry-run; not after 21:30.

## 2 What changes for LIVE
- **X1 Fold.** D-v112-18 (R112:131) rehearses "the fresh image and the timed `apt install`" on PI-2's first radio-less boot. PF times apt -> postinst start -> 200 on an EMPTY store (PF:56-67; P1 PF:136, 1800 s); the mask (U:83) makes PI print `HomeSynapse Core was installed but did not start cleanly.` (PI:60). Arms: (a) mask; record apt time and unmask->200 (not row 34's measure); (b) PF B2-B3 as shipped (empty config: `zigbee.transport_unbound` PERMANENT, ZA:1058-1063, no radio), stop, rename the empty store aside, restore. Image: PF pins Bookworm (PF:23, :47), hs-dev-1 is Debian 13 (MG24:68) - RECORD `PRETTY_NAME`. Nick: "PI-2 boots an image nobody rehearsed" (R111:142).
- **X2 Paths.** UNIT:41 HOMESYNAPSE_HOME=/var/lib/homesynapse: store `data/homesynapse-events.db` (MN:88; CS:34), config + token `config/` (MN:87; CS:33, :35); the store's payload keys live in config (MN:287-288). U:83 writes `/var/lib/homesynapse/homesynapse-events.db` and `/etc/homesynapse/`, U:85 reads the token there: all miss (= B.3(3)'s empty-store boot). U:82 sends only the .db: config transfer UNKNOWN.
- **X3 Dead instruments.** `pgrep -f homesynapse-app` (U:83 fence, :84 RSS): the JVM is `…/java <CS:114> -cp /opt/homesynapse/lib/* com.homesynapse.app.Main` (BI:40, :155-160): it matches no JVM (at most its own `bash -c`); key on the class (BS:10). `journalctl -u homesynapse` (U:85; PF:69-81) loses app lines under the append: drop-in (U:84 over UNIT:113-115). BT reads a file's FIRST boot (BT:2-8, :24-36); the sink appends: mark bytes (C9:37).
- **X4 Artifact.** 176adad's .deb. CI keeps 7 days (SM:167); 176adad committed 2026-10-12 09:30 -0500: if run that day, gone ~Oct 19 (derived; run date UNKNOWN). Re-mint `workflow_dispatch` (SM:25; PF:17); form PF:16-20.
- **X5 LAN opt-in.** No Java reads `HOMESYNAPSE_BIND_HOST` at 176adad: ENV:19-25 "inert"; README.md:257-261; MN:127 -> HomeSynapseConfig.java:89-94 (loopback, 7070). PF:99's `listen: 0.0.0.0:7070` cannot hold; DIST-CENSUS misread them (audits/2026-10-07_v99_…:24, :33). Keep C1 (PF:88) as P4's finding; C2 = a restart for a known negative. Fix = Core E2 (distribution/docs/escalations.md:28), Java after the freeze.
- **X6 B.6's line.** ZY:1 `serial_port: /dev/zigbee` = hs-dev-1's udev symlink (audits/2026-08-30_R3a_…:559), absent on PI-2. A configured port is authoritative (ZA:1050-1056); the failed open throws TransportFailureException (JS:57-59; RuntimeException, TransportFailureException.java:21) -> TRANSIENT (EC:66-67) -> backoff restarts (SV:677-681) to the intensity limit. Immediate `integration.failed` is the unset-port arm (ZA:1058-1063; SV:663-675, :886). EXPECTED: UNKNOWN (SV's restart lines). U:91's CONFIG-ERROR-1 premise holds (audits/2026-10-09_v101-b7_…:24-25).
- **X7 Probe/flash** (U:92, :94; R111:234). Band v13 only (EP:78, :87); >13 `zigbee.ezsp_version_unsupported` PERMANENT (EP:556-566); 8-12 WARN `zigbee.ezsp_legacy_version` (EP:76, :574): no <13 arm in the record. Baud fixed 115200 (JS:34). U:92's PASS names 7.4.5.0 (the MG24's). Precedent flasher 1.1.0 (MG24:41). `_scratch/kit/` absent: B.7 not run. PI-2 install: only `pipx install universal-silabs-flasher` named (U:94); pipx, network UNKNOWN.
- **X8 Corpus** `corpus/coordinators/sonoff-zbdongle-e_efr32mg21_ezsp.md`, MG24's form (U:91; R111:234). U:91's "B.5" is HZ:43's B5 (6/6 on the air before hand-over), not §B.0's; boot-health is not on hs-pi2 (U:85). Folder: MG24 file only. Fields MG24:18-41, :65-69. Commands UNKNOWN (nearest PF:46, :116).
- **X9 BC9b scoped admit** (D-v112-22, B4:66, UNLANDED; R112:115 and audits/2026-10-17_v112-b3_BC10_…:43 still say Sunday). Device SNZB-03P `0xF044D3FFFE11B08F`: unjoined, unadopted, in its box (A9:67). EXPECT verbatim: "the scoped admit (EXPECT device_join … USE_PRECONFIGURED_KEY → device_announce → device_proposed) and, on the next boot, P4 (J2a's boot-listed interview of the unadopted device)" (A9:55); B4:66 repeats it. Open: C9:38-39 and C9:43, new scope, token CS:35 (the zigbee id is derived: BS:80-86). RECORD not STOP: `key_establishment_failed` WARN + `transient_key_expired` INFO (A9:64). STOP: "`decision=DENY_JOIN` for the SENSOR" (C9:58). Gesture "the 5-s hold at open" (A9:41). Order: NOT listed at the admit - a listed device is adopted at once (ZA:1613-1623) and J2a skips it (ZA:1793).
- **X10 J2a.** P4 verbatim: "a boot with the SNZB-06P24 cached, unadopted and LISTED reads `zigbee.device_proposed … source=boot_listed` within the interview timeout when the device is awake, and `rejoin_candidate`-class retries when it is not; no `device_proposed` on a boot where the device is already adopted" (J2:50; now the SNZB-03P). Code: `zigbee.boot_listed_candidate: device={} nwk=0x{}` (ZA:1799) -> `zigbee.device_proposed … source=boot_listed` (ZS:305-309) -> `proposal_accepted … source=config` (ZA:1621). Needs the IEEE in `adopt_devices` (ZA:149; read once at init, ZA:1840-1860) after X9, then a restart; device awake (J2:42; gesture UNKNOWN). Edit command UNKNOWN (precedent: audits/2026-09-04_R-4b_…:206).

## 3 Gates, and the card without each
- `KIT-ORDER:` (SSD Kit, +27 W PSU if needed; ZBDongle-E; Dongle Plus-MG24; USB extension): not placed, Nick's money (R112:34, :115, :123; B4:72). No SSD: no PI-2 (U:74), hs-dev-1 untouched. No MG21: Part A only (U:91); X8-X10 wait (B4:66).
- Pi 5 board: arrives Tue (U:76); RAM RECORD (U:81).
- `FLASHER:` open: probe-only - v13 proceeds, else label and wait (U:92); flash arm not dry-runnable (U:94).
- 176adad .deb (X4). SNZB-03P on hand (A9:67); without it formation + corpus run, X9-X10 wait.
- Imager -> NVMe path, and what boots before BOOT_ORDER: UNKNOWN (U:81; no NVMe-USB adapter in R111:152). An SD bring-up card needs its own hostname.
- `TAILSCALE: expiry-off`/`REMOTE:` asked by Oct 19 (HZ:138), in no v112 word list (R112:34): UNKNOWN; login is Nick's. Without: LAN only.
- Desk alias `hs-pi2`, sqlite3 on hs-pi2: UNKNOWN (PF:46 used `nick@<IP>`). MG24 spare unused (R111:151).

## 4 Proposed LIVE blocks (one act each: what | EXPECTED | STOP)
Two sittings, A (SSD) and B (MG21), each <= 2 h (U:76), no hour shared with dry-run #2 (U:99; R2).
- A0 STATE (PF:11) | slots | start <= 2 h before 21:30
- A1 desk .deb (PF:16-20) | PF:20, g176adad | debs != 1, hash, gone
- A2 desk SSD write (U:81) | `FLASHED:` (PF:23) | path UNKNOWN
- A3 hands power on | ping (PF:43) | none in 3 min
- A4 desk first contact (PF:45-47; U:81) | U:81 line, aarch64, 10c4 count 0, not installed | aarch64 missing, count >= 1 (PF:47)
- A5 BOOT_ORDER (U:81) | UNKNOWN | UNKNOWN (R9)
- A6 hs-dev-1 copy (U:82) | C10:35 (md5-pi, integrity ok) | integrity != ok, error
- A7 desk .db + config -> hs-pi2 | md5 = md5-pi (U:82) | 2nd mismatch (C10:39)
- A8 desk T0 .deb (PF:51-54) | PF:54, g176adad | hash mismatch
- A9 install, X1 arm (U:83) | `masked`, rc=0, PI:60 line, no JVM by class | JVM up
- A10 restore to X2 paths | UNKNOWN; no `data/zigbee/zigbee-network.json` | file present (R1)
- A11 drop-in + daemon-reload (U:84) | UNKNOWN | UNKNOWN
- A12 unmask + start (U:84) | active (UNIT:54, :61), 200, BT line, `registry.projection_rebuilt` skipped=0 (HomeSynapseCore.java:643), X6 | start-limit (UNIT:19-21); any `network_*` line: POWER OFF (PF:9)
- A13 desk readings (U:84-85) | rows=10 all UNAVAILABLE, RSS, replay | rows != 10
- A14 desk LAN before (PF:85-88) | `unreachable (or 000)` | RECORD (X5)
- A15 close: line (U:88 re-cut) | BLOCK 5 on any STOP (U:86)
- B0 STATE: active, port absent, no custody file, stick in hand
- B1 flasher, pinned (U:94) | `--version` = FLASHER | mismatch
- B2 hands MG21 in, extension lead (MG24:39) | one by-id (PF:116); no `zigbee.production_session_started` (ZA:661) | that line
- B3 probe (U:92) | `protocol 13` | `protocol 14` label (U:92); <13 UNKNOWN
- B4 flash, only with FLASHER's file, then probe (U:92) | v13 | not v13
- B5 config: MG21 port + channel ruling (R2) | UNKNOWN | exit 10 (UNIT:72)
- B6 restart | `zigbee.network_formed: channel={} panId=0x{}` (ZA:1148), `production_session_started … protocolVersion=13` (ZA:661) | POWER OFF: `network_restored_from_parameters` (NF:294), `network_resumed` (ZA:1144), `network_parameter_mismatch` (NF:307), `ezsp_version_unsupported` (EP:556-558)
- B7 desk corpus fields (X8) | MG24 rows filled | none
- B8 scoped open (X9) | C9:43 form | C9:43
- B9 hands 5-s hold, watch | A9:55 | DENY_JOIN (C9:58); `proposal_accepted`
- B10 list the IEEE (X10) | UNKNOWN | exit 10
- B11 restart = next boot | `boot_listed_candidate` (ZA:1799) | UNKNOWN
- B12 hands wake sensor, watch | J2:50 | RECORD retries
- B13 close: line; stick in or out UNKNOWN

## 5 Risks and side effects
- **R1 Twin network.** NF:285-298 re-forms the STORED channel/PAN/ext-PAN/key on an NCP with none; custody = `data/zigbee/zigbee-network.json` + `.root-key`/`scope_keys.json`/`secrets.enc` (PS:24-47; MN:104). B.3(1)'s "network parameters, so the fleet re-adopts without a re-join" (U:75) would clone hs-dev-1's network onto the MG21: strike it (U:82 copies neither).
- **R2 Channel.** ZY:2 pins 20; hs-dev-1 is on 20 (UNIT:101; MG24:67); a pin forms there (ZA:1161-1166) - shared air through dry-run #2 (Oct 22-23) and the run (Oct 30-Nov 2) (R112:33). Re-pin or radio off: hub.
- **R3 Adopt list** ZY:3-12 = hs-dev-1's fleet; a listed joiner is adopted at once (X9). Scoped windows only (foreign DENY, A9:29); never `bench.sh permit-join` (no scope, BS:117).
- **R4 hs-dev-1.** BLOCK 1 reads the live store, writes ~1.2 GB (U:82, :86) while the rig stays closed (R112:129, :131); BC11's Sunday BACKUP-1 is fresher (B4:86): reuse or re-copy, hub; free space UNKNOWN (C10:35). `scp pi:… hs-pi2:…` (U:82) does not pin whether hs-dev-1 connects to hs-pi2.
- **R5 Restarts.** Restart=always, 10 s, 5/300 s; exit 10 never restarted (UNIT:19-21, :70-72); start waits on the 90-s probe (UNIT:54, :61). At A12, C2 if kept, B6, B11; daemon-reload A11.
- **R6 Config writes** B5, B10: bad key = exit 10, unit down (UNIT:68-72). The copy brings hs-dev-1's `home_id` (MN:252-253), token (CS:35).
- **R7** PF:9 "`network_formed` in ANY output = POWER OFF the Pi and STOP" would stop B6: re-scope.
- **R8 Sticks.** Rig MG24 never in PI-2 (U:76); MG21 never on hs-dev-1 or the desk COM port (U:94); both 10c4:ea60 (MG24:59): tell by by-id (MG24:35-37).
- **R9** Nick's irreversible-class writes: EEPROM (U:81), the flash (U:92).
- **R10** Hostnames only (U:76); PF says "held card": do not carry it.
- **R11** The stub (lessons/pm-lessons.md:481) cannot prove mask-before-install, the sink under ProtectSystem=strict (UNIT:79), flash flags, NVMe path: first-sitting RECORDs.
- **R12 Bench verbs** (hs-dev-1 only, BS:6-9; not on hs-pi2, U:85). Read-only: status, health, log, entities, runs, state, digest (BS:214-220, :226). Side effects: start/stop/restart/run relaunch the Core (BS:210-213; via `systemctl --user` once bench-boot is on, BS:204-207); `scenario boot-health` restarts (R112:128); `permit-join` unscoped (R3); `events` reads the live store without mode=ro (BS:219); `export` writes files (BS:245). The card needs none.
