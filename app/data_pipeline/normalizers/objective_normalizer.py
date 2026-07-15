from __future__ import annotations

from app.data_pipeline.models import (
    AtlasObjective,
    ObjectiveType,
)
from app.data_pipeline.normalizers.map_normalizer import MapNormalizer
from app.data_pipeline.normalizers.npc_normalizer import NpcNormalizer


class ObjectiveNormalizer:

    @staticmethod
    def normalize(data: dict) -> AtlasObjective:

        objective_type = ObjectiveType.UNKNOWN

        raw_type = str(data.get("type", "")).lower()

        try:
            objective_type = ObjectiveType(raw_type)
        except ValueError:
            pass

        npc = None
        if isinstance(data.get("npc"), dict):
            npc = NpcNormalizer.normalize(data["npc"])

        game_map = None
        if isinstance(data.get("map"), dict):
            game_map = MapNormalizer.normalize(data["map"])

        return AtlasObjective(
            id=data["id"],
            type=objective_type,
            description=data.get("description", ""),
            npc=npc,
            map=game_map,
            item_id=data.get("item_id"),
            item_name=data.get("item_name"),
            monster_id=data.get("monster_id"),
            monster_name=data.get("monster_name"),
            quantity=data.get("quantity", 1),
            dialog_id=data.get("dialog_id"),
            optional=data.get("optional", False),
        )