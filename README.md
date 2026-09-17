# HR Copilot — Agentic AI-Powered Human Resource Assistant

HR Copilot is an Agentic AI capstone project for practical HR operations. It combines an LLM agent with specialized tools, structured employee records, HR-policy retrieval, team/skill matching, analytics, safety guardrails, and a Streamlit dashboard.

## Features
- Natural-language HR assistant
- LangGraph/LangChain ReAct-style tool selection
- Employee search and detailed profiles
- Skill matching and project-team recommendations
- Leave balance lookup
- HR policy retrieval / lightweight local RAG
- Workforce analytics dashboard
- Agent execution trace in the UI
- Human-in-the-loop safety rule for consequential HR decisions
- SQLite local database with synthetic employee data
- Demo mode works without an API key
- Docker + GitHub Actions + pytest

## Project Structure
```
HR_Copilot_Complete/
├── agent/
│   ├── tools.py
│   └── workflow.py
├── database/
│   ├── db_connection.py
│   └── seed.py
├── data/
│   ├── employees.csv
│   └── hr_policies.txt
├── docs/ARCHITECTURE.md
├── tests/test_tools.py
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

## Windows Setup
```bat
cd /d "C:\path\to\HR_Copilot_Complete"
conda create -n hr_copilot python=3.11 -y
conda activate hr_copilot
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```
Open http://localhost:8501.

The application works in demo mode without an API key. For the full LLM agent, place your key in `.env` as `OPENAI_API_KEY=...`.

## Test Prompts
- Show employees with Python skills.
- Build a team for a Python machine-learning project.
- What is the annual leave policy?
- Show workforce analytics.
- Find available employees with LLM and RAG experience.

## Tests
```bash
pytest -q
```

## Docker
```bash
docker compose up --build
```

## Safety
The system does not autonomously make hiring, firing, disciplinary, promotion, or compensation decisions. It can retrieve evidence and assist an authorized HR professional, while final consequential decisions require human review.

## Demo Video Flow
1. Explain the HR operations problem.
2. Show the architecture diagram.
3. Demonstrate employee search.
4. Ask for a skill-based project team.
5. Ask an HR-policy question.
6. Show HR analytics and the agent execution trace.
7. Explain safety/human approval and deployment.
