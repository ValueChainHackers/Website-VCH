# Project Detail Pages - Implementation Guide

**Created:** 2025-10-22
**Purpose:** Comprehensive project showcase with dedicated pages

---

## Overview

Each VCH project now has a dedicated detail page with the following sections:

1. **Project Overview** - Main content and description
2. **Presentation** - Embedded slides or downloadable presentation
3. **Documentation** - Research papers, reports, PDFs
4. **Demo** - Live demo or video
5. **LinkedIn Posts** - Latest project updates
6. **Background Information** - Context and motivation
7. **Project Roadmap** - Timeline and milestones
8. **Links** - GitHub, website, social media

---

## File Structure

```
_projects/
├── lemonti.md
├── textile-twicely.md
├── cacao-guide.md
├── bakery-network.md
├── cacao-chain.md
├── beer-bottle.md
├── windmill.md
└── phone-battery.md

_layouts/
└── project.html
```

---

## How It Works

### 1. Project Cards (Homepage)

Each project card now has two links:
- **Website** (external link) - Links to project subdomain
- **Learn More** button - Links to dedicated project page

Example:
```html
<div class="flex items-center gap-3">
    <a href="https://lemonti.valuechainhackers.xyz">
        <i class="fas fa-external-link-alt"></i> Website
    </a>
    <a href="/projects/lemonti/">
        Learn More →
    </a>
</div>
```

### 2. Project Markdown Files

Each project has a markdown file in `_projects/` with frontmatter:

```yaml
---
layout: project
title: "CRM Lemonti"
description: "Short description"
status: "Completed"  # or "Ongoing"
category: "Student Project"  # or "Research Output" or "Partner Collaboration"
permalink: /projects/lemonti/

# Links
website: "https://lemonti.valuechainhackers.xyz"
github: "https://github.com/ValueChainHackers/lemonti"
linkedin: "#"

# Project Details
team: "Student Team Names"
duration: "September 2024 - January 2025"
partners: "Partner Company"
tags: [CRM, Supply Chain, Software]

# Media
presentation: "/assets/documents/project-placeholder.html"
demo: "https://demo.lemonti.valuechainhackers.xyz"

# Documentation
documentation:
  - title: "Project Report"
    type: "PDF Document"
    url: "/assets/documents/lemonti-report.pdf"
  - title: "Technical Docs"
    type: "PDF Document"
    url: "/assets/documents/lemonti-tech.pdf"

# Roadmap
roadmap:
  - phase: "Project Kickoff"
    date: "September 2024"
    completed: true
  - phase: "Development"
    date: "October 2024"
    completed: true
  - phase: "Testing"
    date: "November 2024"
    completed: false

# LinkedIn Posts
linkedin_posts:
  - url: "https://linkedin.com/posts/..."
    date: "January 2025"
    excerpt: "Project update..."

# Background
background: |
  Extended background information about the project,
  why it was started, and its significance.
---

## Main Content

The content here appears in the "Project Overview" section.

Write in markdown format. You can include:

### Subsections
- Bullet points
- **Bold text**
- *Italic text*
- Links
- Images

etc.
```

### 3. Project Layout Template

The `_layouts/project.html` template renders all the sections automatically based on the frontmatter data.

**Sections rendered:**
- ✅ Header with status, category, title
- ✅ Quick links to website and GitHub
- ✅ Main content area (from markdown body)
- ✅ Presentation section (if `presentation` provided)
- ✅ Documentation section (if `documentation` array provided)
- ✅ Demo section (if `demo` provided)
- ✅ LinkedIn posts (if `linkedin_posts` array provided)
- ✅ Sidebar with project info (team, duration, partners, tags)
- ✅ Project roadmap (if `roadmap` array provided)
- ✅ Background information (if `background` provided)
- ✅ Quick links section

---

## Updating Project Pages

### To Update an Existing Project

1. Open the project markdown file (e.g., `_projects/lemonti.md`)
2. Update the frontmatter fields:
   - Change `status` from "Ongoing" to "Completed"
   - Add real `github` URL
   - Add `documentation` items
   - Update `roadmap` phases
3. Update the main content (markdown body)
4. Commit and push changes

### To Add a New Project

1. Create a new file: `_projects/my-project.md`
2. Copy frontmatter template from existing project
3. Update all fields
4. Write project content in markdown
5. Add project card to `index.html`
6. Commit and push

---

## Content Guidelines

### Project Title
- Keep concise (2-4 words)
- Use proper capitalization

### Description
- 1-2 sentences max
- Focus on the value/outcome
- Avoid jargon

### Main Content
- Start with "About the Project"
- Include: Objectives, Technologies, Outcomes
- Use headings (##, ###)
- Add images if available

### Documentation
- Link to real PDFs when available
- Use placeholder until ready
- Include file type (PDF, DOCX, PPTX)

### Roadmap
- 3-5 key phases
- Include dates (month/year)
- Mark completed phases `completed: true`

### LinkedIn Posts
- Link to actual posts
- Short excerpt (1-2 sentences)
- Recent posts first

---

## Example: Complete Project Page

See `_projects/lemonti.md` for a fully featured example with:
- ✅ All frontmatter fields populated
- ✅ Roadmap with 5 phases
- ✅ Documentation links
- ✅ Team and partner information
- ✅ Tags for categorization
- ✅ Rich markdown content

---

## URLs and Routing

Each project is accessible at:
```
https://valuechainhackers.xyz/projects/[project-slug]/
```

Examples:
- `/projects/lemonti/`
- `/projects/textile-twicely/`
- `/projects/cacao-guide/`
- `/projects/bakery-network/`
- `/projects/cacao-chain/`
- `/projects/beer-bottle/`
- `/projects/windmill/`
- `/projects/phone-battery/`

---

## Integration with Jekyll

The `_config.yml` already has the `projects` collection configured:

```yaml
collections:
  projects:
    output: true
    permalink: /:collection/:name/
```

This means:
- Jekyll automatically processes files in `_projects/`
- Each file generates a page at the `permalink` specified
- The `project.html` layout is applied

---

## Next Steps

### Immediate (For Maxime & Team)

1. **Gather real project information:**
   - Team member names
   - Project descriptions
   - GitHub repository URLs
   - Documentation PDFs
   - LinkedIn post URLs

2. **Update each project file:**
   - Replace "TBD" placeholders
   - Add real content
   - Upload documentation

3. **Test project pages:**
   - Click "Learn More" on each project card
   - Verify all sections display correctly
   - Check all links work

### Future Enhancements

- [ ] Add project images/screenshots
- [ ] Embed presentation slides (Google Slides, PowerPoint)
- [ ] Add team member profiles with photos
- [ ] Include project timeline visualization
- [ ] Add related projects section
- [ ] Implement project search/filtering

---

## Troubleshooting

**Problem:** Project page shows 404
**Solution:** Check `permalink` matches link in `index.html`

**Problem:** Section doesn't appear
**Solution:** Check frontmatter field spelling and formatting

**Problem:** Documentation links broken
**Solution:** Verify file exists in `/assets/documents/`

**Problem:** Roadmap not showing
**Solution:** Ensure `roadmap` is an array with `phase`, `date`, `completed` fields

---

## Contact

Questions about project pages? Contact:
- Christiaan Verhoef (c.verhoef@windesheim.nl)
- info@valuechainhackers.org

---

**Last Updated:** 2025-10-22
