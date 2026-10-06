import os
import sys
import json
import requests

SHREYAN_PROFILE_CONTEXT = """
You are F.R.I.D.A.Y., the tactical, highly intelligent AI assistant created by and representing Kavati John Shreyan.
Your persona is sleek, polite, articulate, tech-savvy, and helpful. You address users professionally (and refer to Shreyan as "Boss" or "Shreyan" when discussing him).

Knowledge Base about Kavati John Shreyan:
- Role: AI Engineer | Full Stack AI Developer | GenAI Developer | CSE (AI & Computational Intelligence).
- Location: Hyderabad, India.
- Email: 2400033326cse2@gmail.com
- Primary Focus: Enterprise LLM Systems, RAG Pipelines, Autonomous AI Agents, Multimodal AI, Scalable Backend Services.
- Skills: Python, Java, JavaScript, TypeScript, React, Next.js, FastAPI, Firebase, MySQL, SQLite, REST APIs, JWT, Git/GitHub, AWS, GCP, Tailwind CSS, UI/UX Design.
- Featured Projects:
  1. AetherMind Multimodal AI: Enterprise Multi-LLM operating system with document intelligence, PDF RAG, voice interaction, and multi-tenant auth.
  2. AetherMind Genesis: Autonomous Enterprise Blueprint Generator that outputs database schemas, API contracts, and deployment roadmaps from natural language requirements.
  3. AetherMind EDU: AI-powered educational workspace providing document analysis, flashcards, and tutoring assistance.
  4. Smart Resource & Timetable Optimizer: Full-stack university resource allocation platform with AI scheduling.
  5. KL University Attendance Calculator: Open-source contribution redesigning UI/UX and student interaction.

Rules:
- Answer the user's question accurately based on Shreyan's profile context.
- Keep responses engaging, structured in markdown, concise, and helpful.
- Always maintain your F.R.I.D.A.Y. AI persona.
"""

def reply_to_issue(issue_number: int, issue_title: str, issue_body: str, repo: str, token: str):
    user_prompt = f"Issue Title: {issue_title}\nIssue Query: {issue_body}"
    
    api_key = os.getenv("GEMINI_API_KEY")
    ai_response = ""
    
    if api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{SHREYAN_PROFILE_CONTEXT}\n\nUser Question:\n{user_prompt}",
            )
            if response and response.text:
                ai_response = response.text
        except Exception as e:
            print(f"[WARN] Gemini API error: {e}")
    
    if not ai_response:
        ai_response = (
            f"### 🤖 F.R.I.D.A.Y. System Response\n\n"
            f"Hello! I am **F.R.I.D.A.Y.**, Shreyan's tactical AI assistant.\n\n"
            f"Thank you for reaching out regarding: *'{issue_title}'*.\n\n"
            f"Shreyan specializes in **Generative AI, Autonomous LLM Agents, and Enterprise RAG Systems**. "
            f"You can connect directly with him via email at [`2400033326cse2@gmail.com`](mailto:2400033326cse2@gmail.com) "
            f"or inspect his featured projects on his profile.\n\n"
            f"*System status: Query logged successfully.*"
        )
    else:
        ai_response = f"### 🤖 F.R.I.D.A.Y. System Protocol\n\n{ai_response}\n\n---\n*F.R.I.D.A.Y. AI Assistant // Powered by Gemini*"

    # Post comment back to GitHub Issue
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    res = requests.post(url, json={"body": ai_response}, headers=headers)
    if res.status_code in [200, 201]:
        print(f"[SUCCESS] Successfully commented on issue #{issue_number}")
    else:
        print(f"[ERROR] Failed to comment on issue #{issue_number}: {res.status_code} - {res.text}")

if __name__ == "__main__":
    event_path = os.getenv("GITHUB_EVENT_PATH")
    repo = os.getenv("GITHUB_REPOSITORY")
    token = os.getenv("GITHUB_TOKEN")

    if not event_path or not os.path.exists(event_path):
        print("[ERROR] No GitHub event path found.")
        sys.exit(1)

    with open(event_path, "r", encoding="utf-8") as f:
        event = json.load(f)

    issue = event.get("issue", {})
    issue_number = issue.get("number")
    issue_title = issue.get("title", "")
    issue_body = issue.get("body", "")

    if issue_number:
        reply_to_issue(issue_number, issue_title, issue_body, repo, token)
    else:
        print("[WARN] Event is not an issue.")
