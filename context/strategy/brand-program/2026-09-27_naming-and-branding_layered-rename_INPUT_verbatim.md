<!--
file: context/strategy/brand-program/2026-09-27_naming-and-branding_layered-rename_INPUT_verbatim.md
purpose: INPUT to the brand program, filed VERBATIM by the v83 hub at beat 3 (Sun 2026-09-27 ~17:3x CT): a research return Nick brought to the hub (another session's analysis — "Nothing was written to your folders … treat this as input to the brand program rather than a ruling"). It proposes the three-layer rename model (brand surfaces · public engineering names · permanent protocol constants), names the two rename traps (the integration-ID hash namespace; the migration checksums), reads NEXSYS's registrations and the public-release blocker (the file headers), and gives a read on Asimtote as a parent name. Its claims are INPUT: the hub's two-layer read of them is `2026-09-27_v83_NAME-ARCHITECTURE_hub-read.md` beside this file; nothing here is a ruling (rulings are Nick's words in a DR). The candidate name appears here as it does in the record's own brand-program files; THE PREMISE (D-v80-3) governs every OUTWARD text and every code token (`{{NAME}}`), not this directory.
audience: the hub (the strategy pass, Tue 2026-09-29) · Nick · counsel (the parts marked for counsel)
state-type: research input (verbatim; not a ruling)
status: FILED — v83 beat 3. Body byte-identical to the file Nick attached (sha256 of the body below in the hub-read).
-->

1. PALOKI: keep the plan, rename once, in layers

The filing is set up correctly. NEXSYS LLC is the right applicant. If the LLC changes its name later, you record the change with the USPTO; you don't refile. Don't let the company question delay the filing.

Don't rename the knowledge base. Your record's rule that history is never rewritten is right: archives, beats and locked docs keep "HomeSynapse." The private repos (nexsys-hivemind, -bench, -skills) can keep their names as internal codenames. Renaming them would touch thousands of path references and change nothing a customer sees.

The real design problem is that "homesynapse" shows up as three kinds of identifier, each with its own cost curve:

Layer	In the code today	When it gets expensive	What to do
Brand surfaces	BRAND.productName, website, READMEs	Never (one token)	Flip at its protocol row (already in the runbook)
Public engineering names	.deb package name, /var/lib·/etc·/opt·/var/log/homesynapse, homesynapse.yaml, homesynapse-events.db, homesynapse-token, X-HomeSynapse-* headers, homesynapse.local/problems/, com.homesynapse.*	At the pilot's first install (Nov 25), the first outside plugin (contributions open at the license change), the first Maven publish	Rename in the Nov 3–9 rename work unit, before the pilot, or keep permanently. Never "later."
Permanent protocol constants	The integration-ID hash namespace; migrations V001–V005	Already	Never rename; lock them with tests

The two traps, confirmed by reading the source:

Integration IDs. IntegrationIds.deriveStable hashes "homesynapse:integration:" + type to make every integration ID. Change that string and every ID changes, which orphans the Device.integrationId rows exactly as the class comment warns. The existing tests compute IDs through the same function, so CI would stay green while the bench fleet lost command routing.
Migrations. All five applied migrations carry "HomeSynapse Core / … NexSys" in their header comments. MigrationRunner checksums the raw file bytes and halts on any change. A rename sweep, or the license-change header rewrite, that touches V001–V005 stops every existing database from booting.

Worth doing now (no name involved):

Two small tests that lock the literal "zigbee" integration ID and the SHA-256 of V001–V005.
The read-only rename census the hub offered on 09-26 (D-v81-3), using these three layers as its columns.

Smaller findings:

Error-type URIs. The dashboard's contract.ts hardcodes the homesynapse.local/problems/ prefix, so renaming those URIs has to change the frontend and backend together.
The view-position header. The dashboard never reads X-HomeSynapse-View-Position; only comments in fixtures mention it. The same value already travels in the ETag and meta.viewPosition, so you could drop the header instead of renaming it.
paloki.com. Maven Central only grants a com.paloki namespace after a DNS check on paloki.com. The registry still shows Atom.com as registrar, Atom's parking nameservers, and a last change of 2026-03-26. That's consistent with holding it at the marketplace, but confirm the registrant is NEXSYS LLC and turn on 2FA and auto-renew (it expires 2027-03-14).
homesynapse.com. Keep it renewed and redirecting (expires 2027-07-14). Shipped code sends users to homesynapse.com/docs/storage, and a lapse would hand that link to a squatter.
GitHub. paloki is taken by a dormant personal account, so pick the organization-name variant on the day the application is filed. If you rename nexsys-io rather than moving repos out of it, anyone can claim the old name, so keep it as an empty placeholder.
Greek. The earlier language screen didn't cover Greek. παλούκι (pa-LOO-kee) means "stake" and, colloquially, "a hard slog." It's one vowel off: a marketing note for Greece, not a legal issue.
Wordmark. Never let the design split the word at the L (Pa·Loki, PaLoki, a color break). The earlier screen's argument about Grafana's LOKI mark depends on PALOKI reading as one invented word, and your dashboard sits right next to logs.
2. NexSys: right instinct, but it will become blocking

I checked today: there are six live NEXSYS registrations. Four are in Class 9: EnerSys (batteries), Lakewood (programmable controllers), Crest Audio (monitoring software) and Applied Avionics (switches and sensors). TSMC holds one covering Classes 40/42. There's also a dead Tyco NEXSYS for building-automation hardware and software. It can't be your public name; as a private legal name it's harmless.

It stops being private in three places:

The public repo. About 1,200 files say Copyright (c) 2026 NexSys, and the core repo lives at github.com/nexsys-io. At the license change (Nov 3–9), that becomes permanent public git history.
The App Store. Apple displays the legal entity as the seller and doesn't accept DBAs.
Customer paperwork. Terms of service, the privacy policy and invoices all name the legal entity.

Recommendation: separate the name from the code now, rename the company later.

Pick the file-header format now. Use SPDX-License-Identifier: Apache-2.0 with either Copyright The Paloki Authors (the Linux Foundation's recommended form) or no per-file copyright line at all (Apache's own policy keeps it in the NOTICE file). The company name then lives in at most one file, and "not blocking" becomes true. Copyright notices aren't required to keep ownership.
When you rename, amend the existing LLC. That means:
a name-change filing on geauxBIZ (guides quote $75–150)
your fraud-protection (SBF) PIN approval
the same EIN, with a letter to the IRS
the bank
a change-of-name recording at the USPTO
the domain registrations and the state contact email, which is currently on nexsys.io
Don't form a new company and move PALOKI into it before you file the statement of use. An intent-to-use application assigned to anyone other than a successor to the ongoing business is void.
Rename when the first of these happens: an App Store listing, the public install flow or first sale, a standards-body membership, or the first investor conversation.
3. Asimtote: my take

Your record has used it as the working parent name since June. The July brand-architecture ruling made it the quiet parent. The August entity ruling deliberately kept the LLC as NexSys. The clearance brief drafted for counsel in July was never sent.

For it:

It fits where the company is going. Your research tracks (runtime enforcement, Simplex, shields, capability substrates) and the Substrate Thesis describe "accountability infrastructure for other people's intelligence." That audience reads names more than it hears them. A separate parent name also keeps the company from being tied to home products.
There's precedent in your exact field. Home Assistant is the product and Nabu Casa is the company. When Home Assistant moved into the Open Home Foundation in April 2024, that was clean only because product and company had different names.
The trademark screens are clean today. There are no ASIMTOTE hits, and no live ASYMPTOTE registration in Class 9 or 42. The live ones are D. E. Shaw (financial services, Class 36) and Asymptote Genetic Medicines (pending, biology). You also own the .com and .io.

Against it:

Pronunciation. The dictionary says "AS-əm(p)-tote." Your "ay-sim-toat" follows asymmetric, which shares the same Greek "a-" meaning "not," but it separates the sound from the word the name is built on. Your June and July memos assumed "AS-im-tote" or "a-SIM-tote," so three readings are now in play. Choose one deliberately. If you want the meaning to come across when people hear it, say it the dictionary way.
It looks like a misspelling to the very readers it's aimed at. It's one letter off Romanian asimptote and close to Indonesian/Turkish asimtot.
The handles are taken. GitHub asimtote is an individual's personal account. On PyPI, asimtote is an active Cambridge tool that even uses your metaphor ("will probably never ever get there").
It has never been cleared. Asimptote B.V., a Dutch thermodynamics-software company, is one letter away and also in software. That's the key question for counsel.

A note for a formal-methods audience: "approaches but never touches" is false for horizontal asymptotes; sin x/x crosses y=0 infinitely often. The exact version is the vertical asymptote that a barrier function places at the edge of the safe set, which is literally your L1 story. Tell it that way.

Verdict: keep Asimtote as the working parent name, and run three checks before amending the LLC:

Say your chosen pronunciation to ten people and have them spell it, then show ten others the spelling and have them say it.
Run a USPTO/EUIPO trademark knockout search, and ask Pelton (your trademark firm) for a separate quote on the July clearance brief.
Pick one handle variant and use it everywhere.

If the checks come back clean, rename the LLC in place when the first trigger arrives. If they don't, "Paloki LLC" costs nothing, but it ties the company to home products.

I'm not a lawyer, so counsel should confirm the entity and trademark mechanics. Nothing was written to your folders. Your record keeps naming rulings out of chat, so treat this as input to the brand program rather than a ruling. Want me to turn it into a doc for the next hub session?

Sources:

EnerSys NexSys® batteries
Trademarkia searches: NEXSYS · ASYMPTOTE · ASIMTOTE · PALOKI (an aggregator, not clearance)
Merriam-Webster: asymptote
LSJ: παλούκι
PyPI: asimtote
asimptote.com
GitHub: asimtote · paloki
GitHub: renaming an organization
Maven Central: register a namespace
Linux Foundation: copyright notices
ASF source-header policy
Apple Developer enrollment
Announcing the Open Home Foundation
TMEP 502.02(a) · TMEP 501.01(a) · 15 U.S.C. §1060
Louisiana LLC name change: LLC University · Northwest Registered Agent
Registry records: paloki.com · homesynapse.com · asimtote.com