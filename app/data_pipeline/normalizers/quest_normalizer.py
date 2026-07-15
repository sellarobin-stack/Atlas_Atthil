from __future__ import annotations

from app.data_pipeline.models import (
    AtlasMap,
    AtlasNpc,
    AtlasPrerequisite,
    AtlasQuest,
)
from app.data_pipeline.normalizers.map_normalizer import MapNormalizer
from app.data_pipeline.normalizers.npc_normalizer import NpcNormalizer
from app.data_pipeline.normalizers.prerequisite_normalizer import (
    PrerequisiteNormalizer,
)
from app.data_pipeline.normalizers.reward_normalizer import RewardNormalizer
from app.data_pipeline.normalizers.step_normalizer import StepNormalizer


class QuestNormalizer:

    @staticmethod
    def normalize(data: dict) -> AtlasQuest:

        quest = AtlasQuest(
            id=data["id"],
            name=data.get("name", ""),
            level=data.get("level"),
            category=data.get("category"),
            campaign=data.get("campaign"),
            repeatable=data.get("repeatable", False),
        )

        for npc in QuestNormalizer._extract_start_npcs(data):
            quest.add_start_npc(npc)

        for game_map in QuestNormalizer._extract_start_maps(data):
            quest.add_start_map(game_map)

        for prerequisite in data.get("prerequisites", []):
            quest.add_prerequisite(
                PrerequisiteNormalizer.normalize(prerequisite)
            )

        for step in data.get("steps", []):
            quest.add_step(
                StepNormalizer.normalize(step)
            )

        for reward in data.get("rewards", []):
            quest.add_reward(
                RewardNormalizer.normalize(reward)
            )

        return quest

    @staticmethod
    def _extract_start_npcs(data: dict) -> list[AtlasNpc]:

        npcs = []

        for npc in data.get("start_npcs", []):

            if isinstance(npc, dict):
                npcs.append(NpcNormalizer.normalize(npc))

        return npcs

    @staticmethod
    def _extract_start_maps(data: dict) -> list[AtlasMap]:

        maps = []

        for game_map in data.get("start_maps", []):

            if isinstance(game_map, dict):
                maps.append(MapNormalizer.normalize(game_map))

        return maps