<!--
file: context/audits/2026-10-09_HERO-U2a_return.md
purpose: The HERO-U2a lane return — the recovery card designed in DESIGN MODE: SPEC.md, FIELDS.md, states.html, README.md under homesynapse-core/web-ui/dashboard/design/recovery-card-v1/; the §0 card (census, P1–P5, defaults, the NOT-ON-WIRE list, the questions), then §1–§4 as the charter §3 names them.
audience: the hub (audits at the bytes; cuts AVAIL-API-1 from FIELDS.md) · Nick (rules on SPEC §12 in one batch)
state-type: lane return (frontend; design mode)
status: RETURNED Fri 2026-10-09 (instrument 2026-10-09T22:29:40Z at start; CT = UTC−5 → 2026-10-09). Baseline homesynapse-core HEAD da9ca3d on main; the FE mirror v1.1.5.
-->

# HERO-U2a — return

## §0 The card
- **Instrument limit.** Shell on Nick's computer (`git show`, `grep`, `sed`, `date -u`); the mockup rendered headless in the lane's container to check it; no `npm`, no gate, no Java, nothing installed.
- **Census (`homesynapse-core/web-ui/dashboard/design/recovery-card-v1/`):** `SPEC.md` 43,228 B · `FIELDS.md` 4,039 B · `states.html` 69,788 B (no script, no external resource) · `README.md` 1,234 B. Nothing else written; no git verb run.
- **P1 — HOLDS.** FIELDS.md tags every field the card reads (IN-MIRROR 5 + two joins · ON-WIRE-NOT-IN-MIRROR 3 · NOT-ON-WIRE 10) with a `file:line` cite at `da9ca3d`; SPEC §3 reads only those.
- **P2 — HOLDS.** `grep -ril` for any name but `{{NAME}}`: 0 files. `{{NAME}}` sits in the mock's header only; no card string carries it (Register C — SPEC §12 Q1).
- **P3 — HOLDS.** `git status --porcelain -- web-ui/dashboard/src` empty at start and at close; `src/` was never in the write-set.
- **P4 — HOLDS, three findings.** (a) The wire carries the reason name LOWER-CASED, not the NAME (`ZigbeeIntegrationAdapter.java:2080–:2081`; `AvailabilityReason.java:10–:12`), and the cite `:27–:46` misses a sixth value, `LEAVE` `:48–:49`. (b) "Quiet = AVAILABLE + PING_SUCCESS": a reply to a device that stays AVAILABLE publishes nothing (`StandardAvailabilityTracker.java:599–:600`) — the signature exists only on an UNAVAILABLE→AVAILABLE edge; steady-state Quiet needs the probe keys. (c) The seed's `unknown` seeds UNKNOWN (`:284–:291`), which the sweep probes (`:465–:467` skips only UNAVAILABLE; `:477–:487`); the never-asked class is the device seeded UNAVAILABLE (IR-112 arm (a)) — on the wire UNAVAILABLE + null reason + null `lastSeenAt`, or UNKNOWN (`StateProjection.java:1115`). Every other cite in the charter holds.
- **P5 — HOLDS.** The fifth state's label is "Not heard from since startup (not asked)" — the verb "not asked" against R3's "no answer" — and `states.html` shows the two side by side (section "P5"), question mark vs two outgoing arrows, unknown vs error hue.
- **Defaults taken:** Register C card copy (no "we", no name); 254-s window; "Not responding" in the error register; the passive Quiet row sayable only with a declared interval; the `leave` reason renders the bare label; the S1 dark form drops the parenthesis and says "not shown here yet".
- **NOT-ON-WIRE (from FIELDS.md §3):** `reportIntervalSeconds` · `silenceLimitSeconds` · `lastProbeOutcome` + `lastProbeAt` · `probeMisses` · `availabilityClass` · (no key: seeded-never-asked = `lastProbeAt` null ∧ UNAVAILABLE) · `integrationId` · `ieeeAddress` · the open-window read (a separate unit) · the join moments (B1, not a key).
- **Questions for Nick:** SPEC §12 Q1–Q8 (§3 below); two block build row 3 only (Q3, Q6); none blocks rows 1–2.

## §1 What was designed; the defaults (one line each)
- One component on three surfaces (device row · entity detail · the why-not card under "Watching"), two disclosure levels, one act; `stale` never on the card (SPEC §6 B moves the pill to the value cell).
- The five rows with the open-vocabulary arm, each × three stages (S1 four mirror keys · S2 the mirror bump · S3 AVAIL-API-1), every cell a sentence or an honest "not sayable" naming what shows instead.
- The contract sentence per class in Register C ("This plug reports at least every 10 minutes. After 11 minutes of silence it is asked."), the floor form, the passive form, the class-unknown fallback.
- The act's seven moments as full copy (before · open with the countdown · the gesture card per class, "no steps yet" where the record has none · a foreign joiner turned away · rejoined · closed with nothing · the failed request), each surface twice (today / once the keys land).
- Copy table: 61 keys, every string graded (≤ 9.6; longest sentence 16 words; zero banned-list hits); a11y pairs computed in both themes (all ≥ 4.5:1); five distinct glyphs; tokens by name, no token request.
- Defaults: Register C; 254 s; error hue for dark rows; passive Quiet gated on a declared interval; `leave` → bare label; S1 dark form without the parenthesis.

## §2 Coverage and the counts
- State table: 6 rows × 3 stages = 18 / 18 cells filled (three are honest "not sayable" cells: R2 S1, R4 S1, R4 S3's null-interval arm).
- FIELDS.md: IN-MIRROR 5 (+ the `name` / `triggerRef` joins) · ON-WIRE-NOT-IN-MIRROR 3 · NOT-ON-WIRE 10 (the hub's six gaps: 1, 2, 3, 4, 6 CONFIRMED; 5 CONFIRMED as a gap, REFUTED as a separate key and re-sourced; plus `integrationId`, `ieeeAddress`, the window read, the join moments).

## §3 The questions for Nick (SPEC §12)
Q1 Register C vs the charter's "we" / `{{NAME}}` wording — rec (a) Register C; no block. Q2 the window length — rec 254 s; no block. Q3 the dashboard's first write (the client is GET-only, `client.ts:22`) — rec (b) ship the card read-only first, the act as its own reviewed unit; blocks row 3. Q4 the passive Quiet threshold (the sensor declares none, IR-121) — rec (a) only with a declared interval, (c) declare it per class later; no block. Q5 the restart ambiguity (seeded-dark keeps the old reason, never re-asked) — rec (a) S3's `lastProbeAt` null flips to the fifth state; (c) one probe at boot raised to the hub; no block. Q6 scope by IEEE (additive `ieeeAddress`) vs `deviceId` on the POST — rec (a); blocks row 3. Q7 gesture cards with no steps (Shelly Gen4 · TR3 · S31 Lite; the Hue has a fact, no steps) — rec "no steps yet" + a bench card per class; no block. Q8 "Not responding" in the error hue — rec (a); no block.

## §4 The next recommended lane (refuse to close)
**HERO-U2b — the mirror bump + the card on mocked fields** (SPEC §11 rows 1–2): `availabilityReason · lastSeenAt · link` into `contract.ts` as optional additive keys under the tri-state law with a fixture from a real `/api/v1/entities` row (never from the Java record — IR-89), then `RecoveryCard` on the S1/S2 columns with the §7 catalog test-locked and the three surfaces swapped; row 3 (the act) waits on Q3/Q6; row 4 waits on AVAIL-API-1, which the hub cuts from FIELDS.md §3. Observation for the hub, outside this lane: one probe at boot for a seeded-dark mains device would retire the fifth state on silicon (Q5 (c)). Verification register: DESIGN-ONLY — nothing here touched a wire.

RETURNED nexsys-hivemind/context/audits/2026-10-09_HERO-U2a_return.md 7189
