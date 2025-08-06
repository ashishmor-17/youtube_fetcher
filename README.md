# YouTube Video Fetcher API

## Description
This Django project fetches and stores the latest YouTube videos using the YouTube Data API v3 in the background, and serves them via a paginated REST API.

## Features
- Async fetching every 10 seconds via Celery
- API key rotation when quota exhausted
- Paginated GET API
- Dockerized deployment

## Getting Started

docker-compose up --build
