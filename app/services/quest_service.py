from app.repositories.quest_repository import QuestRepository


class QuestService:

    def list_quests(self):

        repo = QuestRepository()

        quests = repo.all()

        repo.close()

        return quests
    
    def available_quests(
    self,
    completed_quests: set[int],
):

        repo = QuestRepository()

        available = []

        quests = repo.all()

        for quest in quests:

            dependencies = repo.dependencies(quest.id)

        if all(
            dependency.required_quest_id in completed_quests
            for dependency in dependencies
        ):
            available.append(quest)

        repo.close()

        return available