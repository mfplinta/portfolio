# syntax=docker/dockerfile:1.7
FROM caddy:2.11.4-alpine@sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648 AS caddy
RUN setcap -r /usr/bin/caddy

FROM python:3.13.14-slim-bookworm@sha256:9d7f287598e1a5a978c015ee176d8216435aaf335ed69ac3c38dd1bbb10e8d64

ENV DJANGO_DEBUG=False \
    DJANGO_DATA_DIR=/app/data \
    DJANGO_STATIC_ROOT=/app/staticfiles \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    XDG_CONFIG_HOME=/tmp/caddy-config \
    XDG_DATA_HOME=/tmp/caddy-data

WORKDIR /app

COPY --from=caddy /usr/bin/caddy /usr/bin/caddy
COPY requirements.txt ./
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt \
    && groupadd --system --gid 10001 portfolio \
    && useradd --system --uid 10001 --gid portfolio --home-dir /app --shell /usr/sbin/nologin portfolio

COPY --chown=portfolio:portfolio . .
COPY --chmod=755 docker/entrypoint.sh /usr/local/bin/portfolio-entrypoint

RUN SECRET_KEY=build-only-secret \
    DJANGO_ALLOWED_HOSTS=localhost \
    python manage.py collectstatic --noinput \
    && mkdir -p /app/data/media \
    && chown -R portfolio:portfolio /app/data

USER 10001:10001
EXPOSE 8000
VOLUME ["/app/data"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=3)"]

ENTRYPOINT ["portfolio-entrypoint"]
