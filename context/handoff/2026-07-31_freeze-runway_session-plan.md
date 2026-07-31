<!--
file: context/handoff/2026-07-31_freeze-runway_session-plan.md
purpose: The detailed session-dispatch plan, tonight -> THE READ (Aug-16). Authored v42 beat 11 at Nick's ask; superseded by THE LAUNCH-RUNWAY CHARTER at Aug-12-13 (which consumes it + the R-1/R-2/R-3 returns + the strategic seed).
audience: Nick (dispatch), Hub (intake sequencing)
state-type: plan (point-in-time; the spine remains the state of record)
status: ACTIVE until the charter lands
-->

# The Freeze-Runway Session Plan (2026-07-31 → Aug-16)

Every session below is one of four types: **OPERATOR** (Nick's hands — Pi, silicon, captures), **CODER LANE** (a dispatched desk session against a hub-authored instruction), **RESEARCH LANE** (a web-research session against a §R brief — parallel, never blocking), **HUB BEAT** (this orchestrator: intakes, audits, authoring, stamps). The standing laws hold everywhere: lanes commit nothing; the hub audits then orders; tokens travel by path; no attribution trailers; J1 frozen.

## The dispatch map

| # | When | Type | Session | Produces | Gates/feeds |
|---|---|---|---|---|---|
| S-0 | TONIGHT | OPERATOR | The B3 install (return §9): linger enable → night-1 park (`~/nexsys-bench/tools/bench.sh scenario command-s31-settle`) → timer enable | The installed nightly | Feeds S-1 |
| S-1 | Fri Aug-1 AM | HUB BEAT | First-digest intake: paste `~/nexsys-bench/tools/bench.sh digest`; CI check on `60d3ab5` | **H2 cadence half CLOSES · B3 [M] FLIPS** at the ledger | Gates nothing; banks two cells |
| S-2 | Fri–Sat | OPERATOR | **THE CONVERGENT DEPLOY TRIP**: warm rebuild at `60d3ab5` → deploy (core fix + the `4288a9d` FE SPA — charge 4 discharges here) → capture the boot log seed line + re-run the F2 discriminator curl ~15 min post-boot | The deploy captures | Gates S-3; the Hue flips honest-UNAVAILABLE = the discriminator re-read banks |
| S-3 | Weekend evening (REC Sat/Sun) | OPERATOR | **THE ATTENDED EVENING** (one evening, both reps): the F2 rep BOTH directions on the deployed build (SNZB-02P report→AVAILABLE · S31 wall-unplug→offline-within-window→replug→online-on-evidence; the ping arm's first live exercise, grep-visible via `zigbee.availability_ping`) + the B3 §10 rejoin-race rep | The rep evidence | **F2 [M] CLOSES on intake** — the last open non-scheduled MUST |
| S-4 | Launch ANYTIME (this weekend REC) | RESEARCH ×3 | R-1 TECHNICAL · R-2 BRAND · R-3 FRONTIER (the briefs file, §-scoped dispatch lines below) | Three structured returns, landed at `context/research/` | **Due Aug-10** so the charter (S-10) eats them; never block engineering |
| S-5 | Mon–Tue Aug-3/4 | HUB → 2 CODER LANES | The small-fix stack authored + dispatched: (a) STATE-DIALECT core P2 (core lane) · (b) FE-LIVE-V112 (f)/(g) (FE lane, nexsys-frontend) | Two small returns → audits | Queues behind nothing; must land before Aug-8 |
| S-6 | Mid-week | HUB BEAT | THE DOCS-REPO FOLD (INV-SE-02 in-place · Doc 13 §3.2–§3.3 as-built · E3's paragraph) WITH grounding reads | The docs-repo commit order | Deferred-with-reasons since beat 8; dedicated beat |
| S-7 | Mid-week | HUB BEAT | M14 (charge 8, per the v42 brief) | Per the brief | Sequenced after S-5 audits |
| S-8 | Aug-8/9 | OPERATOR | H3 [M] attended (per the gate calendar) | H3 evidence | Banks H3 |
| S-9 | ~Aug-10 | OPERATOR + HUB | **THE DRY-RUN** — a CONFIRMATION pass over the 29 rows (17→by-then ~20 of 21 MUSTs banked; gate-day reads artifacts) | The dry-run record | Names any residue with 4 days of margin |
| S-10 | Aug-12–13 | HUB BEAT | I2 re-sweep · the v42 close-out · **v43 BANKED** · **THE LAUNCH-RUNWAY CHARTER** (deliverable = THE ORDERING, compounds-first; consumes this plan + the strategic seed + the R-returns + the post-gate candidates + the Nick-IRL track) | The charter | The strategic instrument for post-gate |
| S-11 | **Aug-14 EOD** | — | **FREEZE** (no scope past it; holding it IS the executive act) | — | — |
| S-12 | **Aug-16** | OPERATOR + HUB | **THE READ** (go/no-go at the ledger; gate-day reads artifacts, never memories) | The verdict | — |

## The parallelism law

Engineering sessions (S-0..S-3, S-5..S-9) are SEQUENCED — one Coder lane in flight per repo, audits between. Research lanes (S-4) are PARALLEL and non-blocking: they burn Nick's spare compute, never the critical path; a late return simply misses the charter and rides v43. If any engineering session slips, S-4 never inherits its slot — the freeze absorbs slack by dropping S-6/S-7 scope, never by compressing reps or audits.

## The post-gate candidate shelf (charter inputs, NOT pre-freeze work)

Minted and parked, in compounds-first order: (1) availability-history-in-FE on the new `lastEvidenceAt` asset ("last heard 2 h ago" — feeds the explainability hero; the data now persists); (2) the DP-2 stretch as a first-class boot-epoch/health-surface ruling (the OBS-1 sketch); (3) ping-cadence/backoff tuning on accumulated digest ON-latency data; (4) the executor parameters-byte-determinism candidate (CMD-API I5's second half); (5) the carried candidates ledger (04P two-window silicon leg · real-store setAll teeth · FRAME-CTR custody · 0x81/0x82 ruling · IAS dedup posture · StandardExplanationService flattening · LC-LABEL-LOG · EXEC-DETERMINISM).
