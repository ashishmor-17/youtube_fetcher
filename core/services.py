# -*- coding: utf-8 -*-
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from core.models import Video
from datetime import datetime


API_KEYS = os.getenv("YOUTUBE_API_KEYS", "").split(",")
QUERY = os.getenv("YOUTUBE_QUERY", "cricket")
MAX_RESULTS = 10


def fetch_youtube_videos():
    # Get latest saved video time
    latest_video = Video.objects.order_by("-published_at").first()
    if latest_video:
        published_after = latest_video.published_at.isoformat("T") + "Z"
    else:
        published_after = "2024-01-01T00:00:00Z"

    # Try each API key
    for key in API_KEYS:
        try:
            youtube = build("youtube", "v3", developerKey=key)
            req = youtube.search().list(
                q=QUERY,
                part="snippet",
                type="video",
                order="date",
                maxResults=MAX_RESULTS,
                publishedAfter=published_after,
            )
            response = req.execute()

            # Save only new videos
            save_videos(response)
            return response
        except HttpError as e:
            if e.resp.status in [403, 429]:
                print(f"[YOUTUBE API] Quota exceeded for key: {key}")
                continue  # Try next key
            else:
                raise e

    raise Exception("All API keys exhausted.")


def save_videos(response):
    for item in response.get("items", []):
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]
        title = snippet["title"]
        description = snippet["description"]
        published_at = snippet["publishedAt"]
        thumbnail_url = snippet["thumbnails"]["high"]["url"]

        # Skip if already saved
        if not Video.objects.filter(video_id=video_id).exists():
            Video.objects.create(
                video_id=video_id,
                title=title,
                description=description,
                published_at=datetime.fromisoformat(published_at.replace("Z", "+00:00")),
                thumbnail_url=thumbnail_url,
            )
