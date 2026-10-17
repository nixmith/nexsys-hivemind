<!--
file: context/research/2026-10-23_LICENSE-1_the-line-before-the-flip_return.md
purpose: LICENSE-1 return: the H10, four tables, the flip checklist, the signing checklist. Read-only on core@176adad, docs@e2a5844, hivemind @ce84c07; web read 2026-10-15. No legal advice (questions for counsel). No name.
status: RETURNED Thu 2026-10-15 (date -u at start 14:02:50Z = 09:02 CT)
-->
# LICENSE-1 — the line before the flip

## §0 The H10
```
ESCALATION TO NICK — LICENSE-1 (one word by Nov 2; the flip, Nov 3-9, is one-way)
LICENSE: a | b | c
(a) Apache on the whole core, engine private forever. COST low: the consent as drafted already says this. RISK low-med: a published engine later needs a new consent; anyone may host the core (as in b). BUYS household: all of it free, forkable, patent-licensed (§3); company: the cleanest story, the mark (§6), a private engine.
(b) Apache on the household core + a source-available engine (FSL-1.1-ALv2, §2), own repo, from commit 1. COST low now (re-scope the UNSIGNED consent), med later (2nd approval; inbound-grant rule). RISK med: two regimes; open-core suspicion (DCO on the core answers it). BUYS household: same as (a), 0 files move; company: a publishable engine no rival may host, each version Apache 2 years on, never a relicense.
(c) Docs first, defer. COST med: Nov 19-25 installs would run a tree whose LICENSE:4-6 prohibits "use ... without the express written permission of NexSys" (Q-C4). RISK med: the LOCKED decision unexecuted; "free and open" stays false (COMMERCIAL-1:53). BUYS option value; a published doc's grant is NOT retractable (CC BY 4.0 §2(a)(1) "irrevocable"; Apache §2), so HORIZON-1 :559's "cost nothing to retract" holds for the page only.
(b) TESTED (§1 T1-T6): passes at the bytes (0 cross-home code; seam = read API + site-scoped tokens + home_id) and the license (Apache §4 last ¶); FAILS at the instrument as drafted: the consent approves Apache for "the Company's public software releases, including ... homesynapse-core and any successor repositories" (DRAFT:28-32), i.e. (a).
Recommendation: (b), the consent scoped to named repositories BEFORE signing; FSL-1.1-ALv2 for the engine; DCO on the core.
Refutable-by: counsel reads OA §VIII(4)'s "successor license" as one approval only (OA amendment: a now, b later) · the engine is never to be published (b = a) · the Dec 1-14 re-read finds no engine buyer (keep the scoped consent; defer the engine's).
Blocking: the flip only (the order: §6).
```

## §0b The premise table, re-run (ClaudeFolder, 14:03Z)
| # | Pasted output | Reading |
|---|---|---|
| 1 | `176adad` · `Copyright (c) 2026 NexSys. All rights reserved.` | ✓ HEAD = 176adad869cb…; tree clean |
| 2 | `0` | ✓ 0 of 1,267 `*.java` (0 files of any type) |
| 3 | `83` · `43:[libraries]` | ✓ same via `git show 176adad:` |
| 4 | `2026-08-28_DRAFT_confirmatory-IP-assignment_NDS-to-NexSysLLC.md` · `2026-08-28_DRAFT_written-consent_successor-license_Apache-2.0.md` · `finance` · `trademark` | ✓ both line 1 "DRAFT — FOR COUNSEL REVIEW — NOT EXECUTED"; signature lines blank |
| 5 | `3` · `27` · `43` | ✓ :43 is the OA sentence (§6) |
| 6 | `12` | ✗ partial: the §2 line is :38 "No fragment…" (capital N; `-i` gives 12, 38, 53) |
| 7 | `211` | ✓ the row; its (a)/(b)/(c) as written head §1 (HORIZON-1 return :559 adds "(a) … the fleet engine and graders stay private forever") |

## §1 The three options at the bytes
IR-200 as written: "(a) Apache on the whole core; (b) Apache on the household core + source-available on the fleet/multi-site engine from its first commit; (c) design docs first, defer".

| | (a) Apache all; engine private | (b) Apache household core; FSL engine, own repo | (c) docs first, defer |
|---|---|---|---|
| the 22 `settings.gradle.kts` projects + build-logic, distribution, scripts, docs, specs, spike | Apache-2.0 | Apache-2.0 (household core = 100 % of today's tree) | proprietary (LICENSE:1) |
| The engine (COMMERCIAL-1 §2 items 3-4, :35-36) | private: not a "public release" (the OA's words) | own repo, FSL-1.1-ALv2 from commit 1 | undecided |
| Gives away | host/fork/sell the core, no network clause (§2); LLC patent claims "necessarily infringed by their Contribution(s)" (§3), ended for a licensee who sues | same; the engine readable, usable except a Competing Use, Apache 2 years later per version | the docs |
| Keeps | the mark (§6), the hosted tier, corpus + graders (A1, private `nexsys-bench`) | same + 2 years per engine version with no competing hosted rival | everything |
| One-way after release 1 | each released version, forever ("perpetual … irrevocable") | same + each engine version's future grant ("irrevocably") | the docs' grant |
| Instrument | the consent as drafted | consent re-scoped + a 2nd approval at the engine's first public commit | a permission per household |

**(b), tested. T1 bytes:** 0 cross-home code at 176adad (the 15 source files matching `fleet|multi-site|tenant` mean the in-home device fleet or T2's hook); nothing to carve out. **T2 seam:** already in the core: `ApiKeyClaims(List<String> scopes, String siteId)` (`api/rest-api/…/ApiKeyClaims.java:39`; :15-19 "the per-scope / per-site authorization model (the enterprise tier) can be layered on additively"), `home_id` on every event (AMD-34; `Main.java:92-95`); Doc 16 SP6 (docs `design/16-superior-automation.md:41`): "a licensing + API tier over the identical HomeSynapse Core runtime, not a fork and not a feature-gate on the core". The engine is a client of the read API, the backup copy and A1's graders: its own repo (HORIZON-1 :120 "a second repo"). **T3 one repo:** lawful (Elasticsearch@v7.10.2 `LICENSE.txt`: Apache-2.0 default, "Elastic Licensed code is found only in the x-pack directory"; pnpm@ecd3d289: MIT root, `pnpr/LICENSE.md` PolyForm Shield) but not chosen: Spotless, `moduleGraphAssert` and DCO would split by directory, and Elastic's 2021 move of that code to SSPL/ELv2 (`LICENSE.txt`@0144bdff) is the rug "core forever" forbids. **T4 license:** Apache §4 last ¶ "may provide additional or different license terms and conditions … for any such Derivative Works as a whole". **T5 instrument:** FAILS as drafted; passes with §6's scope edit. **T6 contributions:** FSL's future grant is the licensor's; outside engine code needs an inbound grant (Sentry's, §3) or stays out.

## §2 The source-available choice for (b)'s engine
| License | The clause that does the work | Forbids | OSI | Change date | Precedent |
|---|---|---|---|---|---|
| PolyForm NC 1.0.0 | "Any noncommercial purpose is a permitted purpose." | all commercial use | no | none | EPPlus Software · `EPPlusSoftware/EPPlus`@f00956b7 `license.md` (v5+; sells commercial licenses) |
| FSL-1.1-ALv2 | "A Permitted Purpose is any purpose other than a Competing Use." + "the Apache License, Version 2.0 that is effective on the second anniversary of the date we make the Software available" | a commercial product/service substituting for it or "any other product or service we offer using the Software", or offering "the same or substantially similar functionality" | no | 2 years per version → Apache-2.0 | Sentry · `getsentry/sentry`@de75b8dd `LICENSE.md` ("FSL-1.1-Apache-2.0") |
| BUSL-1.1 | "make non-production use of the Licensed Work. The Licensor may make an Additional Use Grant" | production use beyond the grant | no ("is not an Open Source license") | Licensor's date ≤ 4 years; Change License GPL-2.0-or-later-compatible (Covenant 1) | IBM · `hashicorp/terraform`@9ec49e06 `LICENSE` (4 years → MPL 2.0) |
| Elastic-2.0 | "You may not provide the software to third parties as a hosted or managed service, where the service provides users with access to any substantial set of the features or functionality of the software." | hosting; license-key circumvention; removing notices | no | none | Elastic · `elastic/elasticsearch`@0144bdff `LICENSE.txt` |
| SSPL-1.0 | §13 "you must make the Service Source Code available via network download to everyone at no charge, under the terms of this License" | hosting unless the whole service stack is published | no | none | MongoDB · `mongodb/mongo`@995f294b `LICENSE-Community.txt` |

OSI: `isOsiApproved=false` for all five, `true` for Apache-2.0 (SPDX License List 3.29.0, `spdx/license-list-data`@31ba1a50). **Fit: FSL-1.1-ALv2:** it permits internal use and "professional services that you provide to a licensee", forbids only a substituting commercial service, and each version lands in the household's license after two years. ELv2 and SSPL never convert (SSPL reaches the whole service stack); BUSL needs four parameters per release; PolyForm NC, the OA's default (§6), bars the engine's buyers (installers, property managers) from commercial use.

## §3 The precedents, pinned
| Project | `LICENSE` @ revision | NOTICE / headers | CLA / DCO | Trademark | Sells |
|---|---|---|---|---|---|
| Home Assistant core | `LICENSE.md` Apache-2.0 @4edec269 (2026-10-15) | none; no per-file header | `CLA.md`: DCO-derived, "modified to explicitly use the Apache 2.0 license and not mention sign-off" | the Open Home Foundation's "trademarks and guidelines" | Home Assistant Cloud (Nabu Casa): remote access, Google Assistant, Alexa, Assist TTS/STT; "Subscriptions also help fund the development of Home Assistant itself" |
| Zigbee2MQTT | `LICENSE` GPL-3.0 @344b6e03 (master; COMPARATOR-1's pin) | none (`lib/controller.ts` opens with imports) | none in `CONTRIBUTING.md` | none found | nothing; a PayPal donate badge (`README.md:26-27`) |
| openHAB core | `LICENSE` EPL-2.0 @992cae35 | `NOTICE` (987 B); per-file header `licenses/epl-2.0/header.txt`, ending "SPDX-License-Identifier: EPL-2.0" | DCO 1.1 sign-off (`CONTRIBUTING.md:82-104`) | the marks "are valuable assets of the openHAB Foundation" (effective 2023-03-01) | nothing (foundation) |
| Hubitat | platform closed; `hubitat/HubitatPublic`@96789818: no LICENSE | 21 of 38 `.groovy`: "Copyright … Hubitat Inc. All Rights Reserved" | — | not read | hubs; Hub Protect ("cloud backup and ongoing warranty"); Remote Admin ("optional monthly subscription") |
| Sentry | `LICENSE.md` FSL-1.1-Apache-2.0 @de75b8dd | none; FOSSA checks on PRs | PR "Legal Boilerplate": "Sentry can use, modify, copy, and redistribute my contributions, under Sentry's choice of terms" | "Sentry is a registered Trademark of Functional Software, Inc." | hosted plans: "one free Developer plan and three paid plans: Team, Business, and Enterprise" |
| Elastic | `LICENSE.txt`@0144bdff: AGPL-3.0-only / SSPL-1.0 / ELv2 by header, ELv2-only in x-pack | per-file headers | CLA: "not asking you to assign copyright to us, but to give us the right to distribute your code without restriction" | elastic.co/legal/trademarks | Elastic Cloud; self-managed subscriptions |

**COMMERCIAL-1 §3, re-pinned.** Q1: HA@4edec269 is Apache-2.0; Nabu Casa sells the Cloud: §2's shape, a convenience (not the record) behind the tier. Q4: HA's trace code is Apache-2.0 (A1's graders may borrow it with notices); Z2M is GPL-3.0 (copied code in a distributed engine would carry it); openHAB is EPL-2.0 (file-level). Q2, Q3 are not license questions: open, not answered from memory.

## §4 The dependency set and its notices
Direct runtime deps from the build files at 176adad; transitives from each upstream's POM/build file at its release tag (GitHub). Maven Central refused this lane (proxy 403; robots for the fetcher): no jar opened.

| Dependency | License (source) | Flag | NOTICE lines it brings |
|---|---|---|---|
| Jackson core, databind, annotations, jsr310, blackbird 2.18.6 + dataformat-yaml (via networknt, BOM-aligned: `jackson-bom/base/pom.xml:195-215`) + snakeyaml 2.3 | Apache-2.0 | — | "Copyright 2007-, Tatu Saloranta"; core's FastDoubleParser 1.0.90 (MIT, "Copyright © 2023 Werner Randelshofer"), crediting fast_double_parser "BSL License" (= Boost BSL-1.0, not BUSL), fast_float (MIT), bigint (BSD-2-Clause) |
| snakeyaml-engine 2.9; javalin 6.7.0; logstash-logback-encoder 8.0 (+ MIT `LogstashBasicMarker`; shades lmax disruptor 3.4.4); ethlo itu 1.10.3 | Apache-2.0 | — | none |
| sqlite-jdbc 3.51.3.0 | Apache-2.0; `LICENSE.zentus` BSD-style ("Copyright (c) 2006, David Crawshaw"), packed by its pom | — | "This product includes the following softwares developed by David Crawshaw. See LICENSE.zentus file." (its last line is cut mid-word) |
| Jetty 11.0.25 ×14 (server, http, io, util, servlet, security, webapp, xml + 6 websocket) | "EPL-2.0 OR Apache-2.0" (`header-template.txt`) | CHOICE → Apache-2.0 | "Eclipse Jetty, and Jetty are trademarks of the Eclipse Foundation."; UnixCrypt (jetty-util): "Copyright 1996 Aki Yoshida, modified April 2001 by Iris Van den Broeke, Daniel Deville … provided that the copyright notice appears in all copies." |
| jetty-jakarta-servlet-api 5.0.2 (repackages jakarta.servlet-api 5.0.0) | `NOTICE.md` "EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0"; `LICENSE.md` EPL-2.0 or Apache-2.0 | FLAG, the Java EE line: elect EPL-2.0 (named by both; ASF Category B) | the Eclipse trademark line |
| kotlin-stdlib(-jdk7/-jdk8) 1.9.25 + jetbrains annotations 13.0 (`stdlib/jvm/build.gradle:89`) | Apache-2.0; parts from GWT/Guava (Apache), Boost (BSL-1.0) | — | jar unread |
| logback-classic/-core 1.5.32 | "Eclipse Public License v2.0 … or (per the licensee's choosing) … GNU Lesser General Public License version 2.1" | CHOICE → EPL-2.0 (LGPL is ASF Category X) | — (Q-C6) |
| json-schema-validator 1.5.6 | Apache-2.0 | — | "JSON Schema Validator Copyright (c) 2016 and onwards Network New Technologies Inc."; "Apache Commons Validator Copyright 2001-2023 The Apache Software Foundation" + the ASF "This product includes software developed at" line |
| jSerialComm 2.11.2 | "either the Apache Software License, version 2, or the GNU Lesser General Public License … version 3 or above" | CHOICE → Apache-2.0 (`libs.versions.toml:70`) | "Fazecast jSerialComm Copyright (C) 2012-2022 Fazecast, Inc." |
| slf4j-api 2.0.17; preact 10.29.3, uplot 1.6.32 (`package-lock.json`: the only non-dev packages) | MIT ("Copyright (c) 2004-2023 QOS.ch"; "… 2015-present Jason Miller"; "… 2022 Leon Sorokin") | — | — |
| Inter subset (blob f9c2ea32, 25,388 B) | OFL-1.1, no Reserved Font Name (`rsms/inter`@v4.1) | FLAG: keeps name ID 0 (copyright), drops 13/14 (license): ship the OFL text (condition 2) | — |
| the `.deb`'s jlinked JDK 21 (`control.in:15-16`; Corretto in CI, `build-image.sh:67`) | GPL-2.0 + "CLASSPATH" EXCEPTION; jlink keeps `runtime/legal/*/` (checked with `build-image.sh:119-124`'s flags) | FLAG: GPLv2 §3 source obligation (Q-C6) | — |

Test and dev dependencies are not distributed. After the four elections no jar is GPL/AGPL/LGPL-only; the runtime is GPL-2.0 with the Classpath exception (flagged).

**The NOTICE lines** (the `.deb`'s; ASF practice bubbles up a bundled Apache dependency's NOTICE, infra.apache.org/licensing-howto): the LLC's · Jackson + FastDoubleParser · sqlite-jdbc · jSerialComm · json-schema-validator + Commons Validator · Jetty's two. MIT/BSD/OFL/EPL texts go to LICENSE-side pointers ("Do not add anything to `NOTICE` which is not legally required"). Whether §4(d), worded for "Derivative Works", reaches an aggregate `.deb` is Q-C7; including them is the conservative reading. Source tree: the LLC's line only.

## §5 The flip, as one card (`F` = the flip commit)
1. `LICENSE` ← the Apache-2.0 text verbatim. `git show F:LICENSE | md5sum` = `3b83ef96387f14655fc854ddc3c6bd57` (11,358 B; today 802 B).
2. Java: the Spotless string (`build-logic/…/homesynapse.java-conventions.gradle.kts:109-114`) → `SPDX-License-Identifier: Apache-2.0` + `Copyright $YEAR <holder>`; `spotlessApply` (1,225 files). It skips package-info/module-info (`LicenseHeaderStep.java:196-197`, spotless@gradle/7.0.2): hand-edit those 40 (31 old header, 1 "NexSys Technologies", 8 none) + 2 in the unincluded spike. `git grep -L 'SPDX-License-Identifier: Apache-2.0' F -- '*.java' | wc -l` = 0.
3. `*.kts` (30), `*.ts`/`*.tsx` (88), `*.sh` (19): prepend a line by script (5 kts and 83 ts/tsx open with a comment a Spotless delimiter rule would replace). `git grep -L SPDX-License-Identifier F -- '*.kts' '*.ts' '*.tsx' '*.sh' | wc -l` = 0.
4. Never touch V001-V005: "a changed byte in V001–V005 is a stopped core, not a migration" (`MigrationBytesPinTest.java:33-35`); V002-V005 line 1 says "All rights reserved". `git diff --quiet F^ F -- core/persistence/src/main/resources/db/migration/events/`; `git grep -l 'All rights reserved' F | wc -l` = 4, those four (today 1,283; Q-C8).
5. `NOTICE`: source = "HomeSynapse Core" / "Copyright 2026 <holder>"; `.deb` = that + §4's blocks. `dpkg-deb -c *.deb | grep -c usr/share/doc/homesynapse/NOTICE` = 1.
6. `usr/share/doc/homesynapse/copyright` in DEP-5 (`Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/`; `Files: *` Apache-2.0; stanzas per §4; `runtime/*` GPL-2.0 with Classpath exception → `runtime/legal`), "neither be compressed nor be a symbolic link" (Policy §12.5), by one `cp` in `build-deb.sh`. `dpkg-deb -c … | grep -c usr/share/doc/homesynapse/copyright` = 1; lintian (`build-deb.sh:105-107`) without `no-copyright-file`.
7. `THIRD-PARTY-NOTICES` from the real closure (re-derive: `./gradlew :app:homesynapse-app:dependencies --configuration runtimeClasspath`) + preact/uplot, Inter's OFL (ship `fonts/OFL.txt`), FastDoubleParser, LICENSE.zentus, EPL-2.0. Entries = `JAR_COUNT` (`build-image.sh:90-91`) + the bundle's.
8. `web-ui/dashboard/package.json:7` "UNLICENSED" → "Apache-2.0". `git show F:web-ui/dashboard/package.json | grep -c '"license": "Apache-2.0"'` = 1.
9. Docs `LICENSE` (277 B, "… NexSys Technologies. All rights reserved."): **Nick's question: CC BY 4.0 or Apache 2.0.** CC suits prose ("CC licenses may be used for software documentation") but "Patent and trademark rights are not licensed under this Public License" (§2(b)(2)); the repo holds code too (`website/site/`); COMMERCIAL-1 A4 says "the same Apache 2.0". Lean: Apache-2.0. `git show <docs-F>:LICENSE | head -1`.
10. **DCO, not a CLA.** Apache §5 already makes inbound = outbound; a DCO never gives the LLC a right to relicense outside code, so "never a license rug" is structural (HA's CLA is DCO-shaped; openHAB signs off; a CLA let Elastic relicense contributors' code in 2021). `CONTRIBUTING.md` (DCO 1.1) + a CI step failing a commit without `Signed-off-by:`. `git log --format='%(trailers:key=Signed-off-by,valueonly)' <first-public>..HEAD | grep -c .` = the commit count (today 5 of 281). The (b) engine: Sentry's inbound grant, or no outside code.
11. Trademark sentence (README + NOTICE): "The Apache License 2.0 does not grant permission to use the trade names, trademarks, service marks, or product names of NexSys LLC (Apache-2.0 §6)." No product mark; the v82 HEADERS-1 text `Copyright The {{NAME}} Authors` (`planning/2026-09-27_v82_…:75`) cannot ship before the written opinion. The docket's three name tokens: 0 hits in tree, messages, `-i -S` history (both repos; today 0·0·0); re-run at F, which publishes 281 + 158 commits.
12. README (replaces `:407-415` and the header sample `:366-374`): "## License — Apache License 2.0; see LICENSE and NOTICE. Copyright 2026 <holder>. Contributions under DCO 1.1 (`git commit -s`). No trademark rights (§6)." `git grep -c Proprietary F -- README.md` = 0.

## §6 The signing checklist (counsel's wave; N1)
**The OA sentence** (entity posture :43): *"All public releases of Company Software shall be under the PolyForm Noncommercial 1.0 license (or successor license approved by the Member)."*
**Consent DRAFT** (1,995 B): :4-5 "to be executed only at (or before) the public-launch license change, and only on counsel's confirmation"; :28-32 Apache 2.0 approved "as the successor license … for the Company's public software releases, including the repository homesynapse-core and any successor repositories"; blanks: date, signature (:42-46). **Assignment DRAFT** (2,768 B): :26-30 "irrevocably assigns … all right, title, and interest, worldwide" in what was "created by Assignor for the HomeSynapse/NexSys project, whether created before or after July 17, 2025"; :32-39 five repos, the website, a catch-all; :41-43 copyrights, patents, trade secrets, trademarks; blanks: two dates, two signatures (:54-64). The lane's reading, not advice: Apache needs the LLC to hold what it grants (§2; §3 "licensable by such Contributor").
**Under (b), the OA sentence standing:** a consent scoped to the household repos leaves a later public engine release on the OA default, PolyForm NC, until a second approval names FSL; the consent as drafted displaces PolyForm for all public software, so a source-available engine needs a superseding consent. Either way the household flip is not blocked.
**Questions for counsel:**
- Q-C1 Does "successor license" (singular) allow per-repository and later approvals, or does (b) need an OA amendment?
- Q-C2 Should :28-32 name repositories (homesynapse-core; docs if Apache) instead of "… and any successor repositories"?
- Q-C3 Are design documents "Company Software"? Does CC BY 4.0 for them need approval?
- Q-C4 Is a private install in two households a "public release"? Before the flip, does each need written permission under LICENSE:4-6?
- Q-C5 Assignment: is a "good and valuable consideration" recital right for a Louisiana act? Record it with the Copyright Office? Could another employer or institution claim enumerated work? Do AI co-author trailers (4 core commits) change what it conveys? Sign it before the consent?
- Q-C6 The `.deb` ships GPL-2.0-with-Classpath-exception binaries (GPLv2 §3: source, or a "written offer, valid for at least three years") and EPL-2.0 jars: which statements must ship?
- Q-C7 Does §4(d) reach an aggregate `.deb`, or only Derivative Works?
- Q-C8 Holder: core "NexSys", docs and one fixture "NexSys Technologies", the entity NexSys LLC: which goes in LICENSE/NOTICE/headers? Do the pinned migrations' "All rights reserved" lines need more than the top-level LICENSE?
- Q-C9 Which counsel? The trademark practice is "limited to federal trademark matters", so Q8 (the consent; the assignment) "returns to the company track" (PELTON ruling §3 item 7, :44).
**Order:** counsel's review → sign the assignment → sign the consent (dated on or before F) → counsel's receipt → the flip card → the first public commit (the strategy of record :59: assignment → consent → flip).

## §7 What the lane did not read
The jars (Maven Central closed; their NOTICE files inferred from the tags) and a resolved Gradle tree (§5.7) · snakeyaml's Bitbucket tags (GitHub mirror HEAD read) · gnu.org, openjdk.org (fetch errors; GPLv2 §3 and the Classpath exception read in the lane's jlinked OpenJDK 21.0.12 `legal/java.base/LICENSE`, not Corretto's) · the built bundle (no `dist/`) · Hubitat's trademark policy; HA Cloud's price · IR-138 (:149) and IR-184 (:195): no license content.

## Prior art (each read 2026-10-15)
Apache-2.0 (2004) https://www.apache.org/licenses/LICENSE-2.0 · PolyForm NC 1.0.0 https://polyformproject.org/licenses/noncommercial/1.0.0 · FSL-1.1-ALv2 https://fsl.software/FSL-1.1-ALv2.template.md · BUSL-1.1 https://mariadb.com/bsl11/ · ELv2 (2021) https://www.elastic.co/licensing/elastic-license · SSPL v1 (2018) https://www.mongodb.com/licensing/server-side-public-license · SPDX list 3.29.0 (2026) https://github.com/spdx/license-list-data · DEP-5 1.0 https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/ · Policy ch. 12 https://www.debian.org/doc/debian-policy/ch-docs.html · DCO 1.1 (2004, 2006) https://developercertificate.org/ · ASF LICENSE/NOTICE https://infra.apache.org/licensing-howto.html · ASF categories https://www.apache.org/legal/resolved.html · CC BY 4.0 https://creativecommons.org/licenses/by/4.0/legalcode · CC FAQ https://creativecommons.org/faq/ · OFL-1.1 (2007) https://openfontlicense.org/open-font-license-official-text/ · GPL-2.0 (1991; fetch error) https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt · HA Cloud https://www.home-assistant.io/cloud/ · WWHA https://works-with.home-assistant.io/resources/wwha-compliance-guide/ · openHAB (2023) https://www.openhab.org/about/trademark.html · Hubitat https://docs2.hubitat.com/services/hub-protect , https://docs2.hubitat.com/services/remote-admin · Sentry https://sentry.io/legal , https://docs.sentry.io/pricing/legacy-pricing/ · Elastic https://www.elastic.co/brand , https://www.Elastic.Co/pricing/faq/licensing · EPPlus https://www.epplussoftware.com/en/Home/LgplToPolyform · pnpr https://pnpm.io/pnpr/license · repos: as pinned in §1-§4.
RETURNED nexsys-hivemind/context/research/2026-10-23_LICENSE-1_the-line-before-the-flip_return.md 24894
