# Data Pipeline Module

- Purpose: Handles data collection from YouTube, audio transcripts harvesting, data cleaning, and dataset transformation.
- Key files:
  - `Youtube_Data_Collection_API/collector.py` — Core YouTube Data API v3 and RYD API scraper.
  - `Youtube_Data_Collection_API/main.py` — CLI entry point accepting `--input-csv` and writing raw CSVs.
  - `Youtube_Data_Collection_API/test_collector.py` — Unit tests using pytest and mocked responses.
  - `fetch_youtube_transcripts.py` — Transcript extractor with auto-resume and Proton VPN rotation.
  - `data_preprocessing.py` — 4-pillar data preprocessing script (cleaning, reduction, transformation, understanding).
- How it works:
  1. Input video list defined in `data/raw/input_videos.csv`.
  2. Collector fetches video snippets, statistics, and top comment threads (excluding replies to save quota).
  3. `fetch_youtube_transcripts.py` iterates over video IDs, handles IP blocks via Proton VPN rotation, and saves raw transcripts to `data/raw/dataset_transkrip_video.csv` and `data/processed/video_transcripts.json`.
  4. `data_preprocessing.py` drops null/empty comments, cleans text with regex, removes `author` column completely for privacy, computes Min-Max and Z-Score on video metrics, detects IQR outliers, and verifies foreign key integrity.
- Interfaces:
  - Outputs `data/processed/dataset_komentar_clean.csv` (5,207 rows) and `data/processed/dataset_video_clean.csv` (55 rows).
  - Prepares sanitized copies in `data/public/` for open-source distribution.
- Gotchas:
  - YouTube API quota is limited (10,000 units/day); avoid re-fetching existing data.
  - Always run scripts with `.venv/bin/python3`.
- Tests:
  - `.venv/bin/python3 -m pytest Youtube_Data_Collection_API/test_collector.py`
- Last touched: 2026-10-29

