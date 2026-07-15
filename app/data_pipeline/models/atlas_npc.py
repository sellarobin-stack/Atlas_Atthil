from __future__ import annotations

from dataclasses import dataclass

from .atlas_map import AtlasMap


@dataclass(slots=True)
class AtlasNpc:
    id: int

    name: str

    map: AtlasMap | None = None

    dialog_id: int | None = None

    breed_id: int | None = None

    look: str | None = None

    notes: str | None = None