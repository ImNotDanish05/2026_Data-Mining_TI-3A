# DANISH_AI_AGENT.md
> This file is for AI agents, not humans. Update after finishing every task. Read this BEFORE exploring other files.

## Overview
Academic Data Mining project (TI-3A). Official chosen topic: Topic 1 (Unsupervised NLP Topic Modeling on MBG YouTube Comments using Latent Dirichlet Allocation / LDA).
Presentation Deadline: Thursday, 22 October 2026.

## Stack
- Python 3.12+
- Libraries: google-api-python-client, requests, pandas, isodate, python-dotenv, pytest, gensim, pyLDAvis, scikit-learn

## Commands
- Install: `pip install -r Youtube_Data_Collection_API/requirements.txt`
- Run: `python Youtube_Data_Collection_API/main.py --input-csv Youtube_Data_Collection_API/input_videos_template.csv`
- Preprocess: `python data_preprocessing.py`
- Transcribe: `python fetch_youtube_transcripts.py`
- Topic Modeling (LDA): `python train_lda_topic_modeling.py`
- Test: `pytest Youtube_Data_Collection_API/test_collector.py`

## Structure map (top-level only, 1 line per folder)
- `SKILL.md` — AI context management rules
- `data/` — Raw (`data/raw/`), preprocessed (`data/processed/`), and sanitized public releases (`data/public/`)
- `informasi/` — Lecture notes (`materi/`) and preprocessing analysis/roadmap (`catatan/`)
- `models/` — Saved LDA models, dictionary, and transformer cache (gitignored)
- `data_preprocessing.py` — 100% Data preprocessing pipeline script
- `analisis_komparasi_framing_sinta2.py` — SINTA 2 cross-modal comparative media framing analysis (Cross-tab & Chi-Square)
- `fetch_youtube_transcripts.py` — YouTube transcript extraction with auto-resume & VPN rotation
- `classify_sentiment_indobert.py` — Local Indo-RoBERTa sentiment classifier for comments
- `Youtube_Data_Collection_API/` — YouTube Data API v3 & RYD data collection implementation

## Conventions that differ from defaults / can't be inferred
- STRICT: NO SUPERVISED LABELS. Lecturer strictly forbids manual/pseudo labeling. All model training MUST be Unsupervised NLP (Topic Modeling LDA).
- Neutrality: scripts, logs, comments, and variable names must remain politically neutral and statistical.
- Quota efficiency: never paginate comment replies; use `totalReplyCount` from `commentThreads`.
- Output: Clean CSV files in data/raw/ and data/processed/ (video, komentar, transkrip) with cleaned tabs/newlines.
- Summary column in dataset_video_clean.csv must contain no commas and no double-quotes to keep naive CSV split safe.

## Next milestone (Presentation: 22 Oct 2026)
- Unsupervised NLP architecture documented in `informasi/catatan/rencana_dan_alur_training_model.md`.
- Build LDA script (`train_lda_topic_modeling.py`) with Indonesian stopwords filtering, Dictionary/Corpus, and Coherence Score tuning ($C_v$).
- Export interactive pyLDAvis HTML (`visualisasi_lda_interaktif.html`) and topic distribution plots.
- Prepare slide presentation for 22 Oct 2026.

## DO NOT touch
- `.env` (contains sensitive `YOUTUBE_API_KEY`)
- `informasi/catatan_pribadi/` (User's private notes and assignments — strictly gitignored and never pushed to GitHub)
- `data/processed/dataset_komentar_labeled.csv` (CRITICAL: DO NOT DELETE OR OVERWRITE! Contains valuable 5,207 Indo-RoBERTa sentiment labels classified earlier; preserve as backup/validation asset even though current training uses unsupervised LDA).

## Known gotchas
- RYD API (`returnyoutubedislikeapi.com`) may fail or return null; fallback `dislike_count_est` to 0.
- Disabled comments or private videos must be handled gracefully without script failure.

## Changelog (newest first, 1 line per entry, NOT a diff)
- 2026-10-15: Added informasi/catatan_pribadi/ and *.docx to .gitignore and protected in DO NOT touch to prevent accidental upload to GitHub.
- 2026-10-15: Duplicated sanitized 100% anonymized datasets into data/public/ (comments, video metadata, transcripts) and whitelisted in .gitignore for safe GitHub public release.
- 2026-10-15: Documented full Indonesian statutory legal protections (UU Dikti, UU PDP, UU ITE, KUHP, UU Hak Cipta) in informasi/catatan/landasan_hukum_dan_perlindungan_peneliti.md and README.md.
- 2026-10-15: Overhauled README.md for public repository release with strict legal, ethical, PPDM/UU PDP privacy, and political neutrality disclaimers.
- 2026-10-15: Pivoted model architecture to Unsupervised NLP (LDA Topic Modeling) without labeling per lecturer requirement; documented in informasi/catatan/rencana_dan_alur_training_model.md.
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

