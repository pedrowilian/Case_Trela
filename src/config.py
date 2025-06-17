import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration settings."""
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY", "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")
    MENU_PATH: Path = Path(r"C:\Users\23.01307-9\Documents\Trela_Final\menu.json")
    LOG_FILE: str = "debug.log"
    LOG_LEVEL: str = "DEBUG"
    LOG_FORMAT: str = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_ENCODING: str = "utf-8"

    @classmethod
    def validate(cls) -> None:
        """Validate required configuration settings."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set.")
        if not cls.MENU_PATH.exists():
            raise FileNotFoundError(f"Menu file not found at {cls.MENU_PATH}")