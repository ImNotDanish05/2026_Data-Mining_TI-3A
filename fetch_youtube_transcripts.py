"""
Modul: fetch_youtube_transcripts.py
Deskripsi: Mengambil transkrip dari seluruh video YouTube menggunakan library youtube-transcript-api.
Menangani berbagai skenario (transkrip otomatis, manual, disabled, atau tidak ada transkrip).
Menyimpan output dalam format JSON terstruktur di data/processed/video_transcripts.json
dan ringkasan dalam format Markdown.
"""

import json
import logging
import os
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import pandas as pd
from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def extract_video_transcript(
    api: YouTubeTranscriptApi,
    video_id: str,
    preferred_languages: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Mengambil transkrip untuk satu video_id secara aman dengan fallback bahasa.
    """
    if preferred_languages is None:
        preferred_languages = ["id", "en"]

    result: Dict[str, Any] = {
        "status": "pending",
        "language": None,
        "is_generated": None,
        "word_count": 0,
        "char_count": 0,
        "full_text": "",
        "segments": [],
        "error": None,
    }

    try:
        transcript_list = api.list(video_id)

        transcript = None
        # 1. Coba cari bahasa preferensi (id / en)
        try:
            transcript = transcript_list.find_transcript(preferred_languages)
        except Exception:
            # 2. Fallback: ambil transkrip pertama apa pun yang tersedia
            available = list(transcript_list)
            if available:
                transcript = available[0]

        if not transcript:
            result["status"] = "no_transcript"
            result["error"] = "Tidak ditemukan transkrip yang tersedia"
            return result

        result["language"] = transcript.language_code
        result["is_generated"] = transcript.is_generated

        snippets = transcript.fetch()
        segments = []
        text_parts = []

        for s in snippets:
            clean_s_text = " ".join(s.text.split())
            if clean_s_text:
                text_parts.append(clean_s_text)
                segments.append({
                    "start": round(s.start, 2),
                    "duration": round(s.duration, 2),
                    "text": clean_s_text,
                })

        full_text = " ".join(text_parts)
        result["status"] = "success"
        result["full_text"] = full_text
        result["word_count"] = len(full_text.split()) if full_text else 0
        result["char_count"] = len(full_text)
        result["segments"] = segments
        return result

    except TranscriptsDisabled:
        result["status"] = "disabled"
        result["error"] = "Transkrip dinonaktifkan oleh pembuat video"
        return result
    except NoTranscriptFound:
        result["status"] = "no_transcript"
        result["error"] = "Transkrip tidak ditemukan untuk bahasa yang diminta"
        return result
    except VideoUnavailable:
        result["status"] = "unavailable"
        result["error"] = "Video bersifat privat atau tidak tersedia"
        return result
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        return result


def fetch_all_transcripts(
    input_csv_path: str = "data/processed/dataset_video_clean.csv",
    output_json_path: str = "data/processed/video_transcripts.json",
    output_summary_md: str = "data/processed/ringkasan_transkrip.md",
    delay_between_requests: float = 0.5,
) -> Dict[str, Any]:
    """
    Iterasi seluruh video dari dataset dan simpan hasilnya.
    """
    if not os.path.exists(input_csv_path):
        # Fallback ke raw jika clean belum ada
        input_csv_path = "data/raw/dataset_video_politik.csv"

    logger.info("Membaca daftar video dari: %s", input_csv_path)
    df = pd.read_csv(input_csv_path)
    total_videos = len(df)
    logger.info("Total video yang akan diproses: %d video", total_videos)

    api = YouTubeTranscriptApi()
    transcripts_data = []

    success_count = 0
    disabled_count = 0
    no_transcript_count = 0
    error_count = 0

    print("=" * 60)
    print("MEMULAI PENGAMBILAN TRANSKRIP YOUTUBE")
    print("=" * 60)

    for idx, row in df.iterrows():
        video_id = str(row["video_id"])
        title = str(row.get("title", ""))
        channel = str(row.get("channel_video", row.get("channel_title", "")))
        topik = str(row.get("topik_video", ""))
        tipe = str(row.get("tipe_video", ""))

        print(f"[{idx + 1}/{total_videos}] Memproses video: {video_id} ({channel} - {tipe})...", end=" ", flush=True)

        res = extract_video_transcript(api, video_id)

        entry = {
            "video_id": video_id,
            "title": title,
            "channel": channel,
            "topik_video": topik,
            "tipe_video": tipe,
            "status": res["status"],
            "language": res["language"],
            "is_generated": res["is_generated"],
            "word_count": res["word_count"],
            "char_count": res["char_count"],
            "error_detail": res["error"],
            "full_text": res["full_text"],
            "segments": res["segments"],
        }
        transcripts_data.append(entry)

        if res["status"] == "success":
            success_count += 1
            print(f"SUKSES ({res['word_count']:,} kata, bahasa: {res['language']})")
        elif res["status"] == "disabled":
            disabled_count += 1
            print("DINONAKTIFKAN")
        elif res["status"] == "no_transcript":
            no_transcript_count += 1
            print("TIDAK ADA TRANSKRIP (misal: musik/meme)")
        else:
            error_count += 1
            print(f"GAGAL: {res['error']}")

        # Jeda sejenak untuk menghindari rate limit YouTube
        if delay_between_requests > 0:
            time.sleep(delay_between_requests)

    # Susun payload JSON lengkap
    output_payload = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_videos": total_videos,
            "successful_transcripts": success_count,
            "transcripts_disabled": disabled_count,
            "no_transcripts_found": no_transcript_count,
            "other_errors": error_count,
            "success_rate_percent": round((success_count / total_videos) * 100, 2) if total_videos > 0 else 0.0,
        },
        "transcripts": transcripts_data,
    }

    # Simpan file JSON
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, indent=2, ensure_ascii=False)
    logger.info("Transkrip berhasil disimpan ke JSON: %s", output_json_path)

    # Simpan ringkasan Markdown
    with open(output_summary_md, "w", encoding="utf-8") as f:
        f.write("# Ringkasan Hasil Ekstraksi Transkrip YouTube\n\n")
        f.write("## Statistik Ekstraksi\n")
        f.write(f"- **Total Video Dianalisis**: {total_videos}\n")
        f.write(f"- **Transkrip Berhasil Diambil**: {success_count} video ({output_payload['metadata']['success_rate_percent']}%)\n")
        f.write(f"- **Transkrip Dinonaktifkan**: {disabled_count} video\n")
        f.write(f"- **Tidak Ada Transkrip (Meme/Musik)**: {no_transcript_count} video\n")
        f.write(f"- **Error Lainnya**: {error_count} video\n\n")

        f.write("## Daftar Status Transkrip per Video\n\n")
        f.write("| No | Video ID | Channel | Tipe | Topik | Status | Bahasa | Jumlah Kata | Cuplikan Transkrip Awal |\n")
        f.write("|:---|:---|:---|:---|:---|:---|:---|:---|:---|\n")
        for i, t in enumerate(transcripts_data, start=1):
            snippet = (t["full_text"][:60] + "...") if t["full_text"] else (t["error_detail"] or "-")
            snippet_escaped = snippet.replace("|", "/")
            lang = t["language"] or "-"
            words = f"{t['word_count']:,}" if t["status"] == "success" else "0"
            f.write(f"| {i} | `{t['video_id']}` | {t['channel']} | {t['tipe_video']} | {t['topik_video']} | **{t['status']}** | {lang} | {words} | {snippet_escaped} |\n")

    logger.info("Ringkasan Markdown disimpan ke: %s", output_summary_md)

    print("\n" + "=" * 60)
    print(f"SELESAI! Sukses: {success_count}/{total_videos} video.")
    print(f"Output JSON: {output_json_path}")
    print(f"Output MD  : {output_summary_md}")
    print("=" * 60)

    return output_payload


if __name__ == "__main__":
    fetch_all_transcripts()

