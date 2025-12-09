from fastapi import APIRouter

# Every new tool MUST use APIRouter, not FastAPI
router = APIRouter(
    prefix="/health",
    tags=["System Health"]
)

@router.get("/ping")
def ping_server():
    return {"ping": "pong", "system": "nominal"}