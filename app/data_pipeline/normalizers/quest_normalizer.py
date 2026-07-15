from __future__ import annotations

from app.data_pipeline.models.atlas_quest import AtlasQuest


class QuestNormalizer:
    """
    Transforme une quête provenant d'une source externe
    (DofusDB, Ankama, etc.) en AtlasQuest.
    """

    @staticmethod
    def normalize(data: dict) -> AtlasQuest:

        return AtlasQuest(
            id=data["id"],
            name=data["name"],
            level=data.get("level", 1),
            campaign=data.get("campaign"),

            zone_id=data.get("zone_id"),
            map_id=data.get("map_id"),

            repeatable=data.get("repeatable", False),

            prerequisites=QuestNormalizer._extract_prerequisites(data),
            steps=QuestNormalizer._extract_steps(data),
            rewards=QuestNormalizer._extract_rewards(data),
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _extract_prerequisites(data: dict) -> list[int]:

        prerequisites = data.get("prerequisites", [])

        result: list[int] = []

        for prerequisite in prerequisites:

            if isinstance(prerequisite, dict):
                result.append(prerequisite["id"])
            else:
                result.append(prerequisite)

        return result

    @staticmethod
    def _extract_steps(data: dict) -> list[int]:

        steps = data.get("steps", [])

        result: list[int] = []

        for step in steps:

            if isinstance(step, dict):
                result.append(step["id"])
            else:
                result.append(step)

        return result

    @staticmethod
    def _extract_rewards(data: dict) -> list[int]:

        rewards = data.get("rewards", [])

        result: list[int] = []

        for reward in rewards:

            if isinstance(reward, dict):
                result.append(reward["id"])
            else:
                result.append(reward)

        return result