# Rencana & Arsitektur Pemodelan Unsupervised NLP: Topic Modeling (LDA)

Dokumen ini memuat **alur kerja resmi, metodologi pelatihan, dan target luaran model AI** untuk tugas mata kuliah **Data Mining (TI-3A)** yang akan dipresentasikan pada **Kamis, 22 Oktober 2026**.

---

## ⚠️ CATATAN RESMI ARAHAN DOSEN (KENAPA HARUS UNSUPERVISED NLP?)

> [!IMPORTANT]
> **Keputusan Resmi Dosen Penguji (15 Oktober 2026):**
> 1. **Dosen secara tegas MELARANG penggunaan data berlabel (*STRICTLY NO LABELLING*)**, baik pelabelan manual oleh manusia maupun *pseudo-labeling*.
> 2. **Dosen mewajibkan penggunaan algoritma Natural Language Processing (NLP)** yang mampu membedah data teks komentar secara mandiri langsung dari data (*pure data-driven*).
> 3. **Alasan Perubahan Metodologi:** Seluruh rencana training terawasi (*Supervised Learning* seperti Naïve Bayes, SVM, atau klasifikasi sentimen terbimbing) **RESMI DIHAPUS**. Proyek dialihkan 100% ke ranah **Unsupervised NLP / Topic Discovery** menggunakan algoritma **Latent Dirichlet Allocation (LDA)**. Model ini tidak memerlukan satu pun label kelas masukan.

---

## 📌 1. Profil Proyek & Topik Resmi (Approved ⭐⭐⭐⭐⭐)

* **Judul Penelitian**:
  > *"Pemodelan Topik Dinamis (Topic Modeling) Opini Publik terhadap Kebijakan Makan Bergizi Gratis (MBG) pada Komentar YouTube Menggunakan Algoritma Unsupervised Latent Dirichlet Allocation (LDA)"*
* **Objektif Utama**:
  1. Menemukan tema-tema isu keluhan dan aspirasi publik secara otomatis (*thematic discovery*) dari 5.207 komentar tanpa intervensi label manusia.
  2. Mengukur proporsi dominasi isu publik (misal: berapa persen warganet yang resah soal anggaran vs kualitas makanan vs tata kelola).
  3. Memvisualisasikan peta semantik topik secara interaktif menggunakan **pyLDAvis** untuk materi presentasi ujian.

---

## 📊 2. Sumber Data Masukan

* **Dataset Primer yang Digunakan**: `data/processed/dataset_komentar_clean.csv`
  - Total sampel: **5.207 komentar netizen** (100% bebas missing value, emoji, timestamp, dan telah melalui *case-folding*).
  - Kolom masukan utama: `comment_text_clean`.
* **Karakteristik Data**: Teks pendek bahasa Indonesia informal (*slang*, singkatan) tanpa label target ($Y$).
* **Aset Data yang WAJIB DILINDUNGI (JANGAN DIHAPUS)**:
  - `data/processed/dataset_komentar_labeled.csv` (Berisi 5.207 data berlabel Indo-RoBERTa terdahulu. Meskipun pemodelan utama saat ini memakai LDA Unsupervised tanpa label, **aset berlabel ini dilarang keras dihapus** dan tetap disimpan permanen sebagai cadangan / validasi cross-check jika sewaktu-waktu dibutuhkan).

---

## ⚙️ 3. Arsitektur Pipeline Unsupervised NLP (LDA)

```
       [ DATASET KOMENTAR BERSIH ] (5.207 Teks)
                         │
                         ▼
       [ TEXT PREPARATION UNTUK NLP ]
         ├── Tokenization (Pemecahan kata/token)
         ├── Filtering Stopwords Bahasa Indonesia
         │   (hapus: 'yang', 'di', 'dan', 'dari', 'ini', 'itu', dll.)
         ├── Frasa Ekstraksi: N-Gram (Unigram & Bigram)
         └── Ekstrem Frequency Filter (buang kata sangat langka / sangat umum)
                         │
                         ▼
       [ PEMBENTUKAN DICTIONARY & CORPUS ]
         ├── Dictionary ID2Word (Pemetaan kosakata ke ID unik)
         └── Bag-of-Words (BoW) Corpus Matrix: (Word_ID, Frekuensi)
                         │
                         ▼
       [ PENALAAN JUMLAH TOPIK OPTIMAL (K) ]
         ├── Iterasi K = [2, 3, 4, 5, 6, 7]
         └── Evaluasi Metrik: Topic Coherence Score (Cv)
                         │
                         ▼
       [ PELATIHAN MODEL AKHIR LDA ]
         ├── Algoritma: Latent Dirichlet Allocation (Gensim / Scikit-Learn)
         ├── Estimasi Variational Bayes / Gibbs Sampling
         └── Distribusi: Dirichlet Prior (Alpha & Beta/Eta)
                         │
                         ▼
       [ GENERASI DELIVERABLES UNTUK PRESENTASI ]
         ├── 1. Interactive Web HTML: pyLDAvis visualization
         ├── 2. Grafik Distribusi Proporsi Isu Warganet (% Pie/Bar Chart)
         ├── 3. Word Cloud Kata Kunci per Topik
         └── 4. Ekspor Dataset Baru (+ kolom: dominant_topic, topic_prob)
```

---

## 🎯 4. Target Luaran (*Deliverables*) Training Model

Hasil nyata yang akan dihasilkan skrip pelatihan (`train_lda_topic_modeling.py`):

### A. Tabel Ekstraksi Topik Otomatis (Temuan Model)
Model mengeluarkan daftar topik murni dari asosiasi kata, misalnya:
* **Topik 1 (Kualitas & Higienitas Makanan):** `basi`, `keracunan`, `menu`, `dapur`, `ompreng`, `susu`.
* **Topik 2 (Kekhawatiran Anggaran & Korupsi):** `anggaran`, `apbn`, `pajak`, `korupsi`, `triliun`, `dana`.
* **Topik 3 (Prioritas Kebijakan & Pendidikan):** `guru`, `honorer`, `gaji`, `sekolah`, `beasiswa`, `kuliah`.

### B. Visualisasi Mewah untuk Presentasi (`visualisasi_lda_interaktif.html`)
* Visualisasi interaktif berbasis **pyLDAvis**:
  - Lingkaran topik di ruang 2 dimensi (*Principal Component / Intertopic Distance Map*).
  - Jika lingkaran diklik, menampilkan diagram batang 30 kata kunci teratas beserta tingkat relevansinya ($\lambda$).
  - Sangat mudah dipresentasikan langsung di depan dosen lewat browser Chrome/Firefox.

### C. Grafik Proporsi Isu Warganet
* Diagram lingkaran (*Pie Chart*) yang menyimpulkan:
  - Berapa % masyarakat yang mengkritisi anggaran.
  - Berapa % yang mengkhawatirkan kualitas makanan.
  - Berapa % yang mendukung atau menuntut prioritas lain.

### D. Dataset Baru Beranotasi Otomatis (`dataset_komentar_topik.csv`)
File CSV komentar yang diperkaya 2 kolom baru hasil inferensi model:
1. `dominant_topic`: Topik utama dari isi komentar tersebut (Topik 1, 2, atau 3).
2. `topic_probability`: Tingkat keyakinan model terhadap topik tersebut (misal: 0.89).

### E. Metrik Validasi Matematis Tanpa Label
* **Topic Coherence ($C_v$)**: Membuktikan secara matematis bahwa kata-kata dalam satu topik memiliki kemiripan semantik tinggi, bukan kumpulan kata acak.
* **Perplexity Score**: Memvalidasi daya generalisasi model terhadap teks baru.

---

## 📅 5. Roadmap Eksekusi Menuju 22 Oktober 2026

| Waktu | Agenda | Status |
| :--- | :--- | :---: |
| **15 Okt 2026** | Formulasi arsitektur Unsupervised NLP (LDA) & persetujuan dosen | **SELESAI** |
| **16–18 Okt 2026** | Standby (Danish fokus menyelesaikan tugas kuliah yang lebih urgen) | *On Hold* |
| **19 Okt 2026** | Eksekusi skrip `train_lda_topic_modeling.py` (Gensim + Stopwords ID + Coherence) | *Next Step* |
| **20 Okt 2026** | Generate visualisasi pyLDAvis HTML & grafik proporsi isu publik | *Next Step* |
| **21 Okt 2026** | Penyusunan slide presentasi (memasukkan hasil temuan topik & visualisasi) | *Next Step* |
| **22 Okt 2026** | **HARI-H PRESENTASI DI HADAPAN DOSEN PENGUJI** | 🎯 **GOAL** |

---
*Dokumen ini merupakan acuan tunggal metodologi pemodelan AI menggantikan seluruh rencana supervised training sebelumnya.*
