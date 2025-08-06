<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [YouTube Video Fetcher API](#youtube-video-fetcher-api)
  - [Description](#description)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Environment Setup](#environment-setup)
    - [Run the Project](#run-the-project)
  - [Dashboard](#dashboard)
  - [Notes](#notes)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# YouTube Video Fetcher API

## Description
This Django project fetches and stores the latest YouTube videos using the YouTube Data API v3 in the background, and serves them via a paginated REST API.

## Features
- 🔁 Async fetching every 30 seconds via Celery *(30 seconds for testing — recommended 10–15 mins in production to avoid exhausting API quota)*
- 🔐 API key rotation when quota is exhausted
- 📦 Paginated GET API to retrieve videos
- 🐳 Dockerized deployment for easy setup
- 🖥️ Simple frontend dashboard to view videos

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local dev/testing)
- YouTube Data API v3 keys

### Environment Setup
1. Copy the sample environment file:
   ```bash
   cp .env.sample .env
   ```

2. Fill in your API keys and other configurations in `.env`:
   ```env
   YOUTUBE_API_KEYS=api_key_1,api_key_2
   ```

3. *(Optional)* Add additional search queries:
   ```env
   YOUTUBE_SEARCH_QUERY=cricket,football
   ```

### Run the Project

To build and start everything using Docker Compose:

```bash
docker-compose up --build
```

This will start:
- Django backend (API + dashboard)
- Celery worker (for background tasks)
- Redis (Celery broker)
- PostgreSQL (database)

Visit:
- API: [http://localhost:8000/api/videos/](http://localhost:8000/api/videos/)
- Dashboard: [http://localhost:8000/dashboard](http://localhost:8000/dashboard)

## Dashboard

A simple HTML-based dashboard to view fetched videos:
- See thumbnails, titles, channel names
- Easily test visually if videos are being stored and updated

## Notes
- YouTube API quota is limited (typically 10,000 units/day per key). Keep the polling interval higher in production to avoid exhausting keys.
- Task polling is done using Celery, scheduled via Django-Celery-Beat.
