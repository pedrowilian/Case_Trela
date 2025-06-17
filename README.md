🥗 Trela — Healthy Meals Recommendation API
Trela is a FastAPI-based web application that recommends healthy meals based on user preferences — including budget, dietary restrictions, and ingredients. It features a conversational UI and intelligent query processing using LangChain and fuzzy matching.

<div align="center"> <img src="https://img.shields.io/badge/FastAPI-API-green" /> <img src="https://img.shields.io/badge/LangChain-Agent-blue" /> <img src="https://img.shields.io/badge/TailwindCSS-UI-lightblue" /> <img src="https://img.shields.io/badge/License-MIT-yellow" /> </div>
🚀 Features
🍽 Meal Recommendations
Filter meals by budget, keywords (e.g., "frango", "salada"), and dietary tags (e.g., vegan, lactose-free).

🔍 Fuzzy Matching
Uses fuzzywuzzy to handle synonyms and typos for more flexible querying.

🧠 Agent-Based Reasoning
Incorporates LangChain for natural language query parsing and intelligent meal suggestions.

💬 Interactive UI
Chat-like frontend with quick-access suggestion buttons, styled with Tailwind CSS.

📜 Logging
Debug-level logging included for easier development and troubleshooting.

🧱 Modular Architecture
Clean, modular design with well-separated concerns: API, agents, utilities, and configuration.

⚙️ Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/pedrowilian/Case_Trela.git
cd Case_Trela
2. Install Dependencies
Option 1: Individually
bash
Copy
Edit
pip install fastapi uvicorn openai-agents langchain python-dotenv fuzzywuzzy python-Levenshtein pydantic nest_asyncio pyngrok
Option 2: Using requirements.txt
bash
Copy
Edit
pip install -r requirements.txt
3. Configure API Key
Create a .env file in the root directory:

bash
Copy
Edit
touch .env
Add your OpenAI key:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
Ensure the .env file is excluded from version control (it's already listed in .gitignore).

4. Prepare Menu Data
Ensure menu.json is in the project root.

If not, copy it from your original location:

bash
Copy
Edit
cp /path/to/menu.json ./menu.json
Update the path in src/config.py:

python
Copy
Edit
MENU_PATH: Path = Path("menu.json")
5. Run the App
bash
Copy
Edit
python run.py
Then open your browser at http://localhost:8000

💡 Usage
In the UI, type natural language queries like:

Prato vegano até R$40

Salada com frango

Algo sem lactose com peixe

The API routes the query to /recommend, processes it using LangChain and fuzzy matching, and returns a list of matching meals from menu.json.

🗂 Project Structure
bash
Copy
Edit
Case_Trela/
├── src/
│   ├── api/
│   │   ├── app.py                # FastAPI application setup
│   │   └── routes.py             # API endpoints
│   ├── agents/
│   │   └── meal_recommender.py   # LangChain agent logic
│   ├── utils/
│   │   ├── menu_loader.py        # Menu loading and schema validation
│   │   ├── budget_extractor.py   # Budget parsing from queries
│   │   └── logger.py             # Logging setup
│   ├── config.py                 # Global configuration
│   └── static/
│       ├── index.html            # Chat UI frontend
│       └── assets/               # Tailwind CSS and JS files
├── .env                          # Secret keys (not tracked)
├── .gitignore                    # Files ignored by Git
├── debug.log                     # Application logs (not tracked)
├── menu.json                     # Menu data source
├── requirements.txt              # Dependency list
├── run.py                        # Entry point
└── README.md                     # Project documentation
🤝 Contributing
Pull requests and feedback are welcome! Please open an issue to discuss changes or bugs.
