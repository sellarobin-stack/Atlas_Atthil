from sqlalchemy import select

from app.database.models import Quest
from app.database.session import SessionLocal
from app.database.models import QuestDependency


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

    def close(self):
        self.db.close()

    def dependencies(self, quest_id: int):

        return self.db.query(QuestDependency).filter(
        QuestDependency.quest_id == quest_id
    ).all()


def by_id(self, quest_id: int):

    return self.db.get(Quest, quest_id)