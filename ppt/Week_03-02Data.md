# Materi Pembelajaran: Mengenal Data Anda (Getting to Know Your Data)

Materi ini membahas karakteristik objek dan atribut data, deskripsi statistik dasar, visualisasi data multidimensi, serta formulasi matematis untuk mengukur tingkat kemiripan (*similarity*) dan ketidaksamaan (*dissimilarity/distance*).

---

## 1. Objek Data dan Tipe Atribut (*Data Objects & Attribute Types*)

### 1.1 Definisi Objek Data
- **Objek Data (*Data Objects*)**: Representasi dari entitas nyata dalam suatu kumpulan data.
  - Disebut juga: *samples, examples, instances, data points, tuples*.
  - *Contoh*: Dalam database penjualan, objek dapat berupa pelanggan, item produk, atau transaksi.

### 1.2 Definisi Atribut
- **Atribut (*Attribute*)**: Karakteristik, dimensi, atau fitur dari suatu objek data.
  - Disebut juga: *dimensions, features, variables*.

### 1.3 Klasifikasi Tipe Atribut

| Tipe Atribut | Deskripsi | Operasi yang Valid | Contoh |
| :--- | :--- | :--- | :--- |
| **Nominal** | Nilai berupa kategori, simbol, atau label nama tanpa urutan intrinsik. | $=, \neq$ | Warna mata (`hitam`, `cokelat`), Pekerjaan, Status Pernikahan. |
| **Biner (Binary)** | Atribut nominal dengan tepat dua status (0 dan 1). | $=, \neq$ | Lolos/Gagal, Merokok/Tidak. |
| **Ordinal** | Nilai memiliki tingkatan atau urutan bermakna (*ranking*), tetapi jarak kuantitatif antar nilai tidak diketahui secara pasti. | $=, \neq, <, >$ | Ukuran pakaian (`S`, `M`, `L`, `XL`), Tingkat Kepuasan (1–5), Peringkat Akademik. |
| **Numerik - Interval** | Nilai kuantitatif dengan satuan pengukuran yang sama, namun **TIDAK memiliki nilai nol mutlak** (*arbitrary zero*). | $+ , -$ | Suhu Celsius/Fahrenheit (0°C bukan berarti tidak ada suhu), Tahun Kalender. |
| **Numerik - Rasio** | Nilai kuantitatif dengan **nilai nol mutlak** (*inherent true zero*). Nilai nol berarti ketiadaan kuantitas fisik. | $+ , - , \times , \div$ | Suhu Kelvin (0 K = nol mutlak), Usia, Berat badan, Gaji bulanan. |

#### Pembagian Atribut Biner:
1. **Biner Simetris (*Symmetric Binary*)**: Kedua hasil memiliki bobot/kepentingan yang setara (misal: Jenis Kelamin: Pria/Wanita).
2. **Biner Asimetris (*Asymmetric Binary*)**: Kedua hasil memiliki bobot kepentingan yang tidak sama. Biasanya status 1 mewakili kehadiran kondisi langka/penting dan 0 mewakili ketiadaan kondisi tersebut (misal: Hasil tes medis HIV: Positif = 1, Negatif = 0).

#### Atribut Diskrit vs Kontinu:
- **Diskrit (*Discrete*)**: Memiliki himpunan nilai yang berhingga (*finite*) atau terhitung (*countably infinite*). Contoh: Jumlah tanggungan, Kode pos.
- **Kontinu (*Continuous*)**: Nilai berupa bilangan riil kontinu dengan presisi floating-point tak terhingga. Contoh: Tekanan darah, tinggi badan.

---

## 2. Deskripsi Statistik Dasar Data (*Basic Statistical Descriptions*)

### 2.1 Pengukuran Tendensi Sentral (*Central Tendency*)

#### A. Rata-Rata (*Mean*)
- **Rata-Rata Aritmatika**:
  $$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i = \frac{x_1 + x_2 + \dots + x_n}{n}$$
- **Rata-Rata Berbobot (*Weighted Mean*)**:
  $$\bar{x} = \frac{\sum_{i=1}^n w_i x_i}{\sum_{i=1}^n w_i}$$
- **Karakteristik**: *Mean* sangat sensitif terhadap nilai ekstrem (*outlier*).
- **Trimmed Mean**: Rata-rata yang dihitung setelah membuang sebagian kecil persentase nilai ekstrem tertinggi dan terendah (misal: 2% atau 5% *trimmed mean*).

#### B. Median
- Nilai tengah setelah data diurutkan dari terkecil ke terbesar.
- **Karakteristik**: Kebal terhadap pencilan (*robust/outlier-resistant*).
- Untuk data berukuran $n$:
  - Jika $n$ ganjil: Nilai pada posisi $\frac{n+1}{2}$.
  - Jika $n$ genap: Rata-rata dari dua nilai di posisi $\frac{n}{2}$ dan $\frac{n}{2} + 1$.

#### C. Modus (*Mode*)
- Nilai yang paling sering muncul dalam kumpulan data.
- Kategori data berdasarkan modus: *Unimodal* (1 modus), *Bimodal* (2 modus), *Trimodal* (3 modus), atau *Multimodal*.
- **Hubungan Empiris untuk Distribusi Miring Unimodal Moderat**:
  $$\text{Mean} - \text{Modus} \approx 3 \times (\text{Mean} - \text{Median})$$

#### D. Titik Tengah Rentang (*Midrange*)
$$\text{Midrange} = \frac{\min(x) + \max(x)}{2}$$

---

### 2.2 Pengukuran Sebaran Data (*Data Dispersion*)

#### A. Rentang (*Range*)
$$\text{Range} = \max(x) - \min(x)$$

#### B. Kuantil, Kuartil, dan Interquartile Range (IQR)
- **Kuartil**: Titik potong yang membagi data terurut menjadi 4 bagian sama besar:
  - $Q_1$ (*Kuartil Bawah / 25th percentile*)
  - $Q_2$ (*Median / 50th percentile*)
  - $Q_3$ (*Kuartil Atas / 75th percentile*)
- **Rentang Antarkuartil (*Interquartile Range - IQR*)**:
  $$IQR = Q_3 - Q_1$$

#### C. Ringkasan Lima Angka (*Five-Number Summary*)
Representasi ringkas sebaran data yang terdiri dari:
$$[\min, Q_1, \text{Median}, Q_3, \max]$$

#### D. Boxplot dan Deteksi Pencilan (*Outlier Detection*)
- **Kotak (*Box*)**: Membentang dari $Q_1$ hingga $Q_3$ (panjang kotak = $IQR$).
- **Garis Dalam Kotak**: Menandai nilai Median.
- **Kumis (*Whiskers*)**: Ditarik dari tepi kotak ke nilai data terdekat yang masih berada dalam batas toleransi $1.5 \times IQR$.
  - Batas Bawah: $Q_1 - 1.5 \times IQR$
  - Batas Atas: $Q_3 + 1.5 \times IQR$
- **Pencilan (*Outliers*)**: Data yang berada di luar jangkauan kumis (lebih kecil dari $Q_1 - 1.5 \times IQR$ atau lebih besar dari $Q_3 + 1.5 \times IQR$).

#### E. Varians dan Standar Deviasi (*Variance & Standard Deviation*)
- **Varians Populasi**:
  $$\sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2 = \frac{1}{N} \sum x_i^2 - \mu^2$$
- **Varians Sampel**:
  $$s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$$
- **Standar Deviasi**: Akar kuadrat dari varians ($\sigma = \sqrt{\sigma^2}$ atau $s = \sqrt{s^2}$).

---

## 3. Tampilan Grafik Deskripsi Statistik Dasar

1. **Boxplot**: Menampilkan ringkasan lima angka dan identifikasi pencilan secara visual.
2. **Histogram**: Membagi rentang atribut ke dalam interval (*bins*) dan menampilkan frekuensi data per interval.
3. **Quantile Plot**: Memplot nilai data terurut terhadap persentil kumulatif $f_i = \frac{i - 0.5}{N}$.
4. **Quantile-Quantile (Q-Q) Plot**: Membandingkan kuantil suatu distribusi dengan distribusi lainnya (atau distribusi standar seperti normalitas). Jika titik-titik membentuk garis lurus, kedua distribusi memiliki bentuk yang serupa.
5. **Scatter Plot (Diagram Pencar)**: Memvisualisasikan pola hubungan antara dua variabel numerik:
   - Korelasi Positif: Titik-titik membentuk tren diagonal naik dari kiri-bawah ke kanan-atas.
   - Korelasi Negatif: Titik-titik membentuk tren diagonal turun dari kiri-atas ke kanan-bawah.
   - Nol Korelasi: Titik-titik menyebar secara acak tanpa pola terarah.

---

## 4. Teknik Visualisasi Data Multidimensi

1. **Teknik Berorientasi Piksel (*Pixel-Oriented Techniques*)**:
   - Memetakan setiap nilai dimensi ke warna satu piksel pada layar.
   - Disusun menggunakan kurva pengisi ruang (*space-filling curves*): Kurva Hilbert, Kurva Morton, Pola Spiral.
2. **Teknik Proyeksi Geometris (*Geometric Projection Techniques*)**:
   - Memproyeksikan data dimensi tinggi ke ruang 2D atau 3D.
   - *Scatter Plot Matrix*: Kisi matriks grafik 2D berukuran $d \times d$ untuk $d$ atribut numerik.
   - *Parallel Coordinates*: Membuat $d$ sumbu sejajar berjarak sama; tiap objek data direpresentasikan sebagai garis poligon yang memotong tiap sumbu pada nilai atributnya.
3. **Teknik Berbasis Ikon (*Icon-Based Techniques*)**:
   - *Chernoff Faces*: Menghubungkan variabel atribut ke fitur wajah manusia (bentuk mata, lekuk mulut, lebar wajah) hingga 18 dimensi.
   - *Stick Figures*: Bentuk tubuh dan sudut dahan anggota badan mewakili dimensi atribut.
4. **Teknik Hierarkis (*Hierarchical Techniques*)**:
   - *Dimensional Stacking*: Membagi ruang dimensi menjadi kisi-kisi bersarang.
   - *Treemaps*: Persegi panjang bertingkat yang mengkodekan hierarki melalui ukuran area dan warna.
5. **Visualisasi Graf & Jejaring**:
   - Menampilkan hubungan antar-entitas dalam bentuk simpul (*nodes*) dan sisi (*edges*).

---

## 5. Pengukuran Kemiripan dan Ketidaksamaan Data (*Similarity & Dissimilarity*)

### 5.1 Struktur Matriks Representasi
- **Matriks Data (*Two-Mode Matrix*)**: $n$ objek $\times$ $p$ atribut.
  $$X = \begin{bmatrix} x_{11} & \cdots & x_{1f} & \cdots & x_{1p} \\ \vdots & & \vdots & & \vdots \\ x_{i1} & \cdots & x_{if} & \cdots & x_{ip} \\ \vdots & & \vdots & & \vdots \\ x_{n1} & \cdots & x_{nf} & \cdots & x_{np} \end{bmatrix}$$

- **Matriks Ketidaksamaan (*One-Mode Matrix*)**: $n \times n$ pasangan jarak antar-objek (segitiga bawah):
  $$D = \begin{bmatrix} 0 & & & \\ d(2,1) & 0 & & \\ d(3,1) & d(3,2) & 0 & \\ \vdots & \vdots & \vdots & 0 \end{bmatrix}$$

---

### 5.2 Jarak untuk Atribut Nominal
Berdasarkan rasio ketidakcocokan (*Simple Matching*):
$$d(i, j) = \frac{p - m}{p}$$
- $p$: Total jumlah atribut nominal.
- $m$: Jumlah atribut yang nilainya sama (*cocok*) antara objek $i$ dan $j$.
- Kemiripan: $s(i, j) = 1 - d(i, j) = \frac{m}{p}$.

---

### 5.3 Jarak untuk Atribut Biner
Tabel Kontinjensi $2 \times 2$ antara objek $i$ dan $j$:

| | Objek $j = 1$ | Objek $j = 0$ | Total |
| :--- | :---: | :---: | :---: |
| **Objek $i = 1$** | $q$ | $r$ | $q + r$ |
| **Objek $i = 0$** | $s$ | $t$ | $s + t$ |
| **Total** | $q + s$ | $r + t$ | $p = q + r + s + t$ |

- **Biner Simetris (*Simple Matching Distance*)**:
  $$d(i, j) = \frac{r + s}{q + r + s + t}$$
  $$sim(i, j) = \frac{q + t}{q + r + s + t}$$

- **Biner Asimetris (*Jaccard Distance / Jaccard Coefficient*)**:
  Kehadiran kondisi bersama ($t$, bernilai 0 di kedua objek) diabaikan karena tidak informatif.
  $$d_{\text{Jaccard}}(i, j) = \frac{r + s}{q + r + s}$$
  $$sim_{\text{Jaccard}}(i, j) = \frac{q}{q + r + s}$$

---

### 5.4 Jarak untuk Atribut Numerik

#### A. Jarak Minkowski ($L_p$ Norm)
Generalisasi jarak metrik untuk parameter $h \ge 1$:
$$d(i, j) = \left( \sum_{k=1}^p |x_{ik} - x_{jk}|^h \right)^{\frac{1}{h}}$$

1. **Jarak Manhattan ($h = 1, L_1$ Norm / City Block Distance)**:
   $$d(i, j) = \sum_{k=1}^p |x_{ik} - x_{jk}|$$

2. **Jarak Euclidean ($h = 2, L_2$ Norm)**:
   $$d(i, j) = \sqrt{\sum_{k=1}^p (x_{ik} - x_{jk})^2}$$

3. **Jarak Supremum / Chebyshev ($h \rightarrow \infty, L_\infty$ Norm / $L_{\max}$)**:
   $$d(i, j) = \lim_{h\to\infty} \left( \sum_{k=1}^p |x_{ik} - x_{jk}|^h \right)^{\frac{1}{h}} = \max_{k=1}^p |x_{ik} - x_{jk}|$$

#### B. Sifat-Sifat Metrik Jarak yang Valid
Suatu fungsi jarak $d(i, j)$ disebut metrik sah jika memenuhi:
1. **Non-negativitas**: $d(i, j) \ge 0$.
2. **Identitas**: $d(i, i) = 0$.
3. **Simetri**: $d(i, j) = d(j, i)$.
4. **Ketaksamaan Segitiga (*Triangle Inequality*)**: $d(i, j) \le d(i, k) + d(k, j)$.

#### C. Jarak Mahalanobis
Memperhitungkan korelasi antar-variabel menggunakan matriks kovarians $\Sigma$:
$$d_{\text{Mahalanobis}}(i, j) = \sqrt{(x_i - x_j)^T \Sigma^{-1} (x_i - x_j)}$$

---

### 5.5 Cosine Similarity (Untuk Teks / Vektor Sparse)
Digunakan ketika ukuran frekuensi kata bervariasi namun arah orientasi vektor lebih penting daripada panjang absolutnya:
$$\cos(x, y) = \frac{x \cdot y}{\|x\| \|y\|} = \frac{\sum_{k=1}^p x_k y_k}{\sqrt{\sum_{k=1}^p x_k^2} \sqrt{\sum_{k=1}^p y_k^2}}$$
- Nilai berkisar antara 0 (vektor tegak lurus/tidak mirip sama sekali) hingga 1 (vektor sejajar searah/identik).

---

### 5.6 Pengukuran untuk Atribut Ordinal
1. Urutkan nilai ordinal dari rank terkecil $1$ hingga rank terbesar $M_f$.
2. Petakan rank objek $i$ pada atribut $f$, yaitu $r_{if}$, ke rentang kontinu $[0, 1]$:
   $$z_{if} = \frac{r_{if} - 1}{M_f - 1}$$
3. Hitung jarak antar-objek menggunakan jarak numerik (seperti Euclidean atau Manhattan) terhadap nilai $z_{if}$.

---

### 5.7 Pengukuran untuk Tipe Atribut Campuran (*Mixed Attributes*)
Untuk dataset yang menggabungkan atribut nominal, biner, ordinal, dan numerik sekaligus, digunakan koefisien jarak gabungan (rumus Gower):

$$d(i, j) = \frac{\sum_{f=1}^p \delta_{ij}^{(f)} d_{ij}^{(f)}}{\sum_{f=1}^p \delta_{ij}^{(f)}}$$

- **Indikator $\delta_{ij}^{(f)}$**:
  - $\delta_{ij}^{(f)} = 0$ jika nilai atribut $f$ hilang (*missing*) pada salah satu objek, atau jika $f$ adalah biner asimetris dan bernilai 0 di kedua objek ($x_{if} = x_{jf} = 0$).
  - $\delta_{ij}^{(f)} = 1$ untuk kondisi lainnya.
- **Kontribusi Jarak $d_{ij}^{(f)}$**:
  - Untuk *Nominal / Biner*: $d_{ij}^{(f)} = 0$ jika $x_{if} = x_{jf}$; sebaliknya $d_{ij}^{(f)} = 1$.
  - Untuk *Numerik*: $d_{ij}^{(f)} = \frac{|x_{if} - x_{jf}|}{\max_h(x_{hf}) - \min_h(x_{hf})}$.
  - Untuk *Ordinal*: Dihitung selisih nilai $z$-score normalisasinya seperti pada atribut numerik.

