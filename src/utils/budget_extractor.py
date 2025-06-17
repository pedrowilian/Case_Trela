import re
from typing import Optional
from src.utils.logger import get_logger

logger = get_logger(__name__)

def extract_budget(query: str) -> Optional[float]:
    """
    Extract numerical budget from user query using regex patterns.

    Args:
        query: User input query string.

    Returns:
        Extracted budget as float, or None if no budget is found.
    """
    patterns = [
        r'até\s*r?\$?\s*(\d+[,.]?\d*)',
        r'menos\s*de\s*r?\$?\s*(\d+[,.]?\d*)',
        r'por\s*r?\$?\s*(\d+[,.]?\d*)',
        r'r?\$?\s*(\d+[,.]?\d*)'
    ]
    for pattern in patterns:
        match = re.search(pattern, query.lower(), re.IGNORECASE)
        if match:
            try:
                budget = float(match.group(1).replace(',', '.'))
                logger.debug(f"Extracted budget: {budget} from query: {query}")
                return budget
            except ValueError:
                logger.warning(f"Invalid budget format in match: {match.group(1)}")
                continue
    logger.debug(f"No budget found in query: {query}")
    return None