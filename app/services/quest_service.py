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
    def quests_by_level(self, level: int):

        repo = QuestRepository()

        try:
            return repo.by_level(level)

        finally:
            repo.close()


    def quests_by_campaign(self, campaign_id: int):

        repo = QuestRepository()

        try:
            return repo.by_campaign(campaign_id)

        finally:
            repo.close()