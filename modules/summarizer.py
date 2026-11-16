import os
from typing import List, Dict
from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

def summarize_text(text: str) -> Dict[str, str]:
    """Summarize *text* using the Groq LLM.
    Returns ``{"content": summary}`` or ``{"error": ...}``.
    """
    if not text.strip():
        return {"error": "Input text is empty."}
    from prompts import summarizer_prompt
    messages = [
        {"role": "system", "content": summarizer_prompt()},
        {"role": "user", "content": text},
    ]
    try:
        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            temperature=0.5,
        )
        reply = completion.choices[0].message.content.strip()
        return {"content": reply}
    except Exception as e:
        return {"error": str(e)}
