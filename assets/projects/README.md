# VCH Project Templates & Assets

This folder contains templates and assets for managing VCH/Windesheim projects.

## Templates Available

### 1. AI_PROJECT_CONCEPT_TEMPLATE.md
**Use this for:** Planning new AI/ML project ideas before committing resources

**Key features:**
- 3 Minute Rule pitch framework (Brant Pinvidic's 6 questions)
- Agile sprint planning with detailed milestone table
- Visual asset management checklist
- Complete worked example (coffee quality prediction)

**When to use:**
- You have an AI project idea but need to think it through
- You want to pitch a project to partners or get approval
- You need to plan timeline and resources before starting

### 2. PROJECT_TEMPLATE.md
**Use this for:** Adding completed or ongoing projects to the website

**Key features:**
- Simple format for basic project information
- Fields for links, status, descriptions
- Quick to fill out for existing projects

**When to use:**
- You have a finished project to showcase
- You're documenting an ongoing student project
- You need a quick project card on the website

## Folder Structure

Each project should have its own folder with assets:

```
assets/projects/
├── PROJECT_TEMPLATE.md                    ← Template for simple projects
├── AI_PROJECT_CONCEPT_TEMPLATE.md         ← Template for AI projects
├── README.md                              ← This file
├── re-used/                               ← Example: completed project
│   └── project-info.md
├── beyond-the-bar/                        ← Example: completed project
│   └── project-info.md
└── ai-coffee-quality/                     ← Example: concept project
    ├── README.md                          ← Asset documentation
    ├── hero-image.png                     ← Main visual (1200x600px)
    ├── thumbnail.png                      ← Card preview (400x300px)
    ├── diagrams/
    │   ├── model-architecture.png
    │   └── user-flow.png
    └── screenshots/
        ├── dashboard-v1.png
        └── mobile-mockup.png
```

## Workflow: From Concept to Website

### For AI Project Concepts

1. **Copy the template**
   ```bash
   cp AI_PROJECT_CONCEPT_TEMPLATE.md my-project-concept.md
   ```

2. **Fill out the 3 Minute Rule pitch** (6 questions)
   - What is it?
   - How does it work?
   - Are you sure it can work?
   - Can you do it?
   - What's the value?
   - What are the risks?

3. **Plan the timeline**
   - Decide sprint length (usually 2 weeks)
   - Fill out the milestone table with specific dates
   - Plan Agile ceremonies (standups, reviews, retros)

4. **Create asset folder**
   ```bash
   mkdir -p assets/projects/my-project-name
   mkdir -p assets/projects/my-project-name/diagrams
   mkdir -p assets/projects/my-project-name/screenshots
   ```

5. **Add visual assets**
   - Create or find a hero image (1200x600px)
   - Make a thumbnail (400x300px)
   - Add diagrams if you have them
   - Document in the folder's README.md

6. **Get approval**
   - Review with Christiaan
   - Confirm with partners if applicable
   - Decide: go, no-go, or revise

7. **Add to website with "Concept" badge**
   - Shows you're exploring this idea
   - Gauges interest from students/partners
   - Can update status as project progresses

### For Completed/Ongoing Projects

1. **Use the simple template**
   ```bash
   cp PROJECT_TEMPLATE.md projects/my-project.md
   ```

2. **Fill in basic info**
   - Title, category, status
   - Short description (1-2 sentences)
   - Links to GitHub, website, paper, etc.

3. **Add assets** (if you have them)
   - Create folder: `assets/projects/my-project/`
   - Add thumbnail and hero image
   - Update paths in the markdown file

4. **Provide to Claude** to add to the website

## Image Guidelines

### Required Sizes
- **Hero image:** 1200x600px (2:1 ratio) - Used on project detail pages
- **Thumbnail:** 400x300px (4:3 ratio) - Used on homepage project cards
- **Logo/Icon:** 200x200px or SVG - Optional project branding

### File Formats
- Photos: JPG (for smaller file size)
- Graphics/Diagrams: PNG (for quality)
- Logos: SVG preferred (scalable)

### Naming Convention
- `hero-image.jpg` or `hero-image.png`
- `thumbnail.jpg` or `thumbnail.png`
- `logo.svg` or `logo.png`
- `diagram-[name].png` (e.g., `diagram-architecture.png`)
- `screenshot-[name].png` (e.g., `screenshot-dashboard.png`)

### Best Practices
- Keep files under 1MB for web performance
- Use descriptive alt text for accessibility
- Compress images before adding to repo
- Update assets as project evolves (mockup → prototype → final)

## Agile Project Management

All AI projects follow Agile principles:

### Core Principles
- **Iterative development:** Build in small increments
- **Regular feedback:** Demo every sprint
- **Adapt and improve:** Use retrospectives
- **Deliver value:** Focus on working software

### Standard Sprint Cycle (2 weeks)
1. **Sprint Planning** (Monday Week 1)
   - What will we accomplish this sprint?
   - Break work into tasks

2. **Daily Standups** (Throughout sprint)
   - What did I do?
   - What will I do?
   - What's blocking me?

3. **Development** (Week 1-2)
   - Build, test, document

4. **Sprint Review** (Friday Week 2)
   - Demo working software
   - Get stakeholder feedback

5. **Sprint Retrospective** (Friday Week 2)
   - What went well?
   - What could improve?
   - What will we change?

### Milestone Tracking
- Use the detailed milestone table in the AI template
- Update status after each sprint
- Mark completed deliverables
- Adjust future sprints based on learning

## Examples

### Concept Project
See: `ai-coffee-quality/` - Full example of an AI project concept with:
- Complete 3 Minute Rule pitch
- 12-sprint timeline with specific dates
- Asset folder structure
- Agile ceremony planning

### Completed Project
See: `re-used/` and `beyond-the-bar/` - Simple project documentation

## Tips

**For Project Concepts:**
- Be honest about unknowns and risks
- Start with the problem, not the tech
- Make timeline realistic (add buffer!)
- Identify deal-breakers early

**For Asset Management:**
- Create folder structure early
- Use placeholders if needed
- Document what each asset shows
- Keep original files separate from web versions

**For Agile Planning:**
- 2-week sprints work well for student projects
- Don't skip retrospectives
- Make demos visible (screenshot or record them)
- Adapt timeline as you learn

## Questions?

Contact Christiaan or ask in the VCH Discord.
