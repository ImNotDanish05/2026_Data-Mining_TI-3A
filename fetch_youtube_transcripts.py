"""
Modul: fetch_youtube_transcripts.py
Deskripsi: Mengambil transkrip dari seluruh video YouTube menggunakan youtube-transcript-api
dengan fitur cerdas:
1. Incremental Resume: Menghindari fetch ulang video yang sudah sukses diambil sebelumnya.
2. Jitter / Noise Cooldown: Jeda realistis antar-request (base delay + random noise).
3. Full Automatic VPN Rotation: Jika terkena blokir IP / rate-limit, otomatis merotasi server
   Proton VPN via CLI (protonvpn connect --random), menunggu koneksi stabil, lalu retry otomatis!
4. Auto-Save: Menyimpan progress ke JSON dan Markdown setiap kali ada video yang diproses.
"""

import json
import logging
import os
import random
import subprocess
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
from youtube_transcript_api import (
    CouldNotRetrieveTranscript,
    IpBlocked,
    NoTranscriptFound,
    RequestBlocked,
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


def rotate_protonvpn() -> bool:
    """
    Otomatis mengganti IP menggunakan Proton VPN CLI (connect --random).
    """
    try:
        print("\n" + ">" * 60)
        print("MENGGANTI SERVER PROTON VPN OTOMATIS...")
        print(">" * 60)
        res = subprocess.run(
            ["protonvpn", "connect", "--random"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        output_msg = res.stdout.strip() or res.stderr.strip()
        print(f"Hasil Rotasi VPN: {output_msg}")
        # Beri jeda 8-10 detik agar antarmuka jaringan & DNS stabil
        print("Menunggu antarmuka jaringan VPN stabil (8 detik)...")
        time.sleep(8)
        return res.returncode == 0
    except Exception as e:
        logger.error("Gagal melakukan rotasi VPN via CLI: %s", e)
        return False


def extract_video_transcript(
    api: YouTubeTranscriptApi,
    video_id: str,
    preferred_languages: Optional[List[str]] = None,
    max_retries: int = 3,
) -> Tuple[Dict[str, Any], bool]:
    """
    Mengambil transkrip untuk satu video_id dengan penanganan retry & auto VPN rotation.
    Return: (result_dict, was_rate_limited)
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

    was_blocked = False

    for attempt in range(1, max_retries + 1):
        try:
            transcript_list = api.list(video_id)

            transcript = None
            try:
                transcript = transcript_list.find_transcript(preferred_languages)
            except Exception:
                available = list(transcript_list)
                if available:
                    transcript = available[0]

            if not transcript:
                result["status"] = "no_transcript"
                result["error"] = "Tidak ada transkrip tersedia"
                return result, was_blocked

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
            return result, was_blocked

        except TranscriptsDisabled:
            result["status"] = "disabled"
            result["error"] = "Transkrip dinonaktifkan oleh pemilik video"
            return result, was_blocked

        except NoTranscriptFound:
            result["status"] = "no_transcript"
            result["error"] = "Transkrip tidak ditemukan untuk bahasa yang diminta"
            return result, was_blocked

        except VideoUnavailable:
            result["status"] = "unavailable"
            result["error"] = "Video privat atau tidak tersedia"
            return result, was_blocked

        except (IpBlocked, RequestBlocked, CouldNotRetrieveTranscript) as e:
            err_str = str(e)
            is_ip_block = "blocking requests from your IP" in err_str or isinstance(e, (IpBlocked, RequestBlocked))

            if is_ip_block and attempt < max_retries:
                was_blocked = True
                logger.warning(
                    "Terdeteksi rate-limit YouTube pada percobaan %d/%d untuk video %s!",
                    attempt,
                    max_retries,
                    video_id,
                )
                # Rotasi VPN secara otomatis!
                rotate_protonvpn()
                api = YouTubeTranscriptApi()
                continue
            else:
                result["status"] = "error"
                result["error"] = "IP Rate-Limited / Blocked" if is_ip_block else err_str
                return result, was_blocked

        except Exception as e:
            result["status"] = "error"
            result["error"] = str(e)
            return result, was_blocked

    return result, was_blocked


def save_progress(
    output_json_path: str,
    output_summary_md: str,
    transcripts_map: Dict[str, Dict[str, Any]],
    total_videos: int,
):
    """
    Menyimpan kondisi terkini ke file JSON dan Markdown.
    """
    transcripts_list = list(transcripts_map.values())
    success_count = sum(1 for t in transcripts_list if t["status"] == "success")
    disabled_count = sum(1 for t in transcripts_list if t["status"] == "disabled")
    no_trans_count = sum(1 for t in transcripts_list if t["status"] == "no_transcript")
    error_count = sum(1 for t in transcripts_list if t["status"] == "error")

    payload = {
        "metadata": {
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "total_videos": total_videos,
            "successful_transcripts": success_count,
            "transcripts_disabled": disabled_count,
            "no_transcripts_found": no_trans_count,
            "errors": error_count,
            "success_rate_percent": round((success_count / total_videos) * 100, 2) if total_videos > 0 else 0.0,
        },
        "transcripts": transcripts_list,
    }

    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    with open(output_summary_md, "w", encoding="utf-8") as f:
        f.write("# Ringkasan Hasil Ekstraksi Transkrip YouTube\n\n")
        f.write("## Statistik Ekstraksi Terkini\n")
        f.write(f"- **Total Video**: {total_videos}\n")
        f.write(f"- **Transkrip Berhasil**: {success_count} video ({payload['metadata']['success_rate_percent']}%)\n")
        f.write(f"- **Transkrip Dinonaktifkan**: {disabled_count} video\n")
        f.write(f"- **Tidak Ada Transkrip (Meme/Musik)**: {no_trans_count} video\n")
        f.write(f"- **Gagal / Rate Limited**: {error_count} video\n\n")

        f.write("## Daftar Status Transkrip per Video\n\n")
        f.write("| No | Video ID | Channel | Tipe | Topik | Status | Bahasa | Jumlah Kata | Cuplikan Transkrip Awal |\n")
        f.write("|:---|:---|:---|:---|:---|:---|:---|:---|:---|\n")
        for i, t in enumerate(transcripts_list, start=1):
            snippet = (t["full_text"][:60] + "...") if t["full_text"] else (t.get("error_detail") or "-")
            snippet_escaped = snippet.replace("|", "/")
            lang = t.get("language") or "-"
            words = f"{t.get('word_count', 0):,}" if t["status"] == "success" else "0"
            f.write(f"| {i} | `{t['video_id']}` | {t.get('channel', '')} | {t.get('tipe_video', '')} | {t.get('topik_video', '')} | **{t['status']}** | {lang} | {words} | {snippet_escaped} |\n")


def fetch_all_transcripts(
    input_csv_path: str = "data/processed/dataset_video_clean.csv",
    output_json_path: str = "data/processed/video_transcripts.json",
    output_summary_md: str = "data/processed/ringkasan_transkrip.md",
    base_delay: float = 6.0,
    noise_range: Tuple[float, float] = (2.0, 5.0),
    resume: bool = True,
):
    """
    Eksekusi ekstraksi dengan jeda realistis, auto-resume, dan rotasi Proton VPN otomatis.
    """
    if not os.path.exists(input_csv_path):
        input_csv_path = "data/raw/dataset_video_politik.csv"

    df = pd.read_csv(input_csv_path)
    total_videos = len(df)

    # 1. Load existing cache jika resume diaktifkan
    transcripts_map: Dict[str, Dict[str, Any]] = {}
    if resume and os.path.exists(output_json_path):
        try:
            with open(output_json_path, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                for item in old_data.get("transcripts", []):
                    vid = item.get("video_id")
                    if vid:
                        transcripts_map[vid] = item
            logger.info("Memuat %d entri dari cache sebelumnya.", len(transcripts_map))
        except Exception as e:
            logger.warning("Gagal membaca cache sebelumnya: %s", e)

    api = YouTubeTranscriptApi()

    print("=" * 65)
    print("MEMULAI PENGAMBILAN TRANSKRIP (FULL OTOMATIS + ROTASI PROTON VPN)")
    print("=" * 65)

    for idx, row in df.iterrows():
        video_id = str(row["video_id"])
        title = str(row.get("title", ""))
        channel = str(row.get("channel_video", row.get("channel_title", "")))
        topik = str(row.get("topik_video", ""))
        tipe = str(row.get("tipe_video", ""))

        # Cek apakah sudah sukses sebelumnya
        cached = transcripts_map.get(video_id)
        if cached and cached.get("status") == "success":
            print(f"[{idx + 1}/{total_videos}] {video_id} ({channel} - {tipe}): [CACHE SUKSES] {cached['word_count']:,} kata")
            continue

        print(f"[{idx + 1}/{total_videos}] Memproses {video_id} ({channel} - {tipe})...", end=" ", flush=True)

        res, was_blocked = extract_video_transcript(api, video_id)

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
        transcripts_map[video_id] = entry

        # Simpan progress seketika
        save_progress(output_json_path, output_summary_md, transcripts_map, total_videos)

        if res["status"] == "success":
            print(f"SUKSES ({res['word_count']:,} kata, bahasa: {res['language']})")
        else:
            print(f"{res['status'].upper()}: {res['error']}")

        # Cooldown realistis dengan noise acak
        noise = random.uniform(*noise_range)
        sleep_duration = round(base_delay + noise, 2)
        print(f"     -> Jeda santai: {sleep_duration} detik...")
        time.sleep(sleep_duration)

    print("\n" + "=" * 65)
    print("PROSES SELESAI!")
    print(f"Output JSON: {output_json_path}")
    print(f"Output MD  : {output_summary_md}")
    print("=" * 65)


if __name__ == "__main__":
    fetch_all_transcripts()
