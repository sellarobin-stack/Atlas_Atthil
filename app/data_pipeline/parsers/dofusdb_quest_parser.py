from __future__ import annotations

from app.data_pipeline.models import AtlasQuest
from app.data_pipeline.normalizers import QuestNormalizer


class DofusDbQuestParser:
    """
    Convertit une réponse brute de l'API DofusDB
    en modèle AtlasQuest.
    """

    @staticmethod
    def parse(data: dict) -> AtlasQuest:
        return QuestNormalizer.normalize(data)

    @staticmethod
    def parse_many(data: list[dict]) -> list[AtlasQuest]:
        return [
            QuestNormalizer.normalize(quest)
            for quest in data
        ]