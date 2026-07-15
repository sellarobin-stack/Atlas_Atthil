from __future__ import annotations

from app.data_pipeline.models import (
    AtlasMap,
    AtlasNpc,
)
from app.data_pipeline.normalizers.map_normalizer import MapNormalizer


class NpcNormalizer:

    @staticmethod
    def normalize(data: dict) -> AtlasNpc:

        game_map: AtlasMap | None = None

        if isinstance(data.get("map"), dict):
            game_map = MapNormalizer.normalize(data["map"])

        return AtlasNpc(
            id=data["id"],
            name=data.get("name", ""),
            map=game_map,
            dialog_id=data.get("dialog_id"),
            breed_id=data.get("breed_id"),
            look=data.get("look"),
            notes=data.get("notes"),
        )