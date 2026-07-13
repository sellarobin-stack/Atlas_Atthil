from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from .game_map import GameMap


class Npc(BaseModel):
    __tablename__ = "npcs"

    ankama_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(150)
    )

    map_id: Mapped[int] = mapped_column(
        ForeignKey("maps.id")
    )

    map: Mapped["GameMap"] = relationship(
        back_populates="npcs"
    )