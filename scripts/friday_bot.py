import os
import sys
import json
import requests

def fetch_github_user_data(username: str, token: str = None) -> str:
    """Dynamically fetch all live public GitHub repositories, stars, languages, and details for the user."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    summary_lines = []
    
    # 1. User details
    user_url = f"https://api.github.com/users/{username}"
    try:
        u_res = requests.get(user_url, headers=headers, timeout=10)
        if u_res.status_code == 200:
            u_data = u_res.json()
            summary_lines.append(f"GitHub User: {u_data.get('login')} ({u_data.get('name')})")
            summary_lines.append(f"Bio: {u_data.get('bio')}")
            summary_lines.append(f"Public Repositories Count: {u_data.get('public_repos')}")
            summary_lines.append(f"Followers: {u_data.get('followers')}")
    except Exception as e:
        print(f"[WARN] Failed to fetch user info: {e}")

    # 2. Public repositories
    repos_url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=30"
    try:
        r_res = requests.get(repos_url, headers=headers, timeout=10)
        if r_res.status_code == 200:
            repos = r_res.json()
            summary_lines.append("\nLive Repositories & Projects on GitHub:")
            for r in repos:
                if not r.get("fork"): # focus on original repos
                    name = r.get("name")
                    desc = r.get("description") or "No description provided"
                    lang = r.get("language") or "N/A"
                    stars = r.get("stargazers_count", 0)
                    topics = ", ".join(r.get("topics", []))
                    summary_lines.append(f"- Project Name: {name} | Primary Language: {lang} | Stars: {stars}")
                    summary_lines.append(f"  Description: {desc}")
                    if topics:
                        summary_lines.append(f"  Topics: {topics}")
    except Exception as e:
        print(f"[WARN] Failed to fetch repositories: {e}")

    return "\n".join(summary_lines)

def reply_to_issue(issue_number: int, issue_title: str, issue_body: str, repo: str, token: str):
    username = repo.split("/")[0] if "/" in repo else "KAVATIJOHNSHREYAN"
    
    # Fetch live GitHub data automatically
    live_github_context = fetch_github_user_data(username, token)
    
    # Read README context if available
    readme_context = ""
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    if os.path.exists(readme_path):
        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                readme_context = f.read()[:3000] # first 3000 chars for context
        except Exception as e:
            print(f"[WARN] Could not read local README: {e}")

    system_prompt = f"""
You are F.R.I.D.A.Y., the tactical, highly intelligent AI assistant created by and representing Kavati John Shreyan.
Your persona is sleek, polite, articulate, tech-savvy, and helpful. You address users professionally (and refer to Shreyan as "Boss" or "Shreyan" when discussing him).

Full Context & Profile Data for Kavati John Shreyan:
- Role: AI Engineer | Full Stack AI Developer | GenAI Developer | CSE (AI & Computational Intelligence).
- Location: Hyderabad, India.
- Email: 2400033326cse2@gmail.com
- Main Focus: Enterprise LLM Systems, RAG Pipelines, Autonomous AI Agents, Multimodal AI, Scalable Backend Services.
- Featured Projects:
  1. AetherMind Multimodal AI
  2. AetherMind Genesis
  3. AetherMind EDU
  4. Smart Resource & Timetable Optimizer
  5. KL University Attendance Calculator

Dynamically Fetched Live GitHub Data:
{live_github_context}

Profile README Content:
{readme_context}

Instructions:
- Answer the user's question accurately using both the curated context and the dynamically fetched live GitHub repository data.
- Keep responses engaging, structured in clean markdown, concise, and helpful.
- Address the user politely as F.R.I.D.A.Y.
"""

    user_query = f"Issue Title: {issue_title}\nIssue Query: {issue_body}"
    api_key = os.getenv("GEMINI_API_KEY")
    ai_response = ""

    if api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{system_prompt}\n\nUser Question:\n{user_query}",
            )
            if response and response.text:
                ai_response = response.text
        except Exception as e:
            print(f"[WARN] Gemini API call error: {e}")

    if not ai_response:
        ai_response = (
            f"### 🤖 F.R.I.D.A.Y. Tactical Response\n\n"
            f"Greetings! I am **F.R.I.D.A.Y.**, Shreyan's tactical AI assistant.\n\n"
            f"I have received your query regarding: *'{issue_title}'*.\n\n"
            f"Shreyan specializes in **Generative AI, Autonomous Multi-Agent Systems, and Enterprise RAG Pipelines**. "
            f"I have logged your request into Shreyan's system. You can reach out directly via email at [`2400033326cse2@gmail.com`](mailto:2400033326cse2@gmail.com).\n\n"
            f"**Dynamically Scanned GitHub Context:**\n{live_github_context[:500]}\n\n"
            f"*F.R.I.D.A.Y. Protocol // Standing by.*"
        )
    else:
        ai_response = f"### 🤖 F.R.I.D.A.Y. Tactical Response\n\n{ai_response}\n\n---\n*F.R.I.D.A.Y. AI Assistant // Live GitHub Data & Gemini Connected*"

    # Post comment back to GitHub Issue
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    res = requests.post(url, json={"body": ai_response}, headers=headers)
    if res.status_code in [200, 201]:
        print(f"[SUCCESS] Successfully posted F.R.I.D.A.Y. reply to issue #{issue_number}")
    else:
        print(f"[ERROR] Failed to post comment: {res.status_code} - {res.text}")

if __name__ == "__main__":
    event_path = os.getenv("GITHUB_EVENT_PATH")
    repo = os.getenv("GITHUB_REPOSITORY")
    token = os.getenv("GITHUB_TOKEN")

    if not event_path or not os.path.exists(event_path):
        print("[ERROR] No event path found.")
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
