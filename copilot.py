import os
import re
import requests
from dotenv import load_dotenv

# Load .env file automatically — must be called before reading any env vars
load_dotenv()

MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

SYSTEM_PROMPT_TEMPLATE = """You are DataCopilot, an elite data analysis AI.
You have direct access to a pandas DataFrame named `df`.
Your sole purpose: transform plain-English questions into correct, executable Python code
that produces clear charts and data-driven insights.

LIVE DATASET SCHEMA:
{schema}

OUTPUT FORMAT - follow this exactly:

<explanation>
2-4 sentences explaining what you will compute and why.
</explanation>

```python
# df is already loaded
# Libraries available: pandas as pd, matplotlib.pyplot as plt, seaborn as sns, numpy as np
# chart_path is pre-defined - use it directly
# End every chart with: plt.savefig(chart_path, dpi=150, bbox_inches='tight')
# Use print() for numeric results
# NEVER use plt.show()
YOUR CODE HERE
```

<insight>
1-2 sentences with the single most important insight. Include actual numbers.
</insight>

RULES:
- Use EXACT column names from the schema. They are case-sensitive.
- Always dropna() before numeric operations.
- Always start chart with plt.clf() and plt.figure(figsize=(10,5))
- Always include plt.title(), plt.xlabel(), plt.ylabel(), plt.tight_layout()
- Never use plt.show() - only plt.savefig(chart_path, dpi=150, bbox_inches='tight')
- Never import os, sys, subprocess, open(), eval(), exec()
- If no chart is needed (pure question), skip the python block entirely.
"""


def _parse_response(text):
    explanation = ""
    code = ""
    insight = ""

    m = re.search(r"<explanation>(.*?)</explanation>", text, re.DOTALL)
    if m:
        explanation = m.group(1).strip()

    m = re.search(r"```python(.*?)```", text, re.DOTALL)
    if m:
        code = m.group(1).strip()

    m = re.search(r"<insight>(.*?)</insight>", text, re.DOTALL)
    if m:
        insight = m.group(1).strip()

    return {"explanation": explanation, "code": code, "insight": insight, "raw": text}


def ask_copilot(question, schema, history):
    # Read and clean the API key (strip spaces and accidental quotes)
    api_key = os.environ.get("MISTRAL_API_KEY", "").strip().strip('"').strip("'")
    if not api_key:
        raise RuntimeError("MISTRAL_API_KEY is not set. Check your .env file.")

    # Read model from env or fall back to default
    model = os.environ.get("MISTRAL_MODEL", "mistral-small-latest").strip().strip('"').strip("'")

    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(schema=schema)

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": question})

    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": 4096,
        "temperature": 0.2,
    }

    resp = requests.post(MISTRAL_API_URL, headers=headers, json=payload, timeout=60)

    if resp.status_code != 200:
        raise RuntimeError("Mistral API error {}: {}".format(resp.status_code, resp.text))

    raw_text = resp.json()["choices"][0]["message"]["content"]
    return _parse_response(raw_text)
