#!/bin/sh

echo "Starting app..."
python3 -m jurigged -v -m app

exec "$@"