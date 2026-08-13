<!--
file: context/handoff/2026-08-12_H3-stage2_pause-and-resume-note.md
purpose: Pause-and-resume note for the H3 Stage-2 hardware half. Phases 0–1 completed Wed
  2026-08-12; the operator elected to re-slot the hardware half (1b → 6) to Thu 2026-08-13.
  This note exists so the Thursday session starts at Phase 1b in minutes, not hours.
audience: the Thursday H3 Stage-2 operator-support session; Nick
status: ACTIVE until the hardware half completes
read-order: (1) 2026-08-09 operator packet · (2) 2026-08-11 Stage-2 dispatch addendum ·
  (3) THIS NOTE (newest — wins on conflict with both) · (4) the interim return at
  context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md
-->

# H3 Stage 2 — pause & resume note (Wed 2026-08-12 → Thu 2026-08-13)

## 1. Do not redo any of this — it is done and verified

- **Raspberry Pi Imager v2.0.10** installed at `C:\Program Files\Raspberry Pi Ltd\Imager\`.
- **The fresh card is WRITTEN and VERIFIED AT THE ARTIFACT** — not merely "the GUI said so".
  Image: Raspberry Pi OS Lite (64-bit), Debian **Trixie**, released 2026-06-18, 500.6 MB.
  Flash end **2026-08-12 21:12:34 CDT**. All ten applied settings confirmed by reading
  `user-data` off the boot partition: `hs-fresh` · user **`nick`** · password set · timezone
  **America/New_York** · keyboard us · SSH on, **public-key only**, key = `id_ed25519_pi.pub`
  (exact match) · **no Wi-Fi** · RPi Connect off.
- **Pre-swap bench baseline captured** (`s2-1`, `s2-1b`, `s2-1c` in `_scratch/h3/`).
- **Ten findings banked** (F-S2-1 … F-S2-10). They need no further hardware access.

## 2. Corrections that supersede the older documents

| Older document says | Reality |
|---|---|
| rep runs Tue 2026-08-11 | ran Wed 2026-08-12; hardware half re-slotted to **Thu 2026-08-13** |
| card label `— 2026-08-11` | use the **true date** on the day |
| Imager "OS customisation → GENERAL/SERVICES" | v2.0.10 six-step rail (F-S2-1). OS path `Raspberry Pi OS (other)` is unchanged |
| "your new cards are 32–64 G" | dead; the new card is 119.2 GB, same as the bench card |
| `ssh nick@hs-fresh.local` "works with no password" | needs `-i ~/.ssh/id_ed25519_pi` (F-S2-6) |
| "run the S2-1 read block" | did not exist (F-S2-8); authored as `_scratch/h3/s2-1-preswap.sh` |
| leaving Wi-Fi blank keeps the radio off | it does **not** (F-S2-7); card deliberately NOT edited |

## 3. Bench state at pause — nothing is owed to it

UP and untouched. App pid 115453 (started Wed 04:31:54 EDT by the nightly wrapper). Coordinator
attached (`/dev/zigbee → ttyUSB0`, `10c4:ea60`). Nightly timer armed and will fire normally at
03:30 CDT. `degraded / 1 failed = nexsys-bench-nightly.service` is **pre-existing** since
2026-07-16 — one failing bench test (`FAIL command-identify-honest`), not infrastructure.

**The Wednesday nightly will have run before Thursday's session.** Re-run `s2-1c-bench-baseline.sh`
first to confirm the bench is unchanged and to refresh the replay baseline.

## 4. Thursday's sequence — resume at Phase 1b

1. `ssh pi 'bash -s' < s2-1c-bench-baseline.sh 2>&1 | tee s2-1c-thu.out.txt` — confirm bench state.
2. **S2-2 shutdown** (its own STOP-gate): `sudo shutdown -h now`. Wait for the activity LED to go
   dark and STAY dark ~10 s. Only then pull power.
3. **Move the Pi** to the desk. The single Ethernet cable stays connected at both ends (C-2).
4. **⛔ Unplug the Zigbee coordinator.** SD-5 rail — out for the whole rep.
5. **Pull the bench microSD and LABEL IT IMMEDIATELY:**
   `hs-dev-1 BENCH SD128 0xb4c3895a — 2026-08-13`
   (Pi 5 slot is friction-fit: pull straight out, no push-click.) Never both cards loose+unlabeled.
6. Insert the fresh card. Monitor + USB keyboard attached. Power on. **Watch first boot** — this is
   where F-S2-7's predicted `network-online.target` stall would appear.
7. Reach it: `ssh -i ~/.ssh/id_ed25519_pi nick@hs-fresh.local`. Allow **minutes** — `avahi-daemon`
   is apt-installed by cloud-init on first boot, so mDNS is late. Fallbacks: router DHCP table
   (LAN is 192.168.1.0/24), then the console. **A headless-access failure is a numbered finding even
   if the console rescues it.**
8. **Before installing:** `dpkg -l | grep -E "curl|wget"` (C-3 — converts F-9 to a measurement).
9. Phase 2–4 per the packet: verify the .deb sha256, install AS WRITTEN, then the probe set
   (health green · service RUNNING · token at its printed path · auth enforced).

## 5. ⚠️ Phase 6 restore — two steps that appear in NO existing runbook

1. **Re-plug the coordinator** — only AFTER the fresh card is physically out (keeps Fence 2 intact).
   Neither the packet's Phase 6 nor the settings doc says to. Omit it and the bench restores with no
   radio, the open S31 read stays dead, and the nightly fires against a radio-less bench. **(C-1)**
2. **Run `~/bench.sh start`.** The app has **no systemd unit** — it is a `nohup` child of the oneshot
   nightly. After the restore boot `pgrep` returns NOTHING, and the next thing that would start it is
   the 04:30 timer, i.e. after the deadline. **(C-4 / F-S2-9)**

**Restore verification (like-for-like against Wednesday's baseline):**

- `~/bench.sh status` → `[OK] running (pid …)` + health tokens + **empty** failure tokens
- `~/bench.sh entities` → 200, ~585 B, **six entities: 5 AVAILABLE + 1 UNAVAILABLE**
  (the UNAVAILABLE one is the dead-and-kept Hue). Fewer than 5 AVAILABLE ⇒ coordinator did not return.
- Zigbee should report channel 20, panId `0x774c`, 6 devices, `EMBER_NETWORK_UP`.
- `systemctl --user status` → `degraded / 1 failed = nexsys-bench-nightly.service` is **EXPECTED**.

## 6. Fences and clock

Unchanged: bench untouchable outside the swap · coordinator out for the whole rep · read-only,
findings-never-fixes · abort = restore FIRST. Project fences: **soft stop 01:00 CT, hard stop
03:30 CT** (for a Thursday-evening run, that is Fri 2026-08-14 03:30).

**Schedule fact, stated without spin:** the gate freeze is **Fri 2026-08-14 EOD**, so Thursday
evening is the **last full swing**. If Thursday is lost, the hub must choose between a
Friday-evening attempt against the freeze boundary or carrying the H3 row.

## 7. The return

`context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md` is **already filed**
(interim, supersedes-in-place) with the phase log, timings, AS-DOCUMENTED vs AS-RUN table, all ten
findings, the S-10 insight rider, and a self-audit. Thursday's session **supersedes it in place** —
it does not start a new file.
