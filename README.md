# Value Chain Hackers Website

Official website for Value Chain Hackers - a student-led initiative at Windesheim University bringing together students, researchers, and businesses to solve real-world supply chain challenges.

🌐 **Live Site:** [valuechainhackers.xyz](https://valuechainhackers.xyz)

---

## 🚀 Quick Start

This is a Jekyll static site hosted on GitHub Pages.

### Local Development

```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Visit http://localhost:4000
```

### Deployment

The site auto-deploys to GitHub Pages when you push to the `main` branch.

---

## 📂 Project Structure

```
Website-VCH/
├── _layouts/           # Page templates
│   ├── default.html    # Main layout with navigation
│   └── project.html    # Project detail template
├── _projects/          # Student project pages
├── _team/              # Team member profiles
├── assets/
│   ├── css/           # Stylesheets
│   ├── images/        # Images (WebP + fallbacks)
│   └── documents/     # PDFs and other files
├── .docs/             # Documentation (not published)
├── index.html         # Homepage
├── about.html         # Team & about page
├── events.html        # Events & meetups
├── workshops.html     # Workshop library
├── sustainability-news.html  # Auto-updating sustainability news
├── ai-news.html       # Auto-updating AI news
├── onboarding.html    # Join VCH guide
└── TASKS.md           # Current tasks & issues
```

---

## 🎨 Key Features

### Auto-Updating News Pages
- **Sustainability News** (`/sustainability-news.html`) - Pulls from 7 RSS feeds
- **AI News** (`/ai-news.html`) - Pulls from 10 AI/ML RSS feeds
- Updates automatically on every page load

### Performance Optimized
- ✅ WebP images with fallbacks (90% size reduction)
- ✅ Async loading for fonts and icons
- ✅ Lazy loading for below-fold images
- ✅ Preconnect to external CDNs
- **Target LCP:** <2.5s

### Event Registration
- Google Forms integration with modal popups
- Discord webhook notifications
- See `.docs/EVENT_REGISTRATION_GUIDE.md`

### Contact Form
- EmailJS integration (200 emails/month free tier)
- See `.docs/EMAILJS_SETUP_GUIDE.md`

---

## 📝 Content Management

### Adding a New Project

1. Create file in `_projects/project-name.md`
2. Use frontmatter template:
```yaml
---
layout: project
title: "Project Name"
description: "Brief description"
category: student
tags: [sustainability, AI]
team: [Name 1, Name 2]
status: completed
---
```
3. See `.docs/PROJECT_PAGES_GUIDE.md` for details

### Updating LinkedIn Feed

1. Open `index.html`
2. Find LinkedIn section (lines 388-444)
3. Update 3 posts with real content
4. See `.docs/LINKEDIN_UPDATE_GUIDE.md`

### Adding Workshops

1. Upload Quarto/PowerPoint to `assets/workshops/`
2. Update `workshops.html`
3. Follow HTML comments for instructions

### Managing Events

1. Create Google Form for registration
2. Update `events.html` with form ID
3. See `.docs/EVENT_REGISTRATION_GUIDE.md`

---

## 🛠️ Tech Stack

- **Jekyll** - Static site generator
- **Tailwind CSS** - Utility-first CSS (via CDN)
- **Font Awesome 6.4** - Icons
- **Google Fonts** - Inter typeface
- **EmailJS** - Contact form
- **GitHub Actions** - Discord deployment notifications

---

## 📚 Documentation

All documentation is in the `.docs/` directory:

- `TASKS.md` - Current tasks & issues (kept in root for visibility)
- `.docs/PERFORMANCE_IMPROVEMENTS.md` - Performance optimization guide
- `.docs/EMAILJS_SETUP_GUIDE.md` - Contact form setup
- `.docs/LINKEDIN_UPDATE_GUIDE.md` - Monthly LinkedIn updates
- `.docs/EVENT_REGISTRATION_GUIDE.md` - Event registration system
- `.docs/DISCORD_WEBHOOK_SETUP.md` - Discord notifications
- `.docs/PROJECT_PAGES_GUIDE.md` - How to add projects
- `.docs/DNS_SUBDOMAIN_SETUP.md` - DNS configuration

---

## 🔧 Configuration

### Required Setup

1. **EmailJS** (for contact form)
   - Create account at emailjs.com
   - Add API keys to `index.html`
   - See `.docs/EMAILJS_SETUP_GUIDE.md`

2. **Discord Webhook** (for deployment notifications)
   - Create webhook in Discord
   - Add to GitHub Secrets as `DISCORD_WEBHOOK`
   - See `.docs/DISCORD_WEBHOOK_SETUP.md`

3. **Google Forms** (for event registration)
   - Create forms for each event
   - Update `events.html` with form IDs
   - See `.docs/EVENT_REGISTRATION_GUIDE.md`

### Optional Setup

- **LinkedIn Feed** - Update monthly with real posts
- **Discord Widget** - Add server ID to `index.html`

---

## 🎯 Current Tasks

See `TASKS.md` for the complete list of:
- 🔴 Critical issues
- 🟡 High priority items
- 🟢 Medium priority improvements
- 🔵 Future enhancements

---

## 👥 Team

- **Michiel Steeman** - Lector, Project Owner
- **Maxime Bouillon** - Teacher/Researcher, Manager
- **Rea Vaz** - Researcher
- **Christiaan Verhoef** - Technical Facilitator

---

## 📧 Contact

- **Email:** info@valuechainhackers.xyz
- **Discord:** [discord.gg/mkbjsQsV](https://discord.gg/mkbjsQsV)
- **Website:** [valuechainhackers.xyz](https://valuechainhackers.xyz)

---

## 📄 License

This project is maintained by Value Chain Hackers at Windesheim University.

---

## 🔄 Recent Updates

### October 2025
- ✅ Added auto-updating news pages (Sustainability + AI)
- ✅ Created workshops page with upload system
- ✅ Built interactive onboarding flow
- ✅ Added events page with Google Forms registration
- ✅ Converted all images to WebP (90% size reduction)
- ✅ Optimized LCP performance (<2.5s target)
- ✅ Added navigation for all new pages
- ✅ Fixed header logo
- ✅ Implemented Discord webhook for deployments

See `.docs/` for detailed change history.
