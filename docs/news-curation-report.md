# News Curation Strategy Report
## Value Chain Hackers Website

**Report Date:** November 13, 2025
**Purpose:** Document the news article sourcing methodology and RSS feed strategy

---

## Overview

The VCH website automatically fetches and displays news articles from curated RSS feeds across two main categories:
1. **AI & Machine Learning News** - Focusing on AI applications in supply chain and general AI research
2. **Sustainability & Supply Chain News** - Focusing on circular economy, logistics, and sustainable supply chain practices

The news is fetched via a Python script (`scripts/fetch_news_feeds.py`) that runs automatically through GitHub Actions, updating the content regularly.

---

## 1. AI & Machine Learning News Sources

### Primary Sources

#### **Google AI Blog**
- **RSS Feed:** `https://blog.google/technology/ai/rss`
- **Category:** AI Research
- **Focus Areas:**
  - Latest AI developments from Google
  - Gemini API updates and features
  - AI in education and learning
  - Privacy and AI computing
  - Practical AI applications

#### **MIT AI News**
- **RSS Feed:** `https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml`
- **Category:** AI Research
- **Focus Areas:**
  - Academic AI research
  - AI energy efficiency and sustainability
  - Robotics and AI systems
  - AI in ecosystem monitoring
  - Novel AI architectures and methods

#### **KDnuggets**
- **RSS Feed:** `https://www.kdnuggets.com/feed`
- **Category:** Machine Learning
- **Focus Areas:**
  - Practical ML tutorials and guides
  - Data science best practices
  - AI tools and alternatives
  - Data pipeline engineering
  - Business impact of data science
  - Python and ML frameworks

#### **SupplyChainBrain AI**
- **RSS Feed:** `https://www.supplychainbrain.com/topics/technology/artificial-intelligence-ai-machine-learning/rss`
- **Category:** Supply Chain Technology
- **Focus Areas:**
  - AI applications in logistics
  - Supply chain visibility solutions
  - Predictive analytics for supply chain
  - Warehouse automation

---

## 2. Sustainability & Supply Chain News Sources

### Primary Sources

#### **Supply Chain 24/7**
- **RSS Feed:** `https://www.supplychain247.com/rss`
- **Category:** Supply Chain Operations
- **Focus Areas:**
  - Port operations and emissions
  - Material handling industry
  - Intermodal freight solutions
  - Warehouse automation
  - EDI and API integration
  - Last-mile delivery innovations
  - Container shipping and logistics

#### **Circular Online**
- **RSS Feed:** `https://www.circularonline.co.uk/feed/`
- **Category:** Circular Economy
- **Focus Areas:**
  - Circular economy policy and strategy
  - Waste management and recycling
  - Climate change and sustainability
  - Deposit return schemes
  - Food waste solutions
  - Sustainable materials (wood, plastics)
  - Environmental compliance

#### **SupplyChainBrain**
- **RSS Feed:** `https://www.supplychainbrain.com/rss`
- **Category:** Supply Chain Management
- **Focus Areas:**
  - General supply chain trends
  - Logistics and transportation
  - Supply chain technology
  - Industry best practices

#### **Logistics Management**
- **RSS Feed:** `https://www.logisticsmgmt.com/rss`
- **Category:** Logistics Operations
- **Focus Areas:**
  - Transportation management
  - Warehouse operations
  - Freight and logistics trends
  - Supply chain optimization

#### **BSR Insights**
- **RSS Feed:** `https://www.bsr.org/en/blog/rss`
- **Category:** Sustainability
- **Focus Areas:**
  - Corporate sustainability practices
  - ESG and responsible business
  - Supply chain sustainability
  - Sustainable development insights

---

## 3. Content Filtering & Selection Methodology

### Automated Process

The news fetching system uses the following approach:

1. **RSS Feed Parsing**
   - Fetches latest articles from each RSS feed
   - Retrieves up to 10 articles per source initially
   - Extracts: title, link, description, publication date, source

2. **Content Aggregation**
   - Combines articles from all sources in each category
   - Sorts by publication date (newest first)
   - Keeps top 50 most recent articles per category

3. **Data Structure**
   - Stores articles in YAML format (`_data/ai_news.yml` and `_data/sustainability_news.yml`)
   - Each article includes:
     - Title
     - Link to original article
     - Description (truncated to ~200 characters)
     - Publication date (ISO format)
     - Source name
     - Category tag
     - Icon for visual identification

4. **Update Frequency**
   - Automated via GitHub Actions
   - Runs on schedule (configuration in `.github/workflows/`)
   - Last updated timestamp tracked in YAML files

---

## 4. Keywords & Topics Covered

### AI & Machine Learning Topics
- Artificial intelligence applications
- Machine learning frameworks
- Data science and analytics
- AI in education
- Computer vision
- Natural language processing
- AI ethics and privacy
- Automation and robotics
- Predictive analytics
- AI infrastructure and energy

### Supply Chain & Sustainability Topics
- Supply chain visibility
- Logistics optimization
- Warehouse automation
- Circular economy
- Waste management and recycling
- Zero emissions and clean energy
- Port operations
- Material handling
- Freight and transportation
- Sustainable packaging
- Climate change mitigation
- ESG and corporate responsibility
- Supply chain resilience

---

## 5. Content Quality Indicators

### Source Selection Criteria

Sources were chosen based on:
1. **Authority** - Reputable institutions (MIT, Google) or industry leaders
2. **Relevance** - Direct connection to VCH mission and focus areas
3. **Update Frequency** - Regular publication schedule
4. **Content Quality** - Professional, informative, research-backed content
5. **Accessibility** - Open access to content via RSS

### Content Characteristics

Articles typically feature:
- Research findings and academic insights
- Industry trends and analysis
- Practical applications and case studies
- Technology innovations
- Policy and regulatory updates
- Business impact and ROI discussions

---

## 6. Recommendations for Enhancement

### Potential Additional Sources

**AI & Supply Chain:**
- Stanford HAI (Human-Centered AI) Blog
- DeepMind Research Blog
- AI in Logistics publications
- Gartner Supply Chain research

**Sustainability:**
- Ellen MacArthur Foundation (Circular Economy)
- World Economic Forum Supply Chain posts
- GreenBiz sustainability news
- Supply Chain Dive sustainability section

### Content Refinement Options

1. **Keyword Filtering**
   - Add specific keyword filtering to focus on:
     - "supply chain"
     - "value chain"
     - "sustainability"
     - "circular economy"
     - "logistics AI"
     - "predictive analytics"
     - "warehouse automation"

2. **Category Expansion**
   - Add subcategories for better organization
   - Consider tags: blockchain, IoT, automation, policy, case-studies

3. **Content Scoring**
   - Implement relevance scoring based on keyword matches
   - Prioritize articles mentioning key VCH focus areas

4. **Duplicate Detection**
   - Add logic to filter duplicate stories from multiple sources
   - Keep highest-quality or most detailed version

---

## 7. Technical Implementation

### Script Location
`scripts/fetch_news_feeds.py`

### Dependencies
- `feedparser` - RSS/Atom feed parsing
- `pyyaml` - YAML file handling
- Python 3.x standard library

### Configuration
Edit the `SUSTAINABILITY_FEEDS` and `AI_FEEDS` lists in the script to:
- Add new RSS sources
- Modify categories
- Change icons
- Adjust article limits

### Manual Update
Run locally:
```bash
cd scripts
python fetch_news_feeds.py
```

---

## 8. Current Performance Metrics

### Last Update Stats
- **AI News:** ~30 articles from 4 sources (updated 2025-11-13)
- **Sustainability News:** ~20 articles from 5 sources (updated 2025-11-13)
- **Date Range:** Typically covers last 7-14 days of content
- **Retention:** Top 50 articles per category

### Source Distribution
**AI News:**
- KDnuggets: ~40% (high-volume, practical content)
- Google AI Blog: ~30% (official announcements, features)
- MIT AI News: ~20% (research-focused)
- SupplyChainBrain AI: ~10% (industry-specific)

**Sustainability News:**
- Supply Chain 24/7: ~40% (frequent updates)
- Circular Online: ~35% (UK-focused circular economy)
- Other sources: ~25% (varied perspectives)

---

## Conclusion

The VCH news curation system provides a balanced mix of cutting-edge AI research, practical machine learning applications, and supply chain sustainability insights. The automated RSS-based approach ensures fresh content while maintaining high relevance to the VCH community's interests in value chain innovation and sustainable practices.

The current source selection effectively bridges academic research (MIT), industry leaders (Google), practical applications (KDnuggets), and domain-specific publications (Supply Chain 24/7, Circular Online), creating a comprehensive news experience for students, researchers, and industry partners.
