from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["System"])
def health():

    return {
        "application": "Atlas d'Atthil",
        "status": "running",
        "version": "0.1.0",
    }