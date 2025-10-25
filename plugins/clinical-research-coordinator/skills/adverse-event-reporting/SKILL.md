# Adverse Event Reporting Skill

Comprehensive patterns for adverse event documentation, causality assessment, severity grading, and regulatory reporting following ICH-E2A and FDA guidelines.

## AE vs SAE Classification

### Adverse Event (AE) Definition
**Any untoward medical occurrence** in a patient or clinical investigation subject administered a pharmaceutical product, which does not necessarily have a causal relationship with this treatment.

**Key Points**:
- Does NOT require causality
- Includes any unfavorable and unintended sign, symptom, or disease
- Temporally associated with use of investigational product
- Whether or not considered related to product

**Examples**:
- New illness or symptom
- Worsening of pre-existing condition
- Laboratory abnormality (if clinically significant)
- Injury or accident
- Abnormal physical exam finding (if new or worsening)

### Serious Adverse Event (SAE) Criteria

An AE is "serious" if it results in **ANY** of the following:

1. **Death**
   - Death during study
   - Death after study if related to study drug
   - Include time from event to death

2. **Life-Threatening**
   - Patient at immediate risk of death from event
   - NOT: Event that hypothetically might cause death if more severe
   - Example: Anaphylaxis (life-threatening), headache (not life-threatening even if severe)

3. **Hospitalization or Prolongation**
   - Requires inpatient hospitalization
   - Prolongs existing hospitalization
   - Excludes: Hospitalization for elective procedure unrelated to AE
   - Excludes: Social admission, convenience

4. **Persistent or Significant Disability/Incapacity**
   - Substantial disruption of ability to conduct normal life functions
   - Example: Stroke with residual paralysis
   - NOT: Temporary discomfort

5. **Congenital Anomaly/Birth Defect**
   - In offspring of subject who received study drug

6. **Important Medical Event (IME)**
   - Medical or scientific judgment
   - May jeopardize patient
   - May require intervention to prevent serious outcome
   - Examples:
     - Intensive treatment for bronchospasm in ER (not hospitalized)
     - Development of drug dependency
     - Severe blood dyscrasia
     - Seizure without hospitalization

## Severity Grading

### CTCAE v5.0 (Common Terminology Criteria for Adverse Events)

**Grade 1 - Mild**
- Asymptomatic or mild symptoms
- Clinical or diagnostic observations only
- Intervention not indicated

**Grade 2 - Moderate**
- Minimal, local, or noninvasive intervention indicated
- Limiting age-appropriate instrumental ADL*
- *Instrumental ADL: preparing meals, shopping, managing money, phone, housekeeping

**Grade 3 - Severe**
- Medically significant but not immediately life-threatening
- Hospitalization or prolongation of hospitalization indicated
- Disabling; limiting self-care ADL**
- **Self-care ADL: bathing, dressing, eating, toileting, mobility

**Grade 4 - Life-Threatening**
- Urgent intervention indicated
- Life-threatening consequences

**Grade 5 - Death**
- Death related to AE

### Examples by Body System

**Anemia (Hemoglobin)**:
- Grade 1: <LLN-10 g/dL; <LLN-6.2 mmol/L
- Grade 2: <10-8 g/dL; <6.2-4.9 mmol/L
- Grade 3: <8 g/dL; <4.9 mmol/L; transfusion indicated
- Grade 4: Life-threatening; urgent intervention indicated
- Grade 5: Death

**Nausea**:
- Grade 1: Loss of appetite without alteration in eating habits
- Grade 2: Oral intake decreased without significant weight loss
- Grade 3: Inadequate oral caloric/fluid intake; IV fluids indicated
- Grade 4: N/A
- Grade 5: N/A

**Diarrhea**:
- Grade 1: <4 stools/day over baseline
- Grade 2: 4-6 stools/day over baseline
- Grade 3: ≥7 stools/day over baseline; IV fluids indicated
- Grade 4: Life-threatening; urgent intervention indicated
- Grade 5: Death

**Hypertension**:
- Grade 1: SBP 120-139 or DBP 80-89 mmHg
- Grade 2: SBP 140-159 or DBP 90-99 mmHg; intervention indicated
- Grade 3: SBP ≥160 or DBP ≥100 mmHg; medical intervention indicated
- Grade 4: Life-threatening (e.g., malignant hypertension); urgent intervention indicated
- Grade 5: Death

## Causality Assessment

### Relationship Categories

**Unrelated (Not Related)**
- Clearly due to another cause (disease, environment, other drug)
- Temporal relationship makes relationship unlikely
- Example: Subject develops pneumonia 6 months after single dose; unrelated

**Unlikely (Doubtful)**
- More likely explained by alternative cause
- Temporal relationship present but unconvincing
- Not consistent with known drug effects
- Example: Headache 24 hours after starting drug, but subject has migraines

**Possible (Potentially Related)**
- Could be related to study drug
- Alternative causes also plausible
- Temporal relationship reasonable
- Consistent with known drug effects, but not specific
- Example: Nausea 2 days after starting drug (nausea is common with drug, but patient also has GI disease)

**Probable (Likely Related)**
- Temporal relationship convincing
- Follows known pattern for drug
- Difficult to explain by alternative causes
- Improved with dechallenge (if applicable)
- Example: Rash appearing 3 days after drug initiation, resolves when drug stopped, no other explanation

**Definite (Certainly Related)**
- Clear temporal relationship
- Follows known pattern
- Cannot be explained by disease or other causes
- Rechallenge positive (if done - usually not ethical)
- Pharmacologically plausible
- Example: Anaphylaxis during infusion of study drug

### Causality Assessment Factors

**1. Temporal Relationship**
- When did event occur relative to drug administration?
- Reasonable time frame for drug effect?
- Onset: Immediate vs. delayed
- Duration: Transient vs. persistent

**2. Known Drug Effects**
- Is event listed in Investigator's Brochure?
- Reported in preclinical studies?
- Reported in previous clinical trials?
- Known class effect?

**3. Dechallenge**
- Did event improve when drug stopped/reduced?
- Time course of improvement
- Complete resolution vs. partial

**4. Rechallenge**
- Did event recur when drug restarted?
- (Rarely done - ethical concerns)
- Strongest evidence of causality

**5. Alternative Causes**
- Underlying disease progression?
- Concomitant medications?
- Pre-existing conditions?
- Environmental factors?

**6. Biological Plausibility**
- Pharmacologically reasonable?
- Mechanism understood?
- Dose-related?

**7. Laboratory Evidence**
- Drug levels correlate with event?
- Biomarkers support relationship?

### Causality Assessment Algorithm

```
START
↓
Is there temporal relationship? (Drug before event?)
NO → UNRELATED
YES ↓
Is event consistent with known drug effects?
NO → Alternative causes obvious? YES → UNRELATED
                                 NO → UNLIKELY
YES ↓
Are there alternative causes that better explain event?
YES → POSSIBLE
NO ↓
Did event improve with dechallenge (if applicable)?
NO → POSSIBLE
YES → PROBABLE
↓
Did event recur with rechallenge (if done)?
YES → DEFINITE
NO → PROBABLE
```

## Expectedness

### Expected AE
**Definition**: Event listed in Investigator's Brochure (IB) or product label with comparable specificity and severity

**Includes**:
- Event type matches
- Severity matches or less
- Frequency consistent with IB

**Example**: Nausea (Grade 1-2) when IB lists "nausea (common)"

### Unexpected AE
**Definition**: Event NOT listed in current IB/label, OR greater severity/specificity than listed

**Includes**:
- Event type not listed at all
- More severe than described (Grade 3 when only Grade 1-2 listed)
- More specific diagnosis (MI when only "cardiac events" listed)

**Example**: Anaphylaxis when IB lists only "mild allergic reactions"

**Regulatory Impact**:
- Unexpected + Serious + Related = Expedited reporting to FDA (IND Safety Report)
- Updates to IB may be required
- Consent form updates

## Regulatory Reporting

### SAE Reporting Timelines

**To Sponsor/CRO**:
- **Fatal or Life-Threatening**: 24 hours (phone/email)
- **Other SAEs**: 24-48 hours (per protocol)
- **Follow-up**: As information becomes available

**Sponsor to FDA (IND Safety Reports)**:
- **Fatal or Life-Threatening + Unexpected + Related**: 7 calendar days
- **Other Serious + Unexpected + Related**: 15 calendar days
- **Follow-up**: 15 calendar days from initial report

**To IRB/EC**:
- Per local requirements (typically 5-15 days)
- Unanticipated problems involving risk
- Protocol deviations affecting safety

### IND Safety Report Criteria (FDA)

Report required if ALL three:
1. **Serious**: Meets SAE criteria
2. **Unexpected**: Not in IB/label
3. **Related**: At least possibly related

**Types**:
- 7-day: Fatal or life-threatening
- 15-day: Other serious unexpected suspected AEs
- Annual: Summary of all SAEs

### Reporting Content

**Minimum Information for Initial Report**:
- Identifiable reporter
- Identifiable patient (ID, initials, DOB or age, sex)
- Suspect drug
- Adverse event or outcome

**Complete Information**:
- Patient demographics
- Medical history
- Concomitant medications
- Event description (detailed narrative)
- Onset date/time
- Event outcome and date
- Seriousness criteria met
- Severity grade
- Causality assessment
- Action taken with study drug
- Dechallenge/rechallenge (if applicable)
- Relevant lab values
- Treatment for event

## AE Documentation Best Practices

### Source Documentation

**Required Elements**:
- Patient identifier
- Date of visit/contact
- AE reported by patient (exact words when possible)
- Onset date (at least month/year)
- End date or "ongoing"
- Severity assessment (with justification)
- Action taken
- Outcome
- Provider signature and date

**Good Documentation**:
```
10-Jan-2025: Patient reports "stomach pain and nausea" starting
yesterday evening, ~2 hours after taking study drug. Pain located in
epigastric region, 5/10 intensity, constant. Also reports two episodes
of non-bloody, non-bilious emesis. Denies fever, diarrhea. Ate usual
dinner. No change in other medications. Exam: Abdomen soft, mild
epigastric tenderness, no rebound. Advised to take with food and use
antacid PRN. Will follow up in 3 days. AE: Nausea and vomiting, Grade 2,
possibly related to study drug. No action taken with study drug.
- Dr. Smith, 10-Jan-2025
```

**Poor Documentation**:
```
10-Jan-2025: GI upset. Patient ok. Continue study.
```

### Case Report Form (CRF)

**AE Page Should Capture**:
- AE term (MedDRA preferred term)
- Verbatim term (patient's words)
- Body system
- Onset date (at least partial)
- End date or ongoing
- Continuing at study completion?
- Severity (Grade 1-5)
- Serious? (Y/N)
- If serious, criteria (check all that apply)
- Relationship to study drug
- Relationship to study procedures
- Action taken with study drug (none, reduced, interrupted, discontinued)
- Treatment for AE (Y/N, describe)
- Outcome (recovered, recovering, not recovered, fatal, unknown)

### MedDRA Coding

**Medical Dictionary for Regulatory Activities**:
- Standardized medical terminology
- Hierarchical structure
- Used for regulatory submissions

**Hierarchy**:
- System Organ Class (SOC): "Gastrointestinal disorders"
- High Level Group Term (HLGT): "Gastrointestinal signs and symptoms"
- High Level Term (HLT): "Nausea and vomiting symptoms"
- Preferred Term (PT): "Nausea" (THIS IS WHAT'S USED)
- Lowest Level Term (LLT): "Feeling nauseous"

**Coding Best Practices**:
- Code to most specific diagnosis (not signs/symptoms if diagnosis known)
- Use PT level for data entry
- One AE = one PT (don't use "syndrome" codes)
- Be consistent
- Use latest MedDRA version

**Examples**:
- Verbatim: "stomach pain" → PT: "Abdominal pain" (not "pain")
- Verbatim: "heart attack" → PT: "Myocardial infarction" (not "chest pain")
- Verbatim: "bad headache" → PT: "Headache" (severity captured separately)

## Safety Signal Detection

### Signal Definition
**Safety signal**: Information arising from one or multiple sources that suggests a new potentially causal association, or a new aspect of a known association, between an intervention and an event.

### Monitoring Strategies

**Individual Case Review**:
- Review all SAEs immediately
- Look for patterns by:
  - Event type
  - Time to onset
  - Dose relationship
  - Patient characteristics

**Aggregate Review**:
- Regular safety data review meetings
- DSMB meetings with unblinded data
- Compare to:
  - Expected rates from IB
  - Placebo/comparator rates
  - Background population rates

**Statistical Methods**:
- Disproportionality analysis (for large databases)
- Bayesian methods
- Time-to-event analysis

### Actions Based on Signals

**If signal detected**:
1. **Investigate**: Review all cases, request follow-up
2. **Assess causality**: Could it be real?
3. **Evaluate seriousness**: Public health impact?
4. **Determine actions**:
   - Update IB
   - Update consent forms
   - Protocol amendment (exclusions, monitoring)
   - Notify investigators
   - Regulatory notification
   - Study pause or termination (if severe)

## Special Situations

### Pregnancy

**Pregnancy Itself**:
- NOT an AE (physiologic state)
- Should be reported to sponsor immediately
- Follow per protocol (often leads to discontinuation)

**Pregnancy Outcomes**:
- Live birth: NOT an AE
- Spontaneous abortion: SAE (medical event of concern)
- Stillbirth: SAE (death)
- Congenital anomaly: SAE
- Elective termination: NOT an AE (unless medically indicated)

### Pre-Existing Conditions

**Worsening of Pre-Existing**:
- IS an AE
- Code the condition (not "worsening")
- Severity reflects current state
- Document baseline severity for comparison

**Stable Pre-Existing**:
- NOT an AE
- Captured in medical history

### Laboratory Abnormalities

**When to Report as AE**:
- New abnormality not present at baseline
- Worsening of baseline abnormality
- Clinically significant per investigator judgment
- Requires intervention

**How to Report**:
- Use specific lab term: "Increased ALT" not "abnormal LFTs"
- Include actual values in narrative
- Grade per CTCAE
- Assess if meets SAE criteria (hospitalization, medical event)

### Deaths

**All Deaths Reported as SAE**:
- Even if unrelated
- Complete narrative of events leading to death
- Autopsy report if available
- Death certificate if available

**Required Information**:
- Date/time of death
- Cause of death (primary, contributing)
- Relationship to study drug
- Relationship to underlying disease
- Timeline of events

## Quality Metrics

### AE Collection Quality
- **Completeness**: All AEs documented (target 100%)
- **Timeliness**: AEs entered within 5 days of visit (target >90%)
- **Accuracy**: Coding correct (target >95%)

### SAE Reporting Quality
- **Timeliness**: Initial report within timeline (target 100%)
- **Completeness**: All required fields complete (target >95%)
- **Follow-up**: Follow-up reports timely (target >90%)

### Safety Oversight
- **DSMB Review**: All serious events reviewed (target 100%)
- **Signal Detection**: Regular aggregate review (monthly minimum)
- **Investigator Notification**: Safety letters distributed timely (target <15 days)

---

**Version**: 1.0
**Last Updated**: January 2025
**Regulatory References**: ICH-E2A, CTCAE v5.0, FDA 21 CFR 312.32
**Key Principles**: Timely reporting, thorough assessment, subject safety first
