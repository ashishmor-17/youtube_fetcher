# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "video_id", "published_at")
    search_fields = ("title", "description", "video_id")
    ordering = ("-published_at",)
