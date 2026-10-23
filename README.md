# NetPulse — Network Operations & Device Intelligence Platform

An independent portfolio project demonstrating network-focused software development, test automation, QA, CI/CD, containerization, and cloud-readiness. This is a simulation lab; it does not connect to production networks or real telecom equipment.

## Goals
- Build REST APIs for network devices, interfaces, telemetry, and incidents.
- Simulate healthy devices and common failures.
- Validate behavior with unit, API integration, regression, and performance tests.
- Produce reproducible defect reports and test evidence.
- Package the service with Docker and automate checks in GitHub Actions.
- Prepare a cloud deployment path (Azure Container Apps or AWS App Runner/ECS).

## Planned stack
- Python 3.12, FastAPI, Pydantic
- PostgreSQL (Phase 2; initial starter uses in-memory demo data)
- pytest, HTTPX, coverage, Locust
- Docker, Docker Compose, GitHub Actions
- Optional UI: React + TypeScript
- Cloud: Azure Container Apps or AWS App Runner

## Repository status
This repository is the **Phase 1 starter scaffold**. The device API and starter tests are included. Database persistence, telemetry simulator, richer QA suites, UI, and cloud deployment are planned milestones—not yet implemented.

## Quick start (Python)
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Run tests
```bash
pytest -v --cov=app --cov-report=term-missing
```

## Run with Docker
```bash
docker build -t netpulse-api .
docker run --rm -p 8000:8000 netpulse-api
```

## API starter endpoints
- `GET /health` — service health
- `GET /api/v1/devices` — list simulated devices
- `GET /api/v1/devices/{device_id}` — get a device
- `POST /api/v1/devices` — register a simulated device
- `GET /api/v1/devices/{device_id}/interfaces` — list interfaces

## Roadmap
1. **API foundation:** device models, validation, errors, API tests.
2. **Network simulation:** interfaces, latency, packet loss, reachability, fault injection.
3. **Telemetry and incidents:** threshold alerts, event history, incident lifecycle.
4. **QA engineering:** test plan, traceability matrix, negative tests, regression, coverage gates, bug reports.
5. **Performance and reliability:** Locust load profile, response-time targets, resilience tests.
6. **Frontend:** device inventory, health summary, incidents, telemetry charts.
7. **Cloud/DevOps:** Docker Compose, CI workflow, secrets/configuration, cloud deployment, logs and health checks.
8. **Portfolio polish:** architecture diagram, demo script, screenshots, interview walkthrough.

## QA evidence
See `docs/TEST_PLAN.md`, `docs/TRACEABILITY_MATRIX.md`, and `docs/BUG_REPORT_TEMPLATE.md`.

## Honest portfolio guidance
Only claim features after you have implemented and tested them. The cloud deployment is not complete until a real deployment URL and deployment evidence are added.
