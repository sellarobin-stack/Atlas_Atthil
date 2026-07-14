from app.optimizer.quest_graph import QuestGraph
from app.optimizer.quest_node import QuestNode


class QuestEngine:
    """
    Contient la logique métier d'Atlas.

    Le QuestGraph stocke les données.

    Le QuestEngine prend les décisions.
    """

    def __init__(self, graph: QuestGraph):

        self.graph = graph

    def available(
        self,
        completed_quests: set[int],
    ) -> list[QuestNode]:

        return self.graph.available(completed_quests)

    def blocked(
        self,
        completed_quests: set[int],
    ) -> list[QuestNode]:

        return self.graph.blocked(completed_quests)
    def missing_requirements(
        self,
        quest_id: int,
        completed_quests: set[int],
    ) -> list[QuestNode]:

        node = self.graph.get_node(quest_id)

        if node is None:
            return []

        return [
            self.graph.get_node(parent_id)
            for parent_id in sorted(node.parents)
            if parent_id not in completed_quests
        ]
    
    def unlocks(
        self,
        quest_id: int,
    ) -> list[QuestNode]:

        node = self.graph.get_node(quest_id)

        if node is None:
            return []

        return sorted(
            [
                self.graph.get_node(child_id)
                for child_id in node.children
            ],
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )
    
    def is_completed(
        self,
        quest_id: int,
        completed_quests: set[int],
    ) -> bool:

        return quest_id in completed_quests