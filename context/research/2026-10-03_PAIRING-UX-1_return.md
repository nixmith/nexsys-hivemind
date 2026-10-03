<!--
file: context/research/2026-10-03_PAIRING-UX-1_return.md
purpose: PAIRING-UX-1 return — field onboarding/recovery vs the seam; `WIZARD:` case (H10); W18 reading.
charter: context/instructions/2026-10-03_research-lane_PAIRING-UX-1_field-onboarding-and-recovery_charter.md
status: RETURNED 2026-10-03 (13:24:18Z = 08:24 CT); read-set 27,420 B; appendix …_PAIRING-UX-1_appendix.md (§A–D; §E cites).
-->

# PAIRING-UX-1 — the field's onboarding and recovery vs our seam

"(r.)" = read 2026-10-03 (UTC); `cr` = community report; (§E) = appendix cite. Claim-register §0 binds: HAS / MISSING stated plainly.

## §0 The card
- **Q1** All four open the window FIRST and tell the user to trigger the device AFTER; only Z2M shows a countdown; only HA/ZHA names interview stages — https://www.home-assistant.io/integrations/zha/ (r.).
- **Q2** None surfaces "returned in pairing mode"; recovery is silent radio rejoin; dark-device timers default to hours (ZHA 7200 s; Z2M 10 min, OFF by default; SmartThings ≈20 min `cr`; Hue undocumented) — https://www.zigbee2mqtt.io/guide/configuration/device-availability.html (r.).
- **Q3** All four say "factory-reset first" in docs; none shows the device's gesture in the add UI; only SmartThings documents REJOIN-then-RESET as an escalation — https://www.samsung.com/sg/support/mobile-devices/overview-of-samsung-smartthings-secure-mode/ (r.).
- **Q4** Failure is a code or a stuck state, never a remedy; ZHA has no failure string; logs one click away only in Z2M — https://raw.githubusercontent.com/home-assistant/frontend/dev/src/panels/config/integrations/integration-panels/zha/zha-add-devices-page.ts (r.).
- **Q5** Installer mode: SmartThings Pro only (B2B, multifamily); pre-paired consumer kits UNFOUND everywhere — https://www.samsung.com/us/business/industries/smartthings-pro/ (r.).
- **Q6** HA and Z2M are LAN-only on day one (HA Cloud $6.50/mo opt-in); SmartThings and Hue are cloud-by-default, free — https://www.home-assistant.io/docs/configuration/remote/ (r.).

## §1 Q1–Q6
### Q1 The add flow
- **HA/ZHA.** "Add device" (step 2), step 3 "Reset your Zigbee devices to factory default settings…" (§0 Q1 URL). UI window `duration: 254`, a spinner, NO countdown, then "Search again" (§0 Q4 URL); stages PAIRED→INTERVIEW_COMPLETE→CONFIGURED→INITIALIZED; QR: action only.
- **Z2M.** "Permit join (All)" opens "for 254 seconds"; "the device can probably be paired by factory resetting it" — https://www.zigbee2mqtt.io/guide/usage/pairing_devices.html (r.). Countdown HAS; state "Interviewing"; install code HAS.
- **SmartThings.** "+" › "Scan Nearby"/QR/brand; step 2 "Make sure the device is put into pairing mode"; step 3 "Wait a few moments… tap Done" — https://support.smartthings.com/hc/en-us/articles/360052390111 (r.). Window length, countdown, stages: UNFOUND.
- **Hue.** QR-first (app 5.38): scan, then "Install and power on your lights. Once installed, tap Next"; "No QR code" → search/serial — https://www.philips-hue.com/en-us/support/connect-hue-product/bulbs-and-lamps (r.). Search length, countdown, stages: UNFOUND.

### Q2 Recovery after power loss
- **HA/ZHA.** Silent rejoin: any frame from a known IEEE flips it available — https://raw.githubusercontent.com/zigpy/zha/dev/zha/application/gateway.py (r.). Unavailable-after default 7200 s mains / 21600 s battery (§0 Q1 URL); "Last Seen" HAS; offline notification MISSING.
- **Z2M.** Availability "default: false"; when on, mains 10 min → ping → `offline`, battery 25 h (§0 Q2 URL). `last_seen` default `disable`; link-key holders rejoin without a window (maintainer `cr`); official "what to do": UNFOUND.
- **SmartThings.** "The Secure Mode toggle blocks or allows insecure ZigBee device rejoin" (§0 Q3 URL). Radio-level health, ONLINE/UNHEALTHY/OFFLINE — https://developer.smartthings.com/docs/devices/health (r.); OFFLINE ≈20 min `cr`; no offline notification `cr`; advice: "Delete and add the device again".
- **Hue.** Power-on behaviour setting HAS; instrument = API `reachable`, default UNFOUND; app 5.47 (Jul 2025) adds a reconnect card to an unreachable light — https://www.philips-hue.com/en-us/support/release-notes/android (r.).

### Q3 "Paired elsewhere" and the reset gesture
- **HA/ZHA.** "will need to be reset… Refer to each device manufacturer's documentation" (§0 Q1 URL); no gesture in the UI; rejoin and reset share one code path; quirks hold signatures, not gestures — https://github.com/zigpy/zha-device-handlers (r.).
- **Z2M.** Gesture library = hand-written Notes per device page; **SNZB-06P24: none** — https://www.zigbee2mqtt.io/devices/SNZB-06P24.html (r.); **Shelly Plug US Gen4: firmware note only** — https://www.zigbee2mqtt.io/devices/S4PL-00116US.html (r.). No rejoin-vs-reset concept; a force-removed device "will still hold the network encryption key" (§E).
- **SmartThings.** Ordered escalation HAS: join mode → "power cycle the device… while the Hub is searching" → "If the above method does not work… perform the reset steps"; "Removing the device from the app is not necessary or recommended" (§0 Q3 URL). Gestures: partner-authored in-app profiles (§E).
- **Hue.** One article: serial-number reset-and-add ("The light will flash, indicating it's been reset"); Dimmer "top and bottom buttons… at least 10 seconds" — https://www.philips-hue.com/en-us/support/article/how-to-factory-reset-philips-hue-lights/000004 (r.). Gesture shown pre-failure: UNFOUND.

### Q4 Failure and remedy
- **HA/ZHA.** No failure string — spinner → `no_devices_found` + "Search again" (§0 Q4 URL); failures show as a stuck "Interview Complete. Configuring." `cr` — https://community.home-assistant.io/t/777247 (r.). "Show logs" toggle HAS.
- **Z2M.** "Failed to interview '…', device has not successfully been paired"; UI "Interview failed"; remedies only in the FAQ — https://www.zigbee2mqtt.io/guide/faq/ (r.); logs one click from notifications.
- **SmartThings.** "Couldn't add device. Something went wrong. Try again later." `cr` — https://community.smartthings.com/t/238793 (r.); no inline remedy; hub logs only via a developer CLI `cr`.
- **Hue.** String UNFOUND; household logs: none.

### Q5 The operator-paired alternative
SmartThings Pro: a "device onboarding application for installers", multifamily, "not intended for single-family homes" `cr` — https://community.smartthings.com/t/280751 (r.). HA, Z2M: none first-party. Hue starter kit: "the Hue app will search for lights"; pre-pairing NOT confirmed — https://www.philips-hue.com/en-us/support/connect-hue-product/starter-kit (r.). Later additions everywhere = the consumer flow (Q1); no installer→household handover documented.

### Q6 Remote access by default
- **HA.** "only listens on your local network"; Cloud "easiest and safest"; VPN "such as Tailscale or ZeroTier One" (§0 Q6 URL); $6.50/mo · $65/yr — https://www.nabucasa.com/pricing/ (r.).
- **Z2M.** Frontend on `0.0.0.0:8080`, `auth_token` "disabled by default"; "Do not expose the frontend publicly"; no VPN guidance — https://www.zigbee2mqtt.io/guide/installation/14_securing.html (r.).
- **SmartThings.** "no subscription fees"; "control… when you are away" — https://www.samsung.com/us/samsung-smartthings/ (r.); the app needs the cloud even on the LAN `cr`.
- **Hue.** Local control offline; "With an account and a Bridge, you'll get access to Out of home control" — https://www.philips-hue.com/en-us/explore-hue/accounts (r.).

## §2 The seam's four targets and the invariant against the field
| Target | HA/ZHA | Z2M | SmartThings | Hue | Our seam note already requires |
|---|---|---|---|---|---|
| 1 reset first, gesture shown | PARTIAL (docs; no UI gesture) | PARTIAL (Notes; SNZB empty) | PARTIAL (docs; partner screens) | PARTIAL (one article) | reset card + gesture first (`seam:52–55`) |
| 2 pair near the hub | PARTIAL (support caveat) | PARTIAL (FAQ) | PARTIAL (one device page) | MISSING | "bring it close" cue (`:57–60`) |
| 3 window first + countdown | PARTIAL (order; no timer) | HAS (254 s countdown) | PARTIAL (order ambiguous) | PARTIAL (order; no timer) | window → "Ns left" → gesture (`:62–66`) |
| 4 stages + actionable errors | PARTIAL (stages; no failure string) | PARTIAL ("Interview failed"; logs) | MISSING | MISSING | stages; remedy + log link (`:68–71`) |
| never a silent blank | MISSING (254 s spinner → blank) | PARTIAL (toasts auto-dismiss) | MISSING | MISSING | progress / next action / remedy, always (`:73–78`) |
| dark device after power loss | 2 h; no notification | OFF by default; 10 min | ≈20 min `cr`; none | `reachable`; reconnect card | IR-117/IR-121: MISSING from us too |

## §3 The case for `WIZARD:` at the mid-point pass (H10; Nick rules, the hub frames)
- **(a) v1-minimal** — four targets, four screens; launch-matrix gestures only. Cost: ~one lane-week after E2 (`seam:86–88`). Risk: the gesture card rests on our own notes — the field has none to borrow (§1 Q3). Buys: what no platform ships — countdown AND a named failure stage with remedy (§2 rows 3–4).
- **(b) operator-paired through the cohort** — joins via `bench.sh permit-join`; the household never sees one. Cost: ~zero build; a visit per device. Risk: every later addition and power-loss return (IR-117: back in pairing mode, no window) needs us; the field's installer path has no handover (§1 Q5). Buys: R6/R7/R8 evidence before a screen is drawn (§4).
- **(c) a later, larger wizard** — gesture library + QR/install-code entry. Cost: several lane-weeks + our own device database. Risk: lands after the cohort's habits form. Buys: target 1 done right (§1 Q3).
- **The case the evidence makes:** (b) through the cohort while **J2 (the core re-admitting a known IEEE) is weighted up** — every platform recovers a powered-off device by silent radio rejoin, not a household gesture (§1 Q2); our IR-117 class instead returns in pairing mode unseen. The field is MISSING a dark-device timer in seconds and any "back in pairing mode — open a window" line; (a)'s first screen starts there, after the cohort's measurements (§4).

## §4 What the cohort's first installs should OBSERVE (pilot zero; installs 1–3)
1. **Window-to-join seconds** — stamp `permit-join` open and `device_announce`; trigger before vs after (field windows 254 s; our SNZB cycle 180 s, IR-117).
2. **Gesture count and kind** — actions until adopted (USB re-seat vs button hold — IR-114).
3. **The first error string a household sees** — verbatim; was a next action beside it.
4. **"Paired elsewhere" if it occurs** — device; what the household did; was a reset shown.
5. **Dark-device detection time** — unplug a mains device; seconds to any visible change on our dashboard; joined or pairing mode on return.

## §5 The W18 reading ("can I see it from work?" on day one)
HA: no — LAN-only until Cloud ($6.50/mo) or a docs-named VPN (Tailscale/ZeroTier); onboarding never asks. Z2M: no — an unauthenticated frontend the docs warn against exposing. SmartThings: yes — cloud-by-default, free, no LAN-only mode. Hue: yes — a Hue account at first launch gives out-of-home control, free. The field splits vendor-cloud vs self-host; a household-kit Tailscale node (W18 rec (b)) is the self-host side's recommended path, made default — {{NAME}}'s layers are not priced here.

## §6 Sources and not-re-executed
All URLs read 2026-10-03; full list in the appendix. **Unfound:** ZHA add-page strings; any documented "returns in pairing mode"; SmartThings scan duration/stages; Hue search length, failure string, time-to-Unreachable. Quotes are near-verbatim (fetch extractor); the lane re-read the strongest directly (ZHA 254/7200; Z2M 254/10 min/off; SmartThings rejoin→reset; Hue reset; HA remote; Nabu Casa price; SNZB-06P24 + Shelly Plug US Gen4 pages).

RETURNED nexsys-hivemind/context/research/2026-10-03_PAIRING-UX-1_return.md 11967
