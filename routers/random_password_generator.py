from fastapi import APIRouter, Query
import random
import string

router = APIRouter(prefix="/random_password", tags=["Random Password Generator"])

@router.get("/generate")
def generate_password(length: int = Query(12, ge=6, le=64, description="Length of the password"), use_special: bool = Query(True, description="Include special characters")):
    """Generate a secure random password"""
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation
    password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))
    return {"password": password}
