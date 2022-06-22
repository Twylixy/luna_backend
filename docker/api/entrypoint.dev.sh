#!/bin/sh

echo "Run migrations"
python web/manage.py migrate

echo "Starting app..."
python web/manage.py runserver 0.0.0.0:8000

exec "$@"