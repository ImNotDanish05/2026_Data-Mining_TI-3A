# Usulan 5 Topik Penelitian & Analisis Data Mining

Dokumen ini memuat 5 rancangan usulan topik penelitian untuk tugas mata kuliah **Data Mining (TI-3A)**. Seluruh topik dirancang agar memanfaatkan aset dataset primer yang telah dikumpulkan, dibersihkan (*clean*), dan dilabeli secara mandiri.

---

## 📌 Modal Aset Dataset yang Tersedia

1. **Dataset Video (`data/processed/dataset_video_clean.csv`)**:
   - 55 video YouTube (29 topik `MBG`, 26 topik `PrabowoSubianto`).
   - 3 kategori format media (`Meme`: 24, `Serious`: 16, `News`: 15).
   - Metrik keterlibatan: *view_count*, *like_count*, *dislike_count_est* (dari RYD API), *comment_count*, *duration_seconds*, normalisasi Min-Max & Z-Score, deteksi pencilan (IQR).
2. **Dataset Komentar (`data/processed/dataset_komentar_labeled.csv`)**:
   - 5.207 komentar warganet (tanpa *missing values*, teks dibersihkan dari emoji, URL, tanda baca berlebih).
   - Label sentimen/sikap hasil klasifikasi model *Transformer* Indo-RoBERTa (`w11wo/indonesian-roberta-base-sentiment-classifier`) dengan rata-rata keyakinan (*confidence*) **88,73%**:
     - **Menolak / Kritis**: 3.495 baris (67,12%)
     - **Netral**: 1.011 baris (19,42%)
     - **Mendukung**: 701 baris (13,46%)
3. **Dataset Transkrip Wicara (`data/raw/dataset_transkrip_video.csv` & `video_transcripts.json`)**:
   - 55 teks transkrip lengkap narasi video dengan total **134.986 kata**.
4. **Landasan Teoretis & Akademis (`informasi/catatan/daftar_20_jurnal_pendukung.md`)**:
   - 20 artikel jurnal ilmiah terakreditasi SINTA dan Scopus beserta DOI resmi.

> 🏆 **STATUS TOPIK**: **PILIHAN RESMI DOSEN (APPROVED) ⭐⭐⭐⭐⭐**  
> 📅 **TANGGAL PRESENTASI**: **Kamis, 22 Oktober 2026**  
> ⚠️ **CATATAN KHUSUS DOSEN**: Dosen melarang keras penggunaan labeling (*no supervised labels*). Model diwajibkan menggunakan **Unsupervised NLP (Topic Modeling - LDA)** untuk menemukan tema dan isu secara mandiri dari data.

---

## 🌟 1. Topik 1: Pemodelan Topik (Topic Modeling) Opini Publik terhadap Kebijakan Makan Bergizi Gratis (MBG) Menggunakan Algoritma Unsupervised NLP (Latent Dirichlet Allocation / LDA)

### A. Deskripsi & Konsep Utama
Menganalisis kecenderungan isu, kritik, dan aspirasi masyarakat Indonesia di kolom komentar YouTube terhadap program Makan Bergizi Gratis (MBG) secara **murni tanpa label (*Unsupervised NLP*)**. Model secara probabilistik membedah 5.207 komentar bersih untuk menemukan kelompok tema tersembunyi (*latent topics*) seperti isu kualitas/keamanan pangan, isu kebocoran anggaran/korupsi, serta isu prioritas pendidikan.

### B. Rumusan Masalah (Research Questions)
1. Topik-topik substantif dan klaster isu apa saja yang diekstraksi secara otomatis oleh algoritma Latent Dirichlet Allocation (LDA) dari 5.207 komentar masyarakat?
2. Berapa proporsi distribusi pembicaraan publik pada masing-masing topik isu utama tersebut?
3. Berdasarkan evaluasi *Topic Coherence Score ($C_v$)*, seberapa optimal jumlah topik ($K$) dalam merepresentasikan opini masyarakat secara kohesif?

### C. Atribut & Metodologi Data Mining
- **Data yang Digunakan**: `dataset_komentar_clean.csv` (5.207 komentar teks bersih, tanpa kolom label kelas).
- **Atribut Kunci**: `comment_text_clean`, `comment_likes`, `topik_video`.
- **Metode**: Natural Language Processing (NLP), N-Gram Tokenization, Indonesian Stopwords Filtering, Dictionary & Bag-of-Words (BoW) Corpus, Algoritma **Latent Dirichlet Allocation (LDA)**, Evaluasi *Topic Coherence ($C_v$)*.
- **Visualisasi**: Peta semantik interaktif **pyLDAvis** (HTML browser), Diagram lingkaran proporsi topik isu, Word Cloud kata kunci per topik.

### D. Keunggulan Akademis di Depan Dosen
- **Sesuai 100% dengan Arahan Dosen**: Murni tanpa pelabelan (*zero manual/pseudo labeling*), menjunjung tinggi integritas analisis data-driven.
- **Kekuatan Teori Probabilistik**: Menggunakan model Bayesian hierarkis 3 tingkat (Dirichlet Prior) yang sangat berbobot untuk ujian Data Mining.
- **Tingkat Kesulitan**: ⭐⭐ (Rendah–Sedang; data teks sudah bersih dan siap dikonversi ke Bag-of-Words).

---

## 2. Topik 2: Pengaruh Framing Konten Media (*News* vs *Serious Opinion* vs *Meme/Satir*) terhadap Sentimen dan Keterlibatan Publik

### A. Deskripsi & Konsep Utama
Mengkaji pengaruh format pembawaan informasi (*media framing*) terhadap reaksi psikologis dan sentimen audiens. Membandingkan apakah kanal berita formal (*News*), kanal opini kritis/edukasi (*Serious*), dan kanal komedi/satir (*Meme*) memicu tingkat penolakan dan interaksi (*engagement rate*) yang berbeda secara signifikan di kalangan warganet.

### B. Rumusan Masalah (Research Questions)
1. Apakah terdapat perbedaan signifikan proporsi penolakan warganet antara video berita konvensional (*News*), opini mendalam (*Serious*), dan konten hiburan (*Meme*)?
2. Format konten mana yang paling efektif memicu diskusi intensif (diukur dari metrik `total_replies` dan `comment_count`)?
3. Bagaimana interaksi antara tipe konten dengan tingkat kesukaan audiens (*like/dislike ratio*)?

### C. Atribut & Metodologi Data Mining
- **Data yang Digunakan**: Relasi gabungan `dataset_video_clean.csv` dan `dataset_komentar_labeled.csv`.
- **Atribut Kunci**: `tipe_video` (*Meme*, *News*, *Serious*), `sentimen`, `dislike_ratio`, `engagement_rate`, `comment_likes`, `total_replies`.
- **Metode**: Tabulasi Silang (*Cross-Tabulation Analysis*), Uji Independensi Chi-Square ($\chi^2$), Analisis Korelasi Spearman / Pearson, Analisis Multivariat.
- **Visualisasi**: *Grouped Bar Chart* sentimen per tipe konten, *Heatmap* korelasi format video vs sentimen, *Boxplot* distribusi balasan komentar per tipe konten.

### D. Keunggulan Akademis di Depan Dosen
- **Orisinalitas Tinggi**: Sangat jarang mahasiswa yang mengkaji korelasi antara format kemasan video dengan reaksi warganet di kolom komentar.
- **Kedalaman Statistik**: Memadukan data penambangan teks (*text mining*) dengan uji hipotesis statistik formal.
- **Tingkat Kesulitan**: ⭐⭐ (Rendah–Sedang; data atribut sudah lengkap terintegrasi).

---

## 3. Topik 3: Prediksi Tingkat Resistensi Penonton (*Dislike Ratio*) pada Video Kebijakan Publik Menggunakan Algoritma *Supervised Machine Learning*

### A. Deskripsi & Konsep Utama
Membangun model prediktif berbasis *Machine Learning* untuk memperkirakan rasio ketidaksukaan publik (*dislike ratio* atau estimasi resistensi audiens) terhadap suatu video kebijakan publik. Prediksi dilakukan berdasarkan kombinasi fitur teknis video (durasi, intensitas tontonan, saluran pembuat) dan karakteristik respons komentar.

### B. Rumusan Masalah (Research Questions)
1. Fitur video manakah yang memiliki bobot pengaruh paling dominan (*feature importance*) terhadap tingginya rasio *dislike* penonton?
2. Algoritma pembelajaran mesin manakah yang memberikan performa estimasi paling akurat antara Random Forest Regressor, Support Vector Regression (SVR), dan Linear Regression?
3. Seberapa besar kontribusi proporsi komentar negatif dalam meningkatkan ketepatan prediksi resistensi video?

### C. Atribut & Metodologi Data Mining
- **Data yang Digunakan**: `dataset_video_clean.csv` yang diagregasikan dengan rasio sentimen dari `dataset_komentar_labeled.csv`.
- **Atribut Kunci (Fitur X)**: `duration_seconds`, `views_per_day`, `topik_video`, `tipe_video`, persentase komentar `Menolak`, persentase komentar `Mendukung`.
- **Target (Label Y)**: `dislike_ratio` (atau `raw_dislikes_ryd`).
- **Metode**: Data Splitting (80:20 Train-Test / K-Fold Cross Validation), Algoritma Regresi (*Random Forest*, *SVR*, *Ridge Regression*), Metrik Evaluasi (*MAE*, *RMSE*, $R^2$ *Score*).
- **Visualisasi**: Scatter plot aktual vs prediksi, diagram batang *Feature Importance*, kurva konvergensi residu error.

### D. Keunggulan Akademis di Depan Dosen
- **Karakter Data Mining Klasik**: Sangat disukai dosen penguji beraliran teknis karena menerapkan siklus lengkap *Supervised Learning* (pelatihan, pengujian, evaluasi metrik kesalahan).
- **Tingkat Kesulitan**: ⭐⭐⭐ (Sedang; memerlukan skrip pelatihan model regresi `scikit-learn`).

---

## 4. Topik 4: Komparasi Kinerja Algoritma Klasifikasi Sentimen Teks Opini Publik Bahasa Indonesia (Naïve Bayes vs SVM vs Indo-RoBERTa)

### A. Deskripsi & Konsep Utama
Melakukan studi komparatif *benchmarking* antara algoritma penambangan teks konvensional berbasis frekuensi (*TF-IDF*) dengan arsitektur berbasis *Deep Learning Transformer*. Fokus komparasi dititikberatkan pada kemampuan masing-masing model dalam menangani gaya bahasa informal, singkatan, sarkasme, dan *slang* khas media sosial Indonesia.

### B. Rumusan Masalah (Research Questions)
1. Bagaimana perbandingan performa akurasi, *Precision*, *Recall*, dan *F1-Score* antara Multinomial Naïve Bayes, Support Vector Machine (Linear SVM), dan Indo-RoBERTa pada klasifikasi komentar YouTube?
2. Bagaimana perbandingan efisiensi sumber daya komputasi (*training/inference time* dan *memory usage*) antar ketiga algoritma tersebut pada lingkungan perangkat keras standar (CPU)?
3. Jenis kesalahan klasifikasi (*misclassification error*) apa yang paling sering terjadi pada model tradisional akibat karakteristik teks informal warganet?

### C. Atribut & Metodologi Data Mining
- **Data yang Digunakan**: `dataset_komentar_clean.csv` dan label validasi `dataset_komentar_labeled.csv`.
- **Atribut Kunci**: `comment_text_clean`, `sentimen`.
- **Metode**: Ekstraksi Fitur TF-IDF (Unigram + Bigram), Klasifikasi *Multinomial Naïve Bayes*, Klasifikasi *Support Vector Classifier (SVC)*, Evaluasi *Confusion Matrix*, Pengukuran *Inference Latency* (detik/sampel).
- **Visualisasi**: Matriks kebingungan (*Confusion Matrix Heatmap*), diagram batang komparasi metrik evaluasi (F1-Score), grafik perbandingan kecepatan eksekusi.

### D. Keunggulan Akademis di Depan Dosen
- **Sangat Aman saat Ujian Sidang**: Format laporan perbandingan algoritma merupakan standar emas tugas akademik data mining yang paling mudah dipertanggungjawabkan ke dosen penguji.
- **Tingkat Kesulitan**: ⭐⭐⭐ (Sedang; tinggal membuat skrip komparasi `scikit-learn` untuk Naive Bayes & SVM).

---

## 5. Topik 5: Analisis Kesenjangan Isu (*Agenda-Setting Gap*) antara Narasi Konten Video (Transkrip) dan Persepsi Publik (Komentar) Menggunakan *Topic Modeling* (LDA)

### A. Deskripsi & Konsep Utama
Memanfaatkan aset data multimodal (transkrip wicara video dan teks komentar publik) untuk menganalisis apakah percakapan masyarakat di kolom komentar selaras dengan substansi yang disampaikan oleh narasumber/pembuat video, ataukah publik mengalami bias agenda politik (membahas topik di luar konteks video, seperti polarisasi pilpres, dinasti politik, atau isu personal figur).

### B. Rumusan Masalah (Research Questions)
1. Topik-topik substantif apa saja yang diekstraksi dari narasi transkrip video 55 narasumber (134.986 kata) menggunakan algoritma *Latent Dirichlet Allocation (LDA)*?
2. Topik-topik apa saja yang paling dominan muncul dari 5.207 komentar tanggapan warganet?
3. Seberapa besar tingkat kesenjangan atau pergeseran isu (*thematic divergence/gap*) antara pesan yang disampaikan video dengan respons yang diberikan warganet?

### C. Atribut & Metodologi Data Mining
- **Data yang Digunakan**: `dataset_transkrip_video.csv` (134.986 kata) dan `dataset_komentar_labeled.csv` (5.207 komentar).
- **Atribut Kunci**: `transcript_text`, `comment_text_clean`, `topik_video`.
- **Metode**: *Latent Dirichlet Allocation (LDA)* atau *NMF (Non-negative Matrix Factorization)*, Perhitungan Skor *Topic Coherence* ($C_v$), Perhitungan *Cosine Similarity* distribusi topik transkrip vs komentar.
- **Visualisasi**: Visualisasi interaktif pyLDAvis, diagram perbandingan distribusi bobot topik (Video vs Komentar).

### D. Keunggulan Akademis di Depan Dosen
- **Bobot Akademis Tertinggi**: Merupakan pendekatan paling mutakhir yang sangat berpotensi diterbitkan menjadi artikel jurnal ilmiah bereputasi (SINTA 2 / Scopus).
- **Pemanfaatan Maksimal Aset Data**: Menjadikan seluruh data ekstraksi transkrip wicara berfungsi optimal dalam penelitian.
- **Tingkat Kesulitan**: ⭐⭐⭐⭐ (Tinggi; memerlukan penalaan jumlah topik optimal $K$ dan evaluasi koherensi teks).

---

## 📊 Matriks Perbandingan Ringkas 5 Pilihan Topik

| No | Judul / Fokus Topik | Kategori Data Mining | Algoritma Utama | Sumber Data Kunci | Tingkat Kesulitan | Rekomendasi Utama |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- |
| **1** | **Polarisasi Sentimen Kebijakan MBG** | *Text Mining & NLP* | Indo-RoBERTa, N-Gram, TF-IDF | Komentar (5.207) | ⭐⭐ (Mudah) | **Paling Cepat & Relevan** (Data sudah 100% siap) |
| **2** | **Pengaruh Framing Format Konten Media** | *Cross-Modal Mining & Statistik* | Tabulasi Silang, Chi-Square, Korelasi | Komentar + Video Meta | ⭐⭐ (Mudah) | **Paling Unik & Segar** (Menghubungkan format vs respons) |
| **3** | **Prediksi Dislike Ratio Video Politik** | *Supervised Regression* | Random Forest, SVR, Linear Regression | Video Meta + Agregasi Sentimen | ⭐⭐⭐ (Sedang) | **Paling Cocok Dosen Teknis** (Ada metrik RMSE, R²) |
| **4** | **Komparasi Algoritma Sentimen Teks** | *Benchmarking Data Mining* | Naïve Bayes, SVM, Indo-RoBERTa | Komentar Berlabel | ⭐⭐⭐ (Sedang) | **Paling Aman untuk Sidang** (Tabel komparasi formal) |
| **5** | **Analisis Kesenjangan Isu Transkrip vs Komentar** | *Topic Modeling & Clustering* | Latent Dirichlet Allocation (LDA) | Transkrip (134k kata) + Komentar | ⭐⭐⭐⭐ (Tinggi) | **Level Skripsi / Jurnal Ilmiah** (Inovasi tertinggi) |

---

## 💡 Rekomendasi Langkah Danish:

1. **Jalur Paling Cepat & Bernilai Tinggi (Sangat Direkomendasikan):**
   > Gabungkan **Topik 1 dan Topik 2** menjadi:
   > *"Analisis Sentimen dan Pengaruh Framing Format Media terhadap Polarisasi Opini Publik Kebijakan Makan Bergizi Gratis Menggunakan Indo-RoBERTa"*.
   > *Alasan:* Seluruh data sudah selesai 100%, visualisasinya kaya, dan pembahasannya sangat komprehensif.

2. **Jalur Akademik Formal (Jika Dosen Mengharuskan Perbandingan Model):**
   > Ambil **Topik 4** (*Komparasi Naive Bayes vs SVM vs Indo-RoBERTa*). Dosen mata kuliah Data Mining sangat suka melihat tabel *Accuracy, Precision, Recall, F1-Score* yang membandingkan metode klasik vs *deep learning*.

