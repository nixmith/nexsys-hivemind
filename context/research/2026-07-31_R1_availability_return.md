<!--
file: context/research/2026-07-31_R1_availability_return.md
purpose: R-1 TECHNICAL lane return. Availability-truth landscape across competing platforms + our stack's near-term ground. Feeds THE LAUNCH-RUNWAY CHARTER (Aug-12-13).
audience: Nick (intake), Hub, charter authors
state-type: research-return
status: DELIVERED
lane: R-1 TECHNICAL
brief: context/instructions/2026-07-31_research-lanes_R1-technical_R2-brand_R3-frontier_briefs.md §0 + §R-1
executed: 2026-07-31
-->

# R-1 TECHNICAL — Return

**Executed 2026-07-31.** All citations carry a source date where determinable and an access date of 2026-07-31. Every URL cited was opened; pages that could not be read are named as such and routed around rather than summarized.

## Method and honesty notes (read before §1)

- **Five sub-lanes ran in parallel**, one per question, each search-first and epistemically labelled per §0. Their returns are reproduced below with light editorial integration.
- **A verification pass was run after the lanes returned.** Four load-bearing claims were independently re-fetched and confirmed: the ZHA `self._available: bool = False` initialisation, the Zigbee2MQTT `isAvailable()` read-time predicate, the OPC UA "stale data can be detected by the client looking at the timestamps" quote, and the SQLite WAL-reset bug entry. **The verification pass materially corrected §4c** — see the correction box there.
- **Access failures to report.** Reddit was proxy-blocked for the whole session, so §2 contains **no Reddit exhibits** (this is R-2's ground anyway, but note the gap). `ci.openhab.org` is robots-disallowed, so the openHAB negative in §5 is capped at MED. GitHub renders issue timestamps client-side, so GitHub issue dates in §2 are inferred from in-page version strings and labelled as such. Several Silicon Labs and Ignition pages 404'd or served inconsistent `latest` aliases; each is flagged inline.
- **Confidence discipline.** Negative/absence findings (§3 Pass C, §5) are capped at MED per §0's absence-of-evidence rule, and each carries a search-work log so a reader can judge how hard the lane looked.

---

## §1 — Availability semantics in the field

**Terms used throughout.** *Evidence-based* = the platform requires positive, recent evidence of liveness before asserting available; absence of evidence yields not-available. *Assumption-based* = available is the default/sticky state, and only an affirmative failure or a long timeout flips it. A third category emerged and is used below: *evidence-derived-but-write-cached* = liveness is computed from a timestamp, but the result is frozen into a boolean flag on a background cadence rather than derived at read time.

### 1.1 Home Assistant — ZHA path

ZHA's availability logic now lives in the split-out `zigpy/zha` library; `home-assistant/core`'s ZHA integration is a thin consumer of it.

**Entity-level: HA just mirrors the library.**

```python
@property
@override
def available(self) -> bool:
    """Return entity availability."""
    return self._zha_state.available
```

— **FACT / HIGH.** [`homeassistant/components/zha/entity.py`](https://raw.githubusercontent.com/home-assistant/core/dev/homeassistant/components/zha/entity.py) — `dev` branch as read, accessed 2026-07-31. Availability arrives as a diff on `subscribe_state(...)` and is written through `async_write_ha_state()`. So HA holds a **cached flag**, not a derivation.

**Device-level: the `available` property is a conjunction, and the device starts NOT available.**

```python
@property
def available(self):
    """Return True if device is available."""
    return self.is_active_coordinator or (self._available and self.on_network)
```

and in `__init__`:

```python
self._available: bool = False
self._checkins_missed_count: int = 0
self._on_network: bool = True
```

— **FACT / HIGH — independently re-verified 2026-07-31.** [`zha/zigbee/device.py`](https://raw.githubusercontent.com/zigpy/zha/dev/zha/zigbee/device.py) — `dev` branch as read, accessed 2026-07-31. This is the single most consequential finding on ZHA: **a freshly constructed ZHA device is unavailable until something proves otherwise.** That is an evidence-based initial posture and it is the closest any surveyed platform comes to our stance.

**The check itself: passive last-heard first, active probe as a fallback.**

```python
async def _check_available(self, *_: Any) -> None:
    # don't flip the availability state of the coordinator
    if self.is_active_coordinator:
        return
    if self.last_seen is None:
        self.debug("last_seen is None, marking the device unavailable")
        self.update_available(False)
        return

    difference = time.time() - self.last_seen
    if difference < self.consider_unavailable_time:
        self.debug(
            "Device seen - marking the device available and resetting counter"
        )
        self.update_available(True)
        self._checkins_missed_count = 0
        return

    if self._gateway.config.allow_polling:
        if (
            self._checkins_missed_count >= _CHECKIN_GRACE_PERIODS
            or self.manufacturer == "LUMI"
            or not self._endpoints
        ):
            ...
            self.update_available(False)
            return
        ...
        res = await safe_read(
            basic, [ATTR_MANUFACTURER], allow_cache=False, only_cache=False
        )
        if res.get(ATTR_MANUFACTURER) is not None:
            self._checkins_missed_count = 0
```

— **FACT / HIGH.** Same file. `_CHECKIN_GRACE_PERIODS = 2`. Reading it:

- **Signal that marks a device "seen":** `last_seen`, maintained by zigpy on any received frame. Purely passive.
- **Active probe:** yes, but only *after* the passive threshold is blown — a non-cached read of the Basic cluster `manufacturer` attribute. A successful read resets the miss counter; it does **not** directly set available — availability still flows back through `last_seen` on the next pass. **INFERENCE / HIGH.**
- **Hard-coded vendor carve-out:** `self.manufacturer == "LUMI"` skips probing entirely and goes straight to unavailable — Aqara/Xiaomi devices are known to drop off the network when polled.
- **Kill switch:** the entire probe branch, and the entire checker, is gated on `allow_polling`. **FACT / HIGH.**

**Cadence and defaults.**

```python
class DeviceAvailabilityChecker:
    _REFRESH_INTERVAL = (30, 45)
    ...
    @periodic(_REFRESH_INTERVAL)
    async def check_device_availability(self):
        if self._gateway.config.allow_polling:
            await gather_with_limited_concurrency(
                20,
                *(dev._check_available() for dev in self._gateway.devices.values()
                  if not dev.is_coordinator),
            )
        else:
            _LOGGER.debug("Device availability checker interval skipped")
```

— **FACT / HIGH.** [`zha/application/helpers.py`](https://raw.githubusercontent.com/zigpy/zha/dev/zha/application/helpers.py) — `dev` as read, accessed 2026-07-31. The `(30, 45)` tuple is a randomized **seconds** range (**INFERENCE / HIGH**, from the start-up log line "started device availability checker with an interval of %s seconds"); concurrency capped at 20 in-flight checks.

```
CONF_DEFAULT_CONSIDER_UNAVAILABLE_MAINS = 60 * 60 * 2    # 2 hours
CONF_DEFAULT_CONSIDER_UNAVAILABLE_BATTERY = 60 * 60 * 6  # 6 hours
```

— **FACT / HIGH.** [`zha/application/const.py`](https://raw.githubusercontent.com/zigpy/zha/dev/zha/application/const.py) — `dev` as read, accessed 2026-07-31. Corroborated user-side: "Consider mains-powered devices unavailable after" = `7200` s, "Consider battery-powered devices unavailable after" = `21600` s, `0` disables the check — [Zigbee Home Automation — Home Assistant](https://www.home-assistant.io/integrations/zha/) — undated docs page, accessed 2026-07-31.

**Field reality check.** A user report against HA Core 2024.8.0 says the flip to unavailable does not fire on its own: *"For the 'Unavailable' check to occur, I have to enter into the 'Configure' menu for my coordinator and click the 'Update Configuration' link at the bottom of the form to manually kick off the logic."* A ZHA maintainer responds asking whether restarting HA or reloading ZHA surfaces the transition. — **FACT / MED** (the report is FACT; whether it is a general defect or a local misconfiguration is NOT ESTABLISHED). [ZHA Not Flagging Devices as Unavailable after Set Times · Issue #123425](https://github.com/home-assistant/core/issues/123425) — opened 2024-08, accessed 2026-07-31.

**Net ZHA characterization (OPINION / MED-HIGH):** the *form* is evidence-based — starts unavailable, derives from `last_seen`, probes on doubt — but the *thresholds* (2 h mains, 6 h battery) are long enough that within any operationally interesting window the reported state is an assumption. A mains-powered relay that dies at 09:00 is still reported ALIVE at 10:59.

### 1.2 Home Assistant — Zigbee2MQTT path

**Off by default.** *"Availability is disabled by default. You must explicitly enable it: `enabled: true`."* — **FACT / HIGH.** [Device Availability | Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/configuration/device-availability.html) — undated docs page, accessed 2026-07-31. Corroborated by the settings schema: `enabled` — "Enable availability checks" — **default `false`, restart required** — [All settings | Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/configuration/all-settings.html) — undated, accessed 2026-07-31.

**Active vs passive classification is derived from the Zigbee node descriptor, not configured:**

```typescript
private isActiveDevice(device: Device): boolean {
    return (
        (device.zh.type === "Router" && device.zh.powerSource !== "Battery") ||
        (device.zh.powerSource !== undefined && device.zh.powerSource !== "Unknown" && device.zh.powerSource !== "Battery")
    );
}
```

— **FACT / HIGH.** [`lib/extension/availability.ts`](https://raw.githubusercontent.com/Koenkk/zigbee2mqtt/master/lib/extension/availability.ts) — `master` as read, accessed 2026-07-31.

**The availability predicate is a pure read-time function of last-seen — no stored flag:**

```typescript
private isAvailable(entity: Device | Group): boolean {
    if (entity.isDevice()) {
        const lastSeen = entity.zh.lastSeen ?? 0;
        return Date.now() - lastSeen < this.getTimeout(entity);
    }
    ...
}

private getTimeout(device: Device): number {
    if (typeof device.options.availability === "object" && device.options.availability?.timeout != null) {
        return utils.minutes(device.options.availability.timeout);
    }
    return utils.minutes(this.isActiveDevice(device) ? settings.get().availability.active.timeout : settings.get().availability.passive.timeout);
}
```

— **FACT / HIGH — independently re-verified 2026-07-31.** Same file. **This is the closest match in the field to our "derive staleness at read time" claim**, and §3 treats it as a named counter-example. `Date.now() - lastSeen < timeout` is computed at call time; the ping merely refreshes `lastSeen` upstream in zigbee-herdsman rather than setting a separate liveness bit (**INFERENCE / MED-HIGH** — zigbee-herdsman's `ping()` was not opened).

**The active probe, with its retry asymmetry:**

```typescript
const available = this.lastPublishedAvailabilities.get(device.ieeeAddr) || this.isAvailable(device);
const attempts = available ? 2 : 1;
...
await this.publishAvailability(device, !pingSuccess);
```

— **FACT / HIGH.** Same file. A device currently believed available gets **2** ping attempts (3 s apart) before demotion; one already believed offline gets **1**. Backoff on failure: `currentBackoff * (available ? 1.5 : 2)`.

**What it publishes:** topic `<friendlyName>/availability`, payload `{"state":"online"|"offline"}`, **retained, QoS 1, publish-on-change only** (`if (!forcePublish && this.lastPublishedAvailabilities.get(entity.ID) === available) return;`). On an offline→online edge it calls `retrieveState(entity)` to re-read `state`, `brightness`, `color`/`color_temp`. — **FACT / HIGH.**

**Documented defaults** — [All settings | Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/configuration/all-settings.html), accessed 2026-07-31 — **FACT / HIGH**:

| key | description (verbatim) | default |
|---|---|---|
| `availability.enabled` | "Enable availability checks" | `false` |
| `availability.active.timeout` | "Time after which an active device will be marked as offline in minutes" | `10` |
| `availability.passive.timeout` | "Time after which an passive device will be marked as offline in minutes" | `1500` (= 25 h) |
| `availability.active.max_jitter` | "Maximum jitter (in msec) allowed on timeout…" | `30000` |
| `availability.active.backoff` | "Enable timeout backoff on failed availability pings (x1.5, x3, x6, x12...)" | `true` |
| `availability.active.pause_on_backoff_gt` | "Pause availability pings when the backoff multiplier reaches over this limit…" | `0` |

**Passive devices are never pinged** — battery devices only get the 25 h passive timeout. — **FACT / HIGH.**

**Config surface churn:** Z2M 2.0.0 removed the deprecated `availability_timeout`, `availability_blocklist`, `availability_passlist`, `availability_blacklist`, `availability_whitelist` and `advanced.legacy_availability_payload` settings, and made `zigbee2mqtt/bridge/state` always a JSON object. — **FACT / HIGH.** [Zigbee2MQTT 2.0.0 breaking changes · Discussion #24198](https://github.com/Koenkk/zigbee2mqtt/discussions/24198) — dated 2024-10-03, accessed 2026-07-31.

**Consumer-side caveat (INFERENCE / MED):** by the time HA sees it, Z2M availability is a **retained MQTT flag published only on change**. HA does not re-derive staleness from a timestamp; it trusts the last retained payload. A Z2M process that dies mid-flight leaves `online` retained on the broker unless the bridge LWT is also wired into the entity's availability list. Whether current Z2M discovery payloads attach both topics is **NOT ESTABLISHED**. *What would answer this:* fetch a raw `homeassistant/.../config` discovery payload emitted by current Z2M and inspect its `availability` array.

### 1.3 SmartThings

**Three states, not two.** Official docs define `ONLINE` ("can be expected to respond to a command (actuator devices) or report an event (sensor devices)"), `UNHEALTHY` ("a device has been inactive longer than its designated health check interval"), and `OFFLINE` ("A device with `UNHEALTHY` status cannot be contacted by the platform"). Health is read via `GET /devices/<deviceId>/health` and `GET /installed-hubs/<hubDeviceId>/health`. — **FACT / HIGH.** [Check Your Device's Health | SmartThings Developer Documentation](https://developer.smartthings.com/docs/devices/health) — undated, accessed 2026-07-31.

The UNHEALTHY tier matters to us: SmartThings already ships a **tri-state** model distinguishing "we have not heard from it lately" from "we tried and failed." — **OPINION / MED.**

**Hub health cascades.** Hub is `DISCONNECTED` when *"no hub connected event has been received in the last 60 seconds"*; and *"When a hub goes offline, all devices connected to this hub will also be marked `OFFLINE`."* — **FACT / HIGH**, same page. This is the only numeric threshold SmartThings publishes first-party.

**Devices opt in.** Devices must set the `healthCheck` capability to be enrolled; hubs are enrolled automatically. — **FACT / HIGH**, same page.

**Groovy era (legacy): explicit, developer-declared interval + platform ping.** SmartThings staff, 2020-12-02: *"When the hub hasn't received a message from a device within the checkInterval time, it will ping the device."*; *"For the vast majority of devices, setting **checkInterval** is the only needed action to track a device."*; and *"No attribute of the `HealthCheck` capability is updated with the "offline"/"online" value"* — health is readable only from the health endpoint. — **FACT / HIGH.** [Can someone explain HealthCheck, checkinterval, healthStatus…](https://community.smartthings.com/t/can-someone-explain-healthcheck-checkinterval-healthstatus-devicewatch-enroll-and-devicewatch-devicestatus/213038) — from 2020-12, accessed 2026-07-31.

**Edge era (current): moved hub-side and made opaque.** SmartThings staff, 2021-08-23: *"Using the health check capability is no longer needed in edge drivers like it was for DTHs… For Zigbee and Z-Wave, the hub will decide a devices health (online/offline status) based on radio communication, and the configuration of the device."* — **FACT / HIGH.** [HealthCheck in Edge Driver](https://community.smartthings.com/t/healthcheck-in-edge-driver/230592) — from 2021-08, accessed 2026-07-31. Confirmed first-party: *"Only useable on LAN type devices and children of LAN type devices. Calls to this API for ZIGBEE, ZWAVE, or MATTER type devices are ignored as their online/offline status are automatically determined at the radio level."* — [Device — SmartThings Edge Device Drivers](https://developer.smartthings.com/docs/edge-device-drivers/device.html) — undated, accessed 2026-07-31.

**The Edge threshold is not first-party documented.** The only figure found is community-derived: *"A monitored attribute will monitor responses from the device… That length is determined by config.maximum_interval * 1.5"*, with observed reads roughly every 8 minutes. Another developer states: *"Edge system sometimes makes mistakes to mark the health status incorrectly… device can be marked offline even if the device sends attributes periodically."* — **FACT** that these statements were made / **MED** that they describe current behaviour. [\[SmartThings Edge\] Issue with the device health (Zigbee)](https://community.smartthings.com/t/smartthings-edge-issue-with-the-device-health-zigbee/241789) — 2022-04 to 2023-02, accessed 2026-07-31.

**NOT ESTABLISHED:** any first-party published numeric health-check interval or multiplier for Edge Zigbee/Z-Wave/Matter devices. *What would answer this:* instrumenting a hub's Zigbee traffic and correlating read cadence with a driver's configured `maximum_interval`.

### 1.4 Hubitat

**There is no first-party liveness derivation.** Nothing surveyed shows Hubitat computing or exposing an online/offline state for a device.

- No stock health attribute: *"HE stock drivers do not support it"* — **FACT / HIGH.** [A way check offline/online status of devices](https://community.hubitat.com/t/a-way-check-offline-online-status-of-devices/143269) — 2024-09, accessed 2026-07-31. No Hubitat staff participated.
- The long-running feature request for a first-party health capability has **no staff commitment to implement**; the community converged on a *de facto* custom attribute `healthStatus` with enum `["offline","online"]`, explicitly modelled on SmartThings' `healthCheck`, implemented per-driver by third parties. — **FACT / MED-HIGH.** [DevicePresent capability](https://community.hubitat.com/t/devicepresent-capability-health-check-capability-and-healthstatus-attribute/89774) — opened 2022, still live, accessed 2026-07-31.

**The only platform-supplied signal is "Last Activity At",** updated when a driver calls `sendEvent()`. — **FACT / MED** (community developer, not staff). [When / what is/makes device page "Last Activity At" update?](https://community.hubitat.com/t/when-what-is-makes-device-page-last-activity-at-update/93012) — 2022-04, accessed 2026-07-31.

**Whether "Last Activity At" also advances on *outbound* commands is NOT ESTABLISHED.** This matters a great deal — if it does, the timestamp is contaminated with self-generated non-evidence and cannot honestly support an ALIVE assertion. *What would answer this:* power down a Zigbee bulb, issue `on()`, observe whether Last Activity At moves.

**Community fills the gap, and admits the gap is unfillable.** The canonical app, Device Activity Check (first post 2020-05-27):

> *"Device Activity Check doesn't actually 'monitor' or subscribe to any of their events; instead, it evaluates the criteria at the time the report or notification is generated."*

> *"This app cannot instantly notify you when a device goes 'offline,' nor is there a good way to tell this for all devices."*

— **FACT / HIGH.** [\[RELEASE\] Device Activity Check](https://community.hubitat.com/t/release-device-activity-check-get-notifications-for-inactive-devices/42176) — opening post 2020-05-27, accessed 2026-07-31. Note the app *does* evaluate at report time rather than caching. **OPINION / MED:** that a community developer independently arrived at read-time derivation, on a platform offering no primitive for it, is a tell that this is the natural design and Hubitat simply never built it.

### 1.5 Homey

**Availability is app/driver-asserted, not platform-derived.** The SDK exposes `setAvailable()`, `setUnavailable(message opt)`, `getAvailable()` and nothing else. — **FACT / HIGH.** [Device — Homey Apps SDK v3](https://apps-sdk-v3.developer.homey.app/Device.html) — undated, accessed 2026-07-31.

The narrative docs frame it as a **UI affordance driven by the app's own knowledge of its transport**: *"A device can be marked as unavailable using `Device#setUnavailable()`. This shows to the user that they cannot interacting with the device for example because the device is offline."* The canonical example wires it to a third-party API's socket events, not to any Homey liveness primitive. The docs are **silent** on default behaviour if an app never calls either method, and describe no platform-side derivation. — **FACT (absence) / HIGH.** [Drivers & Devices | Homey Apps SDK](https://apps.developer.homey.app/the-basics/devices) — undated, accessed 2026-07-31.

**Zigbee specifically: the SDK offloads liveness to the device's own reporting config.** *"It is recommended to configure attribute reporting for sleepy end devices. This ensures that the device periodically sends a message to Homey, allowing Homey to verify that the device is still present on the network."* — **FACT / HIGH.** [Zigbee | Homey Apps SDK](https://apps.developer.homey.app/wireless/zigbee) — undated, accessed 2026-07-31. What Homey *does* with that verification is **NOT ESTABLISHED**.

**The availability path has silently no-opped in production.** An SDK issue reports *"calling `device.setUnavailable()` does nothing"* when no message argument is supplied. Athom engineer: *"It seems we had a fallback for the old homey pro and in 2023 this fallback is never set."* — **FACT / HIGH.** [athombv/homey-apps-sdk-issues#313](https://github.com/athombv/homey-apps-sdk-issues/issues/313) — 2023, accessed 2026-07-31.

**Implication (OPINION / HIGH):** on Homey, "available" is the sticky default, flipped only by an app author who bothered to implement it, had a transport surfacing disconnect events, and passed the right arguments. This is the purest assumption-based design in the survey — and #313 means even a correctly-intentioned app could report ALIVE for a dead device.

### MECHANISM TABLE

| Platform / path | Signal used | Active probe or passive timeout | Default threshold | Where the truth lives | Classification |
|---|---|---|---|---|---|
| **HA — ZHA** (`zigpy/zha`) | `last_seen` (any received frame); `on_network` conjunct | **Both.** Passive `now - last_seen` first; on breach, active non-cached Basic-cluster read, 2 misses before demotion. LUMI never probed. Whole checker gated on `allow_polling`. | Mains **7200 s (2 h)**; battery **21600 s (6 h)**; `0` disables. Checker cadence 30–45 s, ≤20 concurrent. | Boolean `_available` on the device object, mirrored into HA entity state | **Evidence-derived, write-cached.** Starts `False` — no assumption of liveness at birth — but thresholds are hours and the result is a cached flag. |
| **HA — Zigbee2MQTT** | `device.zh.lastSeen` | **Both, asymmetric.** `isAvailable()` = `Date.now() - lastSeen < timeout` at call time. Active devices pinged on timeout (2 attempts if believed available, 1 if not), then backoff. **Passive devices never pinged.** | Active **10 min**; passive **1500 min (25 h)**. **Feature `enabled` defaults to `false`.** | Retained MQTT flag, QoS 1, published **on change only** | **Evidence-based derivation, assumption-shaped transport.** Predicate is pure and read-time; the consumer sees a sticky retained boolean. Off by default. |
| **SmartThings — Edge, Zigbee/Z-Wave/Matter** | Radio-level activity + driver's reporting config, evaluated hub-side | Both, but the mechanism is closed | **Not published.** Community-derived `maximum_interval * 1.5`. Only published number is the **60 s** hub-disconnect window. | Platform health record; readable only at `GET /devices/<id>/health` | **Evidence-based in principle, unauditable in practice.** Tri-state is the most nuanced model found; thresholds and logic are opaque and drivers cannot influence them. |
| **SmartThings — Edge, LAN** | Driver assertion only | Neither — driver calls `online()` / `offline()` | None | Driver-set | **Assumption-based** (driver-asserted) |
| **SmartThings — Groovy DTH (legacy)** | `checkInterval` declared per-device; platform pings on expiry | Passive timeout → active `ping()` | Developer-declared | Health endpoint only | Evidence-based, developer-parameterised |
| **Hubitat** | "Last Activity At", advanced when a driver calls `sendEvent()` | **Neither, first-party.** No platform probe, no timeout, no online/offline state at all. | None | Nowhere — community apps evaluate the timestamp at report time | **Assumption-based by omission.** There is no first-party liveness derivation to classify. |
| **Homey** | Whatever the app decides | Neither, platform-side | None documented | `Device#setUnavailable(message)` / `setAvailable()` | **Assumption-based.** Available is the sticky default; `setUnavailable()` without a message was a documented no-op. |

### READ

- **Nobody in this field derives availability at read time and exposes it that way.** Z2M's `isAvailable()` is the only pure read-time predicate found, and it is immediately collapsed into a retained MQTT boolean published only on change — so every downstream consumer, including HA, is back to trusting a write-time flag. ZHA computes from `last_seen` but caches into `_available` on a 30–45 s sweep. SmartThings caches into a health record. Hubitat and Homey have no derivation at all. **INFERENCE / HIGH.** Our read-time claim is genuinely unoccupied ground, but the honest framing is *"the only one that surfaces staleness at read time,"* not *"the only one that tracks last-seen."*
- **The strongest existing prior art is a detail, not an architecture: ZHA initialises `self._available: bool = False`.** A ZHA device is unavailable until proven otherwise. That single line is the closest any surveyed platform comes to never-false-ALIVE, and it should be cited as convergent evidence that the idea is right rather than treated as a competitive threat — because ZHA then undermines it with 2 h / 6 h thresholds and a checker disableable entirely by `allow_polling`. **FACT + OPINION / HIGH.**
- **Default thresholds across the field are one to three orders of magnitude coarser than "alive."** 10 min (Z2M active) is the tightest default anywhere; ZHA mains is 2 h, ZHA battery 6 h, Z2M passive 25 h. And Z2M's availability feature is **off by default**. On a stock install of any of these, a mains device that dies is reported ALIVE for somewhere between ten minutes and two hours. That is the real gap to attack, and it is a *defaults and honesty* gap more than an algorithmic one. **INFERENCE / HIGH.**
- **Battery/sleepy devices defeat everyone, and everyone has quietly conceded.** Z2M never pings passive devices. ZHA hard-codes a LUMI skip because polling knocks Aqara devices off the mesh. Homey's answer is "configure attribute reporting and hope." Hubitat's community app author states outright *"nor is there a good way to tell this for all devices."* Any evidence-based-availability claim we make must state its position on sleepy end devices explicitly, because the incumbents' unstated position is *we don't actually know*. **INFERENCE / HIGH.**
- **SmartThings already ships the tri-state model — `ONLINE` / `UNHEALTHY` / `OFFLINE` — and it is the right shape.** "Inactive longer than its health-check interval" is meaningfully different from "cannot be contacted." A binary ALIVE/DEAD is a weaker epistemic position than what the largest incumbent already exposes. Where SmartThings is beatable is auditability: no published thresholds, no capability attribute carrying health, hub-side logic its own driver developers describe as making mistakes. **"Evidence-based *and inspectable*" is the sharper differentiator than "evidence-based."** **OPINION / MED-HIGH.**
- **Two of five platforms make availability an app-author responsibility, and it visibly rots.** Homey's `setUnavailable()` silently did nothing without a message argument for an unknown period, per Athom's own engineer; SmartThings Edge gives LAN drivers the same delegation shape. Delegated availability is not a mechanism, it is a convention — and conventions fail silently in exactly the direction that produces a false ALIVE. **OPINION / HIGH.**

---

## §2 — The false-available pain, in the wild

**Method note.** Every URL below was opened and read. Two access failures: (a) **Reddit was unreachable this session** — proxy 403 across six differently-phrased queries, so there are **no Reddit exhibits**; (b) **GitHub renders issue timestamps client-side**, so GitHub exhibit dates are inferred from in-page version strings cross-referenced to project changelogs and labelled INFERENCE. Discourse forums render absolute dates in HTML, so those dates are FACT.

### Exhibit 1 — ZHA reports a dead device ALIVE by design, for up to 2–6 hours

- **Link:** [ZHA availability timeout - device not marked as unavailable, home-assistant/core #56290](https://github.com/home-assistant/core/issues/56290) — accessed 2026-07-31
- **Dates:** body reports `core-2021.9.6` → filed on/after **2021-09** (INFERENCE / MED). Closed.
- **Platform:** HA + ZHA.
- **Mechanism of the lie:** **Timeout-only liveness with no probe.** No positive liveness evidence; a `last_seen` timestamp decays against a fixed window. Kill a bulb's power and HA keeps serving `on` for hours.
- **Status:** **Closed as "working as designed."**
- **Quote:** *"the status does change to 'unavailable' but after a couple of hours"* — and, benchmarking a rival: *"I have seen this works correctly in zigbee2mqtt and others (availability_timeout)"*
- **Corroboration (FACT / HIGH):** [ZHA integration docs](https://www.home-assistant.io/integrations/zha/) — accessed 2026-07-31 — document the `7200` / `21600` defaults with the hint to *"Lower this value (for example, to `3600` (1 hour)) if you want faster detection when a plug or bulb loses power."* **The default configuration of the most-installed open smart home platform permits a 2-hour (mains) / 6-hour (battery) window of false-ALIVE.**

### Exhibit 2 — The ZHA availability checker doesn't actually run; only a manual reload tells the truth

- **Link:** [ZHA Not Flagging Devices as Unavailable after Set Times, home-assistant/core #123425](https://github.com/home-assistant/core/issues/123425) — accessed 2026-07-31
- **Dates:** `core-2024.8.0` → on/after **2024-08** (INFERENCE / MED). Open at access.
- **Mechanism of the lie:** **The periodic checker never fires.** Reporter set the mains timeout to 5 minutes; the device stayed `active` past 7 minutes, correcting only on integration reload. This is *unbounded* false-ALIVE, not a bounded window.
- **Status:** **Open**, no maintainer diagnosis on the page.
- **Quote:** *"After 7 minutes passed HA still showed the smart plug as active. I then reloaded ZHA and HA correctly represented the smart plug as unavailable."*

### Exhibit 3 — Z2M's liveness probe silently stopped running for months (FIXED)

- **Link:** [Availability not working - failed to ping all devices in network, Koenkk/zigbee2mqtt #17152](https://github.com/Koenkk/zigbee2mqtt/issues/17152) — accessed 2026-07-31
- **Dates:** affects Z2M `1.30.2 / 1.30.3 / 1.30.4`; fixed in `1.31.0-1`.
- **Mechanism of the lie:** **The probe was dead, not the logic.** Availability configured at a 5-minute interval; `last_seen` kept updating and availability published fine on reboot, but debug logs showed **zero ping entries from `availability.ts`**. Powering a device off produced *no* offline publication — the retained `online` stood forever.
- **Status:** **Fixed** — root cause in [zigbee-herdsman PR #664](https://github.com/Koenkk/zigbee-herdsman/pull/664).
- **Quote:** *"After powering off the device, the availability is not published - the device is not pinged"*
- **Why this exhibit matters:** it is the cleanest demonstration that **liveness that depends on an active prober is only as good as the prober's own liveness** — nothing detected that the detector had stopped.

### Exhibit 4 — "Z2M lies about the state of offline devices"

- **Link:** [Availability: incorrect state upon Z2M startup (with Home Assistant), Koenkk/zigbee2mqtt #5430](https://github.com/Koenkk/zigbee2mqtt/issues/5430) — accessed 2026-07-31
- **Dates:** Z2M `1.16.2` era (INFERENCE / MED). Stale-botted, un-staled by the reporter; open at access.
- **Mechanism of the lie:** **Optimistic startup assertion.** On boot the availability extension announces **every** device as available, because published availability derives from *bridge* connectivity, not device reachability.
- **Status:** **Open.** The page also records the counter-pressure — pinging everything at startup risks a ping storm whose failures cause the opposite lie.
- **Quote (the single best line in the corpus):** *"Z2M lies about the state of offline devices, which might break automations that rely on the availability state."*

### Exhibit 5 — MIRROR CASE: availability is a one-shot retained message; lose the broker's disk, lose the truth

- **Link:** [Battery Device Availability Messages Not Republished After MQTT Retained Message Loss, Koenkk/zigbee2mqtt #30619](https://github.com/Koenkk/zigbee2mqtt/issues/30619) — accessed 2026-07-31
- **Dates:** Z2M `2.7.1`, dated **2025-12-06** in the changelog (INFERENCE / HIGH). Open at access.
- **Mechanism (MIRROR — shown *unavailable* while alive):** **Availability state is externalised into broker-retained storage rather than recomputed from evidence.** For battery devices Z2M publishes the retained availability message essentially once and never republishes. Clear retained messages during broker maintenance and the device is permanently "Unavailable" while still delivering tens of thousands of messages. Same broken mechanism as Exhibits 1/3/4, sign-flipped.
- **Status:** **Open.**
- **Quote:** *"Home Assistant now permanently shows these devices as 'Unavailable' even though they're actively communicating (41,000+ messages sent over subsequent weeks)."* Reporter's own diagnosis: *"Availability messages shouldn't rely solely on retained MQTT messages from initial pairing—they should be refreshed periodically or when devices communicate."*

### Exhibit 6 — Same retained-message dependency, still live in the 2026 release line

- **Link:** [\[Feature request\]: Device Availability in version 2.8.0, Koenkk/zigbee2mqtt #31057](https://github.com/koenkk/zigbee2mqtt/issues/31057) — accessed 2026-07-31
- **Dates:** Z2M `2.8.0`, dated **2026-02-01** in the changelog (INFERENCE / HIGH). Closed.
- **Mechanism of the lie:** **Broker reboot wipes the liveness ledger** for all devices, never regenerated.
- **Quote:** *"Device Availability works fine, but when then MQTT server reboots it looses the zigbee2mqtt/\[device\]/availability persistent message for all devices."*
- **Read:** filed ~4.5 years after Exhibit 4 and ~2 months after Exhibit 5, against the current major line. **The mechanism is not a regression; it is the design.** (INFERENCE / MED-HIGH)

### Exhibit 7 — Tuya: the integration has no concept of "available" at all

- **Links:** [make-all/tuya-local#4067](https://github.com/make-all/tuya-local/issues/4067) and [rospogrigio/localtuya#1208](https://github.com/rospogrigio/localtuya/issues/1208) — both accessed 2026-07-31. Both **Open**.
- **Mechanism of the lie:** two sub-mechanisms, same outcome: (1) **Sticky last poll result, no availability attribute** — the maintainer states plainly that **`_attr_available` is not used by this integration**, so no code path can ever mark an entity unavailable; (2) **Cloud truth available but ignored** — the device's own cloud record reads `"online": false` while HA renders the entity as available.
- **Status:** Open; maintainer resists tightening: *"These values were settled on a long time ago as a balance between letting all devices work reliably and detection of communication failures."*
- **Quote:** *"The entity continues to appear available to Home Assistant until a new successful poll occurs."*

### Exhibit 8 — SmartThings: devices powered off for **eight days** still reported Online

- **Link:** [Device Status Stuck Online, SmartThings Community #211924](https://community.smartthings.com/t/device-status-stuck-online/211924) — accessed 2026-07-31
- **Dates (FACT / HIGH):** opened **2020-11-19**, last reply **2020-11-24**.
- **Mechanism of the lie:** **Cloud-side health state never re-derived on reconnect.** Two Z-Wave devices had been powered off for 8 days and the hub itself offline; on hub power-up the cloud restored them to Online within ~20 minutes without confirming reachability. Health is attributed to a mix of `checkInterval`, the `offlinePingable` flag, whether the handler implements `ping()`, and (new in hub 32.x) **inferring health from Z-Wave mesh status** — mesh topology inferred as liveness rather than a response from the device.
- **Status:** No staff response; effectively **unresolved**.
- **Corroborating opacity (FACT / HIGH):** [How smart things manage the online/offline status, #250149](https://community.smartthings.com/t/how-smart-things-manage-the-online-offline-status/250149) — 2022-10-18 — contains no technical mechanism; a community expert states *"I have asked for more technical details about when the system decides to mark a device as 'offline' … But I have not received an answer with details yet."*

### Exhibit 9 — Hubitat: dead sensors report a healthy battery level, and the vendor calls it expected

- **Link:** [Batteries die with no warning?, Hubitat Community #92841](https://community.hubitat.com/t/batteries-die-with-no-warning/92841) — accessed 2026-07-31
- **Dates (FACT / HIGH):** opened **2022-04-24**.
- **Mechanism of the lie:** **Sticky last-reported attribute + no independent liveness signal.** When the device dies the last value freezes. Hubitat staff explain the freeze as intended battery-preservation behaviour.
- **Status:** **Answered as normal behaviour** by staff; no defect acknowledged.
- **Quote:** *"Hubitat will show the device having 20% when it's actually dead. It's not just one device. Door sensors, window, motion."*
- **Architectural corroboration:** [Is there a definitive and reliable way to actively monitor devices going down?, #88338](https://community.hubitat.com/t/is-there-a-definitive-and-reliable-way-to-actively-monitor-devices-going-down/88338) — 2022-01-29 — a user asking for *security-device* down-detection is told the hub cannot dictate reporting periods or poll passive devices, and routed to community apps. **No Hubitat staff replied.**

### Exhibit 10 — Home Assistant + deCONZ: pull the batteries out and *nothing happens*

- **Link:** [Dead sensor doesn't show up as unavailable entity in HA, HA Community #218314](https://community.home-assistant.io/t/dead-sensor-doesn-t-show-up-as-unavailable-entity-in-ha/218314) — accessed 2026-07-31
- **Dates (FACT / HIGH):** opened **2020-08-13**, last reply **2023-11-25** — a **3-year-live** thread.
- **Mechanism of the lie:** **State-change-triggered updates only; timestamps ignored.** The bridge holds a `lastupdated` timestamp that would answer the liveness question, but HA's entity state only moves on a *value change* — so a sensor that stops speaking is indistinguishable from a sensor that is quiet.
- **Quote:** *"If I then take out the batteries from the water leak sensor, nothing happens, the entity state doesnt change to 'unavailable'."*
- **Severity note:** this is a **leak sensor** — the class of device whose entire value is being trusted while idle.

### Exhibit 11 — Still being filed six days ago (2026-07-25)

- **Link:** [Make Devices unavailable/unknown if not changed after X instead of being stuck on last value, HA Community #1018695](https://community.home-assistant.io/t/make-devices-unavailable-unknown-if-not-changed-after-x-instead-of-being-stuck-on-last-value/1018695) — accessed 2026-07-31
- **Dates (FACT / HIGH):** opened **2026-07-25**.
- **Mechanism of the lie:** **Sticky last value as the platform default.**
- **Status:** Open feature request. **Notable: the thread's own replies argue against tightening it** — lower timeouts burn battery, and some devices ignore configured reporting intervals entirely, producing flapping.
- **Quote:** *"Currently they stay at the last known read value, making my automations a bit messy."* Counter-pressure: *"The lower you set it, the more you will increase battery consumption."*
- **Baseline (FACT / HIGH):** [Z2M device availability docs](https://github.com/Koenkk/zigbee2mqtt.io/blob/master/docs/guide/configuration/device-availability.md) — accessed 2026-07-31 — battery devices *"have to check-in every 25 hours. If they don't they will be marked as `offline`."* **A battery sensor may be dead for up to 25 hours and still read ALIVE, by documented design.**

### Summary table

| # | Exhibit | Platform | Mechanism of the lie | Direction | Status | Age (2026-07-31) |
|---|---|---|---|---|---|---|
| 1 | HA core #56290 | HA + ZHA | Timeout-only decay, no probe; 2 h / 6 h defaults | False-ALIVE | **Closed — "working as designed"** | ~4.8 yr |
| 2 | HA core #123425 | HA + ZHA | Checker never scheduled; corrects only on reload → *unbounded* | False-ALIVE | **Open**, no maintainer reply | ~2 yr |
| 3 | Z2M #17152 | Z2M + HA | Prober silently stopped; nothing watched the watcher | False-ALIVE | **Fixed** (dependency patch) | 1.30.x era |
| 4 | Z2M #5430 | Z2M + HA | Optimistic startup from *bridge* state | False-ALIVE | **Open** | 1.16.2 era |
| 5 | Z2M #30619 | Z2M + MQTT | One-shot broker-retained message; never republished | **MIRROR** | **Open** | ≥2025-12-06 |
| 6 | Z2M #31057 | Z2M + MQTT | Broker reboot wipes retained availability for all devices | Both | **Closed** | ≥2026-02-01 |
| 7 | tuya-local #4067 + localtuya #1208 | HA + Tuya | No `_attr_available` at all; cloud's own `online:false` ignored | False-ALIVE | **Both open** | ≥2022-12 |
| 8 | SmartThings #211924 | ST cloud + Z-Wave | Cloud health not re-derived on reconnect; mesh inferred as liveness | False-ALIVE (8 days) | **Unresolved** | 5.7 yr |
| 9 | Hubitat #92841 | Hubitat | Sticky last-reported attribute; no hub-initiated probe | False-ALIVE | **Closed as expected behaviour by staff** | 4.3 yr |
| 10 | HA Community #218314 | HA + deCONZ | Value-change-only updates; `lastupdated` ignored | False-ALIVE | **No fix** | 6.0 yr |
| 11 | HA Community #1018695 | HA + Z2M | Sticky last value is the default | False-ALIVE | **Open FR, argued against in-thread** | **6 days** |

### PATTERN READ

**1. The dominant mechanism is decay-by-timeout, not evidence-of-life. — FACT / HIGH.** Across ZHA (7200/21600 s), Z2M (10 min / 25 h), SmartThings (`checkInterval`), and Tuya (poll interval), liveness is a *countdown that has not yet expired*, not a *fact recently confirmed*. Nobody is asked "are you there?"; the system merely notices silence eventually. **Every one of these platforms has a documented, default-configured window during which a dead device reads ALIVE.** That is not a bug report; that is the shipped specification.

**2. Where an active probe does exist, it is unmonitored and can fail silently. — FACT / HIGH.** Exhibit 3 is the proof: Z2M's ping loop stopped emitting entirely across three releases while `last_seen` kept updating and everything looked healthy. **No component detected that the liveness detector had died.** Exhibit 2 is the same shape on ZHA. *A prober without its own liveness accounting converts a bounded lie into an unbounded one.*

**3. Availability is stored as an assertion instead of derived from evidence — which makes it corruptible by unrelated infrastructure. — FACT / HIGH (Exhibits 5, 6); INFERENCE / HIGH on generality.** Z2M writes availability into MQTT retained storage. Wipe the broker's retention and the liveness claim for the whole estate is corrupted. The mirror-case direction is incidental; the defect is that **the liveness claim is a cached side-effect rather than a projection over observed events.** Any system that can lose its truth to someone else's disk has the same hole regardless of which way the error points.

**4. These are architectural, not one-off. — INFERENCE / HIGH.** Five distinct codebases plus two closed commercial platforms exhibit the *same* three mechanisms; the oldest exhibit is 2020-08 and the newest is **six days old**; and Z2M #5430 (1.16.x), #30619 (2.7.1) and #31057 (2.8.0) show the identical retained-availability dependency surviving a full major-version rewrite. **Only one of eleven exhibits was actually fixed** — and that by a dependency patch, not a design change.

**5. The field largely treats this as normal behaviour, and actively resists fixing it. — FACT / HIGH.** Exhibit 1 closed **"working as designed."** Exhibit 9 answered by Hubitat staff as intended behaviour. Exhibit 8's mechanism is undocumented and a community expert reports being unable to get an answer from the vendor. In Exhibit 7 the maintainer defends current timeouts as a long-settled balance; in Exhibit 11 the *community itself* argues against tightening detection. The stated reasons are real engineering tradeoffs — **battery drain, ping storms at startup, and flapping** — which is precisely why the field has settled on "lie quietly" as the cheapest resolution. The standard remedy offered to users is not a platform fix but **third-party watchdog apps and hand-rolled automations**.

**6. The pain lands hardest exactly where trust matters most. — OPINION / MED-HIGH, grounded in the exhibits.** The devices in these reports are water leak sensors, door/window/motion sensors used for security, and automation inputs. The users' own framing is the tell: *"Z2M **lies** about the state of offline devices"*; *"Hubitat will show the device having 20% **when it's actually dead**."* **NOT ESTABLISHED:** how often false-ALIVE causes concrete harm versus mere annoyance — no exhibit quantifies outcomes. *What would answer this:* incident-style reports on r/homeassistant — unreachable this session (Reddit proxy-blocked). **Flag for R-2, which has Reddit as a primary hunting ground.**

---

## §3 — Read-time staleness prior art

**Question:** does any shipping platform derive staleness at read time from a per-entity reporting contract, rather than storing a write-time availability flag?

**Short answer:** Yes — but essentially all of it lives outside the consumer smart home. In industrial and observability stacks the read-time derivation is *normative*. In the consumer smart-home field every mainstream platform reachable stores a write-time boolean. Our claim survives, but only with tight qualifiers, and there are three real counter-examples a hostile reviewer will find.

### Pass A — the home-automation field

**Home Assistant.** **FACT / HIGH.** HA's core availability contract is a stored boolean owned by the integration. The developer docs define `available` only as "Indicate if Home Assistant is able to read the state or control the underlying device," a `bool` defaulting to `True`, settable via `_attr_available` ([Entity | HA Developer Docs](https://developers.home-assistant.io/docs/core/entity/) — last updated 2026-05-19, accessed 2026-07-31). No expected-cadence field, no read-time derivation.

This is not incidental — it is prescribed. The Integration Quality Scale rule states *"If we can't fetch data from a device or service, we should mark it as unavailable"* with worked examples setting `self._attr_available = False` or leaning on `CoordinatorEntity.last_update_success`. No timestamp/interval derivation appears anywhere ([Mark entity unavailable](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/entity-unavailable/) — last updated 2026-06-15, accessed 2026-07-31). **This is the write-time-flag pattern, written down as official platform doctrine.**

The raw material exists but is unconsumed. `last_reported` is "updated regardless of any changes to the state or state attributes" ([State object](https://www.home-assistant.io/docs/configuration/state_object/) — undated, accessed 2026-07-31), but its stated motivation was time-series analysis, **not** trust derivation ([New state timestamp State.last_reported](https://developers.home-assistant.io/blog/2024/03/20/state_reported_timestamp/) — dated 2024-03-20, accessed 2026-07-31). Two years later it is still not surfaced in dashboards and is not an official staleness indicator.

**COUNTER-EXAMPLE 1 — HA MQTT `expire_after`, and it is the strongest one. FACT / HIGH.** "If set, it defines the number of seconds after the sensor's state expires if it's not updated… After expiry, the sensor's state becomes unavailable." Configured per entity ([MQTT Sensor](https://www.home-assistant.io/integrations/sensor.mqtt/) — undated, accessed 2026-07-31). In source:

```python
self._expiration_trigger = async_call_later(self.hass, self._expire_after, self._value_is_expired)
...
@property
def available(self) -> bool:
    """Return true if the device is available and value has not expired."""
    return MqttAvailabilityMixin.available.fget(self) and (
        self._expire_after is None or not self._expired
    )
```

([`mqtt/sensor.py`, `dev`](https://raw.githubusercontent.com/home-assistant/core/dev/homeassistant/components/mqtt/sensor.py) — accessed 2026-07-31). **INFERENCE / HIGH:** a hybrid. The cadence *is* a per-entity contract and the property *is* a getter, but the decision is made by a background timer flipping a stored `_expired` boolean that the getter merely reads. **It is a write-time flag wearing a read-time coat**, and the outcome collapses into `unavailable` rather than a distinct trust state.

Users have asked for exactly our primitive and been given DIY templates. A 2022 request for "expected sensor cadence" drew only template/automation workarounds, with the OP objecting that "these last-updated values are reset on reboot" ([Identify Offline Sensors With Expected Sensor Cadence?](https://community.home-assistant.io/t/identify-offline-sensors-with-expected-sensor-cadence/485192) — key reply 2022-11-06, accessed 2026-07-31). No built-in feature was offered.

A third-party HACS component implements something adjacent — a "Staleness threshold (minutes)" with `degraded` as a state distinct from unavailable — but per *group*, not per entity, and event-fired rather than read-derived ([Home-Assistant-EntityAvailability README](https://raw.githubusercontent.com/italo-lombardi/Home-Assistant-EntityAvailability/main/README.md) — undated, accessed 2026-07-31). **FACT / MED.**

**Zigbee2MQTT. FACT / HIGH.** A genuine per-device cadence contract (10 min active / 1500 min passive, overridable per device) — but the output is a **retained** MQTT message, and the docs concede the flag can lie: *"this timeout is persisted between Zigbee2MQTT restarts. So if you for example stop Zigbee2MQTT for longer than 10 minutes, all your active devices will be marked as `offline` initially until they check-in again"* ([Device availability | Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/configuration/device-availability.html) — undated, accessed 2026-07-31). Per-entity contract: yes. Read-time as seen by consumers: no. **This is a textbook instance of the failure mode our design avoids.**

**COUNTER-EXAMPLE 2 — SmartThings HealthCheck. FACT / MED** (community/staff thread; the Groovy developer docs are gone). The device *declares its own* expected cadence: `sendEvent(name: "checkInterval", value: 1860, ...)`, and "When the hub hasn't received a message from a device within the checkInterval time, it will ping the device." But the result is a stored server-side record: "No attribute of the HealthCheck capability is updated with the 'offline'/'online' value, you can only get the current status in the `devices/deviceId/health` endpoint" ([SmartThings Community #213038](https://community.smartthings.com/t/can-someone-explain-healthcheck-checkinterval-healthstatus-devicewatch-enroll-and-devicewatch-devicestatus/213038) — replies 2020-12-02 onward, accessed 2026-07-31). **This is the closest thing in a shipping consumer platform to a per-entity *declared* reporting contract — and it is resolved by a cloud watchdog into a stored flag.**

**COUNTER-EXAMPLE 3 — Hubitat Device Activity Check. FACT / MED.** No platform primitive, but the de-facto community app *is* read-time: "it evaluates the criteria at the time the report or notification is generated." Thresholds are per *group*, and the output is a notification, not a trust state ([Hubitat Community #42176](https://community.hubitat.com/t/release-device-activity-check-get-notifications-for-inactive-devices/42176) — original post 2020-05-27, accessed 2026-07-31).

**Homey. FACT / HIGH.** Purely write-time and app-driven; no expected-interval concept, no automatic staleness ([Drivers & Devices | Homey Apps SDK](https://apps.developer.homey.app/the-basics/devices) — undated, accessed 2026-07-31).

**openHAB — checked specifically. FACT / HIGH.** Thing status is a write-time state machine set by binding handlers: `UNINITIALIZED`, `INITIALIZING`, `UNKNOWN` ("cannot really tell yet whether the Thing is ONLINE or OFFLINE"), `ONLINE` ("assumed to be working correctly"), `OFFLINE`, `REMOVING`, `REMOVED`. Nothing about expected reporting intervals or freshness ([Things | openHAB](https://www.openhab.org/docs/concepts/things.html) — undated, accessed 2026-07-31). Note `UNKNOWN` is an *initialization* state, not a trust state.

The `expire` item metadata is the field's closest structural analogue and is explicitly write-time: per-item duration (`Switch MySwitch { expire="2h" }`), and on elapse it **posts a new state** — default `UNDEF` — into the item ([Items | openHAB](https://www.openhab.org/docs/configuration/items.html) — undated, accessed 2026-07-31). **INFERENCE / HIGH: this is strictly worse than a boolean flag for our purposes, because it *destroys the last known value* rather than annotating it.** A reader cannot recover "the value was 21.5 °C but we haven't heard from it in 40 minutes." openHAB later added `getLastStateChange` / `getLastStateUpdate` / `getLastState` to `GenericItem` ([openhab-core PR #4351](https://github.com/openhab/openhab-core/pull/4351) — merge date not stated on page, accessed 2026-07-31) — this enables read-time DIY derivation; it is not a contract, a state, or a platform trust signal. **FACT / MED.**

**Domoticz. FACT / MED.** Timeout exists but is **global, not per-device**, and "only checks Sensors (temperature, humidity, lux etc), not Switches/Lights" ([Application Settings — Domoticz Wiki](https://wiki.domoticz.com/Application_Settings) — undated, accessed 2026-07-31). The red highlight is a rendering-time cue, but there is no per-entity contract and it does not become a first-class state.

**Node-RED. FACT / LOW-MED.** No platform-level concept found; Node-RED has no device model, so there is nothing for a per-entity contract to attach to. Null result from limited search.

### Pass B — adjacent domains, where the pattern actually lives

**OPC UA — the single best prior art, and it is normative. FACT / HIGH — independently re-verified 2026-07-31.** The spec explicitly assigns staleness detection to the *client at read time*, and explicitly refuses to encode it in the status code. Verbatim, under `Uncertain_LastUsableValue`:

> "Whatever was updating this value has stopped doing so. This happens when an input variable is configured to receive its value from another variable and this configuration is cleared after one or more values have been received. **This status/substatus is not used to indicate that a value is stale. Stale data can be detected by the client looking at the timestamps.**"

([UA Part 8: DataAccess — 7.3](https://reference.opcfoundation.org/Core/Part8/v105/docs/7.3) — OPC 10000-8 v1.05, accessed 2026-07-31). The same table gives `Bad_NoCommunication` and `Uncertain_SubstituteValue`, confirming Uncertain/Bad/Good severity.

The derivation has the data it needs: every `DataValue` carries `statusCode`, `sourceTimestamp` ("should indicate the time of the last change of the value or statusCode") and `serverTimestamp`, to picosecond resolution ([Part 4 §7.11](https://reference.opcfoundation.org/specs/OPC-10000-4/7.11) — accessed 2026-07-31). And the cadence is a per-item contract: "Each MonitoredItem created by the Client is assigned a sampling interval that is either inherited from the publishing interval of the Subscription or that is defined specifically to override that rate" ([Part 4 §5.13.1.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.13.1.2) — v1.05.07, accessed 2026-07-31).

**INFERENCE / HIGH:** OPC UA has all three ingredients — per-item cadence, per-value timestamps, and an explicit instruction that the reader derives staleness — but stops one step short of our design: **it does not define a normative "compare now against last-heard-at versus the sampling interval" rule.** It hands the reader the timestamps and the interval and leaves the policy to the client. **We are closing a gap OPC UA deliberately left open.** That is a much better story than "we invented this."

**Ignition SCADA — "Stale" as a first-class quality. FACT / MED** (7.9 docs; the 8.1 equivalent page 404'd). Ignition ships `Stale` as a distinct tag quality, value **500**, defined as **"The tag has not been evaluated within the expected time frame. There is likely a deeper problem with the tag provider,"** separate from `Bad` (0), `Config_Error` (300) and `Expression_Eval_Error` (310), surfaced to operators as a visual overlay ([Tag Quality and Overlays — Ignition 7.9](https://www.docs.inductiveautomation.com/docs/7.9/tags/understanding-tags/tag-quality-and-overlays) — undated, accessed 2026-07-31). **This is the clearest example anywhere of "stale ≠ bad ≠ unavailable" as a shipped, operator-visible, trust-carrying state derived from an expected cadence.**

**Prometheus — read-time, but the contract is global not per-entity. FACT / HIGH.** PromQL "takes the newest sample that is less than the lookback period ago. The lookback period is 5 minutes by default." And: "A time series will go stale when it is no longer exported… they will not be returned in queries after they are marked stale" ([Querying basics | Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/) — undated, accessed 2026-07-31). Stale markers are "special samples (internally implemented as a special type of NaN)" ([Staleness and PromQL — Robust Perception](https://www.robustperception.io/staleness-and-promql/) — dated 2019-04-01, accessed 2026-07-31). **INFERENCE / MED-HIGH:** the lookback window is a **global server flag, not per-series**. So Prometheus nails read-time derivation and misses the per-entity contract. **This is the mirror image of Zigbee2MQTT, and the framing is useful: nobody in either field has both halves.**

**DDS / ROS 2 — per-entity contract + reader-side detection. FACT / HIGH.** Deadline QoS is literally a cadence contract: "The deadline policy establishes a contract for the amount of time allowed between messages," with violation detected in the middleware. Liveliness "establishes a contract for how entities report that they are still alive" ([ROS QoS — Deadline, Liveliness, Lifespan](https://design.ros2.org/articles/qos_deadline_liveliness_lifespan.html) — dated 2019-09, accessed 2026-07-31). RTI's implementation makes it explicit that this is a background thread, not read-time: "an internal thread that wakes up at the period set by the DataReader's lease_duration" ([RTI Connext LIVELINESS QosPolicy](https://community.rti.com/static/documentation/connext-dds/current/doc/manuals/connext_dds_professional/users_manual/users_manual/LIVELINESS_QosPolicy.htm) — undated, accessed 2026-07-31). Deadline is applied **per key/instance**, and Lifespan is DDS's closest thing to read-time invalidation ([Fast DDS 2.14.x QoS policies](https://fast-dds.docs.eprosima.com/en/2.14.x/fastdds/dds_layer/core/policy/standardQosPolicies.html) — undated, accessed 2026-07-31). **INFERENCE / HIGH:** the strongest *conceptual* prior art for "per-entity declared cadence, reader decides" — timer-and-callback in implementation, producing an event rather than a per-value trust annotation.

**Matter — a per-subscription contract that consumers throw away. FACT / MED → HIGH on the punchline.** The subscription defines min/max interval and empty reports act as keepalive; "A subscription may be ended if… the subscriber does not receive a Report Data Action within the max interval ceiling" ([Matter Fundamentals: Interaction Model — Silicon Labs](https://docs.silabs.com/matter/latest/matter-fundamentals-interaction-model/) — undated, accessed 2026-07-31). The SDK makes it concrete: the liveness check "is set to the max interval of the subscription + ACK timeout of the underlying session," with `RefreshLivenessCheckTimer` and `OnLivenessTimeoutCallback` ([`connectedhomeip/src/app/ReadClient.h`](https://raw.githubusercontent.com/project-chip/connectedhomeip/master/src/app/ReadClient.h) — accessed 2026-07-31).

**And this is the sharpest point in the whole section.** The protocol hands the controller a per-subscription cadence contract, and the controller immediately flattens it into a boolean:

```python
self._attr_available = (
    self._endpoint.node.available and self._get_bridged_reachable()
)
```

([`matter/entity.py`, `dev`](https://raw.githubusercontent.com/home-assistant/core/dev/homeassistant/components/matter/entity.py) — accessed 2026-07-31). No timestamp or interval arithmetic. **The cadence contract exists at the wire level and the consumer throws it away.** *(This finding is directly relevant to R-3 §2 — flag at intake.)*

**MQTT — keepalive and LWT are connection-level. FACT / HIGH.** Keepalive is broker↔client, not per-entity (§3.1.2.10); the Will Message is a write-time flag emitted by the broker on behalf of a dead client (§3.1.2.5). **The RETAIN semantics attach no freshness guarantee or validity timestamp** ([MQTT v5.0, OASIS Standard](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) — accessed 2026-07-31). **INFERENCE / HIGH: this is *why* retained messages can lie** — a retained `online` payload is indistinguishable from a fresh one, which is exactly the Z2M pathology in §2 Exhibits 5 and 6.

**AWS IoT Device Shadow — read-time freshness without a cadence contract. FACT / MED.** The shadow's `metadata` holds "timestamps, in Epoch time, for each attribute in the `state` section, which enables you to determine when they were updated" ([Device shadow service documents](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-document-syntax.html) — undated, accessed 2026-07-31). Per-attribute read-time age derivation, shipping at scale — but no declared expected cadence to compare against, and no derived trust state.

**Zigbee ZCL reporting intervals. OPINION / LOW — could not verify.** ZCL `Configure Reporting` sets min and max reporting intervals per attribute, and the lane expected to confirm that max-interval functions as a mandatory heartbeat. **It could not be verified from a primary source** — the Silicon Labs page only confirms the mechanism exists and defers to ZCL spec 075123r02 ([Zigbee Cluster Library | Silicon Labs](https://docs.silabs.com/zigbee/8.2.3/zigbee-fundamentals/06-zigbee-cluster-library) — undated, accessed 2026-07-31). **Do not use this line without pulling the ZCL spec PDF.** If it holds it is a strong supporting point: the per-attribute cadence contract already exists at the Zigbee wire level and no consumer platform consumes it as a trust signal.

### VERDICT

**The unqualified claim — "first/only in consumer smart home to do read-time staleness from a per-entity reporting contract" — is NOT defensible as written.** Three shipping counter-examples partially satisfy it and a careful adversary will find all three: HA MQTT `expire_after` (per-entity contract, computed getter — fails on the background timer and on collapsing into `unavailable`); SmartThings `checkInterval` (device-declared cadence, shipping since Groovy — fails on the cloud watchdog resolving it into a stored record); Hubitat Device Activity Check (genuinely read-time — fails on being third-party, per-group, and producing a notification rather than a trust state).

**What a careful person CAN say without being wrong, with all qualifiers intact:**

> Read-time staleness derivation from a per-entity reporting contract is established practice in industrial and observability systems — OPC UA tells clients outright that "stale data can be detected by the client looking at the timestamps"; DDS makes reporting cadence a per-entity QoS contract with reader-side enforcement; Ignition ships `Stale` as a first-class quality distinct from `Bad`; Prometheus derives staleness at query time. In the consumer smart home the same idea appears only in fragments: a per-device timeout that produces a retained flag (Zigbee2MQTT), a device-declared check interval resolved by a cloud watchdog (SmartThings), a per-entity expiry resolved by a background timer (HA MQTT `expire_after`), or a per-item timer that overwrites the last known value with UNDEF (openHAB `expire`). **We found no consumer smart-home platform that makes it a core, platform-wide primitive — every entity, every reader, `stale` as a state distinct from `unavailable`, computed from now vs last-heard-at vs the entity's declared cadence at the moment of the read.** Home Assistant's official quality-scale guidance points the other way, instructing integrations to set `_attr_available = False`.

**The four load-bearing qualifiers — drop any one and a counter-example walks in:**

1. **core/platform-wide** (not per-integration, not a plugin)
2. **every reader** (automations, UI and API see the same derivation)
3. **`stale` distinct from `unavailable`** (the value survives and is annotated rather than discarded)
4. **computed at the read** (no stored flag anywhere in the path)

Per §0's absence rule, the negative half — "no consumer platform does it" — is capped at **MED confidence**. Not read: the Matter core specification PDF, the ZCL specification, current SmartThings Edge driver documentation, or any closed platform's internals (Apple Home, Google Home, Alexa, Aqara, Tuya, Control4, Crestron, Savant). A professional smart-home controller could plausibly do this and not document it publicly.

### SEARCH-WORK LOG (§3)

**30 queries run**, spanning: HA entity/`last_reported`/quality-scale/feature-requests; openHAB expire + Thing status + `lastStateUpdate`; Z2M availability; SmartThings HealthCheck; Hubitat Device Activity Check; Homey SDK; Domoticz timeouts; Prometheus staleness + lookback-delta; OPC UA StatusCode/SamplingInterval/`Uncertain_LastUsableValue`/DataValue timestamps; DDS Liveliness + Deadline; Matter subscription MaxInterval/liveness (three separate phrasings); ZCL Configure Reporting; Sparkplug B NDEATH; Ignition tag quality; ioBroker device-watcher; Node-RED watchdog patterns.

**Five queries returned nothing relevant**, which is itself informative — the concept has no established search vocabulary in this field: `smart home hub "stale" state distinct from "unavailable" per-device expected reporting interval trust`; `home automation platform compute freshness at query time "last seen" versus expected interval instead of availability boolean`; `"heartbeat" OR "keepalive" per-device declared interval smart home hub derive confidence at query time`; `home-assistant architecture ADR discussion staleness "last_reported" availability derive automatically core proposal` (**no relevant ADR exists**).

**~38 pages opened and read** — enumerated in the sub-lane record; the principal ones are cited inline above.

**Could not read — routed around, never summarized:** `piglerautomation.com` Ignition article (TLS failure); the Device Activity Check GitHub tree (robots.txt); Ignition 8.1 tag-quality page (404, fell back to 7.9 and flagged the version); OPC UA Part 8 v1.04 §A.2 (landing page only; found correct v1.05 §7.3); ioBroker device-watcher README (repo chrome only — **ioBroker is an unchecked gap**).

**Known gaps a follow-up should close:** Matter core spec PDF; ZCL spec (max-reporting-interval-as-heartbeat); current SmartThings Edge driver docs; ioBroker; Node-RED beyond one search; all closed consumer/professional platforms.

---

## §4 — Our stack's near-term ground

**Method note.** Four sources refused: the GitHub REST API (403 via proxy), GitHub `/tree/` and `.atom` endpoints (robots-disallowed), `central.sonatype.com` (JS-rendered empty table), and `sqlite.org/walresetbug.html` (404 — **but see the correction box in 4c; the real anchor was found and read**). Silicon Labs docs were reachable but their `latest` alias is self-inconsistent — see 4a.

### 4a. EmberZNet + EZSP

**The bundle got renamed, and the line forked in two.** Silicon Labs migrated from **Gecko SDK (GSDK)** to **Simplicity SDK (SiSDK)** at EmberZNet 8.0.0.0, dropping Series 0/1 silicon; the GSDK line continued for those parts ([EZSP v14 support in bellows? · Issue #632](https://github.com/zigpy/bellows/issues/632) — dated 2024-06, accessed 2026-07-31). EFR32MG24 is Series 2, supported on *both* lines. **FACT / HIGH.**

| Train | Bundle | EmberZNet | EZSP |
|---|---|---|---|
| Legacy/community | Gecko SDK 4.4 / 4.5 | 7.4.x, 7.5.x | **v13 (0x0D)** |
| Forward | Simplicity SDK 2025.x / 2026.x | 8.0 → 9.1.x | v14, v16, v17, v18, (0x13) |

**Current forward-line release and cadence.** SiSDK Zigbee release notes report **Zigbee/EmberZNet 9.1.1, dated 2026-07-29**, in **SiSDK 2026.6.1**, EZSP protocol version **0x13** ([Zigbee Release Notes, Simplicity SDK](https://docs.silabs.com/sisdk-release-notes/latest/sisdk-zigbee-release-notes/) — dated 2026-07-29, accessed 2026-07-31). **Caveat:** a sub-path of that same `latest` alias served **Zigbee 9.0 Revision 2, dated 2026-05-04, SiSDK 2025.12.3**. Silabs multiplexes several "latest" pointers; treat 9.1.1 as newest but do not make the exact patch number load-bearing. Cadence reconstructed from dated notes: **two feature bundles a year, revisions every 4–10 weeks.** **INFERENCE / HIGH.**

**Is EZSP v13 deprecated, removed, or at risk? No — and the evidence runs the other direction.** Five independent confirmations:

1. **Silicon Labs' own release notes for the v13 stack list no deprecations.** EmberZNet 7.5.0.0 declares EZSP protocol version **0x0D**, release date **2025-02-26**, and Section 5 "Deprecated Items" reads **"None"** ([EmberZNet Release Notes 7.5.0.0](https://www.silabs.com/documents/public/release-notes/emberznet-release-notes-7.5.0.0.pdf) — dated 2025-02-26, accessed 2026-07-31). **FACT / HIGH.**
2. **v13 is the enforced *floor* of modern host support, not a deprecation target.** Zigbee2MQTT's `ember` adapter *requires* it: *"ember currently requires a firmware with EZSP v13 (EmberZNet firmware 7.4.x)"*, supported firmware "7.4.x, 8.0.x, 8.1.x, 8.2.x" ([EmberZNet adapters | Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/adapters/emberznet.html) — accessed 2026-07-31). What got deprecated was the *old* `ezsp` driver for pre-v13 firmware ([zigpy discussion #1396](https://github.com/zigpy/zigpy/discussions/1396) — dated 2024-05-06, accessed 2026-07-31). **We are on the safe side of that line.**
3. **bellows still carries a live v13 implementation.** `class EZSPv13(EZSPv12)` with `VERSION = 13` ([raw dev](https://raw.githubusercontent.com/zigpy/bellows/dev/bellows/ezsp/v13/__init__.py)); the `_BY_VERSION` registry spans **v4–v14, v16, v17, v18** ([raw dev](https://raw.githubusercontent.com/zigpy/bellows/dev/bellows/ezsp/__init__.py) — accessed 2026-07-31). Note the shape: **bellows has never removed a version handler, all the way back to v4 from the EM35x era.** **FACT / HIGH.**
4. **No maintainer has signalled intent to drop old versions.** Stated policy is the opposite: *"bellows will successfully use the most recent protocol schema when talking to an adapter: we don't need to explicitly support every protocol version bump unless fundamental commands change"* ([Issue #685](https://github.com/zigpy/bellows/issues/685) — 2025-07, accessed 2026-07-31). **FACT / HIGH.**
5. **The best-supported MG24 coordinator on the market ships EZSP v13 today** — Nabu Casa's current ZBT-2 firmware is EmberZNet **7.5.1.0** (see 4b). We are not on a legacy island; we are on the same version as the reference hardware.

**EZSP version map (all verified, none recited).** v13 = 0x0D = EmberZNet 7.4.x/7.5.x. v14 = EmberZNet 8.0.0.0. **v15 was skipped entirely by Silicon Labs.** v17 = 0x11 = 8.2.0.0 / SiSDK 2025.6.0 (2025-06-16). v18 = 0x12 = 8.2.2 / SiSDK 2025.6.2 (2025-09-24) ([Issue #685](https://github.com/zigpy/bellows/issues/685); [Issue #703](https://github.com/zigpy/bellows/issues/703) — accessed 2026-07-31). Given v17=0x11 and v18=0x12, the 9.1.x line's **0x13 reads as EZSP v19** — **INFERENCE / HIGH**, arithmetic on verified anchors; no page was opened that writes "v19" in decimal.

**Negotiation direction — the part worth internalising.** bellows initialises at **v4**, sends a `desiredProtocolVersion`, and the NCP replies with *its own* version; the host then calls `_switch_protocol_version(ver)` to match. If the host doesn't recognise the reported version it falls back to its newest known schema while preserving the reported number. After any reset it always returns to v4 first ([`bellows/ezsp/__init__.py`](https://raw.githubusercontent.com/zigpy/bellows/dev/bellows/ezsp/__init__.py) — accessed 2026-07-31). So:

- **The firmware picks the EZSP version; the host adapts upward.** There is no "negotiate down" — you cannot ask a v18 NCP to speak v13.
- **But we control the firmware.** v13 stays v13 until someone reflashes the stick. There is no remote or automatic force.
- **Newer host libraries keep working with old NCPs.** That is the direction that matters, and it is well-supported.
- **The one thing to avoid is *hardcoding* `13` on the host side.** If a replacement dongle arrives with 8.2.x factory firmware it will announce v14–v18, and a host that asserts equality with 13 will refuse to start. **Read the reported version; don't assert it.**

**Host library health:** bellows **0.49.2, released 2026-05-27**, requires Python ≥3.11 ([PyPI: bellows](https://pypi.org/project/bellows/) — accessed 2026-07-31). One caution for anyone reading it: **the bellows README is stale**, still claiming "v4/v5/v6/v7/v8" support while the shipped code registry goes to v18. Trust the source, not the README.

**One genuine deprecation, and it is firmware-side.** The 9.0 notes flag the **Zigbee Classic Key Storage** component (plaintext keys in NVM3 tokens) for removal, planned **June 2026**, replaced by Zigbee Secure Key Storage in PSA. This affects on-chip key storage on the 9.x train only — it does not touch a v13 NCP or the host protocol. Relevant only as a future *migration* consideration if we ever jump trains, where network-key backup/restore behaviour could differ. **INFERENCE / MED.**

**VERDICT: STABLE** — v13 is the supported floor of the modern ecosystem, not a ceiling about to be cut. The only self-inflicted risk is hardcoding the version number host-side.

### 4b. The MG24 coordinator dongle ecosystem

**Chip attribution, verified rather than assumed.** The brief's caution was well-placed — the MG21/MG24 split does not follow product-name intuition.

| Stick | Chip |
|---|---|
| **HA Connect ZBT-2** | **EFR32MG24** (+ ESP32-S3 as USB controller) |
| **SONOFF Dongle Plus MG24 ("Dongle-PMG24")** | **EFR32MG24** |
| **SMLIGHT SLZB-07Mg24** | **EFR32MG24** |
| **SeeedStudio Xiao MG24** | **EFR32MG24** |
| SONOFF ZBDongle-E | **EFR32MG21** — *not* MG24 |
| HA Connect ZBT-1 / SkyConnect | EFR32MG21 |
| SMLIGHT SLZB-07 (base) | EFR32MG21 |
| HA Yellow | MGM210P (MG21-class) |

Sources: [HA Connect ZBT-2 blog](https://www.home-assistant.io/blog/2025/11/19/home-assistant-connect-zbt-2/) — dated 2025-11-19; [ZHA integration docs](https://www.home-assistant.io/integrations/zha/); [SONOFF Dongle Plus MG24 product page](https://sonoff.tech/en-us/products/sonoff-zigbee-thread-usb-dongle-dongle-plus-mg24) (states "Zigbee SoC: EFR32MG24"); [darkxst/silabs-firmware-builder](https://github.com/darkxst/silabs-firmware-builder) — all accessed 2026-07-31. **FACT / HIGH.**

**Hardware lineage.** The **ZBT-2 launched 2025-11-19**, superseding the ZBT-1/SkyConnect; ZBT-1 **production has ended** though software support continues. The reference platform for this ecosystem is therefore now MG24. **That is a tailwind for us, not a headwind: we are on the chip the ecosystem is standardising on.** **INFERENCE / HIGH.**

**Firmware supply chain — this is where the picture splits.**

**Healthy: `NabuCasa/silabs-firmware-builder`.** Org-backed, not one-maintainer. Latest release **v2026.02.23, dated 2026-02-24**, targeting SkyConnect / Yellow / **ZBT-2**, built on **Gecko SDK 4.4.5→4.5.0 for Zigbee**, shipping **EmberZNet 7.5.1.0**. Release rhythm over ~12 months: 2025-04-05, 2025-09-17, 2025-09-30, 2025-11-24, 2026-01-11 (beta2), 2026-02-24 — every 1–3 months with substantive content ([NabuCasa releases](https://github.com/NabuCasa/silabs-firmware-builder/releases) — accessed 2026-07-31). **FACT / HIGH.**

Two things fall out of this that matter to us. First, **Nabu Casa is deliberately staying on the Gecko SDK 4.x / EmberZNet 7.5.x / EZSP v13 line for Zigbee NCP firmware on MG24 hardware as of February 2026** — they have not chased the 8.x/9.x SiSDK train. That is the strongest possible corroboration that v13 is not a legacy trap. **INFERENCE / HIGH** (the inference is about intent; the version facts are direct). Second, **our v13 pin and the best-maintained MG24 firmware in the ecosystem are the same version.**

**Fragile: `darkxst/silabs-firmware-builder`.** The fork covering the *non*-Nabu-Casa sticks — SONOFF ZBDongle-E and Dongle Plus, SMLIGHT SLZB-07 series, Aeotec Zi-Stick, SeeedStudio Xiao MG24. Maintained by a **single individual**. Its **most recent release is `20250627`, dated 2025-06-27** — roughly **13 months stale**. **FACT / HIGH.** Honest boundary: the commit feed was robots-disallowed, so *"no release in 13 months"* is established; *"abandoned"* is **NOT ESTABLISHED**. **OPINION / MED:** a single-maintainer fork with a 13-month release gap, serving most of the third-party MG24 fleet, is the one genuinely fragile link in this stack's supply chain.

**Vendor firmware is opaque.** SONOFF ships pre-installed EmberZNet coordinator firmware with NCP / Router / OpenThread RCP / MultiPAN RCP options — but the supported-firmware page publishes **no version numbers, dates, or build provenance** ([SONOFF Dongle-PMG24 supported firmware](https://dongle.sonoff.tech/guide/dongle-pmg24/supported_firmware/) — accessed 2026-07-31). **You cannot tell from vendor documentation which EZSP version a new unit will present.** **FACT / HIGH.**

**What this means concretely.** The risks are procurement-shaped, not architecture-shaped: (i) a replacement dongle bought a year from now may arrive with factory firmware announcing v14–v18 rather than v13 — fine *if* the host reads the negotiated version rather than asserting it; (ii) if we standardise on a SONOFF/SMLIGHT stick, our firmware update path depends materially on one volunteer. Standardising on the ZBT-2 puts us behind an org-backed builder instead. **INFERENCE / MED-HIGH.**

**VERDICT: WATCH** — chip and ecosystem healthy and converging on MG24; the watch items are single-maintainer firmware for third-party sticks and opaque vendor firmware versioning. Mitigation is procurement choice plus not hardcoding EZSP 13 — not a rewrite.

### 4c. SQLite

> ### ⚠️ CORRECTION FROM THE VERIFICATION PASS
>
> The sub-lane reported the WAL-reset bug as "≤3.51.2 affected" with mechanism NOT ESTABLISHED, because `sqlite.org/walresetbug.html` 404'd. **The verification pass found the real anchor** — `https://www.sqlite.org/wal.html#walresetbug` — and read it. The precise facts, verbatim:
>
> - **"The bug is likely present in all version of SQLite from 3.7.0 (2010-07-21) through 3.51.2 (2026-01-09)."** — a **fifteen-year** exposure window, not a recent regression.
> - **"It is fixed in version 3.51.3 (2026-03-13) and later. Backports of the fix are available for some earlier releases: 3.44.6 and 3.50.7."**
> - **"The bug only affects databases in WAL mode when there are two or more database connections open on the same file, in separate threads or processes, and when those two connections attempt to write or checkpoint at the same instant."**
> - Consequence: **database corruption** — parts of committed transactions never reach the database file.
>
> ([Write-Ahead Logging — §11 The WAL-Reset Bug](https://www.sqlite.org/wal.html) — accessed 2026-07-31.) **FACT / HIGH.**
>
> **Why this sharpens rather than softens the finding for us. INFERENCE / HIGH:** the trigger condition is "two or more connections **in separate threads or processes**." A Java application using a JDBC connection pool has exactly that — multiple connections on one file across threads. **An event store in WAL mode with a pooled writer is squarely in the exposed profile.** A strictly single-connection design is not. Either way the fix is a dependency bump, but the connection topology determines whether this was ever a live risk or a theoretical one, and that is worth knowing rather than guessing.

**Current line.** Latest is **3.53.4, dated 2026-07-24** — one week old. Recent train: 3.53.3 (2026-06-26), 3.53.2 (2026-06-03), 3.53.1 (2026-05-05), **3.53.0 (2026-04-09)**, 3.51.3 (2026-03-13), 3.51.0 (2025-11-04), 3.50.0 (2025-05-29) ([SQLite Release History](https://www.sqlite.org/changes.html) — accessed 2026-07-31, independently re-verified). Feature releases roughly twice yearly with rapid patch follow-ups. **FACT / HIGH.**

**Other behaviour changes worth a glance.** In **3.53.0**, floating-point rounding moved from **15 to 17 significant digits by default** (tunable via `SQLITE_DBCONFIG_FP_DIGITS`) — this changes the *text* of serialised floats, which matters if an event store hashes, diffs, or round-trips float representations. **Worth a direct check against our serialization path.** In **3.51.0** (2025-11-04), improved resistance to corruption from broken POSIX advisory locks — relevant if a database ever sits on a network mount. **FACT / HIGH.**

**JDBC driver: healthy, and it determines our actual exposure.** `xerial/sqlite-jdbc` bundles its own native SQLite, so the **driver** version — not the OS's `sqlite3` — decides whether the WAL bug is present.

- Release train and bundled SQLite, read off the releases page: 3.53.1.0 (2026-05-06, SQLite 3.53.1), 3.53.0.0 (2026-04-14, SQLite 3.53.0), **3.51.3.0 (2026-03-16, SQLite 3.52.0)**, 3.51.2.0 (2026-02-10, SQLite 3.51.2), 3.51.1.0 (2025-12-01), 3.51.0.0 (2025-11-05) ([sqlite-jdbc releases](https://github.com/xerial/sqlite-jdbc/releases) — accessed 2026-07-31). **FACT / HIGH.**
- **Version discrepancy, reported honestly:** the sub-lane read **3.53.2.0 (2026-06-05)** as latest from Maven Central; the verification pass read **3.53.1.0 (2026-05-06)** as latest from the GitHub releases page. One of the two views is stale or paginated. **The latest version number is NOT ESTABLISHED to within one release** — but it does not matter, because the load-bearing boundary is well below both.
- **Therefore: sqlite-jdbc 3.51.2.0 (2026-02-10) and older bundle affected SQLite. The first driver release carrying a fixed engine is 3.51.3.0 (2026-03-16).** **INFERENCE / HIGH.**
- **ARM/Pi coverage is good:** native builds for Linux **armv5, armv6, armv7**, and **arm64 under both glibc and musl** ([sqlite-jdbc README](https://github.com/xerial/sqlite-jdbc) — accessed 2026-07-31). No JNI compilation step on a Pi. **FACT / HIGH.**

**Action, and it is small:** check the resolved `org.xerial:sqlite-jdbc` version in the build. If **< 3.51.3.0**, bump it. That is a dependency-line edit, not a rewrite.

**VERDICT: ACT** — bounded and cheap: verify `sqlite-jdbc >= 3.51.3.0`. Everything else about SQLite is placid.

### 4d. Java / JDK LTS

**Current LTS set and support windows**, read off Oracle's roadmap ([Oracle Java SE Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) — accessed 2026-07-31). **FACT / HIGH.**

| Version | GA | Premier support ends | Extended support ends |
|---|---|---|---|
| 8 | Mar 2014 | Mar 2022 | Dec 2030 |
| 11 | Sep 2018 | Sep 2023 | Jan 2032 |
| **17** | Sep 2021 | **Sep 2026** | Sep 2029 |
| **21** | Sep 2023 | **Sep 2028** | Sep 2031 |
| **25** | Sep 2025 | **Sep 2030** | Sep 2033 |

**Release train.** **JDK 26 reached GA on 2026-03-17** and is non-LTS ([JDK 26 project page](https://openjdk.org/projects/jdk/26/) — GA 2026-03-17, accessed 2026-07-31). **JDK 27 is scheduled for Sep 2026**, also non-LTS. Oracle states LTS every two years, making **JDK 29 (Sep 2027)** the next LTS. **FACT / HIGH.**

**Has the conservative pin moved? Yes — one notch, and there is a date on it.** **JDK 17 Premier support ends September 2026 — approximately two months from today.** For a conservative Pi-targeting project, **JDK 21 is now the floor** (Premier through Sep 2028) and **JDK 25 is the forward choice** (Premier through Sep 2030). Staying on 17 past September 2026 means running an LTS in Extended support — not dangerous, but off the mainstream update path. **INFERENCE / HIGH.** If we are already on 21 or 25 this is a non-event; if we are on 17 it is a pre-launch decision better made now than after shipping.

**Constrained ARM hardware.** Eclipse Temurin lists JDK 8, 11, 17, 21 and 25 as LTS offerings ([Adoptium Temurin releases](https://adoptium.net/temurin/releases/?os=linux&arch=aarch64) — accessed 2026-07-31). **Honest limit:** that page's architecture filter is JS-driven and rendered "No releases found," so **Temurin ARM64 binary availability for specific JDK versions is NOT ESTABLISHED from a source actually opened.** Almost certainly fine; verify at build time.

On **GC defaults, heap footprint, and ARM-specific tuning across 17 → 21 → 25**: **NOT ESTABLISHED.** No page could be opened within the time box that documents these deltas. The lane explicitly declined to recite the usual claims about SerialGC selection under low core/memory counts, container awareness, or generational ZGC defaults. *What would answer this:* a targeted lookup against the JDK 21 and 25 release notes and the HotSpot ergonomics documentation.

**VERDICT: WATCH** — no churn in the platform itself; the single dated item is JDK 17 Premier support ending Sep 2026. On 21 or 25, this is STABLE.

### GROUND TABLE

| Component | Current state (verified) | Cadence | Risk where we are pinned | Verdict |
|---|---|---|---|---|
| **EmberZNet / EZSP protocol** | Two live trains. Legacy: EmberZNet 7.5.x, GSDK 4.4/4.5, **EZSP v13 (0x0D)**, 7.5.0.0 dated 2025-02-26, "Deprecated Items: None". Forward: Zigbee 9.1.1 dated 2026-07-29, EZSP 0x13 | SiSDK: 2 bundles/yr + revisions every 4–10 wks; GSDK 4.x stable | **Very low.** v13 is the enforced *minimum* for Z2M's `ember` adapter and the version Nabu Casa ships on MG24 today. Only real risk is self-inflicted: hardcoding `13` host-side | **STABLE** |
| **Host library (bellows / negotiation)** | bellows **0.49.2, 2026-05-27**; registry spans v4–v18; live `EZSPv13` class | Every 1–2 months | **Very low.** No version handler has ever been removed. Firmware picks the version, host adapts upward. README is stale — trust the source | **STABLE** |
| **MG24 coordinator hardware** | Confirmed MG24: HA **Connect ZBT-2** (2025-11-19), SONOFF **Dongle Plus MG24**, SMLIGHT **SLZB-07Mg24**, Seeed Xiao MG24. *Not* MG24: ZBDongle-E, ZBT-1, SLZB-07 base | New reference hardware ~every 2 yrs | **Low.** Ecosystem converging on MG24 — we are on the forward chip | **STABLE** |
| **MG24 firmware supply chain** | NabuCasa builder **v2026.02.23**, EmberZNet **7.5.1.0**, targets ZBT-2. darkxst builder last release **2025-06-27** — ~13 months stale, single maintainer, covers SONOFF/SMLIGHT/Aeotec/Seeed | NabuCasa: 1–3 months. darkxst: none in 13 months | **Medium.** Nabu Casa path is org-backed, healthy, *and ships EZSP v13*. Third-party sticks depend on one volunteer; SONOFF publishes no firmware versions, so a replacement unit's EZSP version is unpredictable at purchase | **WATCH** |
| **SQLite engine** | **3.53.4, 2026-07-24**. WAL-reset corruption bug present **3.7.0 (2010-07-21) → 3.51.2 (2026-01-09)**, fixed **3.51.3 (2026-03-13)**; requires WAL + 2 or more connections across threads/processes. FP default 15→17 sig digits in 3.53.0 | ~2 feature releases/yr + fast patches | **Medium until checked.** A WAL-mode event store with a pooled writer on a Pi is exactly the exposed profile. Fix is a version bump | **ACT** |
| **sqlite-jdbc (Java driver)** | Latest 3.53.1.0 (2026-05-06) per GitHub / 3.53.2.0 (2026-06-05) per Maven — discrepancy unresolved, immaterial. Bundles its own native SQLite. ARM natives for armv5/6/7 + arm64 (glibc & musl) | Tracks upstream within ~1–4 wks | **Low once bumped.** Driver version determines WAL-bug exposure: **< 3.51.3.0 is affected** | **ACT** (verify ≥ 3.51.3.0) |
| **JDK / LTS** | LTS: 8, 11, 17, 21, 25. **JDK 17 Premier ends Sep 2026**; 21 → Sep 2028; 25 → Sep 2030. JDK 26 GA 2026-03-17 (non-LTS); next LTS **29, Sep 2027** | Release every 6 mo; LTS every 2 yrs | **Low, but dated.** On 21 or 25: nothing to do. On 17: Premier lapses in ~2 months. ARM64 build availability and GC-default deltas **NOT ESTABLISHED** | **WATCH** |

**Overall read: low drama, as expected — with one small, cheap, dated exception.** The Zigbee side is the pleasant surprise: EZSP v13 is not a legacy version being sunset, it is the *floor* the modern ecosystem enforces and the version the best-maintained MG24 firmware ships today. The single real action item is the SQLite WAL-reset bug, closed by confirming `sqlite-jdbc >= 3.51.3.0`. Two things to watch rather than act on: single-maintainer firmware for third-party MG24 sticks, and JDK 17's Premier support ending in September 2026 if that is where we sit. **Nothing here implies a rewrite.**

---

## §5 — Nightly self-test and hardware-in-the-loop regimes

**Bottom line:** **no home-automation platform — open source or commercial — publishes automated, scheduled, real-silicon benchmark results.** HIL CI is a mature, named discipline one layer down the stack (kernel, RTOS, silicon vendors, device-OS companies) and is essentially absent from consumer smart-home *product* engineering. The publishing half is rarer still: the category's most sophisticated public data programme is install-count telemetry, not performance.

Four-rung ladder used throughout: **(a)** unit/integration tests on mocks or emulation; **(b)** manual or gate-style QA/certification on hardware; **(c)** automated, scheduled, real-silicon testing; **(d)** publicly published results/trend data from it.

### Pass A — the home-automation field

**Home Assistant Core — rung (a).** The core CI workflow triggers only on pushes to `dev`/`rc`/`master`, pull requests, and manual dispatch. **There is no `schedule:`/cron block, every job is `runs-on: ubuntu-24.04`, and there are no self-hosted runners, Raspberry Pis, or radios anywhere in it** ([`core/.github/workflows/ci.yaml`](https://raw.githubusercontent.com/home-assistant/core/dev/.github/workflows/ci.yaml) — `dev` as read, accessed 2026-07-31). Official guidance points the same way: tests interact only through `async_setup_component`, `hass.states`, and `hass.services`; real devices are not mentioned ([Testing your code | HA Developer Docs](https://developers.home-assistant.io/docs/development_testing/) — "Last updated on Jun 10, 2026", accessed 2026-07-31). **FACT / HIGH.**

**Home Assistant Operating System — rung (a), and this is the sharp one.** HAOS's `test.yaml` runs on `workflow_dispatch` and `workflow_call` — **no cron** — on `ubuntu-22.04`, installing `qemu-system-x86 ovmf` and booting the extracted OS image **in a virtual machine** ([`operating-system/.github/workflows/test.yaml`](https://raw.githubusercontent.com/home-assistant/operating-system/dev/.github/workflows/test.yaml) — `dev` as read, accessed 2026-07-31). **INFERENCE / HIGH: the organisation that designs and sells Home Assistant Green, Yellow, and the Connect ZBT dongles validates its own operating system in emulation, not on the boards it ships.**

**Home Assistant hardware QA — rung (b), demonstrably reactive.** The ZBT-1 recall: a defective voltage regulator bricked units on certain USB-A ports; the failure was found by customers, and the team wrote that **"It took us a couple of weeks to replicate the problem with our own units. We went down some wrong paths"** and that internally they **"have only found one desktop that causes this failure"** ([Connect ZBT-1 issue and replacement](https://www.home-assistant.io/blog/2024/10/02/connect-zbt1-issue-and-replacement/) — dated 2024-10-02, accessed 2026-07-31). The ZBT-2 launch post is the closest thing to published hardware performance data in this category and it is anecdotal — a before/after network map showing "about a 60% increase in direct connections," explicitly captioned **"Not science."** No methodology, no repeatable workload, no trend ([ZBT-2 launch](https://www.home-assistant.io/blog/2025/11/19/home-assistant-connect-zbt-2/) — dated 2025-11-19, accessed 2026-07-31).

**ESPHome — rung (a), explicitly.** *"These are compile tests only and do not test functionality."* Validation configs are run through `esphome config` and "never compiled" ([Component/platform test configurations](https://developers.esphome.io/architecture/ci/component_tests/) — undated, accessed 2026-07-31). **For a project whose entire output is firmware for physical ESP32s, nothing is ever flashed to a board in CI.**

**Zigbee2MQTT / zigbee-herdsman — rung (a), with a partial perf discipline worth noting.** CI runs on `ubuntu-latest` with Node 24; no serial device, no coordinator, no hardware step. But it *does* run continuous microbenchmarks — `Nerivec/action-ci-bench@main` with `npx vitest bench --run --outputJson bench.json`, `compare-against: master`, reported back into the PR/commit context — **not to a public dashboard or trend store** ([`zigbee-herdsman/.github/workflows/ci.yml`](https://raw.githubusercontent.com/Koenkk/zigbee-herdsman/master/.github/workflows/ci.yml) — `master` as read, accessed 2026-07-31). This is the nearest thing to perf-regression discipline in the Zigbee host-stack world, and it is software-only, PR-scoped, and unpublished.

**openHAB — rung (a).** JUnit + Mockito plus OSGi integration tests; no physical devices, and integration tests are advised to be "used sparingly" ([Writing tests | openHAB](https://v2.openhab.org/docs/developer/tests.html) — undated, accessed 2026-07-31). ⚠️ **Could not read:** `https://ci.openhab.org/` returned ROBOTS_DISALLOWED. An unadvertised hardware job on their Jenkins cannot be ruled out. **openHAB negative capped at MED.**

**Z-Wave JS — the most interesting near-miss.** `zwave-js/remote-ctt-tests` is "a complete framework for running Z-Wave CTT certification tests against a Controller DUT" with "a ready-to-use GitHub Actions workflow for running CTT tests in CI using WSL." Crucially it uses **device emulation based on the 'Open Source' Z-Wave stack** — virtualised controllers and end devices on TCP ports, not physical radios. No stated nightly cadence, no published results ([zwave-js/remote-ctt-tests](https://github.com/zwave-js/remote-ctt-tests) — accessed 2026-07-31). Automated *certification* testing, impressive for an OSS project, but rung (a)-with-protocol-fidelity, not rung (c).

**SmartThings — rung (b).** The SmartThings Test Suite requires real hardware — an Android phone, a Station or Hub, a specific sensor or bulb — but the run requires the operator to "perform the indicated user actions for every test case" and "observe the behavior of the bulb" ([Test Edge Drivers using SmartThings Test Suite](https://developer.samsung.com/codelab/smartthings/test-suite.html) — references "SDC2024", accessed 2026-07-31). Real devices, human in the loop, third-party device makers as the subject, certification gate as the purpose.

**Works with Home Assistant — rung (b), one-time.** "Our expert team tests devices," explicitly "not simply a pass/fail." Once the badge is awarded, **no ongoing validation mechanism is described** ([Works with Home Assistant](https://works-with.home-assistant.io/) — undated, accessed 2026-07-31). The 2025 recap adds "previously, everyone was testing in their own way, but now we've standardized the way we test" — process standardisation, not automation ([WWHA 2025 recap](https://www.home-assistant.io/blog/2025/12/09/wwha-2025-recap/) — dated 2025-12-09, accessed 2026-07-31).

**Hubitat, Homey, Tasmota, other commercial hubs — nothing found.** Searches returned only consumer comparison-review content and build-system workflows. **No vendor engineering blog, no test-lab description, no published reliability metrics from any commercial hub vendor surfaced.** Corroborating absence: the widely-referenced curated list of hardware-test/HIL projects covers 20+ test execution engines, analytics platforms, and instrument interfaces — and **contains zero home-automation entries** ([awesome-hardware-test](https://github.com/sschaetz/awesome-hardware-test) — accessed 2026-07-31).

**Pass A conclusion — FACT (for the specific repos read) / MED (as a category-wide negative, per §0's absence rule):** the field sits almost entirely at rung (a), with rung (b) for hardware and certification. **No instance of rung (c) was found, and no instance at all of rung (d).**

### Pass B — the comparison class

**Zephyr RTOS — first-class HIL tooling, privately operated.** Twister has purpose-built hardware support: `west twister --generate-hardware-map map.yml` produces a device inventory, and `--device-testing --hardware-map` builds, flashes, and runs across every mapped board, with `fixtures` matched to test requirements ([Test Runner (Twister)](https://docs.zephyrproject.org/latest/develop/twister/index.html) — undated, accessed 2026-07-31). **Note the asymmetry: the tooling is upstream and excellent; the hardware labs are private to member companies.** The publicly published Zephyr dashboard is the Renode one — "running a range of samples over 470 simulated boards," entirely simulation-based ([Renode Zephyr Dashboard](https://www.zephyrproject.org/improving-data-sources-and-tests-in-the-renode-zephyr-dashboard-and-renodepedia/) — dated 2024-05-28, accessed 2026-07-31).

**KernelCI — the gold standard for (c) + (d).** Distributed labs execute test requests from Maestro; **"Maestro will pull and build a number of git trees every hour,"** with results in a common database (KCIDB) and a public dashboard ([Test your platform | KernelCI](https://docs.kernelci.org/intro/platform-testing/) — last modified 2025-08-04, accessed 2026-07-31). **This is the one place found where scheduled real-hardware testing *and* public result publication coexist as institutional practice.**

**Espressif ESP-IDF — real HIL, internal, unpublished.** ESP-IDF "provides a variety of testing mechanisms that runs directly on target ESP chips (referred to as **target test**)"; in CI, jobs are dispatched to "a CI runner with the corresponding tag" with binaries from "our internal MinIO servers" ([ESP-IDF Tests with Pytest Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/contribute/esp-idf-tests-with-pytest.html) — undated, accessed 2026-07-31). **FACT / HIGH** a silicon vendor runs automated tests on real chips in CI; **INFERENCE / HIGH** the results are internal, not published trends.

**balena — real-device HIL for an IoT device OS, unpublished.** "Every pull request in the meta-balena repository builds balenaOS for each device-type we support," with QEMU for fast feedback and physical-device testing through distributed **AutoKit** rigs. No indication of public result publication ([From PR to Release; OS Testing at balena](https://blog.balena.io/from-pr-to-release-os-testing-at-balena/) — dated 2023-02-10, accessed 2026-07-31).

**Golioth — HIL as advocacy, not assumed baseline.** *"It is my belief that HIL testing should be a part of any firmware testing strategy"* and "my goal with this post is to show you that it's not so difficult to get a minimum viable HIL set up within one week" ([Golioth HIL Testing Part 2](https://blog.golioth.io/golioth-hil-testing-part2/) — dated 2022-08-18, accessed 2026-07-31). **INFERENCE / HIGH: you do not write "it's not so difficult, here's how" posts about practices that are already table stakes.**

**OpenHiL — the field's own admission that this is bespoke work.** A community founded in **2024** by engineers "tired of rebuilding the wheel constantly" and of "proprietary, expensive hardware automation jigs" ([Open Hardware in the Loop Community](https://openhil.github.io/) — accessed 2026-07-31).

**Matter / CSA — a point-in-time gate, not continuous.** Certification runs through Authorized Test Labs or CSA Specification Validation Events; the output is a PDF certificate, a listing, a Certification Declaration blob, and a Distributed Compliance Ledger entry ([Matter Certification – How it Works](https://matter-smarthome.de/en/development/how-the-matter-certification-works/) — dated 2023-03-12, updated 2025-04-29, accessed 2026-07-31). **FACT / HIGH: the artifact of Matter certification is a certificate, not a test stream.** **OPINION / MED:** exactly the wrong shape for catching regressions.

**Pass B conclusion — FACT / HIGH:** HIL CI is a real, named, tooled engineering discipline with mature implementations. **INFERENCE / HIGH:** it lives in kernel, RTOS, silicon-vendor, and device-OS engineering — one layer *below* smart-home product teams — and even there, *publishing* results is rare, KernelCI being the notable exception.

### Pass C — the publishing angle

**Precedents outside the category (all real, all readable).**

- **rustc:** "After every PR is merged, a suite of benchmarks are run against the compiler," and "The results are tracked over time on the https://perf.rust-lang.org/ website" ([Performance testing — rustc dev guide](https://rustc-dev-guide.rust-lang.org/tests/perf.html) — undated, accessed 2026-07-31).
- **Chrome:** "Chrome has multiple performance labs in which benchmarks are run on continuous builds to pinpoint performance regressions down to individual changelists," publicly visible at the chrome.perf console and "monitored by several perf sheriff rotations" ([How does Chrome measure performance?](https://raw.githubusercontent.com/chromium/chromium/main/docs/speed/how_does_chrome_measure_performance.md) — `main` as read, accessed 2026-07-31). ⚠️ The canonical chromium.googlesource.com copy timed out; the GitHub mirror was read instead.
- **KernelCI:** public dashboard + KCIDB, per Pass B.
- **Renode Zephyr Dashboard:** 470+ boards, continuously updated, simulated.

**Inside the category: nothing.** The most sophisticated public data programme in home automation is **Home Assistant Analytics** — 625,530 active installations, version history, installation types, OS versions, board types, integrations — **with no performance, latency, or reliability metrics whatsoever**, self-declared as opt-in from under 25% of users ([Home Assistant Analytics](https://analytics.home-assistant.io/) — live figures, accessed 2026-07-31). The one search result promising a smart-home "Latency Chart" turned out to be an affiliate-monetised explainer with **no measurements at all** ([Latency Chart — DIY Smart Home Hub](https://www.diysmarthomehub.com/latency-chart) — dated 2026-06-13, accessed 2026-07-31).

**Which half is actually rare?**

| | In smart home | In adjacent embedded/software |
|---|---|---|
| Automated real-hardware CI | **Not found** | Established (Zephyr, ESP-IDF, balena, KernelCI, Golioth) |
| Published perf/reliability trends | **Not found** | Established (rustc-perf, chrome.perf, KernelCI dashboard) |

**INFERENCE / MED-HIGH:** "we run HIL" is rare *in this category* but a skeptic can correctly say it is ordinary hygiene one layer down. **"We run it nightly and publish the numbers" is rare in both columns simultaneously** — even Espressif and balena, who run genuine HIL, do not publish. **That combination is the harder-to-deflate half of the claim.**

### Pass D — the verdict

**Is a nightly, published, real-silicon self-benchmark a genuine differentiator in home automation? Yes — INFERENCE / MED-HIGH.** Zero counterexamples across HA Core, HAOS, Works with HA, ESPHome, Zigbee2MQTT/zigbee-herdsman, openHAB, Z-Wave JS, Tasmota, SmartThings, Hubitat, and Homey. Capped at MED-HIGH per §0's absence rule, lifted slightly by having read actual CI workflow files rather than marketing pages, and knocked back by one unreadable source (openHAB's Jenkins) and by commercial vendors' internal practice being unobservable by construction.

**What the skeptical engineer says — six objections, ranked by how much they hurt:**

1. **"One Pi with a dongle on a shelf is not a HIL rig."** *(most damaging)* Real HIL practice implies power cycling, fault/RF injection, controlled environment, multi-DUT orchestration — the DUTLink/AutoKit/labgrid class of apparatus. A single unattended board is closer to "a dev board that runs cron." **Pre-empt with an explicit scope statement.**
2. **"Nightly numbers from one unit measure your rig's noise floor."** Without pinned CPU governor, thermal control, N repetitions, variance bands, and a regression-detection policy, night-over-night deltas are mostly SD-card and thermal noise. Chrome mitigates with sheriff rotations and per-CL bisect; rustc with try-runs against a fixed corpus. **This is a methodological requirement, not a rhetorical one — publish variance or the trend line is decorative.**
3. **"HIL is table stakes in embedded. You're claiming credit for hygiene Espressif and Zephyr had a decade ago."** Partly fair. The honest answer is a comparison-class argument: the relevant peer set for a smart-home core is Home Assistant, openHAB, and Hubitat — not Nordic. **The claim is about *this* category and must be stated that way.**
4. **"Self-published, self-selected numbers are marketing."** Mitigation: publish the method, the raw data, and **the bad nights**. Trend dashboards that never show a regression read as fabricated; ones that show and then close regressions read as real.
5. **"A real radio is not a real network."** A coordinator with a handful of bench devices is not a 60-node mesh with a microwave and a neighbour's Wi-Fi. **Do not generalise from bench topology to deployed topology.**
6. **"Nobody publishes because nobody buying a hub cares."** Absence of practice may indicate absence of demand rather than absence of rigor. Counter: the audience for this claim is not the median buyer — it is the technically-motivated self-hoster and the reviewer, both unusually receptive to method transparency.

**The honest, defensible version of the claim:**

> Every night, unattended, the current build is deployed to physical Raspberry Pi hardware with a real Zigbee coordinator, runs a fixed workload, and records latency and correctness results — which are published, including regressions, as a public trend. We could not find another home-automation platform, open source or commercial, that publishes automated real-hardware benchmark trends. The discipline is borrowed from kernel and RTOS engineering — KernelCI, Zephyr's Twister hardware maps, Espressif's target tests — where it is established practice; what appears to be new is applying it to a consumer smart-home core and showing the numbers.

**Claims to NOT make:**

- ❌ "First HIL testing in home automation" — unfalsifiable and probably false for private internal practice.
- ❌ "Nobody else tests on real hardware" — false. Nabu Casa does manual hardware QA; SmartThings certification runs on real hubs and devices; balena and Espressif run genuine HIL.
- ❌ "Certified" / "validated" — do not let a self-run bench borrow the connotations of a CSA/ATL certification, which is a formally different and point-in-time artifact.
- ❌ Any single-run performance number without variance.

**The strongest, least attackable framing is the publishing, not the testing:** HIL is rare-in-category but ordinary-in-industry; a continuously published, regression-inclusive performance trend for a smart-home platform is, on this evidence, without precedent in either.

### SEARCH-WORK LOG (§5)

**30 queries run**, covering: HA hardware-in-the-loop/CI/nightly (multiple phrasings); ESPHome CI on real ESP32; zigbee2mqtt/zigbee-herdsman hardware CI; HA Green/Yellow/ZBT-1 hardware test lab; Matter connectedhomeip CI hardware; Tasmota CI; Zephyr Twister hardware; KernelCI/LAVA; Hubitat/SmartThings/Homey regression testing and published reliability metrics; HA performance benchmark/regression tracking; open-source smart home HIL nightly rig; Z-Wave JS controller CI; HA "test farm"/"device lab" proposals; public nightly perf dashboards (rust/chrome/ClickHouse); Espressif CI runners; pytest-embedded; Matter recertification-on-firmware-update; smart-home vendor latency dashboards; Nordic HIL; balena leviathan/autokit; Chromium/Mozilla perf dashboards; vendor engineering blogs; Works with HA testing requirements.

**Queries returning zero home-automation hits — the informative nulls:** `Home Assistant hardware-in-the-loop testing CI real hardware nightly` (only generic HIL vendor content); `zigbee2mqtt zigbee-herdsman CI testing real Zigbee coordinator hardware automated`; `Hubitat SmartThings Homey automated regression testing hardware lab published reliability metrics` (**entirely consumer listicles**); `open source smart home project "hardware in the loop" nightly test rig Raspberry Pi Zigbee`; `home-assistant github discussion "hardware in the loop" OR "test farm" OR "device lab"` (**no Home Assistant results at all**); `smart home hub vendor publishes public latency reliability benchmark dashboard`; `"nightly" benchmark published home automation platform performance regression`.

**~28 pages opened and read** — the principal ones cited inline above.

**Blocked / unreadable (routed around, never summarised):** `ci.openhab.org` (ROBOTS_DISALLOWED — openHAB negative capped at MED); GitHub contents API for home-assistant/core workflows (403 — worked around via `raw.githubusercontent.com`); `chromium.googlesource.com` perf README (timeout — substituted GitHub mirror); Zephyr Twister canonical URL (redirect stub — followed to the real page).

**Deliberately not pursued (time-box):** Nordic's internal CI (no public docs found); Amazon/Google internal device labs (unobservable); automotive/aero HIL standards literature — the discipline point is already established without it.

**Non-finding worth recording:** a Justia patent on robotic smart-device regression testing (filed 2018-11-26) describes a gantry robot pressing buttons — but on **utility electric and gas meters**, not home-automation devices. Not a category counterexample.

---

## §6 — WHAT CHANGES OUR PLANS

Seven findings that should alter an ordering, a bet, or a message. Written last, and written hard.

---

**1. Our read-time-staleness claim gets falsified in its current form — it needs four qualifiers, and one of them is a product decision we may not have made yet.**

Three shipping counter-examples partially satisfy "read-time staleness from a per-entity reporting contract" (HA MQTT `expire_after`, SmartThings `checkInterval`, Hubitat Device Activity Check), so the claim only survives with all four qualifiers intact: **core/platform-wide · every reader · `stale` distinct from `unavailable` · computed at the read.** The third is not a wording choice — it is a data-model commitment, and SmartThings already ships tri-state (`ONLINE`/`UNHEALTHY`/`OFFLINE`) while openHAB's `expire` actively *destroys* the last known value. **If we ship binary ALIVE/DEAD we are epistemically behind the largest incumbent and the claim collapses to marketing.** → *§3 VERDICT + the four qualifiers; §1.3 SmartThings tri-state; §3 Pass A openHAB `expire`.*

---

**2. Lead the technical message with "nothing watches the watcher," not with "read-time derivation" — it is the argument a skeptic cannot answer.**

Z2M's ping loop silently stopped emitting across three releases while `last_seen` kept updating and everything looked healthy; ZHA's availability checker does not run until a human reloads the integration. **Both convert a bounded lie into an unbounded one, and read-time derivation is structurally immune to the failure mode** — there is no prober whose own death can go unnoticed, because there is no prober. This is a stronger, more concrete, more demonstrable argument than the staleness framing, and unlike claim #1 it has no counter-examples. → *§2 Exhibits 2 and 3; §2 PATTERN READ #2.*

---

**3. The most persuasive public artifact we have is a number, not an architecture: the field's shipped defaults permit 10 minutes to 25 hours of false-ALIVE.**

ZHA ships 2 h mains / 6 h battery; Z2M ships 10 min active / 25 h passive **and the availability feature is off by default**; ZHA's own docs suggest lowering to 1 hour "if you want faster detection when a plug or bulb loses power." These are citable, user-legible, vendor-documented numbers — not our characterisation of their behaviour. **A demo that shows a leak sensor with its batteries out still reading healthy is more convincing than any explanation of read-time derivation, and every number in it comes from the incumbents' own documentation.** → *§1.1 and §1.2 defaults; §2 Exhibits 1, 10, 11.*

---

**4. Reframe the nightly bench as *publishing*, not *testing* — and the bench needs variance bands before it can be published at all.**

HIL is ordinary hygiene one layer down (Zephyr, ESP-IDF, balena, KernelCI), so "we run HIL" is deflatable by any embedded engineer; **"we run it nightly and publish the numbers, including the regressions" has no precedent in either column.** But the two most damaging objections — "one Pi on a shelf is not a HIL rig" and "nightly deltas from one unit measure your thermal noise floor" — are methodological, not rhetorical. **This adds a pre-publication requirement to B3: pinned governor, N repetitions, published variance, and an explicit scope statement about what the rig is and is not.** → *§5 Pass C table; §5 Pass D objections 1 and 2; §5 "claims to NOT make."*

---

**5. We need a stated position on sleepy/battery devices before any launch message ships — it is where every skeptic will attack, and where the whole field has quietly surrendered.**

Z2M never pings passive devices. ZHA hard-codes a `manufacturer == "LUMI"` carve-out because polling knocks Aqara devices off the mesh. Homey's answer is "configure attribute reporting and hope." Hubitat's own community-app author writes *"nor is there a good way to tell this for all devices."* And the HA community actively argues *against* tighter detection on battery-drain and flapping grounds. **Whatever we claim about never-false-ALIVE, the first question will be "what about my battery sensors," and the honest answer has real engineering constraints behind it.** → *§1 READ bullet 4; §2 PATTERN READ #5; §2 Exhibit 11 counter-pressure.*

---

**6. ACT before the charter: verify `org.xerial:sqlite-jdbc >= 3.51.3.0`. A fifteen-year-old WAL corruption bug is live in every older driver, and a pooled Java writer is exactly the exposed profile.**

The bug is present in **all SQLite from 3.7.0 (2010-07-21) through 3.51.2 (2026-01-09)**, fixed in 3.51.3 (2026-03-13), and triggers only in **WAL mode with two or more connections on the same file across separate threads or processes** writing or checkpointing simultaneously — which is precisely what a JDBC connection pool produces. Consequence is database corruption: parts of committed transactions never reach the file. **The fix is a one-line dependency edit; the first driver carrying a fixed engine is 3.51.3.0 (2026-03-16).** Also worth a direct check: SQLite 3.53.0 changed default float serialisation from 15 to 17 significant digits, which matters if we hash or diff serialised floats. → *§4c correction box; [sqlite.org/wal.html §11](https://www.sqlite.org/wal.html).*

---

**7. Retire the "are we on legacy Zigbee?" question entirely — EZSP v13 is the ecosystem's enforced floor, and Nabu Casa ships it on MG24 today. Budget zero for migration; spend ten minutes on one code check instead.**

EmberZNet 7.5.0.0's own release notes list "Deprecated Items: None"; Z2M's `ember` adapter *requires* v13 as a minimum; bellows has never removed a version handler going back to v4; and Nabu Casa's February 2026 ZBT-2 firmware ships EmberZNet 7.5.1.0 — the same v13 we are on — having deliberately not chased the 8.x/9.x train. **The only real risk is self-inflicted: if any host code asserts `version == 13` rather than reading the negotiated value, a replacement dongle with factory 8.2.x firmware will refuse to start, and SONOFF publishes no firmware version numbers so we cannot know what a new unit ships with.** Secondary watch item: the single-maintainer `darkxst` firmware fork serving most third-party MG24 sticks has had no release in 13 months — a procurement argument for standardising on the ZBT-2. → *§4a five confirmations + negotiation direction; §4b supply-chain split.*

---

### Cross-lane flags (for hub intake, not part of the seven)

- **→ R-2 (BRAND).** §2's phrase harvest was crippled by a **Reddit proxy block** this entire session — zero Reddit exhibits. R-2 has Reddit as a primary hunting ground and should expect to carry that load alone. The verbatim quotes that did survive are strong and unclaimed: *"Z2M **lies** about the state of offline devices"*; *"Hubitat will show the device having 20% **when it's actually dead**"*; *"if i unplug the device, it still shows as available."* The word the users reach for, unprompted, is **lies**. Also: §5 establishes that no competitor publishes performance or reliability data of any kind — the category's most sophisticated public dataset is install counts.
- **→ R-3 (FRONTIER).** §3 found that **Matter hands the controller a per-subscription cadence contract and Home Assistant immediately flattens it into a boolean** (`self._attr_available = self._endpoint.node.available and self._get_bridged_reachable()`, no timestamp arithmetic). This bears directly on R-3 §2's question of whether Matter solves availability-truth or inherits the same lies. On this evidence: **the protocol provides the raw material and the consumer throws it away.**
- **→ Open gaps worth a follow-up lane, in priority order.** (i) Whether Hubitat's "Last Activity At" advances on *outbound* commands — if it does, the field's most-used liveness proxy is contaminated with self-generated non-evidence, which would be a genuinely publishable finding. (ii) The ZCL specification on max-reporting-interval-as-heartbeat — if confirmed, the per-attribute cadence contract already exists at the Zigbee wire level and no consumer platform consumes it. (iii) JDK GC/footprint deltas across 17→21→25 on constrained ARM — declined today rather than recited from memory.

---

*End of R-1 return. Five sub-lanes, ~120 pages opened, ~90 cited. Four load-bearing claims independently re-verified post-hoc; one (§4c) materially corrected as a result. Blocked sources named inline rather than routed around silently.*
