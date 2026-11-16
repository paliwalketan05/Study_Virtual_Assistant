import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root if present
PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

# Retrieve mandatory variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

if not GROQ_API_KEY:
    raise EnvironmentError(
        "GROQ_API_KEY not found. Please create a .env file with your Groq API key or set the variable in Streamlit secrets."
    )

__all__ = ["GROQ_API_KEY", "GROQ_MODEL"]
