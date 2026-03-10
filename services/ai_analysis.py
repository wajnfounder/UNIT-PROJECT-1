import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


def local_analysis(records):

    if not records:
        return "No performance data available."

    avg_progress = sum(r.progress for r in records) / len(records)

    return f"""
Local Performance Analysis

Average Progress: {round(avg_progress, 2)}%

Recommendation:
Focus on improving KPIs with low progress.
"""


def analyze_performance(records):

    if not records:
        return "No performance data available."

    summary = ""

    for r in records:
        summary += f"""
Member: {r.member_id}
KPI: {r.kpi_id}
Cycle: {r.cycle_id}
Progress: {r.progress}%
"""

    prompt = f"""
You are a professional organizational performance analyst.

Analyze the following KPI performance data.

Provide a structured report with:

Executive Summary
Key Strengths
Weak Performance Areas
Strategic Recommendations for Management

Data:
{summary}
"""

    # If API key not available → fallback to local analysis
    if not client:
        return local_analysis(records)

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You analyze company KPI performance."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        print(f"OpenAI Error: {e}")

        return local_analysis(records)