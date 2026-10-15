# Rencana & Alur Kerja Training Model AI Data Mining (Topik 1)

Dokumen ini memuat **desain arsitektur, rencana alur kerja (*workflow*), metodologi pelatihan (*training pipeline*), serta target luaran (*deliverables*)** untuk pembuatan model AI dalam rangka memenuhi tugas mata kuliah **Data Mining (TI-3A)** dengan batas waktu presentasi pada **Kamis, 22 Oktober 2026**.

---

## 📌 1. Profil Masalah & Target Pemodelan

* **Topik Terpilih (Approved Dosen ⭐⭐⭐⭐⭐)**:
  > *"Analisis Sentimen dan Polarisasi Sikap Warganet terhadap Kebijakan Makan Bergizi Gratis (MBG) Menggunakan Model Indo-RoBERTa & Komparasi Machine Learning"*
* **Objektif Teknis**:
  1. Membangun model *Machine Learning* terawasi (*Supervised Learning*) untuk klasifikasi sentimen 3 kelas (`Mendukung`, `Menolak`, `Netral`).
  2. Melakukan komparasi kinerja (*benchmarking*) antara model klasik berbasis frekuensi kata (**TF-IDF + Naïve Bayes & SVM**) melawan model *Deep Learning Transformer* (**Indo-RoBERTa**).
  3. Menghasilkan visualisasi interpretasi dan skrip demo interaktif saat presentasi di hadapan dosen penguji.

---

## 📊 2. Aset Dataset yang Digunakan

* **Sumber Data Teks**:
  - `data/processed/dataset_komentar_clean.csv` (Fitur $X$: `comment_text_clean`, 5.207 baris bebas *noise*).
* **Sumber Data Target (Label $Y$)**:
  - `data/processed/dataset_komentar_labeled.csv` (Label kelas dari hasil inferensi Indo-RoBERTa dengan confidence rata-rata 88,73%):
    - `Menolak`: 3.495 baris (67,12%)
    - `Netral`: 1.011 baris (19,42%)
    - `Mendukung`: 701 baris (13,46%)
* **Sumber Data Pendukung**:
  - `data/processed/dataset_video_clean.csv` (Metadata 55 video, format kemasan: *Meme, Serious, News*).

---

## ⚙️ 3. Arsitektur Pipeline Training

Alur komputasi dirancang modular dalam 1 skrip eksekusi (`train_sentiment_models.py`):

```
     [ DATASET KOMENTAR BERSIH ] (5.207 Baris)
                   │
                   ▼
     [ STRATIFIED TRAIN-TEST SPLIT ]
       ├── Data Training : 80% (4.165 data)
       └── Data Testing  : 20% (1.042 data)
                   │
                   ▼
     [ EKSTRAKSI FITUR TF-IDF ]
       ├── TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_features=5000)
       ├── Fit pada Data Training
       └── Transform pada Data Testing
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 [ MULTINOMIAL NB ]    [ LINEAR SVC / SVM ]
 (Laplace Smoothing)   (Maximum Margin Hyperplane)
        │                     │
        └──────────┬──────────┘
                   ▼
     [ EVALUASI & BENCHMARKING ]
       ├── Hitung: Accuracy, Precision, Recall, F1-Score
       ├── Bandingkan dengan Baseline Indo-RoBERTa (Deep Learning)
       └── Plot Confusion Matrix Heatmap & Top Feature Words
                   │
                   ▼
     [ EXPORT MODEL BINER ] (.joblib / .pkl)
```

### Rincian Komponen Teknis:
1. **Stratified Splitting (80:20)**:
   - Menggunakan *Stratified K-Fold / Train-Test Split* agar proporsi kelas minoritas (`Mendukung`: 13,46%) tetap terjaga identik antara data latih dan data uji.
2. **Ekstraksi Fitur Teks**:
   - **TF-IDF (Term Frequency - Inverse Document Frequency)**:
     - Kombinasi *Unigram* dan *Bigram* (`ngram_range=(1, 2)`) untuk menangkap makna konteks negasi (misal: *"tidak enak"*, *"kurang bersih"*).
     - Pembatasan $5.000$ fitur kata teratas (*max_features=5000*) untuk mencegah *overfitting* dan menjaga latensi inferensi super cepat.
3. **Algoritma Model yang Dilatih**:
   - **Multinomial Naïve Bayes (MNB)**: Model probabilistik berbasis Teorema Bayes. Keunggulan: pelatihan instan ($< 0,1$ detik) dan sangat interpretable.
   - **Linear Support Vector Classifier (LinearSVC)**: Algoritma pencari bidang pemisah maksimal (*hyperplane*). Standar emas untuk klasifikasi teks berdimensi tinggi.
   - **Indo-RoBERTa (Transformer)**: Model deep learning kontekstual berbasis arsitektur self-attention.

---

## 🎯 4. Target Luaran (*Deliverables*) Training

Setelah skrip dijalankan, sistem akan menghasilkan aset-aset berikut di folder `models/` dan `data/processed/`:

### A. File Model Biner (Siap Pakai untuk Demo / Inferensi)
1. `models/tfidf_vectorizer.joblib` — Kamus bobot kosakata TF-IDF.
2. `models/model_naive_bayes.joblib` — Model klasifikasi Naive Bayes terlatih.
3. `models/model_svm.joblib` — Model klasifikasi SVM terlatih.

### B. Tabel Laporan Kinerja Model (Bahan Utama Slide Ujian)
Tabel perbandingan performa pada data uji (Test Set: 1.042 data):

| Algoritma | Tipe Pendekatan | Akurasi | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | Waktu Training |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Multinomial Naïve Bayes** | Probabilistik Klasik | *Estimasi 81–84%* | *TBD* | *TBD* | *TBD* | ~0,1 detik |
| **Linear SVM (LinearSVC)** | Hyperplane Linear | *Estimasi 85–88%* | *TBD* | *TBD* | *TBD* | ~0,3 detik |
| **Indo-RoBERTa (Transformer)**| Deep Learning | **88,73%** | ~87% | ~88% | **~88%** | ~1.400 detik (CPU) |

### C. Visualisasi Grafis untuk Slide Presentasi
1. `confusion_matrix_comparison.png` — Heatmap matriks kebingungan (prediksi benar vs salah) untuk Naive Bayes dan SVM.
2. `top_predictive_words.png` — Diagram batang 15 kata/frasa paling berbobot yang mengindikasikan sentimen *Menolak* vs *Mendukung*.
3. `sentiment_vs_media_framing.png` — Diagram batang perbandingan sentimen pada format video *Meme* vs *News* vs *Serious*.

### D. Fitur Demo Langsung di Depan Dosen (*Live Demo CLI*)
Sebuah skrip kecil `predict_interactive.py` yang memungkinkan dosen atau penguji mengetikkan kalimat komentar baru secara bebas di terminal saat presentasi, dan sistem langsung mencetak prediksi sentimen secara instan:
```bash
$ python predict_interactive.py
Ketik komentar: "Program makan gratis ini lauknya bergizi dan anak-anak jadi semangat"
-> Prediksi SVM         : Mendukung (Confidence: 96.2%)
-> Prediksi Naive Bayes : Mendukung (Confidence: 91.5%)
```

---

## 📅 5. Jadwal Kerja (Timeline Menuju 22 Oktober 2026)

| Target Tanggal | Agenda Pekerjaan | Status |
| :--- | :--- | :---: |
| **15 Okt 2026** | Formulasi arsitektur & dokumentasi rencana training model | **SELESAI** |
| **16–18 Okt 2026** | Fokus tugas urgen Danish (Repositori dalam status *standby*) | *On Hold* |
| **19 Okt 2026** | Eksekusi skrip `train_sentiment_models.py` & ekspor file model | *Next Step* |
| **20 Okt 2026** | Pembuatan grafik visualisasi (Confusion Matrix & Top Features) | *Next Step* |
| **21 Okt 2026** | Finalisasi slide presentasi & uji coba live demo CLI | *Next Step* |
| **22 Okt 2026** | **HARI-H: PRESENTASI DI DEPAN DOSEN PENGUJI** | 🎯 **GOAL** |

---
*Dokumen ini menjadi acuan teknis saat eksekusi pelatihan model AI dimulai.*

