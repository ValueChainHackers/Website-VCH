# New Tasks Summary - User Instructions

## Date: October 24, 2025

This document captures the new tasks the user identified that need to be documented and tracked.

---

## 📸 **Photo Gallery Tasks**

### Context
User uploaded 2 folders with event photos:
- **Autumn 2025**: `/assets/images/Autumn 2025/Photos/Brainstorm/` (18 photos)
- **Spring 2025**: `/assets/images/Spring 2025/Photos/` (14 photos)

### Task Requirements
For EACH folder, create a separate gallery page with:
- Event date and location
- Event description/context
- Photo gallery with lightbox
- WebP optimization
- Mobile responsive design

**Status:** Pending - Need event context from user

---

## 📁 **Student Project Updates**

### Context
User uploaded `/StudentProjects/` folder with 3 subdirectories:
1. **Cacao track** - Team: Suzie Smit & Lonneke Oostmeijer
2. **CRM track** - Team: Unknown (needs research)
3. **Textile track** - Team: Unknown (needs research)

### Key Instruction
> "PER student project make a separate task to update the projects with that project, Take extra care that the information is accurate, and that you understand that each folder is a different team and a different project"

**Critical Understanding:**
- ✅ Each folder = Different team
- ✅ Each folder = Different project
- ✅ Information MUST be accurate (no guessing)
- ✅ Must read ALL documents before updating

**Status:**
- Cacao track: ✅ Complete (100% accurate from source PDF)
- CRM track: ⏸️ Pending (need to read 7 documents)
- Textile track: ⏸️ Pending (need team names from user)

---

## 📰 **LinkedIn Feed Fix**

### Context
User reminder: LinkedIn feed on homepage needs Jekyll-compatible static implementation

### Current State
- Currently placeholder or client-side approach
- **MUST** work with Jekyll static site hosted through GitHub with GitHub Actions
- Cannot use client-side JavaScript to fetch feeds

### Constraints
⚠️ **CRITICAL REMINDER:** "You are aware that this site is hosted through github with github actions so its a jekyll static site?"

### Possible Solutions
1. **Manual YAML data file** (simplest, most reliable)
2. **GitHub Actions workflow** (requires LinkedIn API credentials)
3. **RSS parsing during build** (if LinkedIn provides RSS)

**Status:** Pending - Need to check homepage implementation and propose solution

---

## ✅ **News Pages Verification**

### Context
User reminder: Verify that AI news and sustainability news pages work correctly

### What Was Done Previously
- Rebuilt from client-side JavaScript approach
- Now uses:
  - GitHub Actions workflow: `.github/workflows/update-news-feeds.yml`
  - Python script: `scripts/fetch_news_feeds.py`
  - Jekyll data files: `_data/ai_news.yml` and `_data/sustainability_news.yml`

### Verification Needed
1. Check GitHub Actions runs
2. Verify data files are populated
3. Test page display
4. Confirm RSS feeds working

**Status:** Pending - Need to verify workflow execution

---

## 📋 **Complete Task List (7 Tasks)**

| # | Task | Type | Status | Priority |
|---|------|------|--------|----------|
| 1 | Cacao Track Update | Student Project | ✅ Done | - |
| 2 | CRM/Li-Monti Update | Student Project | ⏸️ Pending | High |
| 3 | Textile Track Update | Student Project | ⏸️ Pending | High |
| 4 | Autumn 2025 Gallery | Photo Gallery | ⏸️ Pending | Medium |
| 5 | Spring 2025 Gallery | Photo Gallery | ⏸️ Pending | Medium |
| 6 | LinkedIn Feed Fix | Static Implementation | ⏸️ Pending | High |
| 7 | News Pages Verify | Verification | ⏸️ Pending | Medium |

**Progress:** 1/7 complete (14%)

---

## 🎯 **User Expectations**

Based on user instructions, they expect:

1. **Accuracy above all else**
   - "Take extra care that the information is accurate"
   - Only use information from source materials
   - Never guess team names or project details

2. **Understanding of separation**
   - "Each folder is a different team and a different project"
   - Don't mix information between folders
   - Treat each project independently

3. **Static site constraints remembered**
   - "This site is hosted through github with github actions so its a jekyll static site"
   - All solutions must work with static generation
   - No client-side API calls for dynamic content

4. **Proper documentation**
   - "Make sure you document those"
   - Track all tasks clearly
   - Explain what's done, what's pending, what's blocked

---

## 🚀 **Recommended Next Actions**

1. **Immediate:** Verify news pages are working with GitHub Actions
2. **Next:** Research Li-Monti project (read 7 documents)
3. **Then:** Propose LinkedIn feed solution to user
4. **Finally:** Get photo gallery context from user

---

## ❓ **Questions to Ask User**

### For Photo Galleries:
- What were these events about? (Autumn brainstorming, Spring presentations?)
- Where were they held?
- Who attended/presented?
- Should they be combined or separate galleries?

### For Textile Track:
- Who are the team members? (Cannot proceed without names)
- Any additional documents not in Canva/Miro?

### For LinkedIn Feed:
- Do you have LinkedIn API credentials?
- How often do you want to update?
- Is manual YAML file acceptable?

---

## ✅ **What Was Documented**

1. ✅ Created `DEFINITION_OF_DONE.md` - Comprehensive acceptance criteria
2. ✅ Created `TASK_BREAKDOWN_STUDENT_PROJECTS.md` - Detailed 7-task breakdown
3. ✅ Created `NEW_TASKS_SUMMARY.md` - This file
4. ✅ Updated todo list with all 7 tasks
5. ✅ Completed Cacao Track project update (100% accurate)

**All new tasks are now properly documented and tracked.**

