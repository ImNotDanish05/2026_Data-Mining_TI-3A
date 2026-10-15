# DANISH_AI_AGENT.md
> This file is for AI agents, not humans. Update after finishing every task. Read this BEFORE exploring other files.

## Overview
Academic Data Mining project (TI-3A). Official chosen topic: Topic 1 (Sentiment & Media Framing Analysis on MBG Policy using Indo-RoBERTa & ML Benchmark).
Presentation Deadline: Thursday, 22 October 2026.

## Stack
- Python 3.12+
- Libraries: google-api-python-client, requests, pandas, isodate, python-dotenv, pytest

## Commands
- Install: `pip install -r Youtube_Data_Collection_API/requirements.txt`
- Run: `python Youtube_Data_Collection_API/main.py --input-csv Youtube_Data_Collection_API/input_videos_template.csv`
- Preprocess: `python data_preprocessing.py`
- Transcribe: `python fetch_youtube_transcripts.py`
- Classify: `python classify_sentiment_indobert.py`
- Test: `pytest Youtube_Data_Collection_API/test_collector.py`

## Structure map (top-level only, 1 line per folder)
- `SKILL.md` — AI context management rules
- `data/` — Raw datasets (`data/raw/`) and preprocessed outputs (`data/processed/`)
- `informasi/` — Lecture notes (`materi/`) and preprocessing analysis/roadmap (`catatan/`)
- `models/` — Local Hugging Face transformer model cache (gitignored)
- `data_preprocessing.py` — 100% Data preprocessing pipeline script
- `fetch_youtube_transcripts.py` — YouTube transcript extraction with auto-resume & VPN rotation
- `classify_sentiment_indobert.py` — Local Indo-RoBERTa sentiment classifier for comments
- `Youtube_Data_Collection_API/` — YouTube Data API v3 & RYD data collection implementation

## Conventions that differ from defaults / can't be inferred
- Neutrality: scripts, logs, comments, and variable names must remain politically neutral and statistical.
- Quota efficiency: never paginate comment replies; use `totalReplyCount` from `commentThreads`.
- Output: Clean CSV files in data/raw/ and data/processed/ (video, komentar, transkrip) with cleaned tabs/newlines.
- Summary column in dataset_video_clean.csv must contain no commas and no double-quotes to keep naive CSV split safe.

## DO NOT touch
- `.env` (contains sensitive `YOUTUBE_API_KEY`)

## Known gotchas
- RYD API (`returnyoutubedislikeapi.com`) may fail or return null; fallback `dislike_count_est` to 0.
- Disabled comments or private videos must be handled gracefully without script failure.

## Changelog (newest first, 1 line per entry, NOT a diff)
- 2026-10-15: Selected Topic 1 as official topic approved by lecturer; scheduled presentation for 22 October 2026.
- 2026-10-15: Compiled empirical evidence and academic defense guide for 100% preprocessing completion in informasi/catatan/bukti_dan_argumen_preprocessing_100_persen.md.
- 2026-10-08: Documented 5 research topic proposals and methodologies in informasi/catatan/usulan_5_topik_penelitian.md.
- 2026-10-08: Classified 5,207 comments using local Indo-RoBERTa model into data/processed/dataset_komentar_labeled.csv (88.7% confidence).
- 2026-10-08: Completed summary for all 55 videos in data/processed/dataset_video_clean.csv with neutral comma-free summaries.
- 2026-10-08: Filled summary for 29 videos in data/processed/dataset_video_clean.csv with neutral comma-free summaries.
- 2026-10-08: Filled summary for first 9 videos in data/processed/dataset_video_clean.csv with neutral comma-free summaries.
- 2026-10-08: Added summary column to data/processed/dataset_video_clean.csv with first video summary for m-VTr83vz98.
- 2026-10-08: Exported transcript dataset to data/raw/dataset_transkrip_video.csv (55 rows, 134k words).
- 2026-10-08: Extracted 100% video transcripts (55/55 videos, 134,986 words) into data/processed/video_transcripts.json.
- 2026-10-08: Curated and verified 20 academic journals supporting dataset and preprocessing in informasi/catatan/.
- 2026-10-08: Built and executed 100% data preprocessing pipeline in data_preprocessing.py into data/processed/.
- 2026-10-08: Documented dataset defense strategy and preprocessing action plan in informasi/catatan/.
- 2026-10-08: Generated sanitized Markdown study notes for Week 01-04 in ppt/ without internal/personal metadata.
- 2026-10-07: Added channel_video attribute support across input CSV parser, collector, and output dataset.
- 2026-10-07: Initial setup of collector, CLI, input CSV template, and test suite.

