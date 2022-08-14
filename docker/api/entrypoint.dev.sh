#!/bin/sh

cd web/

echo "Creating migrations"
python manage.py makemigrations api

echo "Run migrations"
python manage.py migrate

echo "Starting app..."
python manage.py runserver 0.0.0.0:8000

exec "$@"