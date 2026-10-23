# NetPulse Test Plan

## 1. Purpose
Validate API correctness, input validation, device inventory behavior, network telemetry behavior as it is added, and deployment health.

## 2. Scope
**Included:** REST API, device registration, duplicate-IP handling, interface inventory, simulated telemetry, incident rules, UI/API integration, container health, and performance baselines.

**Excluded in the initial lab:** real production networks, physical optical hardware, carrier-grade performance certification, and real customer data.

## 3. Test levels
- Unit: validation rules, threshold calculations, status transitions.
- API integration: HTTP status codes, response schemas, persistence.
- System/end-to-end: register device → emit telemetry → trigger incident → acknowledge/resolve incident.
- Regression: all previously fixed defects remain fixed.
- Performance: concurrent read traffic and device inventory growth using Locust.
- Reliability: restart behavior, health checks, invalid dependencies, and timeout handling.
- Security: input validation, secret handling, dependency scanning, and access-control tests if authentication is implemented.

## 4. Initial acceptance criteria
- Health endpoint returns HTTP 200 and a service status.
- Unknown device IDs return HTTP 404 with a stable error shape.
- Invalid IP addresses and malformed payloads return HTTP 422.
- Duplicate management IP addresses return HTTP 409.
- Device interface queries return the correct list or a clear 404.
- CI runs automated tests on every push and pull request.
- Cloud deployment exposes a health endpoint and uses configuration/secrets safely.

## 5. Defect severity
- P1 Critical: service unavailable, data corruption, or unsafe behavior.
- P2 High: core workflow broken with no practical workaround.
- P3 Medium: partial functionality broken or workaround exists.
- P4 Low: cosmetic/documentation issue.

## 6. Evidence to retain
Test run output, coverage report, screenshots of API docs/dashboard, sample telemetry, Locust report, CI run, cloud health-check response, and completed defect reports.
