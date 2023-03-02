#!/bin/bash
source ./.venv/bin/activate

echo "Run migrations..."
alembic upgrade head
echo "Migration done."

echo "Starting app..."
python -m api

exec "$@"