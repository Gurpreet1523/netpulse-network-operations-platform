# Cloud Deployment Plan

Target option: Azure Container Apps (good fit for Azure DevOps/Microsoft cloud learning) or AWS App Runner.

## Before deployment
1. Add PostgreSQL persistence and environment-based configuration.
2. Add a production ASGI server command and container health check.
3. Never commit credentials or API keys.
4. Add `/health` readiness/liveness verification.
5. Pin dependencies and run tests/security checks in CI.
6. Configure logs and resource limits.

## Azure Container Apps outline
1. Create an Azure resource group and Container Apps environment.
2. Build and push the container image to Azure Container Registry.
3. Deploy the image to Azure Container Apps.
4. Set environment variables and secrets through the platform's secret configuration.
5. Configure ingress and the health probe.
6. Verify `/health`, API docs, logs, and restart behavior.
7. Record the deployment URL and a screenshot of the successful health check.

Do not record a cloud deployment as completed until it has actually been deployed and verified. Avoid placing credentials in source control or screenshots.
