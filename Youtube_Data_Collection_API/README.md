# YouTube & Return YouTube Dislike (RYD) Data Mining Collector

Modul Python untuk mengekstraksi dan menyusun dataset primer dari **YouTube Data API v3** dan **Return YouTube Dislike (RYD) API**. Dataset yang dihasilkan siap digunakan untuk analisis data mining (klasifikasi, klasterisasi, analisis sentimen, asosiasi).

---

## 📌 Fitur Utama
1. **Netral & Bebas Bias**: Logika ekstraksi, metrik, penamaan kolom, dan logging murni berbasis statistik objektif.
2. **Efisiensi Kuota**: Hanya mengambil data yang diperlukan. Tidak melakukan paginasi berulang untuk child reply komentar, melainkan memanfaatkan atribut `totalReplyCount`.
3. **Penanganan Error Tangguh**:
   - Menangani video dengan komentar yang dinonaktifkan (`commentsDisabled`) secara mulus.
   - Fallback otomatis ke default `0` jika RYD API mengalami timeout atau gagal merespons.
   - Sanitasi teks komentar (menghapus karakter `\n`, `\r`, `\t`) agar struktur file CSV tidak rusak.
4. **Fleksibilitas Input**:
   - Mendukung input berkas CSV bertemplate (`link_video`, `topik_video`, `tipe_video`).
   - Otomatis mengekstrak ID video dari format link standar YouTube, shortlink (`youtu.be`), YouTube Shorts, YouTube Live, maupun ID mentah 11 karakter.

---

## 🛠️ Persyaratan & Instalasi

Pastikan menggunakan Python 3.10+ (direkomendasikan Python 3.12+).

1. Buka terminal dan masuk ke direktori modul:
   ```bash
   cd Youtube_Data_Collection_API
   ```

2. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Konfigurasi Environment (`.env`)

1. Salin berkas template konfigurasi:
   ```bash
   cp .env.example .env
   ```

2. Buka `.env` dan masukkan kunci API resmi YouTube Anda:
   ```env
   YOUTUBE_API_KEY=AIzaSyD...your_actual_key_here
   INPUT_CSV=input_videos_template.csv
   MAX_COMMENTS=100
   OUTPUT_DIR=.
   ```

---

## 📋 Format Template Input CSV (`input_videos_template.csv`)

Anda dapat mendaftar video yang ingin di-scraping ke dalam berkas CSV. Kolom yang digunakan:
- `link_video`: Tautan video YouTube (bisa berupa URL lengkap, shortlink youtu.be, link shorts, atau ID video).
- `topik_video`: Kategori atau isu video (contoh: *Debat Kebijakan*, *Sosialisasi Regulasi*).
- `tipe_video`: Format video (contoh: *Talkshow*, *Berita*, *Podcast*, *Meme*, *Serious*).
- `channel_video`: Label/nama channel yang ditentukan pengguna (contoh: *Caveine*, *GuruGembul*, *KOMPASTV*).

Contoh isi:
```csv
link_video,topik_video,tipe_video,channel_video
https://www.youtube.com/watch?v=dQw4w9WgXcQ,Debat Kebijakan Publik,Talkshow,NajwaShihab
https://youtu.be/jNQXAC9IVRw,Sosialisasi Regulasi,Berita,KOMPASTV
https://www.youtube.com/watch?v=9bZkp7q19f0,Opini Pemilih Muda,Podcast,FerryIrwandi
```

---

## 🚀 Cara Menjalankan

### 1. Menjalankan Menggunakan File CSV (Direkomendasikan)
```bash
python main.py --input-csv input_videos_template.csv
```

### 2. Menjalankan dengan Video ID Langsung via CLI
```bash
python main.py --video-ids dQw4w9WgXcQ https://youtu.be/jNQXAC9IVRw --max-comments 50
```

### 3. Opsi Argumen CLI Lengkap
| Argumen | Default | Deskripsi |
|---|---|---|
| `--api-key` | dari `.env` | YouTube Data API v3 Key |
| `--input-csv` | dari `.env` | Jalur berkas CSV input daftar video |
| `--video-ids` | `[]` | Daftar ID / URL video langsung |
| `--max-comments` | `100` | Batas maksimal komentar per video |
| `--output-dir` | `.` | Folder tempat menyimpan berkas CSV hasil |
| `--video-output` | `dataset_video_politik.csv` | Nama berkas CSV level video |
| `--comment-output` | `dataset_komentar_politik.csv` | Nama berkas CSV level komentar |

---

## 📊 Struktur Dataset Output

### 1. `dataset_video_politik.csv` (Level Video)
- `video_id`: ID unik video (11 karakter).
- `title`: Judul video.
- `channel_title`: Nama channel pengunggah.
- `published_at`: Waktu unggah video (ISO 8601).
- `duration_seconds`: Durasi video dalam satuan detik (Integer).
- `category_id`: Kategori ID dari YouTube.
- `view_count`: Jumlah penayangan.
- `like_count`: Jumlah like resmi YouTube.
- `dislike_count_est`: Estimasi dislike dari Return YouTube Dislike (RYD) API.
- `raw_likes_ryd`: Jumlah like pengguna ekstensi RYD.
- `raw_dislikes_ryd`: Jumlah dislike pengguna ekstensi RYD.
- `comment_count`: Total komentar video.
- `dislike_ratio`: Formula: `dislikes / (likes + dislikes)`.
- `engagement_rate`: Formula: `((likes + dislikes + comment_count) / views) * 100`.
- `views_per_day`: Formula: `views / hari_sejak_rilis`.
- `topik_video`: Metadata topik dari berkas CSV input (jika ada).
- `tipe_video`: Metadata tipe video dari berkas CSV input (jika ada).
- `channel_video`: Metadata nama channel dari berkas CSV input (jika ada).

### 2. `dataset_komentar_politik.csv` (Level Komentar)
- `comment_id`: ID unik komentar.
- `video_id`: Foreign key ID video relasi.
- `author`: Username penulis komentar.
- `comment_text`: Teks komentar bersih (tanpa tab atau baris baru).
- `comment_likes`: Jumlah like pada komentar.
- `total_replies`: Total reply pada komentar (dari atribut `totalReplyCount`).
- `published_at`: Waktu komentar diunggah (ISO 8601).

---

## 🧪 Menjalankan Unit Test

Untuk memverifikasi kebenaran formula matematika, parser URL, pembersihan karakter komentar, dan penanganan error:
```bash
pytest test_collector.py -v
```

