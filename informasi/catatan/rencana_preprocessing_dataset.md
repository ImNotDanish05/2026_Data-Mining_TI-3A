# Catatan Analisis Dataset & Rencana Preprocessing

Dokumen ini berisi dokumentasi evaluasi dataset primer, justifikasi akademis untuk pertanggungjawaban di depan dosen, pemetaan kondisi data mentah saat ini, serta *roadmap* pelaksanaan prapemrosesan data (*data preprocessing*).

---

## 1. Profil Dataset Primer Saat Ini

Dataset dikumpulkan secara mandiri menggunakan skrip ekstraksi berbasis **YouTube Data API v3** dan **Return YouTube Dislike (RYD) API**.

### A. Dataset Video (`dataset_video_politik.csv`)
- **Total Sampel**: 55 video
- **Atribut (18 Kolom)**: `video_id`, `title`, `channel_title`, `published_at`, `duration_seconds`, `category_id`, `view_count`, `like_count`, `dislike_count_est`, `raw_likes_ryd`, `raw_dislikes_ryd`, `comment_count`, `dislike_ratio`, `engagement_rate`, `views_per_day`, `topik_video`, `tipe_video`, `channel_video`.
- **Distribusi Topik**:
  - `MBG` (Makan Bergizi Gratis): 29 video
  - `PrabowoSubianto`: 26 video
- **Distribusi Tipe Konten**:
  - `Meme`: 24 video
  - `Serious` (Opini/Edukasi Kritis): 16 video
  - `News` (Berita Formal): 15 video
- **Distribusi Saluran (10 Channel)**: Caveine (17), KOMPASTV (12), GuruGembul (8), TretanMuslim (7), RaymondChin (4), FerryIrwandi (3), NajwaShihab (1), CNNIDOFFICIAL (1), TVOneNews (1), MALAKA (1).

### B. Dataset Komentar (`dataset_komentar_politik.csv`)
- **Total Sampel**: 5.284 baris komentar
- **Atribut (7 Kolom)**: `comment_id`, `video_id`, `author`, `comment_text`, `comment_likes`, `total_replies`, `published_at`.
- **Relasi**: Terhubung secara relasional dengan dataset video melalui kunci `video_id`.

---

## 2. Justifikasi Akademis & Pembelaan Dataset di Depan Dosen

Dataset ini **sangat aman, sah, dan memiliki nilai orisinalitas tinggi** untuk tugas makalah prapemrosesan data mining.

### Poin Kekuatan:
1. **Status Primary Data (Nilai Plus Orisinalitas)**:
   - Data diambil langsung dari sumber primer melalui API resmi, bukan mengunduh dataset instan sekunder dari repositori publik (seperti Kaggle).
2. **Kesesuaian Volume**:
   - Terdiri dari 55 unit observasi video dan **5.284 unit teks komentar**, skala yang sangat proporsional dan realistis untuk eksperimen data mining akademik.
3. **Kaya akan Kasus Preprocessing**:
   - Menghadapi masalah riil media sosial: variansi data numerik yang jomplang (*skewed*), data hilang (*missing values*), teks derau (*noise*: emoji, slang, URL, timestamp), serta kebutuhan etika privasi (*anonymization*).

### Antisipasi Pertanyaan Dosen & Panduan Jawaban:

| Potensi Pertanyaan Penguji | Strategi Jawaban Akademis |
| :--- | :--- |
| **"Topiknya politik, apakah pemilihan video tidak bias?"** | *"Penelitian ini netral dan murni statistik. Pemilihan video sengaja mencakup 3 spektrum berimbang: **News** (media massa formal independen), **Serious** (analisis dan diskusi kritis edukatif), dan **Meme/Kultural** (reaksi organik masyarakat umum), dengan proporsi topik MBG dan figur kebijakan yang relatif seimbang (29 vs 26)."* |
| **"Mengapa jumlahnya 55 video dan bagaimana metode samplingnya?"** | *"Menggunakan metode **Purposive Sampling** (pengambilan sampel bertujuan) dengan kriteria inklusi video paling banyak ditonton dan mendiskusikan topik kebijakan tersebut pada periode waktu pengamatan. Fokus analisis granular kami bertumpu pada **5.284 data komentar netizen**."* |
| **"Apakah pengambilan data komentar tidak melanggar privasi?"** | *"Data diambil dari komentar ranah publik YouTube. Sebagai pemenuhan etika **Privacy-Preserving Data Mining**, pada tahap Preprocessing dilakukan tindakan **Anonymization** dengan membuang kolom identitas akun (`author`)."* |
| **"YouTube kan sudah menutup dislike, dari mana angka dislike didapat?"** | *"Dislike diperoleh melalui estimasi Return YouTube Dislike (RYD) API yang menginterpolasi data ekstensi pengguna terhadap rasio like YouTube API resmi."* |

---

## 3. Evaluasi Kondisi Data Mentah (Status Preprocessing Saat Ini)

Saat ini dataset berada pada status **Data Mentah (*Raw Ingestion*)**.

### Yang Sudah Dilakukan oleh Skrip Collector:
- Sanitasi pemecah baris CSV: Mengganti karakter `\r`, `\n`, dan `\t` menjadi spasi agar sintaks CSV tidak rusak.
- Parsing durasi ISO 8601 (`PT15M33S` $\rightarrow$ detik integer).
- Ekstraksi metrik turunan awal: `dislike_ratio`, `engagement_rate`, dan `views_per_day`.

### Masalah & Derau yang Ditemukan pada Data Mentah:
1. **Missing Values pada Komentar**:
   - Terdapat **4 baris komentar kosong (`NaN/Null`)** pada `comment_text`.
2. **Derau Teks Komentar (*Text Noise*)**:
   - Memuat banyak emoji (`😢`, `😂`, `🥀`).
   - Memuat stempel waktu video (*timestamp*, misal `6:38`, `3:42`).
   - Karakter non-alfanumerik ganda, tanda baca berlebih, dan format huruf campur (*case-folding* belum ada).
   - Bahasa tidak baku, slang, dan singkatan (*wkwkwk*, *anj*, *coy*).
3. **Isu Privasi Akun**:
   - Kolom `author` masih menampilkan nama profil pengguna asli.
4. **Variansi Skala Numerik yang Ekstrem (*Skewed Distribution*)**:
   - `view_count`: Min = 5.622 hingga Max = 6.192.423 (faktor perbedaan > 1.000x).
   - `like_count`: Min = 4 hingga Max = 130.942.
   - Belum dilakukan normalisasi/standarisasi rentang nilai.

---

## 4. Rencana Kerja Preprocessing (*Action Plan*)

Mengacu pada 4 pilar prapemrosesan (Materi Kuliah Bab 3 / Week 04):

```
                     [ RAW DATASETS ]
          (dataset_video.csv & dataset_komentar.csv)
                            │
   ┌────────────────────────┴────────────────────────┐
   ▼                                                 ▼
[ PREPROCESSING TEKS KOMENTAR ]           [ PREPROCESSING TABEL VIDEO ]
1. Drop 4 baris missing value             1. Deteksi Outliers (IQR 1.5x Rule)
2. Anonymize (Drop kolom 'author')        2. Scaling Numerik:
3. Regex Text Cleaning:                      - Min-Max Normalization [0, 1]
   - Hapus URL / Link                        - Z-Score Normalization
   - Hapus Emoji & Simbol Khusus          3. Uji Asosiasi/Korelasi:
   - Hapus Timestamp video                   - Chi-Square (Topik vs Tipe Konten)
4. Case Folding (Lowercase semua)         4. Reduksi Kolom Non-Analitik
5. Filtering Stopwords (Opsional/NLP)
   └────────────────────────┬────────────────────────┘
                            │
                            ▼
              [ CLEAN PREPROCESSED DATASETS ]
       (dataset_video_clean.csv & dataset_komentar_clean.csv)
```

### Langkah Konkret Prapemrosesan:
1. **Data Cleaning (Komentar)**:
   - Menghapus 4 baris bernilai null (*ignore tuple*).
   - Menghapus karakter URL/link, mention `@`, tanda pagar `#`.
   - Menghapus emoji menggunakan pustaka `emoji` atau ekspresi reguler.
   - Menghapus timestamp berpola menit:detik (`\d+:\d+`).
   - Menyeragamkan teks ke huruf kecil (*case folding*).
2. **Data Reduction & Privacy Preservation**:
   - Menghapus kolom `author` demi perlindungan privasi data.
3. **Data Transformation & Normalization (Video)**:
   - Menerapkan **Min-Max Normalization** untuk memetakan metrik numerik (`view_count`, `like_count`, `comment_count`) ke rentang $[0, 1]$:
     $$v' = \frac{v - \min_A}{\max_A - \min_A}$$
   - Menerapkan **Z-Score Normalization** sebagai pembanding:
     $$v' = \frac{v - \bar{A}}{\sigma_A}$$
4. **Analisis Statistik & Outlier**:
   - Menghitung batas *whiskers* boxplot ($Q_1 - 1.5 \times IQR$ dan $Q_3 + 1.5 \times IQR$) untuk mencatat video dengan capaian penonton pencilan.

---

## 5. Kerangka Sistematika Makalah (Khusus Sampai Preprocessing)

1. **BAB I: PENDAHULUAN**
   - Latar belakang fenomena interaksi warganet terhadap isu kebijakan publik di YouTube.
   - Rumusan masalah dan batasan penelitian (fokus pada penyiapan data primer berkualitas).
2. **BAB II: AKUISISI DAN DESKRIPSI DATA PRIMER**
   - Metodologi pengumpulan data menggunakan YouTube Data API v3 dan RYD API.
   - Skema struktur tabel data mentah (*Data Profiling*).
   - Justifikasi pemilihan sampel (*Purposive Sampling*).
3. **BAB III: EKSPLORASI DATA AWAL (EXPLORATORY DATA ANALYSIS)**
   - Identifikasi tipe atribut (Nominal, Biner, Numerik Rasio).
   - Statistik deskriptif (*Mean, Median, Quartiles, IQR, Standar Deviasi*).
   - Identifikasi anomali, nilai kosong, dan sebaran derau pada teks.
4. **BAB IV: METODOLOGI DAN IMPLEMENTASI PRAPEMROSESAN DATA**
   - Pembersihan data hilang dan derau teks (*Data Cleaning*).
   - Preservasi privasi data (*Anonymization*).
   - Transformasi dan normalisasi numerik (*Min-Max / Z-Score Scaling*).
   - Tabel perbandingan kondisi data **Sebelum (*Before*) vs Sesudah (*After*) Preprocessing**.
5. **BAB V: KESIMPULAN DAN RENCANA ANALISIS LANJUTAN**
   - Evaluasi peningkatan kualitas data pasca-prapemrosesan.
   - Rencana pemodelan data mining lanjutan (misal: Klasifikasi Sentimen Teks, Klasterisasi Pola Engagement).

