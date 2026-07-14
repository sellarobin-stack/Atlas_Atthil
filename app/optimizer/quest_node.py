from dataclasses import dataclass, field


@dataclass(slots=True)
class QuestNode:
    """
    Représente une quête dans le graphe d'Atlas.

    Chaque nœud connaît :
        - ses quêtes parentes (prérequis)
        - ses quêtes enfants (débloquées)
    """

    quest_id: int
    name: str
    level: int

    parents: set[int] = field(default_factory=set)
    children: set[int] = field(default_factory=set)

    @property
    def is_root(self) -> bool:
        """
        Une quête racine ne possède aucun prérequis.
        """
        return len(self.parents) == 0

    @property
    def is_leaf(self) -> bool:
        """
        Une feuille ne débloque aucune autre quête.
        """
        return len(self.children) == 0

    @property
    def parents_count(self) -> int:
        """
        Nombre de prérequis.
        """
        return len(self.parents)

    @property
    def children_count(self) -> int:
        """
        Nombre de quêtes débloquées.
        """
        return len(self.children)

    def __repr__(self) -> str:
        return (
            f"QuestNode("
            f"id={self.quest_id}, "
            f"name='{self.name}', "
            f"level={self.level})"
        )