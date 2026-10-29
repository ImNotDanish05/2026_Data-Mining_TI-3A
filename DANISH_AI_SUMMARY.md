# DANISH_AI_SUMMARY.md
> Written by AI agents, for AI agents. Read this, then danish_ai_summary/CURRENT_STATE.md, BEFORE exploring other files.
> Detailed notes live in danish_ai_summary/. Update them as you work, not just at the end.

## Overview
Academic Data Mining project (TI-3A) analyzing Indonesian public discourse on the "Makan Bergizi Gratis" (MBG) national policy from YouTube comments using Unsupervised NLP Topic Modeling (Latent Dirichlet Allocation / LDA). Primary target: Lab Report + Presentation (completed) and Pre-UAS SINTA 2 & SINTA 3 academic journal publications.

## Stack
- Python 3.12.3 (in `.venv/`, use `.venv/bin/python3`)
- Package manager: pip (use `.venv/bin/python3 -m pip`)
- Libraries: pandas, gensim, pyLDAvis, scikit-learn, scipy, matplotlib, seaborn, transformers, torch (CPU), google-api-python-client, youtube-transcript-api, pytest

## Commands
- Run Preprocessing: `.venv/bin/python3 data_preprocessing.py`
- Test: `.venv/bin/python3 -m pytest Youtube_Data_Collection_API/test_collector.py`
- Run Data Collection: `.venv/bin/python3 Youtube_Data_Collection_API/main.py --input-csv data/raw/input_videos.csv`
- Transcribe: `.venv/bin/python3 fetch_youtube_transcripts.py`
- Run Notebook / LDA: Jupyter Notebook `Analisis_Data_Video_Topic_Modeling_LDA.ipynb`
- Sentiment Archive: `.venv/bin/python3 classify_sentiment_indobert.py`

## Structure map (top-level, one line per folder)
- `data/` — Raw (`data/raw/`), preprocessed (`data/processed/`), and sanitized public datasets (`data/public/`)
- `informasi/` — Lecture notes (`informasi/materi/`), research documentation & literature (`informasi/catatan/`), and private files (`informasi/catatan_pribadi/`)
- `models/` — Model artifacts, Gensim LDA zip (`models/models-lda/`), Hugging Face cache (gitignored)
- `Youtube_Data_Collection_API/` — YouTube Data API v3 & RYD extraction pipeline and test suite
- `index.html` — Interactive pyLDAvis topic modeling web visualization

## Notes index (what to read when)
| Need | Read |
|---|---|
| Where did we stop? | danish_ai_summary/CURRENT_STATE.md |
| Big picture & system flow | danish_ai_summary/ARCHITECTURE.md |
| Before writing code / rules | danish_ai_summary/CONVENTIONS.md |
| Why is it like this? | danish_ai_summary/DECISIONS.md |
| Recent changes log | danish_ai_summary/CHANGELOG.md |
| Data pipeline details | danish_ai_summary/modules/data_pipeline.md |
| Topic modeling & LDA details | danish_ai_summary/modules/topic_modeling.md |
| Academic deliverables & SINTA | danish_ai_summary/modules/academic_deliverables.md |
| Older history | danish_ai_summary/archive/ (only if needed) |

## DO NOT touch
- `.env` (contains sensitive `YOUTUBE_API_KEY`)
- `informasi/catatan_pribadi/` (User's private notes, assignments, reports, PPTX — strictly gitignored and never pushed to GitHub)
- `data/processed/dataset_komentar_labeled.csv` (CRITICAL: 5,207 Indo-RoBERTa sentiment labels; preserve as backup/validation asset)
- `models/` (large binary caches, models, blobs)

<!-- last verified: 2026-10-29 -->

