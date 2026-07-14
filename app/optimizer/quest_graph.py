from __future__ import annotations

from app.optimizer.quest_node import QuestNode


class QuestGraph:
    """
    Graphe orienté représentant les dépendances entre les quêtes.

    Chaque noeud est une quête.
    Une arête A -> B signifie :
        B dépend de A.
    """

    def __init__(self) -> None:
        self.nodes: dict[int, QuestNode] = {}

    # -------------------------------------------------------------------------
    # Nodes
    # -------------------------------------------------------------------------

    def add_node(self, node: QuestNode) -> None:
        """Ajoute un noeud au graphe."""
        self.nodes[node.quest_id] = node

    def get_node(self, quest_id: int) -> QuestNode | None:
        """Retourne un noeud ou None."""
        return self.nodes.get(quest_id)

    def has_node(self, quest_id: int) -> bool:
        return quest_id in self.nodes

    # -------------------------------------------------------------------------
    # Dependencies
    # -------------------------------------------------------------------------

    def add_dependency(
        self,
        required_quest_id: int,
        dependent_quest_id: int,
    ) -> None:
        """
        Ajoute une dépendance.

        required -----> dependent
        """

        required = self.get_node(required_quest_id)
        dependent = self.get_node(dependent_quest_id)

        if required is None:
            raise ValueError(
                f"Quest {required_quest_id} not found in graph."
            )

        if dependent is None:
            raise ValueError(
                f"Quest {dependent_quest_id} not found in graph."
            )

        required.children.add(dependent.quest_id)
        dependent.parents.add(required.quest_id)

    # -------------------------------------------------------------------------
    # Navigation
    # -------------------------------------------------------------------------

    def parents(self, quest_id: int) -> list[QuestNode]:
        node = self.get_node(quest_id)

        if node is None:
            return []

        return [
            self.nodes[parent_id]
            for parent_id in node.parents
        ]

    def children(self, quest_id: int) -> list[QuestNode]:
        node = self.get_node(quest_id)

        if node is None:
            return []

        return [
            self.nodes[child_id]
            for child_id in node.children
        ]

    # -------------------------------------------------------------------------
    # Graph information
    # -------------------------------------------------------------------------

    def roots(self) -> list[QuestNode]:
        """
        Retourne les quêtes sans prérequis.
        """
        return [
            node
            for node in self.nodes.values()
            if not node.parents
        ]

    def leaves(self) -> list[QuestNode]:
        """
        Retourne les quêtes qui ne débloquent aucune autre quête.
        """
        return [
            node
            for node in self.nodes.values()
            if not node.children
        ]

    def __len__(self) -> int:
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes.values())
    
    def is_available(
        self,
        quest_id: int,
        completed_quests: set[int],
    ) -> bool:

        node = self.get_node(quest_id)

        if node is None:
            return False

        return node.parents.issubset(completed_quests)
    
    def available(
        self,
        completed_quests: set[int],
    ) -> list[QuestNode]:

        available = []

        for node in self.nodes.values():

            if node.quest_id in completed_quests:
                continue

            if self.is_available(
                node.quest_id,
                completed_quests,
            ):
                available.append(node)

        return sorted(
            available,
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )
    
    def blocked(
        self,
        completed_quests: set[int],
    ) -> list[QuestNode]:

        blocked = []

        for node in self.nodes.values():

            if node.quest_id in completed_quests:
                continue

            if not self.is_available(
                node.quest_id,
                completed_quests,
            ):
                blocked.append(node)

        return sorted(
            blocked,
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )