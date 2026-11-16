# CampusMate – GenAI‑Powered Study Assistant

## Overview
CampusMate is a lightweight web app that helps students **ask questions**, **learn concepts**, **summarise text**, and **generate quizzes** using the Groq LLM API. It runs locally with Streamlit and can be deployed to Streamlit Community Cloud.

## Features
| Feature | Description |
| ------- | ----------- |
| **AI Chat** | Conversational Q&A with session‑based memory (only for the current session). |
| **Study Mode** | Explanations tuned for *Beginner*, *Intermediate* or *Advanced* levels. |
| **Text Summarizer** | Turns any chunk of text into a short summary. |
| **Quiz Generator** | Produces multiple‑choice quizzes (question, 4 options, answer, explanation). |

## Tech Stack
- **Python 3.11+**
- **Streamlit** – UI framework
- **Groq SDK** – LLM inference (e.g., `llama3-70b-8192`)
- **python‑dotenv** – local `.env` handling

## Architecture
```mermaid
flowchart TD
    A[Streamlit Front‑end] -->|HTTP requests| B[app.py (router & UI)]
    B --> C[assistant.GroqAssistant]
    C --> D[Groq API]
    B -->|calls| E[modules/study_mode.py]
    B -->|calls| F[modules/summarizer.py]
    B -->|calls| G[modules/quiz_generator.py]
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## Project Structure
```
campusmate/
│
├─ app.py                     # Streamlit UI & navigation
├─ assistant.py               # Groq client wrapper
├─ config.py                  # .env loading & validation
├─ prompts.py                 # System prompts for each feature
│
├─ modules/
│   ├─ __init__.py
│   ├─ study_mode.py
│   ├─ summarizer.py
│   └─ quiz_generator.py
│
├─ tests/
│   └─ test_prompts.py        # Unit tests for prompts
│
├─ .env.example               # Template env file
├─ .gitignore
├─ requirements.txt
└─ README.md
```

## Setup & Installation
```bash
# Clone the repo
git clone https://github.com/paliwalketan05/Study_Virtual_Assistant.git
cd Study_Virtual_Assistant

# Create a virtual environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Configure credentials
cp .env.example .env
# Edit .env and paste your Groq API key
```

## Running the App Locally
```bash
streamlit run app.py
```
Open the displayed URL (usually http://localhost:8501) in a browser.

## Testing
```bash
pytest -v
```
All tests should pass (`4 passed`).

## Deployment to Streamlit Community Cloud
1. Push the repository to GitHub.
2. In Streamlit Cloud, create a new app pointing to `app.py`.
3. Add **Secrets** → `GROQ_API_KEY` (and optionally `GROQ_MODEL`).
4. Deploy – Streamlit installs `requirements.txt` automatically.

## Future Improvements
- Persistent conversation storage (database).
- Retrieval‑augmented generation (RAG) with PDFs or course material.
- Voice input & text‑to‑speech.
- Multi‑user authentication and dashboard.

---
*Created for the campus project deadline. Happy studying!*