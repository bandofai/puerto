# Backup Management Skill

Comprehensive patterns for automated backup management, verification, and disaster recovery.

## Core Principles: 3-2-1 Backup Rule

- **3 copies** of data (1 primary + 2 backups)
- **2 different media** types (local drive + cloud)
- **1 copy offsite** (cloud storage)

## Backup Types

### Full Backup
Complete copy of all data. Largest size, slowest, but easiest recovery.

### Incremental Backup
Only files changed since last backup (any type). Smallest size, fastest, requires chain for recovery.

### Differential Backup
Files changed since last full backup. Medium size, faster recovery than incremental.

## Retention Policies

### GFS (Grandfather-Father-Son)
- Daily backups (Son): Keep 7 days
- Weekly backups (Father): Keep 4 weeks
- Monthly backups (Grandfather): Keep 12 months

## Multi-Cloud Integration

### Google Drive
- OAuth2 authentication
- Resumable uploads for large files
- Quota: 15GB free, unlimited paid

### Dropbox
- OAuth2 authentication
- Chunked uploads (4MB chunks)
- Quota: 2GB free, varies by plan

### OneDrive
- OAuth2 authentication
- Upload sessions for files >4MB
- Quota: 5GB free, 1TB with Microsoft 365

## Verification Procedures

### Integrity Check
1. Calculate SHA-256 checksum after backup
2. Store checksum in verification log
3. Recalculate and compare periodically

### Recovery Testing
Monthly recommended:
1. Select random files from backup
2. Restore to temporary location
3. Compare with originals
4. Document results

## Disaster Recovery Planning

### Priority Levels
- Critical: Business/work data, financial records
- High: Personal documents, photos
- Medium: Software, configurations
- Low: Cached data, downloads

### Recovery Procedures
1. Assess damage scope
2. Restore critical systems first
3. Verify data integrity
4. Resume normal operations

## Storage Monitoring

### Alert Thresholds
- Warning: 75% capacity
- Critical: 90% capacity
- Emergency: 95% capacity

### Growth Projections
- 7-day trend: Daily growth rate
- 30-day trend: Weekly patterns
- 90-day trend: Seasonal variations

---

**All agents should reference these patterns for consistent backup management.**
