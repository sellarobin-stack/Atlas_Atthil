from dataclasses import dataclass


@dataclass(slots=True)
class AtlasNpc:
    """
    Représentation interne d'un PNJ Atlas.
    """

    id: int

    name: str

    map_id: int | None = None

    zone_id: int | None = None

    x: int | None = None

    y: int | None = None

    dialog_id: int | None = None