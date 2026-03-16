import requests
import json
from logger import get_logger

logger = get_logger(__name__)


def planner(analysis):
    # If analyzer returned dict → convert to readable text for LLM
    if isinstance(analysis, dict):
        analysis_text = json.dumps(analysis)
    else:
        analysis_text = analysis

    prompt = f"""
You are an AI planner for an email assistant.

Your job is to decide the correct action.

Rules:

1. Use "calendar_event" ONLY if a deadline or time exists.
2. Use "reminder" ONLY if a task exists but no time.
3. Use "notify" ONLY if the email is important information.
4. Use "ignore" for newsletters, promotions, greetings.

Return ONLY JSON.

Example:
{{"action": "calendar_event"}}

Email Analysis:
{analysis_text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"].strip()

    logger.info(f"Planner raw LLM output:{result}")

    # Try to extract JSON safely
    try:
        start = result.find("{")
        end = result.rfind("}") + 1
        json_string = result[start:end]

        data = json.loads(json_string)
        action = data.get("action", "ignore")

    except Exception as e:
        logger.error("Planner JSON error:", e)
        action = "ignore"

    # Safety filter
    analysis_str = analysis_text.lower()

    if action == "reminder":
        keywords = ["task", "complete", "submit", "send", "review", "fill"]
        if not any(word in analysis_str for word in keywords):
            action = "ignore"

    logger.info(f"Planner final decision: {action}")

    return action
