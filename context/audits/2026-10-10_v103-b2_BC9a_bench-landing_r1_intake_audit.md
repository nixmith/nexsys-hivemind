<!--
file: context/audits/2026-10-10_v103-b2_BC9a_bench-landing_r1_intake_audit.md
purpose: The v103 hub's beat-2 combined intake. BC9a's return (two layers, P1–P7 and P-v103-1 in order), the bench landing (`32bac40`) with the read its card lost, the HERO-U2b-r1 rider, and the hub's own card-form correction.
audience: the v103 hub (rulings) · the v104 boot (the soak's premise; BC9's re-stamp notes) · Nick (§0)
state-type: intake audit
status: FILED v103 beat 2 (Sat 2026-10-10 ~08:2x CT; instrument 2026-10-10T13:2xZ).
-->

# v103 b2 intake: BC9a, the bench landing, the rider

## §0 Verdicts
- **BC9a: ACCEPT.** The Pi has run `37f05a9` BY SHA since 07:17 CT (BOOT0 `bench-2026-10-10-081747.log`, Pi-local 08:17:47 EDT; jvm pid 71831). Boot-health is PASS 6/6 at 10/10. **P-v103-1 HOLDS:** the Hue reads `availability=UNAVAILABLE availabilityReason=None lastSeenAt=None link=None` on `37f05a9`, so N1's retraction (D-v103-6) stands on silicon.
- **The bench landing: `BENCH: LANDED 32bac40`.** The card's commit, fast-forward and push all ran (5 files, `cddac94..32bac40`). Its last read crashed on the Windows console's code page (IR-146). The hub re-ran it at `32bac40` on the device's Linux shell: `verify72h selftest: 48 check(s), 0 failure(s)`; engine `selftest: 42 check(s), 0 failure(s)`.
- **HERO-U2b-r1: ACCEPT.** Exactly three files changed (md5 `84320a7a021d` · `cfd85e01943a` · `753b13d3c557`, equal to the return's). `src/` is byte-identical to the U2b snapshot. The hub's `npm run verify` in a clean container exits 0, with contract-check ✓ 11 endpoints at v1.1.6-2026-10-09. The core landing card ran gated: `CORE: LANDED 409547c`, `CI: green` (§5).
- **The hub's own correction.** The b1 hivemind card used the library's un-gated form, `card()` with a `;` before `git commit`. IR-101 has been OPEN on this since v87, and every card from v87 to v103 b1 kept the drift. The b1 census held (12 = 12), so the record is true. From b2 on, every hub card is gated by test, written by the beat script. The HERO-U2b landing card is the first; it was dry-run in a throwaway repo (28 paths commit; 29 refuse).

## §1 BC9a, layer 1: the guide's return against the card (P1–P7 in order)
- **P1, the deploy: HELD.**
  - C2: `HEAD is now at 37f05a9`, `ref=HEAD sha=37f05a9 parent=49455fc`, `origin-main=2b4be09`. The re-stamped C2 EXPECTED was `<2b4be09 or newer>`. P1's own sentence still read `37f05a9`, because the re-stamp leaves pre-registrations as cut (pm-lessons 2026-10-07), so P1 is adjudicated against C2's EXPECTED. The guide's obs. 4 named this.
  - C3: `deployed=37f05a9 ref=HEAD`; `avail-shape-in-tree=1` (`integration-zigbee-0.1.0-SNAPSHOT.jar`); `[PASS] boot-health — 6/6 positive · 0 forbidden` (the API assert read 10 rows and the 10 ULIDs); `formed=0 resumed=1 relinked=10 adopted=0 proposed=0 config_issue=0`; `registry rows=10`; `integrity=ok`; rows-after 1,644,011.
- **P2, BENCH-PULL-8: HELD.** `ba846c2..cddac94` fast-forward; `constants-md5: 9b0af47b3376`. Engine 42 · verify72h 46 · bench.sh 27 · digest 54, all with 0 failures. `avail-field-in-tree=24`; `nightly-flags=1` (AVAIL-LINE-1b landed), so Sunday's digest is predicted to carry `avail:`. That is a prediction, not a proof; SOAK-NIGHT-2's P10′ reads it.
- **P3, the first printed probe outcomes: RECORDED.** Five lines, all the S31 (`0x00124B002FA8D1C5`), all `outcome=ok`, rtt 243 / 47 / 53 / 45 / 44 ms, all `seen_during_probe=true`. That field is F-2's reading: on an `ok` line it reads the reply itself and carries information only on `timeout` lines. **The card's premise "`pings=0` because nobody has been silent 60 s yet" is refuted for the floor class across a restart.** The first probe came 4.652 s after `network_resumed`. The silence clock carries over from the sidecar seed (`availability_seeded: devices=10 from_sidecar=10 unknown=0`). After that the probes came every 60.055 / 60.149 / 60.112 / 60.096 s (guide obs. 5).
- **P4, the five mains rows: RECORDED.**
  - G4-1: `AVAILABLE frame_received 2026-10-08T06:55:37.106667040Z` (lqi 248).
  - G4-2: `AVAILABLE frame_received 2026-10-09T11:35:38.667676404Z` (lqi 252).
  - TR3 and S31: `AVAILABLE` with None × 3 (IR-133's shape).
  - The keys are each device's last TRANSITION replayed, not a live last-heard (guide obs. 7). The card shows `lastSeenAt` only on dark rows, as "last heard", where the transition instant is the truth.
- **P5, the sensor: RECORDED.** `AVAILABLE frame_received 2026-10-08T22:10:38.556395459Z` (lqi 240); the Thu 17:10 CT re-power. This is the soak's baseline.
- **P6, the Hue: arm (a)**, as P-v103-1 above.
- **P7, IR-135: RECORDED.** `automation.identity_loaded … automations=1 triggers=1` (bench-hero). 3 handoffs on the nightly boot (Part A, under `df2bc62`); 0 in BOOT0's 4 min 33 s. The trigger is the motion entity, so nothing moving explains the 0. Not read further.
- **The guide's two judgment calls: both RULED right.** (obs. 2) Part A's status line `--- failure tokens ---`, the `status` verb's last line, is BC8's obs. 1 again; the card's EXPECTED was the hub's wording. (obs. 3) `position=849602` graded `≥`: see §2.

## §2 BC9a, layer 2: the hub's own reads at the bytes
- **The kept log** `_scratch/v101/bc9a/bench-2026-10-10-081747.log` (11,592 B): `network_formed` 0 · `network_resumed` 1 · `device_relinked` 10 · WARN 9 · ERROR 0 · `availability_ping` 5, all `outcome=ok` and all `seen_during_probe=true`, all device `0x00124B002FA8D1C5`, at 08:18:20.703 / 08:19:20.758 / 08:20:20.907 / 08:21:21.019 / 08:22:21.115 Pi-local (EDT; CT = −1 h). `availability_link` 0 · `availability_changed` 0 · `ash_frame_rejected` 0 · `automation.run_handoff` 0. `EventTypeRegistry initialized with 58 event types` (BC8: 57; J2's `join_rejected`). `availability_seeded: devices=10 from_sidecar=10 unknown=0`.
- **The registry's position** (`RegistryProjectionSubscriber.onCaughtUp()` at `37f05a9`) logs `lastAppliedPosition`, the global position of the last registration event applied. It moves only when a registration event is appended; there has been none since REHEARSAL-1b (Oct 2). So `849602` on every boot since is correct, and the card's `p > 849602` was the hub's wording. No card now on disk carries the string (grepped: BC9 · PKG-FRESH-1 · SOAK-NIGHT-2).
- **The outputs file** (8,039 B; A 12:00:36Z → E 12:22:33Z): read whole. Its C3 shows two launches, the card's restart (`bench-2026-10-10-081651.log`) and boot-health's own boot (`…081747.log`, BOOT0). This is the pattern on record (BC8's C3); the guide wrote BOOT0 correctly.
- **Not re-executed (disclosed):**
  - the first boot's log (on the Pi, not copied);
  - the boot-health bundle;
  - the backup's `integrity_check` (run on the live db at C3, `ok`);
  - the build log beyond its last lines;
  - a Shelly probe, `seen_during_probe` on a timeout line, and the dark path (none occurred);
  - the S31's rate beyond 4 minutes. BURNIN-1 reads it at ≈ 10:30 CT.

## §3 What BC9a changes
1. **The `CARRIER:` H10 (D-v102-14) is half-tested already.** The floor class is probed every ≈ 60 s while it sends nothing of its own, and each answered probe opens and closes its own silence. So for that class, option (d)'s "one `probe_answered` per silence episode" is one per probe: ≈ 1,440 a day from the S31 alone. BURNIN-1 (≥ 3 h of the same) is the read that finishes the test (P-v103-2). The H10 returns refined before the word is asked.
2. **IR-56's condition row (the 90-s post-restart read, at the class's naming time) is sharper.** Across a restart the floor class's silence clock carries over from the seed, so a plug that does not answer after a boot can be named dark within ≈ 2 min of `network_resumed`, not 70 s after its last frame. The row is written into dry-run #1's packet with that sentence.
3. **Notes for BC9's re-stamp at v104** (BC9 moves to Sunday). Its STATE line names `32bac40` for BENCH-PULL-9. A cached boot prints 0 `zigbee.reporting_cluster` lines (guide obs. 9: the line comes only from `driveReporting` on a fresh adoption or a live re-link), so BC9's Part A reading should expect 0 and the sensor's lines come with a live re-announce. Its `pings=0`-style premises read as in item 1.
4. **The record.** BC9a's card → EXECUTED. SOAK-NIGHT-2's P1′ reads this audit's §1.

## §4 The bench landing, and IR-146
`32bac40 feat(verify72h,scenarios): BENCH-142 + 142b — …` is on `main` and origin. The card's reads matched: `tmp before: 10` → `after: 0`; the branch; `staged: 5`; trailer grep `0`; the fast-forward of 5 files (155+/31−); the push. The last read (`python3 -B tools/verify72h/test_verify72h.py | tail -1`) died on `UnicodeEncodeError: 'charmap' codec can't encode character '→'`: the test names carry "→" and Git Bash's Python writes cp1252. The selftest itself did not fail. **IR-146:** a card's `python3` call on the desk runs as `PYTHONIOENCODING=utf-8 python3 …` (IR-140's renderer rule, made general). IR-142: LANDED `32bac40`; it closes on the Pi at BENCH-PULL-9 (BC9).

## §5 HERO-U2b-r1
- **The diffs at the bytes:**
  - `scripts/contract-check.mjs:22` → `'v1.1.6-2026-10-09'`, with a four-line paragraph (five literal homes; v115 and v116 by pattern).
  - `eslint.config.js`: `files` += `RecoveryCard.tsx`, `recovery.ts`; the comment says eight.
  - `SPEC.md` §7: +4 rows, + the amendment line.
- **The return's additional choices:**
  - the reverse-derived Level and Words columns for the four new rows (52/59 and 58/59 reproduction; "Asked twice; nothing came back." scores 3 words because `;` ends a sentence). ACCEPTED as disclosed.
  - its first census used a plain `git status` before the lock-free rule. No lock was left (`ls .git/*.lock` = 0 at the hub's read).
- **The landing card** `_scratch/v103/b2/card_core_hero_u2b_land.txt` runs gated (HEAD `2b4be09` · `main` · no lock · trailers 0 · staged 28 · nothing outside `web-ui/dashboard/`). The message file is `_scratch/v103/b2/2026-10-10_core_HERO-U2b_commit-msg.txt` (4,133 B; trailer grep 0).
- **It ran at 08:06:** every gate printed as expected (`head=2b4be09 branch=main porcelain=28 locks=0 trailers=0` · `staged: 28 · 7 A 21 M · outside: 0`) → **`CORE: LANDED 409547c`** (28 files, 1,798+/61−), pushed; **`CI: green`** on `409547c` (Nick's word).
