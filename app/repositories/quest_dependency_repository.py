from sqlalchemy import select

from app.database.models.quest_dependency import QuestDependency
from app.database.session import SessionLocal


class QuestDependencyRepository:

    def __init__(self):

        self.db = SessionLocal()

    def all(self):

        return self.db.scalars(
            select(QuestDependency)
        ).all()

    def close(self):

        self.db.close()