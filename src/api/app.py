from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import Config

def create_app() -> FastAPI:
    """
    Create and configure FastAPI application.

    Returns:
        Configured FastAPI instance.
    """
    app = FastAPI(
        title="Trela Healthy Meals API",
        description="API for recommending healthy meals based on user preferences.",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app