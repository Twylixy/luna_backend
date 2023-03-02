#!/bin/bash
source /venv/bin/activate

# Run migrations
alembic upgrade head

# If need debug whole start progress
# python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m api
# Don't wait for client, run immediately
python -m debugpy --listen 0.0.0.0:5678 -m api

exec "$@"