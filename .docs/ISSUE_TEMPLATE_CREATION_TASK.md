---
name: Create Markdown Templates for Content Types
about: Create standardized templates for projects, research, student projects, and events
title: '[TASK] Create Markdown Templates for VCH Content Types'
labels: 'task, documentation, templates'
assignees: ''
---

## 📋 Task Summary
Create standardized markdown templates for 4 content types: VCH Projects, Research Outputs, Student Projects, and Events. Each template should include all fields that AI would need to create high-quality content.

## 🎯 Context

### Background
The VCH website has multiple content types that need consistent structure:
1. **VCH Projects** - Projects Value Chain Hackers is building (e.g., OpenWebUI integration, tools)
2. **Research Outputs** - Research papers, studies, and academic work
3. **Student Projects** - Semester-long student internship projects (e.g., Cacao Guide, Li-Monti)
4. **Events** - Brainstorming sessions, roast days, presentations, workshops

### Why This Matters
- **Consistency:** Ensures all content has the same high-quality structure
- **AI Efficiency:** AI knows exactly what information to extract and where to put it
- **User Experience:** Visitors get consistent, complete information across all content
- **Maintenance:** Easy to add new content by filling in template fields

### Related Work
- Related to student project updates (Tasks 2-3)
- Supports photo gallery creation (Tasks 4-5)
- Foundation for future content additions
- Complements existing `_projects/` Jekyll structure

## 🌍 Environment

### Technical Stack
- **Static Site Generator:** Jekyll 4.x
- **Hosting:** GitHub Pages
- **Content Format:** Markdown with YAML front matter
- **Templating:** Liquid

### Repository Structure
```
/
├── _projects/         # Student project pages (Jekyll collection)
├── _research/         # Research outputs (to be created)
├── _events/           # Events (to be created)
├── _data/            # YAML data files
├── assets/
│   ├── documents/    # PDFs, presentations
│   └── images/       # Photos, graphics
└── .docs/
    └── templates/    # NEW: Markdown templates location
```

### Critical Constraints
⚠️ **MUST READ:** [`.docs/CRITICAL_CONSTRAINTS.md`](.docs/CRITICAL_CONSTRAINTS.md)

**Key Rules:**
1. Templates should include fields for `assets/documents/` references, NOT `StudentProjects/`
2. Must work with Jekyll front matter (YAML)
3. Should include SEO metadata fields
4. Must support mobile-responsive design requirements

## 🎯 Goal

### Primary Objective
Create 4 comprehensive markdown templates in `.docs/templates/`:
1. `vch-project-template.md` - For VCH-built projects
2. `research-template.md` - For research outputs
3. `student-project-template.md` - For student internship projects
4. `event-template.md` - For events and activities

### Secondary Objectives
- [ ] Document what each field is for and when to use it
- [ ] Include examples of good content for each field
- [ ] Specify which fields are required vs. optional
- [ ] Provide guidelines for image optimization and placement

## ✅ Checklist

### Research & Preparation
- [x] Reviewed existing project structure in `_projects/`
- [x] Analyzed `_projects/cacao-guide.md` as reference example
- [x] Reviewed `.docs/DEFINITION_OF_DONE.md` for quality criteria
- [ ] Check what fields AI needs to create complete, accurate content
- [ ] Identify common patterns across different content types

### Implementation - VCH Project Template
- [ ] Create `.docs/templates/vch-project-template.md`
- [ ] Include YAML front matter with all relevant fields
- [ ] Add sections for: Description, Technical Stack, Features, Setup Instructions
- [ ] Include fields for: GitHub repo, live URL, documentation, team
- [ ] Add guidance comments explaining each field

### Implementation - Research Template
- [ ] Create `.docs/templates/research-template.md`
- [ ] Include fields for: Title, Authors, Publication Date, Journal/Conference
- [ ] Add sections for: Abstract, Research Questions, Methodology, Key Findings
- [ ] Include fields for: PDF link, citations, related research, impact metrics
- [ ] Add guidance for linking to external publications

### Implementation - Student Project Template
- [ ] Create `.docs/templates/student-project-template.md`
- [ ] Include fields for: Team names, program, institution, duration, partners
- [ ] Add sections for: Problem, Solution, Methodology, Outcomes, Learnings
- [ ] Include fields for: Presentations (Canva, PPTX), documents, deliverables
- [ ] Add roadmap/timeline structure
- [ ] Include reflection section for team insights

### Implementation - Event Template
- [ ] Create `.docs/templates/event-template.md`
- [ ] Include fields for: Event name, date, location, attendees, organizers
- [ ] Add sections for: Event description, agenda, outcomes, highlights
- [ ] Include photo gallery structure with image optimization notes
- [ ] Add fields for: Related projects, speakers, presentations, recordings

### Documentation
- [ ] Create `.docs/HOW_TO_USE_TEMPLATES.md` with usage instructions
- [ ] Document which template to use for which content type
- [ ] Provide examples of filled-in templates
- [ ] Explain how to adapt templates for special cases

### Quality Assurance
- [ ] All templates include required SEO metadata (title, description, tags)
- [ ] Templates follow Jekyll conventions (YAML front matter format)
- [ ] Field names are clear and self-explanatory
- [ ] Examples are provided for complex fields
- [ ] Templates include comments/guidance for AI
- [ ] Consistent structure across all 4 templates

## 📝 Definition of Done

### Content Quality
- [ ] Each template has clear, descriptive field names
- [ ] All fields include inline comments explaining what to put there
- [ ] Examples are provided for fields that might be unclear
- [ ] Required fields are marked as "REQUIRED"
- [ ] Optional fields are marked as "OPTIONAL"
- [ ] Templates follow existing VCH content style and tone

### Technical Quality
- [ ] YAML front matter syntax is valid
- [ ] Field names follow Jekyll/Liquid conventions (lowercase, underscores)
- [ ] Templates can be copy-pasted and filled in directly
- [ ] No placeholder text that would break Jekyll builds
- [ ] All asset references use correct paths (`/assets/documents/`)

### Integration Quality
- [ ] Templates match existing `_projects/` structure
- [ ] Compatible with Jekyll collections system
- [ ] Support for Liquid templating features
- [ ] Fields align with existing layout files

### Documentation Quality
- [ ] Usage instructions are clear and actionable
- [ ] Examples show realistic, high-quality content
- [ ] Edge cases and special situations are documented
- [ ] Templates are organized in logical location (`.docs/templates/`)

## 🔍 Task Case Details

### Template 1: VCH Project Template

**Purpose:** For projects that Value Chain Hackers is building (tools, platforms, systems)

**Required Fields:**
- Title, description, status (Planning/In Development/Live)
- GitHub repository, live URL, documentation URL
- Technical stack (languages, frameworks, tools)
- Team members, project lead
- Start date, launch date (if applicable)

**Content Sections:**
- Overview/Description
- Features & Capabilities
- Technical Architecture
- Setup/Installation Instructions
- Usage Examples
- Roadmap/Future Plans
- Contributing Guidelines (if open source)

**Example:** OpenWebUI integration, custom supply chain tools, blockchain platforms

---

### Template 2: Research Template

**Purpose:** For academic research, studies, papers, and reports

**Required Fields:**
- Title, authors (with affiliations)
- Publication date, journal/conference name
- DOI, PDF link, external publication link
- Keywords, research areas
- Abstract (short summary)

**Content Sections:**
- Research Questions/Objectives
- Methodology
- Key Findings
- Conclusions
- Impact & Applications
- Related Research
- How to Cite

**Example:** Supply chain sustainability research, circular economy studies, AI in logistics papers

---

### Template 3: Student Project Template

**Purpose:** For semester-long student internship projects (like Cacao Guide, Li-Monti, Textile Twicely)

**Required Fields:**
- Project title, status (Completed/In Progress)
- Team member names (students)
- Program, institution (e.g., "Global Project and Change Management, Windesheim Zwolle")
- Duration (start date - end date, or "6-month internship")
- Supervising professor/mentor (if applicable)
- Industry partners/stakeholders

**Content Sections:**
- Problem Statement (What challenge were they addressing?)
- Project Goals & Objectives
- Research & Methodology
- Solution/Deliverables
- Key Outcomes & Impact
- Team Learnings & Reflections
- Future Recommendations
- Presentations & Documentation (Canva links, PDFs)

**Example:** The Green Cacao Guide, Li-Monti Connect, Textile Twicely

---

### Template 4: Event Template

**Purpose:** For VCH events (brainstorming sessions, roast days, workshops, presentations)

**Required Fields:**
- Event name, type (Workshop/Presentation/Brainstorming/Conference)
- Date, time, location (or "Virtual")
- Organizers, facilitators
- Number of attendees (or "~X participants")

**Content Sections:**
- Event Overview/Purpose
- Agenda/Schedule
- Key Topics Discussed
- Outcomes & Decisions
- Highlights & Takeaways
- Photo Gallery (with optimized images)
- Presentations & Materials
- Next Steps/Follow-up

**Example:** Autumn 2025 Brainstorming Session, Spring 2025 Roast Day, VCH Inspiration Session

---

### What AI Needs in Templates

**For Accuracy:**
- Clear field labels (no ambiguity about what goes where)
- Required vs. optional distinction
- Format specifications (date format, URL format, etc.)
- Character limits for summaries/descriptions

**For Quality:**
- Example content showing tone and style
- Guidelines for writing compelling descriptions
- SEO best practices for titles and meta descriptions
- Image optimization requirements (size, format, alt text)

**For Efficiency:**
- Consistent structure across all templates
- Reusable sections (e.g., "Team" section same across templates)
- Clear instructions for edge cases
- Notes on what to do when information is missing

**For Maintenance:**
- Version number in template
- Last updated date
- Changelog section
- Contact for questions/improvements

---

### Expected Output Files

```
.docs/
└── templates/
    ├── README.md (overview of all templates)
    ├── vch-project-template.md
    ├── research-template.md
    ├── student-project-template.md
    ├── event-template.md
    └── HOW_TO_USE_TEMPLATES.md (detailed usage guide)
```

---

### Testing Scenarios

1. **Test 1: Fill in Student Project Template**
   - Action: Use template to create a new student project page
   - Expected Result: All required information has a place, no confusion about where to put data

2. **Test 2: Validate YAML Syntax**
   - Action: Copy template front matter into Jekyll project
   - Expected Result: Jekyll builds without YAML syntax errors

3. **Test 3: AI Usability**
   - Action: Give template to AI with source materials, ask it to fill in
   - Expected Result: AI understands all fields and produces high-quality content

4. **Test 4: Missing Information**
   - Action: Try to fill template when some information is unavailable
   - Expected Result: Template guidance explains what to do (leave blank, use TBD, ask user, etc.)

---

## 🚧 Blockers & Dependencies

- None identified - can proceed immediately

---

## 📚 Resources & References

- **Existing Example:** `_projects/cacao-guide.md` - Well-structured student project
- **Jekyll Front Matter Docs:** https://jekyllrb.com/docs/front-matter/
- **YAML Syntax Guide:** https://yaml.org/spec/1.2/spec.html
- **VCH Definition of Done:** `.docs/DEFINITION_OF_DONE.md`
- **VCH Critical Constraints:** `.docs/CRITICAL_CONSTRAINTS.md`

---

## 💬 Notes & Comments

### Design Principles for Templates

1. **Completeness over Brevity** - Better to have a field and not use it than to need a field and not have it
2. **Clarity over Cleverness** - Field names should be self-explanatory
3. **Examples over Explanations** - Show, don't just tell
4. **Guidance over Assumptions** - Comment what goes in each field
5. **Flexibility with Structure** - Some fields optional, some required

### Content Type Distinctions

- **VCH Projects** = Value Chain Hackers building something (focus: technical implementation)
- **Research** = Academic output (focus: methodology and findings)
- **Student Projects** = Internship deliverables (focus: learning journey and practical outcomes)
- **Events** = Gatherings and activities (focus: who, what, when, outcomes)

---

## 🤖 AI Instructions

### What to Read First
1. `.docs/CRITICAL_CONSTRAINTS.md` - File reference rules
2. `_projects/cacao-guide.md` - Example of well-structured project
3. `.docs/DEFINITION_OF_DONE.md` - Quality standards

### What to Create

**For Each Template:**
1. YAML front matter with ALL relevant fields
2. Markdown content sections with descriptive headings
3. Inline comments explaining each field (using `# Comment` syntax)
4. Example values showing format and style
5. Mark required vs. optional fields clearly

**Template Structure:**
```markdown
---
# [REQUIRED] Project title - Keep concise, 3-8 words
title: "Example Project Title"

# [REQUIRED] Brief description - 1-2 sentences, <160 characters for SEO
description: "Example description"

# [OPTIONAL] Additional field
field_name: "example value"
---

## Section Heading

Content guidance here...
```

### Quality Standards

- **Field naming:** lowercase, underscores, descriptive (e.g., `team_members`, not `team`)
- **Comments:** Above each field, explain what it's for
- **Examples:** Show realistic data, not "Lorem ipsum"
- **Formatting:** Use proper YAML syntax (strings in quotes, lists with dashes)

### If You Get Stuck
1. Look at `_projects/cacao-guide.md` for inspiration
2. Check Jekyll documentation for field naming conventions
3. Think: "What would I want to know if I was filling this in?"
4. Ask user if uncertain about required fields

### Success Criteria
Templates are done when:
- A human can fill them in without confusion
- AI can extract information from source materials and map to fields
- Jekyll can process the front matter without errors
- The resulting pages look professional and complete
