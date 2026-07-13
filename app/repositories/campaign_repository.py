from sqlalchemy import select

from app.database.models import Campaign
from app.database.session import SessionLocal


class CampaignRepository:

    def __init__(self):
        self.db = SessionLocal()

    def all(self):

        return self.db.scalars(
            select(Campaign).order_by(Campaign.name)
        ).all()

    def by_code(self, code: str):

        return self.db.scalar(
            select(Campaign).where(
                Campaign.code == code
            )
        )

    def close(self):

        self.db.close()