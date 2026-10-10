<!--
file: context/audits/2026-10-10_v104-b1_boot_restore_PKG-FRESH-1_intake_two-layer_audit.md
purpose: The v104 hub's beat-1 audit: the boot (v67 §1), the restore ruled before it, the fence-1 breach at the bytes, PKG-FRESH-1's intake (P1–P7 and P12′ in order), the cold-start failure (IR-148), IR-147's observation, the misses. The decisions live in the v104 DR (D-v104-1..14); this file is the evidence.
audience: the v104 hub · the v105 boot (P12′'s first read; the cold start) · Nick (§0)
state-type: intake audit
status: FILED v104 beat 1 (Sat 2026-10-10 ~12:1x CT; instrument 2026-10-10T17:18:49Z).
-->

# v104 b1: the boot, the restore, PKG-FRESH-1's intake

## §0 Verdicts
- **PKG-FRESH-1: the return ACCEPTED (STOPPED at A3), with findings.** The line is byte-equal to the guide's notes §0. Its numbers are re-derived by the hub at the bytes: the outputs file (18,448 B on disk, md5 `0c0eea18af6f0ac594ad07adffea46f3`, 30 blocks; Part E counted 18,325 B before its own lines), the journal (md5 `b93a7cbb0592b1cb7c7aa07f93a5bd7a`), the startup-failure capture (md5 `95b407d92783e006489c89be0ef9254b`), the guide's notes (66,559 B, md5 `8143eb9b9dfe11baff89dcd7ebc9c181`, read by range).
- **The restore: DONE at D2b** (12:00:49.242 CT; boot-health 6/6; rows 10; relinked 10). The gap was 135.9 min.
- **The breach: no form, nothing sent; hs-fresh's own store changed** (DR D-v104-4).
- **The cold start: J8-class; IR-148 minted** (D-v104-10).
- **P12′'s first read: the metering class ANSWERED 3/3 at the long-gap resume** (D-v104-11; IR-137).
- **IR-147's premise observed** (D-v104-8).
- **Misses on the record:** the guide's M-4; the hub's (the card's D1 order; the "HELD" role word; the label gate, fixed by Amendment 1); D-v103-28's two; v103 ruling 6's.

## §1 The boot (v67 §1, executed; the restore ruled first — DR §2)
- **Read set, by range, byte counts printed:** v67 whole 13,477 · `pm-handoff.md:8` 1,830 · the newest beat (`:15–:19`) 2,069 · `PROJECT_SNAPSHOT.md` 3,434 · the brief 11,506 = 32,316 B. Beyond §1, by range, where beat 1 sent the hub: the v103 DR `:168–:204` (the verdict), `:217–:230` (D-v103-20), `:270–` (D-v103-28); the card `:107–:124` (Part D) and `:126–` (Part E, the one line, §P); the v103 post-close rulings (4,234 B, md5 `e31a9907…96be`).
- **The five HEADs, one call:** core `409547c` · hivemind `ba7923d` · skills `e9a77a8` · bench `32bac40` · docs `5e8eb8b`; porcelain 0 · ahead 0 · `main` in each. The renderer's Windows worktree (`c110575`, `beat-renderer-1/state-file`) reads "prunable" from the device: its path is a Windows path the VM cannot stat. Not an anomaly.
- **The preflight:** one line per check, in the DR §2. C9's instrument: the per-file md5 of the three SOURCE trees on the device against this session's synced copies, 28 lines, `diff` empty. C10: 102 backticked paths in `context/strategic-context-map.md` resolved by basename against `git ls-files` of the five repos; the five misses are the templates `*_PM-mission-control_v*_orchestrator_session_prompt.md`, `YYYY-MM-DD_topic.md`, `handoff/*_session_prompt.md`, `months/YYYY-MM_month.md`, `weeks/YYYY-WNN_monDD-monDD.md`. C11: `(class|interface|record|enum) <Name>\b` resolves once each at `409547c`.
- **The paste against the file:** the paste written to the session and diffed against the staged copy from line 9: 9,752 B · 104 lines · `diff` empty.

## §2 The restore ruling — what it rested on (filed 16:17:03Z, before it was handed)
- **Layer 1 (the guide's claims):** the line (11:07) · guide-notes §13 (`:153–:184`) · outputs.txt D1 → D2-capture (`:86–:146`).
- **Layer 2 (the hub's own reads):**
  - **The journal** (§3 below): no form, no outgoing action, no ERROR-level line. The restore needed no repair act.
  - **The bench Core does not start at boot:** the card's D2 EXPECTED (`status: not running — a cold boot does not relaunch the bench's Core; the nightly does at 03:30`), and D2 relaunches it (`~/bench.sh restart`). Booting the held card without the dongle is therefore inert.
  - **The .80 premise:** `git grep -n '192\.168\.1\.80' -- context` returns hs-fresh's records only (R-4b `:226` "Card = 192.168.1.80 … no Tailscale interface on this card, unlike hs-dev-1"; H8a `:14`; R-5B `:8`). The Aug 23 sitting's E-P3 ("the held card inherits .80") reads NOT TESTED. Nothing in the record puts hs-dev-1 on the LAN at .80.
  - **known_hosts:9 is the hs-dev-1 entry:** D2-diag's refusal under `HostKeyAlias=hs-dev-1` names "Offending ECDSA key in /c/Users/Nick/.ssh/known_hosts:9"; `ssh -G pi` gives `hostname hs-dev-1` and `checkhostip no` (PRE-A, 13:51:48Z); `ssh pi` passed at 14:38:16Z (`pi-before ok`, `pi-after ok`) and A1 printed `hs-dev-1` at 14:39:40Z. Both of R3's forms look up that one entry.

## §3 The breach at the bytes (hs-fresh's journal, `_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_hs-fresh_boot-journal.txt`, 443 lines, 92,572 B)
| grep | count | reading |
|---|---|---|
| `network_formed` | 0 | no form |
| `network_resumed` | 1 | channel 20, PAN 0x774c (`:57`, 11:44:28.827 journal time) |
| ` ERROR ` (the level) | 0 | WARN 380 · INFO 55 |
| `permit` · `leave` | 0 · 0 | no permit-join, no leave |
| `bind` | 1 | `bindHost=127.0.0.1` (the HTTP bind), not a ZDO bind |
| `configure_report\|reporting` | 0 | no reporting configuration |
| `command\|cmd_sent\|send_` | 0 | no command |
| `probe\|ping\|read_attr` | 11 | the loopback `[health-probe]` and the migration runner, not radio reads |
| `ingestion_unknown_sender` | 344 | four senders: 0xb785, 0xb14b, 0xb8c4 (cluster 0x0B04) and 0x4565 (0x0400/0x0406) |
| `rejoin_ignored_window_closed` | 4 | 0xb14b, 0xb8c4, 0xb785 (0x0B04) and 0x4565 (0x0406): the host declined to adopt; the window was closed |
| `child_left` | 3 | 0xF044D3FFFED2A201, 0xF044D3FFFE1C1E8E, 0x449FDAFFFE688F57, sleepy end devices |
| `device_relinked` · `availability_changed` | 4 · 5 | hs-fresh's own registry (5 seeded from its sidecar; 3 named dark at the resume, 2 heard again) |

The distinct `zigbee.*` events (22 names) include no outgoing-action name. **Reading:** hs-fresh's Core opened the fleet's coordinator, resumed its network and listened; it changed its own store, not the network.

## §4 The intake, §P in order (layer 1: the guide's claims; layer 2: the hub's own reads of the files)
| P | verdict | the bytes |
|---|---|---|
| P1 the install completes | NOT MEASURED | STOP at A3: the identity probe (15:41:52Z) printed `hs-fresh` · `Debian GNU/Linux 13 (trixie)` · `ii  homesynapse    0.1.0+git20260914.115803.g6bd8508` · `active` |
| P2 the runtime | NOT MEASURED | — |
| P3 the coordinator-absent posture | NOT MEASURED on a fresh card | hs-fresh's `g6bd8508` printed `zigbee.reopen_no_target: the coordinator port did not re-enumerate; retrying on the watchdog backoff` after the dongle pull (D2-id): an old build's wording, recorded only |
| P4 the loopback friction | NOT MEASURED | — |
| P5 the dashboard at `/` | NOT MEASURED | — |
| P6 the restore | **PASS at D2b; the fence clause FAILED** | D2b (17:00:15Z): `hs-dev-1` · `dongle=1 by-id: usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0` · `core-clone: 37f05a9 ref=HEAD` · `[PASS] boot-health — 6/6 positive · 0 forbidden` · `formed=0 resumed=1 relinked=10 config_issue=0` · `registry rows=10 unavailable=['DHE40F']`. The gap: A2's `poweroff-sent 14:44:56Z` → the restart's `network_resumed` 13:00:49.242 EDT = 135.9 min |
| P7 the artifact | **HELD on two surfaces** | 0a (14:36:26Z): `debs=1` · `bc5185ed…4bfb34 *./deb/build/homesynapse_0.1.0+git20261004.212327.g49455fc_arm64.deb`; the zip `7f53498b…be8d`; B1 not reached |
| P12′ first read | **the class ANSWERS (no pair)** | PE-1 (17:07:15Z), the restart's log `bench-2026-10-10-130019.log`: four `availability_ping … outcome=ok` lines at 13:00:50.083–.086 EDT (rtt 315 · 91 · 56 · 243 ms); LOG0 `…130122.log`: only the S31, `ok` every ≈ 60 s |
| IR-137 | **the row gains "ANSWERED 3/3"** | as P12′; `ok` = the reply matched (`ZigbeeIntegrationAdapter` AVAIL-SHAPE Javadoc: "on an `ok` probe the reply itself is the evidence") |

**The cold-start failure, at the bytes** (`_scratch/v99/fresh1/2026-10-10_PKG-FRESH-1_hs-dev-1_startup-failure.txt`): launch 1 `bench-2026-10-10-124305.log`, persistence up at 12:43:09.158 → `startup_failed` at 12:43:53.987 (44.8 s); launch 2 `…124506.log`, 12:45:08.086 → 12:45:46.384 (38.3 s). Both: "Loaded 10 entities from checkpoint for view state_projection at position 1654229"; then `IllegalStateException: registry projection did not reach LIVE within ~30s during startup` at `HomeSynapseCore.java:1513` ← `:669`; then "WAL checkpoint completed"; then exit 99. Disk: 117G, 18G used (16%). The code at `409547c` (unchanged from `37f05a9`): `maxPolls = 1_500` and `Thread.sleep(20L)` in `awaitRegistryProjectionLive`; the checkpoint reset `:613–:627` ("Because the in-memory registries start empty every boot, the subscriber's checkpoint RESETS TO 0 BEFORE subscribeRuntime"). W1 (16:57:40Z): Mem 4049 MB; buff/cache 1561 → 1735 MB; `real 0m6.540s`.

## §5 IR-147's premise, observed (the journal's bytes)
`:2` the unit starts 11:44:17.892 EDT · `:42` `zigbee.availability_seeded: devices=5 from_sidecar=5 unknown=0` at 11:44:21.052 · `:57` `network_resumed` 11:44:28.827 · `:71` a frame at 11:44:35.537 · **`:72` the next frame at 11:46:56.949**, the same senders at the same few-second cadence on both sides. That is a +141.4 s forward step of the wall clock inside the running packaged Core, 14 s after the tracker seeded (fake-hwclock restored the 10:44:01 CT shutdown time; timesyncd stepped it). The consequence cannot be read here: g6bd8508 (Sep 14) predates AVAIL-SHAPE's INFO probe instrument, and no dark naming follows the step. The premise of IR-147 (a step inside the process on a packaged cold boot) stands on silicon; its effect waits for the clock-step test.

## §6 The misses, on the record
1. **The guide's M-4:** "put the HELD card in" with no label read-back, after a morning of card confusion.
2. **The hub's (the card text):** PKG-FRESH-1's D1 (v99; re-stamped v103) orders the dongle in BEFORE power-on, with no identity read of the card that boots. The guide's gap is the card's gap.
3. **D-v103-28's two:** the v103 re-stamp carried Thursday's "Part 0 DONE" without reading an outputs file; the dry-run never read the desk's ssh trust.
4. **v103 ruling 6's:** "Part 0 DONE (debs=1; FLASHED hs-fresh-1)" was a state line with its `<HH:MM>` slot unfilled — a template, taken as a report.

## §6b The misses, continued
5. **The hub's restore ruling gated power-in on a written label** without reading whether labels existed; the restore stopped at R2 (≈ 11:29 CT) until Amendment 1 (11:33).
6. **"HELD"** was a role word the card texts minted for hs-dev-1. In Nick's usage it names the card in use, and the two senses diverged at D1. The label acts ("label it HELD"; "labelled SECOND · hs-fresh …") were recorded as said in the guide's notes but never physically done.

## §7 Disclosed non-re-executions
The desk's `known_hosts` (a protected path; the guide's prints are cited). hs-fresh's 09:52 boot journal (not captured; its journald storage unread). A true cold-read rate of the store (W1 was partly warm). Whether the 03:30 nightly restart is warm (S2's LOG1 reads it). The guide's notes were read by range (§0–§3, §13), not whole. The restart log beyond PE-1's 24 lines, and the two boot-health bundles, were not read. CI is not involved (no code changed).
