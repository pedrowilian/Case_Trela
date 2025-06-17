import json
from functools import lru_cache
from typing import List, Dict, Any
from src.utils.logger import get_logger
from src.config import Config

logger = get_logger(__name__)

@lru_cache(maxsize=1)
def load_menu() -> List[Dict[str, Any]]:
    """
    Load and validate menu from JSON file with caching.

    Returns:
        List of menu items, each containing required fields.

    Raises:
        FileNotFoundError: If menu file is missing.
        ValueError: If JSON is invalid or menu items are malformed.
    """
    try:
        with open(Config.MENU_PATH, "r", encoding="utf-8") as f:
            menu = json.load(f)
        logger.info(f"Loaded {len(menu)} menu items from {Config.MENU_PATH}")

        for item in menu:
            required_fields = ["nome", "preco", "descricao", "tags"]
            if not all(field in item for field in required_fields):
                logger.error(f"Invalid menu item: {item}. Missing required fields.")
                raise ValueError(f"Invalid menu item: {item}. Missing required fields.")
            if not isinstance(item["tags"], list):
                logger.warning(f"Tags invalid for item: {item['nome']}. Setting to empty list.")
                item["tags"] = []
            item.setdefault("popularity", 0.5)
        return menu
    except FileNotFoundError:
        logger.error(f"Menu file not found at {Config.MENU_PATH}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in menu file: {e}")
        raise ValueError("Invalid JSON format in menu file")
    except Exception as e:
        logger.error(f"Unexpected error loading menu: {e}", exc_info=True)
        raise