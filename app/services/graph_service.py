from app.optimizer.graph_builder import GraphBuilder
from app.optimizer.quest_engine import QuestEngine

from app.repositories.quest_dependency_repository import (
    QuestDependencyRepository,
)
from app.repositories.quest_repository import QuestRepository


class GraphService:
    """
    Charge toutes les données nécessaires pour construire
    le moteur Atlas.
    """

    def __init__(self):

        self.quest_repository = QuestRepository()
        self.dependency_repository = QuestDependencyRepository()

    def build_engine(self) -> QuestEngine:

        quests = self.quest_repository.all()

        dependencies = self.dependency_repository.all()

        graph = GraphBuilder.build(
            quests,
            dependencies,
        )

        return QuestEngine(graph)

    def close(self):

        self.quest_repository.close()
        self.dependency_repository.close()

    def __enter__(self):

        return self

    def __exit__(
        self,
        exc_type,
        exc,
        traceback,
    ):

        self.close()