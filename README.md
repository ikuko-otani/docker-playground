![Status](https://img.shields.io/badge/status-active-success?style=flat-square) ![Mode](https://img.shields.io/badge/mode-minimum_viable-blue?style=flat-square) ![Focus](https://img.shields.io/badge/current_focus-backend_flagship-success?style=flat-square)

# docker-playground

My Docker & Docker Compose learning playground — foundation for containerizing my flagship project [`payment-ledger-api`](https://github.com/ikuko-otani).

## 🎯 Why this repo exists

Target roles (Senior Backend Engineer at EU scale-ups: Mollie, HelloFresh, Revolut, Prima, GetYourGuide) all require Docker fluency. This repo is where I build that fluency with small, deliberate experiments before applying it to the flagship.

## 📅 Learning window

**2026-04-22 → 2026-05-02** (Week 1 late + Week 2 early of the 73-day sprint). See `learning_plan_minimum_viable.md` v3 dated 2026-04-19.

## 🗂 Planned units

### Docker fundamentals (Week 1 late)
- [ ] 01 Docker Desktop setup + `docker run / ps / stop / logs`
- [ ] 02 First Dockerfile: `FROM python:3.12-slim` hello-world FastAPI
- [ ] 03 Multi-stage builds and image size optimization
- [ ] 04 Volumes and bind mounts

### Docker Compose (Week 2 early)
- [ ] 05 First `compose.yml`: single service
- [ ] 06 Two-service setup: FastAPI + PostgreSQL
- [ ] 07 `.env`, `env_file`, `depends_on`, healthchecks
- [ ] 08 Networks and service discovery

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
