<!--
file: context/handoff/2026-08-13_H3-stage2_fresh-session-context-pack.md
purpose: A COMPACT, SELF-CONTAINED context pack so a successor Cowork session can pick up the H3
  Stage-2 thread with a clean token window instead of inheriting the (long) operator transcript.
  Read this INSTEAD of the transcript. It is written to be sufficient on its own.
audience: any successor Cowork session (hub, PM, coder, or a follow-on operator lane); Nick
status: CURRENT as of 2026-08-13 07:00 CDT
-->

# H3 Stage 2 — fresh-session context pack

## 1. Read order (three files, ~35 KB total — no transcript needed)

1. `context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md` — the evidence of record
2. `context/handoff/2026-08-13_H3-stage2_hub-decision-brief.md` — the five open decisions
3. **This file** — state of the world, what exists on disk, and what a successor should do

Historical, only if needed: the 2026-08-09 packet and the 2026-08-11 addendum (both now superseded on
schedule and several specifics; the return's AS-DOCUMENTED vs AS-RUN table lists every divergence).

## 2. One-paragraph state of the world

The H3 clean-image fresh-install rep is **complete**. A fresh Raspberry Pi OS Lite 64-bit (trixie)
image was flashed, the artifact `homesynapse_0.1.0+gd26777c_arm64.deb` was installed on real hardware
by the documented one-command path, and it reached health-green with RUNNING + token + auth enforced —
**the H3 MUST row is satisfied on its stated terms.** The bench (`hs-dev-1`) was restored and verified
against a measured baseline; the Friday 04:30 EDT nightly is armed. The rep produced **12 findings**,
one **CRITICAL**: the packaged jlink runtime omits `jdk.jfr`, so **no integration can start on any
build from `distribution/image/build-image.sh`** — and the CI assert set (boot + health + auth)
structurally cannot see it. Nothing was fixed; findings are never fixes. Five decisions are open with
the hub, listed in the brief.

## 3. Hardware / environment facts a successor will need

| | |
|---|---|
| Bench | `hs-dev-1`, Pi 5, Debian 13 trixie **Desktop** image, SD `SD128` serial `0xb4c3895a` (119.1 G) |
| Bench reach | `ssh pi` → `homesynapse@hs-dev-1`, `IdentityFile ~/.ssh/id_ed25519_pi`. Resolves via **Tailscale MagicDNS** (100.96.31.59). `hs-dev-1.local` resolves via mDNS |
| LAN | `192.168.1.0/24`; the Pi's DHCP lease is `192.168.1.80` (MAC-bound — the fresh image got the same address) |
| Bench app | Gradle `installDist` tree under full **Corretto 21**, started by `~/bench.sh start` (`nohup`, **no systemd unit** — F-21). Port **7070**, loopback only |
| Bench token | **`~/hs-bench/config/initial_api_token`** — NOT `~/.homesynapse/config/…`, which returns 403 (F-22) |
| Bench verbs | `~/bench.sh {start\|stop\|restart\|status\|health\|entities\|runs\|state <ulid>\|api_token\|digest}` |
| Bench baseline | `bench.sh entities` → 585 B, six entities, **5 AVAILABLE + 1 UNAVAILABLE** (the UNAVAILABLE one, `01KX1PA4HSJ581GASYB7DHE40F`, is the dead-and-kept Hue). Zigbee ch 20, panId `0x774c`, 6 devices |
| Nightly | user timer `nexsys-bench-nightly.timer`, `Linger=yes`, fires **03:30 CDT / 04:30 EDT**. Its service ends `failed` (exit 1) whenever a suite test fails — **normal**, and a reboot clears the state |
| Fresh image | user **`nick`** (uid 1000, NOPASSWD sudo), hostname `hs-fresh`, `America/New_York`, SSH pubkey-only. Reach with **`ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local`** (the `-i` is required — F-18) |
| Desktop | Windows `DESKTOP-SRK0P9D`, Git Bash. Raspberry Pi Imager **v2.0.10** at `C:\Program Files\Raspberry Pi Ltd\Imager\` |
| Cards | Bench card labelled `hs-dev-1 BENCH SD128 0xb4c3895a — 2026-08-13`. The fresh card is loose and still carries the completed fresh install — **it is a reusable evidence artifact; do not wipe it without deciding** |

## 4. Blocks on disk (`_scratch/h3/`) — reusable, all read-only unless noted

| Block | What it does |
|---|---|
| `s2-1-preswap.sh` | pre-swap bench read (authored here; the referenced "S2-1" never existed — F-20) |
| `s2-1b-baseline-gap.sh` | names the failed user unit; finds the app's owning cgroup; probes auth |
| `s2-1c-bench-baseline.sh` | **the canonical bench baseline** via `bench.sh` itself — run this first, any session |
| `s2-3-install-and-probe.sh` | Phases 2/3/4 in one pass on a fresh image (C-3 measurement → install → full probe set) |
| `s2-4-defect-and-auth.sh` | paired auth assert + negative control; proves the jlink module set at the artifact |
| `s2-5-final-evidence.sh` | MANIFEST integrity, 24-path route enumeration, clean stop/start leg |
| `s2-5b-reboot-and-stopdefect.sh` | cold-boot assert; characterises the exit-143 stop defect |
| `s2-6-restore-verify.sh` | **restore verification — and it runs `bench.sh start`**, which a reboot does not |
| `artifact/` | the .deb, tarball, build log, `BUILD-SUMMARY.txt` |
| `*.out.txt` | every block's verbatim output — the raw evidence behind the return |

**Re-running the whole hardware half now takes ~45 minutes**, because every block exists and the
artifact is verified. That materially lowers the cost of Decision 1 option 3 ("H3 contingent, re-run
after the module fix").

## 5. Hard-won operational rules a successor should not rediscover

1. **Never let the Imager customisation screens be trusted.** They pre-fill the **bench** profile
   (hostname `hs-dev-1`, the saved password, the saved Wi-Fi). Clearing Wi-Fi **does not stick** —
   it re-arms on every revisit. The review screen shows no values. **Verify from the written card's
   `bootfs/user-data`, never from the GUI.**
2. **The login user must never be `homesynapse`.** `postinst:23-27` creates its locked system account
   only `if ! getent passwd homesynapse`. Use `nick`. Verified good: `homesynapse:x:102:…:/usr/sbin/nologin`.
3. **`ssh -i ~/.ssh/id_ed25519_pi` is mandatory** for `hs-fresh` — the key is a non-default filename
   and OpenSSH will not offer it otherwise.
4. **Restoring the bench requires two steps no runbook states**: re-plug the coordinator (only after
   the fresh card is physically out), and run **`~/bench.sh start`**.
5. **`degraded / 1 failed` on the bench is normal** when the last nightly had a failing test; a reboot
   clears it. Do not read it as damage.
6. **Allow minutes, not seconds, for `hs-fresh.local`** — `avahi-daemon` is apt-installed by cloud-init
   on first boot.
7. **The Windows card reader gets no drive letter automatically.** Use
   `Add-PartitionAccessPath -DiskNumber N -PartitionNumber 1 -AssignDriveLetter` (non-destructive).
8. **Identify cards by elimination, never by size.** Both are ~119 GB. Inventory `Get-Disk` before and
   after inserting; the new row is the target.

## 6. Immediate outstanding items

- ⚠️ **Restore the Rosonway USB topology before Fri 04:30 EDT** (Decision 3). The coordinator is
  currently direct-attached to a Pi USB3 port. It works, but the Friday nightly and the open S31
  evidence read would otherwise run against an undocumented topology.
- The **five hub decisions** in the brief; the freeze is **Fri 2026-08-14 EOD**.
- **Register reconciliation** (RESOLVED: Stage 1 ends at F-12; Stage 2 is F-13..F-24) before any external citation.

## 7. Calibration note for a successor

The return's §8 self-audit lists **five errors made by the operator-support session**, including two
where a bug in its own probe script briefly resembled a product defect (`AUTHENTICATED → 401`, and 118
"integrity failures" that were a wrong working directory). All five were caught and corrected before
anything reached a finding. They are in the record deliberately — a successor should weigh the
remaining claims knowing what the error rate looked like, and should treat **F-19's causation** and
the **"no health surface exists"** claim as the two softest, exactly as the return says.

## 8. Late additions (found on final review — read these before acting)

- **Register is reconciled.** Stage 1 ends at **F-12**; Stage 2 is **F-13 … F-24**. Stage 1's taxonomy
  codes (`DOC`/`LB`/`GI`/`CA`/`LAT`) were deliberately **not** applied to F-13…F-24 — their expansions
  are not defined anywhere this lane could find.
- **F-23 (`jdk.jfr`) is NOT arm64-specific.** The amd64 image CI builds lacks the module too;
  `smoke/run-smoke.sh` simply has **no integration assert**. Every green install-smoke to date has
  certified an artifact whose integration subsystem cannot start.
- **`PrivateDevices=yes`** in `homesynapse.service` is a *second, documented* blocker for serial
  integrations on the packaged path ("RAMP post-M9"). Fixing `jdk.jfr` alone would not let the .deb
  reach a Zigbee coordinator. F-23 is still independent — it throws for every integration type.
- **The recurring failure class** (asserts that verify a proxy, not the property): iteration-3
  REPORTING-CLEAN · B3.1 A-5 · F-10 · F-23. Four instances, individually fixed, class never closed.
- **Bench-suite flake floor:** a *different* test fails each night (Wed `command-identify-honest`,
  Thu `command-confirm-s31`), both at AUTO floor 7/9. Bounds the confidence of any single-run evidence.
- **The fresh card still holds the completed install.** Re-inserting it is a ~10-minute round trip and
  can close the coverage gaps below without re-flashing. **Do not wipe it before deciding.**
- **Known coverage gaps:** `GET /dashboard/` never probed (CI asserts 200) · the `install.sh` tarball
  path never exercised · `/etc/homesynapse/homesynapse.env` contents never read · no `disable-wifi`
  control boot for F-19 causation · no uninstall/update-smoke legs · no load or soak testing.
