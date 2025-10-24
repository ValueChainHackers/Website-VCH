# VCH Content Templates

This directory contains standardized markdown templates for creating consistent, high-quality content across the Value Chain Hackers website.

## 📁 Available Templates

| Template | Purpose | When to Use |
|----------|---------|-------------|
| [vch-project-template.md](vch-project-template.md) | VCH Projects | Tools, platforms, systems that VCH is building |
| [student-project-template.md](student-project-template.md) | Student Projects | Semester-long internship projects by students |
| [research-template.md](research-template.md) | Research Outputs | Academic papers, studies, reports |
| [event-template.md](event-template.md) | Events | Brainstorming sessions, workshops, presentations |

## 🚀 Quick Start

### 1. Choose the Right Template

**VCH Project Template** - Use for:
- OpenWebUI integration
- Custom supply chain tools
- Internal platforms or systems
- Technology implementations
- VCH-built applications

**Student Project Template** - Use for:
- Semester-long student internships
- Capstone projects
- Student research deliverables
- Examples: Cacao Guide, Li-Monti Connect, Textile Twicely

**Research Template** - Use for:
- Published academic papers
- White papers
- Technical reports
- Research studies
- Conference presentations

**Event Template** - Use for:
- Brainstorming sessions
- Roast days (final presentations)
- Workshops and training
- Guest lectures
- Conferences and networking events

### 2. Copy the Template

```bash
# Copy template to appropriate location
cp .docs/templates/student-project-template.md _projects/my-project-name.md
```

### 3. Fill in the Content

- Work through the YAML front matter (section between `---` lines)
- Fill in required fields first
- Optional fields can be omitted or deleted if not relevant
- Follow the inline comments and examples
- Replace all placeholder text

### 4. Write the Markdown Content

- The content below the `---` is the actual page body
- Follow the section structure provided
- Uncomment sections you use (remove `<!--` and `-->`)
- Delete sections you don't need

### 5. Optimize Assets

- Copy images to `/assets/images/projects/` or `/assets/images/events/`
- Copy documents to `/assets/documents/project-name/`
- Optimize images: max 500KB, prefer WebP format
- Test all file paths

### 6. Test Locally

```bash
# Build Jekyll site
bundle exec jekyll build

# Serve locally
bundle exec jekyll serve

# Visit http://localhost:4000 to preview
```

### 7. Commit and Push

```bash
git add _projects/my-project-name.md assets/
git commit -m "Add: My Project Name page"
git push
```

## 📋 Field Reference

### Required vs. Optional Fields

Each template marks fields as:
- `[REQUIRED]` - Must be filled in (use "TBD" if temporarily unknown)
- `[OPTIONAL]` - Can be omitted entirely if not relevant

### Common Fields Across All Templates

| Field | Description | Example |
|-------|-------------|---------|
| `title` | Page title (3-10 words) | "The Green Cacao Guide" |
| `description` | Brief summary (<160 chars) | "Sustainability guide for chocolate companies" |
| `status` | Current status | "Completed" \| "In Progress" \| "Live" |
| `category` | Content type | "Student Project" \| "VCH Project" |
| `permalink` | URL path | /projects/cacao-guide/ |
| `tags` | Categories (3-6 tags) | [Sustainability, Supply Chain] |
| `featured_image` | Card image (800x600px) | /assets/images/projects/name/featured.jpg |

### Student Project Specific Fields

| Field | Description | Example |
|-------|-------------|---------|
| `team` | Student names | "Suzie Smit & Lonneke Oostmeijer" |
| `program` | Academic program | "Global Project and Change Management (Year 2)" |
| `institution` | School name | "Windesheim Zwolle" |
| `duration` | Project length | "6-month internship (2024-2025)" |
| `partners` | Industry partners | "Tony's Chocolonely, Chocolate Makers" |

### Research Specific Fields

| Field | Description | Example |
|-------|-------------|---------|
| `authors` | Paper authors | "Christiaan Verhoef, Maria Garcia" |
| `publication_date` | Publish date | "2024-09-15" |
| `publication_venue` | Journal/conference | "Journal of Supply Chain Management" |
| `doi` | Digital Object Identifier | "10.1234/jsm.2024.56789" |
| `keywords` | Research keywords | [blockchain, supply chain, transparency] |

### Event Specific Fields

| Field | Description | Example |
|-------|-------------|---------|
| `event_date` | Date held | "2025-10-02" |
| `event_type` | Type of event | "Workshop" \| "Brainstorming" \| "Roast Day" |
| `location` | Where held | "Windesheim Zwolle, Room A101" |
| `attendees` | Number | 30 or "~25 participants" |

## 🎨 Content Quality Guidelines

### Writing Style

- **Professional but accessible** - Technical accuracy without jargon overload
- **Active voice** - "Students developed..." not "A guide was developed..."
- **Present tense** - "The platform enables..." not "The platform will enable..."
- **Specific over vague** - "Reduced waste by 30%" not "improved sustainability"
- **Show, don't tell** - Use examples, data, quotes

### Structure

- **Hook readers early** - Start with the problem or impact
- **Tell a story** - Problem → Research → Solution → Impact
- **Use headings** - Break up long text with descriptive H2/H3 headings
- **Include visuals** - Photos, diagrams, charts enhance understanding
- **End with action** - What's next? How to get involved?

### Length Guidelines

| Template Type | Ideal Length | Range |
|---------------|-------------|-------|
| VCH Project | 800-1500 words | 600-2000 |
| Student Project | 1000-2000 words | 800-2500 |
| Research | 800-1200 words | 600-1500 |
| Event | 600-1000 words | 400-1200 |

### SEO Best Practices

1. **Title** - Include main keyword, keep under 60 characters
2. **Description** - Compelling summary, 150-160 characters
3. **Keywords/Tags** - Mix of broad and specific terms (3-6)
4. **Headings** - Use H2/H3 with descriptive text, not "Introduction"
5. **Alt text** - Describe images for accessibility and SEO
6. **Links** - Internal links to related content, external to sources

## 🖼️ Image Guidelines

### Sizes & Formats

| Image Type | Dimensions | Max Size | Format |
|------------|-----------|----------|--------|
| Featured image | 800x600px | 300KB | WebP (JPG fallback) |
| OG image | 1200x630px | 400KB | WebP (JPG fallback) |
| Gallery photos | 1920px max width | 500KB each | WebP (JPG fallback) |
| Diagrams | 1200px max width | 300KB | PNG or WebP |

### Optimization

```bash
# Resize and compress image using ImageMagick
convert input.jpg -resize '1920x1920>' -quality 85 output.jpg

# Convert to WebP
convert input.jpg -quality 85 output.webp
```

### File Naming

- Use descriptive names: `cacao-guide-team-photo.jpg` not `IMG_1234.jpg`
- Lowercase, hyphens only: `supply-chain-diagram.png`
- Include context: `autumn-2025-brainstorming-01.jpg`

### Alt Text

- Describe what's in the image: "Students collaborating around a whiteboard mapping supply chain touchpoints"
- Not just: "Event photo" or "Image"
- Keep under 125 characters
- Don't start with "Image of..." or "Photo of..."

## ⚠️ Critical Rules

### GitIgnore Compliance

**NEVER reference these folders in website content:**
```
StudentProjects/  # In .gitignore
Pitches/          # In .gitignore
Research/         # In .gitignore
```

**ALWAYS use these locations:**
```
/assets/documents/project-name/  ✅ Synced to GitHub
/assets/images/projects/         ✅ Synced to GitHub
/assets/images/events/           ✅ Synced to GitHub
```

See [CRITICAL_CONSTRAINTS.md](../CRITICAL_CONSTRAINTS.md) for full details.

### Accuracy Rules

1. **Never guess information** - Use "TBD" if unknown, ask user
2. **Verify all names** - Double-check team member names, spellings
3. **Check dates** - Cross-reference dates across documents
4. **Test all links** - Ensure URLs work before committing
5. **Read full sources** - Don't just skim titles or abstracts

### Student Project Rules

- Use **exact names** from source documents
- Show respect for students' work and learning journey
- Include team reflections and learnings when available
- Frame challenges as learning opportunities
- Credit all contributors appropriately

## 🔍 AI Instructions

### For AI Assistants Filling Templates:

1. **Read ALL source materials first**
   - PDFs, presentations, documents
   - Canva/Miro links if accessible
   - Related research or context

2. **Extract information systematically**
   - Team names from cover pages, title slides
   - Dates from document metadata
   - Details from content, not just summaries

3. **Organize before writing**
   - Note key points for each section
   - Identify best quotes or examples
   - Map findings to template structure

4. **Write with care**
   - Follow template guidance comments
   - Use specific examples and data
   - Maintain consistent tone and style
   - Proofread for typos and grammar

5. **Verify everything**
   - Check all file paths point to /assets/
   - Test that YAML syntax is valid
   - Ensure Jekyll will build successfully
   - Confirm all required fields filled

### When Information is Missing:

- **Names unclear:** Use "TBD" and flag for user
- **Dates uncertain:** Use "YYYY" or "Month YYYY"
- **Document unavailable:** Note in summary, ask user
- **Conflicting info:** Document conflict, ask user to clarify

### Quality Checklist:

- [ ] All required fields filled with real data (no placeholders)
- [ ] Optional fields deleted if not used
- [ ] All file paths use /assets/ not StudentProjects/
- [ ] Images optimized (<500KB each)
- [ ] YAML syntax valid (test with Jekyll build)
- [ ] Links tested and working
- [ ] Spelling and grammar checked
- [ ] Tone matches VCH style
- [ ] Content tells compelling story

## 📚 Examples

### Excellent Examples

- **[The Green Cacao Guide](_projects/cacao-guide.md)** - Comprehensive student project
  - Accurate team information
  - Detailed problem/solution structure
  - Specific outcomes and metrics
  - Professional yet accessible tone
  - Well-organized with clear sections

### What Makes a Good Page:

✅ **Accuracy** - All information verified from sources
✅ **Completeness** - Full story from start to finish
✅ **Clarity** - Easy to understand for target audience
✅ **Specificity** - Concrete examples and data points
✅ **Visual** - Images enhance the narrative
✅ **Action-oriented** - Clear outcomes and next steps

### Common Mistakes to Avoid:

❌ Guessing team names or details
❌ Leaving placeholder text ("TBD", "Coming soon")
❌ Referencing StudentProjects/ folder in links
❌ Using vague language ("very good", "successful")
❌ Missing required fields
❌ Broken links or missing images
❌ Inconsistent tone or style

## 🆘 Troubleshooting

### Jekyll Build Errors

**YAML Syntax Error**
```
Error: Invalid YAML front matter
```
- Check for unescaped special characters (:, #, ', ")
- Ensure proper indentation (2 spaces, no tabs)
- Validate at https://www.yamllint.com/

**Liquid Template Error**
```
Liquid Exception: undefined method
```
- Check {% if %} statements reference existing fields
- Ensure {% for %} loops close with {% endfor %}
- Test conditional logic with empty fields

### Image Issues

**Image Not Displaying**
- Verify file exists at exact path specified
- Check file permissions (should be readable)
- Test path is relative to site root (/assets/...)
- Confirm image file extension matches (jpg vs jpeg)

**Image Too Large**
- Compress using ImageMagick: `convert -quality 85`
- Resize: `convert -resize '1920x1920>'`
- Convert to WebP for smaller size

### Link Issues

**404 Error on Internal Links**
- Ensure permalink matches URL structure
- Check for .html extension (should not include with permalink: pretty)
- Verify file exists in _projects/, _research/, or _events/

**External Links Broken**
- Test URLs in browser before committing
- For Canva/Miro links, ensure public sharing enabled
- Check if link requires authentication

## 📞 Getting Help

- **Documentation:** [DEFINITION_OF_DONE.md](../DEFINITION_OF_DONE.md)
- **Constraints:** [CRITICAL_CONSTRAINTS.md](../CRITICAL_CONSTRAINTS.md)
- **Task Breakdown:** [TASK_BREAKDOWN_STUDENT_PROJECTS.md](../TASK_BREAKDOWN_STUDENT_PROJECTS.md)
- **Jekyll Docs:** https://jekyllrb.com/docs/
- **GitHub Issues:** Submit questions or improvements as GitHub issues

## 🔄 Template Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-24 | Initial release of all 4 templates |

## 🤝 Contributing

Found a bug in a template? Have a suggestion for improvement?

1. Test your proposed change
2. Document why the change is needed
3. Update template version number and changelog
4. Submit as GitHub issue or PR

---

**Remember:** These templates are tools to ensure quality and consistency. Adapt them as needed, but maintain the core structure and critical rules (especially regarding file paths and information accuracy).
