from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .atlas_map import AtlasMap
from .atlas_npc import AtlasNpc


class ObjectiveType(str, Enum):
    TALK_TO_NPC = "talk_to_npc"
    GO_TO_MAP = "go_to_map"
    KILL_MONSTER = "kill_monster"
    COLLECT_ITEM = "collect_item"
    USE_ITEM = "use_item"
    INTERACT = "interact"
    ENTER_DUNGEON = "enter_dungeon"
    EMOTE = "emote"
    CRAFT = "craft"
    WAIT = "wait"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class AtlasObjective:
    id: int

    type: ObjectiveType

    description: str

    npc: AtlasNpc | None = None

    map: AtlasMap | None = None

    item_id: int | None = None
    item_name: str | None = None

    monster_id: int | None = None
    monster_name: str | None = None

    quantity: int = 1

    dialog_id: int | None = None

    completed: bool = False

    optional: bool = False