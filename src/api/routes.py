import json
import re
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from agents import Runner
from src.agents.meal_recommender import create_meal_recommender
from src.utils.logger import get_logger
from pathlib import Path

logger = get_logger(__name__)
router = APIRouter()

try:
    meal_agent = create_meal_recommender()
    logger.info("Meal recommender agent initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize meal agent: {str(e)}", exc_info=True)
    raise RuntimeError(f"Agent initialization failed: {str(e)}")

# Load HTML content from file
HTML_CONTENT = Path("src/static/index.html").read_text(encoding="utf-8")

class UserRequest(BaseModel):
    """User query for meal recommendations."""
    query: str

class Meal(BaseModel):
    """Menu item model."""
    nome: str
    preco: float
    descricao: str
    tags: List[str]
    popularity: float = Field(default=0.5)

class RecommendationResponse(BaseModel):
    """Response model for meal recommendations."""
    recommendations: List[Meal]
    message: Optional[str]

@router.get("/", response_class=HTMLResponse)
async def serve_ui():
    """Serve the frontend UI."""
    return HTML_CONTENT

@router.post("/recommend", response_model=RecommendationResponse)
async def recommend_meal(request: UserRequest):
    """
    Recommend meals based on user query.

    Args:
        request: User query request.

    Returns:
        Recommended meals and message.

    Raises:
        HTTPException: If query is empty or server error occurs.
    """
    try:
        query = request.query.strip()
        if not query:
            raise HTTPException(status_code=400, detail="Query cannot be empty.")

        logger.debug(f"Processing query: {query}")
        output = await Runner.run(starting_agent=meal_agent, input=query)
        logger.debug(f"Agent output: {output}")

        if not hasattr(output, 'final_output') or output.final_output is None:
            logger.error("Agent returned no output.")
            return RecommendationResponse(
                recommendations=[],
                message="Unable to process request. Please try again."
            )

        raw_output = output.final_output
        result = (
            raw_output if isinstance(raw_output, dict) else
            json.loads(re.sub(r'```(?:json)?\s*?\n|\n```\s*?$', '', raw_output.strip()))
        )

        recommendations = [
            Meal(**item) for item in result.get("recommendations", [])
            if all(field in item for field in ["nome", "preco", "descricao", "tags"])
        ]
        message = result.get("message", "No recommendations found.")

        logger.info(f"Returning {len(recommendations)} recommendations.")
        return RecommendationResponse(recommendations=recommendations, message=message)

    except HTTPException:
        raise
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error: {e}", exc_info=True)
        return RecommendationResponse(
            recommendations=[],
            message="Error processing request. Please try again."
        )
    except Exception as e:
        logger.error(f"Server error processing query '{query}': {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")