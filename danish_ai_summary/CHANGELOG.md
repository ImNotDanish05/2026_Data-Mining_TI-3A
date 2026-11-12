# Changelog

### 2026-11-12 — Added HAC & GMM SINTA 2 Literature & Expanded Benchmark to 6 Algorithms
- What: Added 2 new verified peer-reviewed journal entries (Entries 46 and 47) to `informasi/catatan/daftar_40_jurnal_pendukung.md`:
  1. Entry 46: Hierarchical Agglomerative Clustering (HAC) on Twitter text mining (Sinkron, SINTA 2, DOI: 10.33395/sinkron.v8i3.12616).
  2. Entry 47: Gaussian Mixture Models (GMM) clustering (Jurnal RESTI, SINTA 2, DOI: 10.29207/resti.v6i5.4459).
  Both links verified 200 OK (no 404/403).
- Why: User expanded unsupervised benchmark to 6 algorithms as required by lecturer, necessitating formal literature citations and active DOIs.
- Files: `informasi/catatan/daftar_40_jurnal_pendukung.md`
- Verified: Inspected DOI registries and official OJS portals via web search; confirmed 200 OK status.


### 2026-11-12 — Updated Presentation Deck with Cluster Balance & 4-Algorithm Benchmark
- What: Updated presentation slide deck `informasi/materi/ImNotDanish05 - Analisis Opini Publik MBG - Data Mining TI-3A.pptx` (from 17 to 19 slides):
  1. Slide 11: Added Cluster Balance Check card confirming Disparity Gap = 28.56% (64.28% vs 35.72%), satisfying <= 40% threshold and proving absence of mode collapse.
  2. Slide 14 (New): Inserted 4-Algorithm Unsupervised Topic Modeling Benchmark (LDA, NMF, LSA, K-Means) with Coherence ($C_v$), Training Runtime, Cluster distributions, and Figure 4 donut chart.
  3. Slide 15 (New): Inserted Literature Basis featuring 1 primary algorithm (LDA - Blei 2003 & Wiranto 2022 Jurnal RESTI SINTA 2) + 3 benchmark baseline journals (NMF Nature 1999 & IEEE ICDM 2014, LSA JASIS 1990, K-Means Jurnal RESTI SINTA 2 2019 & NZCSRSC 2008) with verified DOIs and links.
- Why: User requested deck update incorporating cluster balance notification and 4-algorithm benchmark with journal citations and links for course defense.
- Files: `informasi/materi/ImNotDanish05 - Analisis Opini Publik MBG - Data Mining TI-3A.pptx`, `informasi/materi/ImNotDanish05 - Analisis Opini Publik MBG - Data Mining TI-3A.pptx.backup_20261112`
- Verified: Created full backup; inspected slide count (19 slides); verified typography, shapes, and layouts via `python-pptx`.


### 2026-11-05 — Released Analisis_Data_Video_Topic_Modeling_LDA_v1.0.ipynb (Data Balance & 4-Algorithm Benchmark)
- What: Created and fully executed `Analisis_Data_Video_Topic_Modeling_LDA_v1.0.ipynb` (27 cells total, 1.87 MB). Embedded:
  1. Detailed cluster balance evaluation (Cell 20) with Donut & Bar charts proving a **28.60% disparity gap** (Topik 0: 64.30% vs Topik 1: 35.70%), strictly satisfying lecturer's $\le 40\%$ requirement.
  2. Multi-model comparative benchmarking (Cell 24) evaluating 4 Unsupervised NLP models (LDA, NMF, LSA, K-Means Text Clustering) on Topic Coherence ($C_v$), training time, and cluster balance. Proved LDA is Rank 1 ($C_v = 0.4404$) and the ONLY model that prevents severe class imbalance ($\le 40\%$).
  3. Comparative visualization charts (Cell 25) with dual-axis Coherence vs Runtime and multi-panel cluster balance bar charts.
  4. Patched `pyLDAvis` `NumPyEncoder` to prevent `complex128` serialization bug on modern NumPy.
- Why: Fulfill user's request for Option A duplicate (`_v1.0`), explicitly demonstrating data balance and visual multi-model comparison for lecture evaluation and journal publication.
- Files: `Analisis_Data_Video_Topic_Modeling_LDA_v1.0.ipynb`, `website/prediksi/index.html`, `website/prediksi/model_data.js`
- Verified: Executed all 27 cells with exit code 0; verified embedded images and stdout outputs.


### 2026-10-30 — Implemented 4-Algorithm Unsupervised NLP Benchmark & SINTA 2 Visuals
- What: Built and executed `Komparasi_4_Algoritma_NLP_Topic_Modeling_SINTA2.ipynb` comparing LDA, NMF, LSA, and K-Means Text Clustering; evaluated Topic Coherence ($C_v$) and runtime; computed Pearson Chi-Square test ($\chi^2 = 132.9966, p < 0.0001$); generated 6 standalone publication-ready figures (300 DPI) in `gambar_sinta2/`; and exported annotated dataset `data/processed/dataset_komentar_hasil_komparasi_4_algoritma.csv`.
- Why: Fulfill lecturer's multi-algorithm comparative study requirement and equip user with complete empirical evidence for SINTA 2 journal publication.
- Files: `Komparasi_4_Algoritma_NLP_Topic_Modeling_SINTA2.ipynb`, `gambar_sinta2/*.png`, `data/processed/dataset_komentar_hasil_komparasi_4_algoritma.csv`
- Verified: Notebook executed end-to-end with 0 errors; 6 figures verified in `gambar_sinta2/`; benchmark table verified.
- Follow-ups: Draft SINTA 2 manuscript incorporating the generated figures and statistical tables.

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

