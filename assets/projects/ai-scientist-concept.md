# AI Project Concept Template for Windesheim/VCH

**All projects follow Agile principles with iterative development, regular sprint cycles, and continuous stakeholder feedback.**

---

## PROJECT CONCEPT

### Basic Information
**Project Title:** AI Scientist (VCH Adaptation)

**Project Slug:** `ai-scientist`

**Concept Status:** brainstorm

**Category:** research / student-project

**Upstream Repository:** https://github.com/SakanaAI/AI-Scientist

---

## THE 3 MINUTE RULE PITCH

### 1. What is it?
A system where AI models autonomously generate research papers from idea to experiments to final writeup, which we're adapting for supply chain research topics.

### 2. How does it work?
You give it a research template (like "analyze supply chain disruption patterns"), and the AI generates hypotheses, runs experiments, analyzes results, searches literature, writes a complete paper with citations, and even reviews it using another AI.

### 3. Are you sure?
It's a proven open-source project from Sakana AI (11.7k GitHub stars). The question is whether we can adapt it from ML research topics to supply chain research domains.

### 4. Can you do it?
[TO FILL - This requires significant compute (GPUs), LLM API access, and expertise to create supply chain research templates]

### 5. What's the value?
Could massively accelerate supply chain research idea exploration. Students could generate literature reviews automatically. Test hypotheses faster. Identify research gaps. However, needs human validation - AI can generate papers but quality varies.

### 6. Are there any risks?
- Computational costs are high (GPU + LLM APIs)
- Generated papers need expert validation for accuracy
- May produce plausible-sounding but incorrect research
- Ethical questions about AI-generated academic work
- Extremely complex to customize for supply chain domain

---

### The Problem

**What problem does this solve?**
Research is slow. Literature reviews take weeks. Running experiments and writing papers takes months. If AI can explore idea spaces automatically, researchers could test many hypotheses quickly and focus human effort on the promising ones.

**Who has this problem?**
Researchers and students who want to explore supply chain questions but lack time for extensive experimentation.

**How big is the problem?**
Academic research has long cycles. Speeding up initial exploration could increase research output significantly.

---

### The AI Solution

**What AI/ML technique would you use?**
- LLMs (GPT-4, Claude, DeepSeek) for idea generation, writing, literature search
- Automated experimentation frameworks
- LaTeX generation for paper formatting
- AI-based peer review

**What data would you need?**
- Research templates adapted for supply chain topics
- Access to supply chain datasets for experiments
- Literature databases (Semantic Scholar, arXiv)
- Compute: NVIDIA GPUs, cloud credits
- Data availability: Need to create supply chain-specific templates

**Expected output/deliverable:**
Automated research paper generation system customized for supply chain topics. Templates for common supply chain research questions.

---

## FEASIBILITY CHECK

**Technical Difficulty:** Very Hard

**Required Skills:**
- Deep ML/AI expertise
- Research methodology
- Supply chain domain knowledge
- GPU infrastructure management
- Python, PyTorch, LaTeX
- LLM prompt engineering

**Resources Needed:**
- Computing: **NVIDIA GPUs required**, significant cloud compute budget
- Data: Supply chain datasets, literature database access
- People: ML researcher + supply chain expert + student testers
- Budget: High - GPU costs, LLM API costs (could be €1000s/month)

---

## CURRENT STATUS (from Upstream)

**Repository:** https://github.com/SakanaAI/AI-Scientist
**Status:** Active (11.7k stars, 89 issues, 21 PRs)
**Tech Stack:**
- Python 3.11
- PyTorch + CUDA/NVIDIA GPU
- LaTeX (texlive)
- Multiple LLM APIs (OpenAI, Anthropic, DeepSeek, Google)
- Semantic Scholar API

**Templates Provided:**
- NanoGPT (language modeling)
- 2D Diffusion (image generation)
- Grokking (ML phenomenon research)

**Key Features:**
- Fully automatic scientific discovery
- Literature search and citations
- LLM-based peer review
- Multi-model support
- Community template framework

---

## STRATEGIC FIT

**How does this align with VCH goals?**
Potentially accelerates supply chain research, but very experimental. High risk, high reward.

**Student Learning Value:**
Very high if successful - exposes students to cutting-edge AI research. But steep learning curve.

**Reusability:**
If we create supply chain templates, they could be reused across many research questions.

---

## RISKS & UNKNOWNS

**What could go wrong?**
- May not adapt well to supply chain domain (templates are for ML topics)
- Costs spiral out of control
- Generated research quality is poor
- Ethical concerns about AI-generated academic work
- Too complex for student projects

**Deal-breakers:**
- Cannot secure GPU access
- API costs exceed €500/month
- Cannot create working supply chain research templates
- University ethics board rejects AI-generated research

---

## DECISION

**Recommendation:** [TO FILL]
- This is very experimental and resource-intensive
- Consider starting with simpler tools (ChainForge for prompts, LLMs for literature review)
- If pursuing, start tiny: one very narrow supply chain template as proof of concept
- Budget €2000+ for initial experiments

---

## NOTES FOR COMPLETION

**This project needs serious evaluation before proceeding:**
- [ ] Calculate realistic cost estimates for GPU + API usage
- [ ] Assess if supply chain research fits the AI Scientist template model
- [ ] Consider if simpler LLM tools (ChatGPT, Claude) already meet needs
- [ ] Determine if there's a specific research question worth testing
- [ ] Review ethical implications with Windesheim research ethics board

[TO FILL ONLY IF APPROVED - Timeline, team, budget, specific supply chain research template ideas]
