<!--
file: context/handoff/archive/pm-handoff-beats-v70b3-rotated-2026-09-12.md
purpose: v70 beat 3 rotated VERBATIM out of pm-handoff.md at v71 beat 5 (the live cap is 12 blocks). bytes(kept) + bytes(archived body) + 1 = bytes(before), asserted.
status: ARCHIVED 2026-09-12 (v71 beat 5)
-->

## 2026-09-11 (v70 beat 3 — THE DELIVERABLE: R-4c's packet on disk, measurement only, C-003 the exit; beat 2 landed `138e988`, Fri 2026-09-11 ~18:1x CT (instrument 2026-09-11T23:11:29Z))

**Landed (Nick's hands):** hivemind `138e988` (beat 2), pushed, porcelain 0. **Authored by range** (the R-4b packet and record §0/§3/§9; the H8-a form; F-R4-1b's return §0; the adapter's log tokens at `1e26912`): `context/instructions/2026-09-11_R-4c_measurement-only_zdo-surface-C-003_navigator-packet.md` (27197 B) + the scaffold `context/audits/2026-09-12_R-4c_measurement-only_operator-record.md`. **The shape:** §0 the artifact = `1e26912`'s install-smoke run (Java `eabdbb1`: F-R4-1b + HONESTY-1; the `ci` red does not gate the .deb) · §1 fetch + hash · B0 the swap and the pinned IP · B1 the upgrade and nine boot counts (anomaly 0 at boot) · B2 `lastReported` read once and the gradle line · B3 the guarded window key, the 240-s self-counting provocation of the three sleepy Sonoffs, the harvest chain and the census of six IEEEs · B4 the second read, the anomaly count, the disarm · B5 the restore. **The exit:** `ieee_addr_rsp … device=0xF044D3FFFED2A201` and its `device_adopted … source=rejoin` in one invocation; a `zdo_miss` is a finding, not a stop. **A design fact re-derived at source, not assumed:** the rejoin arm admits only while the door is open (`isPermitJoinActive()`; `rejoin_ignored_window_closed` otherwise; opening clears the once-per-nwk set), so measurement-only still needs one window — the config key, not a Core write. **Rotation:** six v68 blocks → `archive/pm-handoff-beats-v68b1-v68b6-rotated-2026-09-11.md`, bytes asserted equal; live blocks 7. **Handed:** this beat's card (4 M + 3 A). **Next:** the H8-a paste at 18:45 by the send · b4 FIX-2's instruction · b5 HERO-1b · b6 P-1 · the H8-a intake on `H8A:`. Order: hivemind 6 = 4 M + 2 A by explicit paths (porcelain holds 7: the HERO-1b return, which arrived during the beat, stays unstaged until v71 files its audit). ctx: beat 3 · calls ≈36 · read ≈150 KB · wrote ≈55 KB

**Leverage line:** Saturday is specified before Friday's rig session starts; nothing is re-planned tomorrow.
**The alternative shape, rejected:** a window-free packet that waits for the SNZB-02P's own report — the adapter ignores unknown senders while the door is closed, so the wait would measure nothing.
**2029 test:** every expected token is one the adapter logs at `1e26912`; the six IEEEs are the record's, not typed.

