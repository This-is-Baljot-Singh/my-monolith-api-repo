from fastapi import APIRouter, Query
import random

router = APIRouter(prefix="/random_number", tags=["Random Number Generator"])

@router.get("/generate")
async def generate_random_number(min: int = Query(0, description="Minimum value, inclusive"), max: int = Query(100, description="Maximum value, inclusive")):
    """Generate a random integer between min and max (inclusive)."""
    if min > max:
        return {"error": "min must be less than or equal to max"}
    number = random.randint(min, max)
    return {"random_number": number}
