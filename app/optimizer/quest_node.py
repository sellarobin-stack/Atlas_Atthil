from dataclasses import dataclass, field


@dataclass(slots=True)
class QuestNode:

    quest_id: int

    name: str

    level: int

    parents: set[int] = field(default_factory=set)

    children: set[int] = field(default_factory=set)