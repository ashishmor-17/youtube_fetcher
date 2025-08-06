from django.db import models


class Video(models.Model):
    video_id = models.CharField(max_length=100, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField(db_index=True)
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
