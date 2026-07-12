from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "application": "Atlas d'Atthil",
        "status": "running",
        "version": "0.1.0",
    }