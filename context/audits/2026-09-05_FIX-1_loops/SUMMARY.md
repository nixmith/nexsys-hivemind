# FAILCHAN-FIX-1 loop corpus — SUMMARY. One line per run: class · tree · run-NN · GREEN|RED · start→end (UTC, per-run stamps = the instrument's clock) · rc · the class's suite counts + wall time · the anomaly tokens seen (bus.delivery_anomaly kinds / integration.route_join_miss) [· RED: method :: message].
# Desk instrument (Windows 11, 24 cores; WSL has no JDK, so the recipe's taskset/busy loops are replicated natively): pinned = 'start /affinity 3' (cores 0,1 — the test JVM measures availableProcessors=2) + two CPU-bound PowerShell loops pinned to the same mask + -PvtParallelism=2 (the FIX-1a knob, passed as ORG_GRADLE_PROJECT_vtParallelism=2 in the environment; inert on ef02d13, which predates it); unpinned = no affinity, no knob, the two busy loops still running (the §A.5 CPU-shape row). Every run: gradlew.bat <task> --tests <class> --rerun --no-daemon --offline --console=plain (a fresh Gradle JVM per run; --rerun re-executes the test task only).
# sequence start 2026-09-05T18:21:07Z
# busy pids: 252588,261276
# loop start 2026-09-05T18:21:08Z mode=pinned tree=fix1a class=HeroLoop task=:lifecycle:lifecycle:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/lifecycle/lifecycle/build/test-results/test/TEST-com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.xml
HeroLoop · fix1a · run-01 · GREEN · 18:21:08.324→18:22:09.437 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="19.87" · tokens: none
HeroLoop · fix1a · run-02 · GREEN · 18:22:09.645→18:22:57.424 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="10.073" · tokens: none
HeroLoop · fix1a · run-03 · GREEN · 18:22:57.624→18:23:51.399 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="16.478" · tokens: none
HeroLoop · fix1a · run-04 · GREEN · 18:23:51.593→18:25:03.836 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="31.995" · tokens: none
HeroLoop · fix1a · run-05 · GREEN · 18:25:04.032→18:26:07.055 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="23.124" · tokens: none
HeroLoop · fix1a · run-06 · GREEN · 18:26:07.255→18:27:15.204 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="27.476" · tokens: none
HeroLoop · fix1a · run-07 · GREEN · 18:27:15.402→18:28:08.157 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="16.038" · tokens: none
HeroLoop · fix1a · run-08 · GREEN · 18:28:08.351→18:29:12.125 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="25.119" · tokens: none
HeroLoop · fix1a · run-09 · GREEN · 18:29:12.321→18:30:04.272 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="16.26" · tokens: none
HeroLoop · fix1a · run-10 · GREEN · 18:30:04.459→18:31:10.398 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="27.021" · tokens: none
HeroLoop · fix1a · run-11 · GREEN · 18:31:10.595→18:32:06.204 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="17.226" · tokens: none
HeroLoop · fix1a · run-12 · GREEN · 18:32:06.402→18:33:02.914 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="21.749" · tokens: none
HeroLoop · fix1a · run-13 · GREEN · 18:33:03.109→18:34:11.429 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="29.006" · tokens: none
HeroLoop · fix1a · run-14 · GREEN · 18:34:11.622→18:35:08.298 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="16.047" · tokens: none
HeroLoop · fix1a · run-15 · GREEN · 18:35:08.495→18:36:15.464 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="27.625" · tokens: none
HeroLoop · fix1a · run-16 · GREEN · 18:36:15.663→18:37:10.408 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="16.73" · tokens: none
HeroLoop · fix1a · run-17 · GREEN · 18:37:10.590→18:38:04.154 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="14.647" · tokens: none
HeroLoop · fix1a · run-18 · GREEN · 18:38:04.346→18:39:05.972 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="24.014" · tokens: none
HeroLoop · fix1a · run-19 · GREEN · 18:39:06.169→18:40:09.235 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="21.919" · tokens: none
HeroLoop · fix1a · run-20 · GREEN · 18:40:09.428→18:40:58.367 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="11.236" · tokens: none
# loop end 2026-09-05T18:40:58Z
# loop start 2026-09-05T18:40:58Z mode=pinned tree=fix1a class=ReplayIT task=:core:event-bus:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/core/event-bus/build/test-results/test/TEST-com.homesynapse.event.bus.ReplayTransitionIT.xml
ReplayIT · fix1a · run-01 · GREEN · 18:40:58.700→18:41:47.893 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="11.628" · tokens: none
ReplayIT · fix1a · run-02 · GREEN · 18:41:48.079→18:42:41.230 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="16.846" · tokens: none
ReplayIT · fix1a · run-03 · GREEN · 18:42:41.438→18:43:36.661 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="17.261" · tokens: none
ReplayIT · fix1a · run-04 · GREEN · 18:43:36.851→18:44:21.762 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="9.808" · tokens: none
ReplayIT · fix1a · run-05 · GREEN · 18:44:21.968→18:45:14.572 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="14.989" · tokens: none
ReplayIT · fix1a · run-06 · GREEN · 18:45:14.770→18:45:43.322 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.212" · tokens: none
ReplayIT · fix1a · run-07 · GREEN · 18:45:43.529→18:46:11.774 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.187" · tokens: none
ReplayIT · fix1a · run-08 · GREEN · 18:46:11.959→18:46:39.958 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.161" · tokens: none
ReplayIT · fix1a · run-09 · GREEN · 18:46:40.136→18:47:10.539 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.198" · tokens: none
ReplayIT · fix1a · run-10 · GREEN · 18:47:10.724→18:47:38.250 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.198" · tokens: none
ReplayIT · fix1a · run-11 · GREEN · 18:47:38.435→18:48:06.141 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.19" · tokens: none
ReplayIT · fix1a · run-12 · GREEN · 18:48:06.317→18:48:38.068 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.242" · tokens: none
ReplayIT · fix1a · run-13 · GREEN · 18:48:38.255→18:49:06.463 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.244" · tokens: none
ReplayIT · fix1a · run-14 · GREEN · 18:49:06.650→18:49:34.690 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.193" · tokens: none
ReplayIT · fix1a · run-15 · GREEN · 18:49:34.880→18:50:03.035 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.16" · tokens: none
ReplayIT · fix1a · run-16 · GREEN · 18:50:03.212→18:50:30.983 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.182" · tokens: none
ReplayIT · fix1a · run-17 · GREEN · 18:50:31.173→18:51:01.530 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.172" · tokens: none
ReplayIT · fix1a · run-18 · GREEN · 18:51:01.735→18:51:30.215 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.26" · tokens: none
ReplayIT · fix1a · run-19 · GREEN · 18:51:30.403→18:51:57.961 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.185" · tokens: none
ReplayIT · fix1a · run-20 · GREEN · 18:51:58.146→18:52:25.724 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.17" · tokens: none
# loop end 2026-09-05T18:52:25Z
# loop start 2026-09-05T18:52:26Z mode=unpinned tree=fix1a class=HeroLoop-cpushape task=:lifecycle:lifecycle:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/lifecycle/lifecycle/build/test-results/test/TEST-com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.xml
HeroLoop-cpushape · fix1a · run-01 · GREEN · 18:52:26.054→18:52:36.816 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.064" · tokens: none
HeroLoop-cpushape · fix1a · run-02 · GREEN · 18:52:37.023→18:52:48.041 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.101" · tokens: none
HeroLoop-cpushape · fix1a · run-03 · GREEN · 18:52:48.227→18:52:58.907 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.077" · tokens: none
HeroLoop-cpushape · fix1a · run-04 · GREEN · 18:52:59.095→18:53:10.085 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.134" · tokens: none
HeroLoop-cpushape · fix1a · run-05 · GREEN · 18:53:10.271→18:53:21.060 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.079" · tokens: none
HeroLoop-cpushape · fix1a · run-06 · GREEN · 18:53:21.254→18:53:32.078 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.026" · tokens: none
HeroLoop-cpushape · fix1a · run-07 · GREEN · 18:53:32.255→18:53:42.956 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.031" · tokens: none
HeroLoop-cpushape · fix1a · run-08 · GREEN · 18:53:43.144→18:53:53.900 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.062" · tokens: none
HeroLoop-cpushape · fix1a · run-09 · GREEN · 18:53:54.086→18:54:05.012 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.035" · tokens: none
HeroLoop-cpushape · fix1a · run-10 · GREEN · 18:54:05.197→18:54:16.017 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.074" · tokens: none
# loop end 2026-09-05T18:54:16Z
# loop start 2026-09-05T18:54:16Z mode=pinned tree=ef02d13 class=HeroLoop task=:lifecycle:lifecycle:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/hs-ef02d13/lifecycle/lifecycle/build/test-results/test/TEST-com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.xml
HeroLoop · ef02d13 · run-01 · GREEN · 18:54:16.330→18:54:44.903 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.245" · tokens: none
HeroLoop · ef02d13 · run-02 · GREEN · 18:54:45.100→18:55:12.793 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.123" · tokens: none
HeroLoop · ef02d13 · run-03 · GREEN · 18:55:12.988→18:55:41.483 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.303" · tokens: none
HeroLoop · ef02d13 · run-04 · GREEN · 18:55:41.665→18:56:09.912 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="6.835" · tokens: none
HeroLoop · ef02d13 · run-05 · GREEN · 18:56:10.106→18:56:38.885 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.667" · tokens: none
HeroLoop · ef02d13 · run-06 · GREEN · 18:56:39.076→18:57:06.892 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.223" · tokens: none
HeroLoop · ef02d13 · run-07 · GREEN · 18:57:07.070→18:57:35.181 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.099" · tokens: none
HeroLoop · ef02d13 · run-08 · GREEN · 18:57:35.372→18:58:06.242 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="8.502" · tokens: none
HeroLoop · ef02d13 · run-09 · GREEN · 18:58:06.420→18:58:42.242 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="15.332" · tokens: none
HeroLoop · ef02d13 · run-10 · GREEN · 18:58:42.432→18:59:08.777 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="6.288" · tokens: none
HeroLoop · ef02d13 · run-11 · GREEN · 18:59:08.966→18:59:40.768 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="6.468" · tokens: none
HeroLoop · ef02d13 · run-12 · GREEN · 18:59:40.960→19:00:09.015 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="6.655" · tokens: none
HeroLoop · ef02d13 · run-13 · GREEN · 19:00:09.193→19:00:37.044 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.111" · tokens: none
HeroLoop · ef02d13 · run-14 · GREEN · 19:00:37.232→19:01:04.567 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="6.986" · tokens: none
HeroLoop · ef02d13 · run-15 · GREEN · 19:01:04.750→19:01:33.322 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="6.84" · tokens: none
HeroLoop · ef02d13 · run-16 · GREEN · 19:01:33.503→19:03:31.010 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="96.863" · tokens: none
HeroLoop · ef02d13 · run-17 · GREEN · 19:03:31.196→19:04:00.081 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="6.98" · tokens: none
HeroLoop · ef02d13 · run-18 · GREEN · 19:04:00.262→19:04:33.713 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.427" · tokens: none
HeroLoop · ef02d13 · run-19 · GREEN · 19:04:33.896→19:05:02.679 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.032" · tokens: none
HeroLoop · ef02d13 · run-20 · GREEN · 19:05:02.857→19:05:31.415 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.021" · tokens: none
# loop end 2026-09-05T19:05:31Z
# busy loops stopped
# sequence end 2026-09-05T19:05:31Z
# noload sequence start 2026-09-05T19:05:38Z — pinned (start /affinity 3 + the knob) WITHOUT busy loops; the shape of run-0-smoke
# loop start 2026-09-05T19:05:38Z mode=pinned tree=fix1a-noload class=ReplayIT task=:core:event-bus:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/core/event-bus/build/test-results/test/TEST-com.homesynapse.event.bus.ReplayTransitionIT.xml
ReplayIT · fix1a-noload · run-01 · GREEN · 19:05:38.703→19:05:57.918 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.025" · tokens: none
ReplayIT · fix1a-noload · run-02 · GREEN · 19:05:58.090→19:06:17.199 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.087" · tokens: none
ReplayIT · fix1a-noload · run-03 · GREEN · 19:06:17.386→19:06:36.625 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.052" · tokens: none
ReplayIT · fix1a-noload · run-04 · GREEN · 19:06:36.807→19:06:55.868 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.026" · tokens: none
ReplayIT · fix1a-noload · run-05 · GREEN · 19:06:56.039→19:07:15.466 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.052" · tokens: none
ReplayIT · fix1a-noload · run-06 · GREEN · 19:07:15.641→19:07:34.455 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.024" · tokens: none
ReplayIT · fix1a-noload · run-07 · GREEN · 19:07:34.635→19:07:54.090 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.027" · tokens: none
ReplayIT · fix1a-noload · run-08 · GREEN · 19:07:54.269→19:08:13.825 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.052" · tokens: none
ReplayIT · fix1a-noload · run-09 · GREEN · 19:08:14.010→19:08:33.098 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.027" · tokens: none
ReplayIT · fix1a-noload · run-10 · GREEN · 19:08:33.268→19:08:52.285 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.02" · tokens: none
ReplayIT · fix1a-noload · run-11 · GREEN · 19:08:52.457→19:09:11.823 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.015" · tokens: none
ReplayIT · fix1a-noload · run-12 · GREEN · 19:09:12.011→19:09:31.382 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.029" · tokens: none
ReplayIT · fix1a-noload · run-13 · GREEN · 19:09:31.552→19:09:50.823 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.027" · tokens: none
ReplayIT · fix1a-noload · run-14 · GREEN · 19:09:50.997→19:10:10.138 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.035" · tokens: none
ReplayIT · fix1a-noload · run-15 · GREEN · 19:10:10.313→19:10:29.618 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.036" · tokens: none
ReplayIT · fix1a-noload · run-16 · GREEN · 19:10:29.794→19:10:48.651 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.027" · tokens: none
ReplayIT · fix1a-noload · run-17 · GREEN · 19:10:48.828→19:11:07.716 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.049" · tokens: none
ReplayIT · fix1a-noload · run-18 · GREEN · 19:11:07.893→19:11:27.066 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.015" · tokens: none
ReplayIT · fix1a-noload · run-19 · GREEN · 19:11:27.233→19:11:46.155 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.019" · tokens: none
ReplayIT · fix1a-noload · run-20 · RED · 19:11:46.333→19:12:16.211 · rc=1 · tests="1" skipped="0" failures="1" errors="0" time="18.668" · tokens: none · RED: subscriber resumes from persisted checkpoint and catches up  :: java.lang.AssertionError: Checkpoint for 'replay-it-sub' did not reach 1000 within 15000 ms
# loop end 2026-09-05T19:12:16Z
# loop start 2026-09-05T19:12:16Z mode=pinned tree=fix1a-noload class=HeroLoop task=:lifecycle:lifecycle:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/lifecycle/lifecycle/build/test-results/test/TEST-com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.xml
HeroLoop · fix1a-noload · run-01 · GREEN · 19:12:16.572→19:12:32.615 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.195" · tokens: none
HeroLoop · fix1a-noload · run-02 · GREEN · 19:12:32.789→19:12:48.431 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.169" · tokens: none
HeroLoop · fix1a-noload · run-03 · GREEN · 19:12:48.616→19:13:04.667 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.119" · tokens: none
HeroLoop · fix1a-noload · run-04 · GREEN · 19:13:04.841→19:13:20.983 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.149" · tokens: none
HeroLoop · fix1a-noload · run-05 · GREEN · 19:13:21.157→19:13:37.099 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.198" · tokens: none
HeroLoop · fix1a-noload · run-06 · GREEN · 19:13:37.275→19:13:53.138 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.105" · tokens: none
HeroLoop · fix1a-noload · run-07 · GREEN · 19:13:53.317→19:14:08.883 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.082" · tokens: none
HeroLoop · fix1a-noload · run-08 · GREEN · 19:14:09.053→19:14:24.993 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.183" · tokens: none
HeroLoop · fix1a-noload · run-09 · GREEN · 19:14:25.172→19:14:41.197 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="3.948" · tokens: none
HeroLoop · fix1a-noload · run-10 · GREEN · 19:14:41.374→19:14:57.622 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.256" · tokens: none
HeroLoop · fix1a-noload · run-11 · GREEN · 19:14:57.801→19:15:13.630 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.132" · tokens: none
HeroLoop · fix1a-noload · run-12 · GREEN · 19:15:13.806→19:15:29.821 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.152" · tokens: none
HeroLoop · fix1a-noload · run-13 · GREEN · 19:15:29.997→19:15:45.638 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.155" · tokens: none
HeroLoop · fix1a-noload · run-14 · GREEN · 19:15:45.817→19:16:01.683 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.077" · tokens: none
HeroLoop · fix1a-noload · run-15 · GREEN · 19:16:01.860→19:16:18.030 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.059" · tokens: none
HeroLoop · fix1a-noload · run-16 · GREEN · 19:16:18.209→19:16:34.233 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.07" · tokens: none
HeroLoop · fix1a-noload · run-17 · GREEN · 19:16:34.410→19:16:50.196 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.29" · tokens: none
HeroLoop · fix1a-noload · run-18 · GREEN · 19:16:50.369→19:17:05.844 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.167" · tokens: none
HeroLoop · fix1a-noload · run-19 · GREEN · 19:17:06.028→19:17:21.457 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.016" · tokens: none
HeroLoop · fix1a-noload · run-20 · GREEN · 19:17:21.635→19:17:37.494 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="4.203" · tokens: none
# loop end 2026-09-05T19:17:37Z
# noload sequence end 2026-09-05T19:17:37Z
# stamp sequence start 2026-09-05T19:18:48Z — FIX-1a bytes + the ReplayTransitionIT message stamps only; pinned, no load (the reproducing shape)
# loop start 2026-09-05T19:18:48Z mode=pinned tree=fix1a-stamp class=ReplayIT task=:core:event-bus:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/core/event-bus/build/test-results/test/TEST-com.homesynapse.event.bus.ReplayTransitionIT.xml
ReplayIT · fix1a-stamp · run-01 · GREEN · 19:18:48.458→19:19:09.509 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.031" · tokens: none
ReplayIT · fix1a-stamp · run-02 · GREEN · 19:19:09.687→19:19:29.046 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.024" · tokens: none
ReplayIT · fix1a-stamp · run-03 · GREEN · 19:19:29.229→19:19:48.466 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.054" · tokens: none
ReplayIT · fix1a-stamp · run-04 · GREEN · 19:19:48.638→19:20:07.505 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.056" · tokens: none
ReplayIT · fix1a-stamp · run-05 · GREEN · 19:20:07.692→19:20:27.130 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.045" · tokens: none
ReplayIT · fix1a-stamp · run-06 · GREEN · 19:20:27.312→19:20:47.013 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.093" · tokens: none
ReplayIT · fix1a-stamp · run-07 · GREEN · 19:20:47.192→19:21:06.095 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.026" · tokens: none
ReplayIT · fix1a-stamp · run-08 · GREEN · 19:21:06.267→19:21:25.356 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.035" · tokens: none
ReplayIT · fix1a-stamp · run-09 · GREEN · 19:21:25.535→19:21:44.499 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.035" · tokens: none
ReplayIT · fix1a-stamp · run-10 · GREEN · 19:21:44.672→19:22:03.837 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.03" · tokens: none
ReplayIT · fix1a-stamp · run-11 · GREEN · 19:22:04.012→19:22:23.141 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.02" · tokens: none
ReplayIT · fix1a-stamp · run-12 · GREEN · 19:22:23.311→19:22:42.446 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.054" · tokens: none
ReplayIT · fix1a-stamp · run-13 · GREEN · 19:22:42.629→19:23:01.819 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.066" · tokens: none
ReplayIT · fix1a-stamp · run-14 · GREEN · 19:23:01.990→19:23:21.213 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.035" · tokens: none
ReplayIT · fix1a-stamp · run-15 · GREEN · 19:23:21.397→19:23:40.143 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.045" · tokens: none
# loop end 2026-09-05T19:23:40Z
# fix1b sequence start 2026-09-05T19:31:38Z — T8/T9 on the FIX-1b tree (FIX-1a + FIX-1b bytes)
# loop start 2026-09-05T19:31:38Z mode=pinned tree=fix1b-noload class=ReplayIT task=:core:event-bus:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/core/event-bus/build/test-results/test/TEST-com.homesynapse.event.bus.ReplayTransitionIT.xml
ReplayIT · fix1b-noload · run-01 · GREEN · 19:31:38.223→19:31:57.287 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.041" · tokens: none
ReplayIT · fix1b-noload · run-02 · GREEN · 19:31:57.458→19:32:16.717 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.06" · tokens: none
ReplayIT · fix1b-noload · run-03 · GREEN · 19:32:16.896→19:32:36.025 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.05" · tokens: none
ReplayIT · fix1b-noload · run-04 · GREEN · 19:32:36.201→19:32:55.049 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.048" · tokens: none
ReplayIT · fix1b-noload · run-05 · GREEN · 19:32:55.229→19:33:15.105 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.03" · tokens: none
ReplayIT · fix1b-noload · run-06 · GREEN · 19:33:15.277→19:33:34.243 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.021" · tokens: none
ReplayIT · fix1b-noload · run-07 · GREEN · 19:33:34.420→19:33:53.800 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.022" · tokens: none
ReplayIT · fix1b-noload · run-08 · GREEN · 19:33:53.976→19:34:13.025 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.038" · tokens: none
ReplayIT · fix1b-noload · run-09 · GREEN · 19:34:13.209→19:34:32.910 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.024" · tokens: none
ReplayIT · fix1b-noload · run-10 · GREEN · 19:34:33.089→19:34:52.138 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.031" · tokens: none
ReplayIT · fix1b-noload · run-11 · GREEN · 19:34:52.320→19:35:11.117 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.017" · tokens: none
ReplayIT · fix1b-noload · run-12 · GREEN · 19:35:11.293→19:35:30.499 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.039" · tokens: none
ReplayIT · fix1b-noload · run-13 · GREEN · 19:35:30.681→19:35:49.788 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.03" · tokens: none
ReplayIT · fix1b-noload · run-14 · GREEN · 19:35:49.965→19:36:08.828 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.043" · tokens: none
ReplayIT · fix1b-noload · run-15 · GREEN · 19:36:09.002→19:36:28.007 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.021" · tokens: none
ReplayIT · fix1b-noload · run-16 · GREEN · 19:36:28.197→19:36:47.146 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.033" · tokens: none
ReplayIT · fix1b-noload · run-17 · GREEN · 19:36:47.322→19:37:06.514 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.041" · tokens: none
ReplayIT · fix1b-noload · run-18 · GREEN · 19:37:06.686→19:37:25.956 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.017" · tokens: none
ReplayIT · fix1b-noload · run-19 · GREEN · 19:37:26.135→19:37:44.868 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.016" · tokens: none
ReplayIT · fix1b-noload · run-20 · GREEN · 19:37:45.048→19:38:04.324 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.03" · tokens: none
# loop end 2026-09-05T19:38:04Z
# busy pids: 320168,319180
# loop start 2026-09-05T19:38:04Z mode=pinned tree=fix1b class=HeroLoop task=:lifecycle:lifecycle:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/lifecycle/lifecycle/build/test-results/test/TEST-com.homesynapse.lifecycle.HeroLoopHardwareFreeIT.xml
HeroLoop · fix1b · run-01 · GREEN · 19:38:04.949→19:38:38.617 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="8.304" · tokens: none
HeroLoop · fix1b · run-02 · GREEN · 19:38:38.796→19:39:14.610 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="10.356" · tokens: none
HeroLoop · fix1b · run-03 · GREEN · 19:39:14.798→19:40:09.429 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="29.639" · tokens: none
HeroLoop · fix1b · run-04 · GREEN · 19:40:09.614→19:40:53.350 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="17.262" · tokens: none
HeroLoop · fix1b · run-05 · GREEN · 19:40:53.538→19:41:26.634 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="8.177" · tokens: none
HeroLoop · fix1b · run-06 · GREEN · 19:41:26.813→19:42:01.246 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="8.521" · tokens: none
HeroLoop · fix1b · run-07 · GREEN · 19:42:01.429→19:42:38.444 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="10.705" · tokens: none
HeroLoop · fix1b · run-08 · GREEN · 19:42:38.626→19:43:12.511 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.896" · tokens: none
HeroLoop · fix1b · run-09 · GREEN · 19:43:12.696→19:43:48.683 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="10.317" · tokens: none
HeroLoop · fix1b · run-10 · GREEN · 19:43:48.874→19:44:22.687 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="8.273" · tokens: none
HeroLoop · fix1b · run-11 · GREEN · 19:44:22.877→19:44:56.193 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.966" · tokens: none
HeroLoop · fix1b · run-12 · GREEN · 19:44:56.376→19:45:52.172 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="29.275" · tokens: none
HeroLoop · fix1b · run-13 · GREEN · 19:45:52.351→19:46:27.025 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="8.056" · tokens: none
HeroLoop · fix1b · run-14 · GREEN · 19:46:27.208→19:47:00.432 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="8.62" · tokens: none
HeroLoop · fix1b · run-15 · GREEN · 19:47:00.620→19:47:34.900 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.739" · tokens: none
HeroLoop · fix1b · run-16 · GREEN · 19:47:35.083→19:48:07.636 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.644" · tokens: none
HeroLoop · fix1b · run-17 · GREEN · 19:48:07.825→19:48:41.289 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.746" · tokens: none
HeroLoop · fix1b · run-18 · GREEN · 19:48:41.475→19:49:46.488 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="38.206" · tokens: none
HeroLoop · fix1b · run-19 · GREEN · 19:49:46.683→19:50:20.011 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="7.317" · tokens: none
HeroLoop · fix1b · run-20 · GREEN · 19:50:20.196→19:50:54.192 · rc=0 · tests="5" skipped="0" failures="0" errors="0" time="8.487" · tokens: none
# loop end 2026-09-05T19:50:54Z
# loop start 2026-09-05T19:50:54Z mode=pinned tree=fix1b class=ReplayIT task=:core:event-bus:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/core/event-bus/build/test-results/test/TEST-com.homesynapse.event.bus.ReplayTransitionIT.xml
ReplayIT · fix1b · run-01 · GREEN · 19:50:54.516→19:51:29.499 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="11.024" · tokens: none
ReplayIT · fix1b · run-02 · GREEN · 19:51:29.699→19:52:03.082 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="9.568" · tokens: none
ReplayIT · fix1b · run-03 · GREEN · 19:52:03.262→19:52:37.857 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.637" · tokens: none
ReplayIT · fix1b · run-04 · GREEN · 19:52:38.042→19:53:12.550 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="11.303" · tokens: none
ReplayIT · fix1b · run-05 · GREEN · 19:53:12.729→19:53:44.597 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.415" · tokens: none
ReplayIT · fix1b · run-06 · GREEN · 19:53:44.785→19:54:17.356 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.762" · tokens: none
ReplayIT · fix1b · run-07 · GREEN · 19:54:17.543→19:54:52.903 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="11.608" · tokens: none
ReplayIT · fix1b · run-08 · GREEN · 19:54:53.088→19:55:25.440 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="9.026" · tokens: none
ReplayIT · fix1b · run-09 · GREEN · 19:55:25.626→19:55:58.610 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.736" · tokens: none
ReplayIT · fix1b · run-10 · GREEN · 19:55:58.800→19:56:34.060 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="11.405" · tokens: none
# loop end 2026-09-05T19:56:34Z
# busy loops stopped
# fix1b sequence end 2026-09-05T19:56:34Z
# run-0-smoke (pre-sequence, 18:18:06Z→18:18:37Z, pinned + knob, NO busy loops): ReplayIT · fix1a · RED · rc=1 · tests=1 failures=1 time=18.656 · tokens: none · RED: Checkpoint for 'replay-it-sub' did not reach 1000 within 15000 ms — XML + gradle.log at ReplayIT/fix1a/run-0-smoke/
# TOTALS: 175 loop runs + 1 smoke = 176. RED 2 (both ReplayIT, PHASE 1, pinned WITHOUT load; zero bus.delivery_anomaly / route_join_miss tokens in any run). Pre-fix: HeroLoop 0/90 (fix1a pinned+load 20 · cpu-shape 10 · ef02d13 20 · fix1a-noload 20 → 0 RED); ReplayIT with load 0/20; ReplayIT WITHOUT load 2/36 (smoke 1/1 · fix1a-noload 1/20 · fix1a-stamp 0/15). Post-fix (FIX-1b): ReplayIT no-load 20/20 · HeroLoop pinned+load 20/20 · ReplayIT pinned+load 10/10.
# Reading a line: `class · tree · run-NN · GREEN|RED · start→end UTC · rc · tests/skipped/failures/errors/time · tokens: …[ · RED: method :: message]`. Instruments (scripts + the affinity probe) under instrument/.
# hubstamp sequence start 2026-09-05T21:28:24Z — FIX-1a bytes + the hub's awaitCheckpoint stamp '(resting checkpoint N)' (v64 b1 note); the ReplayIT row re-run per the note
# busy pids: 336132,335692
# loop start 2026-09-05T21:28:24Z mode=pinned tree=fix1a-hubstamp class=ReplayIT task=:core:event-bus:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/core/event-bus/build/test-results/test/TEST-com.homesynapse.event.bus.ReplayTransitionIT.xml
ReplayIT · fix1a-hubstamp · run-01 · GREEN · 21:28:24.808→21:29:32.405 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="17.008" · tokens: none
ReplayIT · fix1a-hubstamp · run-02 · GREEN · 21:29:32.628→21:30:19.859 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="11.475" · tokens: none
ReplayIT · fix1a-hubstamp · run-03 · GREEN · 21:30:20.076→21:30:53.526 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="10.461" · tokens: none
ReplayIT · fix1a-hubstamp · run-04 · GREEN · 21:30:53.721→21:31:41.239 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="16.938" · tokens: none
ReplayIT · fix1a-hubstamp · run-05 · GREEN · 21:31:41.450→21:32:32.605 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="11.48" · tokens: none
ReplayIT · fix1a-hubstamp · run-06 · GREEN · 21:32:32.815→21:33:21.358 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="11.207" · tokens: none
ReplayIT · fix1a-hubstamp · run-07 · GREEN · 21:33:21.566→21:34:13.277 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="10.783" · tokens: none
ReplayIT · fix1a-hubstamp · run-08 · GREEN · 21:34:13.488→21:35:05.405 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="12.814" · tokens: none
ReplayIT · fix1a-hubstamp · run-09 · GREEN · 21:35:05.606→21:36:05.165 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="21.321" · tokens: none
ReplayIT · fix1a-hubstamp · run-10 · GREEN · 21:36:05.379→21:36:47.456 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="9.63" · tokens: none
ReplayIT · fix1a-hubstamp · run-11 · GREEN · 21:36:47.663→21:37:43.336 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="12.812" · tokens: none
ReplayIT · fix1a-hubstamp · run-12 · GREEN · 21:37:43.555→21:38:37.465 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="15.066" · tokens: none
ReplayIT · fix1a-hubstamp · run-13 · GREEN · 21:38:37.667→21:39:31.930 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="13.617" · tokens: none
ReplayIT · fix1a-hubstamp · run-14 · GREEN · 21:39:32.137→21:40:27.899 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="14.129" · tokens: none
ReplayIT · fix1a-hubstamp · run-15 · GREEN · 21:40:28.110→21:41:23.181 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="13.152" · tokens: none
ReplayIT · fix1a-hubstamp · run-16 · GREEN · 21:41:23.386→21:42:15.840 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="13.687" · tokens: none
ReplayIT · fix1a-hubstamp · run-17 · GREEN · 21:42:16.051→21:43:10.071 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="13.914" · tokens: none
ReplayIT · fix1a-hubstamp · run-18 · GREEN · 21:43:10.281→21:44:11.293 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="20.261" · tokens: none
ReplayIT · fix1a-hubstamp · run-19 · GREEN · 21:44:11.502→21:45:04.005 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="13.611" · tokens: none
ReplayIT · fix1a-hubstamp · run-20 · GREEN · 21:45:04.216→21:46:09.751 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="21.25" · tokens: none
# loop end 2026-09-05T21:46:09Z
# busy loops stopped
# loop start 2026-09-05T21:46:10Z mode=pinned tree=fix1a-hubstamp-noload class=ReplayIT task=:core:event-bus:test xml=C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core/core/event-bus/build/test-results/test/TEST-com.homesynapse.event.bus.ReplayTransitionIT.xml
ReplayIT · fix1a-hubstamp-noload · run-01 · GREEN · 21:46:10.566→21:46:31.157 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.072" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-02 · GREEN · 21:46:31.350→21:46:51.321 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.119" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-03 · GREEN · 21:46:51.520→21:47:11.628 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.065" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-04 · GREEN · 21:47:11.819→21:47:32.254 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.118" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-05 · GREEN · 21:47:32.441→21:47:52.491 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.072" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-06 · GREEN · 21:47:52.689→21:48:13.009 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.067" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-07 · RED · 21:48:13.209→21:48:44.069 · rc=1 · tests="1" skipped="0" failures="1" errors="0" time="18.708" · tokens: none · RED: subscriber resumes from persisted checkpoint and catches up  :: java.lang.AssertionError: Checkpoint for 'replay-it-sub' did not reach 1000 within 15000 ms (resting checkpoint 28)
ReplayIT · fix1a-hubstamp-noload · run-08 · GREEN · 21:48:44.310→21:49:04.985 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.083" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-09 · GREEN · 21:49:05.188→21:49:25.899 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.106" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-10 · GREEN · 21:49:26.111→21:49:46.360 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.081" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-11 · GREEN · 21:49:46.569→21:50:07.322 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.06" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-12 · GREEN · 21:50:07.515→21:50:27.785 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.066" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-13 · GREEN · 21:50:27.996→21:50:49.100 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.092" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-14 · GREEN · 21:50:49.291→21:51:09.820 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.085" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-15 · GREEN · 21:51:10.017→21:51:30.510 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.119" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-16 · GREEN · 21:51:30.703→21:51:50.551 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.013" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-17 · GREEN · 21:51:50.746→21:52:11.074 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.09" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-18 · GREEN · 21:52:11.277→21:52:31.222 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.047" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-19 · GREEN · 21:52:31.423→21:52:51.364 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.067" · tokens: none
ReplayIT · fix1a-hubstamp-noload · run-20 · GREEN · 21:52:51.553→21:53:11.966 · rc=0 · tests="1" skipped="0" failures="0" errors="0" time="8.067" · tokens: none
# loop end 2026-09-05T21:53:12Z
# hubstamp sequence end 2026-09-05T21:53:12Z
# TOTALS v2 (after the hub-stamp re-run, v64 b1 note): 215 loop runs + 1 smoke = 216. RED 3 — all ReplayIT, PHASE 1, pinned WITHOUT load (smoke · fix1a-noload run-20 · fix1a-hubstamp-noload run-07, the stamped one: `(resting checkpoint 28)`). ReplayIT pinned WITH load 0/40 (fix1a 20 · fix1a-hubstamp 20); WITHOUT load 3/56 (smoke 1/1 · fix1a-noload 1/20 · fix1a-stamp 0/15 · fix1a-hubstamp-noload 1/20). HeroLoop pre-fix 0/90. Post-fix (FIX-1b): ReplayIT no-load 20/20 · HeroLoop pinned+load 20/20 · ReplayIT pinned+load 10/10. Zero bus.delivery_anomaly / route_join_miss tokens in any run.
