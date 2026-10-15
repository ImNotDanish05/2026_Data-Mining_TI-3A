# Roadmap & Dokumentasi Target Luaran: Praktikum Mingguan & Jurnal UAS
**Mata Kuliah:** Data Mining (TI-3A)  
**Topik Terpilih (Disetujui Dosen):** Pemodelan Topik Opini Publik Program Makan Bergizi Gratis (MBG) Menggunakan Unsupervised Latent Dirichlet Allocation (LDA)  
**Pembaruan Terakhir:** 15 Oktober 2026  

---

## 📌 1. Klarifikasi Target & Garis Waktu (Timeline)

Proyek ini memiliki 2 tingkatan target luaran (*deliverables*) yang saling berkesinambungan:

```
[TARGET 1: MINGGU INI - 22 OKTOBER 2026]
Laporan Hasil Praktikum + Slide Presentasi Kelas + Google Colab
                         ⬇️ (Diverifikasi Dosen & Disempurnakan)
[TARGET 2: SEBELUM UAS - AKHIR SEMESTER]
2 Versi Naskah Artikel Jurnal Ilmiah (Versi SINTA 3 & Versi SINTA 2)
```

---

## 🎯 2. Target 1: Tugas Praktikum Mingguan (Batas Waktu: Kamis, 22 Oktober 2026)

Berdasarkan dokumen resmi panduan dosen (`informasi/catatan_pribadi/TUGAS PRAKTIKUM DATA MINING.docx`), praktikum ini menuntut pemenuhan Bab I s/d Bab V dengan rincian luaran:

### A. Komponen Wajib dari Dokumen Tugas:
1. **Bab I & II (Tujuan & Latar Belakang)**:
   - Analisis data multimedia/video YouTube untuk mengevaluasi interaksi warganet.
2. **Bab III & IV.1-2 (Dataset & Prapemrosesan)**:
   - Ekstraksi dataset 55 video (`dataset_video_clean.csv`) dan 5.207 komentar publik (`dataset_komentar_clean.csv`).
   - Normalisasi Min-Max dan Z-Score pada fitur interaksi.
3. **Bab IV.3 (Statistik Deskriptif)**:
   - Penghitungan metrik: *Mean*, *Variance*, *Standar Deviasi*, *Min*, dan *Max* untuk fitur interaksi video (`view_count`, `like_count`, `dislike_count_est`, `comment_count`, `engagement_rate`).
   - Telah dieksekusi sempurna di **Cell 6** Google Colab.
4. **Bab IV.6 (Deteksi Outlier & Boxplot)**:
   - Visualisasi Boxplot $1.5 \times IQR$ pada `view_count` dan `like_count` yang membuktikan adanya video viral berkategori outlier.
   - Telah dieksekusi sempurna di **Cell 6** Google Colab.
5. **Bab IV.4-5 (Pemodelan Unsupervised / Clustering Isu)**:
   - Dosen melarang keras penggunaan labeling (*no supervised labels*).
   - Pemodelan menggunakan **Unsupervised Topic Modeling LDA** dengan penalaan matematis *Topic Coherence* ($C_v$).
   - Hasil penalaan: $K=2$ adalah titik optimal puncak ($C_v = 0.3911$).
6. **Bab V (Hasil yang Diharapkan / Deliverables)**:
   - Tabel statistik deskriptif & Diagram Boxplot.
   - Visualisasi interaktif pyLDAvis (`visualisasi_lda_interaktif.html`).
   - Anotasi dominant topic pada 5.207 komentar (`hasil_topic_modeling_komentar.csv`).
   - Bar chart proporsi sebaran isu.
   - Narasi kesimpulan dan *insight* pola pembicaraan publik.
   - Model biner dan kamus biner (`lda_model.gensim*` & `lda_dictionary.dict` dalam `hasil_lda_lengkap.zip`).

### B. Bentuk Fisik Luaran untuk Tanggal 22 Oktober 2026:
* **Dokumen Laporan Praktikum (Word/PDF)**: Menjawab runut seluruh Bab I s/d V.
* **Slide Presentasi (PPT/PDF)**: Bahan tayang ringkas dan profesional untuk presentasi di hadapan dosen dan kelas.
* **Tautan Google Colab**: `Analisis_Data_Video_Topic_Modeling_LDA.ipynb` sebagai artefak komputasi primer.

---

## 🏆 3. Target 2: Naskah Artikel Jurnal Ilmiah (Sebelum UAS)

Pengguna menetapkan bahwa luaran akhir semester (sebelum UAS) adalah **Artikel Jurnal Ilmiah** resmi dengan 2 versi bertingkat:

### A. Versi 1: Naskah Standar Jurnal SINTA 3
* **Fokus**: Pemodelan Topik Opini Publik Program MBG Menggunakan Latent Dirichlet Allocation (LDA) Murni Tanpa Label.
* **Cakupan Utama**:
  1. Eksplorasi prapemrosesan teks bahasa Indonesia pada media sosial YouTube.
  2. Evaluasi koherensi semantik ($C_v$) untuk menentukan jumlah topik optimal ($K=2$).
  3. Pemetaan 2 kluster topik: Topik 0 (Mutu Makanan & Kasus Lapangan - 64.28%) vs Topik 1 (Tata Kelola Kebijakan & Prioritas Guru - 35.72%).
  4. Didukung oleh sitasi dari **20 jurnal ilmiah bereputasi** (`informasi/catatan/daftar_20_jurnal_pendukung.md`).

### B. Versi 2: Naskah Unggulan Jurnal SINTA 2 (Elevated Cross-Modal Analysis)
* **Fokus**: Analisis Komparasi Lintas-Modal (Cross-Modal): Pengaruh Framing Kemasan Media (Meme vs News vs Serious) terhadap Polarisasi Opini Publik.
* **Kebaruan Ilmiah (*Novelty*) & Pengujian Statistik**:
  1. Menghubungkan metadata kemasan video YouTube dengan topik dominan komentar hasil LDA.
  2. Tabulasi Silang (*Cross-Tabulation*):
     - **Meme (2.357 komentar)**: 72.85% membicarakan isu teknis/lapangan (keracunan, gizi, dapur).
     - **News (1.268 komentar)**: 65.93% membicarakan isu lapangan, 34.07% kebijakan.
     - **Serious / Analisis (1.582 komentar)**: Diskusi terbagi seimbang (50.25% isu lapangan vs 49.75% tata kelola anggaran & kesejahteraan guru).
  3. **Uji Independensi Statistik Chi-Square ($\chi^2$)**:
     - $\chi^2 = 212.4579$
     - Derajat Kebebasan ($df$) = $2$
     - Nilai $p < 0.0001$ ($7.33 \times 10^{-47}$)
     - Kesimpulan: Terbukti secara empiris dan signifikan bahwa format kemasan media mengarahkan agenda dan framing pembicaraan masyarakat (*Agenda-Setting & Framing Theory*).
  4. Script otomasi siap pakai: [`analisis_komparasi_framing_sinta2.py`](file:///media/data1/project/kuliah/2026_Data-Mining_TI-3A/analisis_komparasi_framing_sinta2.py) dan gambar visualisasi HD 300 DPI (`komparasi_framing_media_sinta2.png`).

---

## 🔒 4. Batasan & Aturan Ketat (Constraints & Rules)

1. **Dilarang Keras Melakukan Supervised Labeling**:
   - Dosen melarang anotasi label manual/buatan untuk training model tugas ini. Seluruh pipeline wajib *pure unsupervised*.
2. **Perlindungan Aset Data Lama**:
   - File `data/processed/dataset_komentar_labeled.csv` (berisi 5.207 label sentimen Indo-RoBERTa 88.7% confidence) **DILARANG DIHAPUS ATAU DITIMPA**. Aset ini dilindungi sebagai cadangan riset mandiri.
3. **Privasi & Keamanan Hukum (PPDM / UU PDP)**:
   - Seluruh data yang diunggah ke publik (`data/public/`) telah 100% di-anonimkan (tanpa nama akun, tanpa mention @, tanpa URL, tanpa nomor kontak).
   - Peneliti dilindungi oleh UU Dikti Pasal 8-9 (Kebebasan Akademik), UU PDP Pasal 15, UU ITE Pasal 27A, KUHP Pasal 218 ayat 2, dan UU Hak Cipta Pasal 44.
4. **Kerahasiaan Catatan Pribadi**:
   - Folder `informasi/catatan_pribadi/` dan semua file `*.docx` wajib tetap berada di dalam `.gitignore` dan tidak boleh di-push ke GitHub publik.

