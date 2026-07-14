from app.optimizer.graph_builder import GraphBuilder
from app.optimizer.quest_engine import QuestEngine

from app.repositories.quest_repository import QuestRepository
from app.repositories.quest_dependency_repository import (
    QuestDependencyRepository,
)


class GraphService:
    """
    Construit le moteur Atlas à partir de la base.
    """

    def build_engine(self) -> QuestEngine:

        quest_repo = QuestRepository()
        dependency_repo = QuestDependencyRepository()

        try:

            quests = quest_repo.all()
            dependencies = dependency_repo.all()

            graph = GraphBuilder.build(
                quests,
                dependencies,
            )

            return QuestEngine(graph)

        finally:

            quest_repo.close()
            dependency_repo.close()