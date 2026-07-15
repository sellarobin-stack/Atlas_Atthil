from dataclasses import dataclass

from app.optimizer.quest_node import QuestNode


@dataclass(slots=True, frozen=True)
class QuestScore:
    """
    Résultat du calcul de score d'une quête.
    """

    quest: QuestNode

    score: int

    unlocked_quests: int

    descendants: int

    is_root: bool

    is_leaf: bool