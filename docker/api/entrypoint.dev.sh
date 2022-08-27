#!/bin/sh

echo "Run migrations"
alembic upgrade head

echo "Starting app..."
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

exec "$@"