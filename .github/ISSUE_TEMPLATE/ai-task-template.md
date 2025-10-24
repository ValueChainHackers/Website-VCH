---
name: AI Task Template
about: Comprehensive task template for AI context preservation
title: '[TASK] '
labels: 'task'
assignees: ''
---

## 📋 Task Summary
<!-- One-sentence description of what needs to be done -->


## 🎯 Context
<!-- What led to this task? What problem are we solving? -->

### Background
<!-- Provide historical context, previous attempts, or related work -->


### Why This Matters
<!-- Business value, user impact, technical debt, etc. -->


### Related Work
<!-- Links to related issues, PRs, documentation, or conversations -->
- Related Issue: #
- Related PR: #
- Documentation:


## 🌍 Environment

### Technical Stack
- **Static Site Generator:** Jekyll 4.x
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions
- **Templating:** Liquid
- **Build Command:** `bundle exec jekyll build`
- **Local Server:** `bundle exec jekyll serve`

### Repository Structure
```
/
├── _layouts/          # Page templates
├── _includes/         # Reusable components
├── _projects/         # Student project pages (front matter + markdown)
├── _data/            # YAML data files (news feeds, etc.)
├── assets/
│   ├── documents/    # PDFs, presentations (synced to GitHub)
│   ├── images/       # Photos, graphics (synced to GitHub)
│   └── css/          # Stylesheets
├── .docs/            # Documentation (synced to GitHub, excluded from build)
├── scripts/          # Python scripts for RSS feeds, etc.
├── .github/
│   └── workflows/    # GitHub Actions workflows
├── StudentProjects/  # ⚠️ IN .GITIGNORE - Cannot reference directly
├── Pitches/          # ⚠️ IN .GITIGNORE - Cannot reference directly
└── Research/         # ⚠️ IN .GITIGNORE - Cannot reference directly
```

### Critical Constraints
⚠️ **MUST READ:** [`.docs/CRITICAL_CONSTRAINTS.md`](.docs/CRITICAL_CONSTRAINTS.md)

**Key Rules:**
1. **Never reference `StudentProjects/`, `Pitches/`, or `Research/` directly** - These are in `.gitignore`
2. **Always copy files to `assets/documents/[project]/`** before linking in website
3. **Use `permalink: pretty`** - URLs have no `.html` extension
4. **Static site only** - No client-side API calls, content generated at build time
5. **Accuracy over speed** - Verify all information from source documents

### Files Involved
<!-- List specific files this task will modify or create -->
- [ ] File 1: `/path/to/file.ext`
- [ ] File 2: `/path/to/file.ext`


## 🎯 Goal
<!-- Clear, specific objective. What does success look like? -->

### Primary Objective


### Secondary Objectives
- [ ]
- [ ]


## ✅ Checklist
<!-- Step-by-step tasks to complete this work -->

### Research & Preparation
- [ ] Read all relevant source documents
- [ ] Understand existing codebase patterns
- [ ] Identify dependencies and blockers
- [ ] Check `.docs/CRITICAL_CONSTRAINTS.md` for restrictions

### Implementation
- [ ] Step 1:
- [ ] Step 2:
- [ ] Step 3:
- [ ] Step 4:

### Quality Assurance
- [ ] Jekyll builds without errors (`bundle exec jekyll build`)
- [ ] All links are functional (no 404s)
- [ ] Images are optimized (WebP with fallbacks)
- [ ] Mobile responsive (320px-1920px)
- [ ] No console errors in browser
- [ ] Content is typo-free and grammatically correct
- [ ] Follows existing VCH style and tone

### Documentation
- [ ] Update `.docs/` documentation if needed
- [ ] Add comments to complex code
- [ ] Update `README.md` if user-facing changes

### Git & Deployment
- [ ] Files copied from ignored folders to `assets/` (if applicable)
- [ ] All links point to `assets/`, not `StudentProjects/`
- [ ] Commit message follows format: "Type: Brief description"
- [ ] No sensitive information committed
- [ ] Push to GitHub
- [ ] Verify GitHub Actions pass


## 📝 Definition of Done
<!-- Acceptance criteria - ALL must be met to close this issue -->

### Content Quality
- [ ] All information is factually accurate and verified
- [ ] Team names, dates, and details are correct (no guessing)
- [ ] No placeholder text remains (unless explicitly approved)
- [ ] Text is clear, professional, and typo-free
- [ ] Tone matches VCH website style

### Technical Quality
- [ ] Jekyll builds successfully without errors
- [ ] All links work correctly (internal and external)
- [ ] Images load properly and are optimized
- [ ] Page works on desktop, tablet, and mobile
- [ ] No JavaScript errors in console
- [ ] SEO metadata is complete (title, description, tags)

### Integration Quality
- [ ] New content appears in navigation (if applicable)
- [ ] Related content is cross-linked
- [ ] Consistent with existing pages
- [ ] Accessible (alt text, keyboard navigation, etc.)

### Documentation Quality
- [ ] Changes are documented in `.docs/` (if needed)
- [ ] Git commit messages are clear and descriptive
- [ ] Task checklist is 100% complete


## 🔍 Task Case Details
<!-- Specific scenario, data, or context unique to this task -->

### Input Data/Materials
<!-- What files, data, or information will be used? -->
- Source files:
- Reference documents:
- External links:

### Expected Output
<!-- What will be created or modified? -->
- Files created:
- Files modified:
- New pages:

### Edge Cases & Considerations
<!-- Potential issues, special cases, or things to watch out for -->
-
-

### Testing Scenarios
<!-- How to verify this works -->
1. **Test 1:**
   - Action:
   - Expected Result:

2. **Test 2:**
   - Action:
   - Expected Result:


## 🚧 Blockers & Dependencies
<!-- What needs to happen before this can be completed? -->

- [ ] Blocker 1:
- [ ] Dependency 1:


## 📚 Resources & References
<!-- Helpful links, documentation, examples -->

- **Jekyll Docs:** https://jekyllrb.com/docs/
- **Liquid Syntax:** https://shopify.github.io/liquid/
- **GitHub Actions:** https://docs.github.com/en/actions
- **VCH Website:** https://valuechainhackers.xyz
- **Project Docs:** `.docs/DEFINITION_OF_DONE.md`


## 💬 Notes & Comments
<!-- Additional context, questions, or observations -->


---

## 🤖 AI Instructions
<!-- Specific guidance for AI assistant -->

### What to Read First
1. `.docs/CRITICAL_CONSTRAINTS.md` - Understand gitignore rules
2. `.docs/DEFINITION_OF_DONE.md` - Understand acceptance criteria
3. Source materials listed above in "Input Data/Materials"

### What to Avoid
- ❌ Never guess team names or project details
- ❌ Never reference `StudentProjects/`, `Pitches/`, or `Research/` folders in website code
- ❌ Never use client-side JavaScript for dynamic content (static site only)
- ❌ Never commit without testing Jekyll build
- ❌ Never leave placeholder text without user approval

### What to Always Do
- ✅ Read ALL source documents before writing
- ✅ Copy files from ignored folders to `assets/` before linking
- ✅ Test all links and images
- ✅ Verify Jekyll builds successfully
- ✅ Ask user if ANY information is unclear or missing
- ✅ Update todo list as you work

### If You Get Stuck
1. Check `.docs/` documentation for guidance
2. Read this issue template completely
3. Ask user for clarification (don't guess)
4. Document the blocker in "Blockers & Dependencies" section
