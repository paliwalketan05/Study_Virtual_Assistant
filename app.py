# app.py
"""CampusMate – Streamlit front‑end.

This file wires the sidebar navigation, session state, and the four
feature modules (chat, study mode, summarizer, quiz generator).
"""

import streamlit as st
from typing import List, Dict

# Local imports
from assistant import GroqAssistant
from prompts import chat_system_prompt
from modules.study_mode import study_explain
from modules.summarizer import summarize_text
from modules.quiz_generator import generate_quiz

# ---------------------------------------------------------------------
# Initialise session state
# ---------------------------------------------------------------------
def init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []  # chat history
    if "assistant" not in st.session_state:
        st.session_state.assistant = GroqAssistant()
    if "selected_feature" not in st.session_state:
        st.session_state.selected_feature = "AI Chat"

# ---------------------------------------------------------------------
# UI helpers for each feature
# ---------------------------------------------------------------------
def chat_ui() -> None:
    st.header("💬 AI Chat")
    # show history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_prompt := st.chat_input("Ask a question…"):
        # add user message locally
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.write(user_prompt)

        # build payload for LLM (system + history)
        messages: List[Dict[str, str]] = [
            {"role": "system", "content": chat_system_prompt()}
        ] + [
            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
        ]

        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                resp = st.session_state.assistant.chat(messages)
        if "error" in resp:
            st.error(f"⚠️ API error: {resp['error']}")
        else:
            answer = resp["content"]
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.write(answer)

def study_mode_ui() -> None:
    st.header("📚 Study Mode")
    topic = st.text_input("Topic / Question", key="study_topic")
    level = st.radio(
        "Difficulty level",
        options=["Beginner", "Intermediate", "Advanced"],
        index=0,
        key="study_level",
    )
    if st.button("Explain"):
        if not topic.strip():
            st.warning("Please enter a topic.")
            return
        with st.spinner("Generating explanation…"):
            result = study_explain(topic, level.lower())
        if "error" in result:
            st.error(f"⚠️ {result['error']}")
        else:
            st.write(result["content"])

def summarizer_ui() -> None:
    st.header("📝 Text Summarizer")
    text = st.text_area("Enter text to summarise", height=200, key="summ_text")
    if st.button("Summarise"):
        if not text.strip():
            st.warning("Please paste some text.")
            return
        with st.spinner("Summarising…"):
            result = summarize_text(text)
        if "error" in result:
            st.error(f"⚠️ {result['error']}")
        else:
            st.success("**Summary:**")
            st.write(result["content"])

def quiz_ui() -> None:
    st.header("❓ Quiz Generator")
    topic = st.text_input("Quiz topic", key="quiz_topic")
    num_q = st.slider("Number of questions", 1, 10, 5, key="quiz_num")
    if st.button("Generate Quiz"):
        if not topic.strip():
            st.warning("Please provide a topic.")
            return
        with st.spinner("Creating quiz…"):
            result = generate_quiz(topic, num_q)
        if "error" in result:
            st.error(f"⚠️ {result['error']}")
        else:
            st.success("**Quiz:**")
            st.write(result["content"])

# ---------------------------------------------------------------------
# Main layout
# ---------------------------------------------------------------------
def main() -> None:
    st.set_page_config(page_title="CampusMate", page_icon="🎓", layout="centered")
    init_state()

    # Sidebar navigation
    with st.sidebar:
        st.title("CampusMate")
        st.markdown(
            "*Your AI‑powered study companion*\n---\n"
        )
        feature = st.radio(
            "Navigate",
            ["AI Chat", "Study Mode", "Text Summarizer", "Quiz Generator"],
            index=["AI Chat", "Study Mode", "Text Summarizer", "Quiz Generator"].index(
                st.session_state.selected_feature
            ),
        )
        st.session_state.selected_feature = feature
        st.divider()
        if st.button("Clear conversation"):
            st.session_state.messages = []
            st.success("Conversation cleared.")
        st.caption(
            "**Tech stack**\n• Streamlit\n• Groq LLM\n• python‑dotenv"
        )

    # Render selected feature
    if st.session_state.selected_feature == "AI Chat":
        chat_ui()
    elif st.session_state.selected_feature == "Study Mode":
        study_mode_ui()
    elif st.session_state.selected_feature == "Text Summarizer":
        summarizer_ui()
    elif st.session_state.selected_feature == "Quiz Generator":
        quiz_ui()

if __name__ == "__main__":
    main()
