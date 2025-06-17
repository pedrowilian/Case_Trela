# 🥗 Trela — Healthy Meals Recommendation API

**Trela** is a conversational AI-powered API built with **FastAPI** and powered by an **OpenAI agent** using **LangChain**. It recommends healthy meals based on natural language user input, supporting dietary preferences, ingredients, and budget constraints. The frontend features a modern, chat-like interface styled with **Tailwind CSS** and uses **Axios** for smooth interaction with the backend.

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-API-green" />
  <img src="https://img.shields.io/badge/OpenAI-Agent-purple" />
  <img src="https://img.shields.io/badge/TailwindCSS-UI-lightblue" />
</div>

---

## 🚀 Features

- **🍽 Smart Meal Recommendations**  
  Filter dishes by budget, ingredients, and dietary tags (e.g., `vegan`, `sem lactose`).

- **🤖 OpenAI Agent Reasoning**  
  Leverages LangChain with OpenAI’s language models for interpreting natural language input and generating relevant results.

- **🔍 Fuzzy Matching**  
  Uses `fuzzywuzzy` to tolerate typos and synonyms in user queries.

- **💬 Interactive Chat UI**  
  Chat-style frontend with quick-suggestion buttons for an intuitive experience.

- **📜 Logging**  
  Built-in debug logging to assist in development and monitoring.

- **🧱 Modular Design**  
  Organized codebase with clean separation of concerns (agents, routes, utils, UI, config).

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pedrowilian/Case_Trela.git
cd Case_Trela
```
2. Install Dependencies
Option 1: Individually
```bash
pip install fastapi uvicorn openai-agents langchain python-dotenv fuzzywuzzy python-Levenshtein pydantic nest_asyncio pyngrok
```
Option 2: With requirements.txt
```bash
pip install -r requirements.txt
```
4. Add Your OpenAI API Key
Create a .env file in the root directory:

```bash
OPENAI_API_KEY=your_openai_api_key_here
✅ .env is already listed in .gitignore and won’t be tracked by Git.
```
4. Add Menu Data
Ensure menu.json exists in the project root. If it's located elsewhere, copy it:

```bash
cp /path/to/menu.json ./menu.json

MENU_PATH: Path = Path("menu.json")

```
5. Run the App
```bash
python run.py
Then open your browser and go to: http://localhost:8000
```

💡 Usage
You can enter natural language queries into the frontend, such as:

Prato vegano até R$40

Salada com frango

Refeição leve sem lactose

The query is processed by the /recommend route, interpreted by the OpenAI agent using LangChain, and returns matching meal options from menu.json.

🗂 Project Structure
```bash
Case_Trela/
├── src/
│   ├── api/
│   │   ├── app.py                # FastAPI app setup
│   │   └── routes.py             # API endpoints
│   ├── agents/
│   │   └── meal_recommender.py   # OpenAI-based recommendation logic
│   ├── utils/
│   │   ├── menu_loader.py        # Menu parsing and validation
│   │   ├── budget_extractor.py   # Price extraction logic
│   │   └── logger.py             # Logging configuration
│   ├── config.py                 # Centralized settings
│   └── static/
│       ├── index.html            # Frontend UI
│       └── assets/               # CSS, JS, images
├── .env                          # Environment secrets (not tracked)
├── .gitignore                    # Ignored files list
├── debug.log                     # Debug output (optional)
├── menu.json                     # Menu database
├── requirements.txt              # Dependency list
├── run.py                        # App launcher
└── README.md                     # Documentation
```
