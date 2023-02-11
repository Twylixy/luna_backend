#!/bin/bash
source ./.venv/bin/activate

echo "Run migrations"
alembic upgrade head

echo "Starting app..."
uvicorn api.main:app --host 0.0.0.0 --port 8000

exec "$@"