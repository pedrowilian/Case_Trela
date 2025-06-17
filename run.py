import os
import uvicorn
import logging
from src.config import Config
from src.api.app import create_app
from src.api.routes import router

def main():
    """Run the FastAPI server."""
    Config.validate()
    # Set OPENAI_API_KEY in environment to suppress warnings
    if Config.OPENAI_API_KEY:
        os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY
    else:
        logging.error("OPENAI_API_KEY is not set in Config.")
        raise ValueError("OPENAI_API_KEY is not set.")
    
    app = create_app()
    app.include_router(router)
    
    print("Trela - Recomendacoes Saudaveis API is running at http://localhost:8000/")
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")

if __name__ == "__main__":
    main()