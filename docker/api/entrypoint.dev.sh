#!/bin/sh

echo "Run migrations"
python3.9 web/manage.py migrate

echo "Starting app..."
python3 web/manage.py runserver 0.0.0.0:8000

exec "$@"