"""
Main CLI Script untuk ekstraksi dataset YouTube Data API v3 dan Return YouTube Dislike (RYD) API.
Mendukung input berkas CSV (link_video, topik_video, tipe_video) serta argumen CLI.
"""

from __future__ import annotations

import argparse
import csv
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

from collector import YouTubeDataCollector, extract_video_id

# Konfigurasi Logging informatif dan netral
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("YouTubeDataMining")


def load_environment() -> None:
    """
    Memuat variabel environment dari file .env (mencari di direktori kerja atau folder script).
    """
    script_dir = Path(__file__).resolve().parent
    env_paths = [
        Path.cwd() / ".env",
        script_dir / ".env",
        script_dir.parent / ".env",
    ]
    for env_path in env_paths:
        if env_path.is_file():
            load_dotenv(dotenv_path=env_path)
            logger.info("File konfigurasi .env berhasil dimuat dari: %s", env_path)
            return
    # Coba load default jika ada di path saat ini
    load_dotenv()


def read_input_csv(csv_path: str) -> List[Dict[str, str]]:
    """
    Membaca berkas CSV input yang memuat kolom link_video, topik_video, dan tipe_video.
    Mengekstrak video_id dari link_video.
    """
    path = Path(csv_path)
    if not path.is_file():
        raise FileNotFoundError(f"Berkas CSV input tidak ditemukan: {csv_path}")

    targets: List[Dict[str, str]] = []
    with open(path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        # Normalisasi nama kolom (case-insensitive & strip)
        headers = {col.strip().lower(): col for col in (reader.fieldnames or [])}

        link_col = next((headers[k] for k in ["link_video", "link", "url", "video_url"] if k in headers), None)
        topik_col = next((headers[k] for k in ["topik_video", "topik", "topic"] if k in headers), None)
        tipe_col = next((headers[k] for k in ["tipe_video", "tipe", "type"] if k in headers), None)
        channel_col = next((headers[k] for k in ["channel_video", "channel", "nama_channel"] if k in headers), None)

        if not link_col:
            raise ValueError(
                f"Kolom tautan video tidak ditemukan pada {csv_path}. "
                "Harap sediakan kolom 'link_video'."
            )

        row_num = 1
        for row in reader:
            row_num += 1
            raw_link = (row.get(link_col) or "").strip()
            if not raw_link:
                continue

            v_id = extract_video_id(raw_link)
            if not v_id:
                logger.warning(
                    "Baris %d: Tidak dapat mengekstraksi video ID dari tautan '%s'. Dilewati.",
                    row_num,
                    raw_link,
                )
                continue

            topik = (row.get(topik_col) or "").strip() if topik_col else ""
            tipe = (row.get(tipe_col) or "").strip() if tipe_col else ""
            channel = (row.get(channel_col) or "").strip() if channel_col else ""

            targets.append(
                {
                    "video_id": v_id,
                    "topik_video": topik,
                    "tipe_video": tipe,
                    "channel_video": channel,
                    "original_link": raw_link,
                }
            )

    return targets


def parse_video_ids_string(ids_str: str) -> List[Dict[str, str]]:
    """
    Membaca daftar video ID / URL yang dipisahkan oleh koma atau spasi.
    """
    raw_items = [item.strip() for item in ids_str.replace(",", " ").split() if item.strip()]
    targets: List[Dict[str, str]] = []
    for item in raw_items:
        v_id = extract_video_id(item)
        if v_id:
            targets.append(
                {
                    "video_id": v_id,
                    "topik_video": "",
                    "tipe_video": "",
                    "channel_video": "",
                    "original_link": item,
                }
            )
        else:
            logger.warning("Nilai ID/URL tidak valid: '%s'. Dilewati.", item)
    return targets


def export_to_csv(data: List[Dict[str, Any]], fieldnames: List[str], output_path: Path) -> None:
    """
    Mengekspor list dictionary ke berkas CSV secara terstruktur.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)


def main() -> int:
    load_environment()

    parser = argparse.ArgumentParser(
        description="YouTube & Return YouTube Dislike (RYD) Data Mining Extraction Tool"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=os.getenv("YOUTUBE_API_KEY"),
        help="Google YouTube Data API v3 Key (default: dari .env)",
    )
    parser.add_argument(
        "--input-csv",
        type=str,
        default=os.getenv("INPUT_CSV"),
        help="Jalur berkas CSV yang berisi kolom link_video, topik_video, tipe_video",
    )
    parser.add_argument(
        "--video-ids",
        nargs="*",
        default=[],
        help="Daftar YouTube Video ID atau URL langsung (spasi dipisahkan)",
    )
    parser.add_argument(
        "--max-comments",
        type=int,
        default=int(os.getenv("MAX_COMMENTS", "100")),
        help="Batas maksimum jumlah komentar per video (default: 100)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=os.getenv("OUTPUT_DIR", "."),
        help="Direktori target penyimpanan hasil CSV (default: .)",
    )
    parser.add_argument(
        "--video-output",
        type=str,
        default="dataset_video_politik.csv",
        help="Nama berkas CSV level video (default: dataset_video_politik.csv)",
    )
    parser.add_argument(
        "--comment-output",
        type=str,
        default="dataset_komentar_politik.csv",
        help="Nama berkas CSV level komentar (default: dataset_komentar_politik.csv)",
    )

    args = parser.parse_args()

    api_key = args.api_key
    if not api_key or api_key == "your_youtube_data_api_v3_key_here":
        logger.error(
            "YOUTUBE_API_KEY belum disetel. Sediakan via file .env atau argumen --api-key."
        )
        return 1

    # Identifikasi daftar target video
    targets: List[Dict[str, str]] = []

    # 1. Prioritaskan file input CSV jika diberikan
    if args.input_csv:
        csv_target = Path(args.input_csv)
        # Jika relatif dan tidak ditemukan, cek di folder script
        if not csv_target.is_file() and (Path(__file__).parent / args.input_csv).is_file():
            csv_target = Path(__file__).parent / args.input_csv
        try:
            targets = read_input_csv(str(csv_target))
            logger.info("Memuat %d target video dari CSV: %s", len(targets), csv_target)
        except Exception as e:
            logger.error("Gagal membaca input CSV: %s", e)
            return 1

    # 2. Tambahkan / gabungkan dengan argumen --video-ids jika ada
    if args.video_ids:
        cli_ids = " ".join(args.video_ids)
        parsed_cli = parse_video_ids_string(cli_ids)
        targets.extend(parsed_cli)

    # 3. Fallback ke env VIDEO_IDS jika belum ada target sama sekali
    if not targets and os.getenv("VIDEO_IDS"):
        targets = parse_video_ids_string(os.getenv("VIDEO_IDS", ""))

    if not targets:
        logger.error(
            "Tidak ada target video untuk diproses. Berikan --input-csv atau --video-ids."
        )
        return 1

    # Hapus duplikat video_id dengan mempertahankan urutan
    seen_ids = set()
    unique_targets: List[Dict[str, str]] = []
    for item in targets:
        vid = item["video_id"]
        if vid not in seen_ids:
            seen_ids.add(vid)
            unique_targets.append(item)

    logger.info("Total video unik yang akan diekstraksi: %d", len(unique_targets))
    logger.info("Batas maksimal komentar per video: %d", args.max_comments)

    collector = YouTubeDataCollector(api_key=api_key)

    videos_dataset: List[Dict[str, Any]] = []
    comments_dataset: List[Dict[str, Any]] = []

    total_videos = len(unique_targets)
    for idx, target in enumerate(unique_targets, 1):
        vid = target["video_id"]
        topik = target.get("topik_video", "")
        tipe = target.get("tipe_video", "")
        channel = target.get("channel_video", "")

        info_meta = []
        if topik:
            info_meta.append(f"Topik: {topik}")
        if tipe:
            info_meta.append(f"Tipe: {tipe}")
        if channel:
            info_meta.append(f"Channel: {channel}")
        meta_str = f" ({', '.join(info_meta)})" if info_meta else ""

        logger.info(
            "[%d/%d] Memproses video ID: %s%s...",
            idx,
            total_videos,
            vid,
            meta_str,
        )

        # 1. Ekstraksi detail video & RYD
        video_record = collector.fetch_video_details(
            video_id=vid,
            topik_video=topik,
            tipe_video=tipe,
            channel_video=channel,
        )

        if video_record:
            videos_dataset.append(video_record)
        else:
            logger.warning("Melewati video %s karena data detail gagal diambil.", vid)
            continue

        # 2. Ekstraksi komentar video
        if args.max_comments > 0:
            comments = collector.fetch_video_comments(
                video_id=vid,
                max_comments=args.max_comments,
            )
            comments_dataset.extend(comments)
            logger.info("Berhasil mengumpulkan %d komentar untuk video ID: %s", len(comments), vid)

    # Direktori output
    out_dir = Path(args.output_dir)
    video_out_path = out_dir / args.video_output
    comment_out_path = out_dir / args.comment_output

    # Skema kolom dataset_video_politik.csv
    video_columns = [
        "video_id",
        "title",
        "channel_title",
        "published_at",
        "duration_seconds",
        "category_id",
        "view_count",
        "like_count",
        "dislike_count_est",
        "raw_likes_ryd",
        "raw_dislikes_ryd",
        "comment_count",
        "dislike_ratio",
        "engagement_rate",
        "views_per_day",
        "topik_video",
        "tipe_video",
        "channel_video",
    ]

    # Skema kolom dataset_komentar_politik.csv
    comment_columns = [
        "comment_id",
        "video_id",
        "author",
        "comment_text",
        "comment_likes",
        "total_replies",
        "published_at",
    ]

    export_to_csv(videos_dataset, video_columns, video_out_path)
    export_to_csv(comments_dataset, comment_columns, comment_out_path)

    logger.info("=== PROSES SELESAI ===")
    logger.info("Dataset Video disimpan di   : %s (%d baris)", video_out_path, len(videos_dataset))
    logger.info("Dataset Komentar disimpan di: %s (%d baris)", comment_out_path, len(comments_dataset))

    return 0


if __name__ == "__main__":
    sys.exit(main())

