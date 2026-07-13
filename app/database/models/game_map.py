from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from .zone import Zone
    from .npc import Npc


class GameMap(BaseModel):
    __tablename__ = "maps"

    x: Mapped[int] = mapped_column(Integer)
    y: Mapped[int] = mapped_column(Integer)

    zone_id: Mapped[int] = mapped_column(
        ForeignKey("zones.id"),
        index=True,
    )

    zone: Mapped["Zone"] = relationship(
        back_populates="maps"
    )

    npcs: Mapped[list["Npc"]] = relationship(
        back_populates="map",
        cascade="all, delete-orphan",
    )