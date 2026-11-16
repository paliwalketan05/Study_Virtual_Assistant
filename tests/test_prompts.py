import pytest
from prompts import (
    chat_system_prompt,
    study_mode_prompt,
    summarizer_prompt,
    quiz_generator_prompt,
)

def test_chat_prompt_not_empty():
    assert chat_system_prompt().strip() != ""

@pytest.mark.parametrize(
    "level, expected_fragment",
    [
        ("beginner", "simple language"),
        ("intermediate", "technical explanation"),
        ("advanced", "deep, rigorous"),
    ],
)
def test_study_mode_prompt_levels(level, expected_fragment):
    prompt = study_mode_prompt(level)
    assert expected_fragment.lower() in prompt.lower()

def test_summarizer_prompt():
    assert "concise summarizer" in summarizer_prompt().lower()

def test_quiz_generator_prompt():
    assert "multiple‑choice questions" in quiz_generator_prompt().lower()
