from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class PrerequisiteType(str, Enum):
    QUEST_COMPLETED = "quest_completed"
    QUEST_ACTIVE = "quest_active"
    ACHIEVEMENT = "achievement"
    LEVEL = "level"
    ALIGNMENT = "alignment"
    ITEM = "item"
    JOB_LEVEL = "job_level"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class AtlasPrerequisite:
    type: PrerequisiteType
    value: int | str
    operator: str = "=="