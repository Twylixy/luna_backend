#!/bin/sh

echo "Apply database migrations"
python ./web/manage.py migrate

echo "Starting server"
gunicorn --bind 0.0.0.0:8000 --chdir ./web web.wsgi:application

exec "$@"