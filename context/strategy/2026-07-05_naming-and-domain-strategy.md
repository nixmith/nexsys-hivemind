# Naming & Domain Strategy — evaluation of your candidates

**Date:** 2026-07-05 (rev. 2 — updated: you own `asimtote.com` + variants)
**Brief:** product + parent split · exact-match `.com` is a hard requirement · pressure-test `asimtote` against your new ideas (Acemtote, Coromni).
**Method note:** domain status checked live via Google DNS-over-HTTPS (registry delegation = registered; NXDOMAIN = unregistered). Strong signal, **not** a registrar guarantee or legal clearance — confirm at a registrar and run formal trademark clearance before you spend.

---

## TL;DR recommendation

1. **Parent company → `Asimtote`.** You already own `asimtote.com` + the variants, which removes the only thing that was blocking it — and it's the stronger name: it carries a real, ownable story, a positive morpheme ("Asim" = guardian/boundless), and a metaphor that *is your product's thesis* (§1a). Acemtote drops to a clean fallback.
2. **Product → realize your "core" idea as a branded house off the parent.** The cleanest expression of what you described (a coined parent + a "core" product that generalizes to home / ecosystem / enterprise) is **Asimtote Core / Asimtote Home / Asimtote Enterprise** — zero new domains, zero new trademarks, all on a domain you already own. **Drop `Coromni`** (its `.com` is taken and it sits one letter from the game *Coromon*).
3. **The open risk is no longer domains — it's the code namespace.** `asimtote` on PyPI is taken (the Cambridge tool). Settle a package/org namespace strategy before any audience builds on you (§6).
4. Your exact-`.com` requirement remains empirically well-justified (§3).

---

## 1. Verdict on your three names

| Name | Role | Linguistic / brand | `.com` | Collisions | Verdict |
|---|---|---|---|---|---|
| **Asimtote** | parent | Strong, ownable coinage; on-metaphor; positive "Asim" morpheme. One real weakness: cold radio/spell test (mitigable — §5). | ✅ **you own it** (+ `.io` + variants) | Active Cambridge `asimtote` dev tool (PyPI/GitLab, adjacent infra); `asimptote.com` energy-sim firm | **Recommended parent.** The domain question is closed; the remaining work is namespace, not naming. |
| **Acemtote** | parent | Clean/ownable but sacrifices the asymptote story + "Asim" meaning; pronunciation less obvious. | ✅ available (`acemtote.com`) | None found | **Fallback** — only if you ever want to drop the asymptote lineage (and its radio-test baggage) entirely. |
| **Coromni** | product | "cor"(core)+"omni" is a nice idea, but "core" is buried and "omni" is TM-dense. | ❌ **taken** (registered, dead NS) | **Coromon** (popular Steam game) one letter away; "Yardi Corom" (real-estate SaaS) | **Drop it** — fails `.com` + consumer-confusion risk. |

### 1a. The asymptote metaphor is a brand asset — lean into it

An asymptote is a curve that **approaches an ideal ever more closely but never claims to have reached it.** That is, almost exactly, your product's entire thesis: a home system that gets ever more reliable and *never reports a confirmation it doesn't actually have* — the honest "sent, not confirmed" instead of the optimistic lie. Most coined names are empty vessels you have to fill with meaning over years; **`Asimtote` arrives pre-loaded with the right one.** That's a rare and real advantage, and a reason to keep it over the meaning-free `Acemtote`.

---

## 2. The domain reality (live check, 2026-07-05)

**Yours already:** `asimtote.com`, `asimtote.io`, + variants — the parent brand's domains and misspelling fence are handled. That's a meaningful head start.

**Available if you want a distinct product brand (`.com`, unregistered):**

- `emberkor.com` ✅ — ember (hearth/heart-of-home) + kor (core); warm + infrastructural. Watch: brushes *Ember.js* (dev framework).
- `koridel.com` ✅ — clean, softer coinage.
- `acemtote.com` ✅ — your parent fallback.

**Taken / parked / for-sale:** `coromni.com` (registered, broken NS) · `coromon.com` (the game) · and 12/14 "cor/kor" coinages I probed — `coreon` `korveo` `corvane` `corelith` `kordyn` `coranova` `kordwell` `corelume` `koradia` `korhaven` `corvana` `corehearth` (several parked *for sale*).

**Takeaway:** clean short `.com`s in the "core" space are picked over — which is a strong argument for **not** buying a separate product domain at all when you already own `asimtote.com` (see §4).

---

## 3. Why "exact `.com`" is the right requirement (the evidence you asked for)

For a *trust* brand maturing prosumer → mainstream → B2B, the data backs your instinct:

- **~92% of people default to `.com`** on recall; `.io` ≈ **28%**. Users are **~3.8× more likely** to assume `.com`.
- **62%+ of funded startups still choose `.com`;** it carries maximum credibility across all audiences.
- `.io`/`.ai` are fine *within technical circles* (no SEO/fundraising penalty) but underperform on mainstream trust — your maturation target.
- Google ranks TLDs equally; the gap is trust + click-through, not ranking.

Net: prioritize exact `.com` — and value it above any specific string. You've already satisfied this for the parent by owning `asimtote.com`.

---

## 4. Brand architecture — answering "is a product-family even necessary?"

Your instinct (a core that extends to home / ecosystem / enterprise) is a **branded house** — one brand, descriptive extensions. Right model. And now that you own `asimtote.com`, the cheapest *and* cleanest realization is to hang the product line directly off the parent:

```
Asimtote  (parent + brand — the entity, the GitHub org, the domain you own)
   ├── Asimtote Core        the local-first engine (the moat)
   ├── Asimtote Home        the consumer smart-home product/app
   ├── Asimtote Pro         prosumer tier
   ├── Asimtote Enterprise  the B2B / multi-site "ecosystem core"
   └── Asimtote Hub / Bridge   hardware, when it comes
```

- Your "home vs generalized vs enterprise cores" become **editions of one brand** — descriptor words you never trademark or domain separately. Closest analog to what you're building: **Ubiquiti → UniFi** (one brand extends into Network / Protect / Access).
- **Each *new coined* name is a recurring tax** (fresh trademark clearance + `.com` + code/social namespaces + audience re-education). You've paid it once, for Asimtote. Don't pay it per segment.
- Hardware and future software slot in as descriptors — no new brand required.

**This directly answers your uncertainty:** you very likely do **not** need a second fanciful product name. `Asimtote Core` *is* the "smart home core," and it generalizes for free.

---

## 5. The product name — do you still want a distinct one?

Two lanes, now that the parent is settled and owned:

**A. Ride the parent (recommended, cheapest).** `Asimtote Core` / `Asimtote Home` / `Asimtote Enterprise`. Zero new domains or marks; it uses the equity of the name you're already building; it fits your launch audience (prosumers / HA-refugees read receipts and are comfortable with coined infra names). A warmer sub-brand can always come later *if* you push mainstream.

**B. A distinct, warm consumer product brand (optional).** Keep Asimtote as the (semi-invisible) parent and give the consumer product its own clean-`.com` coinage — your original Coromni instinct, done on an available domain. Live options: `emberkor.com`, `koridel.com`, or I run a bigger vetted-`.com` batch to your taste. Only worth it if you want warmth that "Asimtote Home" can't carry.

**My lean: A now, B later.** It matches your brand docs (parent carries the weight; product is what strangers touch) and keeps you from paying the coined-name tax twice before you have two products.

---

## 6. The real open item: namespace strategy (not domains anymore)

Owning the domains closes the domain question. The Asimtote risk that remains is **developer namespace**, and it matters because your audience installs packages and clones repos:

1. **PyPI `asimtote` is taken/active** (Cambridge Cisco-config tool, on the *same* asymptote metaphor). Plan a **distinct distribution name** or a scope — don't fight for the bare name.
2. **Verify + claim** the `asimtote` **GitHub org**, an **npm scope** (`@asimtote/*`), and social handles (X, LinkedIn, YouTube). *(I couldn't confirm these this pass — inconclusive fetches; it's the next screen.)* Then migrate off the `nexsys-io` / `nixmith` orgs.
3. **Radio-test mitigations** (your June note): pick one house pronunciation, spell-on-air in any audio, and always pair the logotype with spoken/marketing moments.
4. **Formal clearance before spend:** USPTO/EUIPO/WIPO on `Asimtote` in Classes 9 / 35 / 42; document the common-law `asimtote`/`asymptote` uses.

---

### Sources
- Domain status: Google Public DNS (`dns.google/resolve`), 2026-07-05.
- `asimtote` PyPI/common-law collisions: your `asymptote-name-recommendation.md` (12 Jun 2026).
- `.com` vs `.io` evidence: aggregated startup-domain studies (recall/memorability, funded-startup TLD share, trust-by-audience).
