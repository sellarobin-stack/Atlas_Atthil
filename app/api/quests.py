from fastapi import APIRouter

from app.services.quest_service import QuestService

router = APIRouter(
    prefix="/quests",
    tags=["Quests"],
)


@router.get("")
def list_quests():

    service = QuestService()

    return service.list_quests()

@router.get("/available")
def available():

    service = QuestService()

    return service.available_quests(set())