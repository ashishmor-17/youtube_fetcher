from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
from datetime import datetime
from django.db.models import Q


class VideoPagination(PageNumberPagination):
    page_size = 10


class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all().order_by("-published_at")
    serializer_class = VideoSerializer
    pagination_class = VideoPagination


def video_list(request):
    videos = Video.objects.order_by("-published_at")
    return render(request, "video_list.html", {"videos": videos})


def video_dashboard(request):
    query = request.GET.get("q", "")
    sort = request.GET.get("sort", "-published_at")
    start_date = request.GET.get("start_date", "")
    end_date = request.GET.get("end_date", "")

    videos = Video.objects.all()

    if query:
        videos = videos.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if start_date:
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            videos = videos.filter(published_at__gte=start)
        except ValueError:
            pass

    if end_date:
        try:
            end = datetime.strptime(end_date, "%Y-%m-%d")
            videos = videos.filter(published_at__lte=end)
        except ValueError:
            pass

    videos = videos.order_by(sort)

    return render(
        request,
        "dashboard.html",
        {"videos": videos, "query": query, "sort": sort, "start_date": start_date, "end_date": end_date},
    )
