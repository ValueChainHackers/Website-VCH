# AI Project Concept Template for Windesheim/VCH

This template is for planning AI project ideas before fully committing to them. Use this to structure your thinking, identify requirements, and decide if the project is worth pursuing.

**All projects follow Agile principles with iterative development, regular sprint cycles, and continuous stakeholder feedback.**

## Instructions
1. Copy this template for each new AI project concept
2. Fill in as much as you know - it's OK to leave sections blank or mark as "TBD"
3. Save with a descriptive filename (e.g., `ai-chocolate-traceability-concept.md`)
4. Create a matching folder: `assets/projects/[project-name]/` for images and visual assets
5. Projects can be added to the website with "Concept" status to gauge interest
6. Once approved and resourced, convert to a full project

---

## VISUAL ASSETS & BRANDING

**Project Folder:**
`assets/projects/[project-name]/`

**Required Assets:**
- [ ] `hero-image.jpg` or `hero-image.png` (1200x600px recommended) - Main visual for website
- [ ] `logo.png` or `icon.svg` (if project has its own branding)
- [ ] `thumbnail.jpg` (400x300px) - For project cards on homepage

**Optional Assets:**
- `diagram-architecture.png` - System architecture or data flow
- `screenshot-*.png` - Screenshots of prototypes, dashboards, interfaces
- `mockup-*.png` - Design mockups or wireframes
- `presentation-deck.pdf` - Pitch deck or project overview slides
- `demo-video-thumbnail.jpg` - If you have a demo video

**Asset Checklist:**
```
assets/projects/[project-name]/
├── hero-image.png          ← Main banner image
├── thumbnail.png           ← Small card preview
├── logo.svg               ← Project logo (optional)
├── diagrams/
│   └── architecture.png
├── screenshots/
│   ├── dashboard.png
│   └── mobile-app.png
└── README.md              ← Asset documentation
```

---

## PROJECT CONCEPT

### Basic Information
**Project Title:**
<!-- Example: "AI-Powered Chocolate Supply Chain Traceability" -->

**Project Slug:**
<!-- URL-friendly name: "ai-chocolate-traceability" - This will be your folder name -->

**Concept Status:**
<!-- Choose ONE: brainstorm / under-review / approved / in-development / completed / on-hold -->

**Category:**
<!-- Choose ONE or MULTIPLE: student-project / research / partner-collaboration / internal-tool -->

---

## THE 3 MINUTE RULE PITCH
*(Answer these 6 questions from Brant Pinvidic's framework)*

### 1. What is it?
<!-- One clear sentence. What is this project? -->

### 2. How does it work?
<!-- Explain the mechanics in 2-3 simple sentences. No jargon. -->

### 3. Are you sure?
<!-- What's your proof this can work? Evidence, similar projects, expert opinions, data availability? -->

### 4. Can you do it?
<!-- Why are you/your team capable of pulling this off? Skills, experience, access to resources? -->

### 5. Can you make money? (or: What's the value?)
<!-- For commercial projects: revenue model. For research/student projects: what value does this create? Impact? Learning outcomes? -->

### 6. Are there any risks?
<!-- Main risks in 2-3 bullets. Be honest. -->

---

### The Problem

**What problem does this solve?**
<!-- Describe the actual problem in supply chains or research. Be specific. -->

**Who has this problem?**
<!-- Example: "Small chocolate importers who need to prove their cacao isn't from deforested areas" -->

**How big is the problem?**
<!-- Rough estimate of scale/impact. Example: "Affects 10,000+ smallholder farmers" or "Costs companies €50k+ annually" -->

---

### The AI Solution

**What AI/ML technique would you use?**
<!-- Examples: Computer Vision, NLP, Time Series Forecasting, Clustering, LLMs, Knowledge Graphs, etc. -->

**Why does this need AI?**
<!-- What makes this an AI problem vs. a regular software problem? -->

**What data would you need?**
<!-- Be specific: What kind of data? How much? Where would it come from? -->
- Data type 1:
- Data type 2:
- Data availability: (Do we have it? Can we get it? How hard?)

**Expected output/deliverable:**
<!-- What would the AI actually produce? Example: "A dashboard showing risk scores for each supplier" -->

---

### Feasibility Check

**Technical Difficulty:**
<!-- Choose ONE: Easy / Medium / Hard / Very Hard / Unknown -->

**Required Skills:**
<!-- List: Python, PyTorch, NLP, Supply Chain Knowledge, etc. -->

**Resources Needed:**
- Computing: <!-- Example: "Standard laptop" / "GPU required" / "Cloud computing budget" -->
- Data: <!-- Example: "Public datasets available" / "Need to collect" / "Partner must provide" -->
- People: <!-- Example: "1 student" / "Small team of 2-3" / "Needs ML expert supervision" -->
- Budget: <!-- If any: €500 / €2000 / €0 (all open-source) -->

---

## TIMELINE & MILESTONES (Agile Planning)

### Project Duration
**Total Estimated Time:**
<!-- Example: 6 months (September 2025 - February 2026) -->

**Sprint Length:**
<!-- Standard: 2 weeks | Alternative: 1 week / 3 weeks / 4 weeks -->

**Total Sprints:**
<!-- Example: 12 sprints of 2 weeks each -->

### High-Level Timeline

**Phase 1: Discovery & Setup** (Estimated: ___ weeks)
- Sprint 1-2: Project kickoff, requirements gathering, data exploration
- Sprint 3: Environment setup, initial data pipeline

**Phase 2: MVP Development** (Estimated: ___ weeks)
- Sprint 4-6: Core model development
- Sprint 7: First working prototype

**Phase 3: Iteration & Enhancement** (Estimated: ___ weeks)
- Sprint 8-10: Feature additions, model improvements
- Sprint 11: User testing and feedback integration

**Phase 4: Delivery & Handoff** (Estimated: ___ weeks)
- Sprint 12: Documentation, final testing, deployment

### Detailed Milestone Plan

| Sprint | Dates | Milestone | Deliverables | Success Criteria |
|--------|-------|-----------|--------------|------------------|
| 1 | [Start Date] - [End Date] | Project Kickoff | • Project plan finalized<br>• Team roles assigned<br>• Initial stakeholder meeting | All stakeholders aligned on goals |
| 2 | | Data Discovery | • Data sources identified<br>• Sample data collected<br>• Data quality assessment | Have 80%+ of needed data |
| 3 | | Environment Setup | • Dev environment configured<br>• Git repo created<br>• First data pipeline running | Team can run basic scripts |
| 4 | | Baseline Model | • Simple benchmark model<br>• Evaluation metrics defined | Have something to beat |
| 5 | | Feature Engineering | • Features extracted<br>• Data preprocessing pipeline | Clean, usable dataset |
| 6 | | Model V1 | • First real model trained<br>• Initial results | Model better than baseline |
| 7 | | MVP Complete | • Working prototype<br>• Demo-ready | Can show to stakeholders |
| 8 | | Iteration 1 | • Model improvements<br>• Bug fixes | Accuracy improved by X% |
| 9 | | UI/Dashboard Start | • Interface mockups<br>• Basic visualization | Users can see outputs |
| 10 | | User Testing | • Prototype with users<br>• Feedback collected | 3+ users test it |
| 11 | | Refinement | • Feedback implemented<br>• Edge cases handled | Users say it's useful |
| 12 | | Final Delivery | • Documentation complete<br>• Code cleaned<br>• Handoff meeting | Project can be maintained |

**Customize this table for your specific project. Add or remove sprints as needed.**

### Agile Ceremonies

**Daily Standups:**
<!-- When and how often? Example: "Every Monday/Wednesday/Friday, 15 min, async on Discord" -->

**Sprint Planning:**
<!-- Example: "First Monday of each sprint, 1 hour" -->

**Sprint Review/Demo:**
<!-- Example: "Last Friday of each sprint, show progress to stakeholders" -->

**Sprint Retrospective:**
<!-- Example: "After each sprint, 30 min team reflection" -->

**Backlog Grooming:**
<!-- Example: "Mid-sprint, review upcoming tasks" -->

### Key Dates & Deadlines

- **Project Start Date:**
- **First Demo:** (Sprint 7 end)
- **User Testing Begins:** (Sprint 10)
- **Final Presentation:**
- **Project End Date:**
- **External Deadlines:** <!-- Conference submissions, partner requirements, etc. -->

---

### Strategic Fit

**How does this align with VCH goals?**
<!-- Does it help students learn? Support research? Solve real supply chain problems? Build useful tools? -->

**Potential Partners:**
<!-- Who might be interested? Companies, NGOs, researchers? -->

**Student Learning Value:**
<!-- What would students learn from this? Is it a good educational project? -->

**Reusability:**
<!-- Could this be used for multiple projects/industries, or is it very specific? -->

---

### Success Criteria

**How would you know if this worked?**
<!-- Be specific. Example: "Can identify cacao origin with >85% accuracy" or "Reduces manual data entry time by 50%" -->

**Minimum Viable Product (MVP):**
<!-- What's the smallest useful version of this? -->

**Stretch Goals:**
<!-- What could you add if you had more time/resources? -->

---

### Risks & Unknowns

**What could go wrong?**
<!-- Technical risks, data availability issues, partner backing out, etc. -->

**What don't you know yet?**
<!-- List your big question marks -->

**Deal-breakers:**
<!-- What would make you abandon this project? -->

---

### Next Steps

**What needs to happen before this becomes a real project?**
<!-- Example: "Need to secure partner commitment" / "Need to verify data availability" / "Need to find interested students" -->

**Who needs to approve this?**
<!-- Example: Christiaan, Windesheim department head, potential partner, etc. -->

**Timeline for decision:**
<!-- When do you want to decide go/no-go? -->

---

## EXAMPLE FILLED OUT

Here's a complete example:

---

## VISUAL ASSETS & BRANDING

**Project Folder:**
`assets/projects/ai-coffee-quality/`

**Required Assets:**
- [x] `hero-image.png` - Coffee farm landscape with data overlay
- [x] `thumbnail.png` - Coffee beans and graph icon
- [ ] `logo.svg` - Not needed yet

**Optional Assets:**
- `diagrams/model-architecture.png` - Shows data flow from farm to prediction
- `screenshots/dashboard-mockup.png` - Wireframe of farmer-facing app

---

## PROJECT CONCEPT

### Basic Information
**Project Title:** AI-Powered Coffee Quality Prediction from Farm Data

**Project Slug:** `ai-coffee-quality`

**Concept Status:** under-review

**Category:** student-project, partner-collaboration

---

## THE 3 MINUTE RULE PITCH

### 1. What is it?
A mobile tool that helps coffee farmers predict their harvest quality before it happens, using machine learning trained on past farm and processing data.

### 2. How does it work?
Farmers input details about their farm (altitude, rainfall) and how they process the coffee (fermentation time, drying method). The AI model compares this to thousands of past harvests and predicts what quality score they'll likely get. Then it suggests changes they could make to improve.

### 3. Are you sure?
Similar models exist for wine grape quality prediction with 85%+ accuracy. Coffee cooperatives already track this data, we just need to partner with one. Research papers show farm conditions strongly correlate with cup quality.

### 4. Can you do it?
We have two computer science students who completed the ML course. Christiaan has supply chain connections to get coffee data. We can start with a simple model in Python and test accuracy before building the app.

### 5. What's the value?
For farmers: better prices if they can improve quality, less income uncertainty. For students: real ML project with actual users and measurable impact. For coffee importers: better supply chain transparency and consistency.

### 6. Are there any risks?
- Might not get enough historical data (need 200+ samples)
- Model accuracy might be too low to be useful
- Farmers might not trust AI predictions over their experience

---

### The Problem
**What problem does this solve?**
Coffee farmers don't know their quality score until after harvest, roasting, and cupping (tasting). By then it's too late to fix problems. This causes income uncertainty and makes it hard to improve.

**Who has this problem?**
Smallholder coffee farmers in Ethiopia, Kenya, Colombia who sell specialty coffee. Also affects coffee importers who buy based on quality.

**How big is the problem?**
Affects 100,000+ smallholder specialty coffee farmers globally. Quality differences can mean 2x price difference.

### The AI Solution
**What AI/ML technique would you use?**
Supervised learning (Random Forest or XGBoost) to predict cupping scores from farm and processing data.

**Why does this need AI?**
Complex interactions between 20+ variables (altitude, rainfall, processing method, fermentation time, drying method). Traditional formulas don't work well.

**What data would you need?**
- Historical cupping scores (quality ratings) from past harvests
- Farm data: altitude, rainfall, soil type, shade coverage
- Processing data: fermentation hours, drying method, storage time
- Data availability: Coffee cooperatives and importers track this. Need partnership to access.

**Expected output/deliverable:**
Mobile app where farmers input their farm and processing choices, get predicted quality score and suggestions for improvement.

### Feasibility Check
**Technical Difficulty:** Medium

**Required Skills:**
- Python, scikit-learn basics
- Data cleaning and feature engineering
- Some supply chain knowledge (can be learned)
- Mobile app development (or start with web app)

**Resources Needed:**
- Computing: Standard laptop is fine
- Data: Need partnership with coffee importer or cooperative
- People: 2 students (one for ML, one for app) + supervision
- Budget: €0 (all open-source tools)

---

## TIMELINE & MILESTONES (Agile Planning)

### Project Duration
**Total Estimated Time:** 6 months (September 2025 - February 2026)

**Sprint Length:** 2 weeks

**Total Sprints:** 12 sprints

### High-Level Timeline

**Phase 1: Discovery & Setup** (6 weeks)
- Sprint 1-2: Partner meetings, data access negotiation, requirements
- Sprint 3: Python environment, initial data exploration

**Phase 2: MVP Development** (8 weeks)
- Sprint 4-6: Model development, testing different algorithms
- Sprint 7: First working model that beats baseline

**Phase 3: Iteration & Enhancement** (6 weeks)
- Sprint 8-9: Model improvements, feature engineering
- Sprint 10: Build simple web interface for testing

**Phase 4: Delivery & Handoff** (4 weeks)
- Sprint 11: User testing with 5 farmers, collect feedback
- Sprint 12: Final documentation, code cleanup, handoff

### Detailed Milestone Plan

| Sprint | Dates | Milestone | Deliverables | Success Criteria |
|--------|-------|-----------|--------------|------------------|
| 1 | Sep 1-14 | Kickoff | • Partner signed on<br>• Data sharing agreement<br>• Team roles assigned | Coffee partner committed |
| 2 | Sep 15-28 | Data Access | • Historical data received<br>• Data quality checked<br>• Feature list drafted | Have 200+ samples |
| 3 | Sep 29-Oct 12 | Setup Complete | • Python env ready<br>• Jupyter notebooks running<br>• First visualizations | Team can explore data |
| 4 | Oct 13-26 | Baseline Model | • Simple linear regression<br>• Train/test split<br>• Metrics defined | Have something to beat |
| 5 | Oct 27-Nov 9 | Feature Engineering | • 15+ features extracted<br>• Correlation analysis<br>• Feature selection | Clean feature matrix |
| 6 | Nov 10-23 | Model V1 | • Random Forest trained<br>• XGBoost comparison<br>• Cross-validation | Better than baseline |
| 7 | Nov 24-Dec 7 | MVP Demo | • Working model<br>• Demo for partner<br>• Mid-project review | Partner gives feedback |
| 8 | Dec 8-21 | Iteration 1 | • Model improvements<br>• Handle edge cases<br>• Error analysis | ±3 points accuracy |
| 9 | Jan 5-18 | Iteration 2 | • Feature importance<br>• Interpretability<br>• Documentation | Can explain predictions |
| 10 | Jan 19-Feb 1 | Web Interface | • Flask/Streamlit app<br>• Input form<br>• Prediction output | Farmers can use it |
| 11 | Feb 2-15 | User Testing | • 5 farmers test it<br>• Feedback session<br>• Bug fixes | Users find it useful |
| 12 | Feb 16-28 | Final Delivery | • Code on GitHub<br>• User guide written<br>• Final presentation | Project complete |

### Agile Ceremonies

**Daily Standups:** Every Monday/Wednesday/Friday, 15 min async on Discord

**Sprint Planning:** First Monday of each sprint, 1 hour on Zoom

**Sprint Review/Demo:** Last Friday of each sprint, show progress to Christiaan and partner

**Sprint Retrospective:** After sprint review, 30 min team-only reflection

**Backlog Grooming:** Mid-sprint, review and prioritize upcoming tasks

### Key Dates & Deadlines

- **Project Start Date:** September 1, 2025
- **First Demo:** November 24 (Sprint 7 end)
- **User Testing Begins:** February 2 (Sprint 11)
- **Final Presentation:** February 28, 2026
- **Project End Date:** February 28, 2026
- **External Deadlines:** None (internal project)

---

### Strategic Fit
**How does this align with VCH goals?**
- Practical AI application for agricultural supply chains
- Helps smallholder farmers (social impact)
- Good student learning project (real data, real impact)
- Could become reusable tool for other crops

**Potential Partners:**
- ClearCaff (coffee data platform)
- Local coffee roasters with direct trade relationships
- Coffee cooperatives in Ethiopia

**Student Learning Value:**
High - covers data cleaning, feature engineering, model selection, deployment, user research with farmers.

**Reusability:**
Medium - could adapt for cacao, tea, wine grapes with similar approach.

### Success Criteria
**How would you know if this worked?**
- Model predicts cupping scores within ±3 points (on 100-point scale)
- At least 5 farmers use the app and find it helpful
- Model identifies at least 2 actionable factors farmers can control

**Minimum Viable Product (MVP):**
Python script that takes CSV input and outputs prediction. No app needed initially.

**Stretch Goals:**
- Full mobile app with translations
- Regional models (Ethiopia vs Colombia might need different models)
- Integration with farm management software
- Recommendations engine ("try fermenting 2 hours longer")

### Risks & Unknowns
**What could go wrong?**
- Can't find partner willing to share cupping score data (it's sensitive business info)
- Not enough data samples (need 200+ for decent model)
- Variables we can collect don't actually predict quality well
- Farmers don't trust or use the predictions

**What don't you know yet?**
- What data is actually available from partners
- How cupping scores are measured consistently
- Whether farmers would actually change practices based on predictions

**Deal-breakers:**
- Can't get data with at least 200 samples
- Model accuracy is worse than random guessing
- No farmers interested in using it

### Next Steps
**What needs to happen before this becomes a real project?**
1. Talk to 2-3 coffee importers about data availability
2. Literature review - has anyone done this already?
3. Find 2 interested students
4. Confirm partner commitment

**Who needs to approve this?**
Christiaan + potential coffee partner

**Timeline for decision:**
2 months - decide by end of Q1 2025

---

## NOTES

**Tips for good AI project concepts:**
- Start with the problem, not the AI technique
- Be honest about what you don't know
- Smaller and focused is better than big and vague
- Consider if this really needs AI or if simpler solutions exist
- Think about who would actually use this

**Common mistakes to avoid:**
- "AI can solve everything" thinking
- Underestimating data requirements
- Not checking if someone already built this
- Ignoring the deployment/usage challenge
- Choosing trendy tech that doesn't fit the problem

**Agile Best Practices:**
- Keep sprints consistent (usually 2 weeks)
- Don't skip retrospectives - they're where you improve
- Demo working software every sprint, even if it's rough
- Adapt the plan as you learn - timelines will change
- Focus on delivering value, not checking boxes
- Make blockers visible early

**Managing Visual Assets:**
- Create the project folder structure early, even if you don't have all assets yet
- Use consistent naming: `hero-image.png`, `thumbnail.png`, `screenshot-dashboard.png`
- Keep original high-res files in a separate folder
- Document what each image shows in the folder README
- Update assets as the project evolves (mockup → screenshot → final)
- Use placeholder images if needed to visualize the website early
