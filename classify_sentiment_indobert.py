"""
Modul: classify_sentiment_indobert.py
Deskripsi: Mengklasifikasikan sentimen / sikap (Mendukung, Menolak, Netral)
pada 5.207 komentar YouTube menggunakan model Transformer Bahasa Indonesia
(w11wo/indonesian-roberta-base-sentiment-classifier) yang berjalan 100% lokal di CPU.
Bobot model tersimpan aman di folder lokal ./models/ (tidak menyentuh root/home).
"""

import json
import logging
import os
import sys
import time
from typing import Dict, List, Tuple

# KUNCI 100% LOKAL: Arahkan cache Hugging Face ke folder ./models di workspace ini
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")
os.makedirs(MODELS_DIR, exist_ok=True)
os.environ["HF_HOME"] = MODELS_DIR
os.environ["TRANSFORMERS_CACHE"] = MODELS_DIR

import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Model Transformer Bahasa Indonesia resmi teruji (100k+ downloads)
MODEL_NAME = "w11wo/indonesian-roberta-base-sentiment-classifier"


def load_model_pipeline(model_name: str = MODEL_NAME):
    """
    Memuat tokenizer dan model Indo-RoBERTa dari folder lokal ./models/
    """
    logger.info("Memuat model NLP: %s", model_name)
    logger.info("Direktori cache lokal: %s", MODELS_DIR)

    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=MODELS_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir=MODELS_DIR)
    model.eval()

    device = torch.device("cpu")
    model.to(device)

    logger.info("Model berhasil dimuat ke perangkat: %s", device)
    return tokenizer, model, device


def map_sentiment_label(raw_label: str) -> str:
    """
    Memetakan label output model menjadi sikap warganet:
    - positive -> Mendukung
    - negative -> Menolak
    - neutral  -> Netral
    """
    norm = str(raw_label).lower().strip()
    if "positive" in norm or "pos" in norm:
        return "Mendukung"
    elif "negative" in norm or "neg" in norm:
        return "Menolak"
    else:
        return "Netral"


def classify_all_comments(
    input_csv: str = "data/processed/dataset_komentar_clean.csv",
    video_meta_csv: str = "data/processed/dataset_video_clean.csv",
    output_csv: str = "data/processed/dataset_komentar_labeled.csv",
    output_md: str = "data/processed/ringkasan_hasil_sentimen.md",
    batch_size: int = 64,
):
    """
    Menjalankan inferensi batch pada seluruh 5.207 komentar YouTube.
    """
    if not os.path.exists(input_csv):
        logger.error("File input tidak ditemukan: %s", input_csv)
        return

    df = pd.read_csv(input_csv)
    total_comments = len(df)
    logger.info("Membaca %d baris komentar bersih dari: %s", total_comments, input_csv)

    tokenizer, model, device = load_model_pipeline()
    id2label = model.config.id2label or {0: "positive", 1: "neutral", 2: "negative"}
    logger.info("Konfigurasi id2label: %s", id2label)

    texts = df["comment_text_clean"].fillna("").astype(str).tolist()

    predicted_labels = []
    confidence_scores = []

    print("\n" + "=" * 65)
    print("MEMULAI KLASIFIKASI SENTIMEN LOKAL (BATCH INFERENCE CPU)")
    print(f"Total Komentar: {total_comments:,} baris | Batch Size: {batch_size}")
    print("=" * 65)

    start_time = time.time()
    total_batches = (total_comments + batch_size - 1) // batch_size

    with torch.no_grad():
        for i in range(0, total_comments, batch_size):
            batch_texts = texts[i : i + batch_size]
            current_batch = (i // batch_size) + 1

            # Tokenisasi dengan padding dan max_length efisien
            inputs = tokenizer(
                batch_texts,
                padding=True,
                truncation=True,
                max_length=96,
                return_tensors="pt",
            ).to(device)

            outputs = model(**inputs)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=1).cpu().numpy()

            preds = np.argmax(probs, axis=1)
            confs = np.max(probs, axis=1)

            for pred_idx, conf in zip(preds, confs):
                raw_label = id2label.get(pred_idx, f"LABEL_{pred_idx}")
                std_label = map_sentiment_label(raw_label)
                predicted_labels.append(std_label)
                confidence_scores.append(round(float(conf), 4))

            # Progress update
            processed_count = min(i + batch_size, total_comments)
            pct = (processed_count / total_comments) * 100
            elapsed = time.time() - start_time
            speed = processed_count / elapsed if elapsed > 0 else 0
            eta_seconds = (total_comments - processed_count) / speed if speed > 0 else 0

            sys.stdout.write(
                f"\rProgress: [{current_batch}/{total_batches}] {processed_count:,}/{total_comments:,} "
                f"({pct:.1f}%) | Kecepatan: {speed:.1f} teks/detik | Sisa waktu: {eta_seconds:.0f}s "
            )
            sys.stdout.flush()

    print("\n" + "=" * 65)
    total_time = time.time() - start_time
    print(f"KLASIFIKASI SELESAI dalam {total_time:.1f} detik ({total_comments:,} komentar)")
    print("=" * 65)

    df["sentimen"] = predicted_labels
    df["confidence_score"] = confidence_scores

    # Hubungkan dengan metadata video (topik & tipe video) untuk analisis silang
    if os.path.exists(video_meta_csv):
        df_vid = pd.read_csv(video_meta_csv)[["video_id", "topik_video", "tipe_video", "channel_video"]]
        df = df.merge(df_vid, on="video_id", how="left")

    # Simpan dataset hasil klasifikasi ke CSV
    df.to_csv(output_csv, index=False)
    logger.info("Dataset berlabel tersimpan di: %s", output_csv)

    # Buat Ringkasan Statistik untuk Makalah
    dist_total = df["sentimen"].value_counts()
    pct_total = (df["sentimen"].value_counts(normalize=True) * 100).round(2)

    with open(output_md, "w", encoding="utf-8") as f:
        f.write("# Ringkasan Hasil Klasifikasi Sentimen Opini Publik (Indo-RoBERTa)\n\n")
        f.write(f"- **Total Komentar Dianalisis**: {total_comments:,} baris\n")
        f.write(f"- **Waktu Pemrosesan CPU**: {total_time:.1f} detik ({total_comments / total_time:.1f} komentar/detik)\n")
        f.write(f"- **Rata-rata Tingkat Keyakinan (Confidence Score)**: {df['confidence_score'].mean() * 100:.2f}%\n\n")

        f.write("## 1. Distribusi Sikap Warganet Keseluruhan\n\n")
        f.write("| Kategori Sikap | Jumlah Komentar | Persentase (%) |\n")
        f.write("|:---|:---:|:---:|\n")
        for label in ["Mendukung", "Menolak", "Netral"]:
            c = dist_total.get(label, 0)
            p = pct_total.get(label, 0.0)
            f.write(f"| **{label}** | {c:,} | {p:.2f}% |\n")
        f.write(f"| **TOTAL** | **{total_comments:,}** | **100.0%** |\n\n")

        if "topik_video" in df.columns:
            f.write("## 2. Distribusi Sikap Berdasarkan Topik Kebijakan\n\n")
            ct_topik = pd.crosstab(df["topik_video"], df["sentimen"], normalize="index") * 100
            ct_topik_count = pd.crosstab(df["topik_video"], df["sentimen"])
            f.write("| Topik Video | Mendukung (%) | Menolak (%) | Netral (%) | Total Komentar |\n")
            f.write("|:---|:---:|:---:|:---:|:---:|\n")
            for topik in ct_topik.index:
                p_dukung = ct_topik.loc[topik].get("Mendukung", 0.0)
                p_tolak = ct_topik.loc[topik].get("Menolak", 0.0)
                p_netral = ct_topik.loc[topik].get("Netral", 0.0)
                t_count = ct_topik_count.loc[topik].sum()
                f.write(f"| `{topik}` | {p_dukung:.2f}% | {p_tolak:.2f}% | {p_netral:.2f}% | {t_count:,} |\n")

        if "tipe_video" in df.columns:
            f.write("\n## 3. Distribusi Sikap Berdasarkan Format/Tipe Konten Video\n\n")
            ct_tipe = pd.crosstab(df["tipe_video"], df["sentimen"], normalize="index") * 100
            f.write("| Tipe Konten | Mendukung (%) | Menolak (%) | Netral (%) |\n")
            f.write("|:---|:---:|:---:|:---:|\n")
            for tipe in ct_tipe.index:
                p_dukung = ct_tipe.loc[tipe].get("Mendukung", 0.0)
                p_tolak = ct_tipe.loc[tipe].get("Menolak", 0.0)
                p_netral = ct_tipe.loc[tipe].get("Netral", 0.0)
                f.write(f"| `{tipe}` | {p_dukung:.2f}% | {p_tolak:.2f}% | {p_netral:.2f}% |\n")

        f.write("\n## 4. Contoh Komentar Nyata Berdasarkan Klasifikasi Model\n\n")
        f.write("### A. Contoh Komentar Mendukung (Skor Keyakinan Tertinggi):\n")
        pro_samples = df[df["sentimen"] == "Mendukung"].sort_values(by="confidence_score", ascending=False).head(4)
        for _, row in pro_samples.iterrows():
            f.write(f"- *\"{row['comment_text_clean']}\"* (Keyakinan: {row['confidence_score'] * 100:.1f}%)\n")

        f.write("\n### B. Contoh Komentar Menolak (Skor Keyakinan Tertinggi):\n")
        contra_samples = df[df["sentimen"] == "Menolak"].sort_values(by="confidence_score", ascending=False).head(4)
        for _, row in contra_samples.iterrows():
            f.write(f"- *\"{row['comment_text_clean']}\"* (Keyakinan: {row['confidence_score'] * 100:.1f}%)\n")

        f.write("\n### C. Contoh Komentar Netral:\n")
        neutral_samples = df[df["sentimen"] == "Netral"].sort_values(by="confidence_score", ascending=False).head(4)
        for _, row in neutral_samples.iterrows():
            f.write(f"- *\"{row['comment_text_clean']}\"* (Keyakinan: {row['confidence_score'] * 100:.1f}%)\n")

    logger.info("Laporan ringkasan sentimen tersimpan di: %s", output_md)
    print(f"\nRingkasan laporan: {output_md}")
    return df


if __name__ == "__main__":
    classify_all_comments()
