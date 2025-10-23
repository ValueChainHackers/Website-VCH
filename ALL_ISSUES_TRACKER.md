# VCH Website - Complete Issues Tracker

**Last Updated:** October 23, 2025
**Total Issues:** 30
**Sources:** Lighthouse Report + Manual Website Analysis

---

## Summary Dashboard

| Category | Total | Critical | High | Medium | Low | Completed |
|----------|-------|----------|------|--------|-----|-----------|
| **Performance** | 10 | 1 | 4 | 3 | 2 | 0 |
| **Accessibility** | 2 | 2 | 0 | 0 | 0 | 0 |
| **Best Practices** | 2 | 0 | 1 | 1 | 0 | 0 |
| **Content** | 8 | 3 | 3 | 2 | 0 | 0 |
| **Functionality** | 5 | 0 | 2 | 2 | 1 | 0 |
| **Integration** | 3 | 0 | 2 | 1 | 0 | 0 |
| **TOTAL** | **30** | **6** | **12** | **9** | **3** | **0** |

---

## 🔴 CRITICAL ISSUES (Must Fix Immediately)

### Performance

#### Issue #1: Largest Contentful Paint (LCP) Too Slow ⚡ CRITICAL
**Source:** Lighthouse
**Current:** 5,220ms | **Target:** < 2,500ms
**Impact:** Users wait 5+ seconds to see main content
**Estimated Fix Time:** 1-2 hours

**Problem:**
The largest contentful element takes 5.2 seconds to paint, making the site feel very slow.

**Definition of Done:**
- [ ] LCP < 2.5 seconds
- [ ] Lighthouse LCP score > 0.9
- [ ] User sees hero content within 2 seconds
- [ ] Performance score improves by 10+ points

**Solution Steps:**
1. Identify LCP element (run Lighthouse → check "Largest Contentful Paint element")
2. If it's an image:
   - Convert to WebP
   - Add proper dimensions
   - Preload it: `<link rel="preload" as="image" href="...">`
3. If it's text:
   - Inline critical CSS for that section
   - Ensure no render-blocking resources delay it

**Test:**
```bash
# Run Lighthouse
npm run lighthouse

# Check:
# - LCP value < 2500ms
# - Score >= 0.9
```

---

### Accessibility

#### Issue #2: Buttons Missing Accessible Names ♿ CRITICAL
**Source:** Lighthouse
**Priority:** 🔴 CRITICAL
**Impact:** Screen reader users can't use buttons
**Estimated Fix Time:** 30 minutes

**Problem:**
Icon-only buttons announce as just "button" to screen readers, making them unusable for blind users.

**Definition of Done:**
- [ ] All buttons have accessible text or `aria-label`
- [ ] Screen reader testing passes
- [ ] Lighthouse "button-name" audit = 100%
- [ ] Zero accessibility violations in axe DevTools

**Solution:**
```html
<!-- Find all buttons like this: -->
<button><i class="fas fa-bars"></i></button>

<!-- Fix with aria-label: -->
<button aria-label="Open mobile menu">
  <i class="fas fa-bars"></i>
</button>
```

**Test:**
```bash
# Find icon-only buttons
grep -r '<button' _layouts/ *.html | grep '<i class'

# Test with screen reader (Mac):
# Cmd + F5 (VoiceOver)
# Navigate to each button
# Verify it has a clear name
```

---

#### Issue #3: Insufficient Color Contrast ♿ CRITICAL
**Source:** Lighthouse
**Priority:** 🔴 CRITICAL
**Impact:** Users with vision impairments can't read text
**Estimated Fix Time:** 1 hour

**Problem:**
Some text doesn't meet WCAG AA contrast requirements (4.5:1 for normal text).

**Current Issues:**
- VCH Green (#7DB04D) on white = 2.59:1 ❌ (needs 4.5:1)
- VCH Yellow (#F1C144) on white = 1.73:1 ❌ (needs 4.5:1)

**Definition of Done:**
- [ ] All text meets WCAG AA (4.5:1 ratio)
- [ ] No green/yellow used for small text on white
- [ ] Lighthouse "color-contrast" audit = 100%
- [ ] Visual appearance still matches brand

**Solution:**
```bash
# Find all instances of colored text
grep -r 'text-vch-green\|text-vch-yellow' _layouts/ *.html

# Replace with:
# - text-vch-gray (#333333) for body text
# - bg-vch-green with text-white for buttons/badges
```

**Test:**
```bash
# Use contrast checker:
# https://webaim.org/resources/contrastchecker/

# Lighthouse check:
# "color-contrast" audit score = 1.0
```

---

### Content

#### Issue #4: Missing Student Project Information 📄 CRITICAL
**Source:** Website Analysis
**Priority:** 🔴 CRITICAL
**Impact:** Students' work is invisible, no portfolio value
**Estimated Fix Time:** 2-3 hours (data collection)

**Problem:**
8 project pages exist but contain "TBD" placeholders instead of real student information.

**What's Missing:**
- Real student names (currently "TBD")
- Actual project descriptions (currently AI guesses)
- Team photos
- Real GitHub repositories
- Project outcomes/results
- LinkedIn posts from teams

**Definition of Done:**
- [ ] All 12 active teams have complete project pages
- [ ] Each page has: team names, description, photo, GitHub link
- [ ] At least one real outcome/deliverable per project
- [ ] Zero "TBD" placeholders remain
- [ ] Students can share their project page as portfolio

**Collection Template:**
```
Email to send to each team:

Subject: Showcase Your Project on VCH Website!

Hi [Team Name],

Please fill out: https://forms.google.com/... (create form)

1. Project Name: ___________
2. Team Members (3-5 names): ___________
3. Short Description (2-3 sentences): ___________
4. Key Outcome/Deliverable: ___________
5. GitHub Repository (if public): ___________
6. Team Photo or Screenshot: [upload]
7. Status: ☐ Completed ☐ Ongoing
8. Semester: Fall 2025

Thank you!
```

**Test:**
```bash
# Check for TBD placeholders
grep -r "TBD" _projects/

# Should return nothing after completion
```

---

#### Issue #5: LinkedIn Feed is Static (Not Dynamic) 📱 CRITICAL
**Source:** Website Analysis
**Priority:** 🔴 CRITICAL (for credibility)
**Impact:** Feed becomes outdated, shows stale content
**Estimated Fix Time:** 15 min/month (manual) OR 4 hours (automation)

**Problem:**
The "Latest Updates" section shows 3 hardcoded posts from the initial build. These will become outdated quickly, making the site look abandoned.

**Current Posts:**
1. "Fall 2025 cohort is underway..." (static example)
2. "Just wrapped up AI workshop..." (static example)
3. "Congrats to Twicely..." (static example)

**Definition of Done:**
- [ ] LinkedIn feed updated monthly with real posts
- [ ] Posts include actual text from VCH LinkedIn page
- [ ] Links point to real LinkedIn post URLs
- [ ] Calendar reminder set for monthly updates
- [ ] Process documented for future updates

**Solution A: Manual Monthly Updates (Recommended)**
```markdown
Process:
1. Go to https://www.linkedin.com/company/valuechainhackers/posts/
2. Copy 3 most recent posts
3. Update index.html lines 390-438
4. Commit and push

Time: 15 minutes
Frequency: 1st of each month
Owner: Maxime + Christiaan (rotate)
```

**Solution B: Automation (Complex)**
- Requires RSS Bridge or LinkedIn API
- LinkedIn API is expensive ($$$)
- RSS Bridge requires self-hosting

**Test:**
```bash
# Verify links are real:
curl -I https://www.linkedin.com/feed/update/[urn]

# Should return 200 OK
```

---

#### Issue #6: No Discord Integration or Widget 💬 CRITICAL
**Source:** Website Analysis
**Priority:** 🔴 CRITICAL (for community growth)
**Impact:** Discord invisible to visitors, missed engagement
**Estimated Fix Time:** 1 hour

**Problem:**
Discord link exists but no visible presence on website. Visitors can't see community activity or member count.

**Definition of Done:**
- [ ] Discord widget visible on website showing online members
- [ ] "Join Our Community" section with member stats
- [ ] Discord invite prominently displayed
- [ ] Widget works on mobile and desktop

**Solution:**
```html
<!-- Add to index.html after LinkedIn feed section -->
<section class="section-spacing bg-white">
    <div class="max-w-7xl mx-auto px-4">
        <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-vch-gray mb-4">
                <i class="fab fa-discord text-vch-green mr-2"></i>
                Join Our Community
            </h2>
            <p class="text-lg text-vch-light-gray">
                Connect with students, researchers, and industry partners
            </p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 items-center">
            <!-- Discord Widget -->
            <div class="flex justify-center">
                <iframe
                    src="https://discord.com/widget?id=YOUR_SERVER_ID&theme=light"
                    width="350"
                    height="500"
                    allowtransparency="true"
                    frameborder="0"
                    sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts">
                </iframe>
            </div>

            <!-- Info Card -->
            <div class="bg-gradient-to-r from-vch-green to-vch-yellow rounded-xl p-8 text-white">
                <h3 class="text-2xl font-bold mb-6">Active Community 🎉</h3>
                <div class="grid grid-cols-2 gap-4 mb-8">
                    <div>
                        <div class="text-4xl font-bold mb-2">100+</div>
                        <div class="text-sm">Members</div>
                    </div>
                    <div>
                        <div class="text-4xl font-bold mb-2">12</div>
                        <div class="text-sm">Channels</div>
                    </div>
                </div>
                <a href="https://discord.gg/mkbjsQsV"
                   target="_blank"
                   class="block bg-white text-vch-green px-8 py-3 rounded-lg font-semibold text-center hover:bg-gray-100 transition-colors">
                    <i class="fab fa-discord mr-2"></i>
                    Join Discord Server
                </a>
            </div>
        </div>
    </div>
</section>
```

**Setup:**
1. Go to Discord Server Settings
2. Widget → Enable Server Widget
3. Copy Server ID
4. Replace `YOUR_SERVER_ID` in code above

**Test:**
```bash
# Load website
# Check Discord widget shows online members
# Click join link → should open Discord invite
```

---

## 🟡 HIGH PRIORITY ISSUES

### Performance

#### Issue #7: Eliminate Render-Blocking Resources ⚡ HIGH
**Source:** Lighthouse
**Savings:** 1,180ms
**Impact:** Page loads 1.2 seconds slower than needed
**Estimated Fix Time:** 2-3 hours

**Problem:**
Tailwind CSS CDN and Font Awesome CDN block initial page render.

**Definition of Done:**
- [ ] First Contentful Paint < 1.8s
- [ ] No render-blocking CSS in critical path
- [ ] Lighthouse "render-blocking-resources" audit passes
- [ ] Performance score improves 5+ points

**Solution:**
```html
<!-- Current (blocking): -->
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@3/dist/..." rel="stylesheet">

<!-- Better: Preload -->
<link rel="preload" href="https://cdn.jsdelivr.net/npm/tailwindcss@3/..." as="style">
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@3/..." rel="stylesheet" media="print" onload="this.media='all'">
```

**Best: Self-host with build process**
```bash
npm install -D tailwindcss
npx tailwindcss -i ./src/input.css -o ./assets/css/output.css --minify
```

---

#### Issue #8: Serve Images in Next-Gen Formats ⚡ HIGH
**Source:** Lighthouse
**Savings:** 755 KiB
**Impact:** Slow image loading, wasted bandwidth
**Estimated Fix Time:** 1-2 hours

**Problem:**
All images are PNG/JPEG instead of WebP (50-70% smaller).

**Definition of Done:**
- [ ] All raster images converted to WebP
- [ ] Fallback PNG/JPEG for old browsers
- [ ] Image sizes reduced by 50%+
- [ ] Lighthouse "modern-image-formats" audit passes

**Solution:**
```bash
# Convert all images
cd assets/images
for img in *.{jpg,jpeg,png}; do
  cwebp -q 85 "$img" -o "${img%.*}.webp"
done
```

```html
<!-- Use picture element for fallback -->
<picture>
  <source srcset="/assets/images/michiel.webp" type="image/webp">
  <img src="/assets/images/michiel.png" alt="Michiel Steeman">
</picture>
```

---

#### Issue #9: Properly Size Images ⚡ HIGH
**Source:** Lighthouse
**Savings:** 824 KiB
**Impact:** Loading huge images for tiny displays
**Estimated Fix Time:** 2 hours

**Problem:**
Images served at full resolution (e.g., 2000x2000px) but displayed at 128x128px.

**Definition of Done:**
- [ ] No image is more than 2x its display size
- [ ] Responsive srcset implemented
- [ ] Page weight reduced by 500+ KiB
- [ ] Lighthouse "uses-responsive-images" audit passes

**Solution:**
```bash
# Resize team photos to appropriate sizes
convert michiel.png -resize 256x256 michiel-256.png
convert michiel.png -resize 512x512 michiel-512.png
```

```html
<img srcset="/assets/images/michiel-256.webp 256w,
             /assets/images/michiel-512.webp 512w"
     sizes="(max-width: 600px) 128px, 256px"
     src="/assets/images/michiel-256.webp"
     alt="Michiel Steeman">
```

---

#### Issue #10: Defer Offscreen Images ⚡ HIGH
**Source:** Lighthouse
**Savings:** 471 KiB
**Impact:** Loading images user hasn't scrolled to
**Estimated Fix Time:** 30 minutes

**Problem:**
All images load immediately, even those below the fold.

**Definition of Done:**
- [ ] Below-fold images have `loading="lazy"`
- [ ] Above-fold images load immediately
- [ ] Initial load time reduced 200ms+
- [ ] Lighthouse "offscreen-images" audit passes

**Solution:**
```html
<!-- Hero image (above fold) -->
<img src="hero.jpg" alt="..." loading="eager">

<!-- Team photos (below fold) -->
<img src="team.jpg" alt="..." loading="lazy">

<!-- Projects section (below fold) -->
<img src="project.jpg" alt="..." loading="lazy">
```

**Quick Fix:**
```bash
# Add loading="lazy" to all images except first 2-3
sed -i 's/<img src="\(.*\)" alt="\(.*\)"/<img src="\1" alt="\2" loading="lazy"/g' index.html

# Then manually change first few images back to loading="eager"
```

---

### Content

#### Issue #11: Event Registration System Missing 📅 HIGH
**Source:** Website Analysis
**Priority:** 🟡 HIGH
**Impact:** Can't register for events, low attendance
**Estimated Fix Time:** 1-2 hours

**Problem:**
Event "Register" buttons use `mailto:` links which are clunky. No proper registration system.

**Definition of Done:**
- [ ] Professional event registration system
- [ ] Attendee list management
- [ ] Automatic confirmation emails
- [ ] Registration data tracked

**Solution Options:**

**Option A: Discord Events + Google Forms (Recommended)**
```markdown
1. Create Discord Event for each workshop/meetup
2. Create Google Form for registration
3. Link form in Discord event description
4. Update website event cards with Google Form link
```

Benefits: Free, integrated with Discord, simple

**Option B: Meetup.com**
- Professional
- Good for recurring events
- Costs $15/month

**Option C: Eventbrite**
- Free tier available
- More features
- Good for larger events

---

#### Issue #12: Missing Past Events Archive 📸 HIGH
**Source:** Website Analysis
**Priority:** 🟡 HIGH
**Impact:** No social proof, can't showcase success
**Estimated Fix Time:** 3-4 hours

**Problem:**
Only upcoming events shown. No record of past workshops, no photos, no outcomes.

**Definition of Done:**
- [ ] "Past Events" page created
- [ ] At least 5 past events documented
- [ ] Photos from each event (3-5 per event)
- [ ] Attendance numbers shown
- [ ] Key takeaways/outcomes listed
- [ ] Downloadable materials linked

**Structure:**
```markdown
Create: _events/past.html

For each past event:
- Event name and date
- Number of attendees
- 3-5 photos
- Brief summary
- Key outcomes
- Downloadable materials (slides, recordings)

Example:
### AI Workshop Series (September 2025)
- 25 attendees
- 3 sessions on AI for supply chains
- 🎥 [Watch Recording](...)
- 📊 [Download Slides](...)
```

---

#### Issue #13: No Student Testimonials 💬 HIGH
**Source:** Website Analysis
**Priority:** 🟡 HIGH
**Impact:** Missing powerful social proof
**Estimated Fix Time:** 2 hours (collection) + 1 hour (implementation)

**Problem:**
No student voices on the website. Potential students can't hear from current students about their experience.

**Definition of Done:**
- [ ] At least 6 student testimonials collected
- [ ] Testimonials section on homepage
- [ ] Student photos and names included
- [ ] Mix of current students and alumni
- [ ] Video testimonials (bonus)

**Collection:**
```markdown
Email to students:

Subject: Share Your VCH Experience!

Hi [Name],

We'd love to feature your experience on our website!

1. In 2-3 sentences, what was the best part of VCH for you?
2. What did you learn?
3. Would you recommend VCH to other students? Why?
4. Can we use your name and photo?

Send your response + headshot to: info@valuechainhackers.xyz

Thanks!
```

**Implementation:**
```html
<section class="section-spacing bg-vch-bg">
    <div class="max-w-7xl mx-auto px-4">
        <h2 class="text-3xl font-bold text-center mb-12">
            What Students Say
        </h2>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white rounded-xl p-6 shadow-sm">
                <p class="text-vch-light-gray mb-4">
                    "VCH gave me hands-on experience with real companies.
                    I learned more in one semester than in my entire degree."
                </p>
                <div class="flex items-center gap-3">
                    <img src="student.jpg" class="w-12 h-12 rounded-full">
                    <div>
                        <div class="font-semibold">Sarah Chen</div>
                        <div class="text-sm text-vch-light-gray">
                            Fall 2024 • Textile Twicely
                        </div>
                    </div>
                </div>
            </div>
            <!-- Repeat for 5 more testimonials -->
        </div>
    </div>
</section>
```

---

### Functionality

#### Issue #14: Contact Form Non-Functional ✉️ HIGH
**Source:** Website Analysis
**Priority:** 🟡 HIGH
**Impact:** Visitors can't actually contact VCH
**Estimated Fix Time:** 1 hour

**Problem:**
Contact form just shows JavaScript alert, doesn't send email.

**Current Code:**
```javascript
// index.html line 568-586
alert('Thank you for your message! We\'ll get back to you soon.');
```

**Definition of Done:**
- [ ] Form submissions sent to info@valuechainhackers.xyz
- [ ] User receives confirmation
- [ ] Spam protection implemented
- [ ] Form data validated
- [ ] Works on mobile and desktop

**Solution: Use EmailJS (Free tier: 200 emails/month)**

1. Sign up at https://www.emailjs.com/
2. Create email service
3. Create email template
4. Get public key

```html
<!-- Add before </body> -->
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script>
emailjs.init('YOUR_PUBLIC_KEY');

document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();

    emailjs.sendForm('service_id', 'template_id', this)
        .then(function() {
            alert('Message sent successfully!');
            document.getElementById('contact-form').reset();
        }, function(error) {
            alert('Failed to send message. Please email us directly.');
        });
});
</script>
```

**Test:**
```bash
# Fill out form
# Check email received at info@valuechainhackers.xyz
# Check user sees confirmation
```

---

#### Issue #15: Email Address Inconsistency 📧 HIGH
**Source:** Website Analysis
**Priority:** 🟡 HIGH
**Impact:** Emails sent to wrong address
**Estimated Fix Time:** 10 minutes

**Problem:**
Config has `info@valuechainhackers.xyz` but some places still show `info@valuechainhackers.org`.

**Definition of Done:**
- [ ] All email addresses use `.xyz` domain
- [ ] Zero instances of `.org` remain
- [ ] Links tested and working

**Solution:**
```bash
# Find all instances of .org email
grep -r "valuechainhackers.org" . --exclude-dir=.git

# Replace all
find . -type f -name "*.html" -o -name "*.md" -exec sed -i 's/valuechainhackers\.org/valuechainhackers.xyz/g' {} +
```

**Affected Files:**
- index.html line 525 (Business Partnerships section)
- Possibly _team/*.md files
- Possibly project files

---

### Integration

#### Issue #16: Discord Webhook for Deployments 🤖 HIGH
**Source:** Website Analysis
**Priority:** 🟡 HIGH
**Impact:** Community doesn't know when website updates
**Estimated Fix Time:** 30 minutes

**Problem:**
No automatic notifications when website is deployed. Discord members miss updates.

**Definition of Done:**
- [ ] GitHub Action created for Discord notifications
- [ ] Message posts to Discord on every deployment
- [ ] Message includes commit message and deploy URL
- [ ] Webhook secured (not exposed in public repo)

**Solution:**
```yaml
# Create: .github/workflows/discord-notify.yml
name: Discord Deployment Notification

on:
  push:
    branches: [main]
  workflow_run:
    workflows: ["Jekyll site CI"]
    types: [completed]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Discord Webhook
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
        run: |
          curl -H "Content-Type: application/json" \
          -X POST \
          -d "{\"content\":\"🚀 **Website Updated!**\n\nCheck out the latest changes at https://valuechainhackers.xyz\n\nCommit: ${{ github.event.head_commit.message }}\",\"username\":\"VCH Bot\",\"avatar_url\":\"https://valuechainhackers.xyz/assets/images/vch-logo.png\"}" \
          $DISCORD_WEBHOOK
```

**Setup:**
1. Discord Server Settings → Integrations → Webhooks
2. Create webhook for #announcements channel
3. Copy webhook URL
4. GitHub repo → Settings → Secrets → New secret
5. Name: `DISCORD_WEBHOOK`, Value: (paste URL)
6. Commit workflow file

---

## 🟢 MEDIUM PRIORITY ISSUES

### Performance

#### Issue #17: Add Width/Height to Images 📐 MEDIUM
**Source:** Lighthouse
**Score:** 0.5/100
**Impact:** Layout shifts (CLS)
**Estimated Fix Time:** 1 hour

**Problem:**
Images don't have explicit dimensions, causing page to jump when they load.

**Definition of Done:**
- [ ] All `<img>` tags have width and height
- [ ] CLS score < 0.1
- [ ] No visible layout jumps
- [ ] Lighthouse "unsized-images" audit = 100%

**Solution:**
```html
<!-- Bad -->
<img src="photo.jpg" alt="...">

<!-- Good -->
<img src="photo.jpg" alt="..." width="800" height="600" style="max-width: 100%; height: auto;">
```

---

#### Issue #18: Reduce Unused CSS 🎨 MEDIUM
**Source:** Lighthouse
**Savings:** 18 KiB
**Impact:** Minor performance gain
**Estimated Fix Time:** 3-4 hours

**Problem:**
Loading full Tailwind CSS with unused classes.

**Definition of Done:**
- [ ] CSS file size < 50 KiB
- [ ] 90%+ unused CSS removed
- [ ] No visual regressions
- [ ] Lighthouse "unused-css-rules" audit passes

**Solution:**
```bash
# Install Tailwind CLI
npm install -D tailwindcss

# Create tailwind.config.js
npx tailwindcss init

# Configure content paths
# Build optimized CSS
npx tailwindcss -i ./src/input.css -o ./assets/css/output.css --minify
```

---

#### Issue #19: Browser Console Errors 🐛 MEDIUM
**Source:** Lighthouse
**Priority:** 🟢 MEDIUM
**Impact:** May indicate bugs
**Estimated Fix Time:** 1-2 hours

**Problem:**
JavaScript errors in browser console.

**Definition of Done:**
- [ ] Zero console errors
- [ ] Zero 404 errors
- [ ] All scripts load successfully
- [ ] Lighthouse "errors-in-console" audit passes

**Test:**
```bash
# Open https://valuechainhackers.xyz
# F12 → Console
# Refresh page
# Document all errors
# Fix each one
```

---

#### Issue #20: Image Aspect Ratios Incorrect 🖼️ MEDIUM
**Source:** Lighthouse
**Priority:** 🟢 MEDIUM
**Impact:** Visual quality
**Estimated Fix Time:** 30 minutes

**Problem:**
Some images stretched/squished due to incorrect display dimensions.

**Definition of Done:**
- [ ] All images maintain natural aspect ratio
- [ ] No distorted images
- [ ] `object-fit` used where needed
- [ ] Lighthouse "image-aspect-ratio" audit passes

**Solution:**
```html
<img src="photo.jpg" class="w-32 h-32 rounded-full object-cover">
```

---

### Content

#### Issue #21: Project Subdomain DNS Not Configured 🌐 MEDIUM
**Source:** Website Analysis
**Priority:** 🟢 MEDIUM
**Impact:** Project subdomain links broken
**Estimated Fix Time:** 2 hours (waiting for DNS propagation)

**Problem:**
Project cards link to subdomains (lemonti.valuechainhackers.xyz) but DNS not configured.

**Subdomains Needed:**
- lemonti.valuechainhackers.xyz
- textile.valuechainhackers.xyz
- cacao.valuechainhackers.xyz
- bakery.valuechainhackers.xyz
- cacaochain.valuechainhackers.xyz
- beerbottle.valuechainhackers.xyz
- windmill.valuechainhackers.xyz
- phonebattery.valuechainhackers.xyz

**Definition of Done:**
- [ ] All 8 subdomains resolve correctly
- [ ] HTTPS enabled for all subdomains
- [ ] Subdomains point to project documentation or placeholder
- [ ] No broken links on website

**Solution:**
See [DNS_SUBDOMAIN_SETUP.md](DNS_SUBDOMAIN_SETUP.md) for detailed guide.

**Quick Steps:**
1. Go to domain registrar DNS settings
2. Add CNAME records for each subdomain
3. Point to GitHub Pages or project hosting
4. Wait for DNS propagation (24-48 hours)

---

#### Issue #22: Missing Legal Pages 📄 MEDIUM
**Source:** Website Analysis
**Priority:** 🟢 MEDIUM
**Impact:** Footer links broken
**Estimated Fix Time:** 2 hours

**Problem:**
Footer links to `/privacy`, `/terms`, `/newsletter` but pages don't exist.

**Definition of Done:**
- [ ] Privacy Policy page created
- [ ] Terms of Service page created
- [ ] Newsletter signup page created
- [ ] All footer links work
- [ ] Pages are GDPR compliant

**Solution:**
```bash
# Create pages
touch privacy.html terms.html newsletter.html

# Use templates:
# - Privacy: https://www.termsfeed.com/privacy-policy/generator/
# - Terms: https://www.termsfeed.com/terms-service/generator/
```

---

### Functionality

#### Issue #23: Discord Roles System Missing 👥 MEDIUM
**Source:** Website Analysis
**Priority:** 🟢 MEDIUM
**Impact:** Poor community organization
**Estimated Fix Time:** 1 hour

**Problem:**
Discord has no role system for organizing students, researchers, industry partners.

**Definition of Done:**
- [ ] Roles created: Student, Researcher, Industry, Alumni, Active Team
- [ ] Role colors match VCH brand (green/yellow)
- [ ] Role assignment channel with bot
- [ ] Announcement sent to community

**Solution:**
1. Discord Server Settings → Roles
2. Create roles with colors:
   - 🎓 Student (green #7DB04D)
   - 🔬 Researcher (yellow #F1C144)
   - 🏢 Industry Partner (green-dark)
   - 👨‍💻 Alumni (gray)
   - 🎯 Active Project Team (orange)
3. Install MEE6 bot for auto role assignment
4. Create #role-assignment channel

---

#### Issue #24: No Resource Library on Discord 📚 MEDIUM
**Source:** Website Analysis
**Priority:** 🟢 MEDIUM
**Impact:** Students can't find helpful resources
**Estimated Fix Time:** 2-3 hours

**Problem:**
No centralized place for templates, datasets, research papers, tools.

**Definition of Done:**
- [ ] Discord channels created for resources
- [ ] At least 20 resources added
- [ ] Resources organized by category
- [ ] Pinned messages with category descriptions

**Channels to Create:**
- #resources-research (papers, frameworks)
- #resources-templates (project docs)
- #resources-datasets (supply chain data)
- #resources-tools (AI, software)

**Initial Resources:**
- Theory U methodology PDF
- Project proposal template
- Research paper template
- List of useful AI tools
- Supply chain datasets links

---

## 🔵 LOW PRIORITY ISSUES

### Performance

#### Issue #25: Cache Lifetimes 💾 LOW
**Source:** Lighthouse
**Savings:** 834 KiB on repeat visits
**Priority:** 🔵 LOW
**Impact:** Slower repeat visits
**Estimated Fix Time:** 2 hours (requires infrastructure)

**Problem:**
Static assets don't have long cache headers.

**Note:** GitHub Pages sets some caching automatically. Full control requires Cloudflare CDN.

---

#### Issue #26: Reduce JS Execution Time ⚡ LOW
**Source:** Lighthouse
**Current:** 1.5s
**Priority:** 🔵 LOW
**Impact:** Minor main thread blocking
**Estimated Fix Time:** 1-2 hours

**Solution:**
- Move inline scripts to external file
- Add `defer` attribute
- Minimize code

---

#### Issue #27: Font Display Optimization 🔤 LOW
**Source:** Lighthouse
**Savings:** 60ms
**Priority:** 🔵 LOW
**Impact:** Very minor FOIT prevention
**Estimated Fix Time:** 30 minutes

**Solution:**
Self-host Font Awesome with `font-display: swap`.

---

### Content

#### Issue #28: No Blog/News Section 📝 LOW
**Source:** Website Analysis
**Priority:** 🔵 LOW
**Impact:** No fresh content, SEO opportunity missed
**Estimated Fix Time:** 4-5 hours

**Future Enhancement:**
Create Jekyll blog for:
- Project highlights
- Industry insights
- Student stories
- Research updates

---

#### Issue #29: No Alumni Network 🎓 LOW
**Source:** Website Analysis
**Priority:** 🔵 LOW
**Impact:** Lost connection with past students
**Estimated Fix Time:** 5-6 hours

**Future Enhancement:**
Create alumni directory with:
- Where are they now?
- Career paths
- Testimonials
- Networking opportunities

---

#### Issue #30: No Analytics 📊 LOW
**Source:** Website Analysis
**Priority:** 🔵 LOW
**Impact:** Can't measure site performance
**Estimated Fix Time:** 1 hour

**Future Enhancement:**
Add Plausible Analytics (privacy-friendly).

---

## Quick Win Checklist (Can Complete Today)

These 5 issues can be fixed in < 3 hours total:

- [ ] **Issue #2:** Add aria-labels to buttons (30 min)
- [ ] **Issue #10:** Add `loading="lazy"` to images (30 min)
- [ ] **Issue #14:** Fix contact form with EmailJS (1 hour)
- [ ] **Issue #15:** Fix email addresses (.org → .xyz) (10 min)
- [ ] **Issue #20:** Add `object-fit: cover` to images (30 min)

**Total Time:** 2.5 hours
**Impact:** Fixes accessibility issues + improves performance

---

## This Week's Focus (Next 5 Days)

### Monday-Tuesday: Critical Issues
- [ ] Issue #1: Fix LCP (2 hours)
- [ ] Issue #2: Button accessibility (30 min)
- [ ] Issue #3: Color contrast (1 hour)
- [ ] Issue #4: Collect student info (3 hours)

### Wednesday-Thursday: High Priority Performance
- [ ] Issue #7: Render-blocking resources (3 hours)
- [ ] Issue #8: Convert images to WebP (2 hours)
- [ ] Issue #9: Resize images (2 hours)
- [ ] Issue #10: Lazy load images (30 min)

### Friday: Integration & Polish
- [ ] Issue #6: Add Discord widget (1 hour)
- [ ] Issue #16: Discord webhook (30 min)
- [ ] Issue #5: Update LinkedIn feed (15 min)
- [ ] Test everything and document

**Total Estimated Time:** 15.25 hours over 5 days = ~3 hours/day

---

## Tracking Progress

Use this checklist format in GitHub issues:

```markdown
## Issue #X: [Title]

**Priority:** 🔴 / 🟡 / 🟢 / 🔵
**Estimated Time:** X hours
**Owner:** [Name]

### Definition of Done
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

### Test
`bash
# Test commands here
`

### Progress
- [x] Step 1
- [ ] Step 2
- [ ] Step 3

### Blockers
- None / [Describe blocker]

### Notes
[Any additional notes]
```

---

**Document Created:** October 23, 2025
**Last Updated:** October 23, 2025
**Next Review:** October 30, 2025 (after this week's fixes)
