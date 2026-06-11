
# 📌 JobLens-AI-Multi-Agent-Career-Intelligence-System

### Multi-Agent Job Search & Career Optimization System

An **agentic AI system** that helps users:

* Analyze job descriptions
* Extract resume insights
* Perform skill gap analysis
* Generate interview questions
* Recommend jobs
* Build personalized learning roadmaps

Built using **LangGraph / LangChain, FastAPI, and LLM tool-calling agents**

---

# 🚀 Problem Statement

Job seekers spend significant time:

* Reading job descriptions
* Tailoring resumes
* Identifying missing skills
* Preparing interviews
* Searching relevant roles

This project automates the entire workflow using **multi-agent AI orchestration**.

---

# 🎯 Solution Overview

This system acts as a **personal AI career coach + recruiter assistant**:

### Input:

* Resume (PDF)
* Job Description (text / URL)

### Output:

* Skill extraction
* Resume profiling
* Job requirement analysis
* Skill gap report
* Interview questions
* Job recommendations
* Learning roadmap

---

# 🧠 System Architecture

```
                 ┌─────────────────────┐
                 │   User Input (UI)   │
                 │ Resume + Job Post   │
                 └─────────┬───────────┘
                           │
                           ▼
        ┌──────────────────────────────────┐
        │        Orchestrator (LangGraph)  │
        └──────────────────────────────────┘
             │          │          │
             ▼          ▼          ▼

 ┌────────────────┐ ┌────────────────┐ ┌──────────────────┐
 │ Resume Agent   │ │ Job Agent      │ │ Tool Agents      │
 │ (Parser)       │ │ (Extractor)    │ │ GitHub / Web     │
 └────────────────┘ └────────────────┘ └──────────────────┘
             │          │
             └────┬─────┘
                  ▼
        ┌───────────────────────┐
        │ Gap Analysis Agent    │
        └───────────────────────┘
                  ▼
        ┌───────────────────────┐
        │ Output Generator      │
        │ (Roadmap + Q/A + Fit) │
        └───────────────────────┘
```

---

# 🤖 Agents Design

## 1. Resume Analyzer Agent

**Role:** Extract structured profile from resume

**Input:**

* PDF resume

**Output:**

```json
{
  "skills": [],
  "projects": [],
  "experience": [],
  "education": []
}
```

---

## 2. Job Description Analyzer Agent

**Role:** Extract structured job requirements

**Input:**

* Job post text / URL

**Output:**

```json
{
  "required_skills": [],
  "preferred_skills": [],
  "experience_level": "",
  "responsibilities": []
}
```

---

## 3. Gap Analysis Agent 🔥 (Core Agent)

**Role:** Compare resume vs job description

**Output:**

```json
{
  "match_score": 78,
  "missing_skills": [],
  "strong_skills": [],
  "recommendations": []
}
```

---

## 4. Interview Preparation Agent

Generates:

* HR questions
* Technical questions
* Project-based questions

---

## 5. Job Recommendation Agent (Optional Phase 2)

Suggests similar roles based on:

* Resume embedding
* Skill profile

---

## 6. Learning Roadmap Agent (Optional Phase 2)

Generates:

* 7–14 day structured learning plan
* Skill-based roadmap

---

# 🧰 Tech Stack

## Backend

* Python 3.10+
* FastAPI
* Pydantic

## AI / Agents

* LangChain OR LangGraph (preferred)
* OpenAI / Groq / Gemini API

## Document Processing

* PyMuPDF (fitz)
* pdfplumber

## Vector DB (optional)

* FAISS

## Tools Integration

* GitHub API
* Web scraping (BeautifulSoup / Playwright)

## Frontend

* React OR simple HTML/CSS/JS dashboard

---

# 🧱 Project Structure

```
ai-career-copilot/
│
├── app/
│   ├── main.py
│   ├── config.py
│
├── agents/
│   ├── resume_agent.py
│   ├── job_agent.py
│   ├── gap_agent.py
│   ├── interview_agent.py
│
├── tools/
│   ├── pdf_parser.py
│   ├── github_tool.py
│   ├── web_tool.py
│
├── graph/
│   ├── workflow.py   # LangGraph orchestration
│
├── data/
│
├── frontend/
│   ├── index.html
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-career-copilot.git
cd ai-career-copilot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
GITHUB_TOKEN=your_token
```

---

## 5. Run Backend

```bash
uvicorn app.main:app --reload
```

---

# 🧪 API Endpoints (MVP)

## Upload Resume

```
POST /upload-resume
```

## Analyze Job

```
POST /analyze-job
```

## Run Full Pipeline

```
POST /analyze
```

Response:

```json
{
  "resume_analysis": {},
  "job_analysis": {},
  "gap_analysis": {},
  "interview_analysis": []
}
```

---

# 🧭 Development Roadmap (10–15 Days)

## 🟢 Phase 1: Core System (Days 1–6)

### Day 1–2

* Setup FastAPI
* Setup project structure
* Setup LLM connection

### Day 3–4

* Resume parser agent
* Job analyzer agent

### Day 5–6

* Gap analysis agent (core logic)

---

## 🟡 Phase 2: Intelligence Layer (Days 7–10)

* Interview question generator
* Structured JSON outputs
* Prompt optimization
* Basic UI

---

## 🔵 Phase 3: Agentic Expansion (Days 11–13)

* LangGraph orchestration
* GitHub tool integration
* Web scraping tool

---

## 🔴 Phase 4: Polish & Deployment (Days 14–15)

* UI improvement
* Logging
* Error handling
* Deployment (Render / Railway / HuggingFace Spaces)

---

# 📈 Future Improvements

* Real-time LinkedIn job ingestion
* Memory-based career tracking
* RAG-based resume improvement system
* Personalized AI recruiter chatbot
* MCP server expansion (filesystem, browser automation)



