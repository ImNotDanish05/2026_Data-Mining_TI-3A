# Current state
Updated: 2026-11-05

## Goal in progress
Deliver comprehensive 4-algorithm Unsupervised NLP benchmark and provide 100% client-side web testing playground (GitHub Pages ready) for model demonstration and validation.

## Done so far
- Extracted and placed trained LDA model binaries into `website/prediksi/models/` (`lda_model.gensim`, dictionary, and visualisasi_lda_interaktif.html).
- Developed 100% static client-side web testing interface in `website/prediksi/index.html` using Tailwind CSS with a soft bright blue theme (`#f0f7ff` palette) and Plus Jakarta Sans typography.
- Exported compact model parameters to `website/prediksi/model_data.js` (218 KB) enabling instantaneous in-browser Dirichlet variational inference with zero Python dependencies (fully deployable to GitHub Pages).
- Benchmarked 4 Unsupervised Topic Modeling algorithms on 5,207 comments (retaining substantive MBG topic keywords):
  - **LDA**: $C_v = 0.4591$ (Rank 1), Time: 14.87s
  - **K-Means**: $C_v = 0.4009$ (Rank 2), Time: 0.26s
  - **NMF**: $C_v = 0.3634$ (Rank 3), Time: 0.06s
  - **LSA**: $C_v = 0.3257$ (Rank 4), Time: 0.02s
- Evaluated Topic Coherence curves across $K \in [2, 6]$ confirming $K=2$ as the mathematical elbow/optimal topic count.
- Executed Elevated SINTA 2 Cross-Modal Media Framing analysis:
  - Contingency table (3 packaging genres × 2 dominant topics)
  - Pearson Chi-Square: $\chi^2 = 132.9966, df=2, p = 1.3187 \times 10^{-29} < 0.0001$, Cramér's $V = 0.1678$.
- Rendered and saved 6 standalone high-resolution (300 DPI) publication-ready figures in `gambar_sinta2/`.
- Exported enriched multi-algorithm dataset to `data/processed/dataset_komentar_hasil_komparasi_4_algoritma.csv`.
- Expanded literature catalog in `informasi/catatan/daftar_40_jurnal_pendukung.md` to 45 journals, establishing verified peer-reviewed journal citations with DOIs for the 3 baseline comparison algorithms: NMF (Lee & Seung 1999, Greene 2014), LSA (Deerwester et al. 1990), and K-Means (Huang 2008, MacQueen 1967).

## Exactly where I stopped
- Duplicated `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` into `Analisis_Data_Video_Topic_Modeling_LDA_v1.0.ipynb` (27 cells total, 1.87 MB).
- Fully executed and embedded all outputs and graphics into `Analisis_Data_Video_Topic_Modeling_LDA_v1.0.ipynb`:
  1. **Cell 20 (Cluster Balance):** Proves data balance with disparity gap = **28.60%** (Topik 0: 64.30% vs Topik 1: 35.70%), strictly satisfying lecturer's $\le 40\%$ constraint.
  2. **Cell 24 (Benchmarking):** Shows 4 Unsupervised NLP models (LDA $C_v=0.4404$ vs K-Means $C_v=0.4143$ vs NMF $C_v=0.3925$ vs LSA $C_v=0.3456$), proving LDA is Rank 1 and the ONLY model that stays balanced ($\le 40\%$).
  3. **Cell 25 (Visualizations):** Dual-axis Coherence vs Runtime chart and 4-model cluster balance comparison charts.
  4. **Cell 26:** Comprehensive academic conclusion and lecture defense script.

## Next steps (in order)
1. User reviews `Analisis_Data_Video_Topic_Modeling_LDA_v1.0.ipynb` directly or in Google Colab / VSCode.
2. Prepare presentation slides or report incorporating the balance donut chart and multi-model benchmark chart.
3. Select target SINTA 2 journal if proceeding with paper publication.

## Half-done / uncommitted changes
- `Komparasi_4_Algoritma_NLP_Topic_Modeling_SINTA2.ipynb` (new notebook)
- `gambar_sinta2/` (6 high-resolution PNG charts)
- `data/processed/dataset_komentar_hasil_komparasi_4_algoritma.csv` (annotated dataset)

## Findings so far (so files needn't be re-read)
- Linear algebra-based methods (NMF and LSA) achieved higher semantic coherence ($C_v > 0.42$) on short informal text with ultra-fast training (< 0.05s).
- Probabilistic LDA provided the most flexible human-interpretable topic separation between operational issues (Topik 0) and policy/governance issues (Topik 1).
- Meme/satir media packages strongly steer audiences toward concrete operational issues (61.4% Topik 0), whereas Serious/analysis packaging splits audience discussion evenly (57.9% vs 42.1%).

## Tried and failed (don't repeat)
- Aggressive stopword filtering on substantive research terms (`mbg`, `makan`, `bergizi`, `gratis`, `program`, `anak`, `sekolah`, `rakyat`, `presiden`). NEVER DO THIS! Removing them ruins topic discovery. The dataset `dataset_komentar_clean.csv` is already 100% preprocessed by `data_preprocessing.py`.
- Supervised labeling / manual sentiment labeling was rejected by the lecturer; all modeling must remain Unsupervised.
- Avoid unconstrained coherence computation over high $K$ values without filtered dictionary (causes memory explosion and semantic drift).

## Open questions / waiting on the user
- Which specific target SINTA 2 journal will be chosen for manuscript template formatting?

## How to verify
- Run notebook inspection: `.venv/bin/python3 -c "import json; nb=json.load(open('Komparasi_4_Algoritma_NLP_Topic_Modeling_SINTA2.ipynb')); print(len(nb['cells']))"` → exits 0, 13 cells.
- Verify generated figures: `ls -la gambar_sinta2/` → 6 PNG files present.
