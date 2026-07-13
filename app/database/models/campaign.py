from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from .quest import Quest

class Campaign(BaseModel):
    __tablename__ = "campaigns"

    code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )
    quests: Mapped[list["Quest"]] = relationship(
    back_populates="campaign",
    cascade="all, delete-orphan",
)