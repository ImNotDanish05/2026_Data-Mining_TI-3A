# Changelog

### 2026-10-29 — Migrated context to Danish AI Summary structure
- What: Migrated legacy single-file `DANISH_AI_AGENT.md` to structured `danish-ai-summary/` directory (`CURRENT_STATE.md`, `ARCHITECTURE.md`, `CONVENTIONS.md`, `DECISIONS.md`, `CHANGELOG.md`, and modules).
- Why: Provide clean separation of concerns, improve prompt caching efficiency, and maintain persistent state for future agent sessions.
- Files: `DANISH_AI_SUMMARY.md`, `danish_ai_summary/*`
- Verified: Checked virtual environment execution (`.venv/bin/python3 data_preprocessing.py` ran with 100% success; pytest ran 12 tests).
- Follow-ups: User verification of migration and transition to Target 2 (Pre-UAS journal articles).

### 2026-10-22 — Finalized Lab Report & Presentation Slide Deck (Target 1)
- What: Completed national standard Lab Report (`LAPORAN_PRAKTIKUM_DATA_MINING_TI3A.docx`) answering Bab I-V and updated presentation deck (`Analisis Opini Publik MBG - Data Mining TI-3A.pptx`) with Polines logo, 4 charts, and speaker notes.
- Why: Full delivery for Target 1 deadline (22 Oct 2026).
- Files: `informasi/catatan_pribadi/LAPORAN_PRAKTIKUM_DATA_MINING_TI3A.docx`, `informasi/catatan_pribadi/Analisis Opini Publik MBG - Data Mining TI-3A.pptx`
- Verified: Files created and backed up in `informasi/catatan_pribadi/`.
- Follow-ups: Lecture presentation and transition to Target 2 journal preparation.

### 2026-10-17 — Configured authorship & generated publication-ready Markdown articles
- What: Configured official authorship (ImNotDanish05 as primary/corresponding author) and generated draft Markdown journal articles featuring full IMRAD structures, KaTeX equations, formal three-line tables, and verified IEEE references.
- Why: Target 2 preparation for SINTA 2 & SINTA 3 submissions.
- Files: `informasi/catatan/standar_dan_syarat_jurnal_sinta2_sinta3.md`
- Verified: Documented ARJUNA SINTA 2 & 3 criteria and typography blueprint.
- Follow-ups: Convert Markdown articles to target journal templates.

### 2026-10-16 — Expanded supporting literature to 42 journals & polished UI
- What: Expanded verified journal repository to 42 entries with SINTA 2 elevation criteria, modernized `index.html` pyLDAvis UI with centered responsive container and topic guides.
- Why: Support rigorous academic defense and improve visualization readability.
- Files: `informasi/catatan/daftar_40_jurnal_pendukung.md`, `index.html`
- Verified: Links and DOIs verified; `index.html` tested in browser.
- Follow-ups: Incorporate top citations into SINTA 2 manuscript.

### 2026-10-15 — Executed LDA Topic Modeling & Cross-Modal Framing Analysis
- What: Ran `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` in Colab end-to-end; found optimal $K=2$ ($C_v=0.3911$), exported pyLDAvis, and performed Chi-Square test ($\chi^2=212.4579, df=2, p < 0.0001$). Anonymized datasets duplicated to `data/public/`.
- Why: Complete core unsupervised modeling and fulfill lecturer requirement without manual labels.
- Files: `Analisis_Data_Video_Topic_Modeling_LDA.ipynb`, `data/public/*`, `models/models-lda/hasil_lda_lengkap.zip`
- Verified: Coherence curve calculated, zip bundle exported, 0 errors in Colab.
- Follow-ups: Assemble Lab Report and presentation deck.

### 2026-10-08 — 100% Data Preprocessing Pipeline & Transcripts Collection
- What: Built standalone preprocessing script `data_preprocessing.py` (5,207 clean comments, 55 clean videos, 0 orphan keys), extracted 100% video transcripts (55 videos, 134,986 words) via `fetch_youtube_transcripts.py`.
- Why: Satisfy Han et al. 4-pillar data preprocessing requirements for academic dataset defense.
- Files: `data_preprocessing.py`, `fetch_youtube_transcripts.py`, `data/processed/video_transcripts.json`, `data/processed/laporan_preprocessing.json`
- Verified: Ran `data_preprocessing.py` and inspected `laporan_preprocessing.json`.
- Follow-ups: Transition from sentiment classification to unsupervised LDA.

### 2026-10-07 — Initial Data Collection Pipeline & Test Suite
- What: Initialized YouTube Data API v3 collector module, CLI parser, input CSV reader, and pytest test suite.
- Why: Automate acquisition of YouTube videos and comment threads.
- Files: `Youtube_Data_Collection_API/collector.py`, `Youtube_Data_Collection_API/main.py`, `Youtube_Data_Collection_API/test_collector.py`
- Verified: Ran `pytest Youtube_Data_Collection_API/test_collector.py`.
- Follow-ups: Execute full harvest of 55 videos and 5,000+ comments.

