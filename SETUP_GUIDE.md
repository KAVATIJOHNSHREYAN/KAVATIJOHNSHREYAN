# 🚀 Setup & Deployment Guide for GitHub Profile

Follow these simple steps to bring your **JARVIS-Inspired Enterprise AI Profile** live on GitHub!

---

### Step 1: Create the Special GitHub Repository
1. Go to [https://github.com/new](https://github.com/new)
2. Enter **`KAVATIJOHNSHREYAN`** as the Repository Name.
3. Make sure the repository visibility is set to **Public**.
4. Leave "Add a README file" unchecked (since we already have a complete custom `README.md` ready).
5. Click **Create repository**.

---

### Step 2: Push Code to GitHub
Open your terminal in this workspace folder (`c:\Users\johns\Documents\GITHUB PROFILE UPDATE`) and run:

```bash
git init
git add .
git commit -m "feat: launch JARVIS enterprise AI profile with dynamic auto-updater"
git branch -M main
git remote add origin https://github.com/KAVATIJOHNSHREYAN/KAVATIJOHNSHREYAN.git
git push -u origin main
```

---

### Step 3: Enable Workflow Permissions for Auto-Updater
To allow GitHub Actions to automatically generate your Snake contribution animation and update your AI insights daily:

1. Open your repository on GitHub: `https://github.com/KAVATIJOHNSHREYAN/KAVATIJOHNSHREYAN`
2. Navigate to **Settings** -> **Actions** -> **General**.
3. Scroll down to **Workflow permissions**.
4. Select **Read and write permissions**.
5. Check the box **"Allow GitHub Actions to create and approve pull requests"**.
6. Click **Save**.

---

### Step 4: (Optional) Add Gemini API Key for AI Insights
If you want the AI updater bot to generate fresh 1-line Generative AI thoughts dynamically every day:

1. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).
2. In your repo on GitHub, go to **Settings** -> **Secrets and variables** -> **Actions**.
3. Click **New repository secret**.
4. Name: `GEMINI_API_KEY`
5. Value: *[Your Gemini API Key]*
6. Click **Add secret**.

*(Note: If no API key is added, the update script automatically falls back to curated high-tech architecture principles!)*

---

### Step 5: Manually Trigger Your First Update (Optional)
To test the automation immediately:
1. Go to the **Actions** tab in your repository.
2. Select **Update Profile & Generate Snake Matrix**.
3. Click **Run workflow** -> **Run workflow**.

Your GitHub profile page is now live and automatically updating! 🌟
