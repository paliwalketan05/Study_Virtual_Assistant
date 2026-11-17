# CampusMate – GenAI‑Powered Study Assistant

## 📖 Overview
**CampusMate** is a lightweight, Streamlit‑based web application that acts as an AI‑powered study companion for college and university students. Using the **Groq** large‑language‑model API, it can:

- Answer academic questions in a conversational manner.
- Explain concepts at *Beginner*, *Intermediate* or *Advanced* levels.
- Summarise arbitrary text into a concise paragraph.
- Generate multiple‑choice quizzes with explanations.

All interactions happen in a single session – the assistant remembers the conversation while the app is open, but no data is persisted to disk, keeping the system simple and privacy‑friendly.

---

## ✨ Features
| Feature | What it does | UI location |
|---------|---------------|-------------|
| **AI Chat** | Natural‑language Q&A with context‑aware follow‑ups. | Sidebar → *AI Chat* |
| **Study Mode** | Tailored explanations for a chosen difficulty level. | Sidebar → *Study Mode* |
| **Text Summariser** | Turns a paragraph (or longer) into a 2‑3 sentence summary. | Sidebar → *Text Summarizer* |
| **Quiz Generator** | Generates 5 MCQs (configurable) on a given topic, with answer keys and short explanations. | Sidebar → *Quiz Generator* |

---

## 🛠️ Tech Stack
- **Python 3.11+** – core language.
- **Streamlit** – UI framework (`streamlit>=1.35`).
- **Groq SDK** – official client for LLM inference (`groq>=0.5.0`).
- **python‑dotenv** – loads local environment variables (`python-dotenv>=1.0.0`).
- **pytest** – unit‑testing framework (`pytest>=8.0`).

---

## 📐 Architecture

## 📁 Repository Layout
```
Study_Virtual_Assistant/
│
├─ app.py                # Streamlit entry point & navigation
├─ assistant.py          # Groq client wrapper
├─ config.py             # Loads .env, validates API key
├─ prompts.py            # System prompts for each capability
│
├─ modules/              # Feature implementations
│   ├─ __init__.py
│   ├─ study_mode.py
│   ├─ summarizer.py
│   └─ quiz_generator.py
│
├─ tests/                # Simple unit tests (no external calls)
│   ├─ __init__.py
│   └─ test_prompts.py
│
├─ .env.example          # Template for local secrets
├─ .gitignore
├─ requirements.txt
└─ README.md
```

---

## 🚀 Getting Started (Local Development)
1. **Clone the repository**
   ```powershell
   git clone https://github.com/paliwalketan05/Study_Virtual_Assistant.git
   cd Study_Virtual_Assistant
   ```
2. **Create & activate a virtual environment**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # PowerShell (use `source .venv/bin/activate` on Linux/macOS)
   ```
3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Set up your Groq credentials**
   ```powershell
   copy .env.example .env   # creates a writable .env file
   notepad .env              # replace `YOUR_GROQ_API_KEY` with your real key
   ```
   The file should look like:
   ```text
   GROQ_API_KEY=your_real_groq_key_here
   GROQ_MODEL=openai/gpt-oss-120b   # you can change the model if you wish
   ```
5. **Run the application**
   ```powershell
   streamlit run app.py
   ```
   Open the URL printed in the console (usually `http://localhost:8501`).

---

## ✅ Running the Test Suite
The repository ships with a tiny test suite that validates the prompt‑generation helpers – no external API calls are made.
```powershell
pytest -v
```
Expected output (example):
```
============================= test session starts ==============================
collected 4 items

tests/test_prompts.py ....                                            [100%]

============================== 4 passed in 0.03s ==============================
```
If you see `4 passed`, everything is wired correctly.

---

## 🌐 Deploying to Streamlit Community Cloud
1. **Push the repo** to GitHub (already done).
2. In the Streamlit Cloud dashboard, click **New app**, select the repository and set the **Main file path** to `app.py`.
3. Add a **Secret** called `GROQ_API_KEY` (and optionally `GROQ_MODEL`) under the *Secrets* tab.
4. Click **Deploy** – Streamlit will install all packages from `requirements.txt` and start the app.

Your app will be publicly reachable at the generated URL.

---

## 🔮 Future Enhancements (Ideas for the Next Iteration)
- **Persistent conversation storage** (e.g., SQLite or a cloud DB) so history survives page reloads.
- **RAG (Retrieval‑Augmented Generation)** – ingest PDF lecture notes or textbook chapters for more accurate answers.
- **Voice input & text‑to‑speech** for hands‑free studying.
- **User authentication & multi‑user dashboards** so each student gets a personal workspace.
- **More advanced quiz options** (true/false, fill‑in‑the‑blank, timed quizzes).

---

## 🙋‍♀️ Acknowledgments & Credits
- **Groq** for providing a fast, affordable LLM inference API.
- **Streamlit** for making web UI creation in pure Python a breeze.
- **Open‑source community** – many small utilities (e.g., `python‑dotenv`) that keep the project lean.

---

## 📄 License
This project is released under the **MIT License** – feel free to copy, modify, and share it for educational purposes.

---

*Happy studying!* 🎓
