# Medical Writer Plugin

Medical and scientific writing specialist for creating clinical trial protocols, medical manuscripts, patient information leaflets, regulatory submissions, and scientific abstracts.

## Overview

The Medical Writer plugin provides specialized agents for creating accurate, compliant medical and scientific documentation following regulatory standards (FDA, EMA, ICH-GCP), medical writing guidelines (AMA, APA, ICMJE), and plain language principles.

## Agents

### 1. protocol-writer (Sonnet, Skill-Aware)
Creates comprehensive clinical trial protocols following ICH-GCP E6 guidelines.

**Use for**: Clinical study protocols, informed consent forms, case report forms, study amendments

**Example**:
```
Use protocol-writer to create Phase III clinical trial protocol.
Study: Randomized, double-blind, placebo-controlled trial
Intervention: Novel diabetes medication
Population: Type 2 diabetes patients (n=500)
Primary endpoint: HbA1c reduction at 24 weeks
Include: Background, objectives, design, methods, statistical analysis, safety monitoring
Standards: ICH-GCP E6(R2), FDA 21 CFR Part 312
```

### 2. manuscript-author (Sonnet, Skill-Aware, WebSearch)
Authors medical manuscripts for peer-reviewed journals following ICMJE guidelines.

**Use for**: Original research articles, systematic reviews, case reports, clinical guidelines

**Example**:
```
Use manuscript-author to write manuscript for cardiovascular study.
Study type: Retrospective cohort study
Findings: Novel biomarker predicts heart failure risk
Data: 1,200 patients, 5-year follow-up, HR 2.3 (95% CI 1.8-2.9)
Target journal: JAMA Cardiology (3,000-3,500 words)
Format: ICMJE Recommendations, STROBE checklist for cohort studies
Include: Abstract (300 words), Introduction, Methods, Results, Discussion, References
```

### 3. patient-educator (Sonnet, Skill-Aware)
Creates patient-facing materials in plain language (6th-8th grade reading level).

**Use for**: Patient information leaflets, informed consent forms, medication guides, health education materials

**Example**:
```
Use patient-educator to create patient information leaflet for new cancer drug.
Drug: Immunotherapy for melanoma
Audience: Cancer patients (varied health literacy)
Content: What it is, how it works, benefits, side effects, what to expect
Reading level: 6th-8th grade (Flesch-Kincaid)
Length: 2-page brochure
Standards: FDA Plain Language guidelines, CDC Clear Communication Index
```

### 4. regulatory-writer (Sonnet, Skill-Aware)
Prepares regulatory submissions for FDA, EMA, and other health authorities.

**Use for**: IND/NDA submissions, clinical study reports, regulatory responses, briefing documents

**Example**:
```
Use regulatory-writer to prepare FDA IND submission for gene therapy.
Therapy: AAV-based gene therapy for rare genetic disorder
Submission: Investigational New Drug (IND) application
Modules: Module 2 (summaries), Module 3 (CMC), Module 4 (nonclinical), Module 5 (clinical)
Include: Investigator's Brochure, protocol, CMC information, preclinical data
Format: eCTD (electronic Common Technical Document)
Standards: FDA 21 CFR 312, ICH M4 guidelines
```

## Skills

### medical-writing
Comprehensive medical writing standards and guidelines:
- **Regulatory**: FDA regulations (21 CFR), EMA guidelines, ICH-GCP, eCTD format
- **Clinical trials**: Protocol structure (ICH E6), informed consent, statistical reporting (ICH E9)
- **Publication**: ICMJE guidelines, CONSORT/STROBE/PRISMA reporting checklists
- **Plain language**: FDA Plain Language guidelines, CDC Clear Communication, health literacy principles
- **Medical style**: AMA Manual of Style, APA style for medical writing
- **Ethics**: Declaration of Helsinki, Good Publication Practice (GPP3)

## Templates

### clinical-trial-protocol-template.md
Complete ICH-GCP compliant protocol structure: Title page, synopsis, background, objectives, trial design, selection criteria, interventions, assessments, statistical considerations, ethics, data management, references, appendices.

### medical-manuscript-template.md
ICMJE-compliant manuscript template: Title page, abstract (structured), introduction, methods, results, discussion, acknowledgments, references, tables, figures. Includes CONSORT/STROBE/PRISMA checklists.

### patient-information-leaflet-template.md
Plain language patient education template: What it is, why you need it, how to take it, side effects, warnings, storage, FAQs. Optimized for 6th-8th grade reading level with visual aids.

### regulatory-submission-template.md
Regulatory submission structure (eCTD format): Module 1 (administrative), Module 2 (summaries), Module 3 (quality/CMC), Module 4 (nonclinical), Module 5 (clinical). FDA/EMA specific requirements.

## Workflows

### Complete Clinical Development Documentation
```
1. Protocol development
Use protocol-writer to create Phase II/III protocol with ICH-GCP compliance

2. Patient materials
Use patient-educator to create informed consent and patient information leaflet

3. Regulatory submission
Use regulatory-writer to prepare IND/CTA submission for health authorities

4. Publication
Use manuscript-author to write journal manuscript when study completes
```

### Medical Publication Workflow
```
1. Draft manuscript
Use manuscript-author with ICMJE guidelines and appropriate reporting checklist

2. Internal review
Review for accuracy, completeness, disclosure of conflicts

3. Journal submission
Format according to target journal requirements

4. Revisions
Use manuscript-author to address peer reviewer comments

5. Patient summary
Use patient-educator to create plain language summary for patients
```

## Requirements Met

✅ Role: Medical and scientific writing specialist
✅ Clinical trial protocols: protocol-writer with ICH-GCP E6 compliance
✅ Medical manuscripts: manuscript-author with ICMJE guidelines and reporting checklists
✅ Patient information leaflets: patient-educator with plain language (6th-8th grade)
✅ Regulatory submissions: regulatory-writer with FDA/EMA/ICH standards
✅ Scientific abstracts: Covered by manuscript-author (abstracts for journals, conferences)
✅ Tools: Medical databases (WebSearch for PubMed, clinical trials), file operations, templates

## Key Features

✓ **Regulatory compliance**: FDA 21 CFR, EMA guidelines, ICH-GCP, eCTD format
✓ **Publication standards**: ICMJE, CONSORT, STROBE, PRISMA reporting
✓ **Plain language**: 6th-8th grade reading level for patient materials
✓ **Medical accuracy**: Evidence-based, scientifically rigorous
✓ **Ethical standards**: Declaration of Helsinki, Good Publication Practice
✓ **Quality assurance**: Structured templates, compliance checklists

## Important Disclaimers

⚠️ **Medical Review Required**: All output requires review by qualified medical professionals, regulatory experts, or clinical researchers before use.

⚠️ **Not Medical Advice**: This plugin assists with medical writing but does not provide medical advice, diagnosis, or treatment recommendations.

⚠️ **Regulatory Responsibility**: Users are responsible for ensuring regulatory compliance. This tool aids documentation but doesn't guarantee regulatory approval.

⚠️ **Clinical Oversight**: Clinical trial protocols require IRB/ethics committee review and qualified investigator oversight.

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive medical-writing skill with regulatory and publication standards
- ✅ 4 professional templates for protocols, manuscripts, patient materials, and regulatory submissions
- ✅ Complete README with workflows and disclaimers
- ✅ Compliance with ICH-GCP, ICMJE, FDA, and EMA guidelines

## Best Practices

1. **Always verify medical accuracy** with subject matter experts
2. **Follow regulatory requirements** for your jurisdiction and indication
3. **Use appropriate reporting checklists** (CONSORT for RCTs, STROBE for observational studies, PRISMA for systematic reviews)
4. **Maintain patient confidentiality** (HIPAA, GDPR compliance)
5. **Disclose conflicts of interest** per ICMJE requirements
6. **Use plain language** for patient-facing materials (6th-8th grade level)
7. **Cite sources properly** using AMA or APA style
8. **Keep audit trails** for regulatory submissions and protocols

## Medical Writing Standards Reference

- **FDA**: 21 CFR Parts 11, 50, 56, 312, 314, 601
- **ICH Guidelines**: E6 (GCP), E9 (Statistics), M4 (CTD), E2A (Safety Reporting)
- **EMA**: Clinical Trial Regulation (EU) 536/2014
- **ICMJE**: Recommendations for manuscript preparation
- **Reporting**: CONSORT, STROBE, PRISMA, SPIRIT, ARRIVE
- **Ethics**: Declaration of Helsinki, Good Publication Practice (GPP3)
- **Style**: AMA Manual of Style (11th ed), APA Publication Manual (7th ed)

Closes #68
