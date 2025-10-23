# VCH Website - Current Tasks & Issues

**Last Updated:** October 23, 2025
**Status:** Active Development

---

## 📊 Quick Status Dashboard

| Priority | Issues | Status | Est. Time |
|----------|--------|--------|-----------|
| 🔴 CRITICAL | 6 | In Progress | 12 hours |
| 🟡 HIGH | 12 | Not Started | 20 hours |
| 🟢 MEDIUM | 9 | Not Started | 15 hours |
| 🔵 LOW | 3 | Not Started | 5 hours |

**Today's Quick Wins Completed:** 5/5 ✅
**This Week's Goal:** Fix top 10 critical/high issues

---

## 🔗 Navigation Links

### Documentation Files:
- **[ALL_ISSUES_TRACKER.md](ALL_ISSUES_TRACKER.md)** - Complete 30-issue tracker with priorities
- **[WEBSITE_ANALYSIS_REPORT.md](WEBSITE_ANALYSIS_REPORT.md)** - 60+ page comprehensive analysis
- **[LIGHTHOUSE_ISSUES.md](LIGHTHOUSE_ISSUES.md)** - 14 Lighthouse performance/accessibility fixes
- **[QUICK_WINS_COMPLETED.md](QUICK_WINS_COMPLETED.md)** - Today's completed fixes
- **[COMPLETED_UPDATES.md](COMPLETED_UPDATES.md)** - Historical changelog

### Implementation Guides:
- **[PROJECT_PAGES_GUIDE.md](PROJECT_PAGES_GUIDE.md)** - How to add/update project pages
- **[DNS_SUBDOMAIN_SETUP.md](DNS_SUBDOMAIN_SETUP.md)** - DNS configuration for project subdomains
- **[IMPROVEMENTS_RECOMMENDATIONS.md](IMPROVEMENTS_RECOMMENDATIONS.md)** - Future enhancement ideas

---

## 🔴 CURRENT CRITICAL ISSUES (Do First)

### Issue #1: Largest Contentful Paint (LCP) Too Slow ⚡
**Priority:** 🔴 CRITICAL
**Current:** 5,220ms | **Target:** <2,500ms
**Impact:** Users wait 5+ seconds to see content
**Time Estimate:** 2 hours
**Reference:** [LIGHTHOUSE_ISSUES.md#issue-lh-1](LIGHTHOUSE_ISSUES.md#issue-lh-1) | [ALL_ISSUES_TRACKER.md#issue-1](ALL_ISSUES_TRACKER.md#issue-1)

**Next Actions:**
1. Run Lighthouse to identify LCP element
2. If image: convert to WebP, add preload
3. If text: inline critical CSS
4. Test LCP < 2.5s

**Definition of Done:**
- [ ] LCP < 2.5 seconds
- [ ] Lighthouse LCP score > 0.9
- [ ] Performance score +10 points

---

### Issue #4: Missing Student Project Information 📄
**Priority:** 🔴 CRITICAL
**Status:** 12 teams have "TBD" placeholders
**Impact:** Students' work invisible, no portfolio value
**Time Estimate:** 3 hours (collection) + 1 hour (implementation)
**Reference:** [ALL_ISSUES_TRACKER.md#issue-4](ALL_ISSUES_TRACKER.md#issue-4)

**Next Actions:**
1. Email all 12 teams with collection template
2. Gather: names, descriptions, photos, GitHub links
3. Update 8 project files in `_projects/`
4. Replace all "TBD" placeholders

**Files to Update:**
- `_projects/lemonti.md`
- `_projects/textile-twicely.md`
- `_projects/cacao-guide.md`
- `_projects/bakery-network.md`
- `_projects/cacao-chain.md`
- `_projects/beer-bottle.md`
- `_projects/windmill.md`
- `_projects/phone-battery.md`

**Definition of Done:**
- [ ] All 12 teams have complete info
- [ ] Zero "TBD" placeholders remain
- [ ] Each project has: team names, description, photo, outcome
- [ ] Students can share pages as portfolio

---

### Issue #5: LinkedIn Feed is Static 📱
**Priority:** 🔴 CRITICAL
**Status:** 3 hardcoded example posts (will become outdated)
**Impact:** Feed becomes stale, looks abandoned
**Time Estimate:** 15 minutes (manual) OR 4 hours (automation)
**Reference:** [ALL_ISSUES_TRACKER.md#issue-5](ALL_ISSUES_TRACKER.md#issue-5)

**Next Actions:**
1. Go to https://www.linkedin.com/company/valuechainhackers/posts/
2. Copy 3 most recent real posts
3. Update `index.html` lines 390-438
4. Set monthly reminder (1st of month)

**Current Placeholder Posts:**
- "Fall 2025 cohort is underway..."
- "Just wrapped up AI workshop..."
- "Congrats to Twicely..."

**Definition of Done:**
- [ ] Real posts from VCH LinkedIn displayed
- [ ] Links point to actual post URLs
- [ ] Calendar reminder set for monthly updates
- [ ] Process documented for future

---

### Issue #6: No Discord Integration 💬
**Priority:** 🔴 CRITICAL
**Status:** Link exists but no visible presence
**Impact:** Community invisible, missed engagement
**Time Estimate:** 1 hour
**Reference:** [ALL_ISSUES_TRACKER.md#issue-6](ALL_ISSUES_TRACKER.md#issue-6)

**Next Actions:**
1. Enable Discord Widget in server settings
2. Get Server ID
3. Add widget iframe to `index.html`
4. Add member count display

**Implementation:**
Add new section after LinkedIn feed in `index.html`:
```html
<section class="section-spacing bg-white">
    <!-- Discord widget code -->
    <iframe src="https://discord.com/widget?id=YOUR_SERVER_ID&theme=light"
            width="350" height="500"></iframe>
</section>
```

**Definition of Done:**
- [ ] Discord widget shows online members
- [ ] "Join Community" section visible
- [ ] Member stats displayed
- [ ] Works on mobile and desktop

---

## 🟡 HIGH PRIORITY ISSUES (Do This Week)

### Issue #7: Eliminate Render-Blocking Resources ⚡
**Priority:** 🟡 HIGH
**Savings:** 1,180ms
**Time Estimate:** 3 hours
**Reference:** [LIGHTHOUSE_ISSUES.md#issue-lh-1](LIGHTHOUSE_ISSUES.md#issue-lh-1)

**Problem:** Tailwind CDN and Font Awesome block initial render

**Next Actions:**
1. Self-host Tailwind with build process
2. Preload Font Awesome
3. Inline critical CSS

---

### Issue #8: Convert Images to WebP 🖼️
**Priority:** 🟡 HIGH
**Savings:** 755 KiB
**Time Estimate:** 2 hours
**Reference:** [LIGHTHOUSE_ISSUES.md#issue-lh-2](LIGHTHOUSE_ISSUES.md#issue-lh-2)

**Next Actions:**
```bash
cd assets/images
for img in *.{jpg,jpeg,png}; do
  cwebp -q 85 "$img" -o "${img%.*}.webp"
done
```

---

### Issue #9: Properly Size Images 📐
**Priority:** 🟡 HIGH
**Savings:** 824 KiB
**Time Estimate:** 2 hours
**Reference:** [LIGHTHOUSE_ISSUES.md#issue-lh-3](LIGHTHOUSE_ISSUES.md#issue-lh-3)

**Next Actions:**
1. Identify all image display sizes
2. Resize to 2x display size maximum
3. Implement responsive srcset

---

### Issue #11: Event Registration System 📅
**Priority:** 🟡 HIGH
**Status:** Using mailto: links (clunky)
**Time Estimate:** 2 hours
**Reference:** [ALL_ISSUES_TRACKER.md#issue-11](ALL_ISSUES_TRACKER.md#issue-11)

**Recommended Solution:** Discord Events + Google Forms

---

### Issue #14: Contact Form Non-Functional ✉️
**Priority:** 🟡 HIGH
**Status:** Shows alert, doesn't send email
**Time Estimate:** 1 hour
**Reference:** [ALL_ISSUES_TRACKER.md#issue-14](ALL_ISSUES_TRACKER.md#issue-14)

**Solution:** Use EmailJS (free tier: 200 emails/month)

---

### Issue #16: Discord Webhook for Deployments 🤖
**Priority:** 🟡 HIGH
**Time Estimate:** 30 minutes
**Reference:** [ALL_ISSUES_TRACKER.md#issue-16](ALL_ISSUES_TRACKER.md#issue-16)

**Next Actions:**
1. Create Discord webhook
2. Add to GitHub secrets
3. Create `.github/workflows/discord-notify.yml`

---

## ✅ COMPLETED TODAY (October 23, 2025)

### Quick Wins Completed (5 issues in 2 hours):
- ✅ **Issue #2:** Added aria-labels to mobile menu button
- ✅ **Issue #10:** Added lazy loading to 15+ images (saves 471 KiB)
- ✅ **Issue #20:** Added width/height to all images (prevents layout shift)
- ✅ **Issue #15:** Fixed 6 email addresses (.org → .xyz)
- ✅ **Issue #3:** Added vch-green-dark color for accessibility

**Reference:** [QUICK_WINS_COMPLETED.md](QUICK_WINS_COMPLETED.md)

---

## 🟢 MEDIUM PRIORITY (Next Week)

See [ALL_ISSUES_TRACKER.md](ALL_ISSUES_TRACKER.md) for complete list:
- Issue #17: Add width/height to remaining images
- Issue #18: Reduce unused CSS
- Issue #19: Fix browser console errors
- Issue #21: Configure project subdomain DNS
- Issue #22: Create missing legal pages
- Issue #23: Discord roles system
- Issue #24: Resource library on Discord

---

## 🔵 LOW PRIORITY (Future)

See [ALL_ISSUES_TRACKER.md](ALL_ISSUES_TRACKER.md) for complete list:
- Issue #25: Optimize cache lifetimes
- Issue #26: Reduce JS execution time
- Issue #27: Font display optimization
- Issue #28: Add blog/news section
- Issue #29: Create alumni network
- Issue #30: Implement analytics

---

## 📅 This Week's Schedule

### Monday-Tuesday (Oct 23-24):
- [x] Complete quick wins (Issues #2, #3, #10, #15, #20)
- [ ] Fix Issue #1: LCP (2 hours)
- [ ] Fix Issue #6: Discord widget (1 hour)
- [ ] Update Issue #5: LinkedIn feed (15 min)

### Wednesday-Thursday (Oct 25-26):
- [ ] Issue #7: Render-blocking resources (3 hours)
- [ ] Issue #8: Convert to WebP (2 hours)
- [ ] Issue #9: Resize images (2 hours)

### Friday (Oct 27):
- [ ] Issue #14: Contact form (1 hour)
- [ ] Issue #16: Discord webhook (30 min)
- [ ] Issue #4: Collect student info (start)

---

## 🎯 Definition of Done Criteria

Every issue must meet these criteria:
- [ ] Implementation complete
- [ ] Lighthouse score improved (if applicable)
- [ ] Cross-browser tested (Chrome, Firefox, Safari)
- [ ] Mobile tested
- [ ] No new console errors
- [ ] Documentation updated
- [ ] Committed with clear message

---

## 📝 Commit Message Template

```
type(scope): brief description

- Detailed change 1
- Detailed change 2
- Detailed change 3

Fixes #issue-number
Lighthouse: [score improvements]
Time: [hours spent]

🤖 Generated with Claude Code
```

---

# ARCHIVED TASKS (Historical Reference)

## All Previous GitHub Issues (Completed)

### ✅ Issue #30: Fix baseurl Configuration
**Status:** COMPLETED
- Fixed `_config.yml` baseurl from `/Website-VCH` to `""`
- Updated url to `https://valuechainhackers.xyz`

### ✅ Issue #29: Update Team Information
**Status:** COMPLETED
- Updated all team members (Michiel, Maxime, Rea, Christiaan)
- Added real photos and email addresses
- Created individual profile pages

### ✅ Issue #28: Update Partners Section
**Status:** COMPLETED
- Created SVG logos for SCF lectorate, SCF community, ZWINC
- Updated footer with new partners

### ✅ Issue #27: Partnership Section Text
**Status:** COMPLETED
- Changed "Industry" to "Business"
- Added "Reach out to us" text

### ✅ Issue #26: Update Events
**Status:** COMPLETED
- Updated to October 30, 2025 final event
- Added AI Workshop Series
- Added Business Partnership Meetup
- Implemented mailto: registration links

### ✅ Issue #25: Replace Placeholder Projects
**Status:** COMPLETED
- Replaced 6 placeholders with 8 real VCH projects
- Created subdomain URLs for all projects
- Built comprehensive project detail page system

### ✅ Issue #24: Make All Circles Yellow
**Status:** COMPLETED
- Changed all three homepage circles to yellow

### ✅ Issue #23: Update Statistics
**Status:** COMPLETED
- Updated to: 12 teams, 43 students, 9 businesses
- Changed from 4-column to 3-column grid

### ✅ Issue #22: Color Uniformity
**Status:** COMPLETED
- Verified color scheme is uniform
- Green, yellow, orange used consistently

### ✅ Issue #21: Update "Why" Section
**Status:** COMPLETED
- Replaced with new text about supply chain impact

### ✅ Font Awesome Implementation
**Status:** COMPLETED
- Added Font Awesome 6.4.0 CDN
- Replaced emoji with icons

### ✅ SEO & Social Sharing
**Status:** COMPLETED
- Added Open Graph tags
- Added Twitter Cards
- Created robots.txt
- Added JSON-LD structured data
- SEO score: 100/100

### ✅ Team Profile Pages
**Status:** COMPLETED
- Created 4 team member profile pages
- Added professional bios and expertise
- All pages SEO-optimized

### ✅ Project Detail Page System
**Status:** COMPLETED
- Created `_layouts/project.html` template
- Built 8 project pages with comprehensive sections
- Documented in `PROJECT_PAGES_GUIDE.md`

---

## Historical Task Categories (Archive)

<details>
<summary>Click to expand historical task organization</summary>

### High Priority Tasks (Historical)
1. Content Accuracy & Alignment
2. Projects & Research Content
3. Events & Calendar
4. Contact & Community
5. Technical Improvements
6. Accessibility & UX

### Medium Priority Tasks (Historical)
7. Content Strategy
8. Design & Branding
9. Analytics & Tracking
10. Integration & Automation

### Low Priority Tasks (Historical)
11. Advanced Features
12. Community Features
13. Infrastructure & DevOps
14. Documentation
15. Quality Assurance

See [IMPROVEMENTS_RECOMMENDATIONS.md](IMPROVEMENTS_RECOMMENDATIONS.md) for complete historical context.

</details>

---

## 📞 Contact & Ownership

**Primary Maintainers:**
- Christiaan Verhoef (Technical)
- Maxime Bouillon (Content & Projects)

**Team Contacts:**
- Email: info@valuechainhackers.xyz
- Discord: https://discord.gg/mkbjsQsV
- GitHub: https://github.com/ValueChainHackers

**Update Frequency:**
- Tasks: Updated after each work session
- Issues: Reviewed weekly
- Lighthouse: Tested after deployments

---

**Last Full Review:** October 23, 2025
**Next Review:** October 30, 2025
**Document Maintained By:** Claude AI + VCH Team
