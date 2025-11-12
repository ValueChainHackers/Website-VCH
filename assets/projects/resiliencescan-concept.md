# AI Project Concept Template for Windesheim/VCH

**All projects follow Agile principles with iterative development, regular sprint cycles, and continuous stakeholder feedback.**

---

## PROJECT CONCEPT

### Basic Information
**Project Title:** RecilienceScan

**Project Slug:** `resiliencescan`

**Concept Status:** in-development (Milestone 1 complete)

**Category:** internal-tool / research

**GitHub Repository:** https://github.com/Windesheim-A-I-Support/RecilienceScan

---

## THE 3 MINUTE RULE PITCH

### 1. What is it?
An automation system that takes survey responses about supply chain resilience and generates branded PDF reports without any manual copy-pasting or formatting.

### 2. How does it work?
Researchers export survey data as CSV. The system validates it automatically, generates a branded PDF report using Quarto and LaTeX, and emails it to recipients through Outlook. Everything that used to take hours of manual work happens in seconds.

### 3. Are you sure?
Already at Milestone 1 with 368 commits. The manual process exists and is painful - we're just automating what already works.

### 4. Can you do it?
[TO FILL - Team already has M1 working, on track for M2-M6]

### 5. What's the value?
Researchers save 2-3 hours per report. No more manual errors. Consistent branding. Reproducible workflow. Can hand off to new team members easily. For students: learn automation, validation, and report generation pipelines.

### 6. Are there any risks?
- Outlook integration might be fragile
- LaTeX template complexity
- Survey platform changes breaking integration
- Maintaining compatibility across different researcher setups

---

### The Problem

**What problem does this solve?**
Researchers currently export survey data from Power BI/Excel, manually clean it, format reports by hand in Word/PDF, and email them individually. This is time-consuming, error-prone, and hard to hand off when team members change.

**Who has this problem?**
Windesheim researchers creating Resilience Reports and similar survey-based deliverables. Any team generating repetitive reports from survey data.

---

### The AI Solution

**What AI/ML technique would you use?**
Not primarily AI - this is automation/validation. Future milestones may add AI for:
- Data quality anomaly detection
- Natural language report summaries
- Automated insight generation from patterns

**What data would you need?**
Survey response CSV files with validated schemas. Report templates. Email recipient lists.

**Expected output/deliverable:**
Automated pipeline from CSV → validated data → branded PDF → emailed to recipients with full audit trail.

---

## TIMELINE & MILESTONES (From GitHub)

### Completed:
**M1 (Milestone 1):** Feature Release One - COMPLETE
- CSV validation with schema and business rules
- Branded PDF generation via Quarto + LaTeX
- Outlook email delivery with logging
- Tested on clean VMs for reproducibility

### Planned:
**M2:** Enhanced validation and error handling
**M3:** GitHub Actions CI/CD
**M4:** Database/object storage migration
**M5:** Integration with survey platforms (Formbricks, LimeSurvey)
**M6:** Full open-source survey pipeline

---

## CURRENT STATUS (from GitHub)

**Repository:** https://github.com/Windesheim-A-I-Support/RecilienceScan
**Status:** Active (368 commits, 41 open issues, 5 PRs)
**Current State:** Milestone 1 complete, working toward M2

**Tech Stack:**
- Quarto + LaTeX (branded PDF generation)
- Python/R scripts (validation)
- Outlook integration (email delivery)
- Local file system (M1), database planned (M4)
- GitHub Actions (M3+)

**Key Features (Working):**
- Automated CSV validation
- Branded PDF report generation
- Email delivery with logging
- Reproducible workflow
- Audit trails
- Comprehensive documentation

**Roadmap:**
- M2: Better error handling
- M3: CI/CD automation
- M4: Database backend
- M5: Survey platform integration
- M6: End-to-end open-source pipeline

---

## NOTES FOR COMPLETION

**Next Steps from GitHub:**
- [ ] Define M2 validation enhancements
- [ ] Set up GitHub Actions (M3)
- [ ] Evaluate database options for M4
- [ ] Test Formbricks integration approach (M5)

**Key Questions:**
- What's the timeline for M2-M6?
- Which survey platform to integrate first?
- Will this expand beyond Resilience Reports?
- How many researchers/teams will use this?

[TO FILL - Detailed sprint breakdown for M2-M6, team assignments, testing plan]
