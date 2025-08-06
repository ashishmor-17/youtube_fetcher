# -*- coding: utf-8 -*-
from django.urls import path
from .views import VideoListAPIView, video_list, video_dashboard

urlpatterns = [
    path("videos/", VideoListAPIView.as_view(), name="video-list"),
    path("", video_list, name="video-list-frontend"),
    path("dashboard/", video_dashboard, name="dashboard"),
]
