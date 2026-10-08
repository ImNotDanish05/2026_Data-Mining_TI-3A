# DANISH_AI_AGENT.md
> This file is for AI agents, not humans. Update after finishing every task. Read this BEFORE exploring other files.

## Overview
Academic Data Mining project (TI-3A) building Python scripts to extract YouTube Data API v3 and Return YouTube Dislike (RYD) API data into primary analysis datasets.

## Stack
- Python 3.12+
- Libraries: google-api-python-client, requests, pandas, isodate, python-dotenv, pytest

## Commands
- Install: `pip install -r Youtube_Data_Collection_API/requirements.txt`
- Run: `python Youtube_Data_Collection_API/main.py --input-csv Youtube_Data_Collection_API/input_videos_template.csv`
- Preprocess: `python data_preprocessing.py`
- Test: `pytest Youtube_Data_Collection_API/test_collector.py`

## Structure map (top-level only, 1 line per folder)
- `SKILL.md` — AI context management rules
- `data/` — Raw datasets (`data/raw/`) and preprocessed outputs (`data/processed/`)
- `informasi/` — Lecture notes (`materi/`) and preprocessing analysis/roadmap (`catatan/`)
- `data_preprocessing.py` — 100% Data preprocessing pipeline script
- `Youtube_Data_Collection_API/` — YouTube Data API v3 & RYD data collection implementation

## Conventions that differ from defaults / can't be inferred
- Neutrality: scripts, logs, comments, and variable names must remain politically neutral and statistical.
- Quota efficiency: never paginate comment replies; use `totalReplyCount` from `commentThreads`.
- Output: 2 clean CSV files (`dataset_video_politik.csv`, `dataset_komentar_politik.csv`) with cleaned tabs/newlines.

## DO NOT touch
- `.env` (contains sensitive `YOUTUBE_API_KEY`)

## Known gotchas
- RYD API (`returnyoutubedislikeapi.com`) may fail or return null; fallback `dislike_count_est` to 0.
- Disabled comments or private videos must be handled gracefully without script failure.

## Changelog (newest first, 1 line per entry, NOT a diff)
- 2026-10-08: Built and executed 100% data preprocessing pipeline in data_preprocessing.py into data/processed/.
- 2026-10-08: Documented dataset defense strategy and preprocessing action plan in informasi/catatan/.
- 2026-10-08: Generated sanitized Markdown study notes for Week 01-04 in ppt/ without internal/personal metadata.
- 2026-10-07: Added channel_video attribute support across input CSV parser, collector, and output dataset.
- 2026-10-07: Initial setup of collector, CLI, input CSV template, and test suite.

