<!--
file: context/handoff/2026-08-11_H3-stage2_dispatch-addendum.md
purpose: Stage-2 dispatch addendum — the deltas between the 2026-08-09 operator packet and tonight's actual conditions (Tue 2026-08-11 evening). Read AFTER the packet, BEFORE any act. The packet's fences and interactive §8 mode govern unchanged; where this addendum and the packet's Stage-2 details conflict, THIS FILE WINS (it is newer and reflects the hardware on the desk).
audience: the dedicated Stage-2 operator-support Cowork session; Nick
status: ACTIVE for the 2026-08-11 evening rep
-->

# H3 Stage 2 — dispatch addendum (2026-08-11)

## 1. Tonight's conditions (supersede the packet's Mon/Tue framing)

- **It is Tuesday 2026-08-11 evening (America/Chicago).** The rep runs tonight. **The bench must be fully restored with margin before the Wed 03:30 America/Chicago nightly fire (04:30 Pi-local — the Pi runs America/New_York).** Persistent=true means a swap spanning 03:30 CT fires the missed suite on the restore boot — priced and acceptable, but aim to restore hours before, not minutes.
- **Hardware ON THE DESK:** the new microSD — **SanDisk 128 GB Ultra UHS-I (U1/C10), still in its packaging** — and a USB microSD reader for the Windows desktop. Nothing else new is needed.
- **Software: NOTHING is installed yet.** Raspberry Pi Imager is NOT on the desktop. Phase 0 of tonight's guidance = download and install it from `https://www.raspberrypi.com/software/` (the Windows installer), then proceed. Do not assume any tool exists on the desktop without checking; the operator will confirm each install step as it completes.

## 2. ⛔ THE 128 GB CAVEAT — the size discriminator is DEAD

`_scratch/h3/STAGE-2-IMAGER-SETTINGS.md` says "your new cards are 32–64 G" — **OBSOLETE.** The new card reads ~119 G in every tool, **the same as the bench card** (`SD128`, serial `0xb4c3895a`). Size can no longer tell the two cards apart. The fences that replace it:

1. **Label the bench card the moment it leaves the Pi, BEFORE the new card leaves its packaging** — `hs-dev-1 BENCH SD128 0xb4c3895a — 2026-08-11`.
2. Never have both cards loose and unlabeled at the same time.
3. At the Imager's Storage step the only card in the desktop reader is the NEW one (the bench card is still in the Pi at flash time) — confirm the reader shows exactly one removable device before writing.

## 3. Everything else stands verbatim

- The packet (`context/handoff/2026-08-09_H3-clean-image_fresh-install_operator-packet.md`) governs: interactive §8 mode (ONE phase at a time; every command source-verified before issue; expected tokens named; STOP-gates in their own blocks); the hard fences (bench card out, labeled, untouched · **the Zigbee coordinator PHYSICALLY UNPLUGGED for the whole rep** — the SD-5 rail · read-only, findings-never-fixes · full restore before the fire; abort = restore first); the insight rider feeding S-10.
- `_scratch/h3/STAGE-2-IMAGER-SETTINGS.md` governs every Imager setting **except the obsolete size line** (§2 above): OS = Raspberry Pi OS Lite 64-bit (trixie) · hostname `hs-fresh` · **login user `nick`, NEVER `homesynapse`** (the postinst landmine) · Wi-Fi OFF · locale America/New_York · SSH public-key-only.
- Record `dpkg -l | grep -E "curl|wget"` on the fresh image BEFORE installing (converts F-9 to a measurement).
- The artifact of record: `homesynapse_0.1.0+gd26777c_arm64.deb` (sha256 `5b1382…575`) — locate per the Stage-1 return; verify the sha256 on whichever copy is transferred before `apt install`.
- Return SUPERSEDES-IN-PLACE at `context/audits/2026-08-09_H3-clean-image_fresh-install_operator-return.md` (law 37). The session guides; Nick executes; findings are never fixes.
