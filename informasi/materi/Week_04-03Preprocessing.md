# Materi Pembelajaran: Prapemrosesan Data (Data Preprocessing)

Materi ini membahas prinsip dasar kualitas data serta empat pilar utama dalam prapemrosesan data: pembersihan data (*data cleaning*), integrasi data (*data integration*), reduksi data (*data reduction*), dan transformasi serta diskretisasi data (*data transformation & discretization*).

---

## 1. Urgensi Prapemrosesan Data & Dimensi Kualitas Data

### 1.1 Mengapa Data Perlu Diproses Awal?
Data mentah di dunia nyata pada umumnya berkualitas buruk (*dirty data*):
- **Tidak Lengkap (*Incomplete*)**: Nilai atribut hilang (*missing values*), hanya berisi data agregat, atau atribut penting belum tercatat.
- **Mengandung Derau (*Noisy*)**: Terdapat kesalahan pencatatan, galat pengukuran (*error*), atau nilai pencilan (*outliers*).
- **Tidak Konsisten (*Inconsistent*)**: Perbedaan format, kodefikasi ganda, atau pelanggaran integritas (misal: data umur tertera 42 tahun, namun tahun lahir tertera 2015).
- **Redundan (*Redundant*)**: Duplikasi data antar-sumber yang berbeda.

> **Prinsip Utama**: *"Garbage In, Garbage Out"* (GIGO). Kualitas hasil penambangan data dan akurasi model prediktif berbanding lurus dengan kualitas data masukan.

### 1.2 Dimensi Kualitas Data (*Measures for Data Quality*)
1. **Akurasi (*Accuracy*)**: Kebenaran nilai data terhadap fakta riil.
2. **Kelengkapan (*Completeness*)**: Ketersediaan seluruh nilai atribut yang dibutuhkan tanpa kekosongan data krusial.
3. **Konsistensi (*Consistency*)**: Keseragaman representasi dan tiadanya pertentangan logika data antar-tabel/sistem.
4. **Ketepatan Waktu (*Timeliness*)**: Pembaruan data terjadi secara berkala dan tepat waktu saat dibutuhkan.
5. **Dapat Dipercaya (*Believability*)**: Tingkat kepercayaan pengguna terhadap integritas dan validitas sumber data.
6. **Keterpahaman (*Interpretability*)**: Kemudahan representasi data untuk dipahami oleh analis dan algoritma.

---

## 2. Pembersihan Data (*Data Cleaning*)

### 2.1 Penanganan Nilai Hilang (*Missing Values*)
Metode penanganan data kosong meliputi:
1. **Abaikan Tupel (*Ignore the Tuple*)**: Menghapus baris yang memiliki nilai kosong. Sering digunakan jika yang hilang adalah label kelas (*class label*), namun berisiko membuang informasi berharga jika persentase data hilang cukup besar.
2. **Pengisian Manual (*Manual Imputation*)**: Dilakukan oleh ahli domain. Sangat akurat namun tidak layak (*infeasible*) untuk data berskala besar.
3. **Pengisian Otomatis**:
   - Menggunakan konstanta global (misal: `"Unknown"` atau $\infty$).
   - Menggunakan nilai rata-rata (*mean*) atau median dari atribut tersebut.
   - Menggunakan nilai rata-rata/median atribut untuk seluruh sampel dalam kelas yang sama (lebih akurat untuk klasifikasi).
   - Menggunakan nilai paling mungkin (*most probable value*): Mengestimasi menggunakan regresi, Naïve Bayes, pohon keputusan, atau algoritma *Expectation-Maximization (EM)*.

---

### 2.2 Penanganan Data Derau (*Handling Noisy Data*)
Derau (*noise*) adalah kesalahan acak atau varians tak diinginkan dalam pengukuran variabel.

#### A. Metode Binning (Penghalusan Lokal)
Mengurutkan nilai data, membaginya ke dalam interval (*bins*), lalu menghaluskan nilai di dalam bin:
1. **Equal-Width Binning**: Membagi rentang nilai menjadi $N$ interval dengan lebar sama:
   $$\text{Lebar Bin} = \frac{\max(A) - \min(A)}{N}$$
2. **Equal-Frequency / Equal-Depth Binning**: Membagi data sehingga setiap bin memuat jumlah sampel yang kurang lebih sama.

Teknik Penghalusan Nilai dalam Bin:
- **Smoothing by Bin Means**: Setiap nilai dalam bin digantikan dengan nilai rata-rata bin tersebut.
- **Smoothing by Bin Medians**: Setiap nilai dalam bin digantikan dengan median bin tersebut.
- **Smoothing by Bin Boundaries**: Nilai minimum dan maksimum dalam bin dijadikan batas; setiap nilai data diubah menjadi nilai batas terdekat dengannya.

#### B. Regresi (*Regression*)
Menghaluskan data dengan mencocokkan titik-titik data ke dalam fungsi matematika (Regresi Linier Sederhana atau Regresi Berganda).

#### C. Analisis Klaster (*Clustering*)
Mengelompokkan data yang mirip ke dalam klaster; data yang berada jauh di luar klaster utama diidentifikasi dan ditangani sebagai pencilan (*outlier*).

---

## 3. Integrasi Data (*Data Integration*)

Menggabungkan data dari berbagai sumber heterogen (basis data relasional, berkas teks, repositori dokumen) ke dalam penyimpanan terpadu (*Data Warehouse*).

### 3.1 Integrasi Skema dan Masalah Identifikasi Entitas
- Menyamakan entitas dunia nyata dari berbagai sistem berbeda (misal: atribut `cust_id` pada sistem A mewakili entitas yang sama dengan `customer_number` pada sistem B).
- Pemanfaatan metadata sangat krusial untuk mencegah inkonsistensi skema.

### 3.2 Analisis Redundansi dan Korelasi

#### A. Data Nominal: Uji Chi-Square ($\chi^2$)
Menguji hipotesis independensi antara dua atribut nominal $A$ dan $B$:

$$\chi^2 = \sum_{i=1}^c \sum_{j=1}^r \frac{(o_{ij} - e_{ij})^2}{e_{ij}}$$

- $o_{ij}$: Frekuensi teramati (*observed frequency*) dari sel $(A = a_i, B = b_j)$.
- $e_{ij}$: Frekuensi harapan (*expected frequency*), dihitung dengan:
  $$e_{ij} = \frac{\text{count}(A = a_i) \times \text{count}(B = b_j)}{N}$$
- Derajat kebebasan (*Degrees of freedom*): $(r - 1)(c - 1)$.
- Jika nilai $\chi^2$ lebih besar dari nilai kritis pada tabel distribusi dengan tingkat signifikansi $\alpha$, hipotesis independensi ditolak (artinya kedua atribut berkorelasi/redundant).

#### B. Data Numerik: Koefisien Korelasi Pearson ($r_{A, B}$)
Mengukur hubungan linier antara dua variabel numerik:

$$r_{A, B} = \frac{\sum_{i=1}^n (a_i - \bar{A})(b_i - \bar{B})}{(n - 1) \sigma_A \sigma_B} = \frac{\sum_{i=1}^n (a_i b_i) - n \bar{A}\bar{B}}{(n - 1) \sigma_A \sigma_B}$$

- $r_{A, B} > 0$: Korelasi Positif (kenaikan $A$ berbanding lurus dengan kenaikan $B$).
- $r_{A, B} = 0$: Tidak Berkolerasi / Independen secara linier.
- $r_{A, B} < 0$: Korelasi Negatif (kenaikan $A$ berbanding terbalik dengan penurunan $B$).

#### C. Kovarians (*Covariance*)
$$\text{Cov}(A, B) = \frac{1}{n} \sum_{i=1}^n (a_i - \bar{A})(b_i - \bar{B})$$
$$r_{A, B} = \frac{\text{Cov}(A, B)}{\sigma_A \sigma_B}$$

---

## 4. Reduksi Data (*Data Reduction*)

Menghasilkan representasi ringkas dari dataset dengan volume fisik jauh lebih kecil, namun tetap mempertahankan integritas analitis dan menghasilkan simpulan yang setara.

### 4.1 Reduksi Dimensi (*Dimensionality Reduction*)

1. **Transformasi Wavelet Diskrit (*Discrete Wavelet Transform - DWT*)**:
   - Memetakan vektor data numerik ke sub-band frekuensi wavelet.
   - Kompresi dilakukan dengan mempertahankan koefisien bernilai signifikan dan membuang koefisien kecil mendekati nol.
2. **Principal Component Analysis (PCA)**:
   - Mencari kombinasi linier ortogonal (komponen utama) dari sekumpulan variabel numerik berdimensi tinggi untuk menangkap varians maksimum data.
   - *Langkah*: Normalisasi data masukan $\rightarrow$ Bentuk matriks kovarians $\rightarrow$ Hitung eigenvector dan eigenvalue $\rightarrow$ Urutkan eigenvector dari eigenvalue terbesar $\rightarrow$ Pilih $k$ komponen teratas.
3. **Seleksi Subset Atribut (*Attribute Subset Selection / Feature Selection*)**:
   - Mengeliminasi fitur yang tidak relevan atau redundan:
     - *Stepwise Forward Selection*: Dimulai dari himpunan kosong, menambahkan atribut dengan performa terbaik satu per satu.
     - *Stepwise Backward Elimination*: Dimulai dari seluruh atribut, mengeliminasi atribut terburuk satu per satu.
     - *Kombinasi Forward & Backward*.
     - *Induksi Pohon Keputusan*: Atribut yang dijadikan simpul internal merupakan fitur paling diskriminatif.

---

### 4.2 Reduksi Numerositas (*Numerosity Reduction*)
Mengganti data asli dengan representasi data alternatif yang berukuran lebih kecil.

#### A. Metode Parametrik
Data dimodelkan ke dalam parameter matematis; hanya parameter model yang disimpan:
- **Model Regresi**: Regresi linier, multivariat, dan polinomial.
- **Model Log-Linear**: Mengaproksimasi distribusi probabilitas multivariat diskrit dalam tabel kontinjensi multidimensi.

#### B. Metode Non-Parametrik
- **Histogram**: Partisi data ke dalam ember (*buckets*), menyimpan frekuensi dan rentang interval (Equal-width, Equal-frequency, V-optimal, MaxDiff).
- **Clustering**: Dataset asli dipadatkan menjadi representasi klaster (vektor centroid dan radius sebaran).
- **Pengambilan Sampel (*Sampling*)**:
  - *Simple Random Sampling Without Replacement (SRSWOR)*: Tiap elemen yang terpilih tidak dikembalikan.
  - *Simple Random Sampling With Replacement (SRSWR)*: Tiap elemen yang terpilih dapat berpeluang terpilih kembali.
  - *Stratified Sampling*: Membagi dataset ke dalam strata/kelompok homogen, lalu mengambil sampel secara proporsional dari tiap strata (menjamin keterwakilan kelas minoritas).
- **Agregasi Kubus Data (*Data Cube Aggregation*)**:
  - Meringkas data numerik pada berbagai tingkat hierarki konsep dimensi (misal: data transaksi harian diagregasi menjadi total pendapatan bulanan).

---

### 4.3 Kompresi Data (*Data Compression*)
- **Lossless Compression**: Rekonstruksi data asli secara sempurna tanpa distorsi sedikit pun (misal: Huffman Coding, Lempel-Ziv-Welch / LZW).
- **Lossy Compression**: Rekonstruksi data bersifat aproksimasi dan mengalami sedikit degradasi informasi demi rasio kompresi yang jauh lebih tinggi (misal: DCT, Wavelet, PCA).

---

## 5. Transformasi Data dan Diskretisasi Data

### 5.1 Strategi Transformasi Data
1. **Penghalusan (*Smoothing*)**: Menghilangkan noise dari data.
2. **Konstruksi Fitur (*Attribute/Feature Construction*)**: Membentuk fitur baru dari kombinasi fitur yang ada untuk mempermudah pemodelan.
3. **Agregasi (*Aggregation*)**: Meringkas data ke tingkat granularitas yang lebih ringkas.
4. **Generalisasi (*Generalization*)**: Mengubah nilai primitif ke konsep hierarki yang lebih tinggi (misal: jalan $\rightarrow$ kota $\rightarrow$ negara).

---

### 5.2 Metode Normalisasi Data Numerik

#### A. Normalisasi Min-Max
Memetakan nilai $v$ dari rentang asli $[\min_A, \max_A]$ ke rentang skala baru $[new\_\min_A, new\_\max_A]$ (biasanya $[0, 1]$):

$$v' = \frac{v - \min_A}{\max_A - \min_A} (new\_\max_A - new\_\min_A) + new\_\min_A$$

*Kelemahan*: Mengalami distorsi batas jika terdapat nilai di luar rentang awal pada data masa depan.

#### B. Normalisasi Skor-Z (*Z-Score / Zero-Mean Normalization*)
Bermanfaat jika nilai minimum dan maksimum aktual tidak diketahui secara pasti, atau dataset mengandung pencilan:

$$v' = \frac{v - \bar{A}}{\sigma_A}$$

Variasi menggunakan Deviasi Absolut Rata-Rata (*Mean Absolute Deviation - $s_A$*):
$$s_A = \frac{1}{n} \sum_{i=1}^n |v_i - \bar{A}|, \quad v' = \frac{v - \bar{A}}{s_A}$$

#### C. Normalisasi Penskalaan Desimal (*Decimal Scaling Normalization*)
Memindahkan posisi titik desimal nilai atribut:

$$v' = \frac{v}{10^j}$$

dimana $j$ adalah bilangan bulat terkecil sedemikian rupa sehingga $\max(|v'|) < 1$.

---

### 5.3 Diskretisasi Data (*Data Discretization*)
Proses membagi rentang atribut numerik kontinu ke dalam interval-interval diskrit terpisah, kemudian mengganti nilai kuantitatif asli dengan label interval kualitatif.

#### Metode Diskretisasi:
1. **Metode Tanpa Pengawasan (*Unsupervised*)**:
   - Binning (*Equal-width* / *Equal-frequency*).
   - Analisis Histogram.
   - Analisis Klaster (*Cluster Analysis*).
2. **Metode Terawasi (*Supervised*)**:
   - Analisis Pohon Keputusan (*Decision Tree Induction*): Menggunakan ukuran kemurnian entropi (*Information Gain*).
   - Uji Korelasi ChiMerge: Pendekatan penggabungan interval dari bawah ke atas (*bottom-up*) berdasarkan signifikansi uji independensi $\chi^2$.

### 5.4 Pembentukan Hierarki Konsep (*Concept Hierarchy Generation*)
- Menyusun tingkatan abstraksi nilai data dari tingkat terinci menuju tingkat general.
- Untuk data nominal: Menggunakan urutan parsial domain (misal: `Kelurahan` $\subset$ `Kecamatan` $\subset$ `Kabupaten/Kota` $\subset$ `Provinsi`).

