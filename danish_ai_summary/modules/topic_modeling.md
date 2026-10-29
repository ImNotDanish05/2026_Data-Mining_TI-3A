# Topic Modeling & LDA Module

- Purpose: Implements unsupervised topic discovery on Indonesian YouTube comments using Gensim LDA, coherence score tuning, and interactive pyLDAvis visualization.
- Key files:
  - `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` — Primary Google Colab / Jupyter notebook executing full LDA modeling pipeline.
  - `index.html` — Interactive pyLDAvis dashboard embedded with modern CSS container.
  - `models/models-lda/hasil_lda_lengkap.zip` — Compressed LDA model binaries, dictionary, and annotated comment CSV.
  - `informasi/catatan/rencana_dan_alur_training_model.md` — Detailed theoretical and mathematical blueprint.
- How it works:
  1. Tokenizes clean Indonesian comment corpus from `data/processed/dataset_komentar_clean.csv`.
  2. Applies PySastrawi stopwords and custom Indonesian slang/filler stopwords.
  3. Builds Gensim Dictionary and Bag-of-Words (BoW) corpus.
  4. Evaluates Topic Coherence ($C_v$) across candidate topic counts $K \in [2, 10]$. Optimal topic count was determined to be $K=2$ ($C_v = 0.3911$).
  5. Assigns dominant topic and topic probability to each comment.
  6. Conducts Cross-Modal Media Framing analysis: cross-tabulating dominant topics against media packaging (Meme vs Serious vs News) and calculates Chi-Square test ($\chi^2 = 212.4579, df=2, p < 0.0001$).
  7. Exports pyLDAvis HTML to `index.html`.
- Interfaces:
  - Consumes `data/processed/dataset_komentar_clean.csv` and `data/processed/dataset_video_clean.csv`.
  - Feeds into research figures and tables in academic publications.
- Gotchas:
  - Must remain strictly unsupervised (no manual or pseudo-labeling).
  - pyLDAvis visualization requires specific CDN scripts loaded in `index.html`.
- Tests / Verification:
  - Inspect coherence scores and dominant topic distribution in notebook outputs.
- Last touched: 2026-10-29

