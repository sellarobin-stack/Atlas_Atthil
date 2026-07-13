from fastapi import APIRouter

from app.services.campaign_service import CampaignService

router = APIRouter(
    prefix="/campaigns",
    tags=["Campaigns"],
)


@router.get("")
def list_campaigns():

    service = CampaignService()

    return service.list_campaigns()