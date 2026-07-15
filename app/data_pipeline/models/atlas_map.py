from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AtlasMap:
    id: int

    x: int | None = None
    y: int | None = None

    world_id: int | None = None
    world_name: str | None = None

    area_id: int | None = None
    area_name: str | None = None

    sub_area_id: int | None = None
    sub_area_name: str | None = None

    outdoor: bool | None = None

    has_zaap: bool = False
    has_zaapi: bool = False
    has_bank: bool = False
    has_phoenix: bool = False

    def coordinates(self) -> tuple[int | None, int | None]:
        return self.x, self.y