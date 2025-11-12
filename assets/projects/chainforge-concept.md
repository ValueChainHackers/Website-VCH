# AI Project Concept Template for Windesheim/VCH

**All projects follow Agile principles with iterative development, regular sprint cycles, and continuous stakeholder feedback.**

---

## PROJECT CONCEPT

### Basic Information
**Project Title:** ChainForge (VCH Fork)

**Project Slug:** `chainforge`

**Concept Status:** in-development

**Category:** internal-tool / research

**GitHub Repository:** https://github.com/Value-Chain-Hacking/ChainForge
**Upstream:** https://github.com/ianarawjo/ChainForge

---

## THE 3 MINUTE RULE PITCH

### 1. What is it?
A visual programming tool for testing and comparing AI prompts across different models without writing code.

### 2. How does it work?
You create prompt variations using a drag-and-drop interface, connect them to multiple AI models (OpenAI, Anthropic, Google, etc.), run them all at once, and see which prompts work best through automatic scoring and comparison charts.

### 3. Are you sure?
It's an existing open-source project (chainforge.ai) with 369 commits and active community. We're forking it to customize for supply chain research use cases.

### 4. Can you do it?
[TO FILL - Is this a fork we're maintaining or contributing upstream?]

### 5. What's the value?
Students and researchers can systematically test prompts instead of ad-hoc trial and error. Critical for supply chain AI projects where prompt quality directly impacts data extraction accuracy.

### 6. Are there any risks?
- Maintenance burden if we fork heavily
- API costs for testing multiple models
- Learning curve for students unfamiliar with visual programming

---

### The Problem

**What problem does this solve?**
Researchers test LLM prompts by manually copying/pasting into ChatGPT and comparing results in their heads. This doesn't scale, isn't reproducible, and wastes time. Need systematic "battle-testing" of prompts.

**Who has this problem?**
VCH students and researchers using LLMs for supply chain data extraction, analysis, and research tasks.

---

### The AI Solution

**What AI/ML technique would you use?**
Prompt engineering, systematic evaluation, multi-model comparison. Not building AI - building tools to use AI better.

**What data would you need?**
Access to LLM APIs (OpenAI, Anthropic, Google, etc.). Test datasets for supply chain scenarios.

**Expected output/deliverable:**
Working ChainForge installation for VCH/Windesheim students, customized with supply chain prompt templates, documentation/tutorials for common use cases.

---

## CURRENT STATUS (from GitHub)

**Repository:** https://github.com/Value-Chain-Hacking/ChainForge (Fork)
**Upstream Status:** Active (369 commits, open beta)
**Created:** July 25, 2024, last activity Nov 10, 2025

**Tech Stack:**
- TypeScript (91.1%), Python (5.2%), CSS (2.9%)
- ReactFlow (visual programming)
- Flask (backend)
- Docker support

**Key Features:**
- Query multiple LLMs simultaneously
- Systematic prompt variation testing
- Custom scoring functions
- Chat conversation template support
- Multi-turn dialogue testing
- Export results to spreadsheet
- Visual metrics comparison

**Supported Providers:**
OpenAI, Anthropic, Google (Gemini, PaLM2), HuggingFace, Ollama, Azure OpenAI, AlephAlpha, Amazon Bedrock

---

## NOTES FOR COMPLETION

**Key Decisions Needed:**
- [ ] Are we maintaining a fork or contributing upstream?
- [ ] What supply chain-specific customizations do we need?
- [ ] How will we provide API keys to students? (cost management)
- [ ] Do we host an instance or students run locally?
- [ ] What tutorials/templates will we create for supply chain use cases?

**Potential Customizations:**
- Pre-built prompt templates for supply chain data extraction
- Sample datasets (ESG reports, shipping docs, etc.)
- Tutorials for common VCH research tasks
- Cost tracking dashboard for API usage
- Integration with SupplyLens or other VCH projects

[TO FILL - Timeline, deployment plan, student training materials]
