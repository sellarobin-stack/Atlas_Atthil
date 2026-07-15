from dataclasses import dataclass, field


@dataclass(slots=True)
class AtlasQuest:
    """
    Représentation interne d'une quête Atlas.

    Cette classe est indépendante de toute source externe
    (DofusDB, DPLN, Ankama...).
    """

    id: int
    name: str
    level: int

    campaign: str | None = None

    zone_id: int | None = None
    map_id: int | None = None

    repeatable: bool = False

    prerequisites: list[int] = field(default_factory=list)

    steps: list[int] = field(default_factory=list)

    rewards: list[int] = field(default_factory=list)