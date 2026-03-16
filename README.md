# 🚀 InboxPilot-AI

**An Autonomous AI Email Agent that reads emails, extracts tasks, and automatically creates reminders or calendar events.**

InboxPilot-AI is an **AI-powered autonomous email assistant** that continuously monitors your inbox, understands incoming emails using a local LLM, and takes intelligent actions such as creating reminders, scheduling calendar events, or sending notifications.

The system is built using a **multi-agent architecture** orchestrated through LangGraph, enabling modular and scalable AI workflows.

---

# ✨ Features

• 📧 Automatically reads incoming emails
• 🧠 Uses an LLM to understand tasks and deadlines
• 📅 Creates Google Calendar events automatically
• ⏰ Generates reminders for tasks without deadlines
• 🔔 Sends notifications for important emails
• 🤖 Built with a **multi-agent architecture**
• 🔄 Runs continuously like a real autonomous AI agent

---

# 🧠 Architecture Overview

InboxPilot-AI follows a **multi-agent workflow architecture** where each agent performs a specific role.

```
                 ┌──────────────────┐
                 │   Email Reader   │
                 │  (Gmail Agent)   │
                 └─────────┬────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │  Analyzer Agent  │
                 │  (LLM reasoning) │
                 └─────────┬────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │   Planner Agent  │
                 │  Decide action   │
                 └─────────┬────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │  Executor Agent  │
                 │  Routes action   │
                 └──────┬─────┬─────┘
                        │     │
                        ▼     ▼
                ┌─────────┐ ┌─────────┐
                │Calendar │ │Reminder │
                │ Agent   │ │ Agent   │
                └─────────┘ └─────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Notification │
                 │    Agent     │
                 └──────────────┘
```

---

# 🤖 Agent Workflow

The agent follows an **Observe → Reason → Decide → Act** loop.

### 1️⃣ Observe

The Email Reader Agent fetches new emails from Gmail.

### 2️⃣ Reason

The Analyzer Agent processes the email content using a local LLM to understand:

* tasks
* deadlines
* importance

Example email:

```
Please fill the onboarding document and send it by tomorrow.
```

Analyzer output:

```
Task: Fill onboarding document
Deadline: Tomorrow
Importance: High
```

### 3️⃣ Decide

The Planner Agent determines the best action:

```
calendar_event
reminder
notify
ignore
```

### 4️⃣ Act

The Executor Agent routes the task to the correct tool agent.

Example actions:

• Create a calendar event
• Save a reminder
• Send a notification

---

# 🖼 Demo (Example Agent Execution)

Example terminal output:

```
AI Email Agent started...

Processing email:
"Please fill the onboarding document and send it tomorrow"

Analyzer Output:
Task detected: Fill onboarding document
Deadline detected: Tomorrow

Planner Decision:
calendar_event

Executor:
Running Calendar Agent...

Calendar event created successfully.

Agent finished.
```

The event will automatically appear in your **Google Calendar**.

---

# 📂 Project Structure

```
InboxPilot-AI
│
├── main.py
├── graph.py
│
├── agents
│   ├── email_reader.py
│   ├── analyzer_agent.py
│   ├── planner_agent.py
│   └── executor_agent.py
│
├── tools
│   ├── calendar_tool.py
│   ├── reminder_tool.py
│   └── notifier_tool.py
│
├── auth.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone the Repository

```
git clone https://github.com/SouravDey78912/InboxPilot-AI.git

cd InboxPilot-AI
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Install and Run Local LLM

Install Ollama:

https://ollama.com

Pull the model:

```
ollama pull llama3
```

Start Ollama:

```
ollama run llama3
```

---

## 5️⃣ Enable Google APIs

Go to Google Cloud Console and enable:

• Gmail API
• Google Calendar API

Download:

```
credentials.json
```

Place it in the project root directory.

---

## 6️⃣ Run the Agent

```
python main.py
```

The AI agent will start monitoring your inbox and processing emails automatically.

---

# 🔁 Continuous Autonomous Execution

The agent runs in a continuous loop:

```
Check emails
 ↓
Analyze email
 ↓
Plan action
 ↓
Execute tool
 ↓
Wait
 ↓
Repeat
```

This makes InboxPilot-AI behave like a **real autonomous AI assistant**.

---

# 🧰 Tech Stack

Python
LangGraph
Ollama
Llama3
Gmail API
Google Calendar API

---

# 🌟 Future Improvements

• Memory using vector databases
• Natural language time parsing
• Slack / WhatsApp notifications
• Smart task prioritization
• Multi-agent collaboration expansion




