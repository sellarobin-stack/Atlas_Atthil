from __future__ import annotations

from collections import deque

from app.optimizer.quest_node import QuestNode


class QuestGraph:
    """
    Graphe orienté représentant les dépendances entre les quêtes.

    Une arête :

        A -----> B

    signifie :

        B dépend de A.
    """

    def __init__(self) -> None:
        self.nodes: dict[int, QuestNode] = {}

    # -------------------------------------------------------------------------
    # Nodes
    # -------------------------------------------------------------------------

    def add_node(self, node: QuestNode) -> None:
        self.nodes[node.quest_id] = node

    def get_node(self, quest_id: int) -> QuestNode | None:
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

        required = self.get_node(required_quest_id)
        dependent = self.get_node(dependent_quest_id)

        if required is None:
            raise ValueError(
                f"Quest {required_quest_id} not found."
            )

        if dependent is None:
            raise ValueError(
                f"Quest {dependent_quest_id} not found."
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

        return sorted(
            [
                self.nodes[parent]
                for parent in node.parents
            ],
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )

    def children(self, quest_id: int) -> list[QuestNode]:

        node = self.get_node(quest_id)

        if node is None:
            return []

        return sorted(
            [
                self.nodes[child]
                for child in node.children
            ],
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )

    # -------------------------------------------------------------------------
    # Recursive navigation
    # -------------------------------------------------------------------------

    def ancestors(self, quest_id: int) -> list[QuestNode]:
        """
        Retourne tous les ancêtres d'une quête.

        Exemple :

            1
            │
            ▼
            2
            │
            ▼
            3

        ancestors(3)

        -> 1,2
        """

        visited: set[int] = set()

        queue = deque([quest_id])

        while queue:

            current = queue.popleft()

            node = self.get_node(current)

            if node is None:
                continue

            for parent in node.parents:

                if parent not in visited:

                    visited.add(parent)

                    queue.append(parent)

        return sorted(
            [
                self.nodes[parent]
                for parent in visited
            ],
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )

    def descendants(self, quest_id: int) -> list[QuestNode]:
        """
        Retourne toutes les quêtes débloquées directement
        ou indirectement.
        """

        visited: set[int] = set()

        queue = deque([quest_id])

        while queue:

            current = queue.popleft()

            node = self.get_node(current)

            if node is None:
                continue

            for child in node.children:

                if child not in visited:

                    visited.add(child)

                    queue.append(child)

        return sorted(
            [
                self.nodes[child]
                for child in visited
            ],
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )

    # -------------------------------------------------------------------------
    # Availability
    # -------------------------------------------------------------------------

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

        quests: list[QuestNode] = []

        for node in self.nodes.values():

            if node.quest_id in completed_quests:
                continue

            if self.is_available(
                node.quest_id,
                completed_quests,
            ):
                quests.append(node)

        return sorted(
            quests,
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )

    def blocked(
        self,
        completed_quests: set[int],
    ) -> list[QuestNode]:

        quests: list[QuestNode] = []

        for node in self.nodes.values():

            if node.quest_id in completed_quests:
                continue

            if not self.is_available(
                node.quest_id,
                completed_quests,
            ):
                quests.append(node)

        return sorted(
            quests,
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )

    # -------------------------------------------------------------------------
    # Graph information
    # -------------------------------------------------------------------------

    def roots(self) -> list[QuestNode]:

        return sorted(
            [
                node
                for node in self.nodes.values()
                if node.is_root
            ],
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )

    def leaves(self) -> list[QuestNode]:

        return sorted(
            [
                node
                for node in self.nodes.values()
                if node.is_leaf
            ],
            key=lambda quest: (
                quest.level,
                quest.name,
            ),
        )

    # -------------------------------------------------------------------------

    def __len__(self) -> int:
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes.values())