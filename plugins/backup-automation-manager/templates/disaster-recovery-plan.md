# Disaster Recovery Plan

**Generated**: {{DATE}}
**Last Updated**: {{LAST_UPDATED}}
**Version**: {{VERSION}}

---

## Executive Summary

This document outlines the disaster recovery procedures for backing up and restoring critical data. Follow these procedures in the event of data loss, system failure, or disaster.

**Recovery Objectives**:
- **RPO (Recovery Point Objective)**: Maximum acceptable data loss
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime

---

## Recovery Priority Matrix

| Priority | Data/System | RPO | RTO | Backup Frequency |
|----------|-------------|-----|-----|------------------|
{{RECOVERY_PRIORITIES}}

---

## Current Backup Status

### Latest Backups

**Local Backup**:
- Location: {{LOCAL_BACKUP_PATH}}
- Last Backup: {{LOCAL_LAST_BACKUP}}
- Status: {{LOCAL_STATUS}}
- Size: {{LOCAL_SIZE}}

**Google Drive**:
- Location: {{GDRIVE_PATH}}
- Last Backup: {{GDRIVE_LAST_BACKUP}}
- Status: {{GDRIVE_STATUS}}
- Space Available: {{GDRIVE_AVAILABLE}}

**Dropbox**:
- Location: {{DROPBOX_PATH}}
- Last Backup: {{DROPBOX_LAST_BACKUP}}
- Status: {{DROPBOX_STATUS}}
- Space Available: {{DROPBOX_AVAILABLE}}

### Verification Status

- Last Verification: {{LAST_VERIFICATION}}
- Verification Result: {{VERIFICATION_RESULT}}
- Last Recovery Test: {{LAST_RECOVERY_TEST}}
- Test Result: {{RECOVERY_TEST_RESULT}}

---

## Disaster Scenarios

### Scenario 1: Individual File Loss

**Cause**: Accidental deletion, file corruption

**Recovery Procedure**:
1. Identify the file and last known good state
2. Locate file in latest backup
   ```bash
   @backup-verifier locate-file "filename.ext"
   ```
3. Restore individual file
   ```bash
   rsync -av {{BACKUP_PATH}}/path/to/file /destination/
   ```
4. Verify restored file integrity
5. Resume operations

**Estimated RTO**: < 1 hour

### Scenario 2: Directory/Project Loss

**Cause**: Accidental deletion, ransomware

**Recovery Procedure**:
1. Assess scope of data loss
2. Identify latest verified backup
   ```bash
   @backup-verifier list-backups --verified
   ```
3. Restore directory to temporary location
   ```bash
   @backup-verifier test-recovery latest /tmp/recovery
   ```
4. Verify data integrity
5. Move to production location
6. Resume operations

**Estimated RTO**: 2-4 hours

### Scenario 3: Complete System Failure

**Cause**: Hardware failure, catastrophic loss

**Recovery Procedure**:
1. Provision new system/storage
2. Install required software and dependencies
3. Restore from most recent full backup
   ```bash
   rsync -av {{BACKUP_PATH}}/full/latest/ /new/system/
   ```
4. Apply incremental backups if needed
5. Verify all critical data restored
6. Test critical functionality
7. Resume operations

**Estimated RTO**: 4-24 hours (depending on data size)

### Scenario 4: Cloud Storage Failure

**Cause**: Service outage, account compromise

**Recovery Procedure**:
1. Verify local backup is intact
2. Switch to alternative cloud provider
   ```bash
   @backup-scheduler configure destination alternate-cloud
   ```
3. Upload latest backup to alternate location
4. Update backup schedule
5. Monitor new destination
6. Resume normal operations

**Estimated RTO**: 1-2 hours

---

## Recovery Procedures

### Phase 1: Assessment (15-30 minutes)

**Checklist**:
- [ ] Identify what data was lost
- [ ] Determine cause of data loss
- [ ] Assess scope of recovery needed
- [ ] Identify most recent viable backup
- [ ] Estimate recovery time
- [ ] Notify stakeholders
- [ ] Document incident

**Key Questions**:
- What data is missing?
- When was it last accessible?
- What is the business impact?
- Which backup should we use?

### Phase 2: Preparation (30-60 minutes)

**Checklist**:
- [ ] Verify backup integrity
   ```bash
   @backup-verifier verify {{BACKUP_ID}}
   ```
- [ ] Prepare recovery environment
- [ ] Notify stakeholders of timeline
- [ ] Document recovery plan
- [ ] Assign recovery tasks
- [ ] Prepare rollback plan (if needed)

**Recovery Environment**:
- Isolated test area: `/tmp/recovery-test/`
- Production area: `{{PRODUCTION_PATH}}`
- Backup source: `{{BACKUP_PATH}}`

### Phase 3: Recovery Execution (Variable)

**Full Restore Procedure**:
```bash
# 1. Create recovery directory
mkdir -p /recovery/destination

# 2. Restore from backup
rsync -av --progress {{BACKUP_PATH}}/full/latest/ /recovery/destination/

# 3. If incremental backups exist, apply them
for incremental in {{BACKUP_PATH}}/incremental/*; do
    rsync -av --progress $incremental/ /recovery/destination/
done

# 4. Verify restoration
@backup-verifier verify-recovery /recovery/destination

# 5. Move to production (if verified)
mv /recovery/destination/* {{PRODUCTION_PATH}}/
```

**Selective Restore Procedure**:
```bash
# 1. Identify files to restore
@backup-verifier locate-file "critical-file.txt"

# 2. Restore specific files/directories
rsync -av {{BACKUP_PATH}}/latest/path/to/files/ /destination/

# 3. Verify restored files
sha256sum restored-files.txt
```

### Phase 4: Validation (1-2 hours)

**Checklist**:
- [ ] Verify file counts match expectations
- [ ] Check file sizes and checksums
- [ ] Test critical operations
- [ ] Verify user access and permissions
- [ ] Check for data corruption
- [ ] Validate timestamps
- [ ] Document recovery results

**Validation Commands**:
```bash
# File count comparison
find {{PRODUCTION_PATH}} -type f | wc -l

# Size validation
du -sh {{PRODUCTION_PATH}}

# Checksum verification
sha256sum -c backup-checksums.txt

# Test critical files
for file in {{CRITICAL_FILES}}; do
    test -f "$file" && echo "✓ $file" || echo "✗ MISSING: $file"
done
```

### Phase 5: Post-Recovery (Ongoing)

**Checklist**:
- [ ] Monitor for issues (24-48 hours)
- [ ] Document lessons learned
- [ ] Update backup procedures if needed
- [ ] Schedule next disaster recovery test
- [ ] Update this recovery plan
- [ ] Notify stakeholders of completion
- [ ] Perform root cause analysis

**Monitoring Period**:
- Watch for application errors
- Check data consistency
- Monitor user reports
- Verify backup schedule resumed

---

## Contact Information

### Technical Team

**Primary Contact**:
- Name: {{PRIMARY_CONTACT_NAME}}
- Role: {{PRIMARY_CONTACT_ROLE}}
- Phone: {{PRIMARY_CONTACT_PHONE}}
- Email: {{PRIMARY_CONTACT_EMAIL}}

**Backup Contact**:
- Name: {{BACKUP_CONTACT_NAME}}
- Role: {{BACKUP_CONTACT_ROLE}}
- Phone: {{BACKUP_CONTACT_PHONE}}
- Email: {{BACKUP_CONTACT_EMAIL}}

### Service Providers

**Google Drive Support**:
- Support: https://support.google.com/drive
- Status: https://www.google.com/appsstatus

**Dropbox Support**:
- Support: https://www.dropbox.com/support
- Status: https://status.dropbox.com

**OneDrive Support**:
- Support: https://support.microsoft.com/onedrive
- Status: https://portal.office.com/servicestatus

---

## Critical File Locations

### Configuration Files
- Backup config: `~/.backup-manager/config.json`
- Cloud credentials: `~/.backup-manager/*-token.json`
- Schedule: `crontab -l`

### Backup Locations
- Local: `{{LOCAL_BACKUP_PATH}}`
- Google Drive: `{{GDRIVE_PATH}}`
- Dropbox: `{{DROPBOX_PATH}}`
- OneDrive: `{{ONEDRIVE_PATH}}`

### Log Files
- Backup log: `~/.backup-manager/backup.log`
- Alert log: `~/.backup-manager/alerts.log`
- Verification log: `~/.backup-manager/verification-*.log`

---

## Testing Schedule

### Recovery Tests

**Monthly (First Sunday)**:
- Selective file recovery test
- Verify 10 random files from latest backup
- Document test results

**Quarterly (Last Sunday)**:
- Full recovery drill to test environment
- Complete restoration validation
- Update disaster recovery plan

**Annually (January)**:
- Comprehensive disaster recovery simulation
- Test all scenarios
- Full team involvement
- Update procedures based on findings

### Next Scheduled Tests

- Next Monthly Test: {{NEXT_MONTHLY_TEST}}
- Next Quarterly Test: {{NEXT_QUARTERLY_TEST}}
- Next Annual Test: {{NEXT_ANNUAL_TEST}}

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | {{INITIAL_DATE}} | Initial creation | Automated |
{{VERSION_HISTORY}}

---

## Appendix A: Quick Reference Commands

### Check Backup Status
```bash
@backup-scheduler status
@backup-verifier verify latest
@storage-monitor capacity
```

### Locate a File in Backups
```bash
@backup-verifier locate-file "filename.ext"
```

### Test Recovery
```bash
@backup-verifier test-recovery latest /tmp/test
```

### Restore Individual File
```bash
rsync -av {{BACKUP_PATH}}/latest/path/to/file /destination/
```

### Full System Restore
```bash
rsync -av {{BACKUP_PATH}}/full/latest/ /destination/
```

### Verify Restoration
```bash
@backup-verifier verify-recovery /destination
```

---

## Appendix B: Backup Retention Policy

**Current Policy**:
- Daily backups: Retain {{DAILY_RETENTION}} days
- Weekly backups: Retain {{WEEKLY_RETENTION}} weeks
- Monthly backups: Retain {{MONTHLY_RETENTION}} months
- Yearly backups: Retain {{YEARLY_RETENTION}} years

**Total Backup Coverage**: {{TOTAL_COVERAGE}} days

---

## Appendix C: Emergency Decision Tree

```
Data Loss Detected
    │
    ├─ Single File?
    │   └─ YES → Scenario 1 (< 1 hour)
    │
    ├─ Directory/Project?
    │   └─ YES → Scenario 2 (2-4 hours)
    │
    ├─ Complete System?
    │   └─ YES → Scenario 3 (4-24 hours)
    │
    └─ Cloud Provider Down?
        └─ YES → Scenario 4 (1-2 hours)
```

---

**Document Control**:
- Owner: {{OWNER}}
- Last Review: {{LAST_REVIEW}}
- Next Review: {{NEXT_REVIEW}}
- Classification: Internal
- Status: {{STATUS}}

---

*This disaster recovery plan is automatically updated by the Backup Automation Manager. Manual updates should be reflected in version history.*
