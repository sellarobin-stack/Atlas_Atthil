from fastapi import FastAPI

from backend.api.router import router
from backend.core.config import APP_NAME, VERSION

app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description="Optimiseur de progression des campagnes Dofus",
)

app.include_router(router)