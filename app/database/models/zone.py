from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from .game_map import GameMap


class Zone(BaseModel):
    __tablename__ = "zones"

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    maps: Mapped[list["GameMap"]] = relationship(
        back_populates="zone",
        cascade="all, delete-orphan",
    )