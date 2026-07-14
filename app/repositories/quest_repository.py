from sqlalchemy import select

from app.database.models import Quest, QuestDependency
from app.database.session import SessionLocal


class QuestRepository:

    def __init__(self):
        self.db = SessionLocal()

    def all(self):

        return self.db.scalars(
            select(Quest).order_by(Quest.level)
        ).all()

    def by_ankama_id(self, ankama_id: int):

        return self.db.scalar(
            select(Quest).where(
                Quest.ankama_id == ankama_id
            )
        )

    def by_id(self, quest_id: int):

        return self.db.get(Quest, quest_id)

    def dependencies(self, quest_id: int):

        return (
            self.db.query(QuestDependency)
            .filter(
                QuestDependency.quest_id == quest_id
            )
            .all()
        )

    def close(self):

        self.db.close()

    def available(self):

        return [
            quest
            for quest in self.all()
            if len(quest.dependencies) == 0
    ]

    def by_level(self, level: int):

        return self.db.scalars(
            select(Quest)
            .where(Quest.level <= level)
            .order_by(Quest.level)
        ).all()


    def by_campaign(self, campaign_id: int):

        return self.db.scalars(
            select(Quest)
            .where(Quest.campaign_id == campaign_id)
            .order_by(Quest.level)
        ).all()