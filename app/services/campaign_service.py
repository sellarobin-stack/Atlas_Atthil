from app.repositories.campaign_repository import CampaignRepository


class CampaignService:

    def list_campaigns(self):

        repo = CampaignRepository()

        campaigns = repo.all()

        repo.close()

        return campaigns