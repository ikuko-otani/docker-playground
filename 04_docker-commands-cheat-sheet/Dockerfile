# D-04: Docker Commands Cheat Sheet
# Ref: N/A (Hands-on exercise: ps, logs, exec, stop, rm, image prune)
# TODO: Fill this file following the lesson guide.

FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN pip install fastapi uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
