# Analisis Data Mining & Topic Modeling Komentar YouTube Kebijakan Publik (Makan Bergizi Gratis)

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Mata Kuliah](https://img.shields.io/badge/Matkul-Data%20Mining%20(TI--3A)-green.svg)]()
[![Metodologi](https://img.shields.io/badge/Metode-Unsupervised%20NLP%20(LDA)-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-Academic%20Research-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

Repositori ini memuat implementasi proyek akademis praktikum dan riset **Data Mining (TI-3A)**. Proyek ini mencakup siklus penambangan data lengkap: mulai dari akuisisi data primer (*YouTube Data API v3* & *Return YouTube Dislike API*), prapemrosesan data 100% (*Data Cleaning, Reduction, Transformation, Outlier Detection*), hingga pemodelan teks tanpa label (*Unsupervised NLP: Topic Modeling menggunakan Latent Dirichlet Allocation / LDA*).

---

## ⚖️ DISCLAIMER HUKUM, ETIKA RISET & PERNYATAAN NETRALITAS POLITIK

> [!IMPORTANT]
> **PERNYATAAN RESMI PENULIS (LEGAL & ETHICAL DISCLAIMER):**
> 
> 1. **Murni Bertujuan Akademik & Pendidikan (*Purely Academic Purpose*):**
>    Proyek dan repositori ini dibuat **semata-mata untuk memenuhi tugas akademik mata kuliah Data Mining pada program studi Teknik Informatika (TI-3A)**. Penulis **TIDAK memiliki afiliasi politik, partisan, relasi kekuasaan, maupun kepentingan finansial** dengan partai politik, organisasi kemasyarakatan, figur pejabat publik, calon pejabat, atau institusi pemerintah mana pun.
>
> 2. **Netralitas Analisis & Sifat Data-Driven (*Strict Political Neutrality*):**
>    Pemilihan studi kasus kebijakan Makan Bergizi Gratis (MBG) dan video figur publik semata-mata didasarkan pada **tingginya volume interaksi warganet dan variansi opini di media sosial** yang menjadikannya studi kasus ideal untuk pengujian prapemrosesan data (*handling noisy text*) dan pemodelan *Unsupervised Topic Modeling*. Penulis tidak memihak (pro maupun kontra) terhadap kebijakan yang dianalisis; seluruh temuan disajikan secara deskriptif dan statistik matematis.
>
> 3. **Kepatuhan Privasi Data (*Privacy-Preserving Data Mining & UU PDP*):**
>    - Seluruh data teks komentar diambil dari **ranah publik YouTube (*public domain*)** secara legal melalui antarmuka resmi **Google YouTube Data API v3** sesuai dengan Ketentuan Layanan (*Terms of Service*) YouTube.
>    - Sebagai bentuk pemenuhan etika penelitian dan kepatuhan terhadap regulasi privasi (termasuk **UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi / UU PDP**), tahap prapemrosesan telah melakukan **Anonimisasi Mutlak (*Anonymization*)**: **Seluruh nama akun, identitas profil, dan username (`author`) telah dihapus secara permanen** dari dataset analisis.
>    - Repositori ini **tidak mengumpulkan, tidak menyimpan, dan tidak menyebarkan data pribadi sensitif (*PII - Personally Identifiable Information*)** apa pun, serta bebas dari praktik *doxxing* atau pelanggaran hukum siber.
>
> 4. **Penafian Tanggung Jawab Isi Komentar (*User-Generated Content Liability Waiver*):**
>    Seluruh opini, sentimen, atau pernyataan yang tertuang dalam teks komentar adalah **murni ekspresi individual dari masing-masing pengguna platform YouTube** dan **BUKAN merupakan pendapat, keyakinan, atau pernyataan dari penulis repositori ini**. Penulis tidak bertanggung jawab atas segala bentuk penafsiran keliru atau penyalahgunaan data oleh pihak ketiga di luar ranah pendidikan.

---

## 📖 Ringkasan Proyek

Penelitian ini membedah respon dan diskursus masyarakat Indonesia di platform YouTube terhadap salah satu kebijakan strategis nasional, yaitu program **Makan Bergizi Gratis (MBG)**. 

Alih-alih menggunakan dataset instan dari internet, proyek ini membangun **dataset primer mandiri** dan menerapkan arsitektur **Unsupervised NLP (Topic Modeling - LDA)** tanpa pelabelan terawasi (*zero supervised labeling*) untuk menemukan secara otomatis tema-tema keresahan, kritik, dan aspirasi warganet langsung dari data.

---

## 📊 Profil Aset Dataset Primer

Dataset dikumpulkan secara legal melalui pipa ekstraksi otomatis berbasis API:

1. **Dataset Komentar Netizen (`data/processed/dataset_komentar_clean.csv`)**:
   - **Total Sampel**: **5.207 baris komentar bersih** (dieliminasi dari 5.284 data mentah setelah pembersihan null dan emoji/timestamp murni).
   - **Tindakan Pembersihan Teks**: Penghapusan URL, mention (`@`), tagar (`#`), emoji Unicode, stempel waktu video (`MM:SS`), tanda baca berlebih, dan penyeragaman huruf kecil (*case-folding*).
   - **Preservasi Privasi**: Kolom `author` dibuang 100% (*anonymized*).

2. **Dataset Metadata Video (`data/processed/dataset_video_clean.csv`)**:
   - **Total Sampel**: **55 video YouTube** dari 10 kanal publik terkemuka (*Kompas TV, CNN Indonesia, Najwa Shihab, Ferry Irwandi, Raymond Chin, Guru Gembul, Caveine, dll.*).
   - **Distribusi Topik**: 29 video seputar kebijakan MBG, 26 video seputar kebijakan pemerintahan Prabowo Subianto.
   - **Distribusi Kemasan Media**: Seimbang antara 3 spektrum: *Meme/Satir* (24 video), *Serious Opinion/Edukasi Kritis* (16 video), dan *News Formal* (15 video).
   - **Normalisasi Numerik**: Fitur views, likes, comments, dislikes (RYD API), dan engagement rate telah dinormalisasi menggunakan **Min-Max Normalization** $[0, 1]$ dan **Z-Score Normalization**.
   - **Deteksi Pencilan**: Pencilan diidentifikasi secara matematis menggunakan rumus Boxplot $1.5 \times IQR$.

3. **Dataset Transkrip Wicara Video (`data/raw/dataset_transkrip_video.csv`)**:
   - Transkrip narasi wicara lengkap dari **55 video (100%)** dengan total volume **134.986 kata**.

---

## 🏗️ Metodologi & Arsitektur Pemodelan

Proyek ini mengadopsi 4 pilar utama prapemrosesan data mining dan pemodelan penambangan teks:

```
[ AKUISISI DATA ] YouTube Data API v3 & RYD API (55 Video & 5.284 Komentar)
       │
       ▼
[ PRAPEMROSESAN DATA (100%) ]
  ├── 1. Data Cleaning: Drop 4 baris null & 73 baris hampa, Regex cleaning 7 derau teks
  ├── 2. Data Reduction & Privacy: Anonymization (Drop author), 0 orphan foreign key
  ├── 3. Data Transformation: Min-Max [0, 1] & Z-Score Scaling pada 6 fitur numerik
  └── 4. Data Understanding: Deteksi pencilan boxplot 1.5x IQR (views & likes outliers)
       │
       ▼
[ PEMODELAN UNSUPERVISED NLP (TOPIC MODELING) ]
  ├── Tokenization & N-Gram (Unigram + Bigram)
  ├── Indonesian Stopwords Filtering
  ├── Pembentukan Dictionary & Bag-of-Words (BoW) Corpus
  ├── Pelatihan Algoritma Latent Dirichlet Allocation (LDA)
  └── Evaluasi Matematis: Topic Coherence Score (Cv) & Perplexity
       │
       ▼
[ OUTPUT & DELIVERABLES ]
  ├── Peta Visualisasi Interaktif pyLDAvis (HTML Browser)
  ├── Distribusi Persentase Isu Publik (Kualitas Makanan vs Anggaran vs Kebijakan)
  └── Dataset Beranotasi Topik Otomatis (dominant_topic & topic_prob)
```

---

## 📁 Struktur Direktori Repositori

```bash
├── data/
│   ├── raw/                           # Data mentah hasil ekstraksi API (CSV)
│   └── processed/                     # Data bersih siap pakai & laporan metrik
│       ├── dataset_komentar_clean.csv # 5.207 komentar bersih (teranonimkan)
│       ├── dataset_video_clean.csv    # 55 metadata video ternormalisasi
│       ├── laporan_preprocessing.json # Laporan statistik before vs after
│       └── ringkasan_perbandingan_preprocessing.md
├── informasi/
│   ├── materi/                        # Ringkasan materi perkuliahan Data Mining (Week 01-04)
│   └── catatan/                       # Dokumentasi pembelaan riset & jurnal rujukan
│       ├── bukti_dan_argumen_preprocessing_100_persen.md # Bukti empiris 4 pilar
│       ├── rencana_dan_alur_training_model.md            # Arsitektur Unsupervised LDA
│       ├── usulan_5_topik_penelitian.md                  # Usulan topik riset
│       └── daftar_20_jurnal_pendukung.md                 # 20 rujukan jurnal SINTA/Scopus
├── Youtube_Data_Collection_API/       # Modul skrip ekstraksi YouTube API v3 & RYD
├── data_preprocessing.py              # Pipeline mandiri pembersihan data
├── fetch_youtube_transcripts.py       # Ekstraksi transkrip wicara video
├── classify_sentiment_indobert.py     # Ekstraksi sentimen (arsip model)
├── DANISH_AI_AGENT.md                 # Konteks proyek ringkas untuk AI assistant
├── SKILL.md                           # Pedoman tata kelola konteks agen AI
└── README.md                          # Dokumentasi utama proyek
```

---

## 🚀 Panduan Instalasi & Menjalankan

### 1. Kloning Repositori
```bash
git clone https://github.com/ImNotDanish05/2026_Data-Mining_TI-3A.git
cd 2026_Data-Mining_TI-3A
```

### 2. Setup Virtual Environment & Dependensi
```bash
python -m venv .venv
source .venv/bin/activate  # Untuk Linux/macOS
# .venv\Scripts\activate   # Untuk Windows

pip install -r Youtube_Data_Collection_API/requirements.txt
pip install gensim pyLDAvis scikit-learn matplotlib
```

### 3. Menjalankan Pipeline Prapemrosesan Data
Untuk memverifikasi pembersihan 5.207 komentar dan normalisasi video:
```bash
python data_preprocessing.py
```
*Hasil pembersihan akan otomatis diperbarui di direktori `data/processed/` bersama laporan statistik ringkasnya.*

---

## 📚 Landasan Teori & Literatur Pendukung

Penelitian ini didukung oleh kajian pustaka ilmiah yang terdokumentasi di [daftar_20_jurnal_pendukung.md](informasi/catatan/daftar_20_jurnal_pendukung.md), meliputi:
- **Jiawei Han, Micheline Kamber, Jian Pei (2012)**: *Data Mining: Concepts and Techniques (3rd Edition)* — Teori 4 pilar data preprocessing, normalisasi skor-Z, min-max, dan deteksi pencilan boxplot.
- **David M. Blei, Andrew Y. Ng, Michael I. Jordan (2003)**: *Latent Dirichlet Allocation* — Fondasi probabilitas model topik tanpa label.
- **Michael Roder, Andreas Both, Alexander Hinneburg (2015)**: *Exploring the Space of Topic Coherence Measures* — Validasi metrik koherensi topik semantik ($C_v$).

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE). Bebas digunakan, dipelajari, dan dikembangkan kembali untuk keperluan edukasi dan riset akademis.

---
*Dikembangkan oleh **ImNotDanish05** untuk Ujian & Praktikum Mata Kuliah Data Mining (TI-3A) — Tahun Akademik 2026.*

## 🚀 Panduan Instalasi & Menjalankan

### 1. Kloning Repositori
```bash
git clone https://github.com/ImNotDanish05/2026_Data-Mining_TI-3A.git
cd 2026_Data-Mining_TI-3A
```

### 2. Setup Virtual Environment & Dependensi
```bash
python -m venv .venv
source .venv/bin/activate  # Untuk Linux/macOS
# .venv\Scripts\activate   # Untuk Windows

pip install -r Youtube_Data_Collection_API/requirements.txt
pip install gensim pyLDAvis scikit-learn matplotlib
```

### 3. Menjalankan Pipeline Prapemrosesan Data
Untuk memverifikasi pembersihan 5.207 komentar dan normalisasi video:
```bash
python data_preprocessing.py
```
*Hasil pembersihan akan otomatis diperbarui di direktori `data/processed/` bersama laporan statistik ringkasnya.*

---

## 📚 Landasan Teori & Literatur Pendukung

Penelitian ini didukung oleh kajian pustaka ilmiah yang terdokumentasi di [daftar_20_jurnal_pendukung.md](informasi/catatan/daftar_20_jurnal_pendukung.md), meliputi:
- **Jiawei Han, Micheline Kamber, Jian Pei (2012)**: *Data Mining: Concepts and Techniques (3rd Edition)* — Teori 4 pilar data preprocessing, normalisasi skor-Z, min-max, dan deteksi pencilan boxplot.
- **David M. Blei, Andrew Y. Ng, Michael I. Jordan (2003)**: *Latent Dirichlet Allocation* — Fondasi probabilitas model topik tanpa label.
- **Michael Roder, Andreas Both, Alexander Hinneburg (2015)**: *Exploring the Space of Topic Coherence Measures* — Validasi metrik koherensi topik semantik ($C_v$).

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE). Bebas digunakan, dipelajari, dan dikembangkan kembali untuk keperluan edukasi dan riset akademis.

---
*Dikembangkan oleh **ImNotDanish05** untuk Ujian & Praktikum Mata Kuliah Data Mining (TI-3A) — Tahun Akademik 2026.*

