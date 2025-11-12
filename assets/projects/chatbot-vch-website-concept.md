# AI Project Concept Template for Windesheim/VCH

**All projects follow Agile principles with iterative development, regular sprint cycles, and continuous stakeholder feedback.**

---

## PROJECT CONCEPT

### Basic Information
**Project Title:** Chatbot for VCH Website

**Project Slug:** `chatbot-vch-website`

**Concept Status:** brainstorm

**Category:** student-project / internal-tool

**GitHub Repository:** [TO FILL - Does this exist yet?]

---

## THE 3 MINUTE RULE PITCH

### 1. What is it?
An AI chatbot on the VCH website that answers questions about projects, research, courses, and supply chain topics.

### 2. How does it work?
[TO FILL - RAG (Retrieval-Augmented Generation) using VCH website content + project docs? Fine-tuned model? Which LLM provider?]

### 3. Are you sure?
Chatbots for educational websites are proven. The challenge is making it knowledgeable about VCH-specific content and keeping it updated.

### 4. Can you do it?
[TO FILL - Team has LLM experience? Infrastructure for hosting?]

### 5. What's the value?**
Visitors can ask questions 24/7 about VCH projects, research areas, how to collaborate, etc. Reduces email load. Helps potential students/partners learn about VCH.

### 6. Are there any risks?
- Chatbot gives incorrect information about VCH
- API costs for LLM usage
- Needs constant updating as VCH content changes
- May answer questions about sensitive topics incorrectly
- Maintenance burden

---

### The Problem

**What problem does this solve?**
People have questions about VCH projects, collaboration opportunities, research areas, but have to dig through the website or send emails. Response time is slow.

**Who has this problem?**
- Potential student collaborators
- Partner companies exploring collaboration
- Researchers looking for VCH expertise
- General visitors wanting to understand VCH

---

### The AI Solution

**What AI/ML technique would you use?**
- RAG (Retrieval-Augmented Generation): Embed VCH content, retrieve relevant docs, use LLM to answer
- Possibly fine-tuning on VCH-specific Q&A pairs
- LLM: OpenAI GPT, Anthropic Claude, or open-source (Llama, Mistral)

**What data would you need?**
- All VCH website content
- Project descriptions and documentation
- Research publications
- FAQ content
- Course descriptions
- Common questions from emails/Discord
- Data availability: We have this, just need to structure it

**Expected output/deliverable:**
Chat widget embedded on VCH website, responds to questions about VCH projects and supply chain research, links to relevant pages.

---

## FEASIBILITY CHECK

**Technical Difficulty:** Medium

**Required Skills:**
- LLM/RAG implementation (LangChain, LlamaIndex)
- Frontend integration (JavaScript chat widget)
- Backend API (Flask/FastAPI)
- Vector database (Pinecone, Weaviate, or pgvector)
- Prompt engineering

**Resources Needed:**
- Computing: Cloud hosting for API, vector database
- Data: VCH website scraping/export, project docs
- People: 1-2 students with AI experience
- Budget: LLM API costs (€50-200/month depending on usage), hosting (€20-50/month)

---

## TIMELINE & MILESTONES

**Total Estimated Time:** 3-4 months

**Suggested Phases:**
1. Content collection and embedding (2 weeks)
2. RAG pipeline development (3 weeks)
3. Chat widget frontend (2 weeks)
4. Testing and refinement (2 weeks)
5. Deployment and monitoring (1 week)

[TO FILL - Detailed sprint breakdown]

---

## STRATEGIC FIT

**Student Learning Value:**
High - Students learn RAG, LLM deployment, prompt engineering, practical AI application.

**Reusability:**
High - Could be template for other educational institution chatbots.

**VCH Goal Alignment:**
Improves accessibility of VCH research, helps onboard new collaborators, demonstrates AI capability.

---

## SUCCESS CRITERIA

**Minimum Viable Product (MVP):**
Chatbot can answer 10 common questions about VCH accurately (who are you, what projects, how to collaborate, etc.)

**Success Metrics:**
- Accuracy: >85% of answers are correct and helpful
- Usage: 50+ questions per month
- Reduces email inquiries by 20%
- User feedback: >70% find it helpful

**Stretch Goals:**
- Multilingual support (Dutch + English)
- Integration with Discord bot
- Can answer technical supply chain questions, not just VCH info
- Conversational memory (remembers context within session)

---

## NOTES FOR COMPLETION

**Key Decisions Needed:**
- [ ] Which LLM provider? (OpenAI cheapest, Claude best quality, open-source no API costs)
- [ ] Where to host? (Vercel, AWS, university servers?)
- [ ] What content sources to include beyond website?
- [ ] How to handle questions it can't answer?
- [ ] Privacy considerations for chat logs?

**Similar Projects to Reference:**
- Educational chatbots (university websites)
- Documentation chatbots (Cursor, GitHub Copilot Docs)
- RAG implementations (LangChain tutorials)

[TO FILL - Full timeline, team assignments, tech stack decisions, budget approval]
