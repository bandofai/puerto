# Medical Appointment Tracker Plugin

> Medical appointment and prescription management specialist - Secure health record organization, appointment scheduling, and medication tracking

## Overview

The Medical Appointment Tracker plugin provides a secure, privacy-first system for managing medical appointments, prescriptions, health records, and healthcare provider information. All data is stored locally with encryption for maximum privacy.

## Features

### Agents

- **appointment-scheduler** (Haiku): Manage appointments, reminders, and scheduling
- **prescription-manager** (Haiku): Track prescriptions, refills, and medication schedules
- **health-record-organizer** (Sonnet): Organize and index medical records
- **provider-directory** (Haiku): Maintain healthcare provider database
- **medical-data-exporter** (Sonnet): Generate reports and summaries for providers
- **health-assistant-coordinator** (Sonnet): Main orchestrator for all medical tasks

### Skills

- **medical-data-security**: HIPAA-aware security patterns, encryption, audit logging
- **appointment-management**: Scheduling patterns, reminders, preparation checklists
- **medication-tracking**: Prescription management, refill calculation, adherence tracking
- **health-records**: Record organization, categorization, privacy-preserving search

## Quick Start

### Installation

```bash
/plugin install medical-appointment-tracker@puerto
```

### Initial Setup

```bash
# Initialize secure encryption
scripts/init-security.sh

# Add your primary care provider
@provider-directory add \
    --name "Dr. Jane Smith" \
    --type "primary_care" \
    --phone "555-1234" \
    --address "123 Medical Plaza"
```

### Basic Usage

**Schedule an appointment:**
```bash
@appointment-scheduler create \
    --date "2025-02-15" \
    --time "14:00" \
    --provider "Dr. Jane Smith" \
    --type "annual_checkup"
```

**Track a prescription:**
```bash
@prescription-manager add \
    --medication "Lisinopril" \
    --dosage "10mg" \
    --frequency "once daily" \
    --days-supply 90
```

**Check upcoming appointments:**
```bash
@appointment-scheduler list --upcoming --days 30
```

## Security & Privacy

### Privacy-First Design

- **Local storage only**: All data stored on your machine, never in the cloud
- **Encryption at rest**: All medical data encrypted using age encryption
- **Audit logging**: Every access to medical data is logged
- **No telemetry**: No usage data sent anywhere
- **HIPAA-aware**: Follows HIPAA privacy principles (not certification)

### Data Encryption

```bash
# All medical data is automatically encrypted
# Encryption keys stored in ~/.claude/medical-tracker/

# Manual encryption utilities available
scripts/encrypt-data.sh input.json encrypted-output.age
scripts/decrypt-data.sh encrypted-output.age
```

### Audit Trail

All access is logged:
```
2025-01-21T14:30:00Z|ENCRYPT|appointment-123.json|SUCCESS
2025-01-21T14:31:00Z|DECRYPT|prescription-456.json|SUCCESS
2025-01-21T14:32:00Z|UPDATE|provider-789.json|SUCCESS
```

## Use Cases

### Example 1: Schedule Annual Physical

```bash
@health-assistant-coordinator "Schedule my annual physical with Dr. Smith"

# Coordinator will:
1. Lookup Dr. Smith in provider directory
2. Create appointment with appointment-scheduler
3. Set reminders (1 week, 24 hours, 2 hours before)
4. Generate pre-appointment checklist:
   - Verify insurance coverage
   - Bring insurance card and ID
   - Bring current medication list
   - Prepare questions for doctor
```

### Example 2: Prescription Refill

```bash
@prescription-manager check-refills

# Output:
Prescriptions Due for Refill:

1. Lisinopril 10mg
   - Next refill date: 2025-01-25 (4 days)
   - Refills remaining: 3
   - Pharmacy: CVS Pharmacy (555-9876)
   - Action: Call pharmacy or use online portal

2. Metformin 500mg
   - Next refill date: 2025-01-28 (7 days)
   - Refills remaining: 2
   - Pharmacy: CVS Pharmacy (555-9876)
```

### Example 3: Prepare for Specialist Visit

```bash
@health-assistant-coordinator "Prepare a summary for my cardiologist appointment"

# Coordinator will:
1. Generate patient summary (medical-data-exporter)
2. Include current medications (prescription-manager)
3. Compile recent test results (health-record-organizer)
4. List relevant medical history
5. Export as PDF for provider

# Output: comprehensive-medical-summary-2025-01-21.pdf
```

## Appointment Management

### Appointment Types

- **Primary Care**: Annual physicals, sick visits
- **Specialist**: Cardiology, dermatology, endocrinology, etc.
- **Dentist**: Cleanings, procedures
- **Therapy**: Mental health, physical therapy
- **Diagnostic**: Lab work, imaging (X-ray, MRI, CT)
- **Telehealth**: Virtual appointments

### Automatic Reminders

```
For primary care/dentist:
  - 24 hours before

For specialist/procedures:
  - 1 week before (verify insurance, prep)
  - 24 hours before (final reminder)
  - 2 hours before (departure time)
```

### Pre-Appointment Checklist

Automatically generated for each appointment:

- [ ] Verify insurance coverage
- [ ] Bring insurance card and photo ID
- [ ] Arrive 15 minutes early for paperwork
- [ ] Bring current medication list
- [ ] Prepare questions for doctor
- [ ] Complete any required forms online

## Prescription Management

### Medication Tracking

Track for each prescription:
- Medication name (brand and generic)
- Dosage and frequency
- Prescribing doctor
- Pharmacy
- Refills remaining
- Next refill date
- Medication schedule

### Refill Reminders

```
Automatic reminders:
  - 14 days before: "Refill eligible soon"
  - 7 days before: "Time to request refill"
  - 3 days before: "Refill request URGENT"
```

### Medication Schedule

```json
{
  "daily_schedule": [
    {
      "time": "08:00",
      "medications": [
        "Lisinopril 10mg (with water)",
        "Metformin 500mg (with food)"
      ]
    },
    {
      "time": "20:00",
      "medications": [
        "Statin 20mg (before bed)"
      ]
    }
  ]
}
```

## Health Records

### Record Categories

- **Lab Results**: Blood work, urinalysis, etc.
- **Imaging**: X-rays, MRI, CT scans
- **Procedures**: Surgical reports, biopsies
- **Consultations**: Specialist notes
- **Diagnoses**: ICD-10 coded diagnoses
- **Prescriptions**: Medication history
- **Vaccinations**: Immunization records

### Privacy-Preserving Search

Search records without exposing full content:

```bash
@health-record-organizer search --query "cholesterol" --date-range "2024"

# Results show metadata only:
1. Lab Results - 2024-06-15 - Primary Care
2. Lab Results - 2024-12-10 - Primary Care

# Access specific record when needed
@health-record-organizer view --record-id "record-123"
```

## Provider Directory

### Provider Information

Track for each provider:
- Name and credentials
- Specialty
- Contact information (phone, fax, email, portal)
- Office address and hours
- Insurance accepted
- Appointment history
- Notes and preferences

### Provider Types

- Primary Care Physician
- Specialist (cardiologist, dermatologist, etc.)
- Dentist
- Therapist (mental health, physical)
- Hospital
- Lab/Diagnostic Center
- Pharmacy

## Data Export

### Report Generation

Generate reports for:

**Patient Summary**:
- Demographics
- Current medications
- Active diagnoses
- Recent test results
- Appointment history

**Medication List**:
- All active prescriptions
- Dosages and schedules
- Prescribing doctors
- Pharmacy information

**Vaccination Record**:
- Complete immunization history
- Dates and locations
- Next due dates

**Emergency Contact Card**:
- Wallet-sized PDF
- Key medical information
- Emergency contacts
- Critical allergies

## Important Disclaimers

**This plugin is a tracking tool only, NOT**:
- Medical advice
- A substitute for professional healthcare
- HIPAA certified (though it follows privacy principles)
- A diagnostic tool
- A treatment recommendation system

**Always**:
- Consult your healthcare providers
- Follow your doctor's instructions
- Seek emergency care when needed
- Verify all information with official sources

## Best Practices

### Stay Organized

1. **Log appointments immediately**: Add to system right after scheduling
2. **Update after each visit**: Document outcomes, prescriptions, follow-ups
3. **Track prescriptions actively**: Don't let refills lapse
4. **Maintain provider info**: Keep contact information current
5. **Back up regularly**: Use encrypted backups

### Privacy & Security

1. **Encrypt everything**: Use provided encryption tools
2. **Secure your keys**: Protect encryption keys carefully
3. **Regular backups**: To encrypted external drive
4. **Enable disk encryption**: FileVault (Mac) or BitLocker (Windows)
5. **Review audit logs**: Check access logs monthly
6. **Limited sharing**: Only share what's necessary with whom it's necessary

### Appointment Management

1. **Confirm 24-48 hrs ahead**: Call to confirm appointments
2. **Set multiple reminders**: Don't rely on memory
3. **Prepare questions**: Write down questions before appointments
4. **Document outcomes**: Record what happened and next steps
5. **Schedule follow-ups immediately**: While you're thinking about it

## Data Backup

### Automated Backup

```bash
# Set up automated backups (weekly)
scripts/backup-medical-data.sh

# Backup creates encrypted archive:
# ~/medical-backups/medical-backup-20250121-143000.tar.gz.age

# Restore from backup
scripts/restore-backup.sh ~/medical-backups/medical-backup-20250121-143000.tar.gz.age
```

### Backup Strategy

- **Frequency**: Weekly automated, plus before/after major updates
- **Location**: Encrypted external drive, not cloud
- **Retention**: Keep 30 days of backups
- **Verification**: Test restore process quarterly

## Troubleshooting

**Issue**: Can't decrypt medical data

**Solution**: Verify encryption keys
```bash
# Check if keys exist
ls ~/.claude/medical-tracker/*.key

# Re-initialize if needed
scripts/init-security.sh --force
```

**Issue**: Reminders not showing up

**Solution**: Check reminder daemon
```bash
# Test reminder system
scripts/reminder-check.sh --test

# Set up daily checks (cron)
crontab -e
# Add: 0 8 * * * /path/to/scripts/reminder-check.sh
```

## Data Storage

```
data/
├── appointments/        # Appointment records (encrypted)
├── prescriptions/       # Medication data (encrypted)
├── records/            # Health records (encrypted)
├── providers/          # Provider database
├── insurance/          # Insurance info (encrypted)
└── reports/            # Generated reports
```

## Integration

### With Calendar Apps

```bash
# Sync appointments to Google Calendar
@appointment-scheduler sync --calendar google --bidirectional true
```

### With Health Apps

```bash
# Export to Apple Health
@medical-data-exporter export --format fhir --output apple-health-import.json
```

## License

MIT

## Support

For issues and questions:
- GitHub Issues: https://github.com/bandofai/puerto/issues

---

**Remember**: Your health data is sensitive. This plugin is designed with privacy as the top priority. All data stays on your device, encrypted at rest, with no cloud storage or external transmission.
