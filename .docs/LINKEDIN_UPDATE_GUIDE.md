# LinkedIn Feed Update Guide

**Purpose:** Keep the "Latest Updates" section current with real VCH LinkedIn posts
**Frequency:** Update on the 1st of every month
**Time Required:** 15 minutes
**Owner:** Maxime Bouillon (primary) / Christiaan Verhoef (backup)

---

## Monthly Update Process

### Step 1: Go to VCH LinkedIn
1. Open https://www.linkedin.com/company/valuechainhackers/posts/
2. Log in if needed
3. Scroll through recent posts (last 30 days)

### Step 2: Select 3 Posts
Choose posts that:
- Have good engagement (likes, comments)
- Represent different aspects of VCH (projects, events, partnerships)
- Are recent (within last month)
- Have clear, interesting content

**Example good posts:**
- Student project announcements
- Event recaps with photos
- Partnership announcements
- Student success stories
- Research highlights

### Step 3: Copy Post Information
For each of the 3 posts, copy:
1. **Post text** (first 2-3 sentences)
2. **Post URL** (click "..." menu → "Copy link to post")
3. **Post category** (e.g., "Project highlight", "Event recap", "Partnership")

### Step 4: Update index.html
Open `index.html` and find the LinkedIn section (around line 390-438)

Replace the 3 post cards with your collected information:

```html
<!-- POST 1 -->
<div class="bg-white rounded-xl shadow-sm border p-6">
    <div class="flex items-center gap-3 mb-4">
        <i class="fab fa-linkedin text-vch-green text-2xl"></i>
        <div>
            <div class="font-semibold text-vch-gray">Value Chain Hackers</div>
            <div class="text-xs text-vch-light-gray">POST CATEGORY HERE</div>
        </div>
    </div>
    <p class="text-vch-light-gray mb-4">
        POST TEXT HERE (2-3 sentences, add emoji if original had one)
    </p>
    <a href="PASTE_LINKEDIN_POST_URL_HERE" target="_blank" rel="noopener noreferrer" class="text-vch-green hover:text-green-600 text-sm font-semibold">
        View on LinkedIn →
    </a>
</div>
```

### Step 5: Test Locally (Optional)
```bash
bundle exec jekyll serve
# Visit http://localhost:4000
# Check LinkedIn section looks good
# Click links to verify they work
```

### Step 6: Commit and Push
```bash
git add index.html
git commit -m "content: update LinkedIn feed with October 2025 posts

- Added [brief description of post 1]
- Added [brief description of post 2]
- Added [brief description of post 3]

Updated: [current date]"
git push
```

---

## Template for Quick Updates

### Post Template:
```html
<div class="bg-white rounded-xl shadow-sm border p-6">
    <div class="flex items-center gap-3 mb-4">
        <i class="fab fa-linkedin text-vch-green text-2xl"></i>
        <div>
            <div class="font-semibold text-vch-gray">Value Chain Hackers</div>
            <div class="text-xs text-vch-light-gray">[CATEGORY]</div>
        </div>
    </div>
    <p class="text-vch-light-gray mb-4">
        [POST TEXT - 2-3 sentences max]
    </p>
    <a href="[LINKEDIN_URL]" target="_blank" rel="noopener noreferrer" class="text-vch-green hover:text-green-600 text-sm font-semibold">
        View on LinkedIn →
    </a>
</div>
```

### Category Examples:
- Project highlight
- Event recap
- Student spotlight
- Partnership announcement
- Research update
- Workshop series
- Community news
- Industry insights

---

## Example: Complete Update

### Original LinkedIn Posts (October 2025):

**Post 1:**
- **Text:** "🎉 Excited to announce our partnership with ZWINC for the Spring 2026 cohort! Together we'll tackle circularity challenges in the Dutch manufacturing sector."
- **URL:** `https://www.linkedin.com/feed/update/urn:li:activity:7123456789/`
- **Category:** Partnership announcement

**Post 2:**
- **Text:** "📊 Check out the amazing work by our Bakery Network team! They've mapped inefficiencies across 15 local bakeries and proposed a collaborative ordering system."
- **URL:** `https://www.linkedin.com/feed/update/urn:li:activity:7123456790/`
- **Category:** Project highlight

**Post 3:**
- **Text:** "🎓 30 students joined our final showcase event last week. From textile circularity to phone battery recycling, the projects blew us away!"
- **URL:** `https://www.linkedin.com/feed/update/urn:li:activity:7123456791/`
- **Category:** Event recap

### Updated HTML:
```html
<div class="grid md:grid-cols-3 gap-6">
    <!-- Post 1: Partnership -->
    <div class="bg-white rounded-xl shadow-sm border p-6">
        <div class="flex items-center gap-3 mb-4">
            <i class="fab fa-linkedin text-vch-green text-2xl"></i>
            <div>
                <div class="font-semibold text-vch-gray">Value Chain Hackers</div>
                <div class="text-xs text-vch-light-gray">Partnership announcement</div>
            </div>
        </div>
        <p class="text-vch-light-gray mb-4">
            🎉 Excited to announce our partnership with ZWINC for the Spring 2026 cohort! Together we'll tackle circularity challenges in the Dutch manufacturing sector.
        </p>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7123456789/" target="_blank" rel="noopener noreferrer" class="text-vch-green hover:text-green-600 text-sm font-semibold">
            View on LinkedIn →
        </a>
    </div>

    <!-- Post 2: Project -->
    <div class="bg-white rounded-xl shadow-sm border p-6">
        <div class="flex items-center gap-3 mb-4">
            <i class="fab fa-linkedin text-vch-green text-2xl"></i>
            <div>
                <div class="font-semibold text-vch-gray">Value Chain Hackers</div>
                <div class="text-xs text-vch-light-gray">Project highlight</div>
            </div>
        </div>
        <p class="text-vch-light-gray mb-4">
            📊 Check out the amazing work by our Bakery Network team! They've mapped inefficiencies across 15 local bakeries and proposed a collaborative ordering system.
        </p>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7123456790/" target="_blank" rel="noopener noreferrer" class="text-vch-green hover:text-green-600 text-sm font-semibold">
            View on LinkedIn →
        </a>
    </div>

    <!-- Post 3: Event -->
    <div class="bg-white rounded-xl shadow-sm border p-6">
        <div class="flex items-center gap-3 mb-4">
            <i class="fab fa-linkedin text-vch-green text-2xl"></i>
            <div>
                <div class="font-semibold text-vch-gray">Value Chain Hackers</div>
                <div class="text-xs text-vch-light-gray">Event recap</div>
            </div>
        </div>
        <p class="text-vch-light-gray mb-4">
            🎓 30 students joined our final showcase event last week. From textile circularity to phone battery recycling, the projects blew us away!
        </p>
        <a href="https://www.linkedin.com/feed/update/urn:li:activity:7123456791/" target="_blank" rel="noopener noreferrer" class="text-vch-green hover:text-green-600 text-sm font-semibold">
            View on LinkedIn →
        </a>
    </div>
</div>
```

---

## Calendar Reminder Setup

### Google Calendar:
1. Go to https://calendar.google.com
2. Click "+ Create" → "Event"
3. Title: "Update VCH Website LinkedIn Feed"
4. Date: 1st of every month
5. Time: 10:00 AM (or your preferred time)
6. Repeat: Monthly
7. Add reminder: 1 day before
8. Description: "Update index.html with 3 recent LinkedIn posts. See LINKEDIN_UPDATE_GUIDE.md"
9. Save

### Outlook Calendar:
1. Open Outlook Calendar
2. New Event → "Update VCH Website LinkedIn Feed"
3. Start: 1st of month, 10:00 AM
4. Recurrence: Monthly
5. Reminder: 1 day
6. Notes: Link to this guide
7. Save

---

##Troubleshooting

### Issue: Can't find LinkedIn post URL
**Solution:**
1. Click "..." menu on post
2. Select "Copy link to post"
3. If that doesn't work, right-click post timestamp and copy link

### Issue: Post text is too long
**Solution:**
- Keep only first 2-3 sentences
- Add "..." at the end if needed
- Full post is on LinkedIn (users can click to read more)

### Issue: Don't see recent posts
**Solution:**
- Make sure VCH account is posting regularly to LinkedIn
- If no recent posts, reuse one previous post + 2 new ones
- Consider this a reminder to post more on LinkedIn!

### Issue: HTML doesn't look right
**Solution:**
- Check you didn't break any closing tags `</div>`
- Make sure quotes are matched
- Test locally before pushing

---

## Tips for Better Posts

### Do:
- ✅ Use emojis from original posts
- ✅ Keep text concise (2-3 sentences)
- ✅ Choose visually different categories
- ✅ Link to actual LinkedIn URLs
- ✅ Test links after updating

### Don't:
- ❌ Copy entire long posts
- ❌ Use old posts (>2 months)
- ❌ Link to company page instead of specific post
- ❌ Forget to update all 3 posts
- ❌ Break HTML tags

---

## Quick Checklist

Before committing:
- [ ] 3 posts selected from VCH LinkedIn
- [ ] Each post has: text, URL, category
- [ ] Post URLs point to specific posts (not just company page)
- [ ] No HTML syntax errors
- [ ] Links tested (open in new tab)
- [ ] Commit message descriptive
- [ ] Pushed to GitHub
- [ ] Calendar reminder set for next month

---

**Last Updated:** October 23, 2025
**Next Update Due:** November 1, 2025
**Template Version:** 1.0
