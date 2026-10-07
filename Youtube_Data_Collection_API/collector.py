"""
Modul Collector untuk ekstraksi data YouTube Data API v3 dan Return YouTube Dislike (RYD) API.
Mematuhi prinsip netralitas data, efisiensi kuota, dan penanganan error yang kuat.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import isodate
import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

logger = logging.getLogger(__name__)

RYD_ENDPOINT = "https://returnyoutubedislikeapi.com/votes?videoId={video_id}"


def extract_video_id(url_or_id: str) -> Optional[str]:
    """
    Mengekstraksi YouTube video ID (11 karakter) dari berbagai format URL atau ID mentah.
    
    Contoh format yang didukung:
    - https://www.youtube.com/watch?v=dQw4w9WgXcQ
    - https://youtu.be/dQw4w9WgXcQ
    - https://www.youtube.com/shorts/dQw4w9WgXcQ
    - https://www.youtube.com/live/dQw4w9WgXcQ
    - https://www.youtube.com/embed/dQw4w9WgXcQ
    - dQw4w9WgXcQ
    """
    if not url_or_id:
        return None

    cleaned = url_or_id.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", cleaned):
        return cleaned

    patterns = [
        r"(?:v=|\/v\/|youtu\.be\/|\/embed\/|\/shorts\/|\/live\/)([A-Za-z0-9_-]{11})",
        r"^([A-Za-z0-9_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, cleaned)
        if match:
            return match.group(1)

    return None


def clean_text(text: Optional[str]) -> str:
    """
    Membersihkan teks komentar dari karakter newline, carriage return, dan tab
    agar tidak merusak struktur baris file CSV.
    """
    if not text:
        return ""
    # Ganti karakter whitespace newline & tab menjadi spasi
    cleaned = re.sub(r"[\r\n\t]+", " ", text)
    # Normalkan multiple spasi menjadi spasi tunggal
    return " ".join(cleaned.split())


def parse_duration_to_seconds(duration_str: Optional[str]) -> int:
    """
    Mengonversi durasi format ISO 8601 (contoh: PT15M33S) menjadi detik (Integer).
    """
    if not duration_str:
        return 0
    try:
        duration = isodate.parse_duration(duration_str)
        return int(duration.total_seconds())
    except Exception as e:
        logger.warning("Gagal mem-parsing durasi ISO 8601 '%s': %s", duration_str, e)
        return 0


def calculate_metrics(
    views: int,
    likes: int,
    dislikes: int,
    comment_count: int,
    published_at: str,
    reference_time: Optional[datetime] = None,
) -> Tuple[float, float, float]:
    """
    Menghitung dislike_ratio, engagement_rate, dan views_per_day secara netral dan matematis.
    
    Formula:
    - dislike_ratio = dislikes / (likes + dislikes) [0.0 jika likes + dislikes == 0]
    - engagement_rate = ((likes + dislikes + comment_count) / views) * 100 [0.0 jika views == 0]
    - views_per_day = views / hari_sejak_rilis
    """
    # 1. Dislike Ratio
    total_votes = likes + dislikes
    dislike_ratio = (dislikes / total_votes) if total_votes > 0 else 0.0

    # 2. Engagement Rate
    engagement_rate = (
        ((likes + dislikes + comment_count) / views) * 100.0 if views > 0 else 0.0
    )

    # 3. Views Per Day
    if not reference_time:
        reference_time = datetime.now(timezone.utc)

    try:
        # Support parsing ISO formats with 'Z' or offset
        iso_str = published_at.replace("Z", "+00:00")
        pub_dt = datetime.fromisoformat(iso_str)
        if pub_dt.tzinfo is None:
            pub_dt = pub_dt.replace(tzinfo=timezone.utc)

        delta_seconds = max((reference_time - pub_dt).total_seconds(), 0.0)
        days = delta_seconds / 86400.0
        # Jika video baru saja diunggah (< 1 jam), gunakan floor pecahan hari agar tidak pembagian nol
        safe_days = max(days, 1.0 / 24.0)
        views_per_day = views / safe_days
    except Exception as e:
        logger.warning("Gagal menghitung views_per_day untuk published_at '%s': %s", published_at, e)
        views_per_day = float(views)

    return round(dislike_ratio, 6), round(engagement_rate, 6), round(views_per_day, 4)


class YouTubeDataCollector:
    """
    Client untuk berinteraksi dengan YouTube Data API v3 dan Return YouTube Dislike (RYD) API.
    """

    def __init__(self, api_key: str, ryd_timeout: int = 10):
        if not api_key:
            raise ValueError("YOUTUBE_API_KEY tidak boleh kosong.")
        self.api_key = api_key
        self.ryd_timeout = ryd_timeout
        self.youtube = build("youtube", "v3", developerKey=self.api_key)

    def fetch_ryd_dislikes(self, video_id: str) -> Dict[str, int]:
        """
        Mengambil estimasi dislike dan data vote dari Return YouTube Dislike (RYD) API.
        Fallback ke nilai default 0 jika API gagal merespons, timeout, atau data kosong.
        """
        url = RYD_ENDPOINT.format(video_id=video_id)
        default_result = {
            "dislike_count_est": 0,
            "raw_likes_ryd": 0,
            "raw_dislikes_ryd": 0,
        }

        try:
            response = requests.get(url, timeout=self.ryd_timeout)
            if response.status_code == 200:
                data = response.json()
                return {
                    "dislike_count_est": int(data.get("dislikes") or 0),
                    "raw_likes_ryd": int(data.get("rawLikes") or 0),
                    "raw_dislikes_ryd": int(data.get("rawDislikes") or 0),
                }
            else:
                logger.warning(
                    "RYD API status %s untuk video %s. Menggunakan default 0.",
                    response.status_code,
                    video_id,
                )
                return default_result
        except requests.RequestException as e:
            logger.warning(
                "Gagal menghubungi RYD API untuk video %s (%s). Menggunakan default 0.",
                video_id,
                e,
            )
            return default_result
        except Exception as e:
            logger.warning(
                "Kesalahan pemrosesan data RYD API untuk video %s: %s", video_id, e
            )
            return default_result

    def fetch_video_details(
        self,
        video_id: str,
        topik_video: Optional[str] = None,
        tipe_video: Optional[str] = None,
        channel_video: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Mengambil metadata video dari YouTube Data API v3 digabung dengan estimasi dislike RYD API.
        """
        try:
            request = self.youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_id,
            )
            response = request.execute()
            items = response.get("items", [])
            if not items:
                logger.warning("Video dengan ID %s tidak ditemukan atau bersifat privat.", video_id)
                return None

            item = items[0]
            snippet = item.get("snippet", {})
            content_details = item.get("contentDetails", {})
            statistics = item.get("statistics", {})

            # Ekstraksi statistik dasar YouTube
            title = snippet.get("title", "")
            channel_title = snippet.get("channelTitle", "")
            published_at = snippet.get("publishedAt", "")
            category_id = snippet.get("categoryId", "")
            duration_str = content_details.get("duration", "PT0S")
            duration_seconds = parse_duration_to_seconds(duration_str)

            view_count = int(statistics.get("viewCount", 0))
            like_count = int(statistics.get("likeCount", 0))
            comment_count = int(statistics.get("commentCount", 0))

            # Ambil data dari RYD API
            ryd_data = self.fetch_ryd_dislikes(video_id)
            dislike_count_est = ryd_data["dislike_count_est"]
            raw_likes_ryd = ryd_data["raw_likes_ryd"]
            raw_dislikes_ryd = ryd_data["raw_dislikes_ryd"]

            # Hitung metrik turunan
            dislike_ratio, engagement_rate, views_per_day = calculate_metrics(
                views=view_count,
                likes=like_count,
                dislikes=dislike_count_est,
                comment_count=comment_count,
                published_at=published_at,
            )

            record: Dict[str, Any] = {
                "video_id": video_id,
                "title": title,
                "channel_title": channel_title,
                "published_at": published_at,
                "duration_seconds": duration_seconds,
                "category_id": category_id,
                "view_count": view_count,
                "like_count": like_count,
                "dislike_count_est": dislike_count_est,
                "raw_likes_ryd": raw_likes_ryd,
                "raw_dislikes_ryd": raw_dislikes_ryd,
                "comment_count": comment_count,
                "dislike_ratio": dislike_ratio,
                "engagement_rate": engagement_rate,
                "views_per_day": views_per_day,
            }

            # Tambahkan metadata opsional jika disediakan dari input CSV
            if topik_video is not None:
                record["topik_video"] = topik_video
            if tipe_video is not None:
                record["tipe_video"] = tipe_video
            if channel_video is not None:
                record["channel_video"] = channel_video

            return record

        except HttpError as e:
            logger.error("HTTP error saat mengambil detail video %s: %s", video_id, e)
            return None
        except Exception as e:
            logger.error("Terjadi kesalahan saat memproses video %s: %s", video_id, e)
            return None

    def fetch_video_comments(
        self, video_id: str, max_comments: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Mengambil komentar dari YouTube Data API v3 (endpoint commentThreads).
        Efisiensi kuota: hanya mengambil top-level comments dan membaca totalReplyCount,
        tanpa melakukan iterasi rekursif ke child replies.
        """
        comments: List[Dict[str, Any]] = []
        if max_comments <= 0:
            return comments

        next_page_token: Optional[str] = None
        remaining = max_comments

        try:
            while remaining > 0:
                fetch_count = min(remaining, 100)
                request = self.youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=fetch_count,
                    textFormat="plainText",
                    pageToken=next_page_token,
                )
                response = request.execute()

                items = response.get("items", [])
                if not items:
                    break

                for item in items:
                    snippet = item.get("snippet", {})
                    top_comment = snippet.get("topLevelComment", {}).get("snippet", {})

                    comment_id = item.get("id", "")
                    author = top_comment.get("authorDisplayName", "")
                    raw_text = top_comment.get("textDisplay", "")
                    cleaned_text = clean_text(raw_text)
                    comment_likes = int(top_comment.get("likeCount", 0))
                    total_replies = int(snippet.get("totalReplyCount", 0))
                    published_at = top_comment.get("publishedAt", "")

                    comments.append(
                        {
                            "comment_id": comment_id,
                            "video_id": video_id,
                            "author": author,
                            "comment_text": cleaned_text,
                            "comment_likes": comment_likes,
                            "total_replies": total_replies,
                            "published_at": published_at,
                        }
                    )
                    remaining -= 1
                    if remaining <= 0:
                        break

                next_page_token = response.get("nextPageToken")
                if not next_page_token:
                    break

            return comments

        except HttpError as e:
            # Tangani skenario jika komentar dinonaktifkan
            error_details = str(e)
            if "commentsDisabled" in error_details:
                logger.info("Komentar dinonaktifkan oleh pembuat video untuk ID: %s.", video_id)
            else:
                logger.warning("Gagal mengambil komentar untuk video %s: %s", video_id, e)
            return comments
        except Exception as e:
            logger.warning("Terjadi kesalahan saat mengekstrak komentar video %s: %s", video_id, e)
            return comments

