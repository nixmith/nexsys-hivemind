/*
 * HomeSynapse Core — OQ-15-2 microbench corpus dumper (SPIKE — DO NOT COMMIT)
 *
 * Serializes representative presence_personal payloads through the REAL
 * EventPayloadCodec (the AMD-52 typed payload — "the plaintext input to
 * encryption", Doc 15 §3.2/§7) and writes the exact bytes persistence would
 * store to build/corpus-oq15-2/, plus a manifest of sizes.
 *
 * Per microbench spec §4: the two genuine TestEventSamples presence events are
 * the REAL observed distribution; the band points (~200/350/500/1024 B) are
 * the SAME real event type with a padded detail string, encoded by the same
 * real codec — included to cover the Doc 15 §10 200–500 B band and the
 * per-byte slope. identity has NO event type in source at HEAD 7c73c91
 * (EventTypes carries no identity row) — recorded in §8, not faked here.
 *
 * USAGE (Nick, desktop — throwaway, working-tree only, never commit):
 *   1. Save as core/persistence/src/test/java/com/homesynapse/persistence/CorpusDumpOQ152Test.java
 *   2. ./gradlew :core:persistence:test --tests "*CorpusDumpOQ152*"
 *   3. Corpus lands in core/persistence/build/corpus-oq15-2/  → scp to the Pi
 *   4. Delete this file (git status must stay clean of it).
 */
package com.homesynapse.persistence;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.homesynapse.event.PresenceChangedEvent;
import com.homesynapse.event.PresenceSignalEvent;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.LinkedHashMap;
import java.util.Map;
import org.junit.jupiter.api.Test;

class CorpusDumpOQ152Test {

    @Test
    void dumpCorpus() throws IOException {
        ObjectMapper mapper = PersistenceObjectMapper.create();
        EventTypeRegistry registry = new EventTypeRegistry(AllEventClasses.ALL_EVENTS);
        JacksonWarmup warmup = JacksonWarmup.warmup(mapper, registry);
        EventPayloadCodec codec = new EventPayloadCodec(registry, warmup);

        Path dir = Path.of("build", "corpus-oq15-2");
        Files.createDirectories(dir);

        Map<String, byte[]> corpus = new LinkedHashMap<>();

        // ── The REAL observed sensitive-PII payloads (genuine samples) ──
        corpus.put("presence_signal_real", codec.encode(TestEventSamples.presenceSignal()));
        corpus.put("presence_changed_real", codec.encode(TestEventSamples.presenceChanged()));

        // ── Band points: real type, real codec, padded detail string ──
        corpus.put("presence_band_200", encodePadded(codec, 200));
        corpus.put("presence_band_350", encodePadded(codec, 350));
        corpus.put("presence_band_500", encodePadded(codec, 500));
        corpus.put("presence_outlier_1024", encodePadded(codec, 1024));

        StringBuilder manifest = new StringBuilder("OQ-15-2 corpus manifest (encoded via EventPayloadCodec)\n");
        for (Map.Entry<String, byte[]> e : corpus.entrySet()) {
            String file = e.getKey() + "-" + e.getValue().length + "B.bin";
            Files.write(dir.resolve(file), e.getValue());
            manifest.append(String.format("%-28s %5d B%n", e.getKey(), e.getValue().length));
        }
        Files.writeString(dir.resolve("manifest.txt"), manifest.toString());
        System.out.println(manifest);
        System.out.println("Corpus written to " + dir.toAbsolutePath());
    }

    /** Binary-searches the pad length so the ENCODED size hits the target ±2 B. */
    private static byte[] encodePadded(EventPayloadCodec codec, int targetBytes) throws IOException {
        int lo = 0;
        int hi = targetBytes + 64;
        byte[] best = null;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            byte[] encoded = codec.encode(
                    new PresenceSignalEvent("motion", "hallway_sensor", "detected_" + "x".repeat(mid)));
            if (Math.abs(encoded.length - targetBytes) <= 2) {
                return encoded;
            }
            best = encoded;
            if (encoded.length < targetBytes) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return best; // closest achievable; manifest records the actual size
    }
}
