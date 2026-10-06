// F.R.I.D.A.Y. AI OS - Core Web Engine
const SHREYAN_KNOWLEDGE = {
  name: "Kavati John Shreyan",
  role: "AI Engineer | Full Stack AI Developer | GenAI Developer | CSE (AI & Computational Intelligence)",
  location: "Hyderabad, India",
  email: "2400033326cse2@gmail.com",
  skills: [
    "Artificial Intelligence (AI)", "Computational Intelligence", "Generative AI", "Large Language Models (LLMs)",
    "Retrieval-Augmented Generation (RAG)", "Prompt Engineering", "AI Agents", "Multimodal AI", "Machine Learning",
    "Python", "Java", "JavaScript", "TypeScript", "React", "Next.js", "FastAPI", "Firebase", "MySQL", "SQLite",
    "REST APIs", "JWT Authentication", "Git & GitHub", "AWS Cloud", "Google Cloud", "Tailwind CSS", "UI/UX Design"
  ],
  projects: {
    aethermind: {
      name: "🚀 AetherMind Multimodal AI",
      desc: "Enterprise-grade Multimodal AI Operating System integrating multiple LLMs, intelligent cognitive routing, document intelligence, PDF RAG, voice interaction, and multi-tenant auth.",
      tech: "Python, FastAPI, React, RAG, OpenAI, Gemini, Firebase"
    },
    genesis: {
      name: "🧠 AetherMind Genesis",
      desc: "Autonomous Enterprise Software Architecture Generator that converts natural language requirements into complete database schemas, API contracts, JWT auth, and deployment roadmaps.",
      tech: "TypeScript, Next.js, Generative AI, Multi-Agent Systems"
    },
    edu: {
      name: "📚 AetherMind EDU",
      desc: "AI-powered educational workspace providing intelligent tutoring, document summarization, flashcards, and collaborative study tools.",
      tech: "Python, FastAPI, Tailwind CSS, Firebase"
    },
    optimizer: {
      name: "📅 Smart Resource & Timetable Optimizer",
      desc: "University resource allocation and schedule optimization engine with AI scheduling algorithms, conflict resolution, and analytics dashboards.",
      tech: "React, FastAPI, MySQL, Optimization Algorithms"
    },
    attendance: {
      name: "🎓 KL University Attendance Calculator",
      desc: "Open-source contribution redesigning the UI/UX, responsiveness, and student attendance forecasting models.",
      tech: "JavaScript, React, Tailwind CSS"
    }
  }
};

let liveRepos = [];
let voiceEnabled = true;

// Initialize App
document.addEventListener("DOMContentLoaded", () => {
  fetchLiveGitHubRepos();
  setupEventListeners();
});

// Fetch Live Repositories from GitHub API
async function fetchLiveGitHubRepos() {
  try {
    const res = await fetch("https://api.github.com/users/KAVATIJOHNSHREYAN/repos?sort=updated");
    if (res.ok) {
      liveRepos = await res.json();
      console.log(`[F.R.I.D.A.Y.] Fetched ${liveRepos.length} live repositories.`);
    }
  } catch (err) {
    console.warn("[F.R.I.D.A.Y.] GitHub API fetch fallback:", err);
  }
}

// Event Listeners
function setupEventListeners() {
  const userInput = document.getElementById("userInput");
  const sendBtn = document.getElementById("sendBtn");
  const voiceBtn = document.getElementById("voiceToggleBtn");

  sendBtn.addEventListener("click", () => handleUserSend());
  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") handleUserSend();
  });

  voiceBtn.addEventListener("click", () => {
    voiceEnabled = !voiceEnabled;
    voiceBtn.querySelector(".btn-text").textContent = voiceEnabled ? "VOICE ON" : "VOICE OFF";
    voiceBtn.style.opacity = voiceEnabled ? "1" : "0.5";
  });

  // Prompt Chips
  document.querySelectorAll(".chip-btn").forEach(chip => {
    chip.addEventListener("click", () => {
      const promptText = chip.getAttribute("data-prompt");
      userInput.value = promptText;
      handleUserSend();
    });
  });

  // Sidebar Projects
  document.querySelectorAll(".project-item").forEach(item => {
    item.addEventListener("click", () => {
      const promptText = item.getAttribute("data-prompt");
      userInput.value = promptText;
      handleUserSend();
    });
  });
}

// Handle User Sending a Message
function handleUserSend() {
  const userInput = document.getElementById("userInput");
  const text = userInput.value.trim();
  if (!text) return;

  // Add User Message
  appendMessage("user", "YOU", text);
  userInput.value = "";

  // Generate F.R.I.D.A.Y. Response
  setTimeout(() => {
    const responseText = generateFridayResponse(text);
    appendMessage("friday", "F.R.I.D.A.Y.", responseText);
    if (voiceEnabled) speakFridayResponse(responseText);
  }, 400);
}

// Append Message to Stream
function appendMessage(sender, name, bodyText) {
  const stream = document.getElementById("chatStream");
  const msgDiv = document.createElement("div");
  msgDiv.className = `chat-message ${sender}-message`;

  const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  const avatar = sender === "user" ? "👤" : "🤖";

  msgDiv.innerHTML = `
    <div class="msg-avatar">${avatar}</div>
    <div class="msg-content">
      <div class="msg-author">${name} <span class="time">${timeStr}</span></div>
      <div class="msg-body">${formatMarkdown(bodyText)}</div>
    </div>
  `;

  stream.appendChild(msgDiv);
  stream.scrollTop = stream.scrollHeight;
}

// Markdown formatting helper
function formatMarkdown(text) {
  return text
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br/>');
}

// F.R.I.D.A.Y. Tactical AI Engine
function generateFridayResponse(query) {
  const q = query.toLowerCase();

  if (q.includes("aethermind multimodal") || q.includes("multimodal ai")) {
    return `<strong>${SHREYAN_KNOWLEDGE.projects.aethermind.name}</strong><br/>${SHREYAN_KNOWLEDGE.projects.aethermind.desc}<br/><br/><strong>Tech Stack:</strong> ${SHREYAN_KNOWLEDGE.projects.aethermind.tech}`;
  }

  if (q.includes("genesis") || q.includes("architecture generator")) {
    return `<strong>${SHREYAN_KNOWLEDGE.projects.genesis.name}</strong><br/>${SHREYAN_KNOWLEDGE.projects.genesis.desc}<br/><br/><strong>Tech Stack:</strong> ${SHREYAN_KNOWLEDGE.projects.genesis.tech}`;
  }

  if (q.includes("edu") || q.includes("learning")) {
    return `<strong>${SHREYAN_KNOWLEDGE.projects.edu.name}</strong><br/>${SHREYAN_KNOWLEDGE.projects.edu.desc}<br/><br/><strong>Tech Stack:</strong> ${SHREYAN_KNOWLEDGE.projects.edu.tech}`;
  }

  if (q.includes("timetable") || q.includes("optimizer") || q.includes("schedule")) {
    return `<strong>${SHREYAN_KNOWLEDGE.projects.optimizer.name}</strong><br/>${SHREYAN_KNOWLEDGE.projects.optimizer.desc}<br/><br/><strong>Tech Stack:</strong> ${SHREYAN_KNOWLEDGE.projects.optimizer.tech}`;
  }

  if (q.includes("attendance") || q.includes("kl university")) {
    return `<strong>${SHREYAN_KNOWLEDGE.projects.attendance.name}</strong><br/>${SHREYAN_KNOWLEDGE.projects.attendance.desc}<br/><br/><strong>Tech Stack:</strong> ${SHREYAN_KNOWLEDGE.projects.attendance.tech}`;
  }

  if (q.includes("skill") || q.includes("tech") || q.includes("stack") || q.includes("expertise")) {
    return `Boss, Shreyan specializes in:<br/><br/>🤖 <strong>Generative AI & LLMs:</strong> LLM Systems, RAG Pipelines, Autonomous AI Agents, Prompt Engineering.<br/>💻 <strong>Full Stack & Backend:</strong> Python, TypeScript, React, Next.js, FastAPI, Node.js.<br/>⚙️ <strong>Databases & Cloud:</strong> MySQL, SQLite, Firebase, AWS, GCP, JWT.`;
  }

  if (q.includes("contact") || q.includes("email") || q.includes("hire") || q.includes("reach")) {
    return `You can connect directly with Shreyan via email at:<br/>✉️ <strong><a href="mailto:${SHREYAN_KNOWLEDGE.email}" style="color:#00e5ff;">${SHREYAN_KNOWLEDGE.email}</a></strong><br/><br/>Or inspect his live work on <strong>GitHub: <a href="https://github.com/KAVATIJOHNSHREYAN" target="_blank" style="color:#00e5ff;">KAVATIJOHNSHREYAN</a></strong>.`;
  }

  if (q.includes("project") || q.includes("built") || q.includes("work")) {
    return `Shreyan has built enterprise AI applications including:<br/>1. 🚀 <strong>AetherMind Multimodal AI</strong> (Multi-LLM RAG & Voice)<br/>2. 🧠 <strong>AetherMind Genesis</strong> (Autonomous Architecture Generator)<br/>3. 📚 <strong>AetherMind EDU</strong> (AI Education Workspace)<br/>4. 📅 <strong>Smart Timetable Optimizer</strong> (University AI Scheduler)<br/>5. 🎓 <strong>KL University Attendance Calculator</strong> (Open Source UX)`;
  }

  if (liveRepos.length > 0 && (q.includes("repo") || q.includes("github"))) {
    const topRepos = liveRepos.slice(0, 5).map(r => `• <strong>${r.name}</strong> (${r.language || 'Code'}) - ${r.description || 'Public Repo'}`).join('<br/>');
    return `I scanned Shreyan's live GitHub profile. Here are his top active repositories:<br/><br/>${topRepos}`;
  }

  return `I have logged your query regarding *"${query}"*. Shreyan specializes in **AI Engineering, Autonomous Agents, and Enterprise RAG Architectures**. Feel free to ask about his **featured projects**, **technical skills**, or **email contact details**!`;
}

// Text-To-Speech Synthesis
function speakFridayResponse(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel(); // Stop current speech

  const cleanText = text.replace(/<[^>]*>?/gm, ''); // Strips HTML tags
  const utterance = new SpeechSynthesisUtterance(cleanText);
  utterance.rate = 1.05;
  utterance.pitch = 1.0;

  const voices = window.speechSynthesis.getVoices();
  const femaleVoice = voices.find(v => v.name.includes("Female") || v.name.includes("Google UK English Female") || v.name.includes("Zira") || v.name.includes("Samantha"));
  if (femaleVoice) utterance.voice = femaleVoice;

  window.speechSynthesis.speak(utterance);
}
