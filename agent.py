import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an autonomous supply chain digital worker for a manufacturing company.

Your role is to:
- Understand supply chain disruptions
- Analyze operational impact
- Recommend and justify mitigation actions

Focus on:
- Production impact
- Customer orders
- Supplier dependencies
- Operational continuity

Be concise but structured in your reasoning.
"""


def call_llm(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ LLM Error: {str(e)}"


# 🔍 Product detection (used by UI + logic)
def detect_product(user_input):
    text = user_input.lower()

    if "hydraulic" in text:
        return "hydraulic pumps"
    elif "control valve" in text:
        return "control valves"
    elif "ecu" in text or "electronic" in text:
        return "electronic control units"
    else:
        return "critical components"