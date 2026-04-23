# DC-03: .env, env_file, healthcheck, networks
# Ref: https://docs.docker.com/compose/environment-variables/
# TODO: Fill this file following the lesson guide.

FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
