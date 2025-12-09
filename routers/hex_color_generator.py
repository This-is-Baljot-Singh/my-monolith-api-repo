from fastapi import APIRouter
import random

router = APIRouter(prefix="/hexcolor", tags=["HexColorGenerator"])

@router.get("/generate")
async def generate_hex_color():
    """Generate a random hex color code."""
    hex_color = "#" + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
    return {"hex_color": hex_color}
