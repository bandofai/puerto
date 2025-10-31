# Skill: Cloud Architecture

## Well-Architected Framework Pillars
1. **Operational Excellence**: Automation, monitoring, continuous improvement
2. **Security**: Identity, data protection, infrastructure protection
3. **Reliability**: High availability, disaster recovery, fault tolerance
4. **Performance Efficiency**: Right-sizing, caching, CDN
5. **Cost Optimization**: Resource efficiency, cost visibility, cost-effective resources

## Common Patterns
### 3-Tier Web Architecture
- Presentation: Load Balancer + Web Servers (Auto Scaling)
- Application: App Servers (Auto Scaling) 
- Data: Managed Database (Multi-AZ)

### Microservices
- API Gateway → Services (containers/serverless)
- Service mesh for inter-service communication
- Event-driven with message queues

### Data Lake
- Ingestion: Streaming + Batch
- Storage: Object storage (S3, Azure Blob, GCS)
- Processing: Spark, data warehouses
- Analytics: BI tools, ML platforms

## High Availability
- Multi-AZ deployment for databases
- Auto Scaling for compute
- Load balancing across AZs
- Health checks and auto-recovery
- RTO/RPO requirements

## Security Best Practices
- Least privilege IAM
- Encryption at rest and in transit
- Network segmentation (VPC, subnets, security groups)
- Secrets management (AWS Secrets Manager, Azure Key Vault)
- Logging and monitoring (CloudTrail, CloudWatch)
