# Value Chain Hackers Website - Task List & Improvements

**Total GitHub Issues:** 26 issues (14 open, 12 closed)
**All open issues created by:** Maxime Bouillon (MaxBouillon)

---

## PRIORITY 1: Maxime's Open Issues (MUST DO FIRST)

### Issue #30: Change website URL ⭐ PARTIALLY DONE
**Created:** 2025-10-06 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/30)

- [x] CNAME file is correct: `valuechainhackers.xyz`
- [ ] **STILL NEEDED:** Fix baseurl in `_config.yml`
  - Current: `baseurl: "/Website-VCH"`
  - Should be: `baseurl: ""`
  - This is causing asset loading issues with the custom domain
- **Files to update:** [_config.yml](/_config.yml) line 6

---

### Issue #29: Update team information ⭐
**Created:** 2025-10-03 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/29)

- [ ] Replace placeholder team members with real VCH team:
  - **Rea Vaz** - Image: `rea.jpg` ✅
  - **Michiel Steeman** - Image: `michiel.png` ✅
  - **Maxime Bouillon** - Image: `maxime.jpg` ✅
  - **Christiaan Verhoef** - Image: `christiaan.jpeg` ✅

- **Files to update:**
  - [_layouts/default.html](/_layouts/default.html) (lines 100-125)
  - [about.html](/about.html) (lines 170-226)
- **Current placeholders to remove:** Dr. Sarah Johnson, Prof. Mark van der Berg, Lisa Chen, Alex Rodriguez
- **Images available:** All team photos exist in [assets/images/](/assets/images/) in different formats
- **Note:** Hendryk Dittfeld also has an image (`hendryk Dittfeld.jpg`) if needed

---

### Issue #28: Update partners section ⭐ COMPLETED
**Created:** 2025-10-03 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/28)

- [x] Update partners to:
  - SCF lectorate ✅
  - SCF community ✅
  - ZWINC ✅
- [x] Created SVG placeholder logos for all partners
- **Files updated:**
  - [_layouts/default.html](/_layouts/default.html) (lines 88-96)
- **Logos created:**
  - `scf-lectorate-logo.svg`
  - `scf-community-logo.svg`
  - `zwinc-logo.svg`
- **Note:** SVG placeholders created with VCH branding colors. Replace with official logos if/when available.

---

### Issue #27: Partnership section improvements ⭐
**Created:** 2025-10-03 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/27)

- [ ] Change "Industry Partnerships" to "Business Partnerships"
- [ ] Add "Reach out to us" before mail address
- **Files to update:** [index.html](/index.html) (lines 336-380)

---

### Issue #26: Events & workshop section ⭐
**Created:** 2025-10-03 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/26)

- [ ] Update featured event to **October 30th** (next event)
- [ ] Add AI workshops (Christiaan's)
- [ ] Add final event (online for external)
- [ ] **Fix event registration links** - currently go nowhere (#)
  - **Options:**
    - A) Meetup.com links (recommended - easy to update later)
    - B) Google Forms
    - C) Eventbrite
    - D) Direct mailto: links to info@valuechainhackers.org
- **Files to update:** [index.html](/index.html) (lines 183-272)
- **Current issue:** Events are outdated (March 2024, April 2024)
- **EVENT DATE:** October 30, 2025

---

### NEW: Fix Icon Rendering 🔧
**Priority:** High - Visual issue affecting user experience

- [ ] Icons aren't rendering properly on the site
- **Current implementation:** Using emoji characters (💡, 👥, ⚡, 🔬, 🤝, 🌱, etc.)
- **Files affected:**
  - [index.html](/index.html) (lines 42, 48, 56, and throughout)
  - [about.html](/about.html)
- **Recommended solutions:**
  - A) **Font Awesome** (free CDN, most reliable)
    - Add to `<head>`: `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">`
    - Replace emoji with: `<i class="fas fa-lightbulb"></i>`, etc.
  - B) **Bootstrap Icons** (lightweight)
  - C) **Custom SVG icons** (best performance but more work)
  - D) **Fix emoji rendering** by ensuring UTF-8 charset and proper fonts

---

### NEW: Fix Placeholder Research Links 📄
**Priority:** High - Broken user journey

- [ ] Research project links currently lead nowhere (#)
- [ ] "View on GitHub", "Read Paper", "Download PDF" buttons are broken
- **Files to update:** [index.html](/index.html) (lines 121, 132, 143, 154, 165, 176)
- **Recommended solutions:**
  - **Option A:** Create placeholder documents in `/assets/documents/`
    - Example: `sample-research-paper.pdf`
    - Example: `project-template.docx`
    - Example: `presentation-template.pptx`
  - **Option B:** Link to GitHub repos under ValueChainHackers org
    - Real repos when available
    - Template repo for placeholders
  - **Option C:** Remove links until real content is ready
  - **Option D:** Show "Coming Soon" modal/message instead of link

---

### Issue #25: Update projects with real names ⭐ PARTIALLY DONE
**Created:** 2025-10-03 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/25)

- [x] Replace placeholder project names with real VCH project names
- [ ] **Replace generic descriptions with actual project descriptions**
  - Currently: Generic descriptions written based on project names only
  - Need: Real descriptions from project teams/documentation
- [x] **Add subdomain links for each project**
  - ✅ Updated all projects to use subdomains (e.g., beerbottle.valuechainhackers.xyz)
  - Project subdomains created:
    - lemonti.valuechainhackers.xyz
    - textile.valuechainhackers.xyz
    - cacao.valuechainhackers.xyz
    - bakery.valuechainhackers.xyz
    - cacaochain.valuechainhackers.xyz
    - beerbottle.valuechainhackers.xyz
    - windmill.valuechainhackers.xyz
    - phonebattery.valuechainhackers.xyz
- [ ] **Configure DNS for project subdomains**
  - Need to add CNAME records or A records for each subdomain
  - Point to appropriate hosting (GitHub Pages or other)
- [ ] **Add real PDF/document links when ready**
  - Currently: "Read Paper", "Download PDF", "View on GitHub" all link to org page
  - Need: Actual documents, papers, or reports
- [ ] **Categorize projects more accurately**
  - Currently: Guessed at Student Project / Research Output / Partner Collaboration
  - Need: Proper categorization confirmed by Maxime

**Current projects in system:**

**Completed projects:**
- CRM Lemonti (currently: Student Project)
- Textile Twicely (currently: Student Project)
- Cacao Guide (currently: Research Output)

**Ongoing projects:**
- Bakery Network (currently: Partner Collaboration)
- Cacao Chain Improvement (currently: Student Project)
- Beer Bottle Waste Reduction (currently: Partner Collaboration)
- Windmill Gearbox Niobium (currently: Research Output)
- Phone Battery Cobalt (currently: Research Output)

- **Files to update:** [index.html](/index.html) (lines 107-196)
- **Consider:** Moving to Jekyll collections for easier management

---

### Issue #24: Switch impact and research elements ⭐
**Created:** 2025-10-03 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/24)

- [ ] Make "Research" the first element (currently "Research" is between "Collaboration" and "Impact")
- [ ] Make all three circle elements the same color (yellow)
- **Files to update:** [index.html](/index.html) (lines 39-61)
- **Current colors:** Green and Yellow mixed

---

### Issue #23: Make statistics accurate ⭐
**Created:** 2025-10-03 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/23)

- [ ] Update statistics to accurate numbers:
  - ~~50+ Projects Completed~~ → **12 teams**
  - ~~25+ Industry Partners~~ → **43 students**
  - ~~200+ Students Involved~~ → **9 businesses**
  - ~~15+ Countries Represented~~ → **REMOVE**
- **Files to update:**
  - [index.html](/index.html) (lines 64-83)
  - [about.html](/about.html) (lines 33-52)

---

### Issue #22: Uniform colors ⭐ COMPLETED
**Created:** 2025-10-02 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/22)

- [x] Reviewed color usage across entire site
- [x] Confirmed uniform color scheme:
  - **Green (#7DB04D)**: Primary brand color, buttons, interactive elements, accents
  - **Yellow (#F1C144)**: Secondary color, status badges, highlights
  - **Orange (#F4A300)**: "Ongoing" status badges only
  - **Gray/White**: Text and backgrounds
- **Analysis:** Color scheme is already uniform and follows good design principles
- **Files reviewed:** All HTML files, consistent use of VCH color palette
- **Related to:** Issues #19 (closed), #24 (completed)

---

## Additional Tasks

### Task #1: Configure DNS for Project Subdomains 🌐
**Priority:** Medium
**Status:** Pending

All project links now use subdomains (e.g., `lemonti.valuechainhackers.xyz`). DNS configuration needed.

**Subdomains to configure:**
- lemonti.valuechainhackers.xyz
- textile.valuechainhackers.xyz
- cacao.valuechainhackers.xyz
- bakery.valuechainhackers.xyz
- cacaochain.valuechainhackers.xyz
- beerbottle.valuechainhackers.xyz
- windmill.valuechainhackers.xyz
- phonebattery.valuechainhackers.xyz

**Action required:**
- [ ] Add DNS CNAME records for each subdomain
- [ ] Point to appropriate hosting (GitHub Pages or other)
- [ ] Test all subdomain links
- [ ] Enable HTTPS for all subdomains

**Reference:** See [DNS_SUBDOMAIN_SETUP.md](/DNS_SUBDOMAIN_SETUP.md) for detailed instructions

---

### Task #2: Gather Real Project Details 📝
**Priority:** Medium
**Status:** Pending

Replace generic project descriptions with real information from project teams.

**For each project, gather:**
- [ ] Detailed project description (2-3 sentences)
- [ ] GitHub repository URL (if available)
- [ ] PDF/document links (research papers, reports, presentations)
- [ ] Correct categorization (Student/Research/Partner)
- [ ] Project team members
- [ ] Project dates/timeline
- [ ] Key outcomes/results

**Projects needing updates:**
1. CRM Lemonti
2. Textile Twicely
3. Cacao Guide
4. Bakery Network
5. Cacao Chain Improvement
6. Beer Bottle Waste Reduction
7. Windmill Gearbox Niobium
8. Phone Battery Cobalt

**Action required:**
- [ ] Contact Maxime for project details
- [ ] Interview project teams
- [ ] Collect documentation
- [ ] Update [index.html](/index.html) with real information

---

### Issue #21: New "Why" section text ⭐
**Created:** 2025-10-02 | [View Issue](https://github.com/ValueChainHackers/Website-VCH/issues/21)

- [ ] Replace current "Our Why" text with:

> "Supply chains shape and impact everything from climate change to social equity. They cause problems which are complex, fragmented, and too urgent to ignore. We believe in giving teams of enthusiasts and innovators the structure, support, and collaboration they need to design solutions that actually work: impactful, viable, and scalable answers to real-world challenges."

- **Files to update:** [index.html](/index.html) (lines 30-37)

---

## Recently Completed Issues ✅

### Issue #20: New paragraph (CLOSED 2025-10-13)
**Implemented:** "We are a community of communities bringing together industry partners, enthusiasts, and researchers, collaborating to solve real-world supply chain challenges through impactful innovative research."

### Issue #19: Make button colors uniform (CLOSED 2025-10-13)
**Implemented:** All buttons now yellow

### Issue #18: Change website header (CLOSED 2025-10-13)
**Implemented:** "Value Chain Hackers: From insight to impact"

### Issue #17: Make tab name simpler (CLOSED 2025-10-13)
**Implemented:** Changed to "Value Chain Hackers"

---

## High Priority Tasks

### 1. Content Accuracy & Alignment
- [ ] **Update team information with actual VCH members**
  - Current: Placeholder names (Dr. Sarah Johnson, Prof. Mark van der Berg, Lisa Chen, Alex Rodriguez)
  - Required: Real team members from README (Michiel Steeman, Maxime Bouillon, Rea Vaz, Christiaan Verhoef, Hendryk Dittfeld, Bart Ras, Liesbeth Rijsdijk)
  - Files to update: [_layouts/default.html](/_layouts/default.html), [about.html](/about.html)

- [ ] **Replace placeholder images**
  - Team member photos need to be real team photos
  - Location: [assets/images/team/](/assets/images/team/)
  - Current files: member-1.jpg, member-2.jpg, member-3.jpg, member-4.jpg

- [ ] **Add Theory U methodology section**
  - README mentions Theory U as core methodology but not visible on website
  - Add to [about.html](/about.html) as mentioned in README section 5.2
  - Include timeline visual showing 7 phases

- [ ] **Update partner logos**
  - Verify evofenedex logo spelling (currently "evofenedx-logo.png")
  - Ensure all partner logos are current and properly sized

### 2. Projects & Research Content

- [ ] **Implement dynamic project data structure**
  - Currently hardcoded in HTML
  - Move to Jekyll collections (already configured in _config.yml)
  - Create `_projects` directory with individual markdown files
  - Add frontmatter: title, category, status, description, link, tags

- [ ] **Connect projects to actual GitHub repositories**
  - Replace placeholder "#" links with real GitHub URLs
  - Add links to actual research outputs (PDFs, reports)
  - Ensure all links open in new tabs with `target="_blank" rel="noopener noreferrer"`

- [ ] **Add project filtering by status AND category**
  - Current: Filter works but projects are static
  - Add date-based sorting (most recent first)

### 3. Events & Calendar

- [ ] **Update events with real dates and information**
  - Current events are outdated (March 2024, April 2024)
  - Add actual upcoming VCH events
  - Consider integrating with calendar API or Google Calendar

- [ ] **Implement event registration system**
  - Current "Register" buttons go nowhere
  - Options: Google Forms, Eventbrite integration, or custom form

- [ ] **Add past events archive section**
  - Show completed events with recaps/photos
  - Add downloadable materials from workshops

### 4. Contact & Community

- [ ] **Implement functional contact form**
  - Current form shows alert() - not functional
  - Options:
    - Formspree integration (free tier available)
    - Netlify Forms (if migrating from GitHub Pages)
    - Custom backend with GitHub Actions
  - Send to info@valuechainhackers.org

- [ ] **Verify social media links**
  - Discord: https://discord.gg/uVKrPbKFF3
  - GitHub: https://github.com/ValueChainHackers
  - LinkedIn: https://www.linkedin.com/company/valuechainhackers/
  - Test all links are working

- [ ] **Create newsletter signup functionality**
  - Footer links to /newsletter but page doesn't exist
  - Options: Mailchimp, Substack, or custom solution

### 5. Technical Improvements

- [ ] **Fix baseurl configuration issue**
  - _config.yml has: `baseurl: "/Website-VCH"`
  - CNAME file points to: valuechainhackers.xyz
  - When using custom domain, baseurl should be empty ""
  - This affects asset loading and navigation

- [ ] **Remove suspicious script from default.html**
  - Line 210: Cloudflare challenge script looks suspicious
  - Verify this is intentional or remove

- [ ] **Add missing pages**
  - /privacy (Privacy Policy)
  - /terms (Terms of Service)
  - /newsletter (Newsletter signup)
  - Create these or remove footer links

- [ ] **Implement SEO improvements**
  - Add proper meta descriptions to all pages
  - Add Open Graph tags for social sharing
  - Generate sitemap.xml (plugin already configured)
  - Add robots.txt file

- [ ] **Performance optimization**
  - Currently loading Tailwind from CDN (3.x)
  - Consider using PostCSS build process for smaller bundle
  - Optimize images (compress team photos, partner logos)
  - Add lazy loading for images

### 6. Accessibility & UX

- [ ] **Improve mobile navigation**
  - Test mobile menu on various devices
  - Ensure all sections are accessible on mobile

- [ ] **Add skip navigation link**
  - For keyboard/screen reader users
  - Jump to main content

- [ ] **Improve form accessibility**
  - Add proper ARIA labels
  - Ensure error messages are accessible
  - Add required field indicators

- [ ] **Color contrast audit**
  - Verify all text meets WCAG AA standards
  - Check vch-light-gray (#666666) on white backgrounds

### 7. Content Strategy

- [ ] **Add "How to Get Involved" section**
  - Clear pathways for students
  - Clear pathways for researchers
  - Clear pathways for industry partners

- [ ] **Create case studies from completed projects**
  - Long-form content for major collaborations
  - Include methodology, results, impact

- [ ] **Add blog/news section**
  - Updates on ongoing research
  - Student project highlights
  - Industry insights

- [ ] **Implement search functionality**
  - Search across projects, events, team members
  - Consider using Lunr.js (client-side) or Algolia

## Medium Priority Tasks

### 8. Design & Branding

- [ ] **Create consistent icon system**
  - Currently using emoji (💡, 👥, ⚡)
  - Consider custom SVG icons or icon font
  - Maintain accessibility with proper alt text/aria-labels

- [ ] **Add loading states for dynamic content**
  - Project filtering animation
  - Form submission feedback

- [ ] **Create 404 error page**
  - Custom branded page
  - Helpful navigation back to main sections

### 9. Analytics & Tracking

- [ ] **Implement privacy-friendly analytics**
  - Options: Plausible, Fathom, or Google Analytics with consent
  - Track: page views, event registrations, project views
  - Align with privacy policy

- [ ] **Add conversion tracking**
  - Discord joins from website
  - Contact form submissions
  - Event registrations

### 10. Integration & Automation

- [ ] **GitHub Actions improvements**
  - Add build status badge to README
  - Add automated testing (HTML validation, link checking)
  - Add deployment notifications (Discord webhook)

- [ ] **Connect to GitHub API**
  - Automatically display latest repositories from ValueChainHackers org
  - Show contribution statistics
  - Display recent commits

- [ ] **Add RSS feed**
  - For blog/news section (when implemented)
  - jekyll-feed plugin already configured

## Low Priority / Future Enhancements

### 11. Advanced Features

- [ ] **Multi-language support**
  - README mentions English + Dutch
  - Implement i18n with Jekyll
  - Add language switcher

- [ ] **Interactive project dashboards**
  - README mentions Quarto or Supabase integration
  - Visualize project data, timelines, impact metrics

- [ ] **Student showcase pages**
  - Semester-based cohort pages
  - Individual student project portfolios

- [ ] **OpenWebUI integration**
  - README mentions this is deferred
  - AI-assisted research navigation
  - Chatbot for common questions

- [ ] **Interactive Theory U visualization**
  - SVG animation showing the process
  - Click through different phases
  - Link to projects in each phase

- [ ] **Testimonials section**
  - From students, partners, researchers
  - Video testimonials

- [ ] **Resources library**
  - Downloadable research frameworks
  - Templates for partner collaborations
  - Educational materials

### 12. Community Features

- [ ] **Discord widget**
  - Show online members count
  - Recent activity feed
  - Direct chat embed

- [ ] **GitHub activity feed**
  - Recent commits across VCH repos
  - Top contributors

- [ ] **Event calendar widget**
  - Embed Google Calendar
  - iCal subscription link

## Infrastructure & DevOps

### 13. Hosting & Domain

- [ ] **Verify DNS configuration**
  - CNAME file points to valuechainhackers.xyz
  - Ensure proper A/AAAA records configured
  - Add www subdomain redirect

- [ ] **Setup CDN**
  - GitHub Pages includes CDN but verify performance
  - Consider Cloudflare for additional optimization

- [ ] **Implement staging environment**
  - Separate branch for testing changes
  - Preview deployments before production

### 14. Documentation

- [ ] **Create contribution guidelines**
  - How to add new projects
  - How to update team information
  - Code style guide

- [ ] **Document update workflow**
  - Monthly update process (Christiaan + Maxime)
  - Content approval process
  - Image requirements

- [ ] **Create content templates**
  - Project submission template
  - Event announcement template
  - News/blog post template

## Quality Assurance

### 15. Testing

- [ ] **Cross-browser testing**
  - Chrome, Firefox, Safari, Edge
  - Mobile browsers (iOS Safari, Chrome Android)

- [ ] **Accessibility testing**
  - Screen reader testing (NVDA, JAWS, VoiceOver)
  - Keyboard navigation testing
  - Color blindness simulation

- [ ] **Performance testing**
  - Google PageSpeed Insights
  - WebPageTest
  - Lighthouse audit

- [ ] **Link checking**
  - Automated broken link detection
  - Regular quarterly checks

## Notes for Future Additions

- Keep this document updated as you complete tasks
- Add new items as they are identified
- Mark items with dates when completed
- Use issue tracker for tracking individual tasks
- Prioritize based on:
  1. Content accuracy (High Priority)
  2. Functionality (High Priority)
  3. User experience (Medium Priority)
  4. Nice-to-have features (Low Priority)

---

**Document Created:** 2025-10-22
**Last Updated:** 2025-10-22
**Maintained By:** Christiaan Verhoef & Contributors
