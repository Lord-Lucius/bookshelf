from fastapi import APIRouter

router = APIRouter(prefix="/info", tags=["health"])

@router.get("/health")
async def health_check():
    return {"healthcheck": "successed"}
