<!--
file: context/audits/2026-09-26_CHAR-sitting-3_return.md
purpose: the CHAR sitting's part-3 (close-out) return, written by the guide session at 19:3x CT and filed VERBATIM below the marker (11,630 B; its §4 facts and §5 questions/proposal are ruled in `context/audits/2026-09-26_v81-b5_CHAR-sitting-3_intake_two-layer-audit.md`). Intaken at v81 beat 5.
status: FILED v81 beat 5 (Sat 2026-09-26 ~19:5x CT; instrument 2026-09-27T00:52:10Z).
-->
<!-- VERBATIM FROM HERE -->
SITTING-3: DONE · key 13:permit_join_duration: 254   # THURSDAY ORDER T1b (2026-09-25): the recovery window; removed at T3 · mtime 2026-09-25 23:16:10.529613905 -0400 · boots-today 3 · windows-opened 3 · G4-2 41905/2s · TR3 488/232s · KEY: remove · S31 in

## §1 The lines (verbatim; [CT] = Nick's message; each paste's shell prompt and echoed command left out — they were the list's own)
1 [18:53]
```
mtime: 2026-09-25 23:16:10.529613905 -0400
size: 669
13:permit_join_duration: 254   # THURSDAY ORDER T1b (2026-09-25): the recovery window; removed at T3
key-lines: 1
boots-today: 3
bench-2026-09-26-043007.log: permit_join_opened=1 device_join=0 device_announce=0
bench-2026-09-26-043028.log: permit_join_opened=1 device_join=0 device_announce=0
bench-2026-09-26-043135.log: permit_join_opened=1 device_join=0 device_announce=0
current: bench-2026-09-26-043135.log
```
2 [18:57]
```
G4-2 AVAILABLE on=False W=0.0 V=124.86 ver=41905 age=2s stale=False
TR3 AVAILABLE on=True W=0.0 V=128.7 ver=488 age=232s stale=False
G4-1 AVAILABLE on=False W=0.0 V=125.23 ver=44014 age=3s stale=False
```
3 [18:58]
```
287 /c/Users/Nick/Desktop/Code/ClaudeFolder/_scratch/v81/sat0926/tmux-scrollback-2.txt
9
```
4 [19:02] `KEY: remove.` (the word; his reason in §2), then [19:02]:
```
WINDOW KEY REMOVED (no restart) · adopt_devices 9 · backup /home/homesynapse/hs-bench/zigbee.yaml.before-key-removal-20260926
key-lines now: 0
```
5 [19:04] 5: S31 in
6 [19:05] 6: rig down
7 [19:08] 7: done

## §2 Not SAY lines, as Nick said them (CT, verbatim)
- 18:41 [the prompt attached] "Read and follow all instructions in the prompt provided. Take your time second-checking any information, being patient with me and explaining/guiding me through things at my level (I am less intelligent than you, after all), and ensuring we thoroughly and accurately encapsulate all results and feedback necessary for the hub/orchestration session to maker the best critical/independent assessment of our results, as possible."
- 18:47 "Note: the rig is setup as `wall -> A -> extension cord -> B2 -> clamp lamp (lit)` with A/B2 reading 41.8/41.7, respectively."
- 18:58 "Note: G4-1, G4-2 and TR3 are all plugged into different outlets in close proximity to the Pi, but only TR3 switched on right now."
- 19:02 "Reason: I messed up and we also quit in the middle. No real reason to keep it, I am pretty sure."
- 19:08 "I need you to take your time very carefully and thoroughly review what the hub is seeing and thinking about — in terms of how it will likely assess your return, then how/what it will think about to begin carefully and strategically planning out what these results/feedback means for our system, and how we proceed." · "Your return should not override the hub/orchestration session's own agency or reasoning, but should encourage and guide it towards an ambitious end goal for how we proceed, which will bring us closer to both our short and long-term objectives."
- Not answered: at 7 the guide asked, optionally, whether "I messed up" meant the T1b script run again Friday night; no reply.

## §3 The guide's departures (one line each)
d1 18:42–18:47, before action 1, read only (no git, no writes, nothing on the Pi): parts 1–2 returns, card1.txt, the bundle's api-captures.json, constants.yaml :76–78 / :174–176 (= the list's three ULIDs), `_scratch/thu0924/` (T3b.txt, T6.txt, pi-capture-2's logs and zigbee.yaml.after-T3), the THURSDAY-ORDER scripts, the seven-cards status (card 1b not run). The paste = the hivemind file, 8,197 B, LF sha256 16ccef46…, byte-identical.
d2 18:47 Nick's rig note interrupted the pre-check; action 1 went out next.
d3 Each action carried a plain-words note, and every Pi time was converted to CT (Nick's 18:41 word). No step added, removed or reordered; the guide ran nothing on the Pi; tmux untouched.
d4 Between actions, read only: `_scratch/thu0924/T1c.txt`, T1b.txt, T1b.sh, the T2b and Half-2 cards, the capture's run2/ listing and transcripts, a hivemind grep (T1c · 232335: only v75 DUR-1 test ids), tmux-scrollback-2.txt (§4.3), the core's `*.java` for a file watcher (none), nightly.sh, boot-health.yaml, the part-2 action script; two searches of Nick's past chats (nothing on Friday 22:16–22:23).
d5 After 1 and at 4 the guide told Nick that three of the prompt's premises did not match the bytes (§4.1) and that the core watches no file; the rec was put as the hub's; Nick chose.
d6 ≈19:11 one `git log -1` in the local nexsys-bench (read-only; printed `f1c2f9a 2026-09-26T09:13:10-05:00`) — against "never run any git command". No lock, no file changed (.git's newest mtimes are part 1's, 14:24:57Z / 14:27:05Z).
d7 At 7, one optional question (§2's last line).
d8 §4–§5, and the size past 6 KB, on Nick's 19:08 word: §4 is facts, §5 questions and one proposal — no rulings. §5 was read against the b4 audit, pm-handoff's b4 beat and the HORIZON RE-CUT.
d9 After 7, a separate agent checked this return read-only against the bytes (no git, no writes; ≈ 80 claims confirmed). Six fixes were applied: G4-1's rate was not idle; boot-health's reach; 598.7 s, not "≥ 10 min"; the TR3's under-load ages; the stopped-run option; `thu0924/`'s mtime.

## §4 Facts from the bytes (CT; the Pi's clock is UTC−4 = CT+1: T6's log 22:06:56 ↔ its bundle 20260926T020656Z)
### 4.1 The key: its writer and its windows
- T3b's removal boot `bench-2026-09-25-215445.log` = Fri 20:54:45 CT (T3b.txt saved 20:55:00). The "21:54 CT" in this prompt and in b4 §0/§5 is the Pi's clock.
- The live line was T1b.sh :19's own text, appended (line 13). 669 B = after-T3's 571 B (sha256 513b2c01…) + that line's 98 B. mtime Fri 22:16:10 CT, 81 min after T3b.
- `_scratch/thu0924/T1c.txt` (2,979 B; saved Fri 22:23:50 CT): `WINDOW KEY ALREADY PRESENT (kept)` → `bench-2026-09-25-232335.log` (22:23:35) → `zigbee.permit_join_opened: duration=254s` at 22:23:48 → `T1b-END`. No T3 after it. Not in the hivemind: run2/ ends at T4–T6's state reads "at 22:59 EDT" (21:59 CT); the Half-2 card: T7 aborted at its first prompt.
- The 22:16:10 write carries T1b.sh's text. `_scratch/thu0924/`'s own mtime is 22:16:11.5 CT, and T1c.txt is the only entry younger than it. So T1c.txt was first created at the write (within ~1 s, two clocks) and rewritten at 22:23: the T1c command ran twice, and the first run wrote the key. Friday 20:30 / 20:50 shows the same pattern (two T1b.sh runs into one T1b.txt). Whether a boot followed the first run is not settled: a full run, a run stopped after the write (Nick: "quit in the middle"), or DRY_RUN=1. Action 1 read only the 09-26 logs.
- Sat 03:30:07 · 03:30:28 · 03:31:35: three boots, each `permit_join_opened=1 · device_join=0 · device_announce=0`; the core up since 03:31:35. nightly.sh restarts at :198 (quiesce) and :244 (restore), and :381 says the suite's fresh-boot legs restart the app too, so three is consistent with the script ("twice" undercounts).
- Windows since T3b: ≥ 4 (Fri 22:23 + Sat ×3), 5 if a boot followed the 22:16 write. No join or announce in this morning's three logs; the 22:23 boot's log was not read past T1c.txt's lines.
- boot-health.yaml's forbidden (:60–63): `device_proposed` · `zigbee.key_establishment_failed` · `network_parameter_mismatch`. `permit_join_opened` is not among them, so boot-health would not flag a window. It judges only its own restart (:35–36); no nightly output was read.
- Removed Sat 19:02, no restart; the backup = the pre-removal text (not read). Not read: whether the live file now equals after-T3 (571 B, 513b2c01…).

### 4.2 The plugs at 18:57 beside the bundle
- G4-2: ver 39518 at 22:37–22:44Z (witness 22:34:31Z) → 41905, age 2 s: reporting again, +2,387. It resumed after 17:44:30 (the bundle's last frozen read). At the Gen4 cadences seen (1 per 1.29–1.8 s), 2,387 versions take ≈ 51–72 min, which puts the resume between 17:44:30 and ≈ 18:05. Action 27's re-plug into the wall (17:44:30–17:47) is at the early edge of that span. That's an inference; the store holds the instant.
- TR3: ver 393 (witness 22:08:05Z) → 488 = +95 in ≈ 105 min (≈ 1 per 66 s); age 232 s (> part 2's 87–165 s); relay on, no load; V 128.7 against the Shellys' 124.86 / 125.23.
- G4-1: ver 36184 (20:07:15Z) → 44014, ≈ 1 per 1.76 s averaged over time partly under the lamp (to ≤ 16:17 and 16:21–16:26; the bundle's loaded rate was 1 per 1.29 s); age 3 s.
- Both Gen4s are now relay-off (on at their reps); the TR3 is on (on at its reps). `stale=False` on all three; `staleAfter` was null in all nine bundle bodies (not re-read) — IR-61 as ruled.

### 4.3 As left (19:05)
wall → A → cord (empty); the lamp, B1, B2 on the desk; G4-1, TR3 (relay on), G4-2 and the S31 (in 19:04, button untouched, not read) in the wall; tmux `metering` alive, detached, at the shell prompt. `tmux-scrollback-2.txt`: 287 lines, 30,111 B, sha256 8f2f0f2e…, from the scenario's first line (= scrollback-1 :1–3); REP at :71 :83 :95 :146 :158 :170 :221 :233 :245 (= the bundle's nine); `[FAIL]` :284; bundle :286; ends at `homesynapse@hs-dev-1:~ $`.

## §5 For the hub's planning: questions the bytes raise, and one proposal (the hub rules)
Q1 The 22:16 write: one read tells whether a boot followed it — `ls ~/hs-bench/bench-2026-09-25-2[23]*.log` with each file's `permit_join_opened`. Nick's own account is §2 19:02.
Q2 G4-2's resume instant (the event store). If the store puts it at the re-plug (17:44:30–17:47), the silence ended with a power-cycle, so it was device- or link-side, not the core's: a lead for IR-61's class. The packet's "one silent" could then read "silent ≥ 598.7 s, back after a power-cycle".
Q3 The fix's proof: the live file = after-T3 before BENCH-CORE-3 restarts, and tonight's nightly boots each `permit_join_opened=0`. It's refutable, and it fits BENCH-CORE-3's opening read, as do the S31's rejoin (not read) and the stray tmux `metering`.
Q4 The TR3's witness was 232 s old at idle now, and 87–165 s old under load in part 2. METER-3's per-plug freshness window may need each plug's configured maximum reporting interval, read at adoption, rather than an assumed figure.

The proposal, to weigh: tonight's three findings were each caught by a person reading bytes. A pairing key stayed live for ~21 h and opened ≥ 4 windows with no alarm. A plug went silent ≥ 598.7 s (~10 min) while the core still called it fresh. A plug's reporting cadence hides a 15 s load step. VERIFY-72H (Oct 30 – Nov 2) is where catching by hand stops scaling. An ambitious bar before the run is a bench that attests its own posture:
(a) the pairing window becomes an explicit, time-boxed, event-logged act (opened and closed, with a reason) instead of a config key that re-arms at every boot, and an undeclared `permit_join_opened` is forbidden in boot-health and the nightly;
(b) every metered entity carries a `staleAfter` set from its measured cadence (IR-61), so that `stale` means something;
(c) the runner VOIDs a stale witness (METER-3).
Its instrument, if wanted: re-create tonight's three conditions on the bench (the key present at a boot; a metered plug unplugged past its `staleAfter`; a REP read on a stale witness), and each must turn a scenario red with no human reading. With those in place, the 72-hour verdict, rehearsal 1's packet and the pilot's install all rest on evidence the system asserts itself: the "did it actually confirm" the product promises a household. Under `pilot-first`, (a) would also be how the pilot's devices get paired by hand.
RETURNED _scratch/v81/sat0926/CHAR-sitting-3_return.md 11630
