# AI Project Concept Template for Windesheim/VCH

**All projects follow Agile principles with iterative development, regular sprint cycles, and continuous stakeholder feedback.**

---

## VISUAL ASSETS & BRANDING

**Project Folder:**
`assets/projects/clearpaper/`

**Required Assets:**
- [ ] `hero-image.jpg` or `hero-image.png` (1200x600px recommended) - Main visual for website
- [ ] `logo.png` or `icon.svg` (if project has its own branding)
- [ ] `thumbnail.jpg` (400x300px) - For project cards on homepage

**Optional Assets:**
- [ ] `diagram-architecture.png` - System architecture or data flow
- [ ] `screenshot-*.png` - Screenshots of prototypes, dashboards, interfaces

---

## PROJECT CONCEPT

### Basic Information
**Project Title:** ClearPaper

**Project Slug:** `clearpaper`

**Concept Status:** in-development

**Category:** research / internal-tool / partner-collaboration

**GitHub Repository:** https://github.com/Value-Chain-Hacking/ClearPaper

---

## THE 3 MINUTE RULE PITCH
*(Answer these 6 questions from Brant Pinvidic's framework)*

### 1. What is it?
<!-- TO FILL: One clear sentence. What is this project? -->
Open-source templates that turn complex EU sustainability regulations into forms small businesses can actually fill out.

### 2. How does it work?
<!-- TO FILL: Explain the mechanics in 2-3 simple sentences. No jargon. -->
We map each field in the template directly to the specific EU regulation requirement. Businesses download the template (Word, PDF, JSON, or LaTeX), fill in their information, and have documentation that meets CSRD, CSDDD, or EUDR compliance requirements.

### 3. Are you sure?
<!-- TO FILL: What's your proof this can work? Evidence, similar projects, expert opinions, data availability? -->
Academic validation through Windesheim UAS partnership. Fields are mapped to legal source citations to ensure accuracy.

### 4. Can you do it?
<!-- TO FILL: Why are you/your team capable of pulling this off? Skills, experience, access to resources? -->
[TO FILL - Need info about team capabilities and resources]

### 5. Can you make money? (or: What's the value?)
<!-- TO FILL: For commercial projects: revenue model. For research/student projects: what value does this create? Impact? Learning outcomes? -->
Removes expensive consultant dependency for SME importers. Creates market access for smaller producers. Standardizes compliance documentation across EU member states.

### 6. Are there any risks?
<!-- TO FILL: Main risks in 2-3 bullets. Be honest. -->
- Regulations change frequently, templates need constant updates
- Legal accuracy must be verified by experts
- Adoption requires buy-in from importers and cooperatives

---

### The Problem

**What problem does this solve?**
EU compliance regulations (CSRD, CSDDD, EUDR) require documentation but there's no universal format. Small importers and producers can't afford compliance consultants (€10k-50k+), forcing them out of markets or into non-compliant guesswork.

**Who has this problem?**
- SME importers bringing goods into EU
- Smallholder farmer cooperatives exporting to EU
- Supply chain actors needing CSRD/CSDDD compliance

**How big is the problem?**
Every EU member state has different interpretations of regulations, creating fragmentation. Thousands of small businesses face compliance costs that exceed their profit margins.

---

### The AI Solution

**What AI/ML technique would you use?**
[TO FILL - Currently appears to be template-based, not AI. Consider if AI assists with field mapping, validation, or document generation]

**Why does this need AI?**
[TO FILL if applicable]

**What data would you need?**
- Complete text of CSRD, CSDDD, EUDR regulations
- Legal interpretations from member states
- Sample compliance documents from industry
- Data availability: Regulations are public, need legal expertise for validation

**Expected output/deliverable:**
Downloadable templates in Word, PDF, LaTeX, and JSON formats. Each template maps fields to specific regulation articles with citations.

---

## TIMELINE & MILESTONES (Agile Planning)

### Project Duration
**Total Estimated Time:**
[TO FILL - Example: 12 months for first release]

**Sprint Length:**
2 weeks (recommended)

**Total Sprints:**
[TO FILL based on total time estimate]

### High-Level Timeline

**Phase 1: Discovery & Setup** (Estimated: ___ weeks)
- [ ] Complete regulatory analysis (CSRD, CSDDD, EUDR)
- [ ] Field mapping documentation
- [ ] Template structure design

**Phase 2: MVP Development** (Estimated: ___ weeks)
- [ ] First template version (pick one regulation)
- [ ] Legal validation with Windesheim experts
- [ ] Multi-format export capability

**Phase 3: Iteration & Enhancement** (Estimated: ___ weeks)
- [ ] Add remaining regulation templates
- [ ] Localization for different member states
- [ ] User testing with pilot importers/cooperatives

**Phase 4: Delivery & Handoff** (Estimated: ___ weeks)
- [ ] Documentation and usage guides
- [ ] GitHub release and distribution
- [ ] Establish update process for regulation changes

### Detailed Milestone Plan

[TO FILL - Create specific sprint-by-sprint milestone table with dates]

### Agile Ceremonies

**Daily Standups:**
[TO FILL - When and how often?]

**Sprint Planning:**
[TO FILL - Example: "First Monday of each sprint, 1 hour"]

**Sprint Review/Demo:**
[TO FILL - Example: "Last Friday of each sprint, show progress to stakeholders"]

**Sprint Retrospective:**
[TO FILL - Example: "After each sprint, 30 min team reflection"]

**Backlog Grooming:**
[TO FILL - Example: "Mid-sprint, review upcoming tasks"]

### Key Dates & Deadlines

- **Project Start Date:** [TO FILL]
- **First Template Release:** [TO FILL]
- **Legal Validation Complete:** [TO FILL]
- **Full Release:** [TO FILL]
- **External Deadlines:** [TO FILL - any regulation compliance dates?]

---

### Feasibility Check

**Technical Difficulty:** Easy to Medium

**Required Skills:**
- Legal/regulatory analysis expertise
- Document template design (Word, LaTeX, JSON schemas)
- Supply chain knowledge
- Technical writing

**Resources Needed:**
- Computing: Standard laptop
- Data: EU regulation texts, legal expertise for validation
- People: Legal/regulatory experts + document designers + supply chain researchers
- Budget: €0 for open-source tools, possible legal consultation fees

---

### Strategic Fit

**How does this align with VCH goals?**
Directly supports supply chain transparency and smallholder farmer inclusion. Removes barriers to EU market access. Creates reusable open-source infrastructure.

**Potential Partners:**
- Smallholder cooperatives (coffee, cocoa)
- SME importers
- EU compliance consultants
- Legal departments at universities

**Student Learning Value:**
High - Students learn EU regulations, document standardization, legal research, and practical supply chain compliance challenges.

**Reusability:**
Very high - Templates can be adapted for different commodities, updated as regulations evolve, translated for different regions.

---

### Success Criteria

**How would you know if this worked?**
- At least 10 businesses use templates for actual compliance submissions
- Templates validated by legal experts
- All three regulation types (CSRD, CSDDD, EUDR) covered
- Available in 3+ languages

**Minimum Viable Product (MVP):**
One complete template for EUDR (most urgent) in English, validated by legal expert, available as Word and PDF.

**Stretch Goals:**
- Automated validation tool that checks if template is filled correctly
- Integration with ClearRoots for automatic field population
- Multilingual versions (French, German, Spanish)
- Template generator that adapts to regulation updates

---

### Risks & Unknowns

**What could go wrong?**
- Legal accuracy issues leading to invalid compliance documents
- Regulations change faster than we can update templates
- Adoption barriers if businesses don't trust open-source compliance
- Liability concerns if template guidance is incorrect

**What don't you know yet?**
- Will regulatory authorities accept standardized templates?
- How often do regulations actually change?
- What level of legal validation is sufficient?
- Can we maintain templates long-term?

**Deal-breakers:**
- Cannot get legal validation from qualified experts
- Regulatory authorities reject template approach
- Maintenance burden too high to sustain

---

### Next Steps

**What needs to happen before this becomes a real project?**
1. [TO FILL] Secure legal expert partnership for validation
2. [TO FILL] Prioritize which regulation to tackle first
3. [TO FILL] Define governance model for template updates
4. [TO FILL] Build team with regulatory + supply chain expertise

**Who needs to approve this?**
[TO FILL - Christiaan, legal partners, Windesheim research department?]

**Timeline for decision:**
[TO FILL]

---

## CURRENT STATUS (from GitHub)

**Repository:** https://github.com/Value-Chain-Hacking/ClearPaper
**Status:** Active (created April 30, 2025)
**Commits:** 2
**Current State:** Early planning stages - repository contains only README, no template files yet

**Tech Stack:**
- Output formats: Word, PDF, LaTeX, JSON
- No code implementation visible yet

**Key Features Planned:**
- Pre-built editable compliance documents
- Fields mapped to legal source citations
- Multi-format output
- Localized versions for jurisdictions
- Academic validation layer

**Contact:** info@clearroots.org | www.clearroots.org

---

## NOTES FOR COMPLETION

This outline needs to be filled with:
- [ ] Specific timeline dates and sprint breakdown
- [ ] Team composition and capabilities
- [ ] Agile ceremony schedule
- [ ] AI/ML components (if any) or clarify it's purely template-based
- [ ] Approval process and decision timeline
- [ ] Visual assets (logo, hero image, screenshots of templates)
