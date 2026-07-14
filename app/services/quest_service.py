from app.repositories.quest_repository import QuestRepository


class QuestService:

    def list_quests(self):

        repo = QuestRepository()

        try:
            return repo.all()

        finally:
            repo.close()

    def available_quests(self):

        repo = QuestRepository()

        try:
            return repo.available()

        finally:
            repo.close()
