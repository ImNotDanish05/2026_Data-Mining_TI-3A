# Dataset Publik Riset Data Mining (TI-3A)

Direktori ini memuat salinan dataset primer yang telah melalui proses **audit keamanan, sanitasi derau, dan anonimisasi mutlak (*100% de-identified*)** sehingga aman dan sah untuk dipublikasikan secara terbuka bagi keperluan pendidikan dan penelitian ilmiah (*open academic research*).

---

## 🔒 Jaminan Keamanan & Privasi Data (*Privacy Assurance*)

1. **Anonimisasi Mutlak (UU PDP No. 27 Tahun 2022)**:
   - Seluruh identitas akun, nama profil pengguna, dan username (`author`) **TIDAK DICANTUMKAN** dalam dataset ini.
   - Karakter mention (`@username`), tautan web (URL), dan stempel waktu (*timestamp*) telah dibersihkan secara komputasional.
   - Tidak memuat informasi identitas pribadi sensitif (*PII - Personally Identifiable Information*).
2. **Kepatuhan Sumber Data**:
   - Diperoleh secara legal melalui antarmuka resmi **Google YouTube Data API v3** dan **Return YouTube Dislike (RYD) API** dari video dan komentar ranah publik (*public domain*).
3. **Pengecualian Penelitian Ilmiah**:
   - Memenuhi ketentuan **Pasal 15 ayat (1) huruf f UU No. 27 Tahun 2022 (UU PDP)** serta **Pasal 44 ayat (1) huruf a UU No. 28 Tahun 2014 (UU Hak Cipta)** untuk riset akademik non-komersial.

---

## 📁 Berkas Dataset yang Tersedia

### 1. `dataset_komentar_publik.csv`
Memuat 5.207 baris teks komentar warganet yang telah bersih dari derau teks dan siap diolah untuk penambangan teks / NLP.

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `comment_id` | String | ID unik komentar yang dihasilkan oleh YouTube API |
| `video_id` | String | Foreign key yang menghubungkan komentar ke video tertentu |
| `comment_text` | String | Teks opini komentar bersih (*clean, lowercase, no noise, no PII*) |
| `comment_likes` | Integer | Jumlah apresiasi suka (*likes*) pada komentar tersebut |
| `total_replies`| Integer | Jumlah balasan (*replies*) pada komentar tersebut |
| `published_at` | Timestamp (ISO 8601) | Waktu komentar dipublikasikan di YouTube |

---

### 2. `dataset_video_publik.csv`
Memuat metadata 55 video YouTube terkait kebijakan Makan Bergizi Gratis (MBG) dan kepemimpinan nasional, lengkap dengan metrik interaksi dan penskalaan numerik standar.

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `video_id` | String | ID unik video YouTube (Primary Key) |
| `title` | String | Judul resmi video di YouTube |
| `channel_title` | String | Nama kanal pembuat video |
| `published_at` | Timestamp | Waktu publikasi video |
| `duration_seconds` | Integer | Durasi video dalam detik |
| `view_count` | Integer | Total penonton video |
| `like_count` | Integer | Total suka pada video |
| `dislike_count_est` | Integer | Estimasi jumlah dislike dari RYD API |
| `comment_count` | Integer | Total komentar pada video |
| `engagement_rate` | Float | Rasio interaksi terhadap penonton (%) |
| `views_per_day` | Float | Kecepatan rata-rata penonton per hari |
| `topik_video` | String | Label topik kebijakan (`MBG` atau `PrabowoSubianto`) |
| `tipe_video` | String | Format kemasan konten (`Meme`, `Serious`, `News`) |
| `is_outlier_views` | Boolean | Penanda pencilan penonton via Boxplot $1.5 \times IQR$ |
| `is_outlier_likes` | Boolean | Penanda pencilan suka via Boxplot $1.5 \times IQR$ |
| `*_minmax` | Float | Fitur numerik hasil normalisasi Min-Max $[0, 1]$ |
| `*_zscore` | Float | Fitur numerik hasil standarisasi Skor-Z (Mean=0, Std=1) |
| `summary` | String | Ringkasan narasi video objektif dan netral |

---

### 3. `dataset_transkrip_publik.csv`
Memuat teks transkrip narasi wicara lengkap dari 55 video (134.986 kata) untuk analisis korpus teks makro.

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `video_id` | String | ID unik video |
| `title` | String | Judul video |
| `channel_video` | String | Saluran YouTube |
| `topik_video` | String | Kategori topik |
| `tipe_video` | String | Kategori format video |
| `language` | String | Bahasa transkrip (`id` = Bahasa Indonesia) |
| `word_count` | Integer | Jumlah kata dalam transkrip |
| `transcript_text` | String | Teks lengkap narasi wicara video |

---
*Dataset ini dirilis untuk kepentingan riset akademis di bawah lisensi MIT.*

