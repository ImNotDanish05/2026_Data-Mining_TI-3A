"""
Unit test suite untuk memvalidasi fungsi kalkulasi, sanitasi, parser URL, dan mocking API collector.
"""

from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from googleapiclient.errors import HttpError
from httplib2 import Response

from collector import (
    YouTubeDataCollector,
    calculate_metrics,
    clean_text,
    extract_video_id,
    parse_duration_to_seconds,
)
from main import read_input_csv


class TestURLAndTextParsing:
    def test_extract_video_id_variants(self):
        expected_id = "dQw4w9WgXcQ"
        test_urls = [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "http://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=share",
            "https://youtu.be/dQw4w9WgXcQ",
            "https://www.youtube.com/shorts/dQw4w9WgXcQ",
            "https://www.youtube.com/live/dQw4w9WgXcQ",
            "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "dQw4w9WgXcQ",
        ]
        for url in test_urls:
            assert extract_video_id(url) == expected_id

    def test_extract_video_id_invalid(self):
        assert extract_video_id("") is None
        assert extract_video_id(None) is None
        assert extract_video_id("https://google.com") is None
        assert extract_video_id("short") is None

    def test_clean_text(self):
        raw_text = "Ini baris 1.\nIni baris 2.\r\nDan ini \ttab  berjarak."
        cleaned = clean_text(raw_text)
        assert "\n" not in cleaned
        assert "\r" not in cleaned
        assert "\t" not in cleaned
        assert cleaned == "Ini baris 1. Ini baris 2. Dan ini tab berjarak."

    def test_clean_text_none_or_empty(self):
        assert clean_text("") == ""
        assert clean_text(None) == ""


class TestMetricCalculations:
    def test_parse_duration_to_seconds(self):
        assert parse_duration_to_seconds("PT15M33S") == 933
        assert parse_duration_to_seconds("PT1H2M3S") == 3723
        assert parse_duration_to_seconds("PT45S") == 45
        assert parse_duration_to_seconds("") == 0
        assert parse_duration_to_seconds("invalid_duration") == 0

    def test_calculate_metrics_normal(self):
        # 1000 views, 100 likes, 25 dislikes, 15 comments
        # dislike_ratio = 25 / (100 + 25) = 25 / 125 = 0.2
        # engagement_rate = ((100 + 25 + 15) / 1000) * 100 = (140 / 1000) * 100 = 14.0
        # published 2 days ago
        ref_time = datetime(2026, 1, 3, 12, 0, 0, tzinfo=timezone.utc)
        pub_at = "2026-01-01T12:00:00Z"
        ratio, eng_rate, vpd = calculate_metrics(
            views=1000,
            likes=100,
            dislikes=25,
            comment_count=15,
            published_at=pub_at,
            reference_time=ref_time,
        )
        assert ratio == 0.2
        assert eng_rate == 14.0
        assert vpd == 500.0  # 1000 views / 2 days

    def test_calculate_metrics_zero_views_and_votes(self):
        ratio, eng_rate, vpd = calculate_metrics(
            views=0,
            likes=0,
            dislikes=0,
            comment_count=0,
            published_at="2026-01-01T00:00:00Z",
        )
        assert ratio == 0.0
        assert eng_rate == 0.0
        assert vpd == 0.0


class TestRYDFetcher:
    @patch("requests.get")
    def test_fetch_ryd_success(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "dislikes": 350,
            "rawLikes": 2000,
            "rawDislikes": 300,
        }
        mock_get.return_value = mock_resp

        collector = YouTubeDataCollector(api_key="dummy_key")
        res = collector.fetch_ryd_dislikes("dummy_video_id")

        assert res["dislike_count_est"] == 350
        assert res["raw_likes_ryd"] == 2000
        assert res["raw_dislikes_ryd"] == 300

    @patch("requests.get")
    def test_fetch_ryd_failure_fallback(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_get.return_value = mock_resp

        collector = YouTubeDataCollector(api_key="dummy_key")
        res = collector.fetch_ryd_dislikes("dummy_video_id")

        # Fallback to zero
        assert res["dislike_count_est"] == 0
        assert res["raw_likes_ryd"] == 0
        assert res["raw_dislikes_ryd"] == 0


class TestYouTubeAPIInteractions:
    @patch("collector.build")
    def test_fetch_video_details_complete(self, mock_build):
        mock_youtube = MagicMock()
        mock_build.return_value = mock_youtube

        # Setup mock video response
        mock_videos_req = MagicMock()
        mock_videos_req.execute.return_value = {
            "items": [
                {
                    "snippet": {
                        "title": "Debat Capres Cawapres",
                        "channelTitle": "Kanal Berita",
                        "publishedAt": "2026-02-01T10:00:00Z",
                        "categoryId": "25",
                    },
                    "contentDetails": {
                        "duration": "PT30M",
                    },
                    "statistics": {
                        "viewCount": "50000",
                        "likeCount": "4000",
                        "commentCount": "500",
                    },
                }
            ]
        }
        mock_youtube.videos().list.return_value = mock_videos_req

        collector = YouTubeDataCollector(api_key="dummy_key")
        with patch.object(
            collector,
            "fetch_ryd_dislikes",
            return_value={"dislike_count_est": 1000, "raw_likes_ryd": 3800, "raw_dislikes_ryd": 950},
        ):
            record = collector.fetch_video_details(
                video_id="dummy_video_id",
                topik_video="Debat Pemilu",
                tipe_video="Talkshow",
                channel_video="KanalManual",
            )

        assert record is not None
        assert record["video_id"] == "dummy_video_id"
        assert record["title"] == "Debat Capres Cawapres"
        assert record["channel_title"] == "Kanal Berita"
        assert record["duration_seconds"] == 1800
        assert record["view_count"] == 50000
        assert record["like_count"] == 4000
        assert record["dislike_count_est"] == 1000
        assert record["topik_video"] == "Debat Pemilu"
        assert record["tipe_video"] == "Talkshow"
        assert record["channel_video"] == "KanalManual"
        assert "dislike_ratio" in record
        assert "engagement_rate" in record
        assert "views_per_day" in record

    @patch("collector.build")
    def test_fetch_video_comments_disabled(self, mock_build):
        mock_youtube = MagicMock()
        mock_build.return_value = mock_youtube

        mock_comments_req = MagicMock()
        # Simulate commentsDisabled HttpError
        http_resp = Response({"status": "403"})
        mock_comments_req.execute.side_effect = HttpError(
            resp=http_resp,
            content=b'{"error": {"errors": [{"reason": "commentsDisabled"}]}}',
        )
        mock_youtube.commentThreads().list.return_value = mock_comments_req

        collector = YouTubeDataCollector(api_key="dummy_key")
        comments = collector.fetch_video_comments(video_id="disabled_id", max_comments=50)

        # Should handle gracefully and return empty list
        assert comments == []


class TestInputCSVReader:
    def test_read_input_csv_template(self):
        template_path = Path(__file__).parent / "input_videos_template.csv"
        records = read_input_csv(str(template_path))
        assert len(records) >= 2
        first = records[0]
        assert "video_id" in first
        assert "topik_video" in first
        assert "tipe_video" in first
        assert "channel_video" in first
        assert len(first["video_id"]) == 11
        assert first["channel_video"] == "Caveine"

