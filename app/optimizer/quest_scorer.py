from app.optimizer.quest_engine import QuestEngine
from app.optimizer.quest_node import QuestNode
from app.optimizer.quest_score import QuestScore


class QuestScorer:
    """
    Premier système de notation d'Atlas.

    Cette classe calcule uniquement un score.

    Elle ne choisit jamais une quête.
    """

    def __init__(self, engine: QuestEngine):

        self.engine = engine

    def score(
        self,
        quest: QuestNode,
    ) -> QuestScore:

        unlocked = self.engine.unlocks(
            quest.quest_id,
        )

        descendants = self.engine.unlock_tree(
            quest.quest_id,
        )

        score = 0

        # ------------------------------------------------------------------
        # Débloque directement des quêtes
        # ------------------------------------------------------------------

        score += len(unlocked) * 10

        # ------------------------------------------------------------------
        # Débloque une grosse partie de la campagne
        # ------------------------------------------------------------------

        score += len(descendants) * 2

        # ------------------------------------------------------------------
        # Quête racine
        # ------------------------------------------------------------------

        if quest.is_root:
            score += 5

        # ------------------------------------------------------------------
        # Les feuilles rapportent moins
        # ------------------------------------------------------------------

        if quest.is_leaf:
            score -= 2

        return QuestScore(
            quest=quest,
            score=score,
            unlocked_quests=len(unlocked),
            descendants=len(descendants),
            is_root=quest.is_root,
            is_leaf=quest.is_leaf,
        )

    def score_all(
        self,
        quests: list[QuestNode],
    ) -> list[QuestScore]:

        scores = [
            self.score(quest)
            for quest in quests
        ]

        return sorted(
            scores,
            key=lambda score: score.score,
            reverse=True,
        )