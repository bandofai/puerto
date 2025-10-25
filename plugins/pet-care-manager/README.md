# Pet Care Manager Plugin

Pet health and care routine management specialist for Puerto.

## Overview

The Pet Care Manager plugin provides comprehensive tools for managing pet health records, veterinary care, medications, and daily care routines.

## Features

- **Vet Appointments**: Schedule checkups, track vaccinations, reminders
- **Medication Tracking**: Daily meds, preventives, refill reminders
- **Health Records**: Vaccination history, vet visits, medical conditions
- **Daily Care**: Feeding schedules, exercise logging, grooming reminders
- **Expense Tracking**: Monitor pet care costs
- **Multi-Pet Support**: Manage multiple pets in one system

## Agents

### 1. vet-appointment-scheduler (Haiku)
Fast vet appointment scheduling and vaccination reminders.

**Usage:**
```
@vet-appointment-scheduler Schedule annual checkup for Max on March 15
@vet-appointment-scheduler Show vaccination schedule for all pets
@vet-appointment-scheduler When is Max's rabies vaccine due?
```

### 2. medication-reminder (Haiku)
Medication tracking and timely reminders.

**Usage:**
```
@medication-reminder Add Heartgard for Max, monthly on 1st of month
@medication-reminder Show today's medications
@medication-reminder Remind me to refill Max's medication
```

### 3. health-record-keeper (Haiku)
Health record management and vaccination history.

**Usage:**
@health-record-keeper Add vaccination: Rabies for Max on 2024-03-15
@health-record-keeper Show Max's complete health history
@health-record-keeper Export health records for travel
```

### 4. care-routine-tracker (Haiku)
Daily care routine and activity tracking.

**Usage:**
```
@care-routine-tracker Log: Fed Max 1 cup at 7am
@care-routine-tracker Track 30-minute walk with Max
@care-routine-tracker Show this week's grooming schedule
```

## Skills

### veterinary-care
Vaccination schedules, appointment patterns, preventive care timelines.

### pet-health
Medication tracking, health monitoring, common conditions by species.

### daily-care
Feeding guidelines, exercise requirements, grooming schedules.

## Templates

### pet-profile.json
Pet information including breed, birthdate, microchip, emergency contacts.

### health-records.json
Vaccination history, vet visits, medications, medical conditions.

### care-schedule.json
Daily/weekly/monthly care routines including feeding, exercise, grooming.

## Getting Started

### 1. Create Pet Profile
```
@health-record-keeper Add pet: Max, Golden Retriever, born May 15, 2020
```

### 2. Add Health Records
```
@health-record-keeper Add rabies vaccination: March 15, 2024, due March 15, 2027
@vet-appointment-scheduler Schedule annual checkup in 6 months
```

### 3. Set Up Medications
```
@medication-reminder Add Heartgard monthly on 1st of month
@medication-reminder Add Frontline flea prevention monthly
```

### 4. Create Care Routine
```
@care-routine-tracker Set feeding schedule: 7am and 6pm, 1 cup each
@care-routine-tracker Add daily walks: 7:30am and 6:30pm, 30 minutes
```

### 5. Track Daily Care
```
@care-routine-tracker Log: Fed Max breakfast
@care-routine-tracker Log: 30-minute walk completed
```

## Vaccination Schedules

### Dogs
- **Puppies**: DHPP series (6, 10, 14 weeks), Rabies (16 weeks)
- **Adults**: DHPP every 3 years, Rabies every 1-3 years
- **Optional**: Bordetella, Lyme, Influenza (based on lifestyle)

### Cats
- **Kittens**: FVRCP series (6, 10, 14 weeks), Rabies (16 weeks)
- **Adults**: FVRCP every 3 years, Rabies every 1-3 years
- **Optional**: FeLV (outdoor cats)

## Best Practices

1. **Regular vet visits**: Annual wellness exams, semi-annual for seniors
2. **Medication adherence**: Never skip heartworm prevention
3. **Daily care logs**: Track feeding, exercise, bathroom habits
4. **Weight monitoring**: Prevent obesity through portion control
5. **Emergency preparedness**: Keep emergency vet contact info current

## Cost Optimization

All agents use **Haiku** for fast, cost-effective pet care management.

## License

MIT
