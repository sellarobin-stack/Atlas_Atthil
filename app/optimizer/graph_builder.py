from app.database.models.quest import Quest
from app.database.models.quest_dependency import QuestDependency

from app.optimizer.quest_graph import QuestGraph
from app.optimizer.quest_node import QuestNode


class GraphBuilder:
    """
    Construit un QuestGraph à partir des objets SQLAlchemy.
    """

    @staticmethod
    def build(
        quests: list[Quest],
        dependencies: list[QuestDependency],
    ) -> QuestGraph:

        graph = QuestGraph()

        # Création des noeuds
        for quest in quests:

            graph.add_node(
                QuestNode(
                    quest_id=quest.id,
                    name=quest.name,
                    level=quest.level,
                )
            )

        # Création des dépendances
        for dependency in dependencies:

            graph.add_dependency(
                required_quest_id=dependency.required_quest_id,
                dependent_quest_id=dependency.quest_id,
            )

        return graph