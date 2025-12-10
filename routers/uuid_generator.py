from fastapi import APIRouter
import uuid

router = APIRouter(prefix="/uuid_generator", tags=["UUID Generator"])

@router.get("/generate")
def generate_uuid():
    """Generate a random UUID4."""
    return {"uuid": str(uuid.uuid4())}
