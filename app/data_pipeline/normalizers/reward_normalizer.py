from __future__ import annotations

from app.data_pipeline.models import (
    AtlasReward,
    RewardType,
)


class RewardNormalizer:

    @staticmethod
    def normalize(data: dict) -> AtlasReward:

        reward_type = RewardType.UNKNOWN

        raw_type = str(data.get("type", "")).lower()

        try:
            reward_type = RewardType(raw_type)
        except ValueError:
            pass

        return AtlasReward(
            type=reward_type,
            value=data.get("value"),
            quantity=data.get("quantity", 1),
            item_id=data.get("item_id"),
            item_name=data.get("item_name"),
            description=data.get("description"),
        )