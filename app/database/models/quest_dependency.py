from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from .quest import Quest


class QuestDependency(BaseModel):
    __tablename__ = "quest_dependencies"

    __table_args__ = (
        UniqueConstraint(
            "quest_id",
            "required_quest_id",
            name="uq_quest_dependency",
        ),
    )

    quest_id: Mapped[int] = mapped_column(
        ForeignKey("quests.id", ondelete="CASCADE")
    )

    required_quest_id: Mapped[int] = mapped_column(
        ForeignKey("quests.id", ondelete="CASCADE")
    )

    quest: Mapped["Quest"] = relationship(
    "Quest",
    foreign_keys=[quest_id],
    back_populates="dependencies",
)

    required_quest: Mapped["Quest"] = relationship(
    "Quest",
    foreign_keys=[required_quest_id],
)