# Use official Python runtime as base image 

FROM python:3.11-slim 

 

# Set working directory in container 

WORKDIR /app 

 

# Set environment variables 

ENV PYTHONDONTWRITEBYTECODE=1 \ 

    PYTHONUNBUFFERED=1 \ 

    FLASK_APP=run.py 

 

# Install system dependencies 

RUN apt-get update && apt-get install -y --no-install-recommends \ 

    gcc \ 

    && rm -rf /var/lib/apt/lists/* 

 

# Copy requirements first for better caching 

COPY requirements.txt . 

 

# Install Python dependencies 

RUN pip install --no-cache-dir --upgrade pip && \ 

    pip install --no-cache-dir -r requirements.txt 

 

# Copy application code 

COPY . . 

 

# Create non-root user for security 

RUN useradd -m -u 1000 appuser && \ 

    chown -R appuser:appuser /app 

 

USER appuser 

 

# Expose port (Railway will use PORT env variable) 

EXPOSE 5000 

 

# Use shell form to allow environment variable expansion 

CMD gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 4 --threads 2 --timeout 60 run:app 
