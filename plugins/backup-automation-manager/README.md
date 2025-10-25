# Backup Automation Manager

Automated backup scheduling, verification, storage monitoring, and disaster recovery planning with multi-cloud support (Google Drive, Dropbox, OneDrive).

## Features

### 3 Specialized Agents

1. **backup-scheduler** (Sonnet) - Strategic orchestrator
   - Backup schedule management (daily/weekly/monthly)
   - Multi-cloud synchronization
   - Retention policy enforcement (GFS rotation)
   - Disaster recovery plan generation

2. **backup-verifier** (Haiku, Fast) - Quality assurance
   - SHA-256 checksum validation
   - Recovery testing
   - Cross-cloud consistency checks
   - Verification reporting

3. **storage-monitor** (Haiku, Fast) - Analytics
   - Capacity monitoring (local & cloud)
   - Usage trend analysis
   - Alert generation (threshold-based)
   - Storage health scoring

### 1 Comprehensive Skill

**backup-management** - Complete patterns for:
- 3-2-1 backup rule (3 copies, 2 media types, 1 offsite)
- Backup types (full, incremental, differential)
- Cloud API integration (Google Drive, Dropbox, OneDrive)
- Verification procedures
- Disaster recovery checklists

## Quick Start

### Initialize Backup System

```bash
@backup-scheduler "Initialize backup configuration for ~/Documents and ~/Projects"
```

### Schedule Backups

```bash
@backup-scheduler "Set up daily backup at 2am to external drive and Google Drive"
```

### Verify Backups

```bash
@backup-verifier "Verify latest backup integrity"
```

### Monitor Storage

```bash
@storage-monitor "Show storage capacity and usage trends"
```

## Key Features

- **Automated Scheduling**: Cron-based daily/weekly/monthly backups
- **Multi-Cloud Sync**: Google Drive, Dropbox, OneDrive integration
- **Verification**: Checksums, recovery testing, consistency checks
- **Monitoring**: Capacity tracking, growth projections, alerts
- **Disaster Recovery**: Automated plan generation with priority-based procedures

## Data Storage

Configuration stored in `~/.backup-manager/`:
- `config.json` - Backup sources, destinations, schedules
- `verification-logs/` - Checksum and test results
- `disaster-recovery/` - Recovery plans and procedures

## License

MIT

---

**Generated as part of Puerto Plugin Collection - Issue #142**
