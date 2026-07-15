from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RewardType(str, Enum):
    EXPERIENCE = "experience"
    KAMAS = "kamas"
    ITEM = "item"
    TITLE = "title"
    ORNAMENT = "ornament"
    EMOTE = "emote"
    SPELL = "spell"
    ACHIEVEMENT = "achievement"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class AtlasReward:
    type: RewardType
    value: int | str | None = None

    quantity: int = 1

    item_id: int | None = None
    item_name: str | None = None

    description: str | None = None