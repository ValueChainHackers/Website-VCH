<!-- Copilot / AI agent instructions for contributors -->
# Quick reference for automated code agents

This repository is a Jekyll-based static website (Value Chain Hackers). The notes below give an AI agent the essential, actionable context to be productive: big-picture architecture, developer workflows, project conventions, and important integration points. Use the exact files and commands listed.

1) Big picture
- Generator: Jekyll (see `Gemfile` and `_config.yml`). Layouts live in `_layouts/` and collections in `_projects/`, `_team/`, `_events/`.
- CSS: Tailwind is used; input at `assets/css/main.css`, built output `assets/css/styles.css` (see `package.json` scripts and `tailwind.config.js`).
- News data: `scripts/fetch_news_feeds.py` produces `_data/sustainability_news.yml` and `_data/ai_news.yml`. These are read by `sustainability-news.html` and `ai-news.html`.
- Hosting: GitHub Pages auto-deploys from `main` branch (standard Jekyll / Pages setup).

2) Essential developer workflows & commands (run these in repo root)
- Install Ruby/Jekyll gems:
  - `bundle install`
- CSS build (Node + Tailwind):
  - `npm install`
  - `npm run build:css` (produce minified `assets/css/styles.css`)
  - `npm run watch:css` for continuous CSS work
- Local preview (Jekyll):
  - Build CSS first (or run the watcher), then `bundle exec jekyll serve` and open `http://localhost:4000`.
- Update news data locally (requires Python dependencies):
  - `pip install feedparser pyyaml`
  - `python scripts/fetch_news_feeds.py` (writes `_data/ai_news.yml` and `_data/sustainability_news.yml`)

3) Project-specific conventions (do not invent different patterns)
- Content files: Add new projects to `_projects/` as markdown with frontmatter; layouts expect `layout: project`. Example frontmatter:
  ```yaml
  ---
  layout: project
  title: "Project Name"
  description: "One-line summary"
  team: [Name1, Name2]
  tags: [sustainability, AI]
  ---
  ```
- Image handling: images in `assets/images/`; repository uses WebP fallbacks. Maintain `width`/`height` attributes on `<img>` to avoid layout shift.
- CSS: Tailwind content paths are defined in `tailwind.config.js`—only update that file if adding new template locations (e.g. new collection folders).
- Excluded files: see `_config.yml: exclude` to avoid touching files that are not processed by Jekyll (e.g. `.docs/`, `TASKS.md`).

4) Integration points and secrets
- Email (contact form): EmailJS keys are referenced from `index.html`. Do not hardcode new keys in source; prefer GitHub Secrets and template injection where possible.
- Discord: Deployment/notification webhook should be stored as a GitHub Secret (`DISCORD_WEBHOOK`) and used in workflow files. Search for references in `.github/workflows/` when creating automation.
- Auto-updating news: `scripts/fetch_news_feeds.py` is the canonical source—do not hand-edit `_data/ai_news.yml` or `_data/sustainability_news.yml` unless for a quick fix; prefer updating the script or the feed list.

5) Files to inspect when making changes (high signal)
- `_layouts/` — layout templates (e.g. `project.html`, `default.html`)
- `_projects/` — project pages (content + frontmatter examples)
- `index.html` — homepage (LinkedIn/Discord sections and many integration points)
- `scripts/fetch_news_feeds.py` — feed list, fetching logic, YAML output structure
- `package.json` & `tailwind.config.js` — CSS build and Tailwind config
- `_config.yml` — Jekyll settings, plugins, collections, exclude/include
- `assets/css/main.css` & `assets/css/styles.css` — Tailwind input + built CSS output

6) Common, discoverable patterns & examples agents should follow
- When adding a project page, copy an existing file from `_projects/` to preserve frontmatter keys and permalink behavior.
- When modifying frontmatter schema, update `_layouts/project.html` and the relevant `.docs/PROJECT_PAGES_GUIDE.md` if present.
- For performance work: follow patterns in `TASKS.md` and `.docs/PERFORMANCE_IMPROVEMENTS.md`—images are WebP, critical CSS is inlined for key content, and Tailwind utility usage is preferred over custom CSS.

7) Quick troubleshooting pointers
- If CSS changes don't appear: ensure `npm run build:css` was run and `assets/css/styles.css` is up-to-date; Jekyll serves the static `assets/` folder.
- If news pages are empty: run `python scripts/fetch_news_feeds.py` and check `_data/*.yml` for content and timestamps.
- If a page fails locally: look at Jekyll's build output when running `bundle exec jekyll serve`—missing frontmatter keys or Liquid errors will be printed.

8) When to ask for human guidance
- Secret/key handling (EmailJS, Discord webhooks) — do not attempt to create or modify secrets; request a maintainer to inject them.
- Significant layout changes or collection schema updates — request design/owner review (see `TASKS.md` for maintainers list).

If anything here is unclear or you need more examples (e.g., a recent project frontmatter to replicate), tell me which area to expand and I will update this file.
