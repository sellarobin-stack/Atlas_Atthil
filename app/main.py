from fastapi import FastAPI

from app.api.campaigns import router as campaign_router
from app.api.quests import router as quest_router
from app.api.router import router
from app.core.config import APP_NAME, VERSION


app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description="Optimiseur de progression Dofus",
    contact={
        "name": "Robin Sella",
    },
)

app.include_router(router)
app.include_router(campaign_router)
app.include_router(quest_router)