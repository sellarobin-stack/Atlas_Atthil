from __future__ import annotations

from app.data_pipeline.models import (
    AtlasPrerequisite,
    PrerequisiteType,
)


class PrerequisiteNormalizer:

    @staticmethod
    def normalize(data: dict) -> AtlasPrerequisite:

        prerequisite_type = PrerequisiteType.UNKNOWN

        raw_type = str(data.get("type", "")).lower()

        try:
            prerequisite_type = PrerequisiteType(raw_type)
        except ValueError:
            pass

        return AtlasPrerequisite(
            type=prerequisite_type,
            value=data.get("value"),
            operator=data.get("operator", "=="),
        )