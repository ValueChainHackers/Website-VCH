# Definition of Done - VCH Website Updates

## Purpose
This document defines the acceptance criteria for all website update tasks related to student projects and photo galleries. Each task must meet ALL criteria before being marked as complete.

## General Acceptance Criteria (All Tasks)

### ✅ Content Accuracy
- [ ] All information is factually correct and verified against source documents
- [ ] Team member names are accurate (if provided)
- [ ] Dates and timelines match the actual project duration
- [ ] Partner names and organizations are correctly spelled
- [ ] No placeholder text remains (or placeholder is clearly marked as temporary)

### ✅ Technical Requirements
- [ ] Jekyll builds successfully without errors (`jekyll build` or GitHub Actions passes)
- [ ] All links are valid and functional (no 404 errors)
- [ ] Images are optimized (WebP format preferred, with fallbacks)
- [ ] Page loads correctly in Chrome, Firefox, and Safari
- [ ] Mobile responsive design works on screens 320px-1920px wide
- [ ] No console errors in browser developer tools

### ✅ Content Quality
- [ ] Text is clear, professional, and free of typos
- [ ] Grammar and spelling are correct
- [ ] Tone matches existing VCH website style (professional but accessible)
- [ ] Content follows existing formatting patterns (headings, lists, spacing)
- [ ] Images have appropriate alt text for accessibility

### ✅ SEO & Metadata
- [ ] Page title is descriptive and unique
- [ ] Meta description is present and compelling (150-160 characters)
- [ ] Relevant tags are included
- [ ] Permalink follows VCH naming convention
- [ ] Images have descriptive filenames (not IMG_1234.jpg)

### ✅ Integration
- [ ] New content appears in navigation (if applicable)
- [ ] Project cards link correctly to detail pages
- [ ] Breadcrumbs work correctly
- [ ] Related projects/content are cross-linked
- [ ] Homepage displays updated content (if applicable)

### ✅ Version Control
- [ ] Changes are committed with clear, descriptive commit messages
- [ ] Commit follows format: "Type: Brief description"
- [ ] No sensitive information is committed (API keys, passwords, etc.)
- [ ] All files are in correct directories
- [ ] `.gitignore` is respected

---

## Task-Specific Criteria

### For Photo Gallery Tasks

#### Content Requirements
- [ ] All photos from the source folder are included
- [ ] Photos are organized by date/event
- [ ] Each photo has descriptive caption (if context is known)
- [ ] Event date and location are accurate
- [ ] Gallery has an introduction explaining the event

#### Technical Requirements
- [ ] Photos are converted to WebP format (with JPG fallback)
- [ ] Thumbnails are generated (if using lightbox/gallery plugin)
- [ ] Lazy loading is implemented for performance
- [ ] Gallery works with keyboard navigation (accessibility)
- [ ] Gallery has prev/next navigation
- [ ] Photos maintain aspect ratio (no distortion)

#### File Organization
- [ ] Original photos are in `/assets/images/[Event]/` directory
- [ ] WebP versions are in same directory with `.webp` extension
- [ ] Naming convention: `event-name-YYYY-MM-DD-##.webp`
- [ ] Large images (>500KB) are resized before commit

### For Student Project Updates

#### Content Requirements
- [ ] Project title matches official project name
- [ ] Team member names are listed (if provided in materials)
- [ ] Project description is 1-2 paragraphs, clear and compelling
- [ ] Key objectives/outcomes are listed (3-5 bullet points)
- [ ] Timeline/duration is accurate
- [ ] Partner organizations are mentioned
- [ ] Project status reflects reality (Completed, In Progress, Planned)

#### Documentation Requirements
- [ ] All provided documents are referenced (PDFs, presentations, etc.)
- [ ] Documents are stored in `/assets/documents/[project-name]/`
- [ ] Document links are tested and working
- [ ] External links (Canva, Miro, etc.) are included in project metadata
- [ ] Document file sizes are reasonable (<10MB for web access)

#### Project-Specific Details
- [ ] Category is correct (Student Project, Research Output, etc.)
- [ ] Tags reflect the actual project focus areas
- [ ] Technologies used are listed (if applicable)
- [ ] Project subdomain is configured (if applicable)
- [ ] GitHub repository is linked (if public)

---

## Review Checklist for Claude/Developer

Before marking ANY task as complete, verify:

1. **Read the source materials thoroughly**
   - Open and read ALL documents in the student project folder
   - Review ALL photos for context
   - Check ALL URLs to understand what they contain
   - Take notes on key information

2. **Understand the project deeply**
   - What problem does it solve?
   - Who worked on it?
   - What were the outcomes?
   - What makes it unique?

3. **Cross-reference information**
   - Do the documents tell a consistent story?
   - Are there contradictions to resolve?
   - Are names/dates consistent across files?
   - Do external links provide additional context?

4. **Verify accuracy before writing**
   - Don't guess team names - only use confirmed information
   - Don't invent dates - use actual project timestamps
   - Don't fabricate outcomes - use documented results
   - Don't assume partners - only list confirmed collaborators

5. **Test everything**
   - Build the site locally (if possible)
   - Click every link
   - View every image
   - Test mobile responsiveness
   - Check browser console for errors

6. **Get user confirmation**
   - If ANY information is unclear or missing, ASK the user
   - Don't proceed with placeholder data without user approval
   - Clarify ambiguous information before implementing
   - Confirm interpretation of complex project details

---

## What "Done" Looks Like

### A Complete Task Means:
- ✅ The project page tells a complete, accurate story
- ✅ All visuals (images, charts) enhance understanding
- ✅ Navigation flows naturally to/from the content
- ✅ The page represents the team's work professionally
- ✅ Technical implementation meets VCH standards
- ✅ Content is error-free and polished
- ✅ The user can find and understand the project easily

### A Task is NOT Done if:
- ❌ Placeholder text remains (unless explicitly approved)
- ❌ Information is guessed or assumed
- ❌ Links are broken or lead to 404 pages
- ❌ Images don't load or are poorly optimized
- ❌ Jekyll build fails or throws warnings
- ❌ Content has typos or grammatical errors
- ❌ Mobile view is broken or unreadable
- ❌ You haven't actually tested the changes

---

## Quality Standards

### Content Depth
- **Minimum**: Project title, description, status, team, duration
- **Good**: Above + objectives, outcomes, technologies, timeline
- **Excellent**: Above + detailed background, impact metrics, team reflections, visuals

### Visual Presentation
- **Minimum**: Project thumbnail, basic layout
- **Good**: Above + multiple images, consistent styling
- **Excellent**: Above + photo galleries, diagrams, demo videos

### Documentation
- **Minimum**: Link to final presentation
- **Good**: Above + research documents, technical docs
- **Excellent**: Above + process documentation, meeting notes, reflections

---

## Notes for Implementation

1. **Each folder is a different team** - Don't mix information between folders
2. **Each project has unique challenges** - Read materials to understand context
3. **Accuracy > completeness** - Better to have less information that's 100% correct than more information that's partially guessed
4. **Source truth is in the files** - The uploaded documents are authoritative
5. **When in doubt, ask** - The user knows the projects better than the documents show

---

## Success Metrics

A task is truly done when:
- A stranger could understand the project from the page alone
- The team would be proud to share the page with their portfolio
- The information accurately represents their work
- The technical implementation is maintainable
- The content enhances VCH's credibility and professionalism

