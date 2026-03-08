import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_performance(records):

    if not records:
        return "No performance data available."

    summary = ""

    for r in records:
        summary += f"""
Member ID: {r.member_id}
KPI ID: {r.kpi_id}
Cycle ID: {r.cycle_id}
Progress: {r.progress}
"""

    prompt = f"""
Analyze the following organizational performance data and give insights:

{summary}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a performance analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content