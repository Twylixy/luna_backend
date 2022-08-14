#!/bin/sh

echo "Apply database migrations"
python ./web/manage.py migrate

echo "Collect static files"
python ./web/manage.py collectstatic --no-input

echo "Starting server"
gunicorn --access-logfile /home/luna/gunicorn/access.log --bind 0.0.0.0:8000 --chdir ./web web.wsgi:application

exec "$@"