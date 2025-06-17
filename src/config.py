import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration settings."""
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    MENU_PATH: Path = Path(r"C:\Users\23.01307-9\Documents\Trela_Final\menu.json")
    LOG_FILE: str = "debug.log"
    LOG_LEVEL: str = "DEBUG"
    LOG_FORMAT: str = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_ENCODING: str = "utf-8"

    @classmethod
    def validate(cls) -> None:
        """Validate required configuration settings."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it in a .env file.")
        if not cls.MENU_PATH.exists():
            raise FileNotFoundError(f"Menu file not found at {cls.MENU_PATH}")