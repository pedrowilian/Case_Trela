Trela Healthy Meals Recommendation API
Trela is a FastAPI-based API that recommends healthy meals based on user queries, supporting dietary preferences, ingredients, and budget constraints. The application features a user-friendly interface built with Tailwind CSS and Axios for seamless API interactions.
Features

Meal Recommendations: Filter menu items by budget, dietary tags (e.g., vegan, lactose-free), and keywords (e.g., "frango", "salada").
Fuzzy Matching: Uses fuzzywuzzy for robust query matching to handle synonyms and misspellings.
Interactive UI: Provides a chat-like interface with quick suggestion buttons.
Logging: Comprehensive debug logging for development and troubleshooting.
Modular Design: Organized codebase with separate modules for configuration, utilities, agents, and API routes.

Project Structure
trela-recommendations/
├── src/
│   ├── config.py           # Configuration settings
│   ├── utils/             # Utility functions
│   │   ├── menu_loader.py       # Menu loading and validation
│   │   ├── budget_extractor.py # Budget extraction logic
│   │   └── logger.py           # Logging configuration
│   ├── agents/            # Agent definitions and tools
│   │   ├── meal_recommender.py  # Meal recommendation agent
│   │   └── tools.py            # Filter and extraction tools
│   ├── api/               # FastAPI application and routes
│   │   ├── app.py              # FastAPI app setup
│   │   └── routes.py          # API endpoints
│   └── static/            # Static frontend files
│       └── index.html         # Frontend UI
├── run.py                # Entry point to run the server
├── README.md              # Project documentation
├── requirements.txt            # Dependencies
└── .gitignore             # Git ignore patterns

Installation

Clone the repository:
git clone https://github.com/yourusername/trela-recommendations.git
cd trela-recommendations


Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Configure environment variables:

Set OPENAI_API_KEY in your environment or a .env file.
Update MENU_PATH in src/config.py to point to your menu.json.


Run the application:
python run.py

The API will be available at http://localhost:8000/.


Usage

Access the UI: Open http://localhost:8000/ in your browser to interact with the chat interface.
API Endpoint: Send POST requests to /recommend with a JSON payload:{
  "query": "Prato vegano até R$40"
}


Example Queries:
"Prato mais barato"
"Almoço sem lactose"
"Prato picante com proteína"



Dependencies
See requirements.txt for a complete list. Key dependencies include:

fastapi: API framework
uvicorn: ASGI server
fuzzywuzzy: Fuzzy string matching
pydantic: Data validation
agents: Custom agent framework (ensure compatibility)

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License
MIT License. See LICENSE for details.
Contact
For issues or questions, please open an issue on GitHub.
