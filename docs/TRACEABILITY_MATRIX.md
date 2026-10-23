# Requirements Traceability Matrix

| Requirement ID | Requirement | Test coverage | Status |
|---|---|---|---|
| API-001 | Service health is observable | `test_health_endpoint_returns_ok` | Implemented |
| DEV-001 | List registered devices | `test_list_devices_returns_seeded_devices` | Implemented |
| DEV-002 | Retrieve a known device | `test_get_existing_device` | Implemented |
| DEV-003 | Unknown device returns 404 | `test_unknown_device_returns_404` | Implemented |
| DEV-004 | Reject duplicate management IP | `test_create_device_rejects_duplicate_management_ip` | Implemented |
| DEV-005 | Reject invalid IP input | `test_create_device_rejects_invalid_ip` | Implemented |
| IF-001 | List interfaces for a known device | `test_interfaces_for_existing_device` | Implemented |
| IF-002 | Unknown device interface query returns 404 | `test_interfaces_for_unknown_device_returns_404` | Implemented |
| TEL-001 | Generate latency/packet-loss telemetry | To be implemented | Planned |
| INC-001 | Create incident when thresholds are exceeded | To be implemented | Planned |
| PERF-001 | Measure API latency under load | Locust scenario to be added | Planned |
| OPS-001 | CI pipeline runs tests | GitHub Actions workflow | Scaffold included |
| CLOUD-001 | Deploy API and verify health endpoint | Deployment guide | Planned |
