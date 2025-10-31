# DevOps Engineer Plugin

**Comprehensive DevOps and infrastructure automation specialist**

This plugin provides a suite of specialized agents for managing CI/CD pipelines, infrastructure as code, deployment strategies, and observability.

## Agents

### 1. **cicd-builder** (Sonnet)
Creates and optimizes CI/CD pipelines for multiple platforms.

**Use when:**
- Setting up new CI/CD pipelines
- Optimizing existing workflows
- Migrating between CI/CD platforms
- Adding quality gates and security scanning

**Platforms supported:**
- GitHub Actions
- GitLab CI/CD
- Jenkins
- CircleCI
- Azure DevOps

**Capabilities:**
- Multi-stage pipeline design
- Test automation integration
- Security scanning (SAST, DAST, dependency checks)
- Artifact management
- Deployment automation
- Cost optimization

### 2. **infrastructure-manager** (Sonnet)
Manages Infrastructure as Code with Terraform, CloudFormation, and other tools.

**Use when:**
- Creating new infrastructure
- Refactoring existing IaC
- Implementing best practices
- Setting up multi-environment deployments

**Tools supported:**
- Terraform (AWS, Azure, GCP, Multi-cloud)
- AWS CloudFormation
- Azure Resource Manager (ARM)
- Pulumi
- Ansible

**Capabilities:**
- Module design and reusability
- State management strategies
- Security hardening
- Cost optimization
- Disaster recovery planning
- Multi-region/multi-cloud architectures

### 3. **deployment-orchestrator** (Sonnet)
Implements advanced deployment strategies and orchestration.

**Use when:**
- Designing deployment strategies
- Setting up Kubernetes deployments
- Implementing blue-green/canary deployments
- Managing container orchestration

**Strategies:**
- Blue-green deployments
- Canary releases
- Rolling updates
- Feature flags integration
- Rollback procedures

**Platforms:**
- Kubernetes
- Docker Swarm
- AWS ECS/Fargate
- Azure Container Instances
- Google Cloud Run

### 4. **monitoring-setup** (Sonnet)
Implements comprehensive monitoring, logging, and alerting.

**Use when:**
- Setting up observability stack
- Creating dashboards and alerts
- Implementing SLIs/SLOs/SLAs
- Troubleshooting production issues

**Tools:**
- Prometheus + Grafana
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Datadog
- New Relic
- CloudWatch
- Azure Monitor
- Google Cloud Monitoring

**Capabilities:**
- Metrics collection and visualization
- Log aggregation and analysis
- Distributed tracing
- Alert rule creation
- On-call runbook generation
- SLO/SLA tracking

## Skills

### 1. **cicd-patterns**
Best practices for CI/CD pipeline design, including:
- Pipeline optimization strategies
- Security scanning integration
- Artifact management
- Testing strategies (unit, integration, e2e)
- Cache optimization
- Parallel execution patterns

### 2. **iac-design**
Infrastructure as Code patterns and best practices:
- Module design and composition
- State management (local, remote, encryption)
- Security hardening
- Cost optimization techniques
- Naming conventions
- Directory structure patterns

### 3. **deployment-strategies**
Advanced deployment patterns:
- Blue-green deployment implementation
- Canary release strategies
- Traffic shifting patterns
- Rollback procedures
- Health checks and readiness probes
- Zero-downtime migrations

### 4. **observability**
Comprehensive monitoring and alerting:
- The Four Golden Signals (latency, traffic, errors, saturation)
- SLI/SLO/SLA design
- Alert rule best practices
- Dashboard design principles
- Logging strategies
- Distributed tracing setup

## Templates

### CI/CD Templates
- **github-actions-template.yml**: Complete GitHub Actions workflow with testing, security, and deployment
- **gitlab-ci-template.yml**: GitLab CI/CD pipeline with multi-stage deployment

### Infrastructure Templates
- **terraform-module-template/**: Reusable Terraform module structure
- **cloudformation-template.yml**: AWS CloudFormation stack template

### Container Templates
- **docker-compose-template.yml**: Multi-service Docker Compose setup
- **kubernetes-deployment.yml**: Complete Kubernetes deployment with service, ingress, and autoscaling

### Monitoring Templates
- **prometheus-rules.yml**: Prometheus alerting rules
- **grafana-dashboard.json**: Grafana dashboard template

## Installation

```bash
# Install plugin
cp -r devops-engineer ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/devops-engineer/agents/
```

## Quick Start

### Example 1: Setup CI/CD Pipeline

```
User: I need a GitHub Actions workflow for my Python FastAPI app with tests and deployment to AWS

Agent: cicd-builder
1. Reads cicd-patterns skill
2. Creates .github/workflows/ci-cd.yml with:
   - Python setup and dependency installation
   - Unit and integration tests with pytest
   - Security scanning (bandit, safety)
   - Docker image build and push
   - AWS ECS deployment
   - Rollback on failure
3. Includes caching for faster builds
4. Sets up environment secrets documentation
```

### Example 2: Infrastructure as Code

```
User: Create Terraform modules for a 3-tier web application on AWS

Agent: infrastructure-manager
1. Reads iac-design skill
2. Creates modular structure:
   - modules/vpc/ (networking)
   - modules/compute/ (EC2, ASG)
   - modules/database/ (RDS)
   - modules/loadbalancer/ (ALB)
3. Implements security best practices
4. Includes remote state configuration
5. Creates dev, staging, prod environments
6. Generates documentation
```

### Example 3: Kubernetes Deployment

```
User: Setup a blue-green deployment for my microservice on Kubernetes

Agent: deployment-orchestrator
1. Reads deployment-strategies skill
2. Creates Kubernetes manifests:
   - Deployment (blue and green versions)
   - Service (selector-based switching)
   - Ingress with traffic routing
   - HorizontalPodAutoscaler
3. Implements health checks
4. Creates deployment script
5. Documents rollback procedure
```

### Example 4: Monitoring Setup

```
User: I need comprehensive monitoring for my Node.js API

Agent: monitoring-setup
1. Reads observability skill
2. Sets up Prometheus + Grafana:
   - Prometheus config with scrape targets
   - Node.js metrics instrumentation
   - Alert rules (high latency, error rate, saturation)
   - Grafana dashboards (RED metrics)
3. Implements logging with structured logs
4. Creates on-call runbook
5. Defines SLOs (99.9% uptime, p95 latency < 200ms)
```

## Workflow Integration

Agents work together for complete DevOps lifecycle:

```
1. infrastructure-manager: Create cloud infrastructure
   ↓
2. cicd-builder: Setup CI/CD pipeline
   ↓
3. deployment-orchestrator: Implement deployment strategy
   ↓
4. monitoring-setup: Add observability
   ↓
5. (iterate) Continuous improvement
```

## Best Practices

### Security
- All agents implement security-first principles
- Secrets management with vault/parameter store
- Least privilege IAM policies
- Network segmentation
- Security scanning in pipelines

### Cost Optimization
- Right-sizing recommendations
- Auto-scaling strategies
- Spot/preemptible instance usage
- Resource tagging for cost allocation
- Cache optimization in CI/CD

### Reliability
- Multi-AZ/multi-region deployments
- Disaster recovery planning
- Automated backup strategies
- Health checks and auto-healing
- Comprehensive monitoring and alerting

## Troubleshooting

### CI/CD Pipeline Failures
1. Use **cicd-builder** to analyze pipeline logs
2. Check for common issues:
   - Dependency conflicts
   - Test failures
   - Security vulnerabilities
   - Timeout issues
3. Implement fixes based on skill recommendations

### Infrastructure Issues
1. Use **infrastructure-manager** to validate IaC
2. Check Terraform/CloudFormation state
3. Review resource dependencies
4. Verify IAM permissions

### Deployment Problems
1. Use **deployment-orchestrator** to review strategy
2. Check health checks and readiness probes
3. Verify traffic routing configuration
4. Implement rollback if needed

### Monitoring Gaps
1. Use **monitoring-setup** to assess coverage
2. Review alert rules and thresholds
3. Check for blind spots
4. Improve SLI/SLO definitions

## Configuration

### Environment Variables
```bash
# Cloud provider credentials (use secrets management)
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
export GOOGLE_APPLICATION_CREDENTIALS="..."
export AZURE_SUBSCRIPTION_ID="..."

# CI/CD platform tokens
export GITHUB_TOKEN="..."
export GITLAB_TOKEN="..."

# Monitoring tools
export PROMETHEUS_URL="..."
export GRAFANA_API_KEY="..."
```

### Tool Dependencies
```bash
# Install required tools
brew install terraform
brew install kubectl
brew install helm
brew install aws-cli
brew install azure-cli
brew install gcloud

# Verify installations
terraform version
kubectl version --client
helm version
```

## Examples

See `examples/` directory for complete use cases:
- `examples/aws-3tier-app/`: Complete 3-tier application on AWS
- `examples/kubernetes-microservices/`: Microservices on Kubernetes
- `examples/multi-cloud-setup/`: Multi-cloud infrastructure
- `examples/observability-stack/`: Full observability implementation

## Contributing

To extend this plugin:
1. Follow skill-aware subagent patterns
2. Add new agents to `agents/` directory
3. Document skills in `skills/` directory
4. Provide templates in `templates/` directory
5. Update this README

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or contributions:
- GitHub Issues: [Link to issues]
- Documentation: [Link to docs]
- Community: [Link to community]

---

**Version**: 1.0.0
**Last Updated**: 2025-01-20
**Agents**: 4
**Skills**: 4
**Templates**: 7+
**Platforms**: AWS, Azure, GCP, Kubernetes, Docker, GitHub Actions, GitLab CI, Jenkins, and more
