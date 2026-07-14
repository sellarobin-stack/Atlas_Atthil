from app.services.quest_service import QuestService

service = QuestService()

quests = service.available_quests()

print("Quêtes disponibles :")

for quest in quests:
    print(f"- {quest.name}")