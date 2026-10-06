import os
import re
import random
from datetime import datetime, timezone

# Fallback AI Insights if GEMINI_API_KEY is not provided
FALLBACK_INSIGHTS = [
    "True intelligence in software lies not just in model parameter size, but in the elegance of context retrieval, deterministic tool binding, and robust error fallback design.",
    "Autonomous agents thrive on structured outputs, schema verification, and clear cognitive boundaries.",
    "RAG pipelines bridge the gap between static model weights and real-time enterprise knowledge graphs.",
    "The future of software architecture is hybrid: deterministic control flows layered with probabilistic AI reasoning.",
    "Multimodal AI opens new frontiers where visual, textual, and acoustic data converge into unified decision engines.",
    "Optimizing latency in Generative AI applications requires intelligent caching, speculative execution, and stream optimization."
]

def generate_ai_insight() -> str:
    """Generate insight using Gemini API if key exists, otherwise fallback to curated list."""
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents="Write one single crisp, powerful, futuristic 1-sentence quote or architecture principle about AI Engineering, LLMs, or RAG for a developer's GitHub README. Do not include quotes around it.",
            )
            if response and response.text:
                return response.text.strip().strip('"')
        except Exception as e:
            print(f"[WARN] Failed to generate AI insight via Gemini API: {e}")
    
    return random.choice(FALLBACK_INSIGHTS)

def update_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    if not os.path.exists(readme_path):
        print(f"[ERROR] README file not found at {readme_path}")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update AI Insight
    insight = generate_ai_insight()
    new_insight_block = f'<!-- AI_INSIGHT_START -->\n> ⚡ **Daily AI Architecture Thought:** *"{insight}"*\n<!-- AI_INSIGHT_END -->'
    content = re.sub(r"<!-- AI_INSIGHT_START -->.*?<!-- AI_INSIGHT_END -->", new_insight_block, content, flags=re.DOTALL)

    # 2. Update Timestamp & Status
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    new_quote_block = f"""<!-- AI_QUOTE_START -->
```yaml
System_Status: Operational
Target_Mission: Building Next-Gen Multimodal AI Systems
Current_Motto: "Code with precision, innovate with AI, scale without limits."
Last_Updated: {now_utc} [Automated via GitHub Actions]
```
<!-- AI_QUOTE_END -->"""
    content = re.sub(r"<!-- AI_QUOTE_START -->.*?<!-- AI_QUOTE_END -->", new_quote_block, content, flags=re.DOTALL)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[SUCCESS] README successfully updated at {now_utc}")

if __name__ == "__main__":
    update_readme()
