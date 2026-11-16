import os
from typing import List, Dict
from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

# Re‑use the same wrapper logic as in assistant.py but expose dedicated helpers

def _get_client() -> Groq:
    return Groq(api_key=GROQ_API_KEY)

def study_explain(topic: str, level: str = "beginner") -> Dict[str, str]:
    """Generate an explanation for *topic* at the requested *level*.
    Returns a dict with either ``{"content": ...}`` or ``{"error": ...}``.
    """
    from prompts import study_mode_prompt
    messages: List[Dict[str, str]] = [
        {"role": "system", "content": study_mode_prompt(level)},
        {"role": "user", "content": topic},
    ]
    try:
        client = _get_client()
        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            temperature=0.7,
        )
        reply = completion.choices[0].message.content.strip()
        return {"content": reply}
    except Exception as e:
        return {"error": str(e)}
