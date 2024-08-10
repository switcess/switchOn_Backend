from fastapi import APIRouter # type: ignore

router = APIRouter(
    prefix="/health",
    tags=["health"]
)

@router.get("/")
def healthCheck():
    return {"Hello": "World"}