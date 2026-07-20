#!/bin/sh
set -eu

mkdir -p "${DJANGO_DATA_DIR:-/app/data}/media"
python manage.py migrate --noinput
python manage.py check --deploy --fail-level ERROR

exec supervisord -c /app/docker/supervisord.conf
