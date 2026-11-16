import os
from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL
from typing import List, Dict

class GroqAssistant:
    """Simple wrapper around the Groq SDK.
    Takes a list of message dicts (role, content) and returns the assistant's reply.
    Handles common API errors and returns a tuple (success: bool, response: str).
    """

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL

    def chat(self, messages: List[Dict[str, str]]) -> Dict[str, str]:
        """Send a conversation to the LLM.
        Returns a dict with keys:
            - 'error' (optional)
            - 'content' (assistant reply when no error)
        """
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
            )
            reply = completion.choices[0].message.content.strip()
            return {"content": reply}
        except Exception as e:
            # Simplify error reporting for the UI layer
            return {"error": str(e)}

__all__ = ["GroqAssistant"]
