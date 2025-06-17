Trela Healthy Meals Recommendation API
Trela is a FastAPI-based API that recommends healthy meals based on user queries, supporting dietary preferences, ingredients, and budget constraints. The application features a user-friendly interface built with Tailwind CSS and Axios for seamless API interactions.
Features

Meal Recommendations: Filter menu items by budget, dietary tags (e.g., vegan, lactose-free), and keywords (e.g., "frango", "salada").
Fuzzy Matching: Uses fuzzywuzzy for robust query matching to handle synonyms and misspellings.
Interactive UI: Provides a chat-like interface with quick suggestion buttons.
Logging: Comprehensive debug logging for development and troubleshooting.
Modular Design: Organized codebase with separate modules for configuration, utilities, agents, and API routes.

Installation

Clone the repository:git clone https://github.com/pedrowilian/Case_Trela.git
cd Case_Trela


Install dependencies:pip install -r requirements.txt


Set up the OpenAI API key:
Create a .env file in the project root.
Add your OpenAI API key (obtain one from OpenAI):OPENAI_API_KEY=your_openai_api_key_here


Ensure .env is not committed to version control (it’s excluded by .gitignore).


Ensure menu.json is available at the path specified in src/config.py (default: C:\Users\23.01307-9\Documents\Trela_Final\menu.json). For portability, copy menu.json to the project root and update src/config.py to:MENU_PATH: Path = Path("menu.json")


Run the application:python run.py


Open http://localhost:8000/ in your browser.

Usage

Enter queries like “Prato vegano até R$40” or “Salada com frango” in the UI.
The API processes queries via the /recommend endpoint, returning filtered meal recommendations.

Project Structure
Case_Trela/
├── src/
│   ├── api/
│   │   ├── app.py          # FastAPI application setup
│   │   └── routes.py       # API routes
│   ├── agents/
│   │   └── meal_recommender.py  # Meal recommendation agent
│   ├── utils/
│   │   ├── menu_loader.py       # Menu loading and validation
│   │   ├── budget_extractor.py  # Budget extraction logic
│   │   └── logger.py           # Logging configuration
│   ├── config.py           # Configuration settings
│   └── static/
│       ├── index.html      # Frontend UI
│       └── assets/         # CSS, JS, and other static files
├── .env                    # Environment variables (not tracked)
├── .gitignore              # Git ignore rules
├── debug.log               # Debug logs (not tracked)
├── menu.json               # Menu data
├── requirements.txt        # Python dependencies
├── run.py                  # Application entry point
└── README.md               # Project documentation

Contributing
Contributions are welcome! Please submit issues or pull requests on GitHub.
License
This project is licensed under the MIT License.
