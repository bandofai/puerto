# Skill: Cost Optimization

## Cost Optimization Strategies
1. **Right-sizing**: Match instance types to workload requirements
2. **Reserved Instances**: 1-3 year commitments for 30-70% savings
3. **Spot Instances**: Up to 90% savings for fault-tolerant workloads
4. **Autoscaling**: Scale down during low usage periods
5. **Storage Tiering**: Move infrequent data to cheaper storage classes
6. **Unused Resources**: Delete orphaned volumes, snapshots, IPs
7. **Region Selection**: Choose cheaper regions when latency allows

## Cost Analysis
- Group costs by: Application, Environment, Team, Cost Center
- Track month-over-month trends
- Set budgets and alerts
- Allocate shared costs fairly

## Quick Wins
- Delete unused EBS volumes
- Right-size over-provisioned instances
- Use S3 Intelligent-Tiering
- Enable auto-scaling
- Purchase reserved instances for steady workloads
- Use spot instances for batch processing

## ROI Calculations
Compare cloud vs on-premise:
- **Cloud**: Pay-as-you-go, no upfront hardware, elastic scaling
- **On-Premise**: CapEx for hardware, data center costs, maintenance
- Consider: Migration costs, training, opportunity cost
