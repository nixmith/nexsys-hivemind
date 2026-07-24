<!--
file: context/strategy/brand-program/2026-07-23_domain-handle-claims-refresh.md
purpose: Fresh availability screen + claims-state refresh run by the brand-program lane, 2026-07-23 — a NEW dated file per the lane charge (the counsel lane's 2026-07-15 inventory is NEVER edited by this lane; that file remains the counsel-package artifact of record for its date). This file feeds Deliverable 4 (the launch-readiness checklist) and hands the counsel lane fresh receipts.
audience: Nick; the hub; the counsel lane (as input to its next inventory pass).
state-type: lane deliverable (brand-program; screen receipts dated 2026-07-23).
not-a-lawyer: availability screens by a non-lawyer (+AI); registrar-grade confirm required before any spend; nothing here is clearance; no public use of any candidate mark before G-2 (the standing counsel discipline).
method: domains via Google DNS-over-HTTPS (dns.google/resolve, NS records; NXDOMAIN = available-signal, NOERROR = registered; the coromni caveat stands — NXDOMAIN can mask registered-undelegated, confirm at registrar). Handles via direct HTTPS profile probes from the cloud session; several platforms block automated reads (recorded honestly as INCONCLUSIVE, with the one-minute desk check named).
-->

# Domain & Handle Claims Refresh — screens of 2026-07-23

## A. Domains (dns.google NS probes, 2026-07-23)

| Domain | Result 2026-07-23 | Reading | Delta vs the 07-21/07-22 record |
|---|---|---|---|
| **tamoro.com** | NOERROR; dns1/dns2.registrar-servers.com | Still third-party-held (Namecheap-infra NS); brokerage negotiation state unchanged from this vantage (offer $2,995 standing; walk $3,400) | No change — seller silent per v36 beat 2; conversation state is Nick's to report |
| **tamoro.co** | NOERROR; ns73/ns74.domaincontrol.com (GoDaddy family) | Consistent with **Nick's 07-22 purchase** (same registrar family as the owned asimtote set) | Confirms the beat-2 purchase is delegated/live |
| **tamoro.tech** | NOERROR; ns45/ns46.domaincontrol.com (GoDaddy family) | Consistent with **Nick's 07-22 purchase** | Same |
| tamoro.ai | NOERROR; registrar-servers NS (same family as tamoro.com) | Third-party; plausibly the tamoro.com seller's portfolio — ask about bundling at any tamoro.com close | Unchanged |
| tamoro.io | NOERROR; registrar-servers NS | Same note | Unchanged |
| **tamoro.app** | NOERROR; registrar-servers NS | **Newly probed this pass** — also registered, same NS family as tamoro.com (same probable portfolio; add to the bundle-ask list) | New row |
| **tamoro.dev** | **NXDOMAIN** | **Available-signal — newly probed**; ~$10–15; a natural developer-surface domain for a local-first product | New row; cheapest open TAMORO-family item |
| **tamorro.com** (double-r misspell) | NOERROR; ns53/ns54.domaincontrol.com (GoDaddy family) | Registered. GoDaddy shared NS serves millions of domains — this is NOT ownership evidence. **One-minute check: is this already Nick's** (a defensive variant), or third-party? If third-party, the closest misspell is fenced against us | New row; needs Nick's registrar-dashboard glance |
| tamodo.com | NOERROR; ns1/ns2.afternic.com | Afternic-parked; consistent with the 07-22 field screen ($2,195 buy-now priced at beat 2; ruled: zero tamodo spend pre-G-2) | Unchanged |
| veromo.com | **NXDOMAIN** | Historical row only — **VEROMO is DECLINED-CLOSED** (v36 beat 4); recorded for continuity (8th consecutive NXDOMAIN), no action attaches | Unchanged; status closed |

Not re-probed (owned, static): asimtote.com/.io + variants incl. asymtote.com (GoDaddy family; ownership recorded 2026-07-15; registrar/date one-liner still owed to the counsel inventory by Nick).

## B. Handles / namespaces (probed 2026-07-23 — first API/HTTP-grade pass on record)

| Namespace | Result 2026-07-23 | Reading + the action it implies |
|---|---|---|
| **GitHub `tamoro`** | **TAKEN — user account exists** (ID 49267312, zero public repos, dormant-looking) | **Material NEW finding** — prior record assumed unclaimed. GitHub user/org names share one namespace, so an org `tamoro` cannot be created while the user exists. Options, in order: (1) pick a house org pattern now — `tamoro-io`, `tamorohq`, or `gettamoro` — and treat it as the plan of record; (2) post-registration, GitHub's trademark-policy process MAY release a dormant name (counsel-adjacent; not assumed). Decide the pattern BEFORE G-2 day so the 48h claim run doesn't stall on it |
| **YouTube `@TAMORO`** | **TAKEN — channel exists** (channel ID UCZN5sypK_KJk9onnhEAA-jg) | Material NEW finding. Same play: a house suffix pattern (`@tamoro_home`-class, matching the GitHub pattern) chosen ahead of time |
| npm package `tamoro` | 404 — **free-signal** | Bare package name open; the plan of record should still be a SCOPE (`@<org>/…`) matching the GitHub org pattern |
| npm user/org `tamoro` | INCONCLUSIVE (registry user endpoint 401; www profile 403 — automated reads blocked) | One-minute desk check at npmjs.com; claim in the 48h run |
| PyPI `tamoro` | 404 — **free-signal** | Open (contrast: `asimtote` on PyPI is taken — the parent's known collision does not extend to the product name) |
| Docker Hub `tamoro` | 404 — **free-signal** | Relevant: the product distributes as an image; claim in the 48h run |
| X `tamoro` · Instagram `tamoro` · TikTok `@tamoro` · Reddit r/tamoro · LinkedIn company | INCONCLUSIVE — robots/login walls block automated probes from this environment (consistent with every prior pass's "social handles unverified") | The 5-minute logged-in desk check remains the only reliable screen; run it the morning of G-2 day and claim in the same sitting |

## C. What changed vs the record (the deltas that matter)

1. **The bare-name assumption is now falsified in two places** (GitHub, YouTube): the near-zero-organic-presence read that justified deferring handle claims remains true for *web presence*, but the two most build-critical namespaces are occupied by dormant third parties. Cost of the finding: near-zero — and the pattern is now **RULED (Nick, 2026-07-23), sharper than this lane's REC:** the `tamorohq`-class handle is CANONICAL on every social/content platform **uniformly, even where the bare name is free** (uniformity beats opportunism — one handle to print, say, and defend); package registries are the exception and claim the **bare** name (there the handle IS the artifact name); free bare-name socials may be claimed defensively but are never canonical.
2. **tamoro.dev is open** — the only NXDOMAIN in the TAMORO family; trivially cheap; a natural home for docs/developer surfaces later.
3. **tamoro.app joins the seller-portfolio set** — fold into the bundle question if the tamoro.com negotiation closes.
4. **tamorro.com needs a one-minute ownership glance** — if not Nick's, the closest misspell is already fenced against us (accept and move on; the fence was always optional taste).

## D. Standing constraints (unchanged, restated)

Owning domains/handles is fine; **using them publicly before G-2 is gated** (counsel discipline). Every purchase/claim gets registrar, date, price → a log line + a row in the counsel lane's NEXT inventory pass (this file hands receipts; the counsel lane owns its inventory). R-1 HELD: nothing in this file presumes the name — it screens the leading candidate so G-2 day is executable.
