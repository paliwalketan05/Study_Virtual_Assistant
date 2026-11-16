import os
from typing import List, Dict
from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

def generate_quiz(topic: str, num_questions: int = 5) -> Dict[str, str]:
    """Generate MCQ quiz on *topic*.
    Returns ``{"content": quiz_text}`` where *quiz_text* is a nicely formatted string,
    or ``{"error": ...}`` on failure.
    """
    if not topic.strip():
        return {"error": "Quiz topic is empty."}
    from prompts import quiz_generator_prompt
    system_prompt = quiz_generator_prompt()
    user_prompt = f"Topic: {topic}\nNumber of questions: {num_questions}"
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    try:
        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            temperature=0.7,
        )
        reply = completion.choices[0].message.content.strip()
        return {"content": reply}
    except Exception as e:
        return {"error": str(e)}
