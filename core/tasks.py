from celery import shared_task
from .services import fetch_youtube_videos
from .models import Video
from django.utils.dateparse import parse_datetime


@shared_task
def poll_youtube():
    data = fetch_youtube_videos()
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]
        Video.objects.get_or_create(
            video_id=video_id,
            defaults={
                "title": snippet["title"],
                "description": snippet["description"],
                "published_at": parse_datetime(snippet["publishedAt"]),
                "thumbnail_url": snippet["thumbnails"]["high"]["url"],
            },
        )
