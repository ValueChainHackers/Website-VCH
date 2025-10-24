---
name: Research and Update CRM/Li-Monti Project Page
about: Read all CRM track documents, extract accurate information, and create comprehensive project page
title: '[TASK] Research and Update CRM/Li-Monti Project Page'
labels: 'task, student-project, content'
assignees: ''
---

## 📋 Task Summary
Read all 7 documents in the CRM track folder, extract accurate team and project information, and create a comprehensive student project page for the Li-Monti Connect project.

## 🎯 Context

### Background
The CRM track is one of three student project tracks from the current academic period. The folder contains 7 documents totaling ~29MB:
1. **Li-Monti Connect.pptx** (21MB) - Main presentation
2. **elevator pitch.docx** (22KB) - Project pitch
3. **li monti maps.docx** (875KB) - Mapping documentation
4. **pitch day update.docx** (582KB) - Progress update
5. **solution lithium till shark tank.docx** (2.2MB) - Solution document
6. **update document research.docx** (2.8MB) - Research documentation
7. **vch systems overview solution draft and interviews.docx** (1.2MB) - System overview

The project appears to focus on CRM (Customer Relationship Management) and lithium supply chain challenges.

### Why This Matters
- **Student Recognition:** Properly document students' work and learning journey
- **Project Showcase:** Demonstrate VCH's impact on real-world supply chain problems
- **Knowledge Preservation:** Capture insights for future students and partners
- **Accuracy Critical:** Team names, dates, and project details must be 100% accurate

### Related Work
- Successfully completed: Cacao Guide project page (reference example)
- Pending: Textile Track project (blocked waiting for team names)
- Template available: `.docs/templates/student-project-template.md`

## 🌍 Environment

### Technical Stack
- **Static Site Generator:** Jekyll 4.x
- **Template Location:** `.docs/templates/student-project-template.md`
- **Output Location:** `_projects/li-monti-connect.md`
- **Documents Location:** `StudentProjects/CRM track/` (NOT synced to GitHub)
- **Assets Location:** `assets/documents/li-monti-connect/` (WILL be synced)

### Repository Structure
```
/
├── StudentProjects/
│   └── CRM track/          # ⚠️ IN .GITIGNORE - read but don't reference
│       ├── Li-Monti Connect.pptx
│       ├── elevator pitch.docx
│       ├── li monti maps.docx
│       ├── pitch day update.docx
│       ├── solution lithium till shark tank.docx
│       ├── update document research.docx
│       └── vch systems overview solution draft and interviews.docx
├── _projects/
│   ├── cacao-guide.md      # ✅ Example reference
│   └── li-monti-connect.md # NEW FILE TO CREATE
└── assets/
    └── documents/
        └── li-monti-connect/  # Copy relevant files here
```

### Critical Constraints
⚠️ **MUST READ:** `.docs/CRITICAL_CONSTRAINTS.md`

**Key Rules:**
1. **NEVER guess team names** - Extract from cover pages, title slides, document metadata
2. **Copy files to assets/** - Don't reference `StudentProjects/` in website code
3. **Read ALL documents** - Don't just skim titles or first pages
4. **Verify dates** - Cross-reference across all documents for consistency
5. **100% accuracy** - Every fact must be verifiable from source materials

## 🎯 Goal

### Primary Objective
Create a comprehensive, accurate student project page for Li-Monti Connect that:
- Uses exact team member names from source documents
- Tells the complete story from problem → research → solution → impact
- Includes all relevant presentations and documentation
- Follows student-project-template.md structure
- Passes all Definition of Done criteria

### Secondary Objectives
- [ ] Copy relevant documents to `assets/documents/li-monti-connect/`
- [ ] Extract key quotes from student reflections (if available)
- [ ] Identify any visual materials (diagrams, photos) to include
- [ ] Link to related VCH projects or research

## ✅ Checklist

### Research & Preparation
- [ ] Read `.docs/CRITICAL_CONSTRAINTS.md` to understand file rules
- [ ] Review `.docs/templates/student-project-template.md` for structure
- [ ] Study `_projects/cacao-guide.md` as reference example
- [ ] Read `.docs/DEFINITION_OF_DONE.md` for quality standards

### Document Analysis - Extract Key Information

#### Step 1: Read Main Presentation (Li-Monti Connect.pptx)
- [ ] Open and review all slides
- [ ] Extract: Team member names (from title slide or credits)
- [ ] Extract: Program name and institution
- [ ] Extract: Project duration/timeline
- [ ] Extract: Problem statement
- [ ] Extract: Solution overview
- [ ] Extract: Key outcomes or deliverables
- [ ] Note: Any charts, diagrams, or visuals to use

#### Step 2: Read Elevator Pitch (elevator pitch.docx)
- [ ] Read full document
- [ ] Extract: Concise problem statement
- [ ] Extract: Target audience or beneficiaries
- [ ] Extract: Value proposition
- [ ] Cross-check: Team names match presentation

#### Step 3: Read Mapping Documentation (li monti maps.docx)
- [ ] Review mapping content
- [ ] Extract: Supply chain touchpoints identified
- [ ] Extract: Stakeholders involved
- [ ] Extract: Methodology for mapping
- [ ] Note: Any maps or diagrams to copy to assets

#### Step 4: Read Progress Update (pitch day update.docx)
- [ ] Read full update
- [ ] Extract: Timeline and milestones
- [ ] Extract: Challenges encountered
- [ ] Extract: Solutions implemented
- [ ] Extract: Feedback received

#### Step 5: Read Solution Document (solution lithium till shark tank.docx)
- [ ] Read comprehensive solution description
- [ ] Extract: Technical details of solution
- [ ] Extract: Implementation approach
- [ ] Extract: Expected impact
- [ ] Extract: Future recommendations

#### Step 6: Read Research Documentation (update document research.docx)
- [ ] Review research process
- [ ] Extract: Research questions
- [ ] Extract: Methodology
- [ ] Extract: Data sources
- [ ] Extract: Key findings

#### Step 7: Read System Overview (vch systems overview solution draft and interviews.docx)
- [ ] Review system architecture
- [ ] Extract: System components
- [ ] Extract: Interview insights
- [ ] Extract: Technical specifications
- [ ] Note: Any system diagrams to include

### Information Verification
- [ ] Cross-check team names across ALL documents
- [ ] Verify dates are consistent across documents
- [ ] Confirm program and institution details
- [ ] Ensure project timeline makes logical sense
- [ ] Flag any contradictions for user review

### Content Creation
- [ ] Copy `student-project-template.md` to `_projects/li-monti-connect.md`
- [ ] Fill in ALL required YAML front matter fields
- [ ] Write compelling "About the Project" section
- [ ] Document "The Challenge" with specific details
- [ ] Describe "Research & Methodology" with methods used
- [ ] Explain "The Solution" with technical details
- [ ] Include "Key Findings & Insights" from research
- [ ] Add "Team Reflection" section (if reflections available)
- [ ] Write "Recommendations & Next Steps"
- [ ] List all "Deliverables & Resources" with correct paths

### Asset Management
- [ ] Create directory: `assets/documents/li-monti-connect/`
- [ ] Copy Li-Monti Connect.pptx to assets (if <10MB after compression)
- [ ] Copy or export relevant diagrams/visuals to assets/images/
- [ ] Extract key slides as PDFs if full PPTX too large
- [ ] Update all file paths in project page to reference /assets/

### Quality Assurance
- [ ] All team names are exact (no guesses, no placeholders)
- [ ] All dates and timeline information verified
- [ ] All links point to /assets/, not StudentProjects/
- [ ] Jekyll builds successfully: `bundle exec jekyll build`
- [ ] No YAML syntax errors
- [ ] All required fields filled in
- [ ] Content is typo-free and grammatically correct
- [ ] Technical terminology is accurate
- [ ] No placeholder text remains

### Testing
- [ ] Build Jekyll site locally
- [ ] Navigate to project page: `/projects/li-monti-connect/`
- [ ] Test all document download links
- [ ] Verify images display correctly
- [ ] Check mobile responsiveness
- [ ] Validate no broken links

### Documentation
- [ ] Update `.docs/TASK_BREAKDOWN_STUDENT_PROJECTS.md` - mark CRM task complete
- [ ] Add project summary to task breakdown
- [ ] Note any issues or blockers encountered

## 📝 Definition of Done

### Content Accuracy
- [ ] Team member names are 100% accurate from source documents
- [ ] Program name and institution verified
- [ ] Project dates and timeline verified
- [ ] All technical details accurate
- [ ] Partner organizations named correctly
- [ ] No guessed or placeholder information

### Content Completeness
- [ ] Full project story told: Problem → Research → Solution → Impact
- [ ] Research methodology documented
- [ ] Key findings and insights included
- [ ] Student reflections included (if available)
- [ ] Recommendations for future work included
- [ ] All deliverables listed with working links

### Technical Quality
- [ ] Jekyll builds without errors
- [ ] YAML front matter syntax valid
- [ ] All links functional (internal and external)
- [ ] Images optimized (<500KB each)
- [ ] Responsive design works (320px-1920px)
- [ ] No console errors

### Integration Quality
- [ ] Project appears in projects collection
- [ ] Tags allow proper categorization
- [ ] Related content linked appropriately
- [ ] Consistent with existing project pages
- [ ] Follows student-project-template structure

### Documentation Quality
- [ ] Project page is comprehensive and professional
- [ ] Writing is clear and engaging
- [ ] Technical concepts explained accessibly
- [ ] Tone respects students' work and learning
- [ ] No typos or grammatical errors

## 🔍 Task Case Details

### Project Context (Based on File Names)

**Project Name:** Li-Monti Connect
**Domain:** CRM (Customer Relationship Management) + Lithium Supply Chain
**Key Components:**
- CRM system or platform ("Li-Monti Connect")
- Supply chain mapping ("li monti maps")
- Lithium sourcing or tracking ("solution lithium till shark tank")
- Stakeholder interviews ("vch systems overview... and interviews")

**Likely Problem:**
Lithium supply chain transparency and traceability challenges, possibly addressing:
- Battery manufacturing supply chains
- Ethical sourcing concerns
- Supply chain visibility
- CRM for managing supplier relationships

### Information Extraction Priorities

#### CRITICAL (Must Extract):
1. **Team member names** - From title slide of main presentation
2. **Academic program** - From cover pages or headers
3. **Institution** - From document footers or title pages
4. **Project dates** - From document metadata or timeline sections

#### HIGH PRIORITY (Should Extract):
1. **Problem statement** - What specific challenge did they address?
2. **Solution overview** - What did they build or propose?
3. **Research methodology** - How did they approach the problem?
4. **Key findings** - What did they discover?
5. **Deliverables** - What tangible outputs did they create?

#### MEDIUM PRIORITY (Good to Have):
1. **Partner organizations** - Who did they work with?
2. **Interview insights** - What did stakeholders say?
3. **Technical specifications** - System architecture details
4. **Impact metrics** - Quantifiable outcomes
5. **Student reflections** - Learning and growth

### Expected Challenges

**Challenge 1: Large PowerPoint File (21MB)**
- **Solution:** Extract key slides as PDF or images
- **Fallback:** Host on external service if too large for GitHub

**Challenge 2: Multiple Overlapping Documents**
- **Solution:** Read all, synthesize into cohesive narrative
- **Avoid:** Redundancy - combine similar information

**Challenge 3: Technical CRM/Supply Chain Terminology**
- **Solution:** Explain jargon, make accessible to general audience
- **Balance:** Technical accuracy + readability

**Challenge 4: Identifying Team Names**
- **Solution:** Check all documents for author fields, title slides, cover pages
- **Blocker:** If names not found in any document, STOP and ask user

### File Organization Plan

```
assets/
└── documents/
    └── li-monti-connect/
        ├── li-monti-connect-presentation.pdf    # Exported or key slides
        ├── elevator-pitch.pdf                    # Converted from DOCX
        ├── supply-chain-maps.pdf                 # Mapping documentation
        ├── solution-overview.pdf                 # Solution document
        └── research-findings.pdf                 # Research document

assets/
└── images/
    └── projects/
        └── li-monti-connect/
            ├── featured.jpg                      # Card image
            ├── system-diagram.png                # Architecture
            └── supply-chain-map.png              # Mapping visual
```

### Testing Scenarios

1. **Test 1: Information Accuracy**
   - Action: Cross-reference team names across all 7 documents
   - Expected Result: Names consistent or documented discrepancy

2. **Test 2: File Access**
   - Action: Click all document download links on project page
   - Expected Result: Files download successfully from /assets/ location

3. **Test 3: Content Completeness**
   - Action: Read project page as external visitor
   - Expected Result: Complete understanding of project without needing additional context

4. **Test 4: Mobile Responsiveness**
   - Action: View page on mobile device or narrow browser
   - Expected Result: Content readable, images scale, no horizontal scroll

## 🚧 Blockers & Dependencies

### Potential Blockers

**Blocker 1: Team Names Not Found**
- **Symptom:** No student names in any of the 7 documents
- **Action:** Document this issue, ask user for team names
- **DO NOT:** Proceed with "Student Name 1" or guesses

**Blocker 2: Documents Won't Open**
- **Symptom:** DOCX or PPTX files corrupted or incompatible
- **Action:** Try alternative tools (LibreOffice, Google Docs converter)
- **Fallback:** Ask user for alternative format

**Blocker 3: Contradictory Information**
- **Symptom:** Different dates, names, or facts across documents
- **Action:** Document all versions, ask user which is correct
- **DO NOT:** Pick one arbitrarily

### Dependencies
- Access to StudentProjects/CRM track/ folder
- Document readers (LibreOffice, Google Docs, or MS Office)
- Permission to copy files to assets/ directory
- Jekyll working for local testing

## 📚 Resources & References

- **Template:** `.docs/templates/student-project-template.md`
- **Example:** `_projects/cacao-guide.md` (excellent reference)
- **Constraints:** `.docs/CRITICAL_CONSTRAINTS.md`
- **Quality Standards:** `.docs/DEFINITION_OF_DONE.md`
- **Task Tracking:** `.docs/TASK_BREAKDOWN_STUDENT_PROJECTS.md`

## 💬 Notes & Comments

### Li-Monti Context

Based on file names, this appears to be about:
- **Li:** Lithium (battery supply chain?)
- **Monti:** Monitoring/Tracking system?
- **CRM:** Customer/Supplier Relationship Management

Possible connections to:
- Electric vehicle battery supply chains
- Ethical lithium sourcing
- Supply chain transparency initiatives
- Blockchain or technology solutions for tracking

### Document Reading Strategy

**Suggested Order:**
1. Elevator pitch (quickest overview)
2. Main presentation (comprehensive view)
3. Solution document (detailed approach)
4. Research document (methodology and findings)
5. Pitch day update (timeline and progress)
6. System overview (technical details)
7. Mapping document (supply chain analysis)

**Why This Order:**
- Start broad, then dive deep
- Build understanding progressively
- Technical details make more sense with context

### Content Focus

This project page should emphasize:
1. **Real-world problem** - Make the lithium supply chain challenge tangible
2. **Student innovation** - What did they create that's novel?
3. **Practical impact** - How could this be used by industry?
4. **Learning journey** - What skills did students develop?
5. **Technical depth** - CRM system details for those interested

## 🤖 AI Instructions

### Before Starting
1. Read CRITICAL_CONSTRAINTS.md completely
2. Review student-project-template.md structure
3. Study cacao-guide.md as reference
4. Prepare note-taking document for extracted information

### Reading Documents
1. Open each document in order suggested above
2. Extract information into structured notes
3. Note page/slide numbers for key information
4. Flag any contradictions immediately
5. Copy exact quotes for team reflections

### Critical Rules - NEVER Violate
- ❌ NEVER guess team names
- ❌ NEVER use placeholder text ("TBD", "Student Name")
- ❌ NEVER reference StudentProjects/ in links
- ❌ NEVER skip reading a document
- ❌ NEVER commit files without testing build

### Writing Guidelines
- Use students' own words when quoting
- Explain technical terms (CRM, supply chain concepts)
- Be specific: "interviewed 12 suppliers" not "talked to stakeholders"
- Show evidence: "as documented in the mapping analysis"
- Respect their work: frame challenges as learning, not failures

### If You Encounter Issues
- **Can't find team names:** STOP, document issue, ask user
- **Documents contradictory:** Document both versions, ask user
- **File too large:** Extract key content, compress, or external host
- **Unclear terminology:** Research to understand, then explain in page

### Success Looks Like
- Complete project story that makes sense to outsider
- All facts verifiable from source documents
- Professional page that students would be proud of
- Technical accuracy combined with accessibility
- Zero guesses or placeholders
