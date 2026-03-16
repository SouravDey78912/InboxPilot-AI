import requests
import json


def analyze_email(email):

    prompt = f"""
You are an AI email analyzer.

Extract task and deadline from the email.

Return ONLY JSON.

Example:

{{
"task": "fill document",
"deadline": "tomorrow",
"important": true
}}

Email:
{email}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    try:
        return json.loads(result)
    except:
        return {
            "task": "",
            "deadline": "",
            "important": False
        }