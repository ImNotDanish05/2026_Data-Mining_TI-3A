# Ringkasan Perbandingan Sebelum vs Sesudah Preprocessing

## 1. Dataset Komentar Netizen
- **Jumlah Baris Mentah**: 5,284
- **Baris Null Dieliminasi**: 4
- **Baris Kosong Pasca-Cleaning Dieliminasi**: 73
- **Jumlah Baris Bersih**: 5,207
- **Preservasi Privasi**: Kolom `author` telah di-anonymize (dihapus).

### Contoh Perbandingan Teks Komentar (Before vs After):

| No | Sebelum (Raw) | Sesudah (Clean) |
|:---|:---|:---|
| 1 | Dewasa di tahun yang salah😢 | dewasa di tahun yang salah |
| 2 | 6:38 stikerin miror coy yang kayak lampu hazard wjwkwkwk😂 | stikerin miror coy yang kayak lampu hazard wjwkwkwk |
| 3 | Hei apa ini 3:42 | hei apa ini |
| 4 | Tumben kagak ada iklan | tumben kagak ada iklan |
| 5 | 6:17 " udah kayak di kota silent hill anj " | udah kayak di kota silent hill anj |

---

## 2. Dataset Video
- **Total Video**: 55
- **Pencilan Views (IQR Rule)**: 3 video (Ambang batas atas: 1,160,782)
- **Pencilan Likes (IQR Rule)**: 6 video (Ambang batas atas: 42,441)

### Tabel Transformasi & Normalisasi Skala Numerik:

| Fitur | Raw Min | Raw Max | Raw Mean | Min-Max Range | Z-Score Mean |
|:---|:---|:---|:---|:---|:---|
| `view_count` | 5,622.00 | 6,192,423.00 | 643,882.58 | [0.0, 1.0] | -0.0 |
| `like_count` | 4.00 | 130,942.00 | 17,394.09 | [0.0, 1.0] | 0.0 |
| `dislike_count_est` | 0.00 | 2,612.00 | 154.44 | [0.0, 1.0] | -0.0 |
| `comment_count` | 27.00 | 17,449.00 | 2,475.16 | [0.0, 1.0] | 0.0 |
| `engagement_rate` | 0.50 | 6.25 | 3.10 | [0.0, 1.0] | 0.0 |
| `views_per_day` | 120.68 | 353,538.97 | 13,602.34 | [0.0, 1.0] | -0.0 |
