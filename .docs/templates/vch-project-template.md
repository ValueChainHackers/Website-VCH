---
# =============================================================================
# VCH PROJECT TEMPLATE
# For projects that Value Chain Hackers is building (tools, platforms, systems)
# Version: 1.0 | Last Updated: 2025-10-24
# =============================================================================

# [REQUIRED] Project title - Keep concise and descriptive (3-10 words)
# Example: "OpenWebUI Integration Platform"
title: "Project Title Here"

# [REQUIRED] Brief description for project cards and SEO
# Guidelines: 1-2 sentences, <160 characters, focus on value proposition
# Example: "AI-powered platform for supply chain optimization and collaborative research"
description: "Brief project description here"

# [REQUIRED] Current project status
# Options: "Planning" | "In Development" | "Beta" | "Live" | "Maintenance" | "Archived"
status: "In Development"

# [REQUIRED] Project category
# Options: "VCH Project" | "Tool" | "Platform" | "Integration" | "Research Tool"
category: "VCH Project"

# [REQUIRED] Unique URL path for this project page
# Format: /projects/project-name/ (lowercase, hyphens only)
permalink: /projects/project-name/

# [OPTIONAL] Live website URL where project is deployed
# Example: "https://openwebui.valuechainhackers.xyz"
website: ""

# [OPTIONAL] GitHub repository URL (if public or internal)
# Example: "https://github.com/ValueChainHackers/project-name"
github: ""

# [OPTIONAL] Documentation URL (ReadTheDocs, Wiki, etc.)
# Example: "https://docs.valuechainhackers.xyz/project-name"
documentation_url: ""

# [OPTIONAL] API documentation URL
# Example: "https://api.valuechainhackers.xyz/docs"
api_docs_url: ""

# [REQUIRED] Project team members
# List primary contributors, use full names
# Example: "Christiaan Verhoef (Lead), Student Contributors"
team: "Team Member Names"

# [OPTIONAL] Project lead/maintainer
project_lead: "Name Here"

# [OPTIONAL] Contributing partners or organizations
partners: ""

# [REQUIRED] Project start date
# Format: "Month Year" or "YYYY-MM-DD"
# Example: "September 2024" or "2024-09-01"
start_date: "Month Year"

# [OPTIONAL] Launch date (if project is live)
# Format: "Month Year" or "YYYY-MM-DD"
launch_date: ""

# [OPTIONAL] Last major update date
last_updated: ""

# [REQUIRED] Tags for categorization and search
# Choose 3-6 relevant tags
# Options: AI, Blockchain, Supply Chain, Sustainability, Education, Tools, Platform, Integration, etc.
tags:
  - Tag1
  - Tag2
  - Tag3

# =============================================================================
# TECHNICAL DETAILS
# =============================================================================

# [OPTIONAL] Technical stack - languages, frameworks, tools used
# Example: ["Python 3.11", "FastAPI", "PostgreSQL", "Docker", "React"]
tech_stack:
  - Technology1
  - Technology2
  - Technology3

# [OPTIONAL] Programming languages used
# Example: ["Python", "JavaScript", "TypeScript"]
languages:
  - Language1

# [OPTIONAL] Key dependencies or services
# Example: ["OpenAI API", "Anthropic Claude", "PostgreSQL", "Redis"]
dependencies:
  - Dependency1

# [OPTIONAL] Deployment platform
# Example: "Docker on VPS" | "Kubernetes" | "GitHub Pages" | "Vercel"
deployment: ""

# [OPTIONAL] License
# Example: "MIT" | "Apache 2.0" | "Proprietary"
license: ""

# =============================================================================
# PROJECT LINKS & RESOURCES
# =============================================================================

# [OPTIONAL] Links to demos, videos, presentations
resources:
  - title: "Resource Title"
    type: "Demo" # Options: Demo, Video, Tutorial, Presentation, Documentation
    url: "/assets/documents/project-name/resource.pdf"

# [OPTIONAL] External integrations or APIs used
integrations:
  - name: "Integration Name"
    url: "https://example.com"
    description: "What it's used for"

# =============================================================================
# PROJECT ROADMAP
# Optional but recommended for ongoing projects
# =============================================================================

roadmap:
  - phase: "Planning & Design"
    date: "Month Year"
    completed: true
    description: "Brief description of what was done"

  - phase: "Core Development"
    date: "Month Year"
    completed: true
    description: ""

  - phase: "Beta Testing"
    date: "Month Year"
    completed: false
    description: ""

  - phase: "Public Launch"
    date: "Month Year"
    completed: false
    description: ""

# =============================================================================
# METADATA & SEO
# =============================================================================

# [OPTIONAL] Open Graph image for social media sharing
# Should be 1200x630px, stored in /assets/images/projects/
og_image: "/assets/images/projects/project-name/og-image.jpg"

# [OPTIONAL] Featured image for project cards
# Should be 800x600px, stored in /assets/images/projects/
featured_image: "/assets/images/projects/project-name/featured.jpg"

# [OPTIONAL] Custom meta description (if different from description)
meta_description: ""

---

<!--
=============================================================================
MARKDOWN CONTENT SECTIONS
Everything below the YAML front matter (---) is the page content
=============================================================================
-->

## About the Project

<!--
[REQUIRED] 2-3 paragraph overview of the project
- What problem does it solve?
- Who is it for?
- What makes it unique or valuable?
- Keep it accessible - explain technical concepts in plain language
-->

Write a compelling overview here that explains what this project is and why it matters.

**Example:**
The OpenWebUI Integration Platform connects Value Chain Hackers' research infrastructure with cutting-edge AI capabilities, enabling students and researchers to leverage large language models for supply chain analysis and optimization. By providing a user-friendly interface and pre-configured tools, the platform reduces the technical barrier to entry for AI-assisted research.


## Key Features

<!--
[REQUIRED] List 4-8 main features or capabilities
- Use descriptive headings
- Explain WHAT it does and WHY it's useful
- Include technical details without being overwhelming
-->

### Feature 1: Descriptive Name
Brief description of this feature and its benefits.

### Feature 2: Another Feature
Description here.

### Feature 3: Third Feature
Description here.


## Technical Architecture

<!--
[OPTIONAL but RECOMMENDED for technical projects]
- High-level overview of how the system works
- Key components and their interactions
- Data flow or system architecture
- Can include diagrams (store in /assets/images/projects/)
-->

Brief explanation of technical architecture, components, and how they work together.

**System Components:**
- **Component 1:** What it does
- **Component 2:** What it does
- **Component 3:** What it does

<!-- Optional: Add architecture diagram -->
<!-- ![Architecture Diagram](/assets/images/projects/project-name/architecture.png) -->


## Getting Started

<!--
[REQUIRED for tools/platforms users can access]
- How to access the project
- Prerequisites (accounts, permissions, etc.)
- Basic setup or onboarding steps
- Link to detailed documentation if available
-->

### Prerequisites
- List any requirements here
- Account or access needed
- Technical knowledge required

### Quick Start

1. **Step 1:** Description of first step
2. **Step 2:** Description of second step
3. **Step 3:** Description of third step

For detailed setup instructions, see the [full documentation]({{ page.documentation_url }}).


## Use Cases

<!--
[OPTIONAL but RECOMMENDED]
- Real-world scenarios where this project is useful
- Specific examples of problems it solves
- Target audience applications
-->

### Use Case 1: Scenario Name
Description of who would use this and how.

### Use Case 2: Another Scenario
Description here.


## Technology Stack

<!--
[OPTIONAL - include if technical details are relevant]
- Programming languages
- Frameworks and libraries
- Infrastructure and deployment
- Third-party services
-->

**Languages:** Python 3.11, JavaScript (ES6+)

**Backend:** FastAPI, PostgreSQL, Redis

**Frontend:** React, Tailwind CSS

**Infrastructure:** Docker, Kubernetes, GitHub Actions

**AI/ML:** OpenAI GPT-4, Anthropic Claude, LangChain


## Roadmap & Future Plans

<!--
[OPTIONAL but RECOMMENDED for ongoing projects]
- What's coming next
- Planned features or improvements
- Long-term vision
- Community contribution opportunities
-->

### Short Term (Next 3 months)
- Feature or improvement 1
- Feature or improvement 2

### Long Term (6-12 months)
- Major feature or change 1
- Major feature or change 2

### Vision
Long-term aspirations for this project.


## Contributing

<!--
[OPTIONAL - include for open-source or collaborative projects]
- How others can contribute
- Contribution guidelines
- Code of conduct
- Contact for questions
-->

We welcome contributions! Here's how you can help:

- **Report bugs:** [Open an issue]({{ page.github }}/issues)
- **Suggest features:** [Start a discussion]({{ page.github }}/discussions)
- **Submit code:** [Create a pull request]({{ page.github }}/pulls)

See our [Contributing Guidelines]({{ page.github }}/blob/main/CONTRIBUTING.md) for details.


## Documentation & Support

<!--
[OPTIONAL]
- Links to documentation
- Support channels
- FAQ
- Tutorials and guides
-->

- **Full Documentation:** [{{ page.documentation_url }}]({{ page.documentation_url }})
- **API Reference:** [{{ page.api_docs_url }}]({{ page.api_docs_url }})
- **GitHub Issues:** [{{ page.github }}/issues]({{ page.github }}/issues)
- **Contact:** [info@valuechainhackers.xyz](mailto:info@valuechainhackers.xyz)


## Screenshots & Demos

<!--
[OPTIONAL but RECOMMENDED for visual projects]
- Screenshots showing key features
- Demo videos
- Interactive examples
- Store images in /assets/images/projects/project-name/
-->

<!--
![Screenshot 1](/assets/images/projects/project-name/screenshot-1.png)
*Caption describing what this shows*

![Screenshot 2](/assets/images/projects/project-name/screenshot-2.png)
*Caption describing what this shows*
-->


## License & Credits

<!--
[OPTIONAL]
- License information
- Attribution for libraries/tools used
- Acknowledgments
-->

This project is licensed under the [{{ page.license }} License]({{ page.github }}/blob/main/LICENSE).

**Built with:**
- Technology or library with link
- Another tool with link


## Related Projects

<!--
[OPTIONAL]
- Links to related VCH projects
- Similar tools or platforms
- Complementary resources
-->

- [Related Project 1](/projects/related-project-1)
- [Related Project 2](/projects/related-project-2)


---

<!--
=============================================================================
TEMPLATE USAGE NOTES FOR AI
=============================================================================

When filling in this template:

1. REQUIRED fields must be filled in - use "TBD" if information is temporarily unavailable
2. OPTIONAL fields can be omitted entirely if not relevant
3. Uncomment sections (remove <!-- and -->) when using them
4. Delete unused sections rather than leaving them empty
5. Keep descriptions concise but informative
6. Use active voice and present tense
7. Technical terms are OK but explain them for general audience
8. All asset paths should point to /assets/ not StudentProjects/ or Pitches/
9. Test all links before publishing
10. Images should be optimized (<500KB, WebP preferred)

Content Quality Standards:
- Professional but accessible tone
- No marketing fluff - focus on facts and value
- Technical accuracy is critical
- Specific examples better than vague statements
- Screenshots and visuals enhance understanding

SEO Best Practices:
- Title: 3-10 words, includes main keyword
- Description: <160 characters, compelling call-to-action
- Tags: 3-6 relevant terms for categorization
- Meta description: Unique per project
- OG image: 1200x630px for social media

Examples of Good Content:
See _projects/cacao-guide.md for reference of well-structured project page
-->
