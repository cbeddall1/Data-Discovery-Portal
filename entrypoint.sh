set -eu
: ${PORT:=5000}
echo "[entrypoint] Starting gunicorn on 0.0.0.0:${PORT}"
echo "[entrypoint] Environment: PORT=${PORT} FLASK_ENV=${FLASK_ENV:-unset} FLASK_DEBUG=${FLASK_DEBUG:-unset}"
echo "[entrypoint] Listing /app:"
ls -la /app || true
echo "[entrypoint] Listing /app/app:"
ls -la /app/app || true
echo "[entrypoint] Listing /app/app/static/templates:"
ls -la /app/app/static/templates || true
echo "[entrypoint] Head of /app/app/routes.py"
sed -n '1,40p' /app/app/routes.py || true
echo "[entrypoint] Head of /app/app/__init__.py"
sed -n '1,40p' /app/app/__init__.py || true
exec gunicorn --bind 0.0.0.0:${PORT} --workers 4 --threads 2 --timeout 60 run:app
