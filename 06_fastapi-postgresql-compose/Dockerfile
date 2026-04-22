# DC-02: FastAPI + PostgreSQL compose.yaml from scratch
# Ref: (self-authored – no official URL for this exercise)
# TODO: Fill this file following the lesson guide.

# Base image
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Export port
EXPOSE 8000

# Start uvicorn
CMD ["uvicorn", "app.main.app", "--host", "0.0.0.0", "--port", "8000"]
