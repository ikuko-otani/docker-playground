# D-03: Build, Tag, and Run Images
# Ref: https://docs.docker.com/get-started/workshop/03_updating_app/
# TODO: Fill this file following the lesson guide.

# Base image: official Python slim image
FROM python:3.12-slim-bookworm

# Set working directory inside the container
WORKDIR /app

# Copy application source code
COPY app.py .

# Expose the port the app listens on
EXPOSE 8080

# Default command to run the app
CMD ["python", "app.py"]
