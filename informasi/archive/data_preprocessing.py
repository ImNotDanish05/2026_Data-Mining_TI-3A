"""
Modul: data_preprocessing.py
Deskripsi: Pipeline Prapemrosesan Data (Data Preprocessing) 100% untuk Dataset Video dan Komentar YouTube Politik.
Mengimplementasikan 4 pilar standar Data Preprocessing:
1. Data Cleaning (Pembersihan Teks, Penanganan Missing Values)
2. Data Reduction & Privacy Preservation (Anonymization kolom author, deteksi outlier IQR)
3. Data Transformation & Scaling (Min-Max Normalization [0, 1] dan Z-Score Standardization)
4. Data Integration (Verifikasi integritas relasional video_id)
"""

import json
import os
import re
import unicodedata
from typing import Dict, Any, Tuple

import numpy as np
import pandas as pd


def clean_comment_text(text: Any) -> str:
    """
    Membersihkan teks komentar netizen dari derau (noise):
    - Mengabaikan tipe non-string / null
    - Menghapus URL/link
    - Menghapus mention akun (@user) dan hashtag (#tag)
    - Menghapus stempel waktu video (timestamp seperti '6:38', '3:42')
    - Menghapus emoji dan karakter grafis khusus via Unicodedata
    - Menghapus tanda baca dan karakter non-alfanumerik
    - Menormalkan spasi ganda
    - Case folding (konversi ke huruf kecil / lowercase)
    """
    if pd.isna(text) or not isinstance(text, str):
        return ""

    s = text

    # 1. Hapus URL / tautan web
    s = re.sub(r"https?://\S+|www\.\S+", " ", s)

    # 2. Hapus mention (@username) dan hashtag (#topik)
    s = re.sub(r"[@#]\w+", " ", s)

    # 3. Hapus timestamp video YouTube (format MM:SS atau HH:MM:SS)
    s = re.sub(r"\b\d{1,2}:\d{2}(?::\d{2})?\b", " ", s)

    # 4. Hapus emoji & karakter simbol khusus berdasarkan kategori Unicode
    s = "".join(
        c for c in s
        if not unicodedata.category(c).startswith("So")  # Other Symbol (emoji dsb)
        and not unicodedata.category(c).startswith("Cn") # Unassigned
        and not unicodedata.category(c).startswith("Cs") # Surrogate
        and ord(c) < 0x1F000
    )

    # 5. Ganti karakter non-alfanumerik (tanda baca, simbol) menjadi spasi
    s = re.sub(r"[^\w\s]", " ", s)

    # 6. Normalkan spasi berlebih
    s = re.sub(r"\s+", " ", s).strip()

    # 7. Case folding ke huruf kecil
    return s.lower()


def detect_outliers_iqr(series: pd.Series) -> Tuple[pd.Series, Dict[str, float]]:
    """
    Mendeteksi pencilan (outliers) menggunakan aturan Boxplot 1.5 * IQR (Materi Kuliah Week 03).
    Batas Bawah = Q1 - 1.5 * IQR
    Batas Atas = Q3 + 1.5 * IQR
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    is_outlier = (series < lower_bound) | (series > upper_bound)
    stats = {
        "q1": float(q1),
        "q3": float(q3),
        "iqr": float(iqr),
        "lower_bound": float(lower_bound),
        "upper_bound": float(upper_bound),
        "outlier_count": int(is_outlier.sum()),
    }
    return is_outlier, stats


def min_max_normalize(series: pd.Series) -> pd.Series:
    """
    Normalisasi Min-Max ke rentang [0, 1] (Materi Kuliah Week 04).
    v' = (v - min) / (max - min)
    """
    s_min = series.min()
    s_max = series.max()
    if s_max == s_min:
        return pd.Series(0.0, index=series.index)
    return (series - s_min) / (s_max - s_min)


def z_score_normalize(series: pd.Series) -> pd.Series:
    """
    Normalisasi Skor-Z / Standarisasi (Materi Kuliah Week 04).
    v' = (v - mean) / std
    """
    s_std = series.std(ddof=1)
    if s_std == 0 or np.isnan(s_std):
        return pd.Series(0.0, index=series.index)
    return (series - series.mean()) / s_std


def preprocess_datasets(
    raw_video_path: str = "data/raw/dataset_video_politik.csv",
    raw_comment_path: str = "data/raw/dataset_komentar_politik.csv",
    output_dir: str = "data/processed",
) -> Dict[str, Any]:
    """
    Fungsi orkestrasi prapemrosesan penuh untuk kedua dataset.
    """
    os.makedirs(output_dir, exist_ok=True)
    report: Dict[str, Any] = {}

    print("=" * 60)
    print("MEMULAI PIPELINE PRAPEMROSESAN DATA (DATA PREPROCESSING)")
    print("=" * 60)

    # -------------------------------------------------------------
    # 1. PREPROCESSING DATASET KOMENTAR
    # -------------------------------------------------------------
    print("\n[1/4] Memuat Dataset Komentar Mentah...")
    df_kom_raw = pd.read_csv(raw_comment_path)
    total_raw_kom = len(df_kom_raw)
    null_kom_count = int(df_kom_raw["comment_text"].isnull().sum())
    print(f"  - Total komentar mentah: {total_raw_kom:,} baris")
    print(f"  - Komentar kosong (null/NaN): {null_kom_count} baris")

    # A. Data Cleaning: Drop Null Comments (Ignore tuple)
    df_kom = df_kom_raw.dropna(subset=["comment_text"]).copy()

    # B. Text Cleaning & Case Folding
    print("  - Menjalankan pembersihan teks (hapus emoji, link, timestamp, simbol, lowercase)...")
    df_kom["comment_text_clean"] = df_kom["comment_text"].apply(clean_comment_text)

    # C. Filter komentar yang menjadi kosong setelah dibersihkan (misal isinya cuma emoji)
    empty_after_clean = (df_kom["comment_text_clean"] == "").sum()
    print(f"  - Komentar kosong setelah pembersihan emoji/simbol: {empty_after_clean} baris")
    df_kom = df_kom[df_kom["comment_text_clean"] != ""].copy()

    # D. Data Reduction & Privacy Preservation: Drop 'author' (Anonymization)
    print("  - Menerapkan Privacy-Preserving Data Mining (Drop kolom 'author')...")
    columns_to_keep = [
        "comment_id",
        "video_id",
        "comment_text",        # teks mentah asli disimpan untuk keperluan audit/perbandingan
        "comment_text_clean",  # teks bersih hasil prapemrosesan
        "comment_likes",
        "total_replies",
        "published_at",
    ]
    df_kom_clean = df_kom[columns_to_keep].copy()
    # Ubah nama kolom comment_text mentah menjadi comment_text_raw agar lebih eksplisit
    df_kom_clean.rename(columns={"comment_text": "comment_text_raw"}, inplace=True)

    output_kom_path = os.path.join(output_dir, "dataset_komentar_clean.csv")
    df_kom_clean.to_csv(output_kom_path, index=False)
    print(f"  -> Disimpan ke: {output_kom_path} ({len(df_kom_clean):,} baris)")

    report["komentar"] = {
        "raw_total": total_raw_kom,
        "null_dropped": null_kom_count,
        "empty_after_cleaning_dropped": int(empty_after_clean),
        "clean_total": len(df_kom_clean),
        "privacy_anonymized": True,
        "sample_comparisons": [
            {
                "raw": row["comment_text_raw"],
                "clean": row["comment_text_clean"]
            }
            for _, row in df_kom_clean.head(5).iterrows()
        ]
    }

    # -------------------------------------------------------------
    # 2. PREPROCESSING DATASET VIDEO
    # -------------------------------------------------------------
    print("\n[2/4] Memuat Dataset Video Mentah...")
    df_vid_raw = pd.read_csv(raw_video_path)
    total_raw_vid = len(df_vid_raw)
    print(f"  - Total video mentah: {total_raw_vid} video")

    df_vid_clean = df_vid_raw.copy()

    # A. Outlier Detection (IQR Boxplot Rule) untuk views dan likes
    print("  - Mendeteksi pencilan (outliers) pada view_count dan like_count...")
    outlier_views, stats_views = detect_outliers_iqr(df_vid_clean["view_count"])
    outlier_likes, stats_likes = detect_outliers_iqr(df_vid_clean["like_count"])

    df_vid_clean["is_outlier_views"] = outlier_views
    df_vid_clean["is_outlier_likes"] = outlier_likes

    print(f"    * Pencilan views (Q3 + 1.5*IQR > {stats_views['upper_bound']:,.0f}): {stats_views['outlier_count']} video")
    print(f"    * Pencilan likes (Q3 + 1.5*IQR > {stats_likes['upper_bound']:,.0f}): {stats_likes['outlier_count']} video")

    # B. Data Transformation & Scaling: Min-Max [0, 1] dan Z-Score
    print("  - Menghitung normalisasi Min-Max [0, 1] dan Z-Score untuk fitur numerik...")
    numeric_cols = [
        "view_count",
        "like_count",
        "dislike_count_est",
        "comment_count",
        "engagement_rate",
        "views_per_day",
    ]

    for col in numeric_cols:
        df_vid_clean[f"{col}_minmax"] = min_max_normalize(df_vid_clean[col]).round(6)
        df_vid_clean[f"{col}_zscore"] = z_score_normalize(df_vid_clean[col]).round(6)

    output_vid_path = os.path.join(output_dir, "dataset_video_clean.csv")
    df_vid_clean.to_csv(output_vid_path, index=False)
    print(f"  -> Disimpan ke: {output_vid_path} ({len(df_vid_clean)} baris, {len(df_vid_clean.columns)} kolom)")

    report["video"] = {
        "raw_total": total_raw_vid,
        "clean_total": len(df_vid_clean),
        "outlier_views_stats": stats_views,
        "outlier_likes_stats": stats_likes,
        "normalized_features": numeric_cols,
        "scaling_summary": {
            col: {
                "raw_min": float(df_vid_clean[col].min()),
                "raw_max": float(df_vid_clean[col].max()),
                "raw_mean": float(round(df_vid_clean[col].mean(), 2)),
                "minmax_range": [float(df_vid_clean[f"{col}_minmax"].min()), float(df_vid_clean[f"{col}_minmax"].max())],
                "zscore_mean": float(round(df_vid_clean[f"{col}_zscore"].mean(), 4)),
            }
            for col in numeric_cols
        }
    }

    # -------------------------------------------------------------
    # 3. VERIFIKASI INTEGRITAS RELASIONAL
    # -------------------------------------------------------------
    print("\n[3/4] Memvalidasi Integritas Relasi (Foreign Key video_id)...")
    vid_ids = set(df_vid_clean["video_id"])
    kom_vid_ids = set(df_kom_clean["video_id"])
    unmatched_ids = kom_vid_ids - vid_ids
    print(f"  - Video ID unik pada video table: {len(vid_ids)}")
    print(f"  - Video ID unik pada komentar table: {len(kom_vid_ids)}")
    print(f"  - Video ID komentar tanpa referensi video: {len(unmatched_ids)} (Harus 0)")

    # -------------------------------------------------------------
    # 4. MENYIMPAN LAPORAN METRIK BEFORE VS AFTER
    # -------------------------------------------------------------
    print("\n[4/4] Menyimpan Laporan Preprocessing...")
    report_json_path = os.path.join(output_dir, "laporan_preprocessing.json")
    with open(report_json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"  -> Laporan JSON: {report_json_path}")

    # Simpan juga dalam format Markdown agar mudah dibaca / disalin ke makalah
    report_md_path = os.path.join(output_dir, "ringkasan_perbandingan_preprocessing.md")
    with open(report_md_path, "w", encoding="utf-8") as f:
        f.write("# Ringkasan Perbandingan Sebelum vs Sesudah Preprocessing\n\n")
        f.write("## 1. Dataset Komentar Netizen\n")
        f.write(f"- **Jumlah Baris Mentah**: {total_raw_kom:,}\n")
        f.write(f"- **Baris Null Dieliminasi**: {null_kom_count}\n")
        f.write(f"- **Baris Kosong Pasca-Cleaning Dieliminasi**: {empty_after_clean}\n")
        f.write(f"- **Jumlah Baris Bersih**: {len(df_kom_clean):,}\n")
        f.write("- **Preservasi Privasi**: Kolom `author` telah di-anonymize (dihapus).\n\n")

        f.write("### Contoh Perbandingan Teks Komentar (Before vs After):\n\n")
        f.write("| No | Sebelum (Raw) | Sesudah (Clean) |\n")
        f.write("|:---|:---|:---|\n")
        for i, sample in enumerate(report["komentar"]["sample_comparisons"], start=1):
            f.write(f"| {i} | {sample['raw']} | {sample['clean']} |\n")

        f.write("\n---\n\n## 2. Dataset Video\n")
        f.write(f"- **Total Video**: {total_raw_vid}\n")
        f.write(f"- **Pencilan Views (IQR Rule)**: {stats_views['outlier_count']} video (Ambang batas atas: {stats_views['upper_bound']:,.0f})\n")
        f.write(f"- **Pencilan Likes (IQR Rule)**: {stats_likes['outlier_count']} video (Ambang batas atas: {stats_likes['upper_bound']:,.0f})\n\n")

        f.write("### Tabel Transformasi & Normalisasi Skala Numerik:\n\n")
        f.write("| Fitur | Raw Min | Raw Max | Raw Mean | Min-Max Range | Z-Score Mean |\n")
        f.write("|:---|:---|:---|:---|:---|:---|\n")
        for col, s in report["video"]["scaling_summary"].items():
            f.write(f"| `{col}` | {s['raw_min']:,.2f} | {s['raw_max']:,.2f} | {s['raw_mean']:,.2f} | [{s['minmax_range'][0]}, {s['minmax_range'][1]}] | {s['zscore_mean']} |\n")

    print(f"  -> Ringkasan Markdown: {report_md_path}")
    print("\n" + "=" * 60)
    print("PREPROCESSING SELESAI 100% SUKSES!")
    print("=" * 60)

    return report


if __name__ == "__main__":
    preprocess_datasets()

