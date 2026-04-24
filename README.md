![Status](https://img.shields.io/badge/status-active-success?style=flat-square) ![Mode](https://img.shields.io/badge/mode-minimum_viable-blue?style=flat-square) ![Focus](https://img.shields.io/badge/current_focus-backend_flagship-success?style=flat-square)

# docker-playground

My Docker & Docker Compose learning playground — foundation for containerizing my flagship project [`payment-ledger-api`](https://github.com/ikuko-otani).

## 🎯 Why this repo exists

Target roles (Senior Backend Engineer at EU scale-ups: Mollie, HelloFresh, Revolut, Prima, GetYourGuide) all require Docker fluency. This repo is where I build that fluency with small, deliberate experiments before applying it to the flagship.

## 📅 Learning window

**2026-04-22 → 2026-05-02** (Week 1 late + Week 2 early of the 73-day sprint). See `learning_plan_minimum_viable.md` v3 dated 2026-04-19.

## 🗂 Planned units

### Docker fundamentals (Week 1 early)
- [x] 01 Install & First Run — Docker Desktop setup + `docker run / ps / stop / logs`
- [x] 02 First Dockerfile — `FROM python:3.12-slim` FastAPI hello-world
- [x] 03 Build, Tag, and Run Images — `docker build / tag / run` options
- [x] 04 Docker Commands Cheat Sheet — `ps / logs -f / exec / stop / rm / image prune`

### Docker Compose (Week 1 late)
- [x] 05 First `compose.yml`: single service
- [x] 06 Two-service setup: FastAPI + PostgreSQL
- [x] 07 `.env`, `env_file`, `depends_on`, healthchecks
- [x] 08 Networks and service discovery

## 🔗 Related repositories

- [`payment-ledger-api`](https://github.com/ikuko-otani) — flagship project (target: ship by 2026-06)
- [`python-playground`](https://github.com/ikuko-otani/python-playground) — Python foundation
- [`fastapi-playground`](https://github.com/ikuko-otani/fastapi-playground) — FastAPI fundamentals
- [`sqlalchemy-playground`](https://github.com/ikuko-otani/sqlalchemy-playground) — SQLAlchemy 2.0 async + Alembic
- [`pytest-playground`](https://github.com/ikuko-otani/pytest-playground) — pytest + pytest-asyncio

## 📚 References

- [Docker Get Started](https://docs.docker.com/get-started/)
- [Docker Compose Getting Started](https://docs.docker.com/compose/gettingstarted/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
