#!/bin/sh
# entrypoint.sh - ensure $PORT is set and start gunicorn

# Default to 5000 if PORT not set
: ${PORT:=5000}

echo "Starting gunicorn on 0.0.0.0:${PORT}"

# Exec gunicorn (replace process so signals are forwarded correctly)
exec gunicorn --bind 0.0.0.0:${PORT} --workers 4 --threads 2 --timeout 60 run:app
