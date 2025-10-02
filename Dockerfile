FROM python:3.11-slim 
FROM python:3.11-slim 
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
     PYTHONUNBUFFERED=1 \
     FLASK_APP=run.py
RUN apt-get update && apt-get install -y --no-install-recommends \
     gcc \
     && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
     pip install --no-cache-dir -r requirements.txt

COPY . .
RUN useradd -m -u 1000 appuser && \
     chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
COPY --chown=appuser:appuser entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD [""]
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 4 --threads 2 --timeout 60 run:app"]