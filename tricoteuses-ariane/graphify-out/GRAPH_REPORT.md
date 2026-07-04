# Graph Report - .  (2026-07-03)

## Corpus Check
- Corpus is ~46,141 words - fits in a single context window. You may not need a graph.

## Summary
- 612 nodes · 796 edges · 56 communities (37 shown, 19 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 38 edges (avg confidence: 0.78)
- Token cost: 240,020 input · 33,547 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]

## God Nodes (most connected - your core abstractions)
1. `MasterClock` - 28 edges
2. `Record` - 23 edges
3. `FakeTime` - 15 edges
4. `FakeTime` - 12 edges
5. `utter()` - 11 edges
6. `snapshot()` - 9 edges
7. `main()` - 9 edges
8. `main()` - 9 edges
9. `acts()` - 8 edges
10. `LiveStreamer` - 8 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `log()`  [INFERRED]
  b3-capture/watch_derouleur_nvs.py → spikes/2026-06-23-ttv-streaming-identification/artifacts/whisper/live_whisper.py
- `test_load_dotenv_reads_repo_style_file_without_overriding_existing_env()` --calls--> `load_dotenv()`  [INFERRED]
  test_ariane_env.py → ariane_env.py
- `main()` --calls--> `Record`  [INFERRED]
  b2-replay/detect_start.py → b2-replay/replay.py
- `main()` --calls--> `MasterClock`  [INFERRED]
  b2-replay/server.py → b2-replay/replay.py
- `main()` --calls--> `Record`  [INFERRED]
  b2-replay/server.py → b2-replay/replay.py

## Communities (56 total, 19 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (34): A B3 capture bundle on disk: the index, the clock origin, and byte access to, Where the sitting's speech starts (ms), read from sitting_start.json —, The raw bytes of `source` current at demo time `t_ms`, or None if the         s, The captured Eliasse summary current at `t_ms` (a dict), or None. The raw, The frozen referential slice `name` (e.g. 'acteurs'), verbatim, out of the, The post-production ground-truth NVS `name` (e.g. 'data.nvs'), verbatim,, The bytes of the most recent raw snapshot of `source`, or None. Used as, The (data.nvs, liveplayer.nvs) bytes to build the NVS view from: the         fr (+26 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (20): Tests for B1 the SSE broadcast layer (spec 2026-07-01, scope §4).  Pure layer,, test_multiple_subscribers_each_get_live_node(), test_new_subscriber_gets_backlog_then_live(), Broadcaster, B1 ariane-weaver — the weaving core.  Turns raw Whisper streaming events into, One Server-Sent-Events frame: a `data:` line + the blank-line terminator., One strictly-increasing `seq` shared by every weaver of the thread (STT +     t, Fans each woven node out to SSE subscribers. Thread-safe: the Whisper thread (+12 more)

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (23): MasterClock, The single authority that owns `t` (ms since video start), spec §B2.      Adva, FakeTime, Tests for B2's master clock — the single authority that owns `t` (spec §B2)., A controllable wall clock: starts at 1000.0 s, advances on demand., test_advances_at_real_time_while_playing(), test_frozen_while_paused(), test_resume_continues_from_where_it_paused() (+15 more)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (27): canon_derouleur(), fetch(), fetch_eliasse(), main(), notify(), _nvs_speakers(), _phases(), At sitting end: schedule the resolver for +delay_min. Log the manual fallback (+19 more)

### Community 4 - "Community 4"
Cohesion: 0.09
Nodes (22): Tests for B1 speech-deduced trame (spec 2026-07-02-b1-speech-deduced-trame)., The resolved actor's groupe_uid becomes canonical.groupe, labelled from     org, No organes referential, or an actor without groupe_uid: no invented group., A name in a chair's call opens a turn (call=True); a name quoted inside     a s, Real false positive: LocalAgreement split «…Sur la réponse pour / Mme     Isabe, A mention emits a linkable node (call=False, heard kept for inline     wrapping, Sittings follow one another on the same live flow (and B4 can switch     B2's r, The derouleur purges discussed lines mid-sitting (verified 26/06):     an entry (+14 more)

### Community 5 - "Community 5"
Cohesion: 0.1
Nodes (19): AgendaIndex, _aslist(), Deducer, extract_amendment_numbers(), extract_ballot(), extract_speaker_names(), from_derouleur(), is_speaker_call() (+11 more)

### Community 6 - "Community 6"
Cohesion: 0.14
Nodes (16): audio_frames(), _default_compute_type(), DiarWorker, _fetch_json(), main(), _make_handler(), poll_referentials(), B1 ariane-weaver — the live wiring (STT + I/O side, kept out of the pure core). (+8 more)

### Community 7 - "Community 7"
Cohesion: 0.13
Nodes (15): causal_snapshot(), current_raw_ref(), load_index(), nvs_timeline(), nvs_tree(), origin_from_video(), Parse a B3 `index.ndjson` into a list of tick dicts (blank lines skipped)., The ground-truth NVS chapters placed on the video timeline, sorted by t. (+7 more)

### Community 8 - "Community 8"
Cohesion: 0.21
Nodes (16): adt(), Tests for B1 trame weaving (spec 2026-07-02-b1-trame-weaving-design).  The tra, Same line id, label enriched in place («(scrutin public)» appended)., XML→JSON convention: `phase` and `ligne` are bare objects when single., Acceptance: replaying the 114 real snapshots of 26/06 weaves the trame,     inc, A minimal derouleur snapshot with one phase carrying the given lines., snapshot(), test_bare_object_shapes_are_parsed() (+8 more)

### Community 9 - "Community 9"
Cohesion: 0.15
Nodes (9): list_records(), LiveStreamer, B2 live streamer — re-broadcast the record's mp4 as a LIVE sliding-window HLS., A record name usable as a path component (no traversal), else None., Point at another sitting's mp4 (record switch); stops the stream., (Re)start the live edge at `t_ms` into the video., Bytes of a servable stream file (whitelisted), or None., The replayable capture bundles under `records_dir`, for B4's picker.      Repl (+1 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (11): Tests for the canonical ID resolver (spec 2026-07-01-canonical-id-resolution)., Civility stripped, exact name -> the uid., elisa martin' (lowercased, no accent) picks the right Martin via first name., A light STT error on the surname still resolves (fuzzy)., Martin' alone matches two actors -> refuse rather than guess., Real 26/06 case: STT «Bruet» scores Gruet 0.800 and Barbut 0.727 — both     ove, test_accent_and_case_insensitive_and_disambiguated_by_first_name(), test_ambiguous_surname_returns_none() (+3 more)

### Community 11 - "Community 11"
Cohesion: 0.16
Nodes (15): apply_transport(), clock_payload(), clock_state(), main(), _make_handler(), A request handler over the mutable server state:     {"record": Record, "clock", Rebuild the real prochainADiscuter.do shape from the captured summary.     Fait, Rebuild the real amendement.do shape from the captured summary. Only the     fi (+7 more)

### Community 12 - "Community 12"
Cohesion: 0.19
Nodes (14): acts(), Tests for the speaker-boundary detector (diarization core, pure part).  pyanno, Build a (frames, 3) activity matrix from (speaker, seconds) spans,     10 frame, ministre (spk1) 8s then présidente (spk2) 2s → boundary at ~8s., Same speaker around a silence: no switch., présidente 3s, silence 1s, Hetzel 6s (real +8s window pattern)., The same handover seen by consecutive sliding windows emits ONCE., A sub-second blip is not a speaker turn. (+6 more)

### Community 13 - "Community 13"
Cohesion: 0.24
Nodes (14): api_documents_by_bibard(), api_get(), extract_derouleur_keys(), extract_keys(), extract_nvs_keys(), main(), notify(), GET <resource> for a set of uids, batched. Returns the rows whose uid is     in (+6 more)

### Community 14 - "Community 14"
Cohesion: 0.2
Nodes (12): derouleur_cursor(), fetch(), main(), now_ms(), parse_derouleur(), parse_nvs(), GET with browser UA + referer + a cache-busting `modulo` param., Return (extract_date_time, highlighted) where highlighted is a list of     (lab (+4 more)

### Community 15 - "Community 15"
Cohesion: 0.24
Nodes (7): build_thread(), Handler, load_json(), main(), Tout le fil en une réponse JSON qui SE TERMINE (réseau au repos -> capture)., summarize(), BaseHTTPRequestHandler

### Community 16 - "Community 16"
Cohesion: 0.23
Nodes (11): Deducer, _name_tokens(), _norm(), _ratio(), Canonical ID resolver (spec 2026-07-01-canonical-id-resolution, issue #9).  De, Lowercase, strip accents (NFKD), keep letters/spaces/hyphens, collapse spaces., Normalized tokens with civility/title words removed., Resolve a detected name to {uid, score, nom} or None.      - single token -> m (+3 more)

### Community 17 - "Community 17"
Cohesion: 0.17
Nodes (11): Tests for B1 ariane-weaver — the weaving core (spec 2026-07-01-b1-weaver-design), t = beg*1000 (ms since the flow's t=0). An utterance is consolidated., D5: an interim (unconfirmed) is a provisional node., Each emitted node gets the next seq, append-only., D5: the confirmed utterance replaces the last provisional (supersedes)., Each interim REWRITES the previous one and must supersede it — otherwise     in, test_interim_is_provisional(), test_seq_is_monotonic() (+3 more)

### Community 18 - "Community 18"
Cohesion: 0.23
Nodes (9): _aslist(), _canonical(), highlighted_lines(), EVAL-ONLY — the régie's highlight as a measuring stick, NEVER a thread source., derouleur.json comes from XML: a single child is a bare object, not a list., The régie's current point: every highlighted line, in document order., Consume one dérouleur snapshot, return the nodes its transitions produce., _text() (+1 more)

### Community 19 - "Community 19"
Cohesion: 0.33
Nodes (9): get_json(), main(), ManagedProcess, read_sitting_start_ms(), request(), tail(), validate_record(), wait_http() (+1 more)

### Community 20 - "Community 20"
Cohesion: 0.29
Nodes (10): derouleur_state(), discover_direct_id(), fetch(), is_open(), main(), notify(), Live (via the dérouleur) = the inter-session slate is gone AND a real     legis, Best-effort live direct-id: candidates from direct.php, confirmed by a     data (+2 more)

### Community 21 - "Community 21"
Cohesion: 0.24
Nodes (7): BoundaryDetector, _dominant_per_frame(), Speaker-boundary detection over sliding segmentation windows (pure core).  pya, Per-frame dominant speaker index, -1 for silence. acts: (frames, K)., Contiguous (speaker, start_s, end_s) runs, silence (-1) dropped., One segmentation window in, at most one boundary (flow seconds) out., _segments()

### Community 22 - "Community 22"
Cohesion: 0.31
Nodes (9): _base_from_nvs(), _direct_id(), _fetch(), main(), manifest_url(), The sitting's direct-id, read from a supervisor log or MANIFEST., The Vodalys media base name from the sitting's data.nvs.      Tries, in order:, The HLS variant URL for `quality` (a resolution the master lists). (+1 more)

### Community 23 - "Community 23"
Cohesion: 0.31
Nodes (8): load_actors(), load_truth(), _noisy(), Measure the canonical ID resolver on real data (spec 2026-07-01, §Test/eval)., (name, 'PA'+tribun) pairs from the most recent data.nvs, deduped., Drop the last vowel of the last word (crude phonetic-error proxy)., run(), _strip_civ()

### Community 24 - "Community 24"
Cohesion: 0.39
Nodes (7): amdt_num(), fetch(), main(), now(), stamp(), state_derouleur(), state_eliasse()

### Community 25 - "Community 25"
Cohesion: 0.32
Nodes (6): _decode_value(), load_dotenv(), Small .env loader for Ariane command-line scripts.  The bricks intentionally avo, Load repository .env into os.environ.      Returns the variables inserted or ove, _strip_inline_comment(), test_load_dotenv_reads_repo_style_file_without_overriding_existing_env()

### Community 26 - "Community 26"
Cohesion: 0.39
Nodes (7): Tests for B2 ariane-replay — the causal replayer.  First contract, the one the, A minimal index.ndjson record: only `wall` matters for the causal gate., test_exact_boundary_is_inclusive(), test_gate_serves_only_snapshots_at_or_before_t(), test_naive_wall_is_read_as_paris_not_the_host_tz(), test_no_future_snapshot_ever_leaks(), _tick()

### Community 27 - "Community 27"
Cohesion: 0.32
Nodes (3): Handler, Fetch liveplayer.nvs for `did`, return {start_epoch} — server-side, no CORS., SimpleHTTPRequestHandler

### Community 28 - "Community 28"
Cohesion: 0.29
Nodes (5): Tests for B1 the append-only thread log (spec 2026-07-01, scope §3).  The log, French text must be written as-is, not \\uXXXX (ensure_ascii=False)., A late SSE subscriber replays the backlog via history()., test_append_is_utf8_not_escaped(), test_history_returns_all_appended_nodes()

### Community 30 - "Community 30"
Cohesion: 0.33
Nodes (7): Ariane Project, B1 â€” weaver (STT), B2 â€” replay (causal), B3 â€” capture (live record), B4 â€” UI (timeline), Causality principle (never leak future), Thread NDJSON format

### Community 31 - "Community 31"
Cohesion: 0.47
Nodes (5): detect(), first_sustained_speech(), main(), First speech start (seconds) from which speech density over the next     `windo, Speech-start (ms) of the video's first `scan_minutes`, by silero VAD.

### Community 33 - "Community 33"
Cohesion: 0.53
Nodes (5): Tests for resolving the current raw snapshot of a source at demo time `t`.  Fo, test_carries_last_ref_across_unchanged_ticks(), test_none_before_any_snapshot(), test_returns_ref_of_latest_tick_at_or_before_t(), _tick()

### Community 35 - "Community 35"
Cohesion: 0.33
Nodes (6): LEGI Dataset (DILA), Tricoteuses API Legifrance, Tricoteuses API Parlement, Tricoteuses React Components, Tricoteuses Juridique Monorepo, Tricoteuses Project Ecosystem

### Community 37 - "Community 37"
Cohesion: 0.5
Nodes (4): fixture(), FIXTURE_DIR, main(), OUT_DIR

### Community 38 - "Community 38"
Cohesion: 0.4
Nodes (4): out, provider, t0, wav

### Community 39 - "Community 39"
Cohesion: 0.4
Nodes (4): MasterClock, Record, causal_snapshot(), Causality guarantee (B2)

### Community 40 - "Community 40"
Cohesion: 0.67
Nodes (3): duration_s(), main(), Spike (2026-07-01): offline Whisper on a downloaded VOD mp4 -> real STT output.

## Knowledge Gaps
- **182 isolated node(s):** `Small .env loader for Ariane command-line scripts.  The bricks intentionally avo`, `Load repository .env into os.environ.      Returns the variables inserted or ove`, `Put this directory on sys.path so tests import `weaver` directly (the brick is`, `B1 ariane-weaver — speech-deduced trame (spec 2026-07-02-b1-speech-deduced-trame`, `derouleur.json comes from XML: a single child is a bare object, not a list.` (+177 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.