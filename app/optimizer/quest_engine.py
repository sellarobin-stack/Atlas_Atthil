from app.optimizer.quest_graph import QuestGraph
from app.optimizer.quest_node import QuestNode


class QuestEngine:
    """
    Moteur métier d'Atlas.

    Le QuestGraph représente les données.

    Le QuestEngine prend les décisions.
    """

    def __init__(self, graph: QuestGraph):

        self.graph = graph

    # -------------------------------------------------------------------------
    # Availability
    # -------------------------------------------------------------------------

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

    # -------------------------------------------------------------------------
    # Completion
    # -------------------------------------------------------------------------

    @staticmethod
    def is_completed(
        quest_id: int,
        completed_quests: set[int],
    ) -> bool:

        return quest_id in completed_quests

    # -------------------------------------------------------------------------
    # Requirements
    # -------------------------------------------------------------------------

    def missing_requirements(
        self,
        quest_id: int,
        completed_quests: set[int],
    ) -> list[QuestNode]:
        """
        Retourne tous les prérequis manquants
        (parents directs et indirects).
        """

        missing = []

        for node in self.graph.ancestors(quest_id):

            if node.quest_id not in completed_quests:
                missing.append(node)

        return missing

    # -------------------------------------------------------------------------
    # Unlocks
    # -------------------------------------------------------------------------

    def unlocks(
        self,
        quest_id: int,
    ) -> list[QuestNode]:
        """
        Retourne les quêtes débloquées directement
        après avoir terminé cette quête.
        """

        return self.graph.children(quest_id)

    def unlock_tree(
        self,
        quest_id: int,
    ) -> list[QuestNode]:
        """
        Retourne toutes les quêtes débloquées
        directement ou indirectement.
        """

        return self.graph.descendants(quest_id)

    # -------------------------------------------------------------------------
    # Statistics
    # -------------------------------------------------------------------------

    def completion_rate(
        self,
        completed_quests: set[int],
    ) -> float:
        """
        Pourcentage de progression.
        """

        total = len(self.graph)

        if total == 0:
            return 0.0

        return round(
            len(completed_quests) / total * 100,
            2,
        )

    def remaining(
        self,
        completed_quests: set[int],
    ) -> int:
        """
        Nombre de quêtes restantes.
        """

        return len(self.graph) - len(completed_quests)