# AI Project Concept Template for Windesheim/VCH

**All projects follow Agile principles with iterative development, regular sprint cycles, and continuous stakeholder feedback.**

---

## PROJECT CONCEPT

### Basic Information
**Project Title:** SupplyLens

**Project Slug:** `supplylens`

**Concept Status:** in-development

**Category:** research / internal-tool

**GitHub Repository:** https://github.com/Value-Chain-Hacking/SupplyLens

---

## THE 3 MINUTE RULE PITCH

### 1. What is it?
An AI-powered supply chain mapping platform that finds hidden supplier relationships by analyzing financial data, shipping records, and ESG reports.

### 2. How does it work?
The system crawls public documents (company reports, trade data, shipping manifests), extracts entities and relationships using AI, stores everything in a knowledge graph database, and lets you query it in natural language to reveal who supplies what to whom across multiple tiers.

### 3. Are you sure?
Graph databases + LLMs are proven for entity extraction. Similar forensic approaches used by investigative journalists and NGOs. PostgreSQL AGE provides the graph infrastructure we need.

### 4. Can you do it?
[TO FILL - Team technical capabilities, access to data sources]

### 5. What's the value?
Exposes supply chain problems companies hide (forced labor, environmental damage, conflict minerals). Helps NGOs, journalists, regulators, and ethical companies find truth in opaque supply networks. For students: real-world AI application with societal impact.

### 6. Are there any risks?
- Data quality and completeness varies wildly
- AI entity extraction produces false positives
- Graph becomes too complex to query effectively
- Legal issues if we expose sensitive business relationships
- Computational costs for large-scale crawling

---

### The Problem

**What problem does this solve?**
"Find the problems in the supply chain no one really wants to talk about." Traditional supply chain mapping tools can't access hidden relationships or infer missing connections. Companies obscure their supply networks to avoid accountability for ESG violations.

**Who has this problem?**
- NGOs investigating labor/environmental violations
- Investigative journalists
- Regulators enforcing CSRD/CSDDD compliance
- Ethical companies wanting true supply chain visibility
- Researchers studying global trade networks

**How big is the problem?**
Most multi-tier supply chains are completely opaque beyond tier 2. ESG violations happen in hidden tiers where no one is looking.

---

### The AI Solution

**What AI/ML technique would you use?**
- Named Entity Recognition (NER) to extract companies, locations, products
- Relationship extraction using LLMs
- Semantic search (pgvector) to find similar entities
- Knowledge graph reasoning to infer hidden connections
- Natural language query interface (LangChain + LLMs)

**What data would you need?**
- ESG reports, sustainability disclosures (public)
- Shipping manifests, customs data (some public, some paid)
- Financial filings, annual reports (public)
- Trade databases
- News articles about supply chain relationships
- Data availability: Mix of public and proprietary sources

**Expected output/deliverable:**
Web platform with natural language query interface, graph visualizations showing supplier networks, API for programmatic access, forensic reasoning reports.

---

## TIMELINE & MILESTONES

### Project Duration
**Total Estimated Time:** [TO FILL]
**Sprint Length:** 2 weeks
**Total Sprints:** [TO FILL]

[TO FILL - Full milestone table]

---

## CURRENT STATUS (from GitHub)

**Repository:** https://github.com/Value-Chain-Hacking/SupplyLens
**Status:** Active (created April 29, 2025, 7 commits)
**Current State:** Early stage - "rebuilding from the ground up with more rigorous development process"

**Tech Stack:**
- PostgreSQL + Apache AGE (graph database)
- pgvector (semantic search)
- LangChain (LLM integration)
- Docker/Docker Compose
- Multiple LLM support (GPT, Ollama, LM Studio)
- n8n, Supabase integration planned

**Key Features Planned:**
- Automated data crawling from ESG reports and trade docs
- Entity extraction and relationship inference
- Natural language query interface
- Knowledge graph visualization
- Forensic reasoning methodology

**Team Status:**
Seeking academic partners, companies, investors, and NGOs for pilot testing

---

## NOTES FOR COMPLETION

[TO FILL - Timeline, team, budget, partnerships, visual assets]

**Key Questions:**
- What data sources have we secured access to?
- Which LLM provider will we use primarily?
- What's the data ingestion pipeline architecture?
- How will we validate AI-extracted relationships?
- What's the query interface UX?
