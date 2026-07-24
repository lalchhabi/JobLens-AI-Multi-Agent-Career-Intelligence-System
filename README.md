
# 📌 JobLens-AI-Multi-Agent-Career-Intelligence-System

### Multi-Agent Job Search & Career Optimization System
JobLens AI is a production-oriented multi-agent career intelligence platform built with LangGraph, LangChain, FastAPI, and Large Language Models. It analyzes resumes against job descriptions using specialized AI agents that perform resume parsing, job understanding, deterministic skill gap analysis, interview preparation, market insights, and personalized learning roadmap generation. It demonstrates how agent workflows can be structured into production-ready AI applications.

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
* Job Description (text)

### Output:

* Skill extraction
* Resume profiling
* Job requirement analysis
* Skill gap report
* Interview questions
* Job recommendations
* Learning roadmap
* Personalized cover letter, application email, linkedin outreach message.

---

# 🧠 System Architecture

```
                                    ┌──────────────────────────────┐
                                    │          User (UI)           │
                                    │ Resume PDF + Job Description │
                                    └──────────────┬───────────────┘
                                                   │
                                                   ▼
                                  ┌─────────────────────────────────┐
                                  │     FastAPI REST API Layer      │
                                  │  (/analyze-stream endpoint)     │
                                  └─────────────────────────────────┘
                                                   │
                                                   ▼
                           ┌─────────────────────────────────────────────┐
                           │       LangGraph Workflow Orchestrator       │
                           │     Stateful Multi-Agent Execution Engine   │
                           └─────────────────────────────────────────────┘
                                                   │
        ┌──────────────────────────────────────────┼──────────────────────────────────────────┐
        │                                          │                                          │
        ▼                                          ▼                                          ▼
┌──────────────────────┐                 ┌──────────────────────┐                 ┌──────────────────────┐
│   PDF Parser Tool    │                 │   Resume Agent       │                 │    Job Agent         │
│  Extract Resume Text │                 │ Resume Understanding │                 │ Job Requirement      │
└──────────────────────┘                 └──────────────────────┘                 │ Extraction           │
        │                                          │                              └──────────────────────┘
        │                                          │
        └──────────────────────────────┬───────────┘
                                       ▼
                        ┌────────────────────────────────────┐
                        │      Structured Pydantic Models     │
                        │ ResumeSchema + JobSchema            │
                        └────────────────────────────────────┘
                                       │
                                       ▼
                     ┌────────────────────────────────────────────┐
                     │        Context Builder Service             │
                     │ Compresses Resume & Job Context            │
                     │ Removes Unused Fields                      │
                     │ Reduces LLM Token Usage                    │
                     └────────────────────────────────────────────┘
                                       │
                                       ▼
                          ┌───────────────────────────────┐
                          │      Gap Analysis Agent       │
                          │ Semantic Skill Matching       │
                          └───────────────────────────────┘
                                       │
                                       ▼
                    ┌─────────────────────────────────────────────┐
                    │ Deterministic Scoring Engine (Backend)      │
                    │ • Required Skill Score                      │
                    │ • Preferred Skill Score                     │
                    │ • Overall Match Score                       │
                    └─────────────────────────────────────────────┘
                                       │
        ┌────────────────┬─────────────┼─────────────┬────────────────┐
        ▼                ▼             ▼             ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────────┐
│ Interview      │ │ Market         │ │ Roadmap        │ │ Cover Letter       │
│ Agent          │ │ Agent          │ │ Agent          │ │ Agent              │
│ Personalized   │ │ Market         │ │ Learning       │ │ Cover Letter       │
│ Questions      │ │ Insights       │ │ Roadmap        │ │ Email              │
│                │ │ Job Search     │ │                │ │ LinkedIn Message   │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────────┘
        └────────────────┬─────────────┼─────────────┬────────────────┘
                         ▼
           ┌──────────────────────────────────────────────┐
           │ Streaming JSON Response                      │
           │ • Resume Analysis                            │
           │ • Job Analysis                               │
           │ • Gap Analysis                               │
           │ • Interview Questions                        │
           │ • Market Insights                            │
           │ • Learning Roadmap                           │
           │ • Cover Letter                               │
           │ • Application Email                          │
           │ • LinkedIn Message                           │
           └──────────────────────────────────────────────┘

```

# LangGraph Workflow

JobLens AI uses LangGraph to orchestrate the complete career intelligence pipeline.

```

                Start
                  │
                  ▼
                Parser
                  │
                  ▼
                Resume
                  │
                  ▼
                  Job
                  │
                  ▼
                  Gap
           ┌──────┼──────┐
           │      │      │
           ▼      ▼      ▼
 Cover Letter  Interview  Market
      │           │        │
      │           └──┐  ┌──┘
      │              ▼  ▼
      │          Roadmap
      │              │
      └──────┬───────┘
             ▼
            End

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
  "matched_required_skills": [],
  "missing_required_skills": [],
  "matched_preferred_skills": [],
  "missing_preferred_skills": [],
  "learning_recommendation": [],
  "match_score": {
      "overall_score": 82,
      "required_skill_score": 75,
      "preferred_skill_score": 100
  }
}
```

---

## 4. Interview Preparation Agent

Generates:

* HR questions
* Technical questions
* Project-based questions

---

## 5. Job Recommendation Agent 

Suggests similar roles based on:

* Resume embedding
* Skill profile

---

## 6. Learning Roadmap Agent 

Generates:

* 7–14 day structured learning plan
* Skill-based roadmap

### 6. Cover Letter Agent

Generates:

* Tailored cover letter
* Professional application email
* LinkedIn connection message

---

## 📨 Application Assistant

JobLens AI helps candidates prepare job applications by automatically generating:

- Personalized Cover Letter
- Professional Application Email
- LinkedIn Outreach Message

Each document is generated based on both the candidate's resume and the target job description, making every application more personalized and relevant.

---

# 🧪 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload-resume` | Uploads a resume PDF for processing. |
| POST | `/analyze-job` | Analyzes a job description and extracts structured requirements. |
| POST | `/analyze-stream` | Executes the complete LangGraph multi-agent workflow and streams results to the frontend in real time. |
---

# 💼 Live Job Search

JobLens AI includes a real-time job search feature that lets users explore current job openings without using the LLM. This keeps searches fast, reduces token usage, and always returns the latest opportunities from the job provider.

## Architecture

```
User
   │
   ▼
Select Country
   │
   ▼
Frontend (JavaScript)
   │
   ▼
FastAPI Endpoint
   │
   ▼
Adzuna Jobs API
   │
   ▼
Display Live Jobs
```

## Design
During the initial implementation, live job retrieval was integrated into the Market Agent using LangChain tool calling and a custom Tool Executor. While this successfully demonstrated agent-tool interaction, it was later replaced with a dedicated FastAPI endpoint for production use.

The feature was redesigned so that:

- Market Agent generates AI-powered market insights only.
- Live job search uses a dedicated FastAPI endpoint.
- Jobs are fetched directly from the Adzuna Jobs API.
- No LLM tokens are consumed during job searches.

This design provides:
- Faster response time
- Real-time job listings
- Lower infrastructure cost
- Better user experience

## Features

- Search AI jobs across multiple countries
- Real-time job listings
- Job title, company, location, salary (if available)
- Posted date
- Short job description
- Direct Apply link

## Supported Countries

Australia • Austria • Belgium • Brazil • Canada • France • Germany • India • Italy • Mexico • Netherlands • New Zealand • Poland • Singapore • South Africa • Spain • Switzerland • United Kingdom • United States



# 🧰 Tech Stack

## Backend

- Python 3.12
- FastAPI
- Pydantic v2
- Uvicorn

## AI & LLM Orchestration

- LangChain
- LangGraph
- Groq API
- Prompt Engineering
- Structured Output Parsing

## AI Architecture

- Multi-Agent Architecture
- Stateful Workflow Orchestration
- Context Builder (Token Optimization)
- Deterministic Scoring Engine
- Streaming Responses (SSE)

## Document Processing

- PyMuPDF (fitz)

## Data Validation

- Pydantic Schemas
- JSON Structured Outputs

## Utilities

- DuckDuckGo Search (DDGS)
- Python Logging

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript

## Development

- Git
- GitHub
- Virtual Environment (venv)

# Deployment

## Live Demo

- **Render (Production Demo):**
  https://joblens-ai-multi-agent-career.onrender.com

## Deployment & DevOps
- Docker
- Docker Compose
- GitHub Actions (CI/CD)
- Render
- AWS EC2

# ✨ Key Features

- Multi-agent AI workflow powered by LangGraph
- Resume parsing from PDF documents
- Structured job description analysis
- Deterministic resume-job match scoring
- Semantic skill gap analysis
- AI-generated interview questions
- Personalized learning roadmap
- Market insights and job recommendations
- Real-time streaming analysis with FastAPI
- Structured JSON outputs using Pydantic
- Generate personalized cover letter, application email, linkedin outreach message
- Live Job Search across multiple countries
- Dockerized deployment
- GitHub Actions CI pipeline
---

# 🧱 Project Structure

```
joblens_AI/
│
│
├── agents/
│   ├── resume_agent.py
│   ├── job_agent.py
│   ├── gap_agent.py
│   ├── interview_agent.py
│   ├── market_agent.py
│   ├── roadmap_agent.py
│  
├── api/
│   ├── routes.py
│
├── data/
│   ├── jobs
│   ├── results 
│   ├── resume
│
├── graph/
│   ├── nodes.py   
│   ├── state.py 
│   ├── workflow.py 
│ 
├── app/
│   ├── main.py
│
├── graph/
│   ├── nodes.py   
│   ├── state.py 
│   ├── workflow.py 
│
├── prompts/
│   ├── gap_prompt.py
│   ├── interview_prompt.py
│   ├── job_prompt.py
│   ├── market_prompt.py
│   ├── resume_prompt.py
│   ├── roadmap_prompt.py
│
├── schemas/
│   ├── career_analysis_schema.py
│   ├── career_response_schema.py
│   ├── gap_schema.py
│   ├── interview_schema.py
│   ├── job_schema.py
│   ├── market_schema.py
│   ├── match_score_schema.py
│   ├── resume_schema.py
│   ├── roadmap_schema.py
│ 
├── services/
│   ├── career_analysis_service.py
│   ├── context_builder.py
│   ├── llm_service.py
│   ├── scoring_engine.py
│   ├── adzuna_job_service.py
│
├── tests/
│
├── tools/
│   ├── pdf_parser.py
│   ├── adzuno_job_search_tool.py
│   ├── tool_executor.py
│ 
ui/
├── static/
│   ├── css/
│   │   ├── main.css
│   │   ├── layout.css
│   │   ├── navigation.css
│   │   ├── cards.css
│   │   ├── forms.css
│   │   ├── buttons.css
│   │   ├── result.css
│   │   └── animation.css
│   │
│   └── js/
│       ├── app.js
│       ├── api.js
│       ├── navigation.js
│       ├── state.js
│       ├── ui.js
│       └── renderers/
│           ├── resume.js
│           ├── gap.js
│           ├── interview.js
│           ├── roadmap.js
│           ├── market.js
│           └── coverletter.js
├── templates/
│        ├── index.html
│ 
├── uploads/
│ 
├── utils/
│   ├── llm_retry.py
│   ├── logger.py 
│   ├── save_results.py
│   ├── validators.py
│
├── data/
│   ├── jobs
│   ├── results 
│   ├── resume
│
│
├── requirements.txt
└── README.md
├── .dockerignore
└── .gitignore
├── Dockerfile
└── docker-compose.yml
```

---

# ⚙️ Installation Setup

## 1. Clone Repository

```bash
git clone https://github.com/lalchhabi/JobLens-AI-Multi-Agent-Career-Intelligence-System
cd JobLens-AI-Multi-Agent-Career-Intelligence-System
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
HUGGINGFACEHUB_ACCESS_TOKEN=your_token
GROQ_API_KEY=your_key
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key
```

---

## 5. Run Backend

```bash
uvicorn app.main:app --reload
```

---

# 🚀 Deployment

## Live Demo

**Render (Production Demo)**

https://joblens-ai-multi-agent-career.onrender.com

## Deployment Platforms

### Render

- Dockerized deployment
- Automatic deployment from GitHub
- GitHub Actions CI/CD
- HTTPS-enabled public demo

### AWS EC2

- Ubuntu EC2
- Docker
- Docker Compose
- FastAPI + Uvicorn
- Environment variables managed through `.env`
- Public deployment via EC2 Security Groups

## Run Locally

```bash
docker compose up --build

```

---

# 📈 Future Improvements
- **Match Score Optimization** – Improve resume–job matching using semantic similarity, skill normalization, and weighted scoring for more accurate results.
- **Resume Optimization** – Generate ATS-friendly resume suggestions tailored to specific job descriptions using RAG and LLMs.
- **Conversation Memory** – Persist user career history and previous analyses to provide personalized long-term guidance.
- **Interactive AI Career Coach** – Enable multi-turn conversations for resume reviews, interview preparation, and career planning.
- **Multi-LLM Routing** – Dynamically route tasks to the most suitable model (Groq, OpenAI, Gemini, etc.) based on latency, cost, and capability.


