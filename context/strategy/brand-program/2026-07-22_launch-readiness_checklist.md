<!--
file: context/strategy/brand-program/2026-07-22_launch-readiness_checklist.md
purpose: Deliverable 4 of the brand-program lane — everything executable within 48 hours of a GREEN G-2 read, sequenced: the domain set, the handle-claim run (fed by the 2026-07-23 claims refresh), the email/DNS plan, and the token-swap map for the dashboard + future site. This is a CHECKLIST for Nick + the hub to execute — the lane orders no commits, no spend, and no public surface; every public-use item stays gated behind counsel's word.
audience: Nick (executes); the hub (sequences the repo-side swaps as WUs).
state-type: lane deliverable (brand-program, authored 2026-07-23 under the 2026-07-22 lane charge).
ruling-fold: 2026-07-23 — the Hour-0 ruling block COLLAPSED by Nick's pre-rulings: Architecture C RATIFIED · engine register = "TAMORO Core" · the house handle pattern RULED (tamorohq-class canonical on EVERY social/content platform, uniform even where the bare name is free; package registries are the exception — npm/PyPI/Docker Hub claim the BARE name, the handle there IS the artifact name; free bare-name socials may be claimed defensively but are NEVER canonical). G-2 day's Hour-0 now requires exactly TWO acts: R-1 itself + the filing go. Results-consult agenda additions approved (public-use definition for parked assets · companion timing · owner-at-filing/LLC · foreign direct-national). Sections below updated to ruled state.
not-a-lawyer: the G-2/public-use gates referenced here are counsel's; where "counsel question" is marked, this lane takes no position. Prices are recorded benchmarks; confirm at spend.
grounding: 2026-07-23_domain-handle-claims-refresh.md (this lane's fresh screen) · 2026-07-15_domain-handle-claims-inventory.md + 2026-07-21_engagement-tracker.md (counsel lane; read, never edited) · 2026-07-11_naming-decision-brief.md §2 (the blast-radius phases + the astro.config sibling-path trap) · v36 beats 2–7 (tamoro.co/.tech bought · Pelton paid, results ~Aug-5 · standard-characters ruling) · the BRAND.productName precedent (dashboard mocks) + {{productName}}/{{companyName}} (the name-tokenized Astro build).
-->

# Launch-Readiness Checklist — the 48 hours after a GREEN G-2

**Trigger:** Nick rules R-1 on the Pelton results (~Aug-5). Everything below is staged NOW so the ruling converts to a claimed, configured, swap-ready brand in ≤48h. Items marked ⛔ are gated on counsel's explicit word about what counts as "public use" — pre-clear that definition at the results consult so the gates are known before the clock starts.

## Hour 0 — the ruling block (Nick, now ~5 min — two of three items PRE-RULED 2026-07-23)

- [ ] R-1 ruled on the Pelton results — **the only ruling left**.
- [x] ~~Architecture~~ **RULED 2026-07-23: Architecture C; "TAMORO Core" engine register** (Deliverable 1 §6).
- [x] ~~Handle pattern~~ **RULED 2026-07-23:** canonical = **tamorohq-class on every social/content platform, uniform even where the bare name is free**; registries (npm/PyPI/Docker Hub) claim the **bare** name; free bare-name socials claimed defensively where cheap, never canonical.
- [ ] The §1(b) filing go given to counsel (standard characters; classes 9+42 per the ruled strategy; the filing itself is counsel's motion, not this checklist's).

## Hours 0–4 — the claims run (Nick, priced, no public use implied)

**Domains** (registrar-grade confirm at checkout; log registrar/date/price per the counsel discipline):

- [ ] tamoro.com — close per the standing doctrine if the negotiation resolves (offer $2,995 standing; walk $3,400; LTO acceptable per the narrowed never-LTO ruling: short-dated-lock only, the two term-checks). If unresolved at G-2: proceed on **tamoro.co as primary** (owned) — the launch does not wait on the .com (the doctrine already priced this: offer stands + silence).
- [ ] tamoro.dev — register (~$12; NXDOMAIN 2026-07-23).
- [ ] At any tamoro.com close: ask the bundle question on .ai/.io/.app (same seller-portfolio NS family).
- [ ] tamorro.com one-minute ownership glance (mine already, or fenced against us — either answer closes the row).
- [ ] Optional misspell fence per taste (tammoro/tomaro-class) — informed by what the Pelton search surfaced (its phonetic sweep is the better fence-picker than another DNS pass).

**Handles** (free; claim-and-park; profiles stay EMPTY/private pre-launch — parking vs "use" is a ⛔ counsel-definition item; the RULED pattern governs every row):

- [ ] GitHub org **`«name»hq`-class (canonical — bare name TAKEN anyway)** · npm org/scope + **bare package name** · **bare** Docker Hub · **bare** PyPI reservation (registries claim bare per the ruling; bare `tamoro` free-signal on all three, 2026-07-23).
- [ ] X · Instagram · YouTube · TikTok · LinkedIn company page (created unpublished) · Reddit — **all at the canonical `«name»hq`-class handle, uniformly**, after the 5-minute logged-in availability sweep; where the bare social name happens to be free, claim it **defensively only** (parked, pointing at canonical, never primary).
- [ ] Log every claim (platform, handle, canonical-vs-defensive, date) for the counsel file's next inventory pass.

## Hours 4–24 — email + DNS foundation (technical, private, no public surface)

- [ ] Pick the mail/primary domain: **tamoro.com if closed, else tamoro.co** (one primary; others redirect later at launch, not now).
- [ ] Mail hosting on the house standard (any of Workspace/Fastmail/Proton — Nick's taste; nothing brand-visible in the choice); create `nick@`, `hello@`, `legal@`, plus a catch-all.
- [ ] SPF + DKIM + DMARC (p=quarantine to start) on day one — the domain's mail reputation starts aging immediately, which is the point of doing this inside the 48h.
- [ ] ⛔ NO public web content on any brand domain (parked/blank is fine; the site ships `noindex` regardless until the W-5 publish gate) — what counts as "use" is counsel's line; default-conservative until stated.
- [ ] DNS hygiene: registrar lock, 2FA, auto-renew ON for the whole family (both registrar accounts), CAA records optional-later.

## Hours 24–48 — the token-swap map (the hub sequences; explicit-paths commits per the standing ABSOLUTE rule; this lane orders none of it)

The controlling design fact: **nothing public has shipped and every name surface is already tokenized** — so the "rename" is a value flip plus a bounded masthead sweep, exactly as the naming brief priced it.

| # | Surface | The swap | Owner | Trap notes |
|---|---|---|---|---|
| 1 | Dashboard (web-ui) | `BRAND.productName` token value → the ruled name (ONE source of truth; no literal enters any component — grep-guard `TAMORO\|Tamoro` in src/ must return only the token definition) | FE lane (rides FE-VERDICT-2 or its own micro-WU) | Verify the token is still the only name source at swap time (preflight Check-8 style) |
| 2 | Marketing site (Astro) | `{{productName}}`/`{{companyName}}` values → ruled name / "Asimtote" (the W-7-successor footer line per the ruled architecture) | Website lane | **The astro.config sibling-checkout path trap** (naming brief §2 Phase-1): any repo rename breaks the token/font import path — same-change fix |
| 3 | Docs-repo masthead | The RATIFIED watermark line + design-doc headers pass (content untouched; one M-pass commit) | Hub | Phaseable; not launch-blocking |
| 4 | Repo names (`homesynapse-core`, `nexsys-*`) | → the ruled-org equivalents, migrated to the claimed GitHub org | Hub, dedicated WU | GitHub auto-redirects; CI badges/remotes + the astro path ride the same change; NOT inside the 48h unless Nick wants it — Phase-1-before-public-surface is the real gate |
| 5 | Distribution artifacts (systemd unit, env prefix, deb name, install paths) | One coordinated rename WU, gated install-smoke-green (H3 discipline) | Hub/Coder | Explicitly OUTSIDE the 48h; before first public artifact |
| 6 | Java namespace `com.homesynapse.*` | **DEFERRED out of v1 entirely** (the naming brief's Phase-2 REC stands; serialization-embed audit before any future attempt) | — | Do not let launch adrenaline pull this in |
| 7 | Hivemind/skills vocabulary (`nexsys-*` skills, lane boilerplate) | Rolls forward at natural currency passes, no big bang | Hub | The skills' rename-readiness sections already anticipate the flip |

## The standing gates (restated so the checklist can't outrun the law)

1. **R-1 is the trigger, not this file.** Nothing above runs early except what is explicitly pre-G-2-safe and already ruled (the tamoro.com doctrine, which stands on its own).
2. **No public use of any candidate mark before counsel's word** — claims yes, use no; the parked-profile line is counsel's to draw (⛔ items).
3. **Every commit is explicit-paths from a stated census** (Nick's absolute rule while multiple writers are live); this lane's files enter the tree only through the hub's audit of the lane return.
4. **The E3 public statement is hub-owned** — launch-day communications are not in this checklist's scope.
5. If G-2 reads **adverse**, this checklist survives intact: only §Hours-0-4's domain rows change target (the fallback branch re-screens per the ruled adverse instrument), and every token-swap row is name-agnostic by construction.
