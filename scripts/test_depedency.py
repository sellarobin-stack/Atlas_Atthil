from app.services.graph_service import GraphService

engine = GraphService().build_engine()

completed = set()

quest = engine.available(completed)[0]

print(f"Quête : {quest.name}")

print()

print("Prérequis manquants :")

for parent in engine.missing_requirements(
    quest.quest_id,
    completed,
):
    print(parent.name)

print()

print("Débloque :")

for child in engine.unlocks(quest.quest_id):
    print(child.name)