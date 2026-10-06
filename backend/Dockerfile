# Dockerfile for OreSight Backend Service
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for OCR, PDF rendering and compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    tesseract-ocr \
    tesseract-ocr-eng \
    libmupdf-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
