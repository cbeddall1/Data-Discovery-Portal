#!/bin/sh
# entrypoint.sh - ensure $PORT is set and start gunicorn
set -eu

# Default to 5000 if PORT not set
: ${PORT:=5000}

echo "[entrypoint] Starting gunicorn on 0.0.0.0:${PORT}"
echo "[entrypoint] Environment: PORT=${PORT} FLASK_ENV=${FLASK_ENV:-unset} FLASK_DEBUG=${FLASK_DEBUG:-unset}"

# Exec gunicorn so signals are forwarded to the app process
exec gunicorn --bind 0.0.0.0:${PORT} --workers 4 --threads 2 --timeout 60 run:app
