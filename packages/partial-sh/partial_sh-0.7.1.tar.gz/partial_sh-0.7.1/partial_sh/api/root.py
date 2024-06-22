from fastapi import APIRouter

from .settings import get_settings

router = APIRouter()


@router.get("/")
def read_root():
    settings = get_settings()
    return {"message": "Welcome to the Partial API!", "settings": settings.model_dump()}
