import logging
from src.config import Config

def get_logger(name: str) -> logging.Logger:
    """
    Configure and return a logger instance.

    Args:
        name: Name of the logger (usually __name__).

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.FileHandler(Config.LOG_FILE, encoding=Config.LOG_ENCODING)
        handler.setFormatter(logging.Formatter(Config.LOG_FORMAT))
        logger.setLevel(Config.LOG_LEVEL)
        logger.addHandler(handler)
    return logger