# AI Project Concept Template for Windesheim/VCH

**All projects follow Agile principles with iterative development, regular sprint cycles, and continuous stakeholder feedback.**

---

## VISUAL ASSETS & BRANDING

**Project Folder:**
`assets/projects/clearroots/`

**Required Assets:**
- [ ] `hero-image.jpg` or `hero-image.png` (1200x600px recommended) - Coffee farm/mobile app visual
- [ ] `logo.png` or `icon.svg` (if project has its own branding)
- [ ] `thumbnail.jpg` (400x300px) - For project cards on homepage

**Optional Assets:**
- [ ] `diagram-architecture.png` - Shows mobile → blockchain → compliance doc flow
- [ ] `screenshot-mobile-app.png` - Mobile interface for farmers
- [ ] `screenshot-dashboard.png` - Importer dashboard view

---

## PROJECT CONCEPT

### Basic Information
**Project Title:** ClearRoots

**Project Slug:** `clearroots`

**Concept Status:** in-development

**Category:** research / partner-collaboration / internal-tool

**GitHub Repository:** https://github.com/Value-Chain-Hacking/ClearRoots

---

## THE 3 MINUTE RULE PITCH
*(Answer these 6 questions from Brant Pinvidic's framework)*

### 1. What is it?
A mobile-first compliance platform that helps coffee farmers collect the data EU regulations require and turns it into verified documentation for importers.

### 2. How does it work?
Farmers use a mobile app (works offline) to record farm data and processing info. The system stores this in a blockchain ledger so it can't be tampered with. When importers need compliance documents for CSRD, CSDDD, or EUDR, the platform generates them automatically with all the farmer data already filled in.

### 3. Are you sure?
EU regulations are creating a compliance gap that's pushing smallholders out of markets. AgUnity provides the blockchain infrastructure that's already being used. AI can fill missing data using satellite imagery and GPS when farmers don't have complete records.

### 4. Can you do it?
[TO FILL - Team capabilities, access to farming cooperatives, technical expertise]

### 5. Can you make money? (or: What's the value?)
For farmers: access to EU markets without paying for expensive compliance consultants. For importers: affordable due diligence documentation. For cooperatives: data ownership and market power. Could explore insurance integration as revenue model.

### 6. Are there any risks?
- Farmers need smartphones and connectivity (even if app works offline)
- Data ownership and privacy concerns
- Adoption requires cooperative buy-in and training
- AI inference accuracy for missing documentation

---

### The Problem

**What problem does this solve?**
EU sustainability laws (CSDDD, CSRD, EUDR) require proof of ethical sourcing, but smallholder farmers don't have tools to generate compliant documentation. Without it, they lose market access. SME importers also lack affordable ways to do due diligence, forcing them toward either market exit or fraudulent compliance.

**Who has this problem?**
- Smallholder coffee farmers (expanding to cocoa and other commodities)
- EU SME importers of agricultural products
- Farming cooperatives managing hundreds of members

**How big is the problem?**
Creates "a dangerous compliance gap" affecting thousands of smallholder farmers globally. Market exclusion risk is real and immediate as EU regulations come into force.

---

### The AI Solution

**What AI/ML technique would you use?**
- Multilingual NLP for form guidance and translation
- Computer vision for satellite imagery analysis (verify deforestation claims)
- Data inference models to fill gaps (predict missing documentation from GPS, weather data)
- Document generation using rule-based systems + AI assistance

**Why does this need AI?**
Many farmers have incomplete records. AI can infer missing data points from available information (satellite images show forest cover, GPS data confirms location claims, weather patterns explain yield variations). Multilingual support requires NLP for multiple languages.

**What data would you need?**
- Farm location data (GPS coordinates)
- Satellite imagery (Copernicus, Planet Labs)
- Processing records (fermentation times, drying methods)
- Historical compliance documents for training
- Weather and environmental data
- Data availability: Satellite data is public, farm data needs to be collected, compliance doc templates exist

**Expected output/deliverable:**
Mobile app for farmers, web dashboard for importers/cooperatives, automated compliance document generation (PDF, JSON, HTML), blockchain-verified audit trails.

---

## TIMELINE & MILESTONES (Agile Planning)

### Project Duration
**Total Estimated Time:**
[TO FILL - Current GitHub shows 9 commits since April 2025, appears early stage]

**Sprint Length:**
2 weeks (recommended)

**Total Sprints:**
[TO FILL - Estimate based on full project scope]

### High-Level Timeline

**Phase 1: Discovery & Setup** (Estimated: ___ weeks)
- [ ] Partner with coffee cooperative for pilot
- [ ] Define data fields needed for EUDR compliance (start with one regulation)
- [ ] Set up AgUnity blockchain infrastructure access
- [ ] Design mobile app UX with farmer input

**Phase 2: MVP Development** (Estimated: ___ weeks)
- [ ] Build mobile data capture app (offline-first)
- [ ] Blockchain integration for data storage
- [ ] Basic document generation for EUDR
- [ ] Test with 10-20 farmers

**Phase 3: Iteration & Enhancement** (Estimated: ___ weeks)
- [ ] Add AI inference capabilities (satellite + GPS)
- [ ] Expand to CSRD and CSDDD compliance docs
- [ ] Build importer dashboard
- [ ] Multilingual support (English, Spanish, French, Amharic)

**Phase 4: Scale & Handoff** (Estimated: ___ weeks)
- [ ] Expand to 100+ farmers
- [ ] Add cocoa commodity support
- [ ] Insurance integration (optional)
- [ ] Cooperative data ownership tools

### Detailed Milestone Plan

[TO FILL - Create specific sprint-by-sprint milestone table with dates]

### Agile Ceremonies

**Daily Standups:**
[TO FILL]

**Sprint Planning:**
[TO FILL]

**Sprint Review/Demo:**
[TO FILL - Important to demo to farming cooperative partners]

**Sprint Retrospective:**
[TO FILL]

**Backlog Grooming:**
[TO FILL]

### Key Dates & Deadlines

- **Project Start Date:** [TO FILL]
- **Pilot Launch:** [TO FILL - Test with first cooperative]
- **EUDR Compliance Deadline:** [TO FILL - Check EU regulation dates]
- **Full Release:** [TO FILL]
- **External Deadlines:** [TO FILL - EU regulation enforcement dates]

---

### Feasibility Check

**Technical Difficulty:** Hard

**Required Skills:**
- Mobile development (offline-first architecture)
- Blockchain integration (AgUnity platform)
- AI/ML (computer vision, NLP, data inference)
- Supply chain compliance knowledge
- Multilingual UX design
- Document generation and templating

**Resources Needed:**
- Computing: Mobile devices for testing, cloud infrastructure for AI models, blockchain access
- Data: Satellite imagery APIs (Copernicus free, Planet Labs paid), GPS data, cooperative farm records
- People: Mobile dev team, AI engineers, supply chain experts, cooperative liaisons
- Budget: [TO FILL - Blockchain costs? Cloud AI inference? Satellite API costs?]

---

### Strategic Fit

**How does this align with VCH goals?**
Core mission alignment - directly helps smallholder farmers access markets, creates transparency in supply chains, uses technology for social impact.

**Potential Partners:**
- Coffee cooperatives in Ethiopia, Kenya, Colombia
- AgUnity (blockchain infrastructure provider)
- EU importers needing compliance solutions
- Insurance companies (future integration)

**Student Learning Value:**
Very high - combines mobile dev, blockchain, AI, supply chain ethics, regulatory compliance, and real-world field testing with farmers.

**Reusability:**
High - Platform can expand from coffee to cocoa, tea, palm oil, and other agricultural commodities. Core compliance logic reusable across products.

---

### Success Criteria

**How would you know if this worked?**
- 100+ farmers successfully using mobile app for data collection
- 10+ importers accept generated compliance documents
- Blockchain audit trail passes third-party verification
- AI inference accuracy >90% for satellite-based deforestation checks
- Documents accepted by EU customs/regulatory authorities

**Minimum Viable Product (MVP):**
Mobile app capturing basic farm data, blockchain storage, generates one EUDR compliance document for coffee, tested with one cooperative (20 farmers).

**Stretch Goals:**
- Insurance integration based on verified compliance data
- Cooperative data marketplace (farmers sell verified sustainability data)
- Expand to 5+ commodities
- Mobile payment integration
- AI-powered yield predictions to help farmers optimize

---

### Risks & Unknowns

**What could go wrong?**
- Smartphone penetration too low in target farming communities
- Blockchain costs become prohibitive at scale
- AI inference produces false compliance claims (legal liability)
- Regulatory authorities don't accept automated documentation
- Farmers don't trust the system with their data
- Cooperative politics prevent adoption

**What don't you know yet?**
- Will EU customs accept blockchain-verified compliance docs?
- What's the real smartphone ownership rate among target farmers?
- How accurate can satellite-based verification actually be?
- What are AgUnity's long-term costs and sustainability?
- Can cooperatives manage data governance?

**Deal-breakers:**
- Cannot achieve >85% AI accuracy for compliance verification
- Blockchain costs exceed €5 per farmer per year
- Regulators reject the documentation approach
- No cooperatives willing to pilot the system

---

### Next Steps

**What needs to happen before this becomes a real project?**
1. [TO FILL] Secure partnership with at least one coffee cooperative
2. [TO FILL] Verify AgUnity blockchain access and costs
3. [TO FILL] Map complete EUDR data requirements
4. [TO FILL] Build team with mobile dev + AI + supply chain expertise
5. [TO FILL] Field visit to understand farmer smartphone access

**Who needs to approve this?**
[TO FILL - Christiaan, cooperative leadership, AgUnity, Windesheim research ethics?]

**Timeline for decision:**
[TO FILL]

---

## CURRENT STATUS (from GitHub)

**Repository:** https://github.com/Value-Chain-Hacking/ClearRoots
**Status:** Active (9 commits, created April 2025)
**Current State:** Early development - planning documents and R project files visible

**Tech Stack:**
- Mobile-first interface (offline-capable)
- AgUnity blockchain ledger
- AI: Multilingual NLP, satellite imagery analysis, data inference
- Document generation: PDF, JSON, HTML formats
- Cooperative data ownership controls

**Key Features Planned:**
- Regulation-aligned documentation templates (CSRD, CSDDD, EUDR)
- Mobile data capture with offline sync
- Blockchain audit trails
- AI-supported inference for missing docs
- Assurance dossier generation for importers
- Optional insurance integration

**Contact:** info@clearroots.org | www.clearroots.org

---

## NOTES FOR COMPLETION

This outline needs:
- [ ] Specific timeline and sprint breakdown
- [ ] Team composition details
- [ ] Partnership status with cooperatives
- [ ] Budget breakdown (blockchain, AI APIs, satellite data)
- [ ] Field research plan
- [ ] Ethical approval for farmer data collection
- [ ] Visual assets (mobile app mockups, architecture diagrams)
