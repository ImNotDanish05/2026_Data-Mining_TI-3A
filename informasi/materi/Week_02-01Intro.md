# Materi Pembelajaran: Pengantar Data Mining (Introduction to Data Mining)

Materi ini membahas konsep dasar, proses penemuan pengetahuan (*Knowledge Discovery in Databases*), fungsionalitas, teknologi pendukung, serta tantangan utama dalam bidang Data Mining.

---

## 1. Mengapa Perlu Data Mining? (*Why Data Mining?*)

### 1.1 Ledakan Pertumbuhan Data (*Explosive Growth of Data*)
- **Perkembangan Volume**: Terjadi eksponensial data dari skala gigabyte, terabyte, hingga petabyte dan exabyte.
- **Sumber Data Melimpah**:
  - *Bisnis & E-Commerce*: Transaksi ritel, riwayat pembelian, perbankan, pasar modal.
  - *Sains & Riset*: Penginderaan jauh (*remote sensing*), bioinformatika, simulasi iklim, genomika.
  - *Masyarakat Digital*: Media sosial, artikel berita, video streaming, sensor IoT.
- **Kondisi Utama**: *"We are drowning in data, but starving for knowledge!"* (Tenggelam dalam lautan data, namun haus akan pengetahuan).
- **Kebutuhan**: Analisis data secara manual tidak lagi memungkinkan, sehingga diperlukan otomatisasi analisis kumpulan data masif (*Data Mining*).

### 1.2 Evolusi Pendekatan Sains
1. **Sains Empiris (Sebelum 1600)**: Berbasis observasi fenomena alam langsung.
2. **Sains Teoretis (1600–1950-an)**: Pemodelan matematis, hukum fisika, dan generalisasi teoretis.
3. **Sains Komputasional (1950-an–1990-an)**: Simulasi fenomena kompleks menggunakan pemrograman dan komputer.
4. **Sains Berbasis Data (*Data-Intensive Science / The 4th Paradigm*)**: Eksplorasi, penambangan pola, dan integrasi data masif untuk menemukan wawasan baru.

### 1.3 Evolusi Teknologi Database Menuju Data Mining
- **1960-an**: Pengumpulan data awal, sistem manajemen berkas, DBMS jaringan dan hierarkis (IMS).
- **1970-an**: Model data relasional oleh E.F. Codd, implementasi RDBMS, standarisasi SQL.
- **1980-an**: RDBMS tingkat lanjut (Object-Oriented DBMS, Deductive DBMS), database berorientasi aplikasi.
- **1990-an**: *Data Warehousing*, Online Analytical Processing (OLAP), penambangan data (*Data Mining*), database web.
- **2000-an–Sekarang**: Big Data, manajemen aliran data (*Data Streams*), analisis jejaring sosial, *Cloud Computing*, dan penambangan data terdistribusi.

---

## 2. Definisi Data Mining & Proses KDD

### 2.1 Apa itu Data Mining?
> **Data Mining** adalah proses penemuan pola atau pengetahuan yang menarik (*interesting*), non-trivial, implisit, sebelumnya belum diketahui, dan berpotensi bermanfaat dari sekumpulan data berukuran masif.

- **Nama Lain / Bidang Terkait**:
  - *Knowledge Discovery from Data (KDD)*
  - *Knowledge Extraction*
  - *Data / Pattern Analysis*
  - *Information Harvesting*
  - *Business Intelligence (BI)*
- **Bukan Data Mining**:
  - Pencarian informasi sederhana via SQL (*deductive query processing*), misal: mencari nomor telepon seseorang.
  - Sistem berbasis aturan statis (*expert systems / deductive rule execution*).

### 2.2 Tahapan Proses KDD (*Knowledge Discovery in Databases*)

Data Mining merupakan langkah inti dari keseluruhan alur KDD:

```
[ Raw Data Sources ]
        │
        ▼ 1. Data Cleaning (membersihkan data kotor/noise)
        ▼ 2. Data Integration (menggabungkan sumber data beragam)
[ Integrated Data / Data Warehouse ]
        │
        ▼ 3. Data Selection (memilih subset data relevan)
        ▼ 4. Data Transformation (normalisasi, agregasi)
[ Transformed Data ]
        │
        ▼ 5. Data Mining (ekstraksi pola menggunakan algoritma cerdas)
[ Patterns ]
        │
        ▼ 6. Pattern Evaluation (evaluasi pola berdasarkan nilai kemenarikan)
[ Knowledge ]
        │
        ▼ 7. Knowledge Presentation (visualisasi dan representasi wawasan)
[ Decision Making ]
```

### 2.3 Data Mining dalam Business Intelligence (BI)
Arsitektur penunjang keputusan bisnis tersusun secara berjenjang:
1. **Data Sources**: Dokumen operasional, berkas log, sistem OLTP.
2. **Data Integration & Warehousing**: Penggabungan data historis ke *Data Warehouse / Data Mart*.
3. **Data Exploration & OLAP**: Laporan berkala, analisis multidimensi, agregasi ringkas (*slicing & dicing*).
4. **Data Mining & Predictive Modeling**: Pemodelan prediktif lanjutan, segmentasi, klasifikasi, deteksi tren.
5. **Presentation & Decision Making**: Dashboard analitik interaktif untuk eksekutif/pengambil keputusan.

---

## 3. Sudut Pandang Multi-Dimensi Data Mining

Data mining dapat diklasifikasikan berdasarkan beberapa dimensi utama:
1. **Berdasarkan Jenis Data yang Ditambang**:
   - Data Relasional, *Data Warehouse*, Data Transaksional.
   - Data Lanjutan: Data runtun waktu (*time-series*), aliran data (*streams*), spasial & spatiotemporal, teks, multimedia, graf & web.
2. **Berdasarkan Pola/Pengetahuan yang Dihasilkan**:
   - Karakterisasi dan diskriminasi.
   - Pola frekuensi tinggi, asosiasi, korelasi.
   - Klasifikasi dan regresi.
   - Analisis klaster (*clustering*).
   - Analisis pencilan (*outlier analysis*).
3. **Berdasarkan Teknik yang Digunakan**:
   - Pembelajaran mesin (*Machine Learning*), Statistik, Sistem Database, Pengambilan Informasi (*Information Retrieval*), Visualisasi.
4. **Berdasarkan Aplikasi Sasaran**:
   - Ritel, telekomunikasi, keuangan/perbankan, deteksi penipuan (*fraud detection*), kesehatan, dan analisis medis.

---

## 4. Jenis-Jenis Data yang Dapat Ditambang

1. **Database Relasional (*Relational Databases*)**:
   - Kumpulan tabel dengan entitas, atribut, dan relasi (*primary key & foreign key*).
2. **Data Warehouse**:
   - Repositori informasi terpusat yang bersifat *subject-oriented, integrated, time-variant, non-volatile* untuk mendukung pengambilan keputusan. Menggunakan struktur skema bintang (*star*), kepingan salju (*snowflake*), dan kubus data multidimensi (*Data Cubes*).
3. **Database Transaksional (*Transactional Databases*)**:
   - Berisi catatan transaksi yang mencakup ID transaksi dan daftar item yang terlibat (misal data keranjang belanja kasir).
4. **Tipe Data Kompleks & Mutakhir**:
   - *Time-Series & Temporal Data*: Data finansial pergerakan saham, riwayat sensor.
   - *Data Streams*: Aliran data kontinu real-time (jaringan komputer, klik web).
   - *Spatial & Spatiotemporal Data*: Peta geografis, rute GPS navigasi.
   - *Text & Multimedia Data*: Dokumen teks bebas, gambar, audio, rekaman video.
   - *Graph & Network Data*: Jaringan pertemanan media sosial, struktur web link (hyperlink).
   - *World Wide Web*: Konten web dinamis dan data akses log.

---

## 5. Fungsionalitas Data Mining (Jenis Pola yang Ditambang)

Fungsionalitas data mining dibedakan menjadi dua kategori utama:
- **Tugas Deskriptif (*Descriptive Tasks*)**: Menggambarkan sifat dan karakteristik umum dari data yang ada.
- **Tugas Prediktif (*Predictive Tasks*)**: Melakukan inferensi pada data saat ini untuk memprediksi nilai atau label di masa depan.

### 5.1 Deskripsi Konsep/Kelas: Karakterisasi dan Diskriminasi
- **Karakterisasi Data (*Data Characterization*)**: Meringkas sifat-sifat umum dari kelas data sasaran (*target class*), misal profil rata-rata pelanggan yang loyal.
- **Diskriminasi Data (*Data Discrimination*)**: Membandingkan karakteristik kelas sasaran dengan satu atau beberapa kelas pembanding (*contrasting classes*), misal membandingkan pembeli laptop premium vs laptop ekonomis.

### 5.2 Pola Berulang, Asosiasi, dan Korelasi (*Frequent Patterns, Associations, Correlations*)
- **Pola Berulang (*Frequent Patterns*)**: Itemset, sekuens, atau substruktur yang sering muncul bersamaan dalam data.
- **Aturan Asosiasi (*Association Rules*)**:
  Menghubungkan kemunculan satu item dengan item lainnya, dinotasikan dengan:
  $$X \Rightarrow Y \quad [\text{support}, \text{confidence}]$$
  
  - **Support**: Persentase transaksi yang memuat kedua himpunan item $X$ dan $Y$.
    $$\text{Support}(X \Rightarrow Y) = P(X \cup Y)$$
  - **Confidence**: Probabilitas bersyarat bahwa transaksi yang memuat $X$ juga memuat $Y$.
    $$\text{Confidence}(X \Rightarrow Y) = P(Y \mid X) = \frac{P(X \cup Y)}{P(X)}$$
  - *Contoh*: $\text{beli}(X, \text{"Laptop"}) \Rightarrow \text{beli}(X, \text{"Mouse"}) \quad [\text{support} = 2\%, \text{confidence} = 60\%]$.

### 5.3 Klasifikasi dan Regresi (*Classification & Regression*)
- **Klasifikasi (*Classification*)**:
  - Membangun model (fungsi) untuk memprediksi label kelas diskrit/kategorikal.
  - *Contoh*: Menentukan status pengajuan pinjaman bank (*Disetujui* vs *Ditolak*), deteksi email (*Spam* vs *Bukan Spam*).
  - *Metode*: Pohon Keputusan (*Decision Tree*), Naïve Bayes, Support Vector Machines (SVM), Neural Networks, k-Nearest Neighbors (k-NN).
- **Regresi (*Regression*)**:
  - Memprediksi nilai numerik kontinu yang belum diketahui atau hilang.
  - *Contoh*: Memprediksi harga rumah, estimasi volume penjualan tahun depan.
  - *Metode*: Regresi Linier, Regresi Non-linier, Regresi Logistik.

### 5.4 Analisis Klaster (*Cluster Analysis / Clustering*)
- Pembelajaran tanpa pengawasan (*Unsupervised Learning*): Data tidak memiliki label kelas awal.
- Mengelompokkan objek data berdasarkan prinsip kemiripan:
  - **Memaksimalkan kemiripan intra-klaster**: Objek dalam satu kelompok memiliki kemiripan yang sangat tinggi.
  - **Meminimalkan kemiripan inter-klaster**: Objek antar kelompok berbeda memiliki ketidaksamaan yang signifikan.
- *Contoh*: Segmentasi pasar pelanggan baru.

### 5.5 Analisis Pencilan (*Outlier Analysis / Anomaly Detection*)
- Mengidentifikasi objek data yang perilakunya menyimpang secara signifikan dari mayoritas data lainnya.
- Meskipun sering dianggap *noise*, pencilan sangat penting untuk aplikasi tertentu:
  - Deteksi kecurangan transaksi kartu kredit (*fraud detection*).
  - Deteksi intrusi keamanan jaringan komputer.
  - Pemantauan anomali sensor medis atau peralatan pabrik.

---

## 6. Kriteria Pola yang Menarik (*Pattern Interestingness*)

Tidak semua pola yang dihasilkan data mining bernilai. Sebuah pola dikatakan **menarik (*interesting*)** jika:
1. **Mudah Dipahami**: Dapat diinterpretasikan oleh manusia.
2. **Valid**: Tetap terbukti benar pada data baru/pengujian dengan tingkat kepastian tertentu.
3. **Bermanfaat**: Memiliki potensi nilai guna untuk aksi nyata (*actionable*).
4. **Novel / Baru**: Memberikan wawasan baru yang belum diketahui sebelumnya atau menentang hipotesis awal pengguna.

Ukuran kemenarikan dibedakan menjadi:
- **Ukuran Objektif**: Berbasis statistik dan struktur data (misal: *support*, *confidence*, korelasi).
- **Ukuran Subjektif**: Berbasis perspektif pengguna (misal: *unexpectedness* / ketidakterdugaan, *actionability*).

---

## 7. Teknologi Pendukung Data Mining

Data Mining adalah bidang multidisipliner yang menggabungkan:
- **Statistik**: Landasan pengujian hipotesis, distribusi probabilitas, dan inferensi numerik.
- **Machine Learning**: Algoritma pembelajaran berbasis data dan penyesuaian parameter mandiri.
- **Sistem Database & Data Warehousing**: Manajemen penyimpanan data efisien, pengindeksan, optimasi query, dan OLAP.
- **Information Retrieval (IR)**: Temu kembali informasi dan penambangan teks.
- **Visualisasi Data**: Representasi visual untuk eksplorasi dan verifikasi wawasan.
- **Komputasi Paralel & Terdistribusi**: Penskalaan pemrosesan data bervolume masif.

---

## 8. Isu dan Tantangan Utama dalam Data Mining

1. **Metodologi Penambangan dan Interaksi Pengguna**:
   - Menambang beragam tipe pengetahuan dalam format fleksibel.
   - Penggabungan pengetahuan domain (*domain knowledge*).
   - Bahasa query penambangan data ad-hoc dan eksplorasi interaktif.
   - Penanganan ketidakpastian dan data derau (*noisy data*).
2. **Kinerja, Skalabilitas, dan Efisiensi**:
   - Efisiensi algoritma terhadap data berukuran raksasa.
   - Algoritma terdistribusi, paralel, dan inkremental (*streaming updates*).
3. **Keberagaman Tipe Data Kompleks**:
   - Menangani data non-relasional: multimedia, teks tidak terstruktur, spasial, jaringan web.
4. **Dampak Sosial dan Etika**:
   - *Privacy-Preserving Data Mining*: Menjaga privasi data individu dan kerahasiaan identitas.
   - Keamanan data dan keadilan algoritmik (*fairness/non-discrimination*).

