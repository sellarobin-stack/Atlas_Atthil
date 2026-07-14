from app.services.graph_service import GraphService

engine = GraphService().build_engine()

print(f"{len(engine.graph)} quêtes chargées")

roots = engine.graph.roots()

print(f"{len(roots)} quêtes racines")

print()

for quest in roots[:20]:
    print(quest)