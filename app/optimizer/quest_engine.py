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