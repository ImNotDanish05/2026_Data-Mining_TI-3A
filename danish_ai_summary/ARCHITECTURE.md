# Architecture & System Design

## System Overview

This project implements an end-to-end academic Data Mining and Unsupervised NLP Topic Modeling pipeline on Indonesian public discourse surrounding the "Makan Bergizi Gratis" (MBG) national policy.

```
[ External APIs ]
  - YouTube Data API v3 (Google LLC)
  - Return YouTube Dislike API (RYD)
           │
           ▼
[ Data Acquisition ] ──────────────────────────────────────────┐
  - Youtube_Data_Collection_API/collector.py                   │
  - fetch_youtube_transcripts.py (Proton VPN rotation)         │
           │                                                   │
           ▼                                                   ▼
[ Raw Storage (data/raw/) ]                             [ Public Data (data/public/) ]
  - dataset_video_politik.csv                             - dataset_video_publik.csv
  - dataset_komentar_politik.csv                          - dataset_komentar_publik.csv
  - dataset_transkrip_video.csv                           - dataset_transkrip_publik.csv
           │                                              (100% Anonymized & Sanitized)
           ▼
[ Preprocessing Pipeline (data_preprocessing.py) ]
  1. Data Cleaning (regex, emoji, links, timestamp removal)
  2. Data Reduction & Privacy (drop 'author' column completely)
  3. Data Transformation (Min-Max [0, 1] & Z-Score scaling)
  4. Data Understanding (Boxplot 1.5x IQR outlier detection)
           │
           ▼
[ Processed Storage (data/processed/) ]
  - dataset_video_clean.csv (55 videos, normalized)
  - dataset_komentar_clean.csv (5,207 clean comments)
  - video_transcripts.json (134,986 words)
  - laporan_preprocessing.json
           │
           ▼
[ Model Training & Analysis ]
  - Analisis_Data_Video_Topic_Modeling_LDA.ipynb (Colab & Local)
    ├── Sastrawi Indonesian Stopwords + Custom Domain Stopwords
    ├── Dictionary & BoW Corpus generation
    ├── Latent Dirichlet Allocation (LDA) training
    ├── Coherence evaluation (C_v) across K=2..10 (K=2 optimal, C_v=0.3911)
    └── SINTA 2 Framing Analysis (Cross-tabulation & Chi-Square test, p < 0.0001)
           │
           ▼
[ Interactive & Academic Deliverables ]
  - index.html (pyLDAvis interactive visualization)
  - models/models-lda/hasil_lda_lengkap.zip (Gensim binaries & CSV annotations)
  - informasi/catatan_pribadi/LAPORAN_PRAKTIKUM_DATA_MINING_TI3A.docx (Target 1)
  - informasi/catatan_pribadi/Analisis Opini Publik MBG - Data Mining TI-3A.pptx (Target 1)
  - Pre-UAS SINTA 3 & SINTA 2 Journal Articles (Target 2)
```

## Key Modules & Responsibilities

| Component | Files | Primary Role |
|---|---|---|
| Data Collector | `Youtube_Data_Collection_API/` | Fetches video metadata and comment threads from YouTube API v3 and dislikes from RYD API |
| Transcript Harvester | `fetch_youtube_transcripts.py` | Extracts speech transcripts using `youtube-transcript-api` with auto-resume and Proton VPN rotation |
| Preprocessing Pipeline | `data_preprocessing.py` | Implements Han et al. 4-pillar data preprocessing (clean, reduce, transform, understand) |
| Topic Modeling (LDA) | `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` | Unsupervised text mining via Gensim LDA, coherence tuning, and pyLDAvis generation |
| Sentiment Classifier (Archived) | `classify_sentiment_indobert.py` | Local Indo-RoBERTa model classifier for validation/benchmarking; cached in `models/` |
| Web Visualization | `index.html` | Standalone interactive pyLDAvis web viewer with modern responsive UI |
| Academic Documentation | `informasi/catatan/` | Literature review (40 journals), statutory legal defense, methodology notes |
| Private Deliverables | `informasi/catatan_pribadi/` | Lab report DOCX and lecture presentation PPTX (gitignored) |

## Data Flow & Storage

1. **Raw State (`data/raw/`)**: API outputs containing raw text, engagement numbers, and transcripts.
2. **Clean State (`data/processed/`)**: 5,207 comments with zero author names (UU PDP compliant), 55 videos with Min-Max & Z-Score columns.
3. **Public Release (`data/public/`)**: Whitelisted sanitized datasets for GitHub distribution.
4. **Binary Artifacts (`models/`)**: Hugging Face local weights and compressed LDA Gensim models.

