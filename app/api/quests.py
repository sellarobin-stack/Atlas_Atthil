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

    return service.available_quests()

@router.get("/level/{level}")
def quests_by_level(level: int):

    service = QuestService()

    return service.quests_by_level(level)


@router.get("/campaign/{campaign_id}")
def quests_by_campaign(campaign_id: int):

    service = QuestService()

    return service.quests_by_campaign(campaign_id)