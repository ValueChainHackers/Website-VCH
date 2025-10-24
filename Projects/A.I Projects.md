```markdown
# 🤖 Active AI Projects — Christiaan Verhoef / Value Chain Hackers

A curated overview of your **current AI-related projects**, their **purpose**, and **links** to repositories or live systems.  
These reflect your ongoing work across the **Value Chain Hackers**, **ClearRoots**, and **Windesheim AI Lab** ecosystems.

---

## 1. 🧠 **AI Sandbox**
**Link:** [https://aisandbox1.ixworx.nl](https://aisandbox1.ixworx.nl)  
**Repo:** _Private (internal deployment)_  
**Description:**  
Self-hosted research and automation environment integrating **OpenWebUI**, **n8n**, **Flowise**, **Supabase**, **Qdrant**, and **Traefik**.  
Built for local-first, privacy-friendly AI workflows and reproducible research pipelines at Windesheim and VCH.

> 💡 *Purpose:* Enable students and researchers to build, test, and deploy AI workflows without external dependencies.

---

## 2. 🪶 **ClearRoots**
**Repo:** [https://github.com/Value-Chain-Hackers/ClearRoots](https://github.com/Value-Chain-Hackers/ClearRoots)  
**Description:**  
An open-source AI and blockchain compliance tool for **sustainability reporting** under **EU CSRD, CSDDD, and EUDR** regulations.  
Combines **automation**, **data assurance**, and **traceability** for smallholder farmers, importers, and auditors.

> 💡 *Purpose:* Build trust and efficiency in green value chains through verifiable AI-assisted documentation.

---

## 3. ⚙️ **AI Reporting Automation**
**Repo:** [https://github.com/Value-Chain-Hackers/Reporting](https://github.com/Value-Chain-Hackers/Reporting)  
**Description:**  
An automated Quarto-based system that generates weekly and mini reports (e.g., *AI Lab Infrastructure & Strategy Reports*).  
Integrates n8n, Supabase, and Markdown templates for dynamic report creation and publication to GitHub.

> 💡 *Purpose:* Streamline research reporting and ensure all deliverables remain reproducible and version-controlled.

---

## 4. 🧩 **Knopenkoning**
**Repo:** _In development (internal graph prototype)_  
**Description:**  
A **forensic supply chain mapping tool** powered by **Apache AGE**, **pgvector**, and **OpenWebUI**.  
Designed to help visualize relationships, risks, and resilience patterns within global supply chains.

> 💡 *Purpose:* Turn complex supply chain data into actionable insights using AI-driven graph reasoning.

---

## 5. 🔄 **AI Integration Pipelines**
**Repo:** _Part of internal `n8n` and `Flowise` setup_  
**Description:**  
A set of modular pipelines connecting:
- OpenWebUI prompts → Supabase logging  
- Formbricks survey data → Quarto dashboards  
- Qdrant embeddings → Semantic search and retrieval  
- Langfuse → Trace monitoring  

> 💡 *Purpose:* Unify data flow between AI tools and research outputs for reproducible automation.

---

## 6. 🧰 **AI for Research Workshop**
**Repo:** _Curriculum under development_  
**Description:**  
Training material and live examples teaching researchers how to use **LLMs, Jupyter, RStudio, Quarto, and n8n** effectively.  
Built using the **Conscious Competence learning model**, developed at Windesheim.

> 💡 *Purpose:* Make AI accessible to non-technical researchers through hands-on, open-source lessons.

---

## 7. 🧬 **NextGen Resilience (AI-Augmented SCF Research)**
**Repo:** _Internal (Windesheim Supply Chain Finance project)_  
**Description:**  
AI-assisted research framework using Quarto and R to analyze the relationship between **financial resilience** and **supply chain performance**.  
Includes automated resilience scoring and radar chart generation.

> 💡 *Purpose:* Support SCF researchers in modeling and visualizing financial resilience with AI-enhanced tools.

---

## 8. 🌿 **Li-Monti Maps**
**Repo:** _Planned under VCH & VIRIDIS partnership_  
**Description:**  
AI-driven mapping system for **battery recycling and lithium supply chains**, aligned with **ClearRoots** principles.  
Integrates graph reasoning, sustainability data, and compliance reporting.

> 💡 *Purpose:* Build transparent, data-driven insights into the circular economy of battery materials.

---

## 🧾 Summary Table

# 🤖 Value Chain Hackers — AI Projects & Concept Portfolio

| # | Project / Concept | Link | Description | Core Focus | Tech Stack / Tools | Status |
|---|--------------------|------|--------------|-------------|--------------------|---------|
| **1** | **AI Sandbox** | [https://aisandbox1.ixworx.nl](https://aisandbox1.ixworx.nl) | Self-hosted AI and automation ecosystem integrating OpenWebUI, n8n, Supabase, Qdrant, and Traefik for reproducible research. | Local-first AI infrastructure | Docker, Traefik, Supabase, Flowise, Langfuse, Redis | 🟢 Active |
| **2** | **ClearRoots** | [github.com/Value-Chain-Hackers/ClearRoots](https://github.com/Value-Chain-Hackers/ClearRoots) | AI + blockchain platform for EU sustainability compliance (CSRD, CSDDD, EUDR). Automates reporting and traceability. | Compliance automation & assurance | n8n, Supabase, Blockchain APIs, Quarto, LangChain | 🟢 Active |
| **3** | **Reporting Automation** | [github.com/Value-Chain-Hackers/Reporting](https://github.com/Value-Chain-Hackers/Reporting) | Automated Quarto pipelines that generate weekly and mini reports for the AI Lab (e.g., Infrastructure & Strategy). | AI-driven research reporting | Quarto, n8n, Supabase, Markdown, GitHub Actions | 🟢 Active |
| **4** | **Knopenkoning** | _Internal Prototype_ | Forensic supply chain mapping system using AI graph reasoning to uncover hidden relationships. | Graph reasoning & network forensics | Apache AGE, pgVector, OpenWebUI, Qdrant | 🟡 In Development |
| **5** | **AI Integration Pipelines** | _Internal_ | Unified automation layer connecting n8n, Flowise, Supabase, Qdrant, and Langfuse to streamline research dataflows. | AI orchestration backbone | n8n, Flowise, Supabase, Langfuse | 🟢 Active |
| **6** | **AI for Research Workshop** | _Windesheim Curriculum_ | Training program teaching LLM-based research methods with RStudio, Jupyter, and local AI models. | Education & AI adoption | Jupyter, RStudio, OpenWebUI, Quarto | 🟢 Active |
| **7** | **NextGen Resilience** | _Windesheim Internal_ | AI-enhanced Supply Chain Finance (SCF) analytics linking financial resilience to performance. | AI for SCF research | R, Python, Quarto, Supabase | 🟡 In Progress |
| **8** | **Li-Monti Maps** | _Planned (VIRIDIS Partnership)_ | AI-driven mapping of battery and lithium recycling chains; links with ClearRoots for compliance data. | Sustainable supply chain intelligence | Graph AI, Qdrant, Flowise, Supabase | 🔵 Planned |
| **9** | **AI Lab Infrastructure Docs** | [github.com/Value-Chain-Hackers/AI-Sandbox](https://github.com/Value-Chain-Hackers/AI-Sandbox) | Documentation hub for AI Lab deployment, routing, and architecture standards. | Infrastructure documentation | Quarto, Markdown, YAML | 🟢 Active |
| **10** | **PocketCFO** | _Draft Business Case_ | AI-powered financial companion for SMEs — combines forecasting, ESG scoring, and scenario simulation. | AI for finance & SME compliance | LangChain, n8n, Supabase, Streamlit (concept) | 🟣 Concept |
| **11** | **Goodboek (AI Ledger)** | _Concept_ | AI-assisted D&D-style ledger system for creative or educational project tracking. | Game-based learning + AI journaling | Python, LangChain, Quarto | 🟣 Concept |
| **12** | **Archon / AI Scientist** | _Experimental Concept_ | Autonomous agent concept that generates, validates, and documents research ideas automatically. | Self-directed AI research | LLM pipelines, Supabase, Langfuse | 🟣 Concept |
| **13** | **Beer Game 2.0 (AI Version)** | _In Planning_ | AI-assisted simulation to teach supply chain dynamics and forecasting through adaptive difficulty and analytics. | Game-based learning in SCF | Quarto, R, Python, OpenWebUI | 🔵 Planned |
| **14** | **GreenChainWorks** | _Concept_ | Framework for AI-driven sustainability evaluation and scoring for SMEs across green supply chains. | ESG intelligence & decision support | LangChain, Supabase, n8n | 🟣 Concept |
| **15** | **Reusable KYC** | _Idea_ | AI-supported identity & compliance verification across decentralized ecosystems (linking with Tonomy). | AI for governance & trust | Blockchain + NLP models | 🟣 Concept |
| **16** | **SupplyLens** | _Concept_ | AI-powered knowledge engine for mapping and querying supply chain research and sustainability data. | Research graph intelligence | Qdrant, LangChain, FastAPI | 🟣 Concept |
| **17** | **AI-Native EDRM Implementation** | _Windesheim Project_ | Research on making data pipelines reproducible using AI-guided metadata and the Enterprise Data Reference Model. | Reproducible research workflows | Quarto, R, Supabase, n8n | 🟡 In Progress |
| **18** | **AI Agent Observatory** | _Idea_ | Local experiment to benchmark, compare, and visualize the behavior of autonomous AI agents in the sandbox. | AI observability & evaluation | Langfuse, Qdrant, Streamlit | 🟣 Concept |

---

**Legend:**  
🟢 Active 🟡 In Development 🔵 Planned 🟣 Concept / Idea  

---

---
```
