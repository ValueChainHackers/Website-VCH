# Task Breakdown: Student Projects & Photo Galleries

## Overview
This document provides a comprehensive breakdown of all tasks for updating the VCH website with student project information and event photo galleries.

---

## ✅ COMPLETED TASKS

### Task 1: Cacao Track Research & Update
**Status:** ✅ COMPLETE
**Team:** Suzie Smit & Lonneke Oostmeijer
**Project:** The Green Cacao Guide

**What was done:**
1. ✅ Read entire 30-page PDF "The Green Cacao Guide"
2. ✅ Extracted accurate team names, program details, timeline
3. ✅ Identified all 8 Canva presentation links
4. ✅ Updated `_projects/cacao-guide.md` with comprehensive information
5. ✅ Moved PDF to `/assets/documents/cacao-guide/`
6. ✅ Created detailed project description covering:
   - Problem statement (Planet, People, Profit challenges)
   - Guide structure (3 main areas with 8 detailed solutions)
   - Research methodology
   - Key outcomes for 3 stakeholder groups
   - Team reflection and philosophy
   - Legacy and future use

**Information Sources:**
- The_Green_Cacao_Guide_-_By_Suzie_Smit_and_Lonneke_Oostmeijer_V1.pdf
- 8 Canva links (agroforestry, Tony Chocolonely analysis, Fairtrade mapping, etc.)
- Research documents folder

**Accuracy:** 100% - All information directly from source materials

---

## 🔄 IN PROGRESS TASKS

### Task 2: CRM/Li-Monti Research
**Status:** 🔄 IN PROGRESS
**Current Step:** Reading source documents

**Available Materials:**
- `Li-Monti Connect.pptx` (21.8 MB PowerPoint)
- `elevator pitch.docx`
- `li monti maps.docx`
- `pitch day update.docx`
- `solution lithium till shark tank.docx`
- `update document research.docx`
- `vch systems overview solution draft and interviews.docx`

**Next Steps:**
1. Open and read PowerPoint presentation
2. Read all Word documents to extract:
   - Team member names
   - Project focus (appears to be lithium/battery supply chain based on filenames)
   - Timeline and key milestones
   - Partner information
   - Technologies used
   - Outcomes and deliverables
3. Update `_projects/lemonti.md` with accurate information
4. Move documents to `/assets/documents/lemonti/`

**Questions to Answer:**
- What exactly is "Li-Monti Connect"?
- Is this related to lithium mining/batteries? (filename suggests "lithium till shark tank")
- Who are the team members?
- What CRM system was developed?
- What were the key outcomes?

---

## 📋 PENDING TASKS

### Task 3: Textile Track Research
**Status:** ⏸️ PENDING
**Estimated Time:** 2-3 hours

**Available Materials:**
- 5 Canva presentation links
- 1 Miro board link
- **NO document files in folder** - all content is in external links

**Challenges:**
- Team names unknown (not in folder)
- Project details in Canva/Miro only
- May need user to provide access or team information

**Next Steps:**
1. Check if Canva links are publicly accessible
2. Review Miro board for project information
3. Extract team names and project details
4. **May need to ASK USER for team member names**
5. Update `_projects/textile-twicely.md`

**Links to Review:**
- Miro board: https://miro.com/app/board/uXjVIXPwIsg=/
- 4 Canva presentations (roast day, design work)

---

### Task 4: Autumn 2025 Photo Gallery
**Status:** ⏸️ PENDING
**Estimated Time:** 2-3 hours

**Materials:**
- 18 photos in `/assets/images/Autumn 2025/Photos/Brainstorm/`
- Photos dated October 2, 2025
- Appear to be brainstorming/workshop session

**Implementation Plan:**
1. Create new page: `events-autumn-2025.html` or add to events page
2. Convert all images to WebP format (with JPG fallbacks)
3. Implement photo gallery with lightbox
4. Add event context:
   - Date: October 2, 2025
   - Event: Brainstorming Session
   - Location: TBD (may need to ask user)
   - Description: TBD (may need to ask user)
5. Ensure lazy loading for performance
6. Test mobile responsiveness

**Questions for User:**
- What was this brainstorming session about?
- Where was it held?
- Who attended? (students, partners, etc.)
- Should these be added to existing events page or separate gallery?

---

### Task 5: Spring 2025 Photo Gallery
**Status:** ⏸️ PENDING
**Estimated Time:** 2-3 hours

**Materials:**
- 14 photos in `/assets/images/Spring 2025/Photos/`
- Photos dated June 12, 2025
- Appear to be presentation/event day

**Implementation Plan:**
- Same as Task 4, but for Spring 2025 event
- Photos suggest final presentations or showcase event

**Questions for User:**
- What was this event? (final presentations, roast day, etc.)
- Where was it held?
- Who presented/attended?
- Should this be combined with Autumn gallery or separate?

---

## 📊 TASK SUMMARY

| Task | Team/Event | Status | Completion % | Blockers |
|------|-----------|--------|--------------|----------|
| Cacao Track | Suzie & Lonneke | ✅ Complete | 100% | None |
| CRM/Li-Monti | TBD | ⏸️ Pending | 0% | Need to read docs |
| Textile Track | TBD | ⏸️ Pending | 0% | Team names unknown |
| Autumn 2025 Photos | Brainstorming Event | ⏸️ Pending | 0% | Event context needed |
| Spring 2025 Photos | Presentation Event | ⏸️ Pending | 0% | Event context needed |
| LinkedIn Feed Fix | Static Implementation | ⏸️ Pending | 0% | Needs Jekyll-compatible approach |
| News Pages Verify | AI + Sustainability | ⏸️ Pending | 0% | Verify GitHub Actions working |

**Overall Progress:** 1/7 tasks complete (14%)

---

## 🎯 DEFINITION OF DONE CHECKLIST

For each task to be considered "done", it must meet:

### Content Accuracy
- [ ] All information is factually correct and verified against source documents
- [ ] Team member names are accurate (not guessed or placeholder)
- [ ] Dates and timelines match actual project duration
- [ ] No placeholder text remains

### Technical Requirements
- [ ] Jekyll builds successfully without errors
- [ ] All links are valid and functional
- [ ] Images are optimized (WebP + fallback)
- [ ] Mobile responsive design works
- [ ] No console errors

### Quality Standards
- [ ] Text is clear, professional, typo-free
- [ ] Grammar and spelling are correct
- [ ] Tone matches VCH website style
- [ ] SEO metadata is complete

### Integration
- [ ] Project appears correctly in navigation
- [ ] Project cards link to detail pages
- [ ] Related content is cross-linked

---

### Task 6: LinkedIn Feed Fix
**Status:** ⏸️ PENDING
**Priority:** HIGH
**Estimated Time:** 3-4 hours

**Current Issue:**
- LinkedIn feed on homepage is currently using placeholder/client-side approach
- Needs Jekyll-compatible STATIC implementation (no client-side JavaScript)
- Must work with GitHub Pages static site generation

**Constraints:**
- ⚠️ **CRITICAL:** This is a Jekyll static site hosted through GitHub with GitHub Actions
- Cannot use client-side JavaScript to fetch LinkedIn posts
- Solution must generate HTML at build time

**Possible Approaches:**
1. **Manual curation:** User updates a YAML data file with LinkedIn post details
2. **GitHub Actions workflow:** Fetch LinkedIn posts during build (requires LinkedIn API credentials)
3. **RSS-to-Jekyll:** If LinkedIn provides RSS, parse during build like news feeds
4. **Embed widget:** Use official LinkedIn embed (but may have client-side limitations)

**Next Steps:**
1. Check current implementation in homepage
2. Determine which approach is feasible (likely manual curation for start)
3. Create `_data/linkedin_posts.yml` structure
4. Update homepage to read from data file
5. Document how user updates the feed

**Questions for User:**
- Do you have LinkedIn API credentials?
- How often do you want to update LinkedIn feed?
- Manual updates acceptable, or need automation?

---

### Task 7: Verify News Pages Working
**Status:** ⏸️ PENDING
**Priority:** MEDIUM
**Estimated Time:** 1-2 hours

**Background:**
- AI news and Sustainability news pages were rebuilt with Jekyll-compatible architecture
- Now use GitHub Actions + Python + Jekyll data files instead of client-side JavaScript
- Workflow: `.github/workflows/update-news-feeds.yml`
- Python script: `scripts/fetch_news_feeds.py`
- Data files: `_data/ai_news.yml` and `_data/sustainability_news.yml`

**Verification Needed:**
1. Check if GitHub Actions workflow has run successfully
2. Verify data files are populated with news articles
3. Test that pages display content correctly
4. Confirm RSS feeds are being fetched properly
5. Test manual workflow trigger (if needed)

**Potential Issues:**
- Python dependencies may need to be installed in workflow
- RSS feeds may be blocked or rate-limited
- YAML formatting issues
- Liquid template syntax errors

**Next Steps:**
1. Check GitHub Actions runs: `gh run list`
2. View latest workflow logs: `gh run view --log`
3. Check if data files have content: `cat _data/ai_news.yml`
4. Visit pages to verify display
5. Manually trigger workflow if needed: `gh workflow run update-news-feeds.yml`

---

## 📝 NOTES FOR NEXT STEPS

### For Li-Monti (CRM Track):
- PowerPoint is 21.8MB - may contain detailed slides with team info
- Filenames suggest lithium/battery supply chain focus
- "Shark tank" reference suggests pitch/competition element
- Multiple iterations of docs suggest evolving scope

### For Textile Track:
- **CRITICAL:** No team names in materials - must ask user or access Canva
- Canva links may require login/permissions
- Miro board might have team member info
- Consider asking user directly for team names before proceeding

### For Photo Galleries:
- Dates are in future (Oct 2025, June 2025) - but files exist
- May be dated incorrectly or from previous semester
- **Ask user for event context before creating galleries**
- Consider creating unified "Events & Activities" page vs. separate galleries

---

## 🚀 RECOMMENDED NEXT ACTIONS

1. **Continue with Li-Monti research** - Open PowerPoint and Word docs
2. **Ask user about Textile Track team** - Cannot proceed without names
3. **Ask user about photo gallery context** - Need event descriptions
4. **Commit and push Cacao Guide updates** - Task 1 is complete and ready

---

## ⚠️ IMPORTANT REMINDERS

- **Never guess team names** - Only use confirmed information
- **Never invent project details** - Only use documented facts
- **Ask user when stuck** - Better to ask than assume
- **Test everything before marking complete** - Build, links, mobile, etc.
- **Each folder is a different team** - Don't mix information

