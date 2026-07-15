from __future__ import annotations

from app.data_pipeline.models import AtlasMap


class MapNormalizer:

    @staticmethod
    def normalize(data: dict) -> AtlasMap:

        return AtlasMap(
            id=data["id"],
            x=data.get("x"),
            y=data.get("y"),
            world_id=data.get("world_id"),
            world_name=data.get("world_name"),
            area_id=data.get("area_id"),
            area_name=data.get("area_name"),
            sub_area_id=data.get("sub_area_id"),
            sub_area_name=data.get("sub_area_name"),
            outdoor=data.get("outdoor"),
            has_zaap=data.get("has_zaap", False),
            has_zaapi=data.get("has_zaapi", False),
            has_bank=data.get("has_bank", False),
            has_phoenix=data.get("has_phoenix", False),
        )