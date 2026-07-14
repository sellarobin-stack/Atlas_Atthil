from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from .campaign import Campaign
    from .npc import Npc
    from .quest_dependency import QuestDependency


class Quest(BaseModel):
    __tablename__ = "quests"

    ankama_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        index=True,
    )

    level: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    official: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    repeatable: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    campaign_id: Mapped[int | None] = mapped_column(
        ForeignKey("campaigns.id"),
        nullable=True,
    )

    start_npc_id: Mapped[int | None] = mapped_column(
        ForeignKey("npcs.id"),
        nullable=True,
    )

    end_npc_id: Mapped[int | None] = mapped_column(
        ForeignKey("npcs.id"),
        nullable=True,
    )

    campaign: Mapped["Campaign"] = relationship(
        back_populates="quests"
    )

    start_npc: Mapped["Npc"] = relationship(
        foreign_keys=[start_npc_id]
    )

    end_npc: Mapped["Npc"] = relationship(
        foreign_keys=[end_npc_id]
    )
    dependencies: Mapped[list["QuestDependency"]] = relationship(
    back_populates="quest",
        foreign_keys="QuestDependency.quest_id",
        cascade="all, delete-orphan",
    )
    required_by: Mapped[list["QuestDependency"]] = relationship(
        back_populates="required_quest",
        foreign_keys="QuestDependency.required_quest_id",
    )