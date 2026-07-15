from dataclasses import dataclass


@dataclass(slots=True)
class AtlasMap:
    """
    Représentation interne d'une carte Atlas.
    """

    id: int

    world_map_id: int | None = None

    zone_id: int | None = None

    sub_area_id: int | None = None

    x: int | None = None

    y: int | None = None

    outdoor: bool = True

    has_zaap: bool = False

    has_zaapi: bool = False

    has_workshop: bool = False