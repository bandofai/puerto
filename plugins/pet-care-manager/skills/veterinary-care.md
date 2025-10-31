# Veterinary Care Skill

Comprehensive patterns for vet appointments, vaccination schedules, and preventive care.

## Vaccination Schedules

### Dogs

**Puppies (6-16 weeks)**
- 6-8 weeks: DHPP (Distemper, Hepatitis, Parvovirus, Parainfluenza) #1
- 10-12 weeks: DHPP #2, Leptospirosis #1
- 14-16 weeks: DHPP #3, Leptospirosis #2, Rabies
- 6 months: Spay/neuter recommended

**Adult Dogs (Annual/Every 3 years)**
- DHPP: Every 3 years (after initial series)
- Rabies: Every 1 or 3 years (per local law)
- Bordetella: Every 6-12 months (if boarding)
- Leptospirosis: Annually
- Lyme: Annually (if endemic area)
- Canine Influenza: Annually (if at risk)

### Cats

**Kittens (6-16 weeks)**
- 6-8 weeks: FVRCP (Feline Viral Rhinotracheitis, Calicivirus, Panleukopenia) #1
- 10-12 weeks: FVRCP #2, FeLV (Feline Leukemia) #1
- 14-16 weeks: FVRCP #3, FeLV #2, Rabies
- 6 months: Spay/neuter recommended

**Adult Cats (Annual/Every 3 years)**
- FVRCP: Every 3 years (after initial series)
- Rabies: Every 1 or 3 years (per local law)
- FeLV: Annually (if at risk - outdoor cats)

## Preventive Care Schedule

### Puppies/Kittens (First Year)
- Monthly: Weigh, check for parasites
- 6-8 weeks: First vet visit, vaccines, deworming
- 10-12 weeks: Second vaccine series
- 14-16 weeks: Final vaccine series, microchip
- 6 months: Spay/neuter consultation

### Adult Pets (Annually)
- Annual wellness exam
- Vaccinations (as scheduled)
- Heartworm test (dogs)
- Fecal test (parasites)
- Dental check
- Blood work (if over 7 years)

### Senior Pets (7+ years)
- Wellness exam every 6 months
- Annual blood work
- Urinalysis
- Blood pressure check
- Dental evaluation

## Appointment Structure

```json
{
  "appointment": {
    "id": "appt-001",
    "petId": "pet-001",
    "type": "wellness",
    "date": "2025-03-15T10:00:00Z",
    "vet": "Dr. Smith",
    "clinic": "Happy Paws Veterinary",
    "reason": "Annual checkup",
    "vaccinations": ["Rabies", "DHPP"],
    "services": ["Wellness exam", "Heartworm test"],
    "cost": 150,
    "notes": "All vaccinations up-to-date",
    "nextVisit": "2026-03-15"
  }
}
```

## Emergency Vet Guidelines

### When to Seek Emergency Care
- Difficulty breathing
- Severe bleeding
- Seizures
- Unconsciousness
- Suspected poisoning
- Inability to urinate/defecate
- Bloated abdomen (especially large dogs)
- Severe vomiting/diarrhea
- Eye injuries
- Broken bones

### Emergency Contacts
- Primary vet emergency line
- 24/7 emergency clinic
- Poison control hotline (ASPCA: 888-426-4435)

## Best Practices

- Keep vaccination records accessible
- Schedule annual exams in advance
- Track preventive medication schedules
- Maintain emergency vet contact info
- Know your pet's baseline vitals
- Regular dental care (prevents disease)
