from app.services.graph_service import GraphService


def print_separator():
    print("-" * 60)


def main():

    with GraphService() as service:

        engine = service.build_engine()

    graph = engine.graph

    print()
    print("========== ATLAS GRAPH ==========")
    print()

    print(f"Quêtes chargées       : {len(graph)}")
    print(f"Quêtes racines        : {len(graph.roots())}")
    print(f"Quêtes feuilles       : {len(graph.leaves())}")

    print_separator()

    available = engine.available(set())

    print(f"Quêtes disponibles au départ : {len(available)}")
    print()

    for quest in available[:10]:
        print(f"[{quest.level}] {quest.name}")

    print_separator()

    completed = {
        quest.quest_id
        for quest in available
    }

    next_available = engine.available(completed)

    print("Après avoir terminé les premières quêtes :")
    print()

    for quest in next_available[:10]:
        print(f"[{quest.level}] {quest.name}")

    print_separator()

    print(
        f"Progression : "
        f"{engine.completion_rate(completed)} %"
    )

    print(
        f"Quêtes restantes : "
        f"{engine.remaining(completed)}"
    )

    print()
    print("=================================")


if __name__ == "__main__":
    main()